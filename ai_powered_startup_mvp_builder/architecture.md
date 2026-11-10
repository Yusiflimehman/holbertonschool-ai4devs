# System Architecture

## High-Level Architecture Diagram
+-------------------------------------------------------+
|                    Frontend UI                        |
|  (React / Next.js / Tailwind CSS Single Page App)     |
+---------------------------+---------------------------+
|
v
+-------------------------------------------------------+
|                    Backend API                        |
|       (Node.js / Express or Python API Gateway)       |
+-------------+-----------------------------+-----------+
|                             |
v                             v
+---------------------------+ +-------------------------+
|     Database Layer        | |    AI Processing Unit   |
|   (SQLite / PostgreSQL)   | |  (LLM Sentiment Engine) |
+---------------------------+ +-------------------------+


## System Components
- **Frontend Layer:** Renders user submission forms and the admin dashboard.
- **Backend API Layer:** Validates inputs, handles routes, and manages database operations.
- **Database Layer:** Persists users, feedback entries, and category definitions.
- **AI Integration Unit:** Performs automated sentiment analysis and text summarizatio
