# 📚 学习资料: 评测与案例

[English](https://github.com/Li-Evan/awesome-jev/blob/main/pages/learn-benchmarks.md) · **简体中文**

官方文档和 cookbook，以及社区里最好的教程、分析、评测和演讲。共 173 条，按社区热度排序。

[← 返回 Awesome Jev](https://github.com/Li-Evan/awesome-jev/blob/main/README.zh-CN.md#评测与案例)

[官方文档](https://github.com/Li-Evan/awesome-jev/blob/main/zh-CN/pages/learn-official-docs.md) (15) · [官方 SDK 与工具](https://github.com/Li-Evan/awesome-jev/blob/main/zh-CN/pages/learn-official-tools.md) (3) · [官方公告](https://github.com/Li-Evan/awesome-jev/blob/main/zh-CN/pages/learn-announcements.md) (2) · [设计模式](https://github.com/Li-Evan/awesome-jev/blob/main/zh-CN/pages/learn-patterns.md) (4) · [官方 Cookbook](https://github.com/Li-Evan/awesome-jev/blob/main/zh-CN/pages/learn-cookbooks.md) (18) · [示例与 Skill](https://github.com/Li-Evan/awesome-jev/blob/main/zh-CN/pages/learn-examples.md) (74) · [教程](https://github.com/Li-Evan/awesome-jev/blob/main/zh-CN/pages/learn-guides.md) (76) · [技巧与分析](https://github.com/Li-Evan/awesome-jev/blob/main/zh-CN/pages/learn-techniques.md) (103) · **评测与案例** · [视频与演讲](https://github.com/Li-Evan/awesome-jev/blob/main/zh-CN/pages/learn-videos.md) (178) · [社区讨论](https://github.com/Li-Evan/awesome-jev/blob/main/zh-CN/pages/learn-discussions.md) (20)

<table>
<tr>
<td width="260" valign="top"><a href="https://github.com/NousResearch/hermes-agent/blob/main/evals/compaction/results/SCORECARD-2026-09-19-jev.md"><img src="https://raw.githubusercontent.com/NousResearch/hermes-agent/main/assets/banner.png" alt="Hermes Agent 上下文压缩成绩单" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/NousResearch/hermes-agent/blob/main/evals/compaction/results/SCORECARD-2026-09-19-jev.md">Hermes Agent 上下文压缩成绩单</a></b><br><sub>NousResearch · GitHub · ⭐ 247.9k 仓库 · 2025-07-22</sub><br>把一个基于 Jev 的上下文压缩插件与 Hermes 自带的压缩器对比，结论是不推荐：每次压缩便宜得多也快得多，但保留的上下文多了一倍，对工具结果的排序也不比按时间远近排更好。<br><sub><b>Jev 用法:</b> Jev 组负责在压缩时给要保留的历史和工具结果排序；成绩单将其与 Hermes 内置压缩器对比。</sub><br><sub>相关: <a href="https://x.com/Teknium/status/2101398453578555898">demo</a> · <a href="https://hermes-agent.nousresearch.com">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://www.langchain.com/blog/jev-agent-evals-langsmith"><img src="https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/6aae04c2c9a23c30549b7035_jev-judge-hero-dark-2400x1260.png" alt="Jev 能成为更好的 agent 评估器吗？" width="240"></a></td>
<td valign="top"><b><a href="https://www.langchain.com/blog/jev-agent-evals-langsmith">Jev 能成为更好的 agent 评估器吗？</a></b><br><sub>LangChain · 文章 · ♥ 2.9k · 2026-09-20</sub><br>LangChain 在 LangSmith 中测试把 Jev 当作 agent 评测的评判器，与 LLM 评判器比较准确率、可重复性、延迟和成本。<br><sub>相关: <a href="https://x.com/LangChain/status/2101454284927959080">demo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://webmcp.com/benchmark"><img src="https://webmcp.com/blog/img/windtunnel-model-comparison-light.png" alt="WindTunnel" width="240"></a></td>
<td valign="top"><b><a href="https://webmcp.com/benchmark">WindTunnel</a></b><br><sub>Idan Levin (webmcp.com) · 文章 · ♥ 2.1k</sub><br>WebMCP 的浏览器 agent 基准，在 8 个真实网站的 49 个任务上测试 21 种配置，Jev + Mercury 2.5 综合得分第一，解出 49/49 个任务，每个任务的中位成本为 $0.0011。<br><sub><b>Jev 用法:</b> Jev 在 WebMCP 接口上选择动作；147 次尝试中通过 141 次，DOM 配置为 76/147。</sub><br><sub>相关: <a href="https://x.com/0xidanlevin/status/2100937437325205568">demo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/MaxRovensky/status/2100706874173575199"><img src="https://pbs.twimg.com/amplify_video_thumb/2100706798533566466/img/RAbrmONSdYbkfjAN.jpg" alt="电车难题：人类还是机器人" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/MaxRovensky/status/2100706874173575199">电车难题：人类还是机器人</a></b><br><sub>MaxRovensky · X · ♥ 1.5k · 2026-09-17</sub><br>Jev 逐个作答电车难题的视频，它选择牺牲一个人来救机器人。</td>
</tr>
<tr>
<td width="260" valign="top"></td>
<td valign="top"><b><a href="https://x.com/h_nilforoshan/status/2100409794276520341">HiringCafe 简历与岗位相关性基准</a></b><br><sub>h_nilforoshan · X · ♥ 808 · 2026-09-17</sub><br>帖子串，在 HiringCafe（一个月活 250 万用户的求职应用）上对 Jev 做简历与岗位描述相关性打分的基准测试。<br><sub>相关: <a href="https://hiringcafe.com">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/liorshkiller/status/2100936106615140757"><img src="https://pbs.twimg.com/media/HSgGI1wWQAAY5zl.jpg?name=orig" alt="代码审查基准" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/liorshkiller/status/2100936106615140757">代码审查基准</a></b><br><sub>liorshkiller · X · ♥ 210 · 2026-09-18</sub><br>基准测试：让 Jev 给原始 Git diff 打分，对比 GLM + Grok + Gemini 组合的审查器：零误报，约快 50 倍、约便宜 100 倍，bug 召回率 75%。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://benchmarkheaven.com/jev-models"><img src="https://benchmarkheaven.com/brand/og-launch.png?v=1" alt="JevBench" width="240"></a></td>
<td valign="top"><b><a href="https://benchmarkheaven.com/jev-models">JevBench</a></b><br><sub>Benchmark Heaven (Florian S) · 应用 · ♥ 999 · 2026-09-19</sub><br>Jev 类决策模型的基准测试，从智能、校准、速度和成本四方面给 Jev、它的开源复刻和指令模型排名，各占 25%，取几何平均；Jev 以 75.3 领先，SemIf 以 74.6 位居第二。<br><sub>相关: <a href="https://x.com/airesearch12/status/2101311769113178270">x</a> · <a href="https://news.ycombinator.com/item?id=49786635">discussion</a> · <a href="https://x.com/airesearch12/status/2101311992984199580">demo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/OpenRouter/status/2101412965765529853"><img src="https://pbs.twimg.com/media/HSm39ISbsAAEPfg.png?name=orig" alt="OpenRouter Ori Eval 评判测试" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/OpenRouter/status/2101412965765529853">OpenRouter Ori Eval 评判测试</a></b><br><sub>OpenRouter · X · ♥ 965 · 2026-09-19</sub><br>OpenRouter 用 Ori Eval 比较 Jev 与热门 LLM 作为评判器的表现：Jev 比第二快的模型快 5 倍以上，它最慢的请求也比其他任何模型的中位数快。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/grichadev/status/2100437998571860087"><img src="https://pbs.twimg.com/media/HSY_7aXbIAAxJoj.png?name=orig" alt="安全流水线中的 Jev" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/grichadev/status/2100437998571860087">安全流水线中的 Jev</a></b><br><sub>grichadev · X · ♥ 924 · 2026-09-17</sub><br>某生产安全流水线的结果表：Jev 准确率达到 99.3%，延迟 0.259s，每 1K 次 $0.026，而 Gemini 和开源模型更慢也更贵。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/crislenta/status/2100457614073327754"><img src="https://pbs.twimg.com/amplify_video_thumb/2100457262372560897/img/zSIVGvaQhEZLMd9-.jpg" alt="3D 场景中的 500 个实时 agent" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/crislenta/status/2100457614073327754">3D 场景中的 500 个实时 agent</a></b><br><sub>crislenta · X · ♥ 655 · 2026-09-17</sub><br>基准测试：在 3D 环境中并行运行 500 个实时 agent，未做任何优化，平均延迟 500 毫秒，每秒 35 次 API 调用。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/nikhilmudholkar/status/2100604560335139083"><img src="https://pbs.twimg.com/media/HSbYODoWoAAKjJR.jpg?name=orig" alt="工业邮件分类基准" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/nikhilmudholkar/status/2100604560335139083">工业邮件分类基准</a></b><br><sub>nikhilmudholkar · X · ♥ 439 · 2026-09-17</sub><br>在 10 个类别、1,565 封德语和英语供应商邮件上的基准测试：Jev 得分 96.4%，Gemini 为 97.5% 和 98.5%，每 1,000 封邮件 $0.08，而它置信度在 99%+ 的 737 个答案无一出错。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/xjuntaro/status/2101989210362454268"><img src="https://pbs.twimg.com/media/HSvEC5qa8AAHqx3.jpg?name=orig" alt="Jev 对比 BERT（Kaggle）" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/xjuntaro/status/2101989210362454268">Jev 对比 BERT（Kaggle）</a></b><br><sub>xjuntaro · X · ♥ 556 · 2026-09-21</sub><br>Kaggle 实验发现，零训练的 Jev 略逊于微调过的 BERT，但与 Fable 和 Astra 相当，并领先 TF-IDF 逻辑回归，其中 Noul 加调优阈值的效果最好。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/stash_pomichter/status/2101149600044224698"><img src="https://pbs.twimg.com/amplify_video_thumb/2101149070140014592/img/DdmO54VKkiBapiqs.jpg" alt="Jev 机器人基准" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/stash_pomichter/status/2101149600044224698">Jev 机器人基准</a></b><br><sub>stash_pomichter · X · ♥ 479 · 2026-09-19</sub><br>基准测试：给 Jev 一副机器人身体，完成 120 项真实和模拟的导航与空间推理任务，按速度、成本、token、碰撞和路径质量评分，对手是 Dimcode、Astra、Fable、Opus 和 5.6。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/NFT_Chen/status/2101253568774697099"><img src="https://pbs.twimg.com/amplify_video_thumb/2101252015779373056/img/an3uKosWqfYtwDq9.jpg" alt="Jev 对比 DeepSeek 做工单路由" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/NFT_Chen/status/2101253568774697099">Jev 对比 DeepSeek 做工单路由</a></b><br><sub>NFT_Chen · X · ♥ 170 · 2026-09-19</sub><br>对 500 张真实电商客服工单做并排路由：Jev 用 83 秒、$0.01 全部处理完，而 DeepSeek V4.1 Flash 在被叫停时只处理了 173 张，花了 $0.06。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://quicqdev.github.io/Jev-vs-ML/"><img src="https://quicqdev.github.io/Jev-vs-ML/assets/benchmark-release-blue.png" alt="Jev 对比传统机器学习" width="240"></a></td>
<td valign="top"><b><a href="https://quicqdev.github.io/Jev-vs-ML/">Jev 对比传统机器学习</a></b><br><sub>QuicqDev · 文章 · ▲ 104 · 2026-09-20</sub><br>在八个数据集上与十一条传统机器学习流水线对比，在 IMDb 影评这类文本上表现强，在表格数据上表现弱，附 notebook。<br><sub>相关: <a href="https://github.com/QuicqDev/Jev-vs-ML">repo</a> · <a href="https://www.reddit.com/r/LLMDevs/comments/1wlc11f/jev_vs_classical_ml_results_from_8_classification/">discussion</a> · <a href="https://www.reddit.com/r/LLMDevs/comments/1wlc11f/jev_vs_classical_ml_results_from_8_classification/">discussion 2</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/nateherk/status/2101368457698697511"><img src="https://pbs.twimg.com/media/HSmPYhAXQAAOaLo.jpg" alt="Jev 的 12 个真实用例" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/nateherk/status/2101368457698697511">Jev 的 12 个真实用例</a></b><br><sub>nateherk · 文章 · ♥ 163 · 2026-09-19</sub><br>在 12 个自动化场景上的动手评测：并行化之后，1,000 封邮件过七条决策规则，约花九美分、用时六秒；另有评论、会议、切片和一个 BTC 模拟交易器。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/Khazix0918/status/2100614133171552435"><img src="https://pbs.twimg.com/media/HSbgXI-agAAkxpB.png?name=orig" alt="AIHOT 预过滤对比" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/Khazix0918/status/2100614133171552435">AIHOT 预过滤对比</a></b><br><sub>Khazix0918 · X · ♥ 199 · 2026-09-17</sub><br>为 AIHOT 做的“是否与 AI 相关”预过滤基准测试：Jev 在 30% 阈值下得分 98.91%，GLM 5.3 Flash 为 100%；Jev 的成本低于 DeepSeek V4.1 Flash，但是 Qwen3.7 Flash 的两倍。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/enhanced_jp/status/2100741417593430233"><img src="https://pbs.twimg.com/media/HSbNhZvaUAEhxJx.jpg" alt="改写规则会改变 Jev 的答案" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/enhanced_jp/status/2100741417593430233">改写规则会改变 Jev 的答案</a></b><br><sub>enhanced_jp · 文章 · ♥ 63 · 2026-09-18</sub><br>日文研究，把 Jev 用作设计 harness 的判断层，展示品牌规范措辞更清晰后它的答案如何翻转；共 9 类测试、650 次调用、4,819 个判断。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/iammrduncan/typesafe-ai-benchmark"><img src="https://opengraph.githubassets.com/1/iammrduncan/typesafe-ai-benchmark" alt="typesafe-ai-benchmark" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/iammrduncan/typesafe-ai-benchmark">typesafe-ai-benchmark</a></b><br><sub>iammrduncan · GitHub · ⭐ 37 · 2026-09-16</sub><br>在七个合成工作负载上并排对比 Cerebras 上 Qwen 3.8 27B 的结构化输出与 Jev，记录错误、延迟、token 和估算成本。<br><sub>相关: <a href="https://x.com/iamMrDuncan/status/2100467548298899918">demo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://www.reddit.com/r/accelerate/comments/1wik61b/tested_typesafeai_s_claim_that_their_new_model/"><img src="https://preview.redd.it/as1ajixqf0qh1.jpg?width=968&amp;format=pjpg&amp;auto=webp&amp;s=519a8b120c6b94bad81e9442e7deaafde9501f80" alt="Jev 对比 Terra 的知识基准" width="240"></a></td>
<td valign="top"><b><a href="https://www.reddit.com/r/accelerate/comments/1wik61b/tested_typesafeai_s_claim_that_their_new_model/">Jev 对比 Terra 的知识基准</a></b><br><sub>N8Programs · Reddit · ▲ 69 · 2026-09-17</sub><br>在 MMLU、GPQA、WinoGrande 和 HellaSwag 等多选基准上比较 Jev 与 GPT-5.6 Terra（关闭推理），除数学外 Jev 都达到 Terra 的水平。<br><sub>相关: <a href="https://x.com/N8Programs/status/2100088523403432357">source</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/kubornetes/status/2101709350264025407"><img src="https://res.cloudinary.com/zenn/image/upload/s--Z-HoZ4JJ--/c_fit%2Cg_north_west%2Cl_text:notosansjp-medium.otf_55:Jev%252C%2520Gemini%252C%2520DistilBERT%252C%2520LightGBM%25E3%2581%25AE%25E5%2588%2586%25E9%25A1%259E%25E6%2580%25A7%25E8%2583%25BD%25E3%2582%2592%25E6%25AF%2594%25E8%25BC%2583%25E3%2581%2597%25E3%2581%25A6%25E3%2581%25BF%25E3%2581%259F%2Cw_1010%2Cx_90%2Cy_100/g_south_west%2Cl_text:notosansjp-medium.otf_37:kubotaka%2Cx_203%2Cy_121/g_south_west%2Ch_90%2Cl_fetch:aHR0cHM6Ly9zdGF0aWMuemVubi5zdHVkaW8vdXNlci11cGxvYWQvYXZhdGFyLzU4YTA5ZTA2NzAuanBlZw==%2Cr_max%2Cw_90%2Cx_87%2Cy_95/v1627283836/default/og-base-w1200-v2.png?_a=BACMTiAE" alt="Jev 对比 Gemini、DistilBERT 和 LightGBM" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/kubornetes/status/2101709350264025407">Jev 对比 Gemini、DistilBERT 和 LightGBM</a></b><br><sub>kubornetes · X · ♥ 204 · 2026-09-20</sub><br>日文分类基准测试，比较 Jev 与 Gemini、DistilBERT 和 LightGBM，结论是 Jev 是分类任务的稳妥默认选择；实验代码已放到 GitHub 上。<br><sub>相关: <a href="https://zenn.dev/xxkuboxx/articles/e232d267a76f43">article</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/libukai/status/2100984923926728920"><img src="https://pbs.twimg.com/amplify_video_thumb/2100977858718113792/img/1cfiUtsApbmw3_sp.jpg" alt="Jev 对比 Gemini Flash Lite 做新闻打标" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/libukai/status/2100984923926728920">Jev 对比 Gemini Flash Lite 做新闻打标</a></b><br><sub>libukai · X · ♥ 163 · 2026-09-18</sub><br>在 1,000 篇人民日报新闻组成的测试集上判断是否与湖北相关：Jev 每篇 0.35 秒，Gemini Flash Lite 为 3 秒，两者约有 15% 的结果不一致。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/everythingmeta/status/2101058921989390395"><img src="https://pbs.twimg.com/media/HSh0glmbQAAr0xv.jpg" alt="Jev 在 Parallel 真实搜索任务上的表现" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/everythingmeta/status/2101058921989390395">Jev 在 Parallel 真实搜索任务上的表现</a></b><br><sub>everythingmeta · 文章 · ♥ 159 · 2026-09-18</sub><br>Parallel 在搜索重排及相关任务上测试 Jev，零样本的 Jev 在 NDCG@10 上至少追平了他们一个经过微调的内部重排器。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/maxim-saplin/llm_chess"><img src="https://github.com/user-attachments/assets/4375a8a8-e226-4ed1-820f-86006d0404e2" alt="LLM Chess：Jev 结果" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/maxim-saplin/llm_chess">LLM Chess：Jev 结果</a></b><br><sub>maxim-saplin · GitHub · ⭐ 131 · 2026-09-17</sub><br>长期运行的 LLM 国际象棋基准加入了 Jev：在对阵随机棋手和 Komodo Dragon 的 80 局中，它零非法走子，赢 8 局、和 22 局。<br><sub><b>Jev 用法:</b> Jev 从合法走法中挑选每一步；每局约 $0.0015，Elo 估计约为 243。</sub><br><sub>相关: <a href="https://maxim-saplin.github.io/llm_chess/">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/get-convex/convex-evals"><img src="https://raw.githubusercontent.com/get-convex/convex-evals/main/docs/assets/visualizer.png" alt="Convex 决策模型评测" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/get-convex/convex-evals">Convex 决策模型评测</a></b><br><sub>get-convex · GitHub · ⭐ 128 · 2025-01-10</sub><br>从 90 个 Convex 编程评测中抽出 106 个决策问题组成的基准，通过 OpenRouter 的 decisions API 把 Jev 与语言模型对比，记录概率、置信度和成本。<br><sub>相关: <a href="https://convex-evals.netlify.app/">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/vinilana/jev-eval-agent"><img src="https://opengraph.githubassets.com/1/vinilana/jev-eval-agent" alt="jev-eval-agent" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/vinilana/jev-eval-agent">jev-eval-agent</a></b><br><sub>vinilana · GitHub · ⭐ 103 · 2026-09-17</sub><br>用一个带 100 个 mock 工具的个人助理 agent 做实验，统计 LLM 自己挑工具，与由 Jev 挑工具、LLM 只填参数这两种方式各需要多少步。<br><sub><b>Jev 用法:</b> 在每一步模型调用前，对工具目录做两阶段裁剪。</sub><br><sub>相关: <a href="https://x.com/oviniciuslana/status/2100610517886771393">demo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://www.reddit.com/r/LLMDevs/comments/1wkukle/i_tested_jev_on_nasa_kepler_signals/"><img src="https://external-preview.redd.it/YWw1cmdnb3Z5aXFoMcOMmaLg4COKusRl8Y9ue1_gcaRiXHaXsbLqmx3IvjD1.png?format=pjpg&amp;auto=webp&amp;s=aceae8acf90db6f7547287ef56382e02c1fd417e" alt="用 Jev 判别 NASA Kepler 信号" width="240"></a></td>
<td valign="top"><b><a href="https://www.reddit.com/r/LLMDevs/comments/1wkukle/i_tested_jev_on_nasa_kepler_signals/">用 Jev 判别 NASA Kepler 信号</a></b><br><sub>This_Cell_1829 · Reddit · ▲ 34 · 2026-09-19</sub><br>在 8,054 个 Kepler 关注天体（KOI）上测试 Jev，根据 21 项测量值在已确认行星、误报和候选之间选择；准确率 54.2%，规则基线为 64.4%，重新格式化输入后达到 72.5%。<br><sub><b>Jev 用法:</b> 每个信号在三个标签上做一个 Choice；第二轮中数值先在代码里分桶成标签。</sub><br><sub>相关: <a href="https://gist.github.com/ipaulsmith/e5c3ae3a492a455435d5bfc161404312">data</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/GoSailGlobal/status/2100877682972258619"><img src="https://pbs.twimg.com/amplify_video_thumb/2100877620292583424/img/7Ztuku-R01C1GvlU.jpg" alt="Jev 重排基准" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/GoSailGlobal/status/2100877682972258619">Jev 重排基准</a></b><br><sub>GoSailGlobal · X · ♥ 71 · 2026-09-18</sub><br>在 33,047 条 Agent Skills Hub 条目上把 Jev 用作搜索重排器的基准测试：单独使用时它比 bge-m3 的 NDCG@10 只提升了 0.012，而两者做 RRF 融合后达到 0.864。<br><sub><b>Jev 用法:</b> 对 bge-m3 的前 30 条结果重排；也作为相关性评判器与 Haiku 做了对比。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/fstandhartinger/jevbench"><img src="https://raw.githubusercontent.com/fstandhartinger/jevbench/main/results/v1.2/charts/main-score.png" alt="JevBench" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/fstandhartinger/jevbench">JevBench</a></b><br><sub>fstandhartinger · GitHub · ⭐ 69 · 2026-09-19</sub><br>第三方基准，运行 534 个冻结的决策问题，把智能、校准、速度和成本合成一个总分，覆盖 Jev、开源复刻、分类器和 LLM 基线。<br><sub>相关: <a href="https://benchmarkheaven.com/jev-models">results</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/ShengyaoZhuang/status/2101212268440723895"><img src="https://pbs.twimg.com/media/HSj9xNobQAEf2w7.jpg?name=orig" alt="Jev 在 DL19/DL20 上当重排器" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/ShengyaoZhuang/status/2101212268440723895">Jev 在 DL19/DL20 上当重排器</a></b><br><sub>ShengyaoZhuang · X · ♥ 64 · 2026-09-19</sub><br>信息检索研究者在 TREC DL19 和 DL20 上，对 BM25 前 100 条结果测试 Jev 作为 pointwise、pairwise、setwise 和 listwise 重排器的表现，结论是效果好且便宜。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/danielgshea/jev-as-a-judge"><img src="https://raw.githubusercontent.com/danielgshea/jev-as-a-judge/main/assets/benchmark-jev-luna-terra-sonnet-oracle/6d08df72-c878-458c-b7c5-a7824ee6e721/does-pass-accuracy.svg" alt="Jev 当评判器" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/danielgshea/jev-as-a-judge">Jev 当评判器</a></b><br><sub>danielgshea · GitHub · ⭐ 62 · 2026-09-17</sub><br>实验：让 Jev 与 GPT-5.6 Luna、GPT-5.6 Terra 和 Claude Sonnet 4.6 评判同一批固定的 agent 运行，测量二分类准确率、分数可靠性、成本和延迟。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/GoSailGlobal/status/2100973279771246861"><img src="https://pbs.twimg.com/media/HSgn1l4aQAEqqvx.jpg" alt="关于 Jev 真实局限的六个实验" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/GoSailGlobal/status/2100973279771246861">关于 Jev 真实局限的六个实验</a></b><br><sub>GoSailGlobal · 文章 · ♥ 50 · 2026-09-18</sub><br>中文记录，在五个开源仓库上做了六个实验：在列含义明确的表格上 Jev 的 AUC 达到 0.83，在哈希化的 CTR 数据上只有 0.46，最适合作为附加到基线模型上的特征。<br><sub>相关: <a href="https://github.com/zhuyansen/jev-cold-start-prior">repo</a> · <a href="https://github.com/zhuyansen/jev-search-rerank-eval">repo2</a> · <a href="https://github.com/zhuyansen/jev-support-pulse">repo3</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/punk2898/status/2102218153766125851"><img src="https://pbs.twimg.com/media/HSuELanbUAAN3Kr.jpg" alt="花 $200 测试 Jev" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/punk2898/status/2102218153766125851">花 $200 测试 Jev</a></b><br><sub>punk2898 · 文章 · ♥ 16 · 2026-09-22</sub><br>中文评测，花 $200 在 2,390 道题（含中文任务）上把 Jev 与 GPT-4.1-mini 以及 GPT-5.6 Sol、Terra、Luna 对比，结论是“便宜 100 倍”大致成立，“快 100 倍”则不成立。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/malleshpai/status/2102207238236500096"><img src="https://pbs.twimg.com/media/HSyJp8GXsAAho-G.jpg" alt="校准 Jev" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/malleshpai/status/2102207238236500096">校准 Jev</a></b><br><sub>malleshpai · 文章 · ♥ 48 · 2026-09-22</sub><br>一位经济学家的校准研究，覆盖五个带标注的任务（约 37,000 条，每条 24 种表述），发现 Jev 的概率常常过度自信，用在线 Foster-Hart 修正后有所改善。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://www.reddit.com/r/machinelearningnews/comments/1wk8lwj/typed_decisions_jev_and_a_frozen_149m_encoder_on/"><img src="https://external-preview.redd.it/yYnCg7p4fjziFlw0ScTc8TfP2KiLGEV0p-BNnYEsjoM.png?auto=webp&amp;s=3d68cc22011896ecaf00d6c5e70f6cddd97feebb" alt="类型化决策基准" width="240"></a></td>
<td valign="top"><b><a href="https://www.reddit.com/r/machinelearningnews/comments/1wk8lwj/typed_decisions_jev_and_a_frozen_149m_encoder_on/">类型化决策基准</a></b><br><sub>asankhs · Reddit · ▲ 14 · 2026-09-19</sub><br>一个新的 400 例类型化决策基准，Jev 得分 0.727，接近 0.735 的教师模型上限，而带小型分类头的冻结 149M ModernBERT 编码器为 0.646。<br><sub>相关: <a href="https://latentnode.pages.dev/articles/typed-decisions">article</a> · <a href="https://latentnode.pages.dev/articles/typed-decisions">project</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://news.ycombinator.com/item?id=49788402"><img src="https://archestra.ai/blog/2026-09-21-jev-model-comparison.webp" alt="Jev 处理 100 个 agent 工具调用" width="240"></a></td>
<td valign="top"><b><a href="https://news.ycombinator.com/item?id=49788402">Jev 处理 100 个 agent 工具调用</a></b><br><sub>arseny_info · Hacker News · ▲ 11 · 2026-09-21</sub><br>Archestra 为自家的信息流标注器在 100 个真实 Claude Code 工具调用上比较 Jev、Sonnet 5 和开源权重模型，而一律回答“无害”就已经能拿到 79%。<br><sub>相关: <a href="https://archestra.ai/blog/we-tested-jev-on-100-real-agent-calls">article</a> · <a href="https://archestra.ai/blog/we-tested-jev-on-100-real-agent-calls">project</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/silverstein/minutes/blob/main/tooling/voice-evals/jev.mjs"><img src="https://raw.githubusercontent.com/silverstein/minutes/main/docs/assets/demo.gif" alt="Minutes 的 Jev 语音评测" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/silverstein/minutes/blob/main/tooling/voice-evals/jev.mjs">Minutes 的 Jev 语音评测</a></b><br><sub>silverstein · GitHub · ⭐ 1.5k 仓库 · 2026-03-18</sub><br>Minutes 会议记忆应用中的合成资格测试脚本，检验 Jev 能否胜任其语音路径需要的七个 Choice 决策，比如参会者约束、语义回忆、已验证的粘贴、过期目标和提示词注入。<br><sub>相关: <a href="https://useminutes.app">app</a> · <a href="https://github.com/silverstein/minutes">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/GoSailGlobal/status/2101259812709535800"><img src="https://pbs.twimg.com/media/HSksmBCbsAAlqY2.jpg" alt="Jev 对比 BERT 家族" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/GoSailGlobal/status/2101259812709535800">Jev 对比 BERT 家族</a></b><br><sub>GoSailGlobal · 文章 · ♥ 14 · 2026-09-19</sub><br>中文公开实验，在 AG News、SST-2、Banking77、TweetEval、PAWS 以及一个发布后的 arXiv 数据集上比较 Jev 与零样本 BERT 家族分类器，并给出 95% 置信区间；Jev 在全部 7 个评测集上胜出。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/stas_sorokin_/status/2101994942818115738"><img src="https://pbs.twimg.com/media/HSvJOjSWEAEtkH7.jpg?name=orig" alt="给 1,000 篇论文分类再审计" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/stas_sorokin_/status/2101994942818115738">给 1,000 篇论文分类再审计</a></b><br><sub>stas_sorokin_ · X · ♥ 6 · 2026-09-21</sub><br>Jev 论文地图的开源复刻：Jev 用 $0.0585 把 1,000 篇 AI 论文分进 24 个主题，以 Opus 5 作为评判，100 个标签中有 85 个一致，但成本是 153 倍，每篇耗时 1.9s 对比 57 毫秒。<br><sub><b>Jev 用法:</b> 每篇论文在 24 个主题上做一个 Choice；用其概率标出哪些标签需要昂贵模型复查。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/dreadnode/status/2102131162386710885"><img src="https://pbs.twimg.com/media/HSxDXD_WsAAL9_r.jpg?name=orig" alt="Jev 挑战 ScopeJudge" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/dreadnode/status/2102131162386710885">Jev 挑战 ScopeJudge</a></b><br><sub>dreadnode · X · ♥ 25 · 2026-09-21</sub><br>安全公司 dreadnode 在自家针对 agent 越界行为的 ScopeJudge 基准上测试 Jev，发现它能与领先的 LLM 评判器一较高下，每千次检查只需几美分，平均响应 130 毫秒。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Zaious/jev-capability-atlas"><img src="https://opengraph.githubassets.com/1/Zaious/jev-capability-atlas" alt="Jev Capability Atlas" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Zaious/jev-capability-atlas">Jev Capability Atlas</a></b><br><sub>Zaious · GitHub · ⭐ 24 · 2026-09-18</sub><br>双语（以繁体中文为主）证据地图，梳理 Jev 的校准决策宣称在哪里成立、在哪里失效，依据是真实的 API 调用凭据、测试套件以及写给 agent 的指南。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/snakajima/bus20"><img src="https://opengraph.githubassets.com/1/snakajima/bus20" alt="Bus 2.0 调度基准" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/snakajima/bus20">Bus 2.0 调度基准</a></b><br><sub>snakajima · GitHub · ⭐ 21 · 2018-08-27</sub><br>按需共享接驳车在线调度的基准测试，比较 Jev、本地 Laya、Claude、OpenAI 和 Gemini 的调度策略；其中关于 Jev 的笔记说明了为什么算术应该交给代码（157.6 min² 对比参考值 16.2）。<br><sub>相关: <a href="https://github.com/snakajima/bus20/blob/master/docs/jev-native.md">notes</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://nearhere.events/blog/typesafe-jev-mistral-gemini-event-validation"><img src="https://external-preview.redd.it/NzBRO0R5S7MxmGwz2RGsa-J3bzfP125gTZDRmnpWI-0.jpeg?auto=webp&amp;s=3fba8ca1c31a53433859005bc9aa4f74a6e5dea4" alt="Jev 对比 Mistral 和 Gemini 做活动审核" width="240"></a></td>
<td valign="top"><b><a href="https://nearhere.events/blog/typesafe-jev-mistral-gemini-event-validation">Jev 对比 Mistral 和 Gemini 做活动审核</a></b><br><sub>Near Here · 文章 · ▲ 7 · 2026-09-16</sub><br>用例研究，比较 Jev 与 Mistral Small 4、Gemini 3.5 Flash-Lite 剔除不合适的本地活动信息的能力；Jev 得分 96%（48/50），耗时 0.59s，每 1,000 次决策 $0.043。<br><sub><b>Jev 用法:</b> 基于活动信息的标题和描述，使用原生的带概率 Choice。</sub><br><sub>相关: <a href="https://www.reddit.com/r/typesafe_ai/comments/1whtaq4/near_here_got_early_access_to_typesafe_jev_so_we/">discussion</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/backnotprop/status/2101713396966338575"><img src="https://pbs.twimg.com/media/HSrISHhaIAEDxM7.jpg?name=orig" alt="Jev 越狱基准" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/backnotprop/status/2101713396966338575">Jev 越狱基准</a></b><br><sub>backnotprop · X · ♥ 20 · 2026-09-20</sub><br>提示词注入基准测试，把 Jev 与包括 Meta 在内的标准护栏分类器对比：它在一个开放测试集和最新的攻击集上胜出，在较老的数据集上落败，也守不住严格的误报预算。<br><sub>相关: <a href="https://backnotprop.com/blog/jev-guardrails">article</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/ilijabogunovic/status/2102075332014624819"><img src="https://pbs.twimg.com/media/HSwP1Z3XoAADcnY.png?name=orig" alt="Jev 挑战 LLM-Wikirace" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/ilijabogunovic/status/2102075332014624819">Jev 挑战 LLM-Wikirace</a></b><br><sub>ilijabogunovic · X · ♥ 19 · 2026-09-21</sub><br>研究者在自己的 LLM-Wikirace 基准上运行 Jev（450 局、8 小时、总花费不到 $1），发现它又快又便宜，但缺乏前沿 LLM 那样的世界知识和规划能力。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/ShenSeanChen/status/2102234040535494876"><img src="https://pbs.twimg.com/amplify_video_thumb/2102216562342309888/img/30v3t9WGnQzugfFu.jpg" alt="判断力竞技场" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/ShenSeanChen/status/2102234040535494876">判断力竞技场</a></b><br><sub>ShenSeanChen · X · ♥ 18 · 2026-09-22</sub><br>视频，讲解 System 1 与 System 2，并在 15 道人工标注的问题上让 Jev 与 Claude Opus、Haiku 4.5 和 GPT-5.4 Mini 比拼；Opus 多答对一道，但耗时是 10 倍，成本是 146 倍。<br><sub>相关: <a href="https://github.com/ShenSeanChen/waku-agent">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/yibie/laya-jev-lab"><img src="https://pbs.twimg.com/media/HSo34y_W4AA1A3-.jpg" alt="laya-jev-lab" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/yibie/laya-jev-lab">laya-jev-lab</a></b><br><sub>yibie · GitHub · ⭐ 2 · 2026-09-20</sub><br>在 M4 Max 上对 Jev 与开源权重 Laya 的独立测量：在 40 张中文客服工单上 Jev 得分 78%、Laya 57%，另有一个本地优先的级联方案，在准确率与 Jev 持平的同时速度约为 1.8 倍。<br><sub>相关: <a href="https://x.com/yibie/status/2101553680889598094">write-up</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/AbdelStark/jev-benchmarks"><img src="https://opengraph.githubassets.com/1/AbdelStark/jev-benchmarks" alt="jev-benchmarks" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/AbdelStark/jev-benchmarks">jev-benchmarks</a></b><br><sub>AbdelStark · GitHub · ⭐ 16 · 2026-09-17</sub><br>考虑概率的基准测试，在零样本文本分类上比较 Jev 与 GLiNER2.5，在三个 BTZSC 数据集上测量校准、固定错误预算下的覆盖率和延迟。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/145k4/status/2100933101966758250"><img src="https://pbs.twimg.com/amplify_video_thumb/2100932546401812480/img/fPV392wDj1Xr1DHo.jpg" alt="用 Choice 和 Noul 做电车难题" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/145k4/status/2100933101966758250">用 Choice 和 Noul 做电车难题</a></b><br><sub>145k4 · X · ♥ 14 · 2026-09-18</sub><br>把一系列电车难题分别以 Choice 和 Noul 的形式交给 Jev，检验问题类型是否会改变它的判断。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/erendikmenn/jev-rag-benchmark"><img src="https://raw.githubusercontent.com/erendikmenn/jev-rag-benchmark/main/assets/benchmark/retrieval-errors.png" alt="jev-rag-benchmark" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/erendikmenn/jev-rag-benchmark">jev-rag-benchmark</a></b><br><sub>erendikmenn · GitHub · ⭐ 14 · 2026-09-19</sub><br>可复现的基准测试，在 1,044 道土耳其语 XQuAD 问题上把 Jev 用作小型 RAG 系统的重排器，测量质量、延迟和成本，每个重排器拿到的都是同样的 20 个候选。<br><sub>相关: <a href="https://x.com/ErenAILab/status/2101629475502817699">demo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/QuicqDev/Jev-vs-ML"><img src="https://opengraph.githubassets.com/1/QuicqDev/Jev-vs-ML" alt="Jev-vs-ML" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/QuicqDev/Jev-vs-ML">Jev-vs-ML</a></b><br><sub>QuicqDev · GitHub · ⭐ 13 · 2026-09-20</sub><br>在八个数据集、三个随机种子上对比 Jev 1.13.0 与 11 条传统分类流水线：在 IMDb 上 Jev 的平衡准确率达到 96.3%，对手为 88.4%，而在表格数据上传统模型领先。<br><sub>相关: <a href="https://quicqdev.github.io/Jev-vs-ML/">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://fatliverfreddy.substack.com/p/a-different-kind-of-model-for-ai"><img src="https://substackcdn.com/image/fetch/$s_!VnMM!,w_1200,h_675,c_fill,f_jpg,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6ee590d4-310d-43ca-b093-6d5960d53672_1734x907.png" alt="用于 AI 可观测性的另一类模型" width="240"></a></td>
<td valign="top"><b><a href="https://fatliverfreddy.substack.com/p/a-different-kind-of-model-for-ai">用于 AI 可观测性的另一类模型</a></b><br><sub>Avital Tamir · 文章 · ▲ 4 · 2026-09-18</sub><br>用约 17 分钟、不到一美元给 10,000 条 agent trace 标注状态和情绪，并与一个评测模型比较准确率。<br><sub>相关: <a href="https://news.ycombinator.com/item?id=49751140">discussion</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/hhilbig/polsci-open-bench"><img src="https://raw.githubusercontent.com/hhilbig/polsci-open-bench/main/output/figures/fig-jev-cost-latency.png" alt="polsci-open-bench" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/hhilbig/polsci-open-bench">polsci-open-bench</a></b><br><sub>hhilbig · GitHub · ⭐ 11 · 2026-04-27</sub><br>在 33 个政治学分类任务上对本地和商业 LLM 的基准测试，Jev 1.13 的平均 F1 为 0.661，Claude Opus 5 为 0.714，而 Jev 每 1,000 条只需 $0.036，中位延迟 0.27 秒。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://huggingface.co/datasets/Praveenrajus/jev-bench"><img src="https://huggingface.co/datasets/Praveenrajus/jev-bench/resolve/main/results/jev-1.13.0/figures/calibration_map.png" alt="jev-bench" width="240"></a></td>
<td valign="top"><b><a href="https://huggingface.co/datasets/Praveenrajus/jev-bench">jev-bench</a></b><br><sub>Praveenrajus · Hugging Face · ♥ 1 · 2026-09-20</sub><br>把人工标注数据集改写成 System One 问题（22 个配置、166,054 行），在有人工标签分布的地方予以保留，并附 jev-1.13.0 的准确率和校准结果。<br><sub>相关: <a href="https://github.com/uspraveen/Jevify">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/brandonjcarl/status/2102064833256387016"><img src="https://pbs.twimg.com/media/HSwIy4gWgAAHsT-.jpg" alt="对 Jev 的全方位考验" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/brandonjcarl/status/2102064833256387016">对 Jev 的全方位考验</a></b><br><sub>brandonjcarl · 文章 · ♥ 1 · 2026-09-21</sub><br>从小学到博士水平，在五个领域、25 个子领域上测试 Jev：Jev 得分 76%，DeepSeek v4.1 Flash 为 93%，但 Jev 成本约低 50 倍，最擅长文本分类。<br><sub>相关: <a href="https://essays.brandoncarl.com">blog</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://www.ramonov.com/blog/64-tiny-benchmarks-for-jev/"><img src="https://ramonov.com/og-default.png" alt="给 Jev 的 64 个小基准" width="240"></a></td>
<td valign="top"><b><a href="https://www.ramonov.com/blog/64-tiny-benchmarks-for-jev/">给 Jev 的 64 个小基准</a></b><br><sub>George Ramonov · 文章 · ▲ 3 · 2026-09-19</sub><br>非正式评测：把 64 个超出常规用途的问题各发给 jev-1.13.0 50 次（共 3,200 次调用），用图表展示返回分布的稳定程度，包括单次答案会翻转的地方。<br><sub>相关: <a href="https://news.ycombinator.com/item?id=49777995">discussion</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"></td>
<td valign="top"><b><a href="https://mikulskibartosz.name/typesafe-jev-guess-what-i-drew">Jev 猜我画的是什么</a></b><br><sub>Bartosz Mikulski · 文章 · ▲ 3 · 2026-09-19</sub><br>实验：把 400 幅手绘草图转成文字，让 Jev 说出画的是什么：它远远好过随机猜测，但输给了 Claude Sonnet 5，而且一半以上都答成了飞机。<br><sub>相关: <a href="https://news.ycombinator.com/item?id=49768633">discussion</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://backnotprop.com/blog/jev-guardrails/"><img src="https://backnotprop.com/blog/jev-guardrails/og.png" alt="Jev 越狱基准" width="240"></a></td>
<td valign="top"><b><a href="https://backnotprop.com/blog/jev-guardrails/">Jev 越狱基准</a></b><br><sub>Mike Ramos · 文章 · ▲ 3 · 2026-09-20</sub><br>每条消息用一个 Noul，与四个本地注入检测器对比，发现 Jev 排序能力强，但在 1% 误报率下召回率很低。<br><sub>相关: <a href="https://news.ycombinator.com/item?id=49777476">discussion</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://usenym.com/technical-blog/rebuilding-our-agent-with-jev"><img src="https://usenym.com/technical-blog/wren-jev-social-20260920.jpg" alt="围绕 Jev 重建 Nym 的 agent" width="240"></a></td>
<td valign="top"><b><a href="https://usenym.com/technical-blog/rebuilding-our-agent-with-jev">围绕 Jev 重建 Nym 的 agent</a></b><br><sub>Nym · 文章 · ▲ 3 · 2026-09-20</sub><br>用 Jev 取代七个 LLM 审核器和工具选择，不确定时回退到更大的模型，提速 4.1 到 5.7 倍。<br><sub>相关: <a href="https://news.ycombinator.com/item?id=49779979">discussion</a> · <a href="https://usenym.com">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://www.southbridge.ai/blog/jev-entity-resolution"><img src="https://www.southbridge.ai/images/og/jev-entity-resolution.png" alt="高吞吐数据流水线中的 System One 模型" width="240"></a></td>
<td valign="top"><b><a href="https://www.southbridge.ai/blog/jev-entity-resolution">高吞吐数据流水线中的 System One 模型</a></b><br><sub>Southbridge AI · 文章 · ▲ 3 · 2026-09-20</sub><br>实体消解：由 Jev 承担大部分工作、LLM 负责复核，成本低 226 倍；把判定标准改写成“什么才算充分证据”后，开发集上的问题得到解决。<br><sub>相关: <a href="https://news.ycombinator.com/item?id=49771931">discussion</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/LargitData1/status/2101679703673454669"><img src="https://pbs.twimg.com/media/HSqqjJebkAA1Xbm.jpg?name=orig" alt="RAG agent 路由基准" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/LargitData1/status/2101679703673454669">RAG agent 路由基准</a></b><br><sub>LargitData1 · X · ♥ 8 · 2026-09-20</sub><br>中文基准测试，用 100 段多轮对话检验 agent 能否选对信息源（知识库、文档、网络、工具、追问用户）：Gemma 4 31B 77.0%，Jev 61.4%，djev-spark 32.2%，SemIf 24.0%，Laya 0%。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/akafukusou/status/2100643727178092903"><img src="https://pbs.twimg.com/amplify_video_thumb/2100642936119836672/img/iQ5xCV_Yd2Z9QfUN.jpg" alt="Jev 在 QASPER 上的检索" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/akafukusou/status/2100643727178092903">Jev 在 QASPER 上的检索</a></b><br><sub>akafukusou · X · ♥ 7 · 2026-09-17</sub><br>在 34 道 QASPER 问题上的检索测试：在标准证据覆盖率上，Jev 以 17 比 3（14 平）胜过搭配 OpenAI text-embedding-3-small 的 pgvector。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/carlaiau/jev-reranking"><img src="https://opengraph.githubassets.com/1/carlaiau/jev-reranking" alt="jev-reranking" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/carlaiau/jev-reranking">jev-reranking</a></b><br><sub>carlaiau · GitHub · ⭐ 7 · 2026-03-13</sub><br>零样本重排实验，在 MS MARCO 和 TREC-1 WSJ 上比较 Jev 与 monoBERT 以及已发表的 TREC 运行结果；在 TREC DL 2021 文档上，Jev 的 MAP 为 0.2790，P@10 为 0.8930。<br><sub><b>Jev 用法:</b> 对每篇文档的重叠窗口做相关性打分，取最高的窗口分数（MaxP）。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/mahlernim/jev-korean-benchmark"><img src="https://raw.githubusercontent.com/mahlernim/jev-korean-benchmark/main/docs/figures/korean-check.png" alt="Jev 处理韩语" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/mahlernim/jev-korean-benchmark">Jev 处理韩语</a></b><br><sub>mahlernim · GitHub · ⭐ 6 · 2026-09-17</sub><br>冻结、可复现的 100 题抽样检验，测试 Jev 处理韩语文本的能力：阅读理解韩语得分 96、英语 97，而细粒度语义判断为 76 对 80。<br><sub>相关: <a href="https://ahn-lab.org/jev-korean-benchmark/">site</a> · <a href="https://ahn-lab.org/jev-korean-benchmark">write-up</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://backnotprop.com/blog/jev-poker/"><img src="https://backnotprop.com/blog/jev-poker/og.png" alt="Jev 是牌桌上的那条鱼" width="240"></a></td>
<td valign="top"><b><a href="https://backnotprop.com/blog/jev-poker/">Jev 是牌桌上的那条鱼</a></b><br><sub>Mike Ramos (backnotprop) · 文章 · ▲ 2 · 2026-09-17</sub><br>扑克测试：同一手牌只是换了标签，Jev 的判断就摆动 15 到 30 个点，而且面对已知成型的同花，16 次运行中 16 次仍然下注，以此警告不要未经评测就部署它。<br><sub>相关: <a href="https://news.ycombinator.com/item?id=49745212">discussion</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/wondertwins/jev-benchmark"><img src="https://raw.githubusercontent.com/wondertwins/jev-benchmark/main/runs/media/v2_jev_vs_sf0_tactical_filter_s4_jev-latest.gif" alt="jev-benchmark" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/wondertwins/jev-benchmark">jev-benchmark</a></b><br><sub>wondertwins · GitHub · ⭐ 6 · 2026-09-16</sub><br>两个 Jev 基准：一是国际象棋，只有在代码提供战术事实时它才能下到约 950 Elo；二是判断语音转文字的玩家在对哪个游戏 NPC 说话，F1 为 0.96，精确率 1.0。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/zhuyansen/jev-search-rerank-eval"><img src="https://opengraph.githubassets.com/1/zhuyansen/jev-search-rerank-eval" alt="jev-search-rerank-eval" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/zhuyansen/jev-search-rerank-eval">jev-search-rerank-eval</a></b><br><sub>zhuyansen · GitHub · ⭐ 6 · 2026-09-18</sub><br>分级相关性评测，在 Agent Skills Hub 目录的 9,831 个标注对和 164 条中英文查询上，比较 Jev Score 重排与关键词、BM25、bge-m3、向量嵌入和融合基线。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/teyhouse/jev-secret-detection"><img src="https://raw.githubusercontent.com/teyhouse/jev-secret-detection/main/assets/screenshot.png" alt="jev-secret-detection" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/teyhouse/jev-secret-detection">jev-secret-detection</a></b><br><sub>teyhouse · GitHub · ▲ 2 · 2026-09-17</sub><br>基准测试：Jev 在 100 个文件片段以及边界用例集和配置集中识别真实可用密钥凭据的能力，报告准确率、AUC 和召回率，不借助正则或服务商验证。<br><sub><b>Jev 用法:</b> 每个片段一个 Noul，与预期标签比对。</sub><br><sub>相关: <a href="https://www.reddit.com/r/LLMDevs/comments/1wiu1ej/typesafe_jev_secret_detection_test/">discussion</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/goodrahstar/pdf-race"><img src="https://opengraph.githubassets.com/1/goodrahstar/pdf-race" alt="PDF Race" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/goodrahstar/pdf-race">PDF Race</a></b><br><sub>goodrahstar · GitHub · ⭐ 6 · 2026-09-20</sub><br>在 12 篇 arXiv 论文上让三条文档流水线赛跑：Docling 加 Jev、Docling 加 Gemini 3.8 Flash，以及由 Gemini 直接读 PDF；三者都拿到 12/12，但 Jev 这条线花费 $0.0022，对比 $0.0882。<br><sub><b>Jev 用法:</b> 在相同的解析文本上，Jev 每份文档的中位决策耗时 388 毫秒，Gemini 为 3,134 毫秒。</sub><br><sub>相关: <a href="https://pdf-race.vercel.app">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/gemanor/jev-code-review-benchmark"><img src="https://raw.githubusercontent.com/gemanor/jev-code-review-benchmark/main/docs/results/comparison.png" alt="Jev 代码审查基准" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/gemanor/jev-code-review-benchmark">Jev 代码审查基准</a></b><br><sub>gemanor · GitHub · ⭐ 5 · 2026-09-17</sub><br>基准测试：Jev、Gemini Flash 和 Claude Fable 按四条审查规则检查 Python 代码，各跑 360 次调用：Jev 比 Flash 便宜 45 倍，中位耗时 0.75 秒，但正确率为 98%，对手为 100%。<br><sub>相关: <a href="https://news.ycombinator.com/item?id=49744021">demo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/anessbelbati/jev-rerank-bench"><img src="https://raw.githubusercontent.com/anessbelbati/jev-rerank-bench/main/docs/readme-header.png" alt="jev-rerank-bench" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/anessbelbati/jev-rerank-bench">jev-rerank-bench</a></b><br><sub>anessbelbati · GitHub · ⭐ 5 · 2026-09-16</sub><br>重排基准测试，在 14 个数据集上比较 Jev 与 Cohere Rerank 4、ZeroEntropy zerank-2 和一个聊天模型基线；Jev 的评分细则平均得分 0.692，Cohere Pro 为 0.691，没有明显赢家。<br><sub>相关: <a href="https://anessbelbati.com/lab/jev-reranking">write-up</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/identityTorn/status/2100475121324728615"><img src="https://pbs.twimg.com/media/HSZizHpasAABVQJ.jpg?name=orig" alt="Jev 对比微调过的 Qwen 分类器" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/identityTorn/status/2100475121324728615">Jev 对比微调过的 Qwen 分类器</a></b><br><sub>identityTorn · X · ♥ 3 · 2026-09-17</sub><br>一线笔记，在内部基准上比较零样本 Jev 与微调过的 Qwen 分类器：在相同精确率下，召回率相差约 5 个点以内，满负荷运行每月约 $70。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/ielab/llm-rankers/tree/main/jev"><img src="https://opengraph.githubassets.com/1/ielab/llm-rankers" alt="llm-rankers 的 Jev 实验" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/ielab/llm-rankers/tree/main/jev">llm-rankers 的 Jev 实验</a></b><br><sub>ielab · GitHub · ⭐ 212 仓库 · 2023-10-14</sub><br>零样本的 TREC DL19/DL20 实验，把 Jev 用作 pointwise、pairwise、setwise 和 listwise 重排器；在一次请求里对全部 100 个 BM25 段落做 listwise Score，在 DL19 上 nDCG@10 达到 0.728，每次查询 $0.0009。<br><sub><b>Jev 用法:</b> Score 问题在所有设置下都胜过 Choice 问题；由于输出免费，100 个候选可以全部放进一次请求。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/chunxiaoxx/nautilus-compass/blob/main/docs/wall/GENESIS_HOSTED_JEV_CALIBRATION.md"><img src="https://opengraph.githubassets.com/1/chunxiaoxx/nautilus-compass" alt="托管版 Jev 校准研究" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/chunxiaoxx/nautilus-compass/blob/main/docs/wall/GENESIS_HOSTED_JEV_CALIBRATION.md">托管版 Jev 校准研究</a></b><br><sub>chunxiaoxx · GitHub · ⭐ 207 仓库 · 2026-04-27</sub><br>对托管版 jev-1.13.0 的可复现校准研究：240 道带种子的问题（准确率 92.2%，Noul 题上 Brier 0.048、ECE 0.041），另有一轮 200 道题的对抗性跟进测试，ECE 为 0.012。<br><sub>相关: <a href="https://github.com/chunxiaoxx/nautilus-compass/blob/main/docs/wall/GENESIS_HOSTED_JEV_ADVCAL.md">adversarial</a> · <a href="https://github.com/chunxiaoxx/nautilus-compass/tree/main/runtime/jev_advcal_20260922">code</a> · <a href="https://github.com/chunxiaoxx/nautilus-compass">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/scienthoon/jev-ood-calibration"><img src="https://opengraph.githubassets.com/1/scienthoon/jev-ood-calibration" alt="Jev 知道自己不知道吗？" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/scienthoon/jev-ood-calibration">Jev 知道自己不知道吗？</a></b><br><sub>scienthoon · GitHub · ⭐ 4 · 2026-09-19</sub><br>对 Jev 的校准测试：900 张它不可能见过的规则生成客服工单，外加三个公开基准，并附原始响应；在公开数据集上接近校准，在规则无从得知的地方则过度自信。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/chenmingtang830/jevarena"><img src="https://jevarena-lab.vercel.app/og-image.png" alt="JevArena" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/chenmingtang830/jevarena">JevArena</a></b><br><sub>chenmingtang830 · GitHub · ⭐ 4 · 2026-09-19</sub><br>自带 key 的竞技场，就你的问题让 Jev 与 OpenRouter 上另一个评判模型对决，先让你投票再揭晓哪个是哪个，同时显示延迟和成本。<br><sub>相关: <a href="https://jevarena-lab.vercel.app">app</a> · <a href="https://jevarena-lab.vercel.app">app 2</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://www.reddit.com/r/LocalLLM/comments/1wl0wyr/benchmarked_typesafes_decision_model_jev_vs/"><img src="https://external-preview.redd.it/nGd0jUCYN79vEjP-jsIWFeaYmT1rlyOztmJb1MN8jcM.png?auto=webp&amp;s=212db4efbf345f508cce40389cae7198a105d8f9" alt="DecaState：Jev 对比前沿 LLM" width="240"></a></td>
<td valign="top"><b><a href="https://www.reddit.com/r/LocalLLM/comments/1wl0wyr/benchmarked_typesafes_decision_model_jev_vs/">DecaState：Jev 对比前沿 LLM</a></b><br><sub>Super_Public_8335 · Reddit · ▲ 1 · 2026-09-19</sub><br>在 36 个客服分拣决策上，从 US-West 和新加坡两地对比 Jev 与四个前沿 LLM：比 GPT-6 Astra 约便宜 176 倍、快 9 倍，类型错误为 0。<br><sub>相关: <a href="https://github.com/tempomesh/DecaState">repo</a> · <a href="https://github.com/tempomesh/decastate">project</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://idlerambling.substack.com/p/does-jev-have-politics-yes"><img src="https://substackcdn.com/image/fetch/$s_!59CN!,w_1200,h_675,c_fill,f_jpg,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9ecaa9e3-e48f-441a-aa60-c8bfb02c6734_1790x1458.png" alt="Jev 有政治立场吗？（有）" width="240"></a></td>
<td valign="top"><b><a href="https://idlerambling.substack.com/p/does-jev-have-politics-yes">Jev 有政治立场吗？（有）</a></b><br><sub>Idle Rambling · 文章 · ▲ 1 · 2026-09-20</sub><br>把 Political Compass 的命题作为 Choice 问题交给 Jev，发现它有稳定的政治立场，且与大多数 LLM 一致，据此认为它只是同一底层模型上的一副新的概率面具。<br><sub>相关: <a href="https://news.ycombinator.com/item?id=49781262">discussion</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/goya4140/jev-reward-model-evaluation"><img src="https://raw.githubusercontent.com/goya4140/jev-reward-model-evaluation/main/assets/headline_comparison.svg" alt="把 Jev 1.13 当作奖励模型" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/goya4140/jev-reward-model-evaluation">把 Jev 1.13 当作奖励模型</a></b><br><sub>goya4140 · GitHub · ⭐ 3 · 2026-09-20</sub><br>可复现的评测：在八个基准赛道、40,940 个样本上把 Jev 1.13 当作奖励模型、LLM 评判器和过程验证器，并附一份包含 54 项 SOTA 对比的交互式报告。<br><sub>相关: <a href="https://goya4140.github.io/jev-reward-model-evaluation/">report</a> · <a href="https://goya4140.github.io/jev-reward-model-evaluation">write-up</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/RINNECODER/jev-behavior-study"><img src="https://opengraph.githubassets.com/1/RINNECODER/jev-behavior-study" alt="jev-behavior-study" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/RINNECODER/jev-behavior-study">jev-behavior-study</a></b><br><sub>RINNECODER · GitHub · ⭐ 3 · 2026-09-16</sub><br>独立整理的 Jev 1.13.0 行为指南，基于 11,621 次文本研究请求、3 项 Snake 研究和一个 3D City 实验，展示措辞框架在哪些地方会改变答案、更难的任务在哪里失败。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/jmanhype/jev-dspy-lab"><img src="https://opengraph.githubassets.com/1/jmanhype/jev-dspy-lab" alt="jev-dspy-lab" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/jmanhype/jev-dspy-lab">jev-dspy-lab</a></b><br><sub>jmanhype · GitHub · ⭐ 3 · 2026-09-17</sub><br>DSPy 流水线的配套实验室，录制并回放 TypeSafe 调用，离线测量 Jev 的校准、选择性风险、按置信度把关的弃权、延迟、token 和估算成本。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/SamuelSacco/jev-exploration"><img src="https://opengraph.githubassets.com/1/SamuelSacco/jev-exploration" alt="jev-exploration" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/SamuelSacco/jev-exploration">jev-exploration</a></b><br><sub>SamuelSacco · GitHub · ⭐ 3 · 2026-09-17</sub><br>Jev 宣称的证据台账：结合样本量噪声重新计算公开的校准结果，并跑了一个 800 条的难度梯度实验，发现在任何难度下概率都没有校准好。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/anisselbd/jev-phishing-bench"><img src="https://opengraph.githubassets.com/1/anisselbd/jev-phishing-bench" alt="jev-phishing-bench" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/anisselbd/jev-phishing-bench">jev-phishing-bench</a></b><br><sub>anisselbd · GitHub · ⭐ 3 · 2026-09-16</sub><br>可复现的基准测试，在 2,000 封邮件上比较 Jev 与 Claude Haiku 4.5 判断邮件 agent 是否应该点击其中链接的能力，Jev 准确率 62.6%，Haiku 为 81.3%，并附校准审计。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/jevals/jevals-data"><img src="https://repository-images.githubusercontent.com/1376455544/1e0c26c8-9ea1-4d3a-a162-dec02fa78fe1" alt="Jevals" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/jevals/jevals-data">Jevals</a></b><br><sub>jevals · GitHub · ▲ 1 · 2026-09-18</sub><br>独立基准数据，在 PubMedQA、Banking77 和 HelpSteer2 上对照人工标签比较 Jev 与六个 LLM，涵盖准确率、校准、成本和延迟。<br><sub><b>Jev 用法:</b> 2026-09-18 版本：Jev 在 PubMedQA 是非题上与最好的 LLM 打平，价格只有 1/28，在 Banking77 上并列第二；在 HelpSteer2 上没有模型胜过瞎猜。</sub><br><sub>相关: <a href="https://jevals.com">app</a> · <a href="https://jevals.com/">app 2</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://www.southbridge.ai/blog/jev-watching-the-agents"><img src="https://www.southbridge.ai/images/og/jev-watching-the-agents.png" alt="用模型监视模型" width="240"></a></td>
<td valign="top"><b><a href="https://www.southbridge.ai/blog/jev-watching-the-agents">用模型监视模型</a></b><br><sub>Southbridge AI · 文章 · ▲ 1 · 2026-09-19</sub><br>在 220,000 次 agent 工具调用中标出高风险调用，展示编码技巧能绕过它，并发现用文字描述的等级比 1 到 100 的打分效果更好。<br><sub>相关: <a href="https://news.ycombinator.com/item?id=49783694">discussion</a> · <a href="https://x.com/hrishioa/status/2101842370052669903">post</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/miptgirl/miptgirl_medium/tree/main/jev"><img src="https://opengraph.githubassets.com/1/miptgirl/miptgirl_medium" alt="Jev 分类基准" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/miptgirl/miptgirl_medium/tree/main/jev">Jev 分类基准</a></b><br><sub>miptgirl · GitHub · ⭐ 109 仓库 · 2023-01-28</sub><br>用 notebook 在 Banking77 意图分类和 StackExchange 数据上把 Jev 与 GPT 模型做基准对比；在 1,000 个 Banking77 样本上，Jev 准确率为 0.790，gpt-5.6-luna 为 0.862。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/TokenTrim/jev-agent-failure-benchmark"><img src="https://raw.githubusercontent.com/TokenTrim/jev-agent-failure-benchmark/main/figures/whowhen_jev_vs_llm.png" alt="jev-agent-failure-benchmark" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/TokenTrim/jev-agent-failure-benchmark">jev-agent-failure-benchmark</a></b><br><sub>TokenTrim · GitHub · ⭐ 2 · 2026-09-17</sub><br>在 Who&amp;When Pro 的 6,257 条文本 trace 上对 Jev 做的基准测试，把多 agent 失败归因到具体 agent、步骤和错误类型；Jev 在每个维度上都胜过 GPT-5.4，总花费约 $1.28。<br><sub><b>Jev 用法:</b> 每条 trace 问三个 Choice 问题，分别在候选 agent、步骤和错误类型中选择。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/jgridifier/jev-research-eval"><img src="https://opengraph.githubassets.com/1/jgridifier/jev-research-eval" alt="jev-research-eval" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/jgridifier/jev-research-eval">jev-research-eval</a></b><br><sub>jgridifier · GitHub · ⭐ 2 · 2026-09-17</sub><br>用 jev-ultrafast 执行研究型浏览器任务的可复现评测 harness 和一线笔记，包含 11 个基线用例、人工和量化压力测试套件、QC 评级、套件运行器和报告生成器。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/TokenTrim/jev-routing-experiment"><img src="https://raw.githubusercontent.com/TokenTrim/jev-routing-experiment/main/results/llmrb_frontier.png" alt="jev-routing-experiment" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/TokenTrim/jev-routing-experiment">jev-routing-experiment</a></b><br><sub>TokenTrim · GitHub · ⭐ 2 · 2026-09-17</sub><br>在 LLMRouterBench 和 RouterArena 上测试把 Jev 用作 LLM 路由器；“Jev 难度判断加检索”的路由器得分 62.4%，最佳单模型为 60.3%，但去掉 Jev 的消融版本也能打平。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Gaurav-Gosain/jev-sec-bench"><img src="https://raw.githubusercontent.com/Gaurav-Gosain/jev-sec-bench/main/docs/overview.png" alt="jev-sec-bench" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Gaurav-Gosain/jev-sec-bench">jev-sec-bench</a></b><br><sub>Gaurav-Gosain · GitHub · ⭐ 2 · 2026-09-16</sub><br>针对 jev-1.13.0 的盲测安全基准，附 Go 运行器和 TUI：在全部 662 条 deepset 提示词注入消息上，以普通的 0.50 阈值取得 96.5% 的准确率，另有 200 对含漏洞的代码。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/dhruv_ko/status/2102185971332878453"><img src="https://pbs.twimg.com/media/HSx241aacAAAYyH.jpg" alt="Jev 对比 LLM、BERT 和 Laya" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/dhruv_ko/status/2102185971332878453">Jev 对比 LLM、BERT 和 Laya</a></b><br><sub>dhruv_ko · 文章 · ♥ 1 · 2026-09-21</sub><br>一个医疗语音 AI 团队在 1,500 个样本上把 Jev 与 Claude Sonnet 5、GPT-5-mini、一个微调过的 BERT 和两个开源权重模型对比，发现它以 1/50 的成本达到接近前沿的准确率。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/nekuda-ai/WindTunnel/tree/main/experiments/jev"><img src="https://raw.githubusercontent.com/nekuda-ai/WindTunnel/main/assets/charts/balanced-leaderboard.svg" alt="WindTunnel 的 Jev 实验" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/nekuda-ai/WindTunnel/tree/main/experiments/jev">WindTunnel 的 Jev 实验</a></b><br><sub>nekuda-ai · GitHub · ⭐ 76 仓库 · 2026-07-27</sub><br>WebMCP 基准运行：由 Jev 选择浏览器动作，Mercury 负责写参数和答案；通过 WebMCP，这一组合解出 49/49 个任务，每次运行中位成本 $0.0011，而通过 DOM 控制只解出 25/49。<br><sub>相关: <a href="https://github.com/nekuda-ai/WindTunnel">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/phuryn/experiments/tree/main/jev-decisions-api"><img src="https://opengraph.githubassets.com/1/phuryn/experiments" alt="Jev 更便宜也更好吗？" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/phuryn/experiments/tree/main/jev-decisions-api">Jev 更便宜也更好吗？</a></b><br><sub>phuryn · GitHub · ⭐ 52 仓库 · 2026-06-10</sub><br>可复现的发票分类测试，50 份文档特意设计成表面线索会误导判断：Jev 得分 50/50，每 1,000 次决策 $0.025，与 Claude Haiku 4.5 持平，两个开源模型为 48/50。<br><sub>相关: <a href="https://github.com/phuryn/experiments">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Adkid-Zephyr/chinese-workflow-decision-bench"><img src="https://raw.githubusercontent.com/Adkid-Zephyr/chinese-workflow-decision-bench/main/assets/xiaohongshu-scorecard-3x4.png" alt="chinese-workflow-decision-bench" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Adkid-Zephyr/chinese-workflow-decision-bench">chinese-workflow-decision-bench</a></b><br><sub>Adkid-Zephyr · GitHub · ⭐ 1 · 2026-09-21</sub><br>飞书风格的中文消息分类基准，包含 64 个冻结的合成场景，Jev 用单个 Choice 分对了 64/64，Laya 为 20/64，并公开了延迟和原始响应。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/shibadogcap/kyotsu-ai-bench"><img src="https://opengraph.githubassets.com/1/shibadogcap/kyotsu-ai-bench" alt="日本共通测试 AI 对比" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/shibadogcap/kyotsu-ai-bench">日本共通测试 AI 对比</a></b><br><sub>shibadogcap · GitHub · ⭐ 1 · 2026-09-16</sub><br>静态看板，在日本 2026 年大学入学共通测试 23 个科目的 836 道题上比较 Jev 与 OpenAI luna、terra、sol 等变体，包括速度和成本。<br><sub>相关: <a href="https://jev-luna-kyotsu-bench.shibadogcap.com">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://huggingface.co/spaces/aahf/JevBenchmark"><img src="https://huggingface.co/spaces/aahf/JevBenchmark/resolve/main/assets/cost_quality.png" alt="Jev 基准测试（广告）" width="240"></a></td>
<td valign="top"><b><a href="https://huggingface.co/spaces/aahf/JevBenchmark">Jev 基准测试（广告）</a></b><br><sub>aahf · 应用 · ♥ 1 · 2026-09-17</sub><br>研究文章，在四种合成广告结果上比较 Jev 与 GPT-5.6 Sol 以及四个 XGBoost 基线：整体质量相近，估算 API 成本约低 64 倍，中位延迟低 5.4 倍。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/CompleteDotTech/paper-package"><img src="https://opengraph.githubassets.com/1/CompleteDotTech/paper-package" alt="Jev 研究论文包" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/CompleteDotTech/paper-package">Jev 研究论文包</a></b><br><sub>CompleteDotTech · GitHub · ⭐ 1 · 2026-09-18</sub><br>关于改进 Jev 决策的可复现研究包：在 413 个 DBLP-ACM 实体对上，实体匹配的 macro-F1 从 0.9605 提升到 0.9859，而 SciFact 关系验证没有显示出确定的提升。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/jjd-lab/jev-synthetic-survey"><img src="https://jjd-lab.github.io/jev-synthetic-survey/assets/og.png" alt="Jev 合成问卷调查" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/jjd-lab/jev-synthetic-survey">Jev 合成问卷调查</a></b><br><sub>jjd-lab · GitHub · ⭐ 1 · 2026-09-20</sub><br>研究：让 Jev 和 GPT-4.1 扮演同样的 300 名合成受访者，覆盖 24,596 个 Twin-2K-500 单元格，发现把是非题以 Noul 形式提问比模型之间的差距影响更大，而成本只有三十四分之一。<br><sub>相关: <a href="https://jjd-lab.github.io/jev-synthetic-survey/">article</a> · <a href="https://jjd-lab.github.io/jev-synthetic-survey">write-up</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/henrylove0/status/2102239256093794663"><img src="https://pbs.twimg.com/media/HSynVzubYAAgXmA.png?name=orig" alt="Jev 与 Laya 正面对比" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/henrylove0/status/2102239256093794663">Jev 与 Laya 正面对比</a></b><br><sub>henrylove0 · X · ♥ 1 · 2026-09-22</sub><br>Jev 与开源 Laya 模型的并排运行，显示 Laya 快得多，而 Jev 的判断质量好得多。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/cruzex100/status/2102202098968666432"><img src="https://pbs.twimg.com/media/HSyFqylbgAAxJYA.jpg?name=orig" alt="Jev 与 Laya 冒烟测试" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/cruzex100/status/2102202098968666432">Jev 与 Laya 冒烟测试</a></b><br><sub>cruzex100 · X · ♥ 1 · 2026-09-22</sub><br>Jev 与开源 Laya 模型的快速并排对比：Jev 准确率 0.727；软准确率 0.580 对 0.471，ECE 0.144 对 0.213，延迟约 710 毫秒 对约 30-40 毫秒，每次决策约 $0.0004 对约 $0。</td>
</tr>
<tr>
<td width="260" valign="top"></td>
<td valign="top"><b><a href="https://gist.github.com/ipaulsmith/e5c3ae3a492a455435d5bfc161404312">用 Jev 回测 NASA Kepler 数据</a></b><br><sub>ipaulsmith · GitHub · ⭐ 1</sub><br>对 Jev 1.13 的回溯测试：在 8,054 个历史 Kepler 关注天体（KOI）上隐藏存档中的判定结果，Jev 与其中 72.5% 相符，固定的 3 条规则基线为 64.4%。<br><sub><b>Jev 用法:</b> 公开了确切的请求、指标、基线和注意事项。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/themsquared/jev-benchmark"><img src="https://webofmike.com/images/og-default.png" alt="jev-benchmark" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/themsquared/jev-benchmark">jev-benchmark</a></b><br><sub>themsquared · GitHub · ⭐ 1 · 2026-09-17</sub><br>可复现的基准测试，让 Jev 把 agent 工具调用分为只读、破坏性、特权和数据外泄四类，测量准确率、延迟以及其置信度是否值得用来做路由，原始结果已提交到仓库。<br><sub>相关: <a href="https://webofmike.com/jev-benchmark/">writeup</a> · <a href="https://webofmike.com/jev-benchmark">write-up</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/baibizhe/jev-decision-benchmarks"><img src="https://opengraph.githubassets.com/1/baibizhe/jev-decision-benchmarks" alt="jev-decision-benchmarks" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/baibizhe/jev-decision-benchmarks">jev-decision-benchmarks</a></b><br><sub>baibizhe · GitHub · ⭐ 1 · 2026-09-19</sub><br>在 MetaTool、When2Call 和 BFCL V4 的工具选择与弃权任务上对 Jev 1.13 的独立评测，附与 ChatGPT、Claude、Qwen 等模型对比的双语表格。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/4esv/jev-eval"><img src="https://raw.githubusercontent.com/4esv/jev-eval/main/results/confidence.png" alt="jev-eval" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/4esv/jev-eval">jev-eval</a></b><br><sub>4esv · GitHub · ⭐ 1 · 2026-09-18</sub><br>在带标注的分类数据上把 Jev 与任意 OpenRouter 模型或本地检查点对比的 harness，测量准确率、校准、延迟和成本，并给出与 GPT-5.6 Terra、open-jev、Kev-0.8B 和 Laya 的对比结果。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/copyleftdev/jev-labs"><img src="https://opengraph.githubassets.com/1/copyleftdev/jev-labs" alt="jev-labs" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/copyleftdev/jev-labs">jev-labs</a></b><br><sub>copyleftdev · GitHub · ⭐ 1 · 2026-09-19</sub><br>围绕 Jev 构建、经 TLA+ 验证的共识内核，生成为 Rust 代码，在带种子的混沌注入下对真实 API 跑了 1,680 个模拟药房决策，零错误裁决，且证据质量下降时升级处理的次数随之增加。<br><sub>相关: <a href="https://www.youtube.com/watch?v=C_l8FI1oddE">video</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/zsavage8/padflow-jev-evals"><img src="https://opengraph.githubassets.com/1/zsavage8/padflow-jev-evals" alt="padflow-jev-evals" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/zsavage8/padflow-jev-evals">padflow-jev-evals</a></b><br><sub>zsavage8 · GitHub · ⭐ 1 · 2026-09-17</sub><br>公开基准，收录一家土地开发 SaaS 在生产中做出的类型化决策，比如把收到的文档路由到对应项目，附 JSON schema、匿名化的标注数据和适用于 OpenAI 兼容模型的运行器。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/markfive-proto/typesafe-vs-deepseek"><img src="https://opengraph.githubassets.com/1/markfive-proto/typesafe-vs-deepseek" alt="typesafe-vs-deepseek" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/markfive-proto/typesafe-vs-deepseek">typesafe-vs-deepseek</a></b><br><sub>markfive-proto · GitHub · ⭐ 1 · 2026-09-18</sub><br>在发票抽取、邮件分类和重排，以及欺诈、护栏和对账流水线上，并排比较 Jev 与 DeepSeek flash 的速度、token、成本和准确率。<br><sub>相关: <a href="https://typesafe-vs-deepseek.vercel.app">app</a> · <a href="https://typesafe-vs-deepseek.vercel.app">app 2</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/alp82/goodwatch-monorepo/tree/main/docs/benchmarks/fingerprint/jev"><img src="https://opengraph.githubassets.com/1/alp82/goodwatch-monorepo" alt="GoodWatch 的 Jev 指纹实验" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/alp82/goodwatch-monorepo/tree/main/docs/benchmarks/fingerprint/jev">GoodWatch 的 Jev 指纹实验</a></b><br><sub>alp82 · GitHub · ⭐ 38 仓库 · 2026-09-17</sub><br>来自观影推荐应用 GoodWatch 的案例研究，测试用 Jev 给每部作品打 74 项特征分：快了 10 到 25 倍，但与经人工审核的 Qwen 分数平均相差 2.65 分，团队因此决定不采用。<br><sub><b>Jev 用法:</b> 对比了十级和六级 Score 等级、判断特征是否存在的 Noul，以及每次请求 1 到 222 个问题的不同批量大小。</sub><br><sub>相关: <a href="https://github.com/alp82/goodwatch-monorepo">repo</a> · <a href="https://github.com/alp82/goodwatch-monorepo/blob/main/docs/adr/0001-no-jev-for-fingerprint-scoring.md">adr</a> · <a href="https://goodwatch.app/">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/hakari-bench/hakari-bench/blob/main/docs/typesafe_reranker_evaluation.md"><img src="https://opengraph.githubassets.com/1/hakari-bench/hakari-bench" alt="HAKARI-Bench 的 Jev 重排器" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/hakari-bench/hakari-bench/blob/main/docs/typesafe_reranker_evaluation.md">HAKARI-Bench 的 Jev 重排器</a></b><br><sub>hakari-bench · GitHub · ⭐ 32 仓库 · 2026-04-30</sub><br>Jev 在 HAKARI-Bench（覆盖 35+ 个基准组的轻量级信息检索基准）中的集成，用 Noul 相关性概率以 listwise 或 pointwise 模式给文档排序，模型固定为 jev-1.13.0。<br><sub>相关: <a href="https://github.com/hakari-bench/hakari-bench">repo</a> · <a href="https://huggingface.co/spaces/hakari-bench/leaderboard">leaderboard</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/brcampidelli/chimera-agent/blob/main/bench/jev_decisions/RESULTS.md"><img src="https://opengraph.githubassets.com/1/brcampidelli/chimera-agent" alt="Chimera 的 Jev 治理基准" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/brcampidelli/chimera-agent/blob/main/bench/jev_decisions/RESULTS.md">Chimera 的 Jev 治理基准</a></b><br><sub>brcampidelli · GitHub · ⭐ 26 仓库 · 2026-06-30</sub><br>Chimera agent 仓库中的预注册基准测试，比较 Jev（一个危险性 Noul 加一个 block/review/allow 的 Choice）、DeepSeek 评判器和口头表述的概率；在模糊条目上 Jev 的 AUROC 达到 0.903。<br><sub>相关: <a href="https://github.com/brcampidelli/chimera-agent">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/ucsandman/claude-harness/blob/main/labs/claude-mods/experiments/jev/FINDINGS.md"><img src="https://opengraph.githubassets.com/1/ucsandman/claude-harness" alt="在真实对话记录上用 Jev 推荐 skill" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/ucsandman/claude-harness/blob/main/labs/claude-mods/experiments/jev/FINDINGS.md">在真实对话记录上用 Jev 推荐 skill</a></b><br><sub>ucsandman · GitHub · ⭐ 24 仓库 · 2026-08-13</sub><br>测量 Jev 每轮挑选正确 skill 的效果：从 838 份 Claude Code 对话记录中挖出 407 个 skill 和 356 轮，错误加载率 73.3%，关键词基线为 96.5%，并指出首次调用的召回率是上限所在。<br><sub>相关: <a href="https://github.com/ucsandman/claude-harness">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/ibm-client-engineering/output-drift-financial-llms/blob/main/paper/arxiv_dfah_bench_v3/v3_extension.tex"><img src="https://opengraph.githubassets.com/1/ibm-client-engineering/output-drift-financial-llms" alt="DFAH-Bench 的 Jev 关卡条件" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/ibm-client-engineering/output-drift-financial-llms/blob/main/paper/arxiv_dfah_bench_v3/v3_extension.tex">DFAH-Bench 的 Jev 关卡条件</a></b><br><sub>ibm-client-engineering · GitHub · ⭐ 18 仓库 · 2025-11-02</sub><br>IBM Client Engineering 面向金融 agent 的 DFAH-Bench 的研究扩展，比较几种动作关卡：仅做结构检查、由 LLM 输出 allow/block/review 的 JSON 判断，以及 Jev 带类别概率的类型化选择。<br><sub>相关: <a href="https://github.com/ibm-client-engineering/output-drift-financial-llms">repo</a> · <a href="https://ibm-client-engineering.github.io/output-drift-financial-llms/">site</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/getaskclaw/amber/tree/main/decision-axis"><img src="https://opengraph.githubassets.com/1/getaskclaw/amber" alt="AMBER 决策轴评测" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/getaskclaw/amber/tree/main/decision-axis">AMBER 决策轴评测</a></b><br><sub>getaskclaw · GitHub · ⭐ 15 仓库 · 2026-08-20</sub><br>AMBER 回放基准中针对 Jev 等决策模型的评测流水线，基于 HMAC 签名的记录报告各类别准确率、校准分箱、ECE、阈值扫描以及成本/延迟。<br><sub>相关: <a href="https://github.com/getaskclaw/amber">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/XiaoConstantine/sgrep/tree/main/bench/jev"><img src="https://raw.githubusercontent.com/XiaoConstantine/sgrep/main/docs/static/architecture.jpg" alt="sgrep 的 Jev 重排基准" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/XiaoConstantine/sgrep/tree/main/bench/jev">sgrep 的 Jev 重排基准</a></b><br><sub>XiaoConstantine · GitHub · ⭐ 15 仓库 · 2025-11-25</sub><br>sgrep（一个面向代码库和编程 agent 历史的本地语义搜索工具）中的独立基准，让 Jev 经由其重排接口运行，并在固定版本的 dspy-go 索引上与本地 Jina、ColBERT 等重排器对比。<br><sub>相关: <a href="https://github.com/XiaoConstantine/sgrep">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/daiwk/auto-research/tree/main/src/auto_research/system_one"><img src="https://opengraph.githubassets.com/1/daiwk/auto-research" alt="auto-research System One" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/daiwk/auto-research/tree/main/src/auto_research/system_one">auto-research System One</a></b><br><sub>daiwk · GitHub · ⭐ 14 仓库 · 2026-07-13</sub><br>一个研究模块，实现了 Choice/Score/Noul 接口约定，并在 Banking77 和公开评测集上把 Jev 与本地校准打分器以及 NanoJev、Nimble、Laya 检查点做对比评测。<br><sub><b>Jev 用法:</b> 一个无依赖的 TypeSafe HTTP provider，与本地后端和开源检查点后端共用同一套接口约定，另附 48 个社区实现的目录。</sub><br><sub>相关: <a href="https://github.com/daiwk/auto-research">repo</a> · <a href="https://github.com/daiwk/auto-research/blob/main/docs/system-one/README.md">docs</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://huggingface.co/datasets/emretheus/jev-rag-benchmark"><img src="https://cdn-thumbnails.huggingface.co/social-thumbnails/datasets/emretheus/jev-rag-benchmark.png" alt="Jev RAG Benchmark" width="240"></a></td>
<td valign="top"><b><a href="https://huggingface.co/datasets/emretheus/jev-rag-benchmark">Jev RAG Benchmark</a></b><br><sub>emretheus · Hugging Face · ⬇ 21 · 2026-09-20</sub><br>冻结候选集的 RAG 评测，把 Jev 1.13 作为重排器与 OpenJev 和一个 NVIDIA 交叉编码器对比：在 SciFact 上 Jev 的 nDCG@10 为 79.29%，对手为 78.70%，但 p50 延迟约 4 秒对比 307 毫秒。<br><sub>相关: <a href="https://github.com/emretheus/jev-rag-benchmark">project</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/bryansparks/armature/tree/main/examples/decision-typesafe"><img src="https://raw.githubusercontent.com/bryansparks/armature/main/demo-hero.gif" alt="Armature 的 TypeSafe 决策 A/B 测试" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/bryansparks/armature/tree/main/examples/decision-typesafe">Armature 的 TypeSafe 决策 A/B 测试</a></b><br><sub>bryansparks · GitHub · ⭐ 9 仓库 · 2026-05-07</sub><br>在 Armature agent harness 内对 20 条带标注的代码审查陈述做 A/B 基准测试：Jev 总分 0.87，qwen3.6-27b 评判器为 0.98，每次调用耗时 260 毫秒 对比 20,591 毫秒。<br><sub>相关: <a href="https://armature.now">app</a> · <a href="https://github.com/bryansparks/armature">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/ensemblr-hq/ensemblr/blob/master/docs/considerations/jev-decision-layer.md"><img src="https://raw.githubusercontent.com/ensemblr-hq/ensemblr/master/assets/wordmark.gif" alt="Ensemblr 的 Jev 决策层研究" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/ensemblr-hq/ensemblr/blob/master/docs/considerations/jev-decision-layer.md">Ensemblr 的 Jev 决策层研究</a></b><br><sub>ensemblr-hq · 文档 · ⭐ 8 仓库 · 2026-06-04</sub><br>设计提案和技术探针：在一个面向 Pi 和 Claude Code 的桌面编排器里用 Jev 挑选 agent 角色、评估难度并标记重复项；修正后重跑的结果仍不支持用于生产，提案因此被否决。<br><sub>相关: <a href="https://github.com/ensemblr-hq/ensemblr">repo</a> · <a href="https://github.com/ensemblr-hq/ensemblr/blob/master/docs/considerations/jev-spike-runbook.md">runbook</a> · <a href="https://www.ensemblr.dev">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/hevmind/status/2101110454785614219"><img src="https://hevmind.com/og-image.png" alt="Jev 当重排器（hev mind）" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/hevmind/status/2101110454785614219">Jev 当重排器（hev mind）</a></b><br><sub>hevmind · X · ▶ 32 · 2026-09-19</sub><br>未经调优的 Jev 重排器平均 nDCG@10 达到 0.501，Voyage rerank-3 为 0.504，所用提示词只在 SciFact 的训练集上调过。<br><sub>相关: <a href="https://hevmind.com/writing/jev-as-a-reranker/">article</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/fstandhartinger/model-market-comparison/tree/main/ops/ux-2026-09-12/jevbench"><img src="https://raw.githubusercontent.com/fstandhartinger/model-market-comparison/main/public/brand/wordmark.svg" alt="JevBench (Benchmark Heaven)" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/fstandhartinger/model-market-comparison/tree/main/ops/ux-2026-09-12/jevbench">JevBench (Benchmark Heaven)</a></b><br><sub>fstandhartinger · GitHub · ⭐ 5 仓库 · 2026-06-15</sub><br>LLM 价格与基准对比网站 Benchmark Heaven 中针对 Jev 及类 Jev 决策模型的基准测试，公开任务集和留出任务集的结果分开报告。<br><sub>相关: <a href="https://github.com/fstandhartinger/model-market-comparison">repo</a> · <a href="https://benchmarkheaven.com">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://zenn.dev/acrosstudioblog/articles/a62c066d5d9938"><img src="https://res.cloudinary.com/zenn/image/upload/s--DfX5i98Y--/c_fit%2Cg_north_west%2Cl_text:notosansjp-medium.otf_55:%25E6%2596%2587%25E7%25AB%25A0%25E3%2582%2592%25E7%2594%259F%25E6%2588%2590%25E3%2581%2597%25E3%2581%25AA%25E3%2581%2584AI%25E3%2580%258CJev%25E3%2580%258D%25E3%2582%2592%25E6%2597%25A5%25E6%259C%25AC%25E8%25AA%259E%25E3%2581%25A748%25E5%259B%259E%25E8%25A9%25A6%25E3%2581%2597%25E3%2581%259F%25E3%2580%2582%25E9%2580%259F%25E3%2581%2595%25E3%2582%2588%25E3%2582%258A%25E9%259D%25A2%25E7%2599%25BD%25E3%2581%258B%25E3%2581%25A3%25E3%2581%259F%25E3%2581%25AE%25E3%2581%25AF%25E3%2580%258C%25E8%25BF%25B7%25E3%2581%2584%25E3%2580%258D%2Cw_1010%2Cx_90%2Cy_100/g_south_west%2Cl_text:notosansjp-medium.otf_34:%25E3%2582%25B7%25E3%2583%25B3%25E3%2582%25A6%25E3%2583%2595%25E3%2583%25A0%2528wooheum%2520xin%2529%2Cx_220%2Cy_108/bo_3px_solid_rgb:d6e3ed%2Cg_south_west%2Ch_90%2Cl_fetch:aHR0cHM6Ly9zdGF0aWMuemVubi5zdHVkaW8vdXNlci11cGxvYWQvYXZhdGFyLzQxMjhmMzRjMjIuanBlZw==%2Cr_20%2Cw_90%2Cx_92%2Cy_102/co_rgb:6e7b85%2Cg_south_west%2Cl_text:notosansjp-medium.otf_30:Acrosstudio%25E3%2583%2586%25E3%2583%2583%25E3%2582%25AF%25E3%2583%2596%25E3%2583%25AD%25E3%2582%25B0%2Cx_220%2Cy_160/bo_4px_solid_white%2Cg_south_west%2Ch_50%2Cl_fetch:aHR0cHM6Ly9zdGF0aWMuemVubi5zdHVkaW8vdXNlci11cGxvYWQvYXZhdGFyLzgwMjc2NjQyOTMuanBlZw==%2Cr_max%2Cw_50%2Cx_139%2Cy_84/v1627283836/default/og-base-w1200-v2.png?_a=BACMTiAE" alt="用日语调用 Jev 48 次" width="240"></a></td>
<td valign="top"><b><a href="https://zenn.dev/acrosstudioblog/articles/a62c066d5d9938">用日语调用 Jev 48 次</a></b><br><sub>Wooheum Xin (Acrosstudio) · 文章 · 2026-09-18</sub><br>日文测试：通过 OpenRouter 把 16 条合成客服消息各发 3 次，每次调用问三个问题，共 48 次调用，中位延迟 286 毫秒，总花费约 $0.00146，标签有分歧的地方置信度也低。</td>
</tr>
<tr>
<td width="260" valign="top"></td>
<td valign="top"><b><a href="https://evals.typesafe.ai/agent_trace_observability">Agent Trace 可观测性工作流评测</a></b><br><sub>TypeSafe AI · 文档</sub><br>官方工作流评测：把已完成的客服 agent trace 分拣为后续跟进事项；Jev 得分 71.6%，每个案例 $0.0003、0.5 秒，而 Opus 5 为 75.2%、$0.1033、27.4 秒。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://lindfors.no/blog/a-first-look-at-typesafes-jev/"><img src="https://lindfors.no/og/a-first-look-at-typesafes-jev.png" alt="Jev 抢先体验测试" width="240"></a></td>
<td valign="top"><b><a href="https://lindfors.no/blog/a-first-look-at-typesafes-jev/">Jev 抢先体验测试</a></b><br><sub>Emil Lindfors · 文章 · 2026-09-18</sub><br>用 Score 问题给挪威语文档打分，每千条约 $0.22，发现更长、更详细的问题反而损害校准。<br><sub><b>Jev 用法:</b> 对 24 份挪威公开听证回复提出 Score 问题。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/jourdanlabs/assay-001"><img src="https://opengraph.githubassets.com/1/jourdanlabs/assay-001" alt="ASSAY-001" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/jourdanlabs/assay-001">ASSAY-001</a></b><br><sub>jourdanlabs · GitHub · 2026-09-17</sub><br>对 Jev 校准和类型安全宣称的预注册检验：在 CLINC150 上校准良好（ECE 0.0204），在 Banking77 上过度自信（ECE 0.0936），8,576 次响应中零类型错误，并公开完整日志。<br><sub>相关: <a href="https://donttrustme.ai/assay-001.html">article</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"></td>
<td valign="top"><b><a href="https://donttrustme.ai/assay-001.html">ASSAY-001：Jev 校准检验</a></b><br><sub>donttrustme.ai (JourdanLabs) · 文章 · 2026-09-17</sub><br>在 Banking77 和 CLINC150 上对 Jev 校准和类型安全宣称的预注册检验：在 CLINC150 上校准良好（ECE 0.0204），在 Banking77 上过度自信（ECE 0.0936），8,576 次响应中零类型错误。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://frederickparsons.substack.com/p/can-a-fast-ai-gate-catch-chemistry"><img src="https://substackcdn.com/image/fetch/$s_!WNmT!,w_1200,h_675,c_fill,f_jpg,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbafd27fe-42f4-4a3d-8ee9-16131e778995_1663x795.png" alt="快速 AI 关卡能抓住化学错误吗？" width="240"></a></td>
<td valign="top"><b><a href="https://frederickparsons.substack.com/p/can-a-fast-ai-gate-catch-chemistry">快速 AI 关卡能抓住化学错误吗？</a></b><br><sub>Frederick Parsons · 文章 · 2026-09-19</sub><br>一个文献断言关卡，在 95% 阈值下拦住了全部 42 条错误断言，并如实交代了分子检查在哪些地方失败。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://zenn.dev/nwn/articles/824026c76116e0"><img src="https://res.cloudinary.com/zenn/image/upload/s--nA63RXC3--/c_fit%2Cg_north_west%2Cl_text:notosansjp-medium.otf_55:TypeSafe%25E3%2581%25AEJev%25E3%2582%2592%25E6%25AD%25A3%25E3%2581%2597%25E3%2581%258F%25E9%25A9%259A%25E3%2581%258F%25E3%2580%2581%25E3%2581%259D%25E3%2582%258C%25E3%2581%25A3%25E3%2581%25A6LLM%25E3%2581%25A7%25E3%2581%25A7%25E3%2581%258D%25E3%2581%25BE%25E3%2581%259B%25E3%2582%2593%25E3%2581%258B%25EF%25BC%259F%2Cw_1010%2Cx_90%2Cy_100/g_south_west%2Cl_text:notosansjp-medium.otf_37:%25E3%2583%25A8%2Cx_203%2Cy_121/g_south_west%2Ch_90%2Cl_fetch:aHR0cHM6Ly9zdGF0aWMuemVubi5zdHVkaW8vdXNlci11cGxvYWQvYXZhdGFyLzllY2U3NmI3N2IuanBlZw==%2Cr_max%2Cw_90%2Cx_87%2Cy_95/v1627283836/default/og-base-w1200-v2.png?_a=BACMTiAE" alt="LLM 做不到 Jev 做的事吗？" width="240"></a></td>
<td valign="top"><b><a href="https://zenn.dev/nwn/articles/824026c76116e0">LLM 做不到 Jev 做的事吗？</a></b><br><sub>nwn · 文章 · 2026-09-17</sub><br>日文文章，在 Gemma3 270M 上用首 token logits 复现 Jev 的并行决策技巧（比 JSON 输出快 77 倍），并在一个公开的玩 Mario 的 harness 上比较 Jev 与 LLM。</td>
</tr>
<tr>
<td width="260" valign="top"></td>
<td valign="top"><b><a href="https://evals.typesafe.ai/customer_service">客服工作流评测</a></b><br><sub>TypeSafe AI · 文档</sub><br>官方工作流评测：在客户发言后为客服助手选择下一步动作；Jev 得分 76.0%，每个案例 $0.0001、0.4 秒，而 Opus 5 为 72.4%、$0.0579、16.6 秒。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/willkelly/jev-evaluation"><img src="https://opengraph.githubassets.com/1/willkelly/jev-evaluation" alt="评测 jev" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/willkelly/jev-evaluation">评测 jev</a></b><br><sub>willkelly · GitHub · 2026-09-20</sub><br>对 jev-1.13.0 的预注册对抗性评测，含九个实验和在拿到任何数据前就定下的 28 个预测，共运行 123,805 次请求、花费 $12.69，另根据结果总结出一份 13 条规则的提示词指南。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/thodoh1/FinancialPredictionJev"><img src="https://opengraph.githubassets.com/1/thodoh1/FinancialPredictionJev" alt="FinancialPredictionJev" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/thodoh1/FinancialPredictionJev">FinancialPredictionJev</a></b><br><sub>thodoh1 · GitHub · 2026-09-16</sub><br>一个 Python 脚本，基于 yfinance 数据用一个 Jev Noul 判断 SPY 次日是否收涨，再对照基线计算准确率、Brier 分数、ROC-AUC 和校准情况。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://kasra.blog/blog/classification-and-jev/"><img src="https://images.kasra.blog/images/wp-content/2026/09/jev-side-quests-og-v5.png" alt="本可以由 Jev 省掉的微调支线任务" width="240"></a></td>
<td valign="top"><b><a href="https://kasra.blog/blog/classification-and-jev/">本可以由 Jev 省掉的微调支线任务</a></b><br><sub>Kasra Rahjerdi · 文章 · 2026-09-18</sub><br>用三个 Noul 在 23 分钟内花 $3.47 过滤了 120,633 条训练样本。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://thoughts.jock.pl/p/jev-typesafe-system-one-model-benchmark-2026"><img src="https://substackcdn.com/image/fetch/$s_!aY6v!,w_1200,h_675,c_fill,f_jpg,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F880b6867-fc92-4181-9cac-73aeaf966630_2048x2048.png" alt="我把 40 张工单交给 Jev 和四个模型" width="240"></a></td>
<td valign="top"><b><a href="https://thoughts.jock.pl/p/jev-typesafe-system-one-model-benchmark-2026">我把 40 张工单交给 Jev 和四个模型</a></b><br><sub>Pawel Jozefiak · 文章 · 2026-09-21</sub><br>把 40 张客服工单交给 Jev 和四个文本模型：Jev 在 370 毫秒 内作答，只花百分之二美分，比 Claude Fable 5.1 快 10 倍、便宜 329 倍，在判断客户恼火程度上也胜过它。</td>
</tr>
<tr>
<td width="260" valign="top"></td>
<td valign="top"><b><a href="https://evals.typesafe.ai/invoice_processing">发票处理工作流评测</a></b><br><sub>TypeSafe AI · 文档</sub><br>官方工作流评测：判断一张发票能否支付以及如何支付；Jev 得分 61.8%，每个案例 $0.0011、0.5 秒，而 Opus 5 为 78.4%、$0.4856、92.1 秒。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://vercel.com/blog/ai-gateway-jev-model-launch"><img src="https://assets.vercel.com/image/upload/contentful/image/e5382hct74si/22MYVE2v97ZfHKIqNx5Sw6/d0e7b0b67c61e51ff3b8ca27ce16cf87/sep-og-blog-jev-launch_2x.jpg" alt="Jev 在 Vercel AI Gateway 上的采用情况" width="240"></a></td>
<td valign="top"><b><a href="https://vercel.com/blog/ai-gateway-jev-model-launch">Jev 在 Vercel AI Gateway 上的采用情况</a></b><br><sub>Vercel · 文章 · 2026-09-18</sub><br>来自 Vercel AI Gateway 的首日采用数据：24 小时内近 13% 的付费团队在用 Jev，约为 GPT-5.6 系列的 2 倍，是 Fable 5.1 份额的 6 倍多。<br><sub>相关: <a href="https://news.ycombinator.com/item?id=49774164">discussion</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://www.mindstudio.ai/blog/jev-system-one-model-classification"><img src="https://i.mscdn.ai/o/iZl0kkZU2R9KXyy7/a/3V2ICO3oSq2QZPii/generated-images/1f03e98a-0622-4dcb-b094-a54da1a98c90.png?fm=auto&amp;w=1200&amp;h=630&amp;fit=crop" alt="Jev AI 实测" width="240"></a></td>
<td valign="top"><b><a href="https://www.mindstudio.ai/blog/jev-system-one-model-classification">Jev AI 实测</a></b><br><sub>MindStudio (Luis Chavez-Mattos) · 文章 · 2026-09-18</sub><br>对 Jev 1.13.0 的动手测试，八个合成案例覆盖工单路由、否定句、提示词注入、“其他”选项和延迟，并说明它在哪些地方靠得住、哪些地方不行。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://huggingface.co/datasets/clduab11/jev-calibration-statistics"><img src="https://huggingface.co/datasets/clduab11/jev-calibration-statistics/resolve/main/calibration.png" alt="Jev 校准统计" width="240"></a></td>
<td valign="top"><b><a href="https://huggingface.co/datasets/clduab11/jev-calibration-statistics">Jev 校准统计</a></b><br><sub>clduab11 · Hugging Face · 2026-09-21</sub><br>由 jev-1.13.0 评判的检索基准的置信度统计：它的分数能区分出包含答案的段落（AUROC 0.899），但经 Jev 评判的流水线得分为 0.612，不用评判器时为 0.740。<br><sub>相关: <a href="https://github.com/clduab11/jev-test">project</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/ghubnab99/jev-enterprise-decision-fabric"><img src="https://opengraph.githubassets.com/1/ghubnab99/jev-enterprise-decision-fabric" alt="Jev Enterprise Decision Fabric" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/ghubnab99/jev-enterprise-decision-fabric">Jev Enterprise Decision Fabric</a></b><br><sub>ghubnab99 · GitHub · 2026-09-19</sub><br>实验性的 .NET 架构，让大量语义决策走同一条经过校验的路径，附一个 111 个带标注案例的基准（在 agent 动作上对比 Jev 与结构化输出的 Claude 基线）和一个决策检查器。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/vehas/thaiexam-jev-charts"><img src="https://opengraph.githubassets.com/1/vehas/thaiexam-jev-charts" alt="Jev 挑战 ThaiExam" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/vehas/thaiexam-jev-charts">Jev 挑战 ThaiExam</a></b><br><sub>vehas · GitHub · 2026-09-17</sub><br>图表页面，在泰国标准化考试上比较 jev-1.13.0 与其他 110 个模型：在 567 道题上准确率 70.7%，每题 0.35 秒、$0.000029，校准误差 7.5 个百分点。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/hegargarcia/jev-playground"><img src="https://opengraph.githubassets.com/1/hegargarcia/jev-playground" alt="Jev Playground" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/hegargarcia/jev-playground">Jev Playground</a></b><br><sub>hegargarcia · GitHub · 2026-09-17</sub><br>基准测试 playground，让 Jev 与 Luna、Haiku 和 Gemini 在显式 state 的游戏中比拼选招，游戏代码掌管规则和合法动作，每个模型只在其中做选择。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://huggingface.co/spaces/emretheus/jev-rag-benchmark-leaderboard"><img src="https://cdn-thumbnails.huggingface.co/social-thumbnails/spaces/emretheus/jev-rag-benchmark-leaderboard.png" alt="Jev RAG 基准排行榜" width="240"></a></td>
<td valign="top"><b><a href="https://huggingface.co/spaces/emretheus/jev-rag-benchmark-leaderboard">Jev RAG 基准排行榜</a></b><br><sub>emretheus · 应用 · 2026-09-20</sub><br>基于真实运行的静态排行榜，在英文 XQuAD 和 SciFact RAG 任务上比较 Jev 1.13、OpenJev 和一个 NVIDIA 交叉编码器作为重排器的表现。<br><sub>相关: <a href="https://github.com/emretheus/jev-rag-benchmark">project</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://medium.com/data-science-collective/i-tested-typesafes-jev-a-470-cheaper-decision-model-against-claude-gpt-6-kimi-minimax-and-d36ed152e861"><img src="https://miro.medium.com/v2/resize:fit:700/1*2bVSI4gUCmeUCE_-7obOAA.jpeg" alt="Jev 对比 Claude、GPT-6、Kimi、MiniMax 和 DeepSeek" width="240"></a></td>
<td valign="top"><b><a href="https://medium.com/data-science-collective/i-tested-typesafes-jev-a-470-cheaper-decision-model-against-claude-gpt-6-kimi-minimax-and-d36ed152e861">Jev 对比 Claude、GPT-6、Kimi、MiniMax 和 DeepSeek</a></b><br><sub>Manjunath Janardhan · 文章 · 2026-09-19</sub><br>把同样的 200 个类型化决策交给 Jev 和五个前沿 LLM，比较准确率和成本，并检查各模型如何处理人工标注者意见不一的案例。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/mameli/jev-vs-luna"><img src="https://raw.githubusercontent.com/mameli/jev-vs-luna/main/assets/benchmark-overview.png" alt="Jev 对比 Luna" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/mameli/jev-vs-luna">Jev 对比 Luna</a></b><br><sub>mameli · GitHub · 2026-09-18</sub><br>可复现的基准测试，通过 OpenRouter 的 Decisions API 把 Jev 与 GPT-5.6 Luna 对比，任务是按主题、情感、星级、是否需要回复和产品缺陷给评论分类，并比较准确率、延迟和成本。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://towardsdatascience.com/a-new-kind-of-model-for-ai-decision-making/"><img src="https://assets.insightmediagroup.io/media/1789719149842_24br2e.webp" alt="Jev 对比 OpenAI 做意图分类" width="240"></a></td>
<td valign="top"><b><a href="https://towardsdatascience.com/a-new-kind-of-model-for-ai-decision-making/">Jev 对比 OpenAI 做意图分类</a></b><br><sub>Mariya Mansurova (Towards Data Science) · 文章 · 2026-09-21</sub><br>在 77 类的 Banking77 意图数据集上比较 Jev 与两个 OpenAI 模型：准确率 79.0% 对 83.9% 和 86.2%，速度快近 2 倍，置信度校准良好；把标签减到 7 个后差距消失。<br><sub>相关: <a href="https://github.com/miptgirl/miptgirl_medium/tree/main/jev">code</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"></td>
<td valign="top"><b><a href="https://www.reddit.com/r/ClaudeAI/comments/1wj3lsw/i_thought_id_found_a_model_5000x_cheaper_than/">Jev 网页表单填写基准</a></b><br><sub>imaxalpha · Reddit · 2026-09-17</sub><br>用一个 harness 在三个真实网页表单上测试 Jev，从 13 步的保险向导到 Lever 职位申请；每个表单花费 $0.001-$0.006，13 步中完成了 0 步，11 个字段中完成了 7 个。<br><sub><b>Jev 用法:</b> 每一步做一个动作 Choice，不做规划；重跑结果说明了为什么多步表单需要规划器。</sub><br><sub>相关: <a href="https://gist.github.com/Tienduyvo/83c28649595e909d675e4fc60efe85e0">data</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/andreaserradev-gbj/jev-access-day"><img src="https://raw.githubusercontent.com/andreaserradev-gbj/jev-access-day/main/demo/assets/og-card.png" alt="jev-access-day" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/andreaserradev-gbj/jev-access-day">jev-access-day</a></b><br><sub>andreaserradev-gbj · GitHub · 2026-09-19</sub><br>学习用脚手架，带一个评测 harness，在 24 个真实运营决策上比较 Jev 与一个替身 LLM，数字可由已提交的运行文件复现，并附交互式结果页面。<br><sub>相关: <a href="https://jev-access-day.vercel.app/">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/marcosmartinez/jev-acento"><img src="https://raw.githubusercontent.com/marcosmartinez/jev-acento/main/figures/reliability_paired_es.png" alt="jev-acento" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/marcosmartinez/jev-acento">jev-acento</a></b><br><sub>marcosmartinez · GitHub · 2026-09-20</sub><br>对 Jev 西班牙语能力的预注册审计，覆盖 3,200 个成对的人工标注条目：state 用西班牙语写时，每个数据集的准确率都下降，XNLI 上最多降 6.4 个百分点，而用西班牙语写指令则毫无影响；附可重跑的 CLI。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Gaurav-Gosain/jev-alpha-bench"><img src="https://opengraph.githubassets.com/1/Gaurav-Gosain/jev-alpha-bench" alt="jev-alpha-bench" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Gaurav-Gosain/jev-alpha-bench">jev-alpha-bench</a></b><br><sub>Gaurav-Gosain · GitHub · 2026-09-16</sub><br>两项研究，检验 Jev 能否根据新闻标题或价格 K 线预测股票收益：当日 rank IC 为 +0.24，到下一个收盘就降到 -0.008，多空组合扣除成本后每笔交易亏 18 bps。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/thijmenkam/jev-benchmarks"><img src="https://opengraph.githubassets.com/1/thijmenkam/jev-benchmarks" alt="jev-benchmarks (thijmenkam)" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/thijmenkam/jev-benchmarks">jev-benchmarks (thijmenkam)</a></b><br><sub>thijmenkam · GitHub · 2026-09-17</sub><br>可复现的 harness，就同一个 state 向 Jev 和前沿 LLM 提出相同的类型化问题，并对准确率、校准、一致性、延迟、成本和 schema 合规性打分，每个模型跑 150 次调用。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/jujumilk3/jev-calibration-audit"><img src="https://opengraph.githubassets.com/1/jujumilk3/jev-calibration-audit" alt="jev-calibration-audit" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/jujumilk3/jev-calibration-audit">jev-calibration-audit</a></b><br><sub>jujumilk3 · GitHub · 2026-09-18</sub><br>仅通过 API 对 Jev 做的独立校准审计，共七个实验（约 7,000 次调用）：去掉弃权选项后，不可回答条目上的准确率从 0.950 跌到 0.000，而使用韩语对校准没有影响。<br><sub><b>Jev 用法:</b> 还发现不存在选项顺序偏差，把 16 个问题打包在一起也不会互相干扰。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/nikkoxgonzales/jev-certify"><img src="https://raw.githubusercontent.com/nikkoxgonzales/jev-certify/main/docs/risk-coverage.svg" alt="jev-certify" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/nikkoxgonzales/jev-certify">jev-certify</a></b><br><sub>nikkoxgonzales · GitHub · 2026-09-21</sub><br>工具包加一项 CLINC150 研究：通过保形风险控制（conformal risk control）把 Jev 的概率转成路由阈值，并用预测驱动推断（prediction-powered inference）审计这些阈值：2,412 次决策花费 $0.23，也展示了界限在哪里失效。</td>
</tr>
</table>

<details><summary>还有 23 条</summary>

- **[jev-demos](https://github.com/Bud-ro/jev-demos)** · <sub>Bud-ro · GitHub · 2026-09-17</sub><br>用 Dart 写的迷宫实验，测试 Jev 的空间前瞻能力：每次请求让它给出多达 100 步后续走法时，它一个迷宫也没解出来；但给出相邻格子的提示、只问下一步时，它解出了 6/10 个 5x5 迷宫。
- **[jev-eval](https://github.com/Shogo-nfrealmusic/jev-eval)** · <sub>Shogo-nfrealmusic · GitHub · 2026-09-18</sub><br>第三方在相同条件下比较 Jev 与 gpt-4o-mini、Claude Sonnet 4.5，任务是为日本一家摄影服务路由 60 条 4 种语言的合成预约咨询。
- **[jev-headline-bench](https://github.com/Gaurav-Gosain/jev-headline-bench)** · <sub>Gaurav-Gosain · GitHub · 2026-09-16</sub><br>测试 jev-1.13.0 仅凭两个标题能否挑出真实 Upworthy A/B 测试的胜者：在 10,984 个随机实验上正确率 64.5%，在差距明显的实验上升到 74.7%。
- **[jev-measured](https://github.com/WallerChen/jev-measured)** · <sub>WallerChen · GitHub · 2026-09-19</sub><br>通过 OpenRouter 在八个用例上对真实 Jev API 的成本、延迟和原始输出做的可复现测量，外加 27 张客服工单上的小规模正面对比；整轮运行花费不到一美分。
- **[jev-orderby-bench](https://github.com/yodablocks/jev-orderby-bench)** · <sub>yodablocks · GitHub · 2026-09-19</sub><br>独立测量对 Jev 概率做 SQL ORDER BY 能否得到站得住的排序：jev-1.13.0 在 360 行带标注数据上通过了六道预注册关卡，但在分级的商品相关性上六道没过四道。
- **[jev-packs](https://github.com/dtduc-git/jev-packs)** · <sub>dtduc-git · GitHub · 2026-09-19</sub><br>Jev 问题包（问题、标准用例、固定版本的模型、实测证据）的注册表，另附 Jev Bench，在相同标签上给 jev-1.13.0、claude-sonnet-5 和一个本地 Qwen 打分，指标包括准确率、ECE、成本和延迟。
- **[jev-report](https://github.com/HackSing/jev-report)** · <sub>HackSing · GitHub · 2026-09-17</sub><br>关于 Jev 的独立中文研究报告：一份 52 页的 PDF，把厂商数字追溯到出处，另有 50 个中文测试用例，90 个判断中 86 个正确（95.6%），ECE 为 0.070。
- **[jev-shadcn-lint-eval](https://github.com/blas0/jev-shadcn-lint-eval)** · <sub>blas0 · GitHub · 2026-09-17</sub><br>为 shadcn-ui/lint 做的第二轮评测，针对 131 个规则测试用例，逐个问 Jev 该用例是否正确、提示信息是否说明了要改什么；Jev 抓住了 91% 的真实违规，但在干净代码上表现较弱。
- **[jev-spam-eval](https://github.com/bitnovus/jev-spam-eval)** · <sub>bitnovus · GitHub · 2026-09-17</sub><br>用 Jev 做零样本的正常/垃圾/钓鱼邮件分类：仅凭书面类别定义，在 5,733 封邮件上达到 98.64%，而每折用约 4,600 个标签训练的 TF-IDF 模型为 98.87%。
- **[jev-trace-classifier](https://github.com/sypherin/jev-trace-classifier)** · <sub>sypherin · GitHub · 2026-09-17</sub><br>测试一个 Jev Noul 能否在全部 4,579 个 collusion.wiki 页面上分辨 agent 写的和人写的页面，并与一个本地 Qwen 模型正面对比；Jev 准确率 0.741，而多数类基线为 77.6%。
- **[Jev：只问一次 62.6%，拆成五问 95%](https://www.beri.net/article/typesafe-jev-typed-decision-model-calibration-decomposition-shadow-eval)** · <sub>Rajesh Beri · 文章 · 2026-09-21</sub><br>独立测试汇总：在 2,000 封邮件的钓鱼测试中，Jev 比 Claude Haiku 4.5 便宜 12-27 倍，只问一个问题得分 62.6%，拆成五个问题后得分 95.0%，且概率存在校准偏差。
- **[Mini-Vibe Check](https://every.to/also-true-for-humans/mini-vibe-check-typesafe-s-jev-judged-everything-i-ve-written-in-0-7-seconds)** · <sub>Mike Taylor (Every) · 文章 · 2026-09-15</sub><br>动手评测：Jev 在 0.7 秒内、花四分之一美分，对作者的 37 篇文章做了 777 个判断，植入的七处缺陷抓出了六处，Fable 则抓出了全部七处。
- **[一次评判调用，还是十二个维度分数？](https://agentjournal.dev/blog/llm-judge-vs-feature-extraction/)** · <sub>ikkun · 文章 · 2026-09-17</sub><br>在三个分类任务上比较两种做法：每行直接问 Jev 一个问题，与由 Jev 给 12-14 个维度打分再用本地拟合的权重组合，共用了 34.1M 输入 token，花费 $1.43。
- **[安全事件工作流评测](https://evals.typesafe.ai/security_incidents)** · <sub>TypeSafe AI · 文档</sub><br>官方工作流评测：判断一条安全告警应当关闭、升级还是遏制；Jev 得分 61.7%，每个案例 $0.0001、0.3 秒，而 Opus 5 为 66.2%、$0.0574、15.1 秒。
- **[SHADE-Arena 的 Jev 监控器](https://github.com/nican2018/shade-arena-jev-monitor)** · <sub>nican2018 · GitHub · 2026-09-17</sub><br>SHADE-Arena 的一个分支，评估把 Jev 用作隐蔽 agent 破坏行为的监控器，对比 Gemini 2.5 Flash 和 Pro；作为逐动作关卡，Jev 在 353 次工具调用上 AUC 达到 0.97，但在完整对话记录上只有 0.78。
- **[我用 Jev 试的六件事](https://isaacflath.com/writing/six-things-i-tried-with-jev)** · <sub>Isaac Flath · 文章 · 2026-09-16</sub><br>六个把 Gemini 换成 Jev 的实验，从脚本事实核查（24/24 正确，中位 0.41 秒）、新闻信息流排序，到 PDF 段落重排（正确段落排第一 7 次对 1 次）和 agent 失败复盘。
- **[smoking-extraction-benchmark](https://github.com/vclic/smoking-extraction-benchmark)** · <sub>vclic · GitHub · 2026-09-18</sub><br>在 1,000 份合成门诊病历上的配对基准，就十个吸烟史字段比较 Jev 1.13.0 与 OpenAI 结构化输出：完整抽取率 92.4% 对 98.7%，并比较成本和延迟。
- **[在公开和私有数据上测试 Jev](https://amankumar.ai/blogs/jev-measured)** · <sub>Aman Kumar · 文章 · 2026-09-18</sub><br>用 16,000 次调用，在四个公开数据集和几千条真实流水线决策上把 Jev 与 gpt-5.4-mini 和 gpt-5.6-luna 对比，展示它在哪里胜出、在哪里失效，以及如何设定阈值。
- **[类型化判断还是 agent 循环？](https://blog.r6i.it/typesafe-jev-vs-agentic-loop.html)** · <sub>samreghenzi · 文章 · 2026-09-21</sub><br>用带扇出的分层 Choice 对比 GPT 工具调用 agent，平均延迟从 9.62 秒降到 1.38 秒。
- **[TypeSafe Jev 下国际象棋](https://dev.to/maximsaplin/typesafe-jev-played-chess-and-landed-next-to-reasoning-models-28ga)** · <sub>Maxim Saplin · 文章 · 2026-09-17</sub><br>让 Jev 跑 LLM Chess 基准，把合法走法作为 Choice，最终排在约第 59 名，Elo 约 243，与中游的推理模型相当，每局约 $0.0015。
- **[TypeSafe Jev 对比 Claude Code：4 个模型、2 项真实任务](https://primeline.cc/blog/typesafe-jev-pre-registered-test)** · <sub>Robin (PrimeLine) · 文章 · 2026-09-18</sub><br>对 Jev、GPT-5.6、Opus 5 和 Haiku 4.5 的预注册测试，任务是两项真实的 Claude Code 工作，两项任务上的排名互相颠倒，作者解释了原因。
- **[typesafe-oracles](https://github.com/trophee-bot/typesafe-oracles)** · <sub>trophee-bot · GitHub · 2026-09-16</sub><br>类型化 oracle 的测量装置；在两个仓库上核对提交信息与 diff 是否一致的任务中，Jev 的准确率与 Haiku 4.5 持平，速度快约 4 倍，成本低约 26 倍，还提供可用的置信度信号。
- **[我们在搜索重排和分类上测试了 Jev](https://parallel.ai/blog/testing-jev)** · <sub>Vlad Shulman (Parallel) · 文章 · 2026-09-18</sub><br>一家搜索 API 公司以零样本方式在重排、主题分类和查询时效性上测试 Jev：在 NDCG@10 上它以 0.7 追平了一个定制重排器，但落后于专门的内部分类器。

</details>

还缺什么？[提交一个资源](https://github.com/Li-Evan/awesome-jev/issues/new/choose)。
