import re

class LogAnalyzer:
    def __init__(self):
        # Regular expression pattern to parse combined Apache/Nginx log lines
        self.log_pattern = re.compile(
            r'^(?P<ip>\S+)\s+\S+\s+\S+\s+\[(?P<timestamp>[^\]]+)\]\s+"(?P<request>[^"]*)"\s+(?P<status>\d{3})\s+(?P<bytes>\S+)'
        )

    def parse_line(self, line: str) -> dict:
        """Parses a single log line into structured dictionary data."""
        line = line.strip()
        if not line:
            return None
        match = self.log_pattern.match(line)
        if not match:
            return None
        data = match.groupdict()
        return {
            "ip": data["ip"],
            "timestamp": data["timestamp"],
            "request": data["request"],
            "status": int(data["status"]),
            "bytes": int(data["bytes"]) if data["bytes"].isdigit() else 0
        }

    def analyze(self, lines: list) -> dict:
        """Parses multiple log lines and generates comprehensive statistical analysis."""
        total_requests = 0
        unique_visitors = set()
        error_count = 0
        status_counts = {"2xx": 0, "4xx": 0, "5xx": 0, "other": 0}

        for line in lines:
            parsed = self.parse_line(line)
            if parsed is None:
                continue

            total_requests += 1
            unique_visitors.add(parsed["ip"])

            status = parsed["status"]
            if 200 <= status < 300:
                status_counts["2xx"] += 1
            elif 400 <= status < 500:
                status_counts["4xx"] += 1
                error_count += 1
            elif 500 <= status < 600:
                status_counts["5xx"] += 1
                error_count += 1
            else:
                status_counts["other"] += 1

        error_rate = (error_count / total_requests * 100.0) if total_requests > 0 else 0.0

        return {
            "total_requests": total_requests,
            "unique_visitors": len(unique_visitors),
            "error_rate": round(error_rate, 2),
            "status_counts": status_counts
        }
