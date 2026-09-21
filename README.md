# Awesome Jev [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> [Jev](https://typesafe.ai) is TypeSafe's System One model. It answers typed questions about text with calibrated probabilities instead of generating prose, so code can branch, sort, and route on its judgments.

Jev has three primitives: **Choice** picks one option, **Score** places something on an ordered scale, and **Noul** gives the probability that a statement is true. This list is organized around *how* Jev gets used. Each entry names the primitives or pattern it relies on and the results it reports, and framework integrations are listed only once they are merged or published upstream.

This list is community-maintained and not affiliated with TypeSafe. The official sites are `typesafe.ai` and `docs.typesafe.ai`, and the official GitHub organization is `typesafe-ai`. Be careful with look-alike domains that claim to be official.

## Contents

- [Getting Started](#getting-started)
- [Official Resources](#official-resources)
  - [Concepts](#concepts)
  - [Reference](#reference)
  - [SDKs and Tools](#sdks-and-tools)
  - [Announcements](#announcements)
- [Patterns](#patterns)
- [Recipes by Use Case](#recipes-by-use-case)
  - [Classification and Routing](#classification-and-routing)
  - [Agents and Tool Use](#agents-and-tool-use)
  - [Search and Retrieval](#search-and-retrieval)
  - [Extraction](#extraction)
  - [Verification and Guardrails](#verification-and-guardrails)
  - [Data and Knowledge Graphs](#data-and-knowledge-graphs)
  - [Reliability and Performance](#reliability-and-performance)
- [Integrations](#integrations)
  - [Model Access](#model-access)
  - [Framework Adapters](#framework-adapters)
  - [Observability](#observability)
  - [Community SDKs](#community-sdks)
- [Projects by Use Case](#projects-by-use-case)
  - [Routing and Tool Selection](#routing-and-tool-selection)
  - [Agents and Computer Use](#agents-and-computer-use)
  - [Coding Agents](#coding-agents)
  - [Guardrails and Context Control](#guardrails-and-context-control)
  - [Search and Databases](#search-and-databases)
  - [Data and Workflows](#data-and-workflows)
  - [Apps and Interfaces](#apps-and-interfaces)
  - [Games and Simulation](#games-and-simulation)
  - [Examples and Skills](#examples-and-skills)
- [Open Models and Compatible Servers](#open-models-and-compatible-servers)
- [Articles and Talks](#articles-and-talks)
  - [Guides](#guides)
  - [Techniques and Analysis](#techniques-and-analysis)
  - [Benchmarks and Case Studies](#benchmarks-and-case-studies)
  - [Talks and Videos](#talks-and-videos)
  - [Discussions](#discussions)

## Getting Started

- [Jev Cheatsheet](https://github.com/Li-Evan/awesome-jev/blob/main/cheatsheet.md) - One-page field guide to primitives, question design, confidence handling, limits, and tested SDK snippets.
- [Quick start](https://docs.typesafe.ai/introduction/quickstart) - First request through the Playground, cURL, the Python SDK, or a coding agent.
- [Playground](https://console.typesafe.ai/playground) - Try a state and a set of questions in the browser before writing code (sign-in required).
- [How to build with TypeSafe](https://docs.typesafe.ai/concepts/how-to-build-with-system-one) - Core design guide on keeping control flow in code and breaking judgments into atomic questions.
- [Agent skill](https://docs.typesafe.ai/agent-skill) - Teaches Claude Code, Codex, and other coding agents to design TypeSafe workflows from the live docs.

## Official Resources

### Concepts

- [System One](https://docs.typesafe.ai/concepts/system-one) - What separates a fast decision model from a text-generating LLM, and where each fits.
- [AI primer](https://docs.typesafe.ai/introduction/machine-learning-primer) - Why Jev is trained with reinforcement learning for calibrated decisions (RLCD) rather than for pleasing text.
- [State](https://docs.typesafe.ai/concepts/state) - How to shape the evidence that every question in a request is judged against.
- [Primitives](https://docs.typesafe.ai/primitives) - Choice, Score, and Noul compared, with rules for picking one and asking many at once.
- [Choice](https://docs.typesafe.ai/primitives/choice) - Selects one of up to 255 options and returns a probability for each.
- [Score](https://docs.typesafe.ai/primitives/score) - Places the state on 2 to 10 described levels and returns a probability-weighted position.
- [Noul](https://docs.typesafe.ai/primitives/noul) - Returns the probability that a yes-or-no condition holds.
- [Advanced structure](https://docs.typesafe.ai/primitives/advanced) - Using JSON in instructions and criteria for definitions, contrasts, exclusions, and examples.
- [Confidence](https://docs.typesafe.ai/confidence) - How confidence differs from probability and how to gate actions on it by risk.
- [Example use cases](https://docs.typesafe.ai/concepts/use-case-map) - Ideas across 18 areas, from support triage and recruiting to financial crime and knowledge graphs.

### Reference

- [API reference](https://docs.typesafe.ai/api) - The `POST /v1/systemone` request and response schema, errors, and rate-limit handling.
- [Models](https://docs.typesafe.ai/models) - Current versions, aliases, pricing per input token, rate limits, and context length.
- [Jev 1.13 jaggedness](https://docs.typesafe.ai/model-jaggedness/jev-1.13) - Known weak spots of the current model, such as counting and date comparison, with workarounds.
- [Migrating to v1](https://docs.typesafe.ai/migrating-to-v1) - Changes from the preview API and the old `typesafe-client` package.
- [Python SDK docs](https://docs.typesafe.ai/sdk/python) - Sync and async clients, typed answers, retries, and exceptions.
- [JavaScript SDK docs](https://docs.typesafe.ai/sdk/javascript) - Client configuration, question helpers, and inferred answer types for TypeScript.

### SDKs and Tools

- [typesafe-sdk-python](https://github.com/typesafe-ai/typesafe-sdk-python) - Official Python client, published on PyPI as `typesafe-sdk`.
- [typesafe-sdk-js](https://github.com/typesafe-ai/typesafe-sdk-js) - Official JavaScript and TypeScript client for Node.js, published on npm as `@typesafe-ai/sdk`.
- [TypeSafe skills](https://github.com/typesafe-ai/skills) - Source of the agent skill, installable as a Claude Code plugin or through skills.sh.
- [System One adapter](https://github.com/typesafe-ai/system-one-adapter-python) - Drop-in `TypeSafeClient` replacement backed by LLM APIs, for comparing cost, speed, and quality with Jev on your own workflow.
- [Workflow evals](https://evals.typesafe.ai) - Compares many models running four real workflows as decomposed questions versus as a single prompt.

### Announcements

- [Introducing System One models and Jev](https://typesafe.ai/blog/introducing-system-one-models-and-jev) - Launch post explaining the bet on decision models over text generators.
- [Manifesto](https://typesafe.ai/manifesto) - TypeSafe's argument for AI-powered software where code, not an agent loop, owns the workflow.

## Patterns

- [Speculative fan-out](https://docs.typesafe.ai/patterns/fan-out) - Ask every question you might need, including branch-specific ones, in one request and let code read only the relevant answers.
- [Confidence-gated routing](https://docs.typesafe.ai/patterns/confidence-routing) - Uses confidence as a second axis, with stricter thresholds for riskier actions such as money transfers.
- [Composite scoring](https://docs.typesafe.ai/patterns/composite-scoring) - Scores each dimension separately and combines them with weights in code, so priorities change without touching the questions.
- [Intent routing](https://docs.typesafe.ai/patterns/intent-routing) - Classifies requests with a Choice and a complexity Score, then sends each to code, a specialist LLM, or a human.

## Recipes by Use Case

Official cookbooks with runnable code. Most were written against `jev-1.12`, so re-check the numbers on the current model before relying on them.

### Classification and Routing

- [Hierarchical classification](https://docs.typesafe.ai/cookbooks/hierarchical_classification) - Walks deep taxonomies such as patent codes, retail products, MeSH, and a source tree with one Choice per node and beam search over the probabilities.
- [Classification using confidence](https://docs.typesafe.ai/cookbooks/classification_using_confidence) - Sorts 60 SEC filings into 75 industry groups and falls back to the broader division below 0.9 confidence, turning 39 correct answers into 48 useful ones.
- [Smart home assistant demo](https://docs.typesafe.ai/demos/smart-home) - Interprets home commands with a long speculative fan-out of Choices, plus a Noul that spots compound requests for an LLM to split.

### Agents and Tool Use

- [Function calling](https://docs.typesafe.ai/cookbooks/function_calling) - Maps trading requests onto ten ordinary typed functions, with Choices for the function and closed-set arguments and Nouls for which arguments were stated.
- [Skill suggestion](https://docs.typesafe.ai/cookbooks/skill_suggestion) - Picks at most one of 182 agent skills per turn in two requests, cutting wrong skill loads from 16.8% to 7.3%.

### Search and Retrieval

- [Re-ranking](https://docs.typesafe.ai/cookbooks/rerank_typesafe) - Scores each BM25 candidate with one Noul per query-passage pair, lifting top-10 legal retrieval accuracy from 38% to 62% for about $0.06 in total.
- [Line-by-line search](https://docs.typesafe.ai/cookbooks/semantic_find) - Ranks 218 lines of a terms-of-service document with a single Choice and uses a Noul to say when the document has no answer.
- [Classifying RAG passages](https://docs.typesafe.ai/cookbooks/classifying_rag_passages) - Runs four Nouls per retrieved passage to drop prompt injections and off-topic text and to flag passages that contradict the question.

### Extraction

- [Date extraction](https://docs.typesafe.ai/cookbooks/date_extraction_cookbook) - Reads date parts with Choices and leaves all calendar math to code, sending low-confidence dates to review.
- [Pre-parsed value extraction](https://docs.typesafe.ai/cookbooks/pre_parsed_value_extraction_cookbook) - Finds emails, phone numbers, and amounts with regular expressions, then lets a Choice select the requested one so values are never invented.
- [Structure recovery](https://docs.typesafe.ai/cookbooks/autoformat) - Rebuilds Markdown from flattened plain text in two requests without generating a single character.

### Verification and Guardrails

- [Double-checking citations](https://docs.typesafe.ai/cookbooks/citation_check) - Pairs an exact string match with a supports, contradicts, or says-nothing Choice to catch fabricated and misused citations.
- [Guardrails for LLMs](https://docs.typesafe.ai/cookbooks/llm_guardrails) - Screens inputs and outputs with hazard Nouls and a severity Score, then maps probabilities to pass, review, or block through code-owned policies.
- [SDE cascade](https://docs.typesafe.ai/cookbooks/sde_cascade) - A small LLM extracts fields, Jev checks each one for hallucination and format errors, and only doubtful cases escalate to a reasoning model.

### Data and Knowledge Graphs

- [Knowledge graph entity alignment](https://docs.typesafe.ai/cookbooks/entity_alignment) - Decides which product pairs match with one three-level Score whose levels are the actions: merge, send to a curator, or leave unlinked.
- [Autoresearch feature discovery](https://docs.typesafe.ai/cookbooks/autoresearch_feature_discovery) - An LLM proposes questions, Jev answers them for every row, and CatBoost learns from the answers, cutting held-out wine-score error (RMSE) from 3.09 to 1.77.

### Reliability and Performance

- [Parallel questions](https://docs.typesafe.ai/cookbooks/parallel_questions) - Batches 13 questions over one long document into a single request, 12.2x cheaper and 10.0x faster with no change in answers.
- [Self-consistency with Nouls](https://docs.typesafe.ai/cookbooks/consistency_noul_cookbook) - Repeats a 14-question insurance triage rubric 15 times and compares answer stability, latency, and cost with several LLMs.
- [Self-consistency with Choices](https://docs.typesafe.ai/cookbooks/consistency_choice_cookbook) - Adds an uncertain outcome to moderation decisions and weighs label agreement against the share of cases handled automatically.

## Integrations

### Model Access

- [Vercel AI Gateway](https://vercel.com/ai-gateway/models/jev) - Serves Jev as `typesafe-ai/jev` through the AI SDK, or as a drop-in base URL for the TypeSafe SDKs.
- [OpenRouter](https://openrouter.ai/typesafe/jev-1.13) - Offers Jev through a separate Decisions API rather than chat completions.
- [OpenRouter Jev Lab](https://openrouter.ai/labs/jev) - Runnable recipes for ticket triage, agent action approval, candidate extraction, feed filtering, and more.
- [Cloudflare Workers AI](https://developers.cloudflare.com/ai/models/typesafe/jev/) - Calls Jev from a Worker with `env.AI.run`, with examples for refund review, department routing, and risk scoring.
- [OpenCode Zen](https://opencode.ai/docs/zen/#jev) - Hosts Jev on a TypeSafe-compatible endpoint, including a free variant.

### Framework Adapters

- [Vercel AI SDK](https://ai-sdk.dev/providers/ai-sdk-providers/typesafe-ai) - Provider for `experimental_evaluate` that maps choice, score, and boolean questions onto Jev's primitives.
- [LangChain](https://docs.langchain.com/oss/python/integrations/providers/typesafe) - Classifier runnable plus experimental middleware for per-request model routing and for stopping risky tool calls (alpha).
- [LangChain.js](https://github.com/langchain-ai/langchainjs/tree/main/libs/providers/langchain-typesafe) - JavaScript version of the classifier and the routing and approval middleware.
- [Pydantic AI](https://pydantic.dev/docs/ai/models/typesafe/) - Runs an agent on Jev by mapping booleans to Nouls, enums to Choices, and integer rubrics to Scores, with an LLM fallback when unsure.
- [TanStack AI](https://tanstack.com/ai/latest/docs/adapters/typesafe) - Adapter for the `decide` API with choice, score, and boolean question helpers.
- [BAML](https://boundaryml.com/blog/typesafe-ai-jev) - Derives Jev questions from a function's return type, turning booleans and floats into Nouls and enums into Choices.
- [Effect](https://github.com/Effect-TS/effect/tree/main/packages/ai/typesafe) - Decision model service with classify, rate, and probability operations backed by Jev (release candidate).
- [Rig](https://github.com/0xPlaygrounds/rig/tree/main/crates/rig-typesafeai) - Rust support that turns structs implementing a query trait into Jev requests (merged, not yet on crates.io).
- [Spring AI TypeSafe](https://github.com/spring-ai-community/spring-ai-typesafe) - Java client and Spring AI components for judging, guardrails, self-refinement, and RAG filtering and reranking.
- [Composio](https://github.com/ComposioHQ/composio/tree/next/ts/packages/providers/typesafe) - TypeScript provider that picks and gates tool calls with a Choice and binds closed-set arguments before execution.

### Observability

- [Langfuse](https://langfuse.com/integrations/model-providers/typesafe) - Traces Jev calls through OpenInference so every judgment appears next to your LLM spans.
- [Arize Phoenix](https://arize.com/docs/phoenix/integrations/llm-providers/typesafe/typesafe-python) - OpenInference instrumentation for Python and TypeScript that records Jev inputs, outputs, and token counts.

### Community SDKs

- [Go SDK](https://github.com/Tangerg/typesafe-sdk-go) - Community Go client for the System One endpoint.
- [Swift SDK](https://github.com/NSStudent/JevSwiftSDK) - Community Swift client that defaults to `jev-latest`.
- [Rust client](https://gitlab.com/porky11/jev) - Community Rust crate published as `jev`.
- [RubyLLM provider](https://github.com/javiergradiche/ruby_llm-providers-typesafe) - Adds Jev as a provider for the RubyLLM library.

## Projects by Use Case

Open-source projects and upstream features that use Jev for a concrete job. Items marked "merged, not yet released" are on the default branch but not in a published package yet.

### Routing and Tool Selection

- [LiteLLM auto router](https://docs.litellm.ai/docs/proxy/auto_routing) - Picks a model tier for each request with a Jev Choice (release candidate).
- [Jev model router for Claude Code](https://github.com/davila7/claude-code-templates/tree/main/cli-tool/components/mods/productivity/jev-model-router) - Hook that asks for a tier Choice, an effort Score, and a risk Noul in one request, then adjusts model and reasoning effort.
- [Jev skill suggestion for Claude Code](https://github.com/davila7/claude-code-templates/tree/main/cli-tool/components/mods/productivity/jev-skill-suggestion) - Hides the skill roster and lets Jev attach at most one skill to each prompt.
- [Agent-native tool prefetch](https://github.com/BuilderIO/agent-native/blob/main/packages/core/src/agent/jev-tool-prefetch.ts) - Ranks up to 128 tools and skills with a single Choice and preloads the top three within 750 ms.
- [jev-router](https://github.com/gargpratyush/jev-router) - Wraps Claude Code and Codex so each turn goes to the cheapest model tier that can finish it, chosen with one dynamically built Choice.
- [JevRouter](https://github.com/BillionsBobby/JevRouter) - Treats models, subagents, skills, MCP servers, and CLIs as one candidate pool and routes with a two-stage Choice when the pool is large.
- [skillranker](https://github.com/Dicklesworthstone/skillranker) - Rust CLI that ranks skills for the current session with a wide Choice, then confirms a shortlist with one Noul each (custom license with usage restrictions).
- [Hermes Jev skills](https://github.com/kerpopule/hermes-jev-skills) - Routing, memory, skill-selection, and triage skills for Hermes, Claude Code, and Codex that start in shadow mode and publish their failures.

### Agents and Computer Use

- [Cua jev-use](https://cua.ai/docs/how-to-guides/driver/jev-use) - Bounded computer use where a Choice picks one of the actions the app exposes, or abstains, and the driver executes it.
- [OpenClaw TypeSafe plugin](https://docs.openclaw.ai/plugins/typesafe) - Gives agents a decision-model role and an optional evaluation tool (merged, not yet released).
- [AutoGPT TypeSafe blocks](https://github.com/Significant-Gravitas/AutoGPT/tree/master/autogpt_platform/backend/backend/blocks/typesafe) - Seven no-code blocks, including a five-exit router, a yes, no, or unsure split, and a score filter.
- [jev-ultrafast](https://github.com/browser-use/jev-ultrafast) - Browser agent that picks each step's operation and target from an element table in one request, with a speculative target per operation and a small LLM only for typed text.
- [jev-browser](https://github.com/jkudish/jev-browser) - Headless browser driver usable as an MCP server, CLI, or library, with a Choice for the next action and Nouls for done or stuck.
- [Jev voice browser](https://github.com/moritzkremb/jev-voice-browser) - Voice control for a real browser that asks 9 to 11 questions per utterance, including a Noul for destructive actions.
- [mobile-jev](https://github.com/droidrun/mobile-jev) - Android agent that applies the operation-plus-speculative-target pattern to a real phone.

### Coding Agents

- [Foreman](https://github.com/thruwire/foreman) - Supervises Codex and OpenCode workers with ten Nouls, such as whether a worker is stuck or looping.
- [jev-review](https://github.com/devagrawal09/jev-review) - Staged code review that builds a Noul risk matrix, then profiles and rates each finding with Choices and Scores.
- [Jev review MCP](https://github.com/NiazMorshed2007/jev-review) - MCP server that rates an agent's diff on 19 quality dimensions, each with an applicability Noul, a Score, and a main-weakness Choice.
- [jev-mcp](https://github.com/jkudish/jev-mcp) - Ten MCP judgment tools for agents, including claim verification, injection screening, reranking, and gating.

### Guardrails and Context Control

- [LiteLLM guardrail](https://docs.litellm.ai/docs/proxy/guardrails/typesafe) - Asks one Noul per finished tool exchange and clears results that are no longer needed before each call (release candidate).
- [Agentgateway guardrail example](https://github.com/agentgateway/agentgateway/tree/main/examples/llm-guardrail-jev) - Webhook that rates jailbreak, harm, and data-leak risk with three Scores and blocks requests at level 2 or above.
- [pi-jev](https://github.com/y0usaf/pi-jev) - Checks coding-agent tool calls with Nouls for destructive, exfiltrating, and out-of-scope actions plus an impact Score, and screens outputs for leaked secrets.
- [fast-jev-compaction](https://github.com/tamaratran/fast-jev-compaction) - Claude Code plugin that replaces the compaction summary with a keep-or-drop Noul per tool call; install it from GitHub, because the npm package with the same name comes from another publisher.
- [jev-pruner](https://github.com/tamaratran/jev-pruner) - Prunes large shell outputs chunk by chunk with one Noul each before they enter the context, keeping the original on disk.

### Search and Databases

- [LanceDB reranker](https://github.com/lancedb/lancedb/blob/main/python/python/lancedb/rerankers/typesafe.py) - Asks one Noul per query-document pair and stores an absolute relevance probability you can threshold (merged, not yet released).
- [OpenViking reranker](https://github.com/volcengine/OpenViking/blob/main/openviking/models/rerank/jev_rerank.py) - Rerank provider for a context database that scores every document with a Noul in one request (merged, not yet released).
- [llama-index-jev](https://github.com/WiktorB2004/llama-index-jev) - LlamaIndex reranker and router; reranking lifts nDCG@5 on NFCorpus from 0.340 to 0.396.
- [jev-search](https://github.com/superagents-lab/jev-search) - Natural-language web search that picks the time range and query with Choices and keeps each source only if its Noul passes (needs a Search1API key).
- [pg-jev](https://github.com/realZachi/pg-jev) - PostgreSQL extension for `WHERE jev(t, '...')` queries that batches 20 rows per request and reports how accuracy falls with larger batches.
- [jev-semgrep](https://github.com/uehaj/jev-semgrep) - Semantic grep across languages with AND, OR, and NOT, asking one Noul per line.

### Data and Workflows

- [Airflow LLM branching](https://github.com/apache/airflow/blob/main/providers/common/ai/docs/classifier_models.rst) - Picks the next task with a Jev Choice and hands low-confidence cases to a person (merged, not yet released).
- [Flyte System One example](https://github.com/flyteorg/flyte-sdk/tree/main/examples/typesafe_ai) - Alternates Jev and an LLM, splitting each task into 11 to 16 atomic questions and routing results to auto, review, or escalate.
- [Inbox Zero classifier](https://github.com/elie222/inbox-zero/blob/main/apps/web/utils/classifier/typesafe.ts) - Replaces two LLM calls per email with one Jev request, a Choice plus a yes-or-no per user rule, with an LLM fallback on errors.
- [n8n TypeSafe node](https://github.com/DomMonte/n8n-nodes-typesafe-ai) - Community node with yes-or-no, choice, and score operations, usable as an AI Agent tool on self-hosted n8n.
- [tax-doc-classifier](https://github.com/kyotofin/tax-doc-classifier) - Sorts PDF pages into IRS form types with two Choices for about a tenth of a cent per page, with error rates on labeled test sets.
- [jev-align](https://github.com/sutro-sh/jev-align) - Turns human labels into reusable, calibrated judgment functions with active learning and prompt optimization.

### Apps and Interfaces

- [json-render](https://json-render.dev/docs/jev) - Generative UI where Jev chooses the root, members, and layout from components the app provides.
- [CopilotKit generative UI cookbook](https://docs.copilotkit.ai/cookbook/jev-generative-ui) - A Choice decides which panel to show and per-candidate Scores order what goes in it.
- [Unclutter](https://github.com/kitze/unclutter) - Browser extension that classifies page elements with a Choice each and hides ads, cookie banners, and other clutter.

### Games and Simulation

- [Temporal tic-tac-toe agent](https://github.com/temporal-community/temporal-agent-harness/tree/main/examples/tictactoe) - Game agent with no LLM, where a Choice picks the square, Nouls spot threats, and a Score rates the position.
- [typesafe-mario](https://github.com/fhshaik/typesafe-mario) - Plays Super Mario with a Choice for the controller action, a jump Noul, and a danger Score.
- [JevPilot](https://github.com/standardagents/jevpilot) - Three.js driving simulator where Jev picks motion and direction as the autopilot.

### Examples and Skills

- [AI cookbook for Jev](https://github.com/daveebbelaar/ai-cookbook/tree/main/models/jev) - Nine runnable examples plus the four official patterns, written against the current Python SDK.
- [Jev experiments](https://github.com/dabit3/jev-experiments) - Twenty-one low-latency demo apps, such as reranking 50 candidates in a single request.
- [Building with Jev skill](https://github.com/dbreunig/building-with-jev-skill) - Compact agent skill that teaches coding agents to structure programs around Jev.

## Open Models and Compatible Servers

Community models and servers that imitate Jev's interface. Their accuracy and calibration are self-reported and generally below Jev's, so evaluate them on your own data.

- [Kev](https://github.com/jaredpalmer/kev) - Open 0.8B to 9B decision models on Qwen3.5 with released weights and a server compatible with `/v1/systemone`, so the official SDKs can point at it.
- [SemIf](https://github.com/TheoLeeCJ/SemIf) - Reads option logits from frozen open models, with WebGPU and MLX runtimes and its own request format.
- [openjev-sglang](https://github.com/ekzhang/openjev-sglang) - Compatible endpoint that serves an open mixture-of-experts model on SGLang, with BoolQ and MMLU-Pro comparisons.
- [Jeff](https://github.com/logan-markewich/jeff) - Compatible server built on a 400M-parameter encoder, with benchmark comparisons against Jev.
- [simple-jev](https://github.com/featherless-ai/simple-jev) - Turns any Hugging Face model into a decision endpoint with a `/v1/systemone` alias (probabilities are not calibrated).
- [NanoJev](https://github.com/TianyuCodings/NanoJev) - 0.6B replica trained for four specific games, with weights and data; not a general-purpose substitute.
- [Jev reproductions tracker](https://huggingface.co/spaces/multimodalart/jev-reproductions-tracker) - Hugging Face space that tracks open reproductions and their reported results.

## Articles and Talks

### Guides

- [How to classify, route, and score with Jev and AI SDK](https://vercel.com/kb/guide/typesafe-jev-and-ai-sdk) - Mixes choice, score, and yes-or-no judgments in one AI SDK call, dispatches only above a confidence bar, and unit-tests the thresholds with a mock model.
- [A deep dive into Jev](https://flaviocopes.com/jev/) - Thorough walkthrough of request and response shapes, picking a primitive, error codes, version pinning, and limits.
- [How to use Jev: a practical guide](https://dev.to/valyuai/how-to-use-jev-a-practical-guide-to-typesafes-system-one-model-g5e) - Five patterns with code: speculative fan-out, per-action confidence gates, composite scoring, cascades, and retrieve-then-judge.
- [Building a harness with Jev](https://www.langchain.com/blog/building-a-harness-with-jev) - LangChain's Jev classifier, a per-request model router middleware, and a middleware that stops risky tool calls before they run.
- [Using TypeSafe's Jev for evals](https://langfuse.com/blog/2026-09-18-using-typesafes-jev-for-evals) - Grades agent runs with a Noul, a Score, and a Choice in one request and writes the results back as Langfuse scores.

### Techniques and Analysis

- [Two techniques for working with System One models](https://www.seangoedecke.com/two-techniques-for-working-with-system-one-models/) - Layered goals, where a slow loop picks the goal and a fast loop picks actions, plus tournament sampling over batches of options, shown on a Doom agent built with an open-model imitation.
- [Jev means structured output is interesting again](https://www.seangoedecke.com/jev-means-structured-output-is-interesting-again/) - Why a decision model has steady latency, and how far prefill plus single-token constrained decoding gets you with open models.
- [Jev at the branches](https://stacktoheap.com/blog/2026/09/21/the-state-machine-is-the-agent/) - A state machine owns the plan and the legal transitions while Jev only chooses among open branches, with stricter margins on risky moves.
- [Is Jev confident?](https://bernoulli.app/articles/is-jev-confident) - Reverse-engineers how Choice confidence is computed from hundreds of thousands of live answers and shows how padding the option list inflates it.

### Benchmarks and Case Studies

- [Jev jailbreak benchmark](https://backnotprop.com/blog/jev-guardrails/) - Pits one Noul per message against four local injection detectors, finding strong ranking but little recall at a 1% false-positive rate.
- [An early-access test of Jev](https://lindfors.no/blog/a-first-look-at-typesafes-jev/) - Scores Norwegian documents with Score questions at about $0.22 per thousand and finds that longer, more detailed questions hurt calibration.
- [Typed judgments or agentic loops?](https://blog.r6i.it/typesafe-jev-vs-agentic-loop.html) - Hierarchical Choices with fan-out against a GPT tool-calling agent, cutting average latency from 9.62 s to 1.38 s.
- [Jev vs. classical ML](https://quicqdev.github.io/Jev-vs-ML/) - Eight datasets against eleven classical pipelines, strong on text such as IMDb reviews and weak on tabular data, with notebooks.
- [System One models in high-throughput data pipelines](https://www.southbridge.ai/blog/jev-entity-resolution) - Entity resolution with Jev doing the bulk work and an LLM reviewing, at 226x lower cost; rewriting criteria as "what counts as sufficient evidence" fixed the dev set.
- [Models watching models](https://www.southbridge.ai/blog/jev-watching-the-agents) - Flags risky calls across 220,000 agent tool calls, shows that encoding tricks slip past it, and finds worded scales beat 1-to-100 ratings.
- [Rebuilding Nym's agent around Jev](https://usenym.com/technical-blog/rebuilding-our-agent-with-jev) - Replaces seven LLM reviewers and tool selection with Jev, falling back to a larger model when unsure, for a 4.1 to 5.7x speedup.
- [Fine-tuning side quests Jev could have removed](https://kasra.blog/blog/classification-and-jev/) - Filters 120,633 training examples with three Nouls in 23 minutes for $3.47.
- [A different kind of model for AI observability](https://fatliverfreddy.substack.com/p/a-different-kind-of-model-for-ai) - Labels 10,000 agent traces for status and sentiment in about 17 minutes for under a dollar and compares accuracy with an evaluation model.
- [Hermes Agent compaction scorecard](https://github.com/NousResearch/hermes-agent/blob/main/evals/compaction/results/SCORECARD-2026-09-19-jev.md) - Tests a Jev-based context-compaction plugin against Hermes' own compressor and recommends against it: far cheaper and faster per compaction, but it kept twice the context and ranked tool results no better than recency.
- [Can a fast AI gate catch chemistry mistakes?](https://frederickparsons.substack.com/p/can-a-fast-ai-gate-catch-chemistry) - A literature-claim gate that stopped all 42 bad claims at a 95% threshold, with an honest account of where molecule checks failed.

### Talks and Videos

- [What's next after RLHF?](https://www.youtube.com/watch?v=cJ0EOzey--o) - TypeSafe's CEO at AI Engineer World's Fair 2026 on training models for calibrated decisions instead of human approval.
- [Jev explained: demos and use cases](https://www.youtube.com/watch?v=QbYBRjOaGOo) - Demos including a model router and a chatbot with no LLM behind it, with companion code.
- [What is Jev and how to use it?](https://www.youtube.com/watch?v=ZgXej_9isxY) - Hands-on Playground and TypeScript SDK walkthrough with a companion repository.

### Discussions

- [Launch thread on Hacker News](https://news.ycombinator.com/item?id=49717558) - Nearly 2,000 points and about 500 comments, with the TypeSafe team answering questions about semantics and limits.
- [Kev thread on Hacker News](https://news.ycombinator.com/item?id=49783999) - Debate around an open family of Jev-like decision models built on Qwen3.5.

## Related Lists

- [yibie/awesome-jev](https://github.com/yibie/awesome-jev) - Large community list organized by application area.
- [Awesome Jev / TypeSafe](https://github.com/AbdelStark/awesome-typesafe-jev) - Source-backed field guide with a website and machine-readable data.
- [cobanov/awesome-jev](https://github.com/cobanov/awesome-jev) - Community list organized by integration and project type.
- [awesome-jev-zh](https://github.com/yzfly/awesome-jev-zh) - Chinese-language list with a getting-started guide.
- [Built with Jev](https://academy.dair.ai/resources/jev-field-notes) - DAIR.AI's regularly updated gallery of community demos, each with caveats.

## Contributing

Contributions welcome! Read the [contribution guidelines](contributing.md) first, or [suggest a resource](https://github.com/Li-Evan/awesome-jev/issues/new/choose) through an issue.
