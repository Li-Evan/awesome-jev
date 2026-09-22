# Awesome Jev [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> [Jev](https://typesafe.ai) is TypeSafe's System One model. It answers typed questions about text with calibrated probabilities instead of generating prose, so code can branch, sort, and route on its judgments.

The most complete collection of what people build with Jev: **3,426 projects, demos, posts, and write-ups**, gathered from GitHub, X, Reddit, Hacker News, YouTube, and the web, and organized by scenario. Every entry links to its original source and says what it does. Jev has three primitives: **Choice** picks one option, **Score** places something on an ordered scale, and **Noul** gives the probability that a statement is true.

This list is community-maintained and not affiliated with TypeSafe. The official sites are `typesafe.ai` and `docs.typesafe.ai`, and the official GitHub organization is `typesafe-ai`. Be careful with look-alike domains that claim to be official.

## Contents

- [Getting Started](#getting-started)
- [Browse by Scenario](#browse-by-scenario)
  - [💰 Finance and Trading](#-finance-and-trading)
  - [💻 Coding and Developer Tools](#-coding-and-developer-tools)
  - [🌐 Browser and Computer Use](#-browser-and-computer-use)
  - [🤖 Agents and Orchestration](#-agents-and-orchestration)
  - [🎮 Games and Interactive](#-games-and-interactive)
  - [🦾 Robotics and Simulation](#-robotics-and-simulation)
  - [🔎 Search and RAG](#-search-and-rag)
  - [🛡️ Safety and Moderation](#-safety-and-moderation)
  - [📊 Data and Evaluation](#-data-and-evaluation)
  - [🎧 Customer Support and Sales](#-customer-support-and-sales)
  - [⚖️ Legal, Health, and Science](#-legal-health-and-science)
  - [🛍️ Commerce and Marketing](#-commerce-and-marketing)
  - [✍️ Writing, Media, and Creative](#-writing-media-and-creative)
  - [🗣️ Voice and Real-Time Interfaces](#-voice-and-real-time-interfaces)
  - [🧰 Personal Productivity](#-personal-productivity)
  - [🎓 Education](#-education)
  - [🧪 Other Experiments](#-other-experiments)
- [Open Models and Compatible Servers](#open-models-and-compatible-servers)
- [Build with Jev](#build-with-jev)
  - [Model Access](#model-access)
  - [Framework Adapters](#framework-adapters)
  - [Observability](#observability)
  - [Community SDKs](#community-sdks)
- [Learn](#learn)
  - [Official Docs](#official-docs)
  - [Official SDKs and Tools](#official-sdks-and-tools)
  - [Announcements](#announcements)
  - [Patterns](#patterns)
  - [Official Cookbooks](#official-cookbooks)
  - [Examples and Skills](#examples-and-skills)
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

## Browse by Scenario

Highlights are ranked by community traction (stars, likes, points, and views). Open a scenario for its full gallery.

<table>
<tr><td><a href="https://github.com/Li-Evan/awesome-jev/blob/main/scenarios/finance.md">💰 Finance and Trading</a> <sub>89</sub></td><td><a href="https://github.com/Li-Evan/awesome-jev/blob/main/scenarios/coding.md">💻 Coding and Developer Tools</a> <sub>515</sub></td><td><a href="https://github.com/Li-Evan/awesome-jev/blob/main/scenarios/browser.md">🌐 Browser and Computer Use</a> <sub>128</sub></td><td><a href="https://github.com/Li-Evan/awesome-jev/blob/main/scenarios/agents.md">🤖 Agents and Orchestration</a> <sub>246</sub></td></tr>
<tr><td><a href="https://github.com/Li-Evan/awesome-jev/blob/main/scenarios/games.md">🎮 Games and Interactive</a> <sub>276</sub></td><td><a href="https://github.com/Li-Evan/awesome-jev/blob/main/scenarios/robotics.md">🦾 Robotics and Simulation</a> <sub>61</sub></td><td><a href="https://github.com/Li-Evan/awesome-jev/blob/main/scenarios/search.md">🔎 Search and RAG</a> <sub>86</sub></td><td><a href="https://github.com/Li-Evan/awesome-jev/blob/main/scenarios/safety.md">🛡️ Safety and Moderation</a> <sub>128</sub></td></tr>
<tr><td><a href="https://github.com/Li-Evan/awesome-jev/blob/main/scenarios/data.md">📊 Data and Evaluation</a> <sub>135</sub></td><td><a href="https://github.com/Li-Evan/awesome-jev/blob/main/scenarios/support.md">🎧 Customer Support and Sales</a> <sub>44</sub></td><td><a href="https://github.com/Li-Evan/awesome-jev/blob/main/scenarios/legal-health.md">⚖️ Legal, Health, and Science</a> <sub>28</sub></td><td><a href="https://github.com/Li-Evan/awesome-jev/blob/main/scenarios/commerce.md">🛍️ Commerce and Marketing</a> <sub>45</sub></td></tr>
<tr><td><a href="https://github.com/Li-Evan/awesome-jev/blob/main/scenarios/creative.md">✍️ Writing, Media, and Creative</a> <sub>134</sub></td><td><a href="https://github.com/Li-Evan/awesome-jev/blob/main/scenarios/voice.md">🗣️ Voice and Real-Time Interfaces</a> <sub>54</sub></td><td><a href="https://github.com/Li-Evan/awesome-jev/blob/main/scenarios/productivity.md">🧰 Personal Productivity</a> <sub>128</sub></td><td><a href="https://github.com/Li-Evan/awesome-jev/blob/main/scenarios/education.md">🎓 Education</a> <sub>10</sub></td></tr>
<tr><td><a href="https://github.com/Li-Evan/awesome-jev/blob/main/scenarios/other.md">🧪 Other Experiments</a> <sub>46</sub></td></tr>
</table>

### 💰 Finance and Trading

Trading agents, market signals, fraud and risk checks, and financial document processing.

<table>
<tr>
<td width="33%" valign="top"><a href="https://x.com/MoonGotchi/status/2101320141065609294"><img src="https://pbs.twimg.com/amplify_video_thumb/2101320107947401216/img/4Uj1jx6q_1O7MusA.jpg" alt="Autonomous onchain trading bot" width="100%"></a><br><b><a href="https://x.com/MoonGotchi/status/2101320141065609294">Autonomous onchain trading bot</a></b><br><sub>MoonGotchi · X · ♥ 23.9k · 2026-09-19</sub><br>Fully autonomous real-time trading bot built in an evening that ingests onchain and offchain data to make rapid trade decisions; the author reports it has lost $31,680 so far.</td>
<td width="33%" valign="top"><a href="https://x.com/abolbuild/status/2100523868913807410"><img src="https://pbs.twimg.com/amplify_video_thumb/2100523731923722240/img/b6b47us-K3FIDHDC.jpg" alt="Jev trading with $10,000" width="100%"></a><br><b><a href="https://x.com/abolbuild/status/2100523868913807410">Jev trading with $10,000</a></b><br><sub>abolbuild · X · ♥ 1.6k · 2026-09-17</sub><br>Experimental trading agent that hands Jev a $10,000 balance and lets it make the trading decisions, shown in a demo video.</td>
<td width="33%" valign="top"><a href="https://github.com/kyotofin/tax-doc-classifier"><img src="https://pbs.twimg.com/amplify_video_thumb/2100973360989773825/img/yMtL6CxrKMVXQEHV.jpg" alt="tax-doc-classifier" width="100%"></a><br><b><a href="https://github.com/kyotofin/tax-doc-classifier">tax-doc-classifier</a></b><br><sub>kyotofin · GitHub · ⭐ 351 · 2026-09-18</sub><br>Sorts PDF pages into IRS form types with two Choices for about a tenth of a cent per page, with error rates on labeled test sets.</td>
</tr>
<tr>
<td width="33%" valign="top"><a href="https://x.com/SUOHA_AI/status/2101275294451515740"><img src="https://pbs.twimg.com/amplify_video_thumb/2101274788513693696/img/Gj7UchuQIdpkqvAz.jpg" alt="Jev Trader (Inverse)" width="100%"></a><br><b><a href="https://x.com/SUOHA_AI/status/2101275294451515740">Jev Trader (Inverse)</a></b><br><sub>SUOHA_AI · X · ♥ 454 · 2026-09-19</sub><br>Inverse version of the Monad Jev trading demo that mirrors every order, selling when the original buys and buying when it sells, one decision per block.</td>
<td width="33%" valign="top"><a href="https://x.com/abolbuild/status/2100690370912805049"><img src="https://pbs.twimg.com/amplify_video_thumb/2100688652665806848/img/1aEeVftB38YD0AWr.jpg" alt="Jev trades BTC with $10,000" width="100%"></a><br><b><a href="https://x.com/abolbuild/status/2100690370912805049">Jev trades BTC with $10,000</a></b><br><sub>abolbuild · X · ♥ 392 · 2026-09-17</sub><br>Experiment giving Jev $10,000 to trade BTC for 30 days, with market data, derivatives, macro, on-chain data, news and sentiment as inputs.</td>
<td width="33%" valign="top"><a href="https://x.com/tommy_jepsen/status/2100939646653903063"><img src="https://pbs.twimg.com/amplify_video_thumb/2100938100272746496/img/8yisuerchTVTcFTn.jpg" alt="Danish stock-market backtest" width="100%"></a><br><b><a href="https://x.com/tommy_jepsen/status/2100939646653903063">Danish stock-market backtest</a></b><br><sub>tommy_jepsen · X · ♥ 850 · 2026-09-18</sub><br>Backtest of Jev trading the Danish stock market for all of 2025 (239 trading days) on sentiment from market data, news, Wikipedia and Google Trends; 8.1 million tokens cost $0.32.</td>
</tr>
</table>

**[Browse all 89 in Finance and Trading →](https://github.com/Li-Evan/awesome-jev/blob/main/scenarios/finance.md)**

### 💻 Coding and Developer Tools

Code review, model routing for coding agents, context compaction, semantic search over code, and CI checks.

<table>
<tr>
<td width="33%" valign="top"><a href="https://github.com/tamaratran/fast-jev-compaction"><img src="https://external-preview.redd.it/MGlnNDRiMG1xYXFoMV6tliTw1N13OJYLOxukOcY6kypXBn-V9gWyZw5eTACt.png?format=pjpg&amp;auto=webp&amp;s=fb4a34a2ae0aa5577c81ee2b59363e6950096c7c" alt="fast-jev-compaction" width="100%"></a><br><b><a href="https://github.com/tamaratran/fast-jev-compaction">fast-jev-compaction</a></b><br><sub>tamaratran · GitHub · ⭐ 6.1k · 2026-09-17</sub><br>Claude Code plugin that replaces the compaction summary with a keep-or-drop Noul per tool call; install it from GitHub, because the npm package with the same name comes from another publisher.</td>
<td width="33%" valign="top"><a href="https://x.com/Neriousy/status/2100287208166969746"><img src="https://pbs.twimg.com/amplify_video_thumb/2100286679386873857/img/vlw6EBlSVZ9uAoHc.jpg" alt="App testing with OpenCode" width="100%"></a><br><b><a href="https://x.com/Neriousy/status/2100287208166969746">App testing with OpenCode</a></b><br><sub>Neriousy · X · ♥ 1.3k · 2026-09-16</sub><br>Demo of fast app testing that pairs Jev with the OpenCode coding agent.</td>
<td width="33%" valign="top"><a href="https://x.com/miu21590/status/2101857866378362926"><img src="https://pbs.twimg.com/amplify_video_thumb/2101857791967178752/img/MiCcd9s5hrptUHqe.jpg" alt="Codex reasoning-effort router" width="100%"></a><br><b><a href="https://x.com/miu21590/status/2101857866378362926">Codex reasoning-effort router</a></b><br><sub>miu21590 · X · ♥ 3k · 2026-09-21</sub><br>Codex setup where Jev changes GPT-6's reasoning effort during a task, adding thinking when stuck and cutting it on routine steps, for 50% lower Astra costs in the author's tests.</td>
</tr>
<tr>
<td width="33%" valign="top"><a href="https://x.com/rafalwilinski/status/2100882207879434359"><img src="https://pbs.twimg.com/amplify_video_thumb/2100881920343105536/img/c1y4THiGwA2GfXGa.jpg" alt="Adversarial browser release testing" width="100%"></a><br><b><a href="https://x.com/rafalwilinski/status/2100882207879434359">Adversarial browser release testing</a></b><br><sub>rafalwilinski · X · ♥ 5.4k · 2026-09-18</sub><br>Massively parallel browser-based adversarial test suite that tries to break each software release, costing pennies per run.</td>
<td width="33%" valign="top"><a href="https://x.com/redp314/status/2100585126652481915"><img src="https://pbs.twimg.com/amplify_video_thumb/2100585029533372416/img/ZcrsntW2yWgtB_HD.jpg" alt="Jev PR reviewer" width="100%"></a><br><b><a href="https://x.com/redp314/status/2100585126652481915">Jev PR reviewer</a></b><br><sub>redp314 · X · ♥ 2.8k · 2026-09-17</sub><br>PR reviewer that sends a diff to Jev in one call and gets 14 typed checks back as probabilities, mapped to block, security review, nits or merge, for $0.00007 per PR.</td>
<td width="33%" valign="top"><a href="https://x.com/dani_avila7/status/2101176629745561686"><img src="https://pbs.twimg.com/amplify_video_thumb/2101176234411425792/img/UgEWGdQPunczzXcv.jpg" alt="Jev Model Router for Claude Code" width="100%"></a><br><b><a href="https://x.com/dani_avila7/status/2101176629745561686">Jev Model Router for Claude Code</a></b><br><sub>dani_avila7 · X · ♥ 1.4k · 2026-09-19</sub><br>Claude Code mod that has Jev classify the subagent model, main model (only at session start to keep the cache) and effort level for every request, via the TypeSafe API or Vercel AI Gateway.</td>
</tr>
</table>

**[Browse all 515 in Coding and Developer Tools →](https://github.com/Li-Evan/awesome-jev/blob/main/scenarios/coding.md)**

### 🌐 Browser and Computer Use

Agents that click, type, and navigate real browsers, desktops, and phones.

<table>
<tr>
<td width="33%" valign="top"><a href="https://github.com/browser-use/jev-ultrafast"><img src="https://raw.githubusercontent.com/browser-use/jev-ultrafast/main/docs/banner.svg" alt="jev-ultrafast" width="100%"></a><br><b><a href="https://github.com/browser-use/jev-ultrafast">jev-ultrafast</a></b><br><sub>browser-use · GitHub · ⭐ 16.6k · 2026-09-16</sub><br>Browser agent that picks each step's operation and target from an element table in one request, with a speculative target per operation and a small LLM only for typed text.</td>
<td width="33%" valign="top"><a href="https://x.com/Saccc_c/status/2100864907046768890"><img src="https://pbs.twimg.com/amplify_video_thumb/2100853279089647616/img/H6altwjZQ28_1bfY.jpg" alt="Jev Use for Codex" width="100%"></a><br><b><a href="https://x.com/Saccc_c/status/2100864907046768890">Jev Use for Codex</a></b><br><sub>Saccc_c · X · ♥ 1.8k · 2026-09-18</sub><br>Computer use for Codex with Jev as the decision layer, shown adding a Mac calendar event faster and more smoothly than Codex's built-in computer use at similar token cost.</td>
<td width="33%" valign="top"><a href="https://x.com/thdxr/status/2100288951978164647"><img src="https://pbs.twimg.com/amplify_video_thumb/2100286679386873857/img/vlw6EBlSVZ9uAoHc.jpg" alt="OpenCode browser use with Jev" width="100%"></a><br><b><a href="https://x.com/thdxr/status/2100288951978164647">OpenCode browser use with Jev</a></b><br><sub>thdxr · X · ♥ 3.7k · 2026-09-16</sub><br>Preview of fast browser automation for app testing that pairs Jev with OpenCode's browser-use CLI.</td>
</tr>
<tr>
<td width="33%" valign="top"><a href="https://github.com/awlevin/typesafe-computer-use"><img src="https://raw.githubusercontent.com/awlevin/typesafe-computer-use/main/docs/banner.svg" alt="typesafe-computer-use" width="100%"></a><br><b><a href="https://github.com/awlevin/typesafe-computer-use">typesafe-computer-use</a></b><br><sub>awlevin · GitHub · ⭐ 769 · 2026-09-16</sub><br>Computer-use agent for macOS that OCRs the screen, has Jev classify the next action from the extracted controls and clicks, for about $0.0002 a step, calling a writing model only for free-text fields.</td>
<td width="33%" valign="top"><a href="https://github.com/milind-soni/tiptour-macos"><img src="https://raw.githubusercontent.com/milind-soni/tiptour-macos/main/gemnew.png" alt="TipTour" width="100%"></a><br><b><a href="https://github.com/milind-soni/tiptour-macos">TipTour</a></b><br><sub>milind-soni · GitHub · ⭐ 644 · 2026-04-08</sub><br>Menu bar computer-use app for macOS whose default mode takes a typed click-based task, has Jev choose among locally detected on-screen controls, then executes and validates each action.</td>
<td width="33%" valign="top"><a href="https://x.com/SUOHA_AI/status/2101640575812239406"><img src="https://pbs.twimg.com/amplify_video_thumb/2101632970717007872/img/lcQeA281BT79Pjt5.jpg" alt="Jev + DeepSeek form-filling agent" width="100%"></a><br><b><a href="https://x.com/SUOHA_AI/status/2101640575812239406">Jev + DeepSeek form-filling agent</a></b><br><sub>SUOHA_AI · X · ♥ 173 · 2026-09-20</sub><br>Browser agent that filled a 16-question application form on an unfamiliar site in 38 seconds, with Jev choosing each action and DeepSeek V4.1 Flash writing the text answers.</td>
</tr>
</table>

**[Browse all 128 in Browser and Computer Use →](https://github.com/Li-Evan/awesome-jev/blob/main/scenarios/browser.md)**

### 🤖 Agents and Orchestration

Tool and skill selection, approvals, planning, memory, and harness decisions for general-purpose agents.

<table>
<tr>
<td width="33%" valign="top"><a href="https://github.com/Significant-Gravitas/AutoGPT/tree/master/autogpt_platform/backend/backend/blocks/typesafe"><img src="https://raw.githubusercontent.com/Significant-Gravitas/AutoGPT/master/docs/home/.gitbook/assets/Banner_image.png" alt="AutoGPT TypeSafe blocks" width="100%"></a><br><b><a href="https://github.com/Significant-Gravitas/AutoGPT/tree/master/autogpt_platform/backend/backend/blocks/typesafe">AutoGPT TypeSafe blocks</a></b><br><sub>Significant-Gravitas · GitHub · ⭐ 187.5k repo · 2023-03-16</sub><br>Seven no-code blocks, including a five-exit router, a yes, no, or unsure split, and a score filter.</td>
<td width="33%" valign="top"><a href="https://x.com/0xCodila/status/2101433560796467348"><img src="https://pbs.twimg.com/amplify_video_thumb/2101426271842349056/img/uEiR8K0UCaFoYsf-.jpg" alt="jev-usage-router" width="100%"></a><br><b><a href="https://x.com/0xCodila/status/2101433560796467348">jev-usage-router</a></b><br><sub>0xCodila · X · ♥ 2.4k · 2026-09-19</sub><br>Usage router for Grok Bot: before browsing, research, retries or spawning extra bots, a Jev Choice picks the route, with a shadow mode, logs and a kill switch before it goes active.</td>
<td width="33%" valign="top"><a href="https://x.com/_aj/status/2102061534956662818"><img src="https://pbs.twimg.com/media/HSwFAsyawAA4tst.jpg?name=orig" alt="AgentRun" width="100%"></a><br><b><a href="https://x.com/_aj/status/2102061534956662818">AgentRun</a></b><br><sub>_aj · X · ♥ 1.6k · 2026-09-21</sub><br>Harness from Grep.ai for repetitive knowledge work that learns the job as it runs, moving steps from LLM calls to code; 100,000 compliance alerts cost under $26K versus over $290K on Opus 5.</td>
</tr>
<tr>
<td width="33%" valign="top"><a href="https://x.com/eve/status/2100430918762832180"><img src="https://pbs.twimg.com/media/HSY6yf5a8AA8NJi.jpg?name=orig" alt="Criteria-based model routing in eve" width="100%"></a><br><b><a href="https://x.com/eve/status/2100430918762832180">Criteria-based model routing in eve</a></b><br><sub>eve · X · ♥ 910 · 2026-09-17</sub><br>Experimental autoModel option in the eve agent framework that uses Jev to route each request between models described by plain-language criteria.</td>
<td width="33%" valign="top"><a href="https://x.com/ephraimduncan/status/2100454070536351824"><img src="https://pbs.twimg.com/amplify_video_thumb/2100454021852954624/img/hqULLONlXw40573G.jpg" alt="Jev model router" width="100%"></a><br><b><a href="https://x.com/ephraimduncan/status/2100454070536351824">Jev model router</a></b><br><sub>ephraimduncan · X · ♥ 1.9k · 2026-09-17</sub><br>Model router that asks Jev which language model best fits each incoming request and forwards the request to that model, shown in a demo video.</td>
<td width="33%" valign="top"><a href="https://x.com/CodingGarden/status/2100665210419950031"><img src="https://pbs.twimg.com/amplify_video_thumb/2100664410935332864/img/KPApgq0AysL_SFeg.jpg" alt="Chat bot with no LLM" width="100%"></a><br><b><a href="https://x.com/CodingGarden/status/2100665210419950031">Chat bot with no LLM</a></b><br><sub>CodingGarden · X · ♥ 1.2k · 2026-09-17</sub><br>Chat assistant built without any LLM: Jev picks the tool and its arguments across web search, Wikipedia, weather, Todoist and Home Assistant, so cited answers arrive instantly.</td>
</tr>
</table>

**[Browse all 246 in Agents and Orchestration →](https://github.com/Li-Evan/awesome-jev/blob/main/scenarios/agents.md)**

### 🎮 Games and Interactive

Game-playing agents, real-time decisions, and playful interactive demos.

<table>
<tr>
<td width="33%" valign="top"><a href="https://x.com/CompleteSkeptic/status/2099925687465570372"><img src="https://pbs.twimg.com/amplify_video_thumb/2099924592534183936/img/hBGk8j8MRxBgPyg9.jpg" alt="Jev plays Doom" width="100%"></a><br><b><a href="https://x.com/CompleteSkeptic/status/2099925687465570372">Jev plays Doom</a></b><br><sub>CompleteSkeptic · X · ♥ 5k · 2026-09-15</sub><br>TypeSafe's launch demo of Jev playing Doom in real time from structured game state, making about 10 calls per second for roughly $7 per hour.</td>
<td width="33%" valign="top"><a href="https://x.com/CompleteSkeptic/status/2099925688925184171"><img src="https://pbs.twimg.com/amplify_video_thumb/2099924665515012096/img/Q3mdVD5jfOZOkMww.jpg" alt="Wikipedia race" width="100%"></a><br><b><a href="https://x.com/CompleteSkeptic/status/2099925688925184171">Wikipedia race</a></b><br><sub>CompleteSkeptic · X · ♥ 2.6k · 2026-09-15</sub><br>Launch demo in which Jev races from one Wikipedia page to another using only links, choosing among hundreds to thousands of links at each step.</td>
<td width="33%" valign="top"><a href="https://github.com/fhshaik/typesafe-mario"><img src="https://external-preview.redd.it/bzVydG83cHlodXBoMZE7fOmaTIl8CDi0AASExP3Al1xQRlZJ2gAIQDJfa5Lr.png?format=pjpg&amp;auto=webp&amp;s=2ba386e6d1e858b09755e0c4f9ecbb8adbfc0c15" alt="typesafe-mario" width="100%"></a><br><b><a href="https://github.com/fhshaik/typesafe-mario">typesafe-mario</a></b><br><sub>fhshaik · GitHub · ⭐ 338 · 2026-09-16</sub><br>Plays Super Mario with a Choice for the controller action, a jump Noul, and a danger Score.</td>
</tr>
<tr>
<td width="33%" valign="top"><a href="https://x.com/aimlapi/status/2100372930282573876"><img src="https://pbs.twimg.com/amplify_video_thumb/2100371773275406336/img/NmHPy0pAprSsC6Gi.jpg" alt="Jev vs Fable 5.1 vs GPT-6 Astra chess" width="100%"></a><br><b><a href="https://x.com/aimlapi/status/2100372930282573876">Jev vs Fable 5.1 vs GPT-6 Astra chess</a></b><br><sub>aimlapi · X · ♥ 2.3k · 2026-09-16</sub><br>Blitz chess at 5+0 with one API call per move: Jev lost on material to Fable 5.1 but won on time at ~2.6s per move, and was mated by GPT-6 Astra in 18 moves.</td>
<td width="33%" valign="top"><a href="https://www.spritefusion.com/blog/generating-game-level-in-real-time-with-jev"><img src="https://www.spritefusion.com/blog/generating-game-level-in-real-time-with-jev/jev-terrain-generation.png" alt="Real-time level generation with Jev" width="100%"></a><br><b><a href="https://www.spritefusion.com/blog/generating-game-level-in-real-time-with-jev">Real-time level generation with Jev</a></b><br><sub>Hugo Duprez (Sprite Fusion) · Article · ♥ 2.8k · 2026-09-18</sub><br>Endless platformer whose terrain is generated in real time from game state, with Jev choosing each segment's width, gap, height and tile type while game code places the tiles.</td>
<td width="33%" valign="top"><a href="https://x.com/_MaxBlade/status/2100634359099232678"><img src="https://pbs.twimg.com/amplify_video_thumb/2100633400717565952/img/KlytLNSLCQA-yY2E.jpg" alt="Jev plays Subway Surfers" width="100%"></a><br><b><a href="https://x.com/_MaxBlade/status/2100634359099232678">Jev plays Subway Surfers</a></b><br><sub>_MaxBlade · X · ♥ 4.1k · 2026-09-17</sub><br>Jev playing Subway Surfers at superhuman speed, including 50 games at once, with the whole run costing less than a cent.</td>
</tr>
</table>

**[Browse all 276 in Games and Interactive →](https://github.com/Li-Evan/awesome-jev/blob/main/scenarios/games.md)**

### 🦾 Robotics and Simulation

Embodied control, driving simulators, and decisions in the physical world.

<table>
<tr>
<td width="33%" valign="top"><a href="https://x.com/leojrr/status/2101161666410893328"><img src="https://pbs.twimg.com/amplify_video_thumb/2101161072447180800/img/sRIOALT11TUpdAdU.jpg" alt="Traffic-light control" width="100%"></a><br><b><a href="https://x.com/leojrr/status/2101161666410893328">Traffic-light control</a></b><br><sub>leojrr · X · ♥ 7k · 2026-09-19</sub><br>City simulation in which Jev controls every traffic light; turning it off raises the average wait time by more than 600%.</td>
<td width="33%" valign="top"><a href="https://x.com/Raptor_zip/status/2101091398447505567"><img src="https://pbs.twimg.com/amplify_video_thumb/2101070240444772353/img/Ci_PCLcMigmoAdks.jpg" alt="Jev dual-arm robot control" width="100%"></a><br><b><a href="https://x.com/Raptor_zip/status/2101091398447505567">Jev dual-arm robot control</a></b><br><sub>Raptor_zip · X · ♥ 432 · 2026-09-18</sub><br>Dual-arm robot where Jev handles the decision layer of a three-layer controller while IK and physics stay in code, responding in 500ms at about 0.5 yen per trial.</td>
<td width="33%" valign="top"><a href="https://github.com/standardagents/jevpilot"><img src="https://raw.githubusercontent.com/standardagents/jevpilot/main/docs/try-jevpilot.svg" alt="JevPilot" width="100%"></a><br><b><a href="https://github.com/standardagents/jevpilot">JevPilot</a></b><br><sub>standardagents · GitHub · ⭐ 160 · 2026-09-17</sub><br>Three.js driving simulator where Jev picks motion and direction as the autopilot.</td>
</tr>
<tr>
<td width="33%" valign="top"><a href="https://x.com/SigGravitas/status/2100325221932958134"><img src="https://pbs.twimg.com/amplify_video_thumb/2100323655389474816/img/LLOAJ3wie1phk45K.jpg" alt="Jev drives in real time" width="100%"></a><br><b><a href="https://x.com/SigGravitas/status/2100325221932958134">Jev drives in real time</a></b><br><sub>SigGravitas · X · ♥ 288 · 2026-09-16</sub><br>Jev wired to the raw controls of a driving simulator that never pauses while it thinks, steering a moving vehicle in real time.</td>
<td width="33%" valign="top"><a href="https://github.com/openroboto-ai/jev-robot-control"><img src="https://raw.githubusercontent.com/openroboto-ai/jev-robot-control/main/media/final.png" alt="Jev robot control" width="100%"></a><br><b><a href="https://github.com/openroboto-ai/jev-robot-control">Jev robot control</a></b><br><sub>openroboto-ai · GitHub · ⭐ 39 · 2026-09-19</sub><br>MuJoCo run where Jev 1.13, GPT-6 Astra, and GPT-4.1 mini steer an xArm7 to put an apple on a plate by choosing motion directions and gripper commands; Jev placed it for $0.018825 versus $5.933624.</td>
<td width="33%" valign="top"><a href="https://x.com/dimentary/status/2101018760371171420"><img src="https://pbs.twimg.com/amplify_video_thumb/2101017646154366976/img/02bH3Hxy9l0qEffS.jpg" alt="Jev MuJoCo arm policy" width="100%"></a><br><b><a href="https://x.com/dimentary/status/2101018760371171420">Jev MuJoCo arm policy</a></b><br><sub>dimentary · X · ♥ 624 · 2026-09-18</sub><br>Test of Jev as a real-time robot-arm policy in MuJoCo, splitting each update into two calls (what to do next, then how to move arm and gripper) from text geometry and contacts.</td>
</tr>
</table>

**[Browse all 61 in Robotics and Simulation →](https://github.com/Li-Evan/awesome-jev/blob/main/scenarios/robotics.md)**

### 🔎 Search and RAG

Reranking, retrieval filtering, semantic search, and knowledge graphs.

<table>
<tr>
<td width="33%" valign="top"><a href="https://x.com/Saboo_Shubham_/status/2101576462042366114"><img src="https://pbs.twimg.com/amplify_video_thumb/2101576307352203264/img/THdpZUHOSRsSoTVr.jpg" alt="Semantic Find (⌘F) extension" width="100%"></a><br><b><a href="https://x.com/Saboo_Shubham_/status/2101576462042366114">Semantic Find (⌘F) extension</a></b><br><sub>Saboo_Shubham_ · X · ♥ 2.3k · 2026-09-20</sub><br>Open-source Chrome extension that replaces Find on page with semantic matching, highlighting passages that mean what you typed in near real time.</td>
<td width="33%" valign="top"><a href="https://github.com/superagents-lab/jev-search"><img src="https://raw.githubusercontent.com/superagents-lab/jev-search/main/public/og-home.png" alt="jev-search" width="100%"></a><br><b><a href="https://github.com/superagents-lab/jev-search">jev-search</a></b><br><sub>superagents-lab · GitHub · ⭐ 387 · 2026-09-17</sub><br>Natural-language web search that picks the time range and query with Choices and keeps each source only if its Noul passes (needs a Search1API key).</td>
<td width="33%" valign="top"><a href="https://x.com/venturetwins/status/2101341075684434245"><img src="https://pbs.twimg.com/amplify_video_thumb/2101339712464326656/img/A8yq5IoXQuhJAi32.jpg" alt="Zillow natural-language search" width="100%"></a><br><b><a href="https://x.com/venturetwins/status/2101341075684434245">Zillow natural-language search</a></b><br><sub>venturetwins · X · ♥ 949 · 2026-09-19</sub><br>Scans thousands of Zillow listings and classifies them by things the site has no filter for, like architecture, renovation status or distance to freeways, in under 20 seconds for $0.18.</td>
</tr>
<tr>
<td width="33%" valign="top"><a href="https://github.com/volcengine/OpenViking/blob/main/openviking/models/rerank/jev_rerank.py"><img src="https://raw.githubusercontent.com/volcengine/OpenViking/main/docs/images/ov-logo.png" alt="OpenViking reranker" width="100%"></a><br><b><a href="https://github.com/volcengine/OpenViking/blob/main/openviking/models/rerank/jev_rerank.py">OpenViking reranker</a></b><br><sub>volcengine · GitHub · ⭐ 38.4k repo · 2026-01-05</sub><br>Rerank provider for a context database that scores every document with a Noul in one request.</td>
<td width="33%" valign="top"><a href="https://github.com/vectorize-io/hindsight/blob/main/hindsight-api-slim/hindsight_api/engine/cross_encoder.py"><img src="https://raw.githubusercontent.com/vectorize-io/hindsight/main/hindsight-docs/static/img/hindsight-github-banner.png" alt="Hindsight Jev reranker" width="100%"></a><br><b><a href="https://github.com/vectorize-io/hindsight/blob/main/hindsight-api-slim/hindsight_api/engine/cross_encoder.py">Hindsight Jev reranker</a></b><br><sub>vectorize-io · GitHub · ⭐ 24.9k repo · 2025-10-30</sub><br>Reranker provider in the Hindsight agent-memory system that asks Jev one question with every recall candidate as an option, so the answer is the ranking, in a single request.</td>
<td width="33%" valign="top"><a href="https://x.com/VisheshBaghell/status/2100536228827496721"><img src="https://pbs.twimg.com/amplify_video_thumb/2100535993141239808/img/Q_giQHiIdU-aAvI6.jpg" alt="Upweight" width="100%"></a><br><b><a href="https://x.com/VisheshBaghell/status/2100536228827496721">Upweight</a></b><br><sub>VisheshBaghell · X · ♥ 73 · 2026-09-17</sub><br>Hacker News front page you re-rank with six sliders (technical depth, drama, practical utility, AI slop, novelty, career relevance), with each story's Jev scores shown; Firecrawl does the reading.</td>
</tr>
</table>

**[Browse all 86 in Search and RAG →](https://github.com/Li-Evan/awesome-jev/blob/main/scenarios/search.md)**

### 🛡️ Safety and Moderation

Guardrails, jailbreak and injection screening, content moderation, and policy checks.

<table>
<tr>
<td width="33%" valign="top"><a href="https://x.com/RBilgil/status/2100976648552169805"><img src="https://pbs.twimg.com/amplify_video_thumb/2100976173836533760/img/APDonY80SB2iSYhj.jpg" alt="Real-time slop detector" width="100%"></a><br><b><a href="https://x.com/RBilgil/status/2100976648552169805">Real-time slop detector</a></b><br><sub>RBilgil · X · ♥ 16k · 2026-09-18</sub><br>Real-time detector that flags AI-generated slop in the feed while you scroll, powered by Jev.</td>
<td width="33%" valign="top"><a href="https://x.com/rauchg/status/2100307962262872105"><img src="https://pbs.twimg.com/media/HSW-E8wWgAAyw9O.jpg?name=orig" alt="fx auto-mode safety reviewer" width="100%"></a><br><b><a href="https://x.com/rauchg/status/2100307962262872105">fx auto-mode safety reviewer</a></b><br><sub>rauchg · X · ♥ 3.9k · 2026-09-16</sub><br>Safety reviewer that checks every command in the fx coding agent's auto mode; Jev benchmarked up to 18x faster at p95 and more accurate than the GPT Luna model it replaces.</td>
<td width="33%" valign="top"><a href="https://github.com/dubinc/dub/blob/main/apps/web/lib/api/links/malicious-link-check.ts"><img src="https://repository-images.githubusercontent.com/529708137/3261d942-ed30-4800-b82c-06e3630ef255" alt="Dub malicious link check" width="100%"></a><br><b><a href="https://github.com/dubinc/dub/blob/main/apps/web/lib/api/links/malicious-link-check.ts">Dub malicious link check</a></b><br><sub>dubinc · GitHub · ⭐ 24.8k repo · 2022-08-27</sub><br>Screens every new short link on the Dub link platform with Jev after a domain blacklist check, blocking phishing, malware, cloaking redirectors, gambling and adult destinations.</td>
</tr>
<tr>
<td width="33%" valign="top"><a href="https://www.reddit.com/r/vibecoding/comments/1wk8jco/using_jev_for_realtime_live_chat_moderation/"><img src="https://external-preview.redd.it/aDk2b3Y5bnpwZHFoMTOXplwNgOesr4K-iFJwFPFaj-sxE-6FkXSkmDW1mccL.png?format=pjpg&amp;auto=webp&amp;s=afac7a4c8fb00d2e7d659fb8bd5f0a05b0b238c1" alt="Real-time chat moderation" width="100%"></a><br><b><a href="https://www.reddit.com/r/vibecoding/comments/1wk8jco/using_jev_for_realtime_live_chat_moderation/">Real-time chat moderation</a></b><br><sub>Rare_Guide_9830 · Reddit · ▲ 264 · 2026-09-19</sub><br>Simulated live-stream chat where Jev sorts each incoming message into viewer-chosen feeds such as Questions, Feedback, or Funny, collapsing repeats and dropping spam.</td>
<td width="33%" valign="top"><a href="https://x.com/jozef_gherman/status/2100627898436571555"><img src="https://pbs.twimg.com/amplify_video_thumb/2100627500082536449/img/v0pfbmvg6HGwc_JF.jpg" alt="Jev Detector" width="100%"></a><br><b><a href="https://x.com/jozef_gherman/status/2100627898436571555">Jev Detector</a></b><br><sub>jozef_gherman · X · ♥ 301 · 2026-09-17</sub><br>Free AI-slop detector that highlights formulaic, generated-sounding sentences in up to about 10,000 words in roughly 2 seconds.</td>
<td width="33%" valign="top"><a href="https://github.com/umputun/tg-spam"><img src="https://github.com/umputun/tg-spam/raw/master/site/tg-spam-bg.png" alt="tg-spam Jev checker" width="100%"></a><br><b><a href="https://github.com/umputun/tg-spam">tg-spam Jev checker</a></b><br><sub>umputun · GitHub · ⭐ 446 · 2023-11-23</sub><br>TG-Spam, a self-hosted Telegram anti-spam bot and library, adds a Jev spam checker that judges each message with a typed question alongside its other detectors.</td>
</tr>
</table>

**[Browse all 128 in Safety and Moderation →](https://github.com/Li-Evan/awesome-jev/blob/main/scenarios/safety.md)**

### 📊 Data and Evaluation

Labeling, classification at scale, data pipelines, observability, and LLM evals.

<table>
<tr>
<td width="33%" valign="top"><a href="https://github.com/realZachi/pg-jev"><img src="https://raw.githubusercontent.com/realZachi/pg-jev/master/docs/assets/header.svg" alt="pg-jev" width="100%"></a><br><b><a href="https://github.com/realZachi/pg-jev">pg-jev</a></b><br><sub>realZachi · GitHub · ⭐ 290 · 2026-09-17</sub><br>PostgreSQL extension for <code>WHERE jev(t, '...')</code> queries that batches 20 rows per request and reports how accuracy falls with larger batches.</td>
<td width="33%" valign="top"><a href="https://github.com/koala73/worldmonitor/blob/main/shared/jev-classify.js"><img src="https://repository-images.githubusercontent.com/1130564872/59ff0927-deb4-4941-8cbc-b68cbe060417" alt="World Monitor Jev headline classifier" width="100%"></a><br><b><a href="https://github.com/koala73/worldmonitor/blob/main/shared/jev-classify.js">World Monitor Jev headline classifier</a></b><br><sub>koala73 · GitHub · ⭐ 87.2k repo · 2026-01-08</sub><br>Headline classifier in a real-time geopolitical news dashboard that asks jev-1.13.0 for a five-level severity and one of 14 topic categories per headline, validating answers and falling back on failure.</td>
<td width="33%" valign="top"><a href="https://x.com/hamiltonulmer/status/2100370557405667768"><img src="https://pbs.twimg.com/media/HSYD5B1bsAAWqeg.jpg?name=orig" alt="DuckDB Jev extension" width="100%"></a><br><b><a href="https://x.com/hamiltonulmer/status/2100370557405667768">DuckDB Jev extension</a></b><br><sub>hamiltonulmer · X · ♥ 1.5k · 2026-09-16</sub><br>DuckDB extension that classifies rows of any CSV, Parquet or DuckDB table with Jev from SQL, taking about 10 seconds for 1k rows.</td>
</tr>
<tr>
<td width="33%" valign="top"><a href="https://github.com/apache/airflow/blob/main/providers/common/ai/docs/classifier_models.rst"><img src="https://raw.githubusercontent.com/apache/airflow/main/airflow-core/docs/img/ui-dark/dags.png" alt="Airflow LLM branching" width="100%"></a><br><b><a href="https://github.com/apache/airflow/blob/main/providers/common/ai/docs/classifier_models.rst">Airflow LLM branching</a></b><br><sub>apache · GitHub · ⭐ 46.9k repo · 2015-04-13</sub><br>Picks the next task with a Jev Choice and hands low-confidence cases to a person.</td>
<td width="33%" valign="top"><a href="https://x.com/tarasshyn/status/2101012033340571952"><img src="https://pbs.twimg.com/amplify_video_thumb/2101011544515526656/img/iSFydnTHWxsRx9hy.jpg" alt="Flowsery session replay triage" width="100%"></a><br><b><a href="https://x.com/tarasshyn/status/2101012033340571952">Flowsery session replay triage</a></b><br><sub>tarasshyn · X · ♥ 829 · 2026-09-18</sub><br>Ran Jev over 3 million session-replay events: in 40 seconds it reviewed 3,247 sessions, caught 132 rage clicks, 116 dead clicks and 95 JavaScript errors, and opened 213 draft fix PRs for $2.17.</td>
<td width="33%" valign="top"><a href="https://x.com/yyyole/status/2101184012899537092"><img src="https://pbs.twimg.com/amplify_video_thumb/2101182941317787648/img/1Imy25EAcuq8Wllx.jpg" alt="AI news filtering" width="100%"></a><br><b><a href="https://x.com/yyyole/status/2101184012899537092">AI news filtering</a></b><br><sub>yyyole · X · ♥ 330 · 2026-09-19</sub><br>Screened nearly 2,700 AI news items from the past 7 days one by one with Jev in about 2 minutes for $0.21, to pick content topics.</td>
</tr>
</table>

**[Browse all 135 in Data and Evaluation →](https://github.com/Li-Evan/awesome-jev/blob/main/scenarios/data.md)**

### 🎧 Customer Support and Sales

Ticket routing, email triage, lead scoring, and CRM automation.

<table>
<tr>
<td width="33%" valign="top"><a href="https://x.com/romanbuildsaas/status/2100891604735099103"><img src="https://pbs.twimg.com/amplify_video_thumb/2100891566340501504/img/agvkcRfNWmnGbRI5.jpg" alt="Lead and outreach scoring" width="100%"></a><br><b><a href="https://x.com/romanbuildsaas/status/2100891604735099103">Lead and outreach scoring</a></b><br><sub>romanbuildsaas · X · ♥ 3.3k · 2026-09-18</sub><br>Scoring of 700 high-intent leads and personalized outreach messages in 40 seconds for $0.09, predicting each message's performance with a confidence score and flagging lead-message mismatches.</td>
<td width="33%" valign="top"><a href="https://github.com/twentyhq/twenty/tree/main/packages/twenty-server/src/modules/workflow/workflow-executor/workflow-actions/classify"><img src="https://repository-images.githubusercontent.com/572984571/ef151ee9-3060-418b-bf88-cb689ab78c7b" alt="Twenty Classify workflow action" width="100%"></a><br><b><a href="https://github.com/twentyhq/twenty/tree/main/packages/twenty-server/src/modules/workflow/workflow-executor/workflow-actions/classify">Twenty Classify workflow action</a></b><br><sub>twentyhq · GitHub · ⭐ 57.2k repo · 2022-12-01</sub><br>Classify step in the open-source Twenty CRM's workflows that asks Jev choice, score or boolean questions about a record, so later steps can branch on the answers and probabilities.</td>
<td width="33%" valign="top"><a href="https://x.com/Box/status/2100993278955188320"><img src="https://pbs.twimg.com/amplify_video_thumb/2100986163511357440/img/o0Yzl7VqISwchxkk.jpg" alt="Box incident triage" width="100%"></a><br><b><a href="https://x.com/Box/status/2100993278955188320">Box incident triage</a></b><br><sub>Box · X · ♥ 31 · 2026-09-18</sub><br>Box workflow that pulls an incident report, asks Jev whether it is customer-facing and how severe it is, moves the file to Escalate, Monitor or Review, and sends low-confidence cases to a human.</td>
</tr>
<tr>
<td width="33%" valign="top"><a href="https://www.youtube.com/watch?v=CupCEehe2OQ"><img src="https://i.ytimg.com/vi/CupCEehe2OQ/hqdefault.jpg" alt="Sales Copilot with Jev" width="100%"></a><br><b><a href="https://www.youtube.com/watch?v=CupCEehe2OQ">Sales Copilot with Jev</a></b><br><sub>Kelvin Cleto · YouTube · ♥ 1.9k · 2026-09-20</sub><br>Portuguese walkthrough of a sales-meeting copilot that tracks calls and playbook steps, where Jev answers cheap decision questions before any LLM call to cut costs.</td>
<td width="33%" valign="top"><a href="https://x.com/tarasshyn/status/2101043617649340678"><img src="https://pbs.twimg.com/amplify_video_thumb/2101043565207916544/img/jTZjaCWwP1d9sx6D.jpg" alt="RedReplier buying-signal scoring" width="100%"></a><br><b><a href="https://x.com/tarasshyn/status/2101043617649340678">RedReplier buying-signal scoring</a></b><br><sub>tarasshyn · X · ♥ 463 · 2026-09-18</sub><br>Scored 1,759,932 buying signals from 1.7 million mentions across Reddit, X, Bluesky, Hacker News and Facebook in 53 seconds for $0.65, ranking intent, product fit and competitor mentions.</td>
<td width="33%" valign="top"><a href="https://x.com/razeden0/status/2102119174466396250"><img src="https://pbs.twimg.com/amplify_video_thumb/2102119097077006336/img/qrIQdb9RSULrBTqB.jpg" alt="Grok and Jev lead screener" width="100%"></a><br><b><a href="https://x.com/razeden0/status/2102119174466396250">Grok and Jev lead screener</a></b><br><sub>razeden0 · X · ♥ 172 · 2026-09-21</sub><br>Lead-qualification pipeline where Jev answers 6 questions on each of 3,412 leads (20,472 decisions in 15.7 seconds for $0.41) and Grok 4.7 only drafts outreach for the leads worth reading.</td>
</tr>
</table>

**[Browse all 44 in Customer Support and Sales →](https://github.com/Li-Evan/awesome-jev/blob/main/scenarios/support.md)**

### ⚖️ Legal, Health, and Science

Compliance checks, medical and scientific screening, and research workflows.

<table>
<tr>
<td width="33%" valign="top"><a href="https://1kpapers.com"><img src="https://www.1kpapers.com/opengraph-image.png?opengraph-image.1mk7bn86uhq5h.png" alt="1kpapers" width="100%"></a><br><b><a href="https://1kpapers.com">1kpapers</a></b><br><sub>nutlope · App · ♥ 2k · 2026-09-17</sub><br>Site mapping 1,018 AI research papers from 2025-2026 by topic, where each paper is summarized by DeepSeek V4 Flash and then classified into 24 topics by Jev for $0.08 total.</td>
<td width="33%" valign="top"><a href="https://x.com/Paiky16/status/2101628198928982219"><img src="https://praneeth16.github.io/jev/og.png" alt="Adverse drug effect detection with GEPA" width="100%"></a><br><b><a href="https://x.com/Paiky16/status/2101628198928982219">Adverse drug effect detection with GEPA</a></b><br><sub>Paiky16 · X · ♥ 138 · 2026-09-20</sub><br>Uses Jev to flag sentences reporting suspected adverse drug effects in medical literature, then GEPA prompt optimization raised F1 from 69.1% to 79.7% and cut false positives from 47 to 22.</td>
<td width="33%" valign="top"><a href="https://x.com/rheum_ai/status/2100454043361722798"><img src="https://pbs.twimg.com/amplify_video_thumb/2100452479016321024/img/nAyq81QFzA6UzPqM.jpg" alt="Live clinical consultation classifier" width="100%"></a><br><b><a href="https://x.com/rheum_ai/status/2100454043361722798">Live clinical consultation classifier</a></b><br><sub>rheum_ai · X · ♥ 432 · 2026-09-17</sub><br>Prototype that feeds an ambient-scribe transcript to Jev during a clinical consultation to traverse a medical ontology, classify symptoms, update the differential diagnosis and flag red flags in real time.</td>
</tr>
<tr>
<td width="33%" valign="top"><a href="https://x.com/rothken/status/2102151333193363791"><img src="https://lawanalyzer.com/social-card.png" alt="LawAnalyzer" width="100%"></a><br><b><a href="https://x.com/rothken/status/2102151333193363791">LawAnalyzer</a></b><br><sub>rothken · X · ♥ 51 · 2026-09-21</sub><br>Free beta construction set from a law firm's AI lab for building legal-analysis applets on Jev, with reusable JSON and Jev code outputs that lawyers and students can save and adapt.</td>
<td width="33%" valign="top"><a href="https://github.com/choxos/jev-reviewer"><img src="https://raw.githubusercontent.com/choxos/jev-reviewer/main/documentation/tour.gif" alt="Jev Reviewer" width="100%"></a><br><b><a href="https://github.com/choxos/jev-reviewer">Jev Reviewer</a></b><br><sub>choxos · GitHub · ⭐ 32 · 2026-09-18</sub><br>In-browser data extraction tool for systematic reviews that answers extraction-form or RoB 2, ROBINS-I, QUADAS-2, and TIDieR template questions with verbatim quotes and page locations from trial reports.</td>
<td width="33%" valign="top"><a href="https://x.com/DevaiahShrithan/status/2102097862805053950"><img src="https://pbs.twimg.com/media/HSwmC5JawAArib5.jpg" alt="Jev reads every AI paper" width="100%"></a><br><b><a href="https://x.com/DevaiahShrithan/status/2102097862805053950">Jev reads every AI paper</a></b><br><sub>DevaiahShrithan · Article · ♥ 6 · 2026-09-21</sub><br>Ran 464,720 arXiv AI abstracts from 1993 to 2026 through Jev with five questions each (state-of-the-art claims, released code, LLM-written style, paper type, hype level) to chart how AI papers changed.</td>
</tr>
</table>

**[Browse all 28 in Legal, Health, and Science →](https://github.com/Li-Evan/awesome-jev/blob/main/scenarios/legal-health.md)**

### 🛍️ Commerce and Marketing

Product catalogs, ads, reviews, pricing, and marketing workflows.

<table>
<tr>
<td width="33%" valign="top"><a href="https://x.com/TheMattBerman/status/2100654891756589230"><img src="https://pbs.twimg.com/amplify_video_thumb/2100654321792684032/img/cXvU50KmCe6QFu86.jpg" alt="Competitor ad breakdown" width="100%"></a><br><b><a href="https://x.com/TheMattBerman/status/2100654891756589230">Competitor ad breakdown</a></b><br><sub>TheMattBerman · X · ♥ 6.7k · 2026-09-17</sub><br>Breakdown of 724 live ads from 37 brands in 40 seconds for 9 cents: Jev tagged each ad's hook, format, offer, CTA, awareness stage and landing-page mismatch.</td>
<td width="33%" valign="top"><a href="https://x.com/borjafat/status/2101018783976722479"><img src="https://pbs.twimg.com/amplify_video_thumb/2101018477087592448/img/9YlAHKLLo_h6rgtK.jpg" alt="Internal-link SEO audit" width="100%"></a><br><b><a href="https://x.com/borjafat/status/2101018783976722479">Internal-link SEO audit</a></b><br><sub>borjafat · X · ♥ 3.9k · 2026-09-18</sub><br>Reads all 586 pages of a site in 45.1 seconds and rebuilds the internal link map for $0.21, placing 584 links and refusing 139 pages with no honest fit; Claude Opus 5 got through 21 pages in the same time.</td>
<td width="33%" valign="top"><a href="https://x.com/elvissun/status/2100951347080421409"><img src="https://pbs.twimg.com/amplify_video_thumb/2100951319108567040/img/AZ1jFv9ySdRV-JYE.jpg" alt="NewsJack brand news matching" width="100%"></a><br><b><a href="https://x.com/elvissun/status/2100951347080421409">NewsJack brand news matching</a></b><br><sub>elvissun · X · ♥ 3.9k · 2026-09-18</sub><br>Reads 384 morning news stories and tells 15 brands which ones to jump on, in 24.9 seconds for $0.19, while Claude Opus 5 got through 4 stories for $0.77; the demo ships with 30+ PR agent skills.</td>
</tr>
<tr>
<td width="33%" valign="top"><a href="https://x.com/nailthy62/status/2101388186916454439"><img src="https://pbs.twimg.com/amplify_video_thumb/2101384523124740096/img/1Q6moTMdLcZ-mJ3r.jpg" alt="Drape real-time try-on" width="100%"></a><br><b><a href="https://x.com/nailthy62/status/2101388186916454439">Drape real-time try-on</a></b><br><sub>nailthy62 · X · ♥ 4.3k · 2026-09-19</sub><br>Real-time virtual try-on experiment for Drape: Jev reads the speech transcript and the current outfit, picks an item from the closet and swaps the outfit live, at $0.0011 and ~620ms per decision.</td>
<td width="33%" valign="top"><a href="https://x.com/irabukht/status/2101090579127951694"><img src="https://pbs.twimg.com/amplify_video_thumb/2101089408099516416/img/Smzn-jtE8prvdY90.jpg" alt="Ryze SEO/GEO agents on Jev" width="100%"></a><br><b><a href="https://x.com/irabukht/status/2101090579127951694">Ryze SEO/GEO agents on Jev</a></b><br><sub>irabukht · X · ♥ 1.5k · 2026-09-18</sub><br>Account of SEO and GEO audit-and-fix agents whose per-client cost fell 90% from about $250 after moving analytics reads, citation scans and gap analysis to Jev.</td>
<td width="33%" valign="top"><a href="https://x.com/OriSilver/status/2100941251478458871"><img src="https://pbs.twimg.com/amplify_video_thumb/2100940464870301696/img/g-uzVt-FDP21an26.jpg" alt="Maxfusion competitor-ad research" width="100%"></a><br><b><a href="https://x.com/OriSilver/status/2100941251478458871">Maxfusion competitor-ad research</a></b><br><sub>OriSilver · X · ♥ 582 · 2026-09-18</sub><br>Competitor research that classified 1,891 ads from Resilia's ad library by customer-journey stage and ad style in 19 seconds for $0.12, with a full account deep dive, coming to the Maxfusion MCP.</td>
</tr>
</table>

**[Browse all 45 in Commerce and Marketing →](https://github.com/Li-Evan/awesome-jev/blob/main/scenarios/commerce.md)**

### ✍️ Writing, Media, and Creative

Writing feedback, generative UI, music, art, and social media tools.

<table>
<tr>
<td width="33%" valign="top"><a href="https://x.com/ctatedev/status/2101022101750571357"><img src="https://pbs.twimg.com/amplify_video_thumb/2101022081810911232/img/3tKdQ3Y2_ZGSg3Q7.jpg" alt="json-render + Jev" width="100%"></a><br><b><a href="https://x.com/ctatedev/status/2101022101750571357">json-render + Jev</a></b><br><sub>ctatedev · X · ♥ 7.7k · 2026-09-18</sub><br>Generative UI experiment where Jev chooses components and actions from your own design system and json-render draws the interface in milliseconds.</td>
<td width="33%" valign="top"><a href="https://x.com/mattdesl/status/2100899669802963060"><img src="https://pbs.twimg.com/amplify_video_thumb/2100898643117068288/img/p9Jp61lJyiq-UoWK.jpg" alt="Colour understanding experiment" width="100%"></a><br><b><a href="https://x.com/mattdesl/status/2100899669802963060">Colour understanding experiment</a></b><br><sub>mattdesl · X · ♥ 5.6k · 2026-09-18</sub><br>Video experiment probing whether Jev understands colour, exploring fast, cheap judgments as a basis for new UI and UX paradigms.</td>
<td width="33%" valign="top"><a href="https://x.com/anshuc/status/2100246929611411501"><img src="https://pbs.twimg.com/amplify_video_thumb/2100245288183066624/img/ARkl8CTLZxp1KXSa.jpg" alt="Parallel pixel drawing" width="100%"></a><br><b><a href="https://x.com/anshuc/status/2100246929611411501">Parallel pixel drawing</a></b><br><sub>anshuc · X · ♥ 1.6k · 2026-09-16</sub><br>Experiment that has Jev draw a picture by predicting every pixel in parallel.</td>
</tr>
<tr>
<td width="33%" valign="top"><a href="https://x.com/robj3d3/status/2100722975645598191"><img src="https://pbs.twimg.com/amplify_video_thumb/2100722766362406912/img/pH0lahpfd-qTj_nE.jpg" alt="SuperX post scorer" width="100%"></a><br><b><a href="https://x.com/robj3d3/status/2100722975645598191">SuperX post scorer</a></b><br><sub>robj3d3 · X · ♥ 1.4k · 2026-09-17</sub><br>Post scorer for X that asks Jev 61 questions per draft in about 1 second for $0.0004, fitted on 9,481 posts from 207 creators and picking the viral post 2 in 3 times.</td>
<td width="33%" valign="top"><a href="https://github.com/ChetasLua/jevmeter"><img src="https://raw.githubusercontent.com/ChetasLua/jevmeter/main/docs/banner.jpg" alt="jevmeter" width="100%"></a><br><b><a href="https://github.com/ChetasLua/jevmeter">jevmeter</a></b><br><sub>ChetasLua · GitHub · ⭐ 81 · 2026-09-17</sub><br>CLI that transcribes any video, has Jev score every sentence against a chosen rubric, such as dodging a debate question, and renders the scores as live meters in a 16:9 edit you can post.</td>
<td width="33%" valign="top"><a href="https://x.com/leojrr/status/2100470174130250127"><img src="https://pbs.twimg.com/amplify_video_thumb/2100467692117295104/img/01ZWSKAA75eSiFlc.jpg" alt="X algorithm rebuilt with Jev" width="100%"></a><br><b><a href="https://x.com/leojrr/status/2100470174130250127">X algorithm rebuilt with Jev</a></b><br><sub>leojrr · X · ♥ 1.2k · 2026-09-17</sub><br>Recreation of the X ranking algorithm with Jev that simulates how far a post will reach, using the published weights and a global feed of everyone's posts.</td>
</tr>
</table>

**[Browse all 134 in Writing, Media, and Creative →](https://github.com/Li-Evan/awesome-jev/blob/main/scenarios/creative.md)**

### 🗣️ Voice and Real-Time Interfaces

Voice assistants and interfaces that react while you type or speak.

<table>
<tr>
<td width="33%" valign="top"><a href="https://x.com/jackcheng/status/2100729670991802386"><img src="https://pbs.twimg.com/amplify_video_thumb/2100729243185324032/img/YNw8njfnSXu-Tbyr.jpg" alt="Point-and-speak canvas" width="100%"></a><br><b><a href="https://x.com/jackcheng/status/2100729670991802386">Point-and-speak canvas</a></b><br><sub>jackcheng · X · ♥ 5k · 2026-09-17</sub><br>Whiteboard canvas controlled by pointing at a webcam and speaking: speech, finger position and canvas shapes go to Jev, which picks the action, target and location in about 167 ms.</td>
<td width="33%" valign="top"><a href="https://x.com/instantricecook/status/2100814590300889426"><img src="https://pbs.twimg.com/amplify_video_thumb/2100809295809974272/img/_1rbvz04k6wjpcGW.jpg" alt="Voice-controlled Mac agent" width="100%"></a><br><b><a href="https://x.com/instantricecook/status/2100814590300889426">Voice-controlled Mac agent</a></b><br><sub>instantricecook · X · ♥ 6.1k · 2026-09-18</sub><br>Voice-controlled computer use for the Mac that acts on spoken instructions as they arrive, opening Notes before the user finishes the sentence.</td>
<td width="33%" valign="top"><a href="https://x.com/moritzkremb/status/2100577979021832365"><img src="https://pbs.twimg.com/amplify_video_thumb/2100577954338373633/img/tbH43kHpUotE3hzK.jpg" alt="Real-time voice browser control" width="100%"></a><br><b><a href="https://x.com/moritzkremb/status/2100577979021832365">Real-time voice browser control</a></b><br><sub>moritzkremb · X · ♥ 3.8k · 2026-09-17</sub><br>Voice control for the browser: the spoken transcript goes to Jev, which returns probabilities in ~300ms and triggers the click, at $0.0002 per decision.</td>
</tr>
<tr>
<td width="33%" valign="top"><a href="https://x.com/nhciao/status/2101967227327267297"><img src="https://pbs.twimg.com/media/HSuwDLga4AEkvLg.jpg?name=orig" alt="Jev + Rime input method" width="100%"></a><br><b><a href="https://x.com/nhciao/status/2101967227327267297">Jev + Rime input method</a></b><br><sub>nhciao · X · ♥ 763 · 2026-09-21</sub><br>Test pairing Jev with the open-source Rime (Squirrel) Chinese input method to rank the wanted character higher among candidates while typing.</td>
<td width="33%" valign="top"><a href="https://x.com/BhosalePratim/status/2100986774742765991"><img src="https://pbs.twimg.com/amplify_video_thumb/2100986186219081728/img/LmAGU-0Pd5ZABGeb.jpg" alt="Voice intent to tool calls" width="100%"></a><br><b><a href="https://x.com/BhosalePratim/status/2100986774742765991">Voice intent to tool calls</a></b><br><sub>BhosalePratim · X · ♥ 476 · 2026-09-18</sub><br>Voice-agent experiment that replaces the LLM's tool-choice step with Jev so decisions run on partial transcripts, letting the agent act before the user finishes the sentence.</td>
<td width="33%" valign="top"><a href="https://x.com/_MaxBlade/status/2100967959879471519"><img src="https://pbs.twimg.com/amplify_video_thumb/2100966551826444288/img/i2s52ZeMNTOO-IRD.jpg" alt="Always-on assistant without a wake word" width="100%"></a><br><b><a href="https://x.com/_MaxBlade/status/2100967959879471519">Always-on assistant without a wake word</a></b><br><sub>_MaxBlade · X · ♥ 1.6k · 2026-09-18</sub><br>Always-listening voice assistant with no wake word, where Jev decides from probabilities whether speech is a command for the computer or ordinary conversation.</td>
</tr>
</table>

**[Browse all 54 in Voice and Real-Time Interfaces →](https://github.com/Li-Evan/awesome-jev/blob/main/scenarios/voice.md)**

### 🧰 Personal Productivity

Email, notes, calendars, browsing, and everyday automation.

<table>
<tr>
<td width="33%" valign="top"><a href="https://jaste.app/"><img src="https://jaste.app/og.png" alt="Jaste" width="100%"></a><br><b><a href="https://jaste.app/">Jaste</a></b><br><sub>Marcus Lowe · App · ♥ 9.7k · 2026-09-21</sub><br>Mac clipboard app whose Smart Paste mode uses Jev to pick the saved clipboard entry that fits the currently focused field; beta with BYOK and a local mode announced.</td>
<td width="33%" valign="top"><a href="https://x.com/ryanvogel/status/2100042788851101842"><img src="https://pbs.twimg.com/amplify_video_thumb/2100042377339588608/img/2O56_xRC0r54ugfr.jpg" alt="Jev email classification test" width="100%"></a><br><b><a href="https://x.com/ryanvogel/status/2100042788851101842">Jev email classification test</a></b><br><sub>ryanvogel · X · ♥ 3.5k · 2026-09-16</sub><br>Test of Jev classifying 1,500 of the author's own emails, shown in a video of batch inbox labeling.</td>
<td width="33%" valign="top"><a href="https://github.com/jev-chat/jev-chat-jarvis"><img src="https://raw.githubusercontent.com/jev-chat/jev-chat-jarvis/main/docs/images/overlay.png" alt="Jev Chat Assistant" width="100%"></a><br><b><a href="https://github.com/jev-chat/jev-chat-jarvis">Jev Chat Assistant</a></b><br><sub>jev-chat · GitHub · ⭐ 1.8k · 2026-09-21</sub><br>Android overlay that reads visible WeChat, QQ and X chats through accessibility, has Jev judge the other person's intent, risk level and best action, ranks three DeepSeek-drafted replies and fills one in without sending.</td>
</tr>
<tr>
<td width="33%" valign="top"><a href="https://x.com/rileybrown/status/2100404532119269426"><img src="https://pbs.twimg.com/amplify_video_thumb/2100403183533125632/img/54ZFO-CHvDeC-rw-.jpg" alt="500-email classification" width="100%"></a><br><b><a href="https://x.com/rileybrown/status/2100404532119269426">500-email classification</a></b><br><sub>rileybrown · X · ♥ 3.9k · 2026-09-17</sub><br>Demo of Jev classifying 500 emails in seconds for 3.5 cents.</td>
<td width="33%" valign="top"><a href="https://x.com/iam_zachi/status/2100529273186472318"><img src="https://pbs.twimg.com/amplify_video_thumb/2100529029761642496/img/OY0Ltm7v7lXv5-y6.jpg" alt="Real-time Jev ad blocker" width="100%"></a><br><b><a href="https://x.com/iam_zachi/status/2100529273186472318">Real-time Jev ad blocker</a></b><br><sub>iam_zachi · X · ♥ 3.9k · 2026-09-17</sub><br>Browser extension that classifies every DOM element as ad or not with Jev and removes ads from the page in real time.</td>
<td width="33%" valign="top"><a href="https://superx.so/instead-of-doomscrolling?niche=jev"><img src="https://superx.so/creators/assets/og-doomscroll-filter.png" alt="Doomscroll Filter" width="100%"></a><br><b><a href="https://superx.so/instead-of-doomscrolling?niche=jev">Doomscroll Filter</a></b><br><sub>SuperX · App · ♥ 1.7k · 2026-09-19</sub><br>Free tool where you pick a niche and Jev reads the last few days of X posts and sorts them into Read, Skim, or Pass.</td>
</tr>
</table>

**[Browse all 128 in Personal Productivity →](https://github.com/Li-Evan/awesome-jev/blob/main/scenarios/productivity.md)**

### 🎓 Education

Tutoring, grading, quizzes, and learning tools.

<table>
<tr>
<td width="33%" valign="top"><a href="https://x.com/hametgholizadeh/status/2101289895624917076"><img src="https://pbs.twimg.com/amplify_video_thumb/2101289673591021568/img/opei88xzp3DDGrcF.jpg" alt="Exam question predictor" width="100%"></a><br><b><a href="https://x.com/hametgholizadeh/status/2101289895624917076">Exam question predictor</a></b><br><sub>hametgholizadeh · X · ♥ 83 · 2026-09-19</sub><br>Ranks 80 real exam questions and 297 practice questions by how likely each is to appear on the actual exam, done in 80 seconds for $0.0256.</td>
<td width="33%" valign="top"><a href="https://x.com/0xaniol/status/2101076982373191927"><img src="https://pbs.twimg.com/amplify_video_thumb/2101074153407422464/img/fzFh7BZaZCmGdh8v.jpg" alt="talkr" width="100%"></a><br><b><a href="https://x.com/0xaniol/status/2101076982373191927">talkr</a></b><br><sub>0xaniol · X · ♥ 111 · 2026-09-18</sub><br>Speaking-practice app that gives you a topic, records 30 seconds of speech and has Jev score pauses, filler words, repetition, confidence and clarity with feedback.</td>
<td width="33%" valign="top"><a href="https://github.com/AustinAWay/Working-Memory-Jev"><img src="https://raw.githubusercontent.com/AustinAWay/Working-Memory-Jev/main/docs/provisional-estimates-live.png" alt="Working Memory Jev (Passage)" width="100%"></a><br><b><a href="https://github.com/AustinAWay/Working-Memory-Jev">Working Memory Jev (Passage)</a></b><br><sub>AustinAWay · GitHub · ⭐ 39 · 2026-09-18</sub><br>Experimental local teaching aid that shows educators where an instructional passage may ask learners to hold too many ideas or relationships at once as the text unfolds.</td>
</tr>
<tr>
<td width="33%" valign="top"><a href="https://github.com/wquguru/dasheng"><img src="https://opengraph.githubassets.com/1/wquguru/dasheng" alt="ReadAloud (dasheng)" width="100%"></a><br><b><a href="https://github.com/wquguru/dasheng">ReadAloud (dasheng)</a></b><br><sub>wquguru · GitHub · ⭐ 122 · 2026-09-20</sub><br>English read-aloud trainer where the R2T2 streaming ASR transcribes your speech, Jev judges whether each mismatched word was misread and how, and code turns those judgments into a score.</td>
<td width="33%" valign="top"><a href="https://github.com/Diogenesoftoronto/keating/blob/main/scripts/training/benchmark_judge_systemone.py"><img src="https://opengraph.githubassets.com/1/Diogenesoftoronto/keating" alt="Keating Jev teaching judge" width="100%"></a><br><b><a href="https://github.com/Diogenesoftoronto/keating/blob/main/scripts/training/benchmark_judge_systemone.py">Keating Jev teaching judge</a></b><br><sub>Diogenesoftoronto · GitHub · ⭐ 36 repo · 2026-04-01</sub><br>Typed-judgment reviewer for the Keating AI tutor's teaching rubric: Jev scores each dimension and selects evidence spans enumerated by code, so quotes cannot be invented, plus a harness comparing it with the incumbent LLM judge.</td>
<td width="33%" valign="top"><a href="https://github.com/freemocap/skellyspeak/tree/main/tools/benchmarks/conversation-prompts/assessment"><img src="https://opengraph.githubassets.com/1/freemocap/skellyspeak" alt="SkellySpeak Jev assessment study" width="100%"></a><br><b><a href="https://github.com/freemocap/skellyspeak/tree/main/tools/benchmarks/conversation-prompts/assessment">SkellySpeak Jev assessment study</a></b><br><sub>freemocap · GitHub · ⭐ 35 repo · 2025-01-24</sub><br>Benchmark in the SkellySpeak language-learning app that assesses learner messages against 45 coaching skills with Jev and compares it to a dense Gemini control in a 648-request Spanish factorial study with a dedicated dashboard.</td>
</tr>
</table>

**[Browse all 10 in Education →](https://github.com/Li-Evan/awesome-jev/blob/main/scenarios/education.md)**

### 🧪 Other Experiments

Everything that does not fit a single scenario yet.

<table>
<tr>
<td width="33%" valign="top"><a href="https://x.com/neogoose_btw/status/2101428888874410069"><img src="https://pbs.twimg.com/amplify_video_thumb/2101427327746093056/img/LiNIpS9HMaBO00kW.jpg" alt="Jevassembler" width="100%"></a><br><b><a href="https://x.com/neogoose_btw/status/2101428888874410069">Jevassembler</a></b><br><sub>neogoose_btw · X · ♥ 1.5k · 2026-09-19</sub><br>Satirical experiment that skips writing code: you give it a task and Jev predicts the next CPU instruction to execute at runtime.</td>
<td width="33%" valign="top"><a href="https://x.com/steventey/status/2101788378882863427"><img src="https://pbs.twimg.com/media/HSsNY_ybUAEFIK_.jpg?name=orig" alt="jev-even-odd" width="100%"></a><br><b><a href="https://x.com/steventey/status/2101788378882863427">jev-even-odd</a></b><br><sub>steventey · X · ♥ 2.4k · 2026-09-20</sub><br>Tongue-in-cheek npm package that checks whether a number is even or odd by asking Jev through the AI SDK.</td>
<td width="33%" valign="top"><a href="https://x.com/sarvagya_kul/status/2100980770206879849"><img src="https://pbs.twimg.com/amplify_video_thumb/2100980671640645632/img/19dyomYRhfAONg7S.jpg" alt="Candidate-company job matching" width="100%"></a><br><b><a href="https://x.com/sarvagya_kul/status/2100980770206879849">Candidate-company job matching</a></b><br><sub>sarvagya_kul · X · ♥ 1.8k · 2026-09-18</sub><br>Matching of one candidate profile against 400 companies in 12 seconds for $0.0005, predicting which jobs they are most likely to land and flagging mismatches.</td>
</tr>
<tr>
<td width="33%" valign="top"><a href="https://github.com/narphorium/nl-logic-interpreter"><img src="https://pbs.twimg.com/amplify_video_thumb/2100984200820121600/img/dXya52zCSiVBJVaF.jpg" alt="Natural Language Logic Interpreter" width="100%"></a><br><b><a href="https://github.com/narphorium/nl-logic-interpreter">Natural Language Logic Interpreter</a></b><br><sub>narphorium · GitHub · ⭐ 6 · 2026-09-19</sub><br>Step-through logic interpreter that proves goals over plain-English facts and rules by SLD resolution as Prolog does, with Jev deciding when two sentences state the same fact so they unify.</td>
<td width="33%" valign="top"><a href="https://github.com/monteduro/killmyidea"><img src="https://killmyidea.stemonte.io/og.png" alt="Kill My Idea" width="100%"></a><br><b><a href="https://github.com/monteduro/killmyidea">Kill My Idea</a></b><br><sub>monteduro · GitHub · ⭐ 76 · 2026-09-17</sub><br>Web app that judges a startup idea as KILL IT, FIX IT, or SHIP IT from one request of 10 parallel Jev questions, with local weights and gates computing the verdict.</td>
<td width="33%" valign="top"><a href="https://x.com/TheBalkanHacker/status/2100962091498684848"><img src="https://pbs.twimg.com/amplify_video_thumb/2100960184327688192/img/7zn9b3VwndkLLzWa.jpg" alt="6502 emulator on Jev" width="100%"></a><br><b><a href="https://x.com/TheBalkanHacker/status/2100962091498684848">6502 emulator on Jev</a></b><br><sub>TheBalkanHacker · X · ♥ 43 · 2026-09-18</sub><br>Experiment that has Jev act as the computer itself, emulating a 6502 CPU in real time; it runs whole short programs but still diverges from a reference emulator now and then.</td>
</tr>
</table>

**[Browse all 46 in Other Experiments →](https://github.com/Li-Evan/awesome-jev/blob/main/scenarios/other.md)**

## Open Models and Compatible Servers

Community models and servers that imitate Jev's interface. Their accuracy and calibration are self-reported and generally below Jev's, so evaluate them on your own data.

<table>
<tr>
<td width="33%" valign="top"><a href="https://huggingface.co/harshatheg/Qwen-2.5-1B-RLCD"><img src="https://cdn-thumbnails.huggingface.co/social-thumbnails/models/harshatheg/Qwen-2.5-1B-RLCD.png" alt="Qwen-2.5-1B-RLCD" width="100%"></a><br><b><a href="https://huggingface.co/harshatheg/Qwen-2.5-1B-RLCD">Qwen-2.5-1B-RLCD</a></b><br><sub>harshatheg · Hugging Face · ♥ 524 · 2026-09-16</sub><br>Parallel constrained decoding engine for Apple Silicon that answers multi-field decision schemas in one pass over stock Qwen2.5-1.5B, shipped as code only with no trained RLCD weights.</td>
<td width="33%" valign="top"><a href="https://github.com/NandhaKishorM/laya"><img src="https://raw.githubusercontent.com/NandhaKishorM/laya/main/assets/laya_vs_jev_full.png" alt="Laya" width="100%"></a><br><b><a href="https://github.com/NandhaKishorM/laya">Laya</a></b><br><sub>NandhaKishorM · GitHub · ⭐ 12k · 2026-09-18</sub><br>Open, local non-autoregressive decision models on ModernBERT-style encoders, from a 421M English checkpoint to multilingual ones, answering Choice, Score and Noul questions in 33 ms per question with a per-request router.</td>
<td width="33%" valign="top"><a href="https://x.com/taroleo/status/2101106887840370919"><img src="https://pbs.twimg.com/amplify_video_thumb/2101102823408807936/img/k_uNGVHacO6DG6mC.jpg" alt="Distilled 4B local decision model" width="100%"></a><br><b><a href="https://x.com/taroleo/status/2101106887840370919">Distilled 4B local decision model</a></b><br><sub>taroleo · X · ♥ 3k · 2026-09-19</sub><br>Distillation of DeepSeek V4 Flash judgments into a Jev-style 4B local model over 26 hours on a DGX Spark, beating the teacher's instant mode at 1/20 the size with about 22ms per decision.</td>
</tr>
<tr>
<td width="33%" valign="top"><a href="https://x.com/atomic_chat_hq/status/2102160983409955244"><img src="https://pbs.twimg.com/amplify_video_thumb/2102158998103363584/img/AStT6MxzhJzruHIE.jpg" alt="Laya vs Jev at Tetris" width="100%"></a><br><b><a href="https://x.com/atomic_chat_hq/status/2102160983409955244">Laya vs Jev at Tetris</a></b><br><sub>atomic_chat_hq · X · ♥ 2.8k · 2026-09-21</sub><br>Tetris showdown in which the open-weights Laya model, running locally on a 16GB MacBook Air, beats cloud Jev by making decisions 11 times faster.</td>
<td width="33%" valign="top"><a href="https://github.com/wdobry/laya-playground"><img src="https://brainfunctioncollapse.com/laya/og.png" alt="Laya playground" width="100%"></a><br><b><a href="https://github.com/wdobry/laya-playground">Laya playground</a></b><br><sub>wdobry · GitHub · ⭐ 71 · 2026-09-20</sub><br>Local website with games, a benchmark and an agent skill for the open-source Laya decision model, comparing it with hosted Jev on the same 500 labelled examples.</td>
<td width="33%" valign="top"><a href="https://github.com/mizorewww/laya-mlx"><img src="https://raw.githubusercontent.com/mizorewww/laya-mlx/main/docs/assets/snake-demo.gif" alt="Laya-MLX" width="100%"></a><br><b><a href="https://github.com/mizorewww/laya-mlx">Laya-MLX</a></b><br><sub>mizorewww · GitHub · ⭐ 4.3k · 2026-09-19</sub><br>Native MLX runtime for the open Laya typed-decision checkpoints on Apple Silicon: 13.4 ms median per short English decision and 7.4 ms with the multilingual checkpoint, with no PyTorch or cloud API; demoed on Snake.</td>
</tr>
</table>

**[Browse all 240 in Open Models and Compatible Servers →](https://github.com/Li-Evan/awesome-jev/blob/main/pages/open-models.md)**

## Build with Jev

Ways to call Jev from your stack: hosted access, framework adapters, observability, and community SDKs.

### Model Access

- [Jev on OpenRouter](https://x.com/OpenRouter/status/2100744709589316009) - OpenRouter's announcement that Jev is available in beta through its API, returning a typed decision with a probability instead of generated text.
- [OpenCode Zen Jev endpoint](https://github.com/anomalyco/opencode/blob/dev/packages/web/src/content/docs/zen.mdx) - OpenCode's Zen gateway serves Jev 1.13 at a /v1/systemone endpoint with the Zen API key, plus a limited-time free jev-1.13-free model.
- [Convex AI Gateway Jev support](https://github.com/get-convex/convex-backend/blob/main/npm-packages/docs/docs/ai-gateway/api.mdx) - Convex's AI Gateway serves Jev as typesafe/jev-1.13 through a decisions endpoint, callable from Convex actions via AI SDK's evaluate and the @convex-dev/ai-sdk-provider package.
- [Bifrost TypeSafe provider](https://github.com/maximhq/bifrost/tree/dev/core/providers/typesafe) - TypeSafe provider in the Bifrost AI gateway that exposes a drop-in /typesafe prefix, so clients written for api.typesafe.ai, including the official SDK, work through Bifrost unchanged.
- [GPT-Load Jev channel](https://github.com/tbphp/gpt-load/blob/main/internal/channel/modules/jev.go) - Jev channel module for the self-hosted GPT-Load AI gateway, adding TypeSafe's official API as a provider with batch key import, scheduling and failover.
- [Jev on the Venice API](https://x.com/sabrinaesaquino/status/2101102660997017747) - Demo marking Jev's beta launch on the Venice API, classifying 24,000 Hacker News posts into 12 categories in about 2 minutes.
- [Experiential TypeSafe provider](https://github.com/experientiallabs/experiential/blob/main/exp/runtime/models/providers/typesafe.py) - TypeSafe provider in the Experiential open-source model gateway that dispatches Jev decisions natively and refuses to treat Jev as a chat model.
- [Cloudflare Jev model catalog](https://github.com/cloudflare/cloudflare-docs/blob/production/src/content/catalog-models/typesafe-jev.json) - Cloudflare's model catalog entry for typesafe/jev, listing Jev for Noul, Choice and Score evaluation at $0.042 per million input tokens and free output, with a worked example.
- [Pollinations Jev API](https://github.com/pollinations/pollinations/blob/main/gen.pollinations.ai/src/text/systemOneClient.ts) - The Pollinations gen API serves Jev as typesafe/jev-1.13 through a typed POST /alpha/decisions endpoint and Chat Completions, plus an Ask Jev MCP server with a jev_decide tool.
- [Jev on Fly.io Sprites](https://x.com/flydotio/status/2102076230183035081) - Fly.io's TypeSafe connector for Sprites, which injects your Jev API key at a gateway so agents running inside hardware-isolated Sprites can call Jev without the key entering the sandbox.

**[See all 68 Model Access →](https://github.com/Li-Evan/awesome-jev/blob/main/pages/build-model-access.md)**

### Framework Adapters

- [OpenClaw TypeSafe plugin](https://github.com/openclaw/openclaw/tree/main/extensions/typesafe) - Official OpenClaw plugin that plugs hosted Jev, or a local Kev server, into OpenClaw's decision-model API for Choice, Score and Boolean judgments, plus an optional typesafe_evaluate tool.
- [langchain-typesafe](https://github.com/langchain-ai/langchain/tree/master/libs/partners/typesafe) - LangChain partner package with a TypeSafeClassifier runnable for Choice, Noul and Score questions, plus experimental auto-mode and model-router middleware.
- [ai-cli](https://x.com/ctatedev/status/2100584917092409479) - Vercel Labs' terminal AI tool, installed with npm, that lets any agent harness ask Jev yes/no questions, choose between options, and score against criteria from the command line.
- [Composio](https://github.com/ComposioHQ/composio/tree/next/ts/packages/providers/typesafe) - TypeScript provider that picks and gates tool calls with a Choice and binds closed-set arguments before execution.
- [AI SDK TypeSafe provider](https://github.com/vercel/ai/tree/main/packages/typesafe-ai) - Official AI SDK provider package @ai-sdk/typesafe-ai that runs Choice, Score and Boolean questions against Jev through the experimental evaluate API.
- [Pydantic AI TypeSafeModel](https://github.com/pydantic/pydantic-ai/blob/main/pydantic_ai_slim/pydantic_ai/models/typesafe.py) - Pydantic AI model class that runs decision agents on Jev: each field of the output_type becomes one question and the answers fill the output, so swapping the model name compares Jev with an LLM.
- [elizaOS TypeSafe adapter](https://github.com/elizaOS/eliza/tree/develop/packages/agent/src/services/typesafe) - Opt-in server-side TypeSafe client in the elizaOS agent package that validates Choice, Score and Noul requests with Zod and sends them only on an explicit systemOne call; it is not registered with the runtime by default.
- [LangChain.js](https://github.com/langchain-ai/langchainjs/tree/main/libs/providers/langchain-typesafe) - JavaScript version of the classifier and the routing and approval middleware.
- [@effect/ai-typesafe](https://github.com/Effect-TS/effect/tree/main/packages/ai/typesafe) - Effect's DecisionModel provider for TypeSafe's System One API, supporting classification, ordered ratings and probabilities through Effect HttpClient, with provider distributions preserved rather than normalized.
- [BAML Jev support](https://github.com/BoundaryML/baml/tree/canary/baml_language/crates/baml_builtins2/baml_std/typesafeai) - Nightly v1 integration in BAML, the programming language for agents, that maps typed function return values to Jev questions; not yet in the stable release line.

**[See all 174 Framework Adapters →](https://github.com/Li-Evan/awesome-jev/blob/main/pages/build-frameworks.md)**

### Observability

- [Opik TypeSafe integration](https://github.com/comet-ml/opik/tree/main/sdks/python/src/opik/integrations/typesafe) - Opik Python SDK integration that wraps sync and async TypeSafe clients so every Jev call is traced in Opik's LLM observability and evaluation platform.
- [Phoenix TypeSafe tracing](https://github.com/Arize-ai/phoenix/tree/main/docs/phoenix/integrations/llm-providers/typesafe) - OpenInference instrumentation for the TypeSafe Python and TypeScript SDKs that records each System One call's state, questions and typed answers as spans in Arize Phoenix.
- [Langfuse TypeSafe integration](https://langfuse.com/integrations/model-providers/typesafe) - Integration guide and notebook for tracing Jev System One calls in Langfuse via OpenInference auto-instrumentation, with no client wrapper.
- [OpenInference TypeSafe instrumentation](https://github.com/Arize-ai/openinference/tree/main/python/instrumentation/openinference-instrumentation-typesafe) - OpenTelemetry instrumentation for the TypeSafe Python SDK that traces each Jev System One call's state, model, questions and typed answers, usable with any OTel backend.
- [Jeview](https://github.com/andududu/jeview) - Unofficial local gateway that sits between your code and TypeSafe, forwards every Jev request, stores each call in SQLite, and draws calls on a live map as they happen.
- [genai-prices TypeSafe provider](https://github.com/pydantic/genai-prices/blob/main/prices/providers/typesafe.yml) - Pydantic library for calculating LLM API costs, extended with TypeSafe pricing so Jev calls to /v1/systemone are matched and billed per input token.
- [Laminar TypeSafe instrumentation](https://github.com/lmnr-ai/lmnr-python/tree/main/src/lmnr/opentelemetry_lib/opentelemetry/instrumentation/typesafe) - OpenTelemetry instrumentation in the Laminar Python SDK that traces TypeSafe SDK system_one calls to Jev as spans alongside other LLM calls.
- [Braintrust TypeSafe instrumentation](https://github.com/braintrustdata/braintrust-sdk-javascript/blob/main/js/src/wrappers/typesafe.ts) - Braintrust JavaScript SDK instrumentation for @typesafe-ai/sdk: wrapTypeSafe and auto-instrumentation trace every systemOne call into Braintrust spans, alongside tracing for the AI SDK evaluate call.
- [Braintrust Python TypeSafe integration](https://github.com/braintrustdata/braintrust-sdk-python/tree/main/py/src/braintrust/integrations/typesafe) - Built-in integration in Braintrust's Python tracing and evals SDK that auto-instruments typesafe-sdk system_one calls so Jev requests and answers show up as Braintrust spans.
- [Laminar TypeSafe instrumentation](https://github.com/lmnr-ai/lmnr-ts/tree/main/packages/lmnr/src/opentelemetry-lib/instrumentation/typesafe) - OpenTelemetry instrumentation in Laminar's TypeScript SDK that patches the TypeSafe SDK's systemOne calls to record Jev requests, responses and errors as spans.

**[See all 14 Observability →](https://github.com/Li-Evan/awesome-jev/blob/main/pages/build-observability.md)**

### Community SDKs

- [rust-sysone](https://github.com/zcoder-run/rust-sysone) - Early unofficial Rust client for the System One API from the author of the genai crate, with a fluent Request builder and typed Noul, Choice and Score questions.
- [http4k TypeSafe connector](https://github.com/http4k/http4k/tree/master/connect/ai/typesafe) - TypeSafe connector for the http4k Kotlin toolkit with a typed System One client and a fake, exposing Jev Noul, Choice and Score questions as http4k actions.
- [ruby_decision_model](https://github.com/obie/ruby_decision_model) - Standard-library-only Ruby client for decision models such as Jev, with one Client that talks to OpenRouter by default or TypeSafe’s native API and parses choices, probabilities, scores and usage.
- [Jev for OTP](https://github.com/dannote/jev) - Elixir client that treats Jev as an OTP peer process: a GenServer sends state and typed questions, and each answer arrives as a message to pattern match on, with a hundred calls able to be in flight.
- [TypeSafe Swift SDK](https://github.com/krzyzanowskim/TypeSafe) - SwiftPM client for the TypeSafe System One API that follows the official JavaScript SDK's behavior for noul, choice, and score questions, with a small demo app.
- [Hunch](https://github.com/carldaws/hunch) - Ruby and Rails gem for probabilistic control flow that turns Jev answers into Ruby values, with chance, pick and rate calls and graded predicates such as likely? for branching directly on a judgment.
- [swift-typesafe](https://github.com/ainame/swift-typesafe) - Unofficial Swift 6.4 SDK following the Python SDK's 0.7.0 API, with a @QuestionSet macro that generates typed answers, dynamic questions and Linux support.
- [openai-scala-client TypeSafe module](https://github.com/cequence-io/openai-scala-client/tree/master/typesafe-client) - TypeSafe module in the async openai-scala-client that sends shared state and typed questions to Jev, with examples for confidence-gated routing, semantic find and an OpenAI-style adapter.
- [typesafe-sdk-go (atharvamhaske)](https://github.com/atharvamhaske/typesafe-sdk-go) - Unofficial Go SDK built to the same wire contract as the official Python and JavaScript SDKs, with typed choice, score and noul questions, a typed answer union and model discovery.
- [typesafe-ai (Rust)](https://github.com/Twister915/typesafe-ai) - Typed Rust client for System One with an async reqwest or blocking ureq backend and observable retries, deserializing Noul, Choice and Score answers into Rust enums with usage data.

**[See all 107 Community SDKs →](https://github.com/Li-Evan/awesome-jev/blob/main/pages/build-community-sdks.md)**

## Learn

Official docs and cookbooks, plus the best guides, analyses, benchmarks, and talks from the community.

### Official Docs

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

**[See all 15 Official Docs →](https://github.com/Li-Evan/awesome-jev/blob/main/pages/learn-official-docs.md)**

### Official SDKs and Tools

- [typesafe-sdk-python](https://github.com/typesafe-ai/typesafe-sdk-python) - Official Python client, published on PyPI as `typesafe-sdk`.
- [typesafe-sdk-js](https://github.com/typesafe-ai/typesafe-sdk-js) - Official JavaScript and TypeScript client for Node.js, published on npm as `@typesafe-ai/sdk`.
- [Workflow evals](https://evals.typesafe.ai) - Compares many models running four real workflows as decomposed questions versus as a single prompt.

### Announcements

- [Introducing System One models and Jev](https://typesafe.ai/blog/introducing-system-one-models-and-jev) - Launch post explaining the bet on decision models over text generators.
- [Manifesto](https://typesafe.ai/manifesto) - TypeSafe's argument for AI-powered software where code, not an agent loop, owns the workflow.

### Patterns

- [Speculative fan-out](https://docs.typesafe.ai/patterns/fan-out) - Ask every question you might need, including branch-specific ones, in one request and let code read only the relevant answers.
- [Confidence-gated routing](https://docs.typesafe.ai/patterns/confidence-routing) - Uses confidence as a second axis, with stricter thresholds for riskier actions such as money transfers.
- [Composite scoring](https://docs.typesafe.ai/patterns/composite-scoring) - Scores each dimension separately and combines them with weights in code, so priorities change without touching the questions.
- [Intent routing](https://docs.typesafe.ai/patterns/intent-routing) - Classifies requests with a Choice and a complexity Score, then sends each to code, a specialist LLM, or a human.

### Official Cookbooks

- [Hierarchical classification](https://docs.typesafe.ai/cookbooks/hierarchical_classification) - Walks deep taxonomies such as patent codes, retail products, MeSH, and a source tree with one Choice per node and beam search over the probabilities.
- [Classification using confidence](https://docs.typesafe.ai/cookbooks/classification_using_confidence) - Sorts 60 SEC filings into 75 industry groups and falls back to the broader division below 0.9 confidence, turning 39 correct answers into 48 useful ones.
- [Smart home assistant demo](https://docs.typesafe.ai/demos/smart-home) - Interprets home commands with a long speculative fan-out of Choices, plus a Noul that spots compound requests for an LLM to split.
- [Function calling](https://docs.typesafe.ai/cookbooks/function_calling) - Maps trading requests onto ten ordinary typed functions, with Choices for the function and closed-set arguments and Nouls for which arguments were stated.
- [Skill suggestion](https://docs.typesafe.ai/cookbooks/skill_suggestion) - Picks at most one of 182 agent skills per turn in two requests, cutting wrong skill loads from 16.8% to 7.3%.
- [Re-ranking](https://docs.typesafe.ai/cookbooks/rerank_typesafe) - Scores each BM25 candidate with one Noul per query-passage pair, lifting top-10 legal retrieval accuracy from 38% to 62% for about $0.06 in total.
- [Line-by-line search](https://docs.typesafe.ai/cookbooks/semantic_find) - Ranks 218 lines of a terms-of-service document with a single Choice and uses a Noul to say when the document has no answer.
- [Classifying RAG passages](https://docs.typesafe.ai/cookbooks/classifying_rag_passages) - Runs four Nouls per retrieved passage to drop prompt injections and off-topic text and to flag passages that contradict the question.
- [Date extraction](https://docs.typesafe.ai/cookbooks/date_extraction_cookbook) - Reads date parts with Choices and leaves all calendar math to code, sending low-confidence dates to review.
- [Pre-parsed value extraction](https://docs.typesafe.ai/cookbooks/pre_parsed_value_extraction_cookbook) - Finds emails, phone numbers, and amounts with regular expressions, then lets a Choice select the requested one so values are never invented.

**[See all 18 Official Cookbooks →](https://github.com/Li-Evan/awesome-jev/blob/main/pages/learn-cookbooks.md)**

### Examples and Skills

- [Jev experiments](https://github.com/dabit3/jev-experiments) - Twenty-one low-latency demo apps, such as reranking 50 candidates in a single request.
- [TypeSafe skills](https://github.com/typesafe-ai/skills) - Source of the agent skill, installable as a Claude Code plugin or through skills.sh.
- [Hello Jev (Real Python)](https://github.com/realpython/materials/tree/master/hello-jev) - Companion code for Real Python's Get Started With Jev in Python video: a train-station help desk that swaps strict Y/N input parsing for a single Noul question.
- [AI cookbook for Jev](https://github.com/daveebbelaar/ai-cookbook/tree/main/models/jev) - Nine runnable examples plus the four official patterns, written against the current Python SDK.
- [Easy-Jev](https://x.com/rory_builds/status/2100606378184171682) - Interactive playground where you change the inputs and watch Jev's classifications update in real time.
- [Jev typed decisions tutorial](https://github.com/marktechpost-ai-media-inc/ai-agents-projects-tutorials/blob/main/LLM%20Projects/typesafe_jev_system_one_typed_decisions_tutorial_Marktechpost.ipynb) - Marktechpost notebook that walks through Jev typed decisions: ticket triage, recomputing confidence, resume scoring, intent routing and a home-automation tool picker, tracking cost as it goes.
- [Building with Jev skill](https://github.com/dbreunig/building-with-jev-skill) - Compact agent skill that teaches coding agents to structure programs around Jev.
- [Jevify](https://github.com/ryana/jevify) - Prompt to paste into a coding agent that has it study the Jev docs and your codebase, then find where cheap semantic judgments could cut cost and latency or enable new features.
- [JEV Playground](https://x.com/mac_eth/status/2101701798968840703) - Simple web playground for trying Jev by entering text context and asking Noul, Choice or Score questions.
- [AI Bootcamp Jev notebook](https://github.com/curiousily/AI-Bootcamp/blob/master/jev.ipynb) - A Jev notebook in the Get Shit Done with AI bootcamp that teaches TypeSafe's System One typed decisions with the Python SDK alongside its other GenAI lessons.

**[See all 74 Examples and Skills →](https://github.com/Li-Evan/awesome-jev/blob/main/pages/learn-examples.md)**

### Guides

- [Building a Harness with Jev](https://x.com/sydneyrunkle/status/2100754364545761643) - Guide to adding Jev to a LangChain agent harness, covering how Jev works, where it fits in the agent loop, model routing and pre-tool risk checks as middleware.
- [Jev Engineering roadmap](https://x.com/0xCodila/status/2100984487802708306) - X article with a 10-step roadmap for setting up Jev as the decision layer that tells agents and LLMs what to do next.
- [30 things you can do with Jev](https://x.com/29meat_ai/status/2100844631693095267) - Japanese-language introduction to what Jev does and does not do, walking through 30 real prototypes and demos (flight search, browser agents, games, trading bots) with reported speed and cost.
- [Jev Engineering in 10 steps](https://x.com/0xMovez/status/2101007482919227841) - X article laying out a 10-step setup that moves an agent's yes/no, next-worker and relevance-scoring calls from an LLM to Jev, then adds a model router and a gate for risky tool calls.
- [Jev x Codex practical guide](https://x.com/MakeAI_CEO/status/2101924475814212065) - Japanese guide to installing the TypeSafe skill in Codex, separating generation from Jev judgments, published experiments, work applications, and ways to improve decision accuracy.
- [How to master Jev (Full Guide)](https://x.com/chddaniel/status/2100925069765534024) - Long guide covering what Jev is good at, using it beside existing LLMs, question patterns, confidence gates against bad decisions, and five money-making workflows.
- [Build your own Jev (100% local)](https://x.com/_avichawla/status/2101563610644496464) - Tutorial on turning an open-source LLM into a local decision engine without retraining, using next-token scoring over fixed choices with SGLang, benchmarked against normal text generation.
- [Giving your agents a decision brain](https://x.com/0xRicker/status/2101292455391809670) - X article with a 10-step guide to moving an agent's yes/no, routing and relevance calls from an expensive LLM to Jev's three question types.
- [WTF Is Jev?](https://x.com/mvanhorn/status/2100784142850097482) - Plain-language explainer of Jev as multiple choice rather than essay writing, followed by nine things people are already building with it, checked against the live posts.
- [Jev Engineering roadmap, summarized](https://x.com/DataChaz/status/2101206777924858319) - Thread condensing a 10-step Jev setup guide: turn agent forks into Choice, Score and probability, batch decisions (13 questions ran 10x faster and 12.2x cheaper in one test), and benchmark the whole loop.

**[See all 76 Guides →](https://github.com/Li-Evan/awesome-jev/blob/main/pages/learn-guides.md)**

### Techniques and Analysis

- [Jev launch thread](https://x.com/CompleteSkeptic/status/2099925682726002904) - Founder Diogo Almeida's launch thread introducing Jev and the RLCD training method, claiming 20-200x faster and 40-400x cheaper decisions than frontier chat models.
- [Jev Clearly Explained](https://x.com/akshay_pachaar/status/2101037514945597645) - X article explaining Jev as a millisecond decision layer: how typed questions replace generate-parse-retry LLM calls, and where it sits next to an LLM in an application.
- [Generating text with Jev](https://x.com/0xSuman/status/2100030221189874015) - Hack that makes Jev write text by asking one Choice question per character position, with a STOP option, and reading off the most likely letters.
- [Jev as a smart switch statement](https://x.com/NathanFlurry/status/2100036101809619314) - Hype-free explainer arguing Jev is a very smart switch statement: it classifies, routes, scores and verifies over predefined options but cannot write code or text.
- [LLM vs Jev at prompt difficulty](https://x.com/k_grajeda/status/2099952715430596710) - Simplified side-by-side showing how an LLM and Jev classify a prompt's difficulty: token-by-token text versus probabilities for every option computed in parallel.
- [Critique of Jev compaction](https://x.com/theo/status/2100762304862384257) - Critique arguing per-tool-call filtering with Jev is a poor compaction strategy, since compaction should reconstruct history and the model lacks context on what came before.
- [What Jev can really do](https://x.com/servasyy_ai/status/2101132667056185544) - Chinese-language reality check on Jev that explains what it is and is not, sorts demos that actually work by use case, and lays out the caveats behind the speed and accuracy claims.
- [Jev as a decision primitive](https://x.com/MichaelLee04/status/2100003037150683593) - Notes from ~5,000 requests (about $2) on classification, routing and intent: p50 ~150ms and p95 ~350ms make per-turn checks viable, and Jev rewards splitting queries into independent questions.
- [LLMs vs. Jev, clearly explained](https://x.com/akshay_pachaar/status/2101309986156712025) - Explains that Jev does not generate faster, it does not generate at all: independent Choice, Score and Noul questions, like urgency, owning team and command risk for a failed deploy, are evaluated in parallel.
- [How Jev-style decoding works](https://x.com/NielsRogge/status/2100239244501430438) - Visual explanation, based on the open Qwen2.5-RLCD model, of reading field probabilities from a cached single decoder pass instead of generating JSON token by token.

**[See all 102 Techniques and Analysis →](https://github.com/Li-Evan/awesome-jev/blob/main/pages/learn-techniques.md)**

### Benchmarks and Case Studies

- [Hermes Agent compaction scorecard](https://github.com/NousResearch/hermes-agent/blob/main/evals/compaction/results/SCORECARD-2026-09-19-jev.md) - Tests a Jev-based context-compaction plugin against Hermes' own compressor and recommends against it: far cheaper and faster per compaction, but it kept twice the context and ranked tool results no better than recency.
- [Can Jev Be a Better Agent Evaluator?](https://www.langchain.com/blog/jev-agent-evals-langsmith) - LangChain tests Jev as a judge against LLM judges for agent evaluation in LangSmith, comparing accuracy, repeatability, latency and cost.
- [Trolley problems: humans vs robots](https://x.com/MaxRovensky/status/2100706874173575199) - Video of Jev working through trolley problems, where it chose to sacrifice a human to save robots.
- [HiringCafe resume-job relevance benchmark](https://x.com/h_nilforoshan/status/2100409794276520341) - Thread benchmarking Jev on resume-to-job-description relevance scoring for HiringCafe, a job search app serving 2.5 million monthly active users.
- [Code review benchmark](https://x.com/liorshkiller/status/2100936106615140757) - Benchmark of Jev scoring raw Git diffs against a GLM + Grok + Gemini ensemble reviewer: zero false positives, ~50x faster, ~100x cheaper, with 75% bug recall.
- [WindTunnel](https://webmcp.com/benchmark) - WebMCP browser-agent benchmark of 49 tasks on 8 real sites across 21 configurations, where Jev + Mercury 2.5 tops the composite score, solving 49/49 tasks at $0.0011 median cost per task.
- [JevBench](https://benchmarkheaven.com/jev-models) - Benchmark of Jev-class decision models that ranks Jev, its open rebuilds, and instruction models on intelligence, calibration, speed, and cost, 25% each as a geometric mean; Jev led at 75.3 with SemIf second at 74.6.
- [Industrial email classification benchmark](https://x.com/nikhilmudholkar/status/2100604560335139083) - Benchmark on 1,565 German and English supplier emails in 10 categories: Jev scored 96.4% vs Gemini's 97.5% and 98.5%, at $0.08 per 1,000 emails, and none of its 737 answers at 99%+ confidence were wrong.
- [Jev vs DeepSeek ticket routing](https://x.com/NFT_Chen/status/2101253568774697099) - Side-by-side routing of 500 real e-commerce support tickets: Jev cleared them in 83 seconds for $0.01, while DeepSeek V4.1 Flash had done 173 for $0.06 when stopped.
- [Jev in a security pipeline](https://x.com/grichadev/status/2100437998571860087) - Results table from a production security pipeline: Jev reached 99.3% accuracy at 0.259s latency and $0.026 per 1K, versus Gemini and open models that were slower and costlier.

**[See all 173 Benchmarks and Case Studies →](https://github.com/Li-Evan/awesome-jev/blob/main/pages/learn-benchmarks.md)**

### Talks and Videos

- [45-second Jev TL;DR](https://x.com/MatijaSosic/status/2100190746389135772) - Short explainer video that walks through Jev's core idea more simply than the launch video.
- [Jev is HERE. How to use it](https://www.youtube.com/watch?v=4mTLpuQpB80) - Startup Ideas Pod episode where Ryan Vogel demos Jev sorting 1,700 emails for 18 cents total, then covers lead scoring, support routing, video clipping, and startup angles.
- [Jev explained in 7 minutes](https://www.youtube.com/watch?v=vj7hysh0mOI) - Seven-minute explainer on RLCD and whether a model that answers with probability distributions instead of text can unlock new use cases.
- [JEV Breakdown: The First AI Model Built For Code](https://www.youtube.com/watch?v=2Bs0Ink_-Uo) - Breakdown of Jev with a live Playground walkthrough of Choice, Score, Noul, and confidence, and where a decision model fits in real apps.
- [Jev is incredible](https://www.youtube.com/watch?v=F3YXg7AaKWE) - Theo explains why Jev is a fast classifier with strong safety perks that complements rather than replaces reasoning models like Astra and Fable.
- [We need to talk about Jev](https://www.youtube.com/watch?v=2z-7pIj57f8) - Matthew Berman reviews the Jev launch and early community demos and reactions from X, and what a decision-only model changes.
- [TypeSafe founder tech talk](https://x.com/0xCodez/status/2101294219633529030) - Recorded 36-minute tech talk in which TypeSafe's founder explains why agents without a human in the loop come next and how models like Jev are trained.
- [Jev - The Ultimate Classification Model?](https://www.youtube.com/watch?v=X117w2Rark8) - Covers the System 1 idea, then demos Choice, Score, and Noul, a practical classification example, and chained actions.
- [Full Jev tutorial](https://x.com/moritzkremb/status/2100715237267660873) - Video tutorial covering what Jev is, API setup, and three demos: a voice-controlled browser, AI memory and a YouTube predictor.
- [What's next after RLHF?](https://www.youtube.com/watch?v=cJ0EOzey--o) - TypeSafe's CEO at AI Engineer World's Fair 2026 on training models for calibrated decisions instead of human approval.

**[See all 178 Talks and Videos →](https://github.com/Li-Evan/awesome-jev/blob/main/pages/learn-videos.md)**

### Discussions

- [Launch thread on Hacker News](https://news.ycombinator.com/item?id=49717558) - Nearly 2,000 points and about 500 comments, with the TypeSafe team answering questions about semantics and limits.
- [What is Jev? (r/LocalLLaMA)](https://www.reddit.com/r/LocalLLaMA/comments/1wleg4w/what_is_jev_and_what_is_it_used_for/) - Large r/LocalLLaMA thread (306 comments) where people explain what Jev is, how it differs from an LLM, and what it is actually useful for.
- [The car wash question on Jev](https://www.reddit.com/r/LLMDevs/comments/1wlciiq/the_famous_car_wash_question_on_jev/) - Tries the well-known car wash reasoning question on Jev and sparks a long debate (104 comments) on how to judge a decision model's intelligence beyond speed and price.
- [Is Jev a generalized BERT?](https://www.reddit.com/r/LocalLLaMA/comments/1wje4xh/still_doesnt_get_what_jev_isis_it_just_a_more/) - Thread in r/LocalLLaMA debating whether Jev is essentially a generalized BERT-style classifier that reads custom criteria at inference time.
- [Jev impressions on r/ArtificialInteligence](https://www.reddit.com/r/ArtificialInteligence/comments/1wkhsyh/jev_typesafeai_is_revolutionary_as_llms/) - Busy thread (155 comments) where early users share first impressions of Jev, including use as a policy prefilter, and argue about how it compares with frontier LLMs.
- [Jev architecture speculation](https://www.reddit.com/r/LocalLLaMA/comments/1wjjecz/jev_architecture/) - Thread in r/LocalLLaMA (57 comments) speculating on how Jev works and whether it is just an LLM read out before text generation.
- [Jev explained in one infographic](https://www.reddit.com/r/LLMDevs/comments/1wkwqu2/what_is_jev_typesafes_system_one_model_explained/) - One-page infographic of what TypeSafe's docs and evals actually say about Jev, covering the primitives, pricing, limits, and why the confidence field matters.
- [Testing Jev for Pi extensions](https://www.reddit.com/r/PiCodingAgent/comments/1whsav6/anyone_else_testing_out_typesafe_ais_new_system/) - Thread where Pi coding-agent users compare early Jev experiments, starting from a tool-call safety rater and a planned prompt-complexity model router.
- [Anyone here using Jev?](https://www.reddit.com/r/PiCodingAgent/comments/1wjibh5/anyone_here_using_jev/) - Thread in r/PiCodingAgent (77 comments) collecting what people build with Jev, starting from routing a natural-language request to one of 250-300 app API calls.
- [Thoughts on Jev? Any use cases?](https://www.reddit.com/r/machinelearningnews/comments/1wjkzs5/thoughts_on_jev_any_usecases/) - Thread weighing whether Jev is worth the hype, comparing it with small encoder classifiers such as GLiNER and pointing to tasks people used Haiku for.

**[See all 20 Discussions →](https://github.com/Li-Evan/awesome-jev/blob/main/pages/learn-discussions.md)**

## Contributing

Contributions welcome! Add an entry to the matching file in `data/`, run `uv run scripts/build.py`, and open a pull request. Read the [contribution guidelines](contributing.md) first, or [suggest a resource](https://github.com/Li-Evan/awesome-jev/issues/new/choose) through an issue.

## Footnotes

Images are loaded from each project's own pages and belong to their owners. The list text is released under CC0.
