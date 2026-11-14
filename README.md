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

The first start downloads the embedding model and embeds all the data for `rag.py`, so it takes a few minutes. After that it loads from `rag/.cache`. Set `GROQ_API_KEY` before starting it to get written answers in the chat. Without it, `/ask` returns the best matching passage from the paper.

Frontend:

```
cd frontend
npm install
npm run dev
```

Open http://localhost:5173
