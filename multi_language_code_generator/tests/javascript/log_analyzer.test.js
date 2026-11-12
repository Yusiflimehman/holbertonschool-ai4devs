const test = require("node:test");
const assert = require("node:assert");
const fs = require("fs");
const path = require("path");
const { LogAnalyzer } = require("../../implementations/javascript/log_analyzer.js");

const CASES = JSON.parse(
  fs.readFileSync(path.join(__dirname, "..", "test_cases.json"), "utf8")
);

function buildLines(testCase) {
  const lines = [...testCase.lines];
  if (testCase.repeat) {
    for (let i = 0; i < testCase.repeat.count; i++) {
      lines.push(testCase.repeat.line);
    }
  }
  return lines;
}

for (const testCase of CASES) {
  test(`shared case: ${testCase.name}`, () => {
    const result = new LogAnalyzer().analyze(buildLines(testCase));
    assert.deepStrictEqual(result, testCase.expected);
  });
}

test("parseLine parses a valid line", () => {
  const parsed = new LogAnalyzer().parseLine(
    '192.168.1.2 - frank [10/Oct/2023:13:56:01 +0000] "POST /login HTTP/1.1" 302 -'
  );
  assert.strictEqual(parsed.ip, "192.168.1.2");
  assert.strictEqual(parsed.status, 302);
  assert.strictEqual(parsed.bytes, 0);
});

test("parseLine returns null for invalid lines", () => {
  assert.strictEqual(new LogAnalyzer().parseLine(""), null);
  assert.strictEqual(new LogAnalyzer().parseLine("not a log line"), null);
});
