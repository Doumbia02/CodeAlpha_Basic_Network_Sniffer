"""
display.py
----------

Responsible for displaying packets in the terminal.

This module does not know anything about Scapy.
It only receives PacketInfo objects.
"""

from colorama import Fore
from colorama import Style
from colorama import init

from config import (
    HEADER_REPEAT_INTERVAL,
    MAX_PAYLOAD_LENGTH,
    SHOW_PACKET_LENGTH,
    SHOW_PAYLOAD,
    SHOW_PORTS,
    SHOW_TIMESTAMP,
)

from models import PacketInfo

from utils import (
    format_timestamp,
    safe_value,
    truncate_text,
)
from scapy.all import hexdump

# Initialize Colorama
init(autoreset=True)

# Internal packet counter
_packet_counter = 0


def display_payload(packet):
    if packet.haslayer("Raw"):
        hexdump(packet["Raw"].load)


def protocol_color(protocol: str) -> str:
    """
    Return the display color for a protocol.
    """

    protocol = protocol.upper()

    colors = {
        "TCP": Fore.GREEN,
        "UDP": Fore.CYAN,
        "ICMP": Fore.YELLOW,
        "ARP": Fore.BLUE,
        "DNS": Fore.MAGENTA,
    }

    return colors.get(protocol, Fore.WHITE)


def print_header() -> None:
    """
    Print the packet table header.
    """

    print("=" * 115)

    print(
        f"{'Time':<20}"
        f"{'Protocol':<12}"
        f"{'Source IP':<18}"
        f"{'Destination IP':<18}"
        f"{'Ports':<20}"
        f"{'Length':<8}"
    )

    print("=" * 115)


def display_packet(packet: PacketInfo) -> None:
    """
    Display one parsed packet.
    """

    global _packet_counter

    _packet_counter += 1

    if _packet_counter == 1 or _packet_counter % HEADER_REPEAT_INTERVAL == 0:
        print_header()

    # ---------------------------------------
    # Timestamp
    # ---------------------------------------

    timestamp = ""

    if SHOW_TIMESTAMP:
        timestamp = format_timestamp(packet.timestamp)

    # ---------------------------------------
    # Protocol
    # ---------------------------------------

    protocol = (
        protocol_color(packet.protocol) + f"{packet.protocol:<12}" + Style.RESET_ALL
    )

    # ---------------------------------------
    # Ports
    # ---------------------------------------

    ports = "-"

    if (
        SHOW_PORTS
        and packet.source_port is not None
        and packet.destination_port is not None
    ):
        ports = f"{packet.source_port} → {packet.destination_port}"

    # ---------------------------------------
    # Length
    # ---------------------------------------

    length = ""

    if SHOW_PACKET_LENGTH:
        length = str(packet.length)

    # ---------------------------------------
    # Print Row
    # ---------------------------------------

    print(
        f"{timestamp:<20}"
        f"{protocol}"
        f"{safe_value(packet.source_ip):<18}"
        f"{safe_value(packet.destination_ip):<18}"
        f"{ports:<20}"
        f"{length:<8}"
    )

    # ---------------------------------------
    # Payload
    # ---------------------------------------

    if SHOW_PAYLOAD and packet.payload:

        payload = truncate_text(
            packet.payload,
            MAX_PAYLOAD_LENGTH,
        )

        print(
            f"    Payload: " f"{Fore.LIGHTBLACK_EX}" f"{payload}" f"{Style.RESET_ALL}"
        )
