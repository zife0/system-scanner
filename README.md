# System Scanner

A lightweight CLI tool for scanning system environments and collecting structured data for analysis.

---

## Features

- System information gathering
- Environment inspection
- JSON report generation
- Command-line execution

---

## Installation

pip install -e .

---

## Usage

scanner --verbose

---

## Output

The tool generates a JSON report file:

scan_report.json

---

## Example Output

{
  "system": "Windows",
  "node": "DESKTOP-123",
  "release": "10",
  "processor": "Intel64 Family",
  "files_in_cwd": 5
}

---

## Project Structure

scanner/
  __init__.py
  __main__.py
  cli.py
  core.py

---

## Notes

- Built for understanding system behavior and structure
- Designed to stay simple and modular
