# Deployment

## Live Demo
- **Live URL:** https://meeting-notes-summarizer-fkdc.onrender.com
- **Health check:** https://meeting-notes-summarizer-fkdc.onrender.com/api/health
- **GitHub repository:** https://github.com/Yusiflimehman/holbertonschool-ai4devs
- **Code location:** `ai_enhanced_team_hackathon/product_code/`

## Platform
**Render** (Web Service, Free instance type).

Render was chosen because the app is a simple Node.js server with no external dependencies, and Render deploys it directly from GitHub on the free plan.

## Deployment Steps
1. Created a Render account and signed in with GitHub.
2. Clicked **New + → Web Service** and connected the `holbertonschool-ai4devs` repository (branch `main`).
3. Filled in the service settings (see the Configuration table below).
4. Clicked **Deploy web service** and waited for the build to finish.
5. The first deploy failed because the Start Command `yarn start` could not find a `package.json` in the service directory. I changed the Build Command to `echo "No build step"` and the Start Command to `node server.js` in **Settings → Build & Deploy**, then redeployed.
6. The second deploy succeeded and the status changed to **Live**.
7. Tested the live site: opened the main page, checked `/api/health` (returns `{"status":"ok"}`) and summarized a sample transcript.

## Configuration
| Setting          | Value                                                      |
|------------------|------------------------------------------------------------|
| Name             | `meeting-notes-summarizer`                                 |
| Language         | Node                                                       |
| Branch           | `main`                                                     |
| Region           | Virginia (US East)                                         |
| Root Directory   | `ai_enhanced_team_hackathon/product_code/backend`          |
| Build Command    | `echo "No build step"`                                     |
| Start Command    | `node server.js`                                           |
| Instance Type    | Free                                                       |
| Environment vars | None (Render sets `PORT` automatically; the server reads it) |

## Verification
- Main page loads and shows the "AI Meeting Notes Summarizer" screen.
- `GET /api/health` returns `{"status":"ok"}`.
- Sample transcript returns a summary, 2 decisions and 2 action items (Bob, due Friday; Carol, due tomorrow).

## Notes
- The free instance goes to sleep after inactivity, so the first request can take up to about 50 seconds.
- Every push to the `main` branch inside the service directory triggers an automatic redeploy.
- The summarizer is rule-based for now; connecting a real LLM API (using an API key stored as a Render environment variable) is the planned next step.
