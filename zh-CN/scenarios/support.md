# 🎧 客服与销售

[English](https://github.com/Li-Evan/awesome-jev/blob/main/scenarios/support.md) · **简体中文**

工单路由、邮件分拣、线索打分和 CRM 自动化。共 44 条，按社区热度排序。

[← 返回 Awesome Jev](https://github.com/Li-Evan/awesome-jev/blob/main/README.zh-CN.md#按场景浏览)

<table>
<tr>
<td width="260" valign="top"><a href="https://x.com/romanbuildsaas/status/2100891604735099103"><img src="https://pbs.twimg.com/amplify_video_thumb/2100891566340501504/img/agvkcRfNWmnGbRI5.jpg" alt="线索与外联消息评分" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/romanbuildsaas/status/2100891604735099103">线索与外联消息评分</a></b><br><sub>romanbuildsaas · X · ♥ 3.3k · 2026-09-18</sub><br>在 40 秒内花 $0.09 为 700 条高意向线索和个性化外联消息打分，用置信度分数预测每条消息的效果，并标记线索与消息不匹配的情况。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://www.youtube.com/watch?v=CupCEehe2OQ"><img src="https://i.ytimg.com/vi/CupCEehe2OQ/hqdefault.jpg" alt="用 Jev 做销售 Copilot" width="240"></a></td>
<td valign="top"><b><a href="https://www.youtube.com/watch?v=CupCEehe2OQ">用 Jev 做销售 Copilot</a></b><br><sub>Kelvin Cleto · 视频 · ♥ 1.9k · 2026-09-20</sub><br>葡萄牙语讲解视频：一个追踪通话和销售剧本步骤的销售会议 copilot，在调用任何 LLM 之前先让 Jev 回答低成本的决策问题，以降低成本。<br><sub><b>Jev 用法:</b> 关于会议 state 的概率问题决定是否发起昂贵的 LLM 调用。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/twentyhq/twenty/tree/main/packages/twenty-server/src/modules/workflow/workflow-executor/workflow-actions/classify"><img src="https://repository-images.githubusercontent.com/572984571/ef151ee9-3060-418b-bf88-cb689ab78c7b" alt="Twenty 的 Classify 工作流动作" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/twentyhq/twenty/tree/main/packages/twenty-server/src/modules/workflow/workflow-executor/workflow-actions/classify">Twenty 的 Classify 工作流动作</a></b><br><sub>twentyhq · GitHub · ⭐ 57.2k 仓库 · 2022-12-01</sub><br>开源 CRM Twenty 工作流中的 Classify 步骤，就一条记录向 Jev 问 choice、score 或布尔问题，让后续步骤根据答案和概率分支。<br><sub><b>Jev 用法:</b> Jev 注册为“evaluation”模型类型（通过 @ai-sdk/typesafe-ai 使用 jev-latest，标注的中位延迟为 200 毫秒）。</sub><br><sub>相关: <a href="https://twenty.com">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/getanyapi-com/lurk"><img src="https://opengraph.githubassets.com/1/getanyapi-com/lurk" alt="lurk" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/getanyapi-com/lurk">lurk</a></b><br><sub>getanyapi-com · GitHub · ⭐ 97 · 2026-09-10</sub><br>可自托管的 Reddit 购买意向发现工具：推断你的产品解决什么问题，让 Jev 针对你的产品评判扫描到的每个标题、帖子和评论。<br><sub><b>Jev 用法:</b> 通过 OpenRouter 或 Vercel AI Gateway 调用 Jev 为每个条目打分；产品画像和聚类由 LLM 负责。</sub><br><sub>相关: <a href="https://x.com/mxfp4/status/2101070906852298910">demo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/Box/status/2100993278955188320"><img src="https://pbs.twimg.com/amplify_video_thumb/2100986163511357440/img/o0Yzl7VqISwchxkk.jpg" alt="Box 事件分诊" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/Box/status/2100993278955188320">Box 事件分诊</a></b><br><sub>Box · X · ♥ 31 · 2026-09-18</sub><br>一个 Box 工作流：拉取一份事件报告，询问 Jev 它是否影响客户、严重程度如何，把文件移到 Escalate、Monitor 或 Review，并把低置信度的情况交给人工。<br><sub><b>Jev 用法:</b> 一个判断是否影响客户的 Noul，加一个严重度 Score，并用置信度阈值决定是否转人工复核。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/tarasshyn/status/2101043617649340678"><img src="https://pbs.twimg.com/amplify_video_thumb/2101043565207916544/img/jTZjaCWwP1d9sx6D.jpg" alt="RedReplier 购买信号评分" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/tarasshyn/status/2101043617649340678">RedReplier 购买信号评分</a></b><br><sub>tarasshyn · X · ♥ 463 · 2026-09-18</sub><br>在 53 秒内花 $0.65，为来自 Reddit、X、Bluesky、Hacker News 和 Facebook 的 170 万条提及中的 1,759,932 个购买信号打分，按意向、产品匹配度和竞品提及排序。</td>
</tr>
<tr>
<td width="260" valign="top"></td>
<td valign="top"><b><a href="https://x.com/t0t0_build/status/2101082444577567162">WhatsApp 客户群监控</a></b><br><sub>t0t0_build · X · ♥ 280 · 2026-09-18</sub><br>实时监控 25+ 个有客户在的 WhatsApp 群，由 Jev 判断是否有需要处理的事，比如紧急问题或未解决的订单，只有这时才让 LLM 写通知。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/sotak/status/2100701152824185319"><img src="https://pbs.twimg.com/amplify_video_thumb/2100700282434826240/img/H7dKngwXowyoEgJ6.jpg" alt="实时 Clippy" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/sotak/status/2100701152824185319">实时 Clippy</a></b><br><sub>sotak · X · ♥ 176 · 2026-09-17</sub><br>产品内的 Clippy，观察用户如何使用应用，只有在 Jev 判断用户犹豫、困惑或卡住时才出现，其反应也由 Jev 选择。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/razeden0/status/2102119174466396250"><img src="https://pbs.twimg.com/amplify_video_thumb/2102119097077006336/img/qrIQdb9RSULrBTqB.jpg" alt="Grok 与 Jev 线索筛选器" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/razeden0/status/2102119174466396250">Grok 与 Jev 线索筛选器</a></b><br><sub>razeden0 · X · ♥ 172 · 2026-09-21</sub><br>线索资格判断管线：Jev 对 3,412 条线索每条回答 6 个问题（15.7 秒内完成 20,472 个决策，花费 $0.41），Grok 4.7 只为值得看的线索起草外联消息。<br><sub><b>Jev 用法:</b> 每条线索六个是/否、单选或打分问题，决定 LLM 要读哪些内容。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/pierreeliottlal/status/2100912453999587657"><img src="https://pbs.twimg.com/amplify_video_thumb/2100911836891660288/img/gqUn5ZSLBlAEMZMT.jpg" alt="能约到演示的外联信号" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/pierreeliottlal/status/2100912453999587657">能约到演示的外联信号</a></b><br><sub>pierreeliottlal · X · ♥ 114 · 2026-09-18</sub><br>销售分析：Jev 读完一个包含数千条外联消息的数据集，找出哪些意向信号带来的演示预约最多，用时 40 秒，花费不到 $0.20。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/nifinet/status/2102065255694409940"><img src="https://pbs.twimg.com/media/HSwI_zwaQAA9uYF.jpg" alt="signal-ranker" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/nifinet/status/2102065255694409940">signal-ranker</a></b><br><sub>nifinet · 文章 · ♥ 105 · 2026-09-21</sub><br>开源外联机器人的搭建指南：Claude Code 抓取线索信号（职位重新发布、融资、招标），Jev 排出优先联系的对象，判断与可调的策略文件分开存放。<br><sub><b>Jev 用法:</b> judge.py 为每条线索信号向 Jev 请求概率；policy.py 无需再次调用，就把它们转成排序。</sub><br><sub>相关: <a href="https://yourmax.ai/">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://www.reddit.com/r/laravel/comments/1wjw2w1/detecting_spam_and_autoreplies_with_jev_and_the/"><img src="https://external-preview.redd.it/Up6svHbkrdKcDREH0Bxoz5U1BdqUtnTWYrPaM5OkqBI.jpeg?auto=webp&amp;s=a662330e21133bc799704e99bd9c97b2df961b97" alt="There There 中的垃圾与自动回复检测" width="240"></a></td>
<td valign="top"><b><a href="https://www.reddit.com/r/laravel/comments/1wjw2w1/detecting_spam_and_autoreplies_with_jev_and_the/">There There 中的垃圾与自动回复检测</a></b><br><sub>freekmurze · Reddit · ▲ 30 · 2026-09-18</sub><br>讲解如何用 Laravel AI SDK 的 Jev 支持在 There There 客服系统中标记垃圾消息和自动回复，附 PHP 编写的 Noul、Choice 和 Score 示例。<br><sub><b>Jev 用法:</b> 对收到的消息用 Noul 判断其为垃圾信息和自动回复的概率。</sub><br><sub>相关: <a href="https://freek.dev/3194-detecting-spam-and-auto-replies-with-jev-and-the-laravel-ai-sdk">article</a> · <a href="https://freek.dev/3194-detecting-spam-and-auto-replies-with-jev-and-the-laravel-ai-sdk">project</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/merefield/discourse-chatbot"><img src="https://raw.githubusercontent.com/merefield/discourse-chatbot/main/images/surety.webp" alt="discourse-chatbot" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/merefield/discourse-chatbot">discourse-chatbot</a></b><br><sub>merefield · GitHub · ⭐ 84 · 2023-02-06</sub><br>用于 Discourse 话题、聊天和客户支持的 RAG 聊天机器人插件，可用 System One 做论坛范围内的判断，用于匹配被屏蔽的问题和选择工具，并以 embedding 作为兜底。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/ENowoslawski/status/2100999124099195377"><img src="https://pbs.twimg.com/amplify_video_thumb/2100998985074835456/img/3FY78J6we-v6cyXz.jpg" alt="即时生成 Clay 工作流" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/ENowoslawski/status/2100999124099195377">即时生成 Clay 工作流</a></b><br><sub>ENowoslawski · X · ♥ 65 · 2026-09-18</sub><br>演示 Jev 几乎瞬间搭建出 Clay 的市场拓展（go-to-market）工作流。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/ZeroGold/call-coach-ai"><img src="https://github.com/user-attachments/assets/b1d3768f-ae61-45a7-a68b-644367ef24ab" alt="Call Coach" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/ZeroGold/call-coach-ai">Call Coach</a></b><br><sub>ZeroGold · GitHub · ⭐ 35 · 2026-09-20</sub><br>实时销售通话助手：每说完一句话就把对话发给 Jev，向销售代表显示建议的下一步动作和购买阶段，并附置信度分数；音源可以是麦克风或示例通话。<br><sub>相关: <a href="https://www.reddit.com/r/LLMDevs/comments/1wltrsa/i_built_an_opensource_app_that_uses_jev_to_coach/">discussion</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/sotak/status/2100927660029247538"><img src="https://pbs.twimg.com/amplify_video_thumb/2100925956978294784/img/grFanN32FuhiSULl.jpg" alt="Inline Manual 自适应帮助" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/sotak/status/2100927660029247538">Inline Manual 自适应帮助</a></b><br><sub>sotak · X · ♥ 23 · 2026-09-18</sub><br>为 InlineManual.com 做的实时应用内支持：检测用户在哪里卡住，直接在界面里加入解释、建议或操作，不需要聊天机器人。<br><sub>相关: <a href="https://inlinemanual.com">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/AIsaOneHQ/status/2100894473085489510"><img src="https://pbs.twimg.com/amplify_video_thumb/2100886600880111616/img/Y6PwJ2mf_8-BWChg.jpg" alt="Worth Replying" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/AIsaOneHQ/status/2100894473085489510">Worth Replying</a></b><br><sub>AIsaOneHQ · X · ♥ 15 · 2026-09-18</sub><br>输入一家公司的域名，找出已经在讨论其产品所解决问题的 X 用户；以 typesafe.ai 为例，它找到 150 条推文，在 18.8s 内做了 750 个 Jev 决策，花费 $0.007。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/yoanbernabeu/demo-symfony-typesafe"><img src="https://raw.githubusercontent.com/yoanbernabeu/demo-symfony-typesafe/main/docs/qualification.jpg" alt="Symfony 客服分诊演示" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/yoanbernabeu/demo-symfony-typesafe">Symfony 客服分诊演示</a></b><br><sub>yoanbernabeu · GitHub · ⭐ 2 · 2026-09-19</sub><br>法语的 Symfony AI 演示：对发给法国公共服务机构的真实请求，每条用一次 Jev 调用做判定，包括请求者属于六种意图中的哪一种、紧急程度，以及是否是需要转给开发者的 bug。<br><sub>相关: <a href="https://x.com/yOyO38/status/2101705862008001011">demo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/GoSailGlobal/status/2100957577958097199"><img src="https://pbs.twimg.com/amplify_video_thumb/2100957554293751809/img/Jfl8lu536UlBOyqr.jpg" alt="jev-support-pulse" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/GoSailGlobal/status/2100957577958097199">jev-support-pulse</a></b><br><sub>GoSailGlobal · X · ♥ 6 · 2026-09-18</sub><br>中文实验：用 Jev 给 170,400 条 2017 年发给七个品牌客服账号的推文打标签，花费 $1.84；在误报相同的情况下，它发现了 17 次故障，比品牌官方承认早约 4.1 小时，而按推文量只能发现 10 次。<br><sub>相关: <a href="https://github.com/zhuyansen/jev-support-pulse">repo</a> · <a href="https://github.com/zhuyansen/jev-support-pulse">project</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/warmbly/warmbly/tree/main/internal/pkg/typesafe"><img src="https://raw.githubusercontent.com/warmbly/warmbly/main/docs/assets/dashboard-campaigns.png" alt="Warmbly 的 TypeSafe 客户端" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/warmbly/warmbly/tree/main/internal/pkg/typesafe">Warmbly 的 TypeSafe 客户端</a></b><br><sub>warmbly · GitHub · ⭐ 308 仓库 · 2026-01-17</sub><br>开源冷外联与邮箱预热平台，用 TypeSafe 判断做收件箱打标签、回复意图分类、草稿把关、退信原因分析和表单提交分诊。<br><sub>相关: <a href="https://warmbly.com">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/malekoo/status/2100439840575684910"><img src="https://pbs.twimg.com/media/HSZCwYKWMAAC4Tr.jpg?name=orig" alt="Mac 应用里的 Jev 应用内帮助" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/malekoo/status/2100439840575684910">Mac 应用里的 Jev 应用内帮助</a></b><br><sub>malekoo · X · ♥ 5 · 2026-09-17</sub><br>无需加载任何模型就能用的 Mac 应用内帮助：Jev 对照内置手册理解问题，选出匹配的文章或判定没有匹配，测试 42/42 全对，中位耗时 0.93 秒。<br><sub><b>Jev 用法:</b> 以整本手册作为 state，在手册文章加一个“无匹配”选项中做 Choice。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/DECRUX9812/openjev"><img src="https://opengraph.githubassets.com/1/DECRUX9812/openjev" alt="open-Jev (DECRUX9812)" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/DECRUX9812/openjev">open-Jev (DECRUX9812)</a></b><br><sub>DECRUX9812 · GitHub · ⭐ 3 · 2026-09-18</sub><br>在本地零成本复刻的 Jev 决策层，在你的 CPU 上就一则招聘启事回答七个类型化问题，把企业内部 IT 招聘与可作为销售线索的小企业区分开。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Nine-Minds/alga-psa/blob/main/ee/server/src/services/smartSearch/typesafeClient.ts"><img src="https://www.nineminds.com/imported-media/Overview%20Dashboard.png" alt="Alga PSA 智能工单搜索" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Nine-Minds/alga-psa/blob/main/ee/server/src/services/smartSearch/typesafeClient.ts">Alga PSA 智能工单搜索</a></b><br><sub>Nine-Minds · GitHub · ⭐ 141 仓库 · 2024-11-04</sub><br>开源 MSP 服务台，其智能搜索让 Jev 重排过滤后的工单和项目列表，于是“客户无法打印”也能搜出“Xerox 报告离线”。<br><sub>相关: <a href="https://github.com/Nine-Minds/alga-psa/blob/main/docs/plans/2026-09-20-jev-smart-ticket-search-plan.md">plan</a> · <a href="https://www.nineminds.com/alga-psa">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/liulangjietou/customer_work/tree/main/customer-work-starter/src/main/java/com/richard/fyoung/customerwork/capability/typesafe"><img src="https://github.com/user-attachments/assets/75a324d7-4e2e-4383-b049-c3cfc7802ee5" alt="customer-work 的 Jev 决策" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/liulangjietou/customer_work/tree/main/customer-work-starter/src/main/java/com/richard/fyoung/customerwork/capability/typesafe">customer-work 的 Jev 决策</a></b><br><sub>liulangjietou · GitHub · ⭐ 133 仓库 · 2026-06-13</sub><br>基于 AgentScope Java 的企业客服 agent 平台，在主对话路径和退款流程中加入 Jev 结构化决策，带熔断器，并在管理后台中影子展示。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/zeetakou/status/2101945022782284192"><img src="https://pbs.twimg.com/amplify_video_thumb/2101930224544104448/img/KJiNk6RfkI8mPRNs.jpg" alt="用 Jev 做电话营销 AI" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/zeetakou/status/2101945022782284192">用 Jev 做电话营销 AI</a></b><br><sub>zeetakou · X · ♥ 2 · 2026-09-21</sub><br>基于 GPT Live API 的外呼 agent，按线索名单拨号并转接有潜力的潜在客户，目前正在测试用 Jev 判断线索是否有潜力、何时转接以及重拨优先级。<br><sub><b>Jev 用法:</b> 通话中和通话后的判断：潜在客户质量、是否立即转接、重拨优先级。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/UiPath/uipath-python/tree/main/packages/uipath/samples/ticket-triage-agent"><img src="https://opengraph.githubassets.com/1/UiPath/uipath-python" alt="UiPath 工单分诊 agent" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/UiPath/uipath-python/tree/main/packages/uipath/samples/ticket-triage-agent">UiPath 工单分诊 agent</a></b><br><sub>UiPath · GitHub · ⭐ 98 仓库 · 2025-01-31</sub><br>一个 UiPath 示例 agent，做两级客服工单分诊：Jev 快速路由每张工单，升级到 Action Center 人工复核，或由 LLM 起草自动回复。<br><sub>相关: <a href="https://uipath.github.io/uipath-python/">docs</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/zhayujie/status/2102009189765881894"><img src="https://pbs.twimg.com/amplify_video_thumb/2102007612569190400/img/Yv_-w6zdmBlVS5Mu.jpg" alt="CowAgent 工单分析工具" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/zhayujie/status/2102009189765881894">CowAgent 工单分析工具</a></b><br><sub>zhayujie · X · ♥ 1 · 2026-09-21</sub><br>基于 Jev 的批量客服工单分析工具，由 CowAgent 构建：每个工单一次调用，约 500 毫秒 返回 7 个带概率的判断。<br><sub><b>Jev 用法:</b> 每个工单在一次请求中问七个类型化问题。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/GhrezaKh74/JevTicktRouter"><img src="https://raw.githubusercontent.com/GhrezaKh74/JevTicktRouter/master/docs/screenshots/00-architecture.png" alt="JevTicketRouter" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/GhrezaKh74/JevTicktRouter">JevTicketRouter</a></b><br><sub>GhrezaKh74 · GitHub · ⭐ 1 · 2026-09-17</sub><br>基于 .NET 10 和 React 19 的客服工单分诊应用，就一张波斯语或英语工单向 Jev 批量问五个问题，再由确定性规则引擎决定路由、升级和脱敏。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/timbuildwithai/status/2102167332172767392"><img src="https://pbs.twimg.com/media/HSxlNgsWMAAzwJr.jpg?name=orig" alt="用 Jev 在 n8n 里做线索资格判断" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/timbuildwithai/status/2102167332172767392">用 Jev 在 n8n 里做线索资格判断</a></b><br><sub>timbuildwithai · X · ♥ 1 · 2026-09-21</sub><br>在 n8n 中搭建的线索资格判断工作流：Jev 返回需求、预算、时机和购买意向的概率，一个 JS 步骤为每条线索打分并按 HOT/WARM/COLD 路由，OpenAI 只负责写回复。<br><sub><b>Jev 用法:</b> 每条线索四个 Noul，在代码中转换为确定性分数。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/TheEleventhAvatar/triage-bot"><img src="https://github.com/user-attachments/assets/9912dc0f-2033-40c7-a149-58a14093dec8" alt="triage-bot" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/TheEleventhAvatar/triage-bot">triage-bot</a></b><br><sub>TheEleventhAvatar · GitHub · ⭐ 1 · 2026-09-19</sub><br>客服工单机器人：Jev 把每张工单路由给通用、账户、账单或技术 agent，并判断是否应由人工接手，然后由 Cerebras 起草回复；两次调用分别计时。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/damien-schneider/reflet/blob/main/packages/backend/convex/feedback/triage_evaluation.ts"><img src="https://opengraph.githubassets.com/1/damien-schneider/reflet" alt="Reflet 反馈分诊" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/damien-schneider/reflet/blob/main/packages/backend/convex/feedback/triage_evaluation.ts">Reflet 反馈分诊</a></b><br><sub>damien-schneider · GitHub · ⭐ 37 仓库 · 2026-01-17</sub><br>开源产品反馈与路线图平台 Reflet 中的反馈分诊：Jev 判断一条提交是否可执行，把垃圾内容挡在公开看板之外，标记需复核的条目并自动打标签。<br><sub><b>Jev 用法:</b> 通过 AI SDK 的 evaluate 调用问 usefulness/junk/needsReview 三个布尔问题，外加每个标签一个问题；junk &gt;= 0.5 即隐藏，标签需达到 0.65，最多 3 个。</sub><br><sub>相关: <a href="https://www.reflet.app">app</a> · <a href="https://github.com/damien-schneider/reflet">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/calagopus/bot/blob/main/src/ai/decisions.rs"><img src="https://opengraph.githubassets.com/1/calagopus/bot" alt="Calagopus 机器人的客服分诊" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/calagopus/bot/blob/main/src/ai/decisions.rs">Calagopus 机器人的客服分诊</a></b><br><sub>calagopus · GitHub · ⭐ 17 仓库 · 2025-12-28</sub><br>为 Calagopus 社区打造的 Rust Discord 机器人中的 AI 客服分诊：用 Jev 判断一条消息是否需要回答，以及起草的回答是否有值得发出的内容。<br><sub>相关: <a href="https://github.com/calagopus/bot">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/abhegd/status/2102195682257854602"><img src="https://pbs.twimg.com/amplify_video_thumb/2102194961856798720/img/WhzCgL1LVnYAq-R9.jpg" alt="自动分拣的应用内反馈" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/abhegd/status/2102195682257854602">自动分拣的应用内反馈</a></b><br><sub>abhegd · X · ▶ 60 · 2026-09-22</sub><br>Layoutstack 演示：打字或语音（ElevenLabs）提交的应用内反馈由 Jev 分类并归入正确的收件箱，附带一份 cookbook，可以让编程 agent 改造复用。<br><sub>相关: <a href="https://www.layoutstack.com/demo/in-appfeedback">app</a> · <a href="https://layoutstack.com/demo/in-appfeedback">project</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/upasana1105/UP_Demos/blob/main/it-helpdesk-assistant/judgment_base_agent/backends/typesafe.py"><img src="https://opengraph.githubassets.com/1/upasana1105/UP_Demos" alt="IT 服务台判断后端" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/upasana1105/UP_Demos/blob/main/it-helpdesk-assistant/judgment_base_agent/backends/typesafe.py">IT 服务台判断后端</a></b><br><sub>upasana1105 · GitHub · ⭐ 9 仓库 · 2026-02-02</sub><br>基于 Gemini agent 平台的企业 IT 服务台 agent 演示，其判断层可以在 TypeSafe System One 上运行 Choice、Noul 和 Score 原语。<br><sub>相关: <a href="https://github.com/upasana1105/UP_Demos">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/rszhd/signalscout/blob/dev/packages/engine/src/ai/provider.ts"><img src="https://opengraph.githubassets.com/1/rszhd/signalscout" alt="SignalScout" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/rszhd/signalscout/blob/dev/packages/engine/src/ai/provider.ts">SignalScout</a></b><br><sub>rszhd · GitHub · ⭐ 8 仓库 · 2026-09-08</sub><br>开源意向监控工具，在 Reddit、X、LinkedIn、YouTube、TikTok 和 Instagram 上搜索正在描述你的产品所解决问题的人，并为每段对话的匹配度和购买意向打分。<br><sub><b>Jev 用法:</b> AI SDK 的 TypeSafe provider 为评分问题提供评估模型（jev-latest，每百万输入 token $0.042）。</sub><br><sub>相关: <a href="https://github.com/rszhd/signalscout">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/sumitrevolt/leadgenrationaivoiceagent/blob/main/app/platform/typesafe_integration.py"><img src="https://opengraph.githubassets.com/1/sumitrevolt/leadgenrationaivoiceagent" alt="LeadGen AI 的 TypeSafe 集成" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/sumitrevolt/leadgenrationaivoiceagent/blob/main/app/platform/typesafe_integration.py">LeadGen AI 的 TypeSafe 集成</a></b><br><sub>sumitrevolt · GitHub · ⭐ 1 仓库 · 2026-09-17</sub><br>面向印度小企业的营销与语音外呼 SaaS LeadGen AI 中的实验性 Jev 层，为 agent 角色挑选专业方向标签，并校验冷邮件等工作产出。<br><sub>相关: <a href="https://github.com/sumitrevolt/leadgenrationaivoiceagent">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/promptgtm-shared/clay-jev-people-ranker"><img src="https://opengraph.githubassets.com/1/promptgtm-shared/clay-jev-people-ranker" alt="clay-jev-people-ranker" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/promptgtm-shared/clay-jev-people-ranker">clay-jev-people-ranker</a></b><br><sub>promptgtm-shared · GitHub · 2026-09-21</sub><br>agent skill 加 Python 工作流：先用确定性过滤条件从 Clay CLI 拉取人员，再在补全数据前让 Jev 判断每个人是否真正符合目标角色，比如目前仍在一线经营的创始人。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/minghanminghan/jev-demo"><img src="https://opengraph.githubassets.com/1/minghanminghan/jev-demo" alt="jev demo" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/minghanminghan/jev-demo">jev demo</a></b><br><sub>minghanminghan · GitHub · 2026-09-17</sub><br>由 Jev 路由的客服聊天机器人，每轮用一次调用问遍路由树的所有层级，在用户要求、表现出不满或置信度低时转交人工。<br><sub><b>Jev 用法:</b> 对所有树层级做推测式扇出，同一请求里还包含一个“是否想找人工”的 Noul 和一个不满程度 Score。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://www.reddit.com/r/SaaS/comments/1wlcpq3/jev_is_insane_for_outbound/"><img src="https://external-preview.redd.it/MDV4czc2Z3JibnFoMWrhC3ZnxXXVSY4h_1Pyuu4bCsFhZrPnFj7vZea_6f45.png?format=pjpg&amp;auto=webp&amp;s=92f8c2805fba08f7d164b31a7d9ed7cb61b0c450" alt="Jev 外联线索分诊" width="240"></a></td>
<td valign="top"><b><a href="https://www.reddit.com/r/SaaS/comments/1wlcpq3/jev_is_insane_for_outbound/">Jev 外联线索分诊</a></b><br><sub>adgrow · Reddit · 2026-09-20</sub><br>外联实验：Jev 在 47 秒内对 462 条线索做了 7,068 个决策，花费约 $0.06，选定开场钩子、切入角度和 CTA，并跳过了 190 条不值得发邮件的线索。<br><sub><b>Jev 用法:</b> 每条线索用 Noul 判断 ICP 匹配度和信号，再用 Choice 选钩子，并在四份起草好的消息中挑一份。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://treg.to/jev"><img src="https://treg.to/media/og.png" alt="Treg 上的 Jev 配方" width="240"></a></td>
<td valign="top"><b><a href="https://treg.to/jev">Treg 上的 Jev 配方</a></b><br><sub>Treg (superdesigndev) · 应用</sub><br>Jev 的交互式指南，包含 LLM 与 Jev 的实时竞速，以及基于 Treg 构建、可复制的 GTM 自动化配方，如注册欺诈筛查、购买信号分诊和爆款内容监控。<br><sub>相关: <a href="https://github.com/superdesigndev/treg">repo</a> · <a href="https://x.com/jasonzhou1993/status/2101988970565603489">demo</a> · <a href="https://github.com/superdesigndev/treg">project</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/EtienneLescot/jev-router"><img src="https://raw.githubusercontent.com/EtienneLescot/jev-router/main/screenshot.png" alt="Jev Router Demo" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/EtienneLescot/jev-router">Jev Router Demo</a></b><br><sub>EtienneLescot · GitHub · 2026-09-18</sub><br>浏览器演示：两次 Jev 调用分别对客服工单做分诊（部门、紧急程度、不满程度）并评估任务规模，再由普通代码将其路由给 agent 或人工，并选择模型档位和推理深度。<br><sub>相关: <a href="https://etiennelescot.github.io/jev-router/">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/ndolinschi/lanebreak"><img src="https://opengraph.githubassets.com/1/ndolinschi/lanebreak" alt="LaneBreak" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/ndolinschi/lanebreak">LaneBreak</a></b><br><sub>ndolinschi · GitHub · 2026-09-17</sub><br>客服工单路由器，选出负责的团队和优先级，并标记退款意图、流失风险，以及应跳过机器人直接交给人工的工单。<br><sub>相关: <a href="https://lanebreak.vercel.app">app</a> · <a href="https://lanebreak.vercel.app">app 2</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://openrouter.ai/labs/jev/triage"><img src="https://openrouter.ai/dynamic-og?title=Support+message+triage&amp;description=Classify+support+messages+with+structured+decisions.&amp;v=2" alt="客服消息分诊" width="240"></a></td>
<td valign="top"><b><a href="https://openrouter.ai/labs/jev/triage">客服消息分诊</a></b><br><sub>OpenRouter · 应用</sub><br>OpenRouter Labs 的配方：就 95 条客服消息每条向 Jev 问五个是/否问题（退款、愤怒、bug、需要人工），并与聊天模型赛跑：每次运行 1.2 秒得到 475 个答案，花费 $0.0014。<br><sub><b>Jev 用法:</b> 每条消息五个 Noul，在一次运行中批量处理。</sub><br><sub>相关: <a href="https://openrouter.ai/typesafe/jev">model</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/brandonbryant12/transcript-scorecard"><img src="https://opengraph.githubassets.com/1/brandonbryant12/transcript-scorecard" alt="Transcript Scorecard" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/brandonbryant12/transcript-scorecard">Transcript Scorecard</a></b><br><sub>brandonbryant12 · GitHub · 2026-09-16</sub><br>概念验证：逐轮回放一通客服电话，每新增一轮就实时评估一次，按加权的员工评分卡重新打分，并把证据、置信度和分数历史存入 SQLite。</td>
</tr>
</table>

还缺什么？[提交一个资源](https://github.com/Li-Evan/awesome-jev/issues/new/choose)。
