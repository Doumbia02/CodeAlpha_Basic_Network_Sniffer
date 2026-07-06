"""
packet_parser.py
----------------

Parse Scapy packets into PacketInfo objects.
"""

from scapy.all import (
    Packet,
    Ether,
    IP,
    TCP,
    UDP,
    ICMP,
    ARP,
    DNS,
    Raw,
)

from models import PacketInfo


def parse_packet(packet: Packet) -> PacketInfo:
    """
    Convert a Scapy packet into a PacketInfo object.

    Parameters
    ----------
    packet : Packet
        The packet captured by Scapy.

    Returns
    -------
    PacketInfo
    """

    info = PacketInfo(
        timestamp=packet.time,
        length=len(packet),
    )

    # ==========================================================
    # Ethernet
    # ==========================================================

    if packet.haslayer(Ether):

        ethernet = packet[Ether]

        info.source_mac = ethernet.src
        info.destination_mac = ethernet.dst

    # ==========================================================
    # IP
    # ==========================================================

    if packet.haslayer(IP):

        ip = packet[IP]

        info.source_ip = ip.src
        info.destination_ip = ip.dst
        info.ttl = ip.ttl

    # ==========================================================
    # TCP
    # ==========================================================

    if packet.haslayer(TCP):

        tcp = packet[TCP]

        info.protocol = "TCP"
        info.source_port = tcp.sport
        info.destination_port = tcp.dport

    # ==========================================================
    # UDP
    # ==========================================================

    elif packet.haslayer(UDP):

        udp = packet[UDP]

        info.protocol = "UDP"
        info.source_port = udp.sport
        info.destination_port = udp.dport

    # ==========================================================
    # ICMP
    # ==========================================================

    elif packet.haslayer(ICMP):

        info.protocol = "ICMP"

    # ==========================================================
    # ARP
    # ==========================================================

    elif packet.haslayer(ARP):

        arp = packet[ARP]

        info.protocol = "ARP"

        info.source_ip = arp.psrc
        info.destination_ip = arp.pdst

    # ==========================================================
    # DNS
    # ==========================================================

    if packet.haslayer(DNS):

        info.protocol = "DNS"

    # ==========================================================
    # Payload
    # ==========================================================

    if packet.haslayer(Raw):

        try:

            info.payload = packet[Raw].load.decode(
                "utf-8",
                errors="ignore"
            )

        except Exception:

            info.payload = None

    return info