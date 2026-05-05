import json
import platform
import os

def scan_system(verbose=False):
    data = {
        "system": platform.system(),
        "node": platform.node(),
        "release": platform.release(),
        "processor": platform.processor(),
        "files_in_cwd": len(os.listdir(".")),
    }

    if verbose:
        print("Scanning system...")
        print(data)

    return json.dumps(data, indent=4)
