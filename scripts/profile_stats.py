"""
profile_stats.py
----------------
Fetches your overall LeetCode profile via GraphQL (total solved by difficulty,
acceptance rate, ranking, badges) and renders it both as a CLI summary and as
a saved PNG dashboard chart.

This is DIFFERENT from stats.py:
    - stats.py    -> analyzes problems already synced into THIS repo
    - profile_stats.py -> pulls your real, full LeetCode account totals
      (including problems solved outside this pipeline, e.g. before you
      started this project)

Usage:
    python scripts/profile_stats.py
"""

import os
import requests
import matplotlib.pyplot as plt
from pathlib import Path
from dotenv import load_dotenv
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

load_dotenv()
console = Console()

LEETCODE_USERNAME = os.environ.get("LEETCODE_USERNAME")
LEETCODE_SESSION = os.environ.get("LEETCODE_SESSION")
LEETCODE_CSRF = os.environ.get("LEETCODE_CSRF")

GRAPHQL_URL = "https://leetcode.com/graphql"
HEADERS = {
    "Content-Type": "application/json",
    "Referer": "https://leetcode.com",
    "Cookie": f"LEETCODE_SESSION={LEETCODE_SESSION}; csrftoken={LEETCODE_CSRF};",
    "x-csrftoken": LEETCODE_CSRF or "",
}

OUTPUT_CHART = Path(__file__).parent.parent / "data" / "profile_dashboard.png"

PROFILE_QUERY = """
query userProfile($username: String!) {
  matchedUser(username: $username) {
    username
    profile {
      ranking
      reputation
      starRating
    }
    submitStats: submitStatsGlobal {
      acSubmissionNum {
        difficulty
        count
        submissions
      }
      totalSubmissionNum {
        difficulty
        count
        submissions
      }
    }
    badges {
      id
      displayName
    }
  }
  allQuestionsCount {
    difficulty
    count
  }
}
"""


def fetch_profile() -> dict:
    payload = {
        "query": PROFILE_QUERY,
        "variables": {"username": LEETCODE_USERNAME},
    }
    resp = requests.post(GRAPHQL_URL, json=payload, headers=HEADERS, timeout=15)
    resp.raise_for_status()
    data = resp.json()
    if "errors" in data:
        raise RuntimeError(f"GraphQL error: {data['errors']}")
    return data["data"]


def to_dict_by_difficulty(entries: list[dict]) -> dict:
    return {e["difficulty"]: e for e in entries}


def print_summary(data: dict):
    user = data["matchedUser"]
    profile = user["profile"]
    ac_by_diff = to_dict_by_difficulty(user["submitStats"]["acSubmissionNum"])
    total_by_diff = to_dict_by_difficulty(user["submitStats"]["totalSubmissionNum"])
    all_questions = to_dict_by_difficulty(data["allQuestionsCount"])

    solved_total = ac_by_diff.get("All", {}).get("count", 0)
    submissions_total = total_by_diff.get("All", {}).get("submissions", 0)
    accepted_submissions = ac_by_diff.get("All", {}).get("submissions", 0)
    acceptance_rate = (
        (accepted_submissions / submissions_total * 100) if submissions_total else 0
    )

    console.print(Panel.fit(
        f"[bold cyan]{user['username']}[/bold cyan]\n"
        f"Global Ranking: [bold]{profile['ranking']}[/bold]\n"
        f"Reputation: {profile['reputation']}  |  Star Rating: {profile['starRating']}",
        title="LeetCode Profile",
    ))

    table = Table(title="Problems Solved by Difficulty")
    table.add_column("Difficulty")
    table.add_column("Solved", justify="right")
    table.add_column("Total Available", justify="right")
    table.add_column("% of Difficulty Solved", justify="right")

    for diff in ["Easy", "Medium", "Hard"]:
        solved = ac_by_diff.get(diff, {}).get("count", 0)
        total = all_questions.get(diff, {}).get("count", 0)
        pct = (solved / total * 100) if total else 0
        table.add_row(diff, str(solved), str(total), f"{pct:.1f}%")

    console.print(table)
    console.print(f"\n[bold]Total solved:[/bold] {solved_total}")
    console.print(f"[bold]Acceptance rate:[/bold] {acceptance_rate:.1f}%")

    badges = user.get("badges", [])
    if badges:
        console.print(f"\n[bold]Badges ({len(badges)}):[/bold]")
        for b in badges:
            console.print(f"  • {b['displayName']}")
    else:
        console.print("\n[bold]Badges:[/bold] none yet")

    return {
        "username": user["username"],
        "ranking": profile["ranking"],
        "solved_total": solved_total,
        "acceptance_rate": acceptance_rate,
        "ac_by_diff": ac_by_diff,
        "all_questions": all_questions,
        "badges": badges,
    }


def render_dashboard(summary: dict):
    """Renders a 3-panel PNG dashboard: solved-vs-total bars, donut, badges."""
    diffs = ["Easy", "Medium", "Hard"]
    solved = [summary["ac_by_diff"].get(d, {}).get("count", 0) for d in diffs]
    totals = [summary["all_questions"].get(d, {}).get("count", 0) for d in diffs]
    colors = ["#00b8a3", "#ffc01e", "#ff375f"]

    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    fig.suptitle(
        f"LeetCode Dashboard — {summary['username']}  "
        f"(Rank #{summary['ranking']:,})",
        fontsize=14, fontweight="bold",
    )

    # Panel 1: solved vs total per difficulty
    ax = axes[0]
    x = range(len(diffs))
    ax.bar(x, totals, color="#e0e0e0", label="Total available")
    ax.bar(x, solved, color=colors, label="Solved")
    ax.set_xticks(list(x))
    ax.set_xticklabels(diffs)
    ax.set_title("Solved vs Available")
    ax.legend(fontsize=8)
    for i, (s, t) in enumerate(zip(solved, totals)):
        ax.text(i, t + max(totals) * 0.02, f"{s}/{t}", ha="center", fontsize=9)

    # Panel 2: donut chart of solved distribution by difficulty
    ax = axes[1]
    if sum(solved) > 0:
        ax.pie(
            solved, labels=diffs, autopct="%1.0f%%", colors=colors,
            wedgeprops=dict(width=0.4), startangle=90,
        )
    ax.set_title(f"Solved Distribution\n(Total: {summary['solved_total']})")

    # Panel 3: acceptance rate gauge (simple bar)
    ax = axes[2]
    rate = summary["acceptance_rate"]
    ax.barh(["Acceptance Rate"], [100], color="#e0e0e0")
    ax.barh(["Acceptance Rate"], [rate], color="#00b8a3")
    ax.set_xlim(0, 100)
    ax.text(rate + 2, 0, f"{rate:.1f}%", va="center", fontsize=11, fontweight="bold")
    ax.set_title("Acceptance Rate")
    ax.set_xlabel("%")

    plt.tight_layout()
    OUTPUT_CHART.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(OUTPUT_CHART, dpi=150)
    console.print(f"\n[bold green]Dashboard image saved to:[/bold green] {OUTPUT_CHART}")


def main():
    if not (LEETCODE_USERNAME and LEETCODE_SESSION and LEETCODE_CSRF):
        raise EnvironmentError("Missing LEETCODE_USERNAME / LEETCODE_SESSION / LEETCODE_CSRF in .env")

    data = fetch_profile()
    summary = print_summary(data)
    render_dashboard(summary)


if __name__ == "__main__":
    main()