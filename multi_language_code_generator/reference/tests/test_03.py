import unittest
from multi_language_code_generator.reference.log_analyzer import LogAnalyzer

class Test03(unittest.TestCase):
    def test_corrupted_lines(self):
        analyzer = LogAnalyzer()
        lines = ['192.168.1.1 - - [30/Mar/2026:10:15:30 +0000] "GET /index.html HTTP/1.1" 200 1024', 'INVALID']
        result = analyzer.analyze(lines)
        self.assertEqual(result["total_requests"], 1)

if __name__ == "__main__":
    unittest.main()
