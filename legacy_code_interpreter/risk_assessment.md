# Risk Assessment

| Risk | Severity | Notes |
| --- | --- | --- |
| Hardcoded credentials | High | Found in config.php and database connection scripts |
| Missing unit tests | Medium | Critical core business logic and modules remain untested |
| Deprecated API usage | High | Relies on removed PHP and third-party library functions |
| Tight coupling | Medium | High interdependence between components makes refactoring difficult |
| No logging | Low | Tracing operational failures and debugging production errors is harder |
| SQL Injection vulnerabilities | High | Raw query concatenations present in legacy reporting endpoints |
