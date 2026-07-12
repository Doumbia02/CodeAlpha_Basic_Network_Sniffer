"""
statistics.py
-------------

Real-time packet statistics.
"""

from __future__ import annotations

import time

from models import PacketInfo


class Statistics:

    def __init__(self):

        self.start_time = time.time()

        self.total_packets = 0
        self.total_bytes = 0

        self.tcp = 0
        self.udp = 0
        self.icmp = 0
        self.arp = 0
        self.dns = 0
        self.other = 0

    def update(self, packet: PacketInfo):

        self.total_packets += 1
        self.total_bytes += packet.length

        protocol = packet.protocol.upper()

        if protocol == "TCP":
            self.tcp += 1

        elif protocol == "UDP":
            self.udp += 1

        elif protocol == "ICMP":
            self.icmp += 1

        elif protocol == "ARP":
            self.arp += 1

        elif protocol == "DNS":
            self.dns += 1

        else:
            self.other += 1

    @property
    def duration(self):

        return time.time() - self.start_time

    @property
    def packets_per_second(self):

        if self.duration == 0:
            return 0

        return self.total_packets / self.duration

    def print_summary(self):

        print()

        print("=" * 60)
        print("Capture Summary")
        print("=" * 60)

        print(f"Total Packets : {self.total_packets}")
        print(f"TCP           : {self.tcp}")
        print(f"UDP           : {self.udp}")
        print(f"ICMP          : {self.icmp}")
        print(f"ARP           : {self.arp}")
        print(f"DNS           : {self.dns}")
        print(f"Other         : {self.other}")

        print()

        print(f"Bytes         : {self.total_bytes}")

        print(f"Duration      : {self.duration:.2f} seconds")

        print(f"PPS           : {self.packets_per_second:.2f}")

        print("=" * 60)
