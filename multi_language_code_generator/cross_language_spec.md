# Cross-Language Specification - Log Analyzer

## Algorithm Description
Parse Web Server logs (Apache/Nginx access log format) and compute key analytical metrics including total requests, unique visitor count, status code distribution, and overall error rate.

## Inputs
- Log files in plain text format (.log or .txt).
- Standard line structure containing client IP, timestamp, HTTP request method, HTTP response status code, and response bytes.

## Outputs
- JSON object containing statistics: `total_requests`, `unique_visitors`, `error_rate`, and `status_counts`.

## Edge Cases
- Empty file (0 bytes).
- Malformed log entries (missing fields or invalid formatting).
- Large log files processed line-by-line to manage memory.
- All requests failing with 4xx/5xx status codes.
- Multiple duplicate requests from a single client IP.

## Test Cases

### Test Case 1: Standard Operational Log
- **Input:** `log_standard.txt` -> 100 requests (80 OK 2xx, 15 Client Error 4xx, 5 Server Error 5xx) from 25 unique IPs.
- **Expected Output:** `{"total_requests": 100, "unique_visitors": 25, "error_rate": 20.0, "status_counts": {"2xx": 80, "4xx": 15, "5xx": 5}}`

### Test Case 2: Empty Log File
- **Input:** `log_empty.txt` -> 0 requests.
- **Expected Output:** `{"total_requests": 0, "unique_visitors": 0, "error_rate": 0.0, "status_counts": {"2xx": 0, "4xx": 0, "5xx": 0}}`

### Test Case 3: Malformed Log Entries
- **Input:** `log_corrupted.txt` -> 5 valid lines, 3 corrupted lines.
- **Expected Output:** `{"total_requests": 5, "unique_visitors": 3, "error_rate": 0.0, "status_counts": {"2xx": 5}}`

### Test Case 4: High Error Rate Log
- **Input:** `log_errors.txt` -> 50 HTTP 500 errors from 1 unique IP.
- **Expected Output:** `{"total_requests": 50, "unique_visitors": 1, "error_rate": 100.0, "status_counts": {"5xx": 50}}`

### Test Case 5: Single Unique Visitor
- **Input:** `log_single_user.txt` -> 10 valid requests from IP 10.0.0.1.
- **Expected Output:** `{"total_requests": 10, "unique_visitors": 1, "error_rate": 0.0, "status_counts": {"2xx": 10}}`
