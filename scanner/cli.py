import argparse
import sys
from scanner.core import scan_system

def main():
    parser = argparse.ArgumentParser(description="System Scanner Tool")

    parser.add_argument("--system", action="store_true", help="Scan system info")
    parser.add_argument("--files", action="store_true", help="Count files in current directory")
    parser.add_argument("--output", type=str, default="scan_report.json", help="Output file name")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose mode")

    args = parser.parse_args()

    try:
        data = {}

        if args.system:
            result = scan_system(verbose=args.verbose)
            data["system"] = result

        if args.files:
            import os
            data["files_in_cwd"] = len(os.listdir("."))

        if not data:
            print("[!] No options selected. Use --help")
            return

        import json
        with open(args.output, "w") as f:
            f.write(json.dumps(data, indent=4))

        print(f"[✓] Report saved to {args.output}")

    except Exception as e:
        print(f"[✗] Error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
