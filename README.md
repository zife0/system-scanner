# System Scanner

A lightweight CLI tool for scanning system environments and collecting structured data for analysis.

---

## Purpose

This tool is designed to inspect system environments and provide structured output for analysis and automation workflows.

---

## Features

- System information gathering
- Environment inspection
- JSON report generation
- Command-line execution
- Multiple output formats (JSON / TXT)
- Pretty terminal output

---

## Installation

pip install -e .

---

## Usage

Run system scan:
scanner --system

Count files:
scanner --files

Full scan with output file:
scanner --system --files

Pretty output (no file):
scanner --system --pretty

Custom output format:
scanner --system --format txt

Verbose mode:
scanner --system --verbose

---

## Output

The tool generates a JSON report file:

scan_report.json

---

## Example Output

{
  "timestamp": "2025-01-01T12:00:00",
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
