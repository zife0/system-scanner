import argparse

from system_scanner.core.scanner import SystemScanner
from system_scanner.core.collectors.cpu import CPUCollector


def main():
    parser = argparse.ArgumentParser(
        description="System Scanner CLI Tool"
    )

    parser.add_argument(
        "--cpu",
        action="store_true",
        help="Scan CPU information"
    )

    args = parser.parse_args()

    scanner = SystemScanner()

    if args.cpu:
        scanner.register(CPUCollector())

    results = scanner.scan()

    print(results)


if __name__ == "__main__":
    main()
