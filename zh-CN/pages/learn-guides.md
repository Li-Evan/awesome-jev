# 📚 学习资料: 教程

[English](https://github.com/Li-Evan/awesome-jev/blob/main/pages/learn-guides.md) · **简体中文**

官方文档和 cookbook，以及社区里最好的教程、分析、评测和演讲。共 76 条，按社区热度排序。

[← 返回 Awesome Jev](https://github.com/Li-Evan/awesome-jev/blob/main/README.zh-CN.md#教程)

[官方文档](https://github.com/Li-Evan/awesome-jev/blob/main/zh-CN/pages/learn-official-docs.md) (15) · [官方 SDK 与工具](https://github.com/Li-Evan/awesome-jev/blob/main/zh-CN/pages/learn-official-tools.md) (3) · [官方公告](https://github.com/Li-Evan/awesome-jev/blob/main/zh-CN/pages/learn-announcements.md) (2) · [设计模式](https://github.com/Li-Evan/awesome-jev/blob/main/zh-CN/pages/learn-patterns.md) (4) · [官方 Cookbook](https://github.com/Li-Evan/awesome-jev/blob/main/zh-CN/pages/learn-cookbooks.md) (18) · [示例与 Skill](https://github.com/Li-Evan/awesome-jev/blob/main/zh-CN/pages/learn-examples.md) (74) · **教程** · [技巧与分析](https://github.com/Li-Evan/awesome-jev/blob/main/zh-CN/pages/learn-techniques.md) (103) · [评测与案例](https://github.com/Li-Evan/awesome-jev/blob/main/zh-CN/pages/learn-benchmarks.md) (173) · [视频与演讲](https://github.com/Li-Evan/awesome-jev/blob/main/zh-CN/pages/learn-videos.md) (178) · [社区讨论](https://github.com/Li-Evan/awesome-jev/blob/main/zh-CN/pages/learn-discussions.md) (20)

<table>
<tr>
<td width="260" valign="top"><a href="https://x.com/sydneyrunkle/status/2100754364545761643"><img src="https://pbs.twimg.com/media/HSdguxyboAAljJm.jpg" alt="用 Jev 搭建 harness" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/sydneyrunkle/status/2100754364545761643">用 Jev 搭建 harness</a></b><br><sub>sydneyrunkle · 文章 · ♥ 5.5k · 2026-09-18</sub><br>指南：如何把 Jev 加进 LangChain 的 agent harness，涵盖 Jev 的工作原理、它在 agent 循环中的位置，以及以中间件形式实现的模型路由和工具调用前风险检查。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/0xCodila/status/2100984487802708306"><img src="https://pbs.twimg.com/media/HSgY7VCXUAAWG9f.jpg" alt="Jev 工程路线图" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/0xCodila/status/2100984487802708306">Jev 工程路线图</a></b><br><sub>0xCodila · 文章 · ♥ 3.1k · 2026-09-18</sub><br>一篇 X 长文，给出 10 步路线图，把 Jev 搭建成决策层，告诉 agent 和 LLM 下一步该做什么。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/29meat_ai/status/2100844631693095267"><img src="https://pbs.twimg.com/media/HSeYgs4aAAALBOy.jpg" alt="用 Jev 能做的 30 件事" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/29meat_ai/status/2100844631693095267">用 Jev 能做的 30 件事</a></b><br><sub>29meat_ai · 文章 · ♥ 2.7k · 2026-09-18</sub><br>日语入门，讲 Jev 能做和不能做什么，逐一介绍 30 个真实原型和演示（航班搜索、浏览器 agent、游戏、交易机器人），并附上报告的速度和成本。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/0xMovez/status/2101007482919227841"><img src="https://pbs.twimg.com/media/HShGxV4XgAA2JRK.jpg" alt="10 步搞定 Jev 工程" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/0xMovez/status/2101007482919227841">10 步搞定 Jev 工程</a></b><br><sub>0xMovez · 文章 · ♥ 689 · 2026-09-18</sub><br>一篇 X 长文，给出 10 步搭建方案：把 agent 的是非判断、下一个 worker 的选择和相关性打分从 LLM 挪到 Jev，再加上模型路由器和高风险工具调用的把关。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/MakeAI_CEO/status/2101924475814212065"><img src="https://pbs.twimg.com/media/HSuJJdSbIAAGIIv.jpg" alt="Jev x Codex 实战指南" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/MakeAI_CEO/status/2101924475814212065">Jev x Codex 实战指南</a></b><br><sub>MakeAI_CEO · 文章 · ♥ 448 · 2026-09-21</sub><br>日文指南，涵盖在 Codex 中安装 TypeSafe skill、把生成与 Jev 判断分开、已公开的实验、工作中的应用，以及提升决策准确率的方法。</td>
</tr>
<tr>
<td width="260" valign="top"></td>
<td valign="top"><b><a href="https://x.com/iannuttall/status/2100982108873191861">TypeSafe skill 入门</a></b><br><sub>iannuttall · X · ♥ 2.6k · 2026-09-18</sub><br>两步上手：先安装官方的 typesafe-ai agent skill，再让编程 agent 用 /typesafe-ai 找出可以用 Jev 替换的又慢又贵的 LLM 调用。<br><sub>相关: <a href="https://github.com/typesafe-ai/skills">skill</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/_avichawla/status/2101563610644496464"><img src="https://pbs.twimg.com/media/HSnaCbRbgAA0RG9.png" alt="自己动手做一个 Jev（100% 本地）" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/_avichawla/status/2101563610644496464">自己动手做一个 Jev（100% 本地）</a></b><br><sub>_avichawla · 文章 · ♥ 2.6k · 2026-09-20</sub><br>教程：不重新训练，就把开源 LLM 变成本地决策引擎，借助 SGLang 对固定选项做下一个 token 打分，并与常规文本生成做基准对比。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/DataChaz/status/2101206777924858319"><img src="https://pbs.twimg.com/media/HSj8bdNa0AAPYPc.jpg?name=orig" alt="Jev 工程路线图精简版" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/DataChaz/status/2101206777924858319">Jev 工程路线图精简版</a></b><br><sub>DataChaz · X · ♥ 2.1k · 2026-09-19</sub><br>帖子串，浓缩了一份 10 步 Jev 搭建指南：把 agent 的分岔点变成 Choice、Score 和概率，批量处理决策（一次测试中 13 个问题快了 10 倍、便宜了 12.2 倍），并对整个循环做基准测试。<br><sub>相关: <a href="https://x.com/0xCodila/status/2100984487802708306">source</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/chddaniel/status/2100925069765534024"><img src="https://pbs.twimg.com/media/HSf8FmcXMAAKnZ2.jpg" alt="精通 Jev（完整指南）" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/chddaniel/status/2100925069765534024">精通 Jev（完整指南）</a></b><br><sub>chddaniel · 文章 · ♥ 1.1k · 2026-09-18</sub><br>长篇指南，涵盖 Jev 擅长什么、如何与现有 LLM 搭配使用、提问模式、用置信度门槛防止错误决策，以及五个赚钱的工作流。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/OpenRouter/status/2101061688338575739"><img src="https://pbs.twimg.com/amplify_video_thumb/2101061589038477312/img/Jrat3MGWY4vtlsjL.jpg" alt="决策模型实战" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/OpenRouter/status/2101061688338575739">决策模型实战</a></b><br><sub>OpenRouter · X · ♥ 1.7k · 2026-09-18</sub><br>OpenRouter 的帖子串，借软件开发中的实际例子解释什么是决策模型：Jev 回答是非题和选择题，并附上置信度。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/0xRicker/status/2101292455391809670"><img src="https://pbs.twimg.com/media/HSk1-arXgAAPiPp.jpg" alt="给你的 agent 装一个决策大脑" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/0xRicker/status/2101292455391809670">给你的 agent 装一个决策大脑</a></b><br><sub>0xRicker · 文章 · ♥ 306 · 2026-09-19</sub><br>一篇 X 长文，分 10 步讲如何把 agent 的是非判断、路由和相关性判断从昂贵的 LLM 挪到 Jev 的三种问题类型上。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/mvanhorn/status/2100784142850097482"><img src="https://pbs.twimg.com/media/HSdxN5LbUAAMq_w.png" alt="Jev 究竟是什么鬼？" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/mvanhorn/status/2100784142850097482">Jev 究竟是什么鬼？</a></b><br><sub>mvanhorn · 文章 · ♥ 1.3k · 2026-09-18</sub><br>用大白话讲解 Jev：它做的是选择题而不是写作文；随后列出人们已经在用它做的九样东西，并逐一对照原帖核实过。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/xmglab/status/2101932146416075073"><img src="https://pbs.twimg.com/media/HStmlB-aAAE0ixN.jpg" alt="在 Claude Code 和 Codex 中使用 Jev（中文）" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/xmglab/status/2101932146416075073">在 Claude Code 和 Codex 中使用 Jev（中文）</a></b><br><sub>xmglab · 文章 · ♥ 456 · 2026-09-21</sub><br>中文教程，涵盖 API key、向 System One 端点发出第一个 curl 请求、定价，以及在 Claude Code 和 Codex 中安装官方 TypeSafe skill。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/29meat_ai/status/2101431162749264219"><img src="https://pbs.twimg.com/media/HSmLh7pa0AAvGzI.jpg" alt="Codex x Jev 教科书" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/29meat_ai/status/2101431162749264219">Codex x Jev 教科书</a></b><br><sub>29meat_ai · 文章 · ♥ 239 · 2026-09-19</sub><br>日文指南：把决策从 Codex 中拆出来交给 Jev，并梳理公开的路由器和集成在模型选择、证据核查和兜底行为上的做法。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/omarsar0/status/2101774405521301681"><img src="https://pbs.twimg.com/media/HSr-innWsAEQPym.jpg" alt="Jev 入门指南" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/omarsar0/status/2101774405521301681">Jev 入门指南</a></b><br><sub>omarsar0 · 文章 · ♥ 889 · 2026-09-20</sub><br>简短的入门指南，把 Jev 解释为做聚焦判断的模型，以一张客服工单作为 state、配一张由类型化问题组成的决策表，并说明它在生产环境中的位置。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/kgsi/status/2100743044698112032"><img src="https://pbs.twimg.com/media/HSdWHhbaUAAGMVn.jpg" alt="写给非工程师和设计师的 Jev" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/kgsi/status/2100743044698112032">写给非工程师和设计师的 Jev</a></b><br><sub>kgsi · 文章 · ♥ 340 · 2026-09-18</sub><br>面向非工程师的日文入门，围绕一个演示展开：在 70-150 毫秒内把直播评论分成提问、感想、请求和其他四类。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/Mileson07/status/2101167448448004249"><img src="https://pbs.twimg.com/media/HSjXgp3bwAAxX95.jpg" alt="Jev 新手教程（中文）" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/Mileson07/status/2101167448448004249">Jev 新手教程（中文）</a></b><br><sub>Mileson07 · 文章 · ♥ 770 · 2026-09-19</sub><br>面向新手的中文分步教程，涵盖 state、问题与答案、Noul/Choice/Score 三种类型，以及如何在 playground 中上手。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/CopilotKit/CopilotKit/blob/main/showcase/shell-docs/src/content/docs/cookbook/jev-generative-ui.mdx"><img src="https://repository-images.githubusercontent.com/655515393/3299a492-753a-4726-ad71-ea5d268c6e79" alt="CopilotKit 的 Jev 生成式 UI 示例" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/CopilotKit/CopilotKit/blob/main/showcase/shell-docs/src/content/docs/cookbook/jev-generative-ui.mdx">CopilotKit 的 Jev 生成式 UI 示例</a></b><br><sub>CopilotKit · 文档 · ⭐ 37.5k 仓库 · 2023-06-19</sub><br>Cookbook 示例：一个 Next.js 工作区选择器，由 Jev 决定是先追问澄清还是直接展示选项，并给房间排序，再由 CopilotKit 和 AG-UI 渲染结果。<br><sub><b>Jev 用法:</b> Jev 在预先准备好的面板之间做选择并给候选项排序；只有两个面板都覆盖不了的请求才交给 OpenAI 模型处理。</sub><br><sub>相关: <a href="https://docs.copilotkit.ai">docs</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/yibie/status/2100541283081023936"><img src="https://pbs.twimg.com/media/HSafHbiWYAAIM5j.jpg" alt="三种原语与分级阈值" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/yibie/status/2100541283081023936">三种原语与分级阈值</a></b><br><sub>yibie · 文章 · ♥ 608 · 2026-09-17</sub><br>中文 Jev 使用指南：Noul、Choice 和 Score 原语及其返回结构，五种上手方式（playground、HTTP、SDK），以及如何设置分级置信度阈值。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/leaf_sanren/status/2101305166721098179"><img src="https://pbs.twimg.com/media/HSlVVQ8bcAAyk-G.jpg" alt="8 个可照抄的 Jev 用例（中文）" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/leaf_sanren/status/2101305166721098179">8 个可照抄的 Jev 用例（中文）</a></b><br><sub>leaf_sanren · 文章 · ♥ 259 · 2026-09-19</sub><br>中文学习笔记，讲解 Jev 是什么、30 分钟跑起来的四种方式、8 个可照抄的真实案例、反直觉的要点，以及什么时候不该用它。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/masahirochaen/status/2101312078627659898"><img src="https://pbs.twimg.com/media/HSlHRjMXgAAGdig.jpg" alt="工作中使用 Jev 的 20 种方式" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/masahirochaen/status/2101312078627659898">工作中使用 Jev 的 20 种方式</a></b><br><sub>masahirochaen · 文章 · ♥ 531 · 2026-09-19</sub><br>日语指南，介绍 Jev 能做什么、20 个已公开的演示和 API 用法（从浏览器控制到客服分流）及其在工作中的应用，以及如何通过 Vercel AI Gateway 免费试用。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/AIMevzulari/status/2101362530241188066"><img src="https://pbs.twimg.com/media/HSlqviuW4AAM7G7.jpg" alt="JEV 是什么？" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/AIMevzulari/status/2101362530241188066">JEV 是什么？</a></b><br><sub>AIMevzulari · 文章 · ♥ 164 · 2026-09-19</sub><br>土耳其语讲解，把 Jev 定位为决策引擎而非 LLM，介绍它在 agent 中的位置、对其宣传说法的保留意见，以及在 Claude Code 和 Codex 中的配置步骤。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://ruben.substack.com/p/jev"><img src="https://substackcdn.com/image/fetch/$s_!jina!,w_1200,h_675,c_fill,f_jpg,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F49573abc-65a6-4b90-87d6-04d5ec96eff3_2400x1260.png" alt="Jev 使用方法（Ruben Hassid）" width="240"></a></td>
<td valign="top"><b><a href="https://ruben.substack.com/p/jev">Jev 使用方法（Ruben Hassid）</a></b><br><sub>Ruben Hassid · 文章 · ♥ 360 · 2026-09-20</sub><br>面向非开发者的指南：在 Claude Code 或 Codex 中通过 TypeSafe skill 使用 Jev，附 LinkedIn 分类、Gmail 分拣和论文筛选的案例，每个都配有可直接复制的提示词。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/akshay_pachaar/status/2102087107410002345"><img src="https://pbs.twimg.com/media/HSsB_z2bMAATp-F.jpg" alt="用 Jev 搭建评判器" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/akshay_pachaar/status/2102087107410002345">用 Jev 搭建评判器</a></b><br><sub>akshay_pachaar · 文章 · ♥ 332 · 2026-09-21</sub><br>教程：在 agent 评测中用 Jev 替代 LLM 评判器，只问边界明确的问题，比如回答是否依据了政策、声称执行的操作是否真的发生了。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/startupideaspod/status/2101029801821941933"><img src="https://pbs.twimg.com/media/HShbadGaAAAujgB.jpg" alt="Jev 来了，以及怎么用" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/startupideaspod/status/2101029801821941933">Jev 来了，以及怎么用</a></b><br><sub>startupideaspod · 文章 · ♥ 61 · 2026-09-18</sub><br>Startup Ideas Podcast 与 OpenCode 的 Ryan Vogel 一起做的指南，讲 Jev 如何工作、在哪里会失灵以及相关创业点子，其中一个演示只花 18 美分就让 Jev 处理了 1,700 封真实邮件。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/jasonzhou1993/status/2101925228335317238"><img src="https://pbs.twimg.com/media/HSuA37PbMAEighq.jpg" alt="用 Jev 做 GTM 自动化" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/jasonzhou1993/status/2101925228335317238">用 Jev 做 GTM 自动化</a></b><br><sub>jasonzhou1993 · 文章 · ♥ 216 · 2026-09-21</sub><br>分步指南：在市场推广（go-to-market）自动化中使用 Jev，解释针对可接受答案的校准概率，以及如何在大批量场景下组织线索和客户决策。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/yupi996/status/2101953504374042658"><img src="https://pbs.twimg.com/media/HSuiiggbAAAZdqO.jpg" alt="Jev 上手实测与教程（中文）" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/yupi996/status/2101953504374042658">Jev 上手实测与教程（中文）</a></b><br><sub>yupi996 · 文章 · ♥ 240 · 2026-09-21</sub><br>中文入门指南兼实测，讲解 System One 模型、Noul/Choice/Score 三种原语（附请求示例），以及在 Jev 开放后如何上手试用。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/ericosiu/status/2101737133165924680"><img src="https://pbs.twimg.com/media/HSq8kZTbgAAZ-Q1.jpg" alt="用 Jev 做营销" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/ericosiu/status/2101737133165924680">用 Jev 做营销</a></b><br><sub>ericosiu · 文章 · ♥ 98 · 2026-09-20</sub><br>一篇 X 长文，走查五个营销工作流，用 Jev 挑出值得投入的内容创意、SEO 选题、切片和线索，附可改写的提示词，并说明早期测试的局限。<br><sub><b>Jev 用法:</b> 对候选创意、选题和线索做分类，现有 agent 只为 Jev 批准的那些起草内容。</sub></td>
</tr>
<tr>
<td width="260" valign="top"></td>
<td valign="top"><b><a href="https://www.reddit.com/r/AIAgentsInAction/comments/1wkoyfc/simplest_guide_to_jev/">最简 Jev 指南</a></b><br><sub>lucid-deaming-in · Reddit · ▲ 21 · 2026-09-19</sub><br>简短入门，讲如何把 state 和问题发给 Jev 并读回 Choice、Score 和 Noul 答案，附一个请求体示例。</td>
</tr>
<tr>
<td width="260" valign="top"></td>
<td valign="top"><b><a href="https://www.reddit.com/r/typesafe_ai/comments/1wiguah/10_jev_commandments/">Jev 10 条戒律</a></b><br><sub>Just_Lingonberry_352 · Reddit · ▲ 8 · 2026-09-17</sub><br>设计 Jev 调用的十条经验法则：问极小的问题，独立的问题并行跑，只有存在依赖时才串联，把 Jev 当门卫用，把概率当作信号。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/davila7/jev-explained"><img src="https://raw.githubusercontent.com/davila7/jev-explained/main/docs/jev-primitives.png" alt="Jev Explained" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/davila7/jev-explained">Jev Explained</a></b><br><sub>davila7 · GitHub · ⭐ 23 · 2026-09-19</sub><br>交互式 playground，用你自己的 TypeSafe 或 Vercel AI Gateway key 逐步运行 Noul、Choice 和 Score 问题，讲解 Jev 如何做出类型化的概率决策。<br><sub>相关: <a href="https://x.com/dani_avila7/status/2101484241762603363">demo</a> · <a href="https://jev-explained-repo.vercel.app/">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://vercel.com/i/what-is-jev"><img src="https://images.ctfassets.net/e5382hct74si/7x5CA1G7tDV7JSxt9iycsY/841a3891f316cf03bef4f76272a7276e/image.png" alt="Jev 是什么？" width="240"></a></td>
<td valign="top"><b><a href="https://vercel.com/i/what-is-jev">Jev 是什么？</a></b><br><sub>Vercel (Ben Sabic) · 文章 · ▲ 3 · 2026-09-19</sub><br>Vercel 的讲解文章，说明 Jev 中 state 和类型化问题的含义、Choice、Score 和 Noul 答案如何返回，以及它的类型安全止步于何处。<br><sub>相关: <a href="https://news.ycombinator.com/item?id=49787870">discussion</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/MisbahSy/status/2102199407630500290"><img src="https://pbs.twimg.com/media/HSyBz3lagAAtzmj.jpg" alt="写给开发者的 Jev" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/MisbahSy/status/2102199407630500290">写给开发者的 Jev</a></b><br><sub>MisbahSy · 文章 · ♥ 8 · 2026-09-22</sub><br>图文并茂的开发者指南，讲如何用 Jev 构建应用：state、类型化问题字典、SDK 配置、LiteLLM 路由和常见模式，写法上也方便 agent 阅读。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://vercel.com/kb/guide/typesafe-jev-and-ai-sdk"><img src="https://vercel.com/api/docs-og?title=How%20to%20classify%2C%20route%2C%20and%20score%20with%20Jev%20and%20AI%20SDK&amp;format=kb&amp;sig=447fbc245d38ca20ca0f1ed58f4f6a66df9cd38071d9e75a9526310f6a4c072d" alt="用 Jev 和 AI SDK 做分类、路由和打分" width="240"></a></td>
<td valign="top"><b><a href="https://vercel.com/kb/guide/typesafe-jev-and-ai-sdk">用 Jev 和 AI SDK 做分类、路由和打分</a></b><br><sub>Vercel · 文章 · ▲ 2 · 2026-09-19</sub><br>在一次 AI SDK 调用里混合选择、打分和是非判断，只在超过置信度门槛时才执行分发，并用 mock 模型对阈值做单元测试。<br><sub>相关: <a href="https://news.ycombinator.com/item?id=49765748">discussion</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Bald0Wang/jev-docs-zh"><img src="https://opengraph.githubassets.com/1/Bald0Wang/jev-docs-zh" alt="jev-docs-zh" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Bald0Wang/jev-docs-zh">jev-docs-zh</a></b><br><sub>Bald0Wang · GitHub · ⭐ 4 · 2026-09-20</sub><br>官方 Jev 文档（docs.typesafe.ai）的非官方中文译本，构建为静态站点。<br><sub>相关: <a href="https://bald0wang.github.io/jev-docs-zh/">site</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/lgyv5/status/2101860029838303522"><img src="https://pbs.twimg.com/media/HStFeVXbAAAQgIf.jpg" alt="Jev 在 agent 中的五个实用场景" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/lgyv5/status/2101860029838303522">Jev 在 agent 中的五个实用场景</a></b><br><sub>lgyv5 · 文章 · ♥ 3 · 2026-09-21</sub><br>中文指南，介绍 Jev 在 agent 流水线中适用的五个位置：内容清洗、固定参数选择、意图路由、RAG 重排和工具调用安全把关，并介绍开源项目 JevShield。<br><sub>相关: <a href="https://github.com/lgy1027/jevshield">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"></td>
<td valign="top"><b><a href="https://www.jrzs.dev/blog/what-the-heck-is-jev/">Jev 到底是个啥？</a></b><br><sub>James O&#x27;Reilly · 文章 · ▲ 1 · 2026-09-18</sub><br>简短的新手讲解，把 Jev 介绍为亚秒级决策模型，讲 Choice、Noul 和 Score 三种问题类型，并附一个示例请求和响应。<br><sub>相关: <a href="https://news.ycombinator.com/item?id=49753818">discussion</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/sherajdev/jev-research"><img src="https://opengraph.githubassets.com/1/sherajdev/jev-research" alt="Jev + Herdr" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/sherajdev/jev-research">Jev + Herdr</a></b><br><sub>sherajdev · GitHub · ⭐ 1 · 2026-09-18</sub><br>指南：用 Jev 和 Herdr 编排 Claude、Codex、Hermes 等编程 agent，附一个小型路由原型，以及对一个 Jev 浏览器 worker 的评述。<br><sub><b>Jev 用法:</b> Jev 根据任务和仓库的 state 为任务选择执行者，并给风险和派发就绪度打分。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/alarcon7a/youtube-tutorial-sources/blob/main/Notebooks/Typesafe/jev_tutorial.ipynb"><img src="https://opengraph.githubassets.com/1/alarcon7a/youtube-tutorial-sources" alt="从零开始学 Jev" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/alarcon7a/youtube-tutorial-sources/blob/main/Notebooks/Typesafe/jev_tutorial.ipynb">从零开始学 Jev</a></b><br><sub>alarcon7a · GitHub · ⭐ 35 仓库 · 2025-02-17</sub><br>配合一个 YouTube 视频的西班牙语分步 Jupyter 教程：构建一个客服工单 state，用 Python SDK 提出 Choice、Noul 和 Score 问题，再用明确写出的 Python 阈值组合这些答案。<br><sub>相关: <a href="https://github.com/alarcon7a/youtube-tutorial-sources">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/earlyaidopters/gumroad-resources/tree/main/resources/jev-starter-kit-explainer-live-playground"><img src="https://i.ytimg.com/vi/zZNm4zP_lEE/maxresdefault.jpg" alt="Jev Starter Kit" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/earlyaidopters/gumroad-resources/tree/main/resources/jev-starter-kit-explainer-live-playground">Jev Starter Kit</a></b><br><sub>earlyaidopters · GitHub · ⭐ 34 仓库 · 2026-08-10</sub><br>Early AI-dopters 的免费入门套件，配合一个 YouTube 讲解视频，包含交互式 Jev 讲解、Ask Jev playground，以及一份编程助手指南，其中有一个酒店细则 API 示例。<br><sub>相关: <a href="https://github.com/earlyaidopters/gumroad-resources">repo</a> · <a href="https://www.youtube.com/watch?v=zZNm4zP_lEE">video</a> · <a href="https://markkashef.gumroad.com/l/jev-starter-kit">gumroad</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/howdeploy/deploychan_mcp/blob/main/content/tools/jev.md"><img src="https://opengraph.githubassets.com/1/howdeploy/deploychan_mcp" alt="deploychan 的 Jev 指南" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/howdeploy/deploychan_mcp/blob/main/content/tools/jev.md">deploychan 的 Jev 指南</a></b><br><sub>howdeploy · GitHub · ⭐ 14 仓库 · 2026-06-24</sub><br>面向编程 agent 的公开 MCP 服务器，附带在现有模型旁接入 Jev 的指南：HTTP 接口约定、Choice/Score/Noul、密钥处理、模型版本固定和失败处理。<br><sub>相关: <a href="https://github.com/howdeploy/deploychan_mcp">repo</a> · <a href="https://mcp.deploychan.webcam/index.html">app</a> · <a href="https://github.com/howdeploy/deploychan_mcp/blob/main/content/routes/jev-integration.md">route</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/howdeploy/LocalForgeLLM/blob/main/docs/interfaces/jev.md"><img src="https://raw.githubusercontent.com/howdeploy/LocalForgeLLM/main/docs/assets/how-it-works.svg" alt="LocalForgeLLM 的 Jev 指南" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/howdeploy/LocalForgeLLM/blob/main/docs/interfaces/jev.md">LocalForgeLLM 的 Jev 指南</a></b><br><sub>howdeploy · GitHub · ⭐ 8 仓库 · 2026-09-10</sub><br>一个本地 AI 技术栈框架中的指南，讲如何把托管的 Jev 与本地 LLM 搭配：Jev 负责在观察到的 browser-use 动作中做选择、做路由并检查结果，本地模型负责写文字和代码。<br><sub>相关: <a href="https://github.com/howdeploy/LocalForgeLLM">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/niket-sharma/AI-Agents-from-scratch/tree/main/tutorials/17-system-one-decisions"><img src="https://opengraph.githubassets.com/1/niket-sharma/AI-Agents-from-scratch" alt="System One 决策教程" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/niket-sharma/AI-Agents-from-scratch/tree/main/tutorials/17-system-one-decisions">System One 决策教程</a></b><br><sub>niket-sharma · GitHub · ⭐ 8 仓库 · 2025-10-15</sub><br>一门 AI agent 实战课程中的一章，把“产出”和“决策”分开，附可运行的脚本：第一个 Jev 决策、用 Jev 当评判器、评判器校准、模型路由、agent 循环把关，以及成本/延迟基准测试。<br><sub>相关: <a href="https://github.com/niket-sharma/AI-Agents-from-scratch">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/limboinf/know-as-ui/blob/main/jev-typesafe/a.html"><img src="https://opengraph.githubassets.com/1/limboinf/know-as-ui" alt="Jev 交互式手册" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/limboinf/know-as-ui/blob/main/jev-typesafe/a.html">Jev 交互式手册</a></b><br><sub>limboinf · GitHub · ⭐ 7 仓库 · 2026-08-24</sub><br>中文交互式 HTML 手册，配有可动手操作的小组件：概率翻译器、请求构建器、模糊工单路由、Score 等级设计器、Noul 天平、校准对比和风险阈值路由。<br><sub>相关: <a href="https://github.com/limboinf/know-as-ui">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"></td>
<td valign="top"><b><a href="https://uditgoenka.medium.com/how-to-use-typesafe-ai-jev-e9f1306300be">Jev 的 30 种用法</a></b><br><sub>Udit Goenka · 文章 · 2026-09-18</sub><br>面向开发者和非程序员的 30 个具体用例合集，全部套用“一个输入、一个问题、一个答案、一个动作”的结构：分流、路由、审核、打分和 agent 控制。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://flaviocopes.com/jev/"><img src="https://flaviocopes.com/images/jev/og.jpg" alt="深入解析 Jev" width="240"></a></td>
<td valign="top"><b><a href="https://flaviocopes.com/jev/">深入解析 Jev</a></b><br><sub>Flavio Copes · 文章 · 2026-09-17</sub><br>详尽讲解请求和响应结构、如何挑选原语、错误码、版本锁定和各项限制。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://ziplyne.agency/blog/ai-that-doesnt-talk-typesafe-jev-guide"><img src="https://pub-aee74429e0604b2da81fc4f8bd15a430.r2.dev/ziplyne-agency/ai-that-doesnt-talk-typesafe-jev-guide-featured-9fe7e111710940d1.webp" alt="不说话的 AI" width="240"></a></td>
<td valign="top"><b><a href="https://ziplyne.agency/blog/ai-that-doesnt-talk-typesafe-jev-guide">不说话的 AI</a></b><br><sub>Isaac Horowitz (ZipLyne) · 文章 · 2026-09-16</sub><br>用大白话讲清 Jev 是什么、适合用在哪、有哪些局限，给出从 playground、Python 和 JS SDK、原始 HTTP 到 agent skill 的入门路径，并建议先影子运行、再决定是否信任它。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://www.langchain.com/blog/building-a-harness-with-jev"><img src="https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/6aac8ce2e3f50ce7069ae68f_jev-harness-a-title-hero-1600x900.png" alt="用 Jev 搭建 harness" width="240"></a></td>
<td valign="top"><b><a href="https://www.langchain.com/blog/building-a-harness-with-jev">用 Jev 搭建 harness</a></b><br><sub>LangChain · 文章 · 2026-09-18</sub><br>介绍 LangChain 的 Jev 分类器、一个按请求路由模型的中间件，以及一个在高风险工具调用执行前将其拦下的中间件。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://note.com/tolove/n/nee8a1ab825a0"><img src="https://assets.st-note.com/production/uploads/images/314891199/rectangle_large_type_2_42dd79d28b9b5b85fba6ccaf350cdd87.png?fit=bounds&amp;quality=85&amp;width=1280" alt="通过 MCP 把 Jev 接入 Claude Code" width="240"></a></td>
<td valign="top"><b><a href="https://note.com/tolove/n/nee8a1ab825a0">通过 MCP 把 Jev 接入 Claude Code</a></b><br><sub>東京PCレスキュー隊長 (tolove) · 文章 · 2026-09-18</sub><br>面向新手的日文实操记录：经由 Vercel AI Gateway 调用 Jev，用 AI SDK 的 evaluate 脚本测试，再封装成 MCP 服务器让 Claude Code 分拣工单，也记下了途中踩到的坑。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://openrouter.ai/docs/cookbook/building-agents/gate-tool-calls-with-jev"><img src="https://openrouter.ai/dynamic-og?title=Gate%20Agent%20Tool%20Calls%20with%20Jev&amp;description=Approve%2C%20refuse%2C%20or%20escalate%20each%20call%20on%20its%20evidence" alt="用 Jev 把关 agent 工具调用" width="240"></a></td>
<td valign="top"><b><a href="https://openrouter.ai/docs/cookbook/building-agents/gate-tool-calls-with-jev">用 Jev 把关 agent 工具调用</a></b><br><sub>OpenRouter · 文档</sub><br>OpenRouter cookbook 示例：把 Agent SDK agent 的每次退款工具调用与工单对照检查，安全的退款直接执行，缺乏依据的予以拒绝，只有模棱两可的才交给人工。<br><sub><b>Jev 用法:</b> 确定性检查加上 Jev 的 Noul 概率，并设有固定的批准、拦截和人工复核阈值。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://dev.to/gabrielanhaia/he-says-he-co-invented-chatgpt-his-new-ai-jev-wont-write-a-word-e3c"><img src="https://media2.dev.to/dynamic/image/width=1200,height=627,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Farticles%2Ftnv0uoo7kcryz640wj5m.png" alt="他的新 AI Jev 一个字都不写" width="240"></a></td>
<td valign="top"><b><a href="https://dev.to/gabrielanhaia/he-says-he-co-invented-chatgpt-his-new-ai-jev-wont-write-a-word-e3c">他的新 AI Jev 一个字都不写</a></b><br><sub>Gabriel Anhaia · 文章 · 2026-09-17</sub><br>讲解如何从 TypeScript 调用 Jev，包括 Vercel AI SDK 的 evaluate 集成，以及“零幻觉”说法背后藏着的限制。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://note.com/daikidomon/n/nfe8ae031a68d"><img src="https://assets.st-note.com/production/uploads/images/315133147/rectangle_large_type_2_2d7c3714b8679255b4c0ecbc1f578f03.png?fit=bounds&amp;quality=85&amp;width=1280" alt="Jev 使用方法（daikidomon）" width="240"></a></td>
<td valign="top"><b><a href="https://note.com/daikidomon/n/nfe8ae031a68d">Jev 使用方法（daikidomon）</a></b><br><sub>土門大貴 (daikidomon) · 文章 · 2026-09-18</sub><br>日文分步指南，从获取 API key 到完成第一次判断、按置信度分支，再到常见设计模式，附 Python、HTTP 和 JavaScript 示例。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://dev.to/valyuai/how-to-use-jev-a-practical-guide-to-typesafes-system-one-model-g5e"><img src="https://media2.dev.to/dynamic/image/width=1200,height=627,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Farticles%2Fl0bgmfbwspy7a4geinx6.png" alt="Jev 实用指南" width="240"></a></td>
<td valign="top"><b><a href="https://dev.to/valyuai/how-to-use-jev-a-practical-guide-to-typesafes-system-one-model-g5e">Jev 实用指南</a></b><br><sub>Valyu (Prosper Otemuyiwa) · 文章 · 2026-09-17</sub><br>五种带代码的模式：推测式扇出、按操作设置置信度门槛、组合打分、级联，以及先检索后判断。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://outcomeschool.com/blog/jev-and-system-one-models-explained"><img src="https://outcomeschool.com/static/images/blog/jev-and-system-one-models-explained.png" alt="Jev 与 System One 模型详解" width="240"></a></td>
<td valign="top"><b><a href="https://outcomeschool.com/blog/jev-and-system-one-models-explained">Jev 与 System One 模型详解</a></b><br><sub>Amit Shekhar (Outcome School) · 文章 · 2026-09-17</sub><br>面向初学者的讲解：System One 与 System Two 思维有何区别，为什么用 LLM 做小决策又慢又贵，以及 Jev 的类型化决策如何接入软件。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://zhuanlan.zhihu.com/p/2084716199309469153"><img src="https://pic4.zhimg.com/v2-f8ffa056090fed3a4f193adaa3295d27_1440w.jpg" alt="Jev 入门教程" width="240"></a></td>
<td valign="top"><b><a href="https://zhuanlan.zhihu.com/p/2084716199309469153">Jev 入门教程</a></b><br><sub>超级峰 · 文章</sub><br>中文入门教程，讲解核心概念、获取访问权限、控制台 Playground，以及如何编写 Noul、Choice 和 Score 问题，并就阈值盲测和中文输入给出建议。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://medium.com/@visrow/jev-by-typesafe-a-model-you-were-waiting-for-19e8fa8cb5cb"><img src="https://cdn-images-1.medium.com/max/1024/1*zLTUDTLbOhyUxC_yHBLM5g.png" alt="TypeSafe 出品的 Jev：你一直在等的模型" width="240"></a></td>
<td valign="top"><b><a href="https://medium.com/@visrow/jev-by-typesafe-a-model-you-were-waiting-for-19e8fa8cb5cb">TypeSafe 出品的 Jev：你一直在等的模型</a></b><br><sub>Vishal Mysore · 文章 · 2026-09-20</sub><br>讲解 Jev 与 LLM 有何不同、“零幻觉”意味着什么又不意味着什么，以及三种问题类型如何对应到医疗、保险、旅行和物流场景。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://qiita.com/titosemi/items/f2ced996f4c9400450a2"><img src="https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-user-contents.imgix.net%2Fhttps%253A%252F%252Fcdn.qiita.com%252Fassets%252Fpublic%252Farticle-ogp-background-afbab5eb44e0b055cce1258705637a91.png%3Fixlib%3Drb-4.1.1%26w%3D1200%26blend64%3DaHR0cHM6Ly9xaWl0YS11c2VyLXByb2ZpbGUtaW1hZ2VzLmltZ2l4Lm5ldC9odHRwcyUzQSUyRiUyRnMzLWFwLW5vcnRoZWFzdC0xLmFtYXpvbmF3cy5jb20lMkZxaWl0YS1pbWFnZS1zdG9yZSUyRjAlMkY0MDc2MDgzJTJGNWYxODNlNzAxM2Q3ZDc3ZjQ2NjgwMjljNDBiOTZmYTE4ZjFhZDBkNSUyRnhfbGFyZ2UucG5nJTNGMTc3MDc4MzU3MT9peGxpYj1yYi00LjEuMSZhcj0xJTNBMSZmaXQ9Y3JvcCZtYXNrPWVsbGlwc2UmYmc9RkZGRkZGJmZtPXBuZzMyJnM9NzJjMDA0MWI3MTQ3NGZhZTgzMTRiNTJlODQ4MmI3OTk%26blend-x%3D120%26blend-y%3D467%26blend-w%3D82%26blend-h%3D82%26blend-mode%3Dnormal%26s%3D5e44a1c5bc25323bbcdeb160850fbf22?ixlib=rb-4.1.1&amp;w=1200&amp;fm=jpg&amp;mark64=aHR0cHM6Ly9xaWl0YS11c2VyLWNvbnRlbnRzLmltZ2l4Lm5ldC9-dGV4dD9peGxpYj1yYi00LjEuMSZ3PTk2MCZoPTMyNCZ0eHQ9SmV2JUU1JUFFJThDJUU1JTg1JUE4JUU1JTg1JUE1JUU5JTk2JTgwJUUzJTgyJUFDJUUzJTgyJUE0JUUzJTgzJTg5JnR4dC1hbGlnbj1sZWZ0JTJDdG9wJnR4dC1jb2xvcj0lMjMxRTIxMjEmdHh0LWZvbnQ9SGlyYWdpbm8lMjBTYW5zJTIwVzYmdHh0LXNpemU9NTYmdHh0LXBhZD0wJnM9MDQ3N2ZhYTI2YjZjYjZhMmExMWMzYTllOWM3NWM0MDk&amp;mark-x=120&amp;mark-y=112&amp;blend64=aHR0cHM6Ly9xaWl0YS11c2VyLWNvbnRlbnRzLmltZ2l4Lm5ldC9-dGV4dD9peGxpYj1yYi00LjEuMSZ3PTgzOCZoPTU4JnR4dD0lNDB0aXRvc2VtaSZ0eHQtY29sb3I9JTIzMUUyMTIxJnR4dC1mb250PUhpcmFnaW5vJTIwU2FucyUyMFc2JnR4dC1zaXplPTM2JnR4dC1wYWQ9MCZzPTE1OTAwYTM4MTViNjQ5YTg5MGM2MjJhYTkwZmRmNmIx&amp;blend-x=242&amp;blend-y=480&amp;blend-w=838&amp;blend-h=46&amp;blend-fit=crop&amp;blend-crop=left%2Cbottom&amp;blend-mode=normal&amp;s=97535b309afff09c29a3cb39c0f9a00e" alt="Jev 零基础完全指南" width="240"></a></td>
<td valign="top"><b><a href="https://qiita.com/titosemi/items/f2ced996f4c9400450a2">Jev 零基础完全指南</a></b><br><sub>titosemi · 文章 · 2026-09-20</sub><br>面向 Python 开发者的日文长篇 Jev 入门，涵盖 state、类型化问题，以及如何把类型化决策接入软件。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://qiita.com/softbase/items/398f3d14a86b9acb55ae"><img src="https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-user-contents.imgix.net%2Fhttps%253A%252F%252Fcdn.qiita.com%252Fassets%252Fpublic%252Farticle-ogp-background-afbab5eb44e0b055cce1258705637a91.png%3Fixlib%3Drb-4.1.1%26w%3D1200%26blend64%3DaHR0cHM6Ly9xaWl0YS11c2VyLXByb2ZpbGUtaW1hZ2VzLmltZ2l4Lm5ldC9odHRwcyUzQSUyRiUyRnMzLWFwLW5vcnRoZWFzdC0xLmFtYXpvbmF3cy5jb20lMkZxaWl0YS1pbWFnZS1zdG9yZSUyRjAlMkYxMjU3NDYlMkYxM2Q3NGUwNzkzZWNiZDU1NjYwNGIzZTBmMDM1Y2RhY2VhN2MyOWRiJTJGbGFyZ2UucG5nJTNGMTc0NjE5MjIyNj9peGxpYj1yYi00LjEuMSZhcj0xJTNBMSZmaXQ9Y3JvcCZtYXNrPWVsbGlwc2UmYmc9RkZGRkZGJmZtPXBuZzMyJnM9NzU4YWE1MjRiMDNlZmU2ZWZhN2VkM2ZlMmIzN2I0MTc%26blend-x%3D120%26blend-y%3D467%26blend-w%3D82%26blend-h%3D82%26blend-mode%3Dnormal%26s%3De75f545fdd39d0207ceed9496afa02b2?ixlib=rb-4.1.1&amp;w=1200&amp;fm=jpg&amp;mark64=aHR0cHM6Ly9xaWl0YS11c2VyLWNvbnRlbnRzLmltZ2l4Lm5ldC9-dGV4dD9peGxpYj1yYi00LjEuMSZ3PTk2MCZoPTMyNCZ0eHQ9QUklMjBKZXYlMjAlRTMlODElQTglRTMlODElQUYlRUYlQkMlOUYlRTMlODAlOEMlRTYlOTYlODclRTclQUIlQTAlRTMlODIlOTIlRTYlOUIlQjglRTMlODElOEZBSSVFMyU4MCU4RCVFMyU4MSVBNyVFMyU4MSVBRiVFMyU4MSVBQSVFMyU4MSU4RiVFMyU4MCU4QyVFMyU4MSU5OSVFMyU4MSVCMCVFMyU4MiU4NCVFMyU4MSU4RiVFNyVBRCU5NCVFMyU4MSU4OCVFMyU4MiU5MiVFOSU4MSVCOCVFMyU4MSVCNkFJJUUzJTgwJThEJUUzJTgyJTkyJUU1JUIwJThGJUU1JUFEJUE2JUU3JTk0JTlGJUUzJTgxJUFCJUUzJTgyJTgyJUUzJTgyJThGJUUzJTgxJThCJUUzJTgyJThCJUUzJTgyJTg4JUUzJTgxJTg2JUUzJTgxJUFCJUU4JUFBJUFDJUU2JTk4JThFJUUzJTgxJTk5JUUzJTgyJThCJnR4dC1hbGlnbj1sZWZ0JTJDdG9wJnR4dC1jb2xvcj0lMjMxRTIxMjEmdHh0LWZvbnQ9SGlyYWdpbm8lMjBTYW5zJTIwVzYmdHh0LXNpemU9NTYmdHh0LXBhZD0wJnM9ZWE2Nzg3MGU4MjMyNzEwN2M5NjA0ZTc3NTdiYjc0Njg&amp;mark-x=120&amp;mark-y=112&amp;blend64=aHR0cHM6Ly9xaWl0YS11c2VyLWNvbnRlbnRzLmltZ2l4Lm5ldC9-dGV4dD9peGxpYj1yYi00LjEuMSZ3PTgzOCZoPTU4JnR4dD0lNDBzb2Z0YmFzZSZ0eHQtY29sb3I9JTIzMUUyMTIxJnR4dC1mb250PUhpcmFnaW5vJTIwU2FucyUyMFc2JnR4dC1zaXplPTM2JnR4dC1wYWQ9MCZzPTQ3MGViOGFmZjdmZDY0OGJmYjNkNmFkZDJlNTc5ZTFh&amp;blend-x=242&amp;blend-y=480&amp;blend-w=838&amp;blend-h=46&amp;blend-fit=crop&amp;blend-crop=left%2Cbottom&amp;blend-mode=normal&amp;s=407629a9317bf8706d76142a78c67d3d" alt="给孩子讲 Jev" width="240"></a></td>
<td valign="top"><b><a href="https://qiita.com/softbase/items/398f3d14a86b9acb55ae">给孩子讲 Jev</a></b><br><sub>softbase · 文章 · 2026-09-18</sub><br>日文讲解，从小学生能听懂的程度讲起，最后落到工程建议：如何设计问题、如何安全使用以及常见陷阱。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://zenn.dev/nix/articles/85cbdf3b1c5c83"><img src="https://res.cloudinary.com/zenn/image/upload/s--rCY7hwCF--/c_fit%2Cg_north_west%2Cl_text:notosansjp-medium.otf_55:%25E3%2580%258CJev%2520%25E3%2581%25A3%25E3%2581%25A6%25E4%25BD%2595%25EF%25BC%259F%25E6%2584%258F%25E5%2591%25B3%25E5%2588%2586%25E3%2581%258B%25E3%2582%2593%25E3%2581%25AA%25E3%2581%2584%25EF%25BC%2581%25E3%2580%258D%25E3%2581%25A8%25E3%2581%2584%25E3%2581%2586%25E6%2596%25B9%25E5%2590%2591%25E3%2581%2591%25E3%2581%25AB%25E3%2580%2581%25E3%2581%2596%25E3%2581%25A3%25E3%2581%258F%25E3%2582%258A%25E8%25A7%25A3%25E8%25AA%25AC%25E3%2581%2597%25E3%2581%25A6%25E3%2581%25BF%25E3%2581%259F%25E3%2582%2588%25EF%25BC%2581%2Cw_1010%2Cx_90%2Cy_100/g_south_west%2Cl_text:notosansjp-medium.otf_37:___nix___%2Cx_203%2Cy_121/g_south_west%2Ch_90%2Cl_fetch:aHR0cHM6Ly9zdGF0aWMuemVubi5zdHVkaW8vdXNlci11cGxvYWQvYXZhdGFyLzllYWYxODlkNGEuanBlZw==%2Cr_max%2Cw_90%2Cx_87%2Cy_95/v1627283836/default/og-base-w1200-v2.png?_a=BACMTiAE" alt="Jev 通俗讲解" width="240"></a></td>
<td valign="top"><b><a href="https://zenn.dev/nix/articles/85cbdf3b1c5c83">Jev 通俗讲解</a></b><br><sub>___nix___ · 文章 · 2026-09-18</sub><br>日文入门讲解，把聊天模型比作写论述题的学生，把 Jev 比作填选择题答题卡的学生，再逐步说明这对代码意味着什么。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://qiita.com/Ninagawa123/items/8ec3f5fe18c20fab1b2a"><img src="https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-user-contents.imgix.net%2Fhttps%253A%252F%252Fcdn.qiita.com%252Fassets%252Fpublic%252Farticle-ogp-background-afbab5eb44e0b055cce1258705637a91.png%3Fixlib%3Drb-4.1.1%26w%3D1200%26blend64%3DaHR0cHM6Ly9xaWl0YS11c2VyLXByb2ZpbGUtaW1hZ2VzLmltZ2l4Lm5ldC9odHRwcyUzQSUyRiUyRnMzLWFwLW5vcnRoZWFzdC0xLmFtYXpvbmF3cy5jb20lMkZxaWl0YS1pbWFnZS1zdG9yZSUyRjAlMkY1NjUwNDMlMkZmYjZjMDA1MzAwZDQ0ZmQ1MmE2Njk0MmJkYzMyOTVlYThlOTAzMTZlJTJGeF9sYXJnZS5wbmclM0YxNTc4NjY2OTc5P2l4bGliPXJiLTQuMS4xJmFyPTElM0ExJmZpdD1jcm9wJm1hc2s9ZWxsaXBzZSZiZz1GRkZGRkYmZm09cG5nMzImcz1lNmQzNmE1NWU5MGQ5YWNlOTg5OTU5Y2MyN2I0ZmQyMg%26blend-x%3D120%26blend-y%3D467%26blend-w%3D82%26blend-h%3D82%26blend-mode%3Dnormal%26s%3D608a3437dc4daed34cd74d8a0378d007?ixlib=rb-4.1.1&amp;w=1200&amp;fm=jpg&amp;mark64=aHR0cHM6Ly9xaWl0YS11c2VyLWNvbnRlbnRzLmltZ2l4Lm5ldC9-dGV4dD9peGxpYj1yYi00LjEuMSZ3PTk2MCZoPTMyNCZ0eHQ9NSVFNSU4OCU4NiVFMyU4MSVBN0pldiVFNSU4NSVBNSVFOSU5NiU4MCVFRiVCQyU4OCVFMyU4MSU5OSVFMyU4MSU5MCVFNCVCRCVCRiVFMyU4MSU4NiVFRiVCQyU4OSZ0eHQtYWxpZ249bGVmdCUyQ3RvcCZ0eHQtY29sb3I9JTIzMUUyMTIxJnR4dC1mb250PUhpcmFnaW5vJTIwU2FucyUyMFc2JnR4dC1zaXplPTU2JnR4dC1wYWQ9MCZzPTkyNzAyMzEyMjdlMjRjNzczYWYwOTk2MDY3Y2QzOTQ1&amp;mark-x=120&amp;mark-y=112&amp;blend64=aHR0cHM6Ly9xaWl0YS11c2VyLWNvbnRlbnRzLmltZ2l4Lm5ldC9-dGV4dD9peGxpYj1yYi00LjEuMSZ3PTgzOCZoPTU4JnR4dD0lNDBOaW5hZ2F3YTEyMyZ0eHQtY29sb3I9JTIzMUUyMTIxJnR4dC1mb250PUhpcmFnaW5vJTIwU2FucyUyMFc2JnR4dC1zaXplPTM2JnR4dC1wYWQ9MCZzPTcyODYxMjY0OTAyNDJjOWI3NDI5OWZhMjVhNDE1ODQ1&amp;blend-x=242&amp;blend-y=480&amp;blend-w=838&amp;blend-h=46&amp;blend-fit=crop&amp;blend-crop=left%2Cbottom&amp;blend-mode=normal&amp;s=8de02104082ea5480069dcd1930a9f29" alt="5 分钟上手 Jev" width="240"></a></td>
<td valign="top"><b><a href="https://qiita.com/Ninagawa123/items/8ec3f5fe18c20fab1b2a">5 分钟上手 Jev</a></b><br><sub>Ninagawa123 · 文章 · 2026-09-19</sub><br>简明的日文快速上手，讲如何在 TypeSafe 控制台注册并完成第一次 Jev 调用。</td>
</tr>
<tr>
<td width="260" valign="top"></td>
<td valign="top"><b><a href="https://juejin.cn/post/7686925590315696138">Jev 第一课</a></b><br><sub>XiaoLei_Liu · 文章 · 2026-09-19</sub><br>中文入门，把 Jev 看作嵌入业务流程的决策函数，并解释它与 LLM 在结构上的三点不同：输出接口、采样和置信度。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://note.com/npaka/n/n5ac6abd04d67"><img src="https://assets.st-note.com/production/uploads/images/315228626/rectangle_large_type_2_e0df04b330fc2b3df14325243124aef8.jpeg?fit=bounds&amp;quality=85&amp;width=1280" alt="Jev 快速上手（npaka）" width="240"></a></td>
<td valign="top"><b><a href="https://note.com/npaka/n/n5ac6abd04d67">Jev 快速上手（npaka）</a></b><br><sub>npaka · 文章 · 2026-09-19</sub><br>日文快速上手，梳理 Jev 的“state、问题、类型化决策”结构和 Choice、Score、Noul 三种类型，并附代码演示最初的 API 调用。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://kelen.cc/posts/jev-system-one-model-guide"><img src="https://static.kelen.cc/images/949192d9-a049-439e-a697-ca78710e9ab0.webp" alt="Jev System One 模型指南" width="240"></a></td>
<td valign="top"><b><a href="https://kelen.cc/posts/jev-system-one-model-guide">Jev System One 模型指南</a></b><br><sub>kelen · 文章 · 2026-09-19</sub><br>中文 Jev 入门，涵盖 Choice、Score 和 Noul，一个基于 Python SDK、按置信度升级处理的工单分拣示例，以及早期社区演示汇总。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://openrouter.ai/docs/cookbook/evaluate-and-optimize/jev-verified-cascade"><img src="https://openrouter.ai/dynamic-og?title=Jev-Verified%20Cascade&amp;description=Draft%20cheaply%2C%20verify%2C%20and%20escalate%20on%20failure" alt="经 Jev 校验的级联" width="240"></a></td>
<td valign="top"><b><a href="https://openrouter.ai/docs/cookbook/evaluate-and-optimize/jev-verified-cascade">经 Jev 校验的级联</a></b><br><sub>OpenRouter · 文档</sub><br>OpenRouter cookbook 示例：先用便宜模型起草，由 Jev 对照依据约束检查草稿，只有检查不通过时才升级给更强的模型。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://zenn.dev/suwash/articles/jev-ai_20260918"><img src="https://res.cloudinary.com/zenn/image/upload/s--SNQqBjex--/c_fit%2Cg_north_west%2Cl_text:notosansjp-medium.otf_55:%25E3%2582%25B3%25E3%2583%25BC%25E3%2583%2589%25E3%2581%258C%25E6%25B6%2588%25E8%25B2%25BB%25E3%2581%25A7%25E3%2581%258D%25E3%2582%258B%25E5%259E%258B%25E4%25BB%2598%25E3%2581%258D%25E6%25B1%25BA%25E5%25AE%259A%25E3%2582%2592%25E8%25BF%2594%25E3%2581%2599%25E3%2583%259B%25E3%2582%25B9%25E3%2583%2588%25E5%259E%258B%25E3%2583%25A2%25E3%2583%2587%25E3%2583%25AB%2520Jev%2520%25E3%2581%25AE%25E6%25A7%258B%25E9%2580%25A0%25E3%2581%25A8%25E4%25BD%25BF%25E3%2581%2584%25E6%2596%25B9%2Cw_1010%2Cx_90%2Cy_100/g_south_west%2Cl_text:notosansjp-medium.otf_37:suwa-sh%2520%252F%2520%25E8%25AB%258F%25E8%25A8%25AA%25E7%259C%259F%25E4%25B8%2580%2Cx_203%2Cy_121/g_south_west%2Ch_90%2Cl_fetch:aHR0cHM6Ly9saDMuZ29vZ2xldXNlcmNvbnRlbnQuY29tL2EvQUVkRlRwNlQ0cjdIdGJrWG10aG42OE53dmlHWXBLcGI5VWQ5N3hnRS1aQnM9czk2LWM=%2Cr_max%2Cw_90%2Cx_87%2Cy_95/v1627283836/default/og-base-w1200-v2.png?_a=BACMTiAE" alt="Jev 的结构与用法" width="240"></a></td>
<td valign="top"><b><a href="https://zenn.dev/suwash/articles/jev-ai_20260918">Jev 的结构与用法</a></b><br><sub>Shinichi Suwa (suwa-sh) · 文章 · 2026-09-19</sub><br>基于官方文档和 SDK 源码整理的日文指南，涵盖 Jev 的数据模型、state 与问题类型、配置步骤以及运维技巧。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://nervegna.substack.com/p/jev-the-ai-that-cant-write-a-single"><img src="https://substackcdn.com/image/fetch/$s_!tM__!,w_1200,h_675,c_fill,f_jpg,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0896ae45-3fa8-4f32-b9c3-5d82dcc5506d_1942x809.png" alt="Jev：一个字都写不了的 AI" width="240"></a></td>
<td valign="top"><b><a href="https://nervegna.substack.com/p/jev-the-ai-that-cant-write-a-single">Jev：一个字都写不了的 AI</a></b><br><sub>Tommaso Nervegna · 文章 · 2026-09-21</sub><br>一期 newsletter 讲解：为什么一个只做决策的模型有用，随后一步步演示如何配置并试用 Jev。</td>
</tr>
<tr>
<td width="260" valign="top"></td>
<td valign="top"><b><a href="https://www.datacamp.com/blog/system-one-models-jev">Jev：TypeSafe 的 System One 模型详解</a></b><br><sub>Matt Crabtree (DataCamp) · 文章 · 2026-09-16</sub><br>讲解 System One 模型、Jev 的 Choice、Score 和 Noul 原语、定价以及厂商工作流评测，并附一个调用 API 的最小 Python 示例。</td>
</tr>
<tr>
<td width="260" valign="top"></td>
<td valign="top"><b><a href="https://zhuanlan.zhihu.com/p/2084624500726022179">Jev 是什么、怎么用</a></b><br><sub>kuhung · 文章</sub><br>中文长文，把 Jev 看作经过校准的判别式分类器，附 API 和 Vercel AI SDK 示例，讲解置信度校准的原理和局限，并指向社区的复现项目。<br><sub>相关: <a href="https://jev.kuhung.me/">original</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://blog.lepine.pro/en/lets-discover-jev/"><img src="https://blog.lepine.pro/images/cover-auto/cover-let-s-look-at-jev-the-ai-that-decides-without-ever-writing-a-sentence.webp" alt="一起来看看 Jev" width="240"></a></td>
<td valign="top"><b><a href="https://blog.lepine.pro/en/lets-discover-jev/">一起来看看 Jev</a></b><br><sub>Jean-François Lépine · 文章 · 2026-09-17</sub><br>逐一讲解 Choice、Noul 和 Score 原语、校准的置信度，以及如何在一次调用中批量问多个问题，最后给出一个完整的 Python 项目。</td>
</tr>
<tr>
<td width="260" valign="top"></td>
<td valign="top"><b><a href="https://docs.typesafe.ai/llms.txt">llms.txt</a></b><br><sub>TypeSafe AI · 文档</sub><br>官方索引，以纯 Markdown 列出全部文档页面，方便把 TypeSafe 文档喂给编程 agent。</td>
</tr>
<tr>
<td width="260" valign="top"></td>
<td valign="top"><b><a href="https://uditgoenka.medium.com/typesafe-ai-jev-model-guide-89b33b74dd64">TypeSafe Jev 完全指南</a></b><br><sub>Udit Goenka · 文章 · 2026-09-18</sub><br>长篇指南，讲解 Choice、Score 和 Noul、如何调用 API，以及替换靠 JSON 提示词做决策的 LLM 调用的模式，起点是作者在自家产品里数出的 41 处这类调用。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://note.com/masa_wunder/n/n61f008d2699a"><img src="https://assets.st-note.com/production/uploads/images/314556573/rectangle_large_type_2_fb4c2fc481f47c500482b884e20a939b.jpg?fit=bounds&amp;quality=85&amp;width=1280" alt="用灯光控制演示试用 Jev" width="240"></a></td>
<td valign="top"><b><a href="https://note.com/masa_wunder/n/n61f008d2699a">用灯光控制演示试用 Jev</a></b><br><sub>まさお (masa_wunder) · 文章 · 2026-09-17</sub><br>日文动手入门，先批判性地审视基准测试结果，再搭一个平面图演示，用自然语言指令调暗房间灯光，展示置信度阈值如何在直接执行和追问之间做取舍。<br><sub>相关: <a href="https://www.youtube.com/watch?v=NttqTDRbGUc">video</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://langfuse.com/blog/2026-09-18-using-typesafes-jev-for-evals"><img src="https://langfuse.com/images/blog/2026-09-18-using-typesafes-jev-for-evals/jev-question-types.png" alt="用 TypeSafe 的 Jev 做评测" width="240"></a></td>
<td valign="top"><b><a href="https://langfuse.com/blog/2026-09-18-using-typesafes-jev-for-evals">用 TypeSafe 的 Jev 做评测</a></b><br><sub>Langfuse · 文章 · 2026-09-18</sub><br>在一次请求里用一个 Noul、一个 Score 和一个 Choice 给 agent 运行打分，并把结果作为 Langfuse score 写回。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://mohammedshehu.com/jev-typesafe-ai/"><img src="https://mohammedshehu.com/wp-content/uploads/2026/09/Jev-1.jpeg" alt="Jev 是什么？" width="240"></a></td>
<td valign="top"><b><a href="https://mohammedshehu.com/jev-typesafe-ai/">Jev 是什么？</a></b><br><sub>Mo Shehu · 文章 · 2026-09-16</sub><br>简短实用的入门，介绍 Jev 的工作方式以及如何从 Python 调用，围绕一个客服工单分拣示例展开。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://whatisjev.com/"><img src="https://whatisjev.com/og.png" alt="Jev 是什么？" width="240"></a></td>
<td valign="top"><b><a href="https://whatisjev.com/">Jev 是什么？</a></b><br><sub>whatisjev.com · 文档 · 2026-09-21</sub><br>独立制作的多语言 Jev 指南，包含任务模板、无需 key 的 playground、第一个请求的演练，以及介绍定价、限制和它与 LLM 区别的页面。<br><sub>相关: <a href="https://whatisjev.com/zh/getting-started">zh</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://zenn.dev/caen/articles/a629b80e76e193"><img src="https://res.cloudinary.com/zenn/image/upload/s--gAXBDpkD--/c_fit%2Cg_north_west%2Cl_text:notosansjp-medium.otf_55:TypeSafe%2520AI%25E3%2580%258CJev%25E3%2580%258D%25E3%2581%25A3%25E3%2581%25A6%25E3%2581%25AA%25E3%2582%2593%25E3%2581%25A0%25EF%25BC%259F%2Cw_1010%2Cx_90%2Cy_100/g_south_west%2Cl_text:notosansjp-medium.otf_37:%25E5%25A4%25A7%25E6%25A3%25AE%25E7%25BF%2594%25E5%2590%25BE%2Cx_203%2Cy_121/g_south_west%2Ch_90%2Cl_fetch:aHR0cHM6Ly9zdGF0aWMuemVubi5zdHVkaW8vdXNlci11cGxvYWQvYXZhdGFyL2Q4MmYyNzQwYjEuanBlZw==%2Cr_max%2Cw_90%2Cx_87%2Cy_95/v1627283836/default/og-base-w1200-v2.png?_a=BACMTiAE" alt="TypeSafe AI 的 Jev 是什么？" width="240"></a></td>
<td valign="top"><b><a href="https://zenn.dev/caen/articles/a629b80e76e193">TypeSafe AI 的 Jev 是什么？</a></b><br><sub>Shogo Omori (caen) · 文章 · 2026-09-17</sub><br>日文概览，介绍 Jev 在 Choice、Score 和 Noul 上的输入输出规范并附示例响应，以及它给日常工程工作带来的变化。</td>
</tr>
</table>

还缺什么？[提交一个资源](https://github.com/Li-Evan/awesome-jev/issues/new/choose)。
