# Cross-Language Specification - Log Analyzer Engine

## Algorithm Description
The Log Analyzer Engine parses standard Web Server log files (such as Apache/Nginx combined access log format), calculates key performance metrics, and extracts statistical insights including total requests, unique visitors, response status distribution, and error rates.

## Input Format
- **Format:** Plain text log file (.log or .txt).
- **Line Structure:** Standard combined log format containing string tokens: `IP_ADDRESS IDENT USER [TIMESTAMP] "METHOD REQUEST HTTP_VER" STATUS BYTES`
- **Example Entry:** `192.168.1.1 - - [30/Mar/2026:10:15:30 +0000] "GET /api/v1/users HTTP/1.1" 200 512`

## Output Format
- **Format:** JSON Object containing structured analytical statistics.
- **Fields:**
  - `total_requests` (integer): Total number of valid parsed log entries.
  - `unique_visitors` (integer): Count of unique IP addresses.
  - `error_rate` (float): Percentage of HTTP 4xx and 5xx responses (0.00 to 100.00).
  - `status_counts` (object): Map of status code groups (e.g., `2xx`, `4xx`, `5xx`).

## Edge Cases
1. **Empty File:** Log file exists but contains 0 bytes.
2. **Malformed Lines:** Missing IP, corrupted timestamp, or truncated HTTP request string.
3. **Large File Stream:** Handling high volume files without loading entire content into memory at once.
4. **All Failing Requests:** Logs containing only 404 or 500 status codes (error rate should be 100%).
5. **Duplicate Visitor IPs:** Multiple identical requests from a single client IP address.

## Test Cases

### Test Case 1: Standard Operational Log
- **Input:** `log_standard.txt` (100 total requests, 80 HTTP 200s, 15 HTTP 404s, 5 HTTP 500s from 25 unique IPs)
- **Expected Output:**
  ```json
  {
    "total_requests": 100,
    "unique_visitors": 25,
    "error_rate": 20.0,
    "status_counts": { "2xx": 80, "4xx": 15, "5xx": 5 }
  }
