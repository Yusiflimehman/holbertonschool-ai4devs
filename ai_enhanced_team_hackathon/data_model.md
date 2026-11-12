# Data Model

Project: **AI Meeting Notes Summarizer**

## Entities

### 1. User
Person who uses the app and owns meetings.

| Field        | Type      | Notes                    |
|--------------|-----------|--------------------------|
| id           | UUID (PK) | Unique identifier        |
| name         | string    | Display name             |
| email        | string    | Unique                   |
| created_at   | datetime  | Account creation time    |

### 2. Meeting
One meeting with its raw transcript.

| Field        | Type      | Notes                          |
|--------------|-----------|--------------------------------|
| id           | UUID (PK) | Unique identifier              |
| user_id      | UUID (FK) | References `User.id`           |
| title        | string    | Meeting title                  |
| transcript   | text      | Raw transcript text            |
| meeting_date | date      | When the meeting took place    |
| created_at   | datetime  | When it was added to the app   |

### 3. Summary
AI-generated summary of a meeting (one summary per meeting).

| Field        | Type      | Notes                              |
|--------------|-----------|------------------------------------|
| id           | UUID (PK) | Unique identifier                  |
| meeting_id   | UUID (FK) | References `Meeting.id`, unique    |
| content      | text      | Summary text (editable by user)    |
| model_name   | string    | AI model used                      |
| created_at   | datetime  | Generation time                    |
| updated_at   | datetime  | Last manual edit                   |

### 4. Decision
A decision extracted from a meeting.

| Field        | Type      | Notes                          |
|--------------|-----------|--------------------------------|
| id           | UUID (PK) | Unique identifier              |
| meeting_id   | UUID (FK) | References `Meeting.id`        |
| text         | string    | Decision text                  |

### 5. ActionItem
A task extracted from a meeting.

| Field        | Type      | Notes                                   |
|--------------|-----------|-----------------------------------------|
| id           | UUID (PK) | Unique identifier                       |
| meeting_id   | UUID (FK) | References `Meeting.id`                 |
| task         | string    | What must be done                       |
| owner        | string    | Responsible person (nullable)           |
| due_date     | date      | Deadline (nullable)                     |
| status       | enum      | `open` or `done` (default `open`)       |

## Relationships

- One **User** has many **Meetings** (1 → N).
- One **Meeting** has one **Summary** (1 → 1).
- One **Meeting** has many **Decisions** (1 → N).
- One **Meeting** has many **ActionItems** (1 → N).
- Deleting a Meeting deletes its Summary, Decisions and ActionItems (cascade).

## Diagram

```
User 1 ──── N Meeting 1 ──── 1 Summary
                 │
                 ├──── N Decision
                 │
                 └──── N ActionItem
```
