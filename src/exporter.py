"""
exporter.py
-----------

Export PacketInfo objects to CSV and JSON files.
"""

from __future__ import annotations

import csv
import json
from dataclasses import asdict
from pathlib import Path

from config import (
    CSV_FILE,
    EXPORT_CSV,
    EXPORT_JSON,
    JSON_FILE,
)

from models import PacketInfo


def _ensure_parent_directory(file_path: str) -> None:
    """
    Create the parent directory if it does not exist.
    """

    Path(file_path).parent.mkdir(
        parents=True,
        exist_ok=True,
    )


def export_to_csv(packet: PacketInfo) -> None:
    """
    Append one packet to the CSV file.
    """

    if not EXPORT_CSV:
        return

    _ensure_parent_directory(CSV_FILE)

    file_exists = Path(CSV_FILE).exists()

    with open(
        CSV_FILE,
        mode="a",
        newline="",
        encoding="utf-8",
    ) as csv_file:

        writer = csv.DictWriter(
            csv_file,
            fieldnames=asdict(packet).keys(),
        )

        if not file_exists:
            writer.writeheader()

        writer.writerow(asdict(packet))


def export_to_json(packet: PacketInfo) -> None:
    """
    Append one packet as a JSON object.

    Each line contains one JSON object (JSON Lines format).
    """

    if not EXPORT_JSON:
        return

    _ensure_parent_directory(JSON_FILE)

    with open(
        JSON_FILE,
        mode="a",
        encoding="utf-8",
    ) as json_file:

        json.dump(
            asdict(packet),
            json_file,
            ensure_ascii=False,
        )

        json_file.write("\n")


def export_packet(packet: PacketInfo) -> None:
    """
    Export one packet to every enabled format.
    """

    export_to_csv(packet)
    export_to_json(packet)
