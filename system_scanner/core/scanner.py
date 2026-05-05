from system_scanner.core.collectors.cpu import CPUCollector


class SystemScanner:
    def __init__(self):
        self.collectors = []

    def register(self, collector):
        self.collectors.append(collector)

    def scan(self):
        results = {}
        for collector in self.collectors:
            results[collector.name] = collector.collect() or {}
        return results


# 🔥 تشغيل تجريبي
if __name__ == "__main__":
    scanner = SystemScanner()
    scanner.register(CPUCollector())

    results = scanner.scan()
    print(results)
