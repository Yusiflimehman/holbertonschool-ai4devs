import unittest
from multi_language_code_generator.reference.log_analyzer import LogAnalyzer

class Test05(unittest.TestCase):
    def test_5xx_server_error(self):
        analyzer = LogAnalyzer()
        lines = ['192.168.1.3 - - [30/Mar/2026:10:15:30 +0000] "POST /api HTTP/1.1" 500 0']
        result = analyzer.analyze(lines)
        self.assertEqual(result["status_counts"]["5xx"], 1)

if __name__ == "__main__":
    unittest.main()
