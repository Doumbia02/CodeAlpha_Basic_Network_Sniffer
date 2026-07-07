"""
cli.py
-------

Command Line Interface for the Network Packet Sniffer.
"""

from argparse import ArgumentParser, Namespace


def parse_arguments() -> Namespace:
    """
    Parse command-line arguments.
    """

    parser = ArgumentParser(
        prog="Network Packet Sniffer",
        description="Capture and analyze network packets using Scapy.",
    )

    parser.add_argument(
        "-i",
        "--interface",
        help="Network interface to capture from (e.g., en0)",
        type=str,
    )

    parser.add_argument(
        "-f",
        "--filter",
        help="BPF filter (e.g., tcp, udp, port 80)",
        type=str,
    )

    parser.add_argument(
        "-c",
        "--count",
        help="Maximum number of packets to capture",
        type=int,
    )

    parser.add_argument(
        "--list",
        action="store_true",
        help="List available network interfaces",
    )

    parser.add_argument(
        "--no-export",
        action="store_true",
        help="Disable CSV/JSON export",
    )

    parser.add_argument(
        "--no-display",
        action="store_true",
        help="Disable terminal output",
    )

    parser.add_argument(
        "--version",
        action="version",
        version="Network Packet Sniffer 1.0.0",
    )

    return parser.parse_args()
