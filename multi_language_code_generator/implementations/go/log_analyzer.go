package main

import (
	"encoding/json"
	"fmt"
	"os"
	"regexp"
	"strconv"
	"strings"
)

// ParsedLine is the structured data of one log line.
type ParsedLine struct {
	IP        string
	Timestamp string
	Request   string
	Status    int
	Bytes     int
}

// StatusCounts groups requests by HTTP status class.
type StatusCounts struct {
	C2xx  int `json:"2xx"`
	C4xx  int `json:"4xx"`
	C5xx  int `json:"5xx"`
	Other int `json:"other"`
}

// Result is the analysis output (same fields as the other languages).
type Result struct {
	TotalRequests  int          `json:"total_requests"`
	UniqueVisitors int          `json:"unique_visitors"`
	ErrorRate      float64      `json:"error_rate"`
	StatusCounts   StatusCounts `json:"status_counts"`
}

// LogAnalyzer parses combined Apache/Nginx log lines.
type LogAnalyzer struct {
	logPattern *regexp.Regexp
}

// NewLogAnalyzer creates an analyzer with the log line pattern.
func NewLogAnalyzer() *LogAnalyzer {
	return &LogAnalyzer{
		logPattern: regexp.MustCompile(
			`^(?P<ip>\S+)\s+\S+\s+\S+\s+\[(?P<timestamp>[^\]]+)\]\s+"(?P<request>[^"]*)"\s+(?P<status>\d{3})\s+(?P<bytes>\S+)`),
	}
}

// ParseLine parses a single log line. It returns nil for empty or invalid lines.
func (a *LogAnalyzer) ParseLine(line string) *ParsedLine {
	line = strings.TrimSpace(line)
	if line == "" {
		return nil
	}
	match := a.logPattern.FindStringSubmatch(line)
	if match == nil {
		return nil
	}
	data := map[string]string{}
	for i, name := range a.logPattern.SubexpNames() {
		if name != "" {
			data[name] = match[i]
		}
	}
	status, _ := strconv.Atoi(data["status"])
	bytes := 0
	if isDigits(data["bytes"]) {
		bytes, _ = strconv.Atoi(data["bytes"])
	}
	return &ParsedLine{
		IP:        data["ip"],
		Timestamp: data["timestamp"],
		Request:   data["request"],
		Status:    status,
		Bytes:     bytes,
	}
}

func isDigits(s string) bool {
	if s == "" {
		return false
	}
	for _, r := range s {
		if r < '0' || r > '9' {
			return false
		}
	}
	return true
}

// Analyze parses multiple log lines and generates statistical analysis.
func (a *LogAnalyzer) Analyze(lines []string) Result {
	totalRequests := 0
	uniqueVisitors := map[string]struct{}{}
	errorCount := 0
	counts := StatusCounts{}

	for _, line := range lines {
		parsed := a.ParseLine(line)
		if parsed == nil {
			continue
		}

		totalRequests++
		uniqueVisitors[parsed.IP] = struct{}{}

		status := parsed.Status
		switch {
		case status >= 200 && status < 300:
			counts.C2xx++
		case status >= 400 && status < 500:
			counts.C4xx++
			errorCount++
		case status >= 500 && status < 600:
			counts.C5xx++
			errorCount++
		default:
			counts.Other++
		}
	}

	errorRate := 0.0
	if totalRequests > 0 {
		errorRate = float64(errorCount) / float64(totalRequests) * 100.0
	}

	return Result{
		TotalRequests:  totalRequests,
		UniqueVisitors: len(uniqueVisitors),
		ErrorRate:      round2(errorRate),
		StatusCounts:   counts,
	}
}

// round2 rounds to 2 decimals exactly like Python's round(x, 2)
// (based on the exact binary value, ties go to the even digit).
func round2(x float64) float64 {
	v, _ := strconv.ParseFloat(strconv.FormatFloat(x, 'f', 2, 64), 64)
	return v
}

// Usage: go run log_analyzer.go <log_file>
func main() {
	if len(os.Args) != 2 {
		fmt.Fprintln(os.Stderr, "Usage: go run log_analyzer.go <log_file>")
		os.Exit(1)
	}
	content, err := os.ReadFile(os.Args[1])
	if err != nil {
		fmt.Fprintln(os.Stderr, err)
		os.Exit(1)
	}
	lines := strings.Split(strings.ReplaceAll(string(content), "\r\n", "\n"), "\n")
	out, _ := json.MarshalIndent(NewLogAnalyzer().Analyze(lines), "", "  ")
	fmt.Println(string(out))
}
