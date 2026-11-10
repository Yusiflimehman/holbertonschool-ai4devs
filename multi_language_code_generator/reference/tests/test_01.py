import unittest
from multi_language_code_generator.reference.log_analyzer import LogAnalyzer

class Test01(unittest.TestCase):
    def test_standard_valid_line(self):
        analyzer = LogAnalyzer()
        line = '192.168.1.1 - - [30/Mar/2026:10:15:30 +0000] "GET /index.html HTTP/1.1" 200 1024'
        result = analyzer.parse_line(line)
        self.assertIsNotNone(result)
        self.assertEqual(result["ip"], "192.168.1.1")
        self.assertEqual(result["status"], 200)

if __name__ == "__main__":
    unittest.main()
