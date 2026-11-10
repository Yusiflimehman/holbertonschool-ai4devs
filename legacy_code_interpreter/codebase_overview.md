# Codebase Overview - Legacy E-Commerce API

## Age
First release in 2012, last major update in 2018.

## Size
~65,000 LOC in Python (Flask/SQLAlchemy).

## Dependencies
- Python 2.7 (Deprecated)
- PostgreSQL 9.4
- Flask 0.12
- SQLAlchemy 1.1

## Issues
- Absence of automated unit and integration tests.
- Monolithic structure with tight coupling between payment and order modules.
- Deprecated Python version causing security vulnerabilities and dependency mismatches.
- Hardcoded configuration parameters within service files.
