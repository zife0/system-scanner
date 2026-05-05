import platform
import socket
import os
import json
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

def collect_environment(limit=15):
    env = dict(os.environ)
    return dict(list(env.items())[:limit])

def save_report(data, filename="scan_report.json"):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

def main():
    report = {
        "system": collect_system_info(),
        "environment": collect_environment()
    }

    save_report(report)
    print("Scan completed successfully.")
    print("Report saved as scan_report.json")

if __name__ == "__main__":
    main()
