import sys
import pandas as pd
import re
from pathlib import Path

INPUT_FILE = sys.argv[1] if len(sys.argv) > 1 else ""
OUTPUT_FILE = sys.argv[2] if len(sys.argv) > 2 else ""

MEASUREMENTS = {
    "oxygen": {
        "suffix": "pct",
        "units": {
            "%": 1,
            "vol.%": 1,
            "mol fraction": 100,
            "volume fraction": 100,
            "fraction": 100,
            "Y_O2":1
        }
    },
    "pressure": {
        "suffix": "kpa",
        "units": {
            "kPa": 1,
            "Pa": 0.001,
            "MPa": 1000,
            "bar": 100,
            "mbar": 0.1,
            "atm": 101.325,
            "psi": 6.89476,
            "psid": 6.89476,
            "psia": 6.89476,
            "mmHg": 0.133322,
            "STP": 101.325
        }
    },
    "flow": {
        "suffix": "cm_s",
        "units": {
            "cm/s": 1,
            "cm/sec": 1,
            "m/s": 100,
            "m/sec": 100,
            "mm/s": 0.1,
            "mm/sec": 0.1,
            "mm/sec": 0.1
        }
    },
    "spread_rate": {
        "suffix": "mm_s",
        "units": {
            "mm/s": 1,
            "mm/sec": 1,
            "cm/s": 10,
            "cm/sec": 10,
            "m/s": 1000,
            "m/sec": 1000,
        }
    },
    "peak_heat_release_rate": {
        "suffix": "w",
        "units": {
            "W": 1,
            "kW": 1000,
        }
    },
    "co_max": {
        "suffix": "ppm",
        "units": {
            "ppm": 1,
            "ppb": 0.001,
        }
    },
    "smoke_max": {
        "suffix": "mg_m3",
        "units": {
            "mg/m3": 1,
            "mg/m³": 1,
            "g/m3": 1000,
            "g/m³": 1000,
        }
    },
    "time_to_detection": {
        "suffix": "s",
        "units": {
            "s": 1,
            "sec": 1,
            "min": 60,
            "h": 3600,
        }
    },
}

NUMBER_PATTERN = re.compile(
    r"[-+]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][-+]?\d+)?"
)

RANGE_SEPARATOR = re.compile(
    r"(?:-|–|—|−|\bto\b|\bthrough\b|\band\b)",
    re.IGNORECASE
)

BOUND_PATTERN = re.compile(
    r"^\s*(<=|>=|<|>|≤|≥)\s*"
)


def find_unit(text, units):
    """Identify a reported unit using longest-match-first."""

    for unit, factor in sorted(
        units.items(),
        key=lambda x: len(x[0]),
        reverse=True
    ):
        pattern = (
            r"(?<![a-z])"
            + re.escape(unit.lower())
            + r"(?![a-z])"
        )

        if re.search(pattern, text):
            return factor

    return None


def get_factor(text, units, fallback_text=None):
    """Find the unit factor associated with a numeric value."""

    factor = find_unit(text, units)

    if factor is None and fallback_text is not None:
        factor = find_unit(fallback_text, units)

    return factor


def parse_measurement(value, units):
    """
    Returns:
        min_value, max_value, status

    Supported:
        Single values
        Numeric ranges
        Ranges with 'to' or 'through'
        Inequality bounds
        Units after either or both range endpoints
    """

    if pd.isna(value):
        return None, None, "missing"

    text = str(value).strip().lower()

    if not text:
        return None, None, "missing"

    matches = list(NUMBER_PATTERN.finditer(text))

    if not matches:
        return None, None, "unparsed"
    
    # Handle equivalent values in parentheses.
    if len(matches) == 2:

        between = text[
            matches[0].end():matches[1].start()
        ]

        if re.match(r"\s*\(", between):

            first_factor = find_unit(
                text[matches[0].end():matches[1].start()],
                units
            )

            if first_factor is not None:

                value = float(matches[0].group()) * first_factor

                return value, value, "equivalent"

    # Identify units independently for each endpoint.
    values = []

    for i, match in enumerate(matches):

        number = float(match.group())

        segment_end = (
            matches[i + 1].start()
            if i + 1 < len(matches)
            else len(text)
        )

        segment = text[match.end():segment_end]

        factor = get_factor(
            segment,
            units,
            fallback_text=text
        )

        if factor is None:
            return None, None, "unknown_unit"

        values.append(number * factor)

    # Handle inequality values.
    if len(matches) == 1:

        prefix = text[:matches[0].start()]
        bound = BOUND_PATTERN.match(prefix)

        if bound:
            operator = bound.group(1)

            if operator in (">", ">=", "≥"):
                return values[0], None, "bound"

            if operator in ("<", "<=", "≤"):
                return None, values[0], "bound"

        return values[0], values[0], "single"

    # Handle ranges only when the separator is explicit.
    if len(matches) == 2:

        between = text[
            matches[0].end():matches[1].start()
        ]

        if RANGE_SEPARATOR.search(between):

            minimum = min(values)
            maximum = max(values)

            return minimum, maximum, "range"

    # Avoid guessing when multiple numbers are ambiguous.
    return None, None, "ambiguous"


def main():

    if not Path(INPUT_FILE).exists():
        raise FileNotFoundError(INPUT_FILE)

    df = pd.read_csv(
        INPUT_FILE,
        encoding="utf-8-sig",
        low_memory=False
    )

    result = pd.DataFrame(index=df.index)

    # Track parsing performance.
    statistics = {}

    for column in df.columns:

        if column in MEASUREMENTS:

            config = MEASUREMENTS[column]
            suffix = config["suffix"]
            units = config["units"]

            # Preserve original extracted values.
            result[f"{column}_raw"] = df[column]

            parsed = df[column].apply(
                lambda x: parse_measurement(x, units)
            )

            result[f"{column}_min_{suffix}"] = parsed.apply(
                lambda x: x[0]
            )

            result[f"{column}_max_{suffix}"] = parsed.apply(
                lambda x: x[1]
            )

            statistics[column] = (
                parsed.apply(lambda x: x[2]).value_counts()
            )

        else:
            result[column] = df[column]

    result.to_csv(
        OUTPUT_FILE,
        index=False,
        encoding="utf-8-sig"
    )

    # Print parsing diagnostics.
    print("\n========== PARSING SUMMARY ==========")

    for column, counts in statistics.items():

        total = len(df)

        successful = (
            counts.get("single", 0)
            + counts.get("range", 0)
            + counts.get("bound", 0)
            + counts.get("equivalent", 0)
        )

        print(f"\n{column}")
        print(f"  Total: {total}")
        print(f"  Successfully parsed: {successful}")
        print(f"  Success rate: {successful / total * 100:.2f}%"
              if total else "  Success rate: N/A")

        for status, count in counts.items():
            print(f"  {status}: {count}")

    print(f"\nOutput saved to: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()