import json
import platform
import os
from datetime import datetime

def scan_system(verbose=False):
    data = {
        "timestamp": datetime.utcnow().isoformat(),
        "system": platform.system(),
        "node": platform.node(),
        "release": platform.release(),
        "processor": platform.processor(),
        "files_in_cwd": len(os.listdir(".")),
    }

    if verbose:
        print("[*] Collecting system data...")
        print(data)

    return json.dumps(data, indent=4)
