# 🤖 Agent 与编排

[English](https://github.com/Li-Evan/awesome-jev/blob/main/scenarios/agents.md) · **简体中文**

通用 agent 的工具与 skill 选择、审批、规划、记忆和 harness 决策。共 246 条，按社区热度排序。

[← 返回 Awesome Jev](https://github.com/Li-Evan/awesome-jev/blob/main/README.zh-CN.md#按场景浏览)

<table>
<tr>
<td width="260" valign="top"><a href="https://github.com/Significant-Gravitas/AutoGPT/tree/master/autogpt_platform/backend/backend/blocks/typesafe"><img src="https://raw.githubusercontent.com/Significant-Gravitas/AutoGPT/master/docs/home/.gitbook/assets/Banner_image.png" alt="AutoGPT TypeSafe blocks" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Significant-Gravitas/AutoGPT/tree/master/autogpt_platform/backend/backend/blocks/typesafe">AutoGPT TypeSafe blocks</a></b><br><sub>Significant-Gravitas · GitHub · ⭐ 187.5k 仓库 · 2023-03-16</sub><br>七个无代码模块，包括一个五出口路由器、一个是/否/不确定三路分流，以及一个分数过滤器。<br><sub><b>Jev 用法:</b> 模块调用 TypeSafe Python SDK 的 system_one，让可视化 agent 工作流能根据 Choice、Noul 和 Score 的答案分支。</sub><br><sub>相关: <a href="https://agpt.co">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/0xCodila/status/2101433560796467348"><img src="https://pbs.twimg.com/amplify_video_thumb/2101426271842349056/img/uEiR8K0UCaFoYsf-.jpg" alt="jev-usage-router" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/0xCodila/status/2101433560796467348">jev-usage-router</a></b><br><sub>0xCodila · X · ♥ 2.4k · 2026-09-19</sub><br>Grok Bot 的用量路由器：在浏览、研究、重试或额外启动机器人之前，由一个 Jev Choice 选择路由；正式启用前有影子模式、日志和紧急开关。<br><sub><b>Jev 用法:</b> 每次高成本的 agent 操作前调用一次 Choice，决定走哪条路由。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/_aj/status/2102061534956662818"><img src="https://pbs.twimg.com/media/HSwFAsyawAA4tst.jpg?name=orig" alt="AgentRun" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/_aj/status/2102061534956662818">AgentRun</a></b><br><sub>_aj · X · ♥ 1.6k · 2026-09-21</sub><br>Grep.ai 推出的 harness，面向重复性知识工作，在运行中学会这项工作，把步骤从 LLM 调用逐步转为代码；处理 100,000 条合规告警花费不到 $26K，而用 Opus 5 要超过 $290K。<br><sub>相关: <a href="https://x.com/MiguelriosEN/status/2100840456200581120">article</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/BerriAI/litellm/blob/main/litellm/router_strategy/complexity_router/jev_classifier.py"><img src="https://opengraph.githubassets.com/1/BerriAI/litellm" alt="LiteLLM Jev complexity router" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/BerriAI/litellm/blob/main/litellm/router_strategy/complexity_router/jev_classifier.py">LiteLLM Jev complexity router</a></b><br><sub>BerriAI · GitHub · ⭐ 59.4k 仓库 · 2026-09-17</sub><br>在 LiteLLM 基于复杂度的路由器中，可以用 Jev 把每个请求归入配置好的档位，据此选择后端模型；另有一个护栏，会清空 Jev 判断为不再需要的工具结果。<br><sub><b>Jev 用法:</b> 路由时每个请求做一个档位 Choice；压缩护栏对每次完成的工具交互问一个是/否 Noul。</sub><br><sub>相关: <a href="https://github.com/BerriAI/litellm">repo</a> · <a href="https://github.com/BerriAI/litellm/tree/main/litellm/proxy/guardrails/guardrail_hooks/typesafe">guardrail</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/eve/status/2100430918762832180"><img src="https://pbs.twimg.com/media/HSY6yf5a8AA8NJi.jpg?name=orig" alt="eve 中基于标准的模型路由" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/eve/status/2100430918762832180">eve 中基于标准的模型路由</a></b><br><sub>eve · X · ♥ 910 · 2026-09-17</sub><br>eve agent 框架中的实验性 autoModel 选项，用 Jev 在多个以自然语言标准描述的模型之间为每个请求做路由。<br><sub><b>Jev 用法:</b> 在候选模型之间做 Choice，每个模型以一段描述为键，例如“Complex reasoning and engineering tasks”（复杂推理和工程任务）。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/ephraimduncan/status/2100454070536351824"><img src="https://pbs.twimg.com/amplify_video_thumb/2100454021852954624/img/hqULLONlXw40573G.jpg" alt="Jev 模型路由器" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/ephraimduncan/status/2100454070536351824">Jev 模型路由器</a></b><br><sub>ephraimduncan · X · ♥ 1.9k · 2026-09-17</sub><br>模型路由器，询问 Jev 哪个语言模型最适合每个传入请求，再把请求转发给该模型，附演示视频。<br><sub><b>Jev 用法:</b> 每个请求在可用模型上做一个 Choice。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/CodingGarden/status/2100665210419950031"><img src="https://pbs.twimg.com/amplify_video_thumb/2100664410935332864/img/KPApgq0AysL_SFeg.jpg" alt="不用 LLM 的聊天机器人" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/CodingGarden/status/2100665210419950031">不用 LLM 的聊天机器人</a></b><br><sub>CodingGarden · X · ♥ 1.2k · 2026-09-17</sub><br>完全不用 LLM 构建的聊天助手：Jev 在网页搜索、Wikipedia、天气、Todoist 和 Home Assistant 之间挑选工具及其参数，带引用的回答即时返回。<br><sub><b>Jev 用法:</b> 每个提示词做一次工具 Choice，外加参数选择。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/corentAI/status/2100965880242770423"><img src="https://pbs.twimg.com/amplify_video_thumb/2100964784581525504/img/S0fJrRk_X0OFZhdh.jpg" alt="Corent model routing" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/corentAI/status/2100965880242770423">Corent model routing</a></b><br><sub>corentAI · X · ♥ 320 · 2026-09-18</sub><br>Corent 的路由器用 Jev 判断每个请求在 1000+ 个模型中需要什么、这个判断有多大把握，以及是走该路由还是回退；对一段 $2 的视频这类高成本任务，置信度要求更严格。<br><sub><b>Jev 用法:</b> 路由用一个 Choice，按工作负载设置置信度阈值，达不到就回退。</sub><br><sub>相关: <a href="http://corent.tech">app</a> · <a href="https://corent.tech">project</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/tinyhumansai/openhuman/tree/main/crates/openhuman-tinyhumans/src/jev"><img src="https://raw.githubusercontent.com/tinyhumansai/openhuman/main/gitbooks/.gitbook/assets/demo.png" alt="OpenHuman Jev tool ranker" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/tinyhumansai/openhuman/tree/main/crates/openhuman-tinyhumans/src/jev">OpenHuman Jev tool ranker</a></b><br><sub>tinyhumansai · GitHub · ⭐ 40k 仓库 · 2026-02-18</sub><br>OpenHuman agent harness 的工具搜索排序器，先用 BM25 为延迟加载的工具列出候选清单，再让一个 Jev Choice 选出正确的工具，未登录时回退到 BM25。<br><sub><b>Jev 用法:</b> BM25 先筛到 20 个候选，再做一个 3 秒时限的 Choice，经后端的 OpenRouter System One 代理转发。</sub><br><sub>相关: <a href="https://tinyhumans.ai/openhuman">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/PrefectHQ/fastmcp/blob/main/fastmcp_slim/fastmcp/experimental/transforms/jev_search.py"><img src="https://raw.githubusercontent.com/PrefectHQ/fastmcp/main/docs/assets/brand/f-watercolor-waves-2.png" alt="FastMCP Jev tool search" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/PrefectHQ/fastmcp/blob/main/fastmcp_slim/fastmcp/experimental/transforms/jev_search.py">FastMCP Jev tool search</a></b><br><sub>PrefectHQ · GitHub · ⭐ 27.9k 仓库 · 2024-11-30</sub><br>实验性的 FastMCP 变换，用 Jev 给服务器的工具目录排序：先在一行摘要上做一次大范围 Choice，再结合完整描述细读入围名单。<br><sub><b>Jev 用法:</b> 一个 Choice 给入围名单排序，每个候选再用一个 Noul 确认它确实能完成请求，因此没有工具能满足的查询会返回空结果。</sub><br><sub>相关: <a href="https://gofastmcp.com">docs</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://www.youtube.com/watch?v=o4Vi5uBZYH0"><img src="https://i.ytimg.com/vi/o4Vi5uBZYH0/hqdefault.jpg" alt="Treg + Jev 自动化" width="240"></a></td>
<td valign="top"><b><a href="https://www.youtube.com/watch?v=o4Vi5uBZYH0">Treg + Jev 自动化</a></b><br><sub>AI Jason · 视频 · ♥ 856 · 2026-09-21</sub><br>演示把 Jev 与 OpenRouter 风格的 agent 工具注册表 Treg 搭配，构建由 Jev 负责快速决策的自动化工作流。<br><sub>相关: <a href="https://github.com/superdesigndev/treg">repo</a> · <a href="https://treg.to/jev">prompt</a> · <a href="https://github.com/superdesigndev/treg">project</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/MiguelriosEN/status/2101033282414768456"><img src="https://pbs.twimg.com/amplify_video_thumb/2101032781270917120/img/8tGv1qWQd8M9mEec.jpg" alt="AgentRun" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/MiguelriosEN/status/2101033282414768456">AgentRun</a></b><br><sub>MiguelriosEN · X · ♥ 311 · 2026-09-18</sub><br>用 pi 和 Jev 搭建的 agent harness：agent 先学会如何完成一项工作，给自己写出一个通用、可复用的解决方案，然后就退出流程。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/omarsar0/status/2101443311454036477"><img src="https://pbs.twimg.com/amplify_video_thumb/2101443076828925952/img/zVy7_B-F8UmXFdKK.jpg" alt="目标完成验证器" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/omarsar0/status/2101443311454036477">目标完成验证器</a></b><br><sub>omarsar0 · X · ♥ 1k · 2026-09-19</sub><br>为某个 agent harness 的 /goal 功能定制的验证器，每轮结束后用 Jev 检查目标是否真的完成，取代了昂贵的推理模型。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/RoundtableSpace/status/2102167236714574280"><img src="https://pbs.twimg.com/amplify_video_thumb/2102148770343407616/img/-rVahOyOBdklAAqC.jpg" alt="HarnessRouter" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/RoundtableSpace/status/2102167236714574280">HarnessRouter</a></b><br><sub>RoundtableSpace · X · ♥ 61 · 2026-09-21</sub><br>开源层，把 Codex、Claude Code、Hermes、DeepSeek Harness、一个由 Jev 驱动的 System One harness 以及另外 9 个 harness 统一到一个接口背后，提供 Unified Harness Protocol 和兼容 OpenAI Responses 的 API。<br><sub>相关: <a href="https://github.com/harnessrouter/harnessrouter">repo</a> · <a href="https://harnessrouter.ai/">app</a> · <a href="https://github.com/harnessrouter/harnessrouter">project</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/rileybrown/status/2100607709317861879"><img src="https://pbs.twimg.com/amplify_video_thumb/2100607557995761664/img/a_foq8dIW_wwab7W.jpg" alt="用 Jev 做模型路由的 agent" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/rileybrown/status/2100607709317861879">用 Jev 做模型路由的 agent</a></b><br><sub>rileybrown · X · ♥ 283 · 2026-09-17</sub><br>一个 agent 项目，由 Jev 充当模型路由器，决定每个请求交给哪个模型处理。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/johnyeo_/status/2100987661926252737"><img src="https://pbs.twimg.com/amplify_video_thumb/2100986453845028864/img/YknQ8SR5kudv19m-.jpg" alt="Slack agent 预路由" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/johnyeo_/status/2100987661926252737">Slack agent 预路由</a></b><br><sub>johnyeo_ · X · ♥ 166 · 2026-09-18</sub><br>在 agent 运行前先让 Jev 根据提示词挑出最合适的 skill、工具和参数，让一个 Slack agent 提速 2 倍。<br><sub><b>Jev 用法:</b> 在 skill 和工具上做 Choice 并挑选参数，然后再交给 LLM agent。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/rashedInt32/jev-mcp"><img src="https://pbs.twimg.com/media/HSeMX0_bYAARs-3.jpg" alt="jev-mcp" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/rashedInt32/jev-mcp">jev-mcp</a></b><br><sub>rashedInt32 · GitHub · ⭐ 6 · 2026-09-17</sub><br>MCP 服务器兼 Claude Code 插件，把 Jev 暴露为 classify、score、check 和批量 ask 工具，返回类型化答案及其完整概率分布。<br><sub>相关: <a href="https://www.npmjs.com/package/jev-mcp">npm</a> · <a href="https://x.com/takamasa045/status/2100809434587124208">write-up</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/kerpopule/hermes-jev-skills"><img src="https://raw.githubusercontent.com/kerpopule/hermes-jev-skills/main/docs/images/model-routing-dashboard.png" alt="Hermes Jev skills" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/kerpopule/hermes-jev-skills">Hermes Jev skills</a></b><br><sub>kerpopule · GitHub · ⭐ 405 · 2026-09-18</sub><br>面向 Hermes、Claude Code 和 Codex 的路由、记忆、skill 选择和分诊 skill，先以影子模式启动，并公开自己的失败案例。<br><sub>相关: <a href="https://x.com/StevenDarlow/status/2101115049280422332">demo</a> · <a href="https://x.com/StevenDarlow/status/2101526148228227519">post</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/ThinkInAIXYZ/deepchat/blob/dev/src/main/provider/providers/jevProvider.ts"><img src="https://opengraph.githubassets.com/1/ThinkInAIXYZ/deepchat" alt="DeepChat Jev judgment model" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/ThinkInAIXYZ/deepchat/blob/dev/src/main/provider/providers/jevProvider.ts">DeepChat Jev judgment model</a></b><br><sub>ThinkInAIXYZ · GitHub · ⭐ 6.3k 仓库 · 2025-02-14</sub><br>桌面 agent 客户端 DeepChat 新增 Jev 作为提供方，并提供一个可选启用的判断模型槽位，通过 System One 协议审核工具权限请求。<br><sub><b>Jev 用法:</b> 按设计，聊天入口使用 Jev 时会直接报错；运行时文件还包含基于 Jev 的工具结果裁剪。</sub><br><sub>相关: <a href="https://github.com/ThinkInAIXYZ/deepchat/blob/dev/docs/features/agent-judgment-model/spec.md">docs</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/BuilderIO/agent-native/blob/main/packages/core/src/agent/jev-tool-prefetch.ts"><img src="https://cdn.builder.io/api/v1/image/assets%2FYJIGb4i01jvw0SRdL5Bt%2F7628600bc10a4940b78f42c5df7628b0" alt="Agent-native tool prefetch" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/BuilderIO/agent-native/blob/main/packages/core/src/agent/jev-tool-prefetch.ts">Agent-native tool prefetch</a></b><br><sub>BuilderIO · GitHub · ⭐ 6.1k 仓库 · 2026-03-12</sub><br>用一个 Choice 为最多 128 个工具和 skill 排序，并在 750 毫秒内预加载排名前三的项。<br><sub>相关: <a href="https://www.agent-native.com">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/JamesWard/status/2100976393546772628"><img src="https://pbs.twimg.com/media/HSgovFqXoAAih_x.png?name=orig" alt="用 Jev 编排 MCP 工作流" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/JamesWard/status/2100976393546772628">用 Jev 编排 MCP 工作流</a></b><br><sub>JamesWard · X · ♥ 298 · 2026-09-18</sub><br>结合 Jev、LLM 和 MCP 的两种模式：Jev 作为外层循环选择合法动作，依据 MCP 输出 schema 构建工作流 AST，最后只用一次 LLM 调用写出最终答案。<br><sub><b>Jev 用法:</b> 每一步在合法动作上做 Choice，然后对 MCP 结果做语义过滤。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/milindlabs/status/2100515910754750741"><img src="https://pbs.twimg.com/amplify_video_thumb/2100515619712184320/img/LFrKN4XyJ024sGe_.jpg" alt="OpenMausBot chief of staff" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/milindlabs/status/2100515910754750741">OpenMausBot chief of staff</a></b><br><sub>milindlabs · X · ♥ 184 · 2026-09-17</sub><br>OpenMausBot 上的多 agent 配置：Jev 读取每个任务，唤醒合适的 agent，并从用户现有的订阅中为每个 agent 分配模型。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/0xPaulius/status/2101312576252481785"><img src="https://pbs.twimg.com/amplify_video_thumb/2101278375423737856/img/AcdfybGwO7dAi1Gu.jpg" alt="Clonk agent canvas" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/0xPaulius/status/2101312576252481785">Clonk agent canvas</a></b><br><sub>0xPaulius · X · ♥ 174 · 2026-09-19</sub><br>画布式 agent 编排器，由 Jev 即时决定启动 agent 等操作，不必等待缓慢的 LLM 循环。<br><sub>相关: <a href="https://clonk.ai">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/shengkunye/status/2102112693041938825"><img src="https://pbs.twimg.com/amplify_video_thumb/2102112249112604672/img/3lR6gxILRYKTiMF_.jpg" alt="借助 Jev 使用 Monid 工具" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/shengkunye/status/2102112693041938825">借助 Jev 使用 Monid 工具</a></b><br><sub>shengkunye · X · ♥ 166 · 2026-09-21</sub><br>Monid 集成，让 agent 通过 OpenRouter 在 2,000 个工具上使用 Jev，完成给 2,000 条线索打分、扫描 TikTok 开头钩子、整理 Reddit 讨论帖等工作，号称提速 30 倍。<br><sub>相关: <a href="https://monid.ai">app</a> · <a href="https://monid.ai">project</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/jkudish/jev-mcp"><img src="https://opengraph.githubassets.com/1/jkudish/jev-mcp" alt="jev-mcp" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/jkudish/jev-mcp">jev-mcp</a></b><br><sub>jkudish · GitHub · ⭐ 247 · 2026-09-17</sub><br>十个面向 agent 的 MCP 判断工具，包括论断核查、注入筛查、重排和把关。<br><sub>相关: <a href="https://x.com/jkudish/status/2100413576284712999">demo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/truespar/sentio"><img src="https://repository-images.githubusercontent.com/1344239263/60e2f09e-0eb6-419c-9533-ef350c19bbab" alt="Sentio SMTP" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/truespar/sentio">Sentio SMTP</a></b><br><sub>truespar · GitHub · ⭐ 246 · 2026-08-23</sub><br>多租户 Rust 邮件服务器，给 AI agent 分配独立收件箱，并可用 Jev 作为邮件分类器给收到的邮件打标签，不改变垃圾邮件评分。<br><sub><b>Jev 用法:</b> 只实现了 MessageClassifier：带校准置信度的 Choice 和 Noul 标签，不生成回复。</sub><br><sub>相关: <a href="https://truespar.com/sentio">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/aipoch/open-science/blob/main/src/main/settings/classification-settings.ts"><img src="https://raw.githubusercontent.com/aipoch/open-science/main/docs/images/readme/open-science-banner.png" alt="Open-Science Jev classification" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/aipoch/open-science/blob/main/src/main/settings/classification-settings.ts">Open-Science Jev classification</a></b><br><sub>aipoch · GitHub · ⭐ 4.9k 仓库 · 2026-07-03</sub><br>AIPOCH Open-Science 研究工作台中的分类服务，用 Jev 判断请求需要哪些 skill，以及某份文档是否应该全文阅读。<br><sub><b>Jev 用法:</b> 通过 TypeSafe、OpenRouter 或自定义端点运行 jev-latest，并设置字节预算，即便是 CJK 文本也能保持在 TypeSafe 的上下文上限之内。</sub><br><sub>相关: <a href="https://aipoch.com/open-science">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/itsmostafa/typesafe-mcp"><img src="https://external-preview.redd.it/foplw_1lcxzLSY41H2Wc8jTRi55au8rxPSdCeT9nTBw.png?auto=webp&amp;s=c9f26ce3c9d2b86f15dc4763a0a17436e965e121" alt="typesafe-mcp" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/itsmostafa/typesafe-mcp">typesafe-mcp</a></b><br><sub>itsmostafa · GitHub · ⭐ 229 · 2026-09-17</sub><br>Go MCP 服务器，暴露一个 evaluate 工具，让 Claude Code、Claude Desktop、Codex 和 pi 把 state 连同 Choice、Score 或 Noul 问题发给 Jev，并根据概率分支。<br><sub>相关: <a href="https://www.reddit.com/r/mcp/comments/1wjfjn3/if_you_have_access_to_the_new_typesafe_ai_try/">discussion</a> · <a href="https://x.com/CindyTaylo82399/status/2101873521077157968">demo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/john_bortotti/status/2102113996505518388"><img src="https://pbs.twimg.com/amplify_video_thumb/2102112486837096449/img/-pAuYpFAhQmzM0uC.jpg" alt="会做判断的角色记忆" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/john_bortotti/status/2102113996505518388">会做判断的角色记忆</a></b><br><sub>john_bortotti · X · ♥ 88 · 2026-09-21</sub><br>Mutuals 的角色记忆系统，每条消息只用一次 Jev 调用来决定：是否保留、保留哪些原话、归到哪里、让哪些旧内容过时，以及它会唤起哪些记忆。<br><sub><b>Jev 用法:</b> 每条收到的消息带多个类型化问题，在一次 Jev 调用中全部回答。</sub><br><sub>相关: <a href="https://mutuals.inc">company</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/kitze/skillbox"><img src="https://opengraph.githubassets.com/1/kitze/skillbox" alt="skillbox" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/kitze/skillbox">skillbox</a></b><br><sub>kitze · GitHub · ⭐ 223 · 2026-09-17</sub><br>自托管、带版本管理的 AI agent skill 库，通过 MCP 向权限受限的客户端提供服务，Jev 可选地从客户端有权访问的 skill 中推荐适合当前任务的那些。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/UnCorped/status/2101707226666893553"><img src="https://pbs.twimg.com/media/HSrBRezaEAEkcmz.jpg" alt="Smriti 接入 Jev" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/UnCorped/status/2101707226666893553">Smriti 接入 Jev</a></b><br><sub>UnCorped · 文章 · ♥ 17 · 2026-09-20</sub><br>给面向 agent 的本地 SQLite 记忆层 Smriti 加上 Jev 的案例研究：Jev 把更多证据拉进了上下文，但有些答案反而变差，重新标注后也只有小幅改善。<br><sub><b>Jev 用法:</b> 在检索到的记忆证据传给回答模型之前给它们打标签。</sub><br><sub>相关: <a href="https://github.com/vn-envy/Smriti">repo</a> · <a href="https://github.com/vn-envy/smriti">project</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/tinyhumansai/opencompany"><img src="https://raw.githubusercontent.com/tinyhumansai/opencompany/main/docs/gitbooks/.gitbook/assets/opencompany-hero.png" alt="OpenCompany" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/tinyhumansai/opencompany">OpenCompany</a></b><br><sub>tinyhumansai · GitHub · ⭐ 196 · 2026-07-10</sub><br>面向一人公司的 agent 蜂巢：Jev 决定一条消息需要找谁、广播由谁接手，没有 key 时回退到工位负责人。<br><sub><b>Jev 用法:</b> 在工位成员加“none”之间做 Choice，经 TinyHumans 代理发送。</sub><br><sub>相关: <a href="https://tinyhumans.ai/opencompany">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/dealerdefi/Jevmind"><img src="https://raw.githubusercontent.com/dealerdefi/Jevmind/main/assets/banner.jpg" alt="Jevmind" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/dealerdefi/Jevmind">Jevmind</a></b><br><sub>dealerdefi · GitHub · ⭐ 164 · 2026-09-15</sub><br>零依赖的 Python 工具包，把 agent 埋在文字里的决策提取成类型化、带置信度的答案，置于代码关卡之后，并记入分级账本；一个开关即可在本地规则大脑和 Jev 之间切换。<br><sub>相关: <a href="https://x.com/dealerdefi/status/2102167087309369731">demo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Foxtailsss-Andy/Anna-Agent"><img src="https://raw.githubusercontent.com/Foxtailsss-Andy/Anna-Agent/main/docs/public/assets/anna-readme-banner-v2.png" alt="Anna" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Foxtailsss-Andy/Anna-Agent">Anna</a></b><br><sub>Foxtailsss-Andy · GitHub · ⭐ 149 · 2026-04-02</sub><br>受治理、本地优先的企业 agent，其 Crew 功能用 Jev 为未分配的任务推荐一个人或 worker，Jev 也可以弃权；它在 22/22 个案例上与 DeepSeek 评判结果一致，p50 延迟低 85.23%。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/BillionsBobby/JevRouter"><img src="https://raw.githubusercontent.com/BillionsBobby/JevRouter/main/docs/assets/jev-api-router-comparison.png" alt="JevRouter" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/BillionsBobby/JevRouter">JevRouter</a></b><br><sub>BillionsBobby · GitHub · ⭐ 148 · 2026-09-18</sub><br>把模型、子 agent、skill、MCP 服务器和 CLI 放进同一个候选池，候选池很大时用两阶段 Choice 做路由。<br><sub>相关: <a href="https://jevrouter.co">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/rlaope/oh-my-hermes/blob/main/src/plugin_bundle/omh/jev_sidekick.py"><img src="https://raw.githubusercontent.com/rlaope/oh-my-hermes/main/assets/oh-my-hermes-wordmark.png" alt="oh-my-hermes Jev posture" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/rlaope/oh-my-hermes/blob/main/src/plugin_bundle/omh/jev_sidekick.py">oh-my-hermes Jev posture</a></b><br><sub>rlaope · GitHub · ⭐ 2.9k 仓库 · 2026-06-03</sub><br>插件 oh-my-hermes 中的模块，检测机器上装了哪些 Jev 类 Hermes 插件，并报告每个插件对其工具、hook 和数据流的声明，但不声称它们实际运行过。<br><sub><b>Jev 用法:</b> 识别以 jev_ 为前缀的工具和已知的 Jev 凭据环境变量名，存在 Jev 类插件时，把工具审批问题交给 Jev。</sub><br><sub>相关: <a href="https://rlaope.github.io/oh-my-hermes/">docs</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/elie222/rakazo/blob/main/packages/adapters/src/jev-auto-review.ts"><img src="https://raw.githubusercontent.com/elie222/rakazo/main/docs/readme-hero.png" alt="Rakazo Jev auto-review" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/elie222/rakazo/blob/main/packages/adapters/src/jev-auto-review.ts">Rakazo Jev auto-review</a></b><br><sub>elie222 · GitHub · ⭐ 2.8k 仓库 · 2026-08-13</sub><br>开源 AI 队友平台 Rakazo 中的自动审查适配器，询问 Jev 某个机器人工具调用应该自动放行，还是发给用户审批。<br><sub><b>Jev 用法:</b> 在 pass 和 ask 之间做一个 Choice，对照置信度阈值；任何意外或高风险的情况默认为 ask。</sub><br><sub>相关: <a href="https://rakazo.com">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/StarchildOnX/status/2100936455401214327"><img src="https://pbs.twimg.com/amplify_video_thumb/2100926778047148032/img/RUW0O6LMX9L7TRzk.jpg" alt="Starchild prompt routing" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/StarchildOnX/status/2100936455401214327">Starchild prompt routing</a></b><br><sub>StarchildOnX · X · ♥ 29 · 2026-09-18</sub><br>Starchild 应用中的 LLM 路由器，实时对提示词分类（平均 140 毫秒），据称提示词分类的成本降低 20 倍、速度提升 6 倍。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/lioensky/VCPToolBox/blob/main/modules/jevClient.js"><img src="https://raw.githubusercontent.com/lioensky/VCPToolBox/main/docs/image/VCPLogo.png" alt="VCPToolBox Jev modules" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/lioensky/VCPToolBox/blob/main/modules/jevClient.js">VCPToolBox Jev modules</a></b><br><sub>lioensky · GitHub · ⭐ 2.3k 仓库 · 2025-05-12</sub><br>VCP agent 基础设施新增 Jev 模块，用于上下文裁剪、折叠过滤、重排和一个语义工具调用实验，支持在 TypeSafe 或 OpenRouter 上轮换多个 key。<br><sub><b>Jev 用法:</b> jevClient 支持 Noul、Choice 和 Score，带重试和 key 轮换；各独立模块把它用于上下文管理和工具选择。</sub><br><sub>相关: <a href="https://www.vcptoolbox.com">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/TianyuCodings/JevHarness"><img src="https://opengraph.githubassets.com/1/TianyuCodings/JevHarness" alt="JevHarness" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/TianyuCodings/JevHarness">JevHarness</a></b><br><sub>TianyuCodings · GitHub · ⭐ 109 · 2026-09-21</sub><br>框架：由强 LLM 编写针对特定任务的 harness，把观察转成 Jev 问题和动作，然后将其冻结，并可选地用 GEPA 根据奖励和完整执行轨迹改进它。<br><sub>相关: <a href="https://jev-harness.tianyuchen99.chatgpt.site">site</a> · <a href="https://jev-harness.tianyuchen99.chatgpt.site">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Dicklesworthstone/skillranker"><img src="https://opengraph.githubassets.com/1/Dicklesworthstone/skillranker" alt="skillranker" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Dicklesworthstone/skillranker">skillranker</a></b><br><sub>Dicklesworthstone · GitHub · ⭐ 109 · 2026-09-17</sub><br>Rust CLI，先用一次大范围 Choice 为当前会话的 skill 排序，再对入围名单逐项用一个 Noul 确认（自定义许可证，有使用限制）。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/k_grajeda/status/2101021361351131464"><img src="https://pbs.twimg.com/amplify_video_thumb/2101018655794331648/img/xm_XTf33FJqqEmIb.jpg" alt="提示词难度分类器" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/k_grajeda/status/2101021361351131464">提示词难度分类器</a></b><br><sub>k_grajeda · X · ♥ 47 · 2026-09-18</sub><br>聊天界面中的检查：用户每次停止输入时就对提示词难度分类，如果是简单提示词，就在用户点发送前提供快速模式。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/HarnessRouter/SystemOneHarness"><img src="https://opengraph.githubassets.com/1/HarnessRouter/SystemOneHarness" alt="System One Harness" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/HarnessRouter/SystemOneHarness">System One Harness</a></b><br><sub>HarnessRouter · GitHub · ⭐ 95 · 2026-09-19</sub><br>Python 控制器，把 System One 模型变成 agent 循环：把环境的有限动作空间编译成类型化 Jev 问题，按置信度把关每一步，并记录完整轨迹。<br><sub>相关: <a href="https://news.ycombinator.com/item?id=49778358">discussion</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/w3cj/jev-chat"><img src="https://raw.githubusercontent.com/w3cj/jev-chat/main/screenshot.png" alt="Jev Chat" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/w3cj/jev-chat">Jev Chat</a></b><br><sub>w3cj · GitHub · ⭐ 85 · 2026-09-18</sub><br>聊天式命令栏：每一轮由 Jev 选定意图、工具、参数值、是否确认以及回复形式，再由代码调用 MCP 服务器并用返回数据组装回复，全程没有模型生成文本。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Devin-AXIS/jev-dsh-decision"><img src="https://raw.githubusercontent.com/Devin-AXIS/jev-dsh-decision/main/assets/jev.png" alt="Jev DSH Decision Engine" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Devin-AXIS/jev-dsh-decision">Jev DSH Decision Engine</a></b><br><sub>Devin-AXIS · GitHub · ⭐ 82 · 2026-09-20</sub><br>agent harness 插件，推荐该用哪个可用的工具、skill 或 agent，并评估输出质量；在 DeepSeek Harness 中原生运行，在 OpenCode 和 Codex Harness 中通过 iPolloWork 运行。<br><sub><b>Jev 用法:</b> 带概率的结构化判断；规划和执行仍由宿主 agent 负责。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/baldaworks/callee"><img src="https://opengraph.githubassets.com/1/baldaworks/callee" alt="Callee" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/baldaworks/callee">Callee</a></b><br><sub>baldaworks · GitHub · ⭐ 74 · 2026-07-14</sub><br>用 Markdown 和 YAML 定义、运行在 ACP 运行时上的 agent 工作流，可混合编程模型、shell 检查和人工步骤，并内置 TypeSafeJev 评估器处理类型化决策和路由。<br><sub>相关: <a href="https://github.com/baldaworks/callee/blob/main/docs/agent-kinds/typesafe-jev.md">docs</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Bodila51/grok-bot-jev"><img src="https://raw.githubusercontent.com/Bodila51/grok-bot-jev/main/media/jev-grok-bot-dashboard.png" alt="Grok Bot Jev Router" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Bodila51/grok-bot-jev">Grok Bot Jev Router</a></b><br><sub>Bodila51 · GitHub · ⭐ 74 · 2026-09-19</sub><br>参考实现的路由器，把 Jev 放在 Grok Bot 前面，在执行高成本的研究、浏览器、重试或子 agent 工作之前先给每个请求分类，选择复用缓存产物、停止重试或询问人类等动作。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/vbcherepanov/total-agent-memory"><img src="https://repository-images.githubusercontent.com/1159027243/9e951761-4a30-40e2-b32a-297ac9223ea7" alt="total-agent-memory" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/vbcherepanov/total-agent-memory">total-agent-memory</a></b><br><sub>vbcherepanov · GitHub · ⭐ 68 · 2026-02-16</sub><br>面向编程 agent 的本地持久记忆，可以用 Jev 检查检索到的事实之间是否矛盾；中位通过时间从 3.1 秒降到 1.9 秒，准确率不变，78 个问题花费 $0.038。<br><sub><b>Jev 用法:</b> 每一对（支持，反对）事实变成一个 Noul，全部放在一次请求里。</sub><br><sub>相关: <a href="https://totalmemory.dev">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/heymrun/heym/blob/main/backend/app/services/decision_models.py"><img src="https://raw.githubusercontent.com/heymrun/heym/main/docs/readme-assets/hero.svg" alt="Heym decision models" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/heymrun/heym/blob/main/backend/app/services/decision_models.py">Heym decision models</a></b><br><sub>heymrun · GitHub · ⭐ 1.2k 仓库 · 2026-03-28</sub><br>自托管 agent 编排运行时 Heym 新增了基于 TypeSafe /v1/systemone 协议的决策模型服务，让工作流可以回答类型化问题，并带有追踪和 SSRF 防护。<br><sub>相关: <a href="https://heym.run">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Asymptote-Labs/agent-beacon/tree/main/cli/beacon/internal/learning"><img src="https://opengraph.githubassets.com/1/Asymptote-Labs/agent-beacon" alt="Beacon Jev memory evaluations" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Asymptote-Labs/agent-beacon/tree/main/cli/beacon/internal/learning">Beacon Jev memory evaluations</a></b><br><sub>Asymptote-Labs · GitHub · ⭐ 926 仓库 · 2026-09-21</sub><br>编程 agent 跨 harness 记忆层 Beacon 中的评测命令，让 Jev 按评分标准判断脱敏后的会话轨迹投影里有没有可复用的经验，保存前由人工复核。<br><sub>相关: <a href="https://beacon.sh">site</a> · <a href="https://github.com/Asymptote-Labs/agent-beacon">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/rohanarun/computer-use-cache"><img src="https://storage.googleapis.com/cheatlayer/landing/computer-use-cache-super-api-hero.jpeg" alt="computer-use-cache" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/rohanarun/computer-use-cache">computer-use-cache</a></b><br><sub>rohanarun · GitHub · ⭐ 42 · 2026-06-04</sub><br>兼容 OpenAI 接口的缓存代理，用于重放重复的电脑操控（computer use）和编程 agent 请求。精确匹配未命中时，Jev 会比对最近的缓存请求，选出一个可复用的响应或判定都不行；任何不确定的请求都转发到上游。<br><sub><b>Jev 用法:</b> 在最多 8 个缓存候选加“无”之间做一次 Choice，置信度达到 0.95 才接受；命中的响应带有 X-Computer-Use-Cache-Match: jev 标记。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/lioensky/VCPChat/blob/main/modules/services/globalJevService.js"><img src="https://raw.githubusercontent.com/lioensky/VCPChat/main/assets/E1-Vchat%E4%B8%BB%E7%95%8C%E9%9D%A2.jpg" alt="VCPChat global Jev service" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/lioensky/VCPChat/blob/main/modules/services/globalJevService.js">VCPChat global Jev service</a></b><br><sub>lioensky · GitHub · ⭐ 778 仓库 · 2025-06-02</sub><br>VCP AI 原生引擎的桌面终端 VCPChat 新增全局 Jev 服务，让各模块可以通过 TypeSafe 或 OpenRouter 做类型化决策。<br><sub><b>Jev 用法:</b> 基于共享的 jevClient，为 typesafe（jev-latest）和 openrouter（~typesafe/jev-latest）设置了提供方默认值。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/kitfunso/hippo-memory/blob/master/src/rerankers/jev.ts"><img src="https://raw.githubusercontent.com/kitfunso/hippo-memory/master/assets/hippo-init.svg" alt="Hippo Jev reranker" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/kitfunso/hippo-memory/blob/master/src/rerankers/jev.ts">Hippo Jev reranker</a></b><br><sub>kitfunso · GitHub · ⭐ 752 仓库 · 2026-03-15</sub><br>Hippo agent 记忆系统中可选启用的重排器，对召回的前 40 条记忆批量做 Jev Noul 判断，并以本地 cross-encoder 作回退；作者的研究发现排序变好了，但回答质量没有提升。<br><sub>相关: <a href="https://github.com/kitfunso/hippo-memory">repo</a> · <a href="https://hippo-memory.com">website</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/shantanugoel/ask-jev-skill"><img src="https://opengraph.githubassets.com/1/shantanugoel/ask-jev-skill" alt="askjev" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/shantanugoel/ask-jev-skill">askjev</a></b><br><sub>shantanugoel · GitHub · ⭐ 37 · 2026-09-17</sub><br>Hermes skill，也可供其他 agent 使用，把 Jev 当作类型化的裁决者来调用，让 agent 在拿到高置信度的 Choice、Score 或 Noul 答案时直接行动，否则升级处理。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/tacticocc/Jevbridge"><img src="https://opengraph.githubassets.com/1/tacticocc/Jevbridge" alt="Jevbridge" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/tacticocc/Jevbridge">Jevbridge</a></b><br><sub>tacticocc · GitHub · ⭐ 37 · 2026-09-18</sub><br>ACP 和 MCP 适配器加 CLI，把 Jev 的类型化决策放在 Codex、Claude、Grok 和 OpenCode 旁边，用于路由、把关、打分和电脑操控（computer use），并带离线规则后端。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/alexjhancock/status/2100932130196852896"><img src="https://pbs.twimg.com/amplify_video_thumb/2100932017512763392/img/Xe2wlgj78FcAayZ2.jpg" alt="Goose 中的即时模型选择" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/alexjhancock/status/2100932130196852896">Goose 中的即时模型选择</a></b><br><sub>alexjhancock · X · ♥ 22 · 2026-09-18</sub><br>Goose agent harness 的原型功能：让 Jev 读取每个提示词，在这一轮开始前挑选由哪个模型运行。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/0xkaushik_k/status/2100928490367230201"><img src="https://pbs.twimg.com/amplify_video_thumb/2100928298834374656/img/LvjSbqapVvdNdvrK.jpg" alt="JevScope" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/0xkaushik_k/status/2100928490367230201">JevScope</a></b><br><sub>0xkaushik_k · X · ♥ 10 · 2026-09-18</sub><br>观察 AI agent 的工作过程，按步骤绘制任务对齐度、进展、重复和卡住程度的判断曲线，演示中抓到了一个在竞态条件上反复打转的编程 agent。<br><sub><b>Jev 用法:</b> 对 agent 轨迹的每一步做判断：是否与任务一致、是否有进展、是否在重复、是否卡住。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/automateyournetwork/netclaw/tree/main/scripts/jev-audit"><img src="https://raw.githubusercontent.com/automateyournetwork/netclaw/main/netclaw.jpg" alt="NetClaw jev-audit" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/automateyournetwork/netclaw/tree/main/scripts/jev-audit">NetClaw jev-audit</a></b><br><sub>automateyournetwork · GitHub · ⭐ 664 仓库 · 2026-02-19</sub><br>网络 agent NetClaw 中的 skill 审计扫描，用 Jev 标记含糊的触发条件、缺失的失败处理、过时的假设和注入嫌疑，并梳理 skill 之间的重叠和覆盖缺口。<br><sub><b>Jev 用法:</b> 每个 skill 问若干 Noul 式问题，配合冲突和覆盖阈值，汇总成一份发现报告。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/matrixorigin/Astra"><img src="https://raw.githubusercontent.com/matrixorigin/Astra/main/docs/assets/explain-analyze-demo.gif" alt="Astra" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/matrixorigin/Astra">Astra</a></b><br><sub>matrixorigin · GitHub · ⭐ 32 · 2026-02-09</sub><br>面向长时间运行企业 agent 的自托管运行时，为上下文提供 EXPLAIN ANALYZE，并在四个决策点原生使用 Jev 判断：记忆过滤、经验剔除、请求分类和 skill 选择。<br><sub><b>Jev 用法:</b> 各调用方共享类型化问题、响应校验、提供方路由和用量统计；Jev 与生成模型分开配置。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/The-Vibe-Company/granite"><img src="https://raw.githubusercontent.com/The-Vibe-Company/granite/main/docs/screenshots/granite-graph.png" alt="Granite" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/The-Vibe-Company/granite">Granite</a></b><br><sub>The-Vibe-Company · GitHub · ⭐ 32 · 2026-03-30</sub><br>本地优先的 markdown 知识编译器兼 MCP 服务器，用作 agent 记忆；它唯一的模型就是 Jev，负责从确定性限定的候选集中选出能回答问题的那一项，并评判每次录入。<br><sub><b>Jev 用法:</b> Jev 在 Granite 选定的集合上返回选择、分数或概率；它从不写链接，没有 key 时 Granite 拒绝启动。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/AgentiLoop/Agent/blob/main/Agent/Services/JevAdvisor.swift"><img src="https://raw.githubusercontent.com/AgentiLoop/Agent/main/agent-demo.gif" alt="Agent! Jev advisor" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/AgentiLoop/Agent/blob/main/Agent/Services/JevAdvisor.swift">Agent! Jev advisor</a></b><br><sub>AgentiLoop · GitHub · ⭐ 623 仓库 · 2026-09-18</sub><br>原生 macOS agent 应用 Agent! 中的 Jev 顾问：对已经通过模式规则的 shell 命令再给一次第二意见，数据销毁概率超过用户设定阈值的命令会被拒绝。<br><sub><b>Jev 用法:</b> 使用内置的 TypeSafeKit Swift 客户端，并采用失败放行（fail open）策略，服务中断也不会卡住工具循环。</sub><br><sub>相关: <a href="https://github.com/AgentiLoop/Agent">repo</a> · <a href="https://github.com/AgentiLoop/Agent/tree/main/TypeSafeKit">sdk</a> · <a href="https://agentiloop.ai">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/samdotmak/jev-recall"><img src="https://opengraph.githubassets.com/1/samdotmak/jev-recall" alt="Jev Recall" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/samdotmak/jev-recall">Jev Recall</a></b><br><sub>samdotmak · GitHub · ⭐ 31 · 2026-09-19</sub><br>面向 AI 助手的记忆检索，返回与查询真正相关的记忆，而不是看起来相似的那些，目标是以语义搜索的成本和速度达到重排器的质量。<br><sub><b>Jev 用法:</b> 一次请求中每条记忆一个校准的 Noul。</sub><br><sub>相关: <a href="https://www.reddit.com/r/MachineLearning/comments/1wl31tp/jev_to_retrieve_memories_is_a_game_changer_p/">demo</a> · <a href="https://www.reddit.com/r/LangChain/comments/1wl324b/jev_to_retrieve_memories_is_a_game_changer_p/">discussion</a> · <a href="https://jev-recall.vercel.app">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/ksenxx/kiss_ai/blob/main/src/kiss/agents/sorcar/decide_tool.py"><img src="https://raw.githubusercontent.com/ksenxx/kiss_ai/main/assets/KISS-Sorcar.png" alt="KISS Sorcar decide tool" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/ksenxx/kiss_ai/blob/main/src/kiss/agents/sorcar/decide_tool.py">KISS Sorcar decide tool</a></b><br><sub>ksenxx · GitHub · ⭐ 553 仓库 · 2026-01-09</sub><br>面向长程任务的通用 agent 框架 KISS Sorcar 为 agent 提供一个 decide 工具，通过向 Jev 提类型化问题来决定下一步。<br><sub><b>Jev 用法:</b> 通过 OpenRouter 的 ~typesafe/jev-latest 提出 noul、choice 和 score 问题，可以并行调用。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/CoWork-OS/CoWork-OS/blob/main/src/electron/agent/decisions/typesafe-provider.ts"><img src="https://raw.githubusercontent.com/CoWork-OS/CoWork-OS/main/screenshots/cowork-os-sl-color-logo.png" alt="CoWork OS TypeSafe decisions" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/CoWork-OS/CoWork-OS/blob/main/src/electron/agent/decisions/typesafe-provider.ts">CoWork OS TypeSafe decisions</a></b><br><sub>CoWork-OS · GitHub · ⭐ 457 仓库 · 2026-01-24</sub><br>本地优先的 agent 型全能应用 CoWork OS 新增了 TypeSafe 决策提供方，让其中的 agent 可以通过 /v1/systemone 做类型化判断。<br><sub><b>Jev 用法:</b> 一个 HTTP 决策提供方，默认使用 jev-latest。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/openagentsinc/openagents/tree/main/crates/jev"><img src="https://opengraph.githubassets.com/1/openagentsinc/openagents" alt="OpenAgents Jev" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/openagentsinc/openagents/tree/main/crates/jev">OpenAgents Jev</a></b><br><sub>openagentsinc · GitHub · ⭐ 449 仓库 · 2023-11-07</sub><br>通用 agent 基础设施，每一轮都从一次 Jev 类型化判断开始，返回一个选择和概率，并可折回到这一轮中。<br><sub><b>Jev 用法:</b> 一个 Rust Jev SDK crate，提供类型化的 Choice、Noul 和 Score 答案，驱动轮次循环中 respond/retry/stop 的结论。</sub><br><sub>相关: <a href="https://openagents.com">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/professorpalmer/puppetmaster/tree/main/puppetmaster/jev"><img src="https://raw.githubusercontent.com/professorpalmer/Puppetmaster/main/docs/demo.gif" alt="Puppetmaster Jev" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/professorpalmer/puppetmaster/tree/main/puppetmaster/jev">Puppetmaster Jev</a></b><br><sub>professorpalmer · GitHub · ⭐ 449 仓库 · 2026-05-06</sub><br>面向持久状态 agent 集群的控制平面 Puppetmaster，在其 worker 拼接流程中用 Jev 做冲突、已答复、准入和停止决策。<br><sub><b>Jev 用法:</b> 通过 OpenRouter 的 ~typesafe/jev-latest 发送问题和阈值，超时 2 秒。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/AgorithmAg/status/2102169114542301526"><img src="https://pbs.twimg.com/media/HSxnqknWEAAgfFK.jpg?name=orig" alt="Drift developmental memory" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/AgorithmAg/status/2102169114542301526">Drift developmental memory</a></b><br><sub>AgorithmAg · X · ♥ 15 · 2026-09-21</sub><br>给 AI 陪伴角色配上基于 Jev 的成长型记忆，记录它尝试过什么、用户如何反应、它学到了什么，让驱动它的不同模型之间保持行为一致。<br><sub>相关: <a href="https://drift-riverbed.com/developmental-memory.html">spec</a> · <a href="https://drift-riverbed.com/developmental-memory.html">project</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://www.elvex.com/blog/early-experimentation-using-jev-to-rethink-harness-ux"><img src="https://cdn.prod.website-files.com/6866aba1d492c973444d9b24/6aad9db0d4b0c68d2079c47f_Blog%20Hero%20Image(6).png" alt="elvex harness 中的 Jev" width="240"></a></td>
<td valign="top"><b><a href="https://www.elvex.com/blog/early-experimentation-using-jev-to-rethink-harness-ux">elvex harness 中的 Jev</a></b><br><sub>Doyle Irvin (elvex) · 文章 · ▲ 7 · 2026-09-18</sub><br>一家 agent 平台的实践文章，讲如何把 Jev 作为可调用工具接入 LLM harness，用于搜索、审批和上下文，其中包括用 20 秒、5 美分给 2,000 份报销单分类。<br><sub>相关: <a href="https://news.ycombinator.com/item?id=49760264">discussion</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/trytenjin/status/2101817410307137937"><img src="https://pbs.twimg.com/amplify_video_thumb/2101816882080718849/img/i6lPMBe0BF-LOcae.jpg" alt="用 Jev 选择 x402 工具" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/trytenjin/status/2101817410307137937">用 Jev 选择 x402 工具</a></b><br><sub>trytenjin · X · ♥ 13 · 2026-09-20</sub><br>Tenjin 的现场演示：Jev 从一组精选工具中决定调用哪个付费 x402 端点。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/decocms/studio/blob/main/apps/api/src/tools/task-board/duplicate-decisions.ts"><img src="https://opengraph.githubassets.com/1/decocms/studio" alt="Deco Studio Jev task dedupe" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/decocms/studio/blob/main/apps/api/src/tools/task-board/duplicate-decisions.ts">Deco Studio Jev task dedupe</a></b><br><sub>decocms · GitHub · ⭐ 408 仓库 · 2025-03-14</sub><br>agent 控制平面，其任务看板会先问 Jev 新任务是否与已有卡片重复，Jev 不可用或拿不准时回退到快速 LLM。<br><sub><b>Jev 用法:</b> 所有新任务共享一个 state，每个任务一个 Choice（含“none”选项）；只有每个 Choice 的概率都至少达到 0.95 时才采纳答案。</sub><br><sub>相关: <a href="https://decocms.com/studio">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/runta-dev/jot"><img src="https://opengraph.githubassets.com/1/runta-dev/jot" alt="Jot" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/runta-dev/jot">Jot</a></b><br><sub>runta-dev · GitHub · ⭐ 19 · 2026-09-18</sub><br>通用 agent 循环：Jev 选择工具及参数，Jot 负责执行，把真实结果反馈进上下文后再问，直到 Jev 可以作答，每次工具调用都清晰可见。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/MiaoWuNYA/rikkahub-sillytavern-android"><img src="https://opengraph.githubassets.com/1/MiaoWuNYA/rikkahub-sillytavern-android" alt="RikkaHub Plus Jev decisions" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/MiaoWuNYA/rikkahub-sillytavern-android">RikkaHub Plus Jev decisions</a></b><br><sub>MiaoWuNYA · GitHub · ⭐ 19 · 2026-09-20</sub><br>兼容 SillyTavern 的安卓 AI 聊天客户端，用 Jev 判断每条记忆与对话的相关性来取代 embedding 搜索，并为主模型提供一个 Jev 评判工具，用于是/否、选择和打分问题。<br><sub><b>Jev 用法:</b> 记忆以并行批次评判，相关性高于 0.5 才注入；Jev 不可用时，所有 Jev 路径都会静默回退。</sub></td>
</tr>
<tr>
<td width="260" valign="top"></td>
<td valign="top"><b><a href="https://www.reddit.com/r/AI_Agents/comments/1wl82fr/tried_typesafe_ais_jev_vs_a_regular_llm_for_model/">Jev 与 LLM 模型路由对比</a></b><br><sub>TigerOk4538 · Reddit · ▲ 6 · 2026-09-20</sub><br>智能模型路由器，在每条消息上并排运行 Jev 和一个结构化输出 LLM；Jev 约 1 秒返回路由决策，LLM 则需要 4-14 秒。<br><sub><b>Jev 用法:</b> 所有路由信号在一次调用中评估完毕。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/blakestone-x/jev-mcp"><img src="https://opengraph.githubassets.com/1/blakestone-x/jev-mcp" alt="jev-mcp" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/blakestone-x/jev-mcp">jev-mcp</a></b><br><sub>blakestone-x · GitHub · ⭐ 18 · 2026-09-16</sub><br>Python MCP 服务器，为 Claude Code、Codex、Cursor 或任意 MCP 客户端提供类型化的 Jev classify、score、check、match 和 screen 工具，每个答案都附带置信度。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Das-rebel/a3m-router"><img src="https://opengraph.githubassets.com/1/Das-rebel/a3m-router" alt="A3M Router" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Das-rebel/a3m-router">A3M Router</a></b><br><sub>Das-rebel · GitHub · ⭐ 16 · 2026-05-15</sub><br>自适应多模型 LLM 路由器，覆盖 80+ 家提供商，支持信息素轨迹式故障切换和集成合并；设置 model=jev-auto 时，由 Jev 一次性把每个请求路由到合适的提供商。<br><sub>相关: <a href="https://www.npmjs.com/package/adaptive-memory-multi-model-router">npm</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/phantomyard/phantombot"><img src="https://opengraph.githubassets.com/1/phantomyard/phantombot" alt="Phantombot" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/phantomyard/phantombot">Phantombot</a></b><br><sub>phantomyard · GitHub · ⭐ 16 · 2026-05-01</sub><br>围绕终端 harness 构建的持久身份 AI 助手，在 PhantomChat、Telegram 和编辑器之间共享长期记忆；可选的 Jev 筛查器充当威胁评判者，并在约 300 毫秒内把每轮路由到主模型或编程模型。<br><sub><b>Jev 用法:</b> 类型化的 primary|coder Choice 取代关键词打分来做换脑路由；出错时回退到打分器，并由 phantombot doctor 报告。</sub><br><sub>相关: <a href="https://phantombot.bot/">app</a> · <a href="https://github.com/phantomyard/phantombot/blob/main/docs/jev.md">docs</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/chopratejas/invalidate"><img src="https://raw.githubusercontent.com/chopratejas/invalidate/main/docs/img/chat.png" alt="invalidate" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/chopratejas/invalidate">invalidate</a></b><br><sub>chopratejas · GitHub · ⭐ 15 · 2026-09-19</sub><br>agent 记忆的失效层：每来一个新事件，就用一个 Jev 是/否问题逐条检查已存事实（每次检查约 150 毫秒、$0.00006），标记被取代的记忆，拿不准的排队交给人工。<br><sub>相关: <a href="https://www.reddit.com/r/AIMemory/comments/1wkqj4i/making_memory_unremember_an_apache_20_oss_project/">discussion</a> · <a href="https://invalidate-playground.vercel.app">app</a> · <a href="https://invalidate-playground.vercel.app">app 2</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/NiazMorshed2007/jcr"><img src="https://raw.githubusercontent.com/NiazMorshed2007/jcr/main/web/src/app/opengraph-image.png" alt="JCR (Jev Capability Resolver)" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/NiazMorshed2007/jcr">JCR (Jev Capability Resolver)</a></b><br><sub>NiazMorshed2007 · GitHub · ⭐ 15 · 2026-09-20</sub><br>解析器，只给 agent 一个工具，用来查找完成任务所需的、有文档的确定性命令：用 Jev 搜索嵌套的能力树，只返回被选中操作的上下文。<br><sub>相关: <a href="https://jcr.niazmorshed.dev">site</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Brainwires/jevwire"><img src="https://opengraph.githubassets.com/1/Brainwires/jevwire" alt="jevwire" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Brainwires/jevwire">jevwire</a></b><br><sub>Brainwires · GitHub · ⭐ 15 · 2026-09-17</sub><br>面向 agent harness 的 Jev 决策层：一个带七个工具（rank、pick、verify、evaluate、gate action、next step、list models）的 MCP 服务器、一个可嵌入的 DecisionModel 库，以及一个只负责升级的 Claude Code 插件。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/ling-kong-ran/pisper/blob/release/runtime/services/decision-service.mjs"><img src="https://raw.githubusercontent.com/ling-kong-ran/pisper/release/docs/brand/banner.svg" alt="Pisper decision service" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/ling-kong-ran/pisper/blob/release/runtime/services/decision-service.mjs">Pisper decision service</a></b><br><sub>ling-kong-ran · GitHub · ⭐ 298 仓库 · 2026-07-19</sub><br>多 agent 桌面和移动应用，新增 Jev 决策服务，在高于 0.9 阈值时自动批准工具权限，并验证电脑操控（computer use）动作。<br><sub><b>Jev 用法:</b> 用 Noul、Choice 和 Score 问题调用 TypeSafe /v1/systemone 或 OpenRouter decisions；低置信度时回退到人工审批。</sub><br><sub>相关: <a href="https://pisper.cc">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/SREGym/SREGym/tree/main/clients/jev"><img src="https://raw.githubusercontent.com/SREGym/SREGym/main/assets/overview.png" alt="SREGym Jev decision tool" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/SREGym/SREGym/tree/main/clients/jev">SREGym Jev decision tool</a></b><br><sub>SREGym · GitHub · ⭐ 290 仓库 · 2025-05-19</sub><br>为 SRE agent 基准测试提供的可选 Codex MCP 工具：在提交诊断或修复前，由 Jev 挑选信息量最大的只读诊断测试，并审查 Kubernetes 证据。<br><sub><b>Jev 用法:</b> 在提议的诊断测试（或“revise_tests”）上做 Choice；Noul 审查是否有因果支撑、故障是否仍在发生、修复是否持久。</sub><br><sub>相关: <a href="https://sregym.com">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/mindroom-ai/mindroom/blob/main/src/mindroom/judgment/evaluator.py"><img src="https://repository-images.githubusercontent.com/1137843985/a7ad6a4c-9828-4e95-91b5-7d05e97c59fc" alt="MindRoom participation judgments" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/mindroom-ai/mindroom/blob/main/src/mindroom/judgment/evaluator.py">MindRoom participation judgments</a></b><br><sub>mindroom-ai · GitHub · ⭐ 284 仓库 · 2026-01-19</sub><br>基于 Matrix 的多 agent 运行时，已在某个讨论串中的 agent 会用 LLM 或 TypeSafe System One（阈值 0.8）决定是否回复未标记的消息。<br><sub>相关: <a href="https://docs.mindroom.chat">docs</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/buberlo/dsh-jev"><img src="https://raw.githubusercontent.com/buberlo/dsh-jev/main/docs/assets/kubernetes-comparison.png" alt="dsh-jev" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/buberlo/dsh-jev">dsh-jev</a></b><br><sub>buberlo · GitHub · ⭐ 13 · 2026-09-19</sub><br>DeepSeek Harness agent 循环的决策层：Jev 在每一步之前收窄相关工具、拦截高风险工具调用、选择模型路由，而且永远不会放宽权限。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/GodsBoy/jev-agent-skill-router"><img src="https://raw.githubusercontent.com/GodsBoy/jev-agent-skill-router/main/assets/jev-agent-skill-router-banner.png" alt="Jev Agent Skill Router" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/GodsBoy/jev-agent-skill-router">Jev Agent Skill Router</a></b><br><sub>GodsBoy · GitHub · ⭐ 13 · 2026-09-16</sub><br>路由层，用带置信度的 Jev 决策挑选要加载哪个 Hermes Agent skill，并拒绝弱匹配；在 72 个合成请求中路由正确 68 个，词法基线为 51 个。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/jon-devlapaz/jev-me"><img src="https://opengraph.githubassets.com/1/jon-devlapaz/jev-me" alt="jev-me" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/jon-devlapaz/jev-me">jev-me</a></b><br><sub>jon-devlapaz · GitHub · ⭐ 13 · 2026-09-17</sub><br>agent skill，以设计树访谈的方式拷问一份计划，每轮列出所有已解锁的决策并给出推荐答案，需要类型化判断时临时调用 Jev。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/krau/kmua-bot/blob/v2/kmua/plugins/agent/jev.py"><img src="https://repository-images.githubusercontent.com/573633729/31372b28-6155-40e6-ac96-6f7ed0b441ad" alt="kmua bot Jev follow-up check" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/krau/kmua-bot/blob/v2/kmua/plugins/agent/jev.py">kmua bot Jev follow-up check</a></b><br><sub>krau · GitHub · ⭐ 241 仓库 · 2022-12-03</sub><br>Telegram 机器人 agent，实验性地用 Jev 判断群里的后续消息是否足够相关、值得机器人继续回复，阈值可配置。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://www.reddit.com/r/LLMDevs/comments/1wihigc/tried_typesafes_new_decisiononly_model_jev_as_an/"><img src="https://preview.redd.it/h90l7rcdszph1.png?width=1080&amp;format=png&amp;auto=webp&amp;s=d1460cf34f1dcc1eb36f720f72be19077dcf6ba6" alt="Agent 路由器测试" width="240"></a></td>
<td valign="top"><b><a href="https://www.reddit.com/r/LLMDevs/comments/1wihigc/tried_typesafes_new_decisiononly_model_jev_as_an/">Agent 路由器测试</a></b><br><sub>blackbarata · Reddit · ▲ 4 · 2026-09-17</sub><br>把 Jev 用作个人知识应用里各个 agent 的路由器，能根据 Instagram Reel 的转录文本正确选出食谱 agent 或抓取 agent，耗时 145-271 毫秒。<br><sub><b>Jev 用法:</b> 在简短的 agent 描述上做一个 Choice，并用置信度决定何时回退。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/fornhere/hafiza-os"><img src="https://opengraph.githubassets.com/1/fornhere/hafiza-os" alt="Hafiza OS" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/fornhere/hafiza-os">Hafiza OS</a></b><br><sub>fornhere · GitHub · ⭐ 12 · 2026-08-30</sub><br>土耳其语的第二大脑系统，把 agent 记忆存放在本地 Markdown 库中，供 Claude Code、Codex 和 Antigravity 使用，Jev 作为可选的检索和审查顾问。<br><sub><b>Jev 用法:</b> 按 0-2 分给知识卡片和记忆目录候选与问题的相关性打分（阈值 1.5），支持 off、shadow、on 三种模式。</sub><br><sub>相关: <a href="https://github.com/fornhere/hafiza-os/blob/main/JEV.md">docs</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/keeltrace/hermes-jev"><img src="https://opengraph.githubassets.com/1/keeltrace/hermes-jev" alt="Hermes-Jev" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/keeltrace/hermes-jev">Hermes-Jev</a></b><br><sub>keeltrace · GitHub · ⭐ 12 · 2026-09-18</sub><br>Hermes Agent 的异步决策层，并行运行轮次准入、相关性路由、完成度与恢复检查，以及可选启用的工具关卡，不阻塞执行。<br><sub><b>Jev 用法:</b> 有边界的 Choice/Noul 问题在后台评估，以消化 Jev 约 500 毫秒的延迟；只有高置信度的质疑才会打断 Hermes。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/anpicasso/hermes-jev-approvals"><img src="https://opengraph.githubassets.com/1/anpicasso/hermes-jev-approvals" alt="hermes-jev-approvals" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/anpicasso/hermes-jev-approvals">hermes-jev-approvals</a></b><br><sub>anpicasso · GitHub · ⭐ 12 · 2026-09-17</sub><br>Hermes Agent 智能命令审批的提供方：Jev 在一次请求中根据六个类型化问题返回 APPROVE、DENY 或 ESCALATE，在 153 条真实命令上实测快 8.7 倍，确认提示少 4.4 倍。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/tidepool-heavy-industries/tidepool"><img src="https://opengraph.githubassets.com/1/tidepool-heavy-industries/tidepool" alt="Tidepool" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/tidepool-heavy-industries/tidepool">Tidepool</a></b><br><sub>tidepool-heavy-industries · GitHub · ⭐ 12 · 2026-02-17</sub><br>构建在实时 Haskell notebook 上的 agent harness，agent 编写混合命令、委派和 Jev 判断的过程，再把它们安装为工具或 hook；322 个问题在 351 毫秒内返回。<br><sub><b>Jev 用法:</b> 由推理型 LLM 设计过程，Jev 在编译后的代码里回答批量类型化问题，例如证据是否相关、哪个后续动作合适。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/DemonDamon/AgenticX/blob/main/agenticx/runtime/jev_intent.py"><img src="https://opengraph.githubassets.com/1/DemonDamon/AgenticX" alt="AgenticX Jev group routing" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/DemonDamon/AgenticX/blob/main/agenticx/runtime/jev_intent.py">AgenticX Jev group routing</a></b><br><sub>DemonDamon · GitHub · ⭐ 233 仓库 · 2024-03-15</sub><br>多 agent 平台，群聊中未被 @ 的消息由 Jev 路由：置信度高时按标签分派，否则回退到 LLM，并在每轮显示一张决策卡片。<br><sub>相关: <a href="https://www.agxbuilder.com/">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/mishrasanjeev/agentic-org"><img src="https://opengraph.githubassets.com/1/mishrasanjeev/agentic-org" alt="AgenticOrg Jev integration" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/mishrasanjeev/agentic-org">AgenticOrg Jev integration</a></b><br><sub>mishrasanjeev · GitHub · ⭐ 11 · 2026-03-20</sub><br>企业级 agent 编排平台，带有 Jev 提供方适配器、离线评估器，以及一个影子模式 hook，用来把 Jev 的工具路由决策与现有运行时的实际结果做对比。<br><sub><b>Jev 用法:</b> 仅作参考，设有 0.8 秒超时、采样上限和熔断器；在经过量化评估并获批之前，生产环境保持关闭。</sub><br><sub>相关: <a href="https://github.com/mishrasanjeev/agentic-org/blob/main/docs/jev-agenticorg-integration.md">docs</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/hellozenstrategist-lab/eutrya"><img src="https://raw.githubusercontent.com/hellozenstrategist-lab/eutrya/main/assets/eutrya-banner.webp" alt="Eutrya" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/hellozenstrategist-lab/eutrya">Eutrya</a></b><br><sub>hellozenstrategist-lab · GitHub · ⭐ 11 · 2026-06-04</sub><br>独立的 CLI 优先 agent harness，用于经授权的安全研究、多 agent 集群和长时间运行的工作流，决策循环内置 Jev，负责注意力分配、候选评分标准和研究微步骤。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/zjunlp/JevLoop"><img src="https://opengraph.githubassets.com/1/zjunlp/JevLoop" alt="JevLoop" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/zjunlp/JevLoop">JevLoop</a></b><br><sub>zjunlp · GitHub · ⭐ 11 · 2026-09-20</sub><br>可运行的 agent harness，把循环中的每个岔路口（用哪个工具、是否安全、是否完成）交给 Jev 或 Laya 这样的决策模型，LLM 只负责写作，带网页 UI，无任何依赖。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/DECRUX9812/typesafe-skill-router"><img src="https://opengraph.githubassets.com/1/DECRUX9812/typesafe-skill-router" alt="typesafe-skill-router" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/DECRUX9812/typesafe-skill-router">typesafe-skill-router</a></b><br><sub>DECRUX9812 · GitHub · ⭐ 11 · 2026-09-16</sub><br>可选启用的 Hermes Agent 插件，在模型调用前询问 Jev 哪一个已安装的 skill 适合当前请求，并追加一行提示，每个路由轮次约 $0.001；没有合适的 skill 时什么也不注入。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/damianvtran/local-operator/tree/main/local_operator/classification"><img src="https://repository-images.githubusercontent.com/922327641/359101c9-d089-4d2c-bb22-a62f973989de" alt="Local Operator classification layer" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/damianvtran/local-operator/tree/main/local_operator/classification">Local Operator classification layer</a></b><br><sub>damianvtran · GitHub · ⭐ 214 仓库 · 2025-01-25</sub><br>agent 中枢，每条消息在启发式规则旁运行一次决策模型层，推荐 skill、MCP 服务器和角色；把评分标准写进选项后，Jev 在标注案例上得分 31/31。<br><sub><b>Jev 用法:</b> 在 Radient、TypeSafe 和 OpenRouter 之间级联，请求体逐字节相同；评测中每次调用 p50 为 0.20 秒。</sub><br><sub>相关: <a href="https://github.com/damianvtran/local-operator/blob/main/docs/design/classification-layer.md">docs</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/jmagly/aiwg/blob/main/src/decision/adapters/jev.ts"><img src="https://raw.githubusercontent.com/jmagly/aiwg/main/docs/.public/aiwg-readme-hero-v2.png" alt="AIWG Jev decision adapter" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/jmagly/aiwg/blob/main/src/decision/adapters/jev.ts">AIWG Jev decision adapter</a></b><br><sub>jmagly · GitHub · ⭐ 211 仓库 · 2025-08-14</sub><br>AI 增强开发工具包中的决策框架，通过带版本的规则集和绑定，让工作流在 Jev 和 LLM 子 agent 之间切换，并配有加固过的 Jev 传输层。<br><sub>相关: <a href="https://github.com/jmagly/aiwg/blob/main/docs/decision/jev-transport.md">docs</a> · <a href="https://aiwg.io">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/RelayPlane/proxy/blob/main/src/classifier/jev_client.ts"><img src="https://raw.githubusercontent.com/RelayPlane/proxy/main/docs/dashboard.png" alt="RelayPlane Jev classifier" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/RelayPlane/proxy/blob/main/src/classifier/jev_client.ts">RelayPlane Jev classifier</a></b><br><sub>RelayPlane · GitHub · ⭐ 203 仓库 · 2026-02-03</sub><br>本地 LLM 成本代理，带可选的 Jev 复杂度分类器，为每个请求评级以辅助模型路由，只需一个环境变量即可启用，超时上限 500 毫秒。<br><sub>相关: <a href="https://relayplane.com">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Arrmlet/dehydrator"><img src="https://opengraph.githubassets.com/1/Arrmlet/dehydrator" alt="Dehydrator" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Arrmlet/dehydrator">Dehydrator</a></b><br><sub>Arrmlet · GitHub · ⭐ 10 · 2026-02-17</sub><br>面向 LLM API 的客户端工具搜索，模型无需发送每一个工具定义就能使用数千个工具，可用 BM25、Jev 或两者结合来匹配工具。<br><sub><b>Jev 用法:</b> Jev 按语义把工具定义与 tool_search 查询做排序；除标准库外不需要额外依赖。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/evoke-build/evoke"><img src="https://opengraph.githubassets.com/1/evoke-build/evoke" alt="evoke" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/evoke-build/evoke">evoke</a></b><br><sub>evoke-build · GitHub · ⭐ 10 · 2026-09-21</sub><br>由 Rust CLI、基于 git 的包管理器和 TypeScript SDK 组成：一句说出或打出的话会变成对某个已安装 reflex 程序的调用，程序由 Jev 选定并带受限参数，再经关卡决定执行、确认、追问还是弃权。<br><sub>相关: <a href="https://evoke.build">site</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/markus-global/markus/blob/main/packages/core/src/tools/multimodal.ts"><img src="https://raw.githubusercontent.com/markus-global/markus/main/docs/images/dashboard-preview.gif" alt="Markus decide tool" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/markus-global/markus/blob/main/packages/core/src/tools/multimodal.ts">Markus decide tool</a></b><br><sub>markus-global · GitHub · ⭐ 195 仓库 · 2026-03-19</sub><br>AI 劳动力平台，为其 agent 提供决策能力和一个由 Jev 类决策模型支撑的 decide 工具，并规定所有证据都必须放进 state。<br><sub>相关: <a href="https://www.markus.global">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/libingzheren/Jev-Mem"><img src="https://raw.githubusercontent.com/libingzheren/Jev-Mem/main/docs/figures/overall_structure.png" alt="Jev-Mem" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/libingzheren/Jev-Mem">Jev-Mem</a></b><br><sub>libingzheren · GitHub · ⭐ 9 · 2026-09-20</sub><br>agent 记忆系统：Jev 作为 System One 控制器负责准入、多关系链接和检索，由语言模型负责作答；论文报告在 LoCoMo 上搭配 GPT-4o-mini 时回答质量提高 11.0%。<br><sub>相关: <a href="https://huggingface.co/spaces/libingzheren/Jev-Mem">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/kushals256/jevcache"><img src="https://raw.githubusercontent.com/kushals256/jevcache/main/docs/demo.gif" alt="jevcache (semantic cache)" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/kushals256/jevcache">jevcache (semantic cache)</a></b><br><sub>kushals256 · GitHub · ⭐ 9 · 2026-09-19</sub><br>本地的 OpenAI 兼容代理，当 Jev 判断新请求与之前某个请求意图相同时，复用缓存的对话补全结果，Jev 出错时直接放行；一次测试中耗时从 3244 毫秒降到 394 毫秒。<br><sub>相关: <a href="https://www.reddit.com/r/LLM/comments/1wm3ijr/your_agent_asks_the_same_thing_twice_in_different/">demo</a> · <a href="https://www.npmjs.com/package/@kushalicious/jevcache">npm</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/ItIsCuthNotCup/MetaCog"><img src="https://opengraph.githubassets.com/1/ItIsCuthNotCup/MetaCog" alt="MetaCog" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/ItIsCuthNotCup/MetaCog">MetaCog</a></b><br><sub>ItIsCuthNotCup · GitHub · ⭐ 9 · 2026-09-20</sub><br>元认知循环：小模型分出多条思路，再由 System One 评判者（Jev 或开源的 Reflex 4B）挑选继续哪一条；逐候选的 Jev Noul 把 HumanEval 从 0.555 提升到 0.756。<br><sub><b>Jev 用法:</b> 逐候选的 Noul 评判优于一次性 Choice（HumanEval 上 0.756 对 0.726，GSM8K 上 0.905 对 0.869）。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/miikkij/aimeat-protocol"><img src="https://raw.githubusercontent.com/miikkij/aimeat-protocol/main/assets/screenshots/portal-landing.png" alt="AIMEAT decide" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/miikkij/aimeat-protocol">AIMEAT decide</a></b><br><sub>miikkij · GitHub · ⭐ 8 · 2026-04-28</sub><br>联邦式、自托管的 AI 操作系统，每个节点在文本模型旁搭载 Jev，应用和 agent 可以通过 JS 库、MCP 工具和一个 skill 提出封闭式的分诊、路由、打分和单选问题。<br><sub><b>Jev 用法:</b> 请求离开节点前会剔除电子邮件、电话号码、芬兰身份证号等个人数据，每次决策都会记录是否经过人工复核。</sub><br><sub>相关: <a href="https://aimeat.io">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/NicolasMontone/jev-memory"><img src="https://opengraph.githubassets.com/1/NicolasMontone/jev-memory" alt="jev-memory" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/NicolasMontone/jev-memory">jev-memory</a></b><br><sub>NicolasMontone · GitHub · ⭐ 8 · 2026-09-18</sub><br>Vercel AI SDK 的长期记忆层，由 Jev 把关写入、检索和淘汰，存储原始字符串，因此记忆永远不会被摘要或改写。<br><sub><b>Jev 用法:</b> 写入、检索和淘汰关卡各是一个布尔、选择或打分问题，通过 AI Gateway 发给 typesafe-ai/jev。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/rajdhakad9826/jev-router"><img src="https://external-preview.redd.it/MYwHHpL0--RYjVWYB4u6LIjIKjKERfy3Z1jmJkPiIyE.png?auto=webp&amp;s=71e8215cba4f41d7887ad24f3c98c27af60055a2" alt="jev-model-router" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/rajdhakad9826/jev-router">jev-model-router</a></b><br><sub>rajdhakad9826 · GitHub · ⭐ 8 · 2026-09-19</sub><br>TypeScript 路由器，在两级或三级级联中把每个查询发给能胜任的最便宜模型，用 Jev 判断查询的难度，而不是调用 LLM。<br><sub>相关: <a href="https://www.reddit.com/r/typesafe/comments/1wkrfos/github_rajdhakad9826jevrouter_costaware_llm/">demo</a> · <a href="https://www.reddit.com/r/typesafe/comments/1wkri7o/build_a_llm_router_using_jev/">discussion</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/PerryLink/jevcore"><img src="https://opengraph.githubassets.com/1/PerryLink/jevcore" alt="jevcore" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/PerryLink/jevcore">jevcore</a></b><br><sub>PerryLink · GitHub · ⭐ 8 · 2026-09-20</sub><br>决策层，通过三个包把 Jev 的 noul、choice 和 score 问题提供给 DeepSeek Harness、任意 MCP 宿主或纯 Node，默认离线，并明示网络外发情况。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/zeeshan8281/slo-router"><img src="https://opengraph.githubassets.com/1/zeeshan8281/slo-router" alt="SLO Router" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/zeeshan8281/slo-router">SLO Router</a></b><br><sub>zeeshan8281 · GitHub · ⭐ 8 · 2026-09-19</sub><br>兼容 OpenAI 接口的代理，把每个请求路由到满足其延迟 SLO 的最便宜后端，可选启用 Jev 1.13 的语义特征；一次实测发现 Jev 没有改变任何路由，却把 p95 从 77.93 毫秒拉高到 490.38 毫秒。<br><sub><b>Jev 用法:</b> 通过 OpenRouter Decisions API 获取类型化语义特征，缺少 key、超时或响应无效时回退到本地特征。</sub><br><sub>相关: <a href="https://github.com/zeeshan8281/slo-router/blob/main/results/live-jev-analysis.md">results</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"></td>
<td valign="top"><b><a href="https://www.npmjs.com/package/@maximem/jev-mcp">@maximem/jev-mcp</a></b><br><sub>maximem-ai · 软件包 · ⬇ 754 · 2026-09-20</sub><br>MCP 服务器，为 Claude Code、Codex 和 Cowork 提供基于 Jev 的分类、打分、检查和排序工具，另有针对 agent 自身工作的计划、操作和验证关卡。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/arunav25/jev-mcp"><img src="https://opengraph.githubassets.com/1/arunav25/jev-mcp" alt="JEV MCP" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/arunav25/jev-mcp">JEV MCP</a></b><br><sub>arunav25 · GitHub · ⭐ 7 · 2026-09-17</sub><br>把 Jev 暴露为单一 evaluate 工具的 MCP 服务器，供 Claude Code、Claude Desktop 和 Codex 使用，并附带评测 harness，在共享数据集上将其准确率与通用 LLM 对比。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/prismhq/jev-router"><img src="https://opengraph.githubassets.com/1/prismhq/jev-router" alt="jev-router" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/prismhq/jev-router">jev-router</a></b><br><sub>prismhq · GitHub · ⭐ 7 · 2026-09-17</sub><br>兼容 OpenAI 接口的 LiteLLM 代理：客户端只请求一个模型 id，经过视觉、输出长度和工具支持的筛选后，由 Jev 挑选哪个提供方模型处理每个请求。<br><sub><b>Jev 用法:</b> 基于请求的精简摘要，在 router.yaml 中的合格模型上做一个 Choice；没有 key 时运行“最便宜合格模型”基线。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/riteshverma/s18"><img src="https://opengraph.githubassets.com/1/riteshverma/s18" alt="s18" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/riteshverma/s18">s18</a></b><br><sub>riteshverma · GitHub · ⭐ 7 · 2026-02-10</sub><br>开源 agent 运行时和编排 API，查询路由、skill 匹配和规划器快速路径都可以使用 Jev 决策；当 Jev 没配 key、无法访问或拿不准时，回退到内置的正则防护。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/cahaseler/determinate"><img src="https://opengraph.githubassets.com/1/cahaseler/determinate" alt="determinate" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/cahaseler/determinate">determinate</a></b><br><sub>cahaseler · GitHub · ⭐ 6 · 2026-03-11</sub><br>把 LLM 当作下一步动作预测器的 TypeScript agent 库；其 Jev 决策器选出下一个合法工具并填好闭集参数，只有自由文本字段或低置信度的情况才交给 LLM。<br><sub><b>Jev 用法:</b> 每次 nextAction() 发一次请求，询问下一个工具以及每个类枚举参数；低于 minConfidence（0.6）时由 LLM 决定。可通过 TypeSafe 或 OpenRouter Decisions 使用。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/iii-hq/workers/blob/main/iii-directory/src/functions/search_jev.rs"><img src="https://opengraph.githubassets.com/1/iii-hq/workers" alt="iii-directory Jev search" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/iii-hq/workers/blob/main/iii-directory/src/functions/search_jev.rs">iii-directory Jev search</a></b><br><sub>iii-hq · GitHub · ⭐ 109 仓库 · 2026-03-18</sub><br>iii 引擎的 worker，用 Jev 相关性判断搜索已注册的函数、已安装的 skill 和触发器，并可回退到混合搜索。<br><sub>相关: <a href="https://workers.iii.dev/">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/JulesLiu390/PetGPT/blob/main/src/utils/social/jevClient.js"><img src="https://repository-images.githubusercontent.com/952838031/91883b7f-7f2b-412f-a048-8eae41b0de5a" alt="PetGPT Jev social signals" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/JulesLiu390/PetGPT/blob/main/src/utils/social/jevClient.js">PetGPT Jev social signals</a></b><br><sub>JulesLiu390 · GitHub · ⭐ 107 仓库 · 2025-03-22</sub><br>AI 桌面宠物，带一个在 QQ、Telegram 和 WhatsApp 群里活动的社交 agent，回复前用 Jev 标注消息情绪、判断群聊氛围。<br><sub>相关: <a href="https://github.com/JulesLiu390/PetGPT/tree/main/jev-test">sandbox</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/hjxwz123/Aivory/tree/main/server/internal/typesafe"><img src="https://raw.githubusercontent.com/hjxwz123/Aivory/main/docs/brand/readme-header.svg" alt="Aivory decision policies" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/hjxwz123/Aivory/tree/main/server/internal/typesafe">Aivory decision policies</a></b><br><sub>hjxwz123 · GitHub · ⭐ 101 仓库 · 2026-06-12</sub><br>自托管 AI 聊天平台，管理员可以把文件路由、工具路由、记忆去重、记忆冲突裁决和内容审核分配给 Jev，每项都带置信度回退。<br><sub><b>Jev 用法:</b> 内容审核对每个类别问一个 Noul，达到 0.85 即拦截；工具路由只有在置信度达到 0.8 时才收窄工具范围。</sub><br><sub>相关: <a href="https://github.com/hjxwz123/Aivory/blob/main/docs/typesafe-decisions.md">docs</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/xudafeng/agent0"><img src="https://raw.githubusercontent.com/xudafeng/agent0/main/docs/images/agent0-jev-demo.gif" alt="agent0" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/xudafeng/agent0">agent0</a></b><br><sub>xudafeng · GitHub · ⭐ 5 · 2026-09-18</sub><br>桌面 AI agent 运行时，集成 MCP、任务规划和持久记忆；可选的 Jev 路由负责挑选相关工具，置信度低时回退到主模型，每次决策都显示在 Activity 面板里。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/lhemerly/mcts-agent"><img src="https://opengraph.githubassets.com/1/lhemerly/mcts-agent" alt="Discriminative MCTS Agent" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/lhemerly/mcts-agent">Discriminative MCTS Agent</a></b><br><sub>lhemerly · GitHub · ⭐ 5 · 2026-09-16</sub><br>自主 agent，对 AGY 或 Pi 等 harness 提出的动作运行蒙特卡洛树搜索，并配有 D3.js 可视化工具，用于回放 rollout 和价值反向传播过程。<br><sub><b>Jev 用法:</b> Choice 负责分配动作先验和动态分支，Score 评估假设状态，Noul 处理是/否检查。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/cyberofficial/dsh-plugin-jev"><img src="https://opengraph.githubassets.com/1/cyberofficial/dsh-plugin-jev" alt="dsh-plugin-jev" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/cyberofficial/dsh-plugin-jev">dsh-plugin-jev</a></b><br><sub>cyberofficial · GitHub · ⭐ 5 · 2026-09-19</sub><br>DeepSeek Harness 网页 GUI 的插件，为主 agent 和子 agent 提供 jev_ask 工具，用于在不确定的情况下做校准判断，带按会话统计的用量，以及设置 key 和模型的设置页。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/doronp/jevc"><img src="https://raw.githubusercontent.com/doronp/jevc/main/docs/hero.svg" alt="jevc" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/doronp/jevc">jevc</a></b><br><sub>doronp · GitHub · ⭐ 5 · 2026-09-18</sub><br>编译器，把自然语言 agent 规则和 JSON Schema 转成 Jev 程序：几个窄而具体的类型化证据问题，加上一段计算结论的代码归约器，于是像“未经要求绝不提交”这样的规则也能测试了。<br><sub>相关: <a href="https://news.ycombinator.com/item?id=49777057">demo</a> · <a href="https://www.npmjs.com/package/jev-compiler">npm</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/rShetty/miser"><img src="https://opengraph.githubassets.com/1/rShetty/miser" alt="Miser" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/rShetty/miser">Miser</a></b><br><sub>rShetty · GitHub · ⭐ 5 · 2026-08-09</sub><br>Rust AI 网关，让 Jev 把每个 OpenAI 兼容的提示词按复杂度归入从 trivial 到 reasoning 的档位，再路由到能胜任的最便宜 OpenRouter 模型；在 116 个留出案例上精确准确率为 90.5%。<br><sub><b>Jev 用法:</b> 约 340 毫秒完成档位和任务分类；会话中档位只升不降，并有启发式回退。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/hemanth/tool-prune"><img src="https://opengraph.githubassets.com/1/hemanth/tool-prune" alt="tool-prune" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/hemanth/tool-prune">tool-prune</a></b><br><sub>hemanth · GitHub · ⭐ 5 · 2026-09-17</sub><br>零依赖的 agent 工具选择和 schema 裁剪工具，在 LLM 调用前把 MCP 工具 schema 砍到少数相关的几个，可通过 TurboQuant 离线运行，也可在 Jev 上运行。<br><sub><b>Jev 用法:</b> Jev 引擎在 BFCL v3 上报告干扰项 Top-1 为 100.0%，耗时 189 毫秒；高置信度的选择可以不经 LLM 直接分派。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/supernovae-st/nika/blob/main/crates/nika-cli-host/src/compile/typesafe.rs"><img src="https://nika.sh/brand/nika-logo-light.svg" alt="Nika System One seat" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/supernovae-st/nika/blob/main/crates/nika-cli-host/src/compile/typesafe.rs">Nika System One seat</a></b><br><sub>supernovae-st · GitHub · ⭐ 88 仓库 · 2026-01-02</sub><br>面向可重复 AI 工作的工作流语言，其编译器可以把有边界的决策交给 TypeSafe System One，每个问题是一个带“none”选项的 Choice。<br><sub>相关: <a href="https://nika.sh">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/haseeb-heaven/jev-system-one"><img src="https://raw.githubusercontent.com/haseeb-heaven/jev-system-one/develop/docs/tui-preview.png" alt="jev-system-one" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/haseeb-heaven/jev-system-one">jev-system-one</a></b><br><sub>haseeb-heaven · GitHub · ⭐ 4 · 2026-09-17</sub><br>终端问答应用：在 LangGraph 工作流中由 Jev 设定回答策略并审查草稿，OpenAI 只负责措辞，每个答案旁附一份决策报告。<br><sub><b>Jev 用法:</b> 每个请求在两个节点上由 Jev 判断回答模式、深度、不确定性和草稿质量。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/NicolasMontone/jev-tool-permissions"><img src="https://opengraph.githubassets.com/1/NicolasMontone/jev-tool-permissions" alt="jev-tool-permissions" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/NicolasMontone/jev-tool-permissions">jev-tool-permissions</a></b><br><sub>NicolasMontone · GitHub · ⭐ 4 · 2026-09-18</sub><br>Vercel AI SDK 的工具权限层，用 Jev 对每个工具调用做自动批准、询问人工或拦截，并在每轮开始前剪掉无关的工具定义。<br><sub><b>Jev 用法:</b> 在确定性的允许/拒绝规则之后运行；出错时关卡按失败即关闭处理，转为询问人工。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/jon-devlapaz/tink-route"><img src="https://opengraph.githubassets.com/1/jon-devlapaz/tink-route" alt="tink-route" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/jon-devlapaz/tink-route">tink-route</a></b><br><sub>jon-devlapaz · GitHub · ⭐ 4 · 2026-09-21</sub><br>Agent Skills 路由器，skill 库平时保持离线，只通过两阶段 Jev 关卡（先用一个 Noul 判断是否需要 skill，再用一个 Choice 选哪个）按需加载需要的 skill，避免每轮提示词膨胀。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/tonone-ai/tonone/tree/main/lib/jev"><img src="https://opengraph.githubassets.com/1/tonone-ai/tonone" alt="Tonone Jev decision layer" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/tonone-ai/tonone/tree/main/lib/jev">Tonone Jev decision layer</a></b><br><sub>tonone-ai · GitHub · ⭐ 73 仓库 · 2026-03-16</sub><br>一个含 426 个 skill 的 AI 公司工具包的共享决策层，用 Jev 回答是/否、N 选一 和评分标准问题，没有 key 时改用本地 TF-IDF 打分器，并把关 skill 清单。<br><sub>相关: <a href="https://second.tonone.ai">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/virtual-context/virtual-context/tree/main/benchmarks/jev"><img src="https://raw.githubusercontent.com/virtual-context/virtual-context/main/assets/dashboard.png" alt="virtual-context Jev judgment seams" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/virtual-context/virtual-context/tree/main/benchmarks/jev">virtual-context Jev judgment seams</a></b><br><sub>virtual-context · GitHub · ⭐ 65 仓库 · 2026-02-13</sub><br>面向 LLM agent 的虚拟上下文记忆层，在各个接缝处增加 Jev 判断模式，用于重排、意图和时间检查；在 140 道 LongMemEval 题上，Jev 把首个正确答案的平均排名从 2.33 降到 1.14。<br><sub>相关: <a href="https://github.com/virtual-context/virtual-context">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/rsdkrasen/hermes-jev-router"><img src="https://opengraph.githubassets.com/1/rsdkrasen/hermes-jev-router" alt="hermes-jev-router" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/rsdkrasen/hermes-jev-router">hermes-jev-router</a></b><br><sub>rsdkrasen · GitHub · ⭐ 3 · 2026-09-19</sub><br>Hermes Agent 插件，增加一个 Jev 决策层，用来压缩工具结果、抑制重复的工具调用，并跳过只会复述结果的主模型调用。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/ajensenwaud/hermes-jev-plugin"><img src="https://opengraph.githubassets.com/1/ajensenwaud/hermes-jev-plugin" alt="Hermes Agent 的 Jev 插件" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/ajensenwaud/hermes-jev-plugin">Hermes Agent 的 Jev 插件</a></b><br><sub>ajensenwaud · GitHub · ⭐ 3 · 2026-09-19</sub><br>Hermes Agent 插件，把 Jev 暴露为 jev_check、jev_route、jev_score 和 jev_evaluate 四个工具，并附带一个 skill，讲如何为编程 agent 工作流写出好问题。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/abhishekashokvkumar/jev-mcp-dispatcher"><img src="https://opengraph.githubassets.com/1/abhishekashokvkumar/jev-mcp-dispatcher" alt="jev-mcp-dispatcher" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/abhishekashokvkumar/jev-mcp-dispatcher">jev-mcp-dispatcher</a></b><br><sub>abhishekashokvkumar · GitHub · ⭐ 3 · 2026-09-18</sub><br>概念验证性质的 MCP 工具分派器，在运行时发现简单 MCP 服务器的工具签名，把自然语言命令路由到正确的工具和参数，全程不用通用 LLM。<br><sub><b>Jev 用法:</b> Choice 选出工具，并从句子中提取每个参数值；Noul 处理是/否检查。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/DanielKillenberger/jev-predict-skill"><img src="https://opengraph.githubassets.com/1/DanielKillenberger/jev-predict-skill" alt="jev-predict-skill" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/DanielKillenberger/jev-predict-skill">jev-predict-skill</a></b><br><sub>DanielKillenberger · GitHub · ⭐ 3 · 2026-09-16</sub><br>宿主 agent skill，把另一个 skill 的结果集交给 Jev，预测它会得出哪个封闭结论（例如 SHIP 或 NEEDS_WORK），而不必真正运行那个 skill。<br><sub><b>Jev 用法:</b> 先用一个 Noul 检查能否做出封闭决策，再用一个 Choice 在目标 skill 的结果中选择。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/jvsteiner/jevex"><img src="https://opengraph.githubassets.com/1/jvsteiner/jevex" alt="Jevex" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/jvsteiner/jevex">Jevex</a></b><br><sub>jvsteiner · GitHub · ⭐ 3 · 2026-09-17</sub><br>agent 循环实验：Jev 选出每一个下一步动作并批准具体调用，LangChain 聊天模型填写参数和最终回复，三个本地 MCP 服务器共提供 12 个工具。<br><sub><b>Jev 用法:</b> 附带一个研究性基准测试，与原生工具调用的 LLM 循环对比，实测 token 和延迟。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/iamvatsalpatel/tiershift"><img src="https://raw.githubusercontent.com/iamvatsalpatel/tiershift/main/bench/chart-light.svg" alt="tiershift" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/iamvatsalpatel/tiershift">tiershift</a></b><br><sub>iamvatsalpatel · GitHub · ⭐ 3 · 2026-09-17</sub><br>面向 TypeScript 和 Python 的模型路由器，把每个 LLM 请求发给能胜任的最便宜档位，遇到多步推理、高难度、高风险或安全问题时升级，策略用纯 YAML 编写。<br><sub><b>Jev 用法:</b> 路由判断约 180 毫秒，每千次路由四美分；每个决策都会打印理由。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/finchtoys/finch-releases/tree/main/extensions/jev"><img src="https://raw.githubusercontent.com/finchtoys/finch-releases/main/home.webp" alt="finch-jev" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/finchtoys/finch-releases/tree/main/extensions/jev">finch-jev</a></b><br><sub>finchtoys · GitHub · ⭐ 57 仓库 · 2026-07-02</sub><br>Finch 桌面 agent 的小工具，注册一个 finch_jev_evaluate 工具，让 agent 可以把文本连同 Choice、Score 和 Noul 问题一起发给 Jev。<br><sub>相关: <a href="https://www.finchwork.app">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/shiro-0x/hersona/blob/main/hersona/integrations/decision/typesafe.py"><img src="https://raw.githubusercontent.com/shiro-0x/hersona/main/docs/hersona-demo.gif" alt="Hersona decide" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/shiro-0x/hersona/blob/main/hersona/integrations/decision/typesafe.py">Hersona decide</a></b><br><sub>shiro-0x · GitHub · ⭐ 52 仓库 · 2026-06-04</sub><br>面向 AI agent 的人设属性库，其 hersona decide 命令用 TypeSafe Jev 推荐回复、追问、搜索、调用工具或暂缓，并给出置信度、人设一致度和风险。<br><sub>相关: <a href="https://shiro-0x.github.io/hersona/">docs</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/adityavardhansharma/EchoFlow/tree/main/app/src/main/java/com/echoflow/data/jev"><img src="https://raw.githubusercontent.com/adityavardhansharma/EchoFlow/main/logo1.png" alt="EchoFlow Jev router" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/adityavardhansharma/EchoFlow/tree/main/app/src/main/java/com/echoflow/data/jev">EchoFlow Jev router</a></b><br><sub>adityavardhansharma · GitHub · ⭐ 48 仓库 · 2026-05-29</sub><br>注重隐私的安卓 AI 聊天应用 EchoFlow 中的逐轮 Jev 路由器，在回答模型运行前决定召回还是跳过记忆、是否强制网页搜索、是否保存记忆，仅用于云端对话。<br><sub><b>Jev 用法:</b> 每轮一次 Jev 调用，使用固定的执行阈值和超时；不确定时交给回答模型决定，失败时回退到旧行为。</sub><br><sub>相关: <a href="https://echoflow.adityavs.tech/">app</a> · <a href="https://github.com/adityavardhansharma/EchoFlow">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/dzhng/duet-agent/tree/main/src/model-routing"><img src="https://raw.githubusercontent.com/dzhng/duet-agent/main/assets/cover.png" alt="duet-agent Jev model routing" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/dzhng/duet-agent/tree/main/src/model-routing">duet-agent Jev model routing</a></b><br><sub>dzhng · GitHub · ⭐ 44 仓库 · 2026-04-10</sub><br>duet-agent harness 中的模型路由层，默认分类器是经 AI Gateway 调用的 Jev，每 5 个助手步骤重新判断该由哪个模型档位处理，任务换领域时就切换。<br><sub>相关: <a href="https://github.com/dzhng/duet-agent">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/maha0525/SAIVerse/blob/main/docs/intent/reflex_judgment.md"><img src="https://opengraph.githubassets.com/1/maha0525/SAIVerse" alt="SAIVerse reflex judgment" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/maha0525/SAIVerse/blob/main/docs/intent/reflex_judgment.md">SAIVerse reflex judgment</a></b><br><sub>maha0525 · GitHub · ⭐ 43 仓库 · 2025-06-07</sub><br>AI 人设世界 SAIVerse 中的反射判断层，返回概率而不是文字，最初用于对自动召回的记忆重排。它可以对接 TypeSafe Jev、OpenRouter、自托管的 localjev 或结构化输出 LLM。<br><sub><b>Jev 用法:</b> 通过与提供方无关的 jev_compat 协议提出类型化的 noul/choice/score 问题，可按人设覆盖模型。</sub><br><sub>相关: <a href="https://github.com/maha0525/SAIVerse">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/tylerjharden/ailerix"><img src="https://opengraph.githubassets.com/1/tylerjharden/ailerix" alt="Ailerix" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/tylerjharden/ailerix">Ailerix</a></b><br><sub>tylerjharden · GitHub · ⭐ 2 · 2026-09-16</sub><br>OpenRouter 风格的模型路由器，只提供一个 ailerix/auto slug：Jev 先把每个请求归入类型化目录中的某条路由，再由按单任务成本构建的帕累托链选择提供商。<br><sub>相关: <a href="https://ailerix.vercel.app">app</a> · <a href="https://ailerix.vercel.app">app 2</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/anpicasso/hermes-jev-curator"><img src="https://opengraph.githubassets.com/1/anpicasso/hermes-jev-curator" alt="hermes-jev-curator" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/anpicasso/hermes-jev-curator">hermes-jev-curator</a></b><br><sub>anpicasso · GitHub · ⭐ 2 · 2026-09-21</sub><br>Hermes Agent 插件，让 Jev 给 agent 创建的每对 skill 标注关系，如重复、子集、冲突、无关等，并把结果转成安全的归档计划。<br><sub><b>Jev 用法:</b> 每对候选 skill 在 8 种关系中做一个 Choice；默认处于只读的观察模式。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/FirasSX914/Janus"><img src="https://raw.githubusercontent.com/FirasSX914/Janus/main/results/figures/janus_demo.gif" alt="Janus" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/FirasSX914/Janus">Janus</a></b><br><sub>FirasSX914 · GitHub · ⭐ 2 · 2026-09-17</sub><br>路由器，根据置信度把每个决策交给 Jev 或更大的回退模型；阈值先在你自己的标注数据集或决策日志上测出来，而不是直接套用默认值。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/iJ03l/jear"><img src="https://opengraph.githubassets.com/1/iJ03l/jear" alt="jear" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/iJ03l/jear">jear</a></b><br><sub>iJ03l · GitHub · ⭐ 2 · 2026-09-18</sub><br>Rust 客户端，按预算、质量和敏感度把请求路由到 NEAR AI Cloud 模型和 IronClaw agent，用户永远不必自己挑模型或 agent。<br><sub><b>Jev 用法:</b> Choice 选 agent，Score 评估复杂度和敏感度，Noul 标记是否需要私有 TEE，以及请求是否有风险或紧急。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/bojansandhaus/jev-decisions"><img src="https://cdn-thumbnails.huggingface.co/social-thumbnails/spaces/bojansandhaus/jev-agent-decision-playground.png" alt="Jev Decisions" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/bojansandhaus/jev-decisions">Jev Decisions</a></b><br><sub>bojansandhaus · GitHub · ⭐ 2 · 2026-09-19</sub><br>面向 Hermes 及其他 agent 的插件，新增若干工具：审查高风险计划、建议人工审批、对照来源核查答案、评估任务是否真正完成，并维护本地决策日志。<br><sub>相关: <a href="https://huggingface.co/spaces/bojansandhaus/jev-agent-decision-playground">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/freepik-company/jev-mcp"><img src="https://opengraph.githubassets.com/1/freepik-company/jev-mcp" alt="Jev MCP (Freepik)" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/freepik-company/jev-mcp">Jev MCP (Freepik)</a></b><br><sub>freepik-company · GitHub · ⭐ 2 · 2026-09-21</sub><br>依赖极少的 Go MCP 服务器，通过 OpenRouter 或 TypeSafe 提供五个类型化决策工具（decide、classify、verify、rerank），校验提供方返回的每个答案，并且从不重试付费调用。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/hugo-alves/jev-router-playground"><img src="https://raw.githubusercontent.com/hugo-alves/jev-router-playground/main/assets/preview.png" alt="Jev Router Playground" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/hugo-alves/jev-router-playground">Jev Router Playground</a></b><br><sub>hugo-alves · GitHub · ⭐ 2 · 2026-09-18</sub><br>演练场：用带路由描述的 OpenRouter 模型组建模型池，交给 Jev 一个任务，再把它的选择和概率分布与你认为最好的答案做对比。<br><sub>相关: <a href="https://kvhx37ziab90c.space.minimax.io">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/typakon4/jev-layer"><img src="https://raw.githubusercontent.com/typakon4/jev-layer/main/docs/jev-layer-banner.svg" alt="jev-layer" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/typakon4/jev-layer">jev-layer</a></b><br><sub>typakon4 · GitHub · ⭐ 2 · 2026-09-19</sub><br>可移植的 agent harness 决策层，适用于 Hermes、OMP、Codex 和通用 MCP，把有边界的选择交给 Jev 并记录回执以便回放，执行、权限和审批仍由宿主掌握。<br><sub>相关: <a href="https://www.npmjs.com/package/jev-layer">npm</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/rajasekharponakala/jev-mcp"><img src="https://external-preview.redd.it/PbioKRcq0xCJWCgwmAl45cEjLvDs5nxQCdmpvf2NylQ.png?auto=webp&amp;s=ac4ff6f727d3bab17dbc1f6dcdee59f0005949cd" alt="jev-mcp" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/rajasekharponakala/jev-mcp">jev-mcp</a></b><br><sub>rajasekharponakala · GitHub · ⭐ 2 · 2026-09-21</sub><br>MCP 服务器，为 Claude Code、OpenCode 等 agent 提供类型化 Jev 工具：jev_evaluate 用于一组并行问题，另有 jev_noul、jev_choice、jev_score 和 jev_models。<br><sub>相关: <a href="https://www.reddit.com/r/opencodeCLI/comments/1wm3mg7/jev_mcp_in_opencode/">demo</a> · <a href="https://www.reddit.com/r/OpenSourceeAI/comments/1wm3n4z/jev_mcp_in_opencode/">discussion</a></sub></td>
</tr>
</table>

<details><summary>还有 96 条</summary>

- **[jev-model-router (OpenRouter)](https://github.com/lucianfialho/jev-model-router)** · <sub>lucianfialho · GitHub · ⭐ 2 · 2026-09-19</sub><br>Python 路由器，对每个请求分类，每次决策都从 OpenRouter 实时的完整模型目录中挑选能胜任的最便宜模型，而不是用写死的模型列表。
- **[todo-jev](https://github.com/maker-KK/todo-jev)** · <sub>maker-KK · GitHub · ⭐ 2 · 2026-09-18</sub><br>任务路由实验，用 Jev 给请求分类，推荐本地规则、专业 skill 或基础模型，把 skill 的适用/排除条件与本地环境检查结合起来。
- **[ToolGate](https://github.com/ndolinschi/toolgate)** · <sub>ndolinschi · GitHub · ⭐ 2 · 2026-09-17</sub><br>针对 agent 计划中的工具或 MCP 调用的关卡，返回允许、询问人工或拒绝，附五级风险评分，并检查数据外泄、不可逆性和违反策略的情况。
- **[typesafe-jev-mcp](https://github.com/anasbekheit/typesafe-jev-mcp)** · <sub>anasbekheit · GitHub · ⭐ 2 · 2026-09-20</sub><br>Rust MCP 服务器，只有一个 evaluate 工具，让 Claude Code、Codex、OpenCode、Antigravity 或 Cursor 把 state 和类型化问题发给 Jev，拿回带概率的 noul、choice 或 score 答案。
- **[Hive Jev routing backend](https://github.com/DJLougen/hive/blob/main/hive/jev_backend.py)** · <sub>DJLougen · GitHub · ⭐ 39 仓库 · 2026-06-01</sub><br>面向 AI agent 的 CPU 侧动作路由器 Hive 的 Jev 后端：Jev 选出下一个工具，并评估它能否不经 LLM 直接安全执行。一次校准探测发现，默认的 0.95 安全关卡从未触发。
- **[agent-rdf-memory 的 Jev 判断模式](https://github.com/OpenLinkSoftware/ai-agent-skills/blob/main/agent-rdf-memory/howto/jev-judgment-modality.ttl)** · <sub>OpenLinkSoftware · GitHub · ⭐ 39 仓库 · 2025-12-19</sub><br>OpenLink 的 OPAL agent skill 中的一份 RDF HowTo，为其记忆 harness 增加可选的 System One 判断模式（Jev、Laya 或 NanoJev），用于把关 HowTo 候选以及“追问还是直接行动”的引导，可在影子或启用模式下运行。
- **[Synkora TypeSafe tools](https://github.com/getsynkora/synkora-ai/blob/master/api/src/services/agents/internal_tools/typesafe_tools.py)** · <sub>getsynkora · GitHub · ⭐ 35 仓库 · 2026-09-18</sub><br>自托管 Synkora 平台上面向 agent 的内置 Jev 评估工具：通用的 state 加问题调用、招聘等具名配置、报告格式化器和演练场。
- **[Grok 机器人的 ask-jev 前置关卡](https://x.com/ChuckHTF/status/2102187054381617367)** · <sub>ChuckHTF · X · ♥ 1 · 2026-09-22</sub><br>由一批 Grok 机器人和助手组成的个人工作台，现在遇到小型的是/否、分桶和 1-5 打分判断时，会先通过 OpenRouter 的 Decisions API 询问 Jev，而不是唤醒 Grok。
- **[LifeOS Jev orchestrator experiments](https://github.com/nbramia/LifeOS/tree/main/scripts/jev_eval)** · <sub>nbramia · GitHub · ⭐ 31 仓库 · 2026-01-07</sub><br>自托管个人助手 LifeOS 中的六个离线实验，在录制的真实对话轮次上测试 Jev 的类型化判断能否在路由、循环内决策和延迟方面帮到其聊天编排器。
- **[Arbos Jev router](https://github.com/unarbos/arbos/blob/main/crates/arbos-engine/src/jev.rs)** · <sub>unarbos · GitHub · ⭐ 30 仓库 · 2026-03-18</sub><br>文件系统原生的 agent 协调器 Arbos 中的结构化路由器：Jev 根据情境卡片选出下一步机械性的工具操作，写作、规划和对话交给 LLM；act=llm 会把这一轮交给聊天模型。
- **[Helm API Jev classifier](https://github.com/EasyMetaAu/helm-api/tree/main/packages/core/src/classifier)** · <sub>EasyMetaAu · GitHub · ⭐ 30 仓库 · 2026-05-29</sub><br>自托管 LLM 路由网关 Helm API 中的请求分类器，把最后一条用户消息发给 Jev，拿回任务类型和复杂度的选择，据此为请求挑选通道和提供方。
- **[Nebius Physical AI Jev model router](https://github.com/nebius/nebius-physical-ai/blob/main/npa/src/npa/agent_backend/model_router.py)** · <sub>nebius · GitHub · ⭐ 30 仓库 · 2026-04-07</sub><br>Nebius Physical AI Workbench agent 后端中仅作参考的模型路由器，询问 Jev 某个请求需要快速的 Nemotron 模型，还是能做多步推理的 MiniMax-M3，Jev 弃权或出错时不选任何模型。
- **[AmberAgent Jev runtime](https://github.com/soul99soul-glitch/AmberAgent/tree/main/app/src/main/java/app/amber/core/jev)** · <sub>soul99soul-glitch · GitHub · ⭐ 26 仓库 · 2026-05-08</sub><br>安卓 AI 工作空间 AmberAgent 中的 Jev 运行时，用于有边界的手机屏幕和网页目标、模型议会路由、记忆重排、语义工具搜索，以及在过长的工具输出送达模型前做裁剪。
- **[Loki Jev Auto](https://github.com/wundercorp/loki/blob/main/agent/jev_auto_router.py)** · <sub>wundercorp · GitHub · ⭐ 26 仓库 · 2026-09-17</sub><br>自我改进型 agent Loki 中的 Jev Auto 路由器，在已选定的网关上，从有限的模型目录中为每个新会话挑选模型，另有可选的 Jev 类型化判断工具。
- **[VisionClaw Jev validation](https://github.com/Huskyauto/VisionClaw-Agent-Public-Release/blob/main/server/lib/typesafe-auto-validation.ts)** · <sub>Huskyauto · GitHub · ⭐ 26 仓库 · 2026-04-15</sub><br>自托管多租户 agent 工作空间 VisionClaw 中有边界、仅作参考的 Jev 客户端，作为 agent 工具暴露，用于评估交付物的证据支撑、需求覆盖以及是否需要人工复核。
- **[abmind System One judgments](https://github.com/aksika/abmind/blob/dev/src/judgment-provider.ts)** · <sub>aksika · GitHub · ⭐ 20 仓库 · 2026-04-13</sub><br>可插拔的 System One 判断提供器，属于面向 AI agent 的持久记忆与 RAG 引擎 abmind，把召回和诊断类问题发给 Jev 或本地部署的 Laya 模型，结果作为建议交给组合代码。
- **[askjev](https://github.com/pZacca/askjev)** · <sub>pZacca · GitHub · ⭐ 1 · 2026-09-17</sub><br>非官方 MCP 服务器，可通过 stdio 在本地运行，也可托管在 Cloudflare Workers 上：agent 针对手头的材料提一个普通问题，Jev 自行选择是/否、量表或选择题形式，并给出校准的概率。
- **[carryforward](https://github.com/Dharundp6/jev-carryforward)** · <sub>Dharundp6 · GitHub · ⭐ 1 · 2026-09-18</sub><br>MCP 服务器，在 agent 会话中把事实记录到按项目划分的账本里，并在任务开始时通过 Vercel AI Gateway 调用 Jev，只召回与该任务相关的事实。
- **[DGUI-HyperMem](https://github.com/ctaxnagomi/dgui-hypermem)** · <sub>ctaxnagomi · GitHub · ⭐ 1 · 2026-09-19</sub><br>部署在 Cloudflare Workers 上的自托管记忆 MCP 服务器，融合向量召回和全文召回，再用 Jev 对记忆重排、标注类型和显著度，并丢掉不值得长期保留的闲聊。
- **[群聊 agent 选择器](https://x.com/vadimchoi/status/2101937206063780084)** · <sub>vadimchoi · X · ♥ 1 · 2026-09-21</sub><br>对比三种决定群聊中由哪个 agent 回答的方式：@提及；LLM 编排器，每条消息 4-7 秒、$0.00046；Jev，中位数 0.29 秒、$0.00002。
- **[Hermes Jev Router](https://github.com/ussyverse/hermes-jev-router)** · <sub>ussyverse · GitHub · ⭐ 1 · 2026-09-16</sub><br>实验性 Hermes 插件，其 jev_route_plan 工具用 Jev 评估任务复杂度，再由策略在成本、token、上下文、延迟和能力限制内挑选允许的模型；尚未在线上实际运行。
- **[hermes-jev-north-star](https://github.com/poponline63/hermes-jev-north-star)** · <sub>poponline63 · GitHub · ⭐ 1 · 2026-09-18</sub><br>Hermes Agent skill，会反复询问所有者，直到这次运行有一条可检验的终点线，然后生成运行提示词，并用 shell 检查加 Jev 来把关完成度，Jev 负责脚本无法判定的需求。
- **[Jev MCP Server](https://github.com/MattiooFR/mcp-server-jev)** · <sub>MattiooFR · GitHub · ⭐ 1 · 2026-09-20</sub><br>MCP 服务器，为 Codex、Claude 等客户端提供一个用于类型化 Jev 决策的通用工具，并附带八个可复现的实时场景，从客服分诊到线索评估再到查重。
- **[Jev One](https://github.com/thezem/jev-one)** · <sub>thezem · GitHub · ⭐ 1 · 2026-09-19</sub><br>实验性 TypeScript 运行时：Jev 从应用提供的词汇表（词语、地点、工具或停止请求）中做选择，应用执行每个选择并把观察结果反馈回去，直到目标被验证达成。
- **[jev-compaction (picaye)](https://github.com/picaye/jev-compaction)** · <sub>picaye · GitHub · ⭐ 1 · 2026-09-18</sub><br>Hermes Agent 会话的上下文压缩，从不做摘要：Jev 给每个工具调用打分，过时的调用和结果被删除或截断，保留下来的内容一字不改。
- **[jev-eval-mcp](https://github.com/BYK/jev-mcp)** · <sub>BYK · GitHub · ⭐ 1 · 2026-09-17</sub><br>评测优先的 Jev MCP 服务器，提供的工具可以快速试写问题、把一组问题映射到大量条目上，并在标注样例上衡量问题变体的准确率、校准和阈值。
- **[jev-harness-router](https://github.com/JoacoMarc/jev-harness-router)** · <sub>JoacoMarc · GitHub · ⭐ 1 · 2026-09-18</sub><br>面向 agent harness 的逐轮路由器：一次约 350 毫秒的 Jev 调用，在硬性截止时间内确定模型档位、推理强度、工具和 skill；选对 skill 的比例为 90.0%，关键词方法为 59.4%。
- **[jev-mcp (CodeIA Academy)](https://github.com/CodeIA-Academy/jev-mcp)** · <sub>CodeIA-Academy · GitHub · ⭐ 1 · 2026-09-20</sub><br>零依赖的本地 MCP 服务器，文档为西班牙语，向 Claude Code、Codex、Cursor、Hermes 等 agent 提供 ask_jev 和 list_jev_models。
- **[jev-model-router](https://github.com/az9713/jev-model-router)** · <sub>az9713 · GitHub · ⭐ 1 · 2026-09-19</sub><br>网页聊天：Jev 为每条消息挑选由哪个 LLM 回答，再由选中的模型回复，二者都经由 Vercel AI Gateway，并附有开发过程记录和可靠性评估。
- **[jev-toolkit](https://github.com/jbt95/jev-toolkit)** · <sub>jbt95 · GitHub · ⭐ 1 · 2026-09-21</sub><br>基于 Effect、MCP 优先的工具包，其 jev mcp 服务器为任意 harness 提供 Choice、Noul 和 Score 判断以及 verify 和 review 工具，另有 CLI 的 triage、audit、label 和 route 命令，以及 Prometheus 影响指标。
- **[JevHarness](https://github.com/kevin9327/jev-harness)** · <sub>kevin9327 · GitHub · ⭐ 1 · 2026-09-18</sub><br>针对单个 agent 工具调用的执行前关卡：一次混合 Jev 请求返回 allow/ask/deny 结论、不可逆程度分数和是/否检查，再由 Python 代码转为执行、确认或拒绝。
- **[openclaw-jev-compaction](https://github.com/SqaaSSL/openclaw-jev-compaction)** · <sub>SqaaSSL · GitHub · ⭐ 1 · 2026-09-20</sub><br>OpenClaw 的上下文引擎，询问 Jev 会话还需要哪些工具调用和结果，丢掉其余部分，并且从不做摘要，因此留下的都是原文。
- **[PerfectRecall](https://github.com/arslanr-com/perfectrecall)** · <sub>arslanr-com · GitHub · ⭐ 1 · 2026-09-21</sub><br>Hermes 的 agent 记忆，让 Jev 根据调用方 agent 给出的简短标准逐条检查已存记忆，不用 embedding；早期版本把 LongMemEval-S 的回答错误从 120 道中的 62 道降到 17 道。
- **[UX3 Product Design Harness Jev gate](https://github.com/cis2042/product-design-harness/blob/main/scripts/jev_gate.py)** · <sub>cis2042 · GitHub · ⭐ 17 仓库 · 2026-07-11</sub><br>由 agent 操作的产品设计 harness 中的决策关卡，用 Jev 路由任务并评估产品决策，返回继续、验证或停下重新框定问题的结论，以及任务边界。
- **[Citadel promotion decisions](https://github.com/masumi-network/Citadel/blob/main/kb/promotion.py)** · <sub>masumi-network · GitHub · ⭐ 16 仓库 · 2026-05-20</sub><br>面向工程团队及其 agent 的自托管记忆系统 Citadel 中的晋升步骤：Jev 以 0.7 为阈值，判断收集到的条目是否相关、能否安全地晋升为共享知识。
- **[Archive Center Jev selector](https://github.com/Flazer31/archive-center/blob/main/go-service/internal/httpapi/prepare_turn_jev.go)** · <sub>Flazer31 · GitHub · ⭐ 15 仓库 · 2026-06-30</sub><br>本地优先的 RisuAI 聊天记忆后端 Archive Center 中可选的 Jev 选择器和审查器，负责挑选哪些已存记忆和来源证据传入下一次请求，但从不写入记忆。
- **[sportsclaw Jev evidence verifier](https://github.com/machina-sports/sportsclaw/blob/main/docs/guide/jev-evidence-verifier.md)** · <sub>machina-sports · GitHub · ⭐ 15 仓库 · 2026-02-22</sub><br>可选启用的证据验证器，属于把 LLM 接入实时体育数据的 CLI 和机器人脚手架 sportsclaw，用类型化的 JevDecisionClient 做最后的证据检查，高置信度支持时跳过生成式验证环节。
- **[ExploitHunter Jev decision specialist](https://github.com/justsml/ExploitHunter.app/blob/main/src/server/research/jev-decision-specialist.ts)** · <sub>justsml · GitHub · ⭐ 14 仓库 · 2026-05-21</sub><br>进攻性安全研究 harness，把 Jev 用作有边界的决策专家来挑选工具和渲染格式，提供 defer 选项，并为每次调用持久保存回执。
- **[JarvisCore Jev decisions](https://github.com/Prescott-Data/jarviscore-framework/blob/main/jarviscore/execution/decisions.py)** · <sub>Prescott-Data · GitHub · ⭐ 14 仓库 · 2026-01-07</sub><br>多 agent 运行时 JarvisCore 原生支持 Jev：agent 通过独立于文本模型的决策客户端提出类型化的 Choice、Score 和 Noul 问题，内核则用 Choice 挑选专家子 agent。
- **[ai-csuite Jev judgments](https://github.com/Fei2-Labs/skill-genie/blob/main/skills/ai-csuite/scripts/jev.py)** · <sub>Fei2-Labs · GitHub · ⭐ 12 仓库 · 2026-01-09</sub><br>AI C-Suite 战略辩论 skill，可以用 Jev 对决策议题分类，并评判各位高管的第一轮立场；没有 key 时回退到关键词逻辑。
- **[ChainlessChain skill decision layer](https://github.com/chainlesschain/chainlesschain/blob/main/packages/cli/src/lib/decision-layer/typesafe-provider.js)** · <sub>chainlesschain · GitHub · ⭐ 11 仓库 · 2025-12-01</sub><br>个人 AI 管理 CLI 中的 skill 决策层，可以询问 Jev 该由哪个 skill 处理请求，带 800 毫秒超时、用量计量和一个基准测试 harness。
- **[IPFS Accelerate TypeSafe advisor](https://github.com/endomorphosis/ipfs_accelerate_py/tree/main/ipfs_accelerate_py/agent_supervisor/integrations)** · <sub>endomorphosis · GitHub · ⭐ 11 仓库 · 2024-05-18</sub><br>模型服务器兼 agent 监管器，带有仅作参考的 TypeSafe 集成，在项目自有的 Intelligence Index 之外负责路由任务类型、守护执行轨迹和校准决策。
- **[tinyhivemind-typesafe](https://github.com/tinyhumansai/tinyhivemind/tree/main/crates/tinyhivemind-typesafe)** · <sub>tinyhumansai · GitHub · ⭐ 11 仓库 · 2026-08-31</sub><br>Rust crate，让多 agent 协调库 TinyHiveMind 用 Jev 路由交接，选出最合适的队友，同时也路由给其他概率高于 20% 的选项。
- **[Soothe TypeSafe decisions](https://github.com/mirasoth/soothe/blob/main/benchmarks/benchmark_typesafe_decisions.py)** · <sub>mirasoth · GitHub · ⭐ 10 仓库 · 2026-03-12</sub><br>面向长时间运行 agent 的目标驱动编排框架，用类型化决策对输入意图分类并审计目标完成情况，另有一个针对托管 Jev、Laya 或 NanoJev 服务器的基准测试。
- **[Starlight dialogue continuation](https://github.com/divaltor/starlight/blob/main/apps/starlight/src/ai/dialogue-continuation.ts)** · <sub>divaltor · GitHub · ⭐ 10 仓库 · 2024-01-05</sub><br>Telegram 机器人，对每条群消息询问 Jev：用文字回复、用表情回应还是保持沉默，以及哪个表情合适。
- **[NyatBot Jev guards](https://github.com/ZYHUO/nyat-bot/blob/nyatos/src/ai/jev.ts)** · <sub>ZYHUO · GitHub · ⭐ 9 仓库 · 2026-04-10</sub><br>Telegram 群聊 agent，用 Jev 识别换了说法的自我重复消息，并拦截群里没人提过、也没人问过的幻觉事实。
- **[Ratify Jev tool-selection adapter](https://github.com/identities-ai/ratify-protocol/blob/main/references/langchain/authority_reference/jev_adapter.py)** · <sub>identities-ai · GitHub · ⭐ 9 仓库 · 2026-04-19</sub><br>Ratify 委托授权协议的 LangChain 参考关卡：Jev 提议 agent 应调用哪个工具，Ratify 再在接收端验证签名授权。
- **[AgentX decision backends](https://github.com/anis-marrouchi/agentx/blob/master/src/decisions/backends/simple-jev.ts)** · <sub>anis-marrouchi · GitHub · ⭐ 8 仓库 · 2026-02-11</sub><br>面向小企业的自托管 AI agent 网格，其决策层可以在本地 LLM 或 simple-jev 服务器上运行 Jev 风格的类型化决策，并把置信度重新计算为归一化熵。
- **[Crucible system_one route](https://github.com/neuralmagic/crucible/blob/main/examples/route/crucible.toml)** · <sub>neuralmagic · GitHub · ⭐ 8 仓库 · 2026-07-29</sub><br>目标导向的研究循环引擎，附带一个示例领域：决策角色通过任意 POST /v1/systemone 服务器为工单做路由，可以是托管的 Jev，也可以是 vLLM DiffusionGemma 服务器。
- **[Diana TypeSafe client](https://github.com/SuInk/Diana/blob/main/model/llm/typesafe.go)** · <sub>SuInk · GitHub · ⭐ 8 仓库 · 2026-07-02</sub><br>面向 QQ、Telegram、钉钉、飞书和企业微信的自托管群聊 agent，可以用 Jev 判断要不要插话，以及某条消息是不是在对机器人说。
- **[DurinDoor Jev routing classifier](https://github.com/bloodf/durindoor/blob/main/open-sse/config/jev.js)** · <sub>bloodf · GitHub · ⭐ 8 仓库 · 2026-07-03</sub><br>覆盖 236 家提供商的自托管 AI 网关，可以让 Jev 把每个请求归为简单、中等、复杂或推理类，并路由到任务级别匹配的组合成员。
- **[HiRoute Jev decider](https://github.com/higress-group/HiRoute/tree/main/decision-extensions/extensions/jev-decider)** · <sub>higress-group · GitHub · ⭐ 8 仓库 · 2026-09-12</sub><br>HiRoute 本地模型路由器的参考决策服务，在每个 agent 轮次边界调用一次 Jev，选出下一个模型分支，并给上一段的完成质量打分。
- **[Imajin TypeSafe connector](https://github.com/ima-jin/imajin-ai/tree/main/apps/kernel/src/lib/typesafe)** · <sub>ima-jin · GitHub · ⭐ 8 仓库 · 2026-02-11</sub><br>MJN 信任协议参考实现中的服务连接器，让各个身份在受限的 typesafe:decide 授权下，用内核持有的密封 API key 调用 Jev。
- **[RememberStack TypeSafe adapter](https://github.com/writeitai/remember-stack/blob/main/src/rememberstack/adapters/typesafe.py)** · <sub>writeitai · GitHub · ⭐ 8 仓库 · 2026-06-11</sub><br>面向 AI agent 的开放记忆基础设施，追踪论断、当前信念及其来源，带一个 System One 端口，其 TypeSafe 适配器在 Jev 上运行类型化评估。
- **[opencompany approval review](https://github.com/useopencompany/opencompany/blob/main/packages/agent/src/approval-review.ts)** · <sub>useopencompany · GitHub · ⭐ 7 仓库 · 2026-05-20</sub><br>AI 工作空间 opencompany 中的审批复核器：只有当日常集成操作与用户请求一致且看起来低风险时，Jev 才会自动批准；破坏性操作、计费操作或权限变更一律询问用户。
- **[OriginOS Jev perception decisions](https://github.com/NeuralNexusPro/startupOS/tree/main/packages/core/src/lib/integrations/jev)** · <sub>NeuralNexusPro · GitHub · ⭐ 7 仓库 · 2026-07-02</sub><br>本地 AI 工作系统 OriginOS 感知规则的可选 Jev 决策模式：当一个事件可能交给多个已授权的项目、角色或 skill 时，由 Jev 选定目标，低置信度的情况交给用户。
- **[Paprwork jev_decide tool](https://github.com/Papr-ai/paprwork/blob/master/docs/JEV.md)** · <sub>Papr-ai · GitHub · ⭐ 7 仓库 · 2026-01-27</sub><br>本地优先的桌面 agent 应用 Paprwork 中的 Mastra 工具，让 agent、子 agent 和定时任务向 Jev 提出类型化的 noul、choice 或 score 问题，带输入护栏，支持 Papr 代理或自带 key 两种认证。
- **[AIQSA Jev decision features](https://github.com/insciqq/AIQSA/blob/main/lib/domain/decisionModels.ts)** · <sub>insciqq · GitHub · ⭐ 6 仓库 · 2026-07-22</sub><br>自托管多提供商 AI 工作空间 AIQSA 中的 Jev 集成，通过 OpenRouter 发起决策调用，用于记忆和知识库相关性判断、工具发现和 skill 推荐，每项功能都在单独验证合格后才启用。
- **[Jev MCP server](https://github.com/podcctv/Narwhal-Cloud-podman-watcher/blob/main/scripts/jev_mcp_server.py)** · <sub>podcctv · GitHub · ⭐ 6 仓库 · 2026-04-14</sub><br>随 Narwhal Cloud 容器监控工具附带的零依赖 Python MCP 服务器，为 Claude Code、Cursor 或 Antigravity 等 agent 提供 jev_choice、jev_noul、jev_score、jev_gate 和 jev_batch 工具。
- **[unhardcoded-engine decision protocol](https://github.com/genlayerlabs/unhardcoded-engine/blob/main/docs/DECISION-PROTOCOL.md)** · <sub>genlayerlabs · GitHub · ⭐ 6 仓库 · 2026-05-19</sub><br>纯 Lua 编写的 LLM 提供方选择策略代数 unhardcoded-engine 中的决策模型路由，按协议划分候选，让 Jev 风格的决策请求只在决策模型之间路由和故障切换。
- **[Mimir TypeSafe skill and tool selection](https://github.com/shivendrasoni/mimir/blob/main/src/typesafe.rs)** · <sub>shivendrasoni · GitHub · ⭐ 5 仓库 · 2026-08-13</sub><br>Rust 递归语言模型 agent 运行时 Mimir 中的 TypeSafe 集成，在模型调用前选出适用的 skill 并列出所需工具的候选清单，经过影子、金丝雀和验收基准测试逐步上线。
- **[nova-decide](https://github.com/mas-bandwidth/nova-tools/blob/main/docs/SPEC-DECIDE.md)** · <sub>mas-bandwidth · GitHub · ⭐ 5 仓库 · 2026-08-07</sub><br>类型化决策路由，属于让不同模型上的 AI agent 互发消息、等待和集群协作的工具集 Nova Tools：Jev 在确定性机制旁回答小型的选择、打分或是/否判断。
- **[Safeplane routing advisor](https://github.com/stefanrossmeier/safeplane/tree/main/experiments/routing_advisor)** · <sub>stefanrossmeier · GitHub · ⭐ 5 仓库 · 2026-07-22</sub><br>实验性路由顾问，通过 OpenRouter Decisions 询问 Jev 操作员的请求该交给哪个工作流；所属的 Safeplane 是面向有边界 AI agent 工作流的本地优先控制平面，带 CLI 和 Telegram 连接器。
- **[SilkChat Jev skill selection](https://github.com/medy17/SilkChat/blob/main/convex/lib/models/typesafe.ts)** · <sub>medy17 · GitHub · ⭐ 5 仓库 · 2026-02-11</sub><br>基于 TanStack Start 和 Convex 的 AI 聊天应用 SilkChat 中的 Jev 集成，在对话第一轮挑选要启用的 skill：网页搜索、代码执行、记忆、数学或图像生成。
- **[the-array Jev decision layer](https://github.com/clduab11/the-array/blob/main/docs/jev-decision-layer.md)** · <sub>clduab11 · GitHub · ⭐ 1 仓库 · 2026-09-11</sub><br>自托管 LiteLLM 网关参考构建中可选启用的 Jev 层，负责挑选模型档位，并把回复裁定为已回答、拒绝或未作答，在高置信度判定拒答后换下一个模型。
- **[Agent 操作审批](https://openrouter.ai/labs/jev/overseer)** · <sub>OpenRouter · 应用</sub><br>OpenRouter Labs 的示例：在一次请求中对 24 个编程或运维 agent 的工具调用各做四项检查（偏离任务、可能造成破坏、不可信输入、需先询问），让有风险的步骤停下来交给人：0.5 秒给出 96 个答案。
- **[Weathernews 的 agent 操作审批](https://zenn.dev/weathernews/articles/jev-auto-approval-poc)** · <sub>Weathernews (Sakamoto) · 文章 · 2026-09-18</sub><br>Weathernews 把内部 AI agent 中负责审批操作的 LLM 换成了 Jev，分类准确率保持不变，同时降低了延迟和成本，文中分享了设计和对比。
- **[agentic-harness-cli](https://github.com/powerpuff-kitty/agentic-harness-cli)** · <sub>powerpuff-kitty · GitHub · 2026-09-03</sub><br>用于治理 agent-native 仓库的 Rust CLI，其 decisions 命令为布尔型、选择型和有序型决策构建 Jev 请求体，把答案存为需要复核的回执，并在 CI 中拦截校准回归。
- **[AskJev MCP](https://github.com/cbruyndoncx/AskJev-MCP)** · <sub>cbruyndoncx · GitHub · 2026-09-18</sub><br>基于官方 @typesafe-ai/sdk 构建的 MCP 服务器，为 agent 提供 ask_choice、ask_noul 和 ask_score 工具，返回 Jev 选中的选项、每个选项的概率和置信度。
- **[decide-mcp](https://github.com/dakdevs/decide-mcp)** · <sub>dakdevs · GitHub · 2026-09-17</sub><br>本地 MCP 服务器，让 agent 把带上下文和选项的决策交给 Jev（默认经由 AI Gateway），返回推荐选项及各项百分比，支持自定义策略和按偏差画像路由。
- **[Decision Graph Protocol](https://github.com/numerous-com/dgp)** · <sub>numerous-com · GitHub · 2026-09-19</sub><br>面向决策型 agent 的开放协议：应用暴露不可变的证据帧、类型化决策和受保护的操作，由 Jev 适配器给出评估，而副作用始终由应用代码掌控。
- **[Frost](https://github.com/marcus/frost)** · <sub>marcus · GitHub · 2026-09-17</sub><br>用 Go 写的 CLI，输入提示词或 markdown 文档，推荐模型、harness 或 API 以及推理强度：先发一次 Jev 分析请求，再在本地确定性地选出满足质量底线的最便宜配置。
- **[HarnessJudge](https://github.com/ndolinschi/harnessjudge)** · <sub>ndolinschi · GitHub · 2026-09-17</sub><br>给 agent 开发者用的工具：粘贴一段 agent 步骤轨迹，得到通过、重试、升级或停止的决策。
- **[Jev Checkpoint](https://github.com/ashishakkumar/Jev-Checkpoint)** · <sub>ashishakkumar · GitHub · 2026-09-21</sub><br>本地 MCP 服务器，把 agent 有边界的下一步决策（例如继续、检查调用方或询问用户）转成一个 Jev Choice，返回路由、概率和按阈值给出的建议。
- **[JEV plugins](https://github.com/Pinutss/jev-plugins)** · <sub>Pinutss · GitHub · 2026-09-18</sub><br>Cursor 和 Hermes 插件市场，收录 JEV Labs 的四个选择器，分别针对记忆、agent、模型和 MCP 工具，按任务和预算筛选候选，默认在本地运行，Jev 作为可选的评判者。
- **[jev-agent-tool](https://github.com/nandansrikrishna/jev-agent-tool)** · <sub>nandansrikrishna · GitHub · 2026-09-19</sub><br>基于官方 Python SDK 构建、自带 key 的 CLI、Python API 和本地 MCP 服务器，让 agent 在运行时自行设计类型化问题，并拿到带概率的 Jev 决策。
- **[jev-decision-gateway](https://github.com/kuldeepsinh19/jev-decision-gateway)** · <sub>kuldeepsinh19 · GitHub · 2026-09-19</sub><br>挡在昂贵 LLM 前面、不绑定提供方的网关：Jev 回答是否继续、用哪个工具、是否相关、是否通过验证这类小问题，策略层只在确实需要生成时才调用生成模型。
- **[Jev-Evolve](https://github.com/novaleolin/jev-evolve)** · <sub>novaleolin · GitHub · 2026-09-21</sub><br>每个分支都是一个类型化 Jev 问题的 agent 框架，策略文本根据 agent 自己的错误不断演化，并报告收益中有多少来自选择噪声；同一个 schema 因选项顺序不同，得分分别为 0.188 或 0.542。
- **[jev-mcp (codaaiteam)](https://github.com/codaaiteam/jev-mcp)** · <sub>codaaiteam · GitHub · 2026-09-19</sub><br>MCP 服务器，为 Claude Code、Codex、Cursor 或 Pi 提供基于 Jev 的工具，可分类、打分、做是/否检查以及拦截高风险工具调用，每项都只需一次 API 调用。
- **[jev.mcp](https://github.com/hangarbay/jev.mcp)** · <sub>hangarbay · GitHub · 2026-09-17</sub><br>用 Go 编写的 MCP 服务器，把 Jev 暴露为五个工具：classify、score、check、在同一 state 上混合提多个问题的 ask，以及模型列表。
- **[jevkit](https://github.com/walidboulanouar/jev-agent-kit)** · <sub>walidboulanouar · GitHub · 2026-09-20</sub><br>零依赖的 CLI 和 MCP 服务器，带有 route、triage、guard、grep、rank、compact、judge 等十一个基于 Jev 的工具，以及六个可运行的用例，包括 Claude Code 护栏 hook 和 PR 排序器。
- **[LiteLLM auto router](https://docs.litellm.ai/docs/proxy/auto_routing)** (候选发布版) · <sub>LiteLLM · 文章</sub><br>用一个 Jev Choice 为每个请求挑选模型档位。
- **[LiteLLM guardrail](https://docs.litellm.ai/docs/proxy/guardrails/typesafe)** (候选发布版) · <sub>LiteLLM · 文章</sub><br>每完成一次工具交互就问一个 Noul，并在每次调用前清掉不再需要的结果。
- **[Maza](https://github.com/prasanth263/maza)** · <sub>prasanth263 · GitHub · 2026-09-18</sub><br>本地 MCP 网关，你的 MCP 服务器只需连接一次，agent 只会看到两个工具：用 Jev Choice 发现能力的 find_tool，以及 execute_tool。
- **[mcp_jev](https://github.com/pedroknigge/mcp_jev)** · <sub>pedroknigge · GitHub · 2026-09-19</sub><br>面向 Cursor 等 agent 的本地 MCP 服务器，运行现成的 Jev 问题包，并提供类型化的 run_questions 工具，用于自定义 Choice、Noul 和 Score 判断。
- **[McpMatch](https://github.com/ndolinschi/mcpmatch)** · <sub>ndolinschi · GitHub · 2026-09-17</sub><br>网页应用，把用户目标匹配到目录中最合适的 MCP 服务器或能力，目录很大时用两阶段 Jev 筛选。
- **[mewcp-jev](https://github.com/AStheTECH/mewcp-jev)** · <sub>AStheTECH · GitHub · 2026-09-18</sub><br>MCP 服务器，暴露 Jev 的 System One API，让 agent 在一次调用中用混合的是/否、单选和评分标准问题给文本或结构化 state 打分，并列出可用的模型别名。
- **[openclaw-plugin-typesafe-ai](https://github.com/jason-allen-oneal/openclaw-plugin-typesafe-ai)** · <sub>jason-allen-oneal · GitHub · 2026-09-18</sub><br>OpenClaw 插件，用 Jev 做群聊分诊（是否回复）、工具调用安全检查、压缩内容筛选和模型路由，不修改 OpenClaw 核心。
- **[openrouter-jev-mcp](https://github.com/ctmx/openrouter-jev-mcp)** · <sub>ctmx · GitHub · 2026-09-19</sub><br>Python 决策网关兼 MCP 服务器，通过 OpenRouter 的 decisions 端点，把 Jev 以 classify、score 和 check 工具的形式提供给 Claude Code、Codex 和 Cursor，处理 agent 常遇到的小型有边界问题。
- **[ProgressGate](https://github.com/AshutoshVJTI/progressgate)** · <sub>AshutoshVJTI · GitHub · 2026-09-18</sub><br>监测 agent 最近步骤中语义停滞的库，即不同的操作一直在追逐同一个已被推翻的假设；Jev 读取轨迹，再由一个小型确定性策略决定如何处理。
- **[Skilltree](https://github.com/its-panzer/skilltree)** · <sub>its-panzer · GitHub · 2026-09-17</sub><br>本地优先的网站兼 MCP 服务器，把一批 agent 指令转成可浏览的 skill 树，Jev 在每一层做一个可见的类型化选择来决定路径。
- **[SpendBrake](https://github.com/ndolinschi/spendbrake)** · <sub>ndolinschi · GitHub · 2026-09-17</sub><br>agent 运行的预算刹车：读取预算、已花费金额和剩余计划，然后决定继续、降级模型还是停止，并给出性价比分数和超预算检查。
- **[SwarmRouter](https://github.com/ndolinschi/swarmrouter)** · <sub>ndolinschi · GitHub · 2026-09-17</sub><br>把任务路由给研究、编程、浏览器、客服或写作 agent，并给出置信度，在可视化的集群地图上展示。
- **[switchboard](https://github.com/aniruddh-krovvidi/switchboard)** · <sub>aniruddh-krovvidi · GitHub · 2026-09-17</sub><br>基于 Jev、只用 Python 标准库的 LLM 网关护栏和模型路由器，附带一份关于其准确率、校准和延迟的独立评测。
- **[typesafe-mcp-server](https://github.com/bestagentkits/typesafe-demo-mcp)** · <sub>bestagentkits · GitHub · 2026-09-17</sub><br>基于 @typesafe-ai/sdk 构建的 MCP 服务器，把 Choice、Score 和 Noul 判断以及模型列表暴露为 agent 可调用的工具，并附带官方 TypeSafe agent skill。
- **[wakegate](https://github.com/shitianfang/wakegate)** · <sub>shitianfang · GitHub · 2026-09-18</sub><br>失败放行的关卡，适用于运行在 Workers、Durable Objects 和 Node 上的长时间运行 agent：在休眠 agent 的 LLM 被定时器或事件唤醒前，结合 agent 自己的休眠备注询问 Jev 这次唤醒是否重要。

</details>

还缺什么？[提交一个资源](https://github.com/Li-Evan/awesome-jev/issues/new/choose)。
