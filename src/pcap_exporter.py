"""
pcap_exporter.py
----------------
Save captured packets to a PCAP file.
"""

from pathlib import Path

from scapy.all import PcapWriter

from config import PCAP_FILE, EXPORT_PCAP


_writer = None


def export_pcap(packet):

    global _writer

    if not EXPORT_PCAP:
        return

    if _writer is None:

        Path(PCAP_FILE).parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        _writer = PcapWriter(
            PCAP_FILE,
            append=True,
            sync=True,
        )

    _writer.write(packet)


def close_pcap():

    global _writer

    if _writer:

        _writer.close()