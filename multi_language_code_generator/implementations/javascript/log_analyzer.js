const fs = require("fs");

// Rounds to 2 decimals exactly like Python's round(x, 2):
// based on the exact binary value, ties go to the even digit.
function round2(x) {
  const [intPart, fracPart] = x.toFixed(60).split(".");
  const rest = fracPart.slice(2);
  let n = BigInt(intPart + fracPart.slice(0, 2));
  const first = rest[0];
  const hasMore = /[1-9]/.test(rest.slice(1));
  if (first > "5" || (first === "5" && hasMore)) {
    n += 1n;
  } else if (first === "5" && n % 2n === 1n) {
    n += 1n;
  }
  return Number(n) / 100;
}

class LogAnalyzer {
  constructor() {
    // Regular expression pattern to parse combined Apache/Nginx log lines
    this.logPattern =
      /^(?<ip>\S+)\s+\S+\s+\S+\s+\[(?<timestamp>[^\]]+)\]\s+"(?<request>[^"]*)"\s+(?<status>\d{3})\s+(?<bytes>\S+)/;
  }

  // Parses a single log line into a structured object (or null).
  parseLine(line) {
    line = line.trim();
    if (!line) {
      return null;
    }
    const match = this.logPattern.exec(line);
    if (!match) {
      return null;
    }
    const data = match.groups;
    return {
      ip: data.ip,
      timestamp: data.timestamp,
      request: data.request,
      status: parseInt(data.status, 10),
      bytes: /^\d+$/.test(data.bytes) ? parseInt(data.bytes, 10) : 0,
    };
  }

  // Parses multiple log lines and generates statistical analysis.
  analyze(lines) {
    let totalRequests = 0;
    const uniqueVisitors = new Set();
    let errorCount = 0;
    const statusCounts = { "2xx": 0, "4xx": 0, "5xx": 0, other: 0 };

    for (const line of lines) {
      const parsed = this.parseLine(line);
      if (parsed === null) {
        continue;
      }

      totalRequests += 1;
      uniqueVisitors.add(parsed.ip);

      const status = parsed.status;
      if (status >= 200 && status < 300) {
        statusCounts["2xx"] += 1;
      } else if (status >= 400 && status < 500) {
        statusCounts["4xx"] += 1;
        errorCount += 1;
      } else if (status >= 500 && status < 600) {
        statusCounts["5xx"] += 1;
        errorCount += 1;
      } else {
        statusCounts.other += 1;
      }
    }

    const errorRate = totalRequests > 0 ? (errorCount / totalRequests) * 100.0 : 0.0;

    return {
      total_requests: totalRequests,
      unique_visitors: uniqueVisitors.size,
      error_rate: round2(errorRate),
      status_counts: statusCounts,
    };
  }
}

module.exports = { LogAnalyzer };

// Usage: node log_analyzer.js <log_file>
if (require.main === module) {
  if (process.argv.length !== 3) {
    console.error("Usage: node log_analyzer.js <log_file>");
    process.exit(1);
  }
  const lines = fs.readFileSync(process.argv[2], "utf8").split(/\r?\n/);
  console.log(JSON.stringify(new LogAnalyzer().analyze(lines), null, 2));
}
