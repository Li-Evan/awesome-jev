# Jev Cheatsheet

**English** · [简体中文](cheatsheet.zh-CN.md)

A one-page field guide to building with Jev, distilled from the [official TypeSafe docs](https://docs.typesafe.ai). When this page and the docs disagree, the docs win.

Last checked on 2026-09-21 against `jev-1.13.0`, `typesafe-sdk` 0.7.0 (Python), and `@typesafe-ai/sdk` 0.6.0 (JavaScript).

- [Mental model](#mental-model)
- [One request, end to end](#one-request-end-to-end)
- [Pick a primitive](#pick-a-primitive)
- [Write good questions](#write-good-questions)
- [Design the state](#design-the-state)
- [Act on probabilities and confidence](#act-on-probabilities-and-confidence)
- [Composition moves](#composition-moves)
- [Limits and pricing](#limits-and-pricing)
- [Known jagged edges in Jev 1.13](#known-jagged-edges-in-jev-113)
- [When not to use Jev](#when-not-to-use-jev)
- [SDK snippets](#sdk-snippets)
- [Where Jev fits](#where-jev-fits)

## Mental model

- Jev is a **System One** model: it makes fast, narrow judgments. It does not generate text, write code, or explain itself.
- You send one **state** (the evidence) and many typed **questions** (the judgments). Every question is evaluated in parallel and in isolation against the same state, so questions cannot see each other's answers.
- You get back **typed answers with probabilities**. Your code owns the control flow: it branches, sorts, thresholds, and escalates.
- Rule of thumb from the docs: a good question is a gut check a knowledgeable person could make in a few seconds with the right context. If it needs deliberation, decompose it.

## One request, end to end

```bash
curl -X POST https://api.typesafe.ai/v1/systemone \
  -H "Authorization: Bearer $TYPESAFE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "jev-latest",
    "state": "I was charged twice for order A-104. Please fix this today.",
    "questions": {
      "department": {
        "type": "choice",
        "instructions": "Which team should handle this message?",
        "criteria": {"billing": "Payments and refunds", "technical": "Bugs and integrations", "other": null}
      },
      "frustration": {
        "type": "score",
        "instructions": "How frustrated does the customer sound?",
        "criteria": ["Calm, just stating facts", "Frustrated but civil", "Very angry, strong language"]
      },
      "is_urgent": {"type": "noul", "instructions": "The message asks for action within a specific time frame."}
    }
  }'
```

The response has the same keys you asked with:

```json
{
  "model": "jev-1.13.0",
  "answers": {
    "department": {"type": "choice", "choice": "billing", "confidence": 0.9, "probabilities": {"billing": 0.95, "technical": 0.03, "other": 0.02}},
    "frustration": {"type": "score", "score": 1.2, "confidence": 0.7, "legend": {"0": "Calm, just stating facts", "1": "Frustrated but civil", "2": "Very angry, strong language"}, "probabilities": {"0": 0.05, "1": 0.7, "2": 0.25}},
    "is_urgent": {"type": "noul", "noul": 0.97}
  },
  "usage": {"input_tokens": 180, "output_tokens": 20}
}
```

The numbers above are illustrative. The response shape matches the [API reference](https://docs.typesafe.ai/api).

## Pick a primitive

| You need | Primitive | Returns | Your code usually does |
| --- | --- | --- | --- |
| One option from a fixed, unordered set | [Choice](https://docs.typesafe.ai/primitives/choice) | `choice`, `probabilities`, `confidence` | `match` / `switch` on the option |
| A position on an ordered scale | [Score](https://docs.typesafe.ai/primitives/score) | `score` (probability-weighted level index), `legend`, `probabilities`, `confidence` | Compare against a threshold, sort, weight |
| Whether one condition holds | [Noul](https://docs.typesafe.ai/primitives/noul) | `noul` = P(yes), from 0 to 1 | `if p > threshold` |

- Choice probabilities always sum to 1, so *something* always wins. Add an `other` or `none` option, or ask a separate Noul such as "does the document answer this at all?".
- A Score can land between levels (for example `1.2`). Round it, threshold it, or read the distribution.
- A Noul of 0.5 means "yes and no are equally likely", **not** "medium intensity". Use a Score to measure degree.
- Multi-label? Ask one Noul per label instead of one Choice.
- Nouls have no `confidence` field: the single probability already says everything.

## Write good questions

- **One judgment per question.** "Is this spam?" hides several judgments. Ask about the sender, the request, and the pressure tactics separately, then combine them in code.
- **One condition per Noul.** Split "angry *and* asking for a refund" into two questions.
- **Phrase the positive case.** Prefer "Does the message contain personal data?" over "Is the message free of personal data?". For verification, make the *failure* the `true` case ("Is this field hallucinated?").
- **Score levels are concrete situations**, ordered low to high, each readable on its own. Avoid bare numbers (`["0", "1", "2"]`) and levels that mix dimensions.
- **Put the judgment in `instructions` and the answer space in `criteria`.** Both accept strings or JSON structure (definitions, contrasts, exclusions, examples). See [Advanced: structure](https://docs.typesafe.ai/primitives/advanced).
- **Question IDs are never sent to the model.** `is_urgent` means nothing to Jev; the instructions must carry the full meaning.
- **Point at nested state with backticked paths**, for example `` `ticket.messages[0].text` ``.

## Design the state

- One state per request, as a string, a JSON object, or an array. Named JSON fields work best when the context has several parts.
- Put everything that must be *compared* in the same state: the message, the order record, and the policy.
- Send only what the questions need. Accuracy drops as irrelevant content grows, so filter and retrieve in code first.
- Prefer your own current data over what the model might "know".
- Treat the state as data that can be adversarial. Injected text can move answers.
- Text only for now. Convert images, audio, and tables to text or structured fields first. English works best; test other languages (including CJK) on your own data.

## Act on probabilities and confidence

- **Three paths** as a starting point: high confidence acts automatically, medium asks for confirmation or review, low goes to a human or a fallback system.
- **Thresholds scale with risk.** A read-only action can act at a lower confidence than a money transfer. The [confidence-gated routing](https://docs.typesafe.ai/patterns/confidence-routing) pattern shows both in one Choice.
- **Nouls get an uncertainty band**, for example 0.30 to 0.70 goes to review, rather than a hard cut at 0.5.
- **Weakest link wins** when several answers feed one action: use the minimum confidence across them.
- **Confidence describes the distribution, not correctness.** Tune thresholds on your own labeled data, and pin a versioned model ID (for example `jev-1.13.0`) once you have tuned them, because `jev-latest` moves.
- Only need the best option? Take the argmax. Running statistics? Use `probabilities`, not `confidence`.

## Composition moves

| Move | What it looks like | Learn from |
| --- | --- | --- |
| Speculative fan-out | Ask every question you *might* need in one request; code reads only the relevant answers | [Fan-out](https://docs.typesafe.ai/patterns/fan-out), [Parallel questions](https://docs.typesafe.ai/cookbooks/parallel_questions) |
| Route with a second axis | The answer says *what*, confidence says *whether to act* | [Confidence-gated routing](https://docs.typesafe.ai/patterns/confidence-routing), [Intent routing](https://docs.typesafe.ai/patterns/intent-routing) |
| Score atomically, weight in code | Several Scores, one formula you can change without re-running inference | [Composite scoring](https://docs.typesafe.ai/patterns/composite-scoring) |
| Select, don't generate | Find candidates with regex or an LLM; Jev picks the right one; code normalizes it | [Pre-parsed value extraction](https://docs.typesafe.ai/cookbooks/pre_parsed_value_extraction_cookbook), [Structure recovery](https://docs.typesafe.ai/cookbooks/autoformat) |
| Model reads, code computes | Jev reads date parts or field values; code does the arithmetic | [Date extraction](https://docs.typesafe.ai/cookbooks/date_extraction_cookbook) |
| Rank by probability | One Noul per query-candidate pair, sort by `noul` | [Re-ranking](https://docs.typesafe.ai/cookbooks/rerank_typesafe) |
| Gate, then decide | A cheap "is any of this relevant?" Noul before or beside the main Choice | [Line-by-line search](https://docs.typesafe.ai/cookbooks/semantic_find), [Skill suggestion](https://docs.typesafe.ai/cookbooks/skill_suggestion) |
| Walk a taxonomy | One Choice per node, beam search over the probabilities | [Hierarchical classification](https://docs.typesafe.ai/cookbooks/hierarchical_classification) |
| Back off when unsure | Report the parent category when confidence is low | [Classification using confidence](https://docs.typesafe.ai/cookbooks/classification_using_confidence) |
| Verify and escalate | A cheap model extracts, Jev checks each field, doubtful cases go to a stronger model or a human | [SDE cascade](https://docs.typesafe.ai/cookbooks/sde_cascade), [Citation check](https://docs.typesafe.ai/cookbooks/citation_check) |
| Judgments as features | Turn text into Noul and Score columns, then train a classical model | [Autoresearch feature discovery](https://docs.typesafe.ai/cookbooks/autoresearch_feature_discovery) |
| Levels as actions | Make each Score level an action (merge, review, leave), so there is no threshold to fit | [Entity alignment](https://docs.typesafe.ai/cookbooks/entity_alignment) |

## Limits and pricing

As listed on the [Models](https://docs.typesafe.ai/models) and [API](https://docs.typesafe.ai/api) pages on 2026-09-21. Check them before you rely on these numbers.

| Item | Value |
| --- | --- |
| Endpoint | `POST https://api.typesafe.ai/v1/systemone` (`GET /v1/models` lists models) |
| Auth | `Authorization: Bearer $TYPESAFE_API_KEY` |
| Current model | `jev-1.13.0`; aliases `jev-latest` and `jev-preview` both point to it |
| Price | $0.042 per million input tokens; output tokens are free |
| Rate limits | 250,000 tokens per second and 1,200 requests per minute (adjusted dynamically; `429` when exceeded) |
| Context | 64k tokens per request; 32k for the state plus the longest question |
| Choice options | Up to 255 per question |
| Score levels | 2 to 10 per question |
| Latency | About 100 ms for most queries, per the docs |
| Input | Text only |
| Customization | No fine-tuning; shape behavior through state, instructions, criteria, and decomposition |
| SDK environment variables | `TYPESAFE_API_KEY`, `TYPESAFE_BASE_URL`, `TYPESAFE_DEFAULT_MODEL`, `TYPESAFE_LOG_LEVEL` |

## Known jagged edges in Jev 1.13

Summarized from [Jev 1.13 jaggedness](https://docs.typesafe.ai/model-jaggedness/jev-1.13). Each has a workaround in code.

| Weak spot | Workaround |
| --- | --- |
| Reads scoping words, negations, and implied conditions literally | State the exact condition; put boundary cases in `criteria` |
| Counting, arithmetic, numeric formats (hex, binary, colors) | Count and compute in code; one question per item |
| Comparing dates and time windows | Extract date parts with Choices, compute in code |
| Double negatives and multi-hop questions | Decompose into direct questions |
| Large state full of irrelevant detail | Filter first, or run a relevance Noul |
| Adversarial or self-arguing text in the state | Explicit criteria; test edge cases |
| Instructions that contradict criteria | Keep `true` meaning "yes" |
| Equivalent questions do not always agree (a Noul versus a yes/no Choice, a question versus its negation) | Do not reuse a Noul threshold for a Choice; calibrate each question |
| Generating text | Generate candidates elsewhere; let Jev choose |

## When not to use Jev

- The answer is text: replies, summaries, code, explanations.
- Code can compute it exactly: arithmetic, dates, lookups, regular expressions, fixed rules.
- The task needs extended reasoning ("analyze and determine the best course of action"). Decompose it, or hand it to a reasoning model.
- You would otherwise build an agent `while` loop that ordinary control flow can express.
- You are treating a guardrail Noul as a security boundary. Use it as one signal among several.
- You would need to call the API from a browser. Keep keys server-side.

## SDK snippets

Python (`pip install typesafe-sdk` or `uv add typesafe-sdk`, Python 3.10+). The client reads `TYPESAFE_API_KEY` and defaults to `jev-latest`.

```python
from typesafe_sdk import Choice, Noul, Score, TypeSafeClient

client = TypeSafeClient()

response = client.system_one(
    state={"message": "I was charged twice for order A-104. Please fix this today."},
    questions={
        "department": Choice(
            instructions="Which team should handle `message`?",
            criteria={"billing": "Payments and refunds", "technical": "Bugs and integrations", "other": None},
        ),
        "frustration": Score(
            instructions="How frustrated does the customer sound in `message`?",
            criteria=["Calm, just stating facts", "Frustrated but civil", "Very angry, strong language"],
        ),
        "is_urgent": Noul(instructions="`message` asks for action within a specific time frame."),
    },
)

department = response.choices["department"]
if department.confidence < 0.5:
    print("send to a human")
else:
    print(department.choice, response.scores["frustration"].score, response.nouls["is_urgent"].noul)
```

Python, async:

```python
import asyncio

from typesafe_sdk import AsyncTypeSafeClient, Noul


async def main() -> None:
    async with AsyncTypeSafeClient() as client:
        response = await client.system_one(
            state="Can I get a refund for a cancelled flight?",
            questions={"asks_refund": Noul(instructions="The message asks for a refund.")},
        )
        print(response.nouls["asks_refund"].noul)


asyncio.run(main())
```

JavaScript or TypeScript (`npm install @typesafe-ai/sdk`, Node.js 20+). Keep the key on the server.

```ts
import { choice, noul, TypeSafeClient } from "@typesafe-ai/sdk";

const client = new TypeSafeClient();

const response = await client.systemOne({
  state: { message: "I was charged twice. Please fix this ASAP." },
  questions: {
    category: choice("What is `message` about?", { billing: null, technical: null, other: null }),
    urgent: noul("`message` asks for action within a specific time frame."),
  },
});

console.log(response.answers.category.choice, response.answers.urgent.noul);
```

## Where Jev fits

The docs' [use-case map](https://docs.typesafe.ai/concepts/use-case-map) lists ideas across 18 areas. They reduce to a handful of decision shapes:

| Decision shape | Typical primitive | Examples |
| --- | --- | --- |
| Classification | Choice | Intent, topic, department, risk type |
| Detection | Noul | Spam, fraud, urgency, jailbreaks, personal data |
| Scoring | Score | Severity, relevance, quality, frustration |
| Routing | Choice plus confidence | Support queues, model routing, tool selection, escalation |
| Search, retrieval, ranking | Noul or Score per candidate, or Choice over line IDs | RAG context selection, reranking, semantic find |
| Verification | Noul battery or Choice | Citation support, tool-call errors, policy violations, hallucinated fields |
| Structured extraction | Choice over candidates or parts | Dates, amounts, contact details, product attributes |
| Feature extraction | Noul and Score columns | Purchase intent, churn signals, competitive pressure |
