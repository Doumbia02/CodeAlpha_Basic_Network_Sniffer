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
NETWORK_INTERFACE = "en0"


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
BPF_FILTER = ""


# Maximum number of packets to capture.
#
# None means:
# Capture indefinitely until the user presses Ctrl + C.
#
MAX_PACKET_COUNT = 0


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

LOG_FILE = "logs/sniffer.log"

LOG_LEVEL = "INFO"


# ==============================================================================
# CSV Export
# ==============================================================================

EXPORT_CSV = True

CSV_FILE = "exports/packets.csv"


# ==============================================================================
# JSON Export
# ==============================================================================

EXPORT_JSON = True

JSON_FILE = "exports/packets.json"


EXPORT_PCAP = True

PCAP_FILE = "exports/capture.pcap"

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
