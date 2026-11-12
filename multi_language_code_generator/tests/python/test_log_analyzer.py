import json
import os
import sys
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "implementations", "python"))

from log_analyzer import LogAnalyzer  # noqa: E402

with open(os.path.join(HERE, "..", "test_cases.json"), encoding="utf-8") as f:
    CASES = json.load(f)


def build_lines(case):
    lines = list(case["lines"])
    if "repeat" in case:
        lines += [case["repeat"]["line"]] * case["repeat"]["count"]
    return lines


class TestLogAnalyzer(unittest.TestCase):
    def test_shared_cases(self):
        for case in CASES:
            with self.subTest(case=case["name"]):
                result = LogAnalyzer().analyze(build_lines(case))
                self.assertEqual(result, case["expected"])

    def test_parse_line_valid(self):
        parsed = LogAnalyzer().parse_line(
            '192.168.1.2 - frank [10/Oct/2023:13:56:01 +0000] "POST /login HTTP/1.1" 302 -'
        )
        self.assertEqual(parsed["ip"], "192.168.1.2")
        self.assertEqual(parsed["status"], 302)
        self.assertEqual(parsed["bytes"], 0)

    def test_parse_line_invalid(self):
        self.assertIsNone(LogAnalyzer().parse_line(""))
        self.assertIsNone(LogAnalyzer().parse_line("not a log line"))


if __name__ == "__main__":
    unittest.main()
