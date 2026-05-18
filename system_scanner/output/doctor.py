import psutil

from rich.console import Console
from rich.table import Table


console = Console()


def get_status(value):
    if value < 70:
        return "[green]OK[/green]"
    elif value < 90:
        return "[yellow]WARNING[/yellow]"
    return "[red]CRITICAL[/red]"


def run_doctor():
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage("/")

    table = Table(title="SYSTEM DOCTOR", border_style="cyan")

    table.add_column("Check", style="cyan")
    table.add_column("Usage", style="green")
    table.add_column("Status")

    table.add_row("CPU", f"{cpu}%", get_status(cpu))
    table.add_row("Memory", f"{memory.percent}%", get_status(memory.percent))
    table.add_row("Disk", f"{disk.percent}%", get_status(disk.percent))

    console.print(table)

    if cpu >= 90 or memory.percent >= 90 or disk.percent >= 90:
        console.print("[red]Critical system pressure detected.[/red]")
    elif cpu >= 70 or memory.percent >= 70 or disk.percent >= 70:
        console.print("[yellow]System usage is elevated. Monitor performance.[/yellow]")
    else:
        console.print("[green]System looks healthy.[/green]")
