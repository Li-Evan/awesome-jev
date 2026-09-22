# 🔌 用 Jev 开发: 模型访问

[English](https://github.com/Li-Evan/awesome-jev/blob/main/pages/build-model-access.md) · **简体中文**

从你的技术栈调用 Jev 的方式：托管访问、框架适配、可观测性和社区 SDK。共 68 条，按社区热度排序。

[← 返回 Awesome Jev](https://github.com/Li-Evan/awesome-jev/blob/main/README.zh-CN.md#模型访问)

**模型访问** · [框架适配](https://github.com/Li-Evan/awesome-jev/blob/main/zh-CN/pages/build-frameworks.md) (174) · [可观测性](https://github.com/Li-Evan/awesome-jev/blob/main/zh-CN/pages/build-observability.md) (14) · [社区 SDK](https://github.com/Li-Evan/awesome-jev/blob/main/zh-CN/pages/build-community-sdks.md) (107)

<table>
<tr>
<td width="260" valign="top"><a href="https://github.com/anomalyco/opencode/blob/dev/packages/web/src/content/docs/zen.mdx"><img src="https://raw.githubusercontent.com/anomalyco/opencode/dev/packages/web/src/assets/lander/screenshot.png" alt="OpenCode Zen 的 Jev 端点" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/anomalyco/opencode/blob/dev/packages/web/src/content/docs/zen.mdx">OpenCode Zen 的 Jev 端点</a></b><br><sub>anomalyco · 文档 · ⭐ 209.2k 仓库 · 2025-04-30</sub><br>OpenCode 的 Zen 网关在 /v1/systemone 端点提供 Jev 1.13，使用 Zen API 密钥，另有限时免费的 jev-1.13-free 模型。<br><sub>相关: <a href="https://opencode.ai/docs/zen">docs</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/OpenRouter/status/2100744709589316009"><img src="https://pbs.twimg.com/amplify_video_thumb/2100744692048818176/img/lnRQ8fZbTFSI0YuV.jpg" alt="OpenRouter 上的 Jev" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/OpenRouter/status/2100744709589316009">OpenRouter 上的 Jev</a></b><br><sub>OpenRouter · X · ♥ 3.9k · 2026-09-18</sub><br>OpenRouter 宣布 Jev 已通过其 API 开放 beta，返回带概率的类型化决策，而不是生成文本。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/get-convex/convex-backend/blob/main/npm-packages/docs/docs/ai-gateway/api.mdx"><img src="https://opengraph.githubassets.com/1/get-convex/convex-backend" alt="Convex AI Gateway 的 Jev 支持" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/get-convex/convex-backend/blob/main/npm-packages/docs/docs/ai-gateway/api.mdx">Convex AI Gateway 的 Jev 支持</a></b><br><sub>get-convex · 文档 · ⭐ 12.6k 仓库 · 2024-03-08</sub><br>Convex 的 AI Gateway 通过 decisions 端点以 typesafe/jev-1.13 提供 Jev，可在 Convex action 中借助 AI SDK 的 evaluate 和 @convex-dev/ai-sdk-provider 包调用。<br><sub><b>Jev 用法:</b> 认证使用短期有效的部署令牌，每次决策的美元成本会在 provider metadata 中返回。</sub><br><sub>相关: <a href="https://github.com/get-convex/convex-backend/tree/main/npm-packages/@convex-dev/ai-sdk-provider">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/sabrinaesaquino/status/2101102660997017747"><img src="https://pbs.twimg.com/amplify_video_thumb/2101101845225865216/img/cubmkjzFZ8i2sPKp.jpg" alt="Venice API 上的 Jev" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/sabrinaesaquino/status/2101102660997017747">Venice API 上的 Jev</a></b><br><sub>sabrinaesaquino · X · ♥ 221 · 2026-09-19</sub><br>为 Jev 在 Venice API 上开放 beta 而做的演示：约 2 分钟内把 24,000 条 Hacker News 帖子分到 12 个类别。<br><sub>相关: <a href="https://x.com/AskVenice/status/2101095644467511578">announcement</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/maximhq/bifrost/tree/dev/core/providers/typesafe"><img src="https://opengraph.githubassets.com/1/maximhq/bifrost" alt="Bifrost 的 TypeSafe 提供方" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/maximhq/bifrost/tree/dev/core/providers/typesafe">Bifrost 的 TypeSafe 提供方</a></b><br><sub>maximhq · GitHub · ⭐ 8.2k 仓库 · 2025-03-19</sub><br>Bifrost AI 网关中的 TypeSafe 提供方，提供可直接替换的 /typesafe 前缀，为 api.typesafe.ai 编写的客户端（包括官方 SDK）无需改动就能经由 Bifrost 使用。<br><sub><b>Jev 用法:</b> 覆盖 Noul、Choice 和 Score，支持 jev-latest 别名解析和模型列表，并附有面向网关和 Go SDK 的 decisions 快速上手指南。</sub><br><sub>相关: <a href="https://www.getmaxim.ai/bifrost">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/tbphp/gpt-load/blob/main/internal/channel/modules/jev.go"><img src="https://repository-images.githubusercontent.com/997490512/48207872-b9e0-4e70-8006-0becdc6507ff" alt="GPT-Load 的 Jev 渠道" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/tbphp/gpt-load/blob/main/internal/channel/modules/jev.go">GPT-Load 的 Jev 渠道</a></b><br><sub>tbphp · GitHub · ⭐ 6.9k 仓库 · 2025-06-06</sub><br>自托管 AI 网关 GPT-Load 的 Jev 渠道模块，把 TypeSafe 官方 API 加为提供方，支持批量导入密钥、调度和故障转移。<br><sub>相关: <a href="https://www.gpt-load.com">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/experientiallabs/experiential/blob/main/exp/runtime/models/providers/typesafe.py"><img src="https://raw.githubusercontent.com/experientiallabs/experiential/main/assets/experiential-workflow.png" alt="Experiential 的 TypeSafe 提供方" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/experientiallabs/experiential/blob/main/exp/runtime/models/providers/typesafe.py">Experiential 的 TypeSafe 提供方</a></b><br><sub>experientiallabs · GitHub · ⭐ 5.4k 仓库 · 2026-06-24</sub><br>开源模型网关 Experiential 中的 TypeSafe 提供方，原生分发 Jev 决策，并拒绝把 Jev 当作聊天模型使用。<br><sub>相关: <a href="https://experientiallabs.ai">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/cloudflare/cloudflare-docs/blob/production/src/content/catalog-models/typesafe-jev.json"><img src="https://opengraph.githubassets.com/1/cloudflare/cloudflare-docs" alt="Cloudflare 的 Jev 模型目录条目" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/cloudflare/cloudflare-docs/blob/production/src/content/catalog-models/typesafe-jev.json">Cloudflare 的 Jev 模型目录条目</a></b><br><sub>cloudflare · 文档 · ⭐ 5.2k 仓库 · 2020-09-03</sub><br>Cloudflare 模型目录中 typesafe/jev 的条目，列出 Jev 可用于 Noul、Choice 和 Score 评估，输入每百万 token $0.042、输出免费，并附一个完整示例。<br><sub>相关: <a href="https://developers.cloudflare.com">docs</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/pollinations/pollinations/blob/main/gen.pollinations.ai/src/text/systemOneClient.ts"><img src="https://raw.githubusercontent.com/pollinations/pollinations/main/packages/ui/src/brand/lockup-horizontal-black.svg" alt="Pollinations 的 Jev API" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/pollinations/pollinations/blob/main/gen.pollinations.ai/src/text/systemOneClient.ts">Pollinations 的 Jev API</a></b><br><sub>pollinations · GitHub · ⭐ 5.1k 仓库 · 2021-04-15</sub><br>Pollinations 的 gen API 通过类型化的 POST /alpha/decisions 端点和 Chat Completions 以 typesafe/jev-1.13 提供 Jev，另有一个带 jev_decide 工具的 Ask Jev MCP 服务器。<br><sub>相关: <a href="https://gen.pollinations.ai/docs">docs</a> · <a href="https://pollinations.ai">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/flydotio/status/2102076230183035081"><img src="https://pbs.twimg.com/media/HSwTDxlaEAMHET8.jpg?name=orig" alt="Fly.io Sprites 上的 Jev" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/flydotio/status/2102076230183035081">Fly.io Sprites 上的 Jev</a></b><br><sub>flydotio · X · ♥ 81 · 2026-09-21</sub><br>Fly.io 为 Sprites 提供的 TypeSafe 连接器，在网关处注入你的 Jev API 密钥，运行在硬件隔离 Sprites 里的 agent 调用 Jev 时密钥无需进入沙箱。<br><sub>相关: <a href="https://fly.io/sprites/jev">docs</a> · <a href="https://fly.io/sprites/jev">project</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://zenmux.ai/docs/api/typesafe/systemone"><img src="https://cdn.marmot-cloud.com/storage/zenmux/2025/09/16/lAK3vlZ/banner.png" alt="ZenMux 的 TypeSafe System One API" width="240"></a></td>
<td valign="top"><b><a href="https://zenmux.ai/docs/api/typesafe/systemone">ZenMux 的 TypeSafe System One API</a></b><br><sub>ZenMux · 文档 · ⭐ 75 · 2026-09-20</sub><br>API 参考文档，介绍如何经由 ZenMux 模型网关用 Jev 发起 TypeSafe System One 评估请求。<br><sub>相关: <a href="https://github.com/ZenMux/zenmux-doc/blob/main/docs_source/en/api/typesafe/systemone.md">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"></td>
<td valign="top"><b><a href="https://docs.venice.ai/api-reference/endpoint/decisions/systemone">Venice 的 System One 兼容接口</a></b><br><sub>Venice · 文档 · ⭐ 65 · 2026-09-18</sub><br>Venice 的 API 参考文档，介绍其 Decisions API 兼容 TypeSafe 的别名 POST /systemone，让 System One 客户端可以通过 Venice 调用 Jev。<br><sub>相关: <a href="https://github.com/veniceai/api-docs/blob/main/api-reference/endpoint/decisions/systemone.mdx">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/theagentrouter/agent-router/tree/main/internal/apischema/typesafe"><img src="https://raw.githubusercontent.com/theagentrouter/agent-router/main/site/static/img/brand/ar-horizontal-primary.svg" alt="Agent Router 的 TypeSafe schema" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/theagentrouter/agent-router/tree/main/internal/apischema/typesafe">Agent Router 的 TypeSafe schema</a></b><br><sub>theagentrouter · GitHub · ⭐ 2.1k 仓库 · 2024-10-21</sub><br>基于 Envoy 的 AI 网关 Agent Router（前身是 Envoy AI Gateway）加入了 TypeSafe System One 的请求和响应 schema，让 Jev 的 /v1/systemone 可以经由它路由。<br><sub><b>Jev 用法:</b> state、instructions 和 criteria 以原始 JSON 保留，网关从不改写其结构。</sub><br><sub>相关: <a href="https://theagentrouter.ai/">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/HarnessRouter/harnessrouter/blob/main/runner/systemone_driver.py"><img src="https://raw.githubusercontent.com/HarnessRouter/harnessrouter/main/docs/images/github-readme-star-cta-desktop.svg" alt="HarnessRouter 的 systemone base" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/HarnessRouter/harnessrouter/blob/main/runner/systemone_driver.py">HarnessRouter 的 systemone base</a></b><br><sub>HarnessRouter · GitHub · ⭐ 2k 仓库 · 2026-08-09</sub><br>自托管的 agent harness 统一接口 HarnessRouter 运行一个 systemone base，分别以 TypeSafe API 或 OpenRouter 各自的模型 id 提供 Jev。<br><sub><b>Jev 用法:</b> 目录中只有 systemone base 列出了 jev 的 id，每一轮请求通过两种接入方式之一提供服务。</sub><br><sub>相关: <a href="https://harnessrouter.ai/">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/yomorun/yomo/blob/main/src/model_api_provider/providers/typesafe_systemone.rs"><img src="https://user-images.githubusercontent.com/65603/162367572-5a0417fa-e2b2-4d35-8c92-2c95d461706d.png" alt="YoMo 的 TypeSafe System One 提供方" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/yomorun/yomo/blob/main/src/model_api_provider/providers/typesafe_systemone.rs">YoMo 的 TypeSafe System One 提供方</a></b><br><sub>yomorun · GitHub · ⭐ 1.9k 仓库 · 2020-07-01</sub><br>serverless 边缘 AI agent 框架 YoMo 新增了 TypeSafe System One 提供方，通过其地理分布式的模型 API 层代理 Jev 决策请求。<br><sub>相关: <a href="https://yomo.run">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/beam-cloud/beta9/blob/main/sdk/src/beta9/abstractions/managed_endpoint.py"><img src="https://raw.githubusercontent.com/beam-cloud/beta9/main/static/beam-logo-white.png" alt="Beam 托管的 System One 端点" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/beam-cloud/beta9/blob/main/sdk/src/beta9/abstractions/managed_endpoint.py">Beam 托管的 System One 端点</a></b><br><sub>beam-cloud · GitHub · ⭐ 1.8k 仓库 · 2023-11-15</sub><br>Beam 的 serverless GPU 运行时可以托管 decision 类型的托管端点，按 TypeSafe 的 /v1/systemone 约定提供 System One 模型。<br><sub><b>Jev 用法:</b> 端点的 decision 类型决定使用 /v1/systemone 路由；调用方发送的就是模型名。</sub><br><sub>相关: <a href="https://beam.cloud">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/theopenco/llmgateway/blob/main/packages/models/src/models/typesafe.ts"><img src="https://opengraph.githubassets.com/1/theopenco/llmgateway" alt="LLM Gateway 的 TypeSafe 模型" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/theopenco/llmgateway/blob/main/packages/models/src/models/typesafe.ts">LLM Gateway 的 TypeSafe 模型</a></b><br><sub>theopenco · GitHub · ⭐ 1.7k 仓库 · 2025-04-12</sub><br>在 LLM Gateway 中把 Jev 1.13 注册为 TypeSafe 决策模型，通过统一网关把 state 加问题的请求路由到 /v1/systemone 端点。<br><sub>相关: <a href="https://llmgateway.io">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"></td>
<td valign="top"><b><a href="https://docs.litellm.ai/blog/typesafe_jev">LiteLLM 上的 TypeSafe Jev</a></b><br><sub>LiteLLM · 文章 · ⭐ 32 · 2026-09-20</sub><br>LiteLLM 宣布其代理（v1.103.0-rc）可透传 TypeSafe 的 /v1/systemone 端点，带日志和成本追踪，客户端用 LiteLLM 虚拟密钥即可调用 Jev。<br><sub>相关: <a href="https://github.com/BerriAI/litellm-docs/tree/main/blog/typesafe_jev">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/dgrid_ai/status/2102231668040040687"><img src="https://pbs.twimg.com/media/HSyghV2bQAAKh8Q.jpg?name=orig" alt="DGrid 上的 Jev" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/dgrid_ai/status/2102231668040040687">DGrid 上的 Jev</a></b><br><sub>dgrid_ai · X · ♥ 17 · 2026-09-22</sub><br>DGrid 把 Jev 1.13 加入模型目录，处理路由、分类和评分请求，每次调用可包含多个类型化问题。<br><sub>相关: <a href="https://dgrid.ai/models/typesafe/jev-1.13">app</a> · <a href="https://dgrid.ai/models/typesafe/jev-1.13">project</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"></td>
<td valign="top"><b><a href="https://docs.aimlapi.com/api-references/decision-models/typesafe/jev">AI/ML API 上的 Jev</a></b><br><sub>AI/ML API · 文档 · ⭐ 28 · 2024-05-28</sub><br>AI/ML API 的文档，介绍如何在其 decision-models API 下以 typesafe/jev 提供 TypeSafe Jev，附带 playground 和 state 加问题请求的 Python/Node.js 代码片段。<br><sub>相关: <a href="https://github.com/aimlapi/api-docs/tree/main/docs/api-references/decision-models/TypeSafe">repo</a> · <a href="https://aimlapi.com/app/typesafe/jev">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/astaxie/TokenHub/blob/main/docs/semantic-routing.md"><img src="https://raw.githubusercontent.com/astaxie/TokenHub/main/frontend/public/brand/tokenhub-logo.png" alt="TokenHub 的 Jev 语义路由" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/astaxie/TokenHub/blob/main/docs/semantic-routing.md">TokenHub 的 Jev 语义路由</a></b><br><sub>astaxie · GitHub · ⭐ 1.3k 仓库 · 2026-06-10</sub><br>企业级 AI 网关 TokenHub 可以用 Jev 为符合条件的 Chat Completions 请求，在基础路由给出的候选中选定提供方和上游模型。<br><sub><b>Jev 用法:</b> 每个请求一个 Choice，返回某个候选或 no_preference；有 observe 和 enforce 两种模式，置信度阈值 0.65，每个请求最多调用一次。</sub><br><sub>相关: <a href="https://thinkinai-labs.github.io/tokenhome/">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/yym68686/uni-api-web"><img src="https://opengraph.githubassets.com/1/yym68686/uni-api-web" alt="uni-api 的 TypeSafe 渠道" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/yym68686/uni-api-web">uni-api 的 TypeSafe 渠道</a></b><br><sub>yym68686 · GitHub · ⭐ 26 · 2025-03-11</sub><br>自托管 uni-api LLM 网关的 Web 控制台，可添加 typesafe 引擎渠道，代理 POST /v1/systemone，让 Jev 的 Choice、Noul 和 Score 问题经由网关发送。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/yym68686/uni-api/blob/main/scripts/verify_typesafe.py"><img src="https://opengraph.githubassets.com/1/yym68686/uni-api" alt="uni-api 的 TypeSafe 后端" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/yym68686/uni-api/blob/main/scripts/verify_typesafe.py">uni-api 的 TypeSafe 后端</a></b><br><sub>yym68686 · GitHub · ⭐ 1.3k 仓库 · 2024-07-04</sub><br>为带负载均衡的统一 LLM API 网关 uni-api 加入 TypeSafe Jev 后端，让决策请求和其他提供方一样走同一套 OpenAI 风格接口。<br><sub>相关: <a href="https://0-0.pro/r/uniapi">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/croit/aiplane"><img src="https://raw.githubusercontent.com/croit/aiplane/main/docs/img/architecture.svg" alt="croit AIplane" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/croit/aiplane">croit AIplane</a></b><br><sub>croit · GitHub · ⭐ 23 · 2026-06-17</sub><br>自托管 AI 网关，提供兼容 TypeSafe System One 的 /v1/systemone 端点，官方 SDK 可直接把它设为 base URL；另有基于 System One 的自动模型路由，以及 GDPR/NDA 内容防护。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/unorouter/new-api-sync"><img src="https://opengraph.githubassets.com/1/unorouter/new-api-sync" alt="new-api-sync 的 TypeSafe 提供方" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/unorouter/new-api-sync">new-api-sync 的 TypeSafe 提供方</a></b><br><sub>unorouter · GitHub · ⭐ 21 · 2026-01-15</sub><br>new-api 网关的同步引擎（UnoRouter 在用），带一个 typesafe 提供方类型，把 Jev 从 OpenRouter 的 decisions 路由同步进网关，并设定自己的售价和 32,000 token 上下文。<br><sub>相关: <a href="https://unorouter.com">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/top-think/think-ai"><img src="https://opengraph.githubassets.com/1/top-think/think-ai" alt="ThinkAI 的决策 API" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/top-think/think-ai">ThinkAI 的决策 API</a></b><br><sub>top-think · GitHub · ⭐ 9 · 2023-12-28</sub><br>ThinkAI 模型聚合服务的 PHP SDK，其 decision() 资源可评估 Jev 的 noul 和 choice 问题（模型 jev-latest），与聊天、图像和语音 API 并列。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/braintrustdata/braintrust-proxy/blob/main/packages/proxy/scripts/sync_typesafe.ts"><img src="https://opengraph.githubassets.com/1/braintrustdata/braintrust-proxy" alt="Braintrust AI Proxy 的 TypeSafe 提供方" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/braintrustdata/braintrust-proxy/blob/main/packages/proxy/scripts/sync_typesafe.ts">Braintrust AI Proxy 的 TypeSafe 提供方</a></b><br><sub>braintrustdata · GitHub · ⭐ 410 仓库 · 2023-11-22</sub><br>在 Braintrust AI proxy 中加入 TypeSafe 提供方，附带一个脚本，从 TypeSafe models API 和文档同步 Jev 的模型 ID、别名和按 token 计价。<br><sub>相关: <a href="https://www.braintrustdata.com/docs/guides/proxy">docs</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/genlayerlabs/unhardcoded"><img src="https://opengraph.githubassets.com/1/genlayerlabs/unhardcoded" alt="unhardcoded" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/genlayerlabs/unhardcoded">unhardcoded</a></b><br><sub>genlayerlabs · GitHub · ⭐ 8 · 2026-06-22</sub><br>兼容 OpenAI 的 LLM 路由器，按调用方提供的策略为每个请求挑选模型，并以同样的选择和回退逻辑通过 POST /v1/decisions 提供 Jev 等决策模型。<br><sub>相关: <a href="https://github.com/genlayerlabs/unhardcoded/blob/main/docs/DECISION-MODELS.md">docs</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/AgentsDanceAI/AIStore"><img src="https://opengraph.githubassets.com/1/AgentsDanceAI/AIStore" alt="AI Store" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/AgentsDanceAI/AIStore">AI Store</a></b><br><sub>AgentsDanceAI · GitHub · ⭐ 7 · 2026-08-21</sub><br>为三十款托管的开源 AI 产品提供账号、积分和工作区的一层服务，同时把自托管的 Laya 决策模型和 TypeSafe 托管的 Jev 作为按量计费的槽位提供。<br><sub>相关: <a href="https://aistore.best">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Muvon/octohub"><img src="https://opengraph.githubassets.com/1/Muvon/octohub" alt="OctoHub" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Muvon/octohub">OctoHub</a></b><br><sub>Muvon · GitHub · ⭐ 7 · 2026-03-19</sub><br>Rust 编写的 LLM 代理，用一套 OpenAI 风格 API 覆盖 20+ 个提供方，支持多租户密钥和请求日志，配置中可把评估模型“jev”映射到 TypeSafe 或 Cloudflare。<br><sub>相关: <a href="https://octomind.run/product/octohub/">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/OpenRouterTeam/typescript-sdk/blob/main/docs/sdks/systemone/README.mdx"><img src="https://raw.githubusercontent.com/OpenRouterTeam/typescript-sdk/main/assets/banner.png" alt="OpenRouter TypeScript SDK 的 System One 资源" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/OpenRouterTeam/typescript-sdk/blob/main/docs/sdks/systemone/README.mdx">OpenRouter TypeScript SDK 的 System One 资源</a></b><br><sub>OpenRouterTeam · GitHub · ⭐ 254 仓库 · 2025-08-21</sub><br>OpenRouter 官方 TypeScript SDK 的资源，把 state 和类型化问题发给 Jev 这类 System One 模型，并把 jev-latest 这样的裸 ID 映射到 typesafe/ 命名空间下。<br><sub>相关: <a href="https://github.com/OpenRouterTeam/typescript-sdk/blob/main/src/sdk/systemone.ts">code</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/RyanKung/rotom"><img src="https://raw.githubusercontent.com/RyanKung/rotom/master/demos/claude-grok-4.3.gif" alt="rotom" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/RyanKung/rotom">rotom</a></b><br><sub>RyanKung · GitHub · ⭐ 5 · 2026-04-27</sub><br>用 Rust 写的本地 API 网关，兼容 OpenAI 和 Anthropic，可让任意客户端复用 Codex、Grok、Kiro 或 Vercel AI Gateway 的登录，也通过其模型目录和评估端点提供 Jev。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/mcowger/plexus/blob/main/packages/backend/src/types/decisions.ts"><img src="https://raw.githubusercontent.com/mcowger/plexus/main/assets/readme/hero.svg" alt="Plexus 的 decisions 网关" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/mcowger/plexus/blob/main/packages/backend/src/types/decisions.ts">Plexus 的 decisions 网关</a></b><br><sub>mcowger · GitHub · ⭐ 234 仓库 · 2025-12-01</sub><br>统一的 LLM API 网关，新增 Jev 风格的 decisions 端点，把 state 加问题的请求路由到 TypeSafe /v1/systemone 或 OpenRouter 的 decisions API。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/OpenRouterTeam/python-sdk/blob/main/src/openrouter/systemone.py"><img src="https://raw.githubusercontent.com/OpenRouterTeam/python-sdk/main/assets/banner.png" alt="OpenRouter Python SDK 的 System One 模块" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/OpenRouterTeam/python-sdk/blob/main/src/openrouter/systemone.py">OpenRouter Python SDK 的 System One 模块</a></b><br><sub>OpenRouterTeam · GitHub · ⭐ 160 仓库 · 2025-08-22</sub><br>OpenRouter 官方 Python SDK 模块，可通过 OpenRouter 把 state 和类型化问题发给 Jev 这类 System One 模型。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/t0ng7u/status/2102062876819374482"><img src="https://pbs.twimg.com/amplify_video_thumb/2102062812709449728/img/SVBMGP0wAoKqO6J1.jpg" alt="New API 的 Jev 插件" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/t0ng7u/status/2102062876819374482">New API 的 Jev 插件</a></b><br><sub>t0ng7u · X · ♥ 3 · 2026-09-21</sub><br>通过自托管 New API 网关暴露 Jev 的 Choice、Score 和 Noul 的插件，官方 TypeSafe SDK 只需指向该网关即可使用，无需改代码。<br><sub>相关: <a href="https://newapi.pro/zh/plugins">plugins</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/FFatTiger/new-api-plugin-typesafe"><img src="https://opengraph.githubassets.com/1/FFatTiger/new-api-plugin-typesafe" alt="new-api-plugin-typesafe" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/FFatTiger/new-api-plugin-typesafe">new-api-plugin-typesafe</a></b><br><sub>FFatTiger · GitHub · ⭐ 3 · 2026-09-18</sub><br>面向自托管 QuantumNous new-api 网关的任务插件，通过原生 /v1/systemone 协议提供 Jev 并按 token 计费，上游可选 TypeSafe 或 Vercel AI Gateway。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/hackclub/ai/blob/main/src/routes/proxy/v1/jev.ts"><img src="https://opengraph.githubassets.com/1/hackclub/ai" alt="Hack Club AI 的 Jev 端点" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/hackclub/ai/blob/main/src/routes/proxy/v1/jev.ts">Hack Club AI 的 Jev 端点</a></b><br><sub>hackclub · GitHub · ⭐ 133 仓库 · 2026-09-17</sub><br>Hack Club 面向青少年的免费 AI 代理中的 Jev 转发路由，复用其 Hack Club 认证、API 密钥、消费限额和用量日志。<br><sub>相关: <a href="https://github.com/hackclub/ai">repo</a> · <a href="https://ai.hackclub.com">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Routstr/routstr-core/blob/main/routstr/upstream/typesafe.py"><img src="https://opengraph.githubassets.com/1/Routstr/routstr-core" alt="Routstr 的 TypeSafe 上游" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Routstr/routstr-core/blob/main/routstr/upstream/typesafe.py">Routstr 的 TypeSafe 上游</a></b><br><sub>Routstr · GitHub · ⭐ 81 仓库 · 2025-04-08</sub><br>去中心化、按请求付费的 AI 推理代理，用 Cashu 比特币微支付结算，新增了 TypeSafe System One 决策端点和 Jev 模型目录。<br><sub>相关: <a href="http://docs.routstr.com/">docs</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/OpenRouterTeam/go-sdk/blob/main/systemone.go"><img src="https://raw.githubusercontent.com/OpenRouterTeam/go-sdk/main/assets/banner.png" alt="OpenRouter Go SDK 的 System One 支持" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/OpenRouterTeam/go-sdk/blob/main/systemone.go">OpenRouter Go SDK 的 System One 支持</a></b><br><sub>OpenRouterTeam · GitHub · ⭐ 70 仓库 · 2025-11-13</sub><br>OpenRouter 官方 Go SDK 的支持，可通过 OpenRouter 把 state 和类型化问题发给 Jev 这类 System One 模型。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/AntSeed/antseed/tree/main/plugins/provider-typesafe"><img src="https://opengraph.githubassets.com/1/AntSeed/antseed" alt="AntSeed 的 TypeSafe 提供方" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/AntSeed/antseed/tree/main/plugins/provider-typesafe">AntSeed 的 TypeSafe 提供方</a></b><br><sub>AntSeed · GitHub · ⭐ 57 仓库 · 2026-02-24</sub><br>点对点 AI 推理市场，提供方可以通过 provider-typesafe 插件出售 TypeSafe System One 决策，买方通过 DHT 发现它们。<br><sub>相关: <a href="https://antseed.com">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/sxueck/llm-gateway/blob/main/packages/backend/src/routes/openai/decisions-handler.ts"><img src="https://github.com/user-attachments/assets/a69d7e89-5225-4c2e-bae3-d11faddc9b56" alt="LLM Gateway 的 System One 端点" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/sxueck/llm-gateway/blob/main/packages/backend/src/routes/openai/decisions-handler.ts">LLM Gateway 的 System One 端点</a></b><br><sub>sxueck · GitHub · ⭐ 52 仓库 · 2025-10-05</sub><br>带 Web UI 的自托管分布式 LLM 网关，新增 decisions 代理处理器，让发往 Jev 的 System One 请求经过它的路由、密钥和用量日志。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/6Kmfi6HP/opencode2api/blob/main/internal/app/systemone.go"><img src="https://opengraph.githubassets.com/1/6Kmfi6HP/opencode2api" alt="opencode2api 的 System One 代理" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/6Kmfi6HP/opencode2api/blob/main/internal/app/systemone.go">opencode2api 的 System One 代理</a></b><br><sub>6Kmfi6HP · GitHub · ⭐ 49 仓库 · 2026-06-04</sub><br>本地代理，把 OpenCode Zen 和 Go 的模型以 OpenAI 和 Anthropic API 的形式暴露出来，并为 Jev 决策请求加了一条 System One 路由。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/netlify/context-and-tools/tree/main/skills/netlify-ai-gateway"><img src="https://opengraph.githubassets.com/1/netlify/context-and-tools" alt="Netlify AI Gateway 的 agent skill" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/netlify/context-and-tools/tree/main/skills/netlify-ai-gateway">Netlify AI Gateway 的 agent skill</a></b><br><sub>netlify · GitHub · ⭐ 37 仓库 · 2025-11-26</sub><br>Netlify 为其 AI Gateway 提供的官方 agent skill，把 TypeSafe Jev 列为自动注入凭证的提供方，并演示一个 Netlify Function 用一个 Choice 把联系表单提交分流到销售、客服或垃圾信息。<br><sub>相关: <a href="https://github.com/netlify/context-and-tools">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/chatbotkit/platform/blob/main/platform/lib/model.provider.typesafe.ts"><img src="https://opengraph.githubassets.com/1/chatbotkit/platform" alt="ChatBotKit 平台的决策接口" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/chatbotkit/platform/blob/main/platform/lib/model.provider.typesafe.ts">ChatBotKit 平台的决策接口</a></b><br><sub>chatbotkit · GitHub · ⭐ 26 仓库 · 2026-09-03</sub><br>开源 ChatBotKit AI 后端中的决策 API（/api/v1/decision/create），通过 TypeSafe、OpenRouter 或 Vercel AI Gateway 提供方处理类型化问题，超时和重试都有上限。<br><sub>相关: <a href="https://cbk.ai">app</a> · <a href="https://github.com/chatbotkit/platform">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Lore-Hex/quill-router/blob/main/src/trusted_router/data/provider_models/typesafe.json"><img src="https://opengraph.githubassets.com/1/Lore-Hex/quill-router" alt="TrustedRouter 上的 Jev" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Lore-Hex/quill-router/blob/main/src/trusted_router/data/provider_models/typesafe.json">TrustedRouter 上的 Jev</a></b><br><sub>Lore-Hex · GitHub · ⭐ 23 仓库 · 2026-05-02</sub><br>运行在硬件 enclave 中的端到端加密 LLM 网关 TrustedRouter，在 decide 端点上以 typesafe-ai/jev 列出 TypeSafe AI Jev，输入价格每小时从 TypeSafe 的模型页面刷新一次。<br><sub>相关: <a href="https://github.com/Lore-Hex/quill-router">repo</a> · <a href="https://trustedrouter.com">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/sapiom/sapiom-js/blob/main/packages/tools/src/llm/decide.ts"><img src="https://opengraph.githubassets.com/1/sapiom/sapiom-js" alt="Sapiom llm.decide" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/sapiom/sapiom-js/blob/main/packages/tools/src/llm/decide.ts">Sapiom llm.decide</a></b><br><sub>sapiom · GitHub · ⭐ 20 仓库 · 2025-11-11</sub><br>Sapiom agent SDK 中的 llm.decide 能力，经 Sapiom 的 Capability Router 调用 Jev，对类型化的 Noul、Choice 和 Score 问题返回调用方自定义答案上的校准概率。<br><sub>相关: <a href="https://github.com/sapiom/sapiom-js">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/QuantumNous/new-api-plugins/tree/main/plugins/tasks/typesafe"><img src="https://opengraph.githubassets.com/1/QuantumNous/new-api-plugins" alt="new-api 的 TypeSafe 插件" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/QuantumNous/new-api-plugins/tree/main/plugins/tasks/typesafe">new-api 的 TypeSafe 插件</a></b><br><sub>QuantumNous · GitHub · ⭐ 16 仓库 · 2026-08-19</sub><br>new-api 网关的官方任务插件，在 POST /typesafe/v1/systemone 提供 Jev（jev-1.13.0、jev-latest、jev-preview），按实际输入 token 计费、输出免费，可直连，也可经由另一个 new-api 网关。<br><sub>相关: <a href="https://github.com/QuantumNous/new-api-plugins">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/orq-ai/orq-node/blob/main/src/sdk/classify.ts"><img src="https://opengraph.githubassets.com/1/orq-ai/orq-node" alt="orq.ai 的 classify API" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/orq-ai/orq-node/blob/main/src/sdk/classify.ts">orq.ai 的 classify API</a></b><br><sub>orq-ai · GitHub · ⭐ 11 仓库 · 2023-12-27</sub><br>orq.ai 网关的 TypeScript SDK，其 beta 版 classify 资源可以针对 typesafe/jev-latest 等分类模型运行类型化的 noul、choice 和 score 问题。<br><sub>相关: <a href="https://orq.ai">app</a> · <a href="https://github.com/orq-ai/orq-node">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/aio-proxy/aio-proxy/tree/main/packages/server/src/routes/systemone"><img src="https://opengraph.githubassets.com/1/aio-proxy/aio-proxy" alt="aio-proxy 的 System One 路由" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/aio-proxy/aio-proxy/tree/main/packages/server/src/routes/systemone">aio-proxy 的 System One 路由</a></b><br><sub>aio-proxy · GitHub · ⭐ 9 仓库 · 2026-07-02</sub><br>自托管的多提供方 API 代理，在 OpenAI 风格的端点之外还提供一个 TypeSafe System One 路由（POST /v1/systemone）。<br><sub>相关: <a href="https://aioproxy.dev">app</a> · <a href="https://github.com/aio-proxy/aio-proxy">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/orq-ai/orq-python/blob/main/src/orq_ai_sdk/classify.py"><img src="https://opengraph.githubassets.com/1/orq-ai/orq-python" alt="orq.ai 的 classify API（Python）" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/orq-ai/orq-python/blob/main/src/orq_ai_sdk/classify.py">orq.ai 的 classify API（Python）</a></b><br><sub>orq-ai · GitHub · ⭐ 9 仓库 · 2022-05-25</sub><br>orq.ai 网关的 Python SDK，带一个 classify 资源，可以针对 typesafe/jev 等分类模型运行类型化的 noul、choice 和 score 问题。<br><sub>相关: <a href="https://orq.ai">app</a> · <a href="https://github.com/orq-ai/orq-python">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Routstr/routstrd/blob/main/src/daemon/http/request-body.ts"><img src="https://opengraph.githubassets.com/1/Routstr/routstrd" alt="routstrd 的 System One 透传" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Routstr/routstrd/blob/main/src/daemon/http/request-body.ts">routstrd 的 System One 透传</a></b><br><sub>Routstr · GitHub · ⭐ 9 仓库 · 2026-03-02</sub><br>Routstr 提供方网络的本地守护进程，会原样转发 TypeSafe /v1/systemone 的请求体，因为这个严格的端点会拒绝它在其他请求里添加的 chat-completion 字段。<br><sub>相关: <a href="https://github.com/Routstr/routstrd">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/OpenRouterTeam/docs/blob/main/guides/community/typesafe-sdk.mdx"><img src="https://opengraph.githubassets.com/1/OpenRouterTeam/docs" alt="OpenRouter 的 TypeSafe SDK 指南" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/OpenRouterTeam/docs/blob/main/guides/community/typesafe-sdk.mdx">OpenRouter 的 TypeSafe SDK 指南</a></b><br><sub>OpenRouter · 文档 · ⭐ 8 仓库 · 2026-03-26</sub><br>OpenRouter 的文档页面，讲如何把官方 TypeSafe JavaScript 或 Python SDK 指向 OpenRouter 的 base URL，通过 System One API 运行 Jev 并由 OpenRouter 计费。<br><sub>相关: <a href="https://github.com/OpenRouterTeam/docs">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/0gfoundation/0g-serving-broker/blob/main/api/inference/internal/ctrl/decisions.go"><img src="https://opengraph.githubassets.com/1/0gfoundation/0g-serving-broker" alt="0G Serving Broker 的决策接口" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/0gfoundation/0g-serving-broker/blob/main/api/inference/internal/ctrl/decisions.go">0G Serving Broker 的决策接口</a></b><br><sub>0gfoundation · GitHub · ⭐ 7 仓库 · 2024-06-25</sub><br>0G Compute Network 的提供方代理（broker），其中的 decisions 处理器会转发 OpenRouter Decisions 风格的请求（如 typesafe/jev-1.13），并根据 usage 块计费。<br><sub>相关: <a href="https://github.com/0gfoundation/0g-serving-broker">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/soyelmismo/openproxy/blob/master/docs/decision-engine.md"><img src="https://raw.githubusercontent.com/soyelmismo/openproxy/master/docs/dashboard-hero.png" alt="openproxy 的决策引擎" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/soyelmismo/openproxy/blob/master/docs/decision-engine.md">openproxy 的决策引擎</a></b><br><sub>soyelmismo · GitHub · ⭐ 7 仓库 · 2026-06-21</sub><br>自托管 LLM 网关，其决策引擎用 System One 模型路由提示词，可以把 Jev 作为 HTTP 上游，也可以在进程内运行本地 Laya ONNX，并对外暴露自己的 /v1/systemone 端点。<br><sub>相关: <a href="https://github.com/soyelmismo/openproxy">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/phaseoteam/Phaseo/tree/main/apps/api/src/protocols/typesafe-systemone"><img src="https://repository-images.githubusercontent.com/1000745244/8fe6f157-a60f-48a6-9517-4d27e549c7e7" alt="Phaseo 的 TypeSafe System One 支持" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/phaseoteam/Phaseo/tree/main/apps/api/src/protocols/typesafe-systemone">Phaseo 的 TypeSafe System One 支持</a></b><br><sub>phaseoteam · GitHub · ⭐ 7 仓库 · 2025-06-12</sub><br>为 Phaseo（兼容 OpenAI 的 AI 网关，支持按健康状态路由，并提供成本和延迟遥测）加入的 System One 协议和执行器，让 Jev 决策请求可以经由该网关发送。<br><sub>相关: <a href="https://phaseo.app">app</a> · <a href="https://github.com/phaseoteam/Phaseo">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://developers.cloudflare.com/ai/models/typesafe/jev/"><img src="https://developers.cloudflare.com/og-docs.png" alt="Cloudflare Workers AI" width="240"></a></td>
<td valign="top"><b><a href="https://developers.cloudflare.com/ai/models/typesafe/jev/">Cloudflare Workers AI</a></b><br><sub>Cloudflare · 文档</sub><br>在 Worker 中用 <code>env.AI.run</code> 调用 Jev，附有退款审核、部门路由和风险评分的示例。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://openrouter.ai/typesafe/jev"><img src="https://openrouter.ai/en-US/typesafe/jev/opengraph-image-vc0va0?221bbfd60a40d134" alt="OpenRouter 上的 Jev" width="240"></a></td>
<td valign="top"><b><a href="https://openrouter.ai/typesafe/jev">OpenRouter 上的 Jev</a></b><br><sub>OpenRouter · Hugging Face</sub><br>OpenRouter 上 typesafe/jev 的模型页面，通过 OpenRouter 的 Decisions API 与其他模型一起提供 Jev。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://www.requesty.ai/blog/typesafe-jev-explained"><img src="https://www.requesty.ai/blog/typesafe-jev-explained/01-jev-vs-llms.png" alt="Requesty 上的 Jev" width="240"></a></td>
<td valign="top"><b><a href="https://www.requesty.ai/blog/typesafe-jev-explained">Requesty 上的 Jev</a></b><br><sub>Requesty (Thibault Jaigu) · 文章 · 2026-09-19</sub><br>Jev 实用指南，演示如何通过 Requesty 兼容 OpenAI 的路由器以 typesafe/jev-latest 调用它、使用 questions 响应格式，附有价格计算和注意事项。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://docs.venice.ai/models/overview"><img src="https://venice.ai/social.webp" alt="Venice 上的 Jev" width="240"></a></td>
<td valign="top"><b><a href="https://docs.venice.ai/models/overview">Venice 上的 Jev</a></b><br><sub>Venice · Hugging Face</sub><br>Venice API 把 Jev（System One）列为 beta 模型，id 为 jev-latest，可以通过 Venice 的私密推理 API 调用。<br><sub>相关: <a href="https://venice.ai">site</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://vercel.com/ai-gateway/models/jev"><img src="https://vercel.com/api/model-og?name=Jev&amp;subtitle=typesafe-ai%2Fjev" alt="Vercel AI Gateway 上的 Jev" width="240"></a></td>
<td valign="top"><b><a href="https://vercel.com/ai-gateway/models/jev">Vercel AI Gateway 上的 Jev</a></b><br><sub>Vercel · Hugging Face</sub><br>Vercel AI Gateway 上 typesafe-ai/jev 的模型页面，含价格和 playground；该网关还支持 TypeSafe 客户端以及调用 Jev 的 HTTP API。<br><sub>相关: <a href="https://vercel.com/ai-gateway">gateway</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"></td>
<td valign="top"><b><a href="https://docs.litellm.ai/docs/pass_through/typesafe">LiteLLM 透传</a></b><br><sub>LiteLLM · 文档</sub><br>把 System One 的 evaluate 端点经由 LiteLLM 代理转发，用于密钥管理、日志记录和按响应 usage 计价的成本追踪；由于 TypeSafe 本身不提供流式输出，这里也不支持流式。</td>
</tr>
<tr>
<td width="260" valign="top"></td>
<td valign="top"><b><a href="https://www.netlify.com/changelog/typesafe-jev-ai-gateway/">Netlify AI Gateway</a></b><br><sub>Netlify · 文章</sub><br>在 Netlify 的 AI Gateway 上零配置使用 Jev：Functions 通过 @typesafe-ai/sdk 调用，无需 API 密钥，凭证和计费由 Netlify 处理。</td>
</tr>
<tr>
<td width="260" valign="top"></td>
<td valign="top"><b><a href="https://opencode.ai/docs/zen/#jev">OpenCode Zen</a></b><br><sub>OpenCode · 文章</sub><br>在兼容 TypeSafe 的端点上托管 Jev，其中包括一个免费版本。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://openrouter.ai/typesafe/jev-1.13"><img src="https://openrouter.ai/en-US/typesafe/jev-1.13/opengraph-image-vc0va0?221bbfd60a40d134" alt="OpenRouter" width="240"></a></td>
<td valign="top"><b><a href="https://openrouter.ai/typesafe/jev-1.13">OpenRouter</a></b><br><sub>OpenRouter · 应用</sub><br>通过独立的 Decisions API 而非 chat completions 提供 Jev。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://openrouter.ai/labs/jev"><img src="https://openrouter.ai/dynamic-og?title=Jev+Lab&amp;description=Run+structured+decisions+with+TypeSafe+Jev+through+OpenRouter.&amp;v=2" alt="OpenRouter Jev Lab" width="240"></a></td>
<td valign="top"><b><a href="https://openrouter.ai/labs/jev">OpenRouter Jev Lab</a></b><br><sub>OpenRouter · 文章</sub><br>可直接运行的示例配方，涵盖工单分诊、agent 动作审批、候选信息提取、信息流过滤等。</td>
</tr>
<tr>
<td width="260" valign="top"></td>
<td valign="top"><b><a href="https://docs.typesafe.ai/api">System One API</a></b><br><sub>TypeSafe AI · 文档</sub><br>Jev 的官方 HTTP 端点：把 state 和类型化问题 POST 到 /v1/systemone，拿回带概率和置信度的类型化答案。</td>
</tr>
<tr>
<td width="260" valign="top"></td>
<td valign="top"><b><a href="https://console.typesafe.ai/">TypeSafe 控制台</a></b><br><sub>TypeSafe AI · 应用</sub><br>官方控制台，可以创建 API 密钥、在 playground 里试用 Jev、查看实时请求。<br><sub>相关: <a href="https://x.com/typesafeai/status/2101786156572823624">announcement</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://vercel.com/changelog/typesafe-ai-jev-now-available-on-ai-gateway"><img src="https://assets.vercel.com/image/upload/contentful/image/e5382hct74si/69YLGxKpc3pTIH8tHrLFgo/51d3f9dc460bf3e7b1c4fdd7a4d757f1/image__104_.png" alt="Vercel AI Gateway" width="240"></a></td>
<td valign="top"><b><a href="https://vercel.com/changelog/typesafe-ai-jev-now-available-on-ai-gateway">Vercel AI Gateway</a></b><br><sub>Vercel · 文章</sub><br>通过 AI SDK 的实验性 evaluate 接口在 Vercel AI Gateway 上提供 typesafe-ai/jev，其中 Boolean 原语对应 TypeSafe 的 Noul。<br><sub>相关: <a href="https://x.com/vercel_dev/status/2100378959653507175">announcement</a></sub></td>
</tr>
</table>

还缺什么？[提交一个资源](https://github.com/Li-Evan/awesome-jev/issues/new/choose)。
