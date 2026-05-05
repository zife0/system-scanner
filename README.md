# system-scanner

A modular command-line tool for inspecting system resources with clean architecture, composable collectors, and structured output.

---

## 🚀 Features

* Modular core architecture (separation of concerns)
* Pluggable collectors (CPU, extensible design)
* Multiple output formats (JSON, text)
* CLI interface with argument parsing
* Logging system with verbose mode
* Production-ready structure

---

## 📦 Installation

Clone the repository:

```
git clone https://github.com/zife0/system-scanner.git
cd system-scanner
```

Install locally:

```
pip install -e .
```

---

## ⚙️ Usage

Run the scanner:

```
system-scanner --cpu
```

With JSON output:

```
system-scanner --cpu --format json
```

Enable verbose logging:

```
system-scanner --cpu --verbose
```

---

## 🧠 Architecture

```
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

## 📌 Example Output

### Text

```
CPU:
  usage_percent: 14.2
  cores: 8
```

### JSON

```
{
    "cpu": {
        "usage_percent": 14.2,
        "cores": 8
    }
}
```

---

## 🛠️ Future Improvements

* Memory and disk collectors
* Table/pretty output
* Config file support
* Plugin auto-discovery
* Cross-platform enhancements

---

## 📄 License

MIT License
