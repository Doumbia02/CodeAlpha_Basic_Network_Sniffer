<div align="center">

# 🌐 Python Network Packet Sniffer

### A Professional Network Packet Analysis Tool Built with Python & Scapy

[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)]()
[![Scapy](https://img.shields.io/badge/Scapy-Packet%20Analysis-blue?style=for-the-badge)]()
[![Platform](https://img.shields.io/badge/Platform-macOS%20%7C%20Linux%20%7C%20Windows-success?style=for-the-badge)]()
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)]()
[![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)]()

---

*A lightweight, extensible, and professional packet sniffer designed for learning network programming, packet analysis, and cybersecurity.*

</div>

---

# 📑 Table of Contents

- [Project Overview](#-project-overview)
- [Why This Project?](#-why-this-project)
- [Features](#-features)
- [Demo](#-demo)
- [Screenshots](#-screenshots)
- [System Architecture](#-system-architecture)
- [Packet Processing Pipeline](#-packet-processing-pipeline)
- [Project Structure](#-project-structure)
- [Technology Stack](#-technology-stack)
- [Installation](#-installation)
- [Configuration](#-configuration)
- [Usage](#-usage)
- [Command Line Reference](#-command-line-reference)
- [Output Files](#-output-files)
- [Testing](#-testing)
- [Logging](#-logging)
- [Statistics Engine](#-statistics-engine)
- [Design Decisions](#-design-decisions)
- [Future Improvements](#-future-improvements)
- [Contributing](#-contributing)
- [License](#-license)
- [Author](#-author)

---

# 📖 Project Overview

## What is this project?

The **Python Network Packet Sniffer** is a command-line application that captures, analyzes, and exports network traffic in real time using the Scapy library.

It was developed to provide hands-on experience with:

- Computer Networking
- Network Programming
- Packet Analysis
- Cybersecurity Fundamentals
- Python Software Engineering
- Clean Project Architecture

Unlike a minimal packet sniffer that only prints packet information to the terminal, this project is organized as a modular Python application with reusable components, export capabilities, logging, statistics, and automated testing.

---

# 🎯 Project Objectives

The main objectives of this project are:

- Capture live packets from a selected network interface.
- Parse packets into structured Python objects.
- Display packet information in a readable format.
- Export captured packets to CSV, JSON, and PCAP formats.
- Produce real-time traffic statistics.
- Provide a user-friendly command-line interface.
- Demonstrate software engineering best practices.

---

# ❓ Why This Project?

Modern cybersecurity professionals and network engineers rely heavily on packet analysis tools to understand network behavior.

Applications such as:

- Wireshark
- tcpdump
- tshark
- Zeek
- NetworkMiner

all begin by capturing packets from a network interface.

This project demonstrates the fundamental concepts behind those tools while remaining approachable for students and developers who want to understand how packet sniffing works internally.

Although it is not intended to replace enterprise-grade analyzers, it serves as an educational foundation for learning packet capture, protocol analysis, and software design.

---

# ✨ Features

## Core Features

- ✅ Live packet capture using Scapy
- ✅ Automatic network interface discovery
- ✅ Berkeley Packet Filter (BPF) support
- ✅ TCP packet parsing
- ✅ UDP packet parsing
- ✅ ICMP packet parsing
- ✅ ARP packet parsing
- ✅ DNS packet detection
- ✅ Graceful handling of unknown protocols

---

## Data Export

Captured packets can be exported as:

- 📄 CSV
- 📄 JSON
- 📦 PCAP (Wireshark compatible)

---

## Monitoring

The application provides:

- Live packet monitoring
- Real-time statistics
- Protocol counters
- Packet rate calculation
- Byte counters
- Capture duration

---

## Software Engineering Features

- Modular architecture
- Object-oriented data model
- Configuration management
- Structured logging
- Command-line interface
- Unit testing
- Type hints
- Clean project organization

---

# 🎥 Demo

When the application starts:

```text
============================================================
Network Packet Sniffer v1.0.0
============================================================

Interface : en0
Filter    : tcp
Count     : Unlimited

CSV Export  : Enabled
JSON Export : Enabled
PCAP Export : Enabled

============================================================
```

During capture:

```text
Time       Protocol Source             Destination        Length
-----------------------------------------------------------------
20:13:04   TCP      192.168.1.10       8.8.8.8            74
20:13:04   UDP      192.168.1.10       1.1.1.1            56
20:13:05   ICMP     192.168.1.10       8.8.4.4            98
```

After stopping the capture:

```text
============================================================
Capture Summary
============================================================

Packets Captured : 1248
TCP              : 845
UDP              : 310
ICMP             : 63
ARP              : 30

Bytes Captured   : 5,912,430
Duration         : 42.5 seconds
Packets/Second   : 29.4

============================================================
```

---

# 📷 Screenshots

Create a folder named:

```text
screenshots/
```

Recommended screenshots:

```
screenshots/
│
├── startup.png
├── interface-list.png
├── packet-capture.png
├── statistics.png
├── csv-output.png
├── json-output.png
└── wireshark-pcap.png
```

Once captured, add them like this:

```markdown
## Application Startup

![Startup](screenshots/startup.png)

## Live Packet Capture

![Capture](screenshots/packet-capture.png)

## Statistics Dashboard

![Statistics](screenshots/statistics.png)
```

---

# 🏗️ System Architecture

```text
                         +----------------------+
                         |      User CLI        |
                         +----------+-----------+
                                    |
                                    ▼
                           Command-Line Parser
                                    |
                                    ▼
                          Network Interface Layer
                                    |
                                    ▼
                               Scapy Sniffer
                                    |
                                    ▼
                            Packet Parser Module
                                    |
                                    ▼
                               PacketInfo Model
                                    |
            +-----------------------+-----------------------+
            |                       |                       |
            ▼                       ▼                       ▼
      Display Module          Statistics Engine      Export Modules
                                                          |
                                      +-------------------+------------------+
                                      |                   |                  |
                                      ▼                   ▼                  ▼
                                    CSV                JSON               PCAP
```

---

# 🔄 Packet Processing Pipeline

```text
Network Traffic
        │
        ▼
Operating System
        │
        ▼
Scapy Packet Capture
        │
        ▼
Packet Parsing
        │
        ▼
PacketInfo Object
        │
        ├────────► Terminal Display
        ├────────► Statistics Engine
        ├────────► CSV Export
        ├────────► JSON Export
        ├────────► PCAP Export
        └────────► Logging
```

---

# 📁 Project Structure

```text
NetworkPacketSniffer/
│
├── src/
│   ├── main.py
│   ├── cli.py
│   ├── config.py
│   ├── network.py
│   ├── packet_parser.py
│   ├── statistics.py
│   ├── display.py
│   ├── exporter.py
│   ├── pcap_exporter.py
│   ├── dashboard.py
│   ├── logger.py
│   ├── models.py
│   └── utils.py
│
├── tests/
├── exports/
├── logs/
├── screenshots/
│
├── README.md
├── requirements.txt
├── pyproject.toml
├── Dockerfile
├── LICENSE
└── CHANGELOG.md
```

---

# 🛠️ Technology Stack

| Category | Technology |
|----------|------------|
| Programming Language | Python 3 |
| Packet Capture | Scapy |
| CLI | argparse |
| Dashboard | Rich |
| Logging | logging |
| Configuration | python-dotenv |
| Testing | pytest |
| Formatting | Black |
| Linting | Ruff |
| Type Checking | MyPy |
| Version Control | Git |
| Repository Hosting | GitHub |

---
# 💻 Installation

This project supports:

- 🍎 macOS
- 🐧 Linux
- 🪟 Windows

---

## Prerequisites

Before installing the project, make sure you have the following software installed:

| Software | Version |
|----------|---------|
| Python | 3.11 or later |
| Git | Latest |
| pip | Latest |
| Virtual Environment | Recommended |

To verify your installation:

```bash
python --version
pip --version
git --version
```

---

# 📥 Clone the Repository

```bash
git clone https://github.com/<your-username>/python-network-packet-sniffer.git

cd python-network-packet-sniffer
```

Replace `<your-username>` with your GitHub username.

---

# 🐍 Create a Virtual Environment

Using a virtual environment keeps your project dependencies isolated from other Python projects.

## macOS / Linux

```bash
python3 -m venv .venv

source .venv/bin/activate
```

---

## Windows

```powershell
python -m venv .venv

.venv\Scripts\activate
```

After activation you should see something similar to:

```text
(.venv)
```

at the beginning of your terminal prompt.

---

# 📦 Install Dependencies

Install all required Python packages:

```bash
pip install -r requirements.txt
```

Verify the installation:

```bash
pip list
```

Expected packages include:

- scapy
- rich
- colorama
- python-dotenv
- pytest

---

# ⚙ Configuration

The application supports configuration through a `.env` file.

Create a new file named:

```text
.env
```

Example:

```text
INTERFACE=en0

FILTER=

COUNT=0

EXPORT_CSV=True

EXPORT_JSON=True

EXPORT_PCAP=True

ENABLE_LOGGING=True

CSV_FILE=exports/packets.csv

JSON_FILE=exports/packets.json

PCAP_FILE=exports/capture.pcap

LOG_FILE=logs/sniffer.log
```

---

## Configuration Options

| Variable | Description |
|-----------|-------------|
| INTERFACE | Network interface used for capturing packets |
| FILTER | Berkeley Packet Filter (BPF) |
| COUNT | Number of packets to capture (0 = unlimited) |
| EXPORT_CSV | Enable CSV export |
| EXPORT_JSON | Enable JSON export |
| EXPORT_PCAP | Enable PCAP export |
| ENABLE_LOGGING | Enable logging |
| CSV_FILE | CSV output file |
| JSON_FILE | JSON output file |
| PCAP_FILE | PCAP output file |
| LOG_FILE | Log output file |

---

# 🚀 Running the Application

The application supports multiple execution modes.

---

## Show Help

```bash
python src/main.py --help
```

Output:

```text
usage: main.py [OPTIONS]

Options:

--help

--list

--interface

--filter

--count
```

---

## List Available Network Interfaces

```bash
python src/main.py --list
```

Example output:

```text
============================================================

Available Network Interfaces

============================================================

1   lo0

2   en0

3   awdl0

4   bridge0

5   utun0
```

---

## Capture on Default Interface

```bash
sudo python src/main.py
```

---

## Capture on a Specific Interface

```bash
sudo python src/main.py --interface en0
```

---

## Capture Only TCP Packets

```bash
sudo python src/main.py --interface en0 --filter tcp
```

---

## Capture Only UDP Packets

```bash
sudo python src/main.py --interface en0 --filter udp
```

---

## Capture DNS Packets

```bash
sudo python src/main.py --interface en0 --filter port 53
```

---

## Capture HTTP Traffic

```bash
sudo python src/main.py --interface en0 --filter port 80
```

---

## Capture HTTPS Traffic

```bash
sudo python src/main.py --interface en0 --filter port 443
```

---

## Capture a Fixed Number of Packets

```bash
sudo python src/main.py --interface en0 --count 100
```

The application automatically stops after capturing 100 packets.

---

# 📖 Command Line Reference

| Command | Description |
|----------|-------------|
| `--help` | Display all available options |
| `--list` | Display available network interfaces |
| `--interface` | Select a network interface |
| `--filter` | Apply a Berkeley Packet Filter |
| `--count` | Capture a fixed number of packets |

---

# 📡 Supported Protocols

The parser currently supports:

| Protocol | Supported |
|----------|-----------|
| Ethernet | ✅ |
| IPv4 | ✅ |
| TCP | ✅ |
| UDP | ✅ |
| ICMP | ✅ |
| ARP | ✅ |
| DNS | ✅ |

Protocols that are not explicitly recognized are safely categorized as **Other**.

---

# 📤 Export Files

During packet capture the application automatically exports captured data.

---

## CSV Export

CSV files are ideal for:

- Excel
- Google Sheets
- Data analysis
- Machine Learning datasets

Example:

```csv
Timestamp,Protocol,Source,Destination,Length
12:30:11,TCP,192.168.1.20,8.8.8.8,74
```

---

## JSON Export

JSON provides structured packet data that can be consumed by other applications.

Example:

```json
{
    "protocol":"TCP",
    "source":"192.168.1.20",
    "destination":"8.8.8.8",
    "length":74
}
```

---

## PCAP Export

The application also saves packets in the PCAP format.

Benefits:

- Compatible with Wireshark
- Compatible with tcpdump
- Can be shared with other analysts
- Useful for offline packet analysis

Example:

```text
exports/

capture.pcap
```

Simply open the generated file in Wireshark for detailed packet inspection.

---

# 📂 Generated Files

After running the application, your project will contain:

```text
exports/

├── packets.csv

├── packets.json

└── capture.pcap

logs/

└── sniffer.log
```

---

# 🖥 Example Workflow

1. Start the application.

2. Select a network interface.

3. Capture packets.

4. Display live packet information.

5. Update statistics.

6. Export packet information.

7. Save logs.

8. Open the PCAP file in Wireshark for deeper analysis.

This workflow mirrors the typical packet analysis process followed by network engineers and cybersecurity professionals.

---

# ⚠ Platform Notes

### macOS

Packet capture usually requires administrator privileges:

```bash
sudo python src/main.py
```

---

### Linux

Packet capture may require:

```bash
sudo
```

or appropriate `CAP_NET_RAW` capabilities depending on your distribution.

---

### Windows

Run the terminal as **Administrator** and ensure that the packet capture driver required by Scapy is installed.

---

# 📊 Statistics Engine

One of the main goals of this project is not only to capture packets but also to provide meaningful real-time insights about the captured traffic.

The `Statistics` module continuously updates information while packets are being captured.

Current metrics include:

| Metric | Description |
|---------|-------------|
| Total Packets | Number of captured packets |
| TCP Packets | Number of TCP packets |
| UDP Packets | Number of UDP packets |
| ICMP Packets | Number of ICMP packets |
| ARP Packets | Number of ARP packets |
| DNS Packets | Number of DNS packets |
| Other Packets | Packets with unsupported or unknown protocols |
| Bytes Captured | Total traffic size |
| Capture Duration | Total capture time |
| Packets Per Second (PPS) | Capture rate |

Example:

```text
===========================================================
Capture Summary
===========================================================

Total Packets : 1842

TCP           : 1134

UDP           : 491

ICMP          : 120

ARP           : 97

Bytes         : 7,483,912

Duration      : 56.4 seconds

Packets/Second: 32.6

===========================================================
```

---

# 📝 Logging

The application maintains structured logs for debugging and auditing purposes.

Example log:

```text
==================================================

Application Started

Version : 1.0.0

Interface : en0

Filter : tcp

==================================================

Packet Captured

Protocol : TCP

Source : 192.168.1.20

Destination : 8.8.8.8

==================================================
```

Log files are stored in:

```text
logs/

└── sniffer.log
```

---

# 🧪 Testing

Quality and reliability are important aspects of this project.

Unit tests are implemented using **pytest**.

Run all tests:

```bash
pytest
```

Example output:

```text
==============================

10 passed

==============================
```

---

## Code Formatting

This project follows the **Black** code style.

Run:

```bash
black src tests
```

---

## Linting

Static analysis is performed using **Ruff**.

```bash
ruff check src tests
```

---

## Type Checking

Type hints are validated using **MyPy**.

```bash
mypy src
```

---

# 🏗 Design Decisions

This project was intentionally designed using a modular architecture.

Instead of placing all logic inside `main.py`, each responsibility has its own module.

| Module | Responsibility |
|----------|----------------|
| cli.py | Parse command-line arguments |
| config.py | Centralized configuration |
| network.py | Interface discovery and validation |
| packet_parser.py | Packet parsing |
| models.py | Packet data model |
| display.py | Packet visualization |
| dashboard.py | Statistics dashboard |
| exporter.py | CSV and JSON export |
| pcap_exporter.py | PCAP export |
| statistics.py | Capture statistics |
| logger.py | Logging |
| utils.py | Helper functions |

This separation of concerns makes the project easier to maintain, test, and extend.

---

# 🔒 Security Considerations

This project is intended for educational and authorized network analysis.

Before capturing network traffic:

- Obtain permission to monitor the network.
- Do not capture traffic belonging to other users without authorization.
- Follow local laws and organizational policies.
- Use the application responsibly.

---

# 🐳 Docker

A Dockerfile is included for containerized execution.

Build:

```bash
docker build -t network-packet-sniffer .
```

Run:

```bash
docker run --rm network-packet-sniffer
```

> **Note:** Capturing live packets from within a container often requires additional networking configuration and elevated privileges. Refer to your Docker platform's documentation if you intend to use live packet capture in a container.

---

# ⚙ Continuous Integration

GitHub Actions automatically performs:

- Dependency installation
- Code formatting checks
- Linting
- Unit testing

Every push to the repository is automatically verified.

---

# 📈 Future Roadmap

### Version 1.1

- IPv6 support
- Additional protocol parsing
- Better filtering
- Rich dashboard improvements

---

### Version 2.0

- Graphical User Interface (GUI)
- Interactive packet viewer
- Search and filtering
- Packet replay

---

### Version 3.0

- Intrusion Detection System (IDS)
- Machine Learning anomaly detection
- GeoIP lookup
- DNS analysis
- HTTP parser
- TLS detection
- REST API
- Web dashboard

---

# 🤝 Contributing

Contributions are welcome.

To contribute:

1. Fork the repository.
2. Create a new branch.

```bash
git checkout -b feature/new-feature
```

3. Commit your changes.

```bash
git commit -m "Add new feature"
```

4. Push your branch.

```bash
git push origin feature/new-feature
```

5. Open a Pull Request.

---

# ❓ Frequently Asked Questions

## Why do I need administrator privileges?

Operating systems restrict access to raw network packets. Running with elevated privileges allows Scapy to capture packets from network interfaces.

---

## Why are no packets being captured?

Possible causes include:

- Incorrect interface selected
- Insufficient privileges
- No network traffic on the interface
- Incorrect Berkeley Packet Filter

Use:

```bash
python src/main.py --list
```

to verify available interfaces.

---

## Why can't I open the PCAP file?

Ensure the capture completed successfully and open the generated file with Wireshark.

---

# 📚 References

This project was inspired by concepts and tools from:

- Scapy Documentation
- Wireshark Documentation
- tcpdump Manual
- Python Documentation
- RFC 791 (IPv4)
- RFC 793 (TCP)
- RFC 768 (UDP)

---

# 🎓 Learning Outcomes

By completing this project, you will gain experience with:

- Python programming
- Software Engineering
- Network Programming
- Packet Analysis
- Cybersecurity Fundamentals
- Command-Line Applications
- Logging
- Testing
- Git and GitHub
- Clean Project Architecture

---

# 📄 License

This project is distributed under the MIT License.

See the `LICENSE` file for additional information.

---

# 👨‍💻 Author

**Youssouf Doumbia**

Bachelor of Science (B.Sc.) in Computer Science & Engineering

Interests:

- Cybersecurity
- DevOps
- Software Engineering
- Machine Learning
- Cloud Computing

GitHub:

```
https://github.com/Doumbia02
```

LinkedIn:

```
linkedin.com/in/youssouf-doumbia-977413257
```

---

# 🙏 Acknowledgements

Special thanks to:

- The Scapy development team
- The Python Software Foundation
- The Wireshark community
- Open-source contributors worldwide

for creating tools and resources that make projects like this possible.

---

<div align="center">

## ⭐ If you found this project useful, please consider giving it a star!

Thank you for visiting this repository.

Happy Packet Sniffing! 🚀

</div>
