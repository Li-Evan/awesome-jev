# 📊 数据与评测

[English](https://github.com/Li-Evan/awesome-jev/blob/main/scenarios/data.md) · **简体中文**

数据标注、大规模分类、数据管道、可观测性和 LLM 评测。共 135 条，按社区热度排序。

[← 返回 Awesome Jev](https://github.com/Li-Evan/awesome-jev/blob/main/README.zh-CN.md#按场景浏览)

<table>
<tr>
<td width="260" valign="top"><a href="https://github.com/realZachi/pg-jev"><img src="https://raw.githubusercontent.com/realZachi/pg-jev/master/docs/assets/header.svg" alt="pg-jev" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/realZachi/pg-jev">pg-jev</a></b><br><sub>realZachi · GitHub · ⭐ 290 · 2026-09-17</sub><br>支持 <code>WHERE jev(t, '...')</code> 查询的 PostgreSQL 扩展，每次请求批量处理 20 行，并报告批次变大时准确率如何下降。<br><sub>相关: <a href="https://pgjev.com">app</a> · <a href="https://pgjev.com">app 2</a> · <a href="https://x.com/iam_zachi/status/2100679300756435135">demo</a> · <a href="https://x.com/iam_zachi/status/2100700176444731780">demo 2</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/koala73/worldmonitor/blob/main/shared/jev-classify.js"><img src="https://repository-images.githubusercontent.com/1130564872/59ff0927-deb4-4941-8cbc-b68cbe060417" alt="World Monitor 的 Jev 标题分类器" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/koala73/worldmonitor/blob/main/shared/jev-classify.js">World Monitor 的 Jev 标题分类器</a></b><br><sub>koala73 · GitHub · ⭐ 87.2k 仓库 · 2026-01-08</sub><br>实时地缘政治新闻看板里的标题分类器：为每条标题向 jev-1.13.0 询问五级严重程度和 14 个主题类别之一，校验答案，失败时走回退。<br><sub>相关: <a href="https://worldmonitor.app">app</a> · <a href="https://github.com/koala73/worldmonitor">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/hamiltonulmer/status/2100370557405667768"><img src="https://pbs.twimg.com/media/HSYD5B1bsAAWqeg.jpg?name=orig" alt="DuckDB 的 Jev 扩展" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/hamiltonulmer/status/2100370557405667768">DuckDB 的 Jev 扩展</a></b><br><sub>hamiltonulmer · X · ♥ 1.5k · 2026-09-16</sub><br>DuckDB 扩展，可在 SQL 里用 Jev 给任意 CSV、Parquet 或 DuckDB 表的行分类，1k 行约需 10 秒。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/apache/airflow/blob/main/providers/common/ai/docs/classifier_models.rst"><img src="https://raw.githubusercontent.com/apache/airflow/main/airflow-core/docs/img/ui-dark/dags.png" alt="Airflow 的 LLM 分支" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/apache/airflow/blob/main/providers/common/ai/docs/classifier_models.rst">Airflow 的 LLM 分支</a></b><br><sub>apache · GitHub · ⭐ 46.9k 仓库 · 2015-04-13</sub><br>用一个 Jev Choice 挑选下一个任务，置信度低的情况交给人处理。<br><sub><b>Jev 用法:</b> 属于 common AI provider 的分类器模型部分；收录时已合并，尚未发布。</sub><br><sub>相关: <a href="https://github.com/apache/airflow/blob/main/providers/common/ai/src/airflow/providers/common/ai/example_dags/example_classifier_model.py">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/tarasshyn/status/2101012033340571952"><img src="https://pbs.twimg.com/amplify_video_thumb/2101011544515526656/img/iSFydnTHWxsRx9hy.jpg" alt="Flowsery 会话回放分拣" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/tarasshyn/status/2101012033340571952">Flowsery 会话回放分拣</a></b><br><sub>tarasshyn · X · ♥ 829 · 2026-09-18</sub><br>用 Jev 跑了 300 万条会话回放事件：40 秒内审阅 3,247 个会话，抓到 132 次愤怒点击、116 次无效点击和 95 个 JavaScript 错误，并开了 213 个修复 PR 草稿，花费 $2.17。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/MisbahSy/status/2100979972194369925"><img src="https://pbs.twimg.com/amplify_video_thumb/2100978985480167424/img/Qcx8F-7plQRcpzqg.jpg" alt="文档 OCR 路由器" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/MisbahSy/status/2100979972194369925">文档 OCR 路由器</a></b><br><sub>MisbahSy · X · ♥ 483 · 2026-09-18</sub><br>路由器：逐页查看 PDF，让 Jev 判断哪些页真正需要 OCR，其余页面在本地直接抽取，降低 OCR 成本和耗时。<br><sub><b>Jev 用法:</b> 每页一个 Choice：需要 OCR，还是直接抽取文本。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/different-ai/openwork/blob/dev/evals/packages/testkit/src/verification-jev.ts"><img src="https://github.com/user-attachments/assets/66a8dd9b-5260-488c-957d-e54331e78c1c" alt="OpenWork 的 Jev 验证" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/different-ai/openwork/blob/dev/evals/packages/testkit/src/verification-jev.ts">OpenWork 的 Jev 验证</a></b><br><sub>different-ai · GitHub · ⭐ 23.7k 仓库 · 2026-01-14</sub><br>OpenWork 桌面应用评测 testkit 中的评估器：通过 Vercel AI Gateway 把测试意图和一组 UI 检查项字典发给 Jev，由它在一次调用中选出要运行的检查项，并判断这些检查能否覆盖该意图。<br><sub><b>Jev 用法:</b> 一个表示是否覆盖的 Boolean，加上每个候选检查项各一个 Boolean；选中的检查项会编译成一份持久化的验证计划。</sub><br><sub>相关: <a href="https://github.com/different-ai/openwork">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/yyyole/status/2101184012899537092"><img src="https://pbs.twimg.com/amplify_video_thumb/2101182941317787648/img/1Imy25EAcuq8Wllx.jpg" alt="AI 新闻筛选" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/yyyole/status/2101184012899537092">AI 新闻筛选</a></b><br><sub>yyyole · X · ♥ 330 · 2026-09-19</sub><br>为挑选内容选题，用 Jev 把过去 7 天近 2,700 条 AI 新闻逐条筛了一遍，用时约 2 分钟，花费 $0.21。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/mrmps/classifier-dev"><img src="https://opengraph.githubassets.com/1/mrmps/classifier-dev" alt="classifier.dev" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/mrmps/classifier-dev">classifier.dev</a></b><br><sub>mrmps · GitHub · ⭐ 408 · 2026-08-13</sub><br>无需 API key 的零样本文本分类，可通过普通 HTTP、CLI 和 MCP 服务器调用，由 Jev 作答；smart 档位会在 Jev 置信度低于 0.7 时再问一次推理模型。<br><sub><b>Jev 用法:</b> 批处理把多条文本打包进一次请求；400 条新闻标题端到端分类只用了 650 毫秒。</sub><br><sub>相关: <a href="https://classifier.dev">app</a> · <a href="https://classifier.dev/">app 2</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/ramsoma/status/2101851201684042083"><img src="https://pbs.twimg.com/media/HStBFZFbIAAIWyp.jpg" alt="用 Jev 主动监控图表" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/ramsoma/status/2101851201684042083">用 Jev 主动监控图表</a></b><br><sub>ramsoma · 文章 · ♥ 48 · 2026-09-21</sub><br>分析实验：用 Jev 标出哪些图表值得深入分析；在一个合成基准测试上，它的成本约为最强的廉价托管基线的 1/3，速度快 5 倍，召回率排第一，但精确率垫底。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/sutro-sh/jev-align"><img src="https://external-preview.redd.it/LyUguT2COJHsL7br_6em8JB9WzRSm8btXeyyt8rmg9I.png?auto=webp&amp;s=ccd844160bd89dae768534357b88bc00db01afed" alt="jev-align" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/sutro-sh/jev-align">jev-align</a></b><br><sub>sutro-sh · GitHub · ⭐ 271 · 2026-09-19</sub><br>借助主动学习和提示词优化，把人工标注变成可复用、校准过的判断函数。<br><sub>相关: <a href="https://x.com/sethkimmel3/status/2101357768640987302">demo</a> · <a href="https://news.ycombinator.com/item?id=49770872">discussion</a> · <a href="https://pypi.org/project/jev-align/">pypi</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/jerryjliu/docjev"><img src="https://raw.githubusercontent.com/jerryjliu/docjev/main/docs/report/summary.png" alt="DocJev" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/jerryjliu/docjev">DocJev</a></b><br><sub>jerryjliu · GitHub · ⭐ 206 · 2026-09-19</sub><br>库、CLI 兼本地应用：基于 LiteParse 提取的文本和 Jev 的预测，按自然语言描述的类别规则给 PDF、DOCX 或 PPTX 文件分类，或把一份合订文件拆分成各个组成文档。<br><sub>相关: <a href="https://x.com/jerryjliu0/status/2101738281046294552">demo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/mmalisper/status/2101001041903009987"><img src="https://pbs.twimg.com/amplify_video_thumb/2100995303935791105/img/eK9B54C5duJ9b-Od.jpg" alt="Jev 查询规划器" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/mmalisper/status/2101001041903009987">Jev 查询规划器</a></b><br><sub>mmalisper · X · ♥ 164 · 2026-09-18</sub><br>用 Jev 搭的 Postgres 查询规划器，经过一些调优后，在 Join Order Benchmark 上把查询提速 12%。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/yongfook/status/2100801037192024478"><img src="https://pbs.twimg.com/amplify_video_thumb/2100800207256756224/img/qfKKxj1Oh8pHHnD7.jpg" alt="Bannerbear 字段映射" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/yongfook/status/2100801037192024478">Bannerbear 字段映射</a></b><br><sub>yongfook · X · ♥ 134 · 2026-09-18</sub><br>已上线的 Bannerbear 功能：一键把模板字段映射到名称不同的数据源字段（photo 对应 avatar，company_name 对应 business）。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/GreptimeTeam/greptimedb/blob/main/src/common/function/src/scalars/jev.rs"><img src="https://raw.githubusercontent.com/GreptimeTeam/greptimedb/main/docs/overview.png" alt="GreptimeDB 的 jev() SQL 函数" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/GreptimeTeam/greptimedb/blob/main/src/common/function/src/scalars/jev.rs">GreptimeDB 的 jev() SQL 函数</a></b><br><sub>GreptimeTeam · GitHub · ⭐ 6.7k 仓库 · 2022-04-11</sub><br>可观测性数据库 GreptimeDB 中的实验性 SQL 谓词 jev(text, statement, threshold)，按一句自然语言陈述是否成立来过滤日志行。<br><sub><b>Jev 用法:</b> 每个非空行变成一个 Noul 问题，再用其概率与阈值比较。</sub><br><sub>相关: <a href="https://greptime.com/product/db">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/hamiltonulmer/status/2102074494655627281"><img src="https://pbs.twimg.com/amplify_video_thumb/2102071614506713088/img/aed3GJoW29Fq1EG0.jpg" alt="MotherDuck prompt_jev()" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/hamiltonulmer/status/2102074494655627281">MotherDuck prompt_jev()</a></b><br><sub>hamiltonulmer · X · ♥ 127 · 2026-09-21</sub><br>一个 MotherDuck SQL 函数，在查询内部运行 Jev 文本分类，包括在 WHERE 子句中按语义过滤；据称速度是同类前沿模型的 50 倍，成本只有其 1%。<br><sub>相关: <a href="https://motherduck.com">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/lightdash/lightdash/tree/main/packages/backend/src/ee/services/ai/decisions"><img src="https://raw.githubusercontent.com/lightdash/lightdash/main/static/screenshots/platform-overview-readme.jpg" alt="Lightdash 的 AI 决策" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/lightdash/lightdash/tree/main/packages/backend/src/ee/services/ai/decisions">Lightdash 的 AI 决策</a></b><br><sub>lightdash · GitHub · ⭐ 6.2k 仓库 · 2021-03-19</sub><br>嵌在 Lightdash BI agent 里的类型化 Jev 决策，用于目录排序、日期范围检查、图表质量、错误分类、回答论断的证据核查和字段恢复。<br><sub><b>Jev 用法:</b> 一个共享的决策客户端负责校验 Noul、Choice 和 Score 答案；其他调用方用它做项目路由、模型路由和就绪度评分。</sub><br><sub>相关: <a href="https://lightdash.com">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/harbor-framework/harbor/blob/main/docs/content/docs/rewardkit/judge-criteria.mdx"><img src="https://opengraph.githubassets.com/1/harbor-framework/harbor" alt="Harbor rewardkit 的 Jev 评委" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/harbor-framework/harbor/blob/main/docs/content/docs/rewardkit/judge-criteria.mdx">Harbor rewardkit 的 Jev 评委</a></b><br><sub>harbor-framework · 文档 · ⭐ 5.5k 仓库 · 2025-08-04</sub><br>rewardkit 中的 Jev 评委选项（rewardkit 是 Terminal-Bench 团队 Harbor 评测框架的评分包），按二元标准和评分细则给 agent 输出打分，不产出推理文本。<br><sub><b>Jev 用法:</b> 在标准 TOML 里设置 judge = "jev"；每条标准返回一个概率或评分细则分数，评分又快又便宜。</sub><br><sub>相关: <a href="https://harborframework.com/">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/langwatch/langwatch/tree/main/platform/app/src/server/app-layer/instant-evals/classifier"><img src="https://opengraph.githubassets.com/1/langwatch/langwatch" alt="基于 Jev 的 LangWatch Instant Evals" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/langwatch/langwatch/tree/main/platform/app/src/server/app-layer/instant-evals/classifier">基于 Jev 的 LangWatch Instant Evals</a></b><br><sub>langwatch · GitHub · ⭐ 4.9k 仓库 · 2023-09-09</sub><br>在 LangWatch 的 Instant Evals 分类器里，Jev 负责在追踪到的文本上运行布尔、分数和类别评估器：每段文本一次请求并携带全部问题，每次调用约 250 毫秒。<br><sub><b>Jev 用法:</b> 分数取各等级的概率加权平均；Retry-After 和 state 超限错误按实际观察到的 API 行为处理。</sub><br><sub>相关: <a href="https://langwatch.ai">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/latitude-dev/latitude-llm/tree/development/packages/platform/ai-jev"><img src="https://raw.githubusercontent.com/latitude-dev/latitude-llm/development/docs/assets/readme/readme-banner.png" alt="Latitude 的 Jev 预分类器" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/latitude-dev/latitude-llm/tree/development/packages/platform/ai-jev">Latitude 的 Jev 预分类器</a></b><br><sub>latitude-dev · GitHub · ⭐ 4.7k 仓库 · 2026-09-17</sub><br>AI agent 可观测性平台 Latitude 中的可选 Jev 预分类器，判断一个会话适用哪些对话检查（flagger），并记录模型、阈值、延迟和选择结果。<br><sub><b>Jev 用法:</b> 作为影子决策 provider 与 LLM 筛查路径并行运行，受阈值和速率限制约束。</sub><br><sub>相关: <a href="https://github.com/latitude-dev/latitude-llm">repo</a> · <a href="https://latitude.so">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/huangyun_122/status/2102112025627476146"><img src="https://pbs.twimg.com/amplify_video_thumb/2102111165195382784/img/mUh4ZV1uJMw-RMYM.jpg" alt="公众号文章分类器" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/huangyun_122/status/2102112025627476146">公众号文章分类器</a></b><br><sub>huangyun_122 · X · ♥ 84 · 2026-09-21</sub><br>一个中文演示：抓取 148 篇微信公众号长文，让 Jev 在不到 2 分钟内按场景分类，作为一次低成本标注尝试。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/dagucloud/dagu/blob/main/specs/071-decision-evaluate.md"><img src="https://opengraph.githubassets.com/1/dagucloud/dagu" alt="Dagu decision.evaluate" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/dagucloud/dagu/blob/main/specs/071-decision-evaluate.md">Dagu decision.evaluate</a></b><br><sub>dagucloud · GitHub · ⭐ 4.1k 仓库 · 2022-04-22</sub><br>内置于 Dagu 工作流的 decision.evaluate 动作：就共享上下文向 Jev 提 choice、score 或是非问题，并根据类型化答案给 DAG 选路。<br><sub><b>Jev 用法:</b> 可对接 TypeSafe 的 /v1/systemone 或 OpenRouter 的 Decisions API，答案记录为步骤输出。</sub><br><sub>相关: <a href="https://github.com/dagucloud/dagu/tree/main/internal/runtime/builtin/decision">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/giuliosmall/pg_typesafe"><img src="https://opengraph.githubassets.com/1/giuliosmall/pg_typesafe" alt="pg_typesafe" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/giuliosmall/pg_typesafe">pg_typesafe</a></b><br><sub>giuliosmall · GitHub · ⭐ 81 · 2026-09-17</sub><br>pre-alpha 阶段的 PostgreSQL C 扩展，从 SQL 调用 Jev，返回 Choice、Noul 和 Score 答案，在查询内部完成分类和打分。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/NanmiCoder/jev-arena"><img src="https://raw.githubusercontent.com/NanmiCoder/jev-arena/main/assets/readme/hero-3d.png" alt="Jev Arena" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/NanmiCoder/jev-arena">Jev Arena</a></b><br><sub>NanmiCoder · GitHub · ⭐ 79 · 2026-09-19</sub><br>并排对比的竞技场，用 Jev 和 DeepSeek 或其他聊天模型给同一批评论打标签；在 10,000 条评论上，Jev 用时 203.2 s、花费 $0.84，对手为 823.5 s 和 $1.50，但 Jev 的准确率略低。<br><sub>相关: <a href="https://nanmicoder.github.io/jev-arena/">site</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/escapeboy/agent-fleet-o"><img src="https://raw.githubusercontent.com/escapeboy/agent-fleet-o/main/screenshots/qa-dashboard.png" alt="FleetQ 决策模型评测 harness" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/escapeboy/agent-fleet-o">FleetQ 决策模型评测 harness</a></b><br><sub>escapeboy · GitHub · ⭐ 70 · 2026-02-08</sub><br>自托管的 agent 编排平台，带 System One 决策驱动和一个 jev:eval harness，可在 JSONL 数据集上从准确率、校准、覆盖率、延迟、成本和确定性几个方面给 Jev 或 LLM 打分。<br><sub>相关: <a href="https://fleetq.net">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/ianarawjo/chainforge/blob/main/chainforge/react-server/src/backend/models.ts"><img src="https://github.com/ianarawjo/ChainForge/assets/5251713/570879ef-ef8a-4e00-b37c-b49bc3c1a370" alt="ChainForge 的 Jev 评委" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/ianarawjo/chainforge/blob/main/chainforge/react-server/src/backend/models.ts">ChainForge 的 Jev 评委</a></b><br><sub>ianarawjo · GitHub · ⭐ 3k 仓库 · 2023-03-26</sub><br>提示词评测环境 ChainForge 把 Jev 加为决策评委，与文本评委分开调用，并根据它给出的概率与标签的对照生成可靠性表。<br><sub><b>Jev 用法:</b> Jev 这类决策模型返回校准的概率，用于按评委展示的可靠性视图。</sub><br><sub>相关: <a href="https://chainforge.ai/docs">docs</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/openlayer-ai/jevals"><img src="https://external-preview.redd.it/QQHJgNvAmxL8Jd0CPbw1hzeEW1AIIeVd7V1E2H6Veoo.png?auto=webp&amp;s=fadb40963b005ee61ab72d453710ef95869182af" alt="jevals" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/openlayer-ai/jevals">jevals</a></b><br><sub>openlayer-ai · GitHub · ⭐ 51 · 2026-09-20</sub><br>与框架无关的 agent 评测和护栏：把一条 trace 的所有检查一次性发给 Jev，快到可以放进 agent 循环里；也可在本地用 Kev 或 Laya，或回退到聊天模型。<br><sub>相关: <a href="https://news.ycombinator.com/item?id=49780849">demo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/YEDASAVG/Stratum"><img src="https://opengraph.githubassets.com/1/YEDASAVG/Stratum" alt="Stratum" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/YEDASAVG/Stratum">Stratum</a></b><br><sub>YEDASAVG · GitHub · ⭐ 51 · 2026-02-03</sub><br>日志智能分析系统，支持语义搜索、异常检测和根因分析；可选的 Jev 步骤会给每条查询的意图、所属服务和严重程度分类，并附置信度。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/RenaGao/jev-dataops"><img src="https://opengraph.githubassets.com/1/RenaGao/jev-dataops" alt="JEV DataOps" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/RenaGao/jev-dataops">JEV DataOps</a></b><br><sub>RenaGao · GitHub · ⭐ 37 · 2026-09-21</sub><br>工作台：用 Jev 筛查上传的训练数据、评估数据质量，自动训练 LoRA 并在留出数据上评估结果，可通过浏览器应用、CLI 以及 Python 和 HTTP API 使用。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/MapleTechLabs/maple/blob/main/apps/ai/src/triage/incident-classifier.ts"><img src="https://opengraph.githubassets.com/1/MapleTechLabs/maple" alt="Maple 事故分拣" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/MapleTechLabs/maple/blob/main/apps/ai/src/triage/incident-classifier.ts">Maple 事故分拣</a></b><br><sub>MapleTechLabs · GitHub · ⭐ 1.8k 仓库 · 2026-02-15</sub><br>OpenTelemetry 可观测性平台 Maple 里的 LLM 前置事故分拣：由一个 Jev 决策把关，判断某个事故是否值得动用完整的模型调查。<br><sub><b>Jev 用法:</b> 在一次不带工具的调用里问一组有边界的问题，其中包括从 low 到 critical 的严重程度评分，并刻意放在 agent 回合之外。</sub><br><sub>相关: <a href="https://maple.dev">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/smkrv/jev-calibrate"><img src="https://opengraph.githubassets.com/1/smkrv/jev-calibrate" alt="jev-calibrate" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/smkrv/jev-calibrate">jev-calibrate</a></b><br><sub>smkrv · GitHub · ⭐ 31 · 2026-09-21</sub><br>CLI 工具：用你的标注样例调优 Jev 问题的判定标准，在留出集上确认效果，并告诉你每个问题能单独把关决策、只能用于排序，还是没有可用信号。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/KryptSec/oasis"><img src="https://opengraph.githubassets.com/1/KryptSec/oasis" alt="OASIS" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/KryptSec/oasis">OASIS</a></b><br><sub>KryptSec · GitHub · ⭐ 29 · 2025-12-22</sub><br>开源 CLI，在带 MITRE ATT&amp;CK 映射的进攻性安全 CTF 题目上给 AI 模型做基准测试；可选的 TypeSafe 评委会在运行结束后重新判定每一步是否成功，取代默认的子串正则。<br><sub><b>Jev 用法:</b> 运行结束后，每一步用固定版本 jev-1.13.0 做一次判断并记录 successConfidence；评委调用失败时保留正则的结论。</sub><br><sub>相关: <a href="https://oasis.kryptsec.com">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/misbahsy/doc-router"><img src="https://opengraph.githubassets.com/1/misbahsy/doc-router" alt="doc-router" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/misbahsy/doc-router">doc-router</a></b><br><sub>misbahsy · GitHub · ⭐ 26 · 2026-09-18</sub><br>带 Python 绑定的 Rust 库和 CLI，用 Jev 作为页面评判，逐页决定哪些 PDF 页需要 OCR；在 155 页上只对 87 页计费，比全部 OCR 便宜 1.74 倍。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/hijohnnylin/neuronpedia/blob/main/apps/webapp/lib/external/autointerp-scorer-jev.ts"><img src="https://repository-images.githubusercontent.com/656892015/8d29d9f6-1ac8-4320-9800-bef44bf1d174" alt="Neuronpedia 的 Jev 自动可解释性评分器" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/hijohnnylin/neuronpedia/blob/main/apps/webapp/lib/external/autointerp-scorer-jev.ts">Neuronpedia 的 Jev 自动可解释性评分器</a></b><br><sub>hijohnnylin · GitHub · ⭐ 1.1k 仓库 · 2023-06-21</sub><br>开放可解释性平台 Neuronpedia 用 Jev 通过检测、模糊测试和 5 级评分给神经元解释的质量打分，每条解释一次请求。<br><sub><b>Jev 用法:</b> jev_detection 和 jev_fuzz 对每个样例问一个是非题，用来计算平衡准确率；jev_score 使用概率加权的 5 级评分。</sub><br><sub>相关: <a href="https://neuronpedia.org">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/goodrahstar/jev-column-race"><img src="https://raw.githubusercontent.com/goodrahstar/jev-column-race/main/docs/banner.svg" alt="Jev Column Race" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/goodrahstar/jev-column-race">Jev Column Race</a></b><br><sub>goodrahstar · GitHub · ⭐ 22 · 2026-09-17</sub><br>实时比赛，给 1,000 条应用评论标注四列：Jev 用 4.6 秒、$0.023 完成，Gemini 3.8 Flash 用了 18.8 秒、$0.158，两者与星级评分的一致性相近。<br><sub>相关: <a href="https://x.com/rahulbuildsmore/status/2100581721515188451">demo</a> · <a href="https://jev-column-race.vercel.app">app</a> · <a href="https://jev-column-race.vercel.app">app 2</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/colliber/duckdb-jev"><img src="https://raw.githubusercontent.com/colliber/duckdb-jev/main/docs/demo.gif" alt="duckdb-jev" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/colliber/duckdb-jev">duckdb-jev</a></b><br><sub>colliber · GitHub · ⭐ 20 · 2026-09-17</sub><br>DuckDB 扩展，在 SQL 里就每一行向 Jev 提问，并把答案作为真正的 SQL 类型返回，比如 ENUM、数值或 STRUCT。<br><sub><b>Jev 用法:</b> 针对每行文本提 Choice、Score 和 Noul 问题，映射为带类型的列。</sub><br><sub>相关: <a href="https://news.ycombinator.com/item?id=49774406">demo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Trampoline-AI/avalanche"><img src="https://raw.githubusercontent.com/Trampoline-AI/avalanche/main/docs/assets/brand/avalanche-logo-3d.png" alt="Avalanche 分类器步骤" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Trampoline-AI/avalanche">Avalanche 分类器步骤</a></b><br><sub>Trampoline-AI · GitHub · ⭐ 19 · 2026-06-30</sub><br>agent 化的 ETL 框架，在同一个 DAG 里混合确定性 Python 步骤和 agent 步骤；由 TypeSafe 支撑的 @ava.classifier_step 节点回答 Choice、Noul 和 Score 问题，并可在运维界面中查看。<br><sub>相关: <a href="https://github.com/Trampoline-AI/avalanche/blob/main/examples/classifier_workflow.py">example</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/AkashPriyadarshii/jev-curate"><img src="https://opengraph.githubassets.com/1/AkashPriyadarshii/jev-curate" alt="jev-curate" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/AkashPriyadarshii/jev-curate">jev-curate</a></b><br><sub>AkashPriyadarshii · GitHub · ⭐ 19 · 2026-09-18</sub><br>Rust 流式 CLI 和 Python API，用本地预过滤器加类型化的 Jev Choice、Score 和 Noul 判断来过滤 Parquet 或 JSONL 格式的合成数据集与预训练数据集，按阈值决定每条记录保留还是剔除。<br><sub>相关: <a href="https://jev-curate.vercel.app">app</a> · <a href="https://crates.io/crates/jev-curate">crate</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/abhixhek/jevcal"><img src="https://raw.githubusercontent.com/abhixhek/jevcal/main/docs/terminal.png" alt="jevcal" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/abhixhek/jevcal">jevcal</a></b><br><sub>abhixhek · GitHub · ⭐ 10 · 2026-09-18</sub><br>工具包：在你自己的标注数据上，把 Jev 这类类型化决策模型与 LLM 教师模型对比测量，为目标准确率选定置信度阈值，报告还有多少流量需要 LLM，并在出现漂移时让 CI 失败。<br><sub>相关: <a href="https://x.com/thenightshipper/status/2100850610962919551">demo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/the_cyw/status/2100807905859739779"><img src="https://pbs.twimg.com/amplify_video_thumb/2100807113576693760/img/8lI0CmDrKghq79Z5.jpg" alt="物理 AI 动作标签质检" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/the_cyw/status/2100807905859739779">物理 AI 动作标签质检</a></b><br><sub>the_cyw · X · ♥ 18 · 2026-09-18</sub><br>对物理 AI 的第一人称视角训练数据做质量检查：Jev 不到 3 分钟质检了 58,643 个动作标签，花费 90 美分。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/keltokhy/jsort"><img src="https://opengraph.githubassets.com/1/keltokhy/jsort" alt="jsort" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/keltokhy/jsort">jsort</a></b><br><sub>keltokhy · GitHub · ⭐ 17 · 2026-09-19</sub><br>按语义排序的命令行工具：每次给 Jev 看两段文本，问在某个用平实英文描述的维度上哪个排更高，再拟合 Bradley-Terry 量表，输出带分数和标准误的行或文档。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/rlaope/jeval"><img src="https://raw.githubusercontent.com/rlaope/jeval/main/docs/report-verdict.png" alt="jeval" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/rlaope/jeval">jeval</a></b><br><sub>rlaope · GitHub · ⭐ 15 · 2026-09-20</sub><br>Python CLI：在标注数据上衡量分类器（包括 Jev）的置信度与准确率吻合得如何，并设定成本最优的转人工阈值，输出离线 HTML 报告和 YAML 配置。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/dayhaysoos/jevals"><img src="https://pbs.twimg.com/amplify_video_thumb/2100965288850145280/img/Ik0MohKW-MEyT6p4.jpg" alt="jevals" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/dayhaysoos/jevals">jevals</a></b><br><sub>dayhaysoos · GitHub · ⭐ 1 · 2026-09-18</sub><br>本地浏览器工作台，用来编写带示例用例和预期答案的 Jev Noul、Choice 和 Score 问题，运行它们并对比已保存的结果。<br><sub>相关: <a href="https://x.com/Dayhaysoos/status/2100968892591968320">demo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/leonardovida/duckdb-ai"><img src="https://raw.githubusercontent.com/leonardovida/duckdb-ai/main/docs/assets/duckdb-ai-logo.svg" alt="duckdb-ai" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/leonardovida/duckdb-ai">duckdb-ai</a></b><br><sub>leonardovida · GitHub · ⭐ 12 · 2026-07-01</sub><br>DuckDB 扩展，可在 SQL 里调用 LLM 做摘要、分类、抽取和 embedding，并提供 TypeSafe Jev provider，原生支持选择、打分和是非概率。<br><sub><b>Jev 用法:</b> 一次 SQL 调用可在单个请求中评估多个类型化问题；有一份 cookbook 专门讲多问题评估。</sub><br><sub>相关: <a href="https://leonardovida.github.io/duckdb-ai/">app</a> · <a href="https://github.com/leonardovida/duckdb-ai/blob/main/docs/cookbooks/jev-decisions.md">docs</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/ktaletsk/jevframe"><img src="https://raw.githubusercontent.com/ktaletsk/jevframe/main/assets/jevframe/preview.png" alt="jevframe" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/ktaletsk/jevframe">jevframe</a></b><br><sub>ktaletsk · GitHub · ⭐ 12 · 2026-09-18</sub><br>面向 pandas 和 Polars 的 Python 库，用自然语言问题给 DataFrame 的行打标签、打分和分类，以普通 Series 返回完整概率分布，并限制异步并发数。<br><sub><b>Jev 用法:</b> 每行的多个问题放在一次请求里，可选缓存；附带一个拆解真实请求的 marimo notebook。</sub><br><sub>相关: <a href="https://x.com/marimo_io/status/2102110394718486863">demo</a> · <a href="https://pypi.org/project/jevframe/">pypi</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/collapseindex/jev-ultralightspeed"><img src="https://raw.githubusercontent.com/collapseindex/jev-ultralightspeed/main/docs/infographic.png" alt="jev-ultralightspeed" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/collapseindex/jev-ultralightspeed">jev-ultralightspeed</a></b><br><sub>collapseindex · GitHub · ⭐ 11 · 2026-09-20</sub><br>批量分类器，把 32 条数据打包进一次 Jev 请求，并校准置信度切分点，把最没把握的行交给人工；一百万条短消息耗时半小时，花费 $4.99。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/kylemclaren/jevql"><img src="https://opengraph.githubassets.com/1/kylemclaren/jevql" alt="jevQL" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/kylemclaren/jevql">jevQL</a></b><br><sub>kylemclaren · GitHub · ⭐ 11 · 2026-09-18</sub><br>给原生 Postgres 用的语义 SQL：一个 psql 风格的 CLI 加 Go、TypeScript 和 Python SDK，可在查询中加入 jev() 条件，先在服务器上执行普通 SQL，再用 Jev 分批评判留下来的行。<br><sub>相关: <a href="https://jevql.fly.dev/">app</a> · <a href="https://jevql.fly.dev">app 2</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/opencx-labs/zevals"><img src="https://raw.githubusercontent.com/opencx-labs/zevals/main/static/zevals-logo-wide.png" alt="zevals 的 Jev 评委" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/opencx-labs/zevals">zevals 的 Jev 评委</a></b><br><sub>opencx-labs · GitHub · ⭐ 11 · 2025-05-06</sub><br>用于端到端 AI agent 测试的 TypeScript 库，断言可以用 Jev 当评委，每条断言报告一个校准的概率，每次调用约 0.5 s、$0.00005。<br><sub><b>Jev 用法:</b> 针对对话记录问一个 Noul，设通过阈值（默认 0.5）；结果与阈值相差不到 0.05 的标记为临界。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/reachjalil/jevlogs"><img src="https://raw.githubusercontent.com/reachjalil/jevlogs/main/docs/assets/readme-banner.png" alt="Jev Logs" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/reachjalil/jevlogs">Jev Logs</a></b><br><sub>reachjalil · GitHub · ⭐ 9 · 2026-09-17</sub><br>TypeScript 库兼 OpenTelemetry exporter 封装，在进行昂贵的 LLM 分析之前，先用 Jev 给每条日志记录的诊断价值、优先级和路由打分，所有记录都保留在归档中。<br><sub><b>Jev 用法:</b> 每条记录一个 0-100 的诊断价值 Score、一个优先级和一个需处理概率。</sub><br><sub>相关: <a href="https://www.reddit.com/r/SideProject/comments/1wil0gi/made_an_open_source_library_for_working_on_logs/">discussion</a> · <a href="https://huggingface.co/datasets/reachjalil/jevlogs-log-triage-benchmark">model</a> · <a href="https://huggingface.co/datasets/reachjalil/jev-luna-pagerduty-trigger">model 2</a> · <a href="https://huggingface.co/spaces/reachjalil/jevlogs-triage-explorer">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/sunil-sadasivan/jevernetes"><img src="https://raw.githubusercontent.com/sunil-sadasivan/jevernetes/main/docs/images/live-demo.gif" alt="jevernetes" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/sunil-sadasivan/jevernetes">jevernetes</a></b><br><sub>sunil-sadasivan · GitHub · ⭐ 9 · 2026-09-20</sub><br>在终端或本地看板里实时分析 Kubernetes 日志：通过提问找出匹配的日志、查看上下文，并把选中的证据交给编程 agent。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/cristianoliveira/jeq"><img src="https://raw.githubusercontent.com/cristianoliveira/jeq/main/docs/assets/jeq-logo-mono.svg" alt="jeq" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/cristianoliveira/jeq">jeq</a></b><br><sub>cristianoliveira · GitHub · ⭐ 8 · 2026-09-19</sub><br>仿 jq 思路的 Go CLI，让脚本和 agent 把 JSON 和 NDJSON 通过管道送进类型化的 Jev 问题，组合 map、reduce、rank 和 rate 步骤，并带有显式的离线策略闸门。<br><sub>相关: <a href="https://www.reddit.com/r/typesafe_ai/comments/1wlejae/jeq_what_happens_when_jev_meets_jq_intelligence/">discussion</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/kunko-ai-labs/judge-audit"><img src="https://raw.githubusercontent.com/kunko-ai-labs/judge-audit/main/docs/assets/hero-arena.png" alt="judge-audit" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/kunko-ai-labs/judge-audit">judge-audit</a></b><br><sub>kunko-ai-labs · GitHub · ⭐ 8 · 2026-09-18</sub><br>以影子模式对照过往人工决策，审计 AI 评委的校准情况；已发布的 Jev 审计报告显示，受攻击时准确率 95.5%，零错误覆盖率 73%，而 Claude Sonnet 4.5 只有 2%。<br><sub><b>Jev 用法:</b> 通过 Vercel AI Gateway 在邮件分拣、对抗性邮件和廉价/前沿模型任务路由器上运行 Jev，并把原始响应提交到仓库以便重新计算。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/theyashwanthsai/jevals"><img src="https://opengraph.githubassets.com/1/theyashwanthsai/jevals" alt="Jevals" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/theyashwanthsai/jevals">Jevals</a></b><br><sub>theyashwanthsai · GitHub · ⭐ 7 · 2026-09-18</sub><br>研究预览版评测框架，按代码写成的规则给 LLM 和 agent 的输出（包括完整 trace）打分，借助 Jev 让每个结论都带置信度；32 个答案约 $0.0002。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/collapseindex/dinostomp"><img src="https://raw.githubusercontent.com/collapseindex/dinostomp/main/data/exports/readme/20260915_120000_readme_pixel-dino_1200x360_s42.gif" alt="dinostomp" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/collapseindex/dinostomp">dinostomp</a></b><br><sub>collapseindex · GitHub · ⭐ 6 · 2026-08-09</sub><br>本地优先的 AI 评测核验层，审计数据集、评分器、运行记录和结论；对 Jev 用户来说，它像测试 if 语句一样测试一个问题，报告准确率、p(yes) 截断值和校准情况。<br><sub>相关: <a href="https://collapseindex.org/">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/koladev32/status/2101660768458391816"><img src="https://pbs.twimg.com/amplify_video_thumb/2101653831247388672/img/ym11-1ZkJv7EL_ZP.jpg" alt="jev-classify" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/koladev32/status/2101660768458391816">jev-classify</a></b><br><sub>koladev32 · X · ♥ 6 · 2026-09-20</sub><br>文档分类与路由流水线：不到 4 分钟用 Jev 处理 39,700 份文档，花费 $1.43，准确率 96.38%，总吞吐约 180 份/秒，p95 延迟 485 毫秒。<br><sub>相关: <a href="https://github.com/koladev32/jev-classify">repo</a> · <a href="https://github.com/koladev32/jev-classify">project</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/TrustifAI/typed_evals"><img src="https://external-preview.redd.it/24DpejsFjNHwV30AJ5IBmdofmgxNJlw0Mpz2QMkwpew.png?auto=webp&amp;s=3d0cfd96b6591ae30a6ec0aa2512309594e094cb" alt="typed_evals" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/TrustifAI/typed_evals">typed_evals</a></b><br><sub>TrustifAI · GitHub · ⭐ 6 · 2026-09-20</sub><br>Python 库兼 CLI，以 Jev 为评委评估 LLM 回复、RAG 数据集和录制的 agent 运行，在工具执行前加一道防护，还能对照人工的通过/失败标注校准指标。<br><sub>相关: <a href="https://www.reddit.com/r/LLMDevs/comments/1wlmeh6/opensource_typed_evals_ai_evaluation_powered_by/">discussion</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/zenml-io/kitaru/tree/develop/plugins/packages/typesafe-evaluator"><img src="https://raw.githubusercontent.com/zenml-io/kitaru/develop/assets/kitaru_header.png" alt="Kitaru 的 TypeSafe 评估器" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/zenml-io/kitaru/tree/develop/plugins/packages/typesafe-evaluator">Kitaru 的 TypeSafe 评估器</a></b><br><sub>zenml-io · GitHub · ⭐ 292 仓库 · 2026-03-05</sub><br>基于回放的 agent 评测平台的可选评估器包：用 Jev 评判录制下来的会话，每个会话发一次请求，每个问题存一条结果。<br><sub>相关: <a href="https://kitaru.ai">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/opaielsheikh/ai-elo-ranker"><img src="https://opengraph.githubassets.com/1/opaielsheikh/ai-elo-ranker" alt="AI Elo Ranker" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/opaielsheikh/ai-elo-ranker">AI Elo Ranker</a></b><br><sub>opaielsheikh · GitHub · ⭐ 5 · 2026-09-17</sub><br>锦标赛引擎：通过 Jev 两两对比判断、瑞士制配对和 Elo 评分，给诗歌、路演稿、冷邮件、广告开头钩子等文本排名，结果实时推送到 WebSocket 看板。<br><sub><b>Jev 用法:</b> 每场比赛做一次两两对比判断，展示顺序随机化以抵消位置偏差。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/AntonG87/codearia-sieve"><img src="https://raw.githubusercontent.com/AntonG87/codearia-sieve/main/docs/banners/01-hero.webp" alt="codearia-sieve" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/AntonG87/codearia-sieve">codearia-sieve</a></b><br><sub>AntonG87 · GitHub · ⭐ 5 · 2026-09-20</sub><br>MCP 服务器兼 TypeScript 库，把网页解析成 Jev 这类决策模型需要的 state：日期就是日期，数字带单位，分块大小刚好合适；测试中，抽取出的 11 条事实 Jev 核实了 11 条。<br><sub>相关: <a href="https://github.com/jkudish/jev-mcp">related</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/maayanlevy/mysql-ailike"><img src="https://raw.githubusercontent.com/maayanlevy/mysql-ailike/main/docs/screenshots/asia.png" alt="AILIKE for MySQL" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/maayanlevy/mysql-ailike">AILIKE for MySQL</a></b><br><sub>maayanlevy · GitHub · ⭐ 4 · 2026-09-19</sub><br>原生 MySQL 插件，新增 AILIKE 运算符和 ailike() 函数，可以用自然语言条件过滤行、比较文本列，每个条件都由 Jev 判断。<br><sub>相关: <a href="https://news.ycombinator.com/item?id=49774592">discussion</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/jkrup/jeveryword"><img src="https://raw.githubusercontent.com/jkrup/jeveryword/main/docs/hero-light.svg" alt="jeveryword" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/jkrup/jeveryword">jeveryword</a></b><br><sub>jkrup · GitHub · ⭐ 4 · 2026-09-19</sub><br>零依赖的 JavaScript 库，用于字段抽取、PII 检测和精确引用：给文本中的每个词编号，让 Jev 来挑选，返回带偏移量和概率的原始子串。<br><sub><b>Jev 用法:</b> 在编号后的词位置上做 Choice，再映射回字符偏移量。</sub><br><sub>相关: <a href="https://jeveryword.vercel.app">app</a> · <a href="https://jeveryword.vercel.app">app 2</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/keltokhy/jlink"><img src="https://opengraph.githubassets.com/1/keltokhy/jlink" alt="jlink" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/keltokhy/jlink">jlink</a></b><br><sub>keltokhy · GitHub · ⭐ 4 · 2026-09-18</sub><br>面向应用经济学研究者的记录链接工具，提供 Python、CLI、Stata 和 R 版本：用平实的英文写匹配规则，Jev 为每个候选对返回一个概率；在其基准测试中，146,119 对花费 $2.49。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/NiceEval/NiceEval/blob/main/packages/niceeval/src/judge/provider.ts"><img src="https://opengraph.githubassets.com/1/NiceEval/NiceEval" alt="NiceEval 的 TypeSafe 评委" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/NiceEval/NiceEval/blob/main/packages/niceeval/src/judge/provider.ts">NiceEval 的 TypeSafe 评委</a></b><br><sub>NiceEval · GitHub · ⭐ 153 仓库 · 2026-06-28</sub><br>本地优先的 agent 评测工具，把 TypeSafe 加为显式的评委 provider，将 Jev 的概率映射为加权分数和批量分类结果。<br><sub>相关: <a href="https://github.com/NiceEval/NiceEval/blob/main/docs/feature/judge/README.md">docs</a> · <a href="https://www.niceeval.com/">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/smithclay/dbt_jev"><img src="https://raw.githubusercontent.com/smithclay/dbt_jev/main/demos/dbt_jev_x_demo.gif" alt="dbt_jev" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/smithclay/dbt_jev">dbt_jev</a></b><br><sub>smithclay · GitHub · ⭐ 3 · 2026-09-20</sub><br>一个 dbt 包，其宏可在 DuckDB 和 ClickHouse 上从 SQL 调用 Jev：Choice 暴露为可为空的标签，Noul 暴露为候选对的匹配概率，Score 暴露为按评分标准给出的数值评分。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/prasanthj/duckdb-jev"><img src="https://raw.githubusercontent.com/prasanthj/duckdb-jev/main/docs/images/terminal-demo.gif" alt="Jev for DuckDB" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/prasanthj/duckdb-jev">Jev for DuckDB</a></b><br><sub>prasanthj · GitHub · ⭐ 3 · 2026-09-20</sub><br>原生 C++ DuckDB 扩展，在 SQL 行上支持 Jev 谓词、Choice 分类和 Score 评分细则；每次请求最多打包 1,000 个判断，跨分块流式处理，并支持按查询设预算和缓存。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/teempai/jev-in-codex"><img src="https://opengraph.githubassets.com/1/teempai/jev-in-codex" alt="Jev in Codex" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/teempai/jev-in-codex">Jev in Codex</a></b><br><sub>teempai · GitHub · ⭐ 3 · 2026-09-19</sub><br>用于批量标注的 Codex 插件，按自定义的问题和标准策略，把一个文本记录 JSONL 文件变成完整标注好的文件，拿不准的决策交给 Codex 复核。<br><sub><b>Jev 用法:</b> 只有一个 jev_label 工具，为每条记录分配一个标签；早期的工具选择和分拣工具在测试显示没有实际收益后被移除。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/stas4000/jev-papers"><img src="https://raw.githubusercontent.com/stas4000/jev-papers/main/docs/preview.png" alt="Jev Papers" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/stas4000/jev-papers">Jev Papers</a></b><br><sub>stas4000 · GitHub · ⭐ 3 · 2026-09-21</sub><br>用每篇一次 Jev 决策把 1,000 篇近期 arXiv AI 论文分到 24 个主题，抽样 100 篇与 Claude Opus 5 的结果对照，并生成可搜索的主题地图。<br><sub><b>Jev 用法:</b> 每篇论文一个 24 选 1 的 Choice：总计 $0.0585，延迟中位数 56.9 毫秒；而用 LLM 评委处理 100 篇就要 $0.8940。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/joshLong145/jev-cli"><img src="https://opengraph.githubassets.com/1/joshLong145/jev-cli" alt="jev-cli" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/joshLong145/jev-cli">jev-cli</a></b><br><sub>joshLong145 · GitHub · ⭐ 3 · 2026-09-21</sub><br>命令行工具，在 JSON、NDJSON 和 JSONC 产物上运行日志分拣、安全审计等问题包，返回锚定到行的类型化答案，可直接用来做卡点。<br><sub><b>Jev 用法:</b> 每个记录窗口把所有选中问题包的问题合并成一次调用；任何数据离开进程之前都会先过滤并脱敏密钥。</sub><br><sub>相关: <a href="https://news.ycombinator.com/item?id=49786725">demo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/ishantanu/jevmetrics"><img src="https://raw.githubusercontent.com/ishantanu/jevmetrics/main/docs/assets/jevmetrics.png" alt="jevmetrics" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/ishantanu/jevmetrics">jevmetrics</a></b><br><sub>ishantanu · GitHub · ⭐ 3 · 2026-09-19</sub><br>实验性的 OpenTelemetry Collector 指标处理器，根据指标 instrument 的元数据推断其运维价值，在送达后端之前对其做标注或过滤。<br><sub><b>Jev 用法:</b> 每个 instrument 得到一个概率，经缓存后通过确定性策略应用，推理异步进行。</sub><br><sub>相关: <a href="https://news.ycombinator.com/item?id=49769491">demo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/EugeneBoondock/jevsql"><img src="https://raw.githubusercontent.com/EugeneBoondock/jevsql/main/jevsql.png" alt="JevSQL" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/EugeneBoondock/jevsql">JevSQL</a></b><br><sub>EugeneBoondock · GitHub · ⭐ 3 · 2026-09-18</sub><br>Node 库兼 CLI，为 SQLite 加入自然语言谓词，让查询按语义过滤、排序、分类和打分，支持批处理、缓存、成本防护和复核队列。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/mgaitan/sqlite-jev"><img src="https://opengraph.githubassets.com/1/mgaitan/sqlite-jev" alt="sqlite-jev" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/mgaitan/sqlite-jev">sqlite-jev</a></b><br><sub>mgaitan · GitHub · ⭐ 3 · 2026-09-18</sub><br>可加载的 C 扩展，以 SQL 函数和批处理虚拟表的形式为 SQLite 加入 Jev 自然语言谓词、分类和打分能力，虚拟表每次请求最多打包 40 行。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/mattn/sqlite3-jev"><img src="https://opengraph.githubassets.com/1/mattn/sqlite3-jev" alt="sqlite3-jev" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/mattn/sqlite3-jev">sqlite3-jev</a></b><br><sub>mattn · GitHub · ⭐ 3 · 2026-09-18</sub><br>用 C 写的 SQLite 扩展，新增 jev_noul、jev_choice 和 jev_score 这几个 SQL 函数，可调用 Jev 或本地的 tensai serve 端点，另有返回完整概率的 JSON 版本。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Query-farm/vgi-typesafe"><img src="https://raw.githubusercontent.com/Query-farm/vgi-typesafe/main/docs/vgi-logo.png" alt="vgi-typesafe" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Query-farm/vgi-typesafe">vgi-typesafe</a></b><br><sub>Query-farm · GitHub · ⭐ 3 · 2026-09-18</sub><br>通过 VGI 扩展加载的 DuckDB worker，把 Jev 的 Choice、Noul 和 Score 暴露为 SQL 表函数，可与数据表做 LATERAL join，返回带置信度和概率的类型化列。<br><sub>相关: <a href="https://query.farm/vgi/">site</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/AgentEvalHQ/AgentEval/tree/main/src/AgentEval.Core/Decisions"><img src="https://raw.githubusercontent.com/AgentEvalHQ/AgentEval/main/assets/AgentEval_bounded.png" alt="AgentEval 决策评测" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/AgentEvalHQ/AgentEval/tree/main/src/AgentEval.Core/Decisions">AgentEval 决策评测</a></b><br><sub>AgentEvalHQ · GitHub · ⭐ 146 仓库 · 2026-01-02</sub><br>.NET AI agent 的评测工具包，通过 TypeSafe 或 OpenRouter 把 Jev 加为第三种评估器，比如针对查询、回复和上下文的一个有据性（groundedness）Noul。<br><sub>相关: <a href="https://github.com/AgentEvalHQ/AgentEval/blob/main/docs/adr/evidence/033-jev-first-calls-2026-09-20.md">evidence</a> · <a href="https://agenteval.dev/">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/vogler75/monster-mq/tree/main/broker/src/main/kotlin/genai/decision"><img src="https://opengraph.githubassets.com/1/vogler75/monster-mq" alt="MonsterMQ 主题决策" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/vogler75/monster-mq/tree/main/broker/src/main/kotlin/genai/decision">MonsterMQ 主题决策</a></b><br><sub>vogler75 · GitHub · ⭐ 142 仓库 · 2024-08-03</sub><br>工业物联网 MQTT broker，新增由主题触发的决策：Jev 通过 OpenRouter 评估主题的当前值和历史值，再把答案发布回 MQTT。<br><sub>相关: <a href="https://github.com/vogler75/monster-mq/blob/main/dev/plans/TOPIC_BASED_DECISION_MAKING.md">plan</a> · <a href="https://monstermq.com">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/AstroVela/vane/blob/main/vane/ai/_jev.py"><img src="https://opengraph.githubassets.com/1/AstroVela/vane" alt="Vane 的 Jev 判断" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/AstroVela/vane/blob/main/vane/ai/_jev.py">Vane 的 Jev 判断</a></b><br><sub>AstroVela · GitHub · ⭐ 135 仓库 · 2026-07-16</sub><br>基于 DuckDB 分支构建的多模态数据引擎，在 Vane 表达式上加入 Jev 判断，通过异步 TypeSafe SDK 分批处理行。<br><sub>相关: <a href="https://github.com/AstroVela/vane/blob/main/examples/jev_judgments.py">example</a> · <a href="https://vane.astrovela.ai/">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/flyteorg/flyte-sdk/tree/main/examples/typesafe_ai"><img src="https://raw.githubusercontent.com/flyteorg/flyte-sdk/main/static/flyte-tui.gif" alt="Flyte 的 System One 示例" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/flyteorg/flyte-sdk/tree/main/examples/typesafe_ai">Flyte 的 System One 示例</a></b><br><sub>flyteorg · GitHub · ⭐ 128 仓库 · 2025-07-29</sub><br>Jev 与 LLM 交替工作，把每个任务拆成 11 到 16 个原子问题，再把结果路由到自动处理、复核或升级。<br><sub>相关: <a href="https://flyte.org/">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Vicente-MD/jev-resilience"><img src="https://opengraph.githubassets.com/1/Vicente-MD/jev-resilience" alt="jev-resilience" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Vicente-MD/jev-resilience">jev-resilience</a></b><br><sub>Vicente-MD · GitHub · ⭐ 2 · 2026-09-17</sub><br>面向 WebFlux 的 Spring Boot starter，充当语义熔断器：让 Jev 检查 HTTP 200 响应体里是否藏着错误、堆栈信息或维护通知，并抛出普通异常。<br><sub><b>Jev 用法:</b> 每个响应体得出一个隐藏故障分，与本地阈值比较；API 出错时按 0.0 处理，默认放行。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/zkjoie/jevbus"><img src="https://opengraph.githubassets.com/1/zkjoie/jevbus" alt="jevbus" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/zkjoie/jevbus">jevbus</a></b><br><sub>zkjoie · GitHub · ⭐ 2 · 2026-09-20</sub><br>Rust 流式事件总线，路由、订阅和消费都由一个概率评判器决定，参考评判器是 Jev；支持自然语言订阅，以及可重放、无 IO 的决策策略。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/CompleteTech-LLC-AI-Research/jev-311-heatmap"><img src="https://raw.githubusercontent.com/CompleteTech-LLC-AI-Research/jev-311-heatmap/main/results/2026-09-01/composite.png" alt="NYC 311 JEV Heatmaps" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/CompleteTech-LLC-AI-Research/jev-311-heatmap">NYC 311 JEV Heatmaps</a></b><br><sub>CompleteTech-LLC-AI-Research · GitHub · ⭐ 2 · 2026-09-20</sub><br>可复现的流水线：评估纽约 311 投诉描述，把得到的影响信号映射到地理网格上，输出交互式 HTML 地图和 PNG；实际运行共发起 634 次 API 调用。<br><sub><b>Jev 用法:</b> 逐条描述做判断，重复描述走缓存，并校验响应。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/itzKashan2912/status/2102169255341171132"><img src="https://pbs.twimg.com/amplify_video_thumb/2102169138940796928/img/r7CEu1B09R5BBNw_.jpg" alt="实时决策看板" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/itzKashan2912/status/2102169255341171132">实时决策看板</a></b><br><sub>itzKashan2912 · X · ♥ 2 · 2026-09-21</sub><br>Next.js 看板，用 Jev 每秒处理 50 个事件，标出重要事项、追踪需要关注的领域，并给出下一步最佳行动。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/TPAteeq/tocsin"><img src="https://raw.githubusercontent.com/TPAteeq/tocsin/main/docs/card.png" alt="tocsin" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/TPAteeq/tocsin">tocsin</a></b><br><sub>TPAteeq · GitHub · ⭐ 2 · 2026-09-18</sub><br>在日志摄入阶段做分拣的 Rust 工具：把日志行脱敏并归并成 Drain 模式，每个新模式只问 Jev 一次，再按一条用平实英文写的策略把日志行路由到呼叫值班、建工单或仅记录。<br><sub><b>Jev 用法:</b> 每个新模式一次请求，携带呼叫策略和四个问题，所以一个重复出现一百万次的模式也只判断一次。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/zzz1YAO/DataJev"><img src="https://raw.githubusercontent.com/zzz1YAO/DataJev/main/assets/datajev-demo.png" alt="DataJev" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/zzz1YAO/DataJev">DataJev</a></b><br><sub>zzz1YAO · GitHub · ⭐ 1 · 2026-09-21</sub><br>数据分析 agent：LLM 编写每一步 Python 分析代码，Jev 读取由目标、schema、近期结果和洞察组成的压缩 state，决定继续、换方向、验证还是停止。</td>
</tr>
<tr>
<td width="260" valign="top"></td>
<td valign="top"><b><a href="https://x.com/BrandonSovran/status/2102230518469181529">BI 数据 agent 的决策层</a></b><br><sub>BrandonSovran · X · ♥ 1 · 2026-09-22</sub><br>供数据 agent 做自动化 BI 分析时依据的决策层；在一轮受策略约束的 120 个用例测试中，Jev 耗时 953 毫秒、召回率 100%，而 Luna 耗时 3,383 毫秒、召回率 90.3%，还出现 14 次不安全操作。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/syphhhhhhhhhh/status/2101767097504121072"><img src="https://pbs.twimg.com/amplify_video_thumb/2101767042718220289/img/W4uwOoMpMY7RN09P.jpg" alt="硬约束与软约束分类器" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/syphhhhhhhhhh/status/2101767097504121072">硬约束与软约束分类器</a></b><br><sub>syphhhhhhhhhh · X · ♥ 1 · 2026-09-20</sub><br>一个小测试：用 Jev 判断一条书面需求是硬约束还是软约束，不到一秒给出答案。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/hemanth/hfjev"><img src="https://opengraph.githubassets.com/1/hemanth/hfjev" alt="hfjev" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/hemanth/hfjev">hfjev</a></b><br><sub>hemanth · GitHub · ⭐ 1 · 2026-09-20</sub><br>Python 和 JavaScript 工具：加载任意 Hugging Face 数据集，按其领域调整评测标准，并用校准的概率给每一行分类；支持流式处理，提供 CLI 和网页工作台。<br><sub><b>Jev 用法:</b> 每行一次并行的 System One 调用，包含领域包里的 Choice、Noul 和 Score 问题。</sub><br><sub>相关: <a href="https://hemanth.github.io/hfjev/">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/gaborishka/jev-wrapped"><img src="https://opengraph.githubassets.com/1/gaborishka/jev-wrapped" alt="Jev Wrapped" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/gaborishka/jev-wrapped">Jev Wrapped</a></b><br><sub>gaborishka · GitHub · ⭐ 1 · 2026-09-19</sub><br>Web 应用：让 Jev 评判一个公开 Telegram 频道过去十二个月的帖子，生成一张可分享的卡片，展示帖子构成、广告、标题党和情绪施压情况，每 1,500 条帖子约 $0.10。<br><sub><b>Jev 用法:</b> 每条帖子一个在十种帖子类型中选择的 Choice，加三个是非题（付费广告、标题党、情绪施压）；代码在全年范围内均匀抽样最多 1,500 条帖子。</sub><br><sub>相关: <a href="https://wrapped.ivanhabor.com">app</a> · <a href="https://wrapped.ivanhabor.com">app 2</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/NicolasMontone/jev-evals"><img src="https://opengraph.githubassets.com/1/NicolasMontone/jev-evals" alt="jev-evals" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/NicolasMontone/jev-evals">jev-evals</a></b><br><sub>NicolasMontone · GitHub · ⭐ 1 · 2026-09-18</sub><br>基于评分细则的 LLM 与 agent 输出评测 harness：把 input、output 和 expected 作为 state 只发送一次，在一次调用里把每条细则都作为 Jev 问题作答，便宜到每个 PR 都能跑。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/jyatesdotdev/jev-logtriage"><img src="https://opengraph.githubassets.com/1/jyatesdotdev/jev-logtriage" alt="jev-logtriage" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/jyatesdotdev/jev-logtriage">jev-logtriage</a></b><br><sub>jyatesdotdev · GitHub · ⭐ 1 · 2026-09-19</sub><br>CLI 工具：把折叠后的 Loki 日志按来源打包，每个来源一次 Jev 调用，包含 Noul、Score 和 Choice 问题，再由代码把答案映射为屏蔽、观察、复核、通知或呼叫值班，低置信度的一律进复核。<br><sub>相关: <a href="https://pypi.org/project/jev-logtriage">pypi</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/nexibeo/jev-organize"><img src="https://raw.githubusercontent.com/nexibeo/jev-organize/main/assets/banner.svg" alt="jev-organize" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/nexibeo/jev-organize">jev-organize</a></b><br><sub>nexibeo · GitHub · ⭐ 1 · 2026-09-19</sub><br>Node CLI、Claude skill 兼 Codex agent：通过 OpenRouter 上的 Jev，按部门、类型、敏感度、日期、交易对手和 PII 给一个文件夹里的公司文件分类并建立索引，每 1,000 个文件约 17 美分。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Cab14bacc/jev-sheets"><img src="https://opengraph.githubassets.com/1/Cab14bacc/jev-sheets" alt="jev-sheets" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Cab14bacc/jev-sheets">jev-sheets</a></b><br><sub>Cab14bacc · GitHub · ⭐ 1 · 2026-09-21</sub><br>一组 Google Sheets 自定义函数（JEV_IF、JEV_PROB、JEV_CHOICE、JEV_SCORE），用 Jev 对每个单元格的文本做分类、打标签和打分，置信度低于设定下限时返回 UNSURE。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/hemanth/tc39-atlas"><img src="https://opengraph.githubassets.com/1/hemanth/tc39-atlas" alt="TC39 Proposal Atlas" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/hemanth/tc39-atlas">TC39 Proposal Atlas</a></b><br><sub>hemanth · GitHub · ⭐ 1 · 2026-09-17</sub><br>ECMAScript TC39 提案的交互式浏览器，附加了一套语义分类体系，比如采纳路径和 7 种意图原型，提案变化时自动刷新。<br><sub><b>Jev 用法:</b> 用 Choice 问题从五个维度给每个提案分类，并归入 7 种原型之一。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://huggingface.co/spaces/iluvblender/yolo-jev-scene-filter"><img src="https://cdn-thumbnails.huggingface.co/social-thumbnails/spaces/iluvblender/yolo-jev-scene-filter.png" alt="YOLO + Jev 场景过滤器" width="240"></a></td>
<td valign="top"><b><a href="https://huggingface.co/spaces/iluvblender/yolo-jev-scene-filter">YOLO + Jev 场景过滤器</a></b><br><sub>iluvblender · 应用 · ♥ 1 · 2026-09-20</sub><br>视觉流水线：YOLO-World 提出开放词表的检测框，Jev 对每个框回答一个是非题决定是否保留，得到数量更少、过滤更好的检测结果。<br><sub><b>Jev 用法:</b> 通过 TypeSafe /v1/systemone API，每个检测框问一个 Noul。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/pinecone-io/cultivar/blob/main/evals/framework/typesafe_grader.py"><img src="https://opengraph.githubassets.com/1/pinecone-io/cultivar" alt="cultivar 的 TypeSafe 评分器" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/pinecone-io/cultivar/blob/main/evals/framework/typesafe_grader.py">cultivar 的 TypeSafe 评分器</a></b><br><sub>pinecone-io · GitHub · ⭐ 40 仓库 · 2026-06-17</sub><br>Pinecone 的 agent skill 测试 CLI 中的可选评分后端：用 Jev 而不是 Claude 按任务标准给沙箱里的 agent 运行打分，据称便宜约 30 倍，面向 CI 卡点。<br><sub>相关: <a href="https://github.com/pinecone-io/cultivar">repo</a> · <a href="https://github.com/pinecone-io/cultivar/blob/main/docs/grader.md">docs</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/cristianodabc/aludel/blob/main/guides/evaluations.md"><img src="https://opengraph.githubassets.com/1/cristianodabc/aludel" alt="Aludel 的 Jev 类型化评委" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/cristianodabc/aludel/blob/main/guides/evaluations.md">Aludel 的 Jev 类型化评委</a></b><br><sub>cristianodabc · GitHub · ⭐ 38 仓库 · 2026-03-20</sub><br>由 Jev 支撑的 typed_judge 断言，属于 Aludel（Phoenix 原生的 Elixir LLM 评测工作台）：生成的输出由 Jev 评判，通过/失败和归一化分数都来自类型化答案，并附带一个预置数据的安全边界演示。<br><sub><b>Jev 用法:</b> 独立应用使用 jev Hex 客户端；Jev 只收到截断到上限的输出和渲染后的输入，从不接触预期答案或元数据。</sub><br><sub>相关: <a href="https://github.com/cristianodabc/aludel">repo</a> · <a href="https://hexdocs.pm/aludel">docs</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/overmind-core/overmind/blob/main/overbae/services/eval/decisions.py"><img src="https://github.com/user-attachments/assets/8ba6a64f-0819-47bd-9d58-af89ee3e7bad" alt="Overmind 的 Jev 决策评委" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/overmind-core/overmind/blob/main/overbae/services/eval/decisions.py">Overmind 的 Jev 决策评委</a></b><br><sub>overmind-core · GitHub · ⭐ 30 仓库 · 2026-03-27</sub><br>决策层，属于 Overmind（把生产环境 agent trace 变成微调模型的平台）：用 Jev 的选择充当评测评委（通过/失败/信息不足，论断得到支持/被反驳），并做数据集的语义检查。<br><sub><b>Jev 用法:</b> Choice 问题在 token 预算内分批发送，配合 Redis 容量预留和 24 h 缓存；state 一律视为不可信证据。</sub><br><sub>相关: <a href="https://github.com/overmind-core/overmind">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/pnthn-ai/polar_llama/blob/main/docs/TYPESAFE.md"><img src="https://raw.githubusercontent.com/daviddrummond95/polar_llama/refs/heads/main/PolarLlama.webp" alt="Polar Llama 的 TypeSafe 支持" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/pnthn-ai/polar_llama/blob/main/docs/TYPESAFE.md">Polar Llama 的 TypeSafe 支持</a></b><br><sub>pnthn-ai · GitHub · ⭐ 30 仓库 · 2024-05-03</sub><br>Polars LLM 插件中的原生 Rust TypeSafe 层：逐行回答 Noul、Choice 和 Score 问题，或对文档的每一行套用一份 Pydantic 契约，结果都以带类型的 dataframe 列返回。<br><sub>相关: <a href="https://github.com/pnthn-ai/polar_llama">repo</a> · <a href="https://pnthn.ai/polar-llama/">site</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/harness/harness-evals/tree/main/src/harness_evals/decision"><img src="https://opengraph.githubassets.com/1/harness/harness-evals" alt="harness-evals 的决策指标" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/harness/harness-evals/tree/main/src/harness_evals/decision">harness-evals 的决策指标</a></b><br><sub>harness · GitHub · ⭐ 28 仓库 · 2026-04-20</sub><br>Harness 开源 LLM agent 评测框架的可选 decision 扩展，在 provider 抽象层之后加入 TypeSafe 的 Choice、Score 和 Noul 指标，与已有的正确性、有据性和安全性指标并列。<br><sub>相关: <a href="https://github.com/harness/harness-evals">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/asimov-platform/asimov-cli/blob/master/src/shared.rs"><img src="https://opengraph.githubassets.com/1/asimov-platform/asimov-cli" alt="ASIMOV CLI 的 Jev 过滤器" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/asimov-platform/asimov-cli/blob/master/src/shared.rs">ASIMOV CLI 的 Jev 过滤器</a></b><br><sub>asimov-platform · GitHub · ⭐ 27 仓库 · 2025-02-13</sub><br>由 Jev 支撑的语义过滤器，内置于 ASIMOV（OSINT 与 AI 平台）的命令行工具：把输入记录流式送进 Jev，只保留与一段自然语言评判标准相符的记录。<br><sub><b>Jev 用法:</b> 在分批的 state 中为每行输入问一个 Noul（“rubric 是否描述了 inputs[i]？”），输出匹配度高于阈值的记录。</sub><br><sub>相关: <a href="https://github.com/asimov-platform/asimov-cli">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"></td>
<td valign="top"><b><a href="https://x.com/inventur_es/status/2101059512048169306">jev-scraper-chrome-extension</a></b><br><sub>inventur_es · X · ▶ 94 · 2026-09-18</sub><br>Chrome 扩展，尝试用 Jev 把网页转成符合 schema 的 JSON；作者说这是个有趣的实验，但最终失败了，对一个分类器来说野心太大。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/orq-ai/evaluatorq/blob/main/docs/classify-judges.md"><img src="https://raw.githubusercontent.com/orq-ai/evaluatorq/main/docs/assets/evaluatorq-splash.svg" alt="evaluatorq 的分类评委" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/orq-ai/evaluatorq/blob/main/docs/classify-judges.md">evaluatorq 的分类评委</a></b><br><sub>orq-ai · GitHub · ⭐ 21 仓库 · 2026-06-19</sub><br>orq 的 Python 评测框架 evaluatorq 中的分类评委：在 LLM-as-a-jury 评审团里让 typesafe/jev-latest 与基于提示词的 LLM 评委同席，通过 Orq 路由器的 classify 端点回答是非、标签、量表或两两对比问题。<br><sub>相关: <a href="https://github.com/orq-ai/evaluatorq">repo</a> · <a href="https://orq-ai.github.io/evaluatorq/">docs</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/valzav/valcraft/blob/main/scripts/jev-grade.py"><img src="https://raw.githubusercontent.com/valzav/valcraft/main/docs/assets/valcraft-banner.png" alt="Valcraft 的 Jev 评分器" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/valzav/valcraft/blob/main/scripts/jev-grade.py">Valcraft 的 Jev 评分器</a></b><br><sub>valzav · GitHub · ⭐ 19 仓库 · 2026-08-11</sub><br>为 Valcraft 的规格驱动 agent skill 写的评测打分脚本：基于一次运行的记录和输出，对每条待评断言向 Jev 问一个 Noul，并在 LLM 评分器结果旁边写出一份 jev-grading.json。<br><sub><b>Jev 用法:</b> 通过 OpenRouter 固定使用 typesafe/jev-1.13；true 表示有清晰、可引用的证据证明任务确实完成。</sub><br><sub>相关: <a href="https://github.com/valzav/valcraft">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/TelecomsXChangeAPi/OpenTextShield/blob/main/evals/label_audit.py"><img src="https://opengraph.githubassets.com/1/TelecomsXChangeAPi/OpenTextShield" alt="OpenTextShield 的 Jev 标签审计" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/TelecomsXChangeAPi/OpenTextShield/blob/main/evals/label_audit.py">OpenTextShield 的 Jev 标签审计</a></b><br><sub>TelecomsXChangeAPi · GitHub · ⭐ 16 仓库 · 2023-12-16</sub><br>为开源短信垃圾与钓鱼分类器 OpenTextShield 写的标签审计脚本：让 Jev 标出 ham/spam/phishing 标签看起来有误的训练数据行，交给人来裁定，答案保存在仓库里。<br><sub>相关: <a href="https://github.com/TelecomsXChangeAPi/OpenTextShield">repo</a> · <a href="https://ots.telecomsxchange.com">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/ujuc/dotrc/blob/main/agents/claude/skills/waza/scripts/typesafe-judge"><img src="https://opengraph.githubassets.com/1/ujuc/dotrc" alt="waza typesafe-judge" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/ujuc/dotrc/blob/main/agents/claude/skills/waza/scripts/typesafe-judge">waza typesafe-judge</a></b><br><sub>ujuc · GitHub · ⭐ 15 仓库 · 2014-10-18</sub><br>个人 dotfiles 仓库里为 skill 评测工具 waza 写的评分脚本：就 agent 的回答向 Jev 提是非题，可选对照一段源文本，只有每个判断都过阈值才算通过。<br><sub>相关: <a href="https://github.com/ujuc/dotrc">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/atanasster/electionsbg/blob/main/ai/llm/jevClient.ts"><img src="https://opengraph.githubassets.com/1/atanasster/electionsbg" alt="naiasno.bg 的 Jev 聊天路由" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/atanasster/electionsbg/blob/main/ai/llm/jevClient.ts">naiasno.bg 的 Jev 聊天路由</a></b><br><sub>atanasster · GitHub · ⭐ 14 仓库 · 2024-11-06</sub><br>保加利亚的选举、议会和预算开放数据平台，其聊天功能用 Jev 把每个问题路由到对应的数据通道，任何环节出错都回退到 Gemini。<br><sub><b>Jev 用法:</b> 通过站点代理发起一个 Choice 调用，时间预算 2.5 s 并带熔断器；失败时返回 null，通道随之降级到确定性路由器或完整的 Gemini 提示词。</sub><br><sub>相关: <a href="https://github.com/atanasster/electionsbg">repo</a> · <a href="https://github.com/atanasster/electionsbg/blob/main/docs/plans/jev-chat-integration-v1.md">docs</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/whilehq/whileai-sdk/blob/main/whileai/simulations/generate/typesafe_backend.py"><img src="https://raw.githubusercontent.com/whilehq/whileai-sdk/main/docs/assets/hero-light.png" alt="whileai 的 Jev 评委后端" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/whilehq/whileai-sdk/blob/main/whileai/simulations/generate/typesafe_backend.py">whileai 的 Jev 评委后端</a></b><br><sub>whilehq · GitHub · ⭐ 14 仓库 · 2026-08-16</sub><br>agent 后训练与评测 SDK，带有 typesafe:&lt;model&gt; 评委后端，把单点、两两对比、评分细则和审计几类评委都放在 Jev 上跑，而不是用聊天模型。<br><sub><b>Jev 用法:</b> 每个评委变成一次包含 Noul、Choice 或 Score 问题的 System One 请求；该后端只做评委，拒绝承担 agent 或模拟器角色。</sub><br><sub>相关: <a href="https://withwhile.com">app</a> · <a href="https://github.com/whilehq/whileai-sdk">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/akakaule/NimBus/blob/master/src/NimBus.Extensions.IntegrationIntelligence/Providers/TypeSafeFailureIntelligenceProvider.cs"><img src="https://raw.githubusercontent.com/akakaule/NimBus/master/assets/banner.png" alt="NimBus 的 TypeSafe 故障分析" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/akakaule/NimBus/blob/master/src/NimBus.Extensions.IntegrationIntelligence/Providers/TypeSafeFailureIntelligenceProvider.cs">NimBus 的 TypeSafe 故障分析</a></b><br><sub>akakaule · GitHub · ⭐ 9 仓库 · 2026-03-06</sub><br>基于 Azure Service Bus 的 .NET 集成平台，其故障分析扩展为每条失败消息发一次有边界的 TypeSafe 请求，替运维人员给故障分类。<br><sub>相关: <a href="https://github.com/akakaule/NimBus">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/databendlabs/databend-udf/blob/main/python/example/jev.py"><img src="https://opengraph.githubassets.com/1/databendlabs/databend-udf" alt="Databend 的 Jev UDF" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/databendlabs/databend-udf/blob/main/python/example/jev.py">Databend 的 Jev UDF</a></b><br><sub>databendlabs · GitHub · ⭐ 8 仓库 · 2023-11-07</sub><br>Databend 数据仓库的示例 UDF 服务器，新增 jev、jev_prob、jev_choice、jev_score 和 jev_eval 这几个 SQL 函数，按批把行发给 Jev。<br><sub><b>Jev 用法:</b> 默认每批 20 行、6 个并发请求；每个函数对应每行一个 Noul、Choice 或 Score 问题。</sub><br><sub>相关: <a href="https://github.com/databendlabs/databend-udf">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/tkersey/skills-zig/tree/main/apps/typesafe"><img src="https://opengraph.githubassets.com/1/tkersey/skills-zig" alt="typesafe (Zig CLI)" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/tkersey/skills-zig/tree/main/apps/typesafe">typesafe (Zig CLI)</a></b><br><sub>tkersey · GitHub · ⭐ 8 仓库 · 2026-02-20</sub><br>用 Zig 写的文档审阅 CLI：把每个文本或 Markdown 文件连同配置好的 Score 问题发给 Jev，输出包含分数、各等级概率、用量和 needs_review 标记的 JSONL。<br><sub><b>Jev 用法:</b> 默认评分细则按 0-3 给表面上的技术准确性打分，低于 2 的文档会被标记出来，作为分拣信号。</sub><br><sub>相关: <a href="https://github.com/tkersey/skills-zig">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/The-Focus-AI/umwelten/blob/main/packages/core/src/judgment/jev.ts"><img src="https://opengraph.githubassets.com/1/The-Focus-AI/umwelten" alt="Umwelten 的 Jev 判断后端" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/The-Focus-AI/umwelten/blob/main/packages/core/src/judgment/jev.ts">Umwelten 的 Jev 判断后端</a></b><br><sub>The-Focus-AI · GitHub · ⭐ 8 仓库 · 2025-03-26</sub><br>模型评测与 agent 栖息环境工具包，其判断后端通过 OpenRouter、TypeSafe 或 Mycel decisions 端点在 Jev 上运行类型化问题，并记录每次尝试及其成本。<br><sub><b>Jev 用法:</b> 每次调用只尝试一次、没有隐藏重试，所以实验会如实记录失败；在 TypeSafe 上固定用 jev-1.13.0，其他渠道固定用 typesafe/jev-1.13。</sub><br><sub>相关: <a href="https://umwelten.thefocus.ai">app</a> · <a href="https://github.com/The-Focus-AI/umwelten">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/ziqi-jin/agent-to-trust/blob/master/docs/jev.md"><img src="https://raw.githubusercontent.com/ziqi-jin/agent-to-trust/master/docs/img/a2t-flow.svg" alt="Agent to Trust 的 Jev 评委交叉核验" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/ziqi-jin/agent-to-trust/blob/master/docs/jev.md">Agent to Trust 的 Jev 评委交叉核验</a></b><br><sub>ziqi-jin · GitHub · ⭐ 7 仓库 · 2026-08-29</sub><br>agent 信用实验室 Agent to Trust 里的交叉核验：用确定性评分器、LLM 评委，以及作为独立第三评委的 Jev 给带金标的样本打分，实时报告准确率、延迟和成本。<br><sub>相关: <a href="https://sealit.cc">app</a> · <a href="https://github.com/ziqi-jin/agent-to-trust">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/buildinternet/releases/blob/main/packages/ai/src/marketing-classifier.ts"><img src="https://raw.githubusercontent.com/buildinternet/releases/main/docs/assets/readme-home.png" alt="Releases.sh 营销内容分类器" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/buildinternet/releases/blob/main/packages/ai/src/marketing-classifier.ts">Releases.sh 营销内容分类器</a></b><br><sub>buildinternet · GitHub · ⭐ 7 仓库 · 2026-03-25</sub><br>更新日志收录站 releases.sh 中的过滤器：对每条刚解析出的 feed 条目运行一个 Jev Choice，把真正的产品新闻与案例研究、newsletter、活动回顾等营销内容区分开，并屏蔽后者。<br><sub><b>Jev 用法:</b> 一个在八个类别（real_product_news、case_study、newsletter……）中选择的 Choice；所选类别的概率达到 0.8 及以上就屏蔽该条目。</sub><br><sub>相关: <a href="https://releases.sh">app</a> · <a href="https://github.com/buildinternet/releases">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/ryanwaits/secondlayer/tree/main/scripts/ops"><img src="https://opengraph.githubassets.com/1/ryanwaits/secondlayer" alt="Secondlayer 的 Jev 运维闸门" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/ryanwaits/secondlayer/tree/main/scripts/ops">Secondlayer 的 Jev 运维闸门</a></b><br><sub>ryanwaits · GitHub · ⭐ 6 仓库 · 2025-05-25</sub><br>自托管 Stacks 索引器 Secondlayer 里的运维脚本：一个 Slack 闸门，只有 Jev 给 page_now 打出 0.8 及以上且严重程度 3+ 时才呼叫值班；另有一个 spike，测试用 Jev 分拣解码器故障。<br><sub><b>Jev 用法:</b> 通过 AI SDK 的 evaluate 调用，发起一个在运维事件类型中选择的 Choice，外加 page_now 和严重程度两个问题；调用失败时默认放行，照常发出呼叫。</sub><br><sub>相关: <a href="https://secondlayer.tools">app</a> · <a href="https://github.com/ryanwaits/secondlayer">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/singi-labs/sifa-sdk/tree/main/src/jev"><img src="https://opengraph.githubassets.com/1/singi-labs/sifa-sdk" alt="Sifa SDK 的 Jev 组织情报" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/singi-labs/sifa-sdk/tree/main/src/jev">Sifa SDK 的 Jev 组织情报</a></b><br><sub>singi-labs · GitHub · ⭐ 6 仓库 · 2026-05-14</sub><br>Jev 子路径，位于 Sifa SDK 中（该 SDK 服务于一个基于 AT Protocol 的职业社交网络）：定义了用于重复组织检测和企业属性分类的问题构造器、分类体系和阈值。<br><sub><b>Jev 用法:</b> 查重时对一对候选组织问一个 Noul；行业、类型和规模则基于单个组织的 state 分别用独立的 Choice 判断。</sub><br><sub>相关: <a href="https://github.com/singi-labs/sifa-sdk">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Enucatl/docker-paperless-ai/blob/main/ai/src/paperless_ai/eval/jev_evaluator.py"><img src="https://opengraph.githubassets.com/1/Enucatl/docker-paperless-ai" alt="docker-paperless-ai 的 Jev 评估器" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Enucatl/docker-paperless-ai/blob/main/ai/src/paperless_ai/eval/jev_evaluator.py">docker-paperless-ai 的 Jev 评估器</a></b><br><sub>Enucatl · GitHub · ⭐ 5 仓库 · 2026-03-25</sub><br>评估模块，属于 docker-paperless-ai（为 Paperless-ngx 归档做 AI OCR 和元数据提取的流水线）：让 Jev 给每份文档抽取出的日期、往来方、标题和摘要打分。<br><sub><b>Jev 用法:</b> 每个抽取字段做一次 Noul 判断，平均成总分，并保留各字段的置信度。</sub><br><sub>相关: <a href="https://github.com/Enucatl/docker-paperless-ai">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/alexgreensh/eval-genius/blob/main/skills/eval-genius/references/15-decision-model-judge.md"><img src="https://raw.githubusercontent.com/alexgreensh/eval-genius/main/assets/img/eval-genius.png" alt="eval-genius 的决策模型评委通道" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/alexgreensh/eval-genius/blob/main/skills/eval-genius/references/15-decision-model-judge.md">eval-genius 的决策模型评委通道</a></b><br><sub>alexgreensh · GitHub · ⭐ 5 仓库 · 2026-09-10</sub><br>一条评委通道，位于 eval-genius agent skill 中：为二元或封闭标签的评测维度推荐 Jev 做评委，附带校准、置信度路由和级联成本的脚本；在达到 kappa 0.8 的下限之前只用于探索。<br><sub>相关: <a href="https://github.com/alexgreensh/eval-genius">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/openwebtrack/openwebtrack/blob/main/src/lib/server/insights.ts"><img src="https://opengraph.githubassets.com/1/openwebtrack/openwebtrack" alt="OpenWebTrack 的 Jev 洞察" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/openwebtrack/openwebtrack/blob/main/src/lib/server/insights.ts">OpenWebTrack 的 Jev 洞察</a></b><br><sub>openwebtrack · GitHub · ⭐ 5 仓库 · 2026-02-23</sub><br>自托管开源网站分析平台 OpenWebTrack 的洞察功能：基于聚合统计，询问 Jev 某一时段的主要流量趋势、最大驱动因素和流量质量。<br><sub><b>Jev 用法:</b> 使用 Choice 问题（增长/平稳/下降之类），每条洞察都存储置信度；只有配置了 key 才启用。</sub><br><sub>相关: <a href="https://openwebtrack.one">app</a> · <a href="https://github.com/openwebtrack/openwebtrack">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/EnjoyDigital/Umbraco.Community.Schemeweaver/blob/main/docs/typesafe-integration.md"><img src="https://opengraph.githubassets.com/1/EnjoyDigital/Umbraco.Community.Schemeweaver" alt="SchemeWeaver 的 TypeSafe 自动映射" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/EnjoyDigital/Umbraco.Community.Schemeweaver/blob/main/docs/typesafe-integration.md">SchemeWeaver 的 TypeSafe 自动映射</a></b><br><sub>EnjoyDigital · GitHub · ⭐ 5 仓库 · 2026-03-19</sub><br>可选配套包，用于 Umbraco 的 JSON-LD 插件 SchemeWeaver：在把 CMS 内容属性自动映射到 Schema.org 属性时，用 Jev 的判断取代名称匹配，可在界面中和通过 MCP 使用。<br><sub>相关: <a href="https://github.com/EnjoyDigital/Umbraco.Community.Schemeweaver">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://qiita.com/asahide/items/ce6c7e0d08fe68a90a5d"><img src="https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-user-contents.imgix.net%2Fhttps%253A%252F%252Fcdn.qiita.com%252Fassets%252Fpublic%252Farticle-ogp-background-afbab5eb44e0b055cce1258705637a91.png%3Fixlib%3Drb-4.1.1%26w%3D1200%26blend64%3DaHR0cHM6Ly9xaWl0YS11c2VyLXByb2ZpbGUtaW1hZ2VzLmltZ2l4Lm5ldC9odHRwcyUzQSUyRiUyRnMzLWFwLW5vcnRoZWFzdC0xLmFtYXpvbmF3cy5jb20lMkZxaWl0YS1pbWFnZS1zdG9yZSUyRjAlMkYyMzEzOTI2JTJGY2QxYmUzYmMxYmQ4ZTZhNzUzYjg5MTNlNzgwNGYxNGY4MjhhYzgzYyUyRnhfbGFyZ2UucG5nJTNGMTY5NjU1OTU3NT9peGxpYj1yYi00LjEuMSZhcj0xJTNBMSZmaXQ9Y3JvcCZtYXNrPWVsbGlwc2UmYmc9RkZGRkZGJmZtPXBuZzMyJnM9ZTc1MzJiZDkzMzI1NjE4MDQ2MTg4OGZhZmVhMjRkOTY%26blend-x%3D120%26blend-y%3D462%26blend-w%3D90%26blend-h%3D90%26blend-mode%3Dnormal%26mark64%3DaHR0cHM6Ly9xaWl0YS1vcmdhbml6YXRpb24taW1hZ2VzLmltZ2l4Lm5ldC9odHRwcyUzQSUyRiUyRnMzLWFwLW5vcnRoZWFzdC0xLmFtYXpvbmF3cy5jb20lMkZxaWl0YS1vcmdhbml6YXRpb24taW1hZ2UlMkY0M2Q5ZDBkOWYwNWM3ZDg4ZTk0OGQ2YjU0ZjdiMDcyNjg2MzM2MDg3JTJGb3JpZ2luYWwuanBnJTNGMTcyMDQwNzIxND9peGxpYj1yYi00LjEuMSZ3PTQ0Jmg9NDQmZml0PWNyb3AmbWFzaz1jb3JuZXJzJmNvcm5lci1yYWRpdXM9OCZiZz1GRkZGRkYmYm9yZGVyPTIlMkNGRkZGRkYmZm09cG5nMzImcz02MGM5YjEyZGUwOWI2MWYyMTAwYmM3N2JhZjkzYzQ2MA%26mark-x%3D186%26mark-y%3D515%26mark-w%3D40%26mark-h%3D40%26s%3D816ce069576dee7b7486ed50d00eb4e6?ixlib=rb-4.1.1&amp;w=1200&amp;fm=jpg&amp;mark64=aHR0cHM6Ly9xaWl0YS11c2VyLWNvbnRlbnRzLmltZ2l4Lm5ldC9-dGV4dD9peGxpYj1yYi00LjEuMSZ3PTk2MCZoPTMyNCZ0eHQ9QXVyb3JhJTIwUG9zdGdyZVNRTCUyMCVFMyU4MSU4QiVFMyU4MiU4OSUyMEpldiUyMCVFMyU4MiU5MiVFNSU5MSVCQyVFMyU4MiU5MyVFMyU4MSVBNyVFMyU4MSVCRiVFMyU4MSU5RiZ0eHQtYWxpZ249bGVmdCUyQ3RvcCZ0eHQtY29sb3I9JTIzMUUyMTIxJnR4dC1mb250PUhpcmFnaW5vJTIwU2FucyUyMFc2JnR4dC1zaXplPTU2JnR4dC1wYWQ9MCZzPWUzNzFhYzJmNDQ0YzVhMzM2MDcyNjI5NzJkNzYwMTIz&amp;mark-x=120&amp;mark-y=112&amp;blend64=aHR0cHM6Ly9xaWl0YS11c2VyLWNvbnRlbnRzLmltZ2l4Lm5ldC9-dGV4dD9peGxpYj1yYi00LjEuMSZ3PTgzOCZoPTU4JnR4dD0lNDBhc2FoaWRlJnR4dC1jb2xvcj0lMjMxRTIxMjEmdHh0LWZvbnQ9SGlyYWdpbm8lMjBTYW5zJTIwVzYmdHh0LXNpemU9MzYmdHh0LXBhZD0wJnM9YzdiYjMxMzczZTNiNjEyZmFiODlhMzc1NjQ1NjUwMTA&amp;blend-x=242&amp;blend-y=454&amp;blend-w=838&amp;blend-h=46&amp;blend-fit=crop&amp;blend-crop=left%2Cbottom&amp;blend-mode=normal&amp;txt64=5qCq5byP5Lya56S-6YeO5p2R57eP5ZCI56CU56m25omA&amp;txt-x=242&amp;txt-y=539&amp;txt-width=838&amp;txt-clip=end%2Cellipsis&amp;txt-color=%231E2121&amp;txt-font=Hiragino%20Sans%20W6&amp;txt-size=28&amp;s=3902fc224b198bf8d4549d88a4b72da1" alt="从 Aurora PostgreSQL 调用 Jev" width="240"></a></td>
<td valign="top"><b><a href="https://qiita.com/asahide/items/ce6c7e0d08fe68a90a5d">从 Aurora PostgreSQL 调用 Jev</a></b><br><sub>asahide · 文章 · 2026-09-20</sub><br>一篇日文实验记录：从 Aurora PostgreSQL 经 Lambda 调用 Jev 评判 1,000 条 Amazon 商品评论，测量每次请求分别打包 1、10、50、100 行时的耗时和准确率。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/expanso-io/demo-expanso-jev"><img src="https://raw.githubusercontent.com/expanso-io/demo-expanso-jev/main/docs/board.png" alt="Expanso × Jev" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/expanso-io/demo-expanso-jev">Expanso × Jev</a></b><br><sub>expanso-io · GitHub · 2026-09-19</sub><br>日志流水线演示：Expanso Edge 不调用模型直接归档常规日志行，其余的交给 Jev 回答四个问题（是否需要处理、严重程度、归属团队、是否复发），据此决定呼叫值班、通知、复核还是归档。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://openrouter.ai/labs/jev/extract"><img src="https://openrouter.ai/dynamic-og?title=Extract+without+guessing&amp;description=Extract+fields+from+a+document+without+inventing+values.&amp;v=2" alt="不靠猜的字段抽取" width="240"></a></td>
<td valign="top"><b><a href="https://openrouter.ai/labs/jev/extract">不靠猜的字段抽取</a></b><br><sub>OpenRouter · 应用</sub><br>OpenRouter Labs 的示例方案：从发票、租约、录用通知书和协议中抽取字段，让 Jev 从文本中找到的候选值里选出每个字段的值，因此无法凭空编造：12 个字段用时 0.6 s。<br><sub><b>Jev 用法:</b> 每个字段一个 Choice，候选项是从文档中找到的文本片段。</sub><br><sub>相关: <a href="https://openrouter.ai/typesafe/jev">model</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/ragelink/firehose-judge"><img src="https://raw.githubusercontent.com/ragelink/firehose-judge/main/public/og.png" alt="firehose-judge" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/ragelink/firehose-judge">firehose-judge</a></b><br><sub>ragelink · GitHub · 2026-09-19</sub><br>监听实时的 Bluesky firehose，对每条抽样帖子向 Jev 问八个问题，从意图、讽刺到是否像机器人、是否适合上屏，拿不准的判断转给人工通道。<br><sub><b>Jev 用法:</b> 每条帖子的八个问题都从一个 Cloudflare Durable Object 一次调用发出；被标为不安全的帖子在服务端直接丢弃。</sub><br><sub>相关: <a href="https://cloutmetrics.ai">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/zavocc/ground-zero"><img src="https://opengraph.githubassets.com/1/zavocc/ground-zero" alt="Ground Zero" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/zavocc/ground-zero">Ground Zero</a></b><br><sub>zavocc · GitHub · 2026-09-18</sub><br>alpha 版 Python 评测库，用 Jev 判断模型输出是否存在幻觉、是否正确、是否偏离指令，并提醒用户手动核验结果。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/rishi-raj-jain/hn-thread-judge"><img src="https://opengraph.githubassets.com/1/rishi-raj-jain/hn-thread-judge" alt="Hacker News Judge" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/rishi-raj-jain/hn-thread-judge">Hacker News Judge</a></b><br><sub>rishi-raj-jain · GitHub · 2026-09-21</sub><br>Hacker News 风格的网站：Jev 逐条阅读讨论最热帖子里的每一条评论，把每个帖子浓缩成一个结论；数据存在 Neon Postgres，支持 BM25 全文搜索。<br><sub>相关: <a href="https://hnjudge.vercel.app">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/steven-shoemaker/hunch"><img src="https://raw.githubusercontent.com/steven-shoemaker/hunch/main/docs/banner.png" alt="hunch" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/steven-shoemaker/hunch">hunch</a></b><br><sub>steven-shoemaker · GitHub · 2026-09-20</sub><br>一组 Python 函数（classify、score、check、pick、rank、where），针对标量、列表或 pandas 列向 Jev 提封闭集合问题，带缓存，并把结果回连到原数据。</td>
</tr>
<tr>
<td width="260" valign="top"></td>
<td valign="top"><b><a href="https://jevclassifier.vercel.app">Jev Classifier</a></b><br><sub>jevclassifier · 应用</sub><br>浏览器工具：加载 Telegram 频道导出的 JSON，按类型、质量、情感和反应基调给每条帖子打标签，还可以让 Jev 和 LLM 对决。<br><sub><b>Jev 用法:</b> 每条帖子四个问题：一个在 11 种帖子类型中选择的 Choice、一个质量 Score、一个情感 Choice 和一个反应基调 Choice。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/WebGrga/jev-board-lab"><img src="https://opengraph.githubassets.com/1/WebGrga/jev-board-lab" alt="Jev CSV Workbench" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/WebGrga/jev-board-lab">Jev CSV Workbench</a></b><br><sub>WebGrga · GitHub · 2026-09-16</sub><br>浏览器优先的工作台，在内存中解析 CSV，把选中的每一行变成 Jev 的 state，用来回答你自己的问题；请求经一个不存储任何数据的 Cloudflare Worker 转发。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/narulaskaran/jev-data-questions"><img src="https://opengraph.githubassets.com/1/narulaskaran/jev-data-questions" alt="Jev Data Analysis" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/narulaskaran/jev-data-questions">Jev Data Analysis</a></b><br><sub>narulaskaran · GitHub · 2026-09-17</sub><br>Web 应用：上传 CSV 或粘贴公开的 CSV URL，界面检查其 schema 并提出一个含 2-4 张图表的看板，再由 Jev 填入洞察数值。<br><sub>相关: <a href="https://jev-gamecast.vercel.app">app</a> · <a href="https://jev-gamecast.vercel.app">app 2</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/smasato/jev-jp-address"><img src="https://opengraph.githubassets.com/1/smasato/jev-jp-address" alt="jev-jp-address" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/smasato/jev-jp-address">jev-jp-address</a></b><br><sub>smasato · GitHub · 2026-09-17</sub><br>CLI 工具：对照日本邮政的 KEN_ALL 主数据，把杂乱的日本地址规范化为邮政编码；先走规则，只有匹配有歧义时才让 Jev 在候选项中做一个 Choice。<br><sub><b>Jev 用法:</b> 在候选的都道府县、市町村或町域（外加“都不是”）中做 Choice，以片假名读音作为判定标准；通过 AI SDK 调用。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/dtduc-git/jev-table"><img src="https://raw.githubusercontent.com/dtduc-git/jev-table/master/docs/demo.gif" alt="jev-table" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/dtduc-git/jev-table">jev-table</a></b><br><sub>dtduc-git · GitHub · 2026-09-19</sub><br>本地优先的 CLI，为 CSV 或 JSONL 文件添加由 Jev 支撑的 AI 列，给每一行标上类型化答案和概率，支持去重、复核队列、断点续跑和 dry-run 成本预估。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/ThyFriendlyFox/jev-triage"><img src="https://opengraph.githubassets.com/1/ThyFriendlyFox/jev-triage" alt="jev-triage" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/ThyFriendlyFox/jev-triage">jev-triage</a></b><br><sub>ThyFriendlyFox · GitHub · 2026-09-19</sub><br>主动学习标注流水线：直接采纳高置信度的 Jev 判断，把拿不准的行排队交给前沿教师模型或人工，并记录软标签用于本地蒸馏。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/k4its1t/jevlens"><img src="https://opengraph.githubassets.com/1/k4its1t/jevlens" alt="JevLens" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/k4its1t/jevlens">JevLens</a></b><br><sub>k4its1t · GitHub · 2026-09-21</sub><br>工具包：在标注好的 CSV 或 JSONL 上运行 YAML 中定义的 Jev 问题，保留完整概率分布以便离线重放，给出阈值建议，并附带 Streamlit 看板和 CI 准确率卡点。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/jeiel85/jevscope"><img src="https://raw.githubusercontent.com/jeiel85/jevscope/main/docs/workbench.png" alt="JevScope" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/jeiel85/jevscope">JevScope</a></b><br><sub>jeiel85 · GitHub · 2026-09-18</sub><br>面向 Jev 项目的本地优先工作台兼回归测试台：编辑 JSON state 和 choice、score、noul 问题，查看概率分布，运行 JSONL 用例，并对比两个项目定义。<br><sub>相关: <a href="https://jeiel85.github.io/jevscope/">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/allebee/pytest-jev"><img src="https://raw.githubusercontent.com/allebee/pytest-jev/main/docs/demo/demo.gif" alt="pytest-jev" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/allebee/pytest-jev">pytest-jev</a></b><br><sub>allebee · GitHub · 2026-09-21</sub><br>pytest 插件，为 LLM 应用的输出加入语义断言：关于同一段文本的多条论断在一次请求里发给 Jev，每个测试报告每条论断的概率，默认让拿不准的论断失败。<br><sub>相关: <a href="https://pypi.org/project/pytest-jev/">pypi</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/zlZayn/AI-decision-maker"><img src="https://opengraph.githubassets.com/1/zlZayn/AI-decision-maker" alt="SignalChain" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/zlZayn/AI-decision-maker">SignalChain</a></b><br><sub>zlZayn · GitHub · 2026-05-12</sub><br>数据清洗框架：Jev 或 LLM 只负责把每个 CSV 列归入 13 种字段类型代码之一、把每个数据集归入一种场景，写入操作全由本地代码完成；在这里 Jev 消耗的 token 是 LLM 的 6.6–12.7 倍。</td>
</tr>
</table>

还缺什么？[提交一个资源](https://github.com/Li-Evan/awesome-jev/issues/new/choose)。
