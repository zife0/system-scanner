import time

import psutil

from rich.console import Console
from rich.live import Live
from rich.table import Table


console = Console()


def build_table():
    table = Table(title="SYSTEM SCANNER LIVE")

    table.add_column("Metric", style="cyan")
    table.add_column("Value", style="green")

    cpu = psutil.cpu_percent()
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage("/")

    table.add_row("CPU Usage", f"{cpu}%")
    table.add_row("Memory Usage", f"{memory.percent}%")
    table.add_row("Disk Usage", f"{disk.percent}%")

    table.add_row("CPU Cores", str(psutil.cpu_count()))

    return table


def run_live_dashboard():
    with Live(build_table(), refresh_per_second=1, console=console) as live:
        while True:
            time.sleep(1)
            live.update(build_table())
