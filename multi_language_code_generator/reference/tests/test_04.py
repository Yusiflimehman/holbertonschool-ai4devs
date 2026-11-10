import unittest
from multi_language_code_generator.reference.log_analyzer import LogAnalyzer

class Test04(unittest.TestCase):
    def test_4xx_client_error(self):
        analyzer = LogAnalyzer()
        lines = ['192.168.1.2 - - [30/Mar/2026:10:15:30 +0000] "GET /missing HTTP/1.1" 404 128']
        result = analyzer.analyze(lines)
        self.assertEqual(result["status_counts"]["4xx"], 1)

if __name__ == "__main__":
    unittest.main()
