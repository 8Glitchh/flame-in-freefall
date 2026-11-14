# flame-in-freefall
AI dashboard that ranks and explains NASA microgravity combustion data /// NASA Space Apps 2026, team Glitxh

## Run it

Backend (Python 3.12):

```
cd backend
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
uvicorn app:app --port 8000
```

The first start downloads the embedding model and embeds all the data for `rag.py`, so it takes a few minutes. After that it loads from `rag/.cache`.

### AI answers (.env)

The chat writes its answers with Gemini. To turn that on:

1. Get a free API key at https://aistudio.google.com (Get API key, then Create API key). No billing needed.
2. In the repo root (next to this README), copy `.env.example` to a new file named `.env`:

```
copy .env.example .env
```

3. Open `.env` and replace `your_gemini_key_here` with your key:

```
LLM_BASE_URL=https://generativelanguage.googleapis.com/v1beta/openai
LLM_API_KEY=your_gemini_key_here
LLM_MODEL=gemini-3.1-flash-lite
```

4. Restart the backend.

`.env` is in `.gitignore`, so your key never gets pushed. Never paste a real key into `.env.example`, the code, or chat.

Any OpenAI-compatible provider works the same way: change the three lines (for example Groq: `LLM_BASE_URL=https://api.groq.com/openai/v1`, `LLM_MODEL=llama-3.3-70b-versatile`).

Without a `.env`, the chat still works: `/ask` returns the best matching passage from the papers instead of a written answer.

To test the RAG on its own from the repo root:

```
python rag\rag.py ask "What fuels were tested in FLEX?"
```

Frontend:

```
cd frontend
npm install
npm run dev
```

Open http://localhost:5173
