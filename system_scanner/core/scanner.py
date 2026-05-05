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
