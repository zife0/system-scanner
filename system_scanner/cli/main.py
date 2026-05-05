import argparse

from system_scanner.core.scanner import SystemScanner
from system_scanner.core.collectors.cpu import CPUCollector

from system_scanner.output.formatters.json_formatter import JSONFormatter
from system_scanner.output.formatters.text_formatter import TextFormatter


def main():
    parser = argparse.ArgumentParser(
        description="System Scanner CLI Tool"
    )

    parser.add_argument("--cpu", action="store_true", help="Scan CPU")

    parser.add_argument(
        "--format",
        choices=["json", "text"],
        default="text",
        help="Output format"
    )

    args = parser.parse_args()

    scanner = SystemScanner()

    if args.cpu:
        scanner.register(CPUCollector())

    results = scanner.scan()

    # اختيار الفورماتر
    if args.format == "json":
        formatter = JSONFormatter()
    else:
        formatter = TextFormatter()

    output = formatter.format(results)

    print(output)


if __name__ == "__main__":
    main()
