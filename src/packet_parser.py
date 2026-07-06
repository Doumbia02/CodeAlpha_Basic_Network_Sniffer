from scapy.all import (
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

    return packet_info