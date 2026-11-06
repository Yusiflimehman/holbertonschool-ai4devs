# Prompt Use Cases

## 1. Code Quality
- **Refactoring**
  - **Goal**: Improve code readability, maintainability, and execution performance without changing external behavior.
  - **Input**: Legacy source function or block in [LANGUAGE].
  - **Output**: Optimized and refactored code block + clear explanation of changes.
- **Style & Standards Enforcement**
  - **Goal**: Enforce consistent naming conventions, formatting, and organization standards across the codebase.
  - **Input**: Unformatted source code snippet.
  - **Output**: Rewritten code compliant with specified style guides (e.g., PEP 8, Airbnb JS Style).
- **Security & Vulnerability Auditing**
  - **Goal**: Identify security risks, static bugs, dynamic memory issues, or vulnerability patterns (e.g., SQL injection, XSS).
  - **Input**: Critical application endpoint or authentication routine.
  - **Output**: Security assessment report with patched code snippets.

## 2. Debugging & Error Handling
- **Root Cause Analysis**
  - **Goal**: Identify the root cause of execution errors, stack traces, or unexpected runtime behavior.
  - **Input**: Stack trace, error logs, and surrounding codebase context.
  - **Output**: Step-by-step diagnostic breakdown + precise bug fix proposal.
- **Edge Case Identification**
  - **Goal**: Uncover unhandled boundary conditions, unexpected null values, or concurrency issues in algorithms.
  - **Input**: Complex function logic or business rule block.
  - **Output**: List of potential failure scenarios + defensive programming patches.
- **Performance Bottleneck Troubleshooting**
  - **Goal**: Pinpoint high latency, inefficient loops, memory leaks, or heavy database query operations.
  - **Input**: Profiling log data or slow function execution block.
  - **Output**: Optimized algorithmic logic (e.g., lower time complexity O(n)) + resource usage notes.

## 3. Documentation & Architecture
- **API & Function Documentation**
  - **Goal**: Generate structured inline documentation, docstrings, and external API specifications.
  - **Input**: Undocumented module, class, or endpoint function.
  - **Output**: Comprehensive docstrings (e.g., Google or JSDoc style) detailing parameters, returns, and exceptions.
- **System Architecture Summarization**
  - **Goal**: Summarize multi-file relationships, data flow mechanisms, or framework architecture for new developers.
  - **Input**: Core application structure files or directory context.
  - **Output**: High-level architectural overview + ASCII module relationship map.

## 4. Testing & Quality Assurance
- **Unit Test Case Generation**
  - **Goal**: Automatically build comprehensive unit test suites covering both standard flows and boundary conditions.
  - **Input**: Core backend function or logic component.
  - **Output**: Executable unit test suite using standard frameworks (e.g., PyTest, Jest, JUnit).
- **Mock Data & Integration Test Creation**
  - **Goal**: Construct realistic mock
