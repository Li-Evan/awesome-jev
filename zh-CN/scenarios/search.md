# 🔎 搜索与 RAG

[English](https://github.com/Li-Evan/awesome-jev/blob/main/scenarios/search.md) · **简体中文**

重排、检索过滤、语义搜索和知识图谱。共 86 条，按社区热度排序。

[← 返回 Awesome Jev](https://github.com/Li-Evan/awesome-jev/blob/main/README.zh-CN.md#按场景浏览)

<table>
<tr>
<td width="260" valign="top"><a href="https://x.com/Saboo_Shubham_/status/2101576462042366114"><img src="https://pbs.twimg.com/amplify_video_thumb/2101576307352203264/img/THdpZUHOSRsSoTVr.jpg" alt="语义查找（⌘F）扩展" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/Saboo_Shubham_/status/2101576462042366114">语义查找（⌘F）扩展</a></b><br><sub>Saboo_Shubham_ · X · ♥ 2.3k · 2026-09-20</sub><br>开源 Chrome 扩展，用语义匹配替代页内查找，近乎实时地高亮与你输入意思一致的段落。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/superagents-lab/jev-search"><img src="https://raw.githubusercontent.com/superagents-lab/jev-search/main/public/og-home.png" alt="jev-search" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/superagents-lab/jev-search">jev-search</a></b><br><sub>superagents-lab · GitHub · ⭐ 387 · 2026-09-17</sub><br>自然语言网页搜索，用 Choice 选择时间范围和查询词，每个来源只有通过其 Noul 才保留（需要 Search1API 密钥）。<br><sub>相关: <a href="https://jev.s1.dev">app</a> · <a href="https://jev.s1.dev">app 2</a> · <a href="https://x.com/fatwang2ai/status/2100653998378516518">demo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/venturetwins/status/2101341075684434245"><img src="https://pbs.twimg.com/amplify_video_thumb/2101339712464326656/img/A8yq5IoXQuhJAi32.jpg" alt="Zillow 自然语言搜索" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/venturetwins/status/2101341075684434245">Zillow 自然语言搜索</a></b><br><sub>venturetwins · X · ♥ 949 · 2026-09-19</sub><br>扫描数千条 Zillow 房源，按网站没有提供筛选项的属性分类，比如建筑风格、翻修状况或离高速公路的距离，用时不到 20 秒，花费 $0.18。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/volcengine/OpenViking/blob/main/openviking/models/rerank/jev_rerank.py"><img src="https://raw.githubusercontent.com/volcengine/OpenViking/main/docs/images/ov-logo.png" alt="OpenViking 重排器" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/volcengine/OpenViking/blob/main/openviking/models/rerank/jev_rerank.py">OpenViking 重排器</a></b><br><sub>volcengine · GitHub · ⭐ 38.4k 仓库 · 2026-01-05</sub><br>上下文数据库的重排提供方，一次请求中用 Noul 为每篇文档打分。<br><sub><b>Jev 用法:</b> 整理时已合并，尚未发布。</sub><br><sub>相关: <a href="https://openviking.ai">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/vectorize-io/hindsight/blob/main/hindsight-api-slim/hindsight_api/engine/cross_encoder.py"><img src="https://raw.githubusercontent.com/vectorize-io/hindsight/main/hindsight-docs/static/img/hindsight-github-banner.png" alt="Hindsight 的 Jev 重排器" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/vectorize-io/hindsight/blob/main/hindsight-api-slim/hindsight_api/engine/cross_encoder.py">Hindsight 的 Jev 重排器</a></b><br><sub>vectorize-io · GitHub · ⭐ 24.9k 仓库 · 2025-10-30</sub><br>agent 记忆系统 Hindsight 中的重排提供方：只向 Jev 问一个问题，把每个召回候选都作为选项，答案本身就是排序，一次请求完成。<br><sub><b>Jev 用法:</b> 通过 HINDSIGHT_API_RERANKER_PROVIDER=typesafe 启用（默认 jev-latest），可选择截掉不相关的尾部；已在 0.10.1 中发布。</sub><br><sub>相关: <a href="https://github.com/vectorize-io/hindsight/blob/main/hindsight-docs/blog/2026-09-21-version-0-10-1.md">docs</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/robbyczgw-cla/hermes-web-search-plus"><img src="https://raw.githubusercontent.com/robbyczgw-cla/hermes-web-search-plus/main/docs/assets/web-search-plus-v3-hero.jpg" alt="Web Search Plus 的 Jev 集成" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/robbyczgw-cla/hermes-web-search-plus">Web Search Plus 的 Jev 集成</a></b><br><sub>robbyczgw-cla · GitHub · ⭐ 414 · 2026-03-17</sub><br>Hermes agent 的多提供方搜索与页面提取插件 Web Search Plus 在受控的接入点加入了可选的 Jev 决策，默认关闭，并设有置信度阈值。<br><sub><b>Jev 用法:</b> 先跑代码；只有在可选接入点才会咨询 Jev，没有密钥时回退为原有行为。</sub><br><sub>相关: <a href="https://websearchplus.xyz">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/iannuttall/status/2100884132272181594"><img src="https://pbs.twimg.com/media/HSfWoEQWcAAalX9.jpg?name=orig" alt="keep.md 的搜索与打标签" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/iannuttall/status/2100884132272181594">keep.md 的搜索与打标签</a></b><br><sub>iannuttall · X · ♥ 303 · 2026-09-18</sub><br>在 keep.md 中测试 Cloudflare Workers 上的 Jev：搜索重排比现有混合方案快 7 倍，内容打标签比 GLM 4.7 Flash 快 50 倍，且没有失败。<br><sub>相关: <a href="https://keep.md">app</a> · <a href="https://keep.md">project</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/aaayandev/status/2102137061490794730"><img src="https://pbs.twimg.com/amplify_video_thumb/2102131502578290688/img/ygqNpGaKAhekXxH1.jpg" alt="YC 创业公司语义搜索" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/aaayandev/status/2102137061490794730">YC 创业公司语义搜索</a></b><br><sub>aaayandev · X · ♥ 230 · 2026-09-21</sub><br>覆盖 6000+ 家 Y Combinator 创业公司的搜索引擎，能在一秒内回答自由形式的查询（颜色、细分领域、竞争对手、成立年限、图片），用 Jev 构建，测试总成本 $2.7。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/lancedb/lancedb/blob/main/python/python/lancedb/rerankers/typesafe.py"><img src="https://github.com/user-attachments/assets/92dad0a2-2a37-4ce1-b783-0d1b4f30a00c" alt="LanceDB 重排器" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/lancedb/lancedb/blob/main/python/python/lancedb/rerankers/typesafe.py">LanceDB 重排器</a></b><br><sub>lancedb · GitHub · ⭐ 11.5k 仓库 · 2023-02-28</sub><br>对每个查询-文档对问一个 Noul，并存储一个可设阈值的绝对相关性概率。<br><sub><b>Jev 用法:</b> 整理时已合并，尚未发布。</sub><br><sub>相关: <a href="https://lancedb.com/docs">docs</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/noperator/siftrank"><img src="https://opengraph.githubassets.com/1/noperator/siftrank" alt="SiftRank" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/noperator/siftrank">SiftRank</a></b><br><sub>noperator · GitHub · ⭐ 202 · 2025-02-13</sub><br>通过迭代排序在大数据集中找出最相关条目的 CLI 和 agent skill，在 Chat Completions API 之外新增了 --provider jev 选项。<br><sub>相关: <a href="https://x.com/noperator/status/2101538373546484216">demo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/s3ththompson/status/2100975114753892550"><img src="https://pbs.twimg.com/amplify_video_thumb/2100974992653500416/img/7rTO_q-ntbWDGTuR.jpg" alt="实体藏书索引搜索" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/s3ththompson/status/2100975114753892550">实体藏书索引搜索</a></b><br><sub>s3ththompson · X · ♥ 171 · 2026-09-18</sub><br>搜索作者的实体藏书：在 300 毫秒 内并行检查一整本书的索引，比如把“谁发明了摄影？”指向 Niepce 条目下的第 98 页。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/VisheshBaghell/status/2100536228827496721"><img src="https://pbs.twimg.com/amplify_video_thumb/2100535993141239808/img/Q_giQHiIdU-aAvI6.jpg" alt="Upweight" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/VisheshBaghell/status/2100536228827496721">Upweight</a></b><br><sub>VisheshBaghell · X · ♥ 73 · 2026-09-17</sub><br>可用六个滑块（技术深度、争议性、实用性、AI 水文、新颖度、职业相关性）重排的 Hacker News 首页，显示每篇文章的 Jev 分数；阅读原文由 Firecrawl 完成。<br><sub><b>Jev 用法:</b> 每篇文章六个 Score 问题，在本地按滑块权重合并。</sub><br><sub>相关: <a href="https://upweight.vercel.app">app</a> · <a href="https://upweight.vercel.app">project</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/zetaalphavector/RAGElo"><img src="https://raw.githubusercontent.com/zetaalphavector/RAGElo/master/docs/images/RAGElo_logo.png" alt="RAGElo 的 Jev 评估器" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/zetaalphavector/RAGElo">RAGElo 的 Jev 评估器</a></b><br><sub>zetaalphavector · GitHub · ⭐ 131 · 2023-10-10</sub><br>基于 Elo 的 RAG agent 评测工具包，可通过 TypeSafe 或 Vercel AI Gateway 把 Jev 用作检索相关性评判和答案两两比较评估器。<br><sub><b>Jev 用法:</b> jev 评估器判断一篇文档是否会被用于该主题的报告；jev_rdnam 把期望等级保留为小数分数。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/hotchpotch/jev-reranker"><img src="https://cdn-uploads.huggingface.co/production/uploads/627c91ff4d0858f003553787/uU_-MZJAuzixqmkxGVO24.webp" alt="jev-reranker" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/hotchpotch/jev-reranker">jev-reranker</a></b><br><sub>hotchpotch · GitHub · ⭐ 10 · 2026-09-19</sub><br>Python 库，用 Jev 为检索到的文档作为答案证据的有用程度打分，在生成前重排并丢弃低于阈值的文档，并处理并发、长候选列表和重试。<br><sub>相关: <a href="https://huggingface.co/blog/hotchpotch/introducing-jev-reranker">write-up</a> · <a href="https://x.com/hotchpotch/status/2101315373366906895">demo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/zaidmukaddam/status/2100910232255992032"><img src="https://pbs.twimg.com/amplify_video_thumb/2100910214530953216/img/pZDYHLcrOl_f0pWI.jpg" alt="Cascade Search" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/zaidmukaddam/status/2100910232255992032">Cascade Search</a></b><br><sub>zaidmukaddam · X · ♥ 95 · 2026-09-18</sub><br>浏览器内搜索栏：一个 27K 参数的模型在 0.25 毫秒 内把“open bugs from sam since last week”这类查询解析成类型化过滤条件，只在拿不准的词上询问 Jev。<br><sub>相关: <a href="https://cascade.scira.ai">app</a> · <a href="https://cascade.scira.ai">project</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/byenzyme/enzyme"><img src="https://repository-images.githubusercontent.com/920398699/6e344f34-0504-4959-b6ce-49b8d6cb5c20" alt="Enzyme" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/byenzyme/enzyme">Enzyme</a></b><br><sub>byenzyme · GitHub · ⭐ 82 · 2025-01-22</sub><br>Markdown 知识库的本地优先编译步骤：其 enzyme compile 通过 OpenRouter Decisions 调用 Jev 扫描整个知识库，写出一段程序，决定 catalyst 问题从哪里学习。<br><sub>相关: <a href="https://memory.enzyme.garden">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/jexp/neo4jev"><img src="https://opengraph.githubassets.com/1/jexp/neo4jev" alt="neo4jev" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/jexp/neo4jev">neo4jev</a></b><br><sub>jexp · GitHub · ⭐ 81 · 2026-09-16</sub><br>演示：朝着一个自然语言目标在 Neo4j 图上一跳一跳地导航，由 Jev 选择沿哪条关系走，并用集束搜索保留最佳路径。<br><sub><b>Jev 用法:</b> 同一次调用里包含一个在出边关系中挑选的 Choice 和一个判断是否到达目标的 Noul，所以每一跳只需一次往返。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Ontos-AI/knowhere/blob/main/apps/worker/scripts/page_memory/eval_jev_toc_anchor_confirm.py"><img src="https://opengraph.githubassets.com/1/Ontos-AI/knowhere" alt="Knowhere 目录锚点评测" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Ontos-AI/knowhere/blob/main/apps/worker/scripts/page_memory/eval_jev_toc_anchor_confirm.py">Knowhere 目录锚点评测</a></b><br><sub>Ontos-AI · GitHub · ⭐ 3.4k 仓库 · 2026-04-30</sub><br>文档解析系统 Knowhere 中的离线评测，比较 Jev 与当前模型在 PDF 解析时确认目录起始页的表现。<br><sub><b>Jev 用法:</b> 基于缓存的页面文本，每页一个真/假 Choice；Jev 不能看截图，所以两组拿到的都是同样的文本。</sub><br><sub>相关: <a href="https://knowhereto.ai">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/neural_avb/status/2100881974780993668"><img src="https://pbs.twimg.com/amplify_video_thumb/2100879106078568449/img/nCefxS323PhF_n7f.jpg" alt="Paper Breakdown 的推荐" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/neural_avb/status/2100881974780993668">Paper Breakdown 的推荐</a></b><br><sub>neural_avb · X · ♥ 65 · 2026-09-18</sub><br>在 Paper Breakdown 基于内容和协同过滤的推荐系统之上加一层 Jev 精选，每个用户约 70 条推荐，成本 $0.0019。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/mukiwu/jev-search-mcp"><img src="https://opengraph.githubassets.com/1/mukiwu/jev-search-mcp" alt="jev-search" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/mukiwu/jev-search-mcp">jev-search</a></b><br><sub>mukiwu · GitHub · ⭐ 59 · 2026-03-23</sub><br>muki-ai-plugins 市场中的 Claude Code 插件，用 Jev 排序的结果响应 WebSearch，由 Jev 选择来源和时间窗口，失败时回退到内置工具。<br><sub>相关: <a href="https://github.com/mukiwu/muki-ai-plugins">marketplace</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/SaaiArora/status/2100807349363741132"><img src="https://pbs.twimg.com/amplify_video_thumb/2100806240406487040/img/CMyCF6BobyP4feED.jpg" alt="Replicas 中的意图感知搜索" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/SaaiArora/status/2100807349363741132">Replicas 中的意图感知搜索</a></b><br><sub>SaaiArora · X · ♥ 30 · 2026-09-18</sub><br>实验：用 Jev 驱动 Replicas 应用的全局搜索，让结果和操作贴合用户的真实意图。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/xerj-org/xerj/tree/main/benchmarks/systemone-gate"><img src="https://raw.githubusercontent.com/xerj-org/xerj/main/docs/media/demo-poster.png" alt="XERJ 的 systemone 验收闸门" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/xerj-org/xerj/tree/main/benchmarks/systemone-gate">XERJ 的 systemone 验收闸门</a></b><br><sub>xerj-org · GitHub · ⭐ 2.3k 仓库 · 2026-06-30</sub><br>本地 AI 搜索引擎 XERJ 暴露了一个兼容 Jev 的 /v1/systemone 端点，现成的 jev-reranker 客户端无需修改就能用它重排搜索索引。<br><sub><b>Jev 用法:</b> 一道验收闸门在 XERJ 节点上，对短信垃圾信息索引运行 jev-reranker 的 listwise 和 relevance 预设，无需任何补丁。</sub><br><sub>相关: <a href="https://xerj.org">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/kbhuw/jev-sift"><img src="https://opengraph.githubassets.com/1/kbhuw/jev-sift" alt="jev-sift" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/kbhuw/jev-sift">jev-sift</a></b><br><sub>kbhuw · GitHub · ⭐ 45 · 2026-09-18</sub><br>agent 插件和 MCP 工具，把一批文件、公开网页、文本或工具描述连同查询发给 Jev，返回相关性概率，让 agent 只打开值得读的条目。<br><sub>相关: <a href="https://x.com/kushbhuwalka/status/2101064922813895154">demo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/dorkitude/webctl"><img src="https://pbs.twimg.com/media/HSx-UqEaIAEjR4L.jpg?name=orig" alt="webctl" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/dorkitude/webctl">webctl</a></b><br><sub>dorkitude · GitHub · ⭐ 37 · 2026-09-20</sub><br>面向 agent 的网页搜索 CLI：查询三个搜索后端，让 Jev 针对查询和目标为每组结果打分，再对高分子集去重，让 agent 少读很多内容。<br><sub>相关: <a href="https://x.com/dorkitude/status/2102194028704092585">demo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/bolau_/status/2102127429418360895"><img src="https://pbs.twimg.com/media/HSw20LaXUAAI3w6.jpg?name=orig" alt="旧金山餐饮许可地图" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/bolau_/status/2102127429418360895">旧金山餐饮许可地图</a></b><br><sub>bolau_ · X · ♥ 32 · 2026-09-21</sub><br>旧金山每家餐饮企业的许可和卫生检查记录地图，Jev 能在几秒内回答关于这些记录的问题。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/AYi_AInotes/status/2102198099498135812"><img src="https://pbs.twimg.com/amplify_video_thumb/2101673555813453825/img/nfWWuk_nW1mtGBW2.jpg" alt="Margin" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/AYi_AInotes/status/2102198099498135812">Margin</a></b><br><sub>AYi_AInotes · X · ♥ 29 · 2026-09-22</sub><br>导入多年 X 书签后用自然语言搜索的工具，Jev 并行为每条收藏推文打分，几秒内返回按相关性排序的列表。<br><sub><b>Jev 用法:</b> 针对查询为每条收藏推文打分。</sub><br><sub>相关: <a href="https://x.com/alexchristou_/status/2101674202361221376">demo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/rodydavis/status/2101802283256463699"><img src="https://pbs.twimg.com/media/HSsZnCSaMAABhjv.jpg" alt="嵌入式数据库搭配 Jev 重排" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/rodydavis/status/2101802283256463699">嵌入式数据库搭配 Jev 重排</a></b><br><sub>rodydavis · 文章 · ♥ 27 · 2026-09-20</sub><br>架构文章：组合 SQLite、DuckDB 和 LadyBugDB 做混合候选检索，用 Jev 作重排器，目标是在一秒内给出 RAG 结果，而不是把 20 到 50 段文本发给前沿 LLM。</td>
</tr>
<tr>
<td width="260" valign="top"></td>
<td valign="top"><b><a href="https://www.reddit.com/r/AI_Agents/comments/1wkusec/building_an_internet_scanner_with_jev/">Tripwire 互联网扫描器</a></b><br><sub>Calm_Apple7505 · Reddit · ▲ 7 · 2026-09-19</sub><br>抢先体验阶段的工具，扫描 Reddit、X 和 LinkedIn 帖子，按自然语言定义的概念而非关键词进行过滤。<br><sub>相关: <a href="https://tripwire.easytech-agency.net/">app</a> · <a href="https://tripwire.easytech-agency.net">project</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/konbakuyomu/smartsearch/blob/main/src/smart_search/jev.py"><img src="https://raw.githubusercontent.com/konbakuyomu/smartsearch/main/assets/branding/smart-search.png" alt="Smart Search 的 Jev 集成" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/konbakuyomu/smartsearch/blob/main/src/smart_search/jev.py">Smart Search 的 Jev 集成</a></b><br><sub>konbakuyomu · GitHub · ⭐ 838 仓库 · 2026-05-10</sub><br>把实时网络信息带入 AI 对话的桌面应用 Smart Search 用 Jev 做类型化判断，执行逻辑和允许的动作集合则保留在代码中。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/serverpod/starguide"><img src="https://opengraph.githubassets.com/1/serverpod/starguide" alt="Starguide" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/serverpod/starguide">Starguide</a></b><br><sub>serverpod · GitHub · ⭐ 16 · 2025-05-27</sub><br>Serverpod 的文档聊天机器人：Jev 挑选能回答问题的文档和网站页面，判断其中是否包含答案以便跳过向量搜索，并评估最终回答是否解决了问题。<br><sub><b>Jev 用法:</b> 通过 jev_dart 包把页面作为 Choice 选项；两个 Noul 分别判断答案覆盖和问题是否解决。</sub><br><sub>相关: <a href="https://pub.dev/packages/jev_dart">package</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/sensahin/transcript-lens"><img src="https://opengraph.githubassets.com/1/sensahin/transcript-lens" alt="Transcript Lens" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/sensahin/transcript-lens">Transcript Lens</a></b><br><sub>sensahin · GitHub · ⭐ 16 · 2026-09-19</sub><br>带土耳其语界面的 Next.js 应用，按意思浏览 YouTube 转录稿：Jev 为每个段落分类但不改写，从中提炼出章节、关键段落和话题提及。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/owengretzinger/status/2101397416826053104"><img src="https://www.boardy.ai/opengraph-image" alt="Boardy 的匹配重排" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/owengretzinger/status/2101397416826053104">Boardy 的匹配重排</a></b><br><sub>owengretzinger · X · ♥ 15 · 2026-09-19</sub><br>AI 超级连接者 Boardy 称，Jev 已在生产环境中重排了超过 100 万次人脉匹配。<br><sub>相关: <a href="https://boardy.ai">app</a> · <a href="https://boardy.ai">project</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://news.ycombinator.com/item?id=49777691"><img src="https://www.hazumi.news/hazumi-news-og.png" alt="Hazumi News" width="240"></a></td>
<td valign="top"><b><a href="https://news.ycombinator.com/item?id=49777691">Hazumi News</a></b><br><sub>jrhey · Hacker News · ▲ 5 · 2026-09-20</sub><br>Hacker News 阅读器，用 Jev 把大型讨论串过滤到只剩值得读的评论。<br><sub>相关: <a href="https://www.hazumi.news/best">app</a> · <a href="https://hazumi.news">project</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Zabaca/lattice"><img src="https://opengraph.githubassets.com/1/Zabaca/lattice" alt="Lattice 的 Jev 重排器" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Zabaca/lattice">Lattice 的 Jev 重排器</a></b><br><sub>Zabaca · GitHub · ⭐ 15 · 2025-11-27</sub><br>本地优先的 markdown 知识库检索引擎 Lattice 中的可选重排阶段：把融合后的靠前命中一次性发给 Jev，按每条回答查询的概率打分。<br><sub>相关: <a href="https://zabaca.com/products/lattice/">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/hraness/wordcell"><img src="https://raw.githubusercontent.com/hraness/wordcell/main/assets/agent-skill.svg" alt="Wordcell" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/hraness/wordcell">Wordcell</a></b><br><sub>hraness · GitHub · ⭐ 14 · 2026-07-22</sub><br>面向编程 agent 的本地 Markdown 知识库，带可选的 Jev 重排通道；在 SciFact 上，它让 300 个查询中的 161 个把相关结果排在第一，只用精确搜索时是 101 个。<br><sub><b>Jev 用法:</b> 固定使用 jev-1.13.0，对有限窗口内的搜索候选重排；精确匹配始终排在最前，提供方失败时保留基线顺序。</sub><br><sub>相关: <a href="https://wordcell.io">app</a> · <a href="https://github.com/hraness/wordcell/blob/main/docs/reranking.md">docs</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/kentcdodds/kody/blob/main/packages/worker/src/mcp/tools/search-jev-rerank.ts"><img src="https://opengraph.githubassets.com/1/kentcdodds/kody" alt="Kody 的 Jev 搜索重排" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/kentcdodds/kody/blob/main/packages/worker/src/mcp/tools/search-jev-rerank.ts">Kody 的 Jev 搜索重排</a></b><br><sub>kentcdodds · GitHub · ⭐ 663 仓库 · 2026-09-18</sub><br>为 Kody 的 MCP 搜索增加的可选第二阶段：遇到含糊查询时扩大词法与向量的混合召回，再通过 Workers AI 用 Jev 对候选重排和过滤。<br><sub><b>Jev 用法:</b> 通过 Cloudflare AI Gateway 为每个候选问 Score 问题，保留截断点自适应调整，置信度低时回退到混合排序。</sub><br><sub>相关: <a href="https://x.com/kodykoala/status/2100943346575253515">demo</a> · <a href="https://github.com/kentcdodds/kody">repo</a> · <a href="https://kody.codes">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/marc2332/findme"><img src="https://opengraph.githubassets.com/1/marc2332/findme" alt="findme" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/marc2332/findme">findme</a></b><br><sub>marc2332 · GitHub · ⭐ 9 · 2026-09-19</sub><br>Rust CLI，根据你对某个文件或文件夹的自然语言记忆找到它：沿目录树逐层遍历，每一层都询问 Jev 哪些条目最有希望。<br><sub><b>Jev 用法:</b> 每一层发送条目名和少量元数据，保留得分最高的目录继续向下，并遵守 .gitignore。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/hev/reranker"><img src="https://opengraph.githubassets.com/1/hev/reranker" alt="hev reranker" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/hev/reranker">hev reranker</a></b><br><sub>hev · GitHub · ⭐ 9 · 2026-09-17</sub><br>一份教程加一个 90 行的 Python 封装，把 Jev 用作校准的重排器，每次调用最多处理 30 篇文档，并给出在 BEIR 候选列表上与托管和开源重排器对比的 nDCG@10 结果。<br><sub><b>Jev 用法:</b> 一次请求中每篇文档一个 Noul 相关性问题；概率既是排序键，也是剪枝阈值。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/chenmingtang830/jevgraph"><img src="https://raw.githubusercontent.com/chenmingtang830/jevgraph/main/docs/assets/jevgraph-overview.svg" alt="JevGraph" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/chenmingtang830/jevgraph">JevGraph</a></b><br><sub>chenmingtang830 · GitHub · ⭐ 9 · 2026-09-20</sub><br>文档转图谱的管线，在本地解析 PDF、DOCX、PPTX 或文本，对每个候选实体对向 Jev 问一个封闭集合的关系问题，导出带概率和页面证据的边。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/magnus919/SlopSearX"><img src="https://opengraph.githubassets.com/1/magnus919/SlopSearX" alt="SlopSearX" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/magnus919/SlopSearX">SlopSearX</a></b><br><sub>magnus919 · GitHub · ⭐ 9 · 2026-06-09</sub><br>面向 AI agent 的无状态元搜索引擎，可直接替换 SearXNG，会询问 Jev 哪些专业引擎能为每个查询补充独特的证据。<br><sub><b>Jev 用法:</b> 所有达到 0.65 阈值的专业引擎都会加入，数量不设上限；显式指定范围时从不调用 Jev，失败时保留确定性路由。</sub><br><sub>相关: <a href="https://github.com/magnus919/SlopSearX/blob/main/docs/JEV_ROUTING.md">docs</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/zaidmukaddam/cascade-search"><img src="https://raw.githubusercontent.com/zaidmukaddam/cascade-search/main/eval/results/m2.png" alt="cascade-search" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/zaidmukaddam/cascade-search">cascade-search</a></b><br><sub>zaidmukaddam · GitHub · ⭐ 8 · 2026-09-17</sub><br>浏览器内的搜索查询解析器：一个 27,193 参数的模型在约 0.25 毫秒 内为每个词标注角色和校准置信度，只有不确定的词才升级给 Jev。<br><sub><b>Jev 用法:</b> 两层都输出到同一个编译器，所以无论哪一层作答，应用拿到的都是同样的类型化过滤条件；升级功能由单独的 cascade-search-jev 包提供。</sub><br><sub>相关: <a href="https://cascade.scira.ai">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/PixelML/av"><img src="https://opengraph.githubassets.com/1/PixelML/av" alt="av" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/PixelML/av">av</a></b><br><sub>PixelML · GitHub · ⭐ 7 · 2026-02-14</sub><br>面向 agent 的视频记忆 CLI，为字幕和转录建立索引，用于搜索和问答；配置 TypeSafe 密钥后，<code>av ask</code> 会让 Jev 过滤并排序检索到的场景，并检查答案是否有依据。<br><sub><b>Jev 用法:</b> 排序时用每条命中的相关性概率乘以检索分数，另用一个 Noul 判断答案是否有依据；Jev 失败时回退到原始检索结果。</sub><br><sub>相关: <a href="https://agentic.video">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/larguesa/jev-search"><img src="https://opengraph.githubassets.com/1/larguesa/jev-search" alt="jev-search" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/larguesa/jev-search">jev-search</a></b><br><sub>larguesa · GitHub · ⭐ 6 · 2026-09-19</sub><br>零依赖的 Python CLI，通过 OpenRouter 上的 Jev 对文档、笔记和知识库做逐行语义搜索，用来补充 agent 的精确关键词搜索。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/tornikegomareli/FindSFSymbols"><img src="https://opengraph.githubassets.com/1/tornikegomareli/FindSFSymbols" alt="FindSFSymbols" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/tornikegomareli/FindSFSymbols">FindSFSymbols</a></b><br><sub>tornikegomareli · GitHub · ⭐ 5 · 2026-09-20</sub><br>用简单描述查找 SF Symbols 的 Mac 应用：设备端词向量先筛出 48 个符号，再由 Jev 在一次请求中回答 48 个是/否问题，分数驱动一个物理堆叠效果，匹配度高的会浮上来。<br><sub><b>Jev 用法:</b> 一次请求中为每个入围符号问一个 Noul；没有密钥时应用只使用设备端匹配。</sub><br><sub>相关: <a href="https://tornikegomareli.github.io/FindSFSymbols/">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/danielwanwx/research-engine"><img src="https://opengraph.githubassets.com/1/danielwanwx/research-engine" alt="Research Engine" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/danielwanwx/research-engine">Research Engine</a></b><br><sub>danielwanwx · GitHub · ⭐ 5 · 2026-06-28</sub><br>面向 AI agent、证据优先的研究运行时，把问题路由到研究包和只读连接器；可选的 <code>jev-triage</code> 命令会询问 Jev 已收集的公开证据行有多相关。<br><sub><b>Jev 用法:</b> 每个请求最多八条白名单内的公开数据行，获得仅供参考的 Noul 相关性概率；Jev 从不增删证据。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/robbyczgw-cla/web-search-plus-mcp"><img src="https://raw.githubusercontent.com/robbyczgw-cla/web-search-plus-mcp/main/docs/assets/web-search-plus-logo.png" alt="web-search-plus-mcp" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/robbyczgw-cla/web-search-plus-mcp">web-search-plus-mcp</a></b><br><sub>robbyczgw-cla · GitHub · ⭐ 5 · 2026-03-13</sub><br>为 agent 提供网页搜索的 MCP 服务器，接入 15 个搜索提供方和 9 个提取提供方，并保留原始来源；可选且默认关闭的 Jev 会确认新闻类搜索、为提取的正文打分并补全缺失的语言信息。<br><sub>相关: <a href="https://websearchplus.xyz">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/colophon-group/jobseek/blob/main/apps/web/src/lib/ai-filter/jev-client.ts"><img src="https://opengraph.githubassets.com/1/colophon-group/jobseek" alt="Job Seek 的 Jev AI 筛选" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/colophon-group/jobseek/blob/main/apps/web/src/lib/ai-filter/jev-client.ts">Job Seek 的 Jev AI 筛选</a></b><br><sub>colophon-group · GitHub · ⭐ 199 仓库 · 2026-02-18</sub><br>基于 5,300+ 个招聘网站构建的开源求职搜索，新增了 Jev AI 筛选，按用户条件把每个职位归为接受或拒绝。<br><sub><b>Jev 用法:</b> 批量请求中每个职位一个 Choice，能抵御职位描述里注入的文本。</sub><br><sub>相关: <a href="https://jseek.co/">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/keltokhy/jselect"><img src="https://opengraph.githubassets.com/1/keltokhy/jselect" alt="jselect" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/keltokhy/jselect">jselect</a></b><br><sub>keltokhy · GitHub · ⭐ 3 · 2026-09-19</sub><br>Python 上下文选择器，询问 Jev 你的文件或记录中每段文字是否是完成某项任务的有用证据，再在 token 预算内挑出多样的原文段落并附上来源链接。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/WiktorB2004/llama-index-jev"><img src="https://opengraph.githubassets.com/1/WiktorB2004/llama-index-jev" alt="llama-index-jev" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/WiktorB2004/llama-index-jev">llama-index-jev</a></b><br><sub>WiktorB2004 · GitHub · ⭐ 3 · 2026-09-18</sub><br>LlamaIndex 的重排器和路由器；重排把 NFCorpus 上的 nDCG@5 从 0.340 提升到 0.396。<br><sub>相关: <a href="https://wiktorb2004.github.io/llama-index-jev">docs</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/kenn-io/docbank/tree/main/document/typesafe"><img src="https://opengraph.githubassets.com/1/kenn-io/docbank" alt="docbank 的 Jev 重排" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/kenn-io/docbank/tree/main/document/typesafe">docbank 的 Jev 重排</a></b><br><sub>kenn-io · GitHub · ⭐ 101 仓库 · 2026-07-07</sub><br>面向人和 agent 的本地优先文档库，新增了 TypeSafe Jev 重排提供方，用于在文档名和提取出的文本上搜索。<br><sub>相关: <a href="https://docbank.ai">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/shinpr/jev-reranker"><img src="https://raw.githubusercontent.com/shinpr/jev-reranker/main/assets/banner.jpg" alt="Jev Reranker" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/shinpr/jev-reranker">Jev Reranker</a></b><br><sub>shinpr · GitHub · ⭐ 2 · 2026-09-20</sub><br>通过 npm 安装的 Rust CLI，从 stdin 读取 JSON 数组形式的搜索结果，用 Jev 对其重排、剔除没有可用证据的候选，或为你的 LLM 抽取与查询相关的段落。<br><sub>相关: <a href="https://norsica.jp/blog/what-retrieval-still-hasnt-decided">article</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/abhishekmamdapure/jev-information-extraction"><img src="https://opengraph.githubassets.com/1/abhishekmamdapure/jev-information-extraction" alt="jev-information-extraction" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/abhishekmamdapure/jev-information-extraction">jev-information-extraction</a></b><br><sub>abhishekmamdapure · GitHub · ⭐ 2 · 2026-09-20</sub><br>上传一份 PDF，然后提问，比如 GST 号码或发票总额；Jev 对能回答每个问题的提取文本分块排序，应用显示每个匹配项、其概率和在页面上的位置。<br><sub>相关: <a href="https://jev-information-extraction-fibby-prod-telegram.up.railway.app/">app</a> · <a href="https://jev-information-extraction-fibby-prod-telegram.up.railway.app">app 2</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/gigabit_million/status/2102200033307422821"><img src="https://pbs.twimg.com/amplify_video_thumb/2101941990254632960/img/gx4NHU9mxvfHKA3y.jpg" alt="模糊内容搜索" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/gigabit_million/status/2102200033307422821">模糊内容搜索</a></b><br><sub>gigabit_million · X · ♥ 1 · 2026-09-22</sub><br>作者为自己发布过的内容做的搜索站：Jev 针对模糊查询为每条内容打分并显示分数，排序依据一目了然。<br><sub><b>Jev 用法:</b> 针对自由文本查询，为每条内容给出一个 Score。</sub><br><sub>相关: <a href="https://gigabit-search.gigabitmillion-games.workers.dev/">app</a> · <a href="https://gigabit-search.gigabitmillion-games.workers.dev">project</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/tedliou/decision-model-playground"><img src="https://opengraph.githubassets.com/1/tedliou/decision-model-playground" alt="decision-model-playground" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/tedliou/decision-model-playground">decision-model-playground</a></b><br><sub>tedliou · GitHub · ⭐ 1 · 2026-09-19</sub><br>本地浏览器试验场：由 Laya 或 Jev 为一个问题挑选最匹配的 vervecode.dev 文章，展示每个选项的原始概率、一个“无匹配”选项，以及加载和推理耗时。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/raahelpie/hn-for-me"><img src="https://external-preview.redd.it/cGZkd252YzFheXFoMeTpqXMSfpCE94rmVlGr8pZ7_z3kfZQqelwwzt-Id7ds.png?format=pjpg&amp;auto=webp&amp;s=e90f071fd20387c7898145a4feed6ca91dc9360f" alt="Hacker News For Me" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/raahelpie/hn-for-me">Hacker News For Me</a></b><br><sub>raahelpie · GitHub · ⭐ 1 · 2026-09-20</sub><br>个人 Hacker News 阅读器，按你保存的兴趣筛选新文章，只在 HN 风格的信息流中显示相关内容。<br><sub><b>Jev 用法:</b> 默认运行在 Codiv 的 OpenJev 模型上，TypeSafe Jev 可作为可切换的提供方；标题阈值 0.7，文章相关性阈值 0.9。</sub><br><sub>相关: <a href="https://news.ycombinator.com/item?id=49788260">demo</a> · <a href="https://www.reddit.com/r/SideProject/comments/1wmruft/hn_for_me_hacker_news_stories_curated_by_jev/">discussion</a> · <a href="https://x.com/RaahelSaidWhat/status/2102162969656475973">demo 2</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/ajanm007/jevrag"><img src="https://opengraph.githubassets.com/1/ajanm007/jevrag" alt="JevRAG" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/ajanm007/jevrag">JevRAG</a></b><br><sub>ajanm007 · GitHub · ⭐ 1 · 2026-09-20</sub><br>RAG 管线的决策层，用校准的闸门替换硬编码阈值，涵盖证据是否充分、分块边界、上下文选择、弃答和缓存可信度，在 HotpotQA 上评测。<br><sub><b>Jev 用法:</b> Jev 是这五个决策原语背后第一个可替换的后端。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/kylemclaren/jevsearch"><img src="https://opengraph.githubassets.com/1/kylemclaren/jevsearch" alt="jevsearch" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/kylemclaren/jevsearch">jevsearch</a></b><br><sub>kylemclaren · GitHub · ⭐ 1 · 2026-09-21</sub><br>可直接接入的 shadcn/ui 站内搜索组件：第一次按键就显示关键词命中，稍后用 Jev 按访客意图重排，调用失败时保留关键词顺序。<br><sub>相关: <a href="https://jevsearch.fly.dev">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/avshalomd/longjev"><img src="https://raw.githubusercontent.com/avshalomd/longjev/main/results/social/longjev_pipeline.png" alt="longjev" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/avshalomd/longjev">longjev</a></b><br><sub>avshalomd · GitHub · ⭐ 1 · 2026-09-18</sub><br>实验性封装，调用方式与 Jev 相同，都是 system_one(state, questions)，能接受超过 Jev 32K token 上限的输入：先给每个分块打分，保留最好的几块，再就剩下的内容询问 Jev。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/komikat/psearch"><img src="https://opengraph.githubassets.com/1/komikat/psearch" alt="psearch" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/komikat/psearch">psearch</a></b><br><sub>komikat · GitHub · ⭐ 1 · 2026-09-17</sub><br>面向终端和 agent 的网页搜索 CLI 与 MCP 服务器：Parallel Search 提供种子页面，本地 Chromium 并发抓取，Jev 评估证据并挑选链接加入广度优先队列。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/micahchoo/qualitative-query"><img src="https://raw.githubusercontent.com/micahchoo/qualitative-query/main/docs/img/query-builder.png" alt="Qualitative Query" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/micahchoo/qualitative-query">Qualitative Query</a></b><br><sub>micahchoo · GitHub · ⭐ 1 · 2026-09-19</sub><br>Obsidian 插件，用笔记中的原文段落回答你保存的问题，再把它们存成一篇链接回来源的笔记，不生成答案。<br><sub><b>Jev 用法:</b> 本地搜索找出候选段落，Jev 评估其中哪些真正回答了问题。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/iAmAustinPiazza/status/2102112514846740749"><img src="https://pbs.twimg.com/amplify_video_thumb/2102112331350102016/img/G-DKU2luzlCVeboq.jpg" alt="语义物体筛选" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/iAmAustinPiazza/status/2102112514846740749">语义物体筛选</a></b><br><sub>iAmAustinPiazza · X · ♥ 1 · 2026-09-21</sub><br>小型交互演示：输入“冬天能穿的东西”这类短语，Jev 就从屏幕上挑出匹配的物体。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Zafer-Liu/book-learning/blob/main/study/jev_gate.py"><img src="https://opengraph.githubassets.com/1/Zafer-Liu/book-learning" alt="Book Learning 的 Jev 检索闸门" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Zafer-Liu/book-learning/blob/main/study/jev_gate.py">Book Learning 的 Jev 检索闸门</a></b><br><sub>Zafer-Liu · GitHub · ⭐ 43 仓库 · 2026-04-23</sub><br>自托管教材 RAG 学习助手 BOOKNOTE 中的检索闸门：在融合后的候选分块进入回答之前，Jev 为每块打相关性分并筛查提示词注入，出错时退回未经过滤的结果。<br><sub><b>Jev 用法:</b> 每个查询一次扇出调用，每个分块一个 0-3 相关性 Score 和一个注入 Noul；保留相关性 &gt;= 2.0 且注入 &lt; 0.5 的分块。</sub><br><sub>相关: <a href="https://github.com/Zafer-Liu/book-learning">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/snaga/status/2101901648184643707"><img src="https://pbs.twimg.com/media/HSt0LTabQAAACdr.jpg?name=orig" alt="Hacker News 个人推荐器" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/snaga/status/2101901648184643707">Hacker News 个人推荐器</a></b><br><sub>snaga · X · ▶ 138 · 2026-09-21</sub><br>实验：每天早上让 Jev 挑出 Hacker News 首页中符合作者兴趣的文章，组合判断的设计写在一个 gist 里。<br><sub>相关: <a href="https://gist.github.com/snaga/12c62ad587d59e4817e00d3ec1846f47">gist</a> · <a href="https://gist.github.com/snaga/12c62ad587d59e4817e00d3ec1846f47">project</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Chia1104/chia1104.dev/blob/develop/packages/ai/src/rerank/jev.ts"><img src="https://repository-images.githubusercontent.com/485318015/26c450f3-6246-4b7d-b8a5-7a658a79989e" alt="chia1104.dev 的 Jev 重排器" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Chia1104/chia1104.dev/blob/develop/packages/ai/src/rerank/jev.ts">chia1104.dev 的 Jev 重排器</a></b><br><sub>Chia1104 · GitHub · ⭐ 32 仓库 · 2022-04-25</sub><br>个人网站与 CMS monorepo chia1104.dev 中的搜索重排器，每个查询只调用一次 Jev：一个在候选文章中挑选的 Choice，加一个判断是否有候选真正回答了查询的 Noul，支持跨语言。<br><sub><b>Jev 用法:</b> Choice 选出最佳候选 id；由于 Choice 的概率总和恒为 1，需要 Noul 把真正的答案与最接近但无关的命中区分开。</sub><br><sub>相关: <a href="https://chia1104.dev">app</a> · <a href="https://github.com/Chia1104/chia1104.dev">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/jreyesdev/status/2102218598668488983"><img src="https://pbs.twimg.com/media/HSyURXUaUAEVMKX.jpg?name=orig" alt="不调用 LLM 的 Sanity 内容 agent" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/jreyesdev/status/2102218598668488983">不调用 LLM 的 Sanity 内容 agent</a></b><br><sub>jreyesdev · X · ▶ 60 · 2026-09-22</sub><br>Jev 搭配 Sanity CMS 的演示：答案在入库时就预先写好，agent 只需选择答案，能跳过检索时就跳过，不到一秒即可响应，而不是 4 秒以上。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/baekenough/second-brain/tree/main/internal/jev"><img src="https://raw.githubusercontent.com/baekenough/second-brain/main/docs/diagrams/01-system-runtime-topology.png" alt="second-brain 的 Jev 分类器" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/baekenough/second-brain/tree/main/internal/jev">second-brain 的 Jev 分类器</a></b><br><sub>baekenough · GitHub · ⭐ 15 仓库 · 2026-04-14</sub><br>由 LLM 整理、覆盖 Slack、GitHub、Drive 和个人消息的私人搜索引擎 second-brain 中的入库分类器：让 Jev 为每条短信、Gmail 邮件或通话转录分配一个分段和一个留存分数。<br><sub><b>Jev 用法:</b> 每个文档一个分段 Choice 和一个留存 Score；请求和响应内容从不写入日志。</sub><br><sub>相关: <a href="https://github.com/baekenough/second-brain">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/jonnyparris/dodo/blob/main/src/browser/web-fetch.ts"><img src="https://raw.githubusercontent.com/jonnyparris/dodo/main/assets/dodo.svg" alt="Dodo 的 Jev 网页工具" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/jonnyparris/dodo/blob/main/src/browser/web-fetch.ts">Dodo 的 Jev 网页工具</a></b><br><sub>jonnyparris · GitHub · ⭐ 13 仓库 · 2026-03-28</sub><br>运行在 Cloudflare Workers 上的编程 agent，其只读网页工具用 Jev 在抓取前给候选 URL 排序，并检查抓取到的页面是否回答了查询。<br><sub><b>Jev 用法:</b> browser_triage 只凭元数据给 URL 排序；browser_markdown 返回一个校准的 Noul 判定，让 agent 决定是否继续浏览。</sub><br><sub>相关: <a href="https://github.com/jonnyparris/dodo">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Mr-remon219/search-boost/tree/master/lib/jev"><img src="https://opengraph.githubassets.com/1/Mr-remon219/search-boost" alt="SearchBoost 的 Jev 证据循环" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Mr-remon219/search-boost/tree/master/lib/jev">SearchBoost 的 Jev 证据循环</a></b><br><sub>Mr-remon219 · GitHub · ⭐ 9 仓库 · 2026-08-17</sub><br>面向编程 agent 的多引擎网页搜索与证据综合工具（MCP 服务器、Pi 扩展、DeepSeek Harness 套件），带一个实验性的 adaptive_search 循环，用 Jev 分批研究目标。<br><sub>相关: <a href="https://github.com/Mr-remon219/search-boost">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/jialuohu/codex-toolbox/tree/main/plugins/typesafe-tools"><img src="https://opengraph.githubassets.com/1/jialuohu/codex-toolbox" alt="typesafe-tools Codex 插件" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/jialuohu/codex-toolbox/tree/main/plugins/typesafe-tools">typesafe-tools Codex 插件</a></b><br><sub>jialuohu · GitHub · ⭐ 9 仓库 · 2026-07-02</sub><br>Codex 插件，含一个 MCP 服务器和 skill，用有限次数的 Jev 评估给公开研究段落排序，并检查来源是否支持某个论断，受支出上限和试点闸门约束。<br><sub>相关: <a href="https://github.com/jialuohu/codex-toolbox">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/dabit3/macos-experiments/tree/main/turbo-rerank"><img src="https://raw.githubusercontent.com/dabit3/macos-experiments/main/turbo-rerank/screenshots/turbo-rerank-home.jpg" alt="Turbo Rerank" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/dabit3/macos-experiments/tree/main/turbo-rerank">Turbo Rerank</a></b><br><sub>dabit3 · GitHub · ⭐ 8 仓库 · 2026-09-07</sub><br>搜索工作区演示：用一次约 170 毫秒 的 Jev 请求重排 50 个候选，在 40 个查询的标注基准上把 top-1 准确率从 50% 提到 100%。<br><sub><b>Jev 用法:</b> 一次请求针对查询评判每个候选，并检查答案是否存在，也可拆成并行批次。</sub><br><sub>相关: <a href="https://github.com/dabit3/macos-experiments">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/serpapi/tutorials/tree/master/python_projects/jev-serpapi-fact-checker"><img src="https://opengraph.githubassets.com/1/serpapi/tutorials" alt="Jev 与 SerpApi 事实核查器" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/serpapi/tutorials/tree/master/python_projects/jev-serpapi-fact-checker">Jev 与 SerpApi 事实核查器</a></b><br><sub>serpapi · GitHub · ⭐ 6 仓库 · 2025-09-05</sub><br>SerpApi 出的教程 CLI：用最多五条 Google 自然搜索摘要检验一个陈述或是/否问题，并通过 OpenRouter 的 Decisions API 从 Jev 获得结论。<br><sub>相关: <a href="https://github.com/serpapi/tutorials">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/The-40-Thieves/obsidian-tc/blob/main/packages/server/src/gateway/typesafe.ts"><img src="https://opengraph.githubassets.com/1/The-40-Thieves/obsidian-tc" alt="obsidian-tc 的 Jev 引用评判" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/The-40-Thieves/obsidian-tc/blob/main/packages/server/src/gateway/typesafe.ts">obsidian-tc 的 Jev 引用评判</a></b><br><sub>The-40-Thieves · GitHub · ⭐ 5 仓库 · 2026-05-18</sub><br>带融合检索和笔记库记忆的受治理 Obsidian MCP 服务器 obsidian-tc 中的可选 Jev 评判提供方，只用于判断笔记之间推断出的引用是否成立。<br><sub><b>Jev 用法:</b> 每条引用一个带真/假标准的 Noul，固定到带版本号的模型，重试次数有上限。</sub><br><sub>相关: <a href="https://github.com/The-40-Thieves/obsidian-tc">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Aias/pattern-languages/blob/master/src/lib/pattern-search.ts"><img src="https://opengraph.githubassets.com/1/Aias/pattern-languages" alt="Patterns of Design 搜索" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Aias/pattern-languages/blob/master/src/lib/pattern-search.ts">Patterns of Design 搜索</a></b><br><sub>Aias · GitHub · ⭐ 5 仓库 · 2019-09-05</sub><br>模式语言网站 patternsof.design 上的搜索：Jev 评估每个设计模式对用户想构建的东西能提供多少实际指导，无论是直接适用还是类比借鉴。<br><sub><b>Jev 用法:</b> 针对查询为每个模式给一个 Score，每个请求 64 个模式，以 0.5 的匹配概率为切分点。</sub><br><sub>相关: <a href="https://patternsof.design">app</a> · <a href="https://github.com/Aias/pattern-languages">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/jokull/ensk"><img src="https://opengraph.githubassets.com/1/jokull/ensk" alt="ensk" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/jokull/ensk">ensk</a></b><br><sub>jokull · GitHub · 2026-09-18</sub><br>运行在 Cloudflare Workers 上的英语-冰岛语词典，结合 D1 全文搜索和 Vectorize 语义召回，再通过 Workers AI 调用 Jev 重排候选短名单，并判断是否有词条真正匹配。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Eliovp-BV/Jev-Radar"><img src="https://raw.githubusercontent.com/Eliovp-BV/Jev-Radar/main/docs/media/radar-demo.gif" alt="Jev Radar" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Eliovp-BV/Jev-Radar">Jev Radar</a></b><br><sub>Eliovp-BV · GitHub · 2026-09-19</sub><br>本地研究工作区：Jev 引导基于公开来源的调查，在各条记录上问同一组研究问题，构建一份与证据关联的对比，每个决策都可检查。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/jh1373/jev-search"><img src="https://opengraph.githubassets.com/1/jh1373/jev-search" alt="Jev Search for Obsidian" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/jh1373/jev-search">Jev Search for Obsidian</a></b><br><sub>jh1373 · GitHub · 2026-09-18</sub><br>Obsidian 插件，先用 BM25 离线搜索笔记库，只有在你批准要发送的内容后，才用 Jev 重排靠前的结果。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/sudeshkar/jev-corrective-rag"><img src="https://opengraph.githubassets.com/1/sudeshkar/jev-corrective-rag" alt="jev-corrective-rag" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/sudeshkar/jev-corrective-rag">jev-corrective-rag</a></b><br><sub>sudeshkar · GitHub · 2026-09-20</sub><br>Corrective RAG 实现：是否检索、分块评级和依据检查这几道闸门都用 Jev 调用代替 LLM 裁判，平均每个查询 0.75 次 LLM 调用，LLM 调用次数少 7 倍，p50 延迟低 4 倍。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/kierandotai/jev-scout"><img src="https://opengraph.githubassets.com/1/kierandotai/jev-scout" alt="jev-scout" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/kierandotai/jev-scout">jev-scout</a></b><br><sub>kierandotai · GitHub · 2026-09-19</sub><br>面向 agent 网络调研的 MCP 服务器，让 Jev 评判每个查询、搜索结果和抓取页面的相关性与可信度，带会话预算、防 SSRF 的抓取和实时决策仪表盘。<br><sub><b>Jev 用法:</b> 每条搜索结果一次调用（相关性、可信度、是否值得抓取），每个抓取页面一次调用（是否已回答、内容类别、操纵风险）；一项 25 条人工标注的研究报告相关性 88%、可信度 96%。</sub><br><sub>相关: <a href="https://github.com/kierandotai/jev-scout/blob/main/docs/accuracy/2026-09-19-jev-golden-set-study.md">study</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/ArielBubis/Jevflix"><img src="https://opengraph.githubassets.com/1/ArielBubis/Jevflix" alt="Jevflix" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/ArielBubis/Jevflix">Jevflix</a></b><br><sub>ArielBubis · GitHub · 2026-09-21</sub><br>电影推荐器：先用 FAISS 和 BM25 把 4,800 部电影缩到一份短名单，再让 Jev 解析你的限制条件并选出一部，依据其置信度决定立即回答还是追问。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://www.theunwindai.com/p/get-started-with-jev-for-free"><img src="https://beehiiv-images-production.s3.amazonaws.com/uploads/asset/file/9ff9d5e8-2f74-4ee2-b95f-2bacfdda1e77/ChatGPT_Image_Sep_20__2026__01_04_29_AM.png?t=1789891484" alt="Needle" width="240"></a></td>
<td valign="top"><b><a href="https://www.theunwindai.com/p/get-started-with-jev-for-free">Needle</a></b><br><sub>The Unwind AI (Shubham Saboo, Gargi Gupta) · 文章 · 2026-09-20</sub><br>开源 Chrome 扩展，按意思而不是字面搜索：提一个问题，Jev 为页面中的句子打分并高亮与你意图匹配的那些，不生成答案。<br><sub><b>Jev 用法:</b> Jev 针对查询为每个原文句子打分，得分最高的段落直接在原处高亮。</sub><br><sub>相关: <a href="https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/advanced_llm_apps/needle">repo</a> · <a href="https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/advanced_llm_apps/needle">project</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Shifros/Search-Function-Test"><img src="https://opengraph.githubassets.com/1/Shifros/Search-Function-Test" alt="Search-Function-Test" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Shifros/Search-Function-Test">Search-Function-Test</a></b><br><sub>Shifros · GitHub · 2026-09-17</sub><br>对话式搜索原型，面向一个有 825 篇澳大利亚企业注册文章的问答网站：Jev 在四个分片上用 Choice 选出最能回答查询的文章，或选择“都不是”。<br><sub>相关: <a href="https://search-function-test.vercel.app">app</a> · <a href="https://search-function-test.vercel.app">app 2</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/liou666/senseek"><img src="https://raw.githubusercontent.com/liou666/senseek/main/assets/senseek/senseek-logo.svg" alt="Senseek" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/liou666/senseek">Senseek</a></b><br><sub>liou666 · GitHub · 2026-09-20</sub><br>浏览器扩展，在类似 Ctrl+F 的输入框里按意思搜索你正在读的页面，并跳转到排好序的段落；使用你自己的 Jev API 密钥，无需后端。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/tylergibbs1/sift"><img src="https://opengraph.githubassets.com/1/tylergibbs1/sift" alt="Sift" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/tylergibbs1/sift">Sift</a></b><br><sub>tylergibbs1 · GitHub · 2026-09-17</sub><br>Chrome 扩展，重排 Google 搜索结果，让真正的答案浮到顶部，把销售页和 SEO 凑数内容折叠起来。<br><sub><b>Jev 用法:</b> 每条结果一次并行调用，含四个 Noul（是否回答查询、是否推广、是否 SEO 凑数、是否讨论）和一个深度 Score，合并成加权排名。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/TrainLCD/Functions/blob/dev/src/agent/rerank.ts"><img src="https://opengraph.githubassets.com/1/TrainLCD/Functions" alt="TrainLCD 的 Jev 支持" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/TrainLCD/Functions/blob/dev/src/agent/rerank.ts">TrainLCD 的 Jev 支持</a></b><br><sub>TrainLCD · GitHub · 2026-09-17</sub><br>交通应用 TrainLCD 背后 Cloudflare Worker 中的 Jev 集成：每个候选一个 Noul，为其 AI 聊天推荐的车站重排；另有一个模块按垃圾信息、类别和优先级分诊用户反馈。<br><sub>相关: <a href="https://github.com/TrainLCD/Functions/pull/33">pr</a> · <a href="https://github.com/TrainLCD/Functions">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/TyrellD1/typesafe-ai_smoke-test"><img src="https://opengraph.githubassets.com/1/TyrellD1/typesafe-ai_smoke-test" alt="typesafe-ai_smoke-test" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/TyrellD1/typesafe-ai_smoke-test">typesafe-ai_smoke-test</a></b><br><sub>TyrellD1 · GitHub · 2026-09-17</sub><br>小型路由器：对每条提示词向 Jev 问两个是/否问题，把它发往工作库、生活库或两者；附带 30 个用例的手写评测，30 个全部路由正确。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://yesno.coderai.dev"><img src="https://yesno.coderai.dev/og-image.png" alt="Yes / No" width="240"></a></td>
<td valign="top"><b><a href="https://yesno.coderai.dev">Yes / No</a></b><br><sub>Coder AI · 应用</sub><br>免费、无需注册的工具，用 Jev 的一个 Noul 以“是”“否”或“也许”回答任何问题，需要最新事实时会接入实时网页搜索。</td>
</tr>
</table>

还缺什么？[提交一个资源](https://github.com/Li-Evan/awesome-jev/issues/new/choose)。
