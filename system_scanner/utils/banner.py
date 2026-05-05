from rich.console import Console
from rich.panel import Panel
from rich.text import Text


def show_banner():
    console = Console()

    title = Text("SYSTEM SCANNER", style="bold cyan")
    subtitle = Text("Modular CLI System Inspection Tool", style="green")

    panel = Panel.fit(
        f"{title}\n{subtitle}",
        border_style="blue"
    )

    console.print(panel)
