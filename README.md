📄 README.md — Ping Sweeper Script

# 🔍 Ping Sweeper – Network Host Discovery Tool (Python)

This script performs a basic *ping sweep* to detect *live hosts* in a given subnet.

It automatically adjusts to *Windows or Linux/Mac*, and sends one ICMP packet (ping) to each IP in the range .1 to .254.

---

## 🚀 Features

- Supports both *Windows* and *Unix/Linux* systems
- Scans full Class C subnet (e.g., 192.168.1.1 – 192.168.1.254)
- Uses built-in Python libraries (os, platform)
- Simple and readable code structure
- Great for beginner-level *network recon*

---

## 🧠 How It Works

1. The user inputs a subnet prefix (e.g., 192.168.56)
2. The script pings all 254 addresses in that range
3. It prints which hosts responded and which didn’t

---

## 📦 Requirements

- Python 3.x
- Works on:
  - 🪟 Windows
  - 🐧 Linux
  - 🍎 macOS

No third-party libraries needed.

---

## 💻 Usage

```bash
python ping-sweep.py

Then enter a subnet prefix like:

192.168.56


---

🖥️ Example Output

🔎 Scanning subnet 192.168.56.1 to 192.168.56.254...

✅ Host 192.168.56.1 is alive
❌ Host 192.168.56.2 is unreachable
✅ Host 192.168.56.3 is alive
...


---

🔐 Educational Use Only

This tool is for educational and lab environments. Always have permission before scanning networks.


---

🧠 Author

Prince Solanki
GitHub | Blog


---

✅ Part of My Cybersecurity Lab Portfolio

This tool is one of several Python utilities I’m building to grow as a blue team analyst. You can find more in my script-tools repo.

---
