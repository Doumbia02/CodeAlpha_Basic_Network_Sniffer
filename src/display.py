"""
display.py
-----------

Handles all terminal output.

This module is responsible ONLY for displaying packet
information in a readable format.
"""

from datetime import datetime

from colorama import Fore, Style, init

from config import (
    SHOW_PACKET_LENGTH,
    SHOW_PAYLOAD,
    SHOW_PORTS,
    SHOW_TIMESTAMP,
    SHOW_TTL,
    MAX_PAYLOAD_LENGTH,
)

# Initialize Colorama
init(autoreset=True)

# Used to know when to print the table header again
_packet_counter = 0


def format_timestamp(timestamp: float) -> str:
    """
    Convert Unix timestamp to HH:MM:SS.
    """
    return datetime.fromtimestamp(timestamp).strftime("%H:%M:%S")


def protocol_color(protocol: str) -> str:
    """
    Return the appropriate color for each protocol.
    """

    colors = {
        "TCP": Fore.GREEN,
        "UDP": Fore.CYAN,
        "DNS": Fore.MAGENTA,
        "ICMP": Fore.YELLOW,
        "ARP": Fore.BLUE,
    }

    return colors.get(protocol, Fore.WHITE)


def print_header() -> None:
    """
    Print the table header.
    """

    print("=" * 120)

    print(
        f"{'Time':<10}"
        f"{'Protocol':<12}"
        f"{'Source IP':<20}"
        f"{'Destination IP':<20}"
        f"{'Ports':<18}"
        f"{'Length':<10}"
    )

    print("=" * 120)


def display_packet(packet_info: dict) -> None:
    """
    Display one parsed packet.
    """

    global _packet_counter

    _packet_counter += 1

    if _packet_counter == 1 or _packet_counter % 25 == 0:
        print_header()

    # -----------------------------
    # Timestamp
    # -----------------------------

    timestamp = ""

    if SHOW_TIMESTAMP:
        timestamp = format_timestamp(packet_info.timestamp)

    # -----------------------------
    # Protocol
    # -----------------------------

    protocol = packet_info.protocol

    colored_protocol = (
        protocol_color(protocol)
        + f"{protocol:<12}"
        + Style.RESET_ALL
    )

    # -----------------------------
    # IP Addresses
    # -----------------------------

    source_ip = packet_info.source_ip or "-"

    destination_ip = packet_info.destination_ip or "-"

    # -----------------------------
    # Ports
    # -----------------------------

    ports = "-"

    if SHOW_PORTS:

        src = packet_info.source_port

        dst = packet_info.destination_port

        if src is not None and dst is not None:
            ports = f"{src} → {dst}"

    # -----------------------------
    # Length
    # -----------------------------

    length = ""

    if SHOW_PACKET_LENGTH:
        length = str(packet_info.length)

    # -----------------------------
    # Main Row
    # -----------------------------

    print(
        f"{timestamp:<10}"
        f"{colored_protocol}"
        f"{source_ip:<20}"
        f"{destination_ip:<20}"
        f"{ports:<18}"
        f"{length:<10}"
    )

    # -----------------------------
    # Payload
    # -----------------------------

    if SHOW_PAYLOAD:

        payload = packet_info.payload

        if payload:

            payload = payload.replace("\n", " ")

            if len(payload) > MAX_PAYLOAD_LENGTH:
                payload = payload[:MAX_PAYLOAD_LENGTH] + "..."

            print(
                f"   Payload: {Fore.LIGHTBLACK_EX}{payload}{Style.RESET_ALL}"
            )