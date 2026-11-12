# User Stories

Project: **AI Meeting Notes Summarizer**

Format: *As a [role], I want [goal], so that [benefit].*

## Core Stories

1. **Submit transcript**
   As a team member, I want to paste a meeting transcript into the app, so that I can get notes without writing them manually.
   - Acceptance: text area accepts at least 20,000 characters; empty input shows an error message.

2. **Upload transcript file**
   As a team member, I want to upload a `.txt` file with the transcript, so that I do not have to copy and paste long text.
   - Acceptance: only `.txt` files are accepted; file content is loaded into the input.

3. **Get meeting summary**
   As a team lead, I want the AI to generate a short summary of the meeting, so that people who missed it can catch up in a minute.
   - Acceptance: summary is shown in under 30 seconds and is no longer than 10 sentences.

4. **Extract decisions**
   As a project manager, I want the key decisions listed separately, so that nothing agreed in the meeting is forgotten.
   - Acceptance: each decision is a single short sentence in a bullet list.

5. **Extract action items**
   As a team member, I want action items with the responsible person and deadline (when mentioned), so that I know what I must do.
   - Acceptance: each item has `task`, `owner` and `due date` fields; missing values are shown as "Not specified".

6. **Edit the result**
   As a user, I want to edit the generated summary, decisions and action items, so that I can fix AI mistakes before sharing.
   - Acceptance: all generated fields are editable; changes are saved.

7. **Export as Markdown**
   As a user, I want to copy or download the notes as Markdown, so that I can share them in chat, email or GitHub.
   - Acceptance: "Copy" and "Download .md" buttons produce a correctly formatted file.

8. **View meeting history**
   As a user, I want to see a list of my previous meetings and their summaries, so that I can find old decisions quickly.
   - Acceptance: list is sorted by date (newest first); clicking an item opens its details.

## Additional Stories

9. **Mark action item as done**
   As a team member, I want to mark an action item as completed, so that the team can track progress.
   - Acceptance: status toggles between "open" and "done" and is saved.

10. **Delete a meeting**
    As a user, I want to delete a meeting and its notes, so that I can remove outdated or sensitive content.
    - Acceptance: deletion asks for confirmation and removes all related data.

11. **Handle AI errors**
    As a user, I want a clear error message and a "Try again" button when the AI request fails, so that I do not lose my transcript.
    - Acceptance: transcript stays in the input after an error.
