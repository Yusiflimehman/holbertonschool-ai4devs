# Performance Report

Benchmark of the three `LogAnalyzer` implementations (Python, JavaScript, Go) from `implementations/`.

## Metrics
- **Runtime (s):** wall-clock time of one complete run (start the program, read the log file, analyze every line, print the JSON result).
- **Memory (MB):** peak resident memory (RSS) of the process during the run.

## Results (1,000,000 log lines, 78 MB file)

| Language             | Runtime (s) | Memory (MB) |
|----------------------|-------------|-------------|
| Python 3.13          | 1.64        | 224         |
| JavaScript (Node 22) | 1.11        | 281         |
| Go 1.24              | 2.17        | 193         |

Values are the **median of 7 runs** after one warm-up run.

| Language             | Runtime min – max (s) | Memory min – max (MB) |
|----------------------|-----------------------|-----------------------|
| Python 3.13          | 1.52 – 1.84           | 224 – 224             |
| JavaScript (Node 22) | 1.00 – 1.45           | 277 – 285             |
| Go 1.24              | 2.11 – 2.24           | 192 – 315             |

All three programs returned **identical output** on this input:
`total_requests` 999800, `unique_visitors` 5000, `error_rate` 19.92, and the same `status_counts` (2xx 700973, 4xx 99844, 5xx 99350, other 99633).

## Results for smaller inputs (median of 7 runs)

| Lines   | Python (s / MB) | JavaScript (s / MB) | Go (s / MB)  |
|---------|-----------------|---------------------|--------------|
| 10,000  | 0.040 / 16      | 0.052 / 48          | 0.022 / 13   |
| 100,000 | 0.199 / 40      | 0.155 / 87          | 0.239 / 23   |

## Test Setup
- **Machine:** 2 vCPU Intel Xeon @ 2.10 GHz, 8 GB RAM, Linux (cloud sandbox).
- **Versions:** Python 3.13.18, Node.js v22.23.4, Go 1.24.7.
- **Go** was compiled first with `go build`, so compile time is not included.
- **Input:** a generated Apache-style log file (fixed random seed 42) with 5,000 distinct IP addresses, a mix of 2xx, 3xx, 4xx and 5xx statuses, and one corrupted line for every 5,000 lines.
- **Measuring:** a small Python script started each program as a child process, recorded wall-clock time with `time.perf_counter()`, and read the peak memory of the child with `resource.getrusage(RUSAGE_CHILDREN).ru_maxrss`.
- All programs read the whole file into memory first and then analyze the lines, as written in the implementations.

## Analysis
- **JavaScript was the fastest on large input** (1.11 s for 1M lines) but used the most memory (281 MB). Node starts slower on tiny inputs (0.052 s for 10,000 lines) because of its runtime start-up cost.
- **Python was in the middle** on runtime (1.64 s) and memory (224 MB), and it was the most consistent between runs.
- **Go was the slowest on the 1M-line input** (2.17 s) but used the least memory (193 MB) and was the fastest on small inputs (0.022 s for 10,000 lines), where start-up cost dominates. The program is compiled, so starting it is very cheap.
- The likely reason for Go's slower large-input time is its regular expression engine, which guarantees linear-time matching but is usually slower on a pattern like this one than the engines of Python and V8. We did not profile this, so it is a hypothesis.
- The large peak memory comes mostly from reading the entire 78 MB file and splitting it into a list of lines in all three versions. Go's single higher peak (315 MB) in one run is most likely caused by the timing of garbage collection.

## Limitations
- One machine, one input shape and one simple task. Results can change with other hardware, other log formats or other versions.
- The cloud sandbox has shared resources, so timings vary a little between runs (see the min – max table).
- We compared the implementations as written. Optimized versions (for example, reading the file line by line instead of loading it all) would use much less memory in every language.

## Conclusion
No language was best in every metric. JavaScript was fastest for a large file, Go used the least memory and started fastest, and Python was a balanced choice. All three give identical results, so the choice depends on the use case: Go for small, frequent runs and low memory, Node.js or Python when speed on big files or ease of development matters more.

## How to Reproduce
```bash
# Go binary
cd multi_language_code_generator/implementations/go && go build -o log_analyzer_go log_analyzer.go

# Run each implementation on a log file
python3 multi_language_code_generator/implementations/python/log_analyzer.py access.log
node multi_language_code_generator/implementations/javascript/log_analyzer.js access.log
./multi_language_code_generator/implementations/go/log_analyzer_go access.log
```
