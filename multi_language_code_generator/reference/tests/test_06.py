import unittest
from multi_language_code_generator.reference.log_analyzer import LogAnalyzer

class Test06(unittest.TestCase):
    def test_unique_visitors(self):
        analyzer = LogAnalyzer()
        lines = [
            '10.0.0.1 - - [30/Mar/2026:10:00:00 +0000] "GET / HTTP/1.1" 200 100',
            '10.0.0.1 - - [30/Mar/2026:10:01:00 +0000] "GET /about HTTP/1.1" 200 100'
        ]
        result = analyzer.analyze(lines)
        self.assertEqual(result["unique_visitors"], 1)

if __name__ == "__main__":
    unittest.main()
