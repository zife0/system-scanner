from system_scanner.output.formatters.base import Formatter


class TextFormatter(Formatter):
    def format(self, data):
        output = ""

        for section, values in data.items():
            output += f"{section.upper()}:\n"

            for key, value in values.items():
                output += f"  {key}: {value}\n"

        return output
