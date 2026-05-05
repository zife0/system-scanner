import argparse
import sys
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

    try:
        result = scan_system(verbose=args.verbose)

        with open(args.output, "w") as f:
            f.write(result)

        print(f"[✓] Report saved to {args.output}")

    except Exception as e:
        print(f"[✗] Error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
