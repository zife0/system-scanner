import time
import platform
import socket

import psutil

from rich.console import Console
from rich.live import Live
from rich.table import Table


console = Console()


def build_table():
    table = Table(title="SYSTEM SCANNER LIVE", border_style="cyan")

    table.add_column("Metric", style="cyan", justify="left")
    table.add_column("Value", style="green", justify="right")

    cpu = psutil.cpu_percent()
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage("/")

    uptime = time.time() - psutil.boot_time()

    cpu_bar = "█" * int(cpu / 5)
    memory_bar = "█" * int(memory.percent / 5)
    disk_bar = "█" * int(disk.percent / 5)

    table.add_row("Hostname", socket.gethostname())
    table.add_row("Platform", platform.system())

    table.add_row(
        "CPU Usage",
        f"{cpu}% {cpu_bar}"
    )

    table.add_row(
        "Memory Usage",
        f"{memory.percent}% {memory_bar}"
    )

    table.add_row(
        "Disk Usage",
        f"{disk.percent}% {disk_bar}"
    )

    table.add_row("CPU Cores", str(psutil.cpu_count()))
    table.add_row("Uptime", f"{int(uptime // 60)} min")

    return table


def run_live_dashboard():
    with Live(build_table(), refresh_per_second=1, console=console) as live:
        while True:
            time.sleep(1)
            live.update(build_table())
