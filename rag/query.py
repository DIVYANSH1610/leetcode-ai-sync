"""
query.py
--------
Simple CLI chat over your embedded LeetCode solutions.

Usage:
    python rag/query.py
    > Have I solved anything like "container with most water"?
    > Show me all my sliding window problems
"""

import os
from pathlib import Path
import chromadb
from chromadb.config import Settings
from chromadb.utils import embedding_functions
import google.generativeai as genai
from rich.console import Console
from rich.markdown import Markdown
from dotenv import load_dotenv

load_dotenv()

console = Console()

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
CHROMA_PATH = Path(__file__).parent.parent / "data" / "chroma_store"

genai.configure(api_key=GEMINI_API_KEY)
client = chromadb.PersistentClient(
    path=str(CHROMA_PATH), settings=Settings(anonymized_telemetry=False)
)

if GEMINI_API_KEY:
    embedding_fn = embedding_functions.GoogleGenerativeAiEmbeddingFunction(
        api_key=GEMINI_API_KEY, model_name="models/gemini-embedding-001"
    )
else:
    embedding_fn = embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name="all-MiniLM-L6-v2"
    )

collection = client.get_or_create_collection(
    name="leetcode_solutions", embedding_function=embedding_fn
)

ANSWER_PROMPT = """You are an assistant that helps a software engineering student
recall their own past LeetCode solutions. Based ONLY on the context below
(retrieved from their personal solved-problems archive), answer their question.
If nothing relevant is found, say so honestly.

Context:
{context}

Question: {question}

Answer concisely, referencing problem names/paths where relevant.
"""


def retrieve(question: str, k: int = 5):
    results = collection.query(query_texts=[question], n_results=k)
    docs = results.get("documents", [[]])[0]
    metas = results.get("metadatas", [[]])[0]
    return list(zip(docs, metas))


def answer(question: str) -> str:
    matches = retrieve(question)
    if not matches:
        return "No solved problems found in your archive yet — run ingest.py first."

    context = "\n\n---\n\n".join(
        f"[{meta['path']}]\n{doc[:1500]}" for doc, meta in matches
    )
    model = genai.GenerativeModel("gemini-2.5-flash-lite")
    prompt = ANSWER_PROMPT.format(context=context, question=question)
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"Gemini request failed (likely rate limit) — try again in a moment.\nDetails: {e}"


def main():
    console.print("[bold cyan]LeetCode RAG Assistant[/bold cyan] — ask about your solved problems. Ctrl+C to quit.\n")
    while True:
        try:
            question = console.input("[bold green]> [/bold green]")
        except (KeyboardInterrupt, EOFError):
            break
        if not question.strip():
            continue
        result = answer(question)
        console.print(Markdown(result))
        console.print()


if __name__ == "__main__":
    main()