import argparse
from scanner.core import scan_system

def main():
    parser = argparse.ArgumentParser(description="System Scanner Tool")

    parser.add_argument(
        "--output",
        type=str,
        default="scan_report.json",
        help="Output file name"
    )

    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Enable verbose mode"
    )

    args = parser.parse_args()

    result = scan_system(verbose=args.verbose)

    with open(args.output, "w") as f:
        f.write(result)

    print(f"Report saved to {args.output}")

if __name__ == "__main__":
    main()
