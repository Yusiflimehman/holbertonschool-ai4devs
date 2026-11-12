# Reflection

Translating the Log Analyzer from Python into JavaScript and Go looked simple at first. The program is short, and the logic (parse a line, count statuses, calculate an error rate) is the same in every language. The real work was making the three versions behave identically, not just look similar.

The hardest part was a small detail: rounding. Python's `round()` sends exact ties to the even digit, so 3.125 becomes 3.12. JavaScript and Go rounded the same value up to 3.13. When I compared the languages over more than 125,000 combinations of requests and errors, 204 results were different. A normal test with a few log lines would never have found this. It only appeared when one error occurred in 32 requests. After fixing it, all three languages matched in every case. This taught me that a translation must reproduce behavior, including edge cases, and that "it runs and looks right" is not proof.

Working with AI was fast, but it needed checking. The assistant produced all three translations quickly and ran them against the same log files. Still, the first test script had a bug and the automatic reviewer later marked the Go rounding as incorrect, even though a test with Python's expected values proved it was right. I learned to ask for evidence, not just a conclusion, and to answer a wrong review with a test instead of an argument.

The shared test file was the most useful decision. One JSON file with the expected results was used by the Python, JavaScript and Go tests, so every language had to pass exactly the same cases. It also made new bugs easy to see.

The benchmark surprised me. Go is often expected to be the fastest, but on one million lines it was the slowest (2.17 s) while using the least memory (193 MB). JavaScript was the fastest (1.11 s). The most likely reason is the regular expression engine, but I did not profile it, so I treat that as a hypothesis. It reminded me that the fastest language on paper is not always the fastest for a specific task.

Next time I would write the shared tests before translating, test rounding and number conversions from the start, and run a benchmark with more than one input size earlier. I would also read automatic feedback carefully and check it against evidence before changing working code.
