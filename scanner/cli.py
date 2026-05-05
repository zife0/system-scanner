import argparse
import sys
import logging
from scanner.core import scan_system

def setup_logger(verbose=False):
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(
        level=level,
        format="%(levelname)s: %(message)s"
    )

def main():
    parser = argparse.ArgumentParser(description="System Scanner Tool")

    parser.add_argument("--system", action="store_true", help="Scan system info")
    parser.add_argument("--files", action="store_true", help="Count files in current directory")
    parser.add_argument("--output", type=str, default="scan_report.json", help="Output file name")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose mode")

    args = parser.parse_args()

    setup_logger(args.verbose)

    try:
        data = {}

        if args.system:
            logging.info("Scanning system info...")
            result = scan_system(verbose=args.verbose)
            import json
            data["system"] = json.loads(result)

        if args.files:
            import os
            logging.info("Counting files in current directory...")
            data["files_in_cwd"] = len(os.listdir("."))

        if not data:
            logging.warning("No options selected. Use --help")
            return

        import json
        with open(args.output, "w") as f:
            f.write(json.dumps(data, indent=4))

        logging.info(f"Report saved to {args.output}")

    except Exception as e:
        logging.error(f"Error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
