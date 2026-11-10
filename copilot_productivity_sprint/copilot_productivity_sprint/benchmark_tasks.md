# Benchmark Tasks Definition

## Overview
This document outlines 3 varied coding benchmark tasks designed to evaluate AI coding assistant capabilities (e.g., GitHub Copilot). Each task is structured to take approximately 15–30 minutes to implement and contains explicit requirements, inputs, outputs, and acceptance criteria.

---

## Task 1 - CRUD Endpoint: User Registration
- **Description:** Implement a backend user registration endpoint with input validation and database/in-memory persistence.
- **Requirements:** 
  - Create a `POST /api/v1/users` REST endpoint.
  - Validate that `name` is a non-empty string and `email` follows a valid standard email format.
  - Return appropriate HTTP status codes and JSON response bodies.
- **Inputs:** JSON Payload `{ "name": "John Doe", "email": "john@example.com" }`
- **Outputs:** JSON Payload `{ "id": "usr_12345", "name": "John Doe", "email": "john@example.com", "createdAt": "2026-03-30T10:00:00Z" }`
- **Acceptance Criteria:**
  - Returns `HTTP 201 Created` with the newly created user object on valid payload.
  - Returns `HTTP 400 Bad Request` with error details when `email` is invalid or missing.
  - Returns `HTTP 409 Conflict` if the email address is already registered.

---

## Task 2 - Data Processing: CSV Sales Aggregator
- **Description:** Write a data processing function that parses a raw CSV string of transaction logs and computes total sales grouped by product category.
- **Requirements:**
  - Parse input CSV data containing transaction details (`transaction_id`, `category`, `amount`, `status`).
  - Filter out any transactions where `status` is not `"COMPLETED"`.
  - Calculate total sales amount per `category` and sort categories alphabetically.
- **Inputs:** String CSV containing: `transaction_id,category,amount,status`
- **Outputs:** Map/Object of aggregated results, e.g., `{ "Electronics": 450.00, "Home Goods": 120.50 }`
- **Acceptance Criteria:**
  - Correctly ignores rows with `status` equal to `"CANCELLED"` or `"PENDING"`.
  - Handles invalid numeric strings safely without crashing (logs or skips corrupted lines).
  - Returns a clean summary dictionary/JSON object sorted by category key.

---

## Task 3 - Algorithmic Logic: Rate Limiter (Token Bucket)
- **Description:** Implement an in-memory Rate Limiter class using the Token Bucket algorithm.
- **Requirements:**
  - Create a `RateLimiter` class initialized with `capacity` (max tokens) and `refill_rate` (tokens per second).
  - Implement a method `allow_request(user_id)` that checks whether a given user has available tokens to execute an operation.
- **Inputs:** `user_id` (string), Timestamp of invocation (implicit/system clock)
- **Outputs:** Boolean (`true` if request is allowed and token consumed, `false` if rate limit exceeded)
- **Acceptance Criteria:**
  - Successfully allows requests up to the maximum token capacity.
  - Refills tokens at the expected rate over time.
  - Returns `false` immediately when a user exceeds their available token bucket without blocking thread execution.
