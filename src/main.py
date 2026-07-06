"""
main.py
--------

Entry point of the Network Packet Sniffer.
"""

from scapy.all import sniff

from config import (
    BPF_FILTER,
    MAX_PACKET_COUNT,
    NETWORK_INTERFACE,
)

from display import display_packet
from exporter import export_packet
from logger import (
    log_exception,
    log_info,
)
from packet_parser import parse_packet
from utils import (
    ensure_directory,
    print_banner,
)


def handle_packet(packet):
    """
    Process one captured packet.
    """

    try:

        packet_info = parse_packet(packet)

        display_packet(packet_info)

        export_packet(packet_info)

    except Exception:

        log_exception("Failed to process packet.")


def main():
    """
    Start the packet sniffer.
    """

    ensure_directory("../logs")

    ensure_directory("../exports")

    print_banner()

    log_info("Application started.")

    print()

    print("Starting packet capture...")

    print("Press CTRL + C to stop.\n")

    try:

        sniff(
            iface=NETWORK_INTERFACE,
            filter=BPF_FILTER,
            prn=handle_packet,
            count=MAX_PACKET_COUNT,
            store=False,
        )

    except KeyboardInterrupt:

        print("\nCapture stopped by user.")

        log_info("Capture stopped by user.")

    except Exception:

        log_exception("Unexpected application error.")

    finally:

        log_info("Application terminated.")


if __name__ == "__main__":
    main()