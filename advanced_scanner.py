import platform
import socket
import os
import json
import argparse
import datetime

def collect_system_info():
    return {
        "os": platform.system(),
        "release": platform.release(),
        "version": platform.version(),
        "machine": platform.machine(),
        "processor": platform.processor(),
        "hostname": socket.gethostname(),
        "user": os.getlogin(),
        "scan_time": datetime.datetime.now().isoformat()
    }

def collect_environment(limit=10):
    env = dict(os.environ)
    return dict(list(env.items())[:limit])

def save_report(data, filename="scan_report.json"):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

def main():
    parser = argparse.ArgumentParser(description="System Scanner Tool")
    parser.add_argument("--system", action="store_true", help="Scan system info")
    parser.add_argument("--env", action="store_true", help="Scan environment variables")
    parser.add_argument("--full", action="store_true", help="Run full scan")

    args = parser.parse_args()

    report = {}

    if args.system or args.full:
        report["system"] = collect_system_info()

    if args.env or args.full:
        report["environment"] = collect_environment()

    if not report:
        print("No scan option selected. Use --help")
        return

    save_report(report)
    print("Scan completed. Output saved to scan_report.json")

if __name__ == "__main__":
    main()
