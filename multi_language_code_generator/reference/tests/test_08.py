import unittest
from multi_language_code_generator.reference.log_analyzer import LogAnalyzer

class Test08(unittest.TestCase):
    def test_empty_strings(self):
        analyzer = LogAnalyzer()
        lines = ["   ", ""]
        result = analyzer.analyze(lines)
        self.assertEqual(result["total_requests"], 0)

if __name__ == "__main__":
    unittest.main()
