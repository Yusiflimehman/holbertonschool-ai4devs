# AI Dev Log

AI assistant used: Claude (Anthropic). All entries below describe real interactions during the implementation of the AI Meeting Notes Summarizer MVP.

## Entry 1: Project structure

### Prompt
Implementation task: organize code in `product_code/` with `/frontend/`, `/backend/` and `/tests/`. Build at least one frontend screen and one backend API endpoint for the AI Meeting Notes Summarizer (paste transcript, get summary, decisions and action items).

### AI Output
Proposed a zero-dependency Node.js project (built-in `http` module only) with this layout:
- `backend/summarizer.js` (summarizing logic)
- `backend/server.js` (HTTP server, `POST /api/summarize`)
- `frontend/index.html` (one screen)
- `tests/summarizer.test.js`

### Action
✅ Applied. Reason: no `npm install` is needed, so every team member can run it with just Node.js.

## Entry 2: Summarizer logic

### Prompt
Write a function that takes a meeting transcript and returns a summary, a list of decisions and a list of action items with owner and due date.

### AI Output
`summarize(transcript)` in `summarizer.js`. It splits the text into sentences, uses keyword rules ("decided", "agreed" for decisions; "will", "should", "needs to" for action items) and regular expressions to find the owner (first name before "will") and the due date ("by Friday", "before tomorrow", `YYYY-MM-DD`). Summary = first 3 sentences.

### Action
✅ Applied for the MVP.
⚠️ Limitation: rule-based logic is simple and misses complex sentences. A real LLM API call is the planned improvement; `summarize()` was written as a separate function so it can be replaced without changing the server or the frontend.

## Entry 3: Backend endpoint

### Prompt
Create the backend endpoint `POST /api/summarize` that accepts `{ "transcript": "..." }` and returns the result as JSON, with input validation and error handling.

### AI Output
`server.js` with:
- `POST /api/summarize` (returns 400 for empty text or invalid JSON, 413 for a body larger than 200 KB)
- `GET /api/health`
- `GET /` that serves the frontend page

### Action
✅ Applied without changes. The size limit was kept because it protects the server from very large requests.

## Entry 4: Frontend screen

### Prompt
Create one frontend screen: a text area for the transcript, a Summarize button, and sections for summary, decisions and action items. Add a "Copy as Markdown" button and keep the transcript if an error happens.

### AI Output
`frontend/index.html` (HTML, CSS and JavaScript in one file) that calls `/api/summarize` with `fetch`, renders the result, lets the user tick action items as done and copies the notes as Markdown.

### Action
✅ Applied.
❌ Rejected for now: editing the AI result and a history page (user stories 6 and 8). Reason: they need a database and are outside the time limit for the first MVP.

## Entry 5: Tests

### Prompt
Write tests for the summarizer and for the API endpoint using only built-in Node.js tools.

### AI Output
`tests/summarizer.test.js` with 4 tests using `node:test`: summary/decisions/action items, owner and due date, empty input error, and the HTTP endpoint (success, empty text, invalid JSON). The first `npm test` script pointed at the whole `../tests/` folder.

### Action
✅ Applied with an edit. Running the tests on the folder failed, so the script in `backend/package.json` was changed to `node --test ../tests/summarizer.test.js`. After that all 4 tests passed.

## How to run

```
cd ai_enhanced_team_hackathon/product_code/backend
npm test          # run tests
npm start         # start the app, then open http://localhost:3000
```
