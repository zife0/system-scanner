# system-scanner

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/status-active-success)

A modular command-line tool for inspecting system resources with clean architecture, composable collectors, and structured output.

> Designed for developers and system engineers who need a lightweight, extensible system inspection tool for automation and diagnostics.

---

## 🚀 Features

* Modular core architecture (separation of concerns)
* Pluggable collectors (CPU, extensible design)
* Multiple output formats (JSON, text)
* CLI interface with argument parsing
* Logging system with verbose mode
* Production-ready structure

---

## 💡 Use Cases

* Automation scripts for system monitoring
* Lightweight diagnostics tool
* Integration with CI/CD pipelines
* Debugging system performance issues

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/zife0/system-scanner.git
cd system-scanner
```

Install locally:

```bash
pip install -e .
```

---

## ⚙️ Usage

Run the scanner:

```bash
system-scanner --cpu
```

With JSON output:

```bash
system-scanner --cpu --format json
```

Enable verbose logging:

```bash
system-scanner --cpu --verbose
```

---

## 🖥️ CLI Preview

```bash
system-scanner --cpu
```

```text
CPU:
  usage_percent: 14.2
  cores: 8
```

---

## 📌 Example Command

```bash
system-scanner --cpu --format json --verbose
```

---

## 🧠 Architecture

```text
system_scanner/
├── core/
│   ├── scanner.py
│   └── collectors/
│       └── cpu.py
│
├── cli/
│   └── main.py
│
├── output/
│   └── formatters/
│       ├── base.py
│       ├── json_formatter.py
│       └── text_formatter.py
│
└── utils/
    └── logger.py
```

---

## 🧩 Design Philosophy

This project follows a modular and extensible architecture:

* Core logic is isolated from CLI
* Collectors act as independent plugins
* Output is abstracted via formatter system
* Designed for scalability and real-world usage

---

## 📄 License

MIT License
