# 🤖 Agents and Orchestration

**English** · [简体中文](https://github.com/Li-Evan/awesome-jev/blob/main/zh-CN/scenarios/agents.md)

Tool and skill selection, approvals, planning, memory, and harness decisions for general-purpose agents. 246 entries, ranked by community traction.

[← Back to Awesome Jev](https://github.com/Li-Evan/awesome-jev#browse-by-scenario)

<table>
<tr>
<td width="260" valign="top"><a href="https://github.com/Significant-Gravitas/AutoGPT/tree/master/autogpt_platform/backend/backend/blocks/typesafe"><img src="https://raw.githubusercontent.com/Significant-Gravitas/AutoGPT/master/docs/home/.gitbook/assets/Banner_image.png" alt="AutoGPT TypeSafe blocks" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Significant-Gravitas/AutoGPT/tree/master/autogpt_platform/backend/backend/blocks/typesafe">AutoGPT TypeSafe blocks</a></b><br><sub>Significant-Gravitas · GitHub · ⭐ 187.5k repo · 2023-03-16</sub><br>Seven no-code blocks, including a five-exit router, a yes, no, or unsure split, and a score filter.<br><sub><b>How it uses Jev:</b> Blocks call the TypeSafe Python SDK's system_one, so visual agent workflows can branch on Choice, Noul and Score answers.</sub><br><sub>Also: <a href="https://agpt.co">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/0xCodila/status/2101433560796467348"><img src="https://pbs.twimg.com/amplify_video_thumb/2101426271842349056/img/uEiR8K0UCaFoYsf-.jpg" alt="jev-usage-router" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/0xCodila/status/2101433560796467348">jev-usage-router</a></b><br><sub>0xCodila · X · ♥ 2.4k · 2026-09-19</sub><br>Usage router for Grok Bot: before browsing, research, retries or spawning extra bots, a Jev Choice picks the route, with a shadow mode, logs and a kill switch before it goes active.<br><sub><b>How it uses Jev:</b> A Choice call before each costly agent action decides which route to take.</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/_aj/status/2102061534956662818"><img src="https://pbs.twimg.com/media/HSwFAsyawAA4tst.jpg?name=orig" alt="AgentRun" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/_aj/status/2102061534956662818">AgentRun</a></b><br><sub>_aj · X · ♥ 1.6k · 2026-09-21</sub><br>Harness from Grep.ai for repetitive knowledge work that learns the job as it runs, moving steps from LLM calls to code; 100,000 compliance alerts cost under $26K versus over $290K on Opus 5.<br><sub>Also: <a href="https://x.com/MiguelriosEN/status/2100840456200581120">article</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/BerriAI/litellm/blob/main/litellm/router_strategy/complexity_router/jev_classifier.py"><img src="https://opengraph.githubassets.com/1/BerriAI/litellm" alt="LiteLLM Jev complexity router" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/BerriAI/litellm/blob/main/litellm/router_strategy/complexity_router/jev_classifier.py">LiteLLM Jev complexity router</a></b><br><sub>BerriAI · GitHub · ⭐ 59.4k repo · 2026-09-17</sub><br>LiteLLM's complexity-based router can use Jev to classify each request into configured tiers that pick the backend model; a separate guardrail blanks tool results Jev judges no longer needed.<br><sub><b>How it uses Jev:</b> A tier Choice per request for routing; the compaction guardrail asks one yes/no Noul per completed tool exchange.</sub><br><sub>Also: <a href="https://github.com/BerriAI/litellm">repo</a> · <a href="https://github.com/BerriAI/litellm/tree/main/litellm/proxy/guardrails/guardrail_hooks/typesafe">guardrail</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/eve/status/2100430918762832180"><img src="https://pbs.twimg.com/media/HSY6yf5a8AA8NJi.jpg?name=orig" alt="Criteria-based model routing in eve" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/eve/status/2100430918762832180">Criteria-based model routing in eve</a></b><br><sub>eve · X · ♥ 910 · 2026-09-17</sub><br>Experimental autoModel option in the eve agent framework that uses Jev to route each request between models described by plain-language criteria.<br><sub><b>How it uses Jev:</b> Choice between candidate models keyed by descriptions like "Complex reasoning and engineering tasks".</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/ephraimduncan/status/2100454070536351824"><img src="https://pbs.twimg.com/amplify_video_thumb/2100454021852954624/img/hqULLONlXw40573G.jpg" alt="Jev model router" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/ephraimduncan/status/2100454070536351824">Jev model router</a></b><br><sub>ephraimduncan · X · ♥ 1.9k · 2026-09-17</sub><br>Model router that asks Jev which language model best fits each incoming request and forwards the request to that model, shown in a demo video.<br><sub><b>How it uses Jev:</b> One Choice over the available models per request.</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/CodingGarden/status/2100665210419950031"><img src="https://pbs.twimg.com/amplify_video_thumb/2100664410935332864/img/KPApgq0AysL_SFeg.jpg" alt="Chat bot with no LLM" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/CodingGarden/status/2100665210419950031">Chat bot with no LLM</a></b><br><sub>CodingGarden · X · ♥ 1.2k · 2026-09-17</sub><br>Chat assistant built without any LLM: Jev picks the tool and its arguments across web search, Wikipedia, weather, Todoist and Home Assistant, so cited answers arrive instantly.<br><sub><b>How it uses Jev:</b> Choice of tool plus argument selection per prompt.</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/corentAI/status/2100965880242770423"><img src="https://pbs.twimg.com/amplify_video_thumb/2100964784581525504/img/S0fJrRk_X0OFZhdh.jpg" alt="Corent model routing" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/corentAI/status/2100965880242770423">Corent model routing</a></b><br><sub>corentAI · X · ♥ 320 · 2026-09-18</sub><br>Corent's router uses Jev to decide what each request needs across 1000+ models, how confident that call is, and whether to take the route or fall back, with stricter confidence for costly jobs like a $2 video clip.<br><sub><b>How it uses Jev:</b> Routing Choice with a per-workload confidence threshold before falling back.</sub><br><sub>Also: <a href="http://corent.tech">app</a> · <a href="https://corent.tech">project</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/tinyhumansai/openhuman/tree/main/crates/openhuman-tinyhumans/src/jev"><img src="https://raw.githubusercontent.com/tinyhumansai/openhuman/main/gitbooks/.gitbook/assets/demo.png" alt="OpenHuman Jev tool ranker" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/tinyhumansai/openhuman/tree/main/crates/openhuman-tinyhumans/src/jev">OpenHuman Jev tool ranker</a></b><br><sub>tinyhumansai · GitHub · ⭐ 40k repo · 2026-02-18</sub><br>Tool-search ranker for the OpenHuman agent harness that shortlists deferred tools with BM25 and lets one Jev Choice pick the right one, falling back to BM25 when signed out.<br><sub><b>How it uses Jev:</b> BM25 to 20 candidates, then one Choice with a 3 s deadline, routed through the backend's OpenRouter System One proxy.</sub><br><sub>Also: <a href="https://tinyhumans.ai/openhuman">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/PrefectHQ/fastmcp/blob/main/fastmcp_slim/fastmcp/experimental/transforms/jev_search.py"><img src="https://raw.githubusercontent.com/PrefectHQ/fastmcp/main/docs/assets/brand/f-watercolor-waves-2.png" alt="FastMCP Jev tool search" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/PrefectHQ/fastmcp/blob/main/fastmcp_slim/fastmcp/experimental/transforms/jev_search.py">FastMCP Jev tool search</a></b><br><sub>PrefectHQ · GitHub · ⭐ 27.9k repo · 2024-11-30</sub><br>Experimental FastMCP transform that ranks a server's tool catalog with Jev: a wide Choice over one-line summaries, then a close read of a shortlist with full descriptions.<br><sub><b>How it uses Jev:</b> A Choice orders the shortlist and one Noul per candidate checks it actually does what was asked, so a query nothing serves returns empty.</sub><br><sub>Also: <a href="https://gofastmcp.com">docs</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://www.youtube.com/watch?v=o4Vi5uBZYH0"><img src="https://i.ytimg.com/vi/o4Vi5uBZYH0/hqdefault.jpg" alt="Treg + Jev automation" width="240"></a></td>
<td valign="top"><b><a href="https://www.youtube.com/watch?v=o4Vi5uBZYH0">Treg + Jev automation</a></b><br><sub>AI Jason · YouTube · ♥ 856 · 2026-09-21</sub><br>Demo of pairing Jev with Treg, an OpenRouter-style registry of agent tools, to build automation workflows where Jev makes the quick decisions.<br><sub>Also: <a href="https://github.com/superdesigndev/treg">repo</a> · <a href="https://treg.to/jev">prompt</a> · <a href="https://github.com/superdesigndev/treg">project</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/MiguelriosEN/status/2101033282414768456"><img src="https://pbs.twimg.com/amplify_video_thumb/2101032781270917120/img/8tGv1qWQd8M9mEec.jpg" alt="AgentRun" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/MiguelriosEN/status/2101033282414768456">AgentRun</a></b><br><sub>MiguelriosEN · X · ♥ 311 · 2026-09-18</sub><br>Agent harness built with pi and Jev in which an agent learns how to do a job, writes itself a general reusable solution, and then gets out of the way.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/omarsar0/status/2101443311454036477"><img src="https://pbs.twimg.com/amplify_video_thumb/2101443076828925952/img/zVy7_B-F8UmXFdKK.jpg" alt="Goal-completion verifier" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/omarsar0/status/2101443311454036477">Goal-completion verifier</a></b><br><sub>omarsar0 · X · ♥ 1k · 2026-09-19</sub><br>Custom verifier for the /goal feature in an agent harness that uses Jev to check after every turn whether the goal is actually complete, replacing an expensive reasoning model.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/RoundtableSpace/status/2102167236714574280"><img src="https://pbs.twimg.com/amplify_video_thumb/2102148770343407616/img/-rVahOyOBdklAAqC.jpg" alt="HarnessRouter" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/RoundtableSpace/status/2102167236714574280">HarnessRouter</a></b><br><sub>RoundtableSpace · X · ♥ 61 · 2026-09-21</sub><br>Open-source layer that runs Codex, Claude Code, Hermes, DeepSeek Harness, a Jev-powered System One harness and 9 more behind one interface, with a Unified Harness Protocol and an OpenAI Responses-compatible API.<br><sub>Also: <a href="https://github.com/harnessrouter/harnessrouter">repo</a> · <a href="https://harnessrouter.ai/">app</a> · <a href="https://github.com/harnessrouter/harnessrouter">project</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/rileybrown/status/2100607709317861879"><img src="https://pbs.twimg.com/amplify_video_thumb/2100607557995761664/img/a_foq8dIW_wwab7W.jpg" alt="Agent with a Jev model router" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/rileybrown/status/2100607709317861879">Agent with a Jev model router</a></b><br><sub>rileybrown · X · ♥ 283 · 2026-09-17</sub><br>Agent build in which Jev acts as the model router, choosing which model handles each request.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/johnyeo_/status/2100987661926252737"><img src="https://pbs.twimg.com/amplify_video_thumb/2100986453845028864/img/YknQ8SR5kudv19m-.jpg" alt="Slack agent pre-routing" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/johnyeo_/status/2100987661926252737">Slack agent pre-routing</a></b><br><sub>johnyeo_ · X · ♥ 166 · 2026-09-18</sub><br>Slack agent made 2x faster by first asking Jev to pick the best skill, tool and parameters from the prompt before the agent runs.<br><sub><b>How it uses Jev:</b> Choice over skills and tools plus parameter picks, before handing off to the LLM agent.</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/rashedInt32/jev-mcp"><img src="https://pbs.twimg.com/media/HSeMX0_bYAARs-3.jpg" alt="jev-mcp" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/rashedInt32/jev-mcp">jev-mcp</a></b><br><sub>rashedInt32 · GitHub · ⭐ 6 · 2026-09-17</sub><br>MCP server and Claude Code plugin exposing Jev as classify, score, check and batched ask tools that return the typed answer with its full probability distribution.<br><sub>Also: <a href="https://www.npmjs.com/package/jev-mcp">npm</a> · <a href="https://x.com/takamasa045/status/2100809434587124208">write-up</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/kerpopule/hermes-jev-skills"><img src="https://raw.githubusercontent.com/kerpopule/hermes-jev-skills/main/docs/images/model-routing-dashboard.png" alt="Hermes Jev skills" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/kerpopule/hermes-jev-skills">Hermes Jev skills</a></b><br><sub>kerpopule · GitHub · ⭐ 405 · 2026-09-18</sub><br>Routing, memory, skill-selection, and triage skills for Hermes, Claude Code, and Codex that start in shadow mode and publish their failures.<br><sub>Also: <a href="https://x.com/StevenDarlow/status/2101115049280422332">demo</a> · <a href="https://x.com/StevenDarlow/status/2101526148228227519">post</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/ThinkInAIXYZ/deepchat/blob/dev/src/main/provider/providers/jevProvider.ts"><img src="https://opengraph.githubassets.com/1/ThinkInAIXYZ/deepchat" alt="DeepChat Jev judgment model" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/ThinkInAIXYZ/deepchat/blob/dev/src/main/provider/providers/jevProvider.ts">DeepChat Jev judgment model</a></b><br><sub>ThinkInAIXYZ · GitHub · ⭐ 6.3k repo · 2025-02-14</sub><br>DeepChat's desktop agent client adds Jev as a provider plus an opt-in judgment-model slot that reviews tool-permission requests through the System One protocol.<br><sub><b>How it uses Jev:</b> Chat entry points fail loudly for Jev by design; runtime files also cover Jev-based tool-result pruning.</sub><br><sub>Also: <a href="https://github.com/ThinkInAIXYZ/deepchat/blob/dev/docs/features/agent-judgment-model/spec.md">docs</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/BuilderIO/agent-native/blob/main/packages/core/src/agent/jev-tool-prefetch.ts"><img src="https://cdn.builder.io/api/v1/image/assets%2FYJIGb4i01jvw0SRdL5Bt%2F7628600bc10a4940b78f42c5df7628b0" alt="Agent-native tool prefetch" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/BuilderIO/agent-native/blob/main/packages/core/src/agent/jev-tool-prefetch.ts">Agent-native tool prefetch</a></b><br><sub>BuilderIO · GitHub · ⭐ 6.1k repo · 2026-03-12</sub><br>Ranks up to 128 tools and skills with a single Choice and preloads the top three within 750 ms.<br><sub>Also: <a href="https://www.agent-native.com">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/JamesWard/status/2100976393546772628"><img src="https://pbs.twimg.com/media/HSgovFqXoAAih_x.png?name=orig" alt="Jev as MCP workflow orchestrator" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/JamesWard/status/2100976393546772628">Jev as MCP workflow orchestrator</a></b><br><sub>JamesWard · X · ♥ 298 · 2026-09-18</sub><br>Two patterns for combining Jev, LLMs and MCP: Jev as an outer loop that chooses valid actions to build a workflow AST from MCP output schemas, with a single LLM call writing the final answer.<br><sub><b>How it uses Jev:</b> Choice over valid actions per step, then semantic filtering of MCP results.</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/milindlabs/status/2100515910754750741"><img src="https://pbs.twimg.com/amplify_video_thumb/2100515619712184320/img/LFrKN4XyJ024sGe_.jpg" alt="OpenMausBot chief of staff" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/milindlabs/status/2100515910754750741">OpenMausBot chief of staff</a></b><br><sub>milindlabs · X · ♥ 184 · 2026-09-17</sub><br>Multi-agent setup on OpenMausBot where Jev reads each task, wakes the right agents and assigns each one a model from the user's existing subscriptions.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/0xPaulius/status/2101312576252481785"><img src="https://pbs.twimg.com/amplify_video_thumb/2101278375423737856/img/AcdfybGwO7dAi1Gu.jpg" alt="Clonk agent canvas" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/0xPaulius/status/2101312576252481785">Clonk agent canvas</a></b><br><sub>0xPaulius · X · ♥ 174 · 2026-09-19</sub><br>Agent orchestrator on a canvas where Jev instantly decides actions such as launching agents, instead of waiting on a slow LLM loop.<br><sub>Also: <a href="https://clonk.ai">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/shengkunye/status/2102112693041938825"><img src="https://pbs.twimg.com/amplify_video_thumb/2102112249112604672/img/3lR6gxILRYKTiMF_.jpg" alt="Monid tools with Jev" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/shengkunye/status/2102112693041938825">Monid tools with Jev</a></b><br><sub>shengkunye · X · ♥ 166 · 2026-09-21</sub><br>Monid integration that lets an agent use Jev through OpenRouter across 2,000 tools, for jobs like scoring 2,000 leads, scanning TikTok hooks, or sorting Reddit threads, with a claimed 30x speed-up.<br><sub>Also: <a href="https://monid.ai">app</a> · <a href="https://monid.ai">project</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/jkudish/jev-mcp"><img src="https://opengraph.githubassets.com/1/jkudish/jev-mcp" alt="jev-mcp" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/jkudish/jev-mcp">jev-mcp</a></b><br><sub>jkudish · GitHub · ⭐ 247 · 2026-09-17</sub><br>Ten MCP judgment tools for agents, including claim verification, injection screening, reranking, and gating.<br><sub>Also: <a href="https://x.com/jkudish/status/2100413576284712999">demo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/truespar/sentio"><img src="https://repository-images.githubusercontent.com/1344239263/60e2f09e-0eb6-419c-9533-ef350c19bbab" alt="Sentio SMTP" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/truespar/sentio">Sentio SMTP</a></b><br><sub>truespar · GitHub · ⭐ 246 · 2026-08-23</sub><br>Multi-tenant Rust mail server that gives AI agents their own inboxes and can use Jev as a message classifier to label inbound mail without changing the spam score.<br><sub><b>How it uses Jev:</b> Implements only a MessageClassifier: Choice and Noul labels with calibrated confidence, no generated replies.</sub><br><sub>Also: <a href="https://truespar.com/sentio">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/aipoch/open-science/blob/main/src/main/settings/classification-settings.ts"><img src="https://raw.githubusercontent.com/aipoch/open-science/main/docs/images/readme/open-science-banner.png" alt="Open-Science Jev classification" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/aipoch/open-science/blob/main/src/main/settings/classification-settings.ts">Open-Science Jev classification</a></b><br><sub>aipoch · GitHub · ⭐ 4.9k repo · 2026-07-03</sub><br>Classification service in the AIPOCH Open-Science research workbench that uses Jev to select which skills a request needs and whether a document should be read in full.<br><sub><b>How it uses Jev:</b> Runs on jev-latest via TypeSafe, OpenRouter or a custom endpoint, with a byte budget kept under TypeSafe's context limit even for CJK text.</sub><br><sub>Also: <a href="https://aipoch.com/open-science">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/itsmostafa/typesafe-mcp"><img src="https://external-preview.redd.it/foplw_1lcxzLSY41H2Wc8jTRi55au8rxPSdCeT9nTBw.png?auto=webp&amp;s=c9f26ce3c9d2b86f15dc4763a0a17436e965e121" alt="typesafe-mcp" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/itsmostafa/typesafe-mcp">typesafe-mcp</a></b><br><sub>itsmostafa · GitHub · ⭐ 229 · 2026-09-17</sub><br>Go MCP server that exposes one evaluate tool so Claude Code, Claude Desktop, Codex and pi can send state plus Choice, Score or Noul questions to Jev and branch on the probabilities.<br><sub>Also: <a href="https://www.reddit.com/r/mcp/comments/1wjfjn3/if_you_have_access_to_the_new_typesafe_ai_try/">discussion</a> · <a href="https://x.com/CindyTaylo82399/status/2101873521077157968">demo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/john_bortotti/status/2102113996505518388"><img src="https://pbs.twimg.com/amplify_video_thumb/2102112486837096449/img/-pAuYpFAhQmzM0uC.jpg" alt="Character memory that judges" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/john_bortotti/status/2102113996505518388">Character memory that judges</a></b><br><sub>john_bortotti · X · ♥ 88 · 2026-09-21</sub><br>Character memory system from Mutuals where one Jev call per message decides whether to keep it, which exact words, where it fits, what it makes outdated and what it recalls.<br><sub><b>How it uses Jev:</b> Several typed questions per incoming message answered in a single Jev call.</sub><br><sub>Also: <a href="https://mutuals.inc">company</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/kitze/skillbox"><img src="https://opengraph.githubassets.com/1/kitze/skillbox" alt="skillbox" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/kitze/skillbox">skillbox</a></b><br><sub>kitze · GitHub · ⭐ 223 · 2026-09-17</sub><br>Self-hosted, versioned skills library for AI agents served over MCP with scoped clients, where Jev can optionally recommend which of the skills a client may access fit the current task.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/UnCorped/status/2101707226666893553"><img src="https://pbs.twimg.com/media/HSrBRezaEAEkcmz.jpg" alt="Smriti with Jev" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/UnCorped/status/2101707226666893553">Smriti with Jev</a></b><br><sub>UnCorped · Article · ♥ 17 · 2026-09-20</sub><br>Case study of adding Jev to Smriti, a local SQLite memory layer for agents: Jev pulled more evidence into context but some answers got worse, improving only modestly after relabeling.<br><sub><b>How it uses Jev:</b> Labels retrieved memory evidence before it is passed to the answering model.</sub><br><sub>Also: <a href="https://github.com/vn-envy/Smriti">repo</a> · <a href="https://github.com/vn-envy/smriti">project</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/tinyhumansai/opencompany"><img src="https://raw.githubusercontent.com/tinyhumansai/opencompany/main/docs/gitbooks/.gitbook/assets/opencompany-hero.png" alt="OpenCompany" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/tinyhumansai/opencompany">OpenCompany</a></b><br><sub>tinyhumansai · GitHub · ⭐ 196 · 2026-07-10</sub><br>Agent hive for one-person businesses where Jev decides who a message needs and who picks up a broadcast, falling back to the desk lead without a key.<br><sub><b>How it uses Jev:</b> Choice over desk members plus "none", sent through the TinyHumans proxy.</sub><br><sub>Also: <a href="https://tinyhumans.ai/opencompany">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/dealerdefi/Jevmind"><img src="https://raw.githubusercontent.com/dealerdefi/Jevmind/main/assets/banner.jpg" alt="Jevmind" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/dealerdefi/Jevmind">Jevmind</a></b><br><sub>dealerdefi · GitHub · ⭐ 164 · 2026-09-15</sub><br>Zero-dependency Python toolkit that pulls an agent's decisions out of prose into typed, confidence-scored answers behind a code gate, logged in a graded ledger, with a local rules brain or Jev behind one flag.<br><sub>Also: <a href="https://x.com/dealerdefi/status/2102167087309369731">demo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Foxtailsss-Andy/Anna-Agent"><img src="https://raw.githubusercontent.com/Foxtailsss-Andy/Anna-Agent/main/docs/public/assets/anna-readme-banner-v2.png" alt="Anna" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Foxtailsss-Andy/Anna-Agent">Anna</a></b><br><sub>Foxtailsss-Andy · GitHub · ⭐ 149 · 2026-04-02</sub><br>Governed local-first enterprise agent whose Crew feature suggests a person or worker for an unassigned task with Jev, which can abstain; it matched a DeepSeek judge on 22/22 cases at 85.23% lower p50 latency.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/BillionsBobby/JevRouter"><img src="https://raw.githubusercontent.com/BillionsBobby/JevRouter/main/docs/assets/jev-api-router-comparison.png" alt="JevRouter" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/BillionsBobby/JevRouter">JevRouter</a></b><br><sub>BillionsBobby · GitHub · ⭐ 148 · 2026-09-18</sub><br>Treats models, subagents, skills, MCP servers, and CLIs as one candidate pool and routes with a two-stage Choice when the pool is large.<br><sub>Also: <a href="https://jevrouter.co">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/rlaope/oh-my-hermes/blob/main/src/plugin_bundle/omh/jev_sidekick.py"><img src="https://raw.githubusercontent.com/rlaope/oh-my-hermes/main/assets/oh-my-hermes-wordmark.png" alt="oh-my-hermes Jev posture" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/rlaope/oh-my-hermes/blob/main/src/plugin_bundle/omh/jev_sidekick.py">oh-my-hermes Jev posture</a></b><br><sub>rlaope · GitHub · ⭐ 2.9k repo · 2026-06-03</sub><br>Module in the oh-my-hermes plugin that detects Jev-class Hermes plugins on a machine and reports what each declares about its tools, hooks and data flow, without claiming any ran.<br><sub><b>How it uses Jev:</b> Recognizes jev_-prefixed tools and known Jev credential env names, and routes a tool-approval question to Jev when a Jev-class plugin is present.</sub><br><sub>Also: <a href="https://rlaope.github.io/oh-my-hermes/">docs</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/elie222/rakazo/blob/main/packages/adapters/src/jev-auto-review.ts"><img src="https://raw.githubusercontent.com/elie222/rakazo/main/docs/readme-hero.png" alt="Rakazo Jev auto-review" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/elie222/rakazo/blob/main/packages/adapters/src/jev-auto-review.ts">Rakazo Jev auto-review</a></b><br><sub>elie222 · GitHub · ⭐ 2.8k repo · 2026-08-13</sub><br>Auto-review adapter in the open-source Rakazo AI-teammate platform that asks Jev whether a bot tool call should auto-pass or be sent to the user for approval.<br><sub><b>How it uses Jev:</b> A Choice of pass or ask against a confidence threshold; anything unexpected or high risk defaults to ask.</sub><br><sub>Also: <a href="https://rakazo.com">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/StarchildOnX/status/2100936455401214327"><img src="https://pbs.twimg.com/amplify_video_thumb/2100926778047148032/img/RUW0O6LMX9L7TRzk.jpg" alt="Starchild prompt routing" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/StarchildOnX/status/2100936455401214327">Starchild prompt routing</a></b><br><sub>StarchildOnX · X · ♥ 29 · 2026-09-18</sub><br>LLM router in the Starchild app that classifies prompts in real time (avg 140ms), reported as a 20x cost decrease and 6x speedup for prompt classification.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/lioensky/VCPToolBox/blob/main/modules/jevClient.js"><img src="https://raw.githubusercontent.com/lioensky/VCPToolBox/main/docs/image/VCPLogo.png" alt="VCPToolBox Jev modules" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/lioensky/VCPToolBox/blob/main/modules/jevClient.js">VCPToolBox Jev modules</a></b><br><sub>lioensky · GitHub · ⭐ 2.3k repo · 2025-05-12</sub><br>The VCP agent infrastructure adds Jev modules for context pruning, fold filtering, reranking and a semantic tool-call experiment, with multi-key rotation over TypeSafe or OpenRouter.<br><sub><b>How it uses Jev:</b> jevClient speaks Noul, Choice and Score with retry and key rotation; separate modules apply it to context management and tool selection.</sub><br><sub>Also: <a href="https://www.vcptoolbox.com">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/TianyuCodings/JevHarness"><img src="https://opengraph.githubassets.com/1/TianyuCodings/JevHarness" alt="JevHarness" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/TianyuCodings/JevHarness">JevHarness</a></b><br><sub>TianyuCodings · GitHub · ⭐ 109 · 2026-09-21</sub><br>Framework where a strong LLM writes a task-specific harness that turns observations into Jev questions and actions, then freezes it and optionally improves it from rewards and full execution traces with GEPA.<br><sub>Also: <a href="https://jev-harness.tianyuchen99.chatgpt.site">site</a> · <a href="https://jev-harness.tianyuchen99.chatgpt.site">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Dicklesworthstone/skillranker"><img src="https://opengraph.githubassets.com/1/Dicklesworthstone/skillranker" alt="skillranker" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Dicklesworthstone/skillranker">skillranker</a></b><br><sub>Dicklesworthstone · GitHub · ⭐ 109 · 2026-09-17</sub><br>Rust CLI that ranks skills for the current session with a wide Choice, then confirms a shortlist with one Noul each (custom license with usage restrictions).</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/k_grajeda/status/2101021361351131464"><img src="https://pbs.twimg.com/amplify_video_thumb/2101018655794331648/img/xm_XTf33FJqqEmIb.jpg" alt="Prompt difficulty classifier" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/k_grajeda/status/2101021361351131464">Prompt difficulty classifier</a></b><br><sub>k_grajeda · X · ♥ 47 · 2026-09-18</sub><br>Chat UI check that classifies the difficulty of the prompt each time the user stops typing and, for simple prompts, offers a fast mode before they hit send.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/HarnessRouter/SystemOneHarness"><img src="https://opengraph.githubassets.com/1/HarnessRouter/SystemOneHarness" alt="System One Harness" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/HarnessRouter/SystemOneHarness">System One Harness</a></b><br><sub>HarnessRouter · GitHub · ⭐ 95 · 2026-09-19</sub><br>Python controller that turns a System One model into an agent loop, compiling an environment's finite action space into typed Jev questions, gating each step by confidence, and recording the full trace.<br><sub>Also: <a href="https://news.ycombinator.com/item?id=49778358">discussion</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/w3cj/jev-chat"><img src="https://raw.githubusercontent.com/w3cj/jev-chat/main/screenshot.png" alt="Jev Chat" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/w3cj/jev-chat">Jev Chat</a></b><br><sub>w3cj · GitHub · ⭐ 85 · 2026-09-18</sub><br>Chat-style command bar where Jev picks the intent, tool, argument values, confirmation, and reply shape each turn, and code calls MCP servers and builds the reply from their data, so no model writes text.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Devin-AXIS/jev-dsh-decision"><img src="https://raw.githubusercontent.com/Devin-AXIS/jev-dsh-decision/main/assets/jev.png" alt="Jev DSH Decision Engine" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Devin-AXIS/jev-dsh-decision">Jev DSH Decision Engine</a></b><br><sub>Devin-AXIS · GitHub · ⭐ 82 · 2026-09-20</sub><br>Agent-harness plugin that recommends which available tool, skill, or agent to use and rates output quality, running natively in DeepSeek Harness and via iPolloWork in OpenCode and Codex Harness.<br><sub><b>How it uses Jev:</b> Structured judgments with probabilities; the host agent keeps planning and execution.</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/baldaworks/callee"><img src="https://opengraph.githubassets.com/1/baldaworks/callee" alt="Callee" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/baldaworks/callee">Callee</a></b><br><sub>baldaworks · GitHub · ⭐ 74 · 2026-07-14</sub><br>Markdown- and YAML-defined agent workflows for ACP runtimes that mix coding models, shell checks and human steps with a native TypeSafeJev evaluator for typed decisions and routing.<br><sub>Also: <a href="https://github.com/baldaworks/callee/blob/main/docs/agent-kinds/typesafe-jev.md">docs</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Bodila51/grok-bot-jev"><img src="https://raw.githubusercontent.com/Bodila51/grok-bot-jev/main/media/jev-grok-bot-dashboard.png" alt="Grok Bot Jev Router" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Bodila51/grok-bot-jev">Grok Bot Jev Router</a></b><br><sub>Bodila51 · GitHub · ⭐ 74 · 2026-09-19</sub><br>Reference router that puts Jev in front of Grok Bot to classify each request before costly research, browser, retry or subagent work, choosing actions like reusing a cached artifact, stopping a retry or asking a human.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/vbcherepanov/total-agent-memory"><img src="https://repository-images.githubusercontent.com/1159027243/9e951761-4a30-40e2-b32a-297ac9223ea7" alt="total-agent-memory" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/vbcherepanov/total-agent-memory">total-agent-memory</a></b><br><sub>vbcherepanov · GitHub · ⭐ 68 · 2026-02-16</sub><br>Local persistent memory for coding agents that can check retrieved facts for contradictions with Jev; median pass time fell from 3.1 s to 1.9 s with accuracy unchanged, costing $0.038 for 78 questions.<br><sub><b>How it uses Jev:</b> Every (supporting, opposing) fact pair becomes one Noul, all in a single request.</sub><br><sub>Also: <a href="https://totalmemory.dev">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/heymrun/heym/blob/main/backend/app/services/decision_models.py"><img src="https://raw.githubusercontent.com/heymrun/heym/main/docs/readme-assets/hero.svg" alt="Heym decision models" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/heymrun/heym/blob/main/backend/app/services/decision_models.py">Heym decision models</a></b><br><sub>heymrun · GitHub · ⭐ 1.2k repo · 2026-03-28</sub><br>Heym, a self-hosted agent orchestration runtime, adds a decision-model service built on TypeSafe's /v1/systemone contract so workflows can answer typed questions with tracing and SSRF guards.<br><sub>Also: <a href="https://heym.run">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Asymptote-Labs/agent-beacon/tree/main/cli/beacon/internal/learning"><img src="https://opengraph.githubassets.com/1/Asymptote-Labs/agent-beacon" alt="Beacon Jev memory evaluations" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Asymptote-Labs/agent-beacon/tree/main/cli/beacon/internal/learning">Beacon Jev memory evaluations</a></b><br><sub>Asymptote-Labs · GitHub · ⭐ 926 repo · 2026-09-21</sub><br>Evaluation command in Beacon, a cross-harness memory layer for coding agents, that has Jev judge redacted session-trace projections against a rubric for reusable lessons, which a person reviews before saving.<br><sub>Also: <a href="https://beacon.sh">site</a> · <a href="https://github.com/Asymptote-Labs/agent-beacon">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/rohanarun/computer-use-cache"><img src="https://storage.googleapis.com/cheatlayer/landing/computer-use-cache-super-api-hero.jpeg" alt="computer-use-cache" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/rohanarun/computer-use-cache">computer-use-cache</a></b><br><sub>rohanarun · GitHub · ⭐ 42 · 2026-06-04</sub><br>OpenAI-compatible caching proxy that replays repeated computer-use and coding-agent requests. On an exact miss, Jev compares recent cached requests and picks a reusable response or none; anything uncertain goes upstream.<br><sub><b>How it uses Jev:</b> One choice over up to 8 cached candidates plus none, accepted at 0.95 confidence; matches are tagged X-Computer-Use-Cache-Match: jev.</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/lioensky/VCPChat/blob/main/modules/services/globalJevService.js"><img src="https://raw.githubusercontent.com/lioensky/VCPChat/main/assets/E1-Vchat%E4%B8%BB%E7%95%8C%E9%9D%A2.jpg" alt="VCPChat global Jev service" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/lioensky/VCPChat/blob/main/modules/services/globalJevService.js">VCPChat global Jev service</a></b><br><sub>lioensky · GitHub · ⭐ 778 repo · 2025-06-02</sub><br>VCPChat, the desktop terminal for the VCP AI-native engine, adds a global Jev service so its modules can make typed decisions through TypeSafe or OpenRouter.<br><sub><b>How it uses Jev:</b> Provider defaults for typesafe (jev-latest) and openrouter (~typesafe/jev-latest) over the shared jevClient.</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/kitfunso/hippo-memory/blob/master/src/rerankers/jev.ts"><img src="https://raw.githubusercontent.com/kitfunso/hippo-memory/master/assets/hippo-init.svg" alt="Hippo Jev reranker" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/kitfunso/hippo-memory/blob/master/src/rerankers/jev.ts">Hippo Jev reranker</a></b><br><sub>kitfunso · GitHub · ⭐ 752 repo · 2026-03-15</sub><br>Opt-in reranker in the Hippo agent-memory system that batches Jev Noul judgments over the top 40 recalled memories and falls back to a local cross-encoder; the author's study found better ranking but no answer-quality gain.<br><sub>Also: <a href="https://github.com/kitfunso/hippo-memory">repo</a> · <a href="https://hippo-memory.com">website</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/shantanugoel/ask-jev-skill"><img src="https://opengraph.githubassets.com/1/shantanugoel/ask-jev-skill" alt="askjev" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/shantanugoel/ask-jev-skill">askjev</a></b><br><sub>shantanugoel · GitHub · ⭐ 37 · 2026-09-17</sub><br>Hermes skill, usable by other agents, that calls Jev as a typed tiebreaker so the agent can act on a confident Choice, Score, or Noul answer or escalate.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/tacticocc/Jevbridge"><img src="https://opengraph.githubassets.com/1/tacticocc/Jevbridge" alt="Jevbridge" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/tacticocc/Jevbridge">Jevbridge</a></b><br><sub>tacticocc · GitHub · ⭐ 37 · 2026-09-18</sub><br>ACP and MCP adapter plus CLI that puts Jev's typed decisions beside Codex, Claude, Grok and OpenCode for routing, gating, scoring and computer use, with an offline rule backend.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/alexjhancock/status/2100932130196852896"><img src="https://pbs.twimg.com/amplify_video_thumb/2100932017512763392/img/Xe2wlgj78FcAayZ2.jpg" alt="Just-in-time model selection in Goose" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/alexjhancock/status/2100932130196852896">Just-in-time model selection in Goose</a></b><br><sub>alexjhancock · X · ♥ 22 · 2026-09-18</sub><br>Prototype for the Goose agent harness that has Jev read each prompt and pick which model should run the turn just before it starts.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/0xkaushik_k/status/2100928490367230201"><img src="https://pbs.twimg.com/amplify_video_thumb/2100928298834374656/img/LvjSbqapVvdNdvrK.jpg" alt="JevScope" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/0xkaushik_k/status/2100928490367230201">JevScope</a></b><br><sub>0xkaushik_k · X · ♥ 10 · 2026-09-18</sub><br>Watches an AI agent work and plots per-step judgments of task alignment, progress, repetition and being stuck, shown catching a coding agent looping on a race condition.<br><sub><b>How it uses Jev:</b> Per-step judgments over agent trace steps: aligned with task, progress, repeating, stuck.</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/automateyournetwork/netclaw/tree/main/scripts/jev-audit"><img src="https://raw.githubusercontent.com/automateyournetwork/netclaw/main/netclaw.jpg" alt="NetClaw jev-audit" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/automateyournetwork/netclaw/tree/main/scripts/jev-audit">NetClaw jev-audit</a></b><br><sub>automateyournetwork · GitHub · ⭐ 664 repo · 2026-02-19</sub><br>Skill-audit sweeps in the NetClaw network agent that use Jev to flag ambiguous triggers, missing failure behavior, stale assumptions and injection smells, and to map skill overlap and coverage gaps.<br><sub><b>How it uses Jev:</b> Noul-style questions per skill with collision and coverage thresholds, aggregated into a findings report.</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/matrixorigin/Astra"><img src="https://raw.githubusercontent.com/matrixorigin/Astra/main/docs/assets/explain-analyze-demo.gif" alt="Astra" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/matrixorigin/Astra">Astra</a></b><br><sub>matrixorigin · GitHub · ⭐ 32 · 2026-02-09</sub><br>Self-hosted runtime for long-running enterprise agents with EXPLAIN ANALYZE for context and native Jev judgments at four decision points: memory filtering, lesson dismissal, request classification and skill selection.<br><sub><b>How it uses Jev:</b> Shared typed questions, validated responses, provider routing and usage accounting across callers; Jev is configured separately from the generation model.</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/The-Vibe-Company/granite"><img src="https://raw.githubusercontent.com/The-Vibe-Company/granite/main/docs/screenshots/granite-graph.png" alt="Granite" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/The-Vibe-Company/granite">Granite</a></b><br><sub>The-Vibe-Company · GitHub · ⭐ 32 · 2026-03-30</sub><br>Local-first markdown knowledge compiler and MCP server that serves as agent memory; its only model is Jev, which picks which candidate from a deterministically bounded set answers a question and judges every capture.<br><sub><b>How it uses Jev:</b> Jev returns a choice, score or probability over a set Granite chose; it never writes links, and Granite refuses to start without a key.</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/AgentiLoop/Agent/blob/main/Agent/Services/JevAdvisor.swift"><img src="https://raw.githubusercontent.com/AgentiLoop/Agent/main/agent-demo.gif" alt="Agent! Jev advisor" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/AgentiLoop/Agent/blob/main/Agent/Services/JevAdvisor.swift">Agent! Jev advisor</a></b><br><sub>AgentiLoop · GitHub · ⭐ 623 repo · 2026-09-18</sub><br>Jev advisor in Agent!, a native macOS agent app, that gives a second opinion on shell commands already passed by pattern rules and refuses those whose data-destruction probability exceeds a user-set threshold.<br><sub><b>How it uses Jev:</b> Uses the bundled TypeSafeKit Swift client and fails open so an outage never stalls the tool loop.</sub><br><sub>Also: <a href="https://github.com/AgentiLoop/Agent">repo</a> · <a href="https://github.com/AgentiLoop/Agent/tree/main/TypeSafeKit">sdk</a> · <a href="https://agentiloop.ai">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/samdotmak/jev-recall"><img src="https://opengraph.githubassets.com/1/samdotmak/jev-recall" alt="Jev Recall" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/samdotmak/jev-recall">Jev Recall</a></b><br><sub>samdotmak · GitHub · ⭐ 31 · 2026-09-19</sub><br>Memory retrieval for AI assistants that returns the memories actually relevant to a query rather than the ones that look similar, aiming for reranker quality at semantic-search cost and speed.<br><sub><b>How it uses Jev:</b> One calibrated Noul per memory in a single request.</sub><br><sub>Also: <a href="https://www.reddit.com/r/MachineLearning/comments/1wl31tp/jev_to_retrieve_memories_is_a_game_changer_p/">demo</a> · <a href="https://www.reddit.com/r/LangChain/comments/1wl324b/jev_to_retrieve_memories_is_a_game_changer_p/">discussion</a> · <a href="https://jev-recall.vercel.app">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/ksenxx/kiss_ai/blob/main/src/kiss/agents/sorcar/decide_tool.py"><img src="https://raw.githubusercontent.com/ksenxx/kiss_ai/main/assets/KISS-Sorcar.png" alt="KISS Sorcar decide tool" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/ksenxx/kiss_ai/blob/main/src/kiss/agents/sorcar/decide_tool.py">KISS Sorcar decide tool</a></b><br><sub>ksenxx · GitHub · ⭐ 553 repo · 2026-01-09</sub><br>KISS Sorcar, a general-purpose agent framework for long-horizon tasks, gives the agent a decide tool that asks Jev typed questions to pick its next move.<br><sub><b>How it uses Jev:</b> noul, choice and score questions through OpenRouter's ~typesafe/jev-latest, callable in parallel.</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/CoWork-OS/CoWork-OS/blob/main/src/electron/agent/decisions/typesafe-provider.ts"><img src="https://raw.githubusercontent.com/CoWork-OS/CoWork-OS/main/screenshots/cowork-os-sl-color-logo.png" alt="CoWork OS TypeSafe decisions" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/CoWork-OS/CoWork-OS/blob/main/src/electron/agent/decisions/typesafe-provider.ts">CoWork OS TypeSafe decisions</a></b><br><sub>CoWork-OS · GitHub · ⭐ 457 repo · 2026-01-24</sub><br>CoWork OS, a local-first agentic everything-app, adds a TypeSafe decision provider so its agents can make typed judgments over /v1/systemone.<br><sub><b>How it uses Jev:</b> An HTTP decision provider defaulting to jev-latest.</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/openagentsinc/openagents/tree/main/crates/jev"><img src="https://opengraph.githubassets.com/1/openagentsinc/openagents" alt="OpenAgents Jev" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/openagentsinc/openagents/tree/main/crates/jev">OpenAgents Jev</a></b><br><sub>openagentsinc · GitHub · ⭐ 449 repo · 2023-11-07</sub><br>OpenAgents builds general agent infrastructure where every turn starts with a Jev typed judgment that returns a choice and probabilities, foldable back into the round.<br><sub><b>How it uses Jev:</b> A Rust Jev SDK crate with typed Choice, Noul and Score answers powering the turn loop's respond/retry/stop verdicts.</sub><br><sub>Also: <a href="https://openagents.com">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/professorpalmer/puppetmaster/tree/main/puppetmaster/jev"><img src="https://raw.githubusercontent.com/professorpalmer/Puppetmaster/main/docs/demo.gif" alt="Puppetmaster Jev" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/professorpalmer/puppetmaster/tree/main/puppetmaster/jev">Puppetmaster Jev</a></b><br><sub>professorpalmer · GitHub · ⭐ 449 repo · 2026-05-06</sub><br>Puppetmaster, a control plane for durable-state agent swarms, uses Jev for conflict, already-answered, admission and stop decisions across its worker stitching.<br><sub><b>How it uses Jev:</b> Questions and thresholds via OpenRouter's ~typesafe/jev-latest on a 2 second timeout.</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/AgorithmAg/status/2102169114542301526"><img src="https://pbs.twimg.com/media/HSxnqknWEAAgfFK.jpg?name=orig" alt="Drift developmental memory" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/AgorithmAg/status/2102169114542301526">Drift developmental memory</a></b><br><sub>AgorithmAg · X · ♥ 15 · 2026-09-21</sub><br>AI companion given a Jev-based developmental memory that records what it tried, how the user reacted and what it learned, keeping behavior consistent across the different models that run it.<br><sub>Also: <a href="https://drift-riverbed.com/developmental-memory.html">spec</a> · <a href="https://drift-riverbed.com/developmental-memory.html">project</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://www.elvex.com/blog/early-experimentation-using-jev-to-rethink-harness-ux"><img src="https://cdn.prod.website-files.com/6866aba1d492c973444d9b24/6aad9db0d4b0c68d2079c47f_Blog%20Hero%20Image(6).png" alt="Jev in the elvex harness" width="240"></a></td>
<td valign="top"><b><a href="https://www.elvex.com/blog/early-experimentation-using-jev-to-rethink-harness-ux">Jev in the elvex harness</a></b><br><sub>Doyle Irvin (elvex) · Article · ▲ 7 · 2026-09-18</sub><br>Agent platform write-up on wiring Jev into an LLM harness as a callable tool for search, approvals and context, including 2,000 expense reports categorized in 20 seconds for 5 cents.<br><sub>Also: <a href="https://news.ycombinator.com/item?id=49760264">discussion</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/trytenjin/status/2101817410307137937"><img src="https://pbs.twimg.com/amplify_video_thumb/2101816882080718849/img/i6lPMBe0BF-LOcae.jpg" alt="Jev x402 tool selection" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/trytenjin/status/2101817410307137937">Jev x402 tool selection</a></b><br><sub>trytenjin · X · ♥ 13 · 2026-09-20</sub><br>Live demo from Tenjin of Jev choosing which paid x402 endpoint to call from a curated set of tools.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/decocms/studio/blob/main/apps/api/src/tools/task-board/duplicate-decisions.ts"><img src="https://opengraph.githubassets.com/1/decocms/studio" alt="Deco Studio Jev task dedupe" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/decocms/studio/blob/main/apps/api/src/tools/task-board/duplicate-decisions.ts">Deco Studio Jev task dedupe</a></b><br><sub>decocms · GitHub · ⭐ 408 repo · 2025-03-14</sub><br>Agent control plane whose task board first asks Jev whether incoming tasks duplicate existing cards, falling back to a fast LLM when Jev is unavailable or unsure.<br><sub><b>How it uses Jev:</b> One shared state with one Choice per incoming task (including "none"); answers are accepted only if every choice has probability of at least 0.95.</sub><br><sub>Also: <a href="https://decocms.com/studio">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/runta-dev/jot"><img src="https://opengraph.githubassets.com/1/runta-dev/jot" alt="Jot" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/runta-dev/jot">Jot</a></b><br><sub>runta-dev · GitHub · ⭐ 19 · 2026-09-18</sub><br>General-purpose agent loop where Jev chooses tools and their arguments while Jot executes them, feeds real results back into context and asks again until Jev can reply, with every tool call visible.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/MiaoWuNYA/rikkahub-sillytavern-android"><img src="https://opengraph.githubassets.com/1/MiaoWuNYA/rikkahub-sillytavern-android" alt="RikkaHub Plus Jev decisions" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/MiaoWuNYA/rikkahub-sillytavern-android">RikkaHub Plus Jev decisions</a></b><br><sub>MiaoWuNYA · GitHub · ⭐ 19 · 2026-09-20</sub><br>Android AI chat client and SillyTavern-compatible app that uses Jev to judge each memory's relevance to the conversation instead of embedding search, and gives the main model a Jev judge tool for yes/no, choice and score questions.<br><sub><b>How it uses Jev:</b> Memories are judged in parallel batches and injected above 0.5 relevance; all Jev paths fall back silently when unavailable.</sub></td>
</tr>
<tr>
<td width="260" valign="top"></td>
<td valign="top"><b><a href="https://www.reddit.com/r/AI_Agents/comments/1wl82fr/tried_typesafe_ais_jev_vs_a_regular_llm_for_model/">Jev vs LLM model router</a></b><br><sub>TigerOk4538 · Reddit · ▲ 6 · 2026-09-20</sub><br>Smart model router that runs Jev and a structured-output LLM side by side on every message; Jev returns the routing decision in about 1 second vs 4-14 seconds for the LLM.<br><sub><b>How it uses Jev:</b> All routing signals evaluated in a single call.</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/blakestone-x/jev-mcp"><img src="https://opengraph.githubassets.com/1/blakestone-x/jev-mcp" alt="jev-mcp" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/blakestone-x/jev-mcp">jev-mcp</a></b><br><sub>blakestone-x · GitHub · ⭐ 18 · 2026-09-16</sub><br>Python MCP server that gives Claude Code, Codex, Cursor or any MCP client typed Jev classify, score, check, match and screen tools, each answer returned with a confidence.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Das-rebel/a3m-router"><img src="https://opengraph.githubassets.com/1/Das-rebel/a3m-router" alt="A3M Router" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Das-rebel/a3m-router">A3M Router</a></b><br><sub>Das-rebel · GitHub · ⭐ 16 · 2026-05-15</sub><br>Adaptive multi-model LLM router across 80+ providers with pheromone-trail failover and ensemble merging, where model=jev-auto lets Jev route each request to a suitable provider in a single pass.<br><sub>Also: <a href="https://www.npmjs.com/package/adaptive-memory-multi-model-router">npm</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/phantomyard/phantombot"><img src="https://opengraph.githubassets.com/1/phantomyard/phantombot" alt="Phantombot" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/phantomyard/phantombot">Phantombot</a></b><br><sub>phantomyard · GitHub · ⭐ 16 · 2026-05-01</sub><br>Persistent-identity AI assistant around terminal harnesses with long-term memory across PhantomChat, Telegram and editors; an optional Jev screener acts as a threat judge and routes each turn to the primary or coder model in ~300 ms.<br><sub><b>How it uses Jev:</b> A typed primary|coder Choice replaces keyword scoring for brain-swap routing; errors fall back to the scorer and are reported by phantombot doctor.</sub><br><sub>Also: <a href="https://phantombot.bot/">app</a> · <a href="https://github.com/phantomyard/phantombot/blob/main/docs/jev.md">docs</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/chopratejas/invalidate"><img src="https://raw.githubusercontent.com/chopratejas/invalidate/main/docs/img/chat.png" alt="invalidate" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/chopratejas/invalidate">invalidate</a></b><br><sub>chopratejas · GitHub · ⭐ 15 · 2026-09-19</sub><br>Invalidation layer for agent memory that checks every stored fact against each new event with a Jev yes/no question (about 150 ms and $0.00006 per check), marking superseded memories and queuing unsure ones for a human.<br><sub>Also: <a href="https://www.reddit.com/r/AIMemory/comments/1wkqj4i/making_memory_unremember_an_apache_20_oss_project/">discussion</a> · <a href="https://invalidate-playground.vercel.app">app</a> · <a href="https://invalidate-playground.vercel.app">app 2</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/NiazMorshed2007/jcr"><img src="https://raw.githubusercontent.com/NiazMorshed2007/jcr/main/web/src/app/opengraph-image.png" alt="JCR (Jev Capability Resolver)" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/NiazMorshed2007/jcr">JCR (Jev Capability Resolver)</a></b><br><sub>NiazMorshed2007 · GitHub · ⭐ 15 · 2026-09-20</sub><br>Resolver that gives an agent one tool to find documented deterministic commands for a task, using Jev to search a nested capability tree and return only the selected operations' context.<br><sub>Also: <a href="https://jcr.niazmorshed.dev">site</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Brainwires/jevwire"><img src="https://opengraph.githubassets.com/1/Brainwires/jevwire" alt="jevwire" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Brainwires/jevwire">jevwire</a></b><br><sub>Brainwires · GitHub · ⭐ 15 · 2026-09-17</sub><br>Jev decision layer for agent harnesses: an MCP server with seven tools (rank, pick, verify, evaluate, gate action, next step, list models), an embeddable DecisionModel library and an escalate-only Claude Code plugin.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/ling-kong-ran/pisper/blob/release/runtime/services/decision-service.mjs"><img src="https://raw.githubusercontent.com/ling-kong-ran/pisper/release/docs/brand/banner.svg" alt="Pisper decision service" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/ling-kong-ran/pisper/blob/release/runtime/services/decision-service.mjs">Pisper decision service</a></b><br><sub>ling-kong-ran · GitHub · ⭐ 298 repo · 2026-07-19</sub><br>Multi-agent desktop and mobile app that adds a Jev decision service for auto-approving tool permissions above a 0.9 threshold and verifying computer-use actions.<br><sub><b>How it uses Jev:</b> Calls TypeSafe /v1/systemone or OpenRouter decisions with Noul, Choice and Score questions; low-confidence cases fall back to manual approval.</sub><br><sub>Also: <a href="https://pisper.cc">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/SREGym/SREGym/tree/main/clients/jev"><img src="https://raw.githubusercontent.com/SREGym/SREGym/main/assets/overview.png" alt="SREGym Jev decision tool" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/SREGym/SREGym/tree/main/clients/jev">SREGym Jev decision tool</a></b><br><sub>SREGym · GitHub · ⭐ 290 repo · 2025-05-19</sub><br>Opt-in Codex MCP tools for an SRE agent benchmark where Jev picks the most informative read-only diagnostic test and reviews Kubernetes evidence before a diagnosis or fix is submitted.<br><sub><b>How it uses Jev:</b> Choice over proposed diagnostic tests (or "revise_tests"); Noul reviews for causal support, active failure and durable repair.</sub><br><sub>Also: <a href="https://sregym.com">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/mindroom-ai/mindroom/blob/main/src/mindroom/judgment/evaluator.py"><img src="https://repository-images.githubusercontent.com/1137843985/a7ad6a4c-9828-4e95-91b5-7d05e97c59fc" alt="MindRoom participation judgments" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/mindroom-ai/mindroom/blob/main/src/mindroom/judgment/evaluator.py">MindRoom participation judgments</a></b><br><sub>mindroom-ai · GitHub · ⭐ 284 repo · 2026-01-19</sub><br>Multi-agent runtime on Matrix where agents already in a thread decide whether to answer untagged messages, using an LLM or TypeSafe System One with a 0.8 threshold.<br><sub>Also: <a href="https://docs.mindroom.chat">docs</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/buberlo/dsh-jev"><img src="https://raw.githubusercontent.com/buberlo/dsh-jev/main/docs/assets/kubernetes-comparison.png" alt="dsh-jev" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/buberlo/dsh-jev">dsh-jev</a></b><br><sub>buberlo · GitHub · ⭐ 13 · 2026-09-19</sub><br>Decision layer for the DeepSeek Harness agent loop where Jev narrows the relevant tools before each step, gates risky tool calls, and picks a model route, and can never widen a permission.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/GodsBoy/jev-agent-skill-router"><img src="https://raw.githubusercontent.com/GodsBoy/jev-agent-skill-router/main/assets/jev-agent-skill-router-banner.png" alt="Jev Agent Skill Router" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/GodsBoy/jev-agent-skill-router">Jev Agent Skill Router</a></b><br><sub>GodsBoy · GitHub · ⭐ 13 · 2026-09-16</sub><br>Routing layer that picks which Hermes Agent skill to load using confidence-aware Jev decisions and declines weak matches; it routed 68 of 72 synthetic requests correctly versus 51 for a lexical baseline.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/jon-devlapaz/jev-me"><img src="https://opengraph.githubassets.com/1/jon-devlapaz/jev-me" alt="jev-me" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/jon-devlapaz/jev-me">jev-me</a></b><br><sub>jon-devlapaz · GitHub · ⭐ 13 · 2026-09-17</sub><br>Agent skill that grills a plan as a design-tree interview, printing every unlocked decision each round with a recommended answer, and calling Jev ad hoc when a typed judgment helps.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/krau/kmua-bot/blob/v2/kmua/plugins/agent/jev.py"><img src="https://repository-images.githubusercontent.com/573633729/31372b28-6155-40e6-ac96-6f7ed0b441ad" alt="kmua bot Jev follow-up check" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/krau/kmua-bot/blob/v2/kmua/plugins/agent/jev.py">kmua bot Jev follow-up check</a></b><br><sub>krau · GitHub · ⭐ 241 repo · 2022-12-03</sub><br>Telegram bot agent that experimentally uses Jev to decide whether a follow-up group message is relevant enough for the bot to keep replying, with a configurable threshold.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://www.reddit.com/r/LLMDevs/comments/1wihigc/tried_typesafes_new_decisiononly_model_jev_as_an/"><img src="https://preview.redd.it/h90l7rcdszph1.png?width=1080&amp;format=png&amp;auto=webp&amp;s=d1460cf34f1dcc1eb36f720f72be19077dcf6ba6" alt="Agent router test" width="240"></a></td>
<td valign="top"><b><a href="https://www.reddit.com/r/LLMDevs/comments/1wihigc/tried_typesafes_new_decisiononly_model_jev_as_an/">Agent router test</a></b><br><sub>blackbarata · Reddit · ▲ 4 · 2026-09-17</sub><br>Uses Jev as the router for a personal knowledge app's agents, correctly picking the recipe or scraper agent from an Instagram reel transcript in 145-271 ms.<br><sub><b>How it uses Jev:</b> One Choice over short agent descriptions, with confidence to decide when to fall back.</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/fornhere/hafiza-os"><img src="https://opengraph.githubassets.com/1/fornhere/hafiza-os" alt="Hafiza OS" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/fornhere/hafiza-os">Hafiza OS</a></b><br><sub>fornhere · GitHub · ⭐ 12 · 2026-08-30</sub><br>Turkish-language second-brain system that keeps agent memory in a local Markdown vault for Claude Code, Codex and Antigravity, with Jev as an optional retrieval and review advisor.<br><sub><b>How it uses Jev:</b> Scores knowledge cards and memory-catalog candidates against the question on a 0-2 scale (threshold 1.5), in off, shadow or on modes.</sub><br><sub>Also: <a href="https://github.com/fornhere/hafiza-os/blob/main/JEV.md">docs</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/keeltrace/hermes-jev"><img src="https://opengraph.githubassets.com/1/keeltrace/hermes-jev" alt="Hermes-Jev" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/keeltrace/hermes-jev">Hermes-Jev</a></b><br><sub>keeltrace · GitHub · ⭐ 12 · 2026-09-18</sub><br>Asynchronous decision layer for Hermes Agent that runs turn admission, relevance routing, completion and recovery checks, and an opt-in tool gate in parallel without blocking execution.<br><sub><b>How it uses Jev:</b> Bounded Choice/Noul questions evaluated in the background around Jev's ~500 ms latency; only high-confidence challenges interrupt Hermes.</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/anpicasso/hermes-jev-approvals"><img src="https://opengraph.githubassets.com/1/anpicasso/hermes-jev-approvals" alt="hermes-jev-approvals" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/anpicasso/hermes-jev-approvals">hermes-jev-approvals</a></b><br><sub>anpicasso · GitHub · ⭐ 12 · 2026-09-17</sub><br>Provider for Hermes Agent's smart command approvals in which Jev returns APPROVE, DENY or ESCALATE from six typed questions in one request, measured 8.7x faster with 4.4x fewer prompts on 153 real commands.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/tidepool-heavy-industries/tidepool"><img src="https://opengraph.githubassets.com/1/tidepool-heavy-industries/tidepool" alt="Tidepool" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/tidepool-heavy-industries/tidepool">Tidepool</a></b><br><sub>tidepool-heavy-industries · GitHub · ⭐ 12 · 2026-02-17</sub><br>Agent harness built on a live Haskell notebook where agents write procedures that mix commands, delegation and Jev judgments, then install them as tools or hooks; 322 questions returned in 351 ms.<br><sub><b>How it uses Jev:</b> Reasoning LLMs design the procedure while Jev answers batched typed questions inside compiled code, such as whether evidence is relevant or which follow-up fits.</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/DemonDamon/AgenticX/blob/main/agenticx/runtime/jev_intent.py"><img src="https://opengraph.githubassets.com/1/DemonDamon/AgenticX" alt="AgenticX Jev group routing" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/DemonDamon/AgenticX/blob/main/agenticx/runtime/jev_intent.py">AgenticX Jev group routing</a></b><br><sub>DemonDamon · GitHub · ⭐ 233 repo · 2024-03-15</sub><br>Multi-agent platform whose group chat routes un-mentioned messages with Jev, dispatching by label when confident and falling back to an LLM, and shows a decision card each turn.<br><sub>Also: <a href="https://www.agxbuilder.com/">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/mishrasanjeev/agentic-org"><img src="https://opengraph.githubassets.com/1/mishrasanjeev/agentic-org" alt="AgenticOrg Jev integration" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/mishrasanjeev/agentic-org">AgenticOrg Jev integration</a></b><br><sub>mishrasanjeev · GitHub · ⭐ 11 · 2026-03-20</sub><br>Enterprise agent orchestration platform with a Jev provider adapter, an offline evaluator and a shadow-mode hook that compares Jev tool-routing decisions with existing runtime outcomes.<br><sub><b>How it uses Jev:</b> Advisory only, with an 0.8 s timeout, sampling caps and a circuit breaker; production stays off until a measured evaluation is approved.</sub><br><sub>Also: <a href="https://github.com/mishrasanjeev/agentic-org/blob/main/docs/jev-agenticorg-integration.md">docs</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/hellozenstrategist-lab/eutrya"><img src="https://raw.githubusercontent.com/hellozenstrategist-lab/eutrya/main/assets/eutrya-banner.webp" alt="Eutrya" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/hellozenstrategist-lab/eutrya">Eutrya</a></b><br><sub>hellozenstrategist-lab · GitHub · ⭐ 11 · 2026-06-04</sub><br>Standalone CLI-first agent harness for authorized security research, multi-agent swarms and long-running workflows, with Jev built into its decision loop for attention, candidate rubrics and research micro-steps.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/zjunlp/JevLoop"><img src="https://opengraph.githubassets.com/1/zjunlp/JevLoop" alt="JevLoop" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/zjunlp/JevLoop">JevLoop</a></b><br><sub>zjunlp · GitHub · ⭐ 11 · 2026-09-20</sub><br>Runnable agent harness that routes every fork in the loop, such as which tool, is it safe, am I done, to a decision model like Jev or Laya and keeps the LLM for writing, with a web UI and no dependencies.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/DECRUX9812/typesafe-skill-router"><img src="https://opengraph.githubassets.com/1/DECRUX9812/typesafe-skill-router" alt="typesafe-skill-router" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/DECRUX9812/typesafe-skill-router">typesafe-skill-router</a></b><br><sub>DECRUX9812 · GitHub · ⭐ 11 · 2026-09-16</sub><br>Opt-in Hermes Agent plugin that asks Jev which one installed skill fits a request before the model call and appends a single hint line, about $0.001 per routed turn, injecting nothing when none fits.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/damianvtran/local-operator/tree/main/local_operator/classification"><img src="https://repository-images.githubusercontent.com/922327641/359101c9-d089-4d2c-bb22-a62f973989de" alt="Local Operator classification layer" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/damianvtran/local-operator/tree/main/local_operator/classification">Local Operator classification layer</a></b><br><sub>damianvtran · GitHub · ⭐ 214 repo · 2025-01-25</sub><br>Agent hub that runs a decision-model layer beside its heuristics once per message to recommend skills, MCP servers and roles; Jev scored 31/31 on labelled cases with the rubric in the options.<br><sub><b>How it uses Jev:</b> Cascade over Radient, TypeSafe and OpenRouter with byte-identical bodies; p50 0.20 s per call in the evaluation.</sub><br><sub>Also: <a href="https://github.com/damianvtran/local-operator/blob/main/docs/design/classification-layer.md">docs</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/jmagly/aiwg/blob/main/src/decision/adapters/jev.ts"><img src="https://raw.githubusercontent.com/jmagly/aiwg/main/docs/.public/aiwg-readme-hero-v2.png" alt="AIWG Jev decision adapter" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/jmagly/aiwg/blob/main/src/decision/adapters/jev.ts">AIWG Jev decision adapter</a></b><br><sub>jmagly · GitHub · ⭐ 211 repo · 2025-08-14</sub><br>Decision framework in an AI-augmented dev toolkit where versioned rulesets and bindings let workflows switch between Jev and an LLM subagent, with a hardened Jev transport.<br><sub>Also: <a href="https://github.com/jmagly/aiwg/blob/main/docs/decision/jev-transport.md">docs</a> · <a href="https://aiwg.io">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/RelayPlane/proxy/blob/main/src/classifier/jev_client.ts"><img src="https://raw.githubusercontent.com/RelayPlane/proxy/main/docs/dashboard.png" alt="RelayPlane Jev classifier" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/RelayPlane/proxy/blob/main/src/classifier/jev_client.ts">RelayPlane Jev classifier</a></b><br><sub>RelayPlane · GitHub · ⭐ 203 repo · 2026-02-03</sub><br>Local LLM cost proxy with an optional Jev complexity classifier that rates each request to inform model routing, enabled by one env var and capped at a 500 ms timeout.<br><sub>Also: <a href="https://relayplane.com">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Arrmlet/dehydrator"><img src="https://opengraph.githubassets.com/1/Arrmlet/dehydrator" alt="Dehydrator" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Arrmlet/dehydrator">Dehydrator</a></b><br><sub>Arrmlet · GitHub · ⭐ 10 · 2026-02-17</sub><br>Client-side tool search for LLM APIs that lets a model use thousands of tools without sending every definition, matching tools with BM25, Jev, or both.<br><sub><b>How it uses Jev:</b> Jev ranks tool definitions against the tool_search query by meaning; it needs no extra dependency beyond the standard library.</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/evoke-build/evoke"><img src="https://opengraph.githubassets.com/1/evoke-build/evoke" alt="evoke" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/evoke-build/evoke">evoke</a></b><br><sub>evoke-build · GitHub · ⭐ 10 · 2026-09-21</sub><br>Rust CLI, git-based package manager and TypeScript SDK where a spoken or typed sentence becomes a call to an installed reflex program chosen by Jev with bounded arguments, gated to run, confirm, ask or abstain.<br><sub>Also: <a href="https://evoke.build">site</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/markus-global/markus/blob/main/packages/core/src/tools/multimodal.ts"><img src="https://raw.githubusercontent.com/markus-global/markus/main/docs/images/dashboard-preview.gif" alt="Markus decide tool" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/markus-global/markus/blob/main/packages/core/src/tools/multimodal.ts">Markus decide tool</a></b><br><sub>markus-global · GitHub · ⭐ 195 repo · 2026-03-19</sub><br>AI workforce platform that gives its agents a decision capability and a decide tool backed by Jev-style decision models, with a rule that all evidence must go into the state.<br><sub>Also: <a href="https://www.markus.global">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/libingzheren/Jev-Mem"><img src="https://raw.githubusercontent.com/libingzheren/Jev-Mem/main/docs/figures/overall_structure.png" alt="Jev-Mem" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/libingzheren/Jev-Mem">Jev-Mem</a></b><br><sub>libingzheren · GitHub · ⭐ 9 · 2026-09-20</sub><br>Agent memory where Jev, as a System One controller, handles admission, multi-relational linking and retrieval while a language model answers; on LoCoMo with GPT-4o-mini the paper reports 11.0% higher answer quality.<br><sub>Also: <a href="https://huggingface.co/spaces/libingzheren/Jev-Mem">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/kushals256/jevcache"><img src="https://raw.githubusercontent.com/kushals256/jevcache/main/docs/demo.gif" alt="jevcache (semantic cache)" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/kushals256/jevcache">jevcache (semantic cache)</a></b><br><sub>kushals256 · GitHub · ⭐ 9 · 2026-09-19</sub><br>Local OpenAI-compatible proxy that reuses a cached chat completion when Jev judges a new request to have the same intent as an earlier one, and fails open on Jev errors; one test went from 3244ms to 394ms.<br><sub>Also: <a href="https://www.reddit.com/r/LLM/comments/1wm3ijr/your_agent_asks_the_same_thing_twice_in_different/">demo</a> · <a href="https://www.npmjs.com/package/@kushalicious/jevcache">npm</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/ItIsCuthNotCup/MetaCog"><img src="https://opengraph.githubassets.com/1/ItIsCuthNotCup/MetaCog" alt="MetaCog" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/ItIsCuthNotCup/MetaCog">MetaCog</a></b><br><sub>ItIsCuthNotCup · GitHub · ⭐ 9 · 2026-09-20</sub><br>Metacognition loop where a small model branches into several thought paths and a System One judge, Jev or the open Reflex 4B, picks which one to continue; per-candidate Jev Nouls lifted HumanEval from 0.555 to 0.756.<br><sub><b>How it uses Jev:</b> Per-candidate Noul judging beat one-shot Choice (0.756 vs 0.726 on HumanEval, 0.905 vs 0.869 on GSM8K).</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/miikkij/aimeat-protocol"><img src="https://raw.githubusercontent.com/miikkij/aimeat-protocol/main/assets/screenshots/portal-landing.png" alt="AIMEAT decide" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/miikkij/aimeat-protocol">AIMEAT decide</a></b><br><sub>miikkij · GitHub · ⭐ 8 · 2026-04-28</sub><br>Federated, self-hosted AI operating system whose nodes carry Jev beside the text model, so apps and agents can ask closed triage, routing, scoring and pick-one questions via a JS library, MCP tools and a skill.<br><sub><b>How it uses Jev:</b> Personal data such as emails, phone numbers and Finnish identity codes are stripped before requests leave the node, and each decision is recorded with whether a person reviewed it.</sub><br><sub>Also: <a href="https://aimeat.io">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/NicolasMontone/jev-memory"><img src="https://opengraph.githubassets.com/1/NicolasMontone/jev-memory" alt="jev-memory" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/NicolasMontone/jev-memory">jev-memory</a></b><br><sub>NicolasMontone · GitHub · ⭐ 8 · 2026-09-18</sub><br>Long-term memory layer for the Vercel AI SDK where Jev gates what gets written, retrieved and evicted, storing exact strings so memories are never summarized or rewritten.<br><sub><b>How it uses Jev:</b> Write, retrieve and evict gates are each a boolean, choice or score question to typesafe-ai/jev via the AI Gateway.</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/rajdhakad9826/jev-router"><img src="https://external-preview.redd.it/MYwHHpL0--RYjVWYB4u6LIjIKjKERfy3Z1jmJkPiIyE.png?auto=webp&amp;s=71e8215cba4f41d7887ad24f3c98c27af60055a2" alt="jev-model-router" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/rajdhakad9826/jev-router">jev-model-router</a></b><br><sub>rajdhakad9826 · GitHub · ⭐ 8 · 2026-09-19</sub><br>TypeScript router that sends each query to the cheapest capable model in a two-tier or three-tier cascade, using Jev to classify how demanding the query is instead of an LLM call.<br><sub>Also: <a href="https://www.reddit.com/r/typesafe/comments/1wkrfos/github_rajdhakad9826jevrouter_costaware_llm/">demo</a> · <a href="https://www.reddit.com/r/typesafe/comments/1wkri7o/build_a_llm_router_using_jev/">discussion</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/PerryLink/jevcore"><img src="https://opengraph.githubassets.com/1/PerryLink/jevcore" alt="jevcore" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/PerryLink/jevcore">jevcore</a></b><br><sub>PerryLink · GitHub · ⭐ 8 · 2026-09-20</sub><br>Decision layer that exposes Jev's noul, choice, and score questions to DeepSeek Harness, any MCP host, or plain Node through three packages, offline by default with network egress disclosed.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/zeeshan8281/slo-router"><img src="https://opengraph.githubassets.com/1/zeeshan8281/slo-router" alt="SLO Router" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/zeeshan8281/slo-router">SLO Router</a></b><br><sub>zeeshan8281 · GitHub · ⭐ 8 · 2026-09-19</sub><br>OpenAI-compatible proxy that routes each request to the cheapest backend meeting its latency SLO, with optional Jev 1.13 semantic features; a live run found Jev changed no routes and raised p95 from 77.93 ms to 490.38 ms.<br><sub><b>How it uses Jev:</b> Typed semantic features via the OpenRouter Decisions API, falling back to local features on missing key, timeout or invalid response.</sub><br><sub>Also: <a href="https://github.com/zeeshan8281/slo-router/blob/main/results/live-jev-analysis.md">results</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"></td>
<td valign="top"><b><a href="https://www.npmjs.com/package/@maximem/jev-mcp">@maximem/jev-mcp</a></b><br><sub>maximem-ai · Package · ⬇ 754 · 2026-09-20</sub><br>MCP server giving Claude Code, Codex and Cowork Jev-backed classify, score, check and rank tools, plus plan, action and verify gates over the agent's own work.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/arunav25/jev-mcp"><img src="https://opengraph.githubassets.com/1/arunav25/jev-mcp" alt="JEV MCP" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/arunav25/jev-mcp">JEV MCP</a></b><br><sub>arunav25 · GitHub · ⭐ 7 · 2026-09-17</sub><br>MCP server exposing Jev as a single evaluate tool for Claude Code, Claude Desktop and Codex, plus an evaluation harness that measures its accuracy against general-purpose LLMs on shared datasets.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/prismhq/jev-router"><img src="https://opengraph.githubassets.com/1/prismhq/jev-router" alt="jev-router" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/prismhq/jev-router">jev-router</a></b><br><sub>prismhq · GitHub · ⭐ 7 · 2026-09-17</sub><br>OpenAI-compatible LiteLLM proxy where clients request one model id and Jev picks which provider model serves each request, after filters for vision, output length and tool support.<br><sub><b>How it uses Jev:</b> A Choice over the eligible models in router.yaml, built from a minimized summary of the request; without a key a cheapest-eligible baseline runs.</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/riteshverma/s18"><img src="https://opengraph.githubassets.com/1/riteshverma/s18" alt="s18" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/riteshverma/s18">s18</a></b><br><sub>riteshverma · GitHub · ⭐ 7 · 2026-02-10</sub><br>Open-source agent runtime and orchestration API where query routing, skill matching and planner fast paths can use Jev decisions, falling back to built-in regex guards when Jev is unkeyed, unreachable or unsure.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/cahaseler/determinate"><img src="https://opengraph.githubassets.com/1/cahaseler/determinate" alt="determinate" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/cahaseler/determinate">determinate</a></b><br><sub>cahaseler · GitHub · ⭐ 6 · 2026-03-11</sub><br>TypeScript agent library that treats LLMs as next-action predictors; its Jev decider picks the next valid tool and fills closed-set parameters, handing only free-text fields or low-confidence cases to the LLM.<br><sub><b>How it uses Jev:</b> One request per nextAction() asks which tool comes next plus each enum-like param; below minConfidence (0.6) the LLM decides. Works via TypeSafe or OpenRouter Decisions.</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/iii-hq/workers/blob/main/iii-directory/src/functions/search_jev.rs"><img src="https://opengraph.githubassets.com/1/iii-hq/workers" alt="iii-directory Jev search" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/iii-hq/workers/blob/main/iii-directory/src/functions/search_jev.rs">iii-directory Jev search</a></b><br><sub>iii-hq · GitHub · ⭐ 109 repo · 2026-03-18</sub><br>Worker for the iii engine that searches registered functions, installed skills and triggers with Jev relevance judgments, falling back to hybrid search.<br><sub>Also: <a href="https://workers.iii.dev/">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/JulesLiu390/PetGPT/blob/main/src/utils/social/jevClient.js"><img src="https://repository-images.githubusercontent.com/952838031/91883b7f-7f2b-412f-a048-8eae41b0de5a" alt="PetGPT Jev social signals" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/JulesLiu390/PetGPT/blob/main/src/utils/social/jevClient.js">PetGPT Jev social signals</a></b><br><sub>JulesLiu390 · GitHub · ⭐ 107 repo · 2025-03-22</sub><br>AI desktop pet with a social agent in QQ, Telegram and WhatsApp groups that uses Jev to tag message mood and read the group's atmosphere before replying.<br><sub>Also: <a href="https://github.com/JulesLiu390/PetGPT/tree/main/jev-test">sandbox</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/hjxwz123/Aivory/tree/main/server/internal/typesafe"><img src="https://raw.githubusercontent.com/hjxwz123/Aivory/main/docs/brand/readme-header.svg" alt="Aivory decision policies" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/hjxwz123/Aivory/tree/main/server/internal/typesafe">Aivory decision policies</a></b><br><sub>hjxwz123 · GitHub · ⭐ 101 repo · 2026-06-12</sub><br>Self-hosted AI chat platform that lets admins assign Jev to file routing, tool routing, memory dedup, memory conflict adjudication and content moderation, each with confidence fallbacks.<br><sub><b>How it uses Jev:</b> Moderation asks one Noul per category and blocks at 0.85; tool routing narrows tools only at 0.8 confidence.</sub><br><sub>Also: <a href="https://github.com/hjxwz123/Aivory/blob/main/docs/typesafe-decisions.md">docs</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/xudafeng/agent0"><img src="https://raw.githubusercontent.com/xudafeng/agent0/main/docs/images/agent0-jev-demo.gif" alt="agent0" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/xudafeng/agent0">agent0</a></b><br><sub>xudafeng · GitHub · ⭐ 5 · 2026-09-18</sub><br>Desktop AI agent runtime with MCP integration, task planning and persistent memory where optional Jev routing selects the relevant tools, falling back to the main model on low confidence, with each decision shown in an Activity panel.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/lhemerly/mcts-agent"><img src="https://opengraph.githubassets.com/1/lhemerly/mcts-agent" alt="Discriminative MCTS Agent" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/lhemerly/mcts-agent">Discriminative MCTS Agent</a></b><br><sub>lhemerly · GitHub · ⭐ 5 · 2026-09-16</sub><br>Autonomous agent that runs Monte Carlo Tree Search over actions proposed by harnesses like AGY or Pi, with a D3.js visualizer for replaying rollouts and value backpropagation.<br><sub><b>How it uses Jev:</b> Choice assigns action priors and dynamic branching, Score evaluates hypothetical states, Noul handles yes/no checks.</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/cyberofficial/dsh-plugin-jev"><img src="https://opengraph.githubassets.com/1/cyberofficial/dsh-plugin-jev" alt="dsh-plugin-jev" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/cyberofficial/dsh-plugin-jev">dsh-plugin-jev</a></b><br><sub>cyberofficial · GitHub · ⭐ 5 · 2026-09-19</sub><br>Plugin for the DeepSeek Harness web GUI that gives the main agent and subagents a jev_ask tool for calibrated judgments under uncertainty, with per-chat usage tracking and a settings tab for the key and model.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/doronp/jevc"><img src="https://raw.githubusercontent.com/doronp/jevc/main/docs/hero.svg" alt="jevc" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/doronp/jevc">jevc</a></b><br><sub>doronp · GitHub · ⭐ 5 · 2026-09-18</sub><br>Compiler that turns natural-language agent rules and JSON Schemas into Jev programs: a few narrow typed evidence questions plus a code reducer that computes the verdict, so a rule like never commit unless asked becomes testable.<br><sub>Also: <a href="https://news.ycombinator.com/item?id=49777057">demo</a> · <a href="https://www.npmjs.com/package/jev-compiler">npm</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/rShetty/miser"><img src="https://opengraph.githubassets.com/1/rShetty/miser" alt="Miser" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/rShetty/miser">Miser</a></b><br><sub>rShetty · GitHub · ⭐ 5 · 2026-08-09</sub><br>Rust AI gateway that has Jev classify every OpenAI-compatible prompt into a complexity tier from trivial to reasoning and routes it to the cheapest capable OpenRouter model; 90.5% exact accuracy on 116 held-out cases.<br><sub><b>How it uses Jev:</b> Tier plus task classification in about 340 ms; sessions never downgrade tiers, with heuristic fallback.</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/hemanth/tool-prune"><img src="https://opengraph.githubassets.com/1/hemanth/tool-prune" alt="tool-prune" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/hemanth/tool-prune">tool-prune</a></b><br><sub>hemanth · GitHub · ⭐ 5 · 2026-09-17</sub><br>Zero-dependency tool selection and schema pruning for agents that cuts MCP tool schemas to the relevant few before an LLM call, running offline via TurboQuant or on Jev.<br><sub><b>How it uses Jev:</b> Jev engine reported 100.0% distractor Top-1 on BFCL v3 at 189 ms; confident picks can dispatch directly without the LLM.</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/supernovae-st/nika/blob/main/crates/nika-cli-host/src/compile/typesafe.rs"><img src="https://nika.sh/brand/nika-logo-light.svg" alt="Nika System One seat" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/supernovae-st/nika/blob/main/crates/nika-cli-host/src/compile/typesafe.rs">Nika System One seat</a></b><br><sub>supernovae-st · GitHub · ⭐ 88 repo · 2026-01-02</sub><br>Workflow language for repeatable AI work whose compiler can hand bounded decisions to TypeSafe System One, one Choice with a "none" option per question.<br><sub>Also: <a href="https://nika.sh">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/haseeb-heaven/jev-system-one"><img src="https://raw.githubusercontent.com/haseeb-heaven/jev-system-one/develop/docs/tui-preview.png" alt="jev-system-one" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/haseeb-heaven/jev-system-one">jev-system-one</a></b><br><sub>haseeb-heaven · GitHub · ⭐ 4 · 2026-09-17</sub><br>Terminal Q&amp;A app where Jev sets the response policy and reviews drafts inside a LangGraph workflow while OpenAI only writes the wording, with a decision report beside each answer.<br><sub><b>How it uses Jev:</b> Jev judges response mode, depth, uncertainty and draft quality at two points per request.</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/NicolasMontone/jev-tool-permissions"><img src="https://opengraph.githubassets.com/1/NicolasMontone/jev-tool-permissions" alt="jev-tool-permissions" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/NicolasMontone/jev-tool-permissions">jev-tool-permissions</a></b><br><sub>NicolasMontone · GitHub · ⭐ 4 · 2026-09-18</sub><br>Tool-permission layer for the Vercel AI SDK that uses Jev to auto-approve, ask a human or block each tool call and to prune irrelevant tool definitions before a turn.<br><sub><b>How it uses Jev:</b> Runs after deterministic allow/deny rules; on errors the gate fails closed to ask-human.</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/jon-devlapaz/tink-route"><img src="https://opengraph.githubassets.com/1/jon-devlapaz/tink-route" alt="tink-route" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/jon-devlapaz/tink-route">tink-route</a></b><br><sub>jon-devlapaz · GitHub · ⭐ 4 · 2026-09-21</sub><br>Agent Skills router that keeps skill libraries offline and loads only the needed ones on demand through a two-stage Jev gate (a Noul on whether a skill is needed, then a Choice of which), avoiding per-turn prompt bloat.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/tonone-ai/tonone/tree/main/lib/jev"><img src="https://opengraph.githubassets.com/1/tonone-ai/tonone" alt="Tonone Jev decision layer" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/tonone-ai/tonone/tree/main/lib/jev">Tonone Jev decision layer</a></b><br><sub>tonone-ai · GitHub · ⭐ 73 repo · 2026-03-16</sub><br>Shared decision layer for a 426-skill AI company toolkit that answers yes/no, one-of-N and rubric questions with Jev, or a local TF-IDF scorer when no key is set, and gates skill manifests.<br><sub>Also: <a href="https://second.tonone.ai">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/virtual-context/virtual-context/tree/main/benchmarks/jev"><img src="https://raw.githubusercontent.com/virtual-context/virtual-context/main/assets/dashboard.png" alt="virtual-context Jev judgment seams" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/virtual-context/virtual-context/tree/main/benchmarks/jev">virtual-context Jev judgment seams</a></b><br><sub>virtual-context · GitHub · ⭐ 65 repo · 2026-02-13</sub><br>Virtual context memory layer for LLM agents that adds per-seam Jev judgment modes for reranking, intent and temporal checks; on 140 LongMemEval questions Jev cut the mean first-gold rank from 2.33 to 1.14.<br><sub>Also: <a href="https://github.com/virtual-context/virtual-context">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/rsdkrasen/hermes-jev-router"><img src="https://opengraph.githubassets.com/1/rsdkrasen/hermes-jev-router" alt="hermes-jev-router" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/rsdkrasen/hermes-jev-router">hermes-jev-router</a></b><br><sub>rsdkrasen · GitHub · ⭐ 3 · 2026-09-19</sub><br>Plugin for Hermes Agent that adds a Jev decision layer to compact tool results, suppress duplicate tool calls, and skip main-model calls that would only restate results.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/ajensenwaud/hermes-jev-plugin"><img src="https://opengraph.githubassets.com/1/ajensenwaud/hermes-jev-plugin" alt="Jev plugin for Hermes Agent" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/ajensenwaud/hermes-jev-plugin">Jev plugin for Hermes Agent</a></b><br><sub>ajensenwaud · GitHub · ⭐ 3 · 2026-09-19</sub><br>Hermes Agent plugin exposing Jev as four tools, jev_check, jev_route, jev_score, and jev_evaluate, with a bundled skill on writing good questions for coding-agent workflows.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/abhishekashokvkumar/jev-mcp-dispatcher"><img src="https://opengraph.githubassets.com/1/abhishekashokvkumar/jev-mcp-dispatcher" alt="jev-mcp-dispatcher" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/abhishekashokvkumar/jev-mcp-dispatcher">jev-mcp-dispatcher</a></b><br><sub>abhishekashokvkumar · GitHub · ⭐ 3 · 2026-09-18</sub><br>Proof-of-concept MCP tool dispatcher that discovers a simple MCP server's tool signatures at runtime and routes a natural-language command to the right tool and arguments with no general-purpose LLM.<br><sub><b>How it uses Jev:</b> Choice picks the tool and extracts each argument value from the sentence; Noul handles yes/no checks.</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/DanielKillenberger/jev-predict-skill"><img src="https://opengraph.githubassets.com/1/DanielKillenberger/jev-predict-skill" alt="jev-predict-skill" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/DanielKillenberger/jev-predict-skill">jev-predict-skill</a></b><br><sub>DanielKillenberger · GitHub · ⭐ 3 · 2026-09-16</sub><br>Host agent skill that predicts which closed verdict another skill would reach, such as SHIP or NEEDS_WORK, by handing its outcome set to Jev instead of running the skill.<br><sub><b>How it uses Jev:</b> A Noul first checks whether a closed decision is possible, then a Choice picks among the target skill's outcomes.</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/jvsteiner/jevex"><img src="https://opengraph.githubassets.com/1/jvsteiner/jevex" alt="Jevex" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/jvsteiner/jevex">Jevex</a></b><br><sub>jvsteiner · GitHub · ⭐ 3 · 2026-09-17</sub><br>Agent loop experiment where Jev picks each next action and approves the concrete call, a LangChain chat model fills arguments and the final reply, and three local MCP servers expose 12 tools.<br><sub><b>How it uses Jev:</b> Includes a research benchmark against native tool-calling LLM loops with measured tokens and latency.</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/iamvatsalpatel/tiershift"><img src="https://raw.githubusercontent.com/iamvatsalpatel/tiershift/main/bench/chart-light.svg" alt="tiershift" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/iamvatsalpatel/tiershift">tiershift</a></b><br><sub>iamvatsalpatel · GitHub · ⭐ 3 · 2026-09-17</sub><br>Model router for TypeScript and Python that sends each LLM request to the cheapest capable tier and escalates on multi-step reasoning, difficulty, stakes, or safety, with policy in plain YAML.<br><sub><b>How it uses Jev:</b> Routing judgments in about 180 ms at four cents per thousand routes; every decision prints its reason.</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/finchtoys/finch-releases/tree/main/extensions/jev"><img src="https://raw.githubusercontent.com/finchtoys/finch-releases/main/home.webp" alt="finch-jev" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/finchtoys/finch-releases/tree/main/extensions/jev">finch-jev</a></b><br><sub>finchtoys · GitHub · ⭐ 57 repo · 2026-07-02</sub><br>Mini tool for the Finch desktop agent that registers a finch_jev_evaluate tool, letting the agent send text plus Choice, Score and Noul questions to Jev.<br><sub>Also: <a href="https://www.finchwork.app">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/shiro-0x/hersona/blob/main/hersona/integrations/decision/typesafe.py"><img src="https://raw.githubusercontent.com/shiro-0x/hersona/main/docs/hersona-demo.gif" alt="Hersona decide" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/shiro-0x/hersona/blob/main/hersona/integrations/decision/typesafe.py">Hersona decide</a></b><br><sub>shiro-0x · GitHub · ⭐ 52 repo · 2026-06-04</sub><br>Persona attribute library for AI agents whose hersona decide command uses TypeSafe Jev to recommend reply, ask, search, use a tool or hold, with confidence, persona alignment and risk.<br><sub>Also: <a href="https://shiro-0x.github.io/hersona/">docs</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/adityavardhansharma/EchoFlow/tree/main/app/src/main/java/com/echoflow/data/jev"><img src="https://raw.githubusercontent.com/adityavardhansharma/EchoFlow/main/logo1.png" alt="EchoFlow Jev router" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/adityavardhansharma/EchoFlow/tree/main/app/src/main/java/com/echoflow/data/jev">EchoFlow Jev router</a></b><br><sub>adityavardhansharma · GitHub · ⭐ 48 repo · 2026-05-29</sub><br>Per-turn Jev router in the EchoFlow privacy-first Android AI chat app that decides whether to recall or skip memory, force web search, or save a memory before the answering model runs, for cloud chats only.<br><sub><b>How it uses Jev:</b> One Jev call per turn with fixed act thresholds and a timeout; uncertainty defers to the answering model and failures fall back to legacy behavior.</sub><br><sub>Also: <a href="https://echoflow.adityavs.tech/">app</a> · <a href="https://github.com/adityavardhansharma/EchoFlow">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/dzhng/duet-agent/tree/main/src/model-routing"><img src="https://raw.githubusercontent.com/dzhng/duet-agent/main/assets/cover.png" alt="duet-agent Jev model routing" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/dzhng/duet-agent/tree/main/src/model-routing">duet-agent Jev model routing</a></b><br><sub>dzhng · GitHub · ⭐ 44 repo · 2026-04-10</sub><br>Model-routing layer in the duet-agent harness whose default classifier is Jev via AI Gateway, re-checking every 5 assistant steps which model tier should handle the work and switching when the task changes domain.<br><sub>Also: <a href="https://github.com/dzhng/duet-agent">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/maha0525/SAIVerse/blob/main/docs/intent/reflex_judgment.md"><img src="https://opengraph.githubassets.com/1/maha0525/SAIVerse" alt="SAIVerse reflex judgment" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/maha0525/SAIVerse/blob/main/docs/intent/reflex_judgment.md">SAIVerse reflex judgment</a></b><br><sub>maha0525 · GitHub · ⭐ 43 repo · 2025-06-07</sub><br>Reflex-judgment layer in the SAIVerse AI-persona world that returns probabilities instead of prose, first used to rerank auto-recalled memories. It can target TypeSafe Jev, OpenRouter, a self-hosted localjev or a structured-output LLM.<br><sub><b>How it uses Jev:</b> Typed noul/choice/score questions through a provider-agnostic jev_compat protocol with per-persona model overrides.</sub><br><sub>Also: <a href="https://github.com/maha0525/SAIVerse">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/tylerjharden/ailerix"><img src="https://opengraph.githubassets.com/1/tylerjharden/ailerix" alt="Ailerix" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/tylerjharden/ailerix">Ailerix</a></b><br><sub>tylerjharden · GitHub · ⭐ 2 · 2026-09-16</sub><br>OpenRouter-style model router with a single ailerix/auto slug: Jev classifies each request into a typed catalog route, then a cost-per-task Pareto chain picks the provider.<br><sub>Also: <a href="https://ailerix.vercel.app">app</a> · <a href="https://ailerix.vercel.app">app 2</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/anpicasso/hermes-jev-curator"><img src="https://opengraph.githubassets.com/1/anpicasso/hermes-jev-curator" alt="hermes-jev-curator" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/anpicasso/hermes-jev-curator">hermes-jev-curator</a></b><br><sub>anpicasso · GitHub · ⭐ 2 · 2026-09-21</sub><br>Hermes Agent plugin that has Jev label each pair of agent-created skills as duplicate, subset, conflict, unrelated and so on, and turns the results into safe archive plans.<br><sub><b>How it uses Jev:</b> An 8-way relation Choice per candidate skill pair; defaults to read-only observe mode.</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/FirasSX914/Janus"><img src="https://raw.githubusercontent.com/FirasSX914/Janus/main/results/figures/janus_demo.gif" alt="Janus" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/FirasSX914/Janus">Janus</a></b><br><sub>FirasSX914 · GitHub · ⭐ 2 · 2026-09-17</sub><br>Router that sends each decision to Jev or a larger fallback model based on confidence, after measuring the threshold on your labeled dataset or decision log instead of shipping a default.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/iJ03l/jear"><img src="https://opengraph.githubassets.com/1/iJ03l/jear" alt="jear" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/iJ03l/jear">jear</a></b><br><sub>iJ03l · GitHub · ⭐ 2 · 2026-09-18</sub><br>Rust client that routes requests across NEAR AI Cloud models and IronClaw agents by budget, quality and sensitivity, so users never pick a model or agent themselves.<br><sub><b>How it uses Jev:</b> Choice picks the agent, Score rates complexity and sensitivity, Noul flags whether a private TEE is needed or the request is risky or urgent.</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/bojansandhaus/jev-decisions"><img src="https://cdn-thumbnails.huggingface.co/social-thumbnails/spaces/bojansandhaus/jev-agent-decision-playground.png" alt="Jev Decisions" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/bojansandhaus/jev-decisions">Jev Decisions</a></b><br><sub>bojansandhaus · GitHub · ⭐ 2 · 2026-09-19</sub><br>Plugin for Hermes and other agents that adds tools to review risky plans, recommend human approval, check answers against sources, assess whether a task is really finished, and keep a local decision journal.<br><sub>Also: <a href="https://huggingface.co/spaces/bojansandhaus/jev-agent-decision-playground">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/freepik-company/jev-mcp"><img src="https://opengraph.githubassets.com/1/freepik-company/jev-mcp" alt="Jev MCP (Freepik)" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/freepik-company/jev-mcp">Jev MCP (Freepik)</a></b><br><sub>freepik-company · GitHub · ⭐ 2 · 2026-09-21</sub><br>Dependency-light Go MCP server with five tools for typed decisions (decide, classify, verify, rerank) via OpenRouter or TypeSafe, validating every provider answer and never retrying a paid call.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/hugo-alves/jev-router-playground"><img src="https://raw.githubusercontent.com/hugo-alves/jev-router-playground/main/assets/preview.png" alt="Jev Router Playground" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/hugo-alves/jev-router-playground">Jev Router Playground</a></b><br><sub>hugo-alves · GitHub · ⭐ 2 · 2026-09-18</sub><br>Playground where you build a pool of OpenRouter models with routing descriptions, give Jev a task, and compare its pick and probability distribution with the answer you judge best.<br><sub>Also: <a href="https://kvhx37ziab90c.space.minimax.io">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/typakon4/jev-layer"><img src="https://raw.githubusercontent.com/typakon4/jev-layer/main/docs/jev-layer-banner.svg" alt="jev-layer" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/typakon4/jev-layer">jev-layer</a></b><br><sub>typakon4 · GitHub · ⭐ 2 · 2026-09-19</sub><br>Portable decision layer for agent harnesses such as Hermes, OMP, Codex and generic MCP that routes bounded choices through Jev and records receipts for replay, while the host keeps execution, permissions and approvals.<br><sub>Also: <a href="https://www.npmjs.com/package/jev-layer">npm</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/rajasekharponakala/jev-mcp"><img src="https://external-preview.redd.it/PbioKRcq0xCJWCgwmAl45cEjLvDs5nxQCdmpvf2NylQ.png?auto=webp&amp;s=ac4ff6f727d3bab17dbc1f6dcdee59f0005949cd" alt="jev-mcp" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/rajasekharponakala/jev-mcp">jev-mcp</a></b><br><sub>rajasekharponakala · GitHub · ⭐ 2 · 2026-09-21</sub><br>MCP server that gives agents such as Claude Code and OpenCode typed Jev tools: jev_evaluate for a map of parallel questions, plus jev_noul, jev_choice, jev_score, and jev_models.<br><sub>Also: <a href="https://www.reddit.com/r/opencodeCLI/comments/1wm3mg7/jev_mcp_in_opencode/">demo</a> · <a href="https://www.reddit.com/r/OpenSourceeAI/comments/1wm3n4z/jev_mcp_in_opencode/">discussion</a></sub></td>
</tr>
</table>

<details><summary>96 more</summary>

- **[jev-model-router (OpenRouter)](https://github.com/lucianfialho/jev-model-router)** · <sub>lucianfialho · GitHub · ⭐ 2 · 2026-09-19</sub><br>Python router that classifies each request and picks the cheapest capable model from OpenRouter's live, full catalog on every decision instead of a hardcoded model list.
- **[todo-jev](https://github.com/maker-KK/todo-jev)** · <sub>maker-KK · GitHub · ⭐ 2 · 2026-09-18</sub><br>Task-routing experiment that classifies a request with Jev and recommends a local rule, a specialist skill or a foundation model, combining skill apply/exclude conditions with local environment checks.
- **[ToolGate](https://github.com/ndolinschi/toolgate)** · <sub>ndolinschi · GitHub · ⭐ 2 · 2026-09-17</sub><br>Gate for planned agent tool or MCP calls that returns allow, ask a human or deny, with a five-level risk score and checks for data exfiltration, irreversibility and policy violations.
- **[typesafe-jev-mcp](https://github.com/anasbekheit/typesafe-jev-mcp)** · <sub>anasbekheit · GitHub · ⭐ 2 · 2026-09-20</sub><br>Rust MCP server with one evaluate tool that lets Claude Code, Codex, OpenCode, Antigravity or Cursor send a state and typed questions to Jev and get noul, choice or score answers with probabilities.
- **[Hive Jev routing backend](https://github.com/DJLougen/hive/blob/main/hive/jev_backend.py)** · <sub>DJLougen · GitHub · ⭐ 39 repo · 2026-06-01</sub><br>Jev backend for Hive, a CPU-side action router for AI agents: Jev picks the next tool and rates whether it is safe to run without the LLM. A calibration probe found the default 0.95 safety gate never fires.
- **[Jev judgment modality for agent-rdf-memory](https://github.com/OpenLinkSoftware/ai-agent-skills/blob/main/agent-rdf-memory/howto/jev-judgment-modality.ttl)** · <sub>OpenLinkSoftware · GitHub · ⭐ 39 repo · 2025-12-19</sub><br>RDF HowTo in OpenLink's OPAL agent skills that adds an optional System One judgment mode (Jev, Laya or NanoJev) to its memory harness, gating HowTo candidates and ask-vs-act elicitation, run in shadow or active mode.
- **[Synkora TypeSafe tools](https://github.com/getsynkora/synkora-ai/blob/master/api/src/services/agents/internal_tools/typesafe_tools.py)** · <sub>getsynkora · GitHub · ⭐ 35 repo · 2026-09-18</sub><br>Built-in Jev evaluation tools for agents on the self-hosted Synkora platform: generic state-and-question calls, named profiles such as recruiting, a report formatter and a playground.
- **[ask-jev gate for Grok bots](https://x.com/ChuckHTF/status/2102187054381617367)** · <sub>ChuckHTF · X · ♥ 1 · 2026-09-22</sub><br>Personal desk of Grok bots and assistants that now asks Jev first, via OpenRouter's Decisions API, for small yes/no, bucket and 1-5 score calls instead of waking Grok.
- **[LifeOS Jev orchestrator experiments](https://github.com/nbramia/LifeOS/tree/main/scripts/jev_eval)** · <sub>nbramia · GitHub · ⭐ 31 repo · 2026-01-07</sub><br>Six offline experiments in the self-hosted LifeOS personal assistant testing, on recorded real turns, whether Jev typed judgments would help its chat orchestrator with routing, in-loop decisions and latency.
- **[Arbos Jev router](https://github.com/unarbos/arbos/blob/main/crates/arbos-engine/src/jev.rs)** · <sub>unarbos · GitHub · ⭐ 30 repo · 2026-03-18</sub><br>Structured router in the Arbos file-system-native agent coordinator where Jev picks the next mechanical tool move from a situation card, while the LLM handles writing, planning and talking; act=llm hands the turn to the chat model.
- **[Helm API Jev classifier](https://github.com/EasyMetaAu/helm-api/tree/main/packages/core/src/classifier)** · <sub>EasyMetaAu · GitHub · ⭐ 30 repo · 2026-05-29</sub><br>Request classifier in the Helm API self-hosted LLM routing gateway that sends Jev the last user message and gets task type and complexity choices, which pick the lane and provider for the request.
- **[Nebius Physical AI Jev model router](https://github.com/nebius/nebius-physical-ai/blob/main/npa/src/npa/agent_backend/model_router.py)** · <sub>nebius · GitHub · ⭐ 30 repo · 2026-04-07</sub><br>Advisory model router in Nebius's Physical AI Workbench agent backend that asks Jev whether a request needs the fast Nemotron model or MiniMax-M3 for multi-step reasoning, selecting no model on abstention or failure.
- **[AmberAgent Jev runtime](https://github.com/soul99soul-glitch/AmberAgent/tree/main/app/src/main/java/app/amber/core/jev)** · <sub>soul99soul-glitch · GitHub · ⭐ 26 repo · 2026-05-08</sub><br>Jev runtime in the AmberAgent Android AI workspace used for bounded phone-screen and web goals, model-council routing, memory reranking, semantic tool search and trimming long tool outputs before they reach the model.
- **[Loki Jev Auto](https://github.com/wundercorp/loki/blob/main/agent/jev_auto_router.py)** · <sub>wundercorp · GitHub · ⭐ 26 repo · 2026-09-17</sub><br>Jev Auto router in the Loki self-improving agent that picks a model for each new session from a bounded catalog on the already-selected gateway, plus optional Jev typed-judgment tools.
- **[VisionClaw Jev validation](https://github.com/Huskyauto/VisionClaw-Agent-Public-Release/blob/main/server/lib/typesafe-auto-validation.ts)** · <sub>Huskyauto · GitHub · ⭐ 26 repo · 2026-04-15</sub><br>Bounded, advisory-only Jev client in the VisionClaw self-hosted multi-tenant agent workspace, exposed as an agent tool and used to score deliverables for evidence support, requirement coverage and need for human review.
- **[abmind System One judgments](https://github.com/aksika/abmind/blob/dev/src/judgment-provider.ts)** · <sub>aksika · GitHub · ⭐ 20 repo · 2026-04-13</sub><br>Pluggable System One judgment provider in abmind, a persistent memory and RAG engine for AI agents, that sends recall and diagnostics questions to Jev or a locally served Laya model as advice to its combining code.
- **[askjev](https://github.com/pZacca/askjev)** · <sub>pZacca · GitHub · ⭐ 1 · 2026-09-17</sub><br>Unofficial MCP server, local over stdio or hosted on Cloudflare Workers, where an agent asks a plain question about material it holds and Jev picks yes/no, scale or choice and answers with calibrated probabilities.
- **[carryforward](https://github.com/Dharundp6/jev-carryforward)** · <sub>Dharundp6 · GitHub · ⭐ 1 · 2026-09-18</sub><br>MCP server that records facts during agent sessions in a per-project ledger and, at the start of a task, uses Jev via Vercel AI Gateway to recall only the facts that matter for it.
- **[DGUI-HyperMem](https://github.com/ctaxnagomi/dgui-hypermem)** · <sub>ctaxnagomi · GitHub · ⭐ 1 · 2026-09-19</sub><br>Self-hosted memory MCP server on Cloudflare Workers that fuses vector and full-text recall, then uses Jev to rerank memories, assign type and salience, and drop non-durable chatter.
- **[Group chat agent picker](https://x.com/vadimchoi/status/2101937206063780084)** · <sub>vadimchoi · X · ♥ 1 · 2026-09-21</sub><br>Compares three ways to decide which agent in a group chat should answer: @mentions, an LLM orchestrator at 4-7s and $0.00046 per message, and Jev at 0.29s median and $0.00002.
- **[Hermes Jev Router](https://github.com/ussyverse/hermes-jev-router)** · <sub>ussyverse · GitHub · ⭐ 1 · 2026-09-16</sub><br>Experimental Hermes plugin whose jev_route_plan tool uses Jev to assess task complexity, then policy picks an allowed model within cost, token, context, latency and capability limits; not yet run live.
- **[hermes-jev-north-star](https://github.com/poponline63/hermes-jev-north-star)** · <sub>poponline63 · GitHub · ⭐ 1 · 2026-09-18</sub><br>Hermes Agent skill that interviews the owner until a run has a checkable finish line, generates the run prompt, and gates completion with shell checks plus Jev for the requirements no script can decide.
- **[Jev MCP Server](https://github.com/MattiooFR/mcp-server-jev)** · <sub>MattiooFR · GitHub · ⭐ 1 · 2026-09-20</sub><br>MCP server that gives Codex, Claude, and other clients one generic tool for typed Jev decisions, with eight reproducible live scenarios from support triage to lead qualification and duplicates.
- **[Jev One](https://github.com/thezem/jev-one)** · <sub>thezem · GitHub · ⭐ 1 · 2026-09-19</sub><br>Experimental TypeScript runtime where Jev picks from application-supplied vocabularies of words, places, tools or stop requests, and the app applies each choice and feeds the observation back until an objective is verified.
- **[jev-compaction (picaye)](https://github.com/picaye/jev-compaction)** · <sub>picaye · GitHub · ⭐ 1 · 2026-09-18</sub><br>Context compaction for Hermes Agent sessions that never summarizes: Jev scores every tool call, stale calls and results are removed or truncated, and everything kept stays verbatim.
- **[jev-eval-mcp](https://github.com/BYK/jev-mcp)** · <sub>BYK · GitHub · ⭐ 1 · 2026-09-17</sub><br>Eval-first MCP server for Jev with tools to prototype a question, map a question set over many items, and measure question variants against labeled examples for accuracy, calibration and thresholds.
- **[jev-harness-router](https://github.com/JoacoMarc/jev-harness-router)** · <sub>JoacoMarc · GitHub · ⭐ 1 · 2026-09-18</sub><br>Per-turn router for agent harnesses where one Jev call of about 350 ms sets the model tier, effort, tools and skill behind a hard deadline; it picks the right skill 90.0% of the time versus 59.4% for keywords.
- **[jev-mcp (CodeIA Academy)](https://github.com/CodeIA-Academy/jev-mcp)** · <sub>CodeIA-Academy · GitHub · ⭐ 1 · 2026-09-20</sub><br>Dependency-free local MCP server, documented in Spanish, that exposes ask_jev and list_jev_models to Claude Code, Codex, Cursor, Hermes, and other agents.
- **[jev-model-router](https://github.com/az9713/jev-model-router)** · <sub>az9713 · GitHub · ⭐ 1 · 2026-09-19</sub><br>Web chat where Jev picks which LLM should answer each message and the chosen model replies, both through the Vercel AI Gateway, with a documented development journey and reliability evaluation.
- **[jev-toolkit](https://github.com/jbt95/jev-toolkit)** · <sub>jbt95 · GitHub · ⭐ 1 · 2026-09-21</sub><br>Effect-based MCP-first toolkit whose jev mcp server gives any harness Choice, Noul and Score judgments plus verify and review tools, with CLI triage, audit, label and route commands and Prometheus impact metrics.
- **[JevHarness](https://github.com/kevin9327/jev-harness)** · <sub>kevin9327 · GitHub · ⭐ 1 · 2026-09-18</sub><br>Pre-execution gate for a single agent tool call: one mixed Jev request returns an allow/ask/deny verdict, irreversibility score and yes/no checks, and Python code turns them into execute, confirm or reject.
- **[openclaw-jev-compaction](https://github.com/SqaaSSL/openclaw-jev-compaction)** · <sub>SqaaSSL · GitHub · ⭐ 1 · 2026-09-20</sub><br>Context engine for OpenClaw that asks Jev which tool calls and results a session still needs, drops the rest, and never summarizes, so what remains is the original text.
- **[PerfectRecall](https://github.com/arslanr-com/perfectrecall)** · <sub>arslanr-com · GitHub · ⭐ 1 · 2026-09-21</sub><br>Agent memory for Hermes that has Jev check every stored memory against short criteria from the calling agent, with no embeddings; an earlier version cut LongMemEval-S answer errors from 62 to 17 of 120.
- **[UX3 Product Design Harness Jev gate](https://github.com/cis2042/product-design-harness/blob/main/scripts/jev_gate.py)** · <sub>cis2042 · GitHub · ⭐ 17 repo · 2026-07-11</sub><br>Decision gate in an agent-operated product design harness that routes tasks and evaluates product decisions with Jev, returning continue, verify or stop-and-reframe verdicts plus task boundaries.
- **[Citadel promotion decisions](https://github.com/masumi-network/Citadel/blob/main/kb/promotion.py)** · <sub>masumi-network · GitHub · ⭐ 16 repo · 2026-05-20</sub><br>Promotion step in Citadel, self-hosted memory for engineering teams and their agents, where Jev decides whether a collected item is relevant and safe to promote into shared knowledge at a 0.7 threshold.
- **[Archive Center Jev selector](https://github.com/Flazer31/archive-center/blob/main/go-service/internal/httpapi/prepare_turn_jev.go)** · <sub>Flazer31 · GitHub · ⭐ 15 repo · 2026-06-30</sub><br>Optional Jev selector and reviewer in Archive Center, a local-first memory backend for RisuAI chats, that picks which stored memories and source evidence to pass into the next request without ever writing memories.
- **[sportsclaw Jev evidence verifier](https://github.com/machina-sports/sportsclaw/blob/main/docs/guide/jev-evidence-verifier.md)** · <sub>machina-sports · GitHub · ⭐ 15 repo · 2026-02-22</sub><br>Opt-in evidence verifier in sportsclaw, a CLI and bot scaffold connecting LLMs to live sports data, that uses a typed JevDecisionClient for the final evidence check so high-confidence support skips the generative verification pass.
- **[ExploitHunter Jev decision specialist](https://github.com/justsml/ExploitHunter.app/blob/main/src/server/research/jev-decision-specialist.ts)** · <sub>justsml · GitHub · ⭐ 14 repo · 2026-05-21</sub><br>Offensive-security research harness that uses Jev as a bounded decision specialist to pick tools and render formats, with a defer option and a persisted receipt for every call.
- **[JarvisCore Jev decisions](https://github.com/Prescott-Data/jarviscore-framework/blob/main/jarviscore/execution/decisions.py)** · <sub>Prescott-Data · GitHub · ⭐ 14 repo · 2026-01-07</sub><br>Native Jev support in the JarvisCore multi-agent runtime: agents ask typed Choice, Score and Noul questions through a decision client separate from the text model, and the kernel picks specialist subagents by Choice.
- **[ai-csuite Jev judgments](https://github.com/Fei2-Labs/skill-genie/blob/main/skills/ai-csuite/scripts/jev.py)** · <sub>Fei2-Labs · GitHub · ⭐ 12 repo · 2026-01-09</sub><br>AI C-Suite strategic debate skill that can use Jev to classify the decision topic and judge the executives' round-one positions, falling back to keyword logic without a key.
- **[ChainlessChain skill decision layer](https://github.com/chainlesschain/chainlesschain/blob/main/packages/cli/src/lib/decision-layer/typesafe-provider.js)** · <sub>chainlesschain · GitHub · ⭐ 11 repo · 2025-12-01</sub><br>Skill decision layer in a personal AI management CLI that can ask Jev which skill should handle a request, with an 800 ms timeout, metered usage and a benchmark harness.
- **[IPFS Accelerate TypeSafe advisor](https://github.com/endomorphosis/ipfs_accelerate_py/tree/main/ipfs_accelerate_py/agent_supervisor/integrations)** · <sub>endomorphosis · GitHub · ⭐ 11 repo · 2024-05-18</sub><br>Model server and agent supervisor with advisory TypeSafe integrations that route task kinds, guard traces and calibrate decisions beside the project's own Intelligence Index.
- **[tinyhivemind-typesafe](https://github.com/tinyhumansai/tinyhivemind/tree/main/crates/tinyhivemind-typesafe)** · <sub>tinyhumansai · GitHub · ⭐ 11 repo · 2026-08-31</sub><br>Rust crate that lets the TinyHiveMind multi-agent coordination library route handoffs with Jev, picking the best-placed teammate and also routing to any other option above 20%.
- **[Soothe TypeSafe decisions](https://github.com/mirasoth/soothe/blob/main/benchmarks/benchmark_typesafe_decisions.py)** · <sub>mirasoth · GitHub · ⭐ 10 repo · 2026-03-12</sub><br>Goal-driven orchestration framework for long-running agents that classifies intake intent and audits goal completion with typed decisions, plus a benchmark against hosted Jev, Laya or NanoJev servers.
- **[Starlight dialogue continuation](https://github.com/divaltor/starlight/blob/main/apps/starlight/src/ai/dialogue-continuation.ts)** · <sub>divaltor · GitHub · ⭐ 10 repo · 2024-01-05</sub><br>Telegram bot that asks Jev, for each group message, whether to reply with text, react with an emoji, or stay silent, and which emoji fits the message.
- **[NyatBot Jev guards](https://github.com/ZYHUO/nyat-bot/blob/nyatos/src/ai/jev.ts)** · <sub>ZYHUO · GitHub · ⭐ 9 repo · 2026-04-10</sub><br>Telegram group-chat agent that uses Jev to catch paraphrased repeats of its own messages and to block hallucinated facts that nobody in the chat mentioned or asked about.
- **[Ratify Jev tool-selection adapter](https://github.com/identities-ai/ratify-protocol/blob/main/references/langchain/authority_reference/jev_adapter.py)** · <sub>identities-ai · GitHub · ⭐ 9 repo · 2026-04-19</sub><br>Reference LangChain gate for the Ratify delegated-authority protocol where Jev proposes which tool an agent should call and Ratify then verifies the signed authority on the receiver side.
- **[AgentX decision backends](https://github.com/anis-marrouchi/agentx/blob/master/src/decisions/backends/simple-jev.ts)** · <sub>anis-marrouchi · GitHub · ⭐ 8 repo · 2026-02-11</sub><br>Self-hosted AI agent mesh for small businesses whose decision layer can run Jev-style typed decisions on a local LLM or a simple-jev server, recomputing confidence as normalized entropy.
- **[Crucible system_one route](https://github.com/neuralmagic/crucible/blob/main/examples/route/crucible.toml)** · <sub>neuralmagic · GitHub · ⭐ 8 repo · 2026-07-29</sub><br>Goal-directed research loop engine with an example domain where a decision role routes tickets through any POST /v1/systemone server, either hosted Jev or a vLLM DiffusionGemma server.
- **[Diana TypeSafe client](https://github.com/SuInk/Diana/blob/main/model/llm/typesafe.go)** · <sub>SuInk · GitHub · ⭐ 8 repo · 2026-07-02</sub><br>Self-hosted group-chat agent for QQ, Telegram, DingTalk, Feishu and WeCom that can use Jev to decide whether to chime in and whether a message is addressed to the bot.
- **[DurinDoor Jev routing classifier](https://github.com/bloodf/durindoor/blob/main/open-sse/config/jev.js)** · <sub>bloodf · GitHub · ⭐ 8 repo · 2026-07-03</sub><br>Self-hosted AI gateway over 236 providers that can ask Jev to classify each request as simple, medium, complex or reasoning and route it to a combo member of matching task level.
- **[HiRoute Jev decider](https://github.com/higress-group/HiRoute/tree/main/decision-extensions/extensions/jev-decider)** · <sub>higress-group · GitHub · ⭐ 8 repo · 2026-09-12</sub><br>Reference decision service for the HiRoute local model router that makes one Jev call per agent-turn boundary to pick the next model branch and score how competently the previous segment went.
- **[Imajin TypeSafe connector](https://github.com/ima-jin/imajin-ai/tree/main/apps/kernel/src/lib/typesafe)** · <sub>ima-jin · GitHub · ⭐ 8 repo · 2026-02-11</sub><br>Service connector in the reference implementation of the MJN trust protocol that lets identities call Jev with a sealed, kernel-held API key under a scoped typesafe:decide grant.
- **[RememberStack TypeSafe adapter](https://github.com/writeitai/remember-stack/blob/main/src/rememberstack/adapters/typesafe.py)** · <sub>writeitai · GitHub · ⭐ 8 repo · 2026-06-11</sub><br>Open memory infrastructure for AI agents that tracks claims, current beliefs and their sources, with a System One port whose TypeSafe adapter runs typed evaluations on Jev.
- **[opencompany approval review](https://github.com/useopencompany/opencompany/blob/main/packages/agent/src/approval-review.ts)** · <sub>useopencompany · GitHub · ⭐ 7 repo · 2026-05-20</sub><br>Approval reviewer in the opencompany AI workspace where Jev auto-approves routine integration actions only when they match the user's request and look low-risk; destructive, metered or permission changes always ask.
- **[OriginOS Jev perception decisions](https://github.com/NeuralNexusPro/startupOS/tree/main/packages/core/src/lib/integrations/jev)** · <sub>NeuralNexusPro · GitHub · ⭐ 7 repo · 2026-07-02</sub><br>Optional Jev decision mode for the perception rules of OriginOS, a local AI work system: when an event could go to several authorized projects, roles or skills, Jev picks the target and low-confidence cases go to the user.
- **[Paprwork jev_decide tool](https://github.com/Papr-ai/paprwork/blob/master/docs/JEV.md)** · <sub>Papr-ai · GitHub · ⭐ 7 repo · 2026-01-27</sub><br>Mastra tool in the Paprwork local-first desktop agent app that lets agents, sub-agents and scheduled jobs ask Jev typed noul, choice or score questions, with input guardrails and Papr-proxy or bring-your-own-key auth.
- **[AIQSA Jev decision features](https://github.com/insciqq/AIQSA/blob/main/lib/domain/decisionModels.ts)** · <sub>insciqq · GitHub · ⭐ 6 repo · 2026-07-22</sub><br>Jev integration in AIQSA, a self-hosted multi-provider AI workspace, that uses decision calls via OpenRouter for memory and knowledge-base relevance, tool discovery and skill suggestions, each enabled after its own qualification.
- **[Jev MCP server](https://github.com/podcctv/Narwhal-Cloud-podman-watcher/blob/main/scripts/jev_mcp_server.py)** · <sub>podcctv · GitHub · ⭐ 6 repo · 2026-04-14</sub><br>Zero-dependency Python MCP server bundled with the Narwhal Cloud container watcher that gives agents such as Claude Code, Cursor or Antigravity jev_choice, jev_noul, jev_score, jev_gate and jev_batch tools.
- **[unhardcoded-engine decision protocol](https://github.com/genlayerlabs/unhardcoded-engine/blob/main/docs/DECISION-PROTOCOL.md)** · <sub>genlayerlabs · GitHub · ⭐ 6 repo · 2026-05-19</sub><br>Decision-model routing in unhardcoded-engine, a pure-Lua policy algebra for LLM provider selection, that partitions candidates by protocol so Jev-style decision requests only route and fail over among decision models.
- **[Mimir TypeSafe skill and tool selection](https://github.com/shivendrasoni/mimir/blob/main/src/typesafe.rs)** · <sub>shivendrasoni · GitHub · ⭐ 5 repo · 2026-08-13</sub><br>TypeSafe integration in Mimir, a Rust recursive-language-model agent runtime, that selects the applicable skill and shortlists needed tools before a model call, rolled out through shadow, canary and acceptance benchmarks.
- **[nova-decide](https://github.com/mas-bandwidth/nova-tools/blob/main/docs/SPEC-DECIDE.md)** · <sub>mas-bandwidth · GitHub · ⭐ 5 repo · 2026-08-07</sub><br>Typed-decision route in Nova Tools, a set of tools for AI agents on different models to message, wait and swarm together, where Jev answers small choice, score or yes/no judgments beside deterministic machinery.
- **[Safeplane routing advisor](https://github.com/stefanrossmeier/safeplane/tree/main/experiments/routing_advisor)** · <sub>stefanrossmeier · GitHub · ⭐ 5 repo · 2026-07-22</sub><br>Experimental routing advisor in Safeplane, a local-first control plane for bounded AI-agent workflows with CLI and Telegram connectors, that asks Jev via OpenRouter Decisions which workflow an operator request should go to.
- **[SilkChat Jev skill selection](https://github.com/medy17/SilkChat/blob/main/convex/lib/models/typesafe.ts)** · <sub>medy17 · GitHub · ⭐ 5 repo · 2026-02-11</sub><br>Jev integration in SilkChat, a TanStack Start and Convex AI chat app, that picks which skills to enable on a conversation's opening turn: web search, code execution, memory, math or image generation.
- **[the-array Jev decision layer](https://github.com/clduab11/the-array/blob/main/docs/jev-decision-layer.md)** · <sub>clduab11 · GitHub · ⭐ 1 repo · 2026-09-11</sub><br>Opt-in Jev layer in a self-hosted LiteLLM gateway reference build that picks model tiers and referees replies as answered, refused, or non-answer, moving to the next model after a confident decline.
- **[Agent action approval](https://openrouter.ai/labs/jev/overseer)** · <sub>OpenRouter · App</sub><br>OpenRouter Labs recipe that runs four checks (off task, could destroy, untrusted input, ask first) on each of 24 coding or ops agent tool calls in one request, so risky steps stop for a person: 96 answers in 0.5 s.
- **[Agent action approval at Weathernews](https://zenn.dev/weathernews/articles/jev-auto-approval-poc)** · <sub>Weathernews (Sakamoto) · Article · 2026-09-18</sub><br>Weathernews replaced the LLM that approved operations in its internal AI agent with Jev, keeping classification accuracy while cutting latency and cost, and shares the design and comparison.
- **[agentic-harness-cli](https://github.com/powerpuff-kitty/agentic-harness-cli)** · <sub>powerpuff-kitty · GitHub · 2026-09-03</sub><br>Rust CLI for governing agent-native repositories whose decisions commands build Jev payloads for boolean, choice, and ordinal decisions, store answers as review-required receipts, and gate calibration regressions in CI.
- **[AskJev MCP](https://github.com/cbruyndoncx/AskJev-MCP)** · <sub>cbruyndoncx · GitHub · 2026-09-18</sub><br>MCP server built on the official @typesafe-ai/sdk that gives agents ask_choice, ask_noul, and ask_score tools returning Jev's selected option, per-option probabilities, and confidence.
- **[decide-mcp](https://github.com/dakdevs/decide-mcp)** · <sub>dakdevs · GitHub · 2026-09-17</sub><br>Local MCP server that lets an agent hand off a decision with context and choices to Jev through AI Gateway by default, returning a recommended choice with percentages, with custom policies and bias-profile routing.
- **[Decision Graph Protocol](https://github.com/numerous-com/dgp)** · <sub>numerous-com · GitHub · 2026-09-19</sub><br>Open protocol for decision-based agents: apps expose immutable evidence frames, typed decisions and guarded actions, and a Jev adapter produces assessments while application code keeps control of effects.
- **[Frost](https://github.com/marcus/frost)** · <sub>marcus · GitHub · 2026-09-17</sub><br>Go CLI that takes a prompt or markdown doc and recommends a model, harness or API and effort level, using one Jev analysis request and then deterministic local selection of the cheapest profile meeting the quality floor.
- **[HarnessJudge](https://github.com/ndolinschi/harnessjudge)** · <sub>ndolinschi · GitHub · 2026-09-17</sub><br>Paste an agent step trace and get an ok, retry, escalate or stop decision for agent builders.
- **[Jev Checkpoint](https://github.com/ashishakkumar/Jev-Checkpoint)** · <sub>ashishakkumar · GitHub · 2026-09-21</sub><br>Local MCP server that turns an agent's bounded next-step decision, such as proceed, inspect callers or ask the user, into one Jev Choice and returns the route, probabilities and a thresholded recommendation.
- **[JEV plugins](https://github.com/Pinutss/jev-plugins)** · <sub>Pinutss · GitHub · 2026-09-18</sub><br>Cursor and Hermes plugin marketplace for four JEV Labs selectors, for memories, agents, models, and MCP tools, that filter candidates by task and budget, locally by default with Jev as an optional judge.
- **[jev-agent-tool](https://github.com/nandansrikrishna/jev-agent-tool)** · <sub>nandansrikrishna · GitHub · 2026-09-19</sub><br>Bring-your-own-key CLI, Python API and local MCP server built on the official Python SDK, letting agents invent typed questions at runtime and get Jev decisions with probabilities.
- **[jev-decision-gateway](https://github.com/kuldeepsinh19/jev-decision-gateway)** · <sub>kuldeepsinh19 · GitHub · 2026-09-19</sub><br>Provider-agnostic gateway in front of expensive LLMs: Jev answers small continue, tool, relevance, and verification questions, and a policy layer calls a generative model only when generation is needed.
- **[Jev-Evolve](https://github.com/novaleolin/jev-evolve)** · <sub>novaleolin · GitHub · 2026-09-21</sub><br>Agent framework where every branch is a typed Jev question and the policy text evolves from the agent's own mistakes, reporting how much of a gain is selection noise; one schema scored 0.188 or 0.542 depending on option order.
- **[jev-mcp (codaaiteam)](https://github.com/codaaiteam/jev-mcp)** · <sub>codaaiteam · GitHub · 2026-09-19</sub><br>MCP server that gives Claude Code, Codex, Cursor or Pi Jev-backed tools to classify, score, check yes/no and gate risky tool calls, each as one API call.
- **[jev.mcp](https://github.com/hangarbay/jev.mcp)** · <sub>hangarbay · GitHub · 2026-09-17</sub><br>Go MCP server exposing Jev as five tools: classify, score, check, a mixed multi-question ask over one state, and model listing.
- **[jevkit](https://github.com/walidboulanouar/jev-agent-kit)** · <sub>walidboulanouar · GitHub · 2026-09-20</sub><br>Zero-dependency CLI and MCP server with eleven Jev-backed tools such as route, triage, guard, grep, rank, compact and judge, plus six runnable use cases including a Claude Code guard hook and a PR ranker.
- **[LiteLLM auto router](https://docs.litellm.ai/docs/proxy/auto_routing)** (release candidate) · <sub>LiteLLM · Article</sub><br>Picks a model tier for each request with a Jev Choice.
- **[LiteLLM guardrail](https://docs.litellm.ai/docs/proxy/guardrails/typesafe)** (release candidate) · <sub>LiteLLM · Article</sub><br>Asks one Noul per finished tool exchange and clears results that are no longer needed before each call.
- **[Maza](https://github.com/prasanth263/maza)** · <sub>prasanth263 · GitHub · 2026-09-18</sub><br>Local MCP gateway that connects your MCP servers once and shows agents just two tools: find_tool, which uses a Jev Choice to discover a capability, and execute_tool.
- **[mcp_jev](https://github.com/pedroknigge/mcp_jev)** · <sub>pedroknigge · GitHub · 2026-09-19</sub><br>Local MCP server for Cursor and other agents that runs ready-made Jev question packs, with a typed run_questions tool for custom Choice, Noul and Score judgments.
- **[McpMatch](https://github.com/ndolinschi/mcpmatch)** · <sub>ndolinschi · GitHub · 2026-09-17</sub><br>Web app that matches a user goal to the best MCP server or capability in a catalog, using a two-stage Jev pass when the catalog is large.
- **[mewcp-jev](https://github.com/AStheTECH/mewcp-jev)** · <sub>AStheTECH · GitHub · 2026-09-18</sub><br>MCP server exposing Jev's System One API so agents can grade text or structured state against mixed yes/no, single-choice and rubric questions in one call and list available model aliases.
- **[openclaw-plugin-typesafe-ai](https://github.com/jason-allen-oneal/openclaw-plugin-typesafe-ai)** · <sub>jason-allen-oneal · GitHub · 2026-09-18</sub><br>OpenClaw plugin that uses Jev for group-chat triage on whether to respond, tool-call safety checks, compaction curation and model routing, without modifying the OpenClaw core.
- **[openrouter-jev-mcp](https://github.com/ctmx/openrouter-jev-mcp)** · <sub>ctmx · GitHub · 2026-09-19</sub><br>Python decision gateway and MCP server that exposes Jev through OpenRouter's decisions endpoint to Claude Code, Codex and Cursor as classify, score and check tools for the small bounded questions agents hit.
- **[ProgressGate](https://github.com/AshutoshVJTI/progressgate)** · <sub>AshutoshVJTI · GitHub · 2026-09-18</sub><br>Library that watches recent agent steps for semantic stagnation, where different actions keep chasing the same contradicted assumption; Jev reads the trajectory and a small deterministic policy decides what to do.
- **[Skilltree](https://github.com/its-panzer/skilltree)** · <sub>its-panzer · GitHub · 2026-09-17</sub><br>Local-first website and MCP server that turns a collection of agent instructions into a navigable skill tree, with Jev making a visible typed choice at each level to pick the path.
- **[SpendBrake](https://github.com/ndolinschi/spendbrake)** · <sub>ndolinschi · GitHub · 2026-09-17</sub><br>Budget brake for agent runs that reads the budget, spend so far and remaining plan, then decides continue, downgrade the model or stop, with a value-for-cost score and over-budget checks.
- **[SwarmRouter](https://github.com/ndolinschi/swarmrouter)** · <sub>ndolinschi · GitHub · 2026-09-17</sub><br>Routes a task to a research, code, browser, support or writer agent with a confidence value, shown on a visual swarm map.
- **[switchboard](https://github.com/aniruddh-krovvidi/switchboard)** · <sub>aniruddh-krovvidi · GitHub · 2026-09-17</sub><br>Stdlib-Python guardrail and model router for LLM gateways built on Jev, shipped with an independent evaluation of its accuracy, calibration and latency.
- **[typesafe-mcp-server](https://github.com/bestagentkits/typesafe-demo-mcp)** · <sub>bestagentkits · GitHub · 2026-09-17</sub><br>MCP server built on @typesafe-ai/sdk that exposes Choice, Score and Noul judgments and model listing as agent-callable tools, bundled with the official TypeSafe agent skill.
- **[wakegate](https://github.com/shitianfang/wakegate)** · <sub>shitianfang · GitHub · 2026-09-18</sub><br>Fail-open gate for long-running agents on Workers, Durable Objects and Node that asks Jev, before a sleeping agent's LLM is resumed by a timer or event, whether the wakeup matters given the agent's own sleep note.

</details>

Missing something? [Suggest a resource](https://github.com/Li-Evan/awesome-jev/issues/new/choose).
