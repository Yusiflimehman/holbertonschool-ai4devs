# AI Effectiveness Summary

## Overview
We used an AI assistant (Claude) throughout the project: to compare ideas, write the planning documents, generate the code and tests, draft the AI development log, and guide us through GitHub and deployment. This report summarizes where the AI helped, where it fell short, and what we learned about working with it. The assessments below are our own judgement, not measured benchmarks.

## Where AI Was Most Effective
- **Planning documents.** From a short project description, the AI produced eleven user stories with acceptance criteria, a five-entity data model with relationships, and an architecture plan with endpoints and a data flow. We reviewed and kept them with almost no changes. This was the biggest time saver.
- **Code scaffolding.** The AI generated the backend (a summarizer module and an HTTP server with validation and error handling), a single-screen frontend and four automated tests. It also chose a zero-dependency design, which removed installation problems.
- **Testing before delivery.** The AI ran the tests itself before giving us the code, and it noticed and fixed a failing test command instead of handing over a broken script.
- **Debugging from evidence.** When the deployment failed, a screenshot of the log was enough. The AI identified that the service could not find `package.json` and proposed changing the start command to run the server directly. The second deployment succeeded.
- **Step-by-step guidance.** The AI broke long tasks into small steps with exact text to copy, which suited our manual workflow in the GitHub and Render web interfaces.
- **Documentation.** The development log and the deployment record were drafted quickly and kept consistent with what actually happened.

## Where AI Fell Short
- **The product itself is not very intelligent.** Although the project is called an AI summarizer, the MVP uses keyword rules and regular expressions, not a language model. It handles clear sentences well but misses indirect ones. The AI built what was achievable without an API key and said so openly, but this is a real limitation.
- **Instructions that did not match reality.** Some steps assumed an interface that looked different in practice, such as the default settings on the deployment platform. We needed screenshots and a second round of instructions to fix them.
- **First deployment assumptions.** The first suggested configuration relied on files being present at runtime, and it failed. The AI could not test the cloud environment itself.
- **No direct access to our accounts.** The AI could not push to GitHub or click through Render for us. Every upload and deployment was done by hand, which left room for human error.
- **Output needs verification.** Pasted content ended up in the wrong place more than once. AI output is only useful if a person checks that it landed where it should.

## Estimated Impact
| Area | Impact | Comment |
|------|--------|---------|
| Planning documents | High | Complete drafts in minutes |
| Code and tests | High | Working MVP, four passing tests |
| Debugging | Medium to high | Fast when given the real log |
| Deployment guidance | Medium | Needed one correction |
| Product intelligence | Low to medium | Rule-based, not model-based |

The whole project, from idea to live demo, was finished in a short working session. Doing the same work without AI would have taken us considerably longer, mostly for the planning documents and the first version of the code.

## Lessons Learned
1. **Give the AI real evidence.** Logs and screenshots produced much better answers than descriptions of problems.
2. **Ask for small steps.** Short, copyable steps reduced mistakes more than long explanations.
3. **Keep a human in the loop.** The AI is fast, but a person must check files, settings and results.
4. **Be clear about limits.** Writing down what the AI did not do (a real language model, editing, history) kept the documentation honest.
5. **Log the decisions.** Recording what we applied or rejected, and why, made the AI's contribution easy to review.

## Recommendations
- Keep a shared library of tested prompts for planning, code and debugging.
- Run every generated command locally before using it in the cloud.
- Add a real language model to the summarizer and compare its output with the rule-based version.
- Review AI output in small pieces rather than in one large batch.
