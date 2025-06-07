import os
import platform

def ping_host(ip):
    param = "-n" if platform.system().lower() == "windows" else "-c"
    response = os.system(f"ping {param} 1 {ip} > nul 2>&1" if platform.system().lower() == "windows" else f"ping {param} 1 {ip} > /dev/null 2>&1")
    return response == 0

def sweep_subnet(subnet_prefix):
    print(f"🔎 Scanning subnet {subnet_prefix}.1 to {subnet_prefix}.254...\n")
    for i in range(1, 255):
        ip = f"{subnet_prefix}.{i}"
        if ping_host(ip):
            print(f"✅ Host {ip} is alive")
        else:
            print(f"❌ Host {ip} is unreachable")

if __name__ == "__main__":
    subnet = input("Enter subnet (e.g., 192.168.56): ").strip()
    sweep_subnet(subnet)
