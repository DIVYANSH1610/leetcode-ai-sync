"""
ingest.py
---------
Walks the leetcode-questions/ folder, reads each enriched README.md + solution
file, and embeds it into a local ChromaDB collection so you can later query
your own solved problems semantically (see query.py).

Run this after enrich.py, or just re-run it on the whole repo periodically
(it's idempotent — re-ingesting a folder overwrites its existing entry).
"""

import os
from pathlib import Path
import chromadb
from chromadb.config import Settings
from chromadb.utils import embedding_functions
from dotenv import load_dotenv

load_dotenv()

REPO_ROOT = Path(__file__).parent.parent / "leetcode-questions"
CHROMA_PATH = Path(__file__).parent.parent / "data" / "chroma_store"

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")

client = chromadb.PersistentClient(
    path=str(CHROMA_PATH), settings=Settings(anonymized_telemetry=False)
)

# Use Gemini embeddings if key is present, otherwise fall back to a local
# sentence-transformers model (no API key needed, slightly lower quality).
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


def build_document_text(folder: Path) -> str | None:
    readme = folder / "README.md"
    if not readme.exists():
        return None
    sol_files = list(folder.glob("solution.*"))
    code = sol_files[0].read_text() if sol_files else ""
    return f"{readme.read_text()}\n\n---\nCode:\n{code}"


def ingest_all():
    count = 0
    for tag_folder in REPO_ROOT.iterdir():
        if not tag_folder.is_dir():
            continue
        for problem_folder in tag_folder.iterdir():
            if not problem_folder.is_dir():
                continue
            doc_text = build_document_text(problem_folder)
            if not doc_text:
                continue

            doc_id = str(problem_folder.relative_to(REPO_ROOT))
            collection.upsert(
                ids=[doc_id],
                documents=[doc_text],
                metadatas=[{
                    "tag": tag_folder.name,
                    "path": doc_id,
                }],
            )
            count += 1
    print(f"Ingested/updated {count} problems into ChromaDB at {CHROMA_PATH}")


if __name__ == "__main__":
    ingest_all()