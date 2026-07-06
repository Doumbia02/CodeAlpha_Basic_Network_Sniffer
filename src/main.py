from scapy.all import sniff

from packet_parser import process_packet


def main():
    """
    Starts the packet sniffer.
    """

    print("Starting Network Packet Sniffer...")
    print("Press Ctrl+C to stop.\n")

    try:
        sniff(
            prn=process_packet,
            store=False
        )

    except KeyboardInterrupt:
        print("\nStopping packet sniffer...")

    finally:
        print("Program terminated successfully.")


if __name__ == "__main__":
    main()