# Pull Request: Add Task Filtering Feature

## Summary
Implements task filtering by status and due date. Adds new API endpoint `/tasks/filter`.

## Changes
- Added `filter_tasks()` in `tasks.py`
- Updated `Task` model to support status-based queries
- Added 5 new unit tests for edge cases

## Context
~150 LOC added. Related issue: #42. Improves API response speed and data accessibility for dashboard integrations.
