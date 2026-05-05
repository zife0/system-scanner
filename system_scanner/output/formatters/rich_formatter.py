from rich.console import Console
from rich.table import Table

from system_scanner.output.formatters.base import Formatter


class RichFormatter(Formatter):
    def format(self, data):
        console = Console()

        for section, values in data.items():
            table = Table(title=section.upper())

            table.add_column("Metric", style="cyan", no_wrap=True)
            table.add_column("Value", style="green")

            for key, value in values.items():
                table.add_row(str(key), str(value))

            console.print(table)

        return ""
