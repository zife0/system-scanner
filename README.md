# system-scanner

> Modular system monitoring and diagnostics toolkit.

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/status-active-success)

---

## ✨ Features

* CPU / Memory / Disk collectors
* Live monitoring dashboard
* Top process monitoring
* Doctor diagnostics mode
* JSON / Table / Rich output
* Export & reporting support
* Structured CLI architecture
* Modular and extensible design

---

## 🚀 Installation

```bash
git clone https://github.com/zife0/system-scanner.git

cd system-scanner

pip install -e .
```

---

## ⚡ Usage

### Scan CPU

```bash
system-scanner --cpu
```

### Scan Memory

```bash
system-scanner --memory
```

### Scan Disk

```bash
system-scanner --disk
```

### Rich Output

```bash
system-scanner --cpu --format rich
```

### Table Output

```bash
system-scanner --cpu --format table
```

### Live Dashboard

```bash
system-scanner --live
```

### Top Processes

```bash
system-scanner --top-processes
```

### Doctor Diagnostics

```bash
system-scanner --doctor
```

### Export Results

```bash
system-scanner --cpu --format json --export report.json
```

---

## 🧠 Architecture

The project is built around a modular collector system:

* Collectors handle data gathering
* Formatters handle output rendering
* CLI layer controls orchestration
* Utilities provide logging and terminal helpers

Designed to stay scalable, extensible, and production-friendly.

---

## 🧪 Tech Stack

* Python
* psutil
* Rich
* argparse

---

## 📌 Roadmap

* Network monitoring
* Watch mode
* Realtime graphs
* Alert system
* Plugin support

---

## 📄 License

MIT
