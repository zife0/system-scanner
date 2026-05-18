import psutil

from rich.console import Console
from rich.table import Table


console = Console()


def show_top_processes(limit=10):
    table = Table(title="TOP PROCESSES", border_style="red")

    table.add_column("PID", style="cyan")
    table.add_column("Name", style="green")
    table.add_column("CPU %", style="yellow")
    table.add_column("Memory %", style="magenta")

    processes = []

    for process in psutil.process_iter(
        ["pid", "name", "cpu_percent", "memory_percent"]
    ):
        try:
            processes.append(process.info)
        except Exception:
            continue

    processes = sorted(
        processes,
        key=lambda p: p["cpu_percent"],
        reverse=True
    )

    for process in processes[:limit]:
        table.add_row(
            str(process["pid"]),
            str(process["name"]),
            f"{process['cpu_percent']:.1f}",
            f"{process['memory_percent']:.1f}"
        )

    console.print(table)
