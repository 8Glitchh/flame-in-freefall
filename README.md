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

The first start downloads the embedding model for `rag.py`, so it takes a minute. Set `GROQ_API_KEY` before starting it to get written answers in the chat. Without it, `/ask` returns the best matching passage from the paper.

Frontend:

```
cd frontend
npm install
npm run dev
```

Open http://localhost:5173
