# 🔌 Build with Jev: Model Access

**English** · [简体中文](https://github.com/Li-Evan/awesome-jev/blob/main/zh-CN/pages/build-model-access.md)

Ways to call Jev from your stack: hosted access, framework adapters, observability, and community SDKs. 68 entries, ranked by community traction.

[← Back to Awesome Jev](https://github.com/Li-Evan/awesome-jev#model-access)

**Model Access** · [Framework Adapters](https://github.com/Li-Evan/awesome-jev/blob/main/pages/build-frameworks.md) (174) · [Observability](https://github.com/Li-Evan/awesome-jev/blob/main/pages/build-observability.md) (14) · [Community SDKs](https://github.com/Li-Evan/awesome-jev/blob/main/pages/build-community-sdks.md) (107)

<table>
<tr>
<td width="260" valign="top"><a href="https://x.com/OpenRouter/status/2100744709589316009"><img src="https://pbs.twimg.com/amplify_video_thumb/2100744692048818176/img/lnRQ8fZbTFSI0YuV.jpg" alt="Jev on OpenRouter" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/OpenRouter/status/2100744709589316009">Jev on OpenRouter</a></b><br><sub>OpenRouter · X · ♥ 3.9k · 2026-09-18</sub><br>OpenRouter's announcement that Jev is available in beta through its API, returning a typed decision with a probability instead of generated text.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/anomalyco/opencode/blob/dev/packages/web/src/content/docs/zen.mdx"><img src="https://raw.githubusercontent.com/anomalyco/opencode/dev/packages/web/src/assets/lander/screenshot.png" alt="OpenCode Zen Jev endpoint" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/anomalyco/opencode/blob/dev/packages/web/src/content/docs/zen.mdx">OpenCode Zen Jev endpoint</a></b><br><sub>anomalyco · Docs · ⭐ 209.2k repo · 2025-04-30</sub><br>OpenCode's Zen gateway serves Jev 1.13 at a /v1/systemone endpoint with the Zen API key, plus a limited-time free jev-1.13-free model.<br><sub>Also: <a href="https://opencode.ai/docs/zen">docs</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/get-convex/convex-backend/blob/main/npm-packages/docs/docs/ai-gateway/api.mdx"><img src="https://opengraph.githubassets.com/1/get-convex/convex-backend" alt="Convex AI Gateway Jev support" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/get-convex/convex-backend/blob/main/npm-packages/docs/docs/ai-gateway/api.mdx">Convex AI Gateway Jev support</a></b><br><sub>get-convex · Docs · ⭐ 12.6k repo · 2024-03-08</sub><br>Convex's AI Gateway serves Jev as typesafe/jev-1.13 through a decisions endpoint, callable from Convex actions via AI SDK's evaluate and the @convex-dev/ai-sdk-provider package.<br><sub><b>How it uses Jev:</b> Authentication uses a short-lived deployment token, and the dollar cost of each decision is returned in provider metadata.</sub><br><sub>Also: <a href="https://github.com/get-convex/convex-backend/tree/main/npm-packages/@convex-dev/ai-sdk-provider">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/maximhq/bifrost/tree/dev/core/providers/typesafe"><img src="https://opengraph.githubassets.com/1/maximhq/bifrost" alt="Bifrost TypeSafe provider" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/maximhq/bifrost/tree/dev/core/providers/typesafe">Bifrost TypeSafe provider</a></b><br><sub>maximhq · GitHub · ⭐ 8.2k repo · 2025-03-19</sub><br>TypeSafe provider in the Bifrost AI gateway that exposes a drop-in /typesafe prefix, so clients written for api.typesafe.ai, including the official SDK, work through Bifrost unchanged.<br><sub><b>How it uses Jev:</b> Covers Noul, Choice and Score, jev-latest alias resolution and model listing, with a decisions quickstart for the gateway and Go SDK.</sub><br><sub>Also: <a href="https://www.getmaxim.ai/bifrost">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/tbphp/gpt-load/blob/main/internal/channel/modules/jev.go"><img src="https://repository-images.githubusercontent.com/997490512/48207872-b9e0-4e70-8006-0becdc6507ff" alt="GPT-Load Jev channel" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/tbphp/gpt-load/blob/main/internal/channel/modules/jev.go">GPT-Load Jev channel</a></b><br><sub>tbphp · GitHub · ⭐ 6.9k repo · 2025-06-06</sub><br>Jev channel module for the self-hosted GPT-Load AI gateway, adding TypeSafe's official API as a provider with batch key import, scheduling and failover.<br><sub>Also: <a href="https://www.gpt-load.com">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/sabrinaesaquino/status/2101102660997017747"><img src="https://pbs.twimg.com/amplify_video_thumb/2101101845225865216/img/cubmkjzFZ8i2sPKp.jpg" alt="Jev on the Venice API" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/sabrinaesaquino/status/2101102660997017747">Jev on the Venice API</a></b><br><sub>sabrinaesaquino · X · ♥ 221 · 2026-09-19</sub><br>Demo marking Jev's beta launch on the Venice API, classifying 24,000 Hacker News posts into 12 categories in about 2 minutes.<br><sub>Also: <a href="https://x.com/AskVenice/status/2101095644467511578">announcement</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/experientiallabs/experiential/blob/main/exp/runtime/models/providers/typesafe.py"><img src="https://raw.githubusercontent.com/experientiallabs/experiential/main/assets/experiential-workflow.png" alt="Experiential TypeSafe provider" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/experientiallabs/experiential/blob/main/exp/runtime/models/providers/typesafe.py">Experiential TypeSafe provider</a></b><br><sub>experientiallabs · GitHub · ⭐ 5.4k repo · 2026-06-24</sub><br>TypeSafe provider in the Experiential open-source model gateway that dispatches Jev decisions natively and refuses to treat Jev as a chat model.<br><sub>Also: <a href="https://experientiallabs.ai">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/cloudflare/cloudflare-docs/blob/production/src/content/catalog-models/typesafe-jev.json"><img src="https://opengraph.githubassets.com/1/cloudflare/cloudflare-docs" alt="Cloudflare Jev model catalog" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/cloudflare/cloudflare-docs/blob/production/src/content/catalog-models/typesafe-jev.json">Cloudflare Jev model catalog</a></b><br><sub>cloudflare · Docs · ⭐ 5.2k repo · 2020-09-03</sub><br>Cloudflare's model catalog entry for typesafe/jev, listing Jev for Noul, Choice and Score evaluation at $0.042 per million input tokens and free output, with a worked example.<br><sub>Also: <a href="https://developers.cloudflare.com">docs</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/pollinations/pollinations/blob/main/gen.pollinations.ai/src/text/systemOneClient.ts"><img src="https://raw.githubusercontent.com/pollinations/pollinations/main/packages/ui/src/brand/lockup-horizontal-black.svg" alt="Pollinations Jev API" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/pollinations/pollinations/blob/main/gen.pollinations.ai/src/text/systemOneClient.ts">Pollinations Jev API</a></b><br><sub>pollinations · GitHub · ⭐ 5.1k repo · 2021-04-15</sub><br>The Pollinations gen API serves Jev as typesafe/jev-1.13 through a typed POST /alpha/decisions endpoint and Chat Completions, plus an Ask Jev MCP server with a jev_decide tool.<br><sub>Also: <a href="https://gen.pollinations.ai/docs">docs</a> · <a href="https://pollinations.ai">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/flydotio/status/2102076230183035081"><img src="https://pbs.twimg.com/media/HSwTDxlaEAMHET8.jpg?name=orig" alt="Jev on Fly.io Sprites" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/flydotio/status/2102076230183035081">Jev on Fly.io Sprites</a></b><br><sub>flydotio · X · ♥ 81 · 2026-09-21</sub><br>Fly.io's TypeSafe connector for Sprites, which injects your Jev API key at a gateway so agents running inside hardware-isolated Sprites can call Jev without the key entering the sandbox.<br><sub>Also: <a href="https://fly.io/sprites/jev">docs</a> · <a href="https://fly.io/sprites/jev">project</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/dgrid_ai/status/2102231668040040687"><img src="https://pbs.twimg.com/media/HSyghV2bQAAKh8Q.jpg?name=orig" alt="Jev on DGrid" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/dgrid_ai/status/2102231668040040687">Jev on DGrid</a></b><br><sub>dgrid_ai · X · ♥ 17 · 2026-09-22</sub><br>DGrid added Jev 1.13 to its model catalog, serving routing, classification and scoring requests with multiple typed questions per call.<br><sub>Also: <a href="https://dgrid.ai/models/typesafe/jev-1.13">app</a> · <a href="https://dgrid.ai/models/typesafe/jev-1.13">project</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/theagentrouter/agent-router/tree/main/internal/apischema/typesafe"><img src="https://raw.githubusercontent.com/theagentrouter/agent-router/main/site/static/img/brand/ar-horizontal-primary.svg" alt="Agent Router TypeSafe schema" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/theagentrouter/agent-router/tree/main/internal/apischema/typesafe">Agent Router TypeSafe schema</a></b><br><sub>theagentrouter · GitHub · ⭐ 2.1k repo · 2024-10-21</sub><br>Agent Router, the Envoy-based AI gateway formerly Envoy AI Gateway, adds TypeSafe System One request and response schema so Jev's /v1/systemone can be routed through it.<br><sub><b>How it uses Jev:</b> State, instructions and criteria are kept as raw JSON and never reshaped by the gateway.</sub><br><sub>Also: <a href="https://theagentrouter.ai/">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/HarnessRouter/harnessrouter/blob/main/runner/systemone_driver.py"><img src="https://raw.githubusercontent.com/HarnessRouter/harnessrouter/main/docs/images/github-readme-star-cta-desktop.svg" alt="HarnessRouter systemone base" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/HarnessRouter/harnessrouter/blob/main/runner/systemone_driver.py">HarnessRouter systemone base</a></b><br><sub>HarnessRouter · GitHub · ⭐ 2k repo · 2026-08-09</sub><br>HarnessRouter, a self-hosted unified interface for agent harnesses, runs a systemone base that serves Jev through either TypeSafe's API or OpenRouter under their own model ids.<br><sub><b>How it uses Jev:</b> The catalog's systemone base is the only place jev ids are listed, and a turn is served through one of the two wirings.</sub><br><sub>Also: <a href="https://harnessrouter.ai/">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/yomorun/yomo/blob/main/src/model_api_provider/providers/typesafe_systemone.rs"><img src="https://user-images.githubusercontent.com/65603/162367572-5a0417fa-e2b2-4d35-8c92-2c95d461706d.png" alt="YoMo TypeSafe System One provider" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/yomorun/yomo/blob/main/src/model_api_provider/providers/typesafe_systemone.rs">YoMo TypeSafe System One provider</a></b><br><sub>yomorun · GitHub · ⭐ 1.9k repo · 2020-07-01</sub><br>YoMo, a serverless edge AI agent framework, adds a TypeSafe System One provider that proxies Jev decision requests through its geo-distributed model API layer.<br><sub>Also: <a href="https://yomo.run">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/beam-cloud/beta9/blob/main/sdk/src/beta9/abstractions/managed_endpoint.py"><img src="https://raw.githubusercontent.com/beam-cloud/beta9/main/static/beam-logo-white.png" alt="Beam managed System One endpoint" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/beam-cloud/beta9/blob/main/sdk/src/beta9/abstractions/managed_endpoint.py">Beam managed System One endpoint</a></b><br><sub>beam-cloud · GitHub · ⭐ 1.8k repo · 2023-11-15</sub><br>Beam's serverless GPU runtime can host a decision-kind managed endpoint that serves a System One model on TypeSafe's /v1/systemone contract.<br><sub><b>How it uses Jev:</b> The endpoint's decision kind picks the /v1/systemone routes; the model name is what callers send.</sub><br><sub>Also: <a href="https://beam.cloud">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/theopenco/llmgateway/blob/main/packages/models/src/models/typesafe.ts"><img src="https://opengraph.githubassets.com/1/theopenco/llmgateway" alt="LLM Gateway TypeSafe model" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/theopenco/llmgateway/blob/main/packages/models/src/models/typesafe.ts">LLM Gateway TypeSafe model</a></b><br><sub>theopenco · GitHub · ⭐ 1.7k repo · 2025-04-12</sub><br>LLM Gateway registers Jev 1.13 as a TypeSafe decision model, routing state-plus-questions requests to the /v1/systemone endpoint through its unified gateway.<br><sub>Also: <a href="https://llmgateway.io">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://zenmux.ai/docs/api/typesafe/systemone"><img src="https://cdn.marmot-cloud.com/storage/zenmux/2025/09/16/lAK3vlZ/banner.png" alt="ZenMux TypeSafe System One API" width="240"></a></td>
<td valign="top"><b><a href="https://zenmux.ai/docs/api/typesafe/systemone">ZenMux TypeSafe System One API</a></b><br><sub>ZenMux · Docs · ⭐ 75 · 2026-09-20</sub><br>API reference for calling TypeSafe System One evaluation requests with Jev through the ZenMux model gateway.<br><sub>Also: <a href="https://github.com/ZenMux/zenmux-doc/blob/main/docs_source/en/api/typesafe/systemone.md">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/astaxie/TokenHub/blob/main/docs/semantic-routing.md"><img src="https://raw.githubusercontent.com/astaxie/TokenHub/main/frontend/public/brand/tokenhub-logo.png" alt="TokenHub Jev semantic routing" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/astaxie/TokenHub/blob/main/docs/semantic-routing.md">TokenHub Jev semantic routing</a></b><br><sub>astaxie · GitHub · ⭐ 1.3k repo · 2026-06-10</sub><br>TokenHub, an enterprise AI gateway, can use Jev to choose the provider and upstream model for eligible Chat Completions requests among the candidates its base routing produced.<br><sub><b>How it uses Jev:</b> One Choice per request returning a candidate or no_preference; observe and enforce modes with a 0.65 confidence threshold, called at most once per request.</sub><br><sub>Also: <a href="https://thinkinai-labs.github.io/tokenhome/">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"></td>
<td valign="top"><b><a href="https://docs.venice.ai/api-reference/endpoint/decisions/systemone">Venice System One compatibility</a></b><br><sub>Venice · Docs · ⭐ 65 · 2026-09-18</sub><br>API reference for Venice's TypeSafe-compatible POST /systemone alias of its Decisions API, letting System One clients call Jev through Venice.<br><sub>Also: <a href="https://github.com/veniceai/api-docs/blob/main/api-reference/endpoint/decisions/systemone.mdx">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/yym68686/uni-api/blob/main/scripts/verify_typesafe.py"><img src="https://opengraph.githubassets.com/1/yym68686/uni-api" alt="uni-api TypeSafe backend" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/yym68686/uni-api/blob/main/scripts/verify_typesafe.py">uni-api TypeSafe backend</a></b><br><sub>yym68686 · GitHub · ⭐ 1.3k repo · 2024-07-04</sub><br>Adds TypeSafe Jev as a backend to uni-api, a unified LLM API gateway with load balancing, so decision requests route through the same OpenAI-style interface as its other providers.<br><sub>Also: <a href="https://0-0.pro/r/uniapi">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"></td>
<td valign="top"><b><a href="https://docs.litellm.ai/blog/typesafe_jev">TypeSafe Jev on LiteLLM</a></b><br><sub>LiteLLM · Article · ⭐ 32 · 2026-09-20</sub><br>LiteLLM announcement that its proxy (v1.103.0-rc) passes through TypeSafe's /v1/systemone endpoint with logging and cost tracking, so clients call Jev with a LiteLLM virtual key.<br><sub>Also: <a href="https://github.com/BerriAI/litellm-docs/tree/main/blog/typesafe_jev">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"></td>
<td valign="top"><b><a href="https://docs.aimlapi.com/api-references/decision-models/typesafe/jev">AI/ML API Jev</a></b><br><sub>AI/ML API · Docs · ⭐ 28 · 2024-05-28</sub><br>AI/ML API documentation for serving TypeSafe Jev as typesafe/jev under its decision-models API, with a playground and Python/Node.js snippets for state-plus-questions requests.<br><sub>Also: <a href="https://github.com/aimlapi/api-docs/tree/main/docs/api-references/decision-models/TypeSafe">repo</a> · <a href="https://aimlapi.com/app/typesafe/jev">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/yym68686/uni-api-web"><img src="https://opengraph.githubassets.com/1/yym68686/uni-api-web" alt="uni-api TypeSafe channel" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/yym68686/uni-api-web">uni-api TypeSafe channel</a></b><br><sub>yym68686 · GitHub · ⭐ 26 · 2025-03-11</sub><br>Web console for the self-hosted uni-api LLM gateway that can add a typesafe engine channel, proxying POST /v1/systemone so Jev's Choice, Noul and Score questions go through the gateway.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/croit/aiplane"><img src="https://raw.githubusercontent.com/croit/aiplane/main/docs/img/architecture.svg" alt="croit AIplane" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/croit/aiplane">croit AIplane</a></b><br><sub>croit · GitHub · ⭐ 23 · 2026-06-17</sub><br>Self-hosted AI gateway with a TypeSafe System One-compatible /v1/systemone endpoint, so the official SDK can use it as base URL, plus System One-based automatic model routing and a GDPR/NDA content guard.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/unorouter/new-api-sync"><img src="https://opengraph.githubassets.com/1/unorouter/new-api-sync" alt="new-api-sync TypeSafe provider" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/unorouter/new-api-sync">new-api-sync TypeSafe provider</a></b><br><sub>unorouter · GitHub · ⭐ 21 · 2026-01-15</sub><br>Sync engine for new-api gateways (used by UnoRouter) with a typesafe provider type that syncs Jev from OpenRouter's decisions route into the gateway with its own sell price and 32,000-token context.<br><sub>Also: <a href="https://unorouter.com">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/braintrustdata/braintrust-proxy/blob/main/packages/proxy/scripts/sync_typesafe.ts"><img src="https://opengraph.githubassets.com/1/braintrustdata/braintrust-proxy" alt="Braintrust AI Proxy TypeSafe provider" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/braintrustdata/braintrust-proxy/blob/main/packages/proxy/scripts/sync_typesafe.ts">Braintrust AI Proxy TypeSafe provider</a></b><br><sub>braintrustdata · GitHub · ⭐ 410 repo · 2023-11-22</sub><br>Adds TypeSafe as a provider in the Braintrust AI proxy, with a script that syncs Jev model IDs, aliases and per-token pricing from the TypeSafe models API and docs.<br><sub>Also: <a href="https://www.braintrustdata.com/docs/guides/proxy">docs</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/OpenRouterTeam/typescript-sdk/blob/main/docs/sdks/systemone/README.mdx"><img src="https://raw.githubusercontent.com/OpenRouterTeam/typescript-sdk/main/assets/banner.png" alt="OpenRouter TypeScript SDK System One" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/OpenRouterTeam/typescript-sdk/blob/main/docs/sdks/systemone/README.mdx">OpenRouter TypeScript SDK System One</a></b><br><sub>OpenRouterTeam · GitHub · ⭐ 254 repo · 2025-08-21</sub><br>Official OpenRouter TypeScript SDK resource that sends state and typed questions to System One models such as Jev, mapping bare IDs like jev-latest onto the typesafe/ namespace.<br><sub>Also: <a href="https://github.com/OpenRouterTeam/typescript-sdk/blob/main/src/sdk/systemone.ts">code</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/mcowger/plexus/blob/main/packages/backend/src/types/decisions.ts"><img src="https://raw.githubusercontent.com/mcowger/plexus/main/assets/readme/hero.svg" alt="Plexus decisions gateway" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/mcowger/plexus/blob/main/packages/backend/src/types/decisions.ts">Plexus decisions gateway</a></b><br><sub>mcowger · GitHub · ⭐ 234 repo · 2025-12-01</sub><br>Unified LLM API gateway that adds a Jev-style decisions endpoint, routing state-plus-questions requests to TypeSafe /v1/systemone or OpenRouter's decisions API.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/top-think/think-ai"><img src="https://opengraph.githubassets.com/1/top-think/think-ai" alt="ThinkAI decision API" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/top-think/think-ai">ThinkAI decision API</a></b><br><sub>top-think · GitHub · ⭐ 9 · 2023-12-28</sub><br>PHP SDK for the ThinkAI model aggregation service whose decision() resource evaluates Jev noul and choice questions (model jev-latest) next to chat, image and voice APIs.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/OpenRouterTeam/python-sdk/blob/main/src/openrouter/systemone.py"><img src="https://raw.githubusercontent.com/OpenRouterTeam/python-sdk/main/assets/banner.png" alt="OpenRouter Python SDK System One" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/OpenRouterTeam/python-sdk/blob/main/src/openrouter/systemone.py">OpenRouter Python SDK System One</a></b><br><sub>OpenRouterTeam · GitHub · ⭐ 160 repo · 2025-08-22</sub><br>Official OpenRouter Python SDK module for sending state and typed questions to System One models like Jev through OpenRouter.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/genlayerlabs/unhardcoded"><img src="https://opengraph.githubassets.com/1/genlayerlabs/unhardcoded" alt="unhardcoded" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/genlayerlabs/unhardcoded">unhardcoded</a></b><br><sub>genlayerlabs · GitHub · ⭐ 8 · 2026-06-22</sub><br>OpenAI-compatible LLM router that picks a model per request from a caller-supplied policy, and serves decision models including Jev through POST /v1/decisions with the same selection and fallback.<br><sub>Also: <a href="https://github.com/genlayerlabs/unhardcoded/blob/main/docs/DECISION-MODELS.md">docs</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/AgentsDanceAI/AIStore"><img src="https://opengraph.githubassets.com/1/AgentsDanceAI/AIStore" alt="AI Store" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/AgentsDanceAI/AIStore">AI Store</a></b><br><sub>AgentsDanceAI · GitHub · ⭐ 7 · 2026-08-21</sub><br>Accounts, credits and workspace layer for thirty hosted open-source AI products that offers both a self-hosted Laya decision model and TypeSafe's hosted Jev as metered slots.<br><sub>Also: <a href="https://aistore.best">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Muvon/octohub"><img src="https://opengraph.githubassets.com/1/Muvon/octohub" alt="OctoHub" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Muvon/octohub">OctoHub</a></b><br><sub>Muvon · GitHub · ⭐ 7 · 2026-03-19</sub><br>Rust LLM proxy with one OpenAI-style API over 20+ providers, multi-tenant keys and request logging, whose config can map an evaluation model "jev" to TypeSafe or Cloudflare.<br><sub>Also: <a href="https://octomind.run/product/octohub/">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/hackclub/ai/blob/main/src/routes/proxy/v1/jev.ts"><img src="https://opengraph.githubassets.com/1/hackclub/ai" alt="Hack Club AI Jev endpoint" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/hackclub/ai/blob/main/src/routes/proxy/v1/jev.ts">Hack Club AI Jev endpoint</a></b><br><sub>hackclub · GitHub · ⭐ 133 repo · 2026-09-17</sub><br>Jev forwarding route in Hack Club's free AI proxy for teens, reusing its Hack Club auth, API keys, spending limits and usage logging.<br><sub>Also: <a href="https://github.com/hackclub/ai">repo</a> · <a href="https://ai.hackclub.com">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/RyanKung/rotom"><img src="https://raw.githubusercontent.com/RyanKung/rotom/master/demos/claude-grok-4.3.gif" alt="rotom" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/RyanKung/rotom">rotom</a></b><br><sub>RyanKung · GitHub · ⭐ 5 · 2026-04-27</sub><br>Local OpenAI- and Anthropic-compatible API gateway in Rust that reuses Codex, Grok, Kiro or Vercel AI Gateway logins for any client, and also carries Jev through its model catalog and evaluation endpoint.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Routstr/routstr-core/blob/main/routstr/upstream/typesafe.py"><img src="https://opengraph.githubassets.com/1/Routstr/routstr-core" alt="Routstr TypeSafe upstream" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Routstr/routstr-core/blob/main/routstr/upstream/typesafe.py">Routstr TypeSafe upstream</a></b><br><sub>Routstr · GitHub · ⭐ 81 repo · 2025-04-08</sub><br>Decentralized pay-per-request AI inference proxy, paid with Cashu Bitcoin micropayments, that adds a TypeSafe System One decision endpoint and Jev model catalog.<br><sub>Also: <a href="http://docs.routstr.com/">docs</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/OpenRouterTeam/go-sdk/blob/main/systemone.go"><img src="https://raw.githubusercontent.com/OpenRouterTeam/go-sdk/main/assets/banner.png" alt="OpenRouter Go SDK System One" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/OpenRouterTeam/go-sdk/blob/main/systemone.go">OpenRouter Go SDK System One</a></b><br><sub>OpenRouterTeam · GitHub · ⭐ 70 repo · 2025-11-13</sub><br>Official OpenRouter Go SDK support for sending state and typed questions to System One models like Jev through OpenRouter.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/t0ng7u/status/2102062876819374482"><img src="https://pbs.twimg.com/amplify_video_thumb/2102062812709449728/img/SVBMGP0wAoKqO6J1.jpg" alt="New API Jev plugin" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/t0ng7u/status/2102062876819374482">New API Jev plugin</a></b><br><sub>t0ng7u · X · ♥ 3 · 2026-09-21</sub><br>Plugin that exposes Jev's Choice, Score and Noul through a self-hosted New API gateway, so the official TypeSafe SDK can point at the gateway without code changes.<br><sub>Also: <a href="https://newapi.pro/zh/plugins">plugins</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/FFatTiger/new-api-plugin-typesafe"><img src="https://opengraph.githubassets.com/1/FFatTiger/new-api-plugin-typesafe" alt="new-api-plugin-typesafe" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/FFatTiger/new-api-plugin-typesafe">new-api-plugin-typesafe</a></b><br><sub>FFatTiger · GitHub · ⭐ 3 · 2026-09-18</sub><br>Task plugin for the self-hosted QuantumNous new-api gateway that serves Jev over the native /v1/systemone protocol with token billing, using TypeSafe or Vercel AI Gateway as the upstream.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/AntSeed/antseed/tree/main/plugins/provider-typesafe"><img src="https://opengraph.githubassets.com/1/AntSeed/antseed" alt="AntSeed TypeSafe provider" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/AntSeed/antseed/tree/main/plugins/provider-typesafe">AntSeed TypeSafe provider</a></b><br><sub>AntSeed · GitHub · ⭐ 57 repo · 2026-02-24</sub><br>Peer-to-peer AI inference market where providers can offer TypeSafe System One decisions through a provider-typesafe plugin, discovered by buyers over DHT.<br><sub>Also: <a href="https://antseed.com">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/sxueck/llm-gateway/blob/main/packages/backend/src/routes/openai/decisions-handler.ts"><img src="https://github.com/user-attachments/assets/a69d7e89-5225-4c2e-bae3-d11faddc9b56" alt="LLM Gateway System One endpoint" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/sxueck/llm-gateway/blob/main/packages/backend/src/routes/openai/decisions-handler.ts">LLM Gateway System One endpoint</a></b><br><sub>sxueck · GitHub · ⭐ 52 repo · 2025-10-05</sub><br>Self-hosted distributed LLM gateway with a web UI that adds a decisions proxy handler so System One requests to Jev pass through its routing, keys and usage logging.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/6Kmfi6HP/opencode2api/blob/main/internal/app/systemone.go"><img src="https://opengraph.githubassets.com/1/6Kmfi6HP/opencode2api" alt="opencode2api System One proxy" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/6Kmfi6HP/opencode2api/blob/main/internal/app/systemone.go">opencode2api System One proxy</a></b><br><sub>6Kmfi6HP · GitHub · ⭐ 49 repo · 2026-06-04</sub><br>Local proxy that exposes OpenCode Zen and Go models as OpenAI and Anthropic APIs, adding a System One route for Jev decision requests.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/netlify/context-and-tools/tree/main/skills/netlify-ai-gateway"><img src="https://opengraph.githubassets.com/1/netlify/context-and-tools" alt="Netlify AI Gateway skill" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/netlify/context-and-tools/tree/main/skills/netlify-ai-gateway">Netlify AI Gateway skill</a></b><br><sub>netlify · GitHub · ⭐ 37 repo · 2025-11-26</sub><br>Netlify's official agent skill for its AI Gateway, which lists TypeSafe Jev as a provider with injected credentials and shows a Netlify Function routing contact-form submissions to sales, support or spam with one Choice.<br><sub>Also: <a href="https://github.com/netlify/context-and-tools">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/chatbotkit/platform/blob/main/platform/lib/model.provider.typesafe.ts"><img src="https://opengraph.githubassets.com/1/chatbotkit/platform" alt="ChatBotKit platform decisions" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/chatbotkit/platform/blob/main/platform/lib/model.provider.typesafe.ts">ChatBotKit platform decisions</a></b><br><sub>chatbotkit · GitHub · ⭐ 26 repo · 2026-09-03</sub><br>Decision API in the open-source ChatBotKit AI backend (/api/v1/decision/create) that serves typed questions through TypeSafe, OpenRouter or Vercel AI Gateway providers with bounded timeouts and retries.<br><sub>Also: <a href="https://cbk.ai">app</a> · <a href="https://github.com/chatbotkit/platform">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Lore-Hex/quill-router/blob/main/src/trusted_router/data/provider_models/typesafe.json"><img src="https://opengraph.githubassets.com/1/Lore-Hex/quill-router" alt="TrustedRouter Jev" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Lore-Hex/quill-router/blob/main/src/trusted_router/data/provider_models/typesafe.json">TrustedRouter Jev</a></b><br><sub>Lore-Hex · GitHub · ⭐ 23 repo · 2026-05-02</sub><br>TrustedRouter, an end-to-end encrypted LLM gateway running in hardware enclaves, lists TypeSafe AI Jev as typesafe-ai/jev on a decide endpoint, with input pricing refreshed hourly from TypeSafe's models page.<br><sub>Also: <a href="https://github.com/Lore-Hex/quill-router">repo</a> · <a href="https://trustedrouter.com">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/sapiom/sapiom-js/blob/main/packages/tools/src/llm/decide.ts"><img src="https://opengraph.githubassets.com/1/sapiom/sapiom-js" alt="Sapiom llm.decide" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/sapiom/sapiom-js/blob/main/packages/tools/src/llm/decide.ts">Sapiom llm.decide</a></b><br><sub>sapiom · GitHub · ⭐ 20 repo · 2025-11-11</sub><br>The llm.decide capability in the Sapiom agent SDK routes Jev through Sapiom's Capability Router and returns calibrated probabilities over caller-defined answers for typed Noul, Choice and Score questions.<br><sub>Also: <a href="https://github.com/sapiom/sapiom-js">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/QuantumNous/new-api-plugins/tree/main/plugins/tasks/typesafe"><img src="https://opengraph.githubassets.com/1/QuantumNous/new-api-plugins" alt="new-api TypeSafe plugin" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/QuantumNous/new-api-plugins/tree/main/plugins/tasks/typesafe">new-api TypeSafe plugin</a></b><br><sub>QuantumNous · GitHub · ⭐ 16 repo · 2026-08-19</sub><br>Official task plugin for the new-api gateway that serves Jev at POST /typesafe/v1/systemone (jev-1.13.0, jev-latest, jev-preview), billing actual input tokens with free output, directly or through another new-api gateway.<br><sub>Also: <a href="https://github.com/QuantumNous/new-api-plugins">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/orq-ai/orq-node/blob/main/src/sdk/classify.ts"><img src="https://opengraph.githubassets.com/1/orq-ai/orq-node" alt="orq.ai classify API" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/orq-ai/orq-node/blob/main/src/sdk/classify.ts">orq.ai classify API</a></b><br><sub>orq-ai · GitHub · ⭐ 11 repo · 2023-12-27</sub><br>TypeScript SDK for the orq.ai gateway whose beta classify resource runs typed noul, choice and score questions against classify models such as typesafe/jev-latest.<br><sub>Also: <a href="https://orq.ai">app</a> · <a href="https://github.com/orq-ai/orq-node">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/aio-proxy/aio-proxy/tree/main/packages/server/src/routes/systemone"><img src="https://opengraph.githubassets.com/1/aio-proxy/aio-proxy" alt="aio-proxy System One route" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/aio-proxy/aio-proxy/tree/main/packages/server/src/routes/systemone">aio-proxy System One route</a></b><br><sub>aio-proxy · GitHub · ⭐ 9 repo · 2026-07-02</sub><br>Self-hosted multi-provider API proxy that exposes a TypeSafe System One route (POST /v1/systemone) alongside its OpenAI-style endpoints.<br><sub>Also: <a href="https://aioproxy.dev">app</a> · <a href="https://github.com/aio-proxy/aio-proxy">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/orq-ai/orq-python/blob/main/src/orq_ai_sdk/classify.py"><img src="https://opengraph.githubassets.com/1/orq-ai/orq-python" alt="orq.ai classify API (Python)" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/orq-ai/orq-python/blob/main/src/orq_ai_sdk/classify.py">orq.ai classify API (Python)</a></b><br><sub>orq-ai · GitHub · ⭐ 9 repo · 2022-05-25</sub><br>Python SDK for the orq.ai gateway with a classify resource that runs typed noul, choice and score questions against classify models such as typesafe/jev.<br><sub>Also: <a href="https://orq.ai">app</a> · <a href="https://github.com/orq-ai/orq-python">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Routstr/routstrd/blob/main/src/daemon/http/request-body.ts"><img src="https://opengraph.githubassets.com/1/Routstr/routstrd" alt="routstrd System One pass-through" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Routstr/routstrd/blob/main/src/daemon/http/request-body.ts">routstrd System One pass-through</a></b><br><sub>Routstr · GitHub · ⭐ 9 repo · 2026-03-02</sub><br>Local daemon for the Routstr provider network that forwards TypeSafe /v1/systemone request bodies verbatim, since the strict endpoint rejects the chat-completion fields it adds elsewhere.<br><sub>Also: <a href="https://github.com/Routstr/routstrd">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/OpenRouterTeam/docs/blob/main/guides/community/typesafe-sdk.mdx"><img src="https://opengraph.githubassets.com/1/OpenRouterTeam/docs" alt="OpenRouter TypeSafe SDK guide" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/OpenRouterTeam/docs/blob/main/guides/community/typesafe-sdk.mdx">OpenRouter TypeSafe SDK guide</a></b><br><sub>OpenRouter · Docs · ⭐ 8 repo · 2026-03-26</sub><br>Documentation page from OpenRouter on pointing the official TypeSafe JavaScript or Python SDK at OpenRouter's base URL to run Jev through the System One API with OpenRouter billing.<br><sub>Also: <a href="https://github.com/OpenRouterTeam/docs">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/0gfoundation/0g-serving-broker/blob/main/api/inference/internal/ctrl/decisions.go"><img src="https://opengraph.githubassets.com/1/0gfoundation/0g-serving-broker" alt="0G Serving Broker decisions" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/0gfoundation/0g-serving-broker/blob/main/api/inference/internal/ctrl/decisions.go">0G Serving Broker decisions</a></b><br><sub>0gfoundation · GitHub · ⭐ 7 repo · 2024-06-25</sub><br>Provider broker for the 0G Compute Network with a decisions handler that proxies OpenRouter Decisions-style requests such as typesafe/jev-1.13 and bills them from the usage block.<br><sub>Also: <a href="https://github.com/0gfoundation/0g-serving-broker">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/soyelmismo/openproxy/blob/master/docs/decision-engine.md"><img src="https://raw.githubusercontent.com/soyelmismo/openproxy/master/docs/dashboard-hero.png" alt="openproxy decision engine" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/soyelmismo/openproxy/blob/master/docs/decision-engine.md">openproxy decision engine</a></b><br><sub>soyelmismo · GitHub · ⭐ 7 repo · 2026-06-21</sub><br>Self-hosted LLM gateway whose decision engine routes prompts with System One models, either Jev as an HTTP upstream or local Laya ONNX in process, and exposes its own /v1/systemone endpoint.<br><sub>Also: <a href="https://github.com/soyelmismo/openproxy">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/phaseoteam/Phaseo/tree/main/apps/api/src/protocols/typesafe-systemone"><img src="https://repository-images.githubusercontent.com/1000745244/8fe6f157-a60f-48a6-9517-4d27e549c7e7" alt="Phaseo TypeSafe System One support" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/phaseoteam/Phaseo/tree/main/apps/api/src/protocols/typesafe-systemone">Phaseo TypeSafe System One support</a></b><br><sub>phaseoteam · GitHub · ⭐ 7 repo · 2025-06-12</sub><br>System One protocol and executor in Phaseo, an OpenAI-compatible AI gateway with health-aware routing and cost and latency telemetry, so Jev decision requests can be sent through the gateway.<br><sub>Also: <a href="https://phaseo.app">app</a> · <a href="https://github.com/phaseoteam/Phaseo">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://developers.cloudflare.com/ai/models/typesafe/jev/"><img src="https://developers.cloudflare.com/og-docs.png" alt="Cloudflare Workers AI" width="240"></a></td>
<td valign="top"><b><a href="https://developers.cloudflare.com/ai/models/typesafe/jev/">Cloudflare Workers AI</a></b><br><sub>Cloudflare · Docs</sub><br>Calls Jev from a Worker with <code>env.AI.run</code>, with examples for refund review, department routing, and risk scoring.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://openrouter.ai/typesafe/jev"><img src="https://openrouter.ai/en-US/typesafe/jev/opengraph-image-vc0va0?221bbfd60a40d134" alt="Jev on OpenRouter" width="240"></a></td>
<td valign="top"><b><a href="https://openrouter.ai/typesafe/jev">Jev on OpenRouter</a></b><br><sub>OpenRouter · Hugging Face</sub><br>OpenRouter's model page for typesafe/jev, which serves Jev through OpenRouter's Decisions API alongside its other models.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://www.requesty.ai/blog/typesafe-jev-explained"><img src="https://www.requesty.ai/blog/typesafe-jev-explained/01-jev-vs-llms.png" alt="Jev on Requesty" width="240"></a></td>
<td valign="top"><b><a href="https://www.requesty.ai/blog/typesafe-jev-explained">Jev on Requesty</a></b><br><sub>Requesty (Thibault Jaigu) · Article · 2026-09-19</sub><br>Practical guide to Jev that shows how to call it through Requesty's OpenAI-compatible router as typesafe/jev-latest, using the questions response format, with pricing math and caveats.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://docs.venice.ai/models/overview"><img src="https://venice.ai/social.webp" alt="Jev on Venice" width="240"></a></td>
<td valign="top"><b><a href="https://docs.venice.ai/models/overview">Jev on Venice</a></b><br><sub>Venice · Hugging Face</sub><br>Venice API lists Jev (System One) as a beta model under the id jev-latest, so it can be called through Venice's private-inference API.<br><sub>Also: <a href="https://venice.ai">site</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://vercel.com/ai-gateway/models/jev"><img src="https://vercel.com/api/model-og?name=Jev&amp;subtitle=typesafe-ai%2Fjev" alt="Jev on Vercel AI Gateway" width="240"></a></td>
<td valign="top"><b><a href="https://vercel.com/ai-gateway/models/jev">Jev on Vercel AI Gateway</a></b><br><sub>Vercel · Hugging Face</sub><br>Vercel AI Gateway model page for typesafe-ai/jev with pricing and a playground; the gateway also supports TypeSafe clients and an HTTP API for Jev.<br><sub>Also: <a href="https://vercel.com/ai-gateway">gateway</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"></td>
<td valign="top"><b><a href="https://docs.litellm.ai/docs/pass_through/typesafe">LiteLLM pass-through</a></b><br><sub>LiteLLM · Docs</sub><br>Routes the System One evaluate endpoint through a LiteLLM proxy for key management, logging and cost tracking priced from response usage; streaming is unsupported since TypeSafe offers none.</td>
</tr>
<tr>
<td width="260" valign="top"></td>
<td valign="top"><b><a href="https://www.netlify.com/changelog/typesafe-jev-ai-gateway/">Netlify AI Gateway</a></b><br><sub>Netlify · Article</sub><br>Zero-configuration Jev access on Netlify's AI Gateway: Functions call it through @typesafe-ai/sdk with no API keys, while Netlify handles credentials and billing.</td>
</tr>
<tr>
<td width="260" valign="top"></td>
<td valign="top"><b><a href="https://opencode.ai/docs/zen/#jev">OpenCode Zen</a></b><br><sub>OpenCode · Article</sub><br>Hosts Jev on a TypeSafe-compatible endpoint, including a free variant.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://openrouter.ai/typesafe/jev-1.13"><img src="https://openrouter.ai/en-US/typesafe/jev-1.13/opengraph-image-vc0va0?221bbfd60a40d134" alt="OpenRouter" width="240"></a></td>
<td valign="top"><b><a href="https://openrouter.ai/typesafe/jev-1.13">OpenRouter</a></b><br><sub>OpenRouter · App</sub><br>Offers Jev through a separate Decisions API rather than chat completions.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://openrouter.ai/labs/jev"><img src="https://openrouter.ai/dynamic-og?title=Jev+Lab&amp;description=Run+structured+decisions+with+TypeSafe+Jev+through+OpenRouter.&amp;v=2" alt="OpenRouter Jev Lab" width="240"></a></td>
<td valign="top"><b><a href="https://openrouter.ai/labs/jev">OpenRouter Jev Lab</a></b><br><sub>OpenRouter · Article</sub><br>Runnable recipes for ticket triage, agent action approval, candidate extraction, feed filtering, and more.</td>
</tr>
<tr>
<td width="260" valign="top"></td>
<td valign="top"><b><a href="https://docs.typesafe.ai/api">System One API</a></b><br><sub>TypeSafe AI · Docs</sub><br>Official HTTP endpoint for Jev: POST a state and typed questions to /v1/systemone and get typed answers with probabilities and confidence back.</td>
</tr>
<tr>
<td width="260" valign="top"></td>
<td valign="top"><b><a href="https://console.typesafe.ai/">TypeSafe console</a></b><br><sub>TypeSafe AI · App</sub><br>Official console for creating API keys, trying Jev in the playground and inspecting live requests.<br><sub>Also: <a href="https://x.com/typesafeai/status/2101786156572823624">announcement</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://vercel.com/changelog/typesafe-ai-jev-now-available-on-ai-gateway"><img src="https://assets.vercel.com/image/upload/contentful/image/e5382hct74si/69YLGxKpc3pTIH8tHrLFgo/51d3f9dc460bf3e7b1c4fdd7a4d757f1/image__104_.png" alt="Vercel AI Gateway" width="240"></a></td>
<td valign="top"><b><a href="https://vercel.com/changelog/typesafe-ai-jev-now-available-on-ai-gateway">Vercel AI Gateway</a></b><br><sub>Vercel · Article</sub><br>Serves typesafe-ai/jev on Vercel's AI Gateway through the AI SDK's experimental evaluate interface, where the Boolean primitive maps to TypeSafe's Noul.<br><sub>Also: <a href="https://x.com/vercel_dev/status/2100378959653507175">announcement</a></sub></td>
</tr>
</table>

Missing something? [Suggest a resource](https://github.com/Li-Evan/awesome-jev/issues/new/choose).
