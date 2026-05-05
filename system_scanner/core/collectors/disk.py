import psutil


class DiskCollector:
    name = "disk"

    def collect(self):
        disk = psutil.disk_usage("/")

        return {
            "total": disk.total,
            "used": disk.used,
            "free": disk.free,
            "usage_percent": disk.percent,
        }
