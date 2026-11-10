import unittest
from multi_language_code_generator.reference.log_analyzer import LogAnalyzer

class Test02(unittest.TestCase):
    def test_empty_file_list(self):
        analyzer = LogAnalyzer()
        result = analyzer.analyze([])
        self.assertEqual(result["total_requests"], 0)
        self.assertEqual(result["unique_visitors"], 0)

if __name__ == "__main__":
    unittest.main()
