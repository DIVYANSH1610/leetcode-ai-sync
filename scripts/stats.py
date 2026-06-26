"""
stats.py
--------
Analyzes your solved-problems archive and prints a breakdown by tag/pattern
and difficulty. Also writes stats.json so the README/dashboard can render
it as a chart.

Usage:
    python scripts/stats.py
"""

import json
import re
from collections import Counter
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent / "leetcode-questions"
STATS_FILE = Path(__file__).parent.parent / "data" / "stats.json"


def parse_readme(readme_path: Path) -> dict:
    text = readme_path.read_text(encoding="utf-8")
    difficulty = re.search(r"\*\*Difficulty:\*\*\s*(\w+)", text)
    pattern = re.search(r"## Pattern\s*\n+(.+)", text)
    return {
        "difficulty": difficulty.group(1) if difficulty else "Unknown",
        "pattern": pattern.group(1).strip() if pattern else "Unknown",
    }


def collect_stats():
    difficulty_counter = Counter()
    pattern_counter = Counter()
    tag_counter = Counter()
    total = 0

    for tag_folder in REPO_ROOT.iterdir():
        if not tag_folder.is_dir():
            continue
        for problem_folder in tag_folder.iterdir():
            readme = problem_folder / "README.md"
            if not readme.exists():
                continue
            total += 1
            tag_counter[tag_folder.name] += 1
            info = parse_readme(readme)
            difficulty_counter[info["difficulty"]] += 1
            pattern_counter[info["pattern"]] += 1

    return {
        "total_problems": total,
        "by_difficulty": dict(difficulty_counter),
        "by_pattern": dict(pattern_counter),
        "by_tag": dict(tag_counter),
    }


def print_bar_chart(title: str, counts: dict):
    print(f"\n{title}")
    print("-" * len(title))
    if not counts:
        print("  (no data)")
        return
    max_count = max(counts.values())
    for label, count in sorted(counts.items(), key=lambda x: -x[1]):
        bar = "█" * int((count / max_count) * 30)
        print(f"  {label:<25} {bar} {count}")


def main():
    stats = collect_stats()

    STATS_FILE.parent.mkdir(parents=True, exist_ok=True)
    STATS_FILE.write_text(json.dumps(stats, indent=2))

    print(f"Total problems solved & synced: {stats['total_problems']}")
    print_bar_chart("By Difficulty", stats["by_difficulty"])
    print_bar_chart("By Pattern", stats["by_pattern"])
    print_bar_chart("By LeetCode Tag", stats["by_tag"])
    print(f"\nStats saved to: {STATS_FILE}")


if __name__ == "__main__":
    main()