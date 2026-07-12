from dataclasses import dataclass
from typing import Optional


@dataclass(slots=True)
class PacketInfo:
    """
    Represents a parsed network packet.

    Every captured packet is converted into this object before
    being displayed, exported or logged.
    """

    # ==========================
    # General Information
    # ==========================

    timestamp: float
    length: int

    # ==========================
    # Layer 2 (Ethernet)
    # ==========================

    source_mac: Optional[str] = None
    destination_mac: Optional[str] = None

    # ==========================
    # Layer 3 (IP)
    # ==========================

    source_ip: Optional[str] = None
    destination_ip: Optional[str] = None
    ttl: Optional[int] = None

    # ==========================
    # Layer 4 (Transport)
    # ==========================

    protocol: str = "Unknown"

    source_port: Optional[int] = None
    destination_port: Optional[int] = None

    # ==========================
    # Payload
    # ==========================

    payload: Optional[str] = None
