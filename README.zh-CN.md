# Awesome Jev [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> [Jev](https://typesafe.ai) 是 TypeSafe 的 System One 模型。它不生成文字，而是对文本回答带类型的问题，并给出校准过的概率，让代码可以直接根据它的判断分支、排序和路由。

[English](README.md) · **简体中文**

这里是最全的 Jev 用例合集：**3,425 个项目、演示、帖子和实测文章**，从 GitHub、X、Reddit、Hacker News、YouTube 和各类网站收集而来，按应用场景整理。每一条都链接到原始出处，并说明它具体做了什么。Jev 有三种原语：**Choice** 从选项中选一个，**Score** 在有序等级上打分，**Noul** 给出某个陈述为真的概率。

本列表由社区维护，与 TypeSafe 官方无关。官方网站是 `typesafe.ai` 和 `docs.typesafe.ai`，官方 GitHub 组织是 `typesafe-ai`。请警惕自称官方的仿冒域名。

## 目录

- [快速上手](#快速上手)
- [按场景浏览](#按场景浏览)
  - [💰 金融与交易](#-金融与交易)
  - [💻 编程与开发工具](#-编程与开发工具)
  - [🌐 浏览器与电脑操控](#-浏览器与电脑操控)
  - [🤖 Agent 与编排](#-agent-与编排)
  - [🎮 游戏与互动](#-游戏与互动)
  - [🦾 机器人与仿真](#-机器人与仿真)
  - [🔎 搜索与 RAG](#-搜索与-rag)
  - [🛡️ 安全与审核](#-安全与审核)
  - [📊 数据与评测](#-数据与评测)
  - [🎧 客服与销售](#-客服与销售)
  - [⚖️ 法律、医疗与科研](#-法律医疗与科研)
  - [🛍️ 电商与营销](#-电商与营销)
  - [✍️ 写作、媒体与创意](#-写作媒体与创意)
  - [🗣️ 语音与实时交互](#-语音与实时交互)
  - [🧰 个人效率](#-个人效率)
  - [🎓 教育](#-教育)
  - [🧪 其他实验](#-其他实验)
- [开源模型与兼容服务](#开源模型与兼容服务)
- [用 Jev 开发](#用-jev-开发)
  - [模型访问](#模型访问)
  - [框架适配](#框架适配)
  - [可观测性](#可观测性)
  - [社区 SDK](#社区-sdk)
- [学习资料](#学习资料)
  - [官方文档](#官方文档)
  - [官方 SDK 与工具](#官方-sdk-与工具)
  - [官方公告](#官方公告)
  - [设计模式](#设计模式)
  - [官方 Cookbook](#官方-cookbook)
  - [示例与 Skill](#示例与-skill)
  - [教程](#教程)
  - [技巧与分析](#技巧与分析)
  - [评测与案例](#评测与案例)
  - [视频与演讲](#视频与演讲)
  - [社区讨论](#社区讨论)

## 快速上手

- [Jev 速查表](https://github.com/Li-Evan/awesome-jev/blob/main/cheatsheet.zh-CN.md) - 一页纸的实战指南，涵盖原语、问题设计、置信度处理、限制，以及经过测试的 SDK 代码片段。
- [快速开始](https://docs.typesafe.ai/introduction/quickstart) - 通过 Playground、cURL、Python SDK 或编程 agent 发出第一个请求。
- [Playground](https://console.typesafe.ai/playground) - 写代码之前，先在浏览器里试试一段 state 和一组问题（需要登录）。
- [如何用 TypeSafe 构建](https://docs.typesafe.ai/concepts/how-to-build-with-system-one) - 核心设计指南：把控制流留在代码里，把判断拆成原子化的问题。
- [Agent skill](https://docs.typesafe.ai/agent-skill) - 教 Claude Code、Codex 等编程 agent 根据实时文档设计 TypeSafe 工作流。

## 按场景浏览

精选按社区热度排序（star、点赞、得分和播放量）。点开场景查看完整画廊。

<table>
<tr><td><a href="https://github.com/Li-Evan/awesome-jev/blob/main/zh-CN/scenarios/finance.md">💰 金融与交易</a> <sub>89</sub></td><td><a href="https://github.com/Li-Evan/awesome-jev/blob/main/zh-CN/scenarios/coding.md">💻 编程与开发工具</a> <sub>515</sub></td><td><a href="https://github.com/Li-Evan/awesome-jev/blob/main/zh-CN/scenarios/browser.md">🌐 浏览器与电脑操控</a> <sub>128</sub></td><td><a href="https://github.com/Li-Evan/awesome-jev/blob/main/zh-CN/scenarios/agents.md">🤖 Agent 与编排</a> <sub>246</sub></td></tr>
<tr><td><a href="https://github.com/Li-Evan/awesome-jev/blob/main/zh-CN/scenarios/games.md">🎮 游戏与互动</a> <sub>276</sub></td><td><a href="https://github.com/Li-Evan/awesome-jev/blob/main/zh-CN/scenarios/robotics.md">🦾 机器人与仿真</a> <sub>61</sub></td><td><a href="https://github.com/Li-Evan/awesome-jev/blob/main/zh-CN/scenarios/search.md">🔎 搜索与 RAG</a> <sub>86</sub></td><td><a href="https://github.com/Li-Evan/awesome-jev/blob/main/zh-CN/scenarios/safety.md">🛡️ 安全与审核</a> <sub>128</sub></td></tr>
<tr><td><a href="https://github.com/Li-Evan/awesome-jev/blob/main/zh-CN/scenarios/data.md">📊 数据与评测</a> <sub>135</sub></td><td><a href="https://github.com/Li-Evan/awesome-jev/blob/main/zh-CN/scenarios/support.md">🎧 客服与销售</a> <sub>44</sub></td><td><a href="https://github.com/Li-Evan/awesome-jev/blob/main/zh-CN/scenarios/legal-health.md">⚖️ 法律、医疗与科研</a> <sub>28</sub></td><td><a href="https://github.com/Li-Evan/awesome-jev/blob/main/zh-CN/scenarios/commerce.md">🛍️ 电商与营销</a> <sub>45</sub></td></tr>
<tr><td><a href="https://github.com/Li-Evan/awesome-jev/blob/main/zh-CN/scenarios/creative.md">✍️ 写作、媒体与创意</a> <sub>134</sub></td><td><a href="https://github.com/Li-Evan/awesome-jev/blob/main/zh-CN/scenarios/voice.md">🗣️ 语音与实时交互</a> <sub>54</sub></td><td><a href="https://github.com/Li-Evan/awesome-jev/blob/main/zh-CN/scenarios/productivity.md">🧰 个人效率</a> <sub>127</sub></td><td><a href="https://github.com/Li-Evan/awesome-jev/blob/main/zh-CN/scenarios/education.md">🎓 教育</a> <sub>10</sub></td></tr>
<tr><td><a href="https://github.com/Li-Evan/awesome-jev/blob/main/zh-CN/scenarios/other.md">🧪 其他实验</a> <sub>46</sub></td></tr>
</table>

### 💰 金融与交易

交易 agent、市场信号、欺诈与风险检查，以及财务文档处理。

<table>
<tr>
<td width="33%" valign="top"><a href="https://x.com/MoonGotchi/status/2101320141065609294"><img src="https://pbs.twimg.com/amplify_video_thumb/2101320107947401216/img/4Uj1jx6q_1O7MusA.jpg" alt="全自动链上交易机器人" width="100%"></a><br><b><a href="https://x.com/MoonGotchi/status/2101320141065609294">全自动链上交易机器人</a></b><br><sub>MoonGotchi · X · ♥ 23.9k · 2026-09-19</sub><br>一个晚上搭出来的全自动实时交易机器人，读取链上和链下数据快速做交易决策；作者自述目前已亏损 $31,680。</td>
<td width="33%" valign="top"><a href="https://x.com/abolbuild/status/2100523868913807410"><img src="https://pbs.twimg.com/amplify_video_thumb/2100523731923722240/img/b6b47us-K3FIDHDC.jpg" alt="用 1 万美元让 Jev 做交易" width="100%"></a><br><b><a href="https://x.com/abolbuild/status/2100523868913807410">用 1 万美元让 Jev 做交易</a></b><br><sub>abolbuild · X · ♥ 1.6k · 2026-09-17</sub><br>实验性交易 agent：交给 Jev $10,000 余额，由它做交易决策，附演示视频。</td>
<td width="33%" valign="top"><a href="https://github.com/kyotofin/tax-doc-classifier"><img src="https://pbs.twimg.com/amplify_video_thumb/2100973360989773825/img/yMtL6CxrKMVXQEHV.jpg" alt="tax-doc-classifier" width="100%"></a><br><b><a href="https://github.com/kyotofin/tax-doc-classifier">tax-doc-classifier</a></b><br><sub>kyotofin · GitHub · ⭐ 351 · 2026-09-18</sub><br>用两个 Choice 把 PDF 页面归入各类 IRS 表格，每页约十分之一美分，并给出在标注测试集上的错误率。</td>
</tr>
<tr>
<td width="33%" valign="top"><a href="https://x.com/SUOHA_AI/status/2101275294451515740"><img src="https://pbs.twimg.com/amplify_video_thumb/2101274788513693696/img/Gj7UchuQIdpkqvAz.jpg" alt="Jev Trader (Inverse)" width="100%"></a><br><b><a href="https://x.com/SUOHA_AI/status/2101275294451515740">Jev Trader (Inverse)</a></b><br><sub>SUOHA_AI · X · ♥ 454 · 2026-09-19</sub><br>Monad Jev 交易演示的反向版本：镜像每一笔订单，原版买入时卖出、卖出时买入，每个区块做一次决策。</td>
<td width="33%" valign="top"><a href="https://x.com/abolbuild/status/2100690370912805049"><img src="https://pbs.twimg.com/amplify_video_thumb/2100688652665806848/img/1aEeVftB38YD0AWr.jpg" alt="用 1 万美元让 Jev 交易 BTC" width="100%"></a><br><b><a href="https://x.com/abolbuild/status/2100690370912805049">用 1 万美元让 Jev 交易 BTC</a></b><br><sub>abolbuild · X · ♥ 392 · 2026-09-17</sub><br>给 Jev $10,000 让它交易 BTC 30 天的实验，输入包括市场数据、衍生品、宏观、链上数据、新闻和情绪。</td>
<td width="33%" valign="top"><a href="https://x.com/tommy_jepsen/status/2100939646653903063"><img src="https://pbs.twimg.com/amplify_video_thumb/2100938100272746496/img/8yisuerchTVTcFTn.jpg" alt="丹麦股市回测" width="100%"></a><br><b><a href="https://x.com/tommy_jepsen/status/2100939646653903063">丹麦股市回测</a></b><br><sub>tommy_jepsen · X · ♥ 850 · 2026-09-18</sub><br>回测 Jev 在整个 2025 年（239 个交易日）交易丹麦股市，依据来自市场数据、新闻、Wikipedia 和 Google Trends 的情绪；810 万个 token 花费 $0.32。</td>
</tr>
</table>

**[查看金融与交易全部 89 条 →](https://github.com/Li-Evan/awesome-jev/blob/main/zh-CN/scenarios/finance.md)**

### 💻 编程与开发工具

代码审查、编程 agent 的模型路由、上下文压缩、代码语义搜索和 CI 检查。

<table>
<tr>
<td width="33%" valign="top"><a href="https://github.com/tamaratran/fast-jev-compaction"><img src="https://external-preview.redd.it/MGlnNDRiMG1xYXFoMV6tliTw1N13OJYLOxukOcY6kypXBn-V9gWyZw5eTACt.png?format=pjpg&amp;auto=webp&amp;s=fb4a34a2ae0aa5577c81ee2b59363e6950096c7c" alt="fast-jev-compaction" width="100%"></a><br><b><a href="https://github.com/tamaratran/fast-jev-compaction">fast-jev-compaction</a></b><br><sub>tamaratran · GitHub · ⭐ 6.1k · 2026-09-17</sub><br>Claude Code 插件，用针对每个工具调用的保留/丢弃 Noul 取代压缩摘要；请从 GitHub 安装，因为 npm 上同名的包来自另一个发布者。</td>
<td width="33%" valign="top"><a href="https://x.com/Neriousy/status/2100287208166969746"><img src="https://pbs.twimg.com/amplify_video_thumb/2100286679386873857/img/vlw6EBlSVZ9uAoHc.jpg" alt="用 OpenCode 做 app 测试" width="100%"></a><br><b><a href="https://x.com/Neriousy/status/2100287208166969746">用 OpenCode 做 app 测试</a></b><br><sub>Neriousy · X · ♥ 1.3k · 2026-09-16</sub><br>把 Jev 与 OpenCode 编程 agent 搭配起来做快速 app 测试的演示。</td>
<td width="33%" valign="top"><a href="https://x.com/miu21590/status/2101857866378362926"><img src="https://pbs.twimg.com/amplify_video_thumb/2101857791967178752/img/MiCcd9s5hrptUHqe.jpg" alt="Codex 推理强度路由器" width="100%"></a><br><b><a href="https://x.com/miu21590/status/2101857866378362926">Codex 推理强度路由器</a></b><br><sub>miu21590 · X · ♥ 3k · 2026-09-21</sub><br>一套 Codex 配置，让 Jev 在任务过程中调整 GPT-6 的推理强度：卡住时加大思考，常规步骤时减少思考，在作者的测试中 Astra 成本降低了 50%。</td>
</tr>
<tr>
<td width="33%" valign="top"><a href="https://x.com/rafalwilinski/status/2100882207879434359"><img src="https://pbs.twimg.com/amplify_video_thumb/2100881920343105536/img/c1y4THiGwA2GfXGa.jpg" alt="对抗式浏览器发布测试" width="100%"></a><br><b><a href="https://x.com/rafalwilinski/status/2100882207879434359">对抗式浏览器发布测试</a></b><br><sub>rafalwilinski · X · ♥ 5.4k · 2026-09-18</sub><br>大规模并行、基于浏览器的对抗式测试套件，专门尝试把每次软件发布搞坏，每跑一次只要几美分。</td>
<td width="33%" valign="top"><a href="https://x.com/redp314/status/2100585126652481915"><img src="https://pbs.twimg.com/amplify_video_thumb/2100585029533372416/img/ZcrsntW2yWgtB_HD.jpg" alt="Jev PR 评审器" width="100%"></a><br><b><a href="https://x.com/redp314/status/2100585126652481915">Jev PR 评审器</a></b><br><sub>redp314 · X · ♥ 2.8k · 2026-09-17</sub><br>PR 评审工具，一次调用把 diff 发给 Jev，拿回以概率表示的 14 项类型化检查，再映射为拦截、安全审查、小问题或合并，每个 PR 只要 $0.00007。</td>
<td width="33%" valign="top"><a href="https://x.com/dani_avila7/status/2101176629745561686"><img src="https://pbs.twimg.com/amplify_video_thumb/2101176234411425792/img/UgEWGdQPunczzXcv.jpg" alt="Claude Code 的 Jev 模型路由器" width="100%"></a><br><b><a href="https://x.com/dani_avila7/status/2101176629745561686">Claude Code 的 Jev 模型路由器</a></b><br><sub>dani_avila7 · X · ♥ 1.4k · 2026-09-19</sub><br>Claude Code 的 mod，通过 TypeSafe API 或 Vercel AI Gateway，让 Jev 为每个请求判定子 agent 模型、主模型（只在会话开始时判定，以保住缓存）和推理强度等级。</td>
</tr>
</table>

**[查看编程与开发工具全部 515 条 →](https://github.com/Li-Evan/awesome-jev/blob/main/zh-CN/scenarios/coding.md)**

### 🌐 浏览器与电脑操控

在真实浏览器、桌面和手机上点击、输入和导航的 agent。

<table>
<tr>
<td width="33%" valign="top"><a href="https://github.com/browser-use/jev-ultrafast"><img src="https://raw.githubusercontent.com/browser-use/jev-ultrafast/main/docs/banner.svg" alt="jev-ultrafast" width="100%"></a><br><b><a href="https://github.com/browser-use/jev-ultrafast">jev-ultrafast</a></b><br><sub>browser-use · GitHub · ⭐ 16.6k · 2026-09-16</sub><br>浏览器 agent：每一步在一次请求里从页面元素表中选出操作和目标，并为每种操作预先推测一个目标，只有需要输入文字时才调用小型 LLM。</td>
<td width="33%" valign="top"><a href="https://x.com/Saccc_c/status/2100864907046768890"><img src="https://pbs.twimg.com/amplify_video_thumb/2100853279089647616/img/H6altwjZQ28_1bfY.jpg" alt="Jev Use for Codex" width="100%"></a><br><b><a href="https://x.com/Saccc_c/status/2100864907046768890">Jev Use for Codex</a></b><br><sub>Saccc_c · X · ♥ 1.8k · 2026-09-18</sub><br>以 Jev 为决策层的 Codex 电脑操控，演示中添加 Mac 日历事件比 Codex 内置的电脑操控更快更流畅，token 成本相近。</td>
<td width="33%" valign="top"><a href="https://x.com/thdxr/status/2100288951978164647"><img src="https://pbs.twimg.com/amplify_video_thumb/2100286679386873857/img/vlw6EBlSVZ9uAoHc.jpg" alt="OpenCode 用 Jev 做浏览器操控" width="100%"></a><br><b><a href="https://x.com/thdxr/status/2100288951978164647">OpenCode 用 Jev 做浏览器操控</a></b><br><sub>thdxr · X · ♥ 3.7k · 2026-09-16</sub><br>面向应用测试的快速浏览器自动化预览，把 Jev 与 OpenCode 的 browser-use CLI 搭配使用。</td>
</tr>
<tr>
<td width="33%" valign="top"><a href="https://github.com/awlevin/typesafe-computer-use"><img src="https://raw.githubusercontent.com/awlevin/typesafe-computer-use/main/docs/banner.svg" alt="typesafe-computer-use" width="100%"></a><br><b><a href="https://github.com/awlevin/typesafe-computer-use">typesafe-computer-use</a></b><br><sub>awlevin · GitHub · ⭐ 769 · 2026-09-16</sub><br>macOS 电脑操控 agent：先对屏幕做 OCR，再让 Jev 从提取出的控件中判定下一步动作并点击，每步约 $0.0002，只有自由文本字段才调用写作模型。</td>
<td width="33%" valign="top"><a href="https://github.com/milind-soni/tiptour-macos"><img src="https://raw.githubusercontent.com/milind-soni/tiptour-macos/main/gemnew.png" alt="TipTour" width="100%"></a><br><b><a href="https://github.com/milind-soni/tiptour-macos">TipTour</a></b><br><sub>milind-soni · GitHub · ⭐ 644 · 2026-04-08</sub><br>macOS 菜单栏电脑操控应用，默认模式接收一个以点击为主的文字任务，让 Jev 在本地检测到的屏幕控件中做选择，然后执行并验证每个动作。</td>
<td width="33%" valign="top"><a href="https://x.com/SUOHA_AI/status/2101640575812239406"><img src="https://pbs.twimg.com/amplify_video_thumb/2101632970717007872/img/lcQeA281BT79Pjt5.jpg" alt="Jev + DeepSeek 表单填写 agent" width="100%"></a><br><b><a href="https://x.com/SUOHA_AI/status/2101640575812239406">Jev + DeepSeek 表单填写 agent</a></b><br><sub>SUOHA_AI · X · ♥ 173 · 2026-09-20</sub><br>浏览器 agent，在一个陌生网站上用 38 秒填完一份 16 题的申请表，Jev 选择每个动作，DeepSeek V4.1 Flash 撰写文字答案。</td>
</tr>
</table>

**[查看浏览器与电脑操控全部 128 条 →](https://github.com/Li-Evan/awesome-jev/blob/main/zh-CN/scenarios/browser.md)**

### 🤖 Agent 与编排

通用 agent 的工具与 skill 选择、审批、规划、记忆和 harness 决策。

<table>
<tr>
<td width="33%" valign="top"><a href="https://github.com/Significant-Gravitas/AutoGPT/tree/master/autogpt_platform/backend/backend/blocks/typesafe"><img src="https://raw.githubusercontent.com/Significant-Gravitas/AutoGPT/master/docs/home/.gitbook/assets/Banner_image.png" alt="AutoGPT TypeSafe blocks" width="100%"></a><br><b><a href="https://github.com/Significant-Gravitas/AutoGPT/tree/master/autogpt_platform/backend/backend/blocks/typesafe">AutoGPT TypeSafe blocks</a></b><br><sub>Significant-Gravitas · GitHub · ⭐ 187.5k 仓库 · 2023-03-16</sub><br>七个无代码模块，包括一个五出口路由器、一个是/否/不确定三路分流，以及一个分数过滤器。</td>
<td width="33%" valign="top"><a href="https://x.com/0xCodila/status/2101433560796467348"><img src="https://pbs.twimg.com/amplify_video_thumb/2101426271842349056/img/uEiR8K0UCaFoYsf-.jpg" alt="jev-usage-router" width="100%"></a><br><b><a href="https://x.com/0xCodila/status/2101433560796467348">jev-usage-router</a></b><br><sub>0xCodila · X · ♥ 2.4k · 2026-09-19</sub><br>Grok Bot 的用量路由器：在浏览、研究、重试或额外启动机器人之前，由一个 Jev Choice 选择路由；正式启用前有影子模式、日志和紧急开关。</td>
<td width="33%" valign="top"><a href="https://x.com/_aj/status/2102061534956662818"><img src="https://pbs.twimg.com/media/HSwFAsyawAA4tst.jpg?name=orig" alt="AgentRun" width="100%"></a><br><b><a href="https://x.com/_aj/status/2102061534956662818">AgentRun</a></b><br><sub>_aj · X · ♥ 1.6k · 2026-09-21</sub><br>Grep.ai 推出的 harness，面向重复性知识工作，在运行中学会这项工作，把步骤从 LLM 调用逐步转为代码；处理 100,000 条合规告警花费不到 $26K，而用 Opus 5 要超过 $290K。</td>
</tr>
<tr>
<td width="33%" valign="top"><a href="https://x.com/eve/status/2100430918762832180"><img src="https://pbs.twimg.com/media/HSY6yf5a8AA8NJi.jpg?name=orig" alt="eve 中基于标准的模型路由" width="100%"></a><br><b><a href="https://x.com/eve/status/2100430918762832180">eve 中基于标准的模型路由</a></b><br><sub>eve · X · ♥ 910 · 2026-09-17</sub><br>eve agent 框架中的实验性 autoModel 选项，用 Jev 在多个以自然语言标准描述的模型之间为每个请求做路由。</td>
<td width="33%" valign="top"><a href="https://x.com/ephraimduncan/status/2100454070536351824"><img src="https://pbs.twimg.com/amplify_video_thumb/2100454021852954624/img/hqULLONlXw40573G.jpg" alt="Jev 模型路由器" width="100%"></a><br><b><a href="https://x.com/ephraimduncan/status/2100454070536351824">Jev 模型路由器</a></b><br><sub>ephraimduncan · X · ♥ 1.9k · 2026-09-17</sub><br>模型路由器，询问 Jev 哪个语言模型最适合每个传入请求，再把请求转发给该模型，附演示视频。</td>
<td width="33%" valign="top"><a href="https://x.com/CodingGarden/status/2100665210419950031"><img src="https://pbs.twimg.com/amplify_video_thumb/2100664410935332864/img/KPApgq0AysL_SFeg.jpg" alt="不用 LLM 的聊天机器人" width="100%"></a><br><b><a href="https://x.com/CodingGarden/status/2100665210419950031">不用 LLM 的聊天机器人</a></b><br><sub>CodingGarden · X · ♥ 1.2k · 2026-09-17</sub><br>完全不用 LLM 构建的聊天助手：Jev 在网页搜索、Wikipedia、天气、Todoist 和 Home Assistant 之间挑选工具及其参数，带引用的回答即时返回。</td>
</tr>
</table>

**[查看Agent 与编排全部 246 条 →](https://github.com/Li-Evan/awesome-jev/blob/main/zh-CN/scenarios/agents.md)**

### 🎮 游戏与互动

会玩游戏的 agent、实时决策，以及好玩的互动演示。

<table>
<tr>
<td width="33%" valign="top"><a href="https://x.com/CompleteSkeptic/status/2099925687465570372"><img src="https://pbs.twimg.com/amplify_video_thumb/2099924592534183936/img/hBGk8j8MRxBgPyg9.jpg" alt="Jev 玩 Doom" width="100%"></a><br><b><a href="https://x.com/CompleteSkeptic/status/2099925687465570372">Jev 玩 Doom</a></b><br><sub>CompleteSkeptic · X · ♥ 5k · 2026-09-15</sub><br>TypeSafe 的发布演示：Jev 根据结构化游戏状态实时玩 Doom，每秒约 10 次调用，每小时约 $7。</td>
<td width="33%" valign="top"><a href="https://x.com/CompleteSkeptic/status/2099925688925184171"><img src="https://pbs.twimg.com/amplify_video_thumb/2099924665515012096/img/Q3mdVD5jfOZOkMww.jpg" alt="维基百科竞速" width="100%"></a><br><b><a href="https://x.com/CompleteSkeptic/status/2099925688925184171">维基百科竞速</a></b><br><sub>CompleteSkeptic · X · ♥ 2.6k · 2026-09-15</sub><br>发布演示：Jev 只通过链接从一个维基百科页面跑到另一个，每一步都要在数百到数千个链接中做选择。</td>
<td width="33%" valign="top"><a href="https://github.com/fhshaik/typesafe-mario"><img src="https://external-preview.redd.it/bzVydG83cHlodXBoMZE7fOmaTIl8CDi0AASExP3Al1xQRlZJ2gAIQDJfa5Lr.png?format=pjpg&amp;auto=webp&amp;s=2ba386e6d1e858b09755e0c4f9ecbb8adbfc0c15" alt="typesafe-mario" width="100%"></a><br><b><a href="https://github.com/fhshaik/typesafe-mario">typesafe-mario</a></b><br><sub>fhshaik · GitHub · ⭐ 338 · 2026-09-16</sub><br>用一个决定手柄动作的 Choice、一个跳跃 Noul 和一个危险 Score 来玩 Super Mario。</td>
</tr>
<tr>
<td width="33%" valign="top"><a href="https://x.com/aimlapi/status/2100372930282573876"><img src="https://pbs.twimg.com/amplify_video_thumb/2100371773275406336/img/NmHPy0pAprSsC6Gi.jpg" alt="Jev 对战 Fable 5.1 和 GPT-6 Astra 下棋" width="100%"></a><br><b><a href="https://x.com/aimlapi/status/2100372930282573876">Jev 对战 Fable 5.1 和 GPT-6 Astra 下棋</a></b><br><sub>aimlapi · X · ♥ 2.3k · 2026-09-16</sub><br>5+0 快棋，每步一次 API 调用：Jev 对 Fable 5.1 子力落后，但凭约 2.6 秒一步的速度赢在对手超时；对 GPT-6 Astra 则在 18 步内被将死。</td>
<td width="33%" valign="top"><a href="https://www.spritefusion.com/blog/generating-game-level-in-real-time-with-jev"><img src="https://www.spritefusion.com/blog/generating-game-level-in-real-time-with-jev/jev-terrain-generation.png" alt="用 Jev 实时生成游戏关卡" width="100%"></a><br><b><a href="https://www.spritefusion.com/blog/generating-game-level-in-real-time-with-jev">用 Jev 实时生成游戏关卡</a></b><br><sub>Hugo Duprez (Sprite Fusion) · 文章 · ♥ 2.8k · 2026-09-18</sub><br>无尽平台跳跃游戏，地形根据游戏状态实时生成：Jev 决定每一段的宽度、间隙、高度和图块类型，由游戏代码放置图块。</td>
<td width="33%" valign="top"><a href="https://x.com/_MaxBlade/status/2100634359099232678"><img src="https://pbs.twimg.com/amplify_video_thumb/2100633400717565952/img/KlytLNSLCQA-yY2E.jpg" alt="Jev 玩 Subway Surfers" width="100%"></a><br><b><a href="https://x.com/_MaxBlade/status/2100634359099232678">Jev 玩 Subway Surfers</a></b><br><sub>_MaxBlade · X · ♥ 4.1k · 2026-09-17</sub><br>Jev 以超越人类的速度玩 Subway Surfers，包括同时开 50 局，整个过程花费不到一美分。</td>
</tr>
</table>

**[查看游戏与互动全部 276 条 →](https://github.com/Li-Evan/awesome-jev/blob/main/zh-CN/scenarios/games.md)**

### 🦾 机器人与仿真

具身控制、驾驶模拟器，以及物理世界中的决策。

<table>
<tr>
<td width="33%" valign="top"><a href="https://x.com/leojrr/status/2101161666410893328"><img src="https://pbs.twimg.com/amplify_video_thumb/2101161072447180800/img/sRIOALT11TUpdAdU.jpg" alt="红绿灯控制" width="100%"></a><br><b><a href="https://x.com/leojrr/status/2101161666410893328">红绿灯控制</a></b><br><sub>leojrr · X · ♥ 7k · 2026-09-19</sub><br>一个城市仿真，由 Jev 控制所有红绿灯；关掉 Jev 后，平均等待时间上升超过 600%。</td>
<td width="33%" valign="top"><a href="https://x.com/Raptor_zip/status/2101091398447505567"><img src="https://pbs.twimg.com/amplify_video_thumb/2101070240444772353/img/Ci_PCLcMigmoAdks.jpg" alt="Jev 控制双臂机器人" width="100%"></a><br><b><a href="https://x.com/Raptor_zip/status/2101091398447505567">Jev 控制双臂机器人</a></b><br><sub>Raptor_zip · X · ♥ 432 · 2026-09-18</sub><br>双臂机器人，Jev 负责三层控制器中的决策层，IK 和物理计算留在代码中，响应时间 500 毫秒，每次试验约 0.5 日元。</td>
<td width="33%" valign="top"><a href="https://github.com/standardagents/jevpilot"><img src="https://raw.githubusercontent.com/standardagents/jevpilot/main/docs/try-jevpilot.svg" alt="JevPilot" width="100%"></a><br><b><a href="https://github.com/standardagents/jevpilot">JevPilot</a></b><br><sub>standardagents · GitHub · ⭐ 160 · 2026-09-17</sub><br>Three.js 驾驶模拟器，由 Jev 作为自动驾驶仪选择运动和方向。</td>
</tr>
<tr>
<td width="33%" valign="top"><a href="https://x.com/SigGravitas/status/2100325221932958134"><img src="https://pbs.twimg.com/amplify_video_thumb/2100323655389474816/img/LLOAJ3wie1phk45K.jpg" alt="Jev 实时驾驶" width="100%"></a><br><b><a href="https://x.com/SigGravitas/status/2100325221932958134">Jev 实时驾驶</a></b><br><sub>SigGravitas · X · ♥ 288 · 2026-09-16</sub><br>把 Jev 接到驾驶模拟器的原始控制上，模拟器不会因为它思考而暂停，Jev 实时操控一辆行驶中的车。</td>
<td width="33%" valign="top"><a href="https://github.com/openroboto-ai/jev-robot-control"><img src="https://raw.githubusercontent.com/openroboto-ai/jev-robot-control/main/media/final.png" alt="Jev 机器人控制" width="100%"></a><br><b><a href="https://github.com/openroboto-ai/jev-robot-control">Jev 机器人控制</a></b><br><sub>openroboto-ai · GitHub · ⭐ 39 · 2026-09-19</sub><br>MuJoCo 实验：Jev 1.13、GPT-6 Astra 和 GPT-4.1 mini 通过选择运动方向和夹爪指令，操控 xArm7 把苹果放到盘子上；Jev 完成任务花费 $0.018825，对比的是 $5.933624。</td>
<td width="33%" valign="top"><a href="https://x.com/dimentary/status/2101018760371171420"><img src="https://pbs.twimg.com/amplify_video_thumb/2101017646154366976/img/02bH3Hxy9l0qEffS.jpg" alt="Jev 作为 MuJoCo 机械臂策略" width="100%"></a><br><b><a href="https://x.com/dimentary/status/2101018760371171420">Jev 作为 MuJoCo 机械臂策略</a></b><br><sub>dimentary · X · ♥ 624 · 2026-09-18</sub><br>在 MuJoCo 中测试把 Jev 当作实时机械臂策略，根据文本形式的几何和接触信息，把每次更新拆成两次调用（先决定下一步做什么，再决定机械臂和夹爪如何移动）。</td>
</tr>
</table>

**[查看机器人与仿真全部 61 条 →](https://github.com/Li-Evan/awesome-jev/blob/main/zh-CN/scenarios/robotics.md)**

### 🔎 搜索与 RAG

重排、检索过滤、语义搜索和知识图谱。

<table>
<tr>
<td width="33%" valign="top"><a href="https://x.com/Saboo_Shubham_/status/2101576462042366114"><img src="https://pbs.twimg.com/amplify_video_thumb/2101576307352203264/img/THdpZUHOSRsSoTVr.jpg" alt="语义查找（⌘F）扩展" width="100%"></a><br><b><a href="https://x.com/Saboo_Shubham_/status/2101576462042366114">语义查找（⌘F）扩展</a></b><br><sub>Saboo_Shubham_ · X · ♥ 2.3k · 2026-09-20</sub><br>开源 Chrome 扩展，用语义匹配替代页内查找，近乎实时地高亮与你输入意思一致的段落。</td>
<td width="33%" valign="top"><a href="https://github.com/superagents-lab/jev-search"><img src="https://raw.githubusercontent.com/superagents-lab/jev-search/main/public/og-home.png" alt="jev-search" width="100%"></a><br><b><a href="https://github.com/superagents-lab/jev-search">jev-search</a></b><br><sub>superagents-lab · GitHub · ⭐ 387 · 2026-09-17</sub><br>自然语言网页搜索，用 Choice 选择时间范围和查询词，每个来源只有通过其 Noul 才保留（需要 Search1API 密钥）。</td>
<td width="33%" valign="top"><a href="https://x.com/venturetwins/status/2101341075684434245"><img src="https://pbs.twimg.com/amplify_video_thumb/2101339712464326656/img/A8yq5IoXQuhJAi32.jpg" alt="Zillow 自然语言搜索" width="100%"></a><br><b><a href="https://x.com/venturetwins/status/2101341075684434245">Zillow 自然语言搜索</a></b><br><sub>venturetwins · X · ♥ 949 · 2026-09-19</sub><br>扫描数千条 Zillow 房源，按网站没有提供筛选项的属性分类，比如建筑风格、翻修状况或离高速公路的距离，用时不到 20 秒，花费 $0.18。</td>
</tr>
<tr>
<td width="33%" valign="top"><a href="https://github.com/volcengine/OpenViking/blob/main/openviking/models/rerank/jev_rerank.py"><img src="https://raw.githubusercontent.com/volcengine/OpenViking/main/docs/images/ov-logo.png" alt="OpenViking 重排器" width="100%"></a><br><b><a href="https://github.com/volcengine/OpenViking/blob/main/openviking/models/rerank/jev_rerank.py">OpenViking 重排器</a></b><br><sub>volcengine · GitHub · ⭐ 38.4k 仓库 · 2026-01-05</sub><br>上下文数据库的重排提供方，一次请求中用 Noul 为每篇文档打分。</td>
<td width="33%" valign="top"><a href="https://github.com/vectorize-io/hindsight/blob/main/hindsight-api-slim/hindsight_api/engine/cross_encoder.py"><img src="https://raw.githubusercontent.com/vectorize-io/hindsight/main/hindsight-docs/static/img/hindsight-github-banner.png" alt="Hindsight 的 Jev 重排器" width="100%"></a><br><b><a href="https://github.com/vectorize-io/hindsight/blob/main/hindsight-api-slim/hindsight_api/engine/cross_encoder.py">Hindsight 的 Jev 重排器</a></b><br><sub>vectorize-io · GitHub · ⭐ 24.9k 仓库 · 2025-10-30</sub><br>agent 记忆系统 Hindsight 中的重排提供方：只向 Jev 问一个问题，把每个召回候选都作为选项，答案本身就是排序，一次请求完成。</td>
<td width="33%" valign="top"><a href="https://x.com/VisheshBaghell/status/2100536228827496721"><img src="https://pbs.twimg.com/amplify_video_thumb/2100535993141239808/img/Q_giQHiIdU-aAvI6.jpg" alt="Upweight" width="100%"></a><br><b><a href="https://x.com/VisheshBaghell/status/2100536228827496721">Upweight</a></b><br><sub>VisheshBaghell · X · ♥ 73 · 2026-09-17</sub><br>可用六个滑块（技术深度、争议性、实用性、AI 水文、新颖度、职业相关性）重排的 Hacker News 首页，显示每篇文章的 Jev 分数；阅读原文由 Firecrawl 完成。</td>
</tr>
</table>

**[查看搜索与 RAG全部 86 条 →](https://github.com/Li-Evan/awesome-jev/blob/main/zh-CN/scenarios/search.md)**

### 🛡️ 安全与审核

护栏、越狱与提示词注入筛查、内容审核和策略检查。

<table>
<tr>
<td width="33%" valign="top"><a href="https://x.com/RBilgil/status/2100976648552169805"><img src="https://pbs.twimg.com/amplify_video_thumb/2100976173836533760/img/APDonY80SB2iSYhj.jpg" alt="实时 AI 水文检测器" width="100%"></a><br><b><a href="https://x.com/RBilgil/status/2100976648552169805">实时 AI 水文检测器</a></b><br><sub>RBilgil · X · ♥ 16k · 2026-09-18</sub><br>由 Jev 驱动的实时检测器，在你滚动信息流时标记 AI 生成的水文。</td>
<td width="33%" valign="top"><a href="https://x.com/rauchg/status/2100307962262872105"><img src="https://pbs.twimg.com/media/HSW-E8wWgAAyw9O.jpg?name=orig" alt="fx 自动模式安全审查器" width="100%"></a><br><b><a href="https://x.com/rauchg/status/2100307962262872105">fx 自动模式安全审查器</a></b><br><sub>rauchg · X · ♥ 3.9k · 2026-09-16</sub><br>安全审查器，检查 fx 编程 agent 自动模式下的每条命令；基准测试中 Jev 的 p95 最多快 18 倍，且比它取代的 GPT Luna 模型更准确。</td>
<td width="33%" valign="top"><a href="https://github.com/dubinc/dub/blob/main/apps/web/lib/api/links/malicious-link-check.ts"><img src="https://repository-images.githubusercontent.com/529708137/3261d942-ed30-4800-b82c-06e3630ef255" alt="Dub 恶意链接检查" width="100%"></a><br><b><a href="https://github.com/dubinc/dub/blob/main/apps/web/lib/api/links/malicious-link-check.ts">Dub 恶意链接检查</a></b><br><sub>dubinc · GitHub · ⭐ 24.8k 仓库 · 2022-08-27</sub><br>在 Dub 链接平台上，每条新短链先过域名黑名单，再由 Jev 筛查，拦截指向钓鱼、恶意软件、伪装跳转、赌博和成人内容的目标地址。</td>
</tr>
<tr>
<td width="33%" valign="top"><a href="https://www.reddit.com/r/vibecoding/comments/1wk8jco/using_jev_for_realtime_live_chat_moderation/"><img src="https://external-preview.redd.it/aDk2b3Y5bnpwZHFoMTOXplwNgOesr4K-iFJwFPFaj-sxE-6FkXSkmDW1mccL.png?format=pjpg&amp;auto=webp&amp;s=afac7a4c8fb00d2e7d659fb8bd5f0a05b0b238c1" alt="实时聊天审核" width="100%"></a><br><b><a href="https://www.reddit.com/r/vibecoding/comments/1wk8jco/using_jev_for_realtime_live_chat_moderation/">实时聊天审核</a></b><br><sub>Rare_Guide_9830 · Reddit · ▲ 264 · 2026-09-19</sub><br>模拟直播聊天：Jev 把每条进来的消息分到观众自选的频道，如“提问”“反馈”“搞笑”，合并重复内容并丢弃垃圾信息。</td>
<td width="33%" valign="top"><a href="https://x.com/jozef_gherman/status/2100627898436571555"><img src="https://pbs.twimg.com/amplify_video_thumb/2100627500082536449/img/v0pfbmvg6HGwc_JF.jpg" alt="Jev Detector" width="100%"></a><br><b><a href="https://x.com/jozef_gherman/status/2100627898436571555">Jev Detector</a></b><br><sub>jozef_gherman · X · ♥ 301 · 2026-09-17</sub><br>免费的 AI 水文检测器，约 2 秒内就能在最多约 10,000 词的文本中高亮出套路化、像机器生成的句子。</td>
<td width="33%" valign="top"><a href="https://github.com/umputun/tg-spam"><img src="https://github.com/umputun/tg-spam/raw/master/site/tg-spam-bg.png" alt="tg-spam 的 Jev 检查器" width="100%"></a><br><b><a href="https://github.com/umputun/tg-spam">tg-spam 的 Jev 检查器</a></b><br><sub>umputun · GitHub · ⭐ 446 · 2023-11-23</sub><br>自托管 Telegram 反垃圾机器人和库 TG-Spam 新增了一个 Jev 垃圾检查器，与其他检测器一起，用一个类型化问题判断每条消息。</td>
</tr>
</table>

**[查看安全与审核全部 128 条 →](https://github.com/Li-Evan/awesome-jev/blob/main/zh-CN/scenarios/safety.md)**

### 📊 数据与评测

数据标注、大规模分类、数据管道、可观测性和 LLM 评测。

<table>
<tr>
<td width="33%" valign="top"><a href="https://github.com/realZachi/pg-jev"><img src="https://raw.githubusercontent.com/realZachi/pg-jev/master/docs/assets/header.svg" alt="pg-jev" width="100%"></a><br><b><a href="https://github.com/realZachi/pg-jev">pg-jev</a></b><br><sub>realZachi · GitHub · ⭐ 290 · 2026-09-17</sub><br>支持 <code>WHERE jev(t, '...')</code> 查询的 PostgreSQL 扩展，每次请求批量处理 20 行，并报告批次变大时准确率如何下降。</td>
<td width="33%" valign="top"><a href="https://github.com/koala73/worldmonitor/blob/main/shared/jev-classify.js"><img src="https://repository-images.githubusercontent.com/1130564872/59ff0927-deb4-4941-8cbc-b68cbe060417" alt="World Monitor 的 Jev 标题分类器" width="100%"></a><br><b><a href="https://github.com/koala73/worldmonitor/blob/main/shared/jev-classify.js">World Monitor 的 Jev 标题分类器</a></b><br><sub>koala73 · GitHub · ⭐ 87.2k 仓库 · 2026-01-08</sub><br>实时地缘政治新闻看板里的标题分类器：为每条标题向 jev-1.13.0 询问五级严重程度和 14 个主题类别之一，校验答案，失败时走回退。</td>
<td width="33%" valign="top"><a href="https://x.com/hamiltonulmer/status/2100370557405667768"><img src="https://pbs.twimg.com/media/HSYD5B1bsAAWqeg.jpg?name=orig" alt="DuckDB 的 Jev 扩展" width="100%"></a><br><b><a href="https://x.com/hamiltonulmer/status/2100370557405667768">DuckDB 的 Jev 扩展</a></b><br><sub>hamiltonulmer · X · ♥ 1.5k · 2026-09-16</sub><br>DuckDB 扩展，可在 SQL 里用 Jev 给任意 CSV、Parquet 或 DuckDB 表的行分类，1k 行约需 10 秒。</td>
</tr>
<tr>
<td width="33%" valign="top"><a href="https://github.com/apache/airflow/blob/main/providers/common/ai/docs/classifier_models.rst"><img src="https://raw.githubusercontent.com/apache/airflow/main/airflow-core/docs/img/ui-dark/dags.png" alt="Airflow 的 LLM 分支" width="100%"></a><br><b><a href="https://github.com/apache/airflow/blob/main/providers/common/ai/docs/classifier_models.rst">Airflow 的 LLM 分支</a></b><br><sub>apache · GitHub · ⭐ 46.9k 仓库 · 2015-04-13</sub><br>用一个 Jev Choice 挑选下一个任务，置信度低的情况交给人处理。</td>
<td width="33%" valign="top"><a href="https://x.com/tarasshyn/status/2101012033340571952"><img src="https://pbs.twimg.com/amplify_video_thumb/2101011544515526656/img/iSFydnTHWxsRx9hy.jpg" alt="Flowsery 会话回放分拣" width="100%"></a><br><b><a href="https://x.com/tarasshyn/status/2101012033340571952">Flowsery 会话回放分拣</a></b><br><sub>tarasshyn · X · ♥ 829 · 2026-09-18</sub><br>用 Jev 跑了 300 万条会话回放事件：40 秒内审阅 3,247 个会话，抓到 132 次愤怒点击、116 次无效点击和 95 个 JavaScript 错误，并开了 213 个修复 PR 草稿，花费 $2.17。</td>
<td width="33%" valign="top"><a href="https://x.com/yyyole/status/2101184012899537092"><img src="https://pbs.twimg.com/amplify_video_thumb/2101182941317787648/img/1Imy25EAcuq8Wllx.jpg" alt="AI 新闻筛选" width="100%"></a><br><b><a href="https://x.com/yyyole/status/2101184012899537092">AI 新闻筛选</a></b><br><sub>yyyole · X · ♥ 330 · 2026-09-19</sub><br>为挑选内容选题，用 Jev 把过去 7 天近 2,700 条 AI 新闻逐条筛了一遍，用时约 2 分钟，花费 $0.21。</td>
</tr>
</table>

**[查看数据与评测全部 135 条 →](https://github.com/Li-Evan/awesome-jev/blob/main/zh-CN/scenarios/data.md)**

### 🎧 客服与销售

工单路由、邮件分拣、线索打分和 CRM 自动化。

<table>
<tr>
<td width="33%" valign="top"><a href="https://x.com/romanbuildsaas/status/2100891604735099103"><img src="https://pbs.twimg.com/amplify_video_thumb/2100891566340501504/img/agvkcRfNWmnGbRI5.jpg" alt="线索与外联消息评分" width="100%"></a><br><b><a href="https://x.com/romanbuildsaas/status/2100891604735099103">线索与外联消息评分</a></b><br><sub>romanbuildsaas · X · ♥ 3.3k · 2026-09-18</sub><br>在 40 秒内花 $0.09 为 700 条高意向线索和个性化外联消息打分，用置信度分数预测每条消息的效果，并标记线索与消息不匹配的情况。</td>
<td width="33%" valign="top"><a href="https://github.com/twentyhq/twenty/tree/main/packages/twenty-server/src/modules/workflow/workflow-executor/workflow-actions/classify"><img src="https://repository-images.githubusercontent.com/572984571/ef151ee9-3060-418b-bf88-cb689ab78c7b" alt="Twenty 的 Classify 工作流动作" width="100%"></a><br><b><a href="https://github.com/twentyhq/twenty/tree/main/packages/twenty-server/src/modules/workflow/workflow-executor/workflow-actions/classify">Twenty 的 Classify 工作流动作</a></b><br><sub>twentyhq · GitHub · ⭐ 57.2k 仓库 · 2022-12-01</sub><br>开源 CRM Twenty 工作流中的 Classify 步骤，就一条记录向 Jev 问 choice、score 或布尔问题，让后续步骤根据答案和概率分支。</td>
<td width="33%" valign="top"><a href="https://x.com/Box/status/2100993278955188320"><img src="https://pbs.twimg.com/amplify_video_thumb/2100986163511357440/img/o0Yzl7VqISwchxkk.jpg" alt="Box 事件分诊" width="100%"></a><br><b><a href="https://x.com/Box/status/2100993278955188320">Box 事件分诊</a></b><br><sub>Box · X · ♥ 31 · 2026-09-18</sub><br>一个 Box 工作流：拉取一份事件报告，询问 Jev 它是否影响客户、严重程度如何，把文件移到 Escalate、Monitor 或 Review，并把低置信度的情况交给人工。</td>
</tr>
<tr>
<td width="33%" valign="top"><a href="https://www.youtube.com/watch?v=CupCEehe2OQ"><img src="https://i.ytimg.com/vi/CupCEehe2OQ/hqdefault.jpg" alt="用 Jev 做销售 Copilot" width="100%"></a><br><b><a href="https://www.youtube.com/watch?v=CupCEehe2OQ">用 Jev 做销售 Copilot</a></b><br><sub>Kelvin Cleto · 视频 · ♥ 1.9k · 2026-09-20</sub><br>葡萄牙语讲解视频：一个追踪通话和销售剧本步骤的销售会议 copilot，在调用任何 LLM 之前先让 Jev 回答低成本的决策问题，以降低成本。</td>
<td width="33%" valign="top"><a href="https://x.com/tarasshyn/status/2101043617649340678"><img src="https://pbs.twimg.com/amplify_video_thumb/2101043565207916544/img/jTZjaCWwP1d9sx6D.jpg" alt="RedReplier 购买信号评分" width="100%"></a><br><b><a href="https://x.com/tarasshyn/status/2101043617649340678">RedReplier 购买信号评分</a></b><br><sub>tarasshyn · X · ♥ 463 · 2026-09-18</sub><br>在 53 秒内花 $0.65，为来自 Reddit、X、Bluesky、Hacker News 和 Facebook 的 170 万条提及中的 1,759,932 个购买信号打分，按意向、产品匹配度和竞品提及排序。</td>
<td width="33%" valign="top"><a href="https://x.com/razeden0/status/2102119174466396250"><img src="https://pbs.twimg.com/amplify_video_thumb/2102119097077006336/img/qrIQdb9RSULrBTqB.jpg" alt="Grok 与 Jev 线索筛选器" width="100%"></a><br><b><a href="https://x.com/razeden0/status/2102119174466396250">Grok 与 Jev 线索筛选器</a></b><br><sub>razeden0 · X · ♥ 172 · 2026-09-21</sub><br>线索资格判断管线：Jev 对 3,412 条线索每条回答 6 个问题（15.7 秒内完成 20,472 个决策，花费 $0.41），Grok 4.7 只为值得看的线索起草外联消息。</td>
</tr>
</table>

**[查看客服与销售全部 44 条 →](https://github.com/Li-Evan/awesome-jev/blob/main/zh-CN/scenarios/support.md)**

### ⚖️ 法律、医疗与科研

合规检查、医学与科学筛查，以及科研工作流。

<table>
<tr>
<td width="33%" valign="top"><a href="https://1kpapers.com"><img src="https://www.1kpapers.com/opengraph-image.png?opengraph-image.1mk7bn86uhq5h.png" alt="1kpapers" width="100%"></a><br><b><a href="https://1kpapers.com">1kpapers</a></b><br><sub>nutlope · 应用 · ♥ 2k · 2026-09-17</sub><br>按主题梳理 2025-2026 年 1,018 篇 AI 研究论文的网站，每篇论文先由 DeepSeek V4 Flash 总结，再由 Jev 分到 24 个主题中，总花费 $0.08。</td>
<td width="33%" valign="top"><a href="https://x.com/Paiky16/status/2101628198928982219"><img src="https://praneeth16.github.io/jev/og.png" alt="结合 GEPA 检测药物不良反应" width="100%"></a><br><b><a href="https://x.com/Paiky16/status/2101628198928982219">结合 GEPA 检测药物不良反应</a></b><br><sub>Paiky16 · X · ♥ 138 · 2026-09-20</sub><br>用 Jev 标记医学文献中报告疑似药物不良反应的句子，再用 GEPA 提示词优化把 F1 从 69.1% 提升到 79.7%，误报从 47 个降到 22 个。</td>
<td width="33%" valign="top"><a href="https://x.com/rheum_ai/status/2100454043361722798"><img src="https://pbs.twimg.com/amplify_video_thumb/2100452479016321024/img/nAyq81QFzA6UzPqM.jpg" alt="实时临床问诊分类器" width="100%"></a><br><b><a href="https://x.com/rheum_ai/status/2100454043361722798">实时临床问诊分类器</a></b><br><sub>rheum_ai · X · ♥ 432 · 2026-09-17</sub><br>原型：在临床问诊过程中把环境记录（ambient scribe）的转录稿喂给 Jev，实时遍历医学本体、分类症状、更新鉴别诊断并标出危险信号。</td>
</tr>
<tr>
<td width="33%" valign="top"><a href="https://x.com/rothken/status/2102151333193363791"><img src="https://lawanalyzer.com/social-card.png" alt="LawAnalyzer" width="100%"></a><br><b><a href="https://x.com/rothken/status/2102151333193363791">LawAnalyzer</a></b><br><sub>rothken · X · ♥ 51 · 2026-09-21</sub><br>一家律所 AI 实验室推出的免费测试版构建套件，用于在 Jev 上搭建法律分析小程序，输出可复用的 JSON 和 Jev 代码，律师和学生可以保存并改编。</td>
<td width="33%" valign="top"><a href="https://github.com/choxos/jev-reviewer"><img src="https://raw.githubusercontent.com/choxos/jev-reviewer/main/documentation/tour.gif" alt="Jev Reviewer" width="100%"></a><br><b><a href="https://github.com/choxos/jev-reviewer">Jev Reviewer</a></b><br><sub>choxos · GitHub · ⭐ 32 · 2026-09-18</sub><br>用于系统综述的浏览器内数据提取工具，回答提取表单或 RoB 2、ROBINS-I、QUADAS-2、TIDieR 模板中的问题，并给出来自试验报告的原文引述和页码位置。</td>
<td width="33%" valign="top"><a href="https://x.com/DevaiahShrithan/status/2102097862805053950"><img src="https://pbs.twimg.com/media/HSwmC5JawAArib5.jpg" alt="让 Jev 读完每一篇 AI 论文" width="100%"></a><br><b><a href="https://x.com/DevaiahShrithan/status/2102097862805053950">让 Jev 读完每一篇 AI 论文</a></b><br><sub>DevaiahShrithan · 文章 · ♥ 6 · 2026-09-21</sub><br>把 1993 到 2026 年的 464,720 篇 arXiv AI 摘要交给 Jev，每篇问五个问题（是否声称达到 SOTA、是否发布代码、是否像 LLM 写的、论文类型、炒作程度），描绘 AI 论文的变化。</td>
</tr>
</table>

**[查看法律、医疗与科研全部 28 条 →](https://github.com/Li-Evan/awesome-jev/blob/main/zh-CN/scenarios/legal-health.md)**

### 🛍️ 电商与营销

商品目录、广告、评论、定价和营销工作流。

<table>
<tr>
<td width="33%" valign="top"><a href="https://x.com/TheMattBerman/status/2100654891756589230"><img src="https://pbs.twimg.com/amplify_video_thumb/2100654321792684032/img/cXvU50KmCe6QFu86.jpg" alt="竞品广告拆解" width="100%"></a><br><b><a href="https://x.com/TheMattBerman/status/2100654891756589230">竞品广告拆解</a></b><br><sub>TheMattBerman · X · ♥ 6.7k · 2026-09-17</sub><br>40 秒、9 美分拆解 37 个品牌的 724 条在投广告：Jev 为每条广告标注钩子、形式、优惠、CTA、认知阶段，以及与落地页是否脱节。</td>
<td width="33%" valign="top"><a href="https://x.com/borjafat/status/2101018783976722479"><img src="https://pbs.twimg.com/amplify_video_thumb/2101018477087592448/img/9YlAHKLLo_h6rgtK.jpg" alt="站内链接 SEO 审计" width="100%"></a><br><b><a href="https://x.com/borjafat/status/2101018783976722479">站内链接 SEO 审计</a></b><br><sub>borjafat · X · ♥ 3.9k · 2026-09-18</sub><br>45.1 秒读完一个网站的全部 586 个页面，花 $0.21 重建内链图，放置了 584 条链接，并对 139 个找不到合理匹配的页面拒绝加链接；同样时间里 Claude Opus 5 只处理了 21 个页面。</td>
<td width="33%" valign="top"><a href="https://x.com/elvissun/status/2100951347080421409"><img src="https://pbs.twimg.com/amplify_video_thumb/2100951319108567040/img/AZ1jFv9ySdRV-JYE.jpg" alt="NewsJack 品牌新闻匹配" width="100%"></a><br><b><a href="https://x.com/elvissun/status/2100951347080421409">NewsJack 品牌新闻匹配</a></b><br><sub>elvissun · X · ♥ 3.9k · 2026-09-18</sub><br>读完早上的 384 条新闻，告诉 15 个品牌各自该蹭哪几条，用时 24.9 秒、花费 $0.19，而 Claude Opus 5 花 $0.77 只处理了 4 条；演示附带 30+ 个 PR agent skill。</td>
</tr>
<tr>
<td width="33%" valign="top"><a href="https://x.com/nailthy62/status/2101388186916454439"><img src="https://pbs.twimg.com/amplify_video_thumb/2101384523124740096/img/1Q6moTMdLcZ-mJ3r.jpg" alt="Drape 实时试穿" width="100%"></a><br><b><a href="https://x.com/nailthy62/status/2101388186916454439">Drape 实时试穿</a></b><br><sub>nailthy62 · X · ♥ 4.3k · 2026-09-19</sub><br>Drape 的实时虚拟试穿实验：Jev 读取语音转写和当前穿搭，从衣橱里挑一件单品并实时换装，每次决策 $0.0011、约 620 毫秒。</td>
<td width="33%" valign="top"><a href="https://x.com/irabukht/status/2101090579127951694"><img src="https://pbs.twimg.com/amplify_video_thumb/2101089408099516416/img/Smzn-jtE8prvdY90.jpg" alt="基于 Jev 的 Ryze SEO/GEO agent" width="100%"></a><br><b><a href="https://x.com/irabukht/status/2101090579127951694">基于 Jev 的 Ryze SEO/GEO agent</a></b><br><sub>irabukht · X · ♥ 1.5k · 2026-09-18</sub><br>SEO 与 GEO 审计修复 agent 的实践记录：把分析数据读取、引用扫描和缺口分析迁移到 Jev 后，每个客户的成本从约 $250 下降了 90%。</td>
<td width="33%" valign="top"><a href="https://x.com/OriSilver/status/2100941251478458871"><img src="https://pbs.twimg.com/amplify_video_thumb/2100940464870301696/img/g-uzVt-FDP21an26.jpg" alt="Maxfusion 竞品广告研究" width="100%"></a><br><b><a href="https://x.com/OriSilver/status/2100941251478458871">Maxfusion 竞品广告研究</a></b><br><sub>OriSilver · X · ♥ 582 · 2026-09-18</sub><br>竞品研究：19 秒、$0.12 把 Resilia 广告库中的 1,891 条广告按客户旅程阶段和广告风格分类，并附有完整的账户深度分析，即将上线 Maxfusion MCP。</td>
</tr>
</table>

**[查看电商与营销全部 45 条 →](https://github.com/Li-Evan/awesome-jev/blob/main/zh-CN/scenarios/commerce.md)**

### ✍️ 写作、媒体与创意

写作反馈、生成式 UI、音乐、艺术和社交媒体工具。

<table>
<tr>
<td width="33%" valign="top"><a href="https://x.com/ctatedev/status/2101022101750571357"><img src="https://pbs.twimg.com/amplify_video_thumb/2101022081810911232/img/3tKdQ3Y2_ZGSg3Q7.jpg" alt="json-render + Jev" width="100%"></a><br><b><a href="https://x.com/ctatedev/status/2101022101750571357">json-render + Jev</a></b><br><sub>ctatedev · X · ♥ 7.7k · 2026-09-18</sub><br>生成式 UI 实验：Jev 从你自己的设计系统中选择组件和动作，json-render 在几毫秒内绘制出界面。</td>
<td width="33%" valign="top"><a href="https://x.com/mattdesl/status/2100899669802963060"><img src="https://pbs.twimg.com/amplify_video_thumb/2100898643117068288/img/p9Jp61lJyiq-UoWK.jpg" alt="颜色理解实验" width="100%"></a><br><b><a href="https://x.com/mattdesl/status/2100899669802963060">颜色理解实验</a></b><br><sub>mattdesl · X · ♥ 5.6k · 2026-09-18</sub><br>视频实验，探究 Jev 是否理解颜色，并探索把快速、低成本的判断作为新 UI 和 UX 范式的基础。</td>
<td width="33%" valign="top"><a href="https://x.com/anshuc/status/2100246929611411501"><img src="https://pbs.twimg.com/amplify_video_thumb/2100245288183066624/img/ARkl8CTLZxp1KXSa.jpg" alt="并行逐像素作画" width="100%"></a><br><b><a href="https://x.com/anshuc/status/2100246929611411501">并行逐像素作画</a></b><br><sub>anshuc · X · ♥ 1.6k · 2026-09-16</sub><br>让 Jev 并行预测每一个像素来画出一幅图的实验。</td>
</tr>
<tr>
<td width="33%" valign="top"><a href="https://x.com/robj3d3/status/2100722975645598191"><img src="https://pbs.twimg.com/amplify_video_thumb/2100722766362406912/img/pH0lahpfd-qTj_nE.jpg" alt="SuperX 帖子评分器" width="100%"></a><br><b><a href="https://x.com/robj3d3/status/2100722975645598191">SuperX 帖子评分器</a></b><br><sub>robj3d3 · X · ♥ 1.4k · 2026-09-17</sub><br>X 帖子评分器：每份草稿向 Jev 问 61 个问题，约 1 秒、花费 $0.0004；模型基于 207 位创作者的 9,481 条帖子拟合，3 次里有 2 次能挑中爆款。</td>
<td width="33%" valign="top"><a href="https://github.com/ChetasLua/jevmeter"><img src="https://raw.githubusercontent.com/ChetasLua/jevmeter/main/docs/banner.jpg" alt="jevmeter" width="100%"></a><br><b><a href="https://github.com/ChetasLua/jevmeter">jevmeter</a></b><br><sub>ChetasLua · GitHub · ⭐ 81 · 2026-09-17</sub><br>CLI，转写任意视频，让 Jev 按选定的评分标准（比如是否在辩论中回避问题）给每句话打分，并把分数渲染成 16:9 剪辑里的实时仪表，可以直接发布。</td>
<td width="33%" valign="top"><a href="https://x.com/leojrr/status/2100470174130250127"><img src="https://pbs.twimg.com/amplify_video_thumb/2100467692117295104/img/01ZWSKAA75eSiFlc.jpg" alt="用 Jev 重建 X 推荐算法" width="100%"></a><br><b><a href="https://x.com/leojrr/status/2100470174130250127">用 Jev 重建 X 推荐算法</a></b><br><sub>leojrr · X · ♥ 1.2k · 2026-09-17</sub><br>用 Jev 复刻 X 的排序算法，基于公开的权重和由所有人帖子组成的全局信息流，模拟一条帖子能触达多远。</td>
</tr>
</table>

**[查看写作、媒体与创意全部 134 条 →](https://github.com/Li-Evan/awesome-jev/blob/main/zh-CN/scenarios/creative.md)**

### 🗣️ 语音与实时交互

语音助手，以及随你打字或说话实时反应的界面。

<table>
<tr>
<td width="33%" valign="top"><a href="https://x.com/jackcheng/status/2100729670991802386"><img src="https://pbs.twimg.com/amplify_video_thumb/2100729243185324032/img/YNw8njfnSXu-Tbyr.jpg" alt="指点加语音的画布" width="100%"></a><br><b><a href="https://x.com/jackcheng/status/2100729670991802386">指点加语音的画布</a></b><br><sub>jackcheng · X · ♥ 5k · 2026-09-17</sub><br>用摄像头指点加说话来控制的白板画布：语音、手指位置和画布形状都发给 Jev，由它在约 167 毫秒 内选出动作、目标和位置。</td>
<td width="33%" valign="top"><a href="https://x.com/instantricecook/status/2100814590300889426"><img src="https://pbs.twimg.com/amplify_video_thumb/2100809295809974272/img/_1rbvz04k6wjpcGW.jpg" alt="语音控制 Mac 的 agent" width="100%"></a><br><b><a href="https://x.com/instantricecook/status/2100814590300889426">语音控制 Mac 的 agent</a></b><br><sub>instantricecook · X · ♥ 6.1k · 2026-09-18</sub><br>Mac 上的语音控制电脑操控（computer use），指令一边说一边执行，用户话还没说完就已经打开了备忘录。</td>
<td width="33%" valign="top"><a href="https://x.com/moritzkremb/status/2100577979021832365"><img src="https://pbs.twimg.com/amplify_video_thumb/2100577954338373633/img/tbH43kHpUotE3hzK.jpg" alt="实时语音控制浏览器" width="100%"></a><br><b><a href="https://x.com/moritzkremb/status/2100577979021832365">实时语音控制浏览器</a></b><br><sub>moritzkremb · X · ♥ 3.8k · 2026-09-17</sub><br>用语音控制浏览器：口述转录交给 Jev，它在约 300 毫秒 内返回概率并触发点击，每次决策 $0.0002。</td>
</tr>
<tr>
<td width="33%" valign="top"><a href="https://x.com/nhciao/status/2101967227327267297"><img src="https://pbs.twimg.com/media/HSuwDLga4AEkvLg.jpg?name=orig" alt="Jev + Rime 输入法" width="100%"></a><br><b><a href="https://x.com/nhciao/status/2101967227327267297">Jev + Rime 输入法</a></b><br><sub>nhciao · X · ♥ 763 · 2026-09-21</sub><br>测试把 Jev 与开源的 Rime（鼠须管）中文输入法搭配，在打字时把想要的字在候选中排得更靠前。</td>
<td width="33%" valign="top"><a href="https://x.com/BhosalePratim/status/2100986774742765991"><img src="https://pbs.twimg.com/amplify_video_thumb/2100986186219081728/img/LmAGU-0Pd5ZABGeb.jpg" alt="从语音意图到工具调用" width="100%"></a><br><b><a href="https://x.com/BhosalePratim/status/2100986774742765991">从语音意图到工具调用</a></b><br><sub>BhosalePratim · X · ♥ 476 · 2026-09-18</sub><br>语音 agent 实验：用 Jev 替换 LLM 的工具选择步骤，让决策在部分转录上就能进行，agent 在用户说完之前就能行动。</td>
<td width="33%" valign="top"><a href="https://x.com/_MaxBlade/status/2100967959879471519"><img src="https://pbs.twimg.com/amplify_video_thumb/2100966551826444288/img/i2s52ZeMNTOO-IRD.jpg" alt="无需唤醒词的常开助手" width="100%"></a><br><b><a href="https://x.com/_MaxBlade/status/2100967959879471519">无需唤醒词的常开助手</a></b><br><sub>_MaxBlade · X · ♥ 1.6k · 2026-09-18</sub><br>持续监听、无需唤醒词的语音助手，由 Jev 根据概率判断一段语音是给电脑的命令还是普通对话。</td>
</tr>
</table>

**[查看语音与实时交互全部 54 条 →](https://github.com/Li-Evan/awesome-jev/blob/main/zh-CN/scenarios/voice.md)**

### 🧰 个人效率

邮件、笔记、日历、浏览和日常自动化。

<table>
<tr>
<td width="33%" valign="top"><a href="https://jaste.app/"><img src="https://jaste.app/og.png" alt="Jaste" width="100%"></a><br><b><a href="https://jaste.app/">Jaste</a></b><br><sub>Marcus Lowe · 应用 · ♥ 9.7k · 2026-09-21</sub><br>Mac 剪贴板应用，其 Smart Paste 模式用 Jev 选出最适合当前焦点输入框的已保存剪贴板条目；目前为 beta 版，已宣布将支持 BYOK 和本地模式。</td>
<td width="33%" valign="top"><a href="https://x.com/ryanvogel/status/2100042788851101842"><img src="https://pbs.twimg.com/amplify_video_thumb/2100042377339588608/img/2O56_xRC0r54ugfr.jpg" alt="Jev 邮件分类测试" width="100%"></a><br><b><a href="https://x.com/ryanvogel/status/2100042788851101842">Jev 邮件分类测试</a></b><br><sub>ryanvogel · X · ♥ 3.5k · 2026-09-16</sub><br>测试 Jev 给作者自己的 1,500 封邮件分类，视频展示了批量给收件箱打标签的过程。</td>
<td width="33%" valign="top"><a href="https://github.com/jev-chat/jev-chat-jarvis"><img src="https://raw.githubusercontent.com/jev-chat/jev-chat-jarvis/main/docs/images/overlay.png" alt="Jev Chat Assistant" width="100%"></a><br><b><a href="https://github.com/jev-chat/jev-chat-jarvis">Jev Chat Assistant</a></b><br><sub>jev-chat · GitHub · ⭐ 1.8k · 2026-09-21</sub><br>Android 悬浮窗工具，通过辅助功能读取屏幕上可见的微信、QQ 和 X 聊天，让 Jev 判断对方的意图、风险等级和最佳应对，为 DeepSeek 起草的三条回复排序，并填入其中一条但不发送。</td>
</tr>
<tr>
<td width="33%" valign="top"><a href="https://x.com/rileybrown/status/2100404532119269426"><img src="https://pbs.twimg.com/amplify_video_thumb/2100403183533125632/img/54ZFO-CHvDeC-rw-.jpg" alt="500 封邮件分类" width="100%"></a><br><b><a href="https://x.com/rileybrown/status/2100404532119269426">500 封邮件分类</a></b><br><sub>rileybrown · X · ♥ 3.9k · 2026-09-17</sub><br>演示 Jev 在几秒内以 3.5 美分完成 500 封邮件的分类。</td>
<td width="33%" valign="top"><a href="https://x.com/iam_zachi/status/2100529273186472318"><img src="https://pbs.twimg.com/amplify_video_thumb/2100529029761642496/img/OY0Ltm7v7lXv5-y6.jpg" alt="基于 Jev 的实时广告拦截器" width="100%"></a><br><b><a href="https://x.com/iam_zachi/status/2100529273186472318">基于 Jev 的实时广告拦截器</a></b><br><sub>iam_zachi · X · ♥ 3.9k · 2026-09-17</sub><br>浏览器扩展，用 Jev 判断每个 DOM 元素是不是广告，并实时从页面中移除广告。</td>
<td width="33%" valign="top"><a href="https://superx.so/instead-of-doomscrolling?niche=jev"><img src="https://superx.so/creators/assets/og-doomscroll-filter.png" alt="Doomscroll Filter" width="100%"></a><br><b><a href="https://superx.so/instead-of-doomscrolling?niche=jev">Doomscroll Filter</a></b><br><sub>SuperX · 应用 · ♥ 1.7k · 2026-09-19</sub><br>免费工具：选一个细分领域，Jev 读取最近几天的 X 帖子，并把它们分成 Read（细读）、Skim（略读）或 Pass（跳过）。</td>
</tr>
</table>

**[查看个人效率全部 127 条 →](https://github.com/Li-Evan/awesome-jev/blob/main/zh-CN/scenarios/productivity.md)**

### 🎓 教育

辅导、批改、测验和学习工具。

<table>
<tr>
<td width="33%" valign="top"><a href="https://x.com/hametgholizadeh/status/2101289895624917076"><img src="https://pbs.twimg.com/amplify_video_thumb/2101289673591021568/img/opei88xzp3DDGrcF.jpg" alt="考题预测器" width="100%"></a><br><b><a href="https://x.com/hametgholizadeh/status/2101289895624917076">考题预测器</a></b><br><sub>hametgholizadeh · X · ♥ 83 · 2026-09-19</sub><br>按出现在真实考试中的可能性，给 80 道真题和 297 道练习题排序，用时 80 秒，花费 $0.0256。</td>
<td width="33%" valign="top"><a href="https://x.com/0xaniol/status/2101076982373191927"><img src="https://pbs.twimg.com/amplify_video_thumb/2101074153407422464/img/fzFh7BZaZCmGdh8v.jpg" alt="talkr" width="100%"></a><br><b><a href="https://x.com/0xaniol/status/2101076982373191927">talkr</a></b><br><sub>0xaniol · X · ♥ 111 · 2026-09-18</sub><br>口语练习应用：给你一个话题，录下 30 秒发言，由 Jev 给停顿、口头禅、重复、自信度和清晰度打分并给出反馈。</td>
<td width="33%" valign="top"><a href="https://github.com/AustinAWay/Working-Memory-Jev"><img src="https://raw.githubusercontent.com/AustinAWay/Working-Memory-Jev/main/docs/provisional-estimates-live.png" alt="Working Memory Jev (Passage)" width="100%"></a><br><b><a href="https://github.com/AustinAWay/Working-Memory-Jev">Working Memory Jev (Passage)</a></b><br><sub>AustinAWay · GitHub · ⭐ 39 · 2026-09-18</sub><br>实验性的本地教学辅助工具，向教师展示一篇教学文章在展开过程中，哪些地方可能要求学习者同时记住过多的概念或关系。</td>
</tr>
<tr>
<td width="33%" valign="top"><a href="https://github.com/wquguru/dasheng"><img src="https://opengraph.githubassets.com/1/wquguru/dasheng" alt="ReadAloud (dasheng)" width="100%"></a><br><b><a href="https://github.com/wquguru/dasheng">ReadAloud (dasheng)</a></b><br><sub>wquguru · GitHub · ⭐ 122 · 2026-09-20</sub><br>英语朗读训练工具：R2T2 流式 ASR 转写你的朗读，Jev 判断每个对不上的词是否读错、怎么读错的，再由代码把这些判断换算成分数。</td>
<td width="33%" valign="top"><a href="https://github.com/Diogenesoftoronto/keating/blob/main/scripts/training/benchmark_judge_systemone.py"><img src="https://opengraph.githubassets.com/1/Diogenesoftoronto/keating" alt="Keating 的 Jev 教学评委" width="100%"></a><br><b><a href="https://github.com/Diogenesoftoronto/keating/blob/main/scripts/training/benchmark_judge_systemone.py">Keating 的 Jev 教学评委</a></b><br><sub>Diogenesoftoronto · GitHub · ⭐ 36 仓库 · 2026-04-01</sub><br>针对 AI 导师 Keating 教学评分细则的类型化判断审阅器：Jev 给每个维度打分，并从代码枚举出的片段中选取证据，因此引文无法凭空编造；另附一个 harness，与现役 LLM 评委做对比。</td>
<td width="33%" valign="top"><a href="https://github.com/freemocap/skellyspeak/tree/main/tools/benchmarks/conversation-prompts/assessment"><img src="https://opengraph.githubassets.com/1/freemocap/skellyspeak" alt="SkellySpeak 的 Jev 评估研究" width="100%"></a><br><b><a href="https://github.com/freemocap/skellyspeak/tree/main/tools/benchmarks/conversation-prompts/assessment">SkellySpeak 的 Jev 评估研究</a></b><br><sub>freemocap · GitHub · ⭐ 35 仓库 · 2025-01-24</sub><br>语言学习应用 SkellySpeak 中的基准测试：用 Jev 按 45 项辅导技能评估学习者的消息，并在一项 648 次请求的西班牙语析因研究中与 dense 模式的 Gemini 对照组比较，配有专门的看板。</td>
</tr>
</table>

**[查看教育全部 10 条 →](https://github.com/Li-Evan/awesome-jev/blob/main/zh-CN/scenarios/education.md)**

### 🧪 其他实验

暂时还归不进单一场景的一切。

<table>
<tr>
<td width="33%" valign="top"><a href="https://x.com/neogoose_btw/status/2101428888874410069"><img src="https://pbs.twimg.com/amplify_video_thumb/2101427327746093056/img/LiNIpS9HMaBO00kW.jpg" alt="Jevassembler" width="100%"></a><br><b><a href="https://x.com/neogoose_btw/status/2101428888874410069">Jevassembler</a></b><br><sub>neogoose_btw · X · ♥ 1.5k · 2026-09-19</sub><br>讽刺性实验，干脆不写代码：你给它一个任务，Jev 在运行时预测下一条要执行的 CPU 指令。</td>
<td width="33%" valign="top"><a href="https://x.com/steventey/status/2101788378882863427"><img src="https://pbs.twimg.com/media/HSsNY_ybUAEFIK_.jpg?name=orig" alt="jev-even-odd" width="100%"></a><br><b><a href="https://x.com/steventey/status/2101788378882863427">jev-even-odd</a></b><br><sub>steventey · X · ♥ 2.4k · 2026-09-20</sub><br>玩笑性质的 npm 包，通过 AI SDK 询问 Jev 来判断一个数字是偶数还是奇数。</td>
<td width="33%" valign="top"><a href="https://x.com/sarvagya_kul/status/2100980770206879849"><img src="https://pbs.twimg.com/amplify_video_thumb/2100980671640645632/img/19dyomYRhfAONg7S.jpg" alt="候选人与公司岗位匹配" width="100%"></a><br><b><a href="https://x.com/sarvagya_kul/status/2100980770206879849">候选人与公司岗位匹配</a></b><br><sub>sarvagya_kul · X · ♥ 1.8k · 2026-09-18</sub><br>用 12 秒、$0.0005 把一份候选人档案与 400 家公司做匹配，预测最有可能拿到的职位，并标出不匹配项。</td>
</tr>
<tr>
<td width="33%" valign="top"><a href="https://github.com/narphorium/nl-logic-interpreter"><img src="https://pbs.twimg.com/amplify_video_thumb/2100984200820121600/img/dXya52zCSiVBJVaF.jpg" alt="Natural Language Logic Interpreter" width="100%"></a><br><b><a href="https://github.com/narphorium/nl-logic-interpreter">Natural Language Logic Interpreter</a></b><br><sub>narphorium · GitHub · ⭐ 6 · 2026-09-19</sub><br>可单步执行的逻辑解释器，像 Prolog 一样用 SLD 归结在纯英文事实和规则上证明目标，由 Jev 判断两句话是否陈述同一事实，从而完成合一。</td>
<td width="33%" valign="top"><a href="https://github.com/monteduro/killmyidea"><img src="https://killmyidea.stemonte.io/og.png" alt="Kill My Idea" width="100%"></a><br><b><a href="https://github.com/monteduro/killmyidea">Kill My Idea</a></b><br><sub>monteduro · GitHub · ⭐ 76 · 2026-09-17</sub><br>Web 应用，用一次请求并行问 Jev 10 个问题，把创业点子判为 KILL IT、FIX IT 或 SHIP IT，最终结论由本地权重和关卡计算得出。</td>
<td width="33%" valign="top"><a href="https://x.com/TheBalkanHacker/status/2100962091498684848"><img src="https://pbs.twimg.com/amplify_video_thumb/2100960184327688192/img/7zn9b3VwndkLLzWa.jpg" alt="用 Jev 模拟 6502" width="100%"></a><br><b><a href="https://x.com/TheBalkanHacker/status/2100962091498684848">用 Jev 模拟 6502</a></b><br><sub>TheBalkanHacker · X · ♥ 43 · 2026-09-18</sub><br>让 Jev 直接充当计算机本身、实时模拟 6502 CPU 的实验；能跑完整的短程序，但仍会不时与参考模拟器的结果出现偏差。</td>
</tr>
</table>

**[查看其他实验全部 46 条 →](https://github.com/Li-Evan/awesome-jev/blob/main/zh-CN/scenarios/other.md)**

## 开源模型与兼容服务

模仿 Jev 接口的社区模型和服务。它们的准确率和校准都是自报数据，普遍不如 Jev，请用自己的数据评估。

<table>
<tr>
<td width="33%" valign="top"><a href="https://huggingface.co/harshatheg/Qwen-2.5-1B-RLCD"><img src="https://cdn-thumbnails.huggingface.co/social-thumbnails/models/harshatheg/Qwen-2.5-1B-RLCD.png" alt="Qwen-2.5-1B-RLCD" width="100%"></a><br><b><a href="https://huggingface.co/harshatheg/Qwen-2.5-1B-RLCD">Qwen-2.5-1B-RLCD</a></b><br><sub>harshatheg · Hugging Face · ♥ 524 · 2026-09-16</sub><br>面向 Apple Silicon 的并行约束解码引擎，基于原版 Qwen2.5-1.5B 一次回答多字段决策 schema，只发布代码，没有训练好的 RLCD 权重。</td>
<td width="33%" valign="top"><a href="https://github.com/NandhaKishorM/laya"><img src="https://raw.githubusercontent.com/NandhaKishorM/laya/main/assets/laya_vs_jev_full.png" alt="Laya" width="100%"></a><br><b><a href="https://github.com/NandhaKishorM/laya">Laya</a></b><br><sub>NandhaKishorM · GitHub · ⭐ 12k · 2026-09-18</sub><br>基于 ModernBERT 式编码器的开放本地非自回归决策模型，从 421M 的英文检查点到多语言检查点都有，回答 Choice、Score 和 Noul 问题每个问题 33 毫秒，并带有按请求分流的路由器。</td>
<td width="33%" valign="top"><a href="https://x.com/taroleo/status/2101106887840370919"><img src="https://pbs.twimg.com/amplify_video_thumb/2101102823408807936/img/k_uNGVHacO6DG6mC.jpg" alt="蒸馏出的 4B 本地决策模型" width="100%"></a><br><b><a href="https://x.com/taroleo/status/2101106887840370919">蒸馏出的 4B 本地决策模型</a></b><br><sub>taroleo · X · ♥ 3k · 2026-09-19</sub><br>在一台 DGX Spark 上用 26 小时把 DeepSeek V4 Flash 的判断蒸馏成 Jev 式 4B 本地模型，以 1/20 的体量胜过老师模型的即时模式，每次决策约 22 毫秒。</td>
</tr>
<tr>
<td width="33%" valign="top"><a href="https://x.com/atomic_chat_hq/status/2102160983409955244"><img src="https://pbs.twimg.com/amplify_video_thumb/2102158998103363584/img/AStT6MxzhJzruHIE.jpg" alt="Laya 对战 Jev：Tetris" width="100%"></a><br><b><a href="https://x.com/atomic_chat_hq/status/2102160983409955244">Laya 对战 Jev：Tetris</a></b><br><sub>atomic_chat_hq · X · ♥ 2.8k · 2026-09-21</sub><br>一场 Tetris 对决：在 16GB MacBook Air 上本地运行的开放权重 Laya 模型，决策速度快 11 倍，击败了云端 Jev。</td>
<td width="33%" valign="top"><a href="https://github.com/wdobry/laya-playground"><img src="https://brainfunctioncollapse.com/laya/og.png" alt="Laya playground" width="100%"></a><br><b><a href="https://github.com/wdobry/laya-playground">Laya playground</a></b><br><sub>wdobry · GitHub · ⭐ 71 · 2026-09-20</sub><br>本地网站，为开源 Laya 决策模型提供游戏、基准测试和 agent skill，并在同样的 500 个带标签样本上与托管版 Jev 对比。</td>
<td width="33%" valign="top"><a href="https://github.com/mizorewww/laya-mlx"><img src="https://raw.githubusercontent.com/mizorewww/laya-mlx/main/docs/assets/snake-demo.gif" alt="Laya-MLX" width="100%"></a><br><b><a href="https://github.com/mizorewww/laya-mlx">Laya-MLX</a></b><br><sub>mizorewww · GitHub · ⭐ 4.3k · 2026-09-19</sub><br>Apple Silicon 上开放 Laya 类型化决策检查点的原生 MLX 运行时：简短英文决策中位耗时 13.4 毫秒，多语言检查点为 7.4 毫秒，无需 PyTorch 或云端 API；以贪吃蛇做了演示。</td>
</tr>
</table>

**[查看开源模型与兼容服务全部 240 条 →](https://github.com/Li-Evan/awesome-jev/blob/main/zh-CN/pages/open-models.md)**

## 用 Jev 开发

从你的技术栈调用 Jev 的方式：托管访问、框架适配、可观测性和社区 SDK。

### 模型访问

- [OpenRouter 上的 Jev](https://x.com/OpenRouter/status/2100744709589316009) - OpenRouter 宣布 Jev 已通过其 API 开放 beta，返回带概率的类型化决策，而不是生成文本。
- [OpenCode Zen 的 Jev 端点](https://github.com/anomalyco/opencode/blob/dev/packages/web/src/content/docs/zen.mdx) - OpenCode 的 Zen 网关在 /v1/systemone 端点提供 Jev 1.13，使用 Zen API 密钥，另有限时免费的 jev-1.13-free 模型。
- [Convex AI Gateway 的 Jev 支持](https://github.com/get-convex/convex-backend/blob/main/npm-packages/docs/docs/ai-gateway/api.mdx) - Convex 的 AI Gateway 通过 decisions 端点以 typesafe/jev-1.13 提供 Jev，可在 Convex action 中借助 AI SDK 的 evaluate 和 @convex-dev/ai-sdk-provider 包调用。
- [Bifrost 的 TypeSafe 提供方](https://github.com/maximhq/bifrost/tree/dev/core/providers/typesafe) - Bifrost AI 网关中的 TypeSafe 提供方，提供可直接替换的 /typesafe 前缀，为 api.typesafe.ai 编写的客户端（包括官方 SDK）无需改动就能经由 Bifrost 使用。
- [GPT-Load 的 Jev 渠道](https://github.com/tbphp/gpt-load/blob/main/internal/channel/modules/jev.go) - 自托管 AI 网关 GPT-Load 的 Jev 渠道模块，把 TypeSafe 官方 API 加为提供方，支持批量导入密钥、调度和故障转移。
- [Venice API 上的 Jev](https://x.com/sabrinaesaquino/status/2101102660997017747) - 为 Jev 在 Venice API 上开放 beta 而做的演示：约 2 分钟内把 24,000 条 Hacker News 帖子分到 12 个类别。
- [Experiential 的 TypeSafe 提供方](https://github.com/experientiallabs/experiential/blob/main/exp/runtime/models/providers/typesafe.py) - 开源模型网关 Experiential 中的 TypeSafe 提供方，原生分发 Jev 决策，并拒绝把 Jev 当作聊天模型使用。
- [Cloudflare 的 Jev 模型目录条目](https://github.com/cloudflare/cloudflare-docs/blob/production/src/content/catalog-models/typesafe-jev.json) - Cloudflare 模型目录中 typesafe/jev 的条目，列出 Jev 可用于 Noul、Choice 和 Score 评估，输入每百万 token $0.042、输出免费，并附一个完整示例。
- [Pollinations 的 Jev API](https://github.com/pollinations/pollinations/blob/main/gen.pollinations.ai/src/text/systemOneClient.ts) - Pollinations 的 gen API 通过类型化的 POST /alpha/decisions 端点和 Chat Completions 以 typesafe/jev-1.13 提供 Jev，另有一个带 jev_decide 工具的 Ask Jev MCP 服务器。
- [Fly.io Sprites 上的 Jev](https://x.com/flydotio/status/2102076230183035081) - Fly.io 为 Sprites 提供的 TypeSafe 连接器，在网关处注入你的 Jev API 密钥，运行在硬件隔离 Sprites 里的 agent 调用 Jev 时密钥无需进入沙箱。

**[查看全部 68 条模型访问 →](https://github.com/Li-Evan/awesome-jev/blob/main/zh-CN/pages/build-model-access.md)**

### 框架适配

- [OpenClaw 的 TypeSafe 插件](https://github.com/openclaw/openclaw/tree/main/extensions/typesafe) - OpenClaw 官方插件，把托管的 Jev 或本地 Kev 服务器接入 OpenClaw 的决策模型 API，用于 Choice、Score 和 Boolean 判断，另有可选的 typesafe_evaluate 工具。
- [langchain-typesafe](https://github.com/langchain-ai/langchain/tree/master/libs/partners/typesafe) - LangChain 合作方包，提供用于 Choice、Noul 和 Score 问题的 TypeSafeClassifier runnable，以及实验性的 auto-mode 和模型路由中间件。
- [ai-cli](https://x.com/ctatedev/status/2100584917092409479) - Vercel Labs 的终端 AI 工具，用 npm 安装，任何 agent harness 都能在命令行里向 Jev 问是/否问题、在选项中做选择、按标准打分。
- [Composio](https://github.com/ComposioHQ/composio/tree/next/ts/packages/providers/typesafe) - TypeScript 提供方，用一个 Choice 选择并把关工具调用，并在执行前绑定取值范围封闭的参数。
- [AI SDK 的 TypeSafe 提供方](https://github.com/vercel/ai/tree/main/packages/typesafe-ai) - AI SDK 官方提供方包 @ai-sdk/typesafe-ai，通过实验性的 evaluate API 向 Jev 运行 Choice、Score 和 Boolean 问题。
- [Pydantic AI TypeSafeModel](https://github.com/pydantic/pydantic-ai/blob/main/pydantic_ai_slim/pydantic_ai/models/typesafe.py) - Pydantic AI 的模型类，在 Jev 上运行决策类 agent：output_type 的每个字段对应一个问题，答案填入输出，只需换模型名就能对比 Jev 和 LLM。
- [elizaOS 的 TypeSafe 适配器](https://github.com/elizaOS/eliza/tree/develop/packages/agent/src/services/typesafe) - elizaOS agent 包中需主动启用的服务端 TypeSafe 客户端，用 Zod 校验 Choice、Score 和 Noul 请求，只在显式调用 systemOne 时才发送；默认不注册到运行时。
- [LangChain.js](https://github.com/langchain-ai/langchainjs/tree/main/libs/providers/langchain-typesafe) - 分类器以及路由和审批中间件的 JavaScript 版本。
- [@effect/ai-typesafe](https://github.com/Effect-TS/effect/tree/main/packages/ai/typesafe) - Effect 为 TypeSafe System One API 提供的 DecisionModel 提供方，通过 Effect HttpClient 支持分类、有序评级和概率，并保留提供方返回的分布而不做归一化。
- [BAML 的 Jev 支持](https://github.com/BoundaryML/baml/tree/canary/baml_language/crates/baml_builtins2/baml_std/typesafeai) - BAML（面向 agent 的编程语言）中的 nightly v1 集成，把类型化的函数返回值映射成 Jev 问题；尚未进入稳定版发布线。

**[查看全部 174 条框架适配 →](https://github.com/Li-Evan/awesome-jev/blob/main/zh-CN/pages/build-frameworks.md)**

### 可观测性

- [Opik 的 TypeSafe 集成](https://github.com/comet-ml/opik/tree/main/sdks/python/src/opik/integrations/typesafe) - Opik Python SDK 的集成，包装同步和异步 TypeSafe 客户端，让每次 Jev 调用都在 Opik 的 LLM 可观测性与评测平台中被追踪。
- [Phoenix 的 TypeSafe 追踪](https://github.com/Arize-ai/phoenix/tree/main/docs/phoenix/integrations/llm-providers/typesafe) - 面向 TypeSafe Python 和 TypeScript SDK 的 OpenInference 埋点，把每次 System One 调用的 state、问题和类型化答案记录为 Arize Phoenix 中的 span。
- [Langfuse 的 TypeSafe 集成](https://langfuse.com/integrations/model-providers/typesafe) - 集成指南和 notebook，介绍如何通过 OpenInference 自动埋点在 Langfuse 中追踪 Jev System One 调用，无需包装客户端。
- [OpenInference 的 TypeSafe 埋点](https://github.com/Arize-ai/openinference/tree/main/python/instrumentation/openinference-instrumentation-typesafe) - 面向 TypeSafe Python SDK 的 OpenTelemetry 埋点，追踪每次 Jev System One 调用的 state、模型、问题和类型化答案，可配合任意 OTel 后端使用。
- [Jeview](https://github.com/andududu/jeview) - 非官方的本地网关，位于你的代码和 TypeSafe 之间，转发每一个 Jev 请求，把每次调用存入 SQLite，并在调用发生时把它们实时画在地图上。
- [genai-prices 的 TypeSafe 提供方](https://github.com/pydantic/genai-prices/blob/main/prices/providers/typesafe.yml) - Pydantic 用于计算 LLM API 成本的库，扩展了 TypeSafe 定价，让发往 /v1/systemone 的 Jev 调用能被识别并按输入 token 计费。
- [Laminar 的 TypeSafe 埋点](https://github.com/lmnr-ai/lmnr-python/tree/main/src/lmnr/opentelemetry_lib/opentelemetry/instrumentation/typesafe) - Laminar Python SDK 中的 OpenTelemetry 埋点，把 TypeSafe SDK 对 Jev 的 system_one 调用与其他 LLM 调用一起追踪为 span。
- [Braintrust 的 TypeSafe 埋点](https://github.com/braintrustdata/braintrust-sdk-javascript/blob/main/js/src/wrappers/typesafe.ts) - Braintrust JavaScript SDK 针对 @typesafe-ai/sdk 的埋点：wrapTypeSafe 和自动埋点把每次 systemOne 调用追踪为 Braintrust span，同时也追踪 AI SDK 的 evaluate 调用。
- [Braintrust Python SDK 的 TypeSafe 集成](https://github.com/braintrustdata/braintrust-sdk-python/tree/main/py/src/braintrust/integrations/typesafe) - Braintrust Python 追踪与评测 SDK 的内置集成，自动为 typesafe-sdk 的 system_one 调用埋点，让 Jev 的请求和答案以 Braintrust span 的形式出现。
- [Laminar 的 TypeSafe 埋点](https://github.com/lmnr-ai/lmnr-ts/tree/main/packages/lmnr/src/opentelemetry-lib/instrumentation/typesafe) - Laminar TypeScript SDK 中的 OpenTelemetry 埋点，为 TypeSafe SDK 的 systemOne 调用打补丁，把 Jev 的请求、响应和错误记录为 span。

**[查看全部 14 条可观测性 →](https://github.com/Li-Evan/awesome-jev/blob/main/zh-CN/pages/build-observability.md)**

### 社区 SDK

- [rust-sysone](https://github.com/zcoder-run/rust-sysone) - 早期的非官方 System One API Rust 客户端，作者也写了 genai crate，提供链式调用的 Request 构造器和类型化的 Noul、Choice 和 Score 问题。
- [http4k 的 TypeSafe 连接器](https://github.com/http4k/http4k/tree/master/connect/ai/typesafe) - http4k Kotlin 工具包的 TypeSafe 连接器，带类型化的 System One 客户端和一个 fake 实现，把 Jev 的 Noul、Choice 和 Score 问题暴露为 http4k action。
- [ruby_decision_model](https://github.com/obie/ruby_decision_model) - 仅用标准库的 Ruby 客户端，面向 Jev 这类决策模型，一个 Client 默认对接 OpenRouter，也可用 TypeSafe 原生 API，并解析选项、概率、评分和用量。
- [Jev for OTP](https://github.com/dannote/jev) - 把 Jev 当作 OTP 对等进程的 Elixir 客户端：GenServer 发送 state 和类型化问题，每个答案以消息的形式到达，可直接模式匹配，同时可有上百个调用在途。
- [TypeSafe Swift SDK](https://github.com/krzyzanowskim/TypeSafe) - TypeSafe System One API 的 SwiftPM 客户端，Noul、Choice、Score 问题的行为与官方 JavaScript SDK 保持一致，附带一个小型演示 app。
- [Hunch](https://github.com/carldaws/hunch) - 用于概率控制流的 Ruby 和 Rails gem，把 Jev 的答案变成 Ruby 值，提供 chance、pick 和 rate 调用，以及 likely? 这类分级谓词，可直接基于判断做分支。
- [swift-typesafe](https://github.com/ainame/swift-typesafe) - 非官方的 Swift 6.4 SDK，跟随 Python SDK 0.7.0 的 API，带一个生成类型化答案的 @QuestionSet 宏，支持动态问题和 Linux。
- [openai-scala-client 的 TypeSafe 模块](https://github.com/cequence-io/openai-scala-client/tree/master/typesafe-client) - 异步 openai-scala-client 中的 TypeSafe 模块，把共享 state 和类型化问题发给 Jev，附有按置信度把关的路由、语义查找和 OpenAI 风格适配器的示例。
- [typesafe-sdk-go (atharvamhaske)](https://github.com/atharvamhaske/typesafe-sdk-go) - 非官方 Go SDK，与官方 Python 和 JavaScript SDK 遵循同一传输协议，支持类型化的 Choice、Score、Noul 问题、类型化的答案联合类型和模型发现。
- [typesafe-ai (Rust)](https://github.com/Twister915/typesafe-ai) - System One 的类型化 Rust 客户端，可选异步 reqwest 或阻塞 ureq 后端，重试过程可观测，把 Noul、Choice 和 Score 答案反序列化为带用量数据的 Rust 枚举。

**[查看全部 107 条社区 SDK →](https://github.com/Li-Evan/awesome-jev/blob/main/zh-CN/pages/build-community-sdks.md)**

## 学习资料

官方文档和 cookbook，以及社区里最好的教程、分析、评测和演讲。

### 官方文档

- [System One](https://docs.typesafe.ai/concepts/system-one) - 快速决策模型和生成文本的 LLM 有什么区别，以及各自适合用在哪里。
- [AI 入门](https://docs.typesafe.ai/introduction/machine-learning-primer) - 为什么 Jev 用面向校准决策的强化学习（RLCD）来训练，而不是为了生成讨喜的文本。
- [状态（State）](https://docs.typesafe.ai/concepts/state) - 如何组织证据，让请求中的每个问题都基于它来判断。
- [原语](https://docs.typesafe.ai/primitives) - 对比 Choice、Score 和 Noul，并给出如何挑选原语以及一次问多个问题的规则。
- [Choice](https://docs.typesafe.ai/primitives/choice) - 从最多 255 个选项中选出一个，并为每个选项返回概率。
- [Score](https://docs.typesafe.ai/primitives/score) - 把 state 放到 2 到 10 个带描述的等级上，返回按概率加权的位置。
- [Noul](https://docs.typesafe.ai/primitives/noul) - 返回某个是非条件成立的概率。
- [进阶结构](https://docs.typesafe.ai/primitives/advanced) - 在指令和判断标准中用 JSON 写定义、对比、排除项和示例。
- [置信度](https://docs.typesafe.ai/confidence) - 置信度和概率有什么不同，以及如何按风险高低用它来决定动作是否执行。
- [用例示例](https://docs.typesafe.ai/concepts/use-case-map) - 覆盖 18 个领域的应用思路，从客服分流、招聘到金融犯罪和知识图谱。

**[查看全部 15 条官方文档 →](https://github.com/Li-Evan/awesome-jev/blob/main/zh-CN/pages/learn-official-docs.md)**

### 官方 SDK 与工具

- [typesafe-sdk-python](https://github.com/typesafe-ai/typesafe-sdk-python) - 官方 Python 客户端，在 PyPI 上以 `typesafe-sdk` 发布。
- [typesafe-sdk-js](https://github.com/typesafe-ai/typesafe-sdk-js) - 适用于 Node.js 的官方 JavaScript 和 TypeScript 客户端，在 npm 上以 `@typesafe-ai/sdk` 发布。
- [工作流评测](https://evals.typesafe.ai) - 比较多种模型在四个真实工作流上，分别以拆解后的问题和单个提示词运行时的效果。

### 官方公告

- [介绍 System One 模型和 Jev](https://typesafe.ai/blog/introducing-system-one-models-and-jev) - 发布文章，解释为什么押注决策模型而不是文本生成器。
- [宣言](https://typesafe.ai/manifesto) - TypeSafe 对 AI 驱动软件的主张：掌控工作流的应该是代码，而不是 agent 循环。

### 设计模式

- [推测式扇出](https://docs.typesafe.ai/patterns/fan-out) - 把可能用到的问题（包括只在某个分支才需要的）在一次请求里全部问完，再让代码只读取相关的答案。
- [置信度门控路由](https://docs.typesafe.ai/patterns/confidence-routing) - 把置信度当作第二个维度，对转账等风险更高的动作设置更严格的阈值。
- [组合评分](https://docs.typesafe.ai/patterns/composite-scoring) - 对每个维度分别打分，再在代码里加权合并，这样调整优先级时无需改动问题。
- [意图路由](https://docs.typesafe.ai/patterns/intent-routing) - 用一个 Choice 和一个复杂度 Score 给请求分类，再把每个请求交给代码、专门的 LLM 或人工。

### 官方 Cookbook

- [层级分类](https://docs.typesafe.ai/cookbooks/hierarchical_classification) - 以每个节点一个 Choice、并在概率上做 beam search 的方式，遍历专利分类号、零售商品、MeSH 和源码树等深层分类体系。
- [基于置信度的分类](https://docs.typesafe.ai/cookbooks/classification_using_confidence) - 把 60 份 SEC 文件归入 75 个行业组，置信度低于 0.9 时回退到更宽泛的大类，把 39 个正确答案变成 48 个有用答案。
- [智能家居助手演示](https://docs.typesafe.ai/demos/smart-home) - 用一长串推测式扇出的 Choice 解析家居指令，外加一个 Noul 识别复合请求，交给 LLM 拆分。
- [函数调用](https://docs.typesafe.ai/cookbooks/function_calling) - 把交易请求映射到十个普通的类型化函数上：用 Choice 选择函数和封闭集合参数，用 Noul 判断请求里说了哪些参数。
- [Skill 推荐](https://docs.typesafe.ai/cookbooks/skill_suggestion) - 每轮用两次请求从 182 个 agent skill 中最多挑一个，把加载错误 skill 的比例从 16.8% 降到 7.3%。
- [重排](https://docs.typesafe.ai/cookbooks/rerank_typesafe) - 每个查询-段落对用一个 Noul 给 BM25 候选打分，把法律检索的 top-10 准确率从 38% 提升到 62%，总花费约 $0.06。
- [逐行搜索](https://docs.typesafe.ai/cookbooks/semantic_find) - 用一个 Choice 给一份服务条款文档的 218 行排序，并用一个 Noul 判断文档里是否根本没有答案。
- [RAG 段落分类](https://docs.typesafe.ai/cookbooks/classifying_rag_passages) - 对每个检索到的段落跑四个 Noul，剔除提示词注入和跑题文本，并标出与问题相矛盾的段落。
- [日期提取](https://docs.typesafe.ai/cookbooks/date_extraction_cookbook) - 用 Choice 读取日期的各个部分，所有日历计算交给代码，低置信度的日期送人工复核。
- [预解析值提取](https://docs.typesafe.ai/cookbooks/pre_parsed_value_extraction_cookbook) - 先用正则表达式找出邮箱、电话号码和金额，再让一个 Choice 选出所需的那个，因此值永远不会是编造的。

**[查看全部 18 条官方 Cookbook →](https://github.com/Li-Evan/awesome-jev/blob/main/zh-CN/pages/learn-cookbooks.md)**

### 示例与 Skill

- [Jev experiments](https://github.com/dabit3/jev-experiments) - 二十一个低延迟演示应用，比如在一次请求里给 50 个候选重排。
- [TypeSafe 官方 skill](https://github.com/typesafe-ai/skills) - agent skill 的源码，可以作为 Claude Code 插件安装，也可以通过 skills.sh 安装。
- [Hello Jev (Real Python)](https://github.com/realpython/materials/tree/master/hello-jev) - Real Python 视频 Get Started With Jev in Python 的配套代码：一个火车站服务台，把严格的 Y/N 输入解析换成单个 Noul 问题。
- [Jev 版 AI cookbook](https://github.com/daveebbelaar/ai-cookbook/tree/main/models/jev) - 九个可运行示例外加四个官方模式，基于当前的 Python SDK 编写。
- [Easy-Jev](https://x.com/rory_builds/status/2100606378184171682) - 交互式 playground：修改输入，就能实时看到 Jev 的分类结果随之更新。
- [Jev 类型化决策教程](https://github.com/marktechpost-ai-media-inc/ai-agents-projects-tutorials/blob/main/LLM%20Projects/typesafe_jev_system_one_typed_decisions_tutorial_Marktechpost.ipynb) - Marktechpost 的 notebook，逐步演示 Jev 类型化决策：工单分流、重新计算置信度、简历打分、意图路由和家居自动化工具选择器，全程跟踪成本。
- [Building with Jev skill](https://github.com/dbreunig/building-with-jev-skill) - 精简的 agent skill，教编程 agent 围绕 Jev 来组织程序结构。
- [Jevify](https://github.com/ryana/jevify) - 一段粘贴进编程 agent 的提示词，让它研读 Jev 文档和你的代码库，找出哪些地方能用廉价的语义判断降低成本和延迟，或解锁新功能。
- [JEV Playground](https://x.com/mac_eth/status/2101701798968840703) - 简单的网页 playground，输入文本上下文，就能向 Jev 提 Noul、Choice 或 Score 问题来试用。
- [AI Bootcamp 的 Jev notebook](https://github.com/curiousily/AI-Bootcamp/blob/master/jev.ipynb) - Get Shit Done with AI 训练营中的一个 Jev notebook，与其他 GenAI 课程并列，用 Python SDK 讲解 TypeSafe 的 System One 类型化决策。

**[查看全部 74 条示例与 Skill →](https://github.com/Li-Evan/awesome-jev/blob/main/zh-CN/pages/learn-examples.md)**

### 教程

- [用 Jev 搭建 harness](https://x.com/sydneyrunkle/status/2100754364545761643) - 指南：如何把 Jev 加进 LangChain 的 agent harness，涵盖 Jev 的工作原理、它在 agent 循环中的位置，以及以中间件形式实现的模型路由和工具调用前风险检查。
- [Jev 工程路线图](https://x.com/0xCodila/status/2100984487802708306) - 一篇 X 长文，给出 10 步路线图，把 Jev 搭建成决策层，告诉 agent 和 LLM 下一步该做什么。
- [用 Jev 能做的 30 件事](https://x.com/29meat_ai/status/2100844631693095267) - 日语入门，讲 Jev 能做和不能做什么，逐一介绍 30 个真实原型和演示（航班搜索、浏览器 agent、游戏、交易机器人），并附上报告的速度和成本。
- [10 步搞定 Jev 工程](https://x.com/0xMovez/status/2101007482919227841) - 一篇 X 长文，给出 10 步搭建方案：把 agent 的是非判断、下一个 worker 的选择和相关性打分从 LLM 挪到 Jev，再加上模型路由器和高风险工具调用的把关。
- [Jev x Codex 实战指南](https://x.com/MakeAI_CEO/status/2101924475814212065) - 日文指南，涵盖在 Codex 中安装 TypeSafe skill、把生成与 Jev 判断分开、已公开的实验、工作中的应用，以及提升决策准确率的方法。
- [精通 Jev（完整指南）](https://x.com/chddaniel/status/2100925069765534024) - 长篇指南，涵盖 Jev 擅长什么、如何与现有 LLM 搭配使用、提问模式、用置信度门槛防止错误决策，以及五个赚钱的工作流。
- [自己动手做一个 Jev（100% 本地）](https://x.com/_avichawla/status/2101563610644496464) - 教程：不重新训练，就把开源 LLM 变成本地决策引擎，借助 SGLang 对固定选项做下一个 token 打分，并与常规文本生成做基准对比。
- [给你的 agent 装一个决策大脑](https://x.com/0xRicker/status/2101292455391809670) - 一篇 X 长文，分 10 步讲如何把 agent 的是非判断、路由和相关性判断从昂贵的 LLM 挪到 Jev 的三种问题类型上。
- [Jev 究竟是什么鬼？](https://x.com/mvanhorn/status/2100784142850097482) - 用大白话讲解 Jev：它做的是选择题而不是写作文；随后列出人们已经在用它做的九样东西，并逐一对照原帖核实过。
- [Jev 工程路线图精简版](https://x.com/DataChaz/status/2101206777924858319) - 帖子串，浓缩了一份 10 步 Jev 搭建指南：把 agent 的分岔点变成 Choice、Score 和概率，批量处理决策（一次测试中 13 个问题快了 10 倍、便宜了 12.2 倍），并对整个循环做基准测试。

**[查看全部 76 条教程 →](https://github.com/Li-Evan/awesome-jev/blob/main/zh-CN/pages/learn-guides.md)**

### 技巧与分析

- [Jev 发布帖子串](https://x.com/CompleteSkeptic/status/2099925682726002904) - 创始人 Diogo Almeida 的发布帖子串，介绍 Jev 和 RLCD 训练方法，宣称决策速度比前沿聊天模型快 20-200 倍、成本低 40-400 倍。
- [把 Jev 讲清楚](https://x.com/akshay_pachaar/status/2101037514945597645) - 一篇 X 长文，把 Jev 解释为毫秒级决策层：类型化问题如何取代“生成、解析、重试”式的 LLM 调用，以及它在应用中如何与 LLM 并列。
- [用 Jev 生成文本](https://x.com/0xSuman/status/2100030221189874015) - 一个 hack：每个字符位置问一个 Choice 问题（带 STOP 选项），读出概率最高的字母，让 Jev 写出文本。
- [把 Jev 当作聪明的 switch 语句](https://x.com/NathanFlurry/status/2100036101809619314) - 不吹不黑的讲解，认为 Jev 就是一个非常聪明的 switch 语句：它能在预定义选项上做分类、路由、打分和核验，但写不了代码或文字。
- [LLM 与 Jev 判断提示词难度的对比](https://x.com/k_grajeda/status/2099952715430596710) - 简化的并排对比，展示 LLM 和 Jev 如何给一个提示词的难度分类：一个逐 token 生成文本，一个并行算出每个选项的概率。
- [对 Jev 上下文压缩的批评](https://x.com/theo/status/2100762304862384257) - 批评观点：用 Jev 按工具调用逐条过滤并不是好的上下文压缩策略，因为压缩应当重建历史，而模型并不掌握之前发生过什么的上下文。
- [Jev 到底能做什么](https://x.com/servasyy_ai/status/2101132667056185544) - 中文的 Jev 现实检验：解释它是什么、不是什么，按用例整理真正能跑通的演示，并列出速度和准确率宣称背后的注意事项。
- [把 Jev 当作决策原语](https://x.com/MichaelLee04/status/2100003037150683593) - 约 5,000 次请求（花费约 $2）在分类、路由和意图识别上的笔记：p50 约 150 毫秒、p95 约 350 毫秒，足以支撑每轮都做检查；而且 Jev 更适合把查询拆成相互独立的问题来问。
- [把 LLM 与 Jev 的区别讲清楚](https://x.com/akshay_pachaar/status/2101309986156712025) - 解释 Jev 并不是生成得更快，而是根本不生成：相互独立的 Choice、Score 和 Noul 问题（比如一次失败部署的紧急程度、负责团队和命令风险）会被并行评估。
- [Jev 式解码的工作原理](https://x.com/NielsRogge/status/2100239244501430438) - 基于开源 Qwen2.5-RLCD 模型的图解：从一次带缓存的解码器前向传播中读出各字段的概率，而不是逐 token 生成 JSON。

**[查看全部 102 条技巧与分析 →](https://github.com/Li-Evan/awesome-jev/blob/main/zh-CN/pages/learn-techniques.md)**

### 评测与案例

- [Hermes Agent 上下文压缩成绩单](https://github.com/NousResearch/hermes-agent/blob/main/evals/compaction/results/SCORECARD-2026-09-19-jev.md) - 把一个基于 Jev 的上下文压缩插件与 Hermes 自带的压缩器对比，结论是不推荐：每次压缩便宜得多也快得多，但保留的上下文多了一倍，对工具结果的排序也不比按时间远近排更好。
- [Jev 能成为更好的 agent 评估器吗？](https://www.langchain.com/blog/jev-agent-evals-langsmith) - LangChain 在 LangSmith 中测试把 Jev 当作 agent 评测的评判器，与 LLM 评判器比较准确率、可重复性、延迟和成本。
- [电车难题：人类还是机器人](https://x.com/MaxRovensky/status/2100706874173575199) - Jev 逐个作答电车难题的视频，它选择牺牲一个人来救机器人。
- [HiringCafe 简历与岗位相关性基准](https://x.com/h_nilforoshan/status/2100409794276520341) - 帖子串，在 HiringCafe（一个月活 250 万用户的求职应用）上对 Jev 做简历与岗位描述相关性打分的基准测试。
- [代码审查基准](https://x.com/liorshkiller/status/2100936106615140757) - 基准测试：让 Jev 给原始 Git diff 打分，对比 GLM + Grok + Gemini 组合的审查器：零误报，约快 50 倍、约便宜 100 倍，bug 召回率 75%。
- [WindTunnel](https://webmcp.com/benchmark) - WebMCP 的浏览器 agent 基准，在 8 个真实网站的 49 个任务上测试 21 种配置，Jev + Mercury 2.5 综合得分第一，解出 49/49 个任务，每个任务的中位成本为 $0.0011。
- [JevBench](https://benchmarkheaven.com/jev-models) - Jev 类决策模型的基准测试，从智能、校准、速度和成本四方面给 Jev、它的开源复刻和指令模型排名，各占 25%，取几何平均；Jev 以 75.3 领先，SemIf 以 74.6 位居第二。
- [工业邮件分类基准](https://x.com/nikhilmudholkar/status/2100604560335139083) - 在 10 个类别、1,565 封德语和英语供应商邮件上的基准测试：Jev 得分 96.4%，Gemini 为 97.5% 和 98.5%，每 1,000 封邮件 $0.08，而它置信度在 99%+ 的 737 个答案无一出错。
- [Jev 对比 DeepSeek 做工单路由](https://x.com/NFT_Chen/status/2101253568774697099) - 对 500 张真实电商客服工单做并排路由：Jev 用 83 秒、$0.01 全部处理完，而 DeepSeek V4.1 Flash 在被叫停时只处理了 173 张，花了 $0.06。
- [安全流水线中的 Jev](https://x.com/grichadev/status/2100437998571860087) - 某生产安全流水线的结果表：Jev 准确率达到 99.3%，延迟 0.259s，每 1K 次 $0.026，而 Gemini 和开源模型更慢也更贵。

**[查看全部 173 条评测与案例 →](https://github.com/Li-Evan/awesome-jev/blob/main/zh-CN/pages/learn-benchmarks.md)**

### 视频与演讲

- [45 秒看懂 Jev](https://x.com/MatijaSosic/status/2100190746389135772) - 简短讲解视频，比发布视频更浅显地讲清 Jev 的核心思路。
- [Jev 来了，怎么用](https://www.youtube.com/watch?v=4mTLpuQpB80) - Startup Ideas Pod 的一期节目，Ryan Vogel 演示 Jev 总共花 18 美分分拣了 1,700 封邮件，然后讲线索打分、客服路由、视频剪辑和创业切入点。
- [7 分钟讲清 Jev](https://www.youtube.com/watch?v=vj7hysh0mOI) - 七分钟讲解 RLCD，并探讨一个用概率分布而不是文本来回答的模型能否解锁新用例。
- [JEV 拆解：首个为代码而生的 AI 模型](https://www.youtube.com/watch?v=2Bs0Ink_-Uo) - 拆解 Jev，在 Playground 中现场演示 Choice、Score、Noul 和置信度，并讨论决策模型在真实应用中适合放在哪里。
- [Jev 太强了](https://www.youtube.com/watch?v=F3YXg7AaKWE) - Theo 解释为什么 Jev 是一个带有强大安全优势的快速分类器，它是 Astra、Fable 这类推理模型的补充，而不是替代。
- [我们得聊聊 Jev](https://www.youtube.com/watch?v=2z-7pIj57f8) - Matthew Berman 回顾 Jev 发布、早期社区演示和 X 上的反应，以及一个只做决策的模型会改变什么。
- [TypeSafe 创始人技术演讲](https://x.com/0xCodez/status/2101294219633529030) - 一场 36 分钟的技术演讲录像，TypeSafe 创始人解释为什么无需人工介入的 agent 是下一步，以及 Jev 这类模型是如何训练的。
- [Jev：终极分类模型？](https://www.youtube.com/watch?v=X117w2Rark8) - 先介绍 System 1 的概念，再演示 Choice、Score 和 Noul、一个实用分类示例以及链式动作。
- [Jev 完整教程](https://x.com/moritzkremb/status/2100715237267660873) - 视频教程，讲 Jev 是什么、如何配置 API，并给出三个演示：语音控制的浏览器、AI 记忆和 YouTube 预测器。
- [RLHF 之后是什么？](https://www.youtube.com/watch?v=cJ0EOzey--o) - TypeSafe CEO 在 AI Engineer World's Fair 2026 上谈如何训练模型做出校准的决策，而不是追求人类认可。

**[查看全部 178 条视频与演讲 →](https://github.com/Li-Evan/awesome-jev/blob/main/zh-CN/pages/learn-videos.md)**

### 社区讨论

- [Hacker News 上的发布讨论帖](https://news.ycombinator.com/item?id=49717558) - 近 2,000 分、约 500 条评论，TypeSafe 团队在帖中回答了关于语义和局限的问题。
- [Jev 是什么？（r/LocalLLaMA）](https://www.reddit.com/r/LocalLLaMA/comments/1wleg4w/what_is_jev_and_what_is_it_used_for/) - r/LocalLLaMA 上的大型讨论帖（306 条评论），大家解释 Jev 是什么、与 LLM 有何不同，以及它真正有什么用。
- [拿洗车问题考 Jev](https://www.reddit.com/r/LLMDevs/comments/1wlciiq/the_famous_car_wash_question_on_jev/) - 在 Jev 上试了著名的洗车推理题，引发一场长篇争论（104 条评论）：除了速度和价格，该如何评判决策模型的智能。
- [Jev 是泛化版的 BERT 吗？](https://www.reddit.com/r/LocalLLaMA/comments/1wje4xh/still_doesnt_get_what_jev_isis_it_just_a_more/) - r/LocalLLaMA 上的讨论帖，争论 Jev 本质上是否就是一个在推理时读取自定义标准的泛化 BERT 式分类器。
- [r/ArtificialInteligence 上的 Jev 使用印象](https://www.reddit.com/r/ArtificialInteligence/comments/1wkhsyh/jev_typesafeai_is_revolutionary_as_llms/) - 热门讨论帖（155 条评论），早期用户分享对 Jev 的第一印象，包括把它用作策略预过滤器，并争论它与前沿 LLM 相比如何。
- [Jev 架构猜想](https://www.reddit.com/r/LocalLLaMA/comments/1wjjecz/jev_architecture/) - r/LocalLLaMA 上的讨论帖（57 条评论），推测 Jev 如何工作，以及它是否只是在生成文本之前就读出结果的 LLM。
- [一张信息图看懂 Jev](https://www.reddit.com/r/LLMDevs/comments/1wkwqu2/what_is_jev_typesafes_system_one_model_explained/) - 一页信息图，整理 TypeSafe 的文档和评测对 Jev 的实际说法，涵盖原语、价格、局限，以及为什么置信度字段很重要。
- [为 Pi 扩展测试 Jev](https://www.reddit.com/r/PiCodingAgent/comments/1whsav6/anyone_else_testing_out_typesafe_ais_new_system/) - 讨论帖，Pi 编程 agent 的用户对比早期的 Jev 实验，从一个工具调用安全评级器和一个计划中按提示词复杂度分流的模型路由器说起。
- [这里有人在用 Jev 吗？](https://www.reddit.com/r/PiCodingAgent/comments/1wjibh5/anyone_here_using_jev/) - r/PiCodingAgent 上的讨论帖（77 条评论），收集大家用 Jev 做的东西，起因是把一条自然语言请求路由到应用 250-300 个 API 调用中的一个。
- [怎么看 Jev？有什么用例？](https://www.reddit.com/r/machinelearningnews/comments/1wjkzs5/thoughts_on_jev_any_usecases/) - 讨论帖，权衡 Jev 是否配得上这波热度，把它与 GLiNER 等小型编码器分类器对比，并指出一些大家以前用 Haiku 做的任务。

**[查看全部 20 条社区讨论 →](https://github.com/Li-Evan/awesome-jev/blob/main/zh-CN/pages/learn-discussions.md)**

## 参与贡献

欢迎贡献！不会写代码也没关系，[填一个表单](https://github.com/Li-Evan/awesome-jev/issues/new/choose)就能提交，X 上的一条演示也算。想直接改数据的话，在 `data/` 里对应场景的文件中加一条，运行 `uv run scripts/build.py`，然后提 PR。详见[贡献指南](contributing.zh-CN.md)。

## 附注

图片直接引用各项目自己的页面，版权归原作者所有。列表文字以 CC0 发布。
