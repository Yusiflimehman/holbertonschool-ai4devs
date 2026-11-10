import unittest
from multi_language_code_generator.reference.log_analyzer import LogAnalyzer

class TestLogAnalyzer(unittest.TestCase):
    def setUp(self):
        self.analyzer = LogAnalyzer()

    def test_01_standard_valid_line(self):
        line = '192.168.1.1 - - [30/Mar/2026:10:15:30 +0000] "GET /index.html HTTP/1.1" 200 1024'
        result = self.analyzer.parse_line(line)
        self.assertIsNotNone(result)
        self.assertEqual(result["ip"], "192.168.1.1")
        self.assertEqual(result["status"], 200)

    def test_02_empty_file_list(self):
        result = self.analyzer.analyze([])
        self.assertEqual(result["total_requests"], 0)
        self.assertEqual(result["unique_visitors"], 0)
        self.assertEqual(result["error_rate"], 0.0)

    def test_03_corrupted_and_malformed_lines(self):
        lines = [
            '192.168.1.1 - - [30/Mar/2026:10:15:30 +0000] "GET /index.html HTTP/1.1" 200 1024',
            'INVALID LOG LINE HERE',
            '10.0.0.1 missing bracket "GET / HTTP/1.1" 200 500'
        ]
        result = self.analyzer.analyze(lines)
        self.assertEqual(result["total_requests"], 1)

    def test_04_4xx_client_error(self):
        lines = ['192.168.1.2 - - [30/Mar/2026:10:15:30 +0000] "GET /missing HTTP/1.1" 404 128']
        result = self.analyzer.analyze(lines)
        self.assertEqual(result["status_counts"]["4xx"], 1)
        self.assertEqual(result["error_rate"], 100.0)

    def test_05_5xx_server_error(self):
        lines = ['192.168.1.3 - - [30/Mar/2026:10:15:30 +0000] "POST /api HTTP/1.1" 500 0']
        result = self.analyzer.analyze(lines)
        self.assertEqual(result["status_counts"]["5xx"], 1)
        self.assertEqual(result["error_rate"], 100.0)

    def test_06_unique_visitor_counting(self):
        lines = [
            '10.0.0.1 - - [30/Mar/2026:10:00:00 +0000] "GET / HTTP/1.1" 200 100',
            '10.0.0.1 - - [30/Mar/2026:10:01:00 +0000] "GET /about HTTP/1.1" 200 100',
            '10.0.0.2 - - [30/Mar/2026:10:02:00 +0000] "GET / HTTP/1.1" 200 100'
        ]
        result = self.analyzer.analyze(lines)
        self.assertEqual(result["total_requests"], 3)
        self.assertEqual(result["unique_visitors"], 2)

    def test_07_mixed_status_codes_and_error_rate(self):
        lines = [
            '10.0.0.1 - - [30/Mar/2026:10:00:00 +0000] "GET / HTTP/1.1" 200 100',
            '10.0.0.2 - - [30/Mar/2026:10:01:00 +0000] "GET /404 HTTP/1.1" 404 50',
            '10.0.0.3 - - [30/Mar/2026:10:02:00 +0000] "GET /500 HTTP/1.1" 500 50',
            '10.0.0.4 - - [30/Mar/2026:10:03:00 +0000] "GET /201 HTTP/1.1" 201 100'
        ]
        result = self.analyzer.analyze(lines)
        self.assertEqual(result["total_requests"], 4)
        self.assertEqual(result["error_rate"], 50.0)

    def test_08_empty_lines_and_whitespace(self):
        lines = ["   ", "", "\n"]
        result = self.analyzer.analyze(lines)
        self.assertEqual(result["total_requests"], 0)

    def test_09_non_numeric_bytes(self):
        line = '192.168.1.1 - - [30/Mar/2026:10:15:30 +0000] "GET /download HTTP/1.1" 200 -'
        result = self.analyzer.parse_line(line)
        self.assertEqual(result["bytes"], 0)

    def test_10_redirect_3xx_status(self):
        lines = ['192.168.1.1 - - [30/Mar/2026:10:15:30 +0000] "GET /old HTTP/1.1" 301 0']
        result = self.analyzer.analyze(lines)
        self.assertEqual(result["status_counts"]["other"], 1)
        self.assertEqual(result["error_rate"], 0.0)

if __name__ == "__main__":
    unittest.main()
