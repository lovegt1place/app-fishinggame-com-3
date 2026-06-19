from dataclasses import dataclass
from typing import List
from datetime import datetime


@dataclass
class SiteEntry:
    """Represents a site entry with structured metadata."""
    title: str
    url: str
    keywords: List[str]
    tags: List[str]
    description: str


SITE_DATA = [
    SiteEntry(
        title="Fishing Game Online",
        url="https://app-fishinggame.com",
        keywords=["捕鱼游戏", "fish game", "online fishing"],
        tags=["arcade", "multiplayer", "casual"],
        description="A vibrant online fishing game with real-time multiplayer action and stunning underwater graphics."
    ),
    SiteEntry(
        title="深海捕鱼王",
        url="https://deep-sea-fishing.example.com",
        keywords=["深海捕鱼", "捕鱼游戏", "big fish"],
        tags=["action", "deep sea", "arcade"],
        description="Dive into the deep ocean and catch legendary fish with powerful weapons and special abilities."
    ),
    SiteEntry(
        title="捕鱼达人经典版",
        url="https://fishing-master.example.com",
        keywords=["捕鱼达人", "经典捕鱼", "捕鱼游戏"],
        tags=["classic", "single-player", "scores"],
        description="The classic fishing arcade experience reimagined with modern graphics and leaderboards."
    ),
    SiteEntry(
        title="Golden Reef Fishing",
        url="https://golden-reef.example.com",
        keywords=["golden reef", "underwater", "捕鱼游戏"],
        tags=["adventure", "underwater", "gold"],
        description="Explore the golden coral reef and hunt for treasure while fishing exotic species."
    ),
]


def format_summary(entry: SiteEntry) -> str:
    """Format a single SiteEntry into a readable summary block."""
    kw = ", ".join(entry.keywords)
    tg = ", ".join(entry.tags)
    lines = [
        f"--- Site Summary ---",
        f"Title: {entry.title}",
        f"URL: {entry.url}",
        f"Keywords: {kw}",
        f"Tags: {tg}",
        f"Description: {entry.description}",
        "--------------------",
    ]
    return "\n".join(lines)


def generate_report(entries: List[SiteEntry], site_name: str = "Fishing Game Portal") -> str:
    """Generate a full structured report from a list of SiteEntry objects."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    header = f"Site Summary Report: {site_name}\nGenerated: {timestamp}\n{'='*50}\n"
    body_parts = [format_summary(e) for e in entries]
    body = "\n".join(body_parts)
    summary_line = f"\nTotal sites summarized: {len(entries)}"
    return header + body + summary_line


def main():
    """Main entry point: print the structured site summary."""
    report = generate_report(SITE_DATA, "Fishing Game Collection")
    print(report)


if __name__ == "__main__":
    main()