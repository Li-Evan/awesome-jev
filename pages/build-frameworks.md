# 🔌 Build with Jev: Framework Adapters

Ways to call Jev from your stack: hosted access, framework adapters, observability, and community SDKs. 174 entries, ranked by community traction.

[← Back to Awesome Jev](https://github.com/Li-Evan/awesome-jev#framework-adapters)

[Model Access](https://github.com/Li-Evan/awesome-jev/blob/main/pages/build-model-access.md) (68) · **Framework Adapters** · [Observability](https://github.com/Li-Evan/awesome-jev/blob/main/pages/build-observability.md) (14) · [Community SDKs](https://github.com/Li-Evan/awesome-jev/blob/main/pages/build-community-sdks.md) (107)

<table>
<tr>
<td width="260" valign="top"><a href="https://github.com/openclaw/openclaw/tree/main/extensions/typesafe"><img src="https://opengraph.githubassets.com/1/openclaw/openclaw" alt="OpenClaw TypeSafe plugin" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/openclaw/openclaw/tree/main/extensions/typesafe">OpenClaw TypeSafe plugin</a></b><br><sub>openclaw · GitHub · ⭐ 75 · 2025-11-24</sub><br>Official OpenClaw plugin that plugs hosted Jev, or a local Kev server, into OpenClaw's decision-model API for Choice, Score and Boolean judgments, plus an optional typesafe_evaluate tool.<br><sub><b>How it uses Jev:</b> Select typesafe/jev-latest as an agent's decisionModel, globally or per agent.</sub><br><sub>Also: <a href="https://docs.openclaw.ai/plugins/typesafe">docs</a> · <a href="https://docs.openclaw.ai/plugins/typesafe">link</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/langchain-ai/langchain/tree/master/libs/partners/typesafe"><img src="https://repository-images.githubusercontent.com/552661142/7392d590-2716-4261-b623-a0579df67e0d" alt="langchain-typesafe" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/langchain-ai/langchain/tree/master/libs/partners/typesafe">langchain-typesafe</a></b><br><sub>langchain-ai · GitHub · ⭐ 146.8k repo · 2026-09-17</sub><br>LangChain partner package with a TypeSafeClassifier runnable for Choice, Noul and Score questions, plus experimental auto-mode and model-router middleware.<br><sub>Also: <a href="https://github.com/langchain-ai/langchain">repo</a> · <a href="https://pypi.org/project/langchain-typesafe/">pypi</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/ctatedev/status/2100584917092409479"><img src="https://pbs.twimg.com/media/HSbG2YLWkAAPqmU.jpg?name=orig" alt="ai-cli" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/ctatedev/status/2100584917092409479">ai-cli</a></b><br><sub>ctatedev · X · ♥ 1.2k · 2026-09-17</sub><br>Vercel Labs' terminal AI tool, installed with npm, that lets any agent harness ask Jev yes/no questions, choose between options, and score against criteria from the command line.<br><sub>Also: <a href="https://github.com/vercel-labs/ai-cli">repo</a> · <a href="https://ai-cli.dev">site</a> · <a href="https://github.com/vercel-labs/ai-cli">project</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/ComposioHQ/composio/tree/next/ts/packages/providers/typesafe"><img src="https://opengraph.githubassets.com/1/ComposioHQ/composio" alt="Composio" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/ComposioHQ/composio/tree/next/ts/packages/providers/typesafe">Composio</a></b><br><sub>ComposioHQ · GitHub · ⭐ 30.3k repo · 2026-09-17</sub><br>TypeScript provider that picks and gates tool calls with a Choice and binds closed-set arguments before execution.<br><sub>Also: <a href="https://github.com/ComposioHQ/composio">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/vercel/ai/tree/main/packages/typesafe-ai"><img src="https://repository-images.githubusercontent.com/644461337/ed2df190-2452-4a24-8529-fbf4871e0c4b" alt="AI SDK TypeSafe provider" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/vercel/ai/tree/main/packages/typesafe-ai">AI SDK TypeSafe provider</a></b><br><sub>vercel · GitHub · ⭐ 26.9k repo · 2026-09-16</sub><br>Official AI SDK provider package @ai-sdk/typesafe-ai that runs Choice, Score and Boolean questions against Jev through the experimental evaluate API.<br><sub>Also: <a href="https://github.com/vercel/ai">repo</a> · <a href="https://github.com/vercel/ai/tree/main/examples/ai-functions/src/evaluate/typesafe-ai">examples</a> · <a href="https://www.npmjs.com/package/@ai-sdk/typesafe-ai">npm</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/pydantic/pydantic-ai/blob/main/pydantic_ai_slim/pydantic_ai/models/typesafe.py"><img src="https://pydantic.dev/docs/ai/img/pydantic-ai-light.svg" alt="Pydantic AI TypeSafeModel" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/pydantic/pydantic-ai/blob/main/pydantic_ai_slim/pydantic_ai/models/typesafe.py">Pydantic AI TypeSafeModel</a></b><br><sub>pydantic · GitHub · ⭐ 20.1k repo · 2026-09-18</sub><br>Pydantic AI model class that runs decision agents on Jev: each field of the output_type becomes one question and the answers fill the output, so swapping the model name compares Jev with an LLM.<br><sub>Also: <a href="https://github.com/pydantic/pydantic-ai">repo</a> · <a href="https://github.com/pydantic/pydantic-ai/blob/main/docs/models/typesafe.md">docs</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/elizaOS/eliza/tree/develop/packages/agent/src/services/typesafe"><img src="https://raw.githubusercontent.com/elizaOS/eliza/develop/packages/shared/assets/banners/elizaos_banner.svg" alt="elizaOS TypeSafe adapter" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/elizaOS/eliza/tree/develop/packages/agent/src/services/typesafe">elizaOS TypeSafe adapter</a></b><br><sub>elizaOS · GitHub · ⭐ 19.4k repo · 2026-09-16</sub><br>Opt-in server-side TypeSafe client in the elizaOS agent package that validates Choice, Score and Noul requests with Zod and sends them only on an explicit systemOne call; it is not registered with the runtime by default.<br><sub>Also: <a href="https://github.com/elizaOS/eliza">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/langchain-ai/langchainjs/tree/main/libs/providers/langchain-typesafe"><img src="https://repository-images.githubusercontent.com/598342280/41cd6da7-4afb-4b7f-b2dd-9fd52b1cc773" alt="LangChain.js" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/langchain-ai/langchainjs/tree/main/libs/providers/langchain-typesafe">LangChain.js</a></b><br><sub>langchain-ai · GitHub · ⭐ 18.2k repo · 2026-09-18</sub><br>JavaScript version of the classifier and the routing and approval middleware.<br><sub>Also: <a href="https://github.com/langchain-ai/langchainjs">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Effect-TS/effect/tree/main/packages/ai/typesafe"><img src="https://opengraph.githubassets.com/1/Effect-TS/effect" alt="@effect/ai-typesafe" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Effect-TS/effect/tree/main/packages/ai/typesafe">@effect/ai-typesafe</a></b><br><sub>Effect-TS · GitHub · ⭐ 16.2k repo · 2026-09-18</sub><br>Effect's DecisionModel provider for TypeSafe's System One API, supporting classification, ordered ratings and probabilities through Effect HttpClient, with provider distributions preserved rather than normalized.<br><sub>Also: <a href="https://github.com/lootlog/monorepo/tree/main/repos/effect/packages/ai/typesafe">mirror</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/BoundaryML/baml/tree/canary/baml_language/crates/baml_builtins2/baml_std/typesafeai"><img src="https://opengraph.githubassets.com/1/BoundaryML/baml" alt="BAML Jev support" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/BoundaryML/baml/tree/canary/baml_language/crates/baml_builtins2/baml_std/typesafeai">BAML Jev support</a></b><br><sub>BoundaryML · GitHub · ⭐ 9.3k repo · 2026-09-19</sub><br>Nightly v1 integration in BAML, the programming language for agents, that maps typed function return values to Jev questions; not yet in the stable release line.<br><sub>Also: <a href="https://github.com/BoundaryML/baml">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/0xPlaygrounds/rig/tree/main/crates/rig-typesafeai"><img src="https://raw.githubusercontent.com/0xPlaygrounds/rig/main/img/rig-rebranded-logo-white.svg" alt="Rig" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/0xPlaygrounds/rig/tree/main/crates/rig-typesafeai">Rig</a></b> <sub>(merged, not yet on crates.io)</sub><br><sub>0xPlaygrounds · GitHub · ⭐ 8.7k repo · 2026-09-18</sub><br>Rust support that turns structs implementing a query trait into Jev requests.<br><sub>Also: <a href="https://github.com/0xPlaygrounds/rig">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/YaoApp/yao/tree/main/agent/decision"><img src="https://raw.githubusercontent.com/YaoApp/yao/main/docs/how-it-works.png" alt="Yao decision role" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/YaoApp/yao/tree/main/agent/decision">Yao decision role</a></b><br><sub>YaoApp · GitHub · ⭐ 8k repo · 2021-09-06</sub><br>Yao Agents adds a decision role connector for typed decision requests, with TypeSafe AI's jev-latest as a preset provider alongside the chat models.<br><sub>Also: <a href="https://yaoagents.com">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/CTNicholas/jev-workflow-builder"><img src="https://pbs.twimg.com/amplify_video_thumb/2102070615926771715/img/PueMU1HUq0WB86ZG.jpg" alt="Jev workflow builder" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/CTNicholas/jev-workflow-builder">Jev workflow builder</a></b><br><sub>CTNicholas · GitHub · ⭐ 78 · 2026-09-21</sub><br>Liveblocks demo of a multiplayer visual workflow builder that wires Jev and LLM nodes together, runs workflows through a REST API, and shows test-run previews and live cursors.<br><sub>Also: <a href="https://x.com/ctnicholasdev/status/2102070640589279318">demo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/samchon/typia/tree/master/packages/jev"><img src="https://repository-images.githubusercontent.com/482949726/ac595228-a409-4c77-99d8-d134b125281d" alt="@typia/jev" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/samchon/typia/tree/master/packages/jev">@typia/jev</a></b><br><sub>samchon · Package · ⭐ 5.9k repo · 2022-04-18</sub><br>Typia package that turns a TypeScript interface into Jev questions via typia.llm.evaluation&lt;T&gt;(), so booleans and string unions become typed Noul and Choice questions.<br><sub><b>How it uses Jev:</b> Converts to the wire format shared by TypeSafe's API and SDK and OpenRouter's Decisions API.</sub><br><sub>Also: <a href="https://www.npmjs.com/package/@typia/jev">npm</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/oomol-lab/open-connector/tree/main/src/providers/typesafe_ai"><img src="https://raw.githubusercontent.com/oomol-lab/open-connector/main/assets/openconnector-readme-banner.png" alt="OpenConnector TypeSafe AI provider" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/oomol-lab/open-connector/tree/main/src/providers/typesafe_ai">OpenConnector TypeSafe AI provider</a></b><br><sub>oomol-lab · GitHub · ⭐ 5.9k repo · 2026-06-29</sub><br>TypeSafe AI provider in the OpenConnector auth gateway, exposing Jev Noul, Choice and Score evaluation as prebuilt actions that agents can call through SDK, CLI, MCP or HTTP.<br><sub>Also: <a href="https://oomol.com">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/vercel/eve/blob/main/packages/eve/src/ai/evaluate.ts"><img src="https://opengraph.githubassets.com/1/vercel/eve" alt="eve Jev support" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/vercel/eve/blob/main/packages/eve/src/ai/evaluate.ts">eve Jev support</a></b><br><sub>vercel · GitHub · ⭐ 5.3k repo · 2026-06-16</sub><br>Jev support in Vercel's eve agent framework: an evaluate helper that asks typed Choice, Score and Boolean questions inside tools, and an auto model router that defaults to Jev through Vercel AI Gateway.<br><sub>Also: <a href="https://github.com/vercel/eve">repo</a> · <a href="https://eve.dev">website</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/beautyyuyanli/status/2100913383143026873"><img src="https://pbs.twimg.com/media/HSfxfsSasAAvv2h.jpg?name=orig" alt="Dify classifier node with Jev" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/beautyyuyanli/status/2100913383143026873">Dify classifier node with Jev</a></b><br><sub>beautyyuyanli · X · ♥ 29 · 2026-09-18</sub><br>Dify's classifier node now supports Jev as the model, so workflow builders can route inputs with Jev's typed decisions.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Kiln-AI/Kiln/tree/main/libs/core/kiln_ai/adapters/jev"><img src="https://repository-images.githubusercontent.com/832879402/669449f8-c948-40a0-9f73-866e06cac97a" alt="Kiln Jev provider" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Kiln-AI/Kiln/tree/main/libs/core/kiln_ai/adapters/jev">Kiln Jev provider</a></b><br><sub>Kiln-AI · GitHub · ⭐ 5.1k repo · 2024-07-23</sub><br>Jev provider for the Kiln AI workbench that runs compatible single-turn tasks and evals on Jev by mapping JSON-schema enums, booleans and scores to Jev questions and back.<br><sub><b>How it uses Jev:</b> Aimed at evals: Kiln's 1-5 star and pass/fail schemas fit Jev's question types, and native probabilities replace G-Eval's logprob approximation.</sub><br><sub>Also: <a href="https://kiln.tech">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/typesafe-ai/system-one-adapter-python"><img src="https://opengraph.githubassets.com/1/typesafe-ai/system-one-adapter-python" alt="System One adapter" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/typesafe-ai/system-one-adapter-python">System One adapter</a></b><br><sub>typesafe-ai · GitHub · ⭐ 245 · 2026-08-08</sub><br>Drop-in <code>TypeSafeClient</code> replacement backed by LLM APIs, for comparing cost, speed, and quality with Jev on your own workflow.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/crmne/ruby_llm/blob/main/lib/ruby_llm/providers/typesafe.rb"><img src="https://raw.githubusercontent.com/crmne/ruby_llm/main/docs/assets/images/logotype.svg" alt="RubyLLM TypeSafe provider" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/crmne/ruby_llm/blob/main/lib/ruby_llm/providers/typesafe.rb">RubyLLM TypeSafe provider</a></b><br><sub>crmne · GitHub · ⭐ 4.4k repo · 2025-01-30</sub><br>TypeSafe provider in RubyLLM, the Ruby and Rails AI framework, connecting Jev judgment models through a dedicated System One protocol alongside the chat providers.<br><sub>Also: <a href="https://rubyllm.com/">docs</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/dromara/liteflow/tree/master/liteflow-agent/liteflow-agent-jev"><img src="https://raw.githubusercontent.com/dromara/liteflow/master/static/img/flow_e1.png" alt="liteflow-agent-jev" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/dromara/liteflow/tree/master/liteflow-agent/liteflow-agent-jev">liteflow-agent-jev</a></b><br><sub>dromara · GitHub · ⭐ 3.9k repo · 2020-03-25</sub><br>Jev switch component for the LiteFlow rule engine: JevSwitchComponent routes a flow to a target node id via a Jev Choice, wired into the DSL's SWITCH().to().DEFAULT().<br><sub><b>How it uses Jev:</b> Configured with a min-confidence threshold; supports TypeSafe and OpenRouter's Decisions API.</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/ash-project/ash_ai"><img src="https://opengraph.githubassets.com/1/ash-project/ash_ai" alt="Ash AI evaluate" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/ash-project/ash_ai">Ash AI evaluate</a></b><br><sub>ash-project · GitHub · ⭐ 189 · 2024-08-29</sub><br>Elixir Ash framework extension whose evaluate/2 maps an Ash action onto typed questions for evaluation models like Jev, returning typed answers with probabilities and confidence.<br><sub><b>How it uses Jev:</b> run evaluate("typesafe:jev-latest") inside an action, with Noul, Choice and Score question builders.</sub><br><sub>Also: <a href="https://ash-hq.org">docs</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/ndrezn/status/2102088289876418563"><img src="https://pbs.twimg.com/media/HSwd5SWW0AA97cu.jpg?name=orig" alt="LangChain Jev routing middleware" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/ndrezn/status/2102088289876418563">LangChain Jev routing middleware</a></b><br><sub>ndrezn · X · ♥ 16 · 2026-09-21</sub><br>LangChain middleware for managed deep agents that lets you define routes and has Jev pick the model for each request.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/TanStack/ai/tree/main/packages/ai-typesafe"><img src="https://tanstack.com/api/readme/ai.png" alt="TanStack AI Jev adapter" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/TanStack/ai/tree/main/packages/ai-typesafe">TanStack AI Jev adapter</a></b><br><sub>TanStack · GitHub · ⭐ 3.1k repo · 2025-10-08</sub><br>Adapter package for TanStack AI that exposes Jev through a decide() call with typed Choice, Score, and yes/no questions, talking to the API over plain fetch with no TypeSafe SDK dependency.<br><sub>Also: <a href="https://github.com/TanStack/ai">repo</a> · <a href="https://www.npmjs.com/package/@tanstack/ai-typesafe">npm</a> · <a href="https://tanstack.com/ai/latest">docs</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/ax-llm/ax/tree/main/src/ax/ai/typesafe"><img src="https://opengraph.githubassets.com/1/ax-llm/ax" alt="Ax TypeSafe provider" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/ax-llm/ax/tree/main/src/ax/ai/typesafe">Ax TypeSafe provider</a></b><br><sub>ax-llm · GitHub · ⭐ 2.9k repo · 2026-09-17</sub><br>TypeSafe provider in Ax, the DSPy-style TypeScript framework, mapping boolean and finite-class signatures to Jev questions or native System One requests, also ported to its generated Python, Go, Java, C++ and Rust libraries.<br><sub>Also: <a href="https://github.com/ax-llm/ax">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/donvito/ai-backends"><img src="https://opengraph.githubassets.com/1/donvito/ai-backends" alt="AI Backends" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/donvito/ai-backends">AI Backends</a></b><br><sub>donvito · GitHub · ⭐ 146 · 2025-05-21</sub><br>Self-hostable API server for common AI tasks that adds a /api/evaluate decision endpoint backed by Jev for Choice, Score and Noul questions.<br><sub>Also: <a href="https://aibackends.com">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/paolino/status/2102086504986169652"><img src="https://pbs.twimg.com/media/HSwbKb7XwAAT9Wj.jpg?name=orig" alt="RubyLLM::Judge" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/paolino/status/2102086504986169652">RubyLLM::Judge</a></b><br><sub>paolino · X · ♥ 123 · 2026-09-21</sub><br>Judgment API in the RubyLLM framework with support for Jev, for typed evaluations from Ruby and Rails apps.<br><sub>Also: <a href="https://rubyllm.com/next/judgments/">docs</a> · <a href="https://github.com/crmne/ruby_llm">repo</a> · <a href="https://github.com/crmne/ruby_llm">project</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/danvega/jev-spring-boot-starter"><img src="https://opengraph.githubassets.com/1/danvega/jev-spring-boot-starter" alt="Jev Spring Boot Starter" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/danvega/jev-spring-boot-starter">Jev Spring Boot Starter</a></b><br><sub>danvega · GitHub · ⭐ 30 · 2026-09-20</sub><br>Community Spring Boot 4 starter that auto-configures an injectable JevClient on Spring MVC and RestClient, so a Java service can ask Jev typed questions after adding one dependency and an API key.<br><sub>Also: <a href="https://www.youtube.com/watch?v=fq_nYo4BnrY">video</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/neuron-core/neuron-ai/tree/3.x/src/Classifier/TypeSafeAI"><img src="https://repository-images.githubusercontent.com/941562247/8b2db3ba-ba3b-4a74-95cc-da8bbead2b8c" alt="Neuron AI TypeSafe classifier" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/neuron-core/neuron-ai/tree/3.x/src/Classifier/TypeSafeAI">Neuron AI TypeSafe classifier</a></b><br><sub>neuron-core · GitHub · ⭐ 2.1k repo · 2025-03-02</sub><br>TypeSafe AI classifier for Neuron AI, the PHP agentic framework, mapping its Boolean, Choice and Score classification requests onto Jev's System One API.<br><sub>Also: <a href="https://docs.neuron-ai.dev">docs</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/peterfriese/jev-foundation-models"><img src="https://pbs.twimg.com/media/HSwjl81bkAAlliY.jpg?name=orig" alt="Jev for Apple Foundation Models" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/peterfriese/jev-foundation-models">Jev for Apple Foundation Models</a></b><br><sub>peterfriese · GitHub · ⭐ 10 · 2026-09-21</sub><br>Swift 6 bridge that maps Apple Foundation Models @Generable Boolean, enum and bounded score fields to one Jev question set and decodes the typed answers through LanguageModelSession.<br><sub>Also: <a href="https://x.com/peterfriese/status/2102094265702821993">demo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/pithings/advocaat"><img src="https://opengraph.githubassets.com/1/pithings/advocaat" alt="Advocaat" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/pithings/advocaat">Advocaat</a></b><br><sub>pithings · GitHub · ⭐ 89 · 2026-09-16</sub><br>Small TypeScript client for asking Jev several yes/no, option and score questions about the same data in one request and reading typed values back, with an agent skill that teaches question design.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/spring-ai-community/spring-ai-typesafe"><img src="https://pbs.twimg.com/media/HSvVraQWUAEukT5.jpg?name=orig" alt="Spring AI TypeSafe" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/spring-ai-community/spring-ai-typesafe">Spring AI TypeSafe</a></b><br><sub>spring-ai-community · GitHub · ⭐ 19 · 2026-09-20</sub><br>Java client and Spring AI components for judging, guardrails, self-refinement, and RAG filtering and reranking.<br><sub>Also: <a href="https://spring-ai-community.github.io/spring-ai-typesafe">docs</a> · <a href="https://x.com/christzolov/status/2102009563083870575">demo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/hyperspaceai/jevcache"><img src="https://repository-images.githubusercontent.com/1375761817/b17d8cf2-457c-446a-82cf-4bd18e00bb47" alt="jevcache" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/hyperspaceai/jevcache">jevcache</a></b><br><sub>hyperspaceai · GitHub · ⭐ 70 · 2026-09-18</sub><br>Local decision cache for Jev-class models, shipped as a 2 MB binary, that memoizes decisions over redacted and canonicalized state so repeats are free and CI can replay fixtures to catch model drift.<br><sub>Also: <a href="https://jevcache.sh">site</a> · <a href="https://jevcache.sh">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/cayu-dev/cayu"><img src="https://opengraph.githubassets.com/1/cayu-dev/cayu" alt="Cayu TypeSafeProvider" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/cayu-dev/cayu">Cayu TypeSafeProvider</a></b><br><sub>cayu-dev · GitHub · ⭐ 69 · 2026-07-16</sub><br>Production runtime for long-horizon Python agents with an experimental TypeSafeProvider for native Choice, Score and Noul decisions through Cayu sessions and events.<br><sub>Also: <a href="https://cayu.dev/">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://deepclause.substack.com/p/jev-prolog-pi-and-the-dream-of-probabilistic"><img src="https://substackcdn.com/image/fetch/$s_!HKv7!,w_1200,h_675,c_fill,f_jpg,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2c7a3019-d2dc-4963-86b0-5e1bb06225d4_1220x364.png" alt="DeepClause + Jev" width="240"></a></td>
<td valign="top"><b><a href="https://deepclause.substack.com/p/jev-prolog-pi-and-the-dream-of-probabilistic">DeepClause + Jev</a></b><br><sub>Andreas (DeepClause) · Article · ▲ 21 · 2026-09-21</sub><br>Announces Jev support in DeepClause and its Pi extension, mapping Jev judgments onto Prolog-style DML predicates for fast, deterministic agent decisions, and asks if this revives probabilistic logic programming.<br><sub><b>How it uses Jev:</b> A judge/2 predicate batches Jev questions over a state; deterministic Prolog relations then select and annotate.</sub><br><sub>Also: <a href="https://github.com/deepclause/deepclause-sdk">repo</a> · <a href="https://www.npmjs.com/package/deepclause-pi">npm</a> · <a href="https://news.ycombinator.com/item?id=49781694">discussion</a> · <a href="https://github.com/deepclause/deepclause-sdk">project</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/typesafeainate/dspy-typesafeify"><img src="https://raw.githubusercontent.com/typesafeainate/dspy-typesafeify/main/examples/typesafe_dspy_ticket_triage/benchmark.svg" alt="dspy-typesafeify" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/typesafeainate/dspy-typesafeify">dspy-typesafeify</a></b><br><sub>typesafeainate · GitHub · ⭐ 61 · 2026-09-15</sub><br>Proof-of-concept DSPy fork with a @typesafeify decorator that routes a Signature's pure-decision outputs to Jev through a hybrid plan while application code keeps calling dspy.Predict as before.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/symfony/ai/tree/main/src/platform/src/Bridge/TypeSafe"><img src="https://opengraph.githubassets.com/1/symfony/ai" alt="Symfony AI TypeSafe bridge" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/symfony/ai/tree/main/src/platform/src/Bridge/TypeSafe">Symfony AI TypeSafe bridge</a></b><br><sub>symfony · GitHub · ⭐ 1.2k repo · 2025-04-17</sub><br>TypeSafe bridge for Symfony AI's Platform component, exposing the Jev model with Question, Answer and Evaluation types so PHP apps can make System One decisions.<br><sub>Also: <a href="https://ai.symfony.com/">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/laravel/ai/blob/1.x/src/Gateway/TypeSafeGateway.php"><img src="https://pbs.twimg.com/media/HScwRSHXcAAmOGT.jpg" alt="Laravel AI TypeSafe provider" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/laravel/ai/blob/1.x/src/Gateway/TypeSafeGateway.php">Laravel AI TypeSafe provider</a></b><br><sub>laravel · GitHub · ⭐ 1.2k repo · 2026-09-17</sub><br>TypeSafe gateway added to the Laravel AI SDK, giving Laravel apps typed classification backed by Jev's /systemone endpoint, with fake responses for testing.<br><sub>Also: <a href="https://x.com/taylorotwell/status/2100700952923713641">demo</a> · <a href="https://github.com/laravel/ai">repo</a> · <a href="https://github.com/laravel/ai/pull/1010">pr</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/caudena/beam_weaver"><img src="https://raw.githubusercontent.com/caudena/beam_weaver/master/docs/assets/weavescope-tracing.png" alt="BeamWeaver" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/caudena/beam_weaver">BeamWeaver</a></b><br><sub>caudena · GitHub · ⭐ 54 · 2026-06-12</sub><br>Elixir-native take on LangChain, LangGraph and Deep Agents that adds TypeSafe Jev decision models for Choice, Score and Noul alongside its chat providers.<br><sub>Also: <a href="https://github.com/caudena/beam_weaver/blob/master/docs/partners/typesafe.md">docs</a> · <a href="https://www.reddit.com/r/elixir/comments/1wmflss/added_jev_support_to_beamweaver/">discussion</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/obie/feelings"><img src="https://opengraph.githubassets.com/1/obie/feelings" alt="feelings" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/obie/feelings">feelings</a></b><br><sub>obie · GitHub · ⭐ 49 · 2026-09-18</sub><br>Ruby gem for probabilistic conditionals such as Feelings(message).like?("genuinely urgent"), with yes/maybe/no branches, label picking via most_like and a YAML registry of descriptions, backed by Jev.<br><sub><b>How it uses Jev:</b> like? is a yes/no question with a calibrated probability, most_like a Choice over labels; runs via OpenRouter or TypeSafe's API.</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/yusukebe/hono-jev-router"><img src="https://hono-jev-router.yusuke.run/og.png" alt="hono-jev-router" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/yusukebe/hono-jev-router">hono-jev-router</a></b><br><sub>yusukebe · GitHub · ⭐ 45 · 2026-09-18</sub><br>Experimental router for the Hono web framework that routes HTTP requests by plain-language descriptions instead of method and path, with Jev scoring which description fits each incoming request.<br><sub>Also: <a href="https://hono-jev-router.yusuke.run">app</a> · <a href="https://hono-jev-router.yusuke.run">app 2</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/getkyo/kyo/blob/main/kyo-ai/shared/src/main/scala/kyo/ai/decider/TypeSafeDecider.scala"><img src="https://raw.githubusercontent.com/getkyo/kyo/main/kyo.png" alt="Kyo TypeSafe decider" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/getkyo/kyo/blob/main/kyo-ai/shared/src/main/scala/kyo/ai/decider/TypeSafeDecider.scala">Kyo TypeSafe decider</a></b><br><sub>getkyo · GitHub · ⭐ 812 repo · 2022-03-08</sub><br>Kyo, a Scala 3 toolkit, adds a TypeSafe decider backend for its AI module that answers every System One question kind with calibrated probabilities in one request.<br><sub>Also: <a href="https://getkyo.io">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/vercel-labs/ai-cli/blob/main/packages/ai-cli/src/commands/evaluate.ts"><img src="https://opengraph.githubassets.com/1/vercel-labs/ai-cli" alt="ai-cli evaluate" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/vercel-labs/ai-cli/blob/main/packages/ai-cli/src/commands/evaluate.ts">ai-cli evaluate</a></b><br><sub>vercel-labs · GitHub · ⭐ 810 repo · 2025-07-28</sub><br>Evaluate command in the ai-cli terminal tool that sends a state and typed questions from flags, files or stdin to an AI Gateway evaluation model such as Jev and prints the typed answers.<br><sub>Also: <a href="https://github.com/vercel-labs/ai-cli">repo</a> · <a href="https://ai-cli.dev">website</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/DevMortimer/pi-typesafe"><img src="https://raw.githubusercontent.com/DevMortimer/pi-typesafe/main/docs/preview.png" alt="pi-typesafe" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/DevMortimer/pi-typesafe">pi-typesafe</a></b><br><sub>DevMortimer · GitHub · ⭐ 40 · 2026-09-16</sub><br>Pi extension that adds a batched typesafe_evaluate tool for the agent, terminal playground commands and a typed client API so other extensions such as pi-warden share one key and usage record.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/OpenRouterTeam/ai-sdk-provider/tree/main/src/evaluation"><img src="https://raw.githubusercontent.com/OpenRouterTeam/ai-sdk-provider/main/assets/banner.png" alt="OpenRouter AI SDK evaluation" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/OpenRouterTeam/ai-sdk-provider/tree/main/src/evaluation">OpenRouter AI SDK evaluation</a></b><br><sub>OpenRouterTeam · GitHub · ⭐ 686 repo · 2024-07-18</sub><br>OpenRouter's Vercel AI SDK provider adds an evaluation model that speaks the Decisions API, so AI SDK's evaluate can call Jev through OpenRouter.<br><sub>Also: <a href="https://www.npmjs.com/package/@openrouter/ai-sdk-provider">npm</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/langgenius/dify-official-plugins/tree/main/models/typesafe_ai"><img src="https://opengraph.githubassets.com/1/langgenius/dify-official-plugins" alt="Dify TypeSafe AI plugin" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/langgenius/dify-official-plugins/tree/main/models/typesafe_ai">Dify TypeSafe AI plugin</a></b><br><sub>langgenius · GitHub · ⭐ 635 repo · 2024-12-18</sub><br>Official Dify plugin that adds TypeSafe AI as a model provider, letting a Dify Question Classifier node route categories through Jev while branches stay unchanged.<br><sub><b>How it uses Jev:</b> Exposes jev-1.13.0 to the classifier node over a constrained six-message text template, returning category_id and category_name.</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/narumiruna/pi-extensions/tree/main/packages/pi-typesafe"><img src="https://opengraph.githubassets.com/1/narumiruna/pi-extensions" alt="pi-typesafe" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/narumiruna/pi-extensions/tree/main/packages/pi-typesafe">pi-typesafe</a></b><br><sub>narumiruna · GitHub · ⭐ 599 repo · 2026-05-07</sub><br>Pi Coding Agent extension that gives Pi a typesafe_question tool for narrow typed decisions through TypeSafe's Jev API, with an opt-in OpenRouter fallback.<br><sub><b>How it uses Jev:</b> Multiple Noul, Choice and Score questions per state in one call, validated before answers reach the model; bundles a typesafe-ai skill.</sub><br><sub>Also: <a href="https://www.npmjs.com/package/@narumitw/pi-typesafe">npm</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/agentjido/req_llm/blob/main/lib/req_llm/providers/typesafe.ex"><img src="https://opengraph.githubassets.com/1/agentjido/req_llm" alt="ReqLLM TypeSafe provider" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/agentjido/req_llm/blob/main/lib/req_llm/providers/typesafe.ex">ReqLLM TypeSafe provider</a></b><br><sub>agentjido · GitHub · ⭐ 581 repo · 2026-09-17</sub><br>TypeSafe provider for ReqLLM, the Elixir LLM library, that calls Jev through a separate evaluate interface, normalizes answers and keeps the raw provider response.<br><sub>Also: <a href="https://github.com/agentjido/req_llm">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/dxos/dxos/tree/main/packages/experimental/ai-typesafe"><img src="https://raw.githubusercontent.com/dxos/dxos/main/assets/images/github-repo-banner.png" alt="@dxos/ai-typesafe" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/dxos/dxos/tree/main/packages/experimental/ai-typesafe">@dxos/ai-typesafe</a></b><br><sub>dxos · GitHub · ⭐ 522 repo · 2021-04-07</sub><br>Experimental Effect client in the DXOS monorepo for TypeSafe's System One model, where a schema is both the request and response and each struct field compiles to one Jev question.<br><sub><b>How it uses Jev:</b> DecisionModel service mirroring Effect's LanguageModel; all fields ride a single call and decode back to the declared type.</sub><br><sub>Also: <a href="https://dxos.org">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"></td>
<td valign="top"><b><a href="https://liteflow.cc/pages/agent-jev-switch/">liteflow-agent-jev</a></b><br><sub>LiteFlow · Docs · ⭐ 24 · 2026-09-20</sub><br>LiteFlow rule-engine module (from 2.16.2, JDK 17+) whose JevSwitchComponent lets Jev pick a SWITCH branch from candidate component IDs, falling to DEFAULT on low confidence; the docs include a customer-service routing demo.<br><sub>Also: <a href="https://github.com/bryan31/liteflow-homepage">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/lnyo-cly/ai4j/tree/main/ai4j/src/main/java/io/github/lnyocly/ai4j/systemone"><img src="https://opengraph.githubassets.com/1/lnyo-cly/ai4j" alt="ai4j System One" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/lnyo-cly/ai4j/tree/main/ai4j/src/main/java/io/github/lnyocly/ai4j/systemone">ai4j System One</a></b><br><sub>lnyo-cly · GitHub · ⭐ 429 repo · 2024-08-17</sub><br>Adds System One support to ai4j, a Java 8+ agentic SDK, so JVM apps can call TypeSafe's Jev for typed decisions alongside its unified LLM, tool-calling and RAG features.<br><sub>Also: <a href="https://lnyo-cly.github.io/ai4j/">docs</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/langchain-ai/docs/blob/main/src/oss/python/integrations/providers/typesafe.mdx"><img src="https://opengraph.githubassets.com/1/langchain-ai/docs" alt="LangChain TypeSafe integration" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/langchain-ai/docs/blob/main/src/oss/python/integrations/providers/typesafe.mdx">LangChain TypeSafe integration</a></b><br><sub>langchain-ai · Docs · ⭐ 418 repo · 2025-05-15</sub><br>LangChain's docs for the TypeSafe integration, where TypeSafeClassifier exposes Jev decisions as a Runnable you can invoke, batch or compose, including inside create_agent middleware.<br><sub>Also: <a href="https://docs.langchain.com">docs</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/lukerramsden/status/2101474124292047201"><img src="https://pbs.twimg.com/media/HSnvKhjboAAteyi.jpg?name=orig" alt="system-one" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/lukerramsden/status/2101474124292047201">system-one</a></b><br><sub>lukerramsden · X · ♥ 10 · 2026-09-20</sub><br>Generic TypeScript library for System 1 typed-decision models that works with Jev, Cloudflare AI Gateway and Laya, with Promise and Effect-native clients.<br><sub>Also: <a href="https://github.com/lukeramsden/system-one">repo</a> · <a href="https://www.npmjs.com/package/system-one">npm</a> · <a href="https://github.com/lukeramsden/system-one">project</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Nasrallah-AL/jev-cli"><img src="https://jevcli.vectorz.app/og.png" alt="jev-cli (jevctl)" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Nasrallah-AL/jev-cli">jev-cli (jevctl)</a></b><br><sub>Nasrallah-AL · GitHub · ⭐ 18 · 2026-09-18</sub><br>TypeScript CLI installed as jevctl that turns Jev judgments into pipeable, exit-code-gated commands: verify claims, screen for prompt injection, classify, extract, match, route, rerank and compact transcripts.<br><sub>Also: <a href="https://jevcli.vectorz.app/">app</a> · <a href="https://jevcli.vectorz.app">app 2</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/kieranklaassen/ruby_llm-typesafe"><img src="https://opengraph.githubassets.com/1/kieranklaassen/ruby_llm-typesafe" alt="ruby_llm-typesafe" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/kieranklaassen/ruby_llm-typesafe">ruby_llm-typesafe</a></b><br><sub>kieranklaassen · GitHub · ⭐ 18 · 2026-09-16</sub><br>RubyLLM 2 provider that exposes Jev through RubyLLM's structured-output API, with a Schema builder for Noul, Choice, and Score questions.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Ray-Hughes/jevalyn"><img src="https://external-preview.redd.it/JABo279iPcc_xYA1_ytsE0l8wg3ThqOJG7hwAAMXtb0.png?auto=webp&amp;s=0ac9aef2698ab0c8b844460c07b5ab091e5e73f2" alt="Jevalyn" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Ray-Hughes/jevalyn">Jevalyn</a></b><br><sub>Ray-Hughes · GitHub · ⭐ 17 · 2026-09-20</sub><br>Rails-native wrapper that puts typed, calibrated Jev decisions into app control flow, with guardrails, a router, and testing helpers.<br><sub>Also: <a href="https://www.reddit.com/r/rails/comments/1wl4psz/new_gem_wrapping_jev/">demo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/cognesy/instructor-php/tree/main/packages/polyglot/src/Decision/Drivers/TypeSafe"><img src="https://raw.githubusercontent.com/cognesy/instructor-php/main/docs/images/concept.png" alt="Instructor PHP TypeSafe driver" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/cognesy/instructor-php/tree/main/packages/polyglot/src/Decision/Drivers/TypeSafe">Instructor PHP TypeSafe driver</a></b><br><sub>cognesy · GitHub · ⭐ 327 repo · 2026-09-17</sub><br>TypeSafe decision driver in Polyglot, the unified LLM API of Instructor for PHP, that turns application state and typed questions into Jev requests and maps answers to PHP decision objects.<br><sub>Also: <a href="https://github.com/cognesy/instructor-php">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/utk2103/jev-studio"><img src="https://pbs.twimg.com/media/HSu0pXwbwAAGhJp.jpg?name=orig" alt="jev-studio" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/utk2103/jev-studio">jev-studio</a></b><br><sub>utk2103 · GitHub · ⭐ 15 · 2026-09-19</sub><br>Python kit with a jev CLI for verify, screen, classify, extract, route, rerank and compact judgments over piped text, plus an MCP server for Choice, Noul and Score and slash commands for the cookbooks.<br><sub>Also: <a href="https://x.com/utk2103/status/2101972303387209821">demo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/saiashirwad/effect-questions"><img src="https://opengraph.githubassets.com/1/saiashirwad/effect-questions" alt="effect-questions" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/saiashirwad/effect-questions">effect-questions</a></b><br><sub>saiashirwad · GitHub · ⭐ 14 · 2026-09-16</sub><br>Effect library that turns semantic judgment into typed Effect operations such as is, choose, rank and branch, failing with UncertainDecision when the model is not confident enough.<br><sub><b>How it uses Jev:</b> Jev is the first QuestionModel provider; Decision adds confidence gates, expected loss and dispatch over evidence.</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/BoundaryML/feelings"><img src="https://opengraph.githubassets.com/1/BoundaryML/feelings" alt="feelings" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/BoundaryML/feelings">feelings</a></b><br><sub>BoundaryML · GitHub · ⭐ 13 · 2026-09-19</sub><br>About 20 lines of BAML that add .feels(), .how() and .matches() methods to any value, turning Jev probabilities into typed AI if-statements inside ordinary BAML code, with an LLM doing any writing.<br><sub>Also: <a href="https://boundaryml.com/blog/typesafe-ai-jev">article</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/tumf/jev-cli"><img src="https://raw.githubusercontent.com/tumf/jev-cli/main/assets/jev-cli-thumbnail.png" alt="jev-cli" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/tumf/jev-cli">jev-cli</a></b><br><sub>tumf · GitHub · ⭐ 12 · 2026-09-17</sub><br>Small dependency-free Python CLI and stdio MCP server that sends text or JSON state from files or stdin to Jev with noul, choice or score questions and prints machine-readable answers for scripts and MCP hosts.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/southpolesteve/probably"><img src="https://opengraph.githubassets.com/1/southpolesteve/probably" alt="Probably" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/southpolesteve/probably">Probably</a></b><br><sub>southpolesteve · GitHub · ⭐ 9 · 2026-09-19</sub><br>Small experimental programming language for LLM workflows where Jev supplies the judgments and probabilities behind if statements and a text model writes prose, with a real parser, interpreter, CLI and playground.<br><sub>Also: <a href="https://probably-lang.southpolesteve.workers.dev">app</a> · <a href="https://probably-lang.southpolesteve.workers.dev">app 2</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/shaharia-lab/jev-cli"><img src="https://raw.githubusercontent.com/shaharia-lab/jev-cli/main/assets/banner.png" alt="jev" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/shaharia-lab/jev-cli">jev</a></b><br><sub>shaharia-lab · GitHub · ⭐ 11 · 2026-09-19</sub><br>Rust command-line tool that asks yes/no, multiple-choice and rubric questions about any text and returns calibrated probabilities as exit codes for shells and CI, JSON for scripts, or MCP tools for agents.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/ekizito96/Turn"><img src="https://opengraph.githubassets.com/1/ekizito96/Turn" alt="Turn" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/ekizito96/Turn">Turn</a></b><br><sub>ekizito96 · GitHub · ⭐ 11 · 2026-02-17</sub><br>Compiled language and runtime for AI agents where decide(state, questions) is a durable effect, with a bundled TypeSafe System One driver that runs Choice, Score and Noul workflows on Jev.<br><sub><b>How it uses Jev:</b> Provider-neutral decide() with a mock driver for local runs; programs branch on answer confidence, for example sending tickets below 0.8 to a reviewer.</sub><br><sub>Also: <a href="https://github.com/ekizito96/Turn/tree/main/providers/turn-provider-typesafe">code</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/doeixd/discern"><img src="https://raw.githubusercontent.com/doeixd/discern/main/docs/assets/discern-explainer-silent.gif" alt="Discern" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/doeixd/discern">Discern</a></b><br><sub>doeixd · GitHub · ⭐ 10 · 2026-09-21</sub><br>TypeScript library of uncertainty-aware semantic pattern matching, policies and routable procedures over Effect's Decision and DecisionModel, where a maybe result is an explicit branch, with Jev as one provider.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/vercel-labs/ai-python/blob/main/examples/models/gateway/evaluation.py"><img src="https://opengraph.githubassets.com/1/vercel-labs/ai-python" alt="AI SDK for Python evaluate" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/vercel-labs/ai-python/blob/main/examples/models/gateway/evaluation.py">AI SDK for Python evaluate</a></b><br><sub>vercel-labs · GitHub · ⭐ 184 repo · 2026-01-16</sub><br>Experimental evaluate operation in Vercel's public-beta AI SDK for Python that asks typed Choice, Score and Boolean questions of Jev through AI Gateway, shown in a runnable example.<br><sub>Also: <a href="https://github.com/vercel-labs/ai-python">repo</a> · <a href="https://ai-python.dev">website</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/matthewp/flue-jev-demo"><img src="https://opengraph.githubassets.com/1/matthewp/flue-jev-demo" alt="Flue + Jev" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/matthewp/flue-jev-demo">Flue + Jev</a></b><br><sub>matthewp · GitHub · ⭐ 9 · 2026-09-18</sub><br>Cloudflare Worker example where a Flue support agent gets a route_with_jev tool built from a typed question map, calling Jev through the Worker AI binding and AI Gateway with no app API keys.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/aaazzam/jev"><img src="https://opengraph.githubassets.com/1/aaazzam/jev" alt="jev (aaazzam)" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/aaazzam/jev">jev (aaazzam)</a></b><br><sub>aaazzam · GitHub · ⭐ 9 · 2026-09-18</sub><br>Python decorator, @jev.fn, that compiles a function's parameters, docstring, and Pydantic return annotation into a Jev state and typed questions, and returns a validated instance when called.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/AntonioCoppe/jev-harness"><img src="https://raw.githubusercontent.com/AntonioCoppe/jev-harness/main/docs/assets/marketing/proof/terminal/claude-cli.png" alt="jev-harness" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/AntonioCoppe/jev-harness">jev-harness</a></b><br><sub>AntonioCoppe · GitHub · ⭐ 9 · 2026-09-18</sub><br>TypeScript library that turns Jev answers into shippable actions with a policy map, confidence gate, shadow mode, recipes and an offline eval CLI; a row-filter job took 1.3 s versus 48.9 s with Claude CLI.<br><sub>Also: <a href="https://x.com/Antoniocoppe/status/2100954520356327577">demo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/hijaidev/status/2101679778801893685"><img src="https://pbs.twimg.com/amplify_video_thumb/2101679740520390656/img/McXbM1E9CZgvK-MZ.jpg" alt="Jev CLI" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/hijaidev/status/2101679778801893685">Jev CLI</a></b><br><sub>hijaidev · X · ♥ 4 · 2026-09-20</sub><br>Command-line tool that exposes Jev as verify, screen, classify, extract, match, route, rerank and ask commands, returning verdicts with probabilities for scripts and agents.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Michaelliv/runline/tree/main/packages/runline-plugins/typesafe"><img src="https://opengraph.githubassets.com/1/Michaelliv/runline" alt="Runline TypeSafe plugin" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Michaelliv/runline/tree/main/packages/runline-plugins/typesafe">Runline TypeSafe plugin</a></b><br><sub>Michaelliv · GitHub · ⭐ 163 repo · 2026-09-17</sub><br>TypeSafe plugin for Runline, a code-mode runtime for agents, exposing evaluate, choice, score and noul as callable actions from agent JavaScript in its QuickJS sandbox.<br><sub>Also: <a href="https://github.com/Michaelliv/runline">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Towow-ai/jpp"><img src="https://raw.githubusercontent.com/Towow-ai/jpp/main/assets/social-card.svg" alt="J++" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Towow-ai/jpp">J++</a></b><br><sub>Towow-ai · GitHub · ⭐ 8 · 2026-09-20</sub><br>Experimental programming language with a Rust runtime where semantic questions and decision methods are composable values, executed through one shared kernel with Jev as a supported provider.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Qew7/jev-feels"><img src="https://external-preview.redd.it/xMmQtp7gSWMuhtgjLSGOmgCl1tjR5re0ilOP9mc2miM.png?auto=webp&amp;s=88bc162d3c91139ece8539bc8801af8fe9b1a44b" alt="jev-feels" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Qew7/jev-feels">jev-feels</a></b><br><sub>Qew7 · GitHub · ⭐ 8 · 2026-09-20</sub><br>Ruby gem that turns Jev judgments into ordinary Ruby: feels?, decide and score on model fields, Rails validations such as validates_feeling, and pattern matching.<br><sub>Also: <a href="https://www.reddit.com/r/ruby/comments/1wm8u7z/i_made_a_jev_gem_with_an_api_that_feels_like_it/">demo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/i-priyanshuverma/laravel-jev"><img src="https://pbs.twimg.com/media/HSrapOOawAAdjuM.jpg?name=orig" alt="Laravel Jev" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/i-priyanshuverma/laravel-jev">Laravel Jev</a></b><br><sub>i-priyanshuverma · GitHub · ⭐ 8 · 2026-09-20</sub><br>PHP package for Laravel apps with one-line <code>Jev::is</code>, <code>choose</code> and <code>score</code> calls, batched questions, form-request validation rules, response caching and a <code>Jev::fake()</code> testing helper.<br><sub>Also: <a href="https://x.com/ipriyanshuverma/status/2101736982745620878">demo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Kevthetech143/super-jev"><img src="https://opengraph.githubassets.com/1/Kevthetech143/super-jev" alt="super-jev" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Kevthetech143/super-jev">super-jev</a></b><br><sub>Kevthetech143 · GitHub · ⭐ 8 · 2026-09-17</sub><br>Domain-independent TypeScript harness that links evidence, Jev judgments, permitted tool actions and verified outcomes, with pluggable data sources and tools, argument checks and local JSONL traces.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/miaotouy/aio-hub/blob/dev/packages/llm-core/src/providers/typesafe-system-one.ts"><img src="https://raw.githubusercontent.com/miaotouy/aio-hub/dev/docs/public/assets/产品概念图-1.jpg" alt="AIO Hub System One channel" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/miaotouy/aio-hub/blob/dev/packages/llm-core/src/providers/typesafe-system-one.ts">AIO Hub System One channel</a></b><br><sub>miaotouy · GitHub · ⭐ 144 repo · 2025-10-28</sub><br>Local-first desktop and mobile AI hub that adds TypeSafe System One as a dedicated decision channel, with Jev models listed only where a decision operation is needed.<br><sub>Also: <a href="http://aiohub-app.com">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/mattt/AnyDecisionModel"><img src="https://opengraph.githubassets.com/1/mattt/AnyDecisionModel" alt="AnyDecisionModel" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/mattt/AnyDecisionModel">AnyDecisionModel</a></b><br><sub>mattt · GitHub · ⭐ 7 · 2026-09-21</sub><br>Swift package for typed decisions (probabilities, enum-backed choices, ordinal scores) in the Foundation Models session style, backed either by Jev's System One API or a local MLX model on Apple silicon.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Kiln-AI/jev_jsonschema"><img src="https://opengraph.githubassets.com/1/Kiln-AI/jev_jsonschema" alt="jev_jsonschema" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Kiln-AI/jev_jsonschema">jev_jsonschema</a></b><br><sub>Kiln-AI · GitHub · ⭐ 7 · 2026-09-19</sub><br>Python library that converts a JSON Schema into Jev questions and returns JSON that validates against the original schema, with sync and async clients.<br><sub>Also: <a href="https://news.ycombinator.com/item?id=49769277">demo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/MoeclubM/PlayJev"><img src="https://raw.githubusercontent.com/MoeclubM/PlayJev/main/docs/images/screenshot-desktop.png" alt="PlayJev" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/MoeclubM/PlayJev">PlayJev</a></b><br><sub>MoeclubM · GitHub · ⭐ 7 · 2026-09-19</sub><br>Visual IDE for composing Jev requests, with a state editor, a question builder, JSON preview and validation, answers rendered as visual cards, and an LLM that drafts a whole request from one sentence.<br><sub>Also: <a href="https://playjev.telecom.moe">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/jomatsu/zod-jev"><img src="https://opengraph.githubassets.com/1/jomatsu/zod-jev" alt="zod-jev" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/jomatsu/zod-jev">zod-jev</a></b><br><sub>jomatsu · GitHub · ⭐ 7 · 2026-09-17</sub><br>Adds semantic checks to Zod 4 schemas, such as whether a body contains personal data or a price is plausible, while shape rules stay in Zod and results come back as ordinary Zod issues.<br><sub><b>How it uses Jev:</b> All semantic rules in one parseAsync become Noul questions in a single request; thresholds map probabilities to issues.</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/juspay/neurolink/blob/release/src/lib/providers/typesafe.ts"><img src="https://repository-images.githubusercontent.com/993805781/24ad8594-ddb9-4c8d-a4f9-15c3f72f9390" alt="NeuroLink decide" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/juspay/neurolink/blob/release/src/lib/providers/typesafe.ts">NeuroLink decide</a></b><br><sub>juspay · GitHub · ⭐ 137 repo · 2025-05-31</sub><br>Jev provider in Juspay's NeuroLink TypeScript SDK that adds decide, returning typed boolean, choice and score judgments, as a third inference type beside generate and stream, also used internally for routing and compaction.<br><sub>Also: <a href="https://github.com/juspay/neurolink">repo</a> · <a href="https://neurolink.ink">website</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"></td>
<td valign="top"><b><a href="https://pypi.org/project/jev/">jev</a></b><br><sub>Package · ⬇ 640 · 2026-09-18</sub><br>Python decorator that compiles a function's signature, docstring and Pydantic return type into a Jev request, mapping bool, Literal/Enum and bounded number fields to Noul, Choice and Score.</td>
</tr>
<tr>
<td width="260" valign="top"></td>
<td valign="top"><b><a href="https://www.npmjs.com/package/typesafe-jev-cli">typesafe-jev-cli</a></b><br><sub>lbflow · Package · ⬇ 616 · 2026-09-20</sub><br>Dependency-free Node.js CLI that sends Choice, Noul and Score evaluations to Jev through OpenRouter's decisions endpoint, including batch evaluation of many text files.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/danieljvdm/effect-agent/tree/main/packages/ai-decision"><img src="https://opengraph.githubassets.com/1/danieljvdm/effect-agent" alt="Effect Agent AutoModel" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/danieljvdm/effect-agent/tree/main/packages/ai-decision">Effect Agent AutoModel</a></b><br><sub>danieljvdm · GitHub · ⭐ 121 repo · 2026-09-17</sub><br>AutoModel package for Effect Agent that picks a native language model once per thread from an app-approved catalog using a DecisionModel such as TypeSafeDecisionModel with jev-latest.<br><sub>Also: <a href="https://github.com/danieljvdm/effect-agent">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/obie/decide"><img src="https://opengraph.githubassets.com/1/obie/decide" alt="decide" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/obie/decide">decide</a></b><br><sub>obie · GitHub · ⭐ 6 · 2026-09-18</sub><br>Backend-agnostic Ruby layer that turns decision-model answers into named policy verdicts with explicit fail-open or fail-closed handling, with Jev via OpenRouter as the first answer source.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/terryds/jevplayground"><img src="https://opengraph.githubassets.com/1/terryds/jevplayground" alt="Jev Playground" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/terryds/jevplayground">Jev Playground</a></b><br><sub>terryds · GitHub · ⭐ 1 · 2026-09-19</sub><br>Browser-only playground for Jev over Vercel AI Gateway where you build boolean, choice and score questions against text or JSON state and see verdicts, probability bars, latency, tokens and cost.<br><sub>Also: <a href="https://jevplayground.terrydjony.com">app</a> · <a href="https://jevplayground.terrydjony.com/">app 2</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/SamSaffron/term-llm/tree/main/internal/typesafe"><img src="https://opengraph.githubassets.com/1/SamSaffron/term-llm" alt="term-llm classify" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/SamSaffron/term-llm/tree/main/internal/typesafe">term-llm classify</a></b><br><sub>SamSaffron · GitHub · ⭐ 116 repo · 2025-12-31</sub><br>Terminal AI runtime with a classify command backed by TypeSafe System One for intent routing, parallel safety checks and scoring structured state from the shell.<br><sub>Also: <a href="https://term-llm.com/guides/classify/">docs</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/hndrr/ComfyUI-Jev"><img src="https://opengraph.githubassets.com/1/hndrr/ComfyUI-Jev" alt="ComfyUI-Jev" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/hndrr/ComfyUI-Jev">ComfyUI-Jev</a></b><br><sub>hndrr · GitHub · ⭐ 5 · 2026-09-19</sub><br>Work-in-progress ComfyUI custom nodes that select candidates, evaluate conditions, score text, extract numbers, or pick local skills with Jev and pass the results to other nodes.<br><sub>Also: <a href="https://registry.comfy.org/ja/nodes/comfyui-jev">registry</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/docxology/daf-jev"><img src="https://opengraph.githubassets.com/1/docxology/daf-jev" alt="daf-jev" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/docxology/daf-jev">daf-jev</a></b><br><sub>docxology · GitHub · ⭐ 5 · 2026-09-17</sub><br>Composable Python toolkit for the Jev API with question builders, sync and async clients with retries, confidence gates, a batch evaluator, calibration tools, a CLI and an MCP server.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Mawfyy/jevflow"><img src="https://opengraph.githubassets.com/1/Mawfyy/jevflow" alt="JevFlow" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Mawfyy/jevflow">JevFlow</a></b><br><sub>Mawfyy · GitHub · ⭐ 5 · 2026-09-20</sub><br>TypeScript backend library for defining typed noul, score and choice judgments with explicit thresholds and deterministic policy kept separate from the model, plus explainable workflows; Jev is the default provider.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/alexwestco/llm-to-jev"><img src="https://opengraph.githubassets.com/1/alexwestco/llm-to-jev" alt="LLMtoJev" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/alexwestco/llm-to-jev">LLMtoJev</a></b><br><sub>alexwestco · GitHub · ⭐ 5 · 2026-09-19</sub><br>Converter that finds bounded decisions inside prompts written for GPT, Claude or Gemini and proposes Jev Choice, Score and Noul questions, separating them from generative work that must stay with an LLM.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/topce/pizx"><img src="https://raw.githubusercontent.com/topce/pizx/main/github-social-banner.png" alt="pizx" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/topce/pizx">pizx</a></b><br><sub>topce · GitHub · ⭐ 5 · 2026-06-08</sub><br>Fork of Google's zx for AI shell scripting with Pi agents that adds TypeSafe choice, score and noul as built-in letters, with JSONL run traces and a local result cache.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/nitoba/questions"><img src="https://opengraph.githubassets.com/1/nitoba/questions" alt="Questions" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/nitoba/questions">Questions</a></b><br><sub>nitoba · GitHub · ⭐ 5 · 2026-09-17</sub><br>TypeScript library for typed semantic decisions defined with Zod 4 schemas or native question batches, running on Jev by default with confidence gates, deadlines, retries, replay, and observability.<br><sub><b>How it uses Jev:</b> Uses TypeSafe or Vercel evaluation for Jev, with an optional AI SDK adapter for generative models.</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/3clyp50/a0-typesafe-ai"><img src="https://raw.githubusercontent.com/3clyp50/a0-typesafe-ai/main/docs/results.png" alt="TypeSafe AI for Agent Zero" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/3clyp50/a0-typesafe-ai">TypeSafe AI for Agent Zero</a></b><br><sub>3clyp50 · GitHub · ⭐ 5 · 2026-09-17</sub><br>Agent Zero plugin whose typesafe_query tool combines Choice, Noul and Score questions over the same evidence and renders probability cards in chat; bundles the official TypeSafe agent skill.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/TypeSafeAI/typesafe-ui"><img src="https://opengraph.githubassets.com/1/TypeSafeAI/typesafe-ui" alt="TypeSafe UI" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/TypeSafeAI/typesafe-ui">TypeSafe UI</a></b><br><sub>TypeSafeAI · GitHub · ⭐ 4 · 2026-09-17</sub><br>Community shadcn-style React components and interface blocks for TypeSafe projects, built on Base UI and Tailwind v4, with a Next.js component browser, source previews and an interactive Lab.<br><sub>Also: <a href="https://ui.jev.works">app</a> · <a href="https://typesafe-ui.vercel.app">app 2</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/deepclause/deepclause-sdk/blob/main/src/judge/jev.ts"><img src="https://raw.githubusercontent.com/deepclause/deepclause-sdk/main/docs/DeepClause_AI_Logic_Framework_Overview.png" alt="DeepClause Jev judge backend" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/deepclause/deepclause-sdk/blob/main/src/judge/jev.ts">DeepClause Jev judge backend</a></b><br><sub>deepclause · GitHub · ⭐ 64 repo · 2026-01-29</sub><br>SDK that compiles Markdown specs into executable logic programs, adding generic judgment primitives with interchangeable LLM, Jev and mock backends.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/betalyra/effect-uai/tree/main/packages/providers/typesafe-ai"><img src="https://raw.githubusercontent.com/betalyra/effect-uai/main/webpage/src/assets/effect-uai-logo-bg.png" alt="@effect-uai/typesafe-ai" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/betalyra/effect-uai/tree/main/packages/providers/typesafe-ai">@effect-uai/typesafe-ai</a></b><br><sub>betalyra · GitHub · ⭐ 63 repo · 2026-04-26</sub><br>Effect-based building blocks for AI agents with a TypeSafe Jev DecisionModel provider for typed classify, rate and probability questions answered in one call.<br><sub>Also: <a href="https://effect-uai.betalyra.com">docs</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/soderlind/ai-provider-for-jev"><img src="https://repository-images.githubusercontent.com/1375771750/d0ec3827-1a39-44d6-83e5-85a31e8a15eb" alt="AI Provider for Jev" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/soderlind/ai-provider-for-jev">AI Provider for Jev</a></b><br><sub>soderlind · GitHub · ⭐ 3 · 2026-09-18</sub><br>WordPress plugin that connects a site to Jev, with a settings page, PHP helpers and REST endpoints for Choice, Score and Noul questions.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/noetion/dsh-jev"><img src="https://opengraph.githubassets.com/1/noetion/dsh-jev" alt="dsh-jev" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/noetion/dsh-jev">dsh-jev</a></b><br><sub>noetion · GitHub · ⭐ 3 · 2026-09-17</sub><br>DeepSeek Harness plugin that registers a jev_ask tool and a bundled skill so a DSH agent can send mixed noul, choice and score questions about one state to Jev.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/collapseindex/jev-builder"><img src="https://raw.githubusercontent.com/collapseindex/jev-builder/main/docs/preview.png" alt="jev-builder" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/collapseindex/jev-builder">jev-builder</a></b><br><sub>collapseindex · GitHub · ⭐ 3 · 2026-09-19</sub><br>Static browser form for writing Jev requests from templates or from scratch without hand-escaping JSON, then running them several times to see whether the answer holds.<br><sub>Also: <a href="https://collapseindex.github.io/jev-builder/">app</a> · <a href="https://collapseindex.github.io/jev-builder">app 2</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/reachjalil/jev-tree"><img src="https://huggingface.co/datasets/reachjalil/jev-tree-choice-cap/resolve/main/charts/accuracy.png" alt="jev-tree" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/reachjalil/jev-tree">jev-tree</a></b><br><sub>reachjalil · GitHub · ⭐ 3 · 2026-09-18</sub><br>TypeScript library that classifies into catalogs larger than Jev's 255-option Choice limit by walking a taxonomy with one Choice per level, auto-bucketing oversized sibling lists.<br><sub>Also: <a href="https://reachjalil.github.io/jev-tree/">app</a> · <a href="https://reachjalil.github.io/jev-tree">app 2</a> · <a href="https://huggingface.co/datasets/reachjalil/jev-tree-choice-cap">model</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/ariel-frischer/jevkit"><img src="https://repository-images.githubusercontent.com/1376435020/cf19659b-38fb-4ba6-ba01-8d77363a7bad" alt="jevkit" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/ariel-frischer/jevkit">jevkit</a></b><br><sub>ariel-frischer · GitHub · ⭐ 3 · 2026-09-18</sub><br>Rust CLI for Jev that takes Choice, Score and Noul question sets in terse YAML or JSON, lints them offline before any paid call, and prints parsed answers as JSON, with an agent skill for coding agents.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/mateonunez/jod"><img src="https://opengraph.githubassets.com/1/mateonunez/jod" alt="jod" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/mateonunez/jod">jod</a></b><br><sub>mateonunez · GitHub · ⭐ 3 · 2026-09-17</sub><br>TypeScript library that binds a Standard Schema state and a set of questions into one artifact, validates the state locally, then sends all questions in one parallel Jev request and returns typed domain values.<br><sub><b>How it uses Jev:</b> Built on @typesafe-ai/sdk; adds validation, answer projection and fixtures.</sub><br><sub>Also: <a href="https://npmjs.com/package/@mateonunez/jod">npm</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/SEMOSS/Semoss/tree/dev/py/genai_client/typesafe"><img src="https://opengraph.githubassets.com/1/SEMOSS/Semoss" alt="SEMOSS TypeSafe client" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/SEMOSS/Semoss/tree/dev/py/genai_client/typesafe">SEMOSS TypeSafe client</a></b><br><sub>SEMOSS · GitHub · ⭐ 54 repo · 2013-05-30</sub><br>Low-code data and AI application platform that adds a TypeSafe Jev client to its GenAI layer, with a how-to guide for using Jev decisions.<br><sub>Also: <a href="https://github.com/SEMOSS/Semoss/blob/dev/docs/how-to-guides/using_typesafe_jev.md">docs</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/YaoApp/gou/tree/main/connector/typesafe"><img src="https://opengraph.githubassets.com/1/YaoApp/gou" alt="Gou TypeSafe connector" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/YaoApp/gou/tree/main/connector/typesafe">Gou TypeSafe connector</a></b><br><sub>YaoApp · GitHub · ⭐ 51 repo · 2021-08-24</sub><br>Low-code Go app engine framework that adds a TypeSafe connector with a Decide capability for calling Jev from Yao apps.<br><sub>Also: <a href="https://yaoapps.com">docs</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/everruns/everruns/tree/main/integrations/typesafe"><img src="https://raw.githubusercontent.com/everruns/everruns/main/assets/readme/banner.png" alt="everruns-integrations-typesafe" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/everruns/everruns/tree/main/integrations/typesafe">everruns-integrations-typesafe</a></b><br><sub>everruns · GitHub · ⭐ 48 repo · 2025-12-14</sub><br>Rust crate that adds a jev capability to the Everruns durable agent harness: one jev_evaluate tool lets an agent ask typed Noul, Score and Choice questions to verify, rate, route or classify content.<br><sub>Also: <a href="https://github.com/everruns/everruns">repo</a> · <a href="https://crates.io/crates/everruns-integrations-typesafe">crate</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/driftlessaf/go-driftlessaf/tree/main/agents/executor/systemone"><img src="https://opengraph.githubassets.com/1/driftlessaf/go-driftlessaf" alt="DriftlessAF systemone executor" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/driftlessaf/go-driftlessaf/tree/main/agents/executor/systemone">DriftlessAF systemone executor</a></b><br><sub>driftlessaf · GitHub · ⭐ 40 repo · 2026-01-26</sub><br>Go package in Chainguard's DriftlessAF agent framework that calls TypeSafe's System One API with typed Noul, Choice and Score questions, validates every answer and reuses the framework's retries and GenAI metrics.<br><sub>Also: <a href="https://github.com/driftlessaf/go-driftlessaf">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/molis-ai/jev-workbench"><img src="https://raw.githubusercontent.com/molis-ai/jev-workbench/main/docs/images/workbench.png" alt="Jev Workbench" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/molis-ai/jev-workbench">Jev Workbench</a></b><br><sub>molis-ai · GitHub · ⭐ 2 · 2026-09-17</sub><br>Local service for defining, testing and publishing versioned Jev judgment functions in a browser UI, then calling the same pinned version from backends over HTTP and from coding agents over MCP.<br><sub><b>How it uses Jev:</b> Each function encodes a classification or evidence check as Noul, Choice or Score questions; callers get scoped tokens while the vendor key stays local.</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/jtsang4/jev-cli"><img src="https://opengraph.githubassets.com/1/jtsang4/jev-cli" alt="jev-cli" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/jtsang4/jev-cli">jev-cli</a></b><br><sub>jtsang4 · GitHub · ⭐ 2 · 2026-09-17</sub><br>Command-line client for Jev that takes a state and typed questions from files or stdin and prints structured JSON answers, calling TypeSafe directly or through Vercel AI Gateway.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/hamakyo/jev-starter"><img src="https://opengraph.githubassets.com/1/hamakyo/jev-starter" alt="jev-starter" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/hamakyo/jev-starter">jev-starter</a></b><br><sub>hamakyo · GitHub · ⭐ 2 · 2026-09-17</sub><br>Published npm package and GitHub template with TypeScript patterns around the TypeSafe SDK: decision contracts, confidence thresholds, fallbacks, human review, evaluation and RAG examples.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/etweisberg/jev-ui"><img src="https://github.com/user-attachments/assets/ba3b7a4f-b800-49c0-b078-089ca332ff1d" alt="jev-ui" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/etweisberg/jev-ui">jev-ui</a></b><br><sub>etweisberg · GitHub · ⭐ 2 · 2026-09-20</sub><br>React components for Next.js that decide which component to render, how to order a list and whether to show an affordance from Jev judgments, while your code keeps thresholds, fallbacks and actions.<br><sub>Also: <a href="https://docs.jev-ui.dev/">docs</a> · <a href="https://docs.jev-ui.dev">link</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/SoundBlaster/Jev4Mellea"><img src="https://opengraph.githubassets.com/1/SoundBlaster/Jev4Mellea" alt="Jev4Mellea" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/SoundBlaster/Jev4Mellea">Jev4Mellea</a></b><br><sub>SoundBlaster · GitHub · ⭐ 2 · 2026-09-17</sub><br>Unofficial Python adapter that brings Jev checks into Mellea to verify requirements with Noul thresholds, classify with Choice, and score text, while Mellea keeps handling generation and repair.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Butochnikov/laravel-typesafe-jev"><img src="https://opengraph.githubassets.com/1/Butochnikov/laravel-typesafe-jev" alt="Laravel TypeSafe Jev" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Butochnikov/laravel-typesafe-jev">Laravel TypeSafe Jev</a></b><br><sub>Butochnikov · GitHub · ⭐ 2 · 2026-09-17</sub><br>Unofficial Laravel integration for Jev built on a community PHP SDK, adding package discovery, scoped dependency injection, configuration, a facade and a request-recording test fake.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/vibe-with-me-tools/n8n-nodes-jev"><img src="https://raw.githubusercontent.com/vibe-with-me-tools/n8n-nodes-jev/main/docs/images/route-by-choice-workflow.png" alt="n8n-nodes-jev" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/vibe-with-me-tools/n8n-nodes-jev">n8n-nodes-jev</a></b><br><sub>vibe-with-me-tools · GitHub · ⭐ 2 · 2026-09-19</sub><br>Community node for n8n that classifies, routes and scores text with questions you define, returning a probability per answer so unsure items can be sent to a person.<br><sub>Also: <a href="https://www.npmjs.com/package/n8n-nodes-jev">npm</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/n3ndor/n8n-nodes-typesafe-jev"><img src="https://opengraph.githubassets.com/1/n3ndor/n8n-nodes-typesafe-jev" alt="n8n-nodes-typesafe-jev" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/n3ndor/n8n-nodes-typesafe-jev">n8n-nodes-typesafe-jev</a></b><br><sub>n3ndor · GitHub · ⭐ 2 · 2026-09-18</sub><br>Unofficial n8n community node that builds state and several typed questions from workflow items, calls Jev, and appends the calibrated answers for routing, classification, and scoring.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/muvonteam/status/2101175341498941935"><img src="https://muvon.io/blog/octolib-0-39-0-evaluation-models-jev/index.png" alt="octolib 0.39.0" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/muvonteam/status/2101175341498941935">octolib 0.39.0</a></b><br><sub>muvonteam · X · ♥ 2 · 2026-09-19</sub><br>Rust library for 30+ AI providers adds evaluation as a fourth call type next to generate, embed and rerank, backed by Jev directly, through Cloudflare or through OctoHub.<br><sub>Also: <a href="https://github.com/muvon/octolib">repo</a> · <a href="https://muvon.io/blog/octolib-0-39-0-evaluation-models-jev">article</a> · <a href="https://github.com/muvon/octolib">project</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/legacybridge-tech/pi-typesafe-jev"><img src="https://opengraph.githubassets.com/1/legacybridge-tech/pi-typesafe-jev" alt="pi-typesafe-jev" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/legacybridge-tech/pi-typesafe-jev">pi-typesafe-jev</a></b><br><sub>legacybridge-tech · GitHub · ⭐ 2 · 2026-09-17</sub><br>Pi extension that exposes Jev as five narrow tools, for Noul, Choice, Score, multi-question evaluate and questions pinned in local YAML or JSON, while thresholds, weights and actions stay in host code.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/GenieRobot/typesafe-ai-rails"><img src="https://opengraph.githubassets.com/1/GenieRobot/typesafe-ai-rails" alt="typesafe-ai-rails" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/GenieRobot/typesafe-ai-rails">typesafe-ai-rails</a></b><br><sub>GenieRobot · GitHub · ⭐ 2 · 2026-09-16</sub><br>Rails integration built on the community Ruby SDK that adds configuration, persisted usage and cost telemetry, and an opt-in confidence policy for Choice and Score answers.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/phenobarbital/ai-parrot/tree/main/packages/ai-parrot-client-jev"><img src="https://opengraph.githubassets.com/1/phenobarbital/ai-parrot" alt="ai-parrot-client-jev" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/phenobarbital/ai-parrot/tree/main/packages/ai-parrot-client-jev">ai-parrot-client-jev</a></b><br><sub>phenobarbital · GitHub · ⭐ 30 repo · 2024-08-12</sub><br>Jev client package for the AI-Parrot async agent framework that maps System One onto its client interface and turns Pydantic models into questions (bool to Noul, Literal/Enum to Choice, leveled numbers to Score).<br><sub>Also: <a href="https://github.com/phenobarbital/ai-parrot">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/gurenjs/guren/tree/main/examples/agents"><img src="https://opengraph.githubassets.com/1/gurenjs/guren" alt="Guren AI evaluation models" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/gurenjs/guren/tree/main/examples/agents">Guren AI evaluation models</a></b><br><sub>gurenjs · GitHub · ⭐ 29 repo · 2025-11-01</sub><br>Evaluation-model support in the Guren Bun fullstack framework's AI plugin, where Jev via the AI SDK is the default evaluation provider; the agents example triages support tickets through POST /tickets/:id/triage.<br><sub>Also: <a href="https://github.com/gurenjs/guren">repo</a> · <a href="https://guren.dev">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/tale-project/tale/tree/main/configs/platform/system/connectors/jev"><img src="https://opengraph.githubassets.com/1/tale-project/tale" alt="Tale Jev decisions connector" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/tale-project/tale/tree/main/configs/platform/system/connectors/jev">Tale Jev decisions connector</a></b><br><sub>tale-project · GitHub · ⭐ 29 repo · 2025-11-30</sub><br>Workflow connector for Tale, a self-hosted AI agent orchestrator and workspace, that exposes Jev via OpenRouter as a decide action for gating steps such as send, escalate or write on calibrated answers.<br><sub>Also: <a href="https://tale.dev">app</a> · <a href="https://github.com/tale-project/tale">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/SEMOSS/semoss-ui/blob/dev/packages/client/src/components/import/model/jev-model-import.constants.ts"><img src="https://opengraph.githubassets.com/1/SEMOSS/semoss-ui" alt="SEMOSS Jev model engine" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/SEMOSS/semoss-ui/blob/dev/packages/client/src/components/import/model/jev-model-import.constants.ts">SEMOSS Jev model engine</a></b><br><sub>SEMOSS · GitHub · ⭐ 27 repo · 2024-06-20</sub><br>Model-import form in the SEMOSS platform UI that connects Jev by TypeSafe as an evaluation engine for classifying, scoring and evaluating text or structured data, with optional inference-log retention.<br><sub>Also: <a href="https://github.com/SEMOSS/semoss-ui">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Govcraft/emergent/blob/main/skills/emergent/references/primitives.md"><img src="https://raw.githubusercontent.com/Govcraft/emergent/main/docs/images/system-monitor.png" alt="Emergent jev-handler" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Govcraft/emergent/blob/main/skills/emergent/references/primitives.md">Emergent jev-handler</a></b><br><sub>Govcraft · GitHub · ⭐ 23 repo · 2026-01-06</sub><br>Handler primitive for Emergent, an event-driven workflow engine that composes CLI tools, that asks Jev a fixed set of typed questions about every event payload and publishes the calibrated answers downstream.<br><sub>Also: <a href="https://github.com/Govcraft/emergent">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/lm15-dev/lm15-python/blob/main/lm15/providers/typesafe.py"><img src="https://opengraph.githubassets.com/1/lm15-dev/lm15-python" alt="lm15 typesafe provider" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/lm15-dev/lm15-python/blob/main/lm15/providers/typesafe.py">lm15 typesafe provider</a></b><br><sub>lm15-dev · GitHub · ⭐ 23 repo · 2026-04-08</sub><br>TypeSafe provider for lm15, a stdlib-only, provider-neutral Python foundation for LLM APIs: messages become Jev's state, judgment properties of a JSON schema become questions, and answers return as a data part with distributions.<br><sub>Also: <a href="https://github.com/lm15-dev/lm15-python">repo</a> · <a href="https://pypi.org/project/lm15/">pypi</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/juanlentino/jev-connector"><img src="https://opengraph.githubassets.com/1/juanlentino/jev-connector" alt="Connector for TypeSafe Jev" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/juanlentino/jev-connector">Connector for TypeSafe Jev</a></b><br><sub>juanlentino · GitHub · ⭐ 1 · 2026-09-18</sub><br>WordPress plugin that lets themes and plugins ask typed questions about content and branch on a probability, named choice or score, with the API key managed by core's Connectors API.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/yairshy/decido"><img src="https://opengraph.githubassets.com/1/yairshy/decido" alt="Decido" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/yairshy/decido">Decido</a></b><br><sub>yairshy · GitHub · ⭐ 1 · 2026-09-17</sub><br>Python library for typed questions about evidence that keeps every probability, adding validated distributions, batching, request budgets, ranking and exportable decision records around a pluggable provider.<br><sub><b>How it uses Jev:</b> Also ships optional Playwright crawling and local MCP tools.</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/xienda/dsh-jev-verify"><img src="https://opengraph.githubassets.com/1/xienda/dsh-jev-verify" alt="dsh-jev-verify" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/xienda/dsh-jev-verify">dsh-jev-verify</a></b><br><sub>xienda · GitHub · ⭐ 1 · 2026-09-21</sub><br>DeepSeek Harness plugin exposing a jev_decision tool for mixed Choice, Score and Noul questions, an opt-in risk and loop auto-guard, and a jev_verify tool that runs a 23-case labeled benchmark against live Jev.<br><sub>Also: <a href="https://www.npmjs.com/package/dsh-jev-verify">npm</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/edgardcham/huncho"><img src="https://opengraph.githubassets.com/1/edgardcham/huncho" alt="huncho" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/edgardcham/huncho">huncho</a></b><br><sub>edgardcham · GitHub · ⭐ 1 · 2026-09-18</sub><br>Dependency-free TypeScript SDK that turns Jev answers into named decisions with hysteresis thresholds, nested decisions settled in one call, a JSONL journal, replay of policy changes without inference, and calibration.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/wenchenxi/jev-console"><img src="https://raw.githubusercontent.com/wenchenxi/jev-console/main/assets/screenshot.png" alt="Jev Console" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/wenchenxi/jev-console">Jev Console</a></b><br><sub>wenchenxi · GitHub · ⭐ 1 · 2026-09-20</sub><br>Small Tkinter desktop console and CLI for using the Jev API by hand: paste a state, add Noul, Choice, or Score questions, and read the calibrated probabilities without writing code.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/litshing/jevcore"><img src="https://opengraph.githubassets.com/1/litshing/jevcore" alt="JEV core" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/litshing/jevcore">JEV core</a></b><br><sub>litshing · GitHub · ⭐ 1 · 2026-09-20</sub><br>Standard-library Python primitive for asking N items times K typed questions in bounded, fail-open requests, plus a harness that refuses any answer outside the enumerated set before code consumes it.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Nolane-x/JEV-language"><img src="https://opengraph.githubassets.com/1/Nolane-x/JEV-language" alt="JEV Language" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Nolane-x/JEV-language">JEV Language</a></b><br><sub>Nolane-x · GitHub · ⭐ 1 · 2026-09-19</sub><br>Work-in-progress runtime that composes bounded typed Jev judgments into broader expression through explicit semantic representations, deterministic compilation and verification, with zero generative-LLM calls in the core.<br><sub>Also: <a href="https://nolane-x.github.io/JEV-language/">site</a> · <a href="https://nolane-x.github.io/JEV-language">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Little-Planet-Labs/jev-playground"><img src="https://raw.githubusercontent.com/Little-Planet-Labs/jev-playground/main/docs/screenshot.png" alt="Jev Playground" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Little-Planet-Labs/jev-playground">Jev Playground</a></b><br><sub>Little-Planet-Labs · GitHub · ⭐ 1 · 2026-09-17</sub><br>Small Next.js playground where you paste a state, build any mix of Noul, Choice and Score questions and see the typed answers, distributions and confidence from one request.<br><sub>Also: <a href="https://jev-playground-zeta.vercel.app">app</a> · <a href="https://jev-playground-zeta.vercel.app">app 2</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/LeddoEngano/jev-eyes"><img src="https://raw.githubusercontent.com/LeddoEngano/jev-eyes/main/docs/demo.gif" alt="jev-eyes" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/LeddoEngano/jev-eyes">jev-eyes</a></b><br><sub>LeddoEngano · GitHub · ⭐ 1 · 2026-09-20</sub><br>Local image perception for text-only Jev: OCR and spatial layout turn an image into the exact text state Jev decides over, available as a Python library, CLI, MCP server, and agent skill.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/hemanth/jevish"><img src="https://opengraph.githubassets.com/1/hemanth/jevish" alt="jevish" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/hemanth/jevish">jevish</a></b><br><sub>hemanth · GitHub · ⭐ 1 · 2026-09-19</sub><br>JavaScript library for semantic pattern matching and zero-shot classification that runs a local zero-dependency matcher first and escalates to Jev in the cloud when needed.<br><sub><b>How it uses Jev:</b> Falls back to jev-latest via the System One endpoint when TYPESAFE_API_KEY is set.</sub><br><sub>Also: <a href="https://hemanth.github.io/jevish/">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Hugo-DDT/JevTape"><img src="https://repository-images.githubusercontent.com/1378424135/cac21bab-bdcb-4dff-b67b-808fe5242923" alt="JevTape" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Hugo-DDT/JevTape">JevTape</a></b><br><sub>Hugo-DDT · GitHub · ⭐ 1 · 2026-09-20</sub><br>Java record/replay tool with a CLI and local proxy that saves real Jev decisions as JSON cassettes, including state, question contract and model, so tests and CI replay them offline without an API key.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/lexingtonhibiki/judgekit"><img src="https://raw.githubusercontent.com/lexingtonhibiki/judgekit/main/docs/pareto.png" alt="judgekit" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/lexingtonhibiki/judgekit">judgekit</a></b><br><sub>lexingtonhibiki · GitHub · ⭐ 1 · 2026-09-19</sub><br>Provider-agnostic engine that runs YAML-defined classify, score, route, and verify tasks natively on Jev or any OpenAI-compatible LLM with cost-accuracy benchmarking; reports 97.7% on 130 Chinese samples.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/carlsonchik/judging-with-typesafe"><img src="https://opengraph.githubassets.com/1/carlsonchik/judging-with-typesafe" alt="judging-with-typesafe" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/carlsonchik/judging-with-typesafe">judging-with-typesafe</a></b><br><sub>carlsonchik · GitHub · ⭐ 1 · 2026-09-17</sub><br>Skill for Letta agents that uses Jev as a fast external judge for texts and decisions against criteria, returning a number and distribution instead of text; reports 0.004-0.014 spread over 8 runs.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/qddegtya/qualm"><img src="https://opengraph.githubassets.com/1/qddegtya/qualm" alt="qualm" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/qddegtya/qualm">qualm</a></b><br><sub>qddegtya · GitHub · ⭐ 1 · 2026-09-18</sub><br>TypeScript wrapper for Jev with tagged-template questions and literal-union answer types where every decision has an unsure branch the compiler forces you to handle.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/DonaldMurillo/system-one-playground"><img src="https://opengraph.githubassets.com/1/DonaldMurillo/system-one-playground" alt="System One Playground" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/DonaldMurillo/system-one-playground">System One Playground</a></b><br><sub>DonaldMurillo · GitHub · ⭐ 1 · 2026-09-20</sub><br>SysOneScript scripting language with a CLI and VS Code extension, a Go System One client, a Studio app and semlint semantic code checks, designed to run offline and add live Jev judgments when needed.<br><sub>Also: <a href="https://donaldmurillo.github.io/system-one-playground/">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/tinystruct/tinystruct-typesafe-sdk"><img src="https://opengraph.githubassets.com/1/tinystruct/tinystruct-typesafe-sdk" alt="tinystruct-typesafe" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/tinystruct/tinystruct-typesafe-sdk">tinystruct-typesafe</a></b><br><sub>tinystruct · GitHub · ⭐ 1 · 2026-09-21</sub><br>Java integration that lets natural language invoke existing tinystruct @Action methods, with Jev acting as a semantic dispatcher and a confirmation workflow for pending calls.<br><sub><b>How it uses Jev:</b> Arguments are only enum constants, booleans or verbatim spans of the user's input, since Jev only picks among supplied options.</sub><br><sub>Also: <a href="https://tinystruct.org">site</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/bakaphp/kanvas-ecosystem-api/tree/development/src/Domains/Connectors/TypeSafe"><img src="https://cdn.prod.website-files.com/66c9f056ff6b7f7ba51cdf21/66ccb2a881e7036ab59136f2_Logo_Kanvas_3.png" alt="Kanvas TypeSafe connector" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/bakaphp/kanvas-ecosystem-api/tree/development/src/Domains/Connectors/TypeSafe">Kanvas TypeSafe connector</a></b><br><sub>bakaphp · GitHub · ⭐ 15 repo · 2022-07-13</sub><br>PHP connector for the Kanvas operations platform (Laravel) with typed Noul, Choice and Score DTOs and per-decision OFF/SHADOW/LIVE modes, so call sites can let Jev decide while the existing LLM stays as fallback.<br><sub>Also: <a href="https://github.com/bakaphp/kanvas-ecosystem-api">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/workglow-dev/libs/tree/main/providers/typesafeai"><img src="https://raw.githubusercontent.com/workglow-dev/libs/main/docs/developers/img/cli.png" alt="@workglow/typesafeai" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/workglow-dev/libs/tree/main/providers/typesafeai">@workglow/typesafeai</a></b><br><sub>workglow-dev · GitHub · ⭐ 14 repo · 2024-01-04</sub><br>TypeSafe provider for the Workglow workflow library that exposes Jev as a SystemOneTask plus zero-shot text classification and per-candidate reranking tasks.<br><sub><b>How it uses Jev:</b> Classification is one Choice over candidate labels; reranking sends one Noul per candidate, 8 at a time by default, to keep scores independent.</sub><br><sub>Also: <a href="https://workglow.dev">app</a> · <a href="https://github.com/workglow-dev/libs">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/packstub/filament-flow/blob/main/src/Support/Jev.php"><img src="https://raw.githubusercontent.com/packstub/art/main/filament-flow/banner.jpg" alt="Filament Flow Jev node" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/packstub/filament-flow/blob/main/src/Support/Jev.php">Filament Flow Jev node</a></b><br><sub>packstub · GitHub · ⭐ 14 repo · 2026-09-02</sub><br>Visual workflow builder for Laravel Filament panels with a Jev node that evaluates a record state against typed noul, choice or score questions and branches on the answers.<br><sub>Also: <a href="https://packstub.dev/plugins/filament-flow">app</a> · <a href="https://github.com/packstub/filament-flow">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/fox1245/NeoGraph/blob/master/schemas/openrouter_decisions.json"><img src="https://raw.githubusercontent.com/fox1245/NeoGraph/master/docs/images/neograph-promo-v3.gif" alt="NeoGraph OpenRouter Decisions schema" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/fox1245/NeoGraph/blob/master/schemas/openrouter_decisions.json">NeoGraph OpenRouter Decisions schema</a></b><br><sub>fox1245 · GitHub · ⭐ 11 repo · 2026-04-02</sub><br>Provider schema that lets NeoGraph, a C++ graph agent engine in the style of LangGraph, call Jev through OpenRouter's alpha Decisions endpoint.<br><sub>Also: <a href="https://fox1245.github.io/NeoGraph/">app</a> · <a href="https://github.com/fox1245/NeoGraph">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/harlan-zw/harlan-nuxt/tree/main/packages/nuxt-jev"><img src="https://opengraph.githubassets.com/1/harlan-zw/harlan-nuxt" alt="nuxt-jev" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/harlan-zw/harlan-nuxt/tree/main/packages/nuxt-jev">nuxt-jev</a></b><br><sub>harlan-zw · GitHub · ⭐ 11 repo · 2026-08-10</sub><br>Nuxt module and framework-free base package for Jev: an HTTP client, question builders, a decision runner that reuses a journal of past answers, a Drizzle decisions table and eval replay math.<br><sub>Also: <a href="https://github.com/harlan-zw/harlan-nuxt">repo</a> · <a href="https://github.com/harlan-zw/harlan-nuxt/tree/main/packages/jev">base</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/hamr0/bareagent/blob/main/src/provider-jev.js"><img src="https://opengraph.githubassets.com/1/hamr0/bareagent" alt="bareagent Jev provider" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/hamr0/bareagent/blob/main/src/provider-jev.js">bareagent Jev provider</a></b><br><sub>hamr0 · GitHub · ⭐ 9 repo · 2026-02-17</sub><br>Zero-dependency agent orchestration library whose refine loop can use Jev as a cheap calibrated classifier tier for evaluating generated work, alongside predicate, rubric and agentic graders.<br><sub>Also: <a href="https://github.com/hamr0/bareagent">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/swamp-club/swamp-extensions/tree/main/typesafe-ai"><img src="https://opengraph.githubassets.com/1/swamp-club/swamp-extensions" alt="@swamp/typesafe-ai" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/swamp-club/swamp-extensions/tree/main/typesafe-ai">@swamp/typesafe-ai</a></b><br><sub>swamp-club · GitHub · ⭐ 8 repo · 2026-03-17</sub><br>Extension for the swamp automation tool that asks Jev typed Noul, Choice and Score questions and lets workflows branch on the calibrated answers, stored as swamp resources.<br><sub>Also: <a href="https://github.com/swamp-club/swamp-extensions">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/agentiumOS/agentium/blob/main/packages/core/src/toolkits/jev.ts"><img src="https://opengraph.githubassets.com/1/agentiumOS/agentium" alt="Agentium Jev toolkit" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/agentiumOS/agentium/blob/main/packages/core/src/toolkits/jev.ts">Agentium Jev toolkit</a></b><br><sub>agentiumOS · GitHub · ⭐ 8 repo · 2026-05-22</sub><br>TypeScript agent framework whose JevToolkit exposes TypeSafe System One judgments as tools on a chat agent, including named question packs for a jev_evaluate tool.<br><sub>Also: <a href="https://agentium.in">app</a> · <a href="https://github.com/agentiumOS/agentium">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/rulego/rulego-components-ai/tree/main/jev"><img src="https://opengraph.githubassets.com/1/rulego/rulego-components-ai" alt="RuleGo Jev nodes" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/rulego/rulego-components-ai/tree/main/jev">RuleGo Jev nodes</a></b><br><sub>rulego · GitHub · ⭐ 6 repo · 2024-04-19</sub><br>Nodes for the RuleGo declarative agent framework (ai/jev and ai/jevFilter) that route rule-chain messages by a Jev choice, noul or score answer, like a semantic switch or filter.<br><sub>Also: <a href="https://github.com/rulego/rulego-components-ai">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/redwood-labs-ai/cambium/blob/main/packages/cambium-runner/src/providers/typesafe.ts"><img src="https://opengraph.githubassets.com/1/redwood-labs-ai/cambium" alt="Cambium decision mode" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/redwood-labs-ai/cambium/blob/main/packages/cambium-runner/src/providers/typesafe.ts">Cambium decision mode</a></b><br><sub>redwood-labs-ai · GitHub · ⭐ 5 repo · 2026-04-20</sub><br>Decision mode in Cambium, a Ruby DSL for LLM programs compiled to auditable JSON, that sends forced-choice and yes/no gens to Jev through a built-in typesafe provider, using the returns block as the question set.<br><sub>Also: <a href="https://github.com/redwood-labs-ai/cambium">repo</a></sub></td>
</tr>
</table>

<details><summary>24 more</summary>

- **[cargo-ai TypeSafe provider](https://github.com/cargo-ai/cargo-ai/blob/develop/docs/providers/typesafe.md)** · <sub>cargo-ai · GitHub · ⭐ 5 repo · 2025-07-21</sub><br>TypeSafe provider for cargo-ai, a Rust framework for lightweight AI agents declared in JSON, that maps an agent's output schema to Jev questions: string enums become Choices and bounded numbers become Scores.
- **[NPipeline Jev decisions extension](https://github.com/npipeline/NPipeline/tree/main/src/NPipeline.Extensions.AI.Decisions.Jev)** · <sub>npipeline · GitHub · ⭐ 5 repo · 2025-09-02</sub><br>NPipeline.Extensions.AI.Decisions.Jev package for the NPipeline .NET streaming data-pipeline library that plugs Jev Choice questions into typed routing, with Score and Noul available through a lower-level client.
- **[goodall typesafe package](https://github.com/bensyverson/goodall/tree/main/typesafe)** · <sub>bensyverson · GitHub · ⭐ 2 repo · 2026-09-15</sub><br>Optional typesafe package in goodall, a small Go agent-loop library, that uses Jev as a tool or turn-routing judge alongside chat models, with a mail-triage example.
- **[ai-cli](https://ai-cli.dev)** · <sub>Vercel Labs · App</sub><br>Terminal CLI for the AI SDK whose evaluate command pipes text into typed boolean, choice, and score questions and returns probabilities for use in shell scripts.
- **[BAML](https://boundaryml.com/blog/typesafe-ai-jev)** · <sub>BoundaryML · Article · 2026-09-17</sub><br>Derives Jev questions from a function's return type, turning booleans and floats into Nouls and enums into Choices.
- **[Jev Symfony Bundle](https://github.com/vbcherepanov/jev-symfony-bundle)** · <sub>vbcherepanov · GitHub · 2026-09-21</sub><br>Unofficial Symfony bundle for Jev with a typed HttpClient-based client, #[JevNoul] and #[JevChoice] validator constraints, background Messenger evaluation, Workflow guards and a profiler panel.
- **[jev-acp](https://github.com/formulahendry/jev-acp)** · <sub>formulahendry · GitHub · 2026-09-21</sub><br>Standalone Agent Client Protocol agent that lets any ACP client or IDE, such as JetBrains, ask Jev Choice, Score and Noul questions with guided input, reusable templates and probability displays.
- **[jev-gates](https://github.com/carlchou0dailyfresh/jev-gates)** · <sub>carlchou0dailyfresh · GitHub · 2026-09-19</sub><br>Zero-dependency TypeScript library for composing Jev judgments and exact rules into three-valued TRUE/FALSE/UNKNOWN logic circuits defined in JSON, reusable inside larger circuits.
- **[jev-judge](https://github.com/ohmyjiro/jev-judge)** · <sub>ohmyjiro · GitHub · 2026-09-20</sub><br>Dependency-free Python CLI and Codex skill that sends a JSON state with named Noul, Choice or Score questions to Jev and returns only the typed answers, so an agent reads a small answer instead of the full evidence.
- **[jev-router (carllippert)](https://github.com/carllippert/jev-router)** · <sub>carllippert · GitHub · 2026-09-18</sub><br>Express middleware with no route table: you register plain-English intents with named functions, and one Jev Choice over the method, path and body decides which handler runs.
- **[JevGuard](https://github.com/seb4ez/jevguard)** · <sub>seb4ez · GitHub · 2026-09-19</sub><br>Standard-library Python layer around Jev that caches decisions in SQLite by fingerprinted state, prunes state, injects a neutral escape option and flags poorly calibrated answers.
- **[JevPlay](https://github.com/ndolinschi/jevplay)** · <sub>ndolinschi · GitHub · 2026-09-17</sub><br>Next.js playground where you enter a freeform state, invent custom Choice, Score and Noul questions and see the live probability distributions.
- **[jevtok](https://github.com/LabGuy94/jevtok)** · <sub>LabGuy94 · GitHub · 2026-09-21</sub><br>Tiktoken-style encoder that reproduces Jev's tokenizer bit for bit, reconstructed from API usage counts, for exact token counting and request-cost prediction, verified on 20,034 strings with 0 mismatches.
- **[LangChain](https://docs.langchain.com/oss/python/integrations/providers/typesafe)** (alpha) · <sub>LangChain · Article</sub><br>Classifier runnable plus experimental middleware for per-request model routing and for stopping risky tool calls.
- **[n8n TypeSafe node](https://github.com/DomMonte/n8n-nodes-typesafe-ai)** · <sub>DomMonte · GitHub · 2026-09-17</sub><br>Community node with yes-or-no, choice, and score operations, usable as an AI Agent tool on self-hosted n8n.
- **[n8n-nodes-agent-langfuse](https://community.n8n.io/t/jev-in-n8n-a-node-for-typesafes-decision-model-traced-in-langfuse/315249)** · <sub>Diward · X · 2026-09-21</sub><br>Community n8n node that sends a state plus yes/no, choice and score questions to Jev through OpenRouter and traces each call to Langfuse with the provider-reported cost.
- **[n8n-nodes-jev-classification](https://github.com/khmuhtadin/n8n-nodes-jev-classification)** · <sub>khmuhtadin · GitHub · 2026-09-21</sub><br>Community node for n8n that classifies, scores and checks text with Jev like the built-in Text Classifier, with one branch per category plus Needs Review, parallel requests and multi-item batching.
- **[n8n-nodes-typesafe](https://github.com/Biztactix/n8n-nodes-typesafe)** · <sub>Biztactix · GitHub · 2026-09-19</sub><br>Community node for n8n that sends workflow text or JSON with named noul, choice and score questions to the System One API and returns typed answers to route on, plus a List Models operation.
- **[nf-jev](https://github.com/nextflow-io/nf-jev)** · <sub>nextflow-io · GitHub · 2026-09-20</sub><br>Beta Nextflow plugin that exposes Jev noul, choice and score judgments as ordinary pipeline functions, so a pipeline can build typed questions as values and gate on the returned probabilities.
- **[openclaw-typesafe-ai](https://github.com/Olli0103/openclaw-typesafe-ai)** · <sub>Olli0103 · GitHub · 2026-09-18</sub><br>OpenClaw plugin that registers one explicitly invoked typesafe_decide tool sending text or JSON state and typed questions to Jev, with SecretRef credentials and no hooks or model provider.
- **[Pydantic AI](https://pydantic.dev/docs/ai/models/typesafe/)** · <sub>Pydantic · Docs</sub><br>Runs an agent on Jev by mapping booleans to Nouls, enums to Choices, and integer rubrics to Scores, with an LLM fallback when unsure.
- **[semgate](https://github.com/m-mizutani/semgate)** · <sub>m-mizutani · GitHub · 2026-09-19</sub><br>Go net/http middlewares that ask Jev typed questions about each incoming request and hand the answers to your function to pass it on, block it or route it to another handler.
- **[TanStack AI](https://tanstack.com/ai/latest/docs/adapters/typesafe)** · <sub>TanStack · Article</sub><br>Adapter for the <code>decide</code> API with choice, score, and boolean question helpers.
- **[Vercel AI SDK](https://ai-sdk.dev/providers/ai-sdk-providers/typesafe-ai)** · <sub>Vercel · Docs</sub><br>Provider for <code>experimental_evaluate</code> that maps choice, score, and boolean questions onto Jev's primitives.

</details>

Missing something? [Suggest a resource](https://github.com/Li-Evan/awesome-jev/issues/new/choose).
