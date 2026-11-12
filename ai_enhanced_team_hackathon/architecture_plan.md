# Architecture Plan

Project: **AI Meeting Notes Summarizer**

## 1. Overview

A web application where a user submits a meeting transcript and receives a structured result: summary, decisions and action items. The system has three main parts: a frontend, a backend API and an external AI service, plus a database.

```
┌──────────────┐   HTTP/JSON   ┌───────────────┐   API call   ┌──────────────┐
│   Frontend   │ ────────────► │  Backend API  │ ───────────► │  AI Service  │
│  (Web UI)    │ ◄──────────── │               │ ◄─────────── │  (LLM API)   │
└──────────────┘               └───────┬───────┘              └──────────────┘
                                       │
                                       ▼
                               ┌───────────────┐
                               │   Database    │
                               └───────────────┘
```

## 2. Components

### Frontend (Web UI)
- Pages: transcript input, result view/editor, meeting history.
- Sends the transcript to the backend and displays the structured result.
- Provides copy / download Markdown buttons.
- Suggested stack: React (or plain HTML/JS) with a simple CSS framework.

### Backend API
- REST API that validates input, calls the AI service, parses the response and stores data.
- Keeps the AI API key on the server (never in the frontend).
- Suggested stack: Python (FastAPI) or Node.js (Express).

### AI Service
- An LLM API receives a prompt with the transcript and returns JSON with `summary`, `decisions` and `action_items`.
- Prompt is managed by the AI Prompt Strategist and stored in a separate file so it can be improved without code changes.

### Database
- Stores users, meetings, summaries, decisions and action items (see `data_model.md`).
- Suggested: SQLite for the MVP (easy setup), PostgreSQL later if needed.

## 3. API Endpoints (high level)

| Method | Endpoint                 | Purpose                                      |
|--------|--------------------------|----------------------------------------------|
| POST   | `/api/meetings`          | Submit transcript, run AI, save and return result |
| GET    | `/api/meetings`          | List meeting history                         |
| GET    | `/api/meetings/{id}`     | Get one meeting with summary, decisions, items |
| PUT    | `/api/meetings/{id}`     | Save user edits                              |
| PATCH  | `/api/action-items/{id}` | Mark action item open / done                 |
| DELETE | `/api/meetings/{id}`     | Delete a meeting and related data            |

## 4. Main Data Flow

1. User pastes or uploads a transcript in the UI.
2. Frontend sends `POST /api/meetings` with title and transcript.
3. Backend validates the input (not empty, size limit).
4. Backend builds a prompt and calls the AI service.
5. AI returns structured JSON; backend validates and parses it.
6. Backend saves Meeting, Summary, Decisions and ActionItems.
7. Backend returns the result; frontend shows it in an editable view.
8. User edits, then copies or downloads the Markdown.

## 5. Non-Functional Considerations

- **Security:** API key stored in environment variables; input length limited; basic input sanitization.
- **Error handling:** if the AI call fails or returns invalid JSON, return a clear error and keep the transcript so the user can retry.
- **Performance:** target response under 30 seconds; show a loading indicator.
- **Privacy:** transcripts may be sensitive, so users can delete their meetings at any time.
- **Testing:** unit tests for the JSON parser and API endpoints; manual UI testing by the UI/UX & Testing Lead.

## 6. Team Responsibilities

| Member   | Role                 | Main Areas                                  |
|----------|----------------------|---------------------------------------------|
| Member 1 | AI Prompt Strategist | Prompt design, JSON output format           |
| Member 2 | Frontend Dev         | UI pages, API integration                   |
| Member 3 | Backend/API Dev      | Endpoints, database, AI service integration |
| Member 4 | UI/UX & Testing Lead | Wireframes, usability, testing              |

## 7. Out of Scope for MVP

- Audio/video transcription
- Real-time meeting integration (Zoom, Teams)
- Multi-user teams and permissions
