import unittest
from multi_language_code_generator.reference.log_analyzer import LogAnalyzer

class Test07(unittest.TestCase):
    def test_error_rate(self):
        analyzer = LogAnalyzer()
        lines = [
            '10.0.0.1 - - [30/Mar/2026:10:00:00 +0000] "GET / HTTP/1.1" 200 100',
            '10.0.0.2 - - [30/Mar/2026:10:01:00 +0000] "GET /404 HTTP/1.1" 404 50'
        ]
        result = analyzer.analyze(lines)
        self.assertEqual(result["error_rate"], 50.0)

if __name__ == "__main__":
    unittest.main()
