import argparse

from system_scanner.core.scanner import SystemScanner
from system_scanner.core.collectors.cpu import CPUCollector

from system_scanner.output.formatters.json_formatter import JSONFormatter
from system_scanner.output.formatters.text_formatter import TextFormatter

from system_scanner.utils.logger import setup_logger


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

    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Enable debug logging"
    )

    args = parser.parse_args()

    logger = setup_logger(args.verbose)

    logger.info("Starting system scan...")

    scanner = SystemScanner()

    if args.cpu:
        logger.debug("Registering CPU collector")
        scanner.register(CPUCollector())

    results = scanner.scan()

    logger.debug("Scan completed")

    if args.format == "json":
        formatter = JSONFormatter()
    else:
        formatter = TextFormatter()

    output = formatter.format(results)

    print(output)

    logger.info("Finished")


if __name__ == "__main__":
    main()
