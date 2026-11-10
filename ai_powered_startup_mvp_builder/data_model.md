# Data Model Definition

## Entities Overview

### 1. User
Represents visitors and administrators using the platform.
- `id` (INTEGER, Primary Key)
- `name` (STRING)
- `email` (STRING)
- `role` (STRING - admin/user)
- `created_at` (TIMESTAMP)

### 2. Feedback
Represents user submitted responses and AI-enriched analysis.
- `id` (INTEGER, Primary Key)
- `user_id` (INTEGER, Foreign Key referencing User)
- `category_id` (INTEGER, Foreign Key referencing Category)
- `comment` (TEXT)
- `rating` (INTEGER)
- `sentiment` (STRING - positive/neutral/negative)
- `created_at` (TIMESTAMP)

### 3. Category
Represents feedback categories and topic definitions.
- `id` (INTEGER, Primary Key)
- `name` (STRING)
- `description` (TEXT)
