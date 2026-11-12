# AI Effectiveness Summary

## Overview
We used an AI assistant throughout the project: to compare ideas, write the planning documents, generate the code and tests, draft the AI development log, and guide us through GitHub and deployment. This report covers where the AI helped, where it fell short, and what we learned. The assessments are our own judgement, not measured benchmarks.

## Where AI Was Most Effective
- Planning documents. From a short description, the AI produced eleven user stories with acceptance criteria, a five-entity data model and an architecture plan with endpoints and data flow. We kept them with almost no changes. This was the biggest time saver.
- Code scaffolding. The AI generated the backend, a single-screen frontend and four automated tests. It chose a design with no external packages, which removed installation problems.
- Testing before delivery. The AI ran the tests itself before giving us the code, and it noticed and fixed a failing test command instead of handing over a broken script.
- Debugging from evidence. When the deployment failed, a screenshot of the log was enough. The AI saw that the service could not find its package file and proposed running the server directly. The second deployment succeeded.
- Step-by-step guidance. The AI split long tasks into small steps with exact text to copy, which suited our manual work in the GitHub and Render web interfaces.

## Where AI Fell Short
- The product is not very intelligent. Although we call it an AI summarizer, the MVP uses keyword rules and regular expressions, not a language model. It handles clear sentences but misses indirect ones. This remains a real limitation.
- Instructions that did not match reality. Some steps assumed an interface that looked different in practice, such as the default settings on the deployment platform. We needed screenshots and a second round of instructions.
- First deployment assumptions. The first configuration relied on files being present at runtime and failed. The AI could not test the cloud environment itself.
- No direct access to our accounts. The AI could not push to GitHub or click through Render, so every upload and deployment was manual, which left room for human error.
- Output needs verification. Pasted content ended up in the wrong place more than once. AI output is only useful if a person checks where it landed.

## Estimated Impact
- Planning documents: high impact, complete drafts in minutes.
- Code and tests: high impact, a working MVP with four passing tests.
- Debugging: medium to high impact, fast when given the real log.
- Deployment guidance: medium impact, one correction was needed.
- Product intelligence: low to medium impact, rule-based and not model-based.

## Lessons Learned
- Give the AI real evidence. Logs and screenshots produced much better answers than descriptions of problems.
- Ask for small steps. Short, copyable steps reduced mistakes more than long explanations.
- Keep a human in the loop. The AI is fast, but a person must check files, settings and results.
- Be clear about limits. Writing down what the AI did not do kept the documentation honest.
- Log the decisions. Recording what we applied or rejected, and why, made the AI contribution easy to review.

## Recommendations
- Keep a shared library of tested prompts for planning, code and debugging.
- Run every generated command locally before using it in the cloud.
- Add a real language model to the summarizer and compare it with the rule-based version.
