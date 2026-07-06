"""
Project configuration.

This file contains values that may change depending on
the user's computer or preferences.


# ==========================
# Network Configuration
# ==========================

# Network interface.
# None means Scapy automatically selects the default interface.
NETWORK_INTERFACE = None

# Capture only these protocols.
# Set to None to capture everything.
BPF_FILTER = None

# ==========================
# Display Configuration
# ==========================

SHOW_PAYLOAD = True
MAX_PAYLOAD_LENGTH = 80

# ==========================
# Logging
# ==========================

ENABLE_LOGGING = True
LOG_FILE = "../logs/sniffer.log"

# ==========================
# Export
# ==========================

#EXPORT_CSV = True
#EXPORT_JSON = True

#CSV_FILE = "../exports/packets.csv"
#JSON_FILE = "../exports/packets.json"
"""
"""
config.py
---------

Central configuration file for the Network Packet Sniffer.

This file contains all configurable settings used throughout the project.
Changing values here allows you to customize the application's behavior
without modifying the rest of the source code.
"""

# ==============================================================================
# Network Configuration
# ==============================================================================

# Network interface to capture packets from.
#
# None:
#     Automatically use the system's default network interface.
#
# Example:
#     "en0"    -> Wi-Fi on most macOS systems
#     "en1"    -> Secondary interface (depends on your Mac)
#     "eth0"   -> Linux Ethernet
#     "wlan0"  -> Linux Wi-Fi
#
NETWORK_INTERFACE = None


# Berkeley Packet Filter (BPF)
#
# None:
#     Capture every packet.
#
# Examples:
#
# "tcp"
# "udp"
# "icmp"
# "arp"
# "port 53"
# "port 80"
# "port 443"
# "host 8.8.8.8"
# "src host 192.168.1.10"
#
BPF_FILTER = None


# Maximum number of packets to capture.
#
# None means:
# Capture indefinitely until the user presses Ctrl + C.
#
MAX_PACKET_COUNT = None


# ==============================================================================
# Display Configuration
# ==============================================================================

# Display packet payload in the terminal.
SHOW_PAYLOAD = True

# Maximum number of payload characters to display.
#
# Long payloads are truncated to keep the terminal readable.
#
MAX_PAYLOAD_LENGTH = 80

# Show packet timestamp.
SHOW_TIMESTAMP = True

# Show MAC addresses.
SHOW_MAC_ADDRESS = True

# Show IP addresses.
SHOW_IP_ADDRESS = True

# Show transport layer ports.
SHOW_PORTS = True

# Show TTL.
SHOW_TTL = True

# Show packet size.
SHOW_PACKET_LENGTH = True


# ==============================================================================
# Logging Configuration
# ==============================================================================

ENABLE_LOGGING = True

LOG_FILE = "../logs/sniffer.log"

LOG_LEVEL = "INFO"


# ==============================================================================
# CSV Export
# ==============================================================================

EXPORT_CSV = True

CSV_FILE = "../exports/packets.csv"


# ==============================================================================
# JSON Export
# ==============================================================================

EXPORT_JSON = True

JSON_FILE = "../exports/packets.json"


# ==============================================================================
# Terminal Display
# ==============================================================================

# Print table header every N packets.
#
# This improves readability during long captures.
#
HEADER_REPEAT_INTERVAL = 25


# ==============================================================================
# Application Information
# ==============================================================================

APP_NAME = "Network Packet Sniffer"

VERSION = "1.0.0"

AUTHOR = "Youssouf Doumbia"

LICENSE = "MIT"