# Team Retrospective

## Project Summary
We built the AI Meeting Notes Summarizer, a web app that turns a raw meeting transcript into a short summary, a list of decisions and a list of action items with owners and due dates. During the hackathon we moved through ideation, planning, implementation, deployment and reflection, and we finished with a working MVP on a live URL, automated tests and written documentation for every stage.

## What Worked
- Fast ideation. We compared three ideas and picked the one with a clear problem and a small, buildable MVP. A narrow scope saved us time later.
- Planning before coding. Eleven user stories, a five-entity data model and an architecture plan gave everyone the same picture of the product, so nobody had to ask what the app should do.
- A small technical stack. We used plain Node.js with no external packages. There was nothing to install, and the four automated tests ran in under a second.
- Documenting as we went. The AI development log recorded each prompt, the output and the decision to apply or reject it, which made our choices easy to explain.
- A real demo. Deploying to Render turned files in a repository into something anyone can open in a browser, and the work finally felt finished.

## Challenges
- Wrong content in the right file. Instructions were pasted into the ideation file instead of the real content, so the automated check reported that the file did not exist. We lost time before we found the cause.
- Wrong file location. After a file was deleted and recreated, it landed in the repository root. GitHub also removes a folder when its last file is deleted, which we did not expect.
- Failed first deployment. The platform defaulted to Python and to yarn commands, and the service could not find a package file when it started. We read the logs, changed the build and start commands and redeployed.
- A broken test command. Running the tests against a whole folder failed while running a single file passed. It showed that we had not run everything end to end before sharing it.
- Manual workflow. Uploading every file through the GitHub web interface was slow and made small mistakes easy.
- A limited summarizer. Keyword rules miss complex sentences, and result editing and meeting history were left out of the first MVP.

## Lessons
- Verify after every step. Opening the file on GitHub and checking its first lines would have caught the wrong content immediately.
- Test the exact commands you will ship. Anything that runs in the cloud should first run locally in the same way.
- Read the logs. The deployment error was written clearly in the log, and reading it before guessing saved time.
- Keep the first version small. A narrow MVP that works beats a large plan that does not.
- Write things down early. Short documents for planning and for AI decisions made later stages faster.

## Next Steps
- Connect a real language model to replace the keyword rules.
- Add result editing and a stored meeting history.
- Use Git from the command line instead of uploading files by hand.
- Add an automatic check that runs the tests on every push.
