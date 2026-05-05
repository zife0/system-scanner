from system_scanner.output.formatters.base import Formatter


class TableFormatter(Formatter):
    def format(self, data):
        lines = []

        for section, values in data.items():
            lines.append(f"\n[{section.upper()}]")
            lines.append("-" * 30)

            for key, value in values.items():
                lines.append(f"{key:<20} | {value}")

        return "\n".join(lines)
