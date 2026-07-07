"""
dashboard.py
------------

Live dashboard for the Network Packet Sniffer.
"""

from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()


def show_statistics(stats):

    table = Table(show_header=False)

    table.add_column("Metric")
    table.add_column("Value")

    table.add_row("Total Packets", str(stats.total_packets))
    table.add_row("TCP", str(stats.tcp))
    table.add_row("UDP", str(stats.udp))
    table.add_row("ICMP", str(stats.icmp))
    table.add_row("ARP", str(stats.arp))
    table.add_row("DNS", str(stats.dns))
    table.add_row("Other", str(stats.other))
    table.add_row("Bytes", str(stats.total_bytes))
    table.add_row("Duration", f"{stats.duration:.2f}s")
    table.add_row("PPS", f"{stats.packets_per_second:.2f}")

    console.print(
        Panel(
            table,
            title="Capture Statistics"
        )
    )