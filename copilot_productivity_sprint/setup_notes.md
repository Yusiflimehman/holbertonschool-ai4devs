# Environment Setup Notes

## Objective
Prepare and document the IDE and AI assistant environment (GitHub Copilot) for testing, development, and productivity benchmarking.

## System & IDE Environment
- **Operating System:** Windows 11 / macOS / Linux
- **IDE:** Visual Studio Code
- **IDE Version:** 1.87.2

## AI Tools & Extensions Installed

### 1. GitHub Copilot
- **Extension Name:** GitHub Copilot
- **Extension ID:** `GitHub.copilot`
- **Installed Version:** v1.156.0
- **Source:** Visual Studio Code Marketplace

### 2. GitHub Copilot Chat
- **Extension Name:** GitHub Copilot Chat
- **Extension ID:** `GitHub.copilot-chat`
- **Installed Version:** v0.13.0
- **Source:** Visual Studio Code Marketplace

## Detailed Setup & Configuration Process

### Prerequisites
- Active GitHub account with an enabled GitHub Copilot subscription (Individual/Enterprise).
- Visual Studio Code installed and updated to the latest stable build.

### Installation Steps
1. Launched Visual Studio Code.
2. Navigated to the Extensions view (`Ctrl+Shift+X` / `Cmd+Shift+X`).
3. Searched for `GitHub.copilot` and clicked **Install**.
4. Searched for `GitHub.copilot-chat` and clicked **Install**.

### Authentication & Sign-In Flow
1. Upon installation, clicked the **Sign in to GitHub** prompt in the bottom status bar.
2. Authorised VS Code to access GitHub account credentials via the external browser login page.
3. Successfully linked the GitHub Copilot subscription to the editor environment.

### Workspace Configuration Settings
- `github.copilot.enable`: `{"*": true}` (Enabled globally for all file types).
- Inline suggestions enabled: `editor.inlineSuggest.enabled: true`.

## Verification & Validation Steps
1. Created a test file `test.js` to verify inline completions.
2. Typed `function calculateSum(a, b)` and verified that GitHub Copilot generated a auto-completion suggestion via `Tab`.
3. Opened Copilot Chat panel (`Ctrl+Alt+I` / `Cmd+Ctrl+I`), sent a query `"Explain quicksort"`, and verified the AI streaming response.
