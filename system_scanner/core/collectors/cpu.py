import psutil


class CPUCollector:
    name = "cpu"

    def collect(self):
        return {
            "usage_percent": psutil.cpu_percent(interval=1),
            "cores": psutil.cpu_count(logical=True),
        }
