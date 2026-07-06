"""
main.py
--------

Entry point of the Network Packet Sniffer.
"""
from cli import parse_arguments
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



from statistics import Statistics

from pcap_exporter import (
    export_pcap,
    close_pcap,
)
args = parse_arguments()
stats = Statistics()

def handle_packet(packet):
    """
    Process one captured packet.
    """

    try:

        packet_info = parse_packet(packet)

        stats.update(packet_info)

        display_packet(packet_info)

        export_packet(packet_info)

        export_pcap(packet)

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
            iface=args.interface or NETWORK_INTERFACE,
            filter=args.filter or BPF_FILTER,
            count=args.count or MAX_PACKET_COUNT,
            prn=handle_packet,
            store=False,
            )

    except KeyboardInterrupt:

        print("\nCapture stopped by user.")

        log_info("Capture stopped by user.")

    except Exception:

        log_exception("Unexpected application error.")

    finally:
        stats.print_summary()
        close_pcap()
        log_info("Application terminated.")
         
       

if __name__ == "__main__":
    main()