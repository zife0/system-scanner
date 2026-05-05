import psutil


class MemoryCollector:
    name = "memory"

    def collect(self):
        mem = psutil.virtual_memory()

        return {
            "total": mem.total,
            "used": mem.used,
            "available": mem.available,
            "usage_percent": mem.percent,
        }
