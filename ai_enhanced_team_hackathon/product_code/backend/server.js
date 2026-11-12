// Zero-dependency HTTP server (Node.js built-ins only).
// Run: node backend/server.js  ->  open http://localhost:3000

const http = require("http");
const fs = require("fs");
const path = require("path");
const { summarize } = require("./summarizer");

const PORT = process.env.PORT || 3000;
const MAX_BODY_BYTES = 200 * 1024; // 200 KB limit for the transcript request
const FRONTEND_FILE = path.join(__dirname, "..", "frontend", "index.html");

function sendJson(res, status, data) {
  res.writeHead(status, { "Content-Type": "application/json; charset=utf-8" });
  res.end(JSON.stringify(data));
}

function readBody(req) {
  return new Promise((resolve, reject) => {
    let size = 0;
    const chunks = [];
    req.on("data", (chunk) => {
      size += chunk.length;
      if (size > MAX_BODY_BYTES) {
        reject(new Error("Request body too large"));
        req.destroy();
        return;
      }
      chunks.push(chunk);
    });
    req.on("end", () => resolve(Buffer.concat(chunks).toString("utf8")));
    req.on("error", reject);
  });
}

const server = http.createServer(async (req, res) => {
  // Frontend page
  if (req.method === "GET" && (req.url === "/" || req.url === "/index.html")) {
    fs.readFile(FRONTEND_FILE, (err, content) => {
      if (err) return sendJson(res, 500, { error: "Frontend file not found" });
      res.writeHead(200, { "Content-Type": "text/html; charset=utf-8" });
      res.end(content);
    });
    return;
  }

  // Health check
  if (req.method === "GET" && req.url === "/api/health") {
    return sendJson(res, 200, { status: "ok" });
  }

  // Main endpoint: POST /api/summarize  { "transcript": "..." }
  if (req.method === "POST" && req.url === "/api/summarize") {
    try {
      const raw = await readBody(req);
      let body;
      try {
        body = JSON.parse(raw);
      } catch {
        return sendJson(res, 400, { error: "Invalid JSON" });
      }
      const result = summarize(body.transcript);
      return sendJson(res, 200, result);
    } catch (err) {
      const status = err.message === "Request body too large" ? 413 : 400;
      return sendJson(res, status, { error: err.message });
    }
  }

  sendJson(res, 404, { error: "Not found" });
});

if (require.main === module) {
  server.listen(PORT, () => console.log(`Server running at http://localhost:${PORT}`));
}

module.exports = server;
