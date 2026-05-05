import os
import platform
from datetime import datetime


def collect_system_info():
    return {
        "timestamp": datetime.utcnow().isoformat(),
        "system": platform.system(),
        "node": platform.node(),
        "release": platform.release(),
        "processor": platform.processor(),
    }


def count_files(path="."):
    return len(os.listdir(path))


def scan_system(include_system=True, include_files=False):
    data = {}

    if include_system:
        data["system"] = collect_system_info()

    if include_files:
        data["files_in_cwd"] = count_files()

    return data
