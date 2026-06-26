"""
sync_leetcode.py
-----------------
Fetches your recent ACCEPTED LeetCode submissions via the internal GraphQL API,
and writes any new ones into a structured local folder (which a GitHub Action
will later commit + push).

Required environment variables (set as GitHub Secrets in production,
or in a local .env file for testing):
    LEETCODE_SESSION   -> value of the 'LEETCODE_SESSION' cookie from your browser
    LEETCODE_CSRF      -> value of the 'csrftoken' cookie from your browser
    LEETCODE_USERNAME  -> your LeetCode username

How to get the cookies:
    1. Log into leetcode.com in your browser
    2. Open DevTools -> Application/Storage -> Cookies -> leetcode.com
    3. Copy the values of 'LEETCODE_SESSION' and 'csrftoken'
    Note: these expire periodically — you'll need to refresh them every so often.
"""

import os
import json
import time
import requests
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

LEETCODE_SESSION = os.environ.get("LEETCODE_SESSION")
LEETCODE_CSRF = os.environ.get("LEETCODE_CSRF")
LEETCODE_USERNAME = os.environ.get("LEETCODE_USERNAME")

GRAPHQL_URL = "https://leetcode.com/graphql"
REPO_ROOT = Path(__file__).parent.parent / "leetcode-questions"
STATE_FILE = Path(__file__).parent.parent / "data" / "synced_submissions.json"

HEADERS = {
    "Content-Type": "application/json",
    "Referer": "https://leetcode.com",
    "Cookie": f"LEETCODE_SESSION={LEETCODE_SESSION}; csrftoken={LEETCODE_CSRF};",
    "x-csrftoken": LEETCODE_CSRF or "",
}

LANG_EXTENSION_MAP = {
    "python3": "py", "python": "py", "java": "java", "cpp": "cpp",
    "c": "c", "csharp": "cs", "javascript": "js", "typescript": "ts",
    "golang": "go", "kotlin": "kt", "swift": "swift", "rust": "rs",
    "ruby": "rb", "scala": "scala", "php": "php",
}


def load_synced_state() -> dict:
    if STATE_FILE.exists():
        return json.loads(STATE_FILE.read_text())
    return {}


def save_synced_state(state: dict) -> None:
    STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
    STATE_FILE.write_text(json.dumps(state, indent=2))


def fetch_recent_accepted_submissions(limit: int = 20) -> list[dict]:
    """Fetches your most recent accepted submissions (lightweight list, no code)."""
    query = """
    query recentAcSubmissions($username: String!, $limit: Int!) {
        recentAcSubmissionList(username: $username, limit: $limit) {
            id
            title
            titleSlug
            timestamp
            lang
        }
    }
    """
    payload = {
        "query": query,
        "variables": {"username": LEETCODE_USERNAME, "limit": limit},
    }
    resp = requests.post(GRAPHQL_URL, json=payload, headers=HEADERS, timeout=15)
    resp.raise_for_status()
    data = resp.json()
    return data.get("data", {}).get("recentAcSubmissionList", []) or []


def fetch_submission_code(submission_id: str) -> str | None:
    """Fetches the actual submitted code for a given submission id."""
    query = """
    query submissionDetails($submissionId: Int!) {
        submissionDetails(submissionId: $submissionId) {
            code
            lang { name }
        }
    }
    """
    payload = {"query": query, "variables": {"submissionId": int(submission_id)}}
    resp = requests.post(GRAPHQL_URL, json=payload, headers=HEADERS, timeout=15)
    resp.raise_for_status()
    data = resp.json()
    details = data.get("data", {}).get("submissionDetails")
    return details.get("code") if details else None


def fetch_problem_metadata(title_slug: str) -> dict:
    """Fetches difficulty, tags, and the problem statement for a problem."""
    query = """
    query questionData($titleSlug: String!) {
        question(titleSlug: $titleSlug) {
            questionFrontendId
            title
            difficulty
            content
            topicTags { name }
        }
    }
    """
    payload = {"query": query, "variables": {"titleSlug": title_slug}}
    resp = requests.post(GRAPHQL_URL, json=payload, headers=HEADERS, timeout=15)
    resp.raise_for_status()
    data = resp.json()
    return data.get("data", {}).get("question", {}) or {}


def slugify_folder(frontend_id: str, title_slug: str) -> str:
    return f"{frontend_id}-{title_slug}"


def write_solution_files(meta: dict, code: str, lang: str) -> Path:
    """Writes solution.<ext> and a metadata README.md into the right folder."""
    difficulty = meta.get("difficulty", "Unknown")
    tags = [t["name"] for t in meta.get("topicTags", [])]
    primary_tag = tags[0] if tags else "Misc"
    frontend_id = meta.get("questionFrontendId", "0")
    title = meta.get("title", "untitled")
    title_slug = title.lower().replace(" ", "-")

    folder = REPO_ROOT / primary_tag.replace(" ", "_") / slugify_folder(frontend_id, title_slug)
    folder.mkdir(parents=True, exist_ok=True)

    ext = LANG_EXTENSION_MAP.get(lang.lower(), "txt")
    (folder / f"solution.{ext}").write_text(code)

    readme = f"""# {frontend_id}. {title}

**Difficulty:** {difficulty}
**Tags:** {", ".join(tags) if tags else "N/A"}
**Language:** {lang}

## Problem

See: https://leetcode.com/problems/{title_slug}/

## My Solution

See `solution.{ext}`

> _AI-generated explanation, complexity analysis, and pattern tagging are added
> by `scripts/enrich.py` in a later step of the pipeline._
"""
    (folder / "README.md").write_text(readme)
    return folder


def run_sync():
    if not (LEETCODE_SESSION and LEETCODE_CSRF and LEETCODE_USERNAME):
        raise EnvironmentError(
            "Missing one of LEETCODE_SESSION / LEETCODE_CSRF / LEETCODE_USERNAME env vars."
        )

    state = load_synced_state()
    submissions = fetch_recent_accepted_submissions(limit=20)
    new_folders = []

    for sub in submissions:
        sub_id = sub["id"]
        if sub_id in state:
            continue  # already synced

        print(f"New accepted submission found: {sub['title']} ({sub['lang']})")
        code = fetch_submission_code(sub_id)
        if not code:
            print(f"  -> Could not fetch code for {sub['title']}, skipping.")
            continue

        meta = fetch_problem_metadata(sub["titleSlug"])
        folder = write_solution_files(meta, code, sub["lang"])
        new_folders.append(str(folder))

        state[sub_id] = {
            "title": sub["title"],
            "timestamp": sub["timestamp"],
            "synced_at": int(time.time()),
        }
        save_synced_state(state)  # persist immediately so an interruption doesn't lose progress
        time.sleep(1)  # be polite to LeetCode's servers

    if new_folders:
        print(f"\nSynced {len(new_folders)} new solution(s):")
        for f in new_folders:
            print(f"  - {f}")
    else:
        print("No new accepted submissions since last sync.")

    return new_folders


if __name__ == "__main__":
    run_sync()