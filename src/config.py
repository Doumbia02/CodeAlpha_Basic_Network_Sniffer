"""
Project configuration.

This file contains values that may change depending on
the user's computer or preferences.
"""

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

EXPORT_CSV = True
EXPORT_JSON = True

CSV_FILE = "../exports/packets.csv"
JSON_FILE = "../exports/packets.json"