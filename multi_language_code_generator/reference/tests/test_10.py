import unittest
from multi_language_code_generator.reference.log_analyzer import LogAnalyzer

class Test10(unittest.TestCase):
    def test_3xx_redirect(self):
        analyzer = LogAnalyzer()
        lines = ['192.168.1.1 - - [30/Mar/2026:10:15:30 +0000] "GET /old HTTP/1.1" 301 0']
        result = analyzer.analyze(lines)
        self.assertEqual(result["status_counts"]["other"], 1)

if __name__ == "__main__":
    unittest.main()
