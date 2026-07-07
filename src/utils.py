"""
utils.py
---------

Reusable utility functions used throughout the project.
"""

from __future__ import annotations

from datetime import datetime
from pathlib import Path


def format_timestamp(timestamp: float) -> str:
    """
    Convert a Unix timestamp into a human-readable format.

    Example:
        1751726521.42

    becomes

        2026-07-06 18:42:01
    """

    return datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d %H:%M:%S")


def truncate_text(text: str | None, max_length: int) -> str:
    """
    Safely truncate long strings.

    None becomes "-".
    """

    if not text:
        return "-"

    if len(text) <= max_length:
        return text

    return text[:max_length] + "..."


def safe_value(value) -> str:
    """
    Convert None into '-'.

    Makes terminal output much cleaner.
    """

    return "-" if value is None else str(value)


def ensure_directory(path: str) -> None:
    """
    Create a directory if it does not already exist.

    Example

    logs/

    exports/

    screenshots/
    """

    Path(path).mkdir(
        parents=True,
        exist_ok=True,
    )


def print_banner() -> None:
    """
    Print the application banner.
    """

    print("=" * 70)

    print("          NETWORK PACKET SNIFFER")

    print("=" * 70)


def separator(length: int = 70) -> None:
    """
    Print a separator line.
    """

    print("-" * length)
