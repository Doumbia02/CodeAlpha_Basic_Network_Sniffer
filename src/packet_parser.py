"""from scapy.all import (
    Ether,
    IP,
    TCP,
    UDP,
    ICMP,
    ARP,
    DNS,
    Raw
)


def process_packet(packet):

    packet_info = {
        "timestamp": packet.time,
        "source_mac": None,
        "destination_mac": None,
        "source_ip": None,
        "destination_ip": None,
        "protocol": "Unknown",
        "source_port": None,
        "destination_port": None,
        "ttl": None,
        "length": len(packet),
        "payload": None
    }

    if packet.haslayer(Ether):
        packet_info["source_mac"] = packet[Ether].src
        packet_info["destination_mac"] = packet[Ether].dst

    if packet.haslayer(IP):
        packet_info["source_ip"] = packet[IP].src
        packet_info["destination_ip"] = packet[IP].dst
        packet_info["ttl"] = packet[IP].ttl

    if packet.haslayer(TCP):
        packet_info["protocol"] = "TCP"
        packet_info["source_port"] = packet[TCP].sport
        packet_info["destination_port"] = packet[TCP].dport

    elif packet.haslayer(UDP):
        packet_info["protocol"] = "UDP"
        packet_info["source_port"] = packet[UDP].sport
        packet_info["destination_port"] = packet[UDP].dport

    elif packet.haslayer(ICMP):
        packet_info["protocol"] = "ICMP"

    elif packet.haslayer(ARP):
        packet_info["protocol"] = "ARP"

    if packet.haslayer(DNS):
        packet_info["protocol"] = "DNS"

    if packet.haslayer(Raw):
        packet_info["payload"] = (
            packet[Raw]
            .load
            .decode(errors="ignore")
        )

    return packet_info"""

"""
packet_parser.py
----------------

Responsible for parsing Scapy packets and converting them into
a structured Python dictionary.

This module DOES NOT:
- print packets
- save packets
- log packets

Its only responsibility is to extract useful information.
"""

from typing import Any, Dict

from scapy.all import (
    ARP,
    DNS,
    Ether,
    ICMP,
    IP,
    Raw,
    TCP,
    UDP,
    Packet,
)


def parse_packet(packet: Packet) -> Dict[str, Any]:
    """
    Parse a Scapy packet into a structured dictionary.

    Parameters
    ----------
    packet : Packet
        A Scapy Packet object.

    Returns
    -------
    dict
        A dictionary containing extracted packet information.
    """

    packet_info = {
        "timestamp": packet.time,
        "length": len(packet),

        # Layer 2
        "source_mac": None,
        "destination_mac": None,

        # Layer 3
        "source_ip": None,
        "destination_ip": None,
        "ttl": None,

        # Layer 4
        "protocol": "Unknown",
        "source_port": None,
        "destination_port": None,

        # Application
        "payload": None,
    }

    # ============================================================
    # Ethernet Layer
    # ============================================================

    if packet.haslayer(Ether):
        ethernet = packet[Ether]

        packet_info["source_mac"] = ethernet.src
        packet_info["destination_mac"] = ethernet.dst

    # ============================================================
    # IP Layer
    # ============================================================

    if packet.haslayer(IP):
        ip = packet[IP]

        packet_info["source_ip"] = ip.src
        packet_info["destination_ip"] = ip.dst
        packet_info["ttl"] = ip.ttl

    # ============================================================
    # TCP
    # ============================================================

    if packet.haslayer(TCP):

        tcp = packet[TCP]

        packet_info["protocol"] = "TCP"
        packet_info["source_port"] = tcp.sport
        packet_info["destination_port"] = tcp.dport

    # ============================================================
    # UDP
    # ============================================================

    elif packet.haslayer(UDP):

        udp = packet[UDP]

        packet_info["protocol"] = "UDP"
        packet_info["source_port"] = udp.sport
        packet_info["destination_port"] = udp.dport

    # ============================================================
    # ICMP
    # ============================================================

    elif packet.haslayer(ICMP):

        packet_info["protocol"] = "ICMP"

    # ============================================================
    # ARP
    # ============================================================

    elif packet.haslayer(ARP):

        packet_info["protocol"] = "ARP"

        arp = packet[ARP]

        packet_info["source_ip"] = arp.psrc
        packet_info["destination_ip"] = arp.pdst

    # ============================================================
    # DNS Detection
    # ============================================================

    if packet.haslayer(DNS):

        packet_info["protocol"] = "DNS"

    # ============================================================
    # Payload
    # ============================================================

    if packet.haslayer(Raw):

        try:

            payload = packet[Raw].load.decode(
                "utf-8",
                errors="ignore"
            )

            packet_info["payload"] = payload

        except Exception:

            packet_info["payload"] = None

    return packet_info