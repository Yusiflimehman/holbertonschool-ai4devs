# Team Retrospective

## Project Summary
We built the AI Meeting Notes Summarizer, a web app that turns a raw meeting transcript into a short summary, a list of decisions and a list of action items with owners and due dates. During the hackathon we moved through ideation, planning, implementation, deployment and reflection, and we finished with a working MVP on a live URL, automated tests and written documentation for every stage.

## What Worked
- **Fast, structured ideation.** We compared three ideas (study planner, code review buddy, meeting notes summarizer) and picked the one with a clear problem and a small, buildable MVP. Choosing a narrow scope early saved us time later.
- **Planning before coding.** Writing eleven user stories, a five-entity data model and an architecture plan gave us a shared picture of the product. When we reached implementation, nobody had to ask what the app should do.
- **A deliberately small technical stack.** We used plain Node.js with no external packages. There was nothing to install, so every member could run the project the same way, and the four automated tests ran in under a second.
- **Documenting as we went.** The AI development log recorded each prompt, the output and the decision to apply or reject it. This made our choices easy to explain, for example why we postponed result editing and the history page.
- **Delivering a real demo.** Deploying to Render turned the project from files in a repository into something anyone can open in a browser, which made the work feel finished.

## Challenges
- **Wrong content in the right file.** At one point instructions were pasted into `team_ideation.md` instead of the actual content, so the automated check reported that the file did not exist. We lost time before we found the cause.
- **Wrong file location.** After we deleted and recreated a file, it ended up in the repository root instead of the `ai_enhanced_team_hackathon` folder. GitHub also removes a folder when its last file is deleted, which we did not expect.
- **Failed first deployment.** The platform defaulted to Python and to `yarn` commands, and the service could not find a `package.json` when it started. We had to read the logs, change the build and start commands in the settings and redeploy.
- **A test command that did not work.** Running the tests against a whole folder failed, while running the single test file passed. We fixed the script, but it showed that we had not run everything end to end before sharing it.
- **Manual workflow.** We uploaded every file through the GitHub web interface, one at a time. It worked, but it was slow and made small mistakes easy.
- **Limited summarizer.** The summarizer uses keyword rules, so it misses complex sentences. Editing results and a meeting history page were left out of the first MVP.

## Lessons
1. **Verify after every step.** Opening the file on GitHub and checking its first lines would have caught the wrong-content problem immediately.
2. **Test the exact commands you will ship.** Anything run in the cloud should be run locally the same way first.
3. **Read the logs.** The deployment error was clearly written in the log. Reading the last lines before guessing saved time.
4. **Keep the first version small.** A narrow MVP that works beats a large plan that does not.
5. **Write things down early.** Short documents for planning and for AI decisions made later stages faster.

## Next Steps
- Connect a real language model to replace the keyword rules.
- Add editing of results and a stored meeting history.
- Set up Git on our computers so that we push from the command line instead of uploading files by hand.
- Add a simple automatic check that runs the tests on every push.
