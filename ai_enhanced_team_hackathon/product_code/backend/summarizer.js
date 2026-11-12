// Rule-based meeting summarizer (MVP).
// The function summarize() can later be replaced by a call to an LLM API
// without changing the server or the frontend.

const DAYS = "monday|tuesday|wednesday|thursday|friday|saturday|sunday";
const DUE_REGEX = new RegExp(
  `\\b(?:by|before|until)\\s+((?:next\\s+)?(?:${DAYS})|tomorrow|end of (?:the )?(?:day|week|month)|\\d{4}-\\d{2}-\\d{2})`,
  "i"
);
const DECISION_REGEX = /\b(decided|agreed|approved|decision|we will go with|settled on)\b/i;
const ACTION_REGEX = /\b(will|needs? to|should|must|to do|action item|is responsible for)\b/i;
const OWNER_REGEX = /^([A-Z][a-z]+)\s+(?:will|needs? to|should|must|is responsible for)\b/;

function splitSentences(text) {
  return text
    .replace(/\r/g, "")
    .split(/(?<=[.!?])\s+|\n+/)
    .map((s) => s.trim())
    .filter(Boolean);
}

// Remove a leading "Speaker:" label, e.g. "Anna: We agreed ..." -> "We agreed ..."
function stripSpeaker(sentence) {
  return sentence.replace(/^[A-Z][A-Za-z ]{0,30}:\s+/, "");
}

function summarize(transcript) {
  if (typeof transcript !== "string" || transcript.trim() === "") {
    throw new Error("Transcript must be a non-empty string");
  }

  const sentences = splitSentences(transcript).map(stripSpeaker);

  const decisions = [];
  const actionItems = [];

  for (const sentence of sentences) {
    if (DECISION_REGEX.test(sentence)) {
      decisions.push(sentence);
      continue;
    }
    if (ACTION_REGEX.test(sentence)) {
      const ownerMatch = sentence.match(OWNER_REGEX);
      const dueMatch = sentence.match(DUE_REGEX);
      actionItems.push({
        task: sentence,
        owner: ownerMatch ? ownerMatch[1] : "Not specified",
        due: dueMatch ? dueMatch[1] : "Not specified",
        status: "open",
      });
    }
  }

  // Summary: first 3 sentences of the meeting.
  const summary = sentences.slice(0, 3).join(" ");

  return { summary, decisions, actionItems };
}

module.exports = { summarize, splitSentences };
