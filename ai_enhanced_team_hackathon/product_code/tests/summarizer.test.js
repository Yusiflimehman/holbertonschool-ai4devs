const test = require("node:test");
const assert = require("node:assert");
const http = require("http");
const { summarize } = require("../backend/summarizer");
const server = require("../backend/server");

const SAMPLE = `Anna: Welcome everyone to the weekly sync. Today we review the website launch. We decided to launch on 2026-12-01. Bob will prepare the release notes by Friday. Carol should test the payment page before tomorrow. We agreed to use the new logo.`;

test("summarize returns summary, decisions and action items", () => {
  const result = summarize(SAMPLE);
  assert.ok(result.summary.length > 0);
  assert.strictEqual(result.decisions.length, 2);
  assert.strictEqual(result.actionItems.length, 2);
});

test("action items contain owner and due date", () => {
  const { actionItems } = summarize(SAMPLE);
  const bob = actionItems.find((a) => a.owner === "Bob");
  assert.ok(bob);
  assert.strictEqual(bob.due.toLowerCase(), "friday");
  assert.strictEqual(bob.status, "open");
});

test("summarize throws on empty input", () => {
  assert.throws(() => summarize("   "), /non-empty/);
});

function post(port, body) {
  return new Promise((resolve, reject) => {
    const req = http.request(
      { port, method: "POST", path: "/api/summarize", headers: { "Content-Type": "application/json" } },
      (res) => {
        let data = "";
        res.on("data", (c) => (data += c));
        res.on("end", () => resolve({ status: res.statusCode, body: JSON.parse(data) }));
      }
    );
    req.on("error", reject);
    req.end(body);
  });
}

test("POST /api/summarize works and validates input", async () => {
  await new Promise((r) => server.listen(0, r));
  const port = server.address().port;
  try {
    const ok = await post(port, JSON.stringify({ transcript: SAMPLE }));
    assert.strictEqual(ok.status, 200);
    assert.ok(Array.isArray(ok.body.actionItems));

    const empty = await post(port, JSON.stringify({ transcript: "" }));
    assert.strictEqual(empty.status, 400);

    const bad = await post(port, "not json");
    assert.strictEqual(bad.status, 400);
  } finally {
    server.close();
  }
});
