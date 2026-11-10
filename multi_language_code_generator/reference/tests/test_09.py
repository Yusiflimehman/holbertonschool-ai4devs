import unittest
from multi_language_code_generator.reference.log_analyzer import LogAnalyzer

class Test09(unittest.TestCase):
    def test_dash_bytes(self):
        analyzer = LogAnalyzer()
        line = '192.168.1.1 - - [30/Mar/2026:10:15:30 +0000] "GET /download HTTP/1.1" 200 -'
        result = analyzer.parse_line(line)
        self.assertEqual(result["bytes"], 0)

if __name__ == "__main__":
    unittest.main()
