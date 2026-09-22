# 📚 学习资料: 技巧与分析

[English](https://github.com/Li-Evan/awesome-jev/blob/main/pages/learn-techniques.md) · **简体中文**

官方文档和 cookbook，以及社区里最好的教程、分析、评测和演讲。共 102 条，按社区热度排序。

[← 返回 Awesome Jev](https://github.com/Li-Evan/awesome-jev/blob/main/README.zh-CN.md#技巧与分析)

[官方文档](https://github.com/Li-Evan/awesome-jev/blob/main/zh-CN/pages/learn-official-docs.md) (15) · [官方 SDK 与工具](https://github.com/Li-Evan/awesome-jev/blob/main/zh-CN/pages/learn-official-tools.md) (3) · [官方公告](https://github.com/Li-Evan/awesome-jev/blob/main/zh-CN/pages/learn-announcements.md) (2) · [设计模式](https://github.com/Li-Evan/awesome-jev/blob/main/zh-CN/pages/learn-patterns.md) (4) · [官方 Cookbook](https://github.com/Li-Evan/awesome-jev/blob/main/zh-CN/pages/learn-cookbooks.md) (18) · [示例与 Skill](https://github.com/Li-Evan/awesome-jev/blob/main/zh-CN/pages/learn-examples.md) (74) · [教程](https://github.com/Li-Evan/awesome-jev/blob/main/zh-CN/pages/learn-guides.md) (76) · **技巧与分析** · [评测与案例](https://github.com/Li-Evan/awesome-jev/blob/main/zh-CN/pages/learn-benchmarks.md) (173) · [视频与演讲](https://github.com/Li-Evan/awesome-jev/blob/main/zh-CN/pages/learn-videos.md) (178) · [社区讨论](https://github.com/Li-Evan/awesome-jev/blob/main/zh-CN/pages/learn-discussions.md) (20)

<table>
<tr>
<td width="260" valign="top"><a href="https://x.com/CompleteSkeptic/status/2099925682726002904"><img src="https://pbs.twimg.com/amplify_video_thumb/2099925575637057536/img/l4J_ZhkaxAe8FJXv.jpg" alt="Jev 发布帖子串" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/CompleteSkeptic/status/2099925682726002904">Jev 发布帖子串</a></b><br><sub>CompleteSkeptic · Hacker News · ♥ 75k · 2026-09-15</sub><br>创始人 Diogo Almeida 的发布帖子串，介绍 Jev 和 RLCD 训练方法，宣称决策速度比前沿聊天模型快 20-200 倍、成本低 40-400 倍。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/akshay_pachaar/status/2101037514945597645"><img src="https://pbs.twimg.com/media/HShfvSbaMAAZt9E.png" alt="把 Jev 讲清楚" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/akshay_pachaar/status/2101037514945597645">把 Jev 讲清楚</a></b><br><sub>akshay_pachaar · 文章 · ♥ 5k · 2026-09-18</sub><br>一篇 X 长文，把 Jev 解释为毫秒级决策层：类型化问题如何取代“生成、解析、重试”式的 LLM 调用，以及它在应用中如何与 LLM 并列。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/0xSuman/status/2100030221189874015"><img src="https://pbs.twimg.com/media/HSTOW1GagAA0xlK.jpg?name=orig" alt="用 Jev 生成文本" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/0xSuman/status/2100030221189874015">用 Jev 生成文本</a></b><br><sub>0xSuman · X · ♥ 4.2k · 2026-09-16</sub><br>一个 hack：每个字符位置问一个 Choice 问题（带 STOP 选项），读出概率最高的字母，让 Jev 写出文本。<br><sub><b>Jev 用法:</b> 每个字符一个 Choice，选项为字母表加 STOP。</sub></td>
</tr>
<tr>
<td width="260" valign="top"></td>
<td valign="top"><b><a href="https://x.com/NathanFlurry/status/2100036101809619314">把 Jev 当作聪明的 switch 语句</a></b><br><sub>NathanFlurry · X · ♥ 7.5k · 2026-09-16</sub><br>不吹不黑的讲解，认为 Jev 就是一个非常聪明的 switch 语句：它能在预定义选项上做分类、路由、打分和核验，但写不了代码或文字。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/k_grajeda/status/2099952715430596710"><img src="https://pbs.twimg.com/media/HSSGbsVXAAEi9jw.png?name=orig" alt="LLM 与 Jev 判断提示词难度的对比" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/k_grajeda/status/2099952715430596710">LLM 与 Jev 判断提示词难度的对比</a></b><br><sub>k_grajeda · X · ♥ 5.7k · 2026-09-15</sub><br>简化的并排对比，展示 LLM 和 Jev 如何给一个提示词的难度分类：一个逐 token 生成文本，一个并行算出每个选项的概率。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/theo/status/2100762304862384257"><img src="https://pbs.twimg.com/amplify_video_thumb/2100694537672998912/img/OF8vottg6-45ZgNl.jpg" alt="对 Jev 上下文压缩的批评" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/theo/status/2100762304862384257">对 Jev 上下文压缩的批评</a></b><br><sub>theo · X · ♥ 2.6k · 2026-09-18</sub><br>批评观点：用 Jev 按工具调用逐条过滤并不是好的上下文压缩策略，因为压缩应当重建历史，而模型并不掌握之前发生过什么的上下文。<br><sub>相关: <a href="https://github.com/tamaratran/fast-jev-compaction">related</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/servasyy_ai/status/2101132667056185544"><img src="https://pbs.twimg.com/media/HSi3JD0bcAEhil0.jpg" alt="Jev 到底能做什么" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/servasyy_ai/status/2101132667056185544">Jev 到底能做什么</a></b><br><sub>servasyy_ai · 文章 · ♥ 779 · 2026-09-19</sub><br>中文的 Jev 现实检验：解释它是什么、不是什么，按用例整理真正能跑通的演示，并列出速度和准确率宣称背后的注意事项。</td>
</tr>
<tr>
<td width="260" valign="top"></td>
<td valign="top"><b><a href="https://x.com/MichaelLee04/status/2100003037150683593">把 Jev 当作决策原语</a></b><br><sub>MichaelLee04 · X · ♥ 3.1k · 2026-09-15</sub><br>约 5,000 次请求（花费约 $2）在分类、路由和意图识别上的笔记：p50 约 150 毫秒、p95 约 350 毫秒，足以支撑每轮都做检查；而且 Jev 更适合把查询拆成相互独立的问题来问。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/akshay_pachaar/status/2101309986156712025"><img src="https://pbs.twimg.com/amplify_video_thumb/2101309969044054016/img/33Ud7QFDU8aMgYlW.jpg" alt="把 LLM 与 Jev 的区别讲清楚" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/akshay_pachaar/status/2101309986156712025">把 LLM 与 Jev 的区别讲清楚</a></b><br><sub>akshay_pachaar · X · ♥ 2.9k · 2026-09-19</sub><br>解释 Jev 并不是生成得更快，而是根本不生成：相互独立的 Choice、Score 和 Noul 问题（比如一次失败部署的紧急程度、负责团队和命令风险）会被并行评估。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/NielsRogge/status/2100239244501430438"><img src="https://pbs.twimg.com/media/HSWLYi3WcAAOPBs.jpg?name=orig" alt="Jev 式解码的工作原理" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/NielsRogge/status/2100239244501430438">Jev 式解码的工作原理</a></b><br><sub>NielsRogge · X · ♥ 3.8k · 2026-09-16</sub><br>基于开源 Qwen2.5-RLCD 模型的图解：从一次带缓存的解码器前向传播中读出各字段的概率，而不是逐 token 生成 JSON。</td>
</tr>
<tr>
<td width="260" valign="top"></td>
<td valign="top"><b><a href="https://x.com/paarangatrai/status/2100113737097367896">LLM 负责生成，Jev 负责决策</a></b><br><sub>paarangatrai · X · ♥ 2.3k · 2026-09-16</sub><br>用一个高风险账户的例子讲解：不再提示 LLM 给出结论，而是预先声明风险等级和人工复核标记，拿回的是 risk = high（96%）这样的概率。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://tech.layerx.co.jp/entry/2026/09/18/185816"><img src="https://cdn.image.st-hatena.com/image/scale/5ed4f6e73205d082af7a8a0518536c4ad98d0eb3/backend=imagemagick;version=1;width=1300/https%3A%2F%2Fcdn-ak.f.st-hatena.com%2Fimages%2Ffotolife%2Fy%2Fyuu2634%2F20260918%2F20260918191032.png" alt="LayerX 内部 Jev 学习会" width="240"></a></td>
<td valign="top"><b><a href="https://tech.layerx.co.jp/entry/2026/09/18/185816">LayerX 内部 Jev 学习会</a></b><br><sub>LayerX (pon) · 文章 · ♥ 959 · 2026-09-18</sub><br>日文记录：LayerX 内部一场 30 分钟的 Jev 学习会，吸引了 50 多名工程师参加，产出了 50 多个把它融入自家产品的点子。<br><sub>相关: <a href="https://x.com/hatebu100/status/2101094920778129466">x</a> · <a href="https://x.com/LayerX_tech/status/2100887864594895154">demo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"></td>
<td valign="top"><b><a href="https://x.com/swill1ams/status/2100421326389354624">为现有工作流定制 Jev 式模型</a></b><br><sub>swill1ams · X · ♥ 1.4k · 2026-09-17</sub><br>帖子串，认为企业可以用过往决策训练一个廉价的并行约束解码分类器，放在已有的 LLM 审核步骤之前，让高置信度的条目直接通过，其余的继续往后送。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/0xMovez/status/2102049863449858053"><img src="https://pbs.twimg.com/media/HSv6c7rXwAAOMVI.jpg?name=orig" alt="Jev Harness 蓝图摘要" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/0xMovez/status/2102049863449858053">Jev Harness 蓝图摘要</a></b><br><sub>0xMovez · X · ♥ 1.3k · 2026-09-21</sub><br>帖子串，总结 TypeSafe 一份 12 页的 PDF，内容是面向编程 agent 的 Jev harness，例如 Opus→Sonnet→Opus 交接的成本为 6.19，纯 Opus 为 4.15，读取和搜索占了 56.2% 的工具轮次。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/ryanvogel/status/2100218045549412499"><img src="https://pbs.twimg.com/amplify_video_thumb/2100217973000617984/img/AFareJummI08B_QB.jpg" alt="用分类器造一个 LLM" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/ryanvogel/status/2100218045549412499">用分类器造一个 LLM</a></b><br><sub>ryanvogel · X · ♥ 889 · 2026-09-16</sub><br>用 Jev 搭出一个自回归文本生成器：每个字符问 29 个是非题来选出下一个键（a-z、空格、逗号、句号），再把文本回灌进去循环往复。<br><sub><b>Jev 用法:</b> 每个字符问 29 个 Noul 问题，追加概率最高的那个键。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/gregisenberg/status/2101018750916948237"><img src="https://pbs.twimg.com/amplify_video_thumb/2101018301409202176/img/HP2Ycx2G3KjqvxJw.jpg" alt="Jev 能催生的生意" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/gregisenberg/status/2101018750916948237">Jev 能催生的生意</a></b><br><sub>gregisenberg · X · ♥ 1.5k · 2026-09-18</sub><br>用大白话把 Jev 解释为分拣器（18 美分处理 1,700 封邮件），并给出一些创业点子：把它放在昂贵队列的最前端，比如即时报价和线索打分。<br><sub>相关: <a href="https://www.youtube.com/watch?v=4mTLpuQpB80">video</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/mvanhorn/status/2100788572316139655"><img src="https://pbs.twimg.com/media/HSdxN5LbUAAMq_w.png" alt="Jev 究竟是什么鬼" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/mvanhorn/status/2100788572316139655">Jev 究竟是什么鬼</a></b><br><sub>mvanhorn · X · ♥ 418 · 2026-09-18</sub><br>讲解文章，把 Jev 定位为做选择题而不是写作文的 AI，并整理了开发者在头 72 小时里用它搭出的九种模式。<br><sub>相关: <a href="https://x.com/i/article/2100772231462961152">article</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"></td>
<td valign="top"><b><a href="https://x.com/da_fant/status/2100659471257366766">Jev 如何让 agent 更便宜</a></b><br><sub>da_fant · X · ♥ 634 · 2026-09-17</sub><br>帖子串，列出 Jev 能给 agent 提速的地方：从模型路由、电脑操控（computer use）和动作安全审查，到判断每个事件应当唤醒昂贵的编排器、交给子 agent 还是排进队列。</td>
</tr>
<tr>
<td width="260" valign="top"></td>
<td valign="top"><b><a href="https://x.com/jiayuan_jy/status/2100876273061102006">用了一天 Jev 后的质疑笔记</a></b><br><sub>jiayuan_jy · X · ♥ 339 · 2026-09-18</sub><br>一天测试后的中文笔记：Jev 更像一个更快的通用分类器，适合 DOM 操作或上下文压缩这类有边界、低延迟的选择，但替代不了带参数的 agent 工具调用。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/anderslie/status/2100388704644919662"><img src="https://pbs.twimg.com/amplify_video_thumb/2100384704868601856/img/TSBG-jeFfuLlRSOS.jpg" alt="在开源权重模型上实现类 Jev API" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/anderslie/status/2100388704644919662">在开源权重模型上实现类 Jev API</a></b><br><sub>anderslie · X · ♥ 567 · 2026-09-17</sub><br>解释 Jev 式的速度可以来自推理层面：共享 state 只预填充一次，按问题分叉上下文，再在任意开源权重 LLM 上读取限定在选项标签上的 logits。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/trycua/status/2101437979180904640"><img src="https://pbs.twimg.com/media/HSnHzhdWoAEwmrh.jpg" alt="Jev 与电脑操控的未来" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/trycua/status/2101437979180904640">Jev 与电脑操控的未来</a></b><br><sub>trycua · 文章 · ♥ 559 · 2026-09-19</sub><br>Cua 的深度文章，分析电脑操控（computer use）agent 内部哪些决策真正需要通用 LLM，并把屏幕转成打好分的候选动作，交给 Jev 以及他们自己的 CUA-S1-FORMS 这类纯文本决策模型。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/Bewinxed/status/2100519569307640097"><img src="https://pbs.twimg.com/amplify_video_thumb/2100519508943228928/img/Vl5XWMF9MjLBasxD.jpg" alt="让 Jev 生成文本" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/Bewinxed/status/2100519569307640097">让 Jev 生成文本</a></b><br><sub>Bewinxed · X · ♥ 320 · 2026-09-17</sub><br>一个 hack：让本不具备生成能力的 Jev 产出文本，花 $0.5 最多能写出 20 个词。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/JoshARosen/status/2101645894818857272"><img src="https://pbs.twimg.com/media/HSqLJdJWoAA4aNR.jpg" alt="Jev 项目实地观察" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/JoshARosen/status/2101645894818857272">Jev 项目实地观察</a></b><br><sub>JoshARosen · 文章 · ♥ 182 · 2026-09-20</sub><br>梳理 Jev 项目中早期出现的架构模式，比如模型、skill 和工具路由、监督者和安全层，它们都是在其余部分相当常规的软件里，于某一个决策点插入 Jev。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/annabellschfr/status/2100962787094597807"><img src="https://pbs.twimg.com/media/HSgRvklXgAA33Rx.jpg" alt="偏科天才 Jev" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/annabellschfr/status/2100962787094597807">偏科天才 Jev</a></b><br><sub>annabellschfr · 文章 · ♥ 64 · 2026-09-18</sub><br>讲解 Jev 在流水线和评测 harness 中的位置，逐一介绍 Choice、Score 和 Noul，并给出一个完整示例：在一次请求里对一次已完成的 agent 运行提出三个判断。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/omarsar0/status/2100693601021997193"><img src="https://pbs.twimg.com/media/HScpisJbEAAMxZb.jpg?name=orig" alt="值得用 Jev 试试的事" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/omarsar0/status/2100693601021997193">值得用 Jev 试试的事</a></b><br><sub>omarsar0 · X · ♥ 679 · 2026-09-17</sub><br>实践者列出的 Jev 潜力用法：LLM 评判式评测、agent harness 中的路由、创建子 agent 和动态生成 harness，作者自己把它用作一个元 harness 的路由器。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://archerhume.com/posts/jevs-architecture-unmasked/"><img src="https://archerhume.com/og-image/jevs-architecture-unmasked.png" alt="揭开 Jev 的架构" width="240"></a></td>
<td valign="top"><b><a href="https://archerhume.com/posts/jevs-architecture-unmasked/">揭开 Jev 的架构</a></b><br><sub>Archer Hume · 文章 · ♥ 437 · 2026-09-17</sub><br>架构拆解：用 10,000 次 API 调用探测 Jev，推断它的构造，从共享 state 加相互隔离的问题分支，到选项之间的相互作用和置信度读出。<br><sub>相关: <a href="https://news.ycombinator.com/item?id=49766351">discussion</a> · <a href="https://x.com/iwashi86/status/2100713337436930288">demo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/Sumanth_077/status/2101639788961112279"><img src="https://pbs.twimg.com/media/HSqGNyCacAAhUYd.jpg" alt="把 Jev 讲清楚" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/Sumanth_077/status/2101639788961112279">把 Jev 讲清楚</a></b><br><sub>Sumanth_077 · 文章 · ♥ 324 · 2026-09-20</sub><br>讲解 agent 一次运行中的许多小决策（模型选择、高风险工具调用、循环、是否完成），以及 Jev 如何用类型化概率而非生成文本来回答它们。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/aparnadhinak/status/2100979688072224957"><img src="https://pbs.twimg.com/media/HSgtobXaEAAaDhD.jpg" alt="TypeSafe 的 Jev 会改变我们构建 AI 应用的方式吗？" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/aparnadhinak/status/2100979688072224957">TypeSafe 的 Jev 会改变我们构建 AI 应用的方式吗？</a></b><br><sub>aparnadhinak · 文章 · ♥ 197 · 2026-09-18</sub><br>Arize AI 的分析，讲一个只做决策的模型能带来什么、要付出什么代价，重点关注 LLM 评判式评测以及它所隐含的架构选择。</td>
</tr>
<tr>
<td width="260" valign="top"></td>
<td valign="top"><b><a href="https://x.com/DalinHuang/status/2101839381589884965">Jev 在生产中哪里划算</a></b><br><sub>DalinHuang · X · ♥ 27 · 2026-09-21</sub><br>中文一线笔记：把 Gemini Flash 或 GPT Luna 做的判断换成 Jev 后，成本降了 20 到 60 倍，延迟降了一个数量级，做法是把置信度低于 80% 的答案升级给小型生成模型。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/Kedr_bit/status/2102132700119191832"><img src="https://pbs.twimg.com/media/HSxGi5rWgAAbZhF.jpg?name=orig" alt="让 Jev 开口说话" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/Kedr_bit/status/2102132700119191832">让 Jev 开口说话</a></b><br><sub>Kedr_bit · X · ♥ 151 · 2026-09-21</sub><br>聊天实验，诱导 Jev 用文字回复，产出简短、混乱但挺好玩的对话。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://www.reddit.com/r/LocalLLaMA/comments/1wkd1dz/digitlogitsbased_classifier_with_llamacpp/"><img src="https://external-preview.redd.it/WB3qVqzuW2bIGtkMVrOZ0TihcSnHaV-pareGCkJDiXs.png?auto=webp&amp;s=19b1cd738d385b0222b357df4dc720a2fdb24a88" alt="用 llama.cpp 做数字 logits 分类器" width="240"></a></td>
<td valign="top"><b><a href="https://www.reddit.com/r/LocalLLaMA/comments/1wkd1dz/digitlogitsbased_classifier_with_llamacpp/">用 llama.cpp 做数字 logits 分类器</a></b><br><sub>rhinodevil · Reddit · ▲ 10 · 2026-09-19</sub><br>来自 mt_llm 库的技巧：读取数字 token 的 logits，把小型本地 LLM 当分类器用，而不依赖 llama.cpp 的语法约束（grammars）。<br><sub>相关: <a href="https://github.com/RhinoDevel/mt_llm">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"></td>
<td valign="top"><b><a href="https://news.ycombinator.com/item?id=49791782">像用 Jev 一样用任何 LLM</a></b><br><sub>theanonymousone · Hacker News · ▲ 10 · 2026-09-21</sub><br>做法：在 llama.cpp 中运行任意 GGUF 模型，只预测一个 token 并取 top logprobs，得到 Jev 式的类别概率，并说明在校准概率上仍有哪些差别。<br><sub>相关: <a href="https://www.reddit.com/r/LocalLLaMA/comments/1wlxpaw/you_can_use_any_llm_just_like_jev/">reddit</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://sereja.tech/blog/typesafe-system-one-jev/"><img src="https://sereja.tech/images/blog/typesafe-system-one-jev-general-reader.png" alt="Jev 讲解（俄语）" width="240"></a></td>
<td valign="top"><b><a href="https://sereja.tech/blog/typesafe-system-one-jev/">Jev 讲解（俄语）</a></b><br><sub>serejaris · 文章 · ⭐ 25 · 2026-09-17</sub><br>俄语博客讲解 TypeSafe 的 Jev：一个从给定选项中做选择的模型如何帮助路由请求、引导助手的动作并检查结果，引用了发布文章、文档、工作流评测和早期第三方测试。<br><sub>相关: <a href="https://github.com/serejaris/sereja.tech/blob/main/content/blog/typesafe-system-one-jev.md">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://anthonymaio.substack.com/p/jev-the-language-model-that-wont"><img src="https://substackcdn.com/image/fetch/$s_!mqdS!,w_1200,h_675,c_fill,f_jpg,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F85790540-64fc-479b-92ea-a0b2baecc21f_1672x941.png" alt="Jev：不说话的语言模型" width="240"></a></td>
<td valign="top"><b><a href="https://anthonymaio.substack.com/p/jev-the-language-model-that-wont">Jev：不说话的语言模型</a></b><br><sub>Anthony Maio · 文章 · ♥ 22 · 2026-09-16</sub><br>随笔，认为 Jev 真正的主张不在价格，而在于：生成的语言也许是模型与那些必须根据其输出采取行动的软件之间一个错误的接口。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://medium.com/@gemanor/most-people-on-the-internet-miss-what-jev-is-about-ad0a983537d5"><img src="https://miro.medium.com/v2/resize:fit:700/0*m5fn7rELknSeGCVp.png" alt="大多数人没看懂 Jev 的重点" width="240"></a></td>
<td valign="top"><b><a href="https://medium.com/@gemanor/most-people-on-the-internet-miss-what-jev-is-about-ad0a983537d5">大多数人没看懂 Jev 的重点</a></b><br><sub>Gabriel L. Manor · 文章 · ▲ 6 · 2026-09-18</sub><br>随笔，认为廉价分类只是 Jev 最无聊的部分，并走查三种 harness 设计，其中类型化、带置信度分数的 System One 模型与 LLM 并列工作。<br><sub>相关: <a href="https://news.ycombinator.com/item?id=49754461">discussion</a> · <a href="https://github.com/gemanor/jev-code-review-benchmark">benchmark</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://sgnt.ai/p/jev/"><img src="https://sgnt.ai/jev-at-home.png" alt="你也能造出 Jev" width="240"></a></td>
<td valign="top"><b><a href="https://sgnt.ai/p/jev/">你也能造出 Jev</a></b><br><sub>sgnt.ai · 文章 · ▲ 6 · 2026-09-18</sub><br>简短的图解文章，认为 Jev 很可能就是一个只返回单个 token 的 LLM，附伪代码并与做同样事情的其他项目对比，让你能从第一性原理去理解它。<br><sub>相关: <a href="https://news.ycombinator.com/item?id=49755430">discussion</a> · <a href="https://x.com/ekzhang1/status/2101117003415105696">x</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://sebastianraschka.com/blog/2026/jev-classification-generalization.html"><img src="https://sebastianraschka.com/images/blog/2026/jev-classification-generalization/jev.png" alt="很容易把 Jev 当成只是个分类器" width="240"></a></td>
<td valign="top"><b><a href="https://sebastianraschka.com/blog/2026/jev-classification-generalization.html">很容易把 Jev 当成只是个分类器</a></b><br><sub>Sebastian Raschka · 文章 · ▲ 4 · 2026-09-20</sub><br>短文，说明 Jev 的泛化能力为何重要，推测其可能采用的类编码器架构和训练方式，并附 Choice 和 Noul 的 API 示例。<br><sub>相关: <a href="https://news.ycombinator.com/item?id=49787418">discussion</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://thefinancialengineer.substack.com/p/typesafes-jev-is-about-to-change"><img src="https://substackcdn.com/image/fetch/$s_!gJGj!,w_1200,h_675,c_fill,f_jpg,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2da657fe-df1c-4bb2-b059-f373a69dec96_1376x768.jpeg" alt="Jev 将要改变 AI 经济" width="240"></a></td>
<td valign="top"><b><a href="https://thefinancialengineer.substack.com/p/typesafes-jev-is-about-to-change">Jev 将要改变 AI 经济</a></b><br><sub>Anton Zagrebelny · 文章 · ▲ 4 · 2026-09-17</sub><br>随笔，讨论免费的输出 token 和一次调用问多个问题如何打破按 token 计的额度计费，以及当 Jev 与 LLM 并列时，计量和权益管控应该放在哪一层。<br><sub>相关: <a href="https://news.ycombinator.com/item?id=49747584">discussion</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"></td>
<td valign="top"><b><a href="https://rajveerbachkaniwala.com/blog/2026/09/19/jev-is-to-tool-use-what-rag-is-to-context/">Jev 之于工具使用，正如 RAG 之于上下文</a></b><br><sub>Rajveer Bachkaniwala · 文章 · ▲ 4 · 2026-09-19</sub><br>短文，把 Jev 看作 RAG 的镜像：开发者预先固定的是模型可以选哪些选项（包括工具），而不是模型读取哪些上下文。<br><sub>相关: <a href="https://news.ycombinator.com/item?id=49770295">discussion</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Siddhant-K-code/distill/tree/main/research/context-is-a-build-artifact"><img src="https://opengraph.githubassets.com/1/Siddhant-K-code/distill" alt="上下文是一种构建产物" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Siddhant-K-code/distill/tree/main/research/context-is-a-build-artifact">上下文是一种构建产物</a></b><br><sub>Siddhant-K-code · GitHub · ⭐ 180 仓库 · 2025-12-31</sub><br>一份预注册的研究设计，附离线试点 harness 和 TypeSafe 适配器，检验字节级稳定的上下文编译能否提升 Jev 决策的一致性、校准和成本表现。<br><sub>相关: <a href="https://github.com/Siddhant-K-code/distill">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://inlevel9.com/en/issues/jev-judgment-not-writing"><img src="https://inlevel9.com/api/og/en/jev-judgment-not-writing?v=6-inlevel9-5" alt="Jev 一行字都写不了，但 13% 的付费团队在用它" width="240"></a></td>
<td valign="top"><b><a href="https://inlevel9.com/en/issues/jev-judgment-not-writing">Jev 一行字都写不了，但 13% 的付费团队在用它</a></b><br><sub>Oswarld (Kwangseob Ahn) · 文章 · ▲ 3 · 2026-09-21</sub><br>一期 newsletter 随笔，谈为“判断”而非文本定价揭示了 Jev 的什么，以及作者为什么要做一个只干五件事的模型。<br><sub>相关: <a href="https://news.ycombinator.com/item?id=49784782">discussion</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"></td>
<td valign="top"><b><a href="https://typesafe.ai/blog/bitterest-lesson">最苦涩的教训</a></b><br><sub>TypeSafe AI · 文章 · ▲ 3 · 2026-09-10</sub><br>官方随笔，延伸 Sutton 的“苦涩的教训”：选对要优化的任务比数据更重要，而数据又比算力和算法更重要。<br><sub>相关: <a href="https://news.ycombinator.com/item?id=49749834">discussion</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://www.seangoedecke.com/two-techniques-for-working-with-system-one-models/"><img src="https://www.seangoedecke.com/static/70f6abb1474ff212395a43c8a17194f8/fcda8/turns.png" alt="使用 System One 模型的两种技巧" width="240"></a></td>
<td valign="top"><b><a href="https://www.seangoedecke.com/two-techniques-for-working-with-system-one-models/">使用 System One 模型的两种技巧</a></b><br><sub>Sean Goedecke · 文章 · ▲ 3 · 2026-09-18</sub><br>一是分层目标：慢循环选目标，快循环选动作；二是对成批选项做锦标赛式采样；两者都在一个用开源模型仿制版搭建的 Doom agent 上演示。<br><sub>相关: <a href="https://news.ycombinator.com/item?id=49755005">discussion</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://stackness.dev/blog/what-is-a-system-one-model-and-where-does-it-go-in-your-stack"><img src="https://cdn.stackness.dev/images/1/1765c1b4-9761-43cb-8c5a-ea646ad17ad2.png" alt="System One 模型在技术栈中的位置" width="240"></a></td>
<td valign="top"><b><a href="https://stackness.dev/blog/what-is-a-system-one-model-and-where-does-it-go-in-your-stack">System One 模型在技术栈中的位置</a></b><br><sub>Sergei Gordeichuk · 文章 · ▲ 3 · 2026-09-18</sub><br>认为 System One 模型是 LLM 旁边新增的一个槽位而不是替代品，区分 TypeSafe 已经证明的和仅仅宣称的内容，并列出引入之前必须满足的前提。<br><sub>相关: <a href="https://news.ycombinator.com/item?id=49760138">discussion</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/erik-dunteman/ChatJev"><img src="https://opengraph.githubassets.com/1/erik-dunteman/ChatJev" alt="ChatJev" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/erik-dunteman/ChatJev">ChatJev</a></b><br><sub>erik-dunteman · GitHub · ⭐ 7 · 2026-09-20</sub><br>一个小实验：把 Jev 放进自回归循环，把候选的下一个 token 作为 Choice 选项，让这个非生成式模型一次一个 token 地产出文本。</td>
</tr>
<tr>
<td width="260" valign="top"></td>
<td valign="top"><b><a href="https://navinpai.github.io/decoding-jev/">解码 Jev</a></b><br><sub>Navin Pai · 文章 · ▲ 2</sub><br>图文并茂的技术深挖，推测 Jev 与 LLM 可能有哪些不同：直接读取类型化概率的 transformer 推理、严格评分规则（proper scoring rules）、策略梯度，以及 RLCD 带来的改变。<br><sub>相关: <a href="https://news.ycombinator.com/item?id=49776494">discussion</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://bernoulli.app/articles/is-jev-confident"><img src="https://bernoulli.app/og-confidence.png" alt="Jev 有把握吗？" width="240"></a></td>
<td valign="top"><b><a href="https://bernoulli.app/articles/is-jev-confident">Jev 有把握吗？</a></b><br><sub>Stanislav Yurin · 文章 · ▲ 2 · 2026-09-18</sub><br>基于数十万条线上答案，逆向推出 Choice 置信度的计算方式，并展示往选项列表里塞填充项会如何抬高置信度。<br><sub>相关: <a href="https://news.ycombinator.com/item?id=49765813">discussion</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"></td>
<td valign="top"><b><a href="https://blog.nimendra.xyz/blog/jev-decision-layer-for-production-ai/">Jev 是生产级 AI 系统缺的那块拼图</a></b><br><sub>Nimendra · 文章 · ▲ 2 · 2026-09-17</sub><br>借一次凌晨 2 点的生产事故，展示 Jev 作为有边界的决策层，在事故 agent 或 LLM 开始推理之前，先选出负责的团队、判断紧急程度以及是否自动处理。<br><sub>相关: <a href="https://news.ycombinator.com/item?id=49737892">discussion</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://patmcguinness.substack.com/p/jev-makes-fast-and-cheap-decisions"><img src="https://substackcdn.com/image/fetch/$s_!3sHt!,w_1200,h_675,c_fill,f_jpg,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb92400f8-6f41-44c7-9233-a2449f4c413e_936x537.png" alt="Jev 做出又快又便宜的决策" width="240"></a></td>
<td valign="top"><b><a href="https://patmcguinness.substack.com/p/jev-makes-fast-and-cheap-decisions">Jev 做出又快又便宜的决策</a></b><br><sub>Patrick McGuinness · 文章 · ♥ 6 · 2026-09-18</sub><br>newsletter 分析，把 Jev 定位为分类器式的生产模型而非通用模型，介绍其设计以及早期社区作品，比如自动驾驶模拟器和开源复刻。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/cookiespiggy/agentic-rl/blob/main/25-%E5%88%A4%E5%88%AB%E8%83%BD%E5%8A%9B%E5%A4%96%E7%BD%AE-%E4%BB%80%E4%B9%88%E6%97%B6%E5%80%99%E4%B8%8D%E8%AF%A5%E7%94%A8RL.md"><img src="https://raw.githubusercontent.com/cookiespiggy/agentic-rl/main/assets/25-01-playground-overview.png" alt="有了 Jev 之后何时不该用 RL" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/cookiespiggy/agentic-rl/blob/main/25-%E5%88%A4%E5%88%AB%E8%83%BD%E5%8A%9B%E5%A4%96%E7%BD%AE-%E4%BB%80%E4%B9%88%E6%97%B6%E5%80%99%E4%B8%8D%E8%AF%A5%E7%94%A8RL.md">有了 Jev 之后何时不该用 RL</a></b><br><sub>cookiespiggy · GitHub · ⭐ 107 仓库 · 2026-06-03</sub><br>一份中文 agentic RL 教程中的一章，认为判别类任务可以外包给 Jev，而策略类任务仍然需要 RL，并用梯度扫描测量它的分辨率。<br><sub>相关: <a href="https://github.com/cookiespiggy/agentic-rl">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"></td>
<td valign="top"><b><a href="https://x.com/sermakarevich/status/2101374291640213785">state 语气敏感性测试</a></b><br><sub>sermakarevich · X · ♥ 4 · 2026-09-19</sub><br>展示 Jev 的答案严重依赖 state 的语气：同一个关于 Python 类型注解的问题，在 state 写明团队不喜欢类型注解后，置信度从 0.97 降到了 0.07。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/y0usaf/jev-lm"><img src="https://opengraph.githubassets.com/1/y0usaf/jev-lm" alt="jev-lm" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/y0usaf/jev-lm">jev-lm</a></b><br><sub>y0usaf · GitHub · ⭐ 5 · 2026-09-16</sub><br>以 Jev 作为输出层的词级语言模型，配有 n-gram 起草器和 Noul 分块校验；在留出文本上，Jev 的得分为 6.92 bits/token，unigram 表为 6.18。<br><sub><b>Jev 用法:</b> 每次往返问一个 229 个选项的下一个词 Choice，外加一个判断是否结束的 Noul，中位耗时约 0.25 秒。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://stacktoheap.com/blog/2026/09/21/the-state-machine-is-the-agent/"><img src="https://stacktoheap.com/images/jev-state-machine-hero.png" alt="让 Jev 只管岔路口" width="240"></a></td>
<td valign="top"><b><a href="https://stacktoheap.com/blog/2026/09/21/the-state-machine-is-the-agent/">让 Jev 只管岔路口</a></b><br><sub>StackToHeap · 文章 · ▲ 1 · 2026-09-21</sub><br>由状态机掌握计划和合法的状态转移，Jev 只在开放的分支之间做选择，高风险的操作要求更严格的置信度余量。<br><sub>相关: <a href="https://news.ycombinator.com/item?id=49784636">discussion</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/adhyaay-karnwal/jev-chat"><img src="https://opengraph.githubassets.com/1/adhyaay-karnwal/jev-chat" alt="jev-chat" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/adhyaay-karnwal/jev-chat">jev-chat</a></b><br><sub>adhyaay-karnwal · GitHub · ⭐ 3 · 2026-09-17</sub><br>一个研究性解码器，在由短语和词构成的分层码本上用 Jev 的 Choice 搭出聊天机器人，并附一篇论文比较逐步解码与直接选择完整回复。<br><sub><b>Jev 用法:</b> 推测式扇出在同一个 state 里同时询问下一个单元和假设的后续单元；朴素的自回归会陷入循环，而整句选择能保持语法通顺。</sub></td>
</tr>
<tr>
<td width="260" valign="top"></td>
<td valign="top"><b><a href="https://x.com/hhkkmon/status/2100443314957038010">System 1 与 System 2 agent 帖子串</a></b><br><sub>hhkkmon · X · ♥ 2 · 2026-09-17</sub><br>讲解帖子串，认为很多 agent 里的 LLM 调用都是“昂贵的 if 语句”，提出用 System 1 层负责路由、评判和护栏，并列出开源的类 Jev 复刻项目。</td>
</tr>
<tr>
<td width="260" valign="top"></td>
<td valign="top"><b><a href="https://jev.kuhung.me">理解 Jev</a></b><br><sub>kuhung · 文章 · ⭐ 2 · 2026-09-18</sub><br>中英双语长文，讨论 Jev 的一步式决策，附本地测试、失败模式和生产环境中的限制，另有一个微决策演示。<br><sub>相关: <a href="https://github.com/kuhung/understanding-jev">repo</a> · <a href="https://askjev.kuhung.me">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/BENZEMA_zzzzzz/status/2102068540530638964"><img src="https://pbs.twimg.com/media/HSwMMToacAAsAh3.jpg?name=orig" alt="公开 Jev 交易仓库评测" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/BENZEMA_zzzzzz/status/2102068540530638964">公开 Jev 交易仓库评测</a></b><br><sub>BENZEMA_zzzzzz · X · ▶ 57 · 2026-09-21</sub><br>帖子串，评测三个在 Kalshi 或 Polymarket 上交易短周期 BTC 窗口的公开 Jev 交易仓库，发现代码有参考价值，但没有可独立验证的交易优势。</td>
</tr>
<tr>
<td width="260" valign="top"></td>
<td valign="top"><b><a href="https://x.com/theanandprasad/status/2102199067057307900">用开源 LLM 做出类 Jev 的决策</a></b><br><sub>theanandprasad · X · ▶ 49 · 2026-09-22</sub><br>帖子串，讲解如何不经训练就从廉价的开源 LLM 得到 Jev 式的快速决策：让提示词结尾停在“Answer:”，再比较允许的答案 token 的 logits。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/ranjankumar/status/2101953564834934999"><img src="https://pbs.twimg.com/tweet_video_thumb/HSujm_1bMAAdo_K.jpg" alt="Jev 在 agent harness 中的位置" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/ranjankumar/status/2101953564834934999">Jev 在 agent harness 中的位置</a></b><br><sub>ranjankumar · X · ▶ 47 · 2026-09-21</sub><br>认为 Jev 给出的排序可信，但置信度数值不可信，因此路由和排序可以直接使用它，而像批准转账这样的阈值关卡需要先做校准。<br><sub>相关: <a href="https://ranjankumar.in/jev-system-one-model-agent-harness-placement">article</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/0xthe0/status/2102213100174741995"><img src="https://pbs.twimg.com/media/HSrq8uWXoAAQ7FF.jpg" alt="Jev 剪枝不是记忆" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/0xthe0/status/2102213100174741995">Jev 剪枝不是记忆</a></b><br><sub>0xthe0 · X · ▶ 24 · 2026-09-22</sub><br>批评基于 Jev 为 Claude Code 做上下文压缩：在一秒内把 1M token 的会话剪到 86K，本质是打分再删除，一次回放就删掉了 16 个后来还要用到的片段。<br><sub>相关: <a href="https://x.com/0xthe0/status/2101751238509400153">article</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/ZataZhang/ZataTree/tree/hugo/content/post/DeepLearning/models_and_strategies/Jev：不写字的决策模型，和它真正适合解决的问题"><img src="https://opengraph.githubassets.com/1/ZataZhang/ZataTree" alt="Jev：不写字的决策模型" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/ZataZhang/ZataTree/tree/hugo/content/post/DeepLearning/models_and_strategies/Jev：不写字的决策模型，和它真正适合解决的问题">Jev：不写字的决策模型</a></b><br><sub>ZataZhang · 文章 · ⭐ 8 仓库 · 2026-09-20</sub><br>个人知识博客上的中文长文，讲解 Jev 和 System One 这两个名字的由来、它的类型化输出与 LLM 生成有何不同，以及它真正适合解决哪些问题。<br><sub>相关: <a href="https://github.com/ZataZhang/ZataTree">repo</a> · <a href="https://www.zata.cc/">site</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/shimo4228/contemplative-agent/blob/main/rfcs/0040-jev-system-one-local-decision-backend.md"><img src="https://opengraph.githubassets.com/1/shimo4228/contemplative-agent" alt="把 Jev 作为本地决策后端（RFC）" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/shimo4228/contemplative-agent/blob/main/rfcs/0040-jev-system-one-local-decision-backend.md">把 Jev 作为本地决策后端（RFC）</a></b><br><sub>shimo4228 · GitHub · ⭐ 6 仓库 · 2026-03-08</sub><br>Contemplative Agent 项目中的一份 RFC 和由使用者自行运行的评测分支，讨论把只做判断的 LLM 调用迁移到 Jev 或本地的类 Jev 模型上；按照 TypeSafe 的客户协议，Jev 的评测数据不放进公开代码树。<br><sub>相关: <a href="https://github.com/shimo4228/contemplative-agent">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"></td>
<td valign="top"><b><a href="https://typesafe.ai/blog/ai-too-good-to-be-true-too-bad-to-be-useful-typesafe-ai">AI：好得难以置信，差得无法使用</a></b><br><sub>TypeSafe AI · 文章 · 2026-06-19</sub><br>官方文章，收录 Diogo Almeida 在 AI Council 的演讲，论证经过偏好优化的聊天模型并不适合自动化，并阐述决策模型的价值。<br><sub>相关: <a href="https://www.youtube.com/watch?v=o-y1HJ6buGQ">video</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://qiita.com/GeneLab_999/items/116aa006fbf93b68d791"><img src="https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-user-contents.imgix.net%2Fhttps%253A%252F%252Fcdn.qiita.com%252Fassets%252Fpublic%252Farticle-ogp-background-afbab5eb44e0b055cce1258705637a91.png%3Fixlib%3Drb-4.1.1%26w%3D1200%26blend64%3DaHR0cHM6Ly9xaWl0YS11c2VyLXByb2ZpbGUtaW1hZ2VzLmltZ2l4Lm5ldC9odHRwcyUzQSUyRiUyRnFpaXRhLWltYWdlLXN0b3JlLnMzLmFwLW5vcnRoZWFzdC0xLmFtYXpvbmF3cy5jb20lMkYwJTJGMzkwODk4MSUyRnByb2ZpbGUtaW1hZ2VzJTJGMTc4NzU1NDY5OD9peGxpYj1yYi00LjEuMSZhcj0xJTNBMSZmaXQ9Y3JvcCZtYXNrPWVsbGlwc2UmYmc9RkZGRkZGJmZtPXBuZzMyJnM9OGVkMDdmYzA3YzdlYmNlNzQ2YTA3MGFhY2ViYzNlZjk%26blend-x%3D120%26blend-y%3D467%26blend-w%3D82%26blend-h%3D82%26blend-mode%3Dnormal%26s%3D74b1732623ee7ae4a142be36aba01640?ixlib=rb-4.1.1&amp;w=1200&amp;fm=jpg&amp;mark64=aHR0cHM6Ly9xaWl0YS11c2VyLWNvbnRlbnRzLmltZ2l4Lm5ldC9-dGV4dD9peGxpYj1yYi00LjEuMSZ3PTk2MCZoPTMyNCZ0eHQ9SmV2JUUzJTgxJUEzJUUzJTgxJUE2JUUzJTgxJUFBJUUzJTgyJTkzJUUzJTgxJUEwJUVGJUJDJTlGJTIwJUUyJTgwJTk0JTIwJUU2JTk2JTg3JUU3JUFCJUEwJUUzJTgyJTkyJUU2JTlCJUI4JUUzJTgxJThCJUUzJTgxJUFBJUUzJTgxJTg0QUklRTMlODElQUIlRTMlODAlODFMTE0lRTMlODElQUVpZiVFNiU5NiU4NyVFNSU4OCVBNCVFNSVBRSU5QSVFMyU4MiU5MiVFNCVCQiVCQiVFMyU4MSU5QiVFMyU4MiU4OSVFMyU4MiU4QyVFMyU4MiU4QiVFMyU4MSU4QiZ0eHQtYWxpZ249bGVmdCUyQ3RvcCZ0eHQtY29sb3I9JTIzMUUyMTIxJnR4dC1mb250PUhpcmFnaW5vJTIwU2FucyUyMFc2JnR4dC1zaXplPTU2JnR4dC1wYWQ9MCZzPWFjNTdiZDkzMzEwYTBjNzI2MzU2NTNlZDQ3NDYzMjI3&amp;mark-x=120&amp;mark-y=112&amp;blend64=aHR0cHM6Ly9xaWl0YS11c2VyLWNvbnRlbnRzLmltZ2l4Lm5ldC9-dGV4dD9peGxpYj1yYi00LjEuMSZ3PTgzOCZoPTU4JnR4dD0lNDBHZW5lTGFiXzk5OSZ0eHQtY29sb3I9JTIzMUUyMTIxJnR4dC1mb250PUhpcmFnaW5vJTIwU2FucyUyMFc2JnR4dC1zaXplPTM2JnR4dC1wYWQ9MCZzPWQ5MDQ1MWRmNGZkZGQwNWUzOGQyNjg4ZTlkOTg1ZTll&amp;blend-x=242&amp;blend-y=480&amp;blend-w=838&amp;blend-h=46&amp;blend-fit=crop&amp;blend-crop=left%2Cbottom&amp;blend-mode=normal&amp;s=11a9ae24aa2246524298dba956a6d7bb" alt="Jev 能接管 LLM 的 if 语句吗？" width="240"></a></td>
<td valign="top"><b><a href="https://qiita.com/GeneLab_999/items/116aa006fbf93b68d791">Jev 能接管 LLM 的 if 语句吗？</a></b><br><sub>GeneLab_999 · 文章 · 2026-09-17</sub><br>日文分析：不调用 API，只凭公开的 SDK 和文档示例，检查 Jev 能替换哪些代码分支，并指出官方文档之间的两处矛盾。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://digidai.github.io/2026/09/21/typesafe-jev-jevable-decision-models/"><img src="https://digidai.github.io/images/articles/typesafe-jev-jevable-decision-models/cover-v1.jpg?v=2026-09-21" alt="从模型发布到 Jevable 上的早期项目" width="240"></a></td>
<td valign="top"><b><a href="https://digidai.github.io/2026/09/21/typesafe-jev-jevable-decision-models/">从模型发布到 Jevable 上的早期项目</a></b><br><sub>Gene Dai · 文章 · 2026-09-21</sub><br>长文，借 Jevable 上收录的 194 个早期项目说明常见的分工方式：由其他软件提供选项、Jev 在其中做选择，也谈到低廉的 token 价格没有算进去的东西。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://zenn.dev/watany/articles/36e11a20ce3743"><img src="https://res.cloudinary.com/zenn/image/upload/s--p7nC-kx3--/c_fit%2Cg_north_west%2Cl_text:notosansjp-medium.otf_55:Jev%25E3%2581%25A7%25E3%2583%258F%25E3%2583%25BC%25E3%2583%258D%25E3%2582%25B9%25E3%2582%25A8%25E3%2583%25B3%25E3%2582%25B8%25E3%2583%258B%25E3%2582%25A2%25E3%2583%25AA%25E3%2583%25B3%25E3%2582%25B0%2Cw_1010%2Cx_90%2Cy_100/g_south_west%2Cl_text:notosansjp-medium.otf_37:watany%2Cx_203%2Cy_121/g_south_west%2Ch_90%2Cl_fetch:aHR0cHM6Ly9zdGF0aWMuemVubi5zdHVkaW8vdXNlci11cGxvYWQvYXZhdGFyLzJiYjJiYTdkZjkuanBlZw==%2Cr_max%2Cw_90%2Cx_87%2Cy_95/v1627283836/default/og-base-w1200-v2.png?_a=BACMTiAE" alt="用 Jev 做 harness 工程" width="240"></a></td>
<td valign="top"><b><a href="https://zenn.dev/watany/articles/36e11a20ce3743">用 Jev 做 harness 工程</a></b><br><sub>watany · 文章 · 2026-09-18</sub><br>日文文章，讲如何把 Jev 用作 agent harness 中偏确定性的一环，并说明通过候补名单、Vercel AI Gateway 或 Cloudflare 获取访问的方法。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://qiita.com/hisashi-ito/items/3d8d26ea591009e7a58e"><img src="https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-user-contents.imgix.net%2Fhttps%253A%252F%252Fcdn.qiita.com%252Fassets%252Fpublic%252Farticle-ogp-background-afbab5eb44e0b055cce1258705637a91.png%3Fixlib%3Drb-4.1.1%26w%3D1200%26blend64%3DaHR0cHM6Ly9xaWl0YS11c2VyLXByb2ZpbGUtaW1hZ2VzLmltZ2l4Lm5ldC9odHRwcyUzQSUyRiUyRnFpaXRhLWltYWdlLXN0b3JlLnMzLmFwLW5vcnRoZWFzdC0xLmFtYXpvbmF3cy5jb20lMkYwJTJGODgzMTYlMkZwcm9maWxlLWltYWdlcyUyRjE3MDgwODAxMjM_aXhsaWI9cmItNC4xLjEmYXI9MSUzQTEmZml0PWNyb3AmbWFzaz1lbGxpcHNlJmJnPUZGRkZGRiZmbT1wbmczMiZzPTdlYWZmOGJmYjU1NzNlNDAzOGMxMjM3ZWUzMjQ4MWNl%26blend-x%3D120%26blend-y%3D467%26blend-w%3D82%26blend-h%3D82%26blend-mode%3Dnormal%26s%3D21470933a45a0ec36724c827775f7517?ixlib=rb-4.1.1&amp;w=1200&amp;fm=jpg&amp;mark64=aHR0cHM6Ly9xaWl0YS11c2VyLWNvbnRlbnRzLmltZ2l4Lm5ldC9-dGV4dD9peGxpYj1yYi00LjEuMSZ3PTk2MCZoPTMyNCZ0eHQ9SmV2JUVGJUJDJTg4VHlwZVNhZmUlMjBBSSVFRiVCQyU4OSVFMyU4MSVBRiVFMyU4MSVCRiVFMyU4MiU5MyVFMyU4MSVBQSVFMyU4MSVBOSVFMyU4MSU4NiVFMyU4MiU4NCVFMyU4MSVBMyVFMyU4MSVBNiVFNCVCRCVCRiVFMyU4MSVBMyVFMyU4MSVBNiVFMyU4MSU4NCVFMyU4MiU4QiVFMyU4MSVBRSVFMyU4MSU4QiVFRiVCQyU5RiZ0eHQtYWxpZ249bGVmdCUyQ3RvcCZ0eHQtY29sb3I9JTIzMUUyMTIxJnR4dC1mb250PUhpcmFnaW5vJTIwU2FucyUyMFc2JnR4dC1zaXplPTU2JnR4dC1wYWQ9MCZzPWJjMTljMjZjY2VkZjM0YmIyYmQ3ZjI0OWM0NmFhNTRh&amp;mark-x=120&amp;mark-y=112&amp;blend64=aHR0cHM6Ly9xaWl0YS11c2VyLWNvbnRlbnRzLmltZ2l4Lm5ldC9-dGV4dD9peGxpYj1yYi00LjEuMSZ3PTgzOCZoPTU4JnR4dD0lNDBoaXNhc2hpLWl0byZ0eHQtY29sb3I9JTIzMUUyMTIxJnR4dC1mb250PUhpcmFnaW5vJTIwU2FucyUyMFc2JnR4dC1zaXplPTM2JnR4dC1wYWQ9MCZzPTU4ZmY0ZGQwMDRlY2ZjMDkxZGM3Y2ZkZWFhMWRlMTU5&amp;blend-x=242&amp;blend-y=480&amp;blend-w=838&amp;blend-h=46&amp;blend-fit=crop&amp;blend-crop=left%2Cbottom&amp;blend-mode=normal&amp;s=7ac19a0ac6f09481b52bbb2f0895087b" alt="大家都在怎么用 Jev？" width="240"></a></td>
<td valign="top"><b><a href="https://qiita.com/hisashi-ito/items/3d8d26ea591009e7a58e">大家都在怎么用 Jev？</a></b><br><sub>hisashi-ito · 文章 · 2026-09-18</sub><br>日文调查，统计了截至发布后第六天 GitHub 和 X 上的公开 Jev 项目，并用图表展示人们拿它做什么。</td>
</tr>
<tr>
<td width="260" valign="top"></td>
<td valign="top"><b><a href="https://docs.bswen.com/blog/2026-09-18-jev-system-one-smart-if/">Jev 是“聪明的 if”吗？</a></b><br><sub>BSWEN (Cowrie Dev) · 文章 · 2026-09-19</sub><br>在 Jev Playground 上的实测表明，Jev 不会像确定性的 if/else 代码那样执行用户写的规则，它最适合的角色是 agent 内部的低延迟决策层。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://flowtivity.ai/blog/jev-typesafe-ai-decision-model/"><img src="https://flowtivity.ai/api/blog/media/blog/1789561319551-hero-8ugxup.svg" alt="快 200 倍的决策模型是否好得不真实？" width="240"></a></td>
<td valign="top"><b><a href="https://flowtivity.ai/blog/jev-typesafe-ai-decision-model/">快 200 倍的决策模型是否好得不真实？</a></b><br><sub>AJ Awan (Flowtivity) · 文章 · 2026-09-16</sub><br>逐条审查 TypeSafe 发布时宣称的快 200 倍、便宜 400 倍，附定价测算以及 Hacker News 上的质疑声音。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://cobusgreyling.medium.com/jev-by-typesafe-ai-4846aaca3186"><img src="https://cdn-images-1.medium.com/max/1024/1*4ZmFqv_O6qa2pr_rWu1Skw.png" alt="TypeSafe AI 的 Jev" width="240"></a></td>
<td valign="top"><b><a href="https://cobusgreyling.medium.com/jev-by-typesafe-ai-4846aaca3186">TypeSafe AI 的 Jev</a></b><br><sub>Cobus Greyling · 文章 · 2026-09-21</sub><br>随笔，把 Jev 视为机器原生的智能，并谈如何引入：先影子运行一个现有决策，按置信度把关，瞄准高频岔路，并与 LLM 搭配而不是取代它们。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://dev.to/miruky/jev-does-not-replace-the-llm-it-changes-who-owns-the-decision-3n6"><img src="https://media2.dev.to/dynamic/image/width=1200,height=627,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Farticles%2Fan164emsrub8iv34h66e.png" alt="Jev 改变了由谁掌握决策" width="240"></a></td>
<td valign="top"><b><a href="https://dev.to/miruky/jev-does-not-replace-the-llm-it-changes-who-owns-the-decision-3n6">Jev 改变了由谁掌握决策</a></b><br><sub>miruky · 文章 · 2026-09-19</sub><br>用 mock 响应审视 Jev 的 API 约定和 SDK 行为，厘清“零幻觉”的确切含义，并在 Jev、LLM 和代码之间分工，由代码负责策略和精确计算。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://medium.com/@thealonemusk/jev-doesnt-chat-that-might-be-the-point-2f12663c661f"><img src="https://cdn-images-1.medium.com/max/1024/1*0-D3Ied-psYthZzWJZsOag.png" alt="Jev 不聊天，也许这正是重点" width="240"></a></td>
<td valign="top"><b><a href="https://medium.com/@thealonemusk/jev-doesnt-chat-that-might-be-the-point-2f12663c661f">Jev 不聊天，也许这正是重点</a></b><br><sub>Ashutosh Jha · 文章 · 2026-09-18</sub><br>逐条批评 System One 的发布：命名、架构、经济性、Doom 演示依赖结构化 state 这一前提，以及为什么抵御提示词注入对决策层很重要。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://www.aibuilderclub.com/blog/jev-engineering-guide"><img src="https://www.aibuilderclub.com/images/blog/jev-engineering-three-role-loop.png" alt="Jev 工程指南" width="240"></a></td>
<td valign="top"><b><a href="https://www.aibuilderclub.com/blog/jev-engineering-guide">Jev 工程指南</a></b><br><sub>AI Jason (AI Builder Club) · 文章 · 2026-09-22</sub><br>一种 agent 模式：LLM 负责写，Jev 负责决策，代码负责执行，通过 Claude Code 守卫 hook、模型路由器和日志分拣定时任务来展示；回放 600 条日志花费 $0.00029，中位延迟 302 毫秒。<br><sub><b>Jev 用法:</b> 用类型化的 Choice/Score/Noul 分岔，阈值写在代码里；只有不确定的情况才升级给 Claude Code。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://qiita.com/ryu-ki/items/e3fe99b5f6704d08a19b"><img src="https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-user-contents.imgix.net%2Fhttps%253A%252F%252Fcdn.qiita.com%252Fassets%252Fpublic%252Farticle-ogp-background-afbab5eb44e0b055cce1258705637a91.png%3Fixlib%3Drb-4.1.1%26w%3D1200%26blend64%3DaHR0cHM6Ly9xaWl0YS11c2VyLXByb2ZpbGUtaW1hZ2VzLmltZ2l4Lm5ldC9odHRwcyUzQSUyRiUyRnMzLWFwLW5vcnRoZWFzdC0xLmFtYXpvbmF3cy5jb20lMkZxaWl0YS1pbWFnZS1zdG9yZSUyRjAlMkYzOTIxODAyJTJGMzM4YjUwMmZkNzA3YWQ4YjkwYWU3MWRkYzgwNGFhNTdjYmNlM2JjZiUyRmxhcmdlLnBuZyUzRjE3ODA3MTQyMDI_aXhsaWI9cmItNC4xLjEmYXI9MSUzQTEmZml0PWNyb3AmbWFzaz1lbGxpcHNlJmJnPUZGRkZGRiZmbT1wbmczMiZzPTRiYTY3MTIxMTc3N2QzNzQ5NTIxMjc5NmMyNmJiNTk1%26blend-x%3D120%26blend-y%3D462%26blend-w%3D90%26blend-h%3D90%26blend-mode%3Dnormal%26mark64%3DaHR0cHM6Ly9xaWl0YS1vcmdhbml6YXRpb24taW1hZ2VzLmltZ2l4Lm5ldC9odHRwcyUzQSUyRiUyRnMzLWFwLW5vcnRoZWFzdC0xLmFtYXpvbmF3cy5jb20lMkZxaWl0YS1vcmdhbml6YXRpb24taW1hZ2UlMkY1NTdmMmM4MGU4N2IwMjhhMjU3ZTIwMjQzZmU4ZTYzNWYxNzFiNDE1JTJGb3JpZ2luYWwuanBnJTNGMTc4Mjg4MTcwMD9peGxpYj1yYi00LjEuMSZ3PTQ0Jmg9NDQmZml0PWNyb3AmbWFzaz1jb3JuZXJzJmNvcm5lci1yYWRpdXM9OCZiZz1GRkZGRkYmYm9yZGVyPTIlMkNGRkZGRkYmZm09cG5nMzImcz1kNThhMjUwOWQ0ZDUwMGE5MmU0MTIwZTc1OGZmNzEzMQ%26mark-x%3D186%26mark-y%3D515%26mark-w%3D40%26mark-h%3D40%26s%3Db305af80e267c0831201b587d6085c96?ixlib=rb-4.1.1&amp;w=1200&amp;fm=jpg&amp;mark64=aHR0cHM6Ly9xaWl0YS11c2VyLWNvbnRlbnRzLmltZ2l4Lm5ldC9-dGV4dD9peGxpYj1yYi00LjEuMSZ3PTk2MCZoPTMyNCZ0eHQ9JUUzJTgwJTkwSmV2JUUzJTgwJTkxJUU2JTk2JTg3JUU3JUFCJUEwJUUzJTgyJTkyJUU4JUJGJTk0JUUzJTgxJTk1JUUzJTgxJUFBJUUzJTgxJTg0JUU1JTg4JUE0JUU2JTk2JUFEJUUzJTgzJUEyJUUzJTgzJTg3JUUzJTgzJUFCJTIwSmV2JTIwJUUzJTgxJUE4JUUzJTgxJUFGJUVGJUJDJTlGJUUzJTgwJTlDJUUzJTgyJUI3JUUzJTgyJUI5JUUzJTgzJTg2JUUzJTgzJUEwJUU5JTgxJThCJUU3JTk0JUE4JUUzJTgxJUE3JUUzJTgxJUFFJUU2JUI0JUJCJUU3JTk0JUE4JUU2JTk2JUI5JUU2JUIzJTk1JUUzJTgxJUFCJUUzJTgxJUE0JUUzJTgxJTg0JUUzJTgxJUE2JUUzJTgyJTgyJUU2JTgzJUIzJUU1JTgzJThGJUUzJTgxJTk3JUUzJTgxJUE2JUUzJTgxJUJGJUUzJTgyJThCJUUzJTgwJTlDJnR4dC1hbGlnbj1sZWZ0JTJDdG9wJnR4dC1jb2xvcj0lMjMxRTIxMjEmdHh0LWZvbnQ9SGlyYWdpbm8lMjBTYW5zJTIwVzYmdHh0LXNpemU9NTYmdHh0LXBhZD0wJnM9NzlhNmQwZDVkMjM0NjViYzJiMGExNzlhMmQyMDY3ZWY&amp;mark-x=120&amp;mark-y=112&amp;blend64=aHR0cHM6Ly9xaWl0YS11c2VyLWNvbnRlbnRzLmltZ2l4Lm5ldC9-dGV4dD9peGxpYj1yYi00LjEuMSZ3PTgzOCZoPTU4JnR4dD0lNDByeXUta2kmdHh0LWNvbG9yPSUyMzFFMjEyMSZ0eHQtZm9udD1IaXJhZ2lubyUyMFNhbnMlMjBXNiZ0eHQtc2l6ZT0zNiZ0eHQtcGFkPTAmcz1iZTI4YjM3MDJlNmVlMTE3YTVmODA3MWNkZmE5MWI2Mg&amp;blend-x=242&amp;blend-y=454&amp;blend-w=838&amp;blend-h=46&amp;blend-fit=crop&amp;blend-crop=left%2Cbottom&amp;blend-mode=normal&amp;txt64=VElTSeagquW8j-S8muekvg&amp;txt-x=242&amp;txt-y=539&amp;txt-width=838&amp;txt-clip=end%2Cellipsis&amp;txt-color=%231E2121&amp;txt-font=Hiragino%20Sans%20W6&amp;txt-size=28&amp;s=f8d06f197ddc5be1166c8224419079f7" alt="用 Jev 做系统运维" width="240"></a></td>
<td valign="top"><b><a href="https://qiita.com/ryu-ki/items/e3fe99b5f6704d08a19b">用 Jev 做系统运维</a></b><br><sub>ryu-ki · 文章 · 2026-09-18</sub><br>日文文章，先总结文档中关于 Jev 的说明，再给出把它用于系统运维工作（如告警处理）的思路。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://zenn.dev/meijin/articles/jev-impressions"><img src="https://res.cloudinary.com/zenn/image/upload/s--W4LKp311--/c_fit%2Cg_north_west%2Cl_text:notosansjp-medium.otf_55:Jev%2520%25E6%2589%2580%25E6%2584%259F%2520%25E3%2583%2580%25E3%2583%25A9%25E3%2583%2580%25E3%2583%25A9%25E3%2581%25A8%25E6%259B%25B8%25E3%2581%258F%2Cw_1010%2Cx_90%2Cy_100/g_south_west%2Cl_text:notosansjp-medium.otf_37:meijin%2Cx_203%2Cy_121/g_south_west%2Ch_90%2Cl_fetch:aHR0cHM6Ly9saDMuZ29vZ2xldXNlcmNvbnRlbnQuY29tL2EtL0FPaDE0R2pPWmtyWk1nS3djRXl5a2w1X2lVTFZFVmtVVUpkNzkzcjlfejhERjRzPXMyNTAtYw==%2Cr_max%2Cw_90%2Cx_87%2Cy_95/v1627283836/default/og-base-w1200-v2.png?_a=BACMTiAE" alt="Jev 使用感想" width="240"></a></td>
<td valign="top"><b><a href="https://zenn.dev/meijin/articles/jev-impressions">Jev 使用感想</a></b><br><sub>meijin · 文章 · 2026-09-18</sub><br>日文笔记，谈 Jev 适合用在哪里：在 Browser Use 这类工具里与读取 state 的 LLM 搭配，由 Jev 选下一步动作；以及根据用户上下文选择下一个 UI，并以 LLM 兜底。</td>
</tr>
<tr>
<td width="260" valign="top"></td>
<td valign="top"><b><a href="https://simonwillison.net/2026/Sep/21/jev/">Jev 带来了一种新形态的 LLM</a></b><br><sub>Simon Willison · 文章 · 2026-09-21</sub><br>把 Jev 解释为返回数字而非文本的“决策模型”，介绍其定价和问题类型，提到先用 BM25 再用 Jev 做搜索重排的实验，并提出黑箱和偏见方面的担忧。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://medium.com/@creativeaininja/typesafes-jev-makes-ai-decisions-fast-enough-to-play-doom-68fdcce1159a"><img src="https://miro.medium.com/v2/resize:fit:700/1*7UqArSYtCxH4sok--XJFZA.png" alt="Jev 让 AI 决策快到能玩 Doom" width="240"></a></td>
<td valign="top"><b><a href="https://medium.com/@creativeaininja/typesafes-jev-makes-ai-decisions-fast-enough-to-play-doom-68fdcce1159a">Jev 让 AI 决策快到能玩 Doom</a></b><br><sub>Kristopher Dunham · 文章 · 2026-09-17</sub><br>讲解毫秒级类型化决策如何支撑实时控制循环，比如 TypeSafe 的 Doom 演示和社区做的 Super Mario agent，其中游戏 state 以结构化文本而不是像素的形式输入。<br><sub>相关: <a href="https://github.com/fhshaik/typesafe-mario">related</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"></td>
<td valign="top"><b><a href="https://www.seangoedecke.com/jev-means-structured-output-is-interesting-again/">Jev 让结构化输出重新变得有意思</a></b><br><sub>Sean Goedecke · 文章 · 2026-09-16</sub><br>解释决策模型的延迟为何稳定，以及在开源模型上用预填充（prefill）加单 token 约束解码能做到什么程度。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/myokoym/misereru-slide-jev"><img src="https://opengraph.githubassets.com/1/myokoym/misereru-slide-jev" alt="Jev 研究幻灯片" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/myokoym/misereru-slide-jev">Jev 研究幻灯片</a></b><br><sub>myokoym · GitHub · 2026-09-17</sub><br>持续更新的日文 Jev 与 System One 模型研究，以 Markdown 幻灯片、演讲稿和文章的形式维护，背后有一份记录来源、第三方验证和注意事项的台账。<br><sub>相关: <a href="https://myokoym.github.io/misereru-slide-jev/">slides</a> · <a href="https://myokoym.github.io/misereru-slide-jev">write-up</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://lilting.ch/en/articles/typesafe-ai-jev-system-one-model"><img src="https://lilting.ch/og/images/hero/ogp.ogp.jpg" alt="Jev 对比自回归 LLM 与 MDLM" width="240"></a></td>
<td valign="top"><b><a href="https://lilting.ch/en/articles/typesafe-ai-jev-system-one-model">Jev 对比自回归 LLM 与 MDLM</a></b><br><sub>lilting channel · 文章 · 2026-09-17</sub><br>技术对比：Jev 的单次并行采样器与逐 token 的自回归解码、掩码扩散语言模型有何不同，同时介绍定价和 RLCD 校准。</td>
</tr>
<tr>
<td width="260" valign="top"></td>
<td valign="top"><b><a href="https://wonderwhy-er.medium.com/typesafe-jev-wont-train-on-your-data-it-can-still-learn-from-it-563f0ad591b6">Jev 不会用你的数据训练</a></b><br><sub>Eduard Ruzga · 文章 · 2026-09-19</sub><br>审视 Jev“更便宜、更快、通用性更弱”的取舍和 TypeSafe 的客户协议，追问在厂商承诺不用你的数据训练的前提下，“衍生遥测”到底允许做什么。</td>
</tr>
<tr>
<td width="260" valign="top"></td>
<td valign="top"><b><a href="https://zhuanlan.zhihu.com/p/2085057727869593002">Jev 零幻觉深度剖析</a></b><br><sub>Zhihu · 文章</sub><br>中文深度文章，审视 TypeSafe Jev 关于 System One“零幻觉”的说法，以及这些说法在多大程度上站得住。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://www.turingpost.com/p/what-is-jev-rlcd"><img src="https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,quality=80,width=1200,onerror=redirect/uploads/asset/file/73da3503-3fd3-4221-98a3-d07a8c8d8398/guide2_1_.jpg?t=1789781447" alt="Jev、RLCD 与 AI 分类器的再发明" width="240"></a></td>
<td valign="top"><b><a href="https://www.turingpost.com/p/what-is-jev-rlcd">Jev、RLCD 与 AI 分类器的再发明</a></b><br><sub>Turing Post (Ksenia Se) · 文章 · 2026-09-19</sub><br>指南，剖析目前关于 Jev 和 RLCD 的已知信息，追溯它所结合的更早的研究思路，并列出开源替代方案和 12 篇相关论文。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://pearpages.com/blog/2026/09/16/jev-sorted-what-typesafes-system-one-model-actually-is-and-what-is-still-just-a-claim"><img src="https://pearpages.com/assets/images/og-c2daec938fe24aa01d8d6904d87cb17d.webp" alt="把 Jev 捋清楚" width="240"></a></td>
<td valign="top"><b><a href="https://pearpages.com/blog/2026/09/16/jev-sorted-what-typesafes-system-one-model-actually-is-and-what-is-still-just-a-claim">把 Jev 捋清楚</a></b><br><sub>Pere Pages · 文章 · 2026-09-16</sub><br>研读发布宣称背后的一手资料，结论是 Jev 是一个比宣传更窄、也更有意思的、面向软件的前沿级训练分类器，而所有基准测试仍然是厂商自报的。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://aiwithmike.substack.com/p/jev-three-days-in-what-is-known-what"><img src="https://substackcdn.com/image/fetch/$s_!ArAN!,w_1200,h_675,c_fill,f_jpg,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F35dc9b92-6756-4ae9-a779-a232ad7c1992_1024x559.jpeg" alt="Jev 发布三天" width="240"></a></td>
<td valign="top"><b><a href="https://aiwithmike.substack.com/p/jev-three-days-in-what-is-known-what">Jev 发布三天</a></b><br><sub>Mike Erlihson · 文章 · 2026-09-18</sub><br>发布三天后的盘点，区分关于 Jev 哪些已被独立测量、哪些只是猜测，以及它适合用在哪里。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://www.linkedin.com/pulse/qu%C3%A9-es-jev-el-modelo-system-one-de-typesafe-ai-que-en-kraayenbrink-g65ff/"><img src="https://media.licdn.com/dms/image/v2/D4D12AQGc13qIPizL8Q/article-cover_image-shrink_720_1280/B4DaDCI.CLIAAQ-/0/1789963526522?e=2147483647&amp;v=beta&amp;t=L_Pc-zhjp2Ac7fdpe-6kwPPqvZCvxOEdBc4gmB2zrWM" alt="Jev 是什么" width="240"></a></td>
<td valign="top"><b><a href="https://www.linkedin.com/pulse/qu%C3%A9-es-jev-el-modelo-system-one-de-typesafe-ai-que-en-kraayenbrink-g65ff/">Jev 是什么</a></b><br><sub>Jon Kraayenbrink · 文章 · 2026-09-21</sub><br>西班牙语讲解，介绍 System One 的理念、相对 LLM 的真实成本，以及人们在用它做什么，依据是对 9 月 15 日至 21 日间 269 人发布的 295 个公开 Jev 项目的索引。</td>
</tr>
<tr>
<td width="260" valign="top"></td>
<td valign="top"><b><a href="https://juejin.cn/post/7687793891199418374">别再吹 Jev 了</a></b><br><sub>stormzhang · 文章 · 2026-09-21</sub><br>中文唱反调文章：Jev 在路由、护栏和批量文档处理上有用，但能力与 DeepSeek Flash 相当，“无幻觉”是换了定义，而且开源复刻在 48 小时内就出现了。</td>
</tr>
<tr>
<td width="260" valign="top"></td>
<td valign="top"><b><a href="https://juejin.cn/post/7687825526383624207">测试 Jev 的概率校准</a></b><br><sub>Hogwarts Testing (霍格沃兹测试开发) · 文章 · 2026-09-21</sub><br>中文文章，讨论 QA 工程师该如何测试 Jev 这类 AI 决策系统：不仅要检查答案对不对，还要检查声称的置信度（如 95%）是否与真实准确率相符。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://www.completeskeptic.com/p/the-bitterest-lesson"><img src="https://substackcdn.com/image/fetch/$s_!Whnc!,w_1200,h_675,c_fill,f_jpg,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F89cfa8bd-40b0-4c8d-a0d1-90435054c92a_1894x1016.png" alt="最苦涩的教训" width="240"></a></td>
<td valign="top"><b><a href="https://www.completeskeptic.com/p/the-bitterest-lesson">最苦涩的教训</a></b><br><sub>Diogo Almeida · 文章 · 2026-09-10</sub><br>TypeSafe CEO 的随笔（也发布在 TypeSafe 博客上），认为模型一旦被训练去做错误的任务，靠算力驱动的进步就白费了，这正是为软件打造决策模型背后的论点。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://warmersun.com/jev/"><img src="https://here.now/og/jovial-cottage-dwgn.jpg" alt="要类型化决策，不要聊天" width="240"></a></td>
<td valign="top"><b><a href="https://warmersun.com/jev/">要类型化决策，不要聊天</a></b><br><sub>Warmer Sun · 文章 · 2026-09-17</sub><br>独立的 Jev 技术走查，把 TypeSafe 的发布宣称与公开证据真正能证实的内容区分开，并附可供检查的审计记录。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://actionbox.cloud/blog/typesafe-ai-jev-review/"><img src="https://actionbox.cloud/blog/images/typesafe-jev-intelligence-cost.webp" alt="TypeSafe AI Jev 评测" width="240"></a></td>
<td valign="top"><b><a href="https://actionbox.cloud/blog/typesafe-ai-jev-review/">TypeSafe AI Jev 评测</a></b><br><sub>ActionBox (Suson Sapkota) · 文章 · 2026-09-15</sub><br>抢先体验评测，检查了 Playground、原始 API 和 SDK 示例，再把 Jev 与规则、分类器、重排器和 LLM 评判器做比较，并审视发布时基准测试的局限。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://www.theneuron.ai/explainer-articles/typesafe-jev-system-one-models-explained/"><img src="https://cdn.theneuron.ai/TypeSafe%20JEV%20Structured%20Decisions%20Beyond%20Chat.png?w=1024" alt="TypeSafe JEV 详解" width="240"></a></td>
<td valign="top"><b><a href="https://www.theneuron.ai/explainer-articles/typesafe-jev-system-one-models-explained/">TypeSafe JEV 详解</a></b><br><sub>Grant Harvey (The Neuron) · 文章 · 2026-09-16</sub><br>用大白话讲解为什么软件决策也许并不需要聊天机器人，涵盖并行的 System One 设计、RLCD 校准、企业适用性以及最有力的反方观点。</td>
</tr>
<tr>
<td width="260" valign="top"></td>
<td valign="top"><b><a href="https://www.developersdigest.tech/blog/typesafe-jev-system-one-models-release-guide-2026">TypeSafe Jev 的基准测试与定价</a></b><br><sub>Developers Digest · 文章 · 2026-09-16</sub><br>发布当周的技术速览，涵盖 Jev 的原语、并行采样器和 RLCD 训练、已公布的工作流评测及其注意事项、定价，以及 API、SDK 和 agent skill 等接入方式。</td>
</tr>
<tr>
<td width="260" valign="top"></td>
<td valign="top"><b><a href="https://docs.typesafe.ai/patterns">TypeSafe 设计模式</a></b><br><sub>TypeSafe AI · 文档</sub><br>官方指南，介绍用 Jev 构建应用的架构模式：推测式扇出、按置信度把关的路由、组合打分和意图路由。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/dnakhoa/jev-deferred-crispification"><img src="https://opengraph.githubassets.com/1/dnakhoa/jev-deferred-crispification" alt="Jev 缺了什么" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/dnakhoa/jev-deferred-crispification">Jev 缺了什么</a></b><br><sub>dnakhoa · GitHub · 2026-09-16</sub><br>立场论文，认为逐跳校准在决策流水线中无法叠加组合，而类型化答案会抹掉模糊性，提出隐马尔可夫和模糊逻辑原语以及一种名为 BSF-S1 的架构。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://note.com/kagawatomo/n/n5425654d0f5d"><img src="https://assets.st-note.com/production/uploads/images/314812501/rectangle_large_type_2_ec7e04d489da5232ca3084c4c3ab514e.png?fit=bounds&amp;quality=85&amp;width=1280" alt="TypeSafe 想用 Jev 做成什么" width="240"></a></td>
<td valign="top"><b><a href="https://note.com/kagawatomo/n/n5425654d0f5d">TypeSafe 想用 Jev 做成什么</a></b><br><sub>香川友志 (kagawatomo) · 文章 · 2026-09-18</sub><br>日文长文分析：Jev 是什么、不是什么，创始人的背景，以及 TypeSafe 押注的方向：把分类、路由、打分、审批和核验决策嵌进软件。</td>
</tr>
<tr>
<td width="260" valign="top"></td>
<td valign="top"><b><a href="https://ranjankumar.in/jev-system-one-model-agent-harness-placement">Jev 在 agent harness 中的位置</a></b><br><sub>Ranjan Kumar · 文章 · 2026-09-21</sub><br>长文分析，认为 Jev 给出的排序可信，但其置信度数值需要在本地重新拟合，并说明决策模型在 agent harness 中应放在哪里、如何用自己的数据设定阈值。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://dev.to/extractdata/jev-the-model-that-cannot-write-a-word-and-where-it-fits-in-web-scraping-does-it-45jb"><img src="https://media2.dev.to/dynamic/image/width=1200,height=627,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fextract.zyte.com%2Fapi%2Fmedia%2Ffile%2Fcnt-1347-01-cover.png" alt="Jev 在网页抓取中的位置" width="240"></a></td>
<td valign="top"><b><a href="https://dev.to/extractdata/jev-the-model-that-cannot-write-a-word-and-where-it-fits-in-web-scraping-does-it-45jb">Jev 在网页抓取中的位置</a></b><br><sub>Ayan Pahwa (Zyte) · 文章 · 2026-09-21</sub><br>认为 Jev 从不输出字符串，所以没法抽取字段，并展示它唯一能胜任的抓取工作：在抽取之前把关，附 requests 和 BeautifulSoup 示例。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://qiita.com/Isaka-code/items/8944ef8b521517f92da0"><img src="https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-user-contents.imgix.net%2Fhttps%253A%252F%252Fcdn.qiita.com%252Fassets%252Fpublic%252Farticle-ogp-background-afbab5eb44e0b055cce1258705637a91.png%3Fixlib%3Drb-4.1.1%26w%3D1200%26blend64%3DaHR0cHM6Ly9xaWl0YS11c2VyLXByb2ZpbGUtaW1hZ2VzLmltZ2l4Lm5ldC9odHRwcyUzQSUyRiUyRnFpaXRhLWltYWdlLXN0b3JlLnMzLmFwLW5vcnRoZWFzdC0xLmFtYXpvbmF3cy5jb20lMkYwJTJGMjYyNzAxNSUyRnByb2ZpbGUtaW1hZ2VzJTJGMTczODM4MDAyOD9peGxpYj1yYi00LjEuMSZhcj0xJTNBMSZmaXQ9Y3JvcCZtYXNrPWVsbGlwc2UmYmc9RkZGRkZGJmZtPXBuZzMyJnM9NjM3MmNhMjU1NmQ2M2IyNzUyZjAwMWY3OWFjNjBiMDY%26blend-x%3D120%26blend-y%3D467%26blend-w%3D82%26blend-h%3D82%26blend-mode%3Dnormal%26s%3D6d046f33d6fa0f0f44d8a349b9b12d4a?ixlib=rb-4.1.1&amp;w=1200&amp;fm=jpg&amp;mark64=aHR0cHM6Ly9xaWl0YS11c2VyLWNvbnRlbnRzLmltZ2l4Lm5ldC9-dGV4dD9peGxpYj1yYi00LjEuMSZ3PTk2MCZoPTMyNCZ0eHQ9SmV2JUUzJTgxJUFGJUUzJTgxJUE5JUUzJTgxJTkzJUUzJTgxJUE3JUU0JUJEJUJGJUUzJTgxJTg2JUUzJTgxJUI5JUUzJTgxJThEJUUzJTgxJThCJUVGJUJDJTlGJTIwTExNJUUzJTgzJUJCJUU2JUE5JTlGJUU2JUEyJUIwJUU1JUFEJUE2JUU3JUJGJTkyJUUzJTgzJUJCJUUzJTgzJUFCJUUzJTgzJUJDJUUzJTgzJUFCJUUzJTgzJTk5JUUzJTgzJUJDJUUzJTgyJUI5JUUzJTgxJUE4JUUzJTgxJUFFJUU0JUJEJUJGJUUzJTgxJTg0JUU1JTg4JTg2JUUzJTgxJTkxJnR4dC1hbGlnbj1sZWZ0JTJDdG9wJnR4dC1jb2xvcj0lMjMxRTIxMjEmdHh0LWZvbnQ9SGlyYWdpbm8lMjBTYW5zJTIwVzYmdHh0LXNpemU9NTYmdHh0LXBhZD0wJnM9NjMxOWY5NjgyMGYwYjgyYjIzZDMxNTQ0MmViZmQ3NmM&amp;mark-x=120&amp;mark-y=112&amp;blend64=aHR0cHM6Ly9xaWl0YS11c2VyLWNvbnRlbnRzLmltZ2l4Lm5ldC9-dGV4dD9peGxpYj1yYi00LjEuMSZ3PTgzOCZoPTU4JnR4dD0lNDBJc2FrYS1jb2RlJnR4dC1jb2xvcj0lMjMxRTIxMjEmdHh0LWZvbnQ9SGlyYWdpbm8lMjBTYW5zJTIwVzYmdHh0LXNpemU9MzYmdHh0LXBhZD0wJnM9ODVjZDg3YWRkMzg5ZjgxODZjMGNkMjdjNGI3NTdmZDc&amp;blend-x=242&amp;blend-y=480&amp;blend-w=838&amp;blend-h=46&amp;blend-fit=crop&amp;blend-crop=left%2Cbottom&amp;blend-mode=normal&amp;s=d5aabfc779d3a385cf32a5f83b19950f" alt="什么场景该用 Jev？" width="240"></a></td>
<td valign="top"><b><a href="https://qiita.com/Isaka-code/items/8944ef8b521517f92da0">什么场景该用 Jev？</a></b><br><sub>Isaka-code · 文章 · 2026-09-19</sub><br>日文指南，讲如何在规则代码、传统机器学习、Jev 和 LLM 之间做选择，以及 Jev 在哪些条件下是合适的工具。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://zenn.dev/1amageek/articles/typesafe-jev-system-one-model"><img src="https://res.cloudinary.com/zenn/image/upload/s--wzI_Yk5V--/c_fit%2Cg_north_west%2Cl_text:notosansjp-medium.otf_55:%25E6%2596%2587%25E5%25AD%2597%25E5%2588%2597%25E3%2582%2592%25E6%258D%25A8%25E3%2581%25A6%25E3%2581%259F%25E3%2583%25A2%25E3%2583%2587%25E3%2583%25AB%25E3%2580%2582Jev%25E3%2581%25AF%25E3%2581%25AA%25E3%2581%259C%25E6%25A1%2581%25E3%2581%25A7%25E9%2580%259F%25E3%2581%2584%25E3%2581%25AE%25E3%2581%258B%2Cw_1010%2Cx_90%2Cy_100/g_south_west%2Cl_text:notosansjp-medium.otf_37:1amageek%2Cx_203%2Cy_121/g_south_west%2Ch_90%2Cl_fetch:aHR0cHM6Ly9saDMuZ29vZ2xldXNlcmNvbnRlbnQuY29tL2EtL0FPaDE0R2dBNEpHWllReTFQVmxXNDFOeHBqZ1Z6a0J3TW9ocjFTQjBMLWgtPXMyNTAtYw==%2Cr_max%2Cw_90%2Cx_87%2Cy_95/v1627283836/default/og-base-w1200-v2.png?_a=BACMTiAE" alt="Jev 为何快了几个数量级" width="240"></a></td>
<td valign="top"><b><a href="https://zenn.dev/1amageek/articles/typesafe-jev-system-one-model">Jev 为何快了几个数量级</a></b><br><sub>1amageek · 文章 · 2026-09-17</sub><br>日文分析，解释为什么去掉字符串生成能让 Jev 快这么多，以及发布时的速度对比实际上比的是什么。</td>
</tr>
<tr>
<td width="260" valign="top"></td>
<td valign="top"><b><a href="https://juejin.cn/post/7686808742222856211">JEV 为什么重要：实用模式</a></b><br><sub>前端小小栈 · 文章 · 2026-09-19</sub><br>中文概述，用伪代码介绍决策模型的几种模式：agent 路由、RAG 相关性打分、代码审查风险关卡，以及 SQL 式的逐行判断。</td>
</tr>
<tr>
<td width="260" valign="top"></td>
<td valign="top"><b><a href="https://www.reddit.com/r/LLMDevs/comments/1wlfmaa/why_jev_might_finally_kill_the_text_prompt/">Jev 可能会终结文本提示词</a></b><br><sub>dpopa · Reddit · 2026-09-20</sub><br>随笔，认为聊天框之所以存在，是因为自回归模型对 UI 事件循环来说太慢了，而 50-100 毫秒 的决策让直接操作式的 AI 界面成为可能。</td>
</tr>
</table>

还缺什么？[提交一个资源](https://github.com/Li-Evan/awesome-jev/issues/new/choose)。
