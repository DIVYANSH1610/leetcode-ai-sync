"""
enrich.py
---------
Takes newly-synced solution folders and uses Gemini to:
  1. Generate a clean explanation of the approach
  2. Compute/verify time & space complexity
  3. Suggest a more optimal approach if one exists
  4. Tag the underlying pattern (sliding window, DP, two pointers, etc.)

This overwrites README.md in each folder with the enriched version.
Run this AFTER sync_leetcode.py, passing the folder paths it printed.

Required env var: GEMINI_API_KEY
"""

import os
import sys
from pathlib import Path
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)

MODEL_NAME = "gemini-2.5-flash-lite"  # higher free-tier daily quota than gemini-2.5-flash

PROMPT_TEMPLATE = """You are a senior software engineer reviewing a LeetCode solution.

Problem title: {title}
Difficulty: {difficulty}
Existing tags: {tags}

Solution code ({lang}):
```
{code}
```

Respond in clean Markdown with EXACTLY these sections:

## Approach
(2-4 sentences explaining the core idea in plain English)

## Complexity
- Time: O(...)
- Space: O(...)

## Pattern
(One or two words identifying the algorithmic pattern, e.g. "Sliding Window", "Two Pointers", "DP - 1D")

## Could it be improved?
(If the approach is already optimal, say so briefly. If a better complexity solution
exists, describe it in 2-3 sentences without writing full code.)

Do not repeat the code. Do not add any other sections.
"""


def enrich_folder(folder: Path):
    readme_path = folder / "README.md"
    if not readme_path.exists():
        print(f"Skipping {folder}, no README.md found.")
        return

    # Find the solution file (solution.<ext>)
    sol_files = list(folder.glob("solution.*"))
    if not sol_files:
        print(f"Skipping {folder}, no solution file found.")
        return
    code = sol_files[0].read_text()
    lang = sol_files[0].suffix.lstrip(".")

    original_readme = readme_path.read_text()
    # crude parse of title/difficulty/tags from the auto-generated README header
    lines = original_readme.splitlines()
    title = lines[0].lstrip("# ").strip() if lines else folder.name
    difficulty = next((l.split(":")[1].strip() for l in lines if l.startswith("**Difficulty:**")), "Unknown")
    tags = next((l.split(":")[1].strip() for l in lines if l.startswith("**Tags:**")), "N/A")

    model = genai.GenerativeModel(MODEL_NAME)
    prompt = PROMPT_TEMPLATE.format(
        title=title, difficulty=difficulty, tags=tags, lang=lang, code=code
    )
    try:
        response = model.generate_content(prompt)
        enriched_section = response.text.strip()
    except Exception as e:
        print(f"  -> Gemini call failed for {folder}: {e}")
        return

    # Append enrichment, keep original header info
    final_content = original_readme.split("## My Solution")[0] + f"## My Solution\n\nSee `solution.{lang}`\n\n" + enriched_section + "\n"
    readme_path.write_text(final_content)
    print(f"Enriched: {readme_path}")


def main(folders: list[str]):
    if not GEMINI_API_KEY:
        raise EnvironmentError("Missing GEMINI_API_KEY env var.")
    for f in folders:
        enrich_folder(Path(f))


if __name__ == "__main__":
    # Accepts folder paths as CLI args, e.g.:
    # python enrich.py leetcode-questions/Array/1-two-sum
    if len(sys.argv) < 2:
        print("Usage: python enrich.py <folder1> <folder2> ...")
        sys.exit(1)
    main(sys.argv[1:]) 