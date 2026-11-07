# Prompt Use Cases

## Code Quality

- **Refactoring**
  - **Goal**: Improve code readability, maintainability, and execution performance without changing external behavior.
  - **Input**: Source function in [LANGUAGE]
  - **Output**: Optimized code + explanation
- **Style Enforcement**
  - **Goal**: Enforce consistent naming conventions, formatting, and organization standards across the codebase.
  - **Input**: Code block
  - **Output**: Rewritten code with consistent style
- **Security Auditing**
  - **Goal**: Identify potential security vulnerabilities and risky code patterns.
  - **Input**: Critical application endpoint code
  - **Output**: Security assessment report + patched code

## Debugging

- **Root Cause Analysis**
  - **Goal**: Identify the root cause of execution errors and runtime failures.
  - **Input**: Stack trace and surrounding code block
  - **Output**: Diagnostic breakdown + bug fix proposal
- **Edge Case Handling**
  - **Goal**: Uncover unhandled boundary conditions and unexpected inputs.
  - **Input**: Function logic block
  - **Output**: List of failure scenarios + defensive code patches
- **Performance Fixes**
  - **Goal**: Resolve memory leaks and high execution latency bottlenecks.
  - **Input**: Profiling logs + slow function block
  - **Output**: Optimized algorithms + resource usage notes

## Documentation
 
- **API Documentation**
  - **Goal**: Generate structured inline documentation and API specifications.
  - **Input**: Undocumented module or function
  - **Output**: Docstrings detailing parameters, returns, and exceptions
- **Architecture Overview**
  - **Goal**: Summarize system architecture and data flow for developers.
  - **Input**: Directory context or core project code
  - **Output**: High-level structural overview + relationship map
- **Codebase Onboarding Guide**
  - **Goal**: Create comprehensive developer setup guides and repository navigation instructions.
  - **Input**: Project configuration files and README structure
  - **Output**: Step-by-step developer onboarding document

## Testing

- **Unit Test Generation**
  - **Goal**: Build automated unit test suites for edge cases and core logic.
  - **Input**: Backend function or utility module
  - **Output**: Executable unit test suite using standard frameworks
- **Mock Data Creation**
  - **Goal**: Construct realistic mock objects and API response structures.
  - **Input**: Database schema or API contract
  - **Output**: Formatted synthetic data fixtures (JSON/YAML)
- **Integration Test Scenarios**
  - **Goal**: Generate end-to-end user flow test specifications for API endpoints.
  - **Input**: Endpoint specifications and expected response schema
  - **Output**: Complete integration test cases and assertion routines
