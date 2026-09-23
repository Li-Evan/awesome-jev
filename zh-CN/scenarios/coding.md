# 💻 编程与开发工具

[English](https://github.com/Li-Evan/awesome-jev/blob/main/scenarios/coding.md) · **简体中文**

代码审查、编程 agent 的模型路由、上下文压缩、代码语义搜索和 CI 检查。共 516 条，按社区热度排序。

[← 返回 Awesome Jev](https://github.com/Li-Evan/awesome-jev/blob/main/README.zh-CN.md#按场景浏览)

<table>
<tr>
<td width="260" valign="top"><a href="https://github.com/tamaratran/fast-jev-compaction"><img src="https://external-preview.redd.it/MGlnNDRiMG1xYXFoMV6tliTw1N13OJYLOxukOcY6kypXBn-V9gWyZw5eTACt.png?format=pjpg&amp;auto=webp&amp;s=fb4a34a2ae0aa5577c81ee2b59363e6950096c7c" alt="fast-jev-compaction" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/tamaratran/fast-jev-compaction">fast-jev-compaction</a></b><br><sub>tamaratran · GitHub · ⭐ 6.1k · 2026-09-17</sub><br>Claude Code 插件，用针对每个工具调用的保留/丢弃 Noul 取代压缩摘要；请从 GitHub 安装，因为 npm 上同名的包来自另一个发布者。<br><sub>相关: <a href="https://x.com/Elizaium/status/2101081763812360471">demo</a> · <a href="https://www.reddit.com/r/LLMDevs/comments/1wjjpk0/compaction_isnt_summarization_anymore_but/">discussion</a> · <a href="https://www.reddit.com/r/accelerate/comments/1wjt68i/found_the_perfect_use_case_for_typesafeai_jev/">discussion 2</a> · <a href="https://x.com/tamarajtran/status/2100694549362553153">demo 2</a> · <a href="https://x.com/altryne/status/2100739055923425589">demo 3</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/rafalwilinski/status/2100882207879434359"><img src="https://pbs.twimg.com/amplify_video_thumb/2100881920343105536/img/c1y4THiGwA2GfXGa.jpg" alt="对抗式浏览器发布测试" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/rafalwilinski/status/2100882207879434359">对抗式浏览器发布测试</a></b><br><sub>rafalwilinski · X · ♥ 5.4k · 2026-09-18</sub><br>大规模并行、基于浏览器的对抗式测试套件，专门尝试把每次软件发布搞坏，每跑一次只要几美分。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/miu21590/status/2101857866378362926"><img src="https://pbs.twimg.com/amplify_video_thumb/2101857791967178752/img/MiCcd9s5hrptUHqe.jpg" alt="Codex 推理强度路由器" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/miu21590/status/2101857866378362926">Codex 推理强度路由器</a></b><br><sub>miu21590 · X · ♥ 3k · 2026-09-21</sub><br>一套 Codex 配置，让 Jev 在任务过程中调整 GPT-6 的推理强度：卡住时加大思考，常规步骤时减少思考，在作者的测试中 Astra 成本降低了 50%。<br><sub><b>Jev 用法:</b> 每一步用 Score 评估难度并映射到推理强度等级，且不会破坏提示词缓存。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/redp314/status/2100585126652481915"><img src="https://pbs.twimg.com/amplify_video_thumb/2100585029533372416/img/ZcrsntW2yWgtB_HD.jpg" alt="Jev PR 评审器" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/redp314/status/2100585126652481915">Jev PR 评审器</a></b><br><sub>redp314 · X · ♥ 2.8k · 2026-09-17</sub><br>PR 评审工具，一次调用把 diff 发给 Jev，拿回以概率表示的 14 项类型化检查，再映射为拦截、安全审查、小问题或合并，每个 PR 只要 $0.00007。<br><sub><b>Jev 用法:</b> 每个 diff 14 个 Noul 检查；关键检查结果不确定（0.35-0.65）时升级给人工或大模型。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/Neriousy/status/2100287208166969746"><img src="https://pbs.twimg.com/amplify_video_thumb/2100286679386873857/img/vlw6EBlSVZ9uAoHc.jpg" alt="用 OpenCode 做 app 测试" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/Neriousy/status/2100287208166969746">用 OpenCode 做 app 测试</a></b><br><sub>Neriousy · X · ♥ 1.3k · 2026-09-16</sub><br>把 Jev 与 OpenCode 编程 agent 搭配起来做快速 app 测试的演示。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/mrnugget/jev-shell-history"><img src="https://raw.githubusercontent.com/mrnugget/jev-shell-history/main/demo/demo.gif" alt="jev-shell-history" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/mrnugget/jev-shell-history">jev-shell-history</a></b><br><sub>mrnugget · GitHub · ⭐ 96 · 2026-09-18</sub><br>zsh 插件，通过询问 Jev 你最可能是在补全最近 100 条不重复历史记录中的哪一条，给出 fish 风格的自动补全建议，以灰色显示并附上分数。<br><sub><b>Jev 用法:</b> 针对当前输入，在最近的历史记录中做一个 Choice。</sub><br><sub>相关: <a href="https://x.com/thorstenball/status/2100858434904109099">demo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/dani_avila7/status/2101176629745561686"><img src="https://pbs.twimg.com/amplify_video_thumb/2101176234411425792/img/UgEWGdQPunczzXcv.jpg" alt="Claude Code 的 Jev 模型路由器" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/dani_avila7/status/2101176629745561686">Claude Code 的 Jev 模型路由器</a></b><br><sub>dani_avila7 · X · ♥ 1.4k · 2026-09-19</sub><br>Claude Code 的 mod，通过 TypeSafe API 或 Vercel AI Gateway，让 Jev 为每个请求判定子 agent 模型、主模型（只在会话开始时判定，以保住缓存）和推理强度等级。<br><sub>相关: <a href="https://aitmpl.com/component/mod/productivity/jev-model-router">docs</a> · <a href="https://aitmpl.com/component/mod/productivity/jev-model-router">project</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/ryanvogel/status/2100068006592123055"><img src="https://pbs.twimg.com/amplify_video_thumb/2100067392223076352/img/BqXd-11SCr3_ff8q.jpg" alt="代码库复杂度分类器" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/ryanvogel/status/2100068006592123055">代码库复杂度分类器</a></b><br><sub>ryanvogel · X · ♥ 1.2k · 2026-09-16</sub><br>让 Jev 评判代码库中代码复杂度的分类器，目的是揪出 agent 常写出的过度工程代码。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://tester.army/e2e"><img src="https://tester.army/e2e/og-image.png" alt="Tester Army e2e" width="240"></a></td>
<td valign="top"><b><a href="https://tester.army/e2e">Tester Army e2e</a></b><br><sub>TesterArmy · 应用 · ♥ 1.1k · 2026-09-18</sub><br>即将开源的 TypeScript 框架，用于由 agent 执行的 Web 和移动应用端到端测试，演示中由 Jev 在每一步选择下一个动作，断言仍写在代码里。<br><sub>相关: <a href="https://x.com/o_kwasniewski/status/2100966838905585687">demo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Yeachan-Heo/oh-my-claudecode/tree/main/src/hooks/jev"><img src="https://repository-images.githubusercontent.com/1130809465/a41c9205-031c-4881-9dbb-2b2a7c4387e6" alt="oh-my-claudecode 的 Jev 判断点" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Yeachan-Heo/oh-my-claudecode/tree/main/src/hooks/jev">oh-my-claudecode 的 Jev 判断点</a></b><br><sub>Yeachan-Heo · GitHub · ⭐ 39.3k 仓库 · 2026-01-09</sub><br>在 oh-my-claudecode 的编排 hook 中设置判断点，由 Jev 决定 skill 触发、循环是否继续、委派任务用哪一档模型、上下文是否过时以及任务规模。<br><sub><b>Jev 用法:</b> 闸门型判断点会等待 Jev 的裁决，检测型判断点在后台完成；建议型判断点只在关闭或影子模式下运行。</sub><br><sub>相关: <a href="https://oh-my-claudecode.dev">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/krzysztof_moch/status/2100513641556549700"><img src="https://pbs.twimg.com/amplify_video_thumb/2100512526303657985/img/-OQ-s3555Nrqr1M9.jpg" alt="Jev QA 测试员" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/krzysztof_moch/status/2100513641556549700">Jev QA 测试员</a></b><br><sub>krzysztof_moch · X · ♥ 781 · 2026-09-17</sub><br>Jev 充当 QA 测试员的演示，由命令行运行器驱动，在模拟器里按测试步骤操作一个 iOS app。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/dani_avila7/status/2101885477158547753"><img src="https://pbs.twimg.com/amplify_video_thumb/2101885207716474880/img/ndbx4dpA8M2NRlsJ.jpg" alt="Claude Code 的 Jev skill 推荐" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/dani_avila7/status/2101885477158547753">Claude Code 的 Jev skill 推荐</a></b><br><sub>dani_avila7 · X · ♥ 713 · 2026-09-21</sub><br>Claude Code 的 mod，把 skill 挡在上下文窗口之外：每个请求都由 Jev 从列表中挑出最匹配的 skill，只注入这一个。<br><sub>相关: <a href="https://aitmpl.com/component/mod/productivity/jev-skill-suggestion">docs</a> · <a href="https://aitmpl.com/component/mod/productivity/jev-skill-suggestion">project</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/can1357/oh-my-pi/blob/main/packages/ai/src/judgment/typesafe.ts"><img src="https://raw.githubusercontent.com/can1357/oh-my-pi/main/assets/hero.png" alt="Oh My Pi 的 Jev 判断" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/can1357/oh-my-pi/blob/main/packages/ai/src/judgment/typesafe.ts">Oh My Pi 的 Jev 判断</a></b><br><sub>can1357 · GitHub · ⭐ 32.4k 仓库 · 2026-09-17</sub><br>编程 agent Oh My Pi 原生的 Jev 判断后端：评测内核里有 judge() 调用，还有一个 jevify 关键字，可批量分类 diff、日志或搜索结果，让 agent 只读被标记的条目。<br><sub><b>Jev 用法:</b> 把判断请求转发到 TypeSafe 的 /v1/systemone 或 OpenRouter 的 Decisions API，两者的请求格式相同。</sub><br><sub>相关: <a href="https://github.com/can1357/oh-my-pi">repo</a> · <a href="https://omp.sh">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/davila7/claude-code-templates/tree/main/cli-tool/components/mods/productivity/jev-skill-suggestion"><img src="https://github.com/user-attachments/assets/d84feaa4-f871-4843-bbee-42d8f51b2f21" alt="Claude Code 的 Jev skill 推荐" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/davila7/claude-code-templates/tree/main/cli-tool/components/mods/productivity/jev-skill-suggestion">Claude Code 的 Jev skill 推荐</a></b><br><sub>davila7 · GitHub · ♥ 76 · 2026-09-19</sub><br>隐藏 skill 列表，让 Jev 为每条提示词最多附加一个 skill。<br><sub>相关: <a href="https://github.com/davila7/claude-code-templates">repo</a> · <a href="https://github.com/davila7/claude-code-templates/tree/main/cli-tool/components/mods/productivity/jev-model-router">model-router</a> · <a href="https://x.com/realfxw/status/2101942956567433395">demo</a> · <a href="https://x.com/shwetabjaj/status/2101917086469759060">demo 2</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/nicobailon/pi-interactive-shell"><img src="https://raw.githubusercontent.com/nicobailon/pi-interactive-shell/main/banner.png" alt="Pi Interactive Shell" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/nicobailon/pi-interactive-shell">Pi Interactive Shell</a></b><br><sub>nicobailon · GitHub · ⭐ 587 · 2026-01-18</sub><br>Pi 编程 agent 扩展，在一个可观察的浮层里自主操作交互式 CLI，并可选用 Jev 对终端输出做语义监督。<br><sub><b>Jev 用法:</b> 默认关闭，要过三道同意关卡才能开启；启用后，Jev 用 jev-1.13.0 评估捕获到的已完成日志块。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/devagrawal09/jev-review"><img src="https://raw.githubusercontent.com/devagrawal09/jev-review/main/docs/dashboard.png" alt="jev-review" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/devagrawal09/jev-review">jev-review</a></b><br><sub>devagrawal09 · GitHub · ⭐ 507 · 2026-09-16</sub><br>分阶段的代码评审：先构建一个 Noul 风险矩阵，再用 Choice 和 Score 对每个问题做画像和评级。<br><sub>相关: <a href="https://x.com/devagrawal09/status/2100341005690298687">demo</a> · <a href="https://www.reddit.com/r/typesafe/comments/1wmb3n3/jevreview_a_staged_code_review_that_keeps_the/">discussion</a> · <a href="https://blink.review">app</a> · <a href="https://blink.review">app 2</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/chddaniel/status/2100919415554617537"><img src="https://pbs.twimg.com/amplify_video_thumb/2100919375989805057/img/-VScsutBqPF0D6Um.jpg" alt="Shipper 网站转应用" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/chddaniel/status/2100919415554617537">Shipper 网站转应用</a></b><br><sub>chddaniel · X · ♥ 408 · 2026-09-18</sub><br>Shipper 里把网站变成应用的功能：Jev 决定如何把粘贴进来的网站重建为原生移动应用，再由 Shipper 提交到各应用商店。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/NiazMorshed2007/jev-review"><img src="https://pbs.twimg.com/amplify_video_thumb/2100465308519759872/img/2uIG43VFGvWzku0s.jpg" alt="Jev 评审 MCP" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/NiazMorshed2007/jev-review">Jev 评审 MCP</a></b><br><sub>NiazMorshed2007 · GitHub · ⭐ 197 · 2026-09-17</sub><br>MCP 服务器，从 19 个质量维度给 agent 的 diff 打分，每个维度都有一个判断是否适用的 Noul、一个 Score 和一个指出主要短板的 Choice。<br><sub>相关: <a href="https://github.com/user-attachments/assets/0ff9f873-0652-4826-af3d-6bb4f42c70b1">video</a> · <a href="https://x.com/niazmorshed_/status/2100465662867218857">demo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/thruwire/foreman"><img src="https://opengraph.githubassets.com/1/thruwire/foreman" alt="Foreman" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/thruwire/foreman">Foreman</a></b><br><sub>thruwire · GitHub · ⭐ 477 · 2026-09-17</sub><br>用十个 Noul 监管 Codex 和 OpenCode 的工人 agent，例如判断某个工人是否卡住或陷入循环。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/marcusquinn/aidevops"><img src="https://raw.githubusercontent.com/marcusquinn/aidevops/main/docs/assets/og-image.png" alt="aidevops" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/marcusquinn/aidevops">aidevops</a></b><br><sub>marcusquinn · GitHub · ⭐ 401 · 2025-11-09</sub><br>OpenCode 插件和 AI DevOps 框架，提供可选开启的 Jev 类型化决策：营销决策批处理、检索和影子分诊试点，以及私有评测报告。<br><sub><b>Jev 用法:</b> 通过 api.typesafe.ai/v1/systemone 针对最小化的 state 提出 Choice、Score 和 Noul 问题，失败时回退到原有的 LLM 路线。</sub><br><sub>相关: <a href="https://github.com/marcusquinn/aidevops/blob/main/.agents/tools/ai-assistants/jev.md">docs</a> · <a href="https://www.aidevops.sh">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/1jehuang/jcode/blob/master/crates/jcode-base/src/jev.rs"><img src="https://opengraph.githubassets.com/1/1jehuang/jcode" alt="jcode 的 Jev 记忆与浏览器交接" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/1jehuang/jcode/blob/master/crates/jcode-base/src/jev.rs">jcode 的 Jev 记忆与浏览器交接</a></b><br><sub>1jehuang · GitHub · ⭐ 20k 仓库 · 2026-01-05</sub><br>jcode 编程 agent harness 用 Jev 判断记忆召回的相关性，并实现快速的浏览器交接：由 Jev 选择每一个可选操作，遇到需要写代码或文字时再交回主 LLM。<br><sub><b>Jev 用法:</b> 记忆召回会把本地记忆分批发送，获取每个候选的相关性概率，阈值为 0.8；浏览器每一步在操作 ID、done、hand_back、script_needed 或 text_needed 中做选择。</sub><br><sub>相关: <a href="https://jcode.sh">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/delexw/claude-code-trace"><img src="https://opengraph.githubassets.com/1/delexw/claude-code-trace" alt="claude-code-trace" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/delexw/claude-code-trace">claude-code-trace</a></b><br><sub>delexw · GitHub · ⭐ 370 · 2026-03-11</sub><br>支持桌面、Web 和 TUI 的 Claude Code 会话日志查看器，用 Jev 给 agent 的进展、工具使用、专注度、探索、恢复能力和 token 效率打分。<br><sub><b>Jev 用法:</b> 针对会话轨迹提出类型化的 Noul 和 Score 问题，其中包括一个衡量思考是否平衡的 Score。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/mohsen1/llm-debugger-vscode-extension"><img src="https://opengraph.githubassets.com/1/mohsen1/llm-debugger-vscode-extension" alt="LLM Debugger" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/mohsen1/llm-debugger-vscode-extension">LLM Debugger</a></b><br><sub>mohsen1 · GitHub · ⭐ 359 · 2025-02-06</sub><br>VS Code 扩展，通过驱动真实的调试器来找 bug：每一步“下一步做什么”由 Jev 回答，只有在提出假设、设置断点、编写表达式和修复时才唤醒生成式模型。<br><sub>相关: <a href="https://github.com/user-attachments/assets/51ccb308-a32c-427c-8767-7952f4caf875">demo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/evotai/evot"><img src="https://opengraph.githubassets.com/1/evotai/evot" alt="evot" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/evotai/evot">evot</a></b><br><sub>evotai · GitHub · ⭐ 328 · 2026-03-09</sub><br>轻量级终端编程 agent，其 Jev 裁剪步骤直接删除过时的上下文而不是对其做摘要，对每个旧的工具调用都问一句任务是否仍依赖它。<br><sub><b>Jev 用法:</b> 每次运行结束后，Jev 先找出哪些请求仍在进行中，再针对每个旧工具调用问两个问题，决定丢弃或截断哪些内容。</sub><br><sub>相关: <a href="https://evot.ai">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/iamaamir/pi-bifrost"><img src="https://raw.githubusercontent.com/iamaamir/pi-bifrost/main/docs/social-card.png" alt="Pi-Bifrost" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/iamaamir/pi-bifrost">Pi-Bifrost</a></b><br><sub>iamaamir · GitHub · ⭐ 53 · 2026-07-25</sub><br>Pi 编程 agent 的模型路由器，按档位和策略为每条提示词选择模型，可选的 TypeSafe/Jev 评判档位负责判断每条提示词的复杂度。<br><sub>相关: <a href="https://iamaamir.github.io/pi-bifrost/">app</a> · <a href="https://www.reddit.com/r/PiCodingAgent/comments/1wlczow/i_think_i_found_the_best_use_case_for_jev_and_pi/">discussion</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://www.youtube.com/watch?v=7w8eRWnUUA8"><img src="https://i.ytimg.com/vi/7w8eRWnUUA8/hqdefault.jpg" alt="herdr 模型路由器" width="240"></a></td>
<td valign="top"><b><a href="https://www.youtube.com/watch?v=7w8eRWnUUA8">herdr 模型路由器</a></b><br><sub>Nidhi Singh · 视频 · ♥ 320 · 2026-09-17</sub><br>一套终端配置：由模型路由 CLI 询问 Jev 每个任务该交给哪个编程 agent（Claude Code、Codex 或 Cursor）、用哪个模型、给多少推理强度。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/gargpratyush/jev-router"><img src="https://raw.githubusercontent.com/gargpratyush/jev-router/master/docs/model-picker.png" alt="jev-router" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/gargpratyush/jev-router">jev-router</a></b><br><sub>gargpratyush · GitHub · ⭐ 318 · 2026-09-16</sub><br>封装 Claude Code 和 Codex，用一个动态构建的 Choice 把每一轮交给能完成它的最便宜模型档位。<br><sub>相关: <a href="https://x.com/PratyushGa39620/status/2100649976422601076">demo</a> · <a href="https://news.ycombinator.com/item?id=49746321">discussion</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/theonedev/onedev/blob/main/server-core/src/main/java/io/onedev/server/web/component/symboltooltip/SymbolTooltipPanel.java"><img src="https://raw.githubusercontent.com/theonedev/onedev/main/doc/images/code-navigation.gif" alt="OneDev 的 Jev 符号跳转" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/theonedev/onedev/blob/main/server-core/src/main/java/io/onedev/server/web/component/symboltooltip/SymbolTooltipPanel.java">OneDev 的 Jev 符号跳转</a></b><br><sub>theonedev · GitHub · ⭐ 15.3k 仓库 · 2018-11-06</sub><br>在 OneDev 的代码导航里，当某个符号有多个可能的定义时，Jev 读取周围的源码、import 和作用域，直接跳到最可能的那个。<br><sub><b>Jev 用法:</b> 以 JSON 形式给出候选定义，用一个 Choice 从中选择，在管理员的 Jev 设置页里配置。</sub><br><sub>相关: <a href="https://onedev.io">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/daniel-farina/nitro"><img src="https://pbs.twimg.com/media/HSrhykQXYAAkMPS.jpg" alt="Nitro" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/daniel-farina/nitro">Nitro</a></b><br><sub>daniel-farina · GitHub · ⭐ 4 · 2026-09-20</sub><br>Grok Build 的一个变体，每轮由 Jev 判断一次这个请求会用到 25 个工具中的哪些，把工具 schema 从约 11K token 压到 2.9K，在相同任务上成本降低 22% 到 40%。<br><sub><b>Jev 用法:</b> 每个工具一个 Noul（完成这个请求是否需要该工具？），全部放在一次约 350 毫秒的请求里。</sub><br><sub>相关: <a href="https://x.com/Daniel_Farinax/status/2101749959980728575">write-up</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/tonhowtf/omniget/blob/main/src-tauri/omniget-core/src/core/llm/prune/jev.rs"><img src="https://raw.githubusercontent.com/tonhowtf/omniget/main/assets/readme/hero.gif" alt="OmniGet 的 Jev 上下文裁剪" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/tonhowtf/omniget/blob/main/src-tauri/omniget-core/src/core/llm/prune/jev.rs">OmniGet 的 Jev 上下文裁剪</a></b><br><sub>tonhowtf · GitHub · ⭐ 14.1k 仓库 · 2026-02-11</sub><br>面向编程 agent 的桌面应用 OmniGet 中可选的上下文裁剪评判器，询问 Jev 每段上下文是否仍然需要，移植自 fast-jev-compaction 和 yoshi。<br><sub><b>Jev 用法:</b> 只用 Noul 问题，每次请求 16 个候选，上限 24,000 字节；默认关闭，选用时会给出隐私提示。</sub><br><sub>相关: <a href="https://tonho.wtf">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/tinacms/tinacms/blob/main/.github/scripts/dedupe-issue.mts"><img src="https://repository-images.githubusercontent.com/198488459/200ad980-a2be-11eb-8762-156abf2914f7" alt="TinaCMS 的 issue 去重器" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/tinacms/tinacms/blob/main/.github/scripts/dedupe-issue.mts">TinaCMS 的 issue 去重器</a></b><br><sub>tinacms · GitHub · ⭐ 13.8k 仓库 · 2019-07-23</sub><br>TinaCMS 仓库中的 GitHub Actions 脚本，用 Jev 把每个新 issue 与所有未关闭的 issue 比对，有把握时就发评论附上原 issue，并加上 Duplicate 标签。<br><sub><b>Jev 用法:</b> 先按页用 Choice 筛出候选，再做 Noul 检查，判定重复的阈值为 0.85，相关 issue 为 0.6。</sub><br><sub>相关: <a href="https://tina.io">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://www.reddit.com/r/PiCodingAgent/comments/1wjqfyo/i_added_jev_as_a_classifier_for_piautomode_faster/"><img src="https://external-preview.redd.it/oIadTIZOORHQiYYTQOvV-0fNYfvTV19bUtu5pvJjAJU.png?auto=webp&amp;s=f4faf66db18e303bfb109025a4638bbc1519e55e" alt="pi-automode" width="240"></a></td>
<td valign="top"><b><a href="https://www.reddit.com/r/PiCodingAgent/comments/1wjqfyo/i_added_jev_as_a_classifier_for_piautomode_faster/">pi-automode</a></b><br><sub>NotTryingToConYou · Reddit · ▲ 91 · 2026-09-18</sub><br>给 pi-automode 加了一个 Jev 分类器后端；pi-automode 是 Pi 编程 agent 上类似 Claude Code 的自动模式，决定哪些操作可以不经询问直接执行。<br><sub>相关: <a href="https://github.com/czottmann/pi-automode">repo</a> · <a href="https://github.com/czottmann/pi-automode/pull/49">pr</a> · <a href="https://github.com/czottmann/pi-automode">project</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/DecapodLabs/decapod"><img src="https://opengraph.githubassets.com/1/DecapodLabs/decapod" alt="Decapod" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/DecapodLabs/decapod">Decapod</a></b><br><sub>DecapodLabs · GitHub · ⭐ 233 · 2026-02-11</sub><br>仓库原生的 AI 编程 agent 治理内核，可选的 Jev provider 会记录 agent 的执行轨迹是否满足既定意图，但只作为观察记录，从不作为批准。<br><sub><b>Jev 用法:</b> 一个 Noul：trajectory_satisfies_intent，结果持久化到轨迹历史中。</sub><br><sub>相关: <a href="https://decapodlabs.github.io/decapod/">docs</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/qf-studio/navigator"><img src="https://opengraph.githubassets.com/1/qf-studio/navigator" alt="Navigator" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/qf-studio/navigator">Navigator</a></b><br><sub>qf-studio · GitHub · ⭐ 232 · 2025-10-10</sub><br>Claude Code 上下文工程插件，在它的循环、复杂度和歧义评分器之后加了一个类型化的 TypeSafe 提示词评判器。<br><sub>相关: <a href="https://github.com/qf-studio/navigator/blob/main/.agent/sops/integrations/typesafe-judge-setup.md">docs</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/morganlinton/Albatross"><img src="https://raw.githubusercontent.com/morganlinton/Albatross/main/docs/assets/demo/agent-session.gif" alt="Albatross" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/morganlinton/Albatross">Albatross</a></b><br><sub>morganlinton · GitHub · ⭐ 230 · 2026-04-25</sub><br>终端编程 agent，把有边界的问题先交给 Jev 处理再轮到主 LLM，只有在有把握时才返回固定的直接答案，提供关闭、影子和启用三种模式。<br><sub>相关: <a href="https://github.com/morganlinton/Albatross/blob/main/docs/JEV_HARNESS.md">docs</a> · <a href="https://albatross.sh">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/vinilana/jev-gateway"><img src="https://raw.githubusercontent.com/vinilana/jev-gateway-bench/main/charts/comparison-light.svg" alt="jev-gateway" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/vinilana/jev-gateway">jev-gateway</a></b><br><sub>vinilana · GitHub · ⭐ 118 · 2026-09-18</sub><br>面向 Codex、Claude Code、OpenCode 和 Gemini 客户端的本地 LLM 网关，把“该调用哪个工具”的决策交给 Jev，其余流量都转发给你平常用的模型。<br><sub>相关: <a href="https://github.com/vinilana/jev-gateway-bench">link</a> · <a href="https://www.youtube.com/watch?v=rtWCFKg7XEs">video</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/coldteadotai/abide"><img src="https://raw.githubusercontent.com/coldteadotai/abide/master/docs/images/abide.png" alt="Abide" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/coldteadotai/abide">Abide</a></b><br><sub>coldteadotai · GitHub · ⭐ 209 · 2026-09-18</sub><br>适用于 Claude Code、Codex 和 OpenCode 的 hook 插件，由 Jev 对照你的 AGENTS.md 和 CLAUDE.md 规则检查 agent 的每一次编辑，每次检查约 300 毫秒，并让 agent 修正违规之处。<br><sub><b>Jev 用法:</b> 回放 93 个真实会话，Jev 标记了 39 次编辑和 15 个轮次；独立评审分别确认了其中 10 次和 11 个。</sub><br><sub>相关: <a href="https://x.com/OhansEmmanuel/status/2101034822760288452">demo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/openchamber/openchamber/blob/main/packages/web/server/lib/routing/jev.js"><img src="https://raw.githubusercontent.com/openchamber/openchamber/main/docs/references/chat_example.png" alt="OpenChamber 的 Jev 路由器" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/openchamber/openchamber/blob/main/packages/web/server/lib/routing/jev.js">OpenChamber 的 Jev 路由器</a></b><br><sub>openchamber · GitHub · ⭐ 10.2k 仓库 · 2026-09-17</sub><br>OpenCode agent 工作区 OpenChamber 中可选的自动模型路由器：Jev 把每条消息归入一个任务类别，每个类别对应一个模型和推理档位，同时它也负责筛查工具权限。<br><sub><b>Jev 用法:</b> 在配置好的路由之间做一个类别 Choice；权限请求会得到一个“是否询问”的 Noul 和一个影响类型的 Choice。</sub><br><sub>相关: <a href="https://github.com/openchamber/openchamber">repo</a> · <a href="https://openchamber.dev/">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/liuyanghejerry/Clausura"><img src="https://opengraph.githubassets.com/1/liuyanghejerry/Clausura" alt="Clausura" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/liuyanghejerry/Clausura">Clausura</a></b><br><sub>liuyanghejerry · GitHub · ⭐ 203 · 2026-05-30</sub><br>CI agent CLI，依据结构化的问题清单决定流水线是否放行，可选的 Jev 校验会在放行判断前逐条询问该问题是否真实、是否有其自身证据支撑。<br><sub><b>Jev 用法:</b> 每个问题一个 Noul；低于阈值的问题不参与放行判断，API 出错时放行。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/sawyerhood/status/2100994779291259187"><img src="https://pbs.twimg.com/amplify_video_thumb/2100990656252661760/img/ceUStNdfX7n8-khU.jpg" alt="自动填好的 agent 输入框" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/sawyerhood/status/2100994779291259187">自动填好的 agent 输入框</a></b><br><sub>sawyerhood · X · ♥ 203 · 2026-09-18</sub><br>一个提示词输入框，让 Jev 为每个请求挑选编程 agent、模型、机器和文件夹，比如大规模重写用 Fable 配 Claude Code，iOS 改动用 Mac。</td>
</tr>
<tr>
<td width="260" valign="top"></td>
<td valign="top"><b><a href="https://www.reddit.com/r/AI_Agents/comments/1wkzjtx/i_tested_jev_as_a_subconscious_helper_for_my_ai/">编程 agent 的潜意识检查</a></b><br><sub>Obvious_Unicorn · Reddit · ▲ 65 · 2026-09-19</sub><br>编程 agent 的辅助工具，由 Jev 折叠通过的测试日志、在约 75 毫秒内拦截破坏性 shell 命令，并为笔记搜索做路由，每天花费不到半美分。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/0xNatoshi/jev-codex-router"><img src="https://pbs.twimg.com/media/HSgeLlIX0AAjedL.png" alt="Jev Codex Router" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/0xNatoshi/jev-codex-router">Jev Codex Router</a></b><br><sub>0xNatoshi · GitHub · ⭐ 185 · 2026-09-17</sub><br>Codex 的逐次调用路由器，由 Jev 为每次模型调用（包括工具续接）选择模型和思考强度；基于历史数据的模拟在 237 轮对话上估算，开销比全程使用 Astra 低约 60%。<br><sub>相关: <a href="https://x.com/antonioleivag/status/2100962426439000484">demo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/marvikomo/code-lens-ai"><img src="https://opengraph.githubassets.com/1/marvikomo/code-lens-ai" alt="code-lens-aI" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/marvikomo/code-lens-ai">code-lens-aI</a></b><br><sub>marvikomo · GitHub · ⭐ 182 · 2025-04-16</sub><br>面向 AI agent 的代码智能 MCP 服务器，基于 Tree-sitter 调用图构建，可选开启 --layers 模式，通过 Jev 给每个文件标注所属的架构层。<br><sub><b>Jev 用法:</b> 每个文件一个 Choice，选项为 api_surface、ui、business_logic、data_access、infrastructure、configuration、utilities、tests 或 unclear，置信度下限 0.6。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/kunchenguid/compact-adviser"><img src="https://raw.githubusercontent.com/kunchenguid/compact-adviser/main/docs/hint-status-line.png" alt="compact-adviser" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/kunchenguid/compact-adviser">compact-adviser</a></b><br><sub>kunchenguid · GitHub · ⭐ 173 · 2026-09-17</sub><br>适用于 Pi、Claude Code、Codex CLI 和 Grok 的插件，询问 Jev 当前工作单元是否已完成、属于动手执行还是协调沟通，然后在安全的边界处提示或触发 /compact。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/kunchenguid/no-mistakes/tree/main/internal/jev"><img src="https://raw.githubusercontent.com/kunchenguid/no-mistakes/main/demo.gif" alt="no-mistakes 的 Jev 审查预简报" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/kunchenguid/no-mistakes/tree/main/internal/jev">no-mistakes 的 Jev 审查预简报</a></b><br><sub>kunchenguid · GitHub · ⭐ 8.6k 仓库 · 2026-04-05</sub><br>no-mistakes push 前审查流水线中的一个可选步骤，用一次批量 Jev 调用排出 AI 审查者应该先读哪些周边文件。<br><sub><b>Jev 用法:</b> 仅作建议：它可以添加阅读建议，但从不移除文件或审查义务，出错时回退为空的预简报；实际调用耗时约 470 毫秒。</sub><br><sub>相关: <a href="https://kunchenguid.github.io/no-mistakes/">docs</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/lakeday-org/perch"><img src="https://opengraph.githubassets.com/1/lakeday-org/perch" alt="perch" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/lakeday-org/perch">perch</a></b><br><sub>lakeday-org · GitHub · ⭐ 168 · 2026-09-16</sub><br>语义代码扫描器，解析方法及其调用图，就范围内的每个方法向 Jev 提带类型的问题，对可能的缺陷和安全问题排序，支持自定义 YAML 规则、agent skill 和 CI 闸门。<br><sub>相关: <a href="https://x.com/joshuafbrown/status/2102085153015451695">demo</a> · <a href="https://perchscan.com">site</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://www.youtube.com/watch?v=WBvmtzkJZsY"><img src="https://i.ytimg.com/vi/WBvmtzkJZsY/hqdefault.jpg" alt="Bambooed" width="240"></a></td>
<td valign="top"><b><a href="https://www.youtube.com/watch?v=WBvmtzkJZsY">Bambooed</a></b><br><sub>AICodeKing · 视频 · ♥ 152 · 2026-09-20</sub><br>演示 Bambooed 中“架构师 + 工人”模式的 AI 编程团队：Astra 架构师负责规划，更便宜的工人模型写代码，可选的 Jev 帮忙挑选工人、检索上下文和审查改动。<br><sub><b>Jev 用法:</b> 工人选择、上下文检索、改动审查和浏览器测试相关的决策。</sub><br><sub>相关: <a href="https://bambooed.ai">app</a> · <a href="https://bambooed.ai">project</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/kunchenguid/firstmate/blob/main/bin/fm-dispatch-resolve.sh"><img src="https://raw.githubusercontent.com/kunchenguid/firstmate/main/assets/banner.png" alt="Firstmate 的 Jev 调度" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/kunchenguid/firstmate/blob/main/bin/fm-dispatch-resolve.sh">Firstmate 的 Jev 调度</a></b><br><sub>kunchenguid · GitHub · ⭐ 6.9k 仓库 · 2026-09-17</sub><br>Firstmate 中可选开启的调度解析器。Firstmate 是并行编程 agent 的团队管理器，这个解析器用一个 Jev Choice 把每份任务简报匹配到某条调度规则，再由本地策略选定 agent 配置。<br><sub><b>Jev 用法:</b> 在所有规则的 when 子句外加一个 none 选项上做一个 Choice；置信度下限、审批和配额随后在 jq 中处理，从不展示给模型。</sub><br><sub>相关: <a href="https://github.com/kunchenguid/firstmate">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/skyfireitdiy/Jarvis"><img src="https://raw.githubusercontent.com/skyfireitdiy/Jarvis/main/docs/images/jarvis-logo.svg" alt="Jarvis" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/skyfireitdiy/Jarvis">Jarvis</a></b><br><sub>skyfireitdiy · GitHub · ⭐ 137 · 2024-12-01</sub><br>协作式 AI 开发平台，可在配置中指定 Jev 作为结构化评估模型，用于在方法论和规则候选之间做选择。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/tamaratran/jev-pruner"><img src="https://i.redd.it/2clt7ycwogqh1.jpeg" alt="jev-pruner" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/tamaratran/jev-pruner">jev-pruner</a></b><br><sub>tamaratran · GitHub · ⭐ 136 · 2026-09-18</sub><br>在大体积 shell 输出进入上下文之前，逐块各用一个 Noul 进行裁剪，原始输出保留在磁盘上。<br><sub>相关: <a href="https://www.reddit.com/r/ClaudeCode/comments/1wkjnrz/instant_claude_code_compaction_is_my_favorite_use/">discussion</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/DevMortimer/pi-warden"><img src="https://raw.githubusercontent.com/DevMortimer/pi-warden/main/docs/preview.png" alt="pi-warden" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/DevMortimer/pi-warden">pi-warden</a></b><br><sub>DevMortimer · GitHub · ⭐ 132 · 2026-09-16</sub><br>Pi 编程 agent 的护栏，每次写入都强制执行项目规则，只拦下难以撤销的操作（真实会话中每 1,000 次调用有 3 次），并能抓出未经验证的“已完成”声明和卡死的循环。<br><sub><b>Jev 用法:</b> Jev 判断是否违反规则、操作是否不可逆以及任务是否跑偏，发现的问题反馈给 agent，而不是打断用户。</sub><br><sub>相关: <a href="https://www.reddit.com/r/PiCodingAgent/comments/1wimfhg/piwarden_a_jevpowered_second_pair_of_eyes_for_pi/">discussion</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/uehaj/jev-semgrep"><img src="https://raw.githubusercontent.com/uehaj/jev-semgrep/main/docs/color.svg" alt="jev-semgrep" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/uehaj/jev-semgrep">jev-semgrep</a></b><br><sub>uehaj · GitHub · ⭐ 125 · 2026-09-19</sub><br>跨语言的语义 grep，支持 AND、OR 和 NOT，每一行问一个 Noul。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/softwarecuddler/status/2100981707105284255"><img src="https://pbs.twimg.com/amplify_video_thumb/2100981261007507456/img/FLs24JzKRsdrrFER.jpg" alt="Supabase RLS 检查器" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/softwarecuddler/status/2100981707105284255">Supabase RLS 检查器</a></b><br><sub>softwarecuddler · X · ♥ 59 · 2026-09-18</sub><br>实验性的 linter，让 Jev 审查 Supabase 行级安全策略并标记问题，还有一个托管的测试页面可以试用。<br><sub>相关: <a href="https://rls-jev-tester.vercel.app/">app</a> · <a href="https://rls-jev-tester.vercel.app">project</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/devagrawal09/stanley-code"><img src="https://opengraph.githubassets.com/1/devagrawal09/stanley-code" alt="Stanley" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/devagrawal09/stanley-code">Stanley</a></b><br><sub>devagrawal09 · GitHub · ⭐ 111 · 2026-09-17</sub><br>用来检查代码改动的编程 CLI，由 Jev 把每条自然语言请求路由到某个确定性工作流，工作流再针对收集到的证据向 Jev 提固定选项问题；没有合适的工作流时回退到 Pi。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/metalbear-co/jev-auto-approve"><img src="https://repository-images.githubusercontent.com/454467716/241fe822-e2b4-4f42-9f1c-871e464e13f3" alt="jev-auto-approve" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/metalbear-co/jev-auto-approve">jev-auto-approve</a></b><br><sub>metalbear-co · GitHub · ⭐ 7 · 2026-09-20</sub><br>GitHub Action，判断一个 pull request 是否需要人工评审，只有当每个问题都以足够置信度越过你设定的阈值时才自动批准，否则指出是哪个问题拦住了跳过评审。<br><sub><b>Jev 用法:</b> 一次调用并行问多个 Noul；校准后的阈值（例如 0.95 对比 0.8）是一个真正可调的旋钮。</sub><br><sub>相关: <a href="https://news.ycombinator.com/item?id=49775144">demo</a> · <a href="https://github.com/metalbear-co/mirrord/blob/main/.github/workflows/jev-auto-approve.yaml">link</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/sonnylazuardi/superterminal"><img src="https://raw.githubusercontent.com/sonnylazuardi/superterminal/main/assets/demo.png" alt="superterminal" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/sonnylazuardi/superterminal">superterminal</a></b><br><sub>sonnylazuardi · GitHub · ⭐ 100 · 2026-08-31</sub><br>GPU 渲染的原生多路复用终端，命令面板用 Jev 理解“kill this tab”这类大白话查询，在停止输入约四分之一秒后对各行排序。<br><sub><b>Jev 用法:</b> 在面板各行之间做一个 Choice；置信度高的选项会移到最上方，而每次按键仍由本地匹配即时响应。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/supercorp-ai/supercov"><img src="https://raw.githubusercontent.com/supercorp-ai/supercov/main/supercov.jpg" alt="Supercov" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/supercorp-ai/supercov">Supercov</a></b><br><sub>supercorp-ai · GitHub · ⭐ 94 · 2026-08-23</sub><br>CLI，告诉编程 agent 该修什么、该测什么：用 Jev 给代码质量属性打分（每 MB 源码约一美分），并把你现有测试命令没覆盖到的路径变成目标。<br><sub>相关: <a href="https://supercov.com">website</a> · <a href="https://www.reddit.com/r/AI_Agents/comments/1wjlac0/jev_to_fix_slop_code/">discussion</a> · <a href="https://www.reddit.com/r/typesafe_ai/comments/1wjlvlx/jev_code_quality_for_codex/">discussion 2</a> · <a href="https://supercov.com">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/LxKus/status/2100611468580323414"><img src="https://pbs.twimg.com/amplify_video_thumb/2100319982433271808/img/Vg2C69AEWtNmsjlL.jpg" alt="Aition 文件过滤" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/LxKus/status/2100611468580323414">Aition 文件过滤</a></b><br><sub>LxKus · X · ♥ 89 · 2026-09-17</sub><br>代码评审工具 Aition 在 Claude 之前放了一层 Jev 来筛选候选文件：发送的文件少 33%，token 少 25%，成本低 23%，给 543 个文件打分只花 $0.037（每个文件 0.38s），召回率没有损失。<br><sub><b>Jev 用法:</b> 在把改动集交给 Claude 之前，先为每个候选文件的相关性打分。</sub><br><sub>相关: <a href="https://aition.app">app</a> · <a href="https://aition.app">project</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/dansyu_callenge/status/2101789813443801556"><img src="https://pbs.twimg.com/media/HSsOrA2a8AAw6WE.jpg" alt="给 Codex 和 Claude Code 用的 Jev 记忆过滤器" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/dansyu_callenge/status/2101789813443801556">给 Codex 和 Claude Code 用的 Jev 记忆过滤器</a></b><br><sub>dansyu_callenge · 文章 · ♥ 84 · 2026-09-20</sub><br>一篇日文文章，介绍用 Jev 把传给 Codex 和 Claude Code 的记忆候选从最多 8 条精简到 3 条（减少 62.5%）的做法，并附有可直接复制粘贴的完整实现提示词。<br><sub><b>Jev 用法:</b> 在每条已存储的记忆或历史对话片段进入编程 agent 上下文之前，先判断它是否相关。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/xcjy8bao/baoer_signal_grep"><img src="https://external-preview.redd.it/u6_hLVhxoVuSTK6uhVkkc4kDWWZo2jZOb13mRX3M6yc.png?auto=webp&amp;s=9cfab12129c0d196dfdd61e39fc3629497543e24" alt="baoer_signal_grep" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/xcjy8bao/baoer_signal_grep">baoer_signal_grep</a></b><br><sub>xcjy8bao · GitHub · ⭐ 82 · 2026-08-27</sub><br>基于 ripgrep 的编程 agent 搜索插件和 MCP 服务器，可选用 Jev 做语义判断，对保留下来的概念候选进行分类，以改进结果排序。<br><sub>相关: <a href="https://www.npmjs.com/package/baoer_signal_grep">npm</a> · <a href="https://www.reddit.com/r/mcp/comments/1wm6x5p/jev_mcp_for_coding_agents_baoer_signal_grep_166/">discussion</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/kirodotdev/KiroCrew/tree/main/src/kiro_crew/decisions"><img src="https://raw.githubusercontent.com/kirodotdev/KiroCrew/main/assets/banner.svg" alt="Kiro Crew 的 Jev 决策点" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/kirodotdev/KiroCrew/tree/main/src/kiro_crew/decisions">Kiro Crew 的 Jev 决策点</a></b><br><sub>kirodotdev · GitHub · ⭐ 4.1k 仓库 · 2026-07-16</sub><br>Kiro Crew 开发工作区中的一系列决策点，由 Jev 的 Choice 挑选 skill、路由模型、评估工具风险、引导消息、召回记忆，并决定压缩时保留哪些内容。<br><sub><b>Jev 用法:</b> 每个答案在使用前都要经过闸门校验，并由闸门提供降级方案；Jev key 只能来自专用的密钥库条目。</sub><br><sub>相关: <a href="https://kiro.dev/crew/">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/duolahypercho/codex-router/blob/main/config/openrouter/decisions/jev-latest.json"><img src="https://opengraph.githubassets.com/1/duolahypercho/codex-router" alt="Codex Router 的 Jev 路由" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/duolahypercho/codex-router/blob/main/config/openrouter/decisions/jev-latest.json">Codex Router 的 Jev 路由</a></b><br><sub>duolahypercho · GitHub · ⭐ 3.8k 仓库 · 2026-07-19</sub><br>Codex Router 为 jev-latest 提供一条不公开列出的 OpenRouter Decisions 路由，它不出现在 Codex 的模型选择器里，专供显式的本地集成使用，比如压缩裁剪器。<br><sub><b>Jev 用法:</b> 使用与对话模型相同的 OpenRouter key，就压缩时保留还是丢弃提出结构化问题，调用 alpha 版 decisions 端点。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/can1357/jegrep"><img src="https://opengraph.githubassets.com/1/can1357/jegrep" alt="jegrep" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/can1357/jegrep">jegrep</a></b><br><sub>can1357 · GitHub · ⭐ 75 · 2026-09-19</sub><br>语义 grep 的 Rust CLI，无需索引，根据大白话描述直接搜索实时的代码树，返回的文件和行范围都带有一个校准过的是/否概率。<br><sub><b>Jev 用法:</b> 每个候选段落都得到一个绝对的 Noul 概率，因此同一个阈值在不同批次间通用；在几千个文件上的一次典型搜索花费 $0.01–0.03。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/f/jev-leftpad"><img src="https://external-preview.redd.it/hT7rDfKqhRRSREfVQDT7VwKY6ZehUiKpPk5n_phMirc.png?auto=webp&amp;s=387f350f2ff68e870a3eb94d3829a97666ee79ba" alt="jev-leftpad" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/f/jev-leftpad">jev-leftpad</a></b><br><sub>f · GitHub · ⭐ 74 · 2026-09-21</sub><br>一个恶搞 npm 包，通过让 Jev 在 space_0 到 space_10 这些选项中做选择来给字符串左侧补空格，每次调用发一次 API 请求，所以最多只能补 10 个空格，而且比 padStart() 还贵。<br><sub>相关: <a href="https://news.ycombinator.com/item?id=49784706">demo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://www.npmjs.com/package/@mizchi/eslint-plugin-jev"><img src="https://pbs.twimg.com/media/HSfSNcab0AAOwet.jpg?name=orig" alt="@mizchi/eslint-plugin-jev" width="240"></a></td>
<td valign="top"><b><a href="https://www.npmjs.com/package/@mizchi/eslint-plugin-jev">@mizchi/eslint-plugin-jev</a></b><br><sub>mizchi · 软件包 · ♥ 70 · 2026-09-18</sub><br>实验性 ESLint 插件，由 Jev 给出判定：可以用一个节点选择器加一句自然语言写成一条规则，也可以拿到每个函数在 八类具名缺陷上的得分。<br><sub><b>Jev 用法:</b> 文件中的所有函数在一次批量请求里完成判断。</sub><br><sub>相关: <a href="https://github.com/mizchi/jev-playground/tree/main/experiments/eslint-plugin-jev">repo</a> · <a href="https://x.com/mizchi/status/2100879638008594513">demo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/mizchi/jev-lint"><img src="https://opengraph.githubassets.com/1/mizchi/jev-lint" alt="jev-lint" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/mizchi/jev-lint">jev-lint</a></b><br><sub>mizchi · GitHub · ⭐ 69 · 2026-09-19</sub><br>每条规则就是一句话的 linter：ast-grep 选出要检查的代码，Jev 针对每处匹配给这句话打分，能抓出注释承诺的行为而函数体并未实现之类的偏差。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/fstandhartinger/chat-seek-vscode"><img src="https://raw.githubusercontent.com/fstandhartinger/chat-seek-vscode/main/media/demo.gif" alt="Chat Seek" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/fstandhartinger/chat-seek-vscode">Chat Seek</a></b><br><sub>fstandhartinger · GitHub · ⭐ 64 · 2026-09-21</sub><br>VS Code 扩展，根据一段大白话描述找回过去的 Claude Code、Codex 和 OpenCode 对话，并用开放的 Laya 决策模型对本地匹配结果重排。<br><sub><b>Jev 用法:</b> 使用在本地运行的开放 Jev 兼容模型 Laya 做重排。</sub><br><sub>相关: <a href="https://x.com/airesearch12/status/2101931275846099315">demo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/nidhi-singh02/agent-router"><img src="https://opengraph.githubassets.com/1/nidhi-singh02/agent-router" alt="agent-router" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/nidhi-singh02/agent-router">agent-router</a></b><br><sub>nidhi-singh02 · GitHub · ⭐ 63 · 2026-09-17</sub><br>一个 CLI：先按配额规则筛选你订阅的编程 agent，再让 Jev 给符合条件的 agent 和模型排序并选定推理强度，然后在 Herdr 面板中启动 Cursor、Claude Code、Codex 或 OpenCode。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/tuxevil/tuxevil-rotator"><img src="https://raw.githubusercontent.com/tuxevil/tuxevil-rotator/main/tuxevil-rotator_logo.png" alt="tuxevil-rotator" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/tuxevil/tuxevil-rotator">tuxevil-rotator</a></b><br><sub>tuxevil · GitHub · ⭐ 63 · 2026-04-22</sub><br>OpenAI 兼容网关，为编程 agent 轮换使用免费档 LLM 账号，模型设为“auto”时可以用 Jev 挑选当前可路由的模型，并有确定性的放行式回退。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/IAmUnbounded/save-token-jev-clean"><img src="https://opengraph.githubassets.com/1/IAmUnbounded/save-token-jev-clean" alt="save-token-jev" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/IAmUnbounded/save-token-jev-clean">save-token-jev</a></b><br><sub>IAmUnbounded · GitHub · ⭐ 62 · 2026-09-18</sub><br>编程 agent 的可移植上下文压缩：由 Jev 决定哪些工具调用完整保留、保留但限制结果长度，或直接丢弃，提供 Codex、OpenCode、Claude Code 和原始对话记录的适配器。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/QAInsights/jmeter-ai"><img src="https://raw.githubusercontent.com/QAInsights/jmeter-ai/main/images/feather-wand.png" alt="Feather Wand" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/QAInsights/jmeter-ai">Feather Wand</a></b><br><sub>QAInsights · GitHub · ⭐ 60 · 2025-02-24</sub><br>Apache JMeter 的 AI agent 插件，其可选的 Jev Smart Routing 会对每个请求的意图分类，为 Agent Mode 提供一个聚焦的工具包，并显示路由卡片，必要时回退到完整工具集。<br><sub>相关: <a href="https://jmeter.ai">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/GhalebDweikat/winnow"><img src="https://opengraph.githubassets.com/1/GhalebDweikat/winnow" alt="winnow" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/GhalebDweikat/winnow">winnow</a></b><br><sub>GhalebDweikat · GitHub · ⭐ 56 · 2026-09-16</sub><br>Claude Code 的上下文筛子，评判每个大的 Read、Bash 或 Grep 结果，把有把握确定你用不上的块换成三行占位，需要时再恢复全文。<br><sub><b>Jev 用法:</b> 每个块一个是非 Noul（当前任务是否需要它？）；拿不准的块会保留。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/wobsoriano/oxlint-plugin-jev"><img src="https://opengraph.githubassets.com/1/wobsoriano/oxlint-plugin-jev" alt="oxlint-plugin-jev" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/wobsoriano/oxlint-plugin-jev">oxlint-plugin-jev</a></b><br><sub>wobsoriano · GitHub · ⭐ 55 · 2026-09-19</sub><br>实验性的 Oxlint 插件，规则是针对函数、调用、JSX 元素或文件的英文是非题，Jev 给出的“是”概率超过你设的阈值时就报告匹配。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/yuzushi-dev/Sando"><img src="https://raw.githubusercontent.com/yuzushi-dev/Sando/main/assets/sando-mark.png" alt="Sando" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/yuzushi-dev/Sando">Sando</a></b><br><sub>yuzushi-dev · GitHub · ⭐ 54 · 2026-08-23</sub><br>面向 Claude Code 和 Codex 的本地上下文管理插件，给过大的工具输出设上限，另有一个可选的 TypeSafe 影子评判器，只做度量，从不改动请求。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/ellipsis-dev/blink"><img src="https://opengraph.githubassets.com/1/ellipsis-dev/blink" alt="blink" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/ellipsis-dev/blink">blink</a></b><br><sub>ellipsis-dev · GitHub · ⭐ 53 · 2026-09-16</sub><br>代码库搜索 CLI，根据自然语言查询找文件：把一组 walker 沿目录树往下派，由 Jev 给文件名和文件夹名打分。<br><sub><b>Jev 用法:</b> Jev 在每一层给名称打分；概率越高的路径分到越多 walker，结果会报告最终落在该处的 walker 占比。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://www.youtube.com/watch?v=goVDTUd7-J0"><img src="https://i.ytimg.com/vi/goVDTUd7-J0/hqdefault.jpg" alt="Jev Realtime Code Check" width="240"></a></td>
<td valign="top"><b><a href="https://www.youtube.com/watch?v=goVDTUd7-J0">Jev Realtime Code Check</a></b><br><sub>Patrick Desjardins · 视频 · ♥ 43 · 2026-09-17</sub><br>一段简短演示：一个 VS Code 和 Cursor 扩展在每次保存时，用 Jev 对照 370 条 Markdown 编码规则检查本地 Git 改动，耗时不到 2 秒。<br><sub><b>Jev 用法:</b> 针对改动的代码，每条适用的规则做一次判断。</sub><br><sub>相关: <a href="https://github.com/MrDesjardins/jevrealtimecodecheck">repo</a> · <a href="https://patrickdesjardins.com/blog/typesafe-ai-jev-running-370-text-rules-under-2-seconds">article</a> · <a href="https://github.com/mrdesjardins/jevrealtimecodecheck">project</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/nahid-sparktales/agent-dispatcher"><img src="https://i.redd.it/f3il3qf2wiqh1.png" alt="agent-dispatcher" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/nahid-sparktales/agent-dispatcher">agent-dispatcher</a></b><br><sub>nahid-sparktales · GitHub · ⭐ 46 · 2026-09-19</sub><br>Claude Code 和 Codex 的调度器，把每个请求路由到 27 个专家角色之一，并配上相应的 skill、工具和有界的上下文包；可选开启的 Jev 引擎能从目录中挑选角色、skill 和工具。<br><sub><b>Jev 用法:</b> 所有 Jev 功能默认关闭；开启后由 Jev 在目录中的角色、skill 和工具之间做选择，失败时回退到编程 agent 自身的路由。</sub><br><sub>相关: <a href="https://www.reddit.com/r/ClaudeAI/comments/1wku51x/agent_dispatcher_automatically_routes_tasks_to/">demo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/EliaAlberti/jev-rules"><img src="https://raw.githubusercontent.com/EliaAlberti/jev-rules/main/social/jev-rules-demo.gif" alt="jev-rules" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/EliaAlberti/jev-rules">jev-rules</a></b><br><sub>EliaAlberti · GitHub · ⭐ 46 · 2026-09-18</sub><br>Claude Code 插件，针对每条常驻规则向 Jev 问一个是/否问题，即当前请求是否与它有关，只把匹配的规则和地图文档传给 Claude，耗时远不到一秒。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/nassim-arifette/jevgrep"><img src="https://raw.githubusercontent.com/nassim-arifette/jevgrep/main/docs/assets/jevgrep-cli-demo.gif" alt="JevGrep" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/nassim-arifette/jevgrep">JevGrep</a></b><br><sub>nassim-arifette · GitHub · ⭐ 45 · 2026-09-20</sub><br>面向编程 agent 的语义代码搜索，可通过 CLI 或 MCP 使用：问某个行为在哪里处理，就能得到带路径和行号的源码原文片段。<br><sub><b>Jev 用法:</b> Jev 针对问题给授权仓库中每个符合条件的代码片段打分。</sub><br><sub>相关: <a href="https://www.reddit.com/r/typesafe_ai/comments/1wlf4v0/we_built_a_smart_grep_using_jev/">demo</a> · <a href="https://www.reddit.com/r/codex/comments/1wlfdu5/i_built_a_jevpowered_mcp_tool_that_gives_codex/">discussion</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/TannerMidd/specpi-jev-guard"><img src="https://raw.githubusercontent.com/TannerMidd/specpi-jev-guard/main/docs/assets/terminal.png" alt="specpi-jev-guard" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/TannerMidd/specpi-jev-guard">specpi-jev-guard</a></b><br><sub>TannerMidd · GitHub · ⭐ 9 · 2026-09-18</sub><br>Pi 扩展，在 agent 执行有风险的 shell 和文件命令前做检查：明显的情况由本地规则在 0 毫秒内定夺，其余交给 Jev 打分，高分直接拦截，中间区间则询问用户。<br><sub><b>Jev 用法:</b> 经 OpenRouter 获取一个危险程度 Score；没有 key、没有网络或答案无法解析时，命令不会执行。</sub><br><sub>相关: <a href="https://www.reddit.com/r/PiCodingAgent/comments/1wllcjy/a_jev_pi_guard_that_checks_risky_shell_commands/">discussion</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/coder/xum/blob/main/src/constants/autoModelRouting.ts"><img src="https://raw.githubusercontent.com/coder/xum/main/docs/img/black-xum.svg" alt="Xum 的自动模型路由" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/coder/xum/blob/main/src/constants/autoModelRouting.ts">Xum 的自动模型路由</a></b><br><sub>coder · GitHub · ⭐ 2k 仓库 · 2025-09-17</sub><br>桌面编程 agent 多路复用器 Xum 会把每条 Auto 模式的提示词发给评测模型，做一次难度档位选择，再用该档位对应的模型和思考档位运行这一轮。<br><sub><b>Jev 用法:</b> TypeSafe 是默认的评测 provider，经 AI SDK 的 experimental_evaluate 调用；它不提供聊天模型，也从不出现在模型列表里。</sub><br><sub>相关: <a href="https://xum.coder.com">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/whosfranki/status/2102195316829077686"><img src="https://pbs.twimg.com/amplify_video_thumb/2102187393717534721/img/FmGLzXqEYRdC2RGo.jpg" alt="matchcn" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/whosfranki/status/2102195316829077686">matchcn</a></b><br><sub>whosfranki · X · ♥ 38 · 2026-09-22</sub><br>面向编程 agent 的语义组件搜索：描述你需要的 UI，它就从 9 个 shadcn registry 的 1,783 个组件中返回匹配的组件和安装命令。<br><sub><b>Jev 用法:</b> 按六个维度（用途、动效、密度、交互、数据、装饰）给每个组件分类，并在匹配打分时用上置信度。</sub><br><sub>相关: <a href="https://matchcn.dev">app</a> · <a href="https://github.com/francesco0242/matchcn">repo</a> · <a href="https://matchcn.dev">project</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/pedrocivita/tocket"><img src="https://raw.githubusercontent.com/pedrocivita/tocket/main/docs/assets/tocket-dashboard.png" alt="Tocket" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/pedrocivita/tocket">Tocket</a></b><br><sub>pedrocivita · GitHub · ⭐ 38 · 2026-02-24</sub><br>以文件为先的项目笔记本，供多个编程 agent 读写；Jev 只负责在选项中挑出下一步，并在 bash、部署或浏览器操作前记录一个 tool_gate 的 allow/block/ask 决定。<br><sub><b>Jev 用法:</b> tocket decide 让 Jev 在选项中做选择，把结果以 JSON 写入 .context/decisions/，tocket work --apply 会照此执行。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/kylejeong/status/2100827289349132657"><img src="https://pbs.twimg.com/amplify_video_thumb/2100827022121713664/img/Bw1G6-A6AyFgOiAD.jpg" alt="带 Jev 记忆压缩的 Nanocode" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/kylejeong/status/2100827289349132657">带 Jev 记忆压缩的 Nanocode</a></b><br><sub>kylejeong · X · ♥ 37 · 2026-09-18</sub><br>nanocode agent 的一个 fork，加了在 memory.md 文件里 grep 的工具，以及用 Jev 删掉多余记忆的压缩功能。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://www.reddit.com/r/accelerate/comments/1wikbwy/jev_solved_local_harnessmodel_routing_i_use_a/"><img src="https://external-preview.redd.it/dXkzdGpxcGFoMHFoMQT370rF_YDmIyi8Xq8HNsDeNrIMDtcsN2uV_Ls25aWJ.png?format=pjpg&amp;auto=webp&amp;s=77fca586f4f9d64d4c03952a95b88ae5abb56ef7" alt="本地 harness 与模型路由" width="240"></a></td>
<td valign="top"><b><a href="https://www.reddit.com/r/accelerate/comments/1wikbwy/jev_solved_local_harnessmodel_routing_i_use_a/">本地 harness 与模型路由</a></b><br><sub>stealthispost · Reddit · ▲ 12 · 2026-09-17</sub><br>Claude Code hook，在委派前让 Jev 给每个任务选路：机械性工作交给 Haiku，较难的交给 Opus 子 agent，长时间的实现任务交给 Codex 或 OpenCode。<br><sub><b>Jev 用法:</b> 用一个在各 harness/模型目标之间选择的 Choice 来判定任务复杂度。</sub><br><sub>相关: <a href="https://x.com/mdlahfir/status/2100314182201802811">demo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/prateekkathal/status/2101084515942965590"><img src="https://pbs.twimg.com/media/HSiM9l8bIAA8Hjj.png?name=orig" alt="Claude Code 提示词打分器" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/prateekkathal/status/2101084515942965590">Claude Code 提示词打分器</a></b><br><sub>prateekkathal · X · ♥ 6 · 2026-09-18</sub><br>Claude Code 插件，用 Jev 给你向编程 agent 写提示词的水平打分，且不增加延迟。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Alurith/jeff"><img src="https://opengraph.githubassets.com/1/Alurith/jeff" alt="jeff" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Alurith/jeff">jeff</a></b><br><sub>Alurith · GitHub · ⭐ 35 · 2026-09-18</sub><br>只读的 Go CLI，按你自己定的规则（例如隐藏的副作用或薄弱的错误处理）检查文件，由 Jev 对每个文件做语义判断，可在本地或 CI 中运行。<br><sub>相关: <a href="https://news.ycombinator.com/item?id=49757757">discussion</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/burnigtm/jev-mcp"><img src="https://opengraph.githubassets.com/1/burnigtm/jev-mcp" alt="jev-mcp" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/burnigtm/jev-mcp">jev-mcp</a></b><br><sub>burnigtm · GitHub · ⭐ 35 · 2026-09-17</sub><br>本地 stdio MCP 服务器，把 Jev 放进 Cursor、Codex 等 MCP 客户端的编程循环，提供的工具可以路由下一步、挑选预备好的工具调用、审查补丁、核实说法和筛查内容。<br><sub>相关: <a href="https://x.com/cu30rry_/status/2101108510511530164">demo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/devanshbatham/commit-miner"><img src="https://opengraph.githubassets.com/1/devanshbatham/commit-miner" alt="commit-miner" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/devanshbatham/commit-miner">commit-miner</a></b><br><sub>devanshbatham · GitHub · ⭐ 33 · 2026-09-17</sub><br>Rust CLI，把 Git 提交信息和 diff 分类为 bug 修复、带 CWE ID 的安全修复以及各种改动类型，并生成 HTML 或 CSV 报告。<br><sub><b>Jev 用法:</b> 每个提交提出固定类别的 Choice 和 Noul 问题，最多 8 个 worker 并行运行。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/TheoOliveira/pi-jev"><img src="https://opengraph.githubassets.com/1/TheoOliveira/pi-jev" alt="pi-jev" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/TheoOliveira/pi-jev">pi-jev</a></b><br><sub>TheoOliveira · GitHub · ⭐ 32 · 2026-09-17</sub><br>Pi 编程 agent 扩展，用 Jev 只激活提示词需要的工具、推荐匹配的 SKILL.md skill，并在 agent 内部运行带类型的 Choice、Noul 和 Score 判断。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/nicobailon/pi-mcp-adapter/blob/main/jev-client.ts"><img src="https://raw.githubusercontent.com/nicobailon/pi-mcp-adapter/main/banner.png" alt="Pi MCP Adapter 的 Jev 搜索" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/nicobailon/pi-mcp-adapter/blob/main/jev-client.ts">Pi MCP Adapter 的 Jev 搜索</a></b><br><sub>nicobailon · GitHub · ⭐ 1.5k 仓库 · 2026-01-19</sub><br>面向 Pi 编程 agent、节省 token 的 MCP 适配器中的可选 Jev 层，在显式语义搜索时对所有已启用服务器上的 MCP 工具排序，还能在白名单控制下评估工具结果。<br><sub>相关: <a href="https://github.com/nicobailon/pi-mcp-adapter">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/fujibee/agmsg/tree/main/scripts/drivers/ext-tools/jev"><img src="https://raw.githubusercontent.com/fujibee/agmsg/main/docs/agmsg-demo.gif" alt="agmsg 的 jev 工具" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/fujibee/agmsg/tree/main/scripts/drivers/ext-tools/jev">agmsg 的 jev 工具</a></b><br><sub>fujibee · GitHub · ⭐ 1.5k 仓库 · 2026-04-02</sub><br>agmsg 中的外部工具驱动。agmsg 是面向 CLI 编程 agent 的跨厂商消息层，这个驱动让某个席位可以就一段 state 向 Jev 提出类型化问题，作为决策辅助。<br><sub><b>Jev 用法:</b> 鼓励通过推测式扇出把多个问题打包进一次调用；调用之间没有记忆，也没有副作用。</sub><br><sub>相关: <a href="https://www.producthunt.com/products/agmsg">demo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/win4r/jev-skill-suggester"><img src="https://opengraph.githubassets.com/1/win4r/jev-skill-suggester" alt="Jev Skill Suggester" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/win4r/jev-skill-suggester">Jev Skill Suggester</a></b><br><sub>win4r · GitHub · ⭐ 30 · 2026-09-19</sub><br>Codex skill 和只用标准库的 Python CLI，依据 skill 的描述和片段，用 Jev 的 Choice 和 Noul 检查为当前任务推荐一个已安装的 skill，答案也可以是“不用 skill”或“不确定”。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/qkal/Canny"><img src="https://opengraph.githubassets.com/1/qkal/Canny" alt="Canny" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/qkal/Canny">Canny</a></b><br><sub>qkal · GitHub · ⭐ 29 · 2026-09-11</sub><br>Claude Code 和 Codex CLI 的 hook，维护一份只追加的编辑与检查台账，如果自上次代码编辑以来没有任何检查通过，就拒绝接受“已完成”的说法。<br><sub><b>Jev 用法:</b> 由确定性 hook 做决定；可选的 Jev Noul 判断只提供建议性信号。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/remorses/kimaki/tree/main/opencode-auto-mode"><img src="https://opengraph.githubassets.com/1/remorses/kimaki" alt="kimaki 的 opencode 自动模式" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/remorses/kimaki/tree/main/opencode-auto-mode">kimaki 的 opencode 自动模式</a></b><br><sub>remorses · GitHub · ⭐ 1.4k 仓库 · 2025-09-02</sub><br>kimaki 是一个基于 Discord 的 OpenCode 编排器，其中的 opencode-auto-mode 插件运行一个默认全拒绝的旁路会话分类器，用 Jev 决定自动模式下的每一轮。<br><sub><b>Jev 用法:</b> 通过 AI SDK 的 evaluate 调用 typesafe-ai/jev，与放行概率阈值比较，配置无效时一律拒绝。</sub><br><sub>相关: <a href="https://kimaki.dev">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/sharziki/semdecide"><img src="https://opengraph.githubassets.com/1/sharziki/semdecide" alt="SemDecide" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/sharziki/semdecide">SemDecide</a></b><br><sub>sharziki · GitHub · ⭐ 28 · 2026-09-16</sub><br>Python CLI，在 Unix 管道和 CI 里充当按语义匹配的 grep：输入文本或 JSONL，得到由 Jev 支撑的谓词判断、路由、评分、过滤后的数据流和稳定的退出码。<br><sub><b>Jev 用法:</b> 在本地对 Jev 的答案套用概率阈值，决定输出和退出码。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/memorax-ai/memorax-code/tree/main/packages/ts/memorax-code-backend/src/provider/jev"><img src="https://raw.githubusercontent.com/memorax-ai/memorax-code/main/docs/assets/memorax-code-lockup-light.svg" alt="Memorax Code 的 Jev 门控" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/memorax-ai/memorax-code/tree/main/packages/ts/memorax-code-backend/src/provider/jev">Memorax Code 的 Jev 门控</a></b><br><sub>memorax-ai · GitHub · ⭐ 1.4k 仓库 · 2026-08-01</sub><br>面向 AI 编程的记忆插件，用 Jev 判断当前提示词是否值得做一次记忆搜索，只在可能有帮助时才检索。<br><sub><b>Jev 用法:</b> 由 jev-1.13.0 给出带概率的“搜索还是跳过”决定，设 2 秒超时并限制输入大小。</sub><br><sub>相关: <a href="https://code.memorax.net/">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/boozedog/pi-codemode"><img src="https://opengraph.githubassets.com/1/boozedog/pi-codemode" alt="Pi Codemode" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/boozedog/pi-codemode">Pi Codemode</a></b><br><sub>boozedog · GitHub · ⭐ 27 · 2026-05-08</sub><br>Pi 扩展，把许多零碎的工具调用换成一个在沙箱中运行、经过类型检查的 TypeScript 程序；设置 TypeSafe key 后，程序可以调用 jev.ask 获取 Noul、Choice 和 Score 答案，并在代码里组合阈值。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/caliber-ai-org/ai-setup/tree/master/plugin/caliber-jev-compaction"><img src="https://repository-images.githubusercontent.com/1178198291/70be5bf9-076a-49fc-aaa7-07cdab8ee077" alt="caliber-jev-compaction" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/caliber-ai-org/ai-setup/tree/master/plugin/caliber-jev-compaction">caliber-jev-compaction</a></b><br><sub>caliber-ai-org · GitHub · ⭐ 1.3k 仓库 · 2026-03-10</sub><br>随 Caliber 发布的 Claude Code 函数 hook 插件，用 Jev 决策取代内置的上下文压缩，以未打包的 TypeScript 形式从磁盘加载。<br><sub><b>Jev 用法:</b> 自带 key（BYOK）的 apiKey 或 gatewayApiKey；压缩 hook 询问 Jev 该保留哪些上下文。</sub><br><sub>相关: <a href="https://trycaliber.ai">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/devtooligan/jevscan-evm"><img src="https://opengraph.githubassets.com/1/devtooligan/jevscan-evm" alt="jevscan-evm" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/devtooligan/jevscan-evm">jevscan-evm</a></b><br><sub>devtooligan · GitHub · ⭐ 25 · 2026-09-19</sub><br>概念验证性质的扫描器，为 EVM 智能合约代码生成一张疑似 bug 的热力图，向 Jev 提出两个通用问题、14 个类别问题和 343 个检测器问题，均取自审计检查清单。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/francesco0242/matchcn"><img src="https://opengraph.githubassets.com/1/francesco0242/matchcn" alt="matchcn" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/francesco0242/matchcn">matchcn</a></b><br><sub>francesco0242 · GitHub · ⭐ 25 · 2026-09-20</sub><br>给 shadcn 格式 registry 里 1,783 个组件建立的语义索引，提供 MCP 工具 pick_component，让开发者和编程 agent 按功能找组件；打标签和需求描述解析都通过 classifier.dev 调用 Jev 完成。<br><sub><b>Jev 用法:</b> 每个组件和每份需求描述都按六个标签维度打标，在代码里按各标签的置信度加权排序；最后一次调用负责裁定难分高下的情况，或回答“没有匹配”。</sub></td>
</tr>
<tr>
<td width="260" valign="top"></td>
<td valign="top"><b><a href="https://www.reddit.com/r/LLMDevs/comments/1wkjufw/tried_using_jev_for_prompt_observability_and_llm/">prompt-oscilloscope</a></b><br><sub>Virtual-Astronaut707 · Reddit · ▲ 8 · 2026-09-19</sub><br>两个实验：一个终端客户端，在提示词送进 GitHub Copilot CLI 之前先用 Jev 检查；一个 PR 审查器，在生成式审查之前用 Jev 精简 diff。<br><sub><b>Jev 用法:</b> 有歧义、自相矛盾或有风险的提示词需要再按一次 Enter；按每个 hunk 算出的“有可操作发现”概率决定是否交给审查器。</sub><br><sub>相关: <a href="https://github.com/shubhangi013/prompt-oscilloscope">repo</a> · <a href="https://github.com/shubhangi013/prune-review">repo2</a> · <a href="https://github.com/shubhangi013/prompt-oscilloscope">project</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/safzanpirani/pi-jev-skill-picker"><img src="https://opengraph.githubassets.com/1/safzanpirani/pi-jev-skill-picker" alt="pi-jev-skill-picker" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/safzanpirani/pi-jev-skill-picker">pi-jev-skill-picker</a></b><br><sub>safzanpirani · GitHub · ⭐ 23 · 2026-09-20</sub><br>Pi 扩展，把系统提示词里约 19,000 token 的 skill 目录移除，改为提供 skill_search 工具，由 Jev 对照任务给每个已启用的 skill 打分，返回匹配的 SKILL.md 文件。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/lomeshdutta/skill-router"><img src="https://pbs.twimg.com/amplify_video_thumb/2100829690625986560/img/wb4qnROl6fZfpHUS.jpg" alt="skill-router" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/lomeshdutta/skill-router">skill-router</a></b><br><sub>lomeshdutta · GitHub · ⭐ 2 · 2026-09-18</sub><br>Claude Code 的命令行工具，用 Jev 判断某个会话需要哪个已安装的 skill，并去 skills.sh 查找你还没装的 skill。<br><sub>相关: <a href="https://x.com/lomeshdutta/status/2100833655518367871">demo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/hussi9/skill-router"><img src="https://opengraph.githubassets.com/1/hussi9/skill-router" alt="skill-router" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/hussi9/skill-router">skill-router</a></b><br><sub>hussi9 · GitHub · ⭐ 23 · 2026-04-13</sub><br>由 hook 驱动的 Claude Code 路由器，在任何工具触发之前选好 skill、agent、模型和思考深度，由 Jev 在整个 skill 索引上做选择；在它的评测中，Jev 正确路由了 39/63 条提示词，旧流水线为 10/66。<br><sub><b>Jev 用法:</b> 在完整索引上提两个 Choice 问题，耗时约 0.4 秒；置信度 &gt;= 0.8 时才路由（34 次中 32 次正确），1.2 秒超时则回退。</sub><br><sub>相关: <a href="https://github.com/hussi9/skill-router/blob/main/docs/jev-eval-2026-09-21/RESULTS.md">eval</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/jstxn/agentdir"><img src="https://raw.githubusercontent.com/jstxn/agentdir/main/docs/assets/agentdir-agent-trace-demo.gif" alt="AgentDir" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/jstxn/agentdir">AgentDir</a></b><br><sub>jstxn · GitHub · ⭐ 22 · 2026-05-08</sub><br>本地优先的编程 agent 飞行记录仪，可记录、回放和审计软件任务；可选开启的 Jev 记忆重排器会在上下文交回 agent 之前，对已脱敏的内容进行筛选。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/jomatsu/pi-jev-auto-mode"><img src="https://media2.dev.to/dynamic/image/width=1200,height=627,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Farticles%2Fz2dfgjjjyn66tgl1f07a.png" alt="pi-jev-auto-mode" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/jomatsu/pi-jev-auto-mode">pi-jev-auto-mode</a></b><br><sub>jomatsu · GitHub · ⭐ 22 · 2026-09-17</sub><br>Pi 编程 agent 的自动模式，先过确定性的拒绝规则，再自动批准 bash、write 和 edit 工具调用，语义判断交给 Jev，拿不准时拒绝执行。<br><sub><b>Jev 用法:</b> Jev 只对规则层放过的调用判断授权和风险，每条规则的阈值都在真实 API 上校准过。</sub><br><sub>相关: <a href="https://news.ycombinator.com/item?id=49745284">discussion</a> · <a href="https://dev.to/jomatsu/jev-pi-a-probability-gate-for-my-coding-agents-shell-commands-95d">write-up</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/compozy/yoshi"><img src="https://raw.githubusercontent.com/compozy/yoshi/main/docs/assets/benchmarks/summary.png" alt="Yoshi" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/compozy/yoshi">Yoshi</a></b><br><sub>compozy · GitHub · ⭐ 22 · 2026-09-18</sub><br>面向 Claude Code 和 Codex 的概念验证本地代理：超过一定大小后由 Jev 判断哪些对话历史仍然需要，Yoshi 丢弃其余部分，同时保持工具协议完整。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/MayDay-wpf/snow-cli/blob/main/source/api/decisionModel.ts"><img src="https://raw.githubusercontent.com/MayDay-wpf/snow-cli/main/docs/images/bloome-home.png" alt="snow-cli 的决策模型" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/MayDay-wpf/snow-cli/blob/main/source/api/decisionModel.ts">snow-cli 的决策模型</a></b><br><sub>MayDay-wpf · GitHub · ⭐ 1.1k 仓库 · 2025-08-16</sub><br>为终端编程 agent snow-cli 加入 TypeSafe Jev 决策模型客户端，在代码库 agent 审查中判断每条搜索结果是否与查询相关。<br><sub><b>Jev 用法:</b> 一个 choice 问题，其裁决直接作为审查结论，不需要再用 LLM 复核。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/wk42worldworld/cybercode/blob/main/src/services/fastJudgment/service.ts"><img src="https://raw.githubusercontent.com/wk42worldworld/cybercode/main/docs/images/cybercode-wordmark.png" alt="CyberCode Fast Judgment" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/wk42worldworld/cybercode/blob/main/src/services/fastJudgment/service.ts">CyberCode Fast Judgment</a></b><br><sub>wk42worldworld · GitHub · ⭐ 1k 仓库 · 2026-04-29</sub><br>CyberCode 是一个把 Claude Code 与 Hermes 自我进化结合起来的 agent，它新增了由 Jev 支撑的 Fast Judgment 服务，用于快速分类和浏览器决策。<br><sub><b>Jev 用法:</b> 通过 api.typesafe.ai（jev-latest）提出 Choice 问题并获取概率和置信度，带缓存、降级方案和较短的超时。</sub><br><sub>相关: <a href="https://wk42worldworld.github.io/cybercode/">docs</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/rhighs/jev-code"><img src="https://raw.githubusercontent.com/rhighs/jev-code/main/assets/jev-code-logo.png" alt="jev-code" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/rhighs/jev-code">jev-code</a></b><br><sub>rhighs · GitHub · ⭐ 20 · 2026-09-17</sub><br>编程 CLI 和 TypeScript SDK：Jev 通过选择 AST 产生式，一次一条语法规则地写出 Python 或 Bash 程序，然后回读、修复、运行并汇报结果。<br><sub><b>Jev 用法:</b> Jev 只从有界的语法和动作列表中选一个选项；库本身提供决策会话、类型化路由器和有界的语法树构建。</sub><br><sub>相关: <a href="https://www.reddit.com/r/typesafe/comments/1wk0b00/i_made_jev_write_code_and_commands/">discussion</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/CelestoAI/celesto/tree/main/examples/pr-review-jev"><img src="https://raw.githubusercontent.com/CelestoAI/celesto/main/open-muse/banner-dark.png" alt="Celesto PR Review Lab" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/CelestoAI/celesto/tree/main/examples/pr-review-jev">Celesto PR Review Lab</a></b><br><sub>CelestoAI · GitHub · ⭐ 959 仓库 · 2026-09-17</sub><br>基于 Celesto microVM 沙箱的示例 app：agent 为某个公开的 GitHub PR 准备测试环境、运行检查，并在候选问题上对比 LLM 评审和 Jev 的表现。<br><sub><b>Jev 用法:</b> Jev 判断每个问题是否由本次改动引入、是否有证据支撑、是否值得修复。</sub><br><sub>相关: <a href="https://github.com/CelestoAI/celesto">repo</a> · <a href="https://www.reddit.com/r/OpenAI/comments/1wkr5lz/jev_vs_luna/">discussion</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/merijjeyn/jive"><img src="https://raw.githubusercontent.com/merijjeyn/jive/main/docs/assets/trace-comparison.gif" alt="Jive" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/merijjeyn/jive">Jive</a></b><br><sub>merijjeyn · GitHub · ⭐ 19 · 2026-09-21</sub><br>终端编程 agent，用图调用取代工具调用：LLM 规划出一个由工具调用和 Jev 调用组成的可执行 DAG，计划中那些快速的直觉判断和批量评估无需额外的 LLM 调用即可完成。<br><sub>相关: <a href="https://www.reddit.com/r/SideProject/comments/1wmp3wn/jive_rethinking_the_agentic_loop_with_system_one/">demo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/repoprompt/repoprompt-ce/tree/main/Sources/RepoPrompt/Features/AgentMode/Routing/Backends/Jev"><img src="https://opengraph.githubassets.com/1/repoprompt/repoprompt-ce" alt="RepoPrompt 的 Jev 任务路由器" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/repoprompt/repoprompt-ce/tree/main/Sources/RepoPrompt/Features/AgentMode/Routing/Backends/Jev">RepoPrompt 的 Jev 任务路由器</a></b><br><sub>repoprompt · GitHub · ⭐ 935 仓库 · 2026-05-12</sub><br>面向编程 agent 的原生 macOS 上下文工程应用 RepoPrompt CE，为 Agent Mode 的模型路由器加了一个 Jev 后端，无需文本模型就能为每个任务选路。<br><sub><b>Jev 用法:</b> 用经过验证的 TypeSafe API key 启用 Model Router；该后端通过 /v1/systemone 路由 agent 任务。</sub><br><sub>相关: <a href="https://repoprompt.com">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/CheshiAI/Cheshi"><img src="https://raw.githubusercontent.com/CheshiAI/Cheshi/main/resources/icons/about-logo.png" alt="Cheshi" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/CheshiAI/Cheshi">Cheshi</a></b><br><sub>CheshiAI · GitHub · ⭐ 18 · 2026-09-13</sub><br>macOS 工作区 app，把 OpenAI Codex 对话、CodeGraph 代码探索、Git 和 Ghostty 终端集中到一处，用 Jev 实现对话记忆，能找回过去的会话和决策并标注出处。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/mlcyclops/lucidagentide"><img src="https://opengraph.githubassets.com/1/mlcyclops/lucidagentide" alt="LUCID 的 Jev 判断后端" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/mlcyclops/lucidagentide">LUCID 的 Jev 判断后端</a></b><br><sub>mlcyclops · GitHub · ⭐ 18 · 2026-06-18</sub><br>为基于 oh-my-pi、安全优先的桌面编程 harness LUCID 加入 Jev 支持：类型化判断、agent 的 judge() 调用，以及从 jev-ultrafast 移植来的 browser_run 策略都交给 Jev 回答，并在每条回复下留有追踪记录。<br><sub><b>Jev 用法:</b> browser_run 每一步针对带索引的控件表提一组问题，选出操作和目标；全程没有模型写文字，任何一次判断出错都会终止运行。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/philipbrembeck/pi-advisor"><img src="https://raw.githubusercontent.com/philipbrembeck/pi-advisor/refs/heads/main/assets/screenshot.png" alt="pi-advisor" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/philipbrembeck/pi-advisor">pi-advisor</a></b><br><sub>philipbrembeck · GitHub · ⭐ 18 · 2026-07-17</sub><br>Pi 编程 agent 的 Advisor 与 Executor 插件，遇到关键决策时咨询更强的模型，可选的 Jev 过滤器会跳过无关紧要的咨询，另有一个 Jev 轮次闸门负责把 Advisor 拉进来。</td>
</tr>
<tr>
<td width="260" valign="top"></td>
<td valign="top"><b><a href="https://www.npmjs.com/package/pi-jev-guard">pi-jev-guard</a></b><br><sub>alucard_24 · 软件包 · ⬇ 1.7k · 2026-09-19</sub><br>Pi 扩展，用 Jev 验证模型输出：既可以通过工具、命令和审查 skill 按需触发，也可以通过一个带防护的 provider 自动执行，在 Jev 批准前扣住回复。<br><sub><b>Jev 用法:</b> 验证结论，外加由模型自定义的 Noul、Choice 和 Score 问题，直接走 TypeSafe 或经由 OpenRouter。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Eriskii/ErisLint"><img src="https://opengraph.githubassets.com/1/Eriskii/ErisLint" alt="ErisLint" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Eriskii/ErisLint">ErisLint</a></b><br><sub>Eriskii · GitHub · ⭐ 17 · 2026-09-18</sub><br>带 VS Code 扩展的 Rust linter，你可以用 JSON 定义代码质量规则，例如某个函数是否复杂得没有必要、某个命名是否有误导性，再把 Jev 的答案映射为警告或错误。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/AndreaGriffiths11/IssueCrush"><img src="https://opengraph.githubassets.com/1/AndreaGriffiths11/IssueCrush" alt="IssueCrush" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/AndreaGriffiths11/IssueCrush">IssueCrush</a></b><br><sub>AndreaGriffiths11 · GitHub · ⭐ 17 · 2026-01-21</sub><br>Tinder 式的 app，左右滑动你的 GitHub issue 来决定关闭还是保留；可选的结构化分诊会为每张卡片向 Jev 请求推荐操作、陈旧度和工作量评分，以及可执行的概率。<br><sub><b>Jev 用法:</b> 一次请求包含一个在实现/需要更多信息/重复/过期关闭/不处理之间的 Choice、两个 Score 和一个 Noul；分诊结果只用来装饰卡片，从不替你滑动。</sub><br><sub>相关: <a href="https://gray-bush-0c5cb190f.2.azurestaticapps.net/">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/shiftynick/jev-axi"><img src="https://raw.githubusercontent.com/shiftynick/jev-axi/main/scripts/demo/safety.gif" alt="jev-axi" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/shiftynick/jev-axi">jev-axi</a></b><br><sub>shiftynick · GitHub · ⭐ 17 · 2026-09-16</sub><br>为 agent 设计易用性的 CLI，让编程 agent 从 shell 获得 Jev 判断，包括拦截危险 Bash 调用的 PreToolUse hook、对抓取文本做提示词注入筛查、日志分诊和排序。<br><sub>相关: <a href="https://www.npmjs.com/package/jev-axi">npm</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/valentynkit/jev-belay"><img src="https://raw.githubusercontent.com/valentynkit/jev-belay/main/demo/demo.gif" alt="jev-belay" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/valentynkit/jev-belay">jev-belay</a></b><br><sub>valentynkit · GitHub · ⭐ 17 · 2026-09-18</sub><br>Claude Code 的 Stop hook：当有文件改动却没有任何检查通过时，就结束消息是否属于未经验证的“完成”向 Jev 问四个问题；在 100 个带标注的停止事件上 AUROC 达到 0.976。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/keltokhy/jgrep"><img src="https://opengraph.githubassets.com/1/keltokhy/jgrep" alt="jgrep" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/keltokhy/jgrep">jgrep</a></b><br><sub>keltokhy · GitHub · ⭐ 17 · 2026-09-18</sub><br>以大白话描述作为匹配模式的命令行 grep：每一行、每条记录、每个函数或每个 diff 片段都变成一个 Jev 是/否问题，在输入流进来时并发判断，接在 tail -f 后面也能用。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Nanako0129/lorenzini"><img src="https://opengraph.githubassets.com/1/Nanako0129/lorenzini" alt="lorenzini" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Nanako0129/lorenzini">lorenzini</a></b><br><sub>Nanako0129 · GitHub · ⭐ 17 · 2026-09-19</sub><br>一组 Claude Code skill，轮询 CodeRabbit、Copilot 和 Codex 这几个 PR 审查者，判断它们的结论是否真的允许合并；可选的 Jev 影子分类器会标记出那些被折叠起来、却描述了未处理工作的审查段落。<br><sub><b>Jev 用法:</b> 仅限影子模式：Jev 可以打印“would HOLD”，但从不改变闸门的结论；问题集有版本管理，并用黄金集做测试。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/kyu1204/oh-my-harness"><img src="https://raw.githubusercontent.com/kyu1204/oh-my-harness/main/docs/demo.gif" alt="oh-my-harness" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/kyu1204/oh-my-harness">oh-my-harness</a></b><br><sub>kyu1204 · GitHub · ⭐ 17 · 2026-03-16</sub><br>CLI，把一段自然语言描述变成 Claude Code、Codex 和 Pi 上强制执行的护栏（CLAUDE.md、hook、settings）；配上 TypeSafe key 后，Jev 一次调用就选好要启用哪些守护块以及严格到什么程度。<br><sub><b>Jev 用法:</b> 每个可选块一个 Noul，外加一个严格程度问题；&gt;= 0.65 启用，&lt;= 0.35 禁用，介于两者之间则保留预设默认值。</sub><br><sub>相关: <a href="https://www.npmjs.com/package/oh-my-harness">npm</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Davidcreador/pi-dcp"><img src="https://opengraph.githubassets.com/1/Davidcreador/pi-dcp" alt="pi-dcp" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Davidcreador/pi-dcp">pi-dcp</a></b><br><sub>Davidcreador · GitHub · ⭐ 17 · 2026-05-13</sub><br>Pi 扩展，在长时间编程会话中通过去重工具调用、剥离出错的载荷、总结已结束的工作流来减少 token 开销，并带有实验性的 Jev 上下文选择，决定保留哪些内容。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/bastani-inc/atomic/tree/main/packages/coding-agent/src/core/structured-output"><img src="https://opengraph.githubassets.com/1/bastani-inc/atomic" alt="Atomic 的 Jev 决策后端" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/bastani-inc/atomic/tree/main/packages/coding-agent/src/core/structured-output">Atomic 的 Jev 决策后端</a></b><br><sub>bastani-inc · GitHub · ⭐ 812 仓库 · 2025-10-23</sub><br>Atomic 编程 agent 运行时中可选的 Jev 后端，用于经过 schema 校验的结构化决策；存在 TypeSafe 凭证时默认用它来选择工作流和子 agent 的模型，否则回退到对话模型。<br><sub>相关: <a href="https://github.com/bastani-inc/atomic">repo</a> · <a href="https://bastani.ai/">website</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://www.reddit.com/r/Anthropic/comments/1wizprg/jev_as_orchestrator/"><img src="https://preview.redd.it/t9zgoqj034qh1.png?width=1050&amp;format=png&amp;auto=webp&amp;s=a488a0150a11da141fb3b6d58c80245590a11cf8" alt="用 Jev 做调试编排器" width="240"></a></td>
<td valign="top"><b><a href="https://www.reddit.com/r/Anthropic/comments/1wizprg/jev_as_orchestrator/">用 Jev 做调试编排器</a></b><br><sub>TemporaryLevel922 · Reddit · ▲ 5 · 2026-09-17</sub><br>一个调试循环：Claude 收集证据，Jev 为各个假设打分并挑选下一步诊断，再由 Claude 或 Codex 执行，减少了反复失败的尝试。<br><sub><b>Jev 用法:</b> 每个假设一个 Noul，判断其与证据是否一致，外加一个 Choice 选择下一步诊断。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/kyu1204/jgrep"><img src="https://raw.githubusercontent.com/kyu1204/jgrep/main/docs/demo.gif" alt="jgrep" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/kyu1204/jgrep">jgrep</a></b><br><sub>kyu1204 · GitHub · ⭐ 15 · 2026-09-19</sub><br>语义 grep，把文件或 git diff 片段切块，对每块问 Jev 一个 Noul，打印超过阈值的 file:line 命中结果，并使用 grep 风格的退出码，因此可以在 CI 中对 diff 做 lint；扫描一个 src 目录约 2 s。<br><sub>相关: <a href="https://www.npmjs.com/package/jevgrep">npm</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/ZephyrDeng/pi-review"><img src="https://raw.githubusercontent.com/ZephyrDeng/pi-review/main/docs/assets/panel-live-pi.jpg" alt="pi-review" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/ZephyrDeng/pi-review">pi-review</a></b><br><sub>ZephyrDeng · GitHub · ⭐ 15 · 2026-06-29</sub><br>CLI、CI 闸门和 agent skill，把代码审查和计划审查交给相互隔离的只读 Pi 审查者；Jev 负责对照缺陷目录做约 1 秒的筛查（1.2 秒，完整一轮则要 30-50 秒），并裁定审查小组是否达成共识。<br><sub><b>Jev 用法:</b> 有歧义的发现对交给 Jev（约 100 毫秒）；落在 0.3-0.7 边界区间的答案再由 Pi 重判一次。</sub><br><sub>相关: <a href="https://www.npmjs.com/package/@zephyrdeng/pi-review">npm</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/AkashPriyadarshii/jev-superpowers"><img src="https://opengraph.githubassets.com/1/AkashPriyadarshii/jev-superpowers" alt="jev-superpowers" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/AkashPriyadarshii/jev-superpowers">jev-superpowers</a></b><br><sub>AkashPriyadarshii · GitHub · ⭐ 14 · 2026-09-18</sub><br>面向 Claude Code、Codex、Cursor 等编程 agent 的 skill 框架，在工作流检查点调用 Jev：安装前审查依赖、把关任务是否完成，以及引导调试决策。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/mizchi/jev-test-filter"><img src="https://opengraph.githubassets.com/1/mizchi/jev-test-filter" alt="jev-test-filter" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/mizchi/jev-test-filter">jev-test-filter</a></b><br><sub>mizchi · GitHub · ⭐ 14 · 2026-09-21</sub><br>CLI 和 agent skill，在一次 Jev 往返中对照 git diff 给每个测试打分，并输出 vitest、Jest、node:test、Playwright、cargo test 和 go test 的过滤参数，只运行可能受影响的测试。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/shitianfang/jev-use"><img src="https://raw.githubusercontent.com/shitianfang/jev-use/main/assets/collab.gif" alt="jev-use" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/shitianfang/jev-use">jev-use</a></b><br><sub>shitianfang · GitHub · ⭐ 14 · 2026-09-19</sub><br>适用于 Claude Code、Codex 和 pi 的插件，把不需要输出文本的 agent 步骤交给 Jev，p50 延迟约 230 毫秒，每 1,000 次判断 $0.02，需要写文字时再以类型化方式升级回 LLM。<br><sub>相关: <a href="https://www.npmjs.com/package/jev-use">npm</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/CarolMonroe/status/2101747586126557230"><img src="https://pbs.twimg.com/amplify_video_thumb/2101741811559710720/img/iwCtvJtHgS16n2kL.jpg" alt="JevRLS" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/CarolMonroe/status/2101747586126557230">JevRLS</a></b><br><sub>CarolMonroe · X · ♥ 14 · 2026-09-20</sub><br>Web app：粘贴 Supabase 行级安全（Row Level Security）策略，就能看到 Jev 与 GPT 和 Gemini 在同一套评分标准和判定规则下比赛找漏洞，并排对比速度和成本。<br><sub>相关: <a href="https://jevrls.lovable.app">app</a> · <a href="https://jevrls.lovable.app">project</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/PanAchy/jevvy"><img src="https://raw.githubusercontent.com/PanAchy/jevvy/main/assets/jevvy-demo.gif" alt="Jevvy" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/PanAchy/jevvy">Jevvy</a></b><br><sub>PanAchy · GitHub · ⭐ 14 · 2026-09-18</sub><br>面向 OpenCode 和 Claude Code 的插件合集，其中的权限插件会自动批准无害的 shell 请求，拿不准的都交回 agent 原有的权限流程处理。<br><sub><b>Jev 用法:</b> 只有所有问询都通过时才批准当前这一个操作；现有的允许和拒绝规则仍具有最终效力。</sub><br><sub>相关: <a href="https://www.reddit.com/r/opencodeCLI/comments/1wl5k2c/i_built_jevvy_autoapprove_harmless_opencode/">demo</a> · <a href="https://www.reddit.com/r/ClaudeCode/comments/1wm062g/jevvy_now_supports_claude_code/">discussion</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/tyler-dot-earth/patdown"><img src="https://github.com/user-attachments/assets/f7c73138-3914-4fbd-9e6b-7a37d161334a" alt="patdown" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/tyler-dot-earth/patdown">patdown</a></b><br><sub>tyler-dot-earth · GitHub · ⭐ 14 · 2026-09-18</sub><br>模糊 linter，按写在一个 Markdown 文件里的规则评判文件或改动，打包成 CLI、GitHub Action、Pi 写入引导包和 Claude Code Write/Edit hook 等形式，其中的 Jev 评判器可以替换。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/philippdubach/pi-jev-router"><img src="https://opengraph.githubassets.com/1/philippdubach/pi-jev-router" alt="pi-jev-router" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/philippdubach/pi-jev-router">pi-jev-router</a></b><br><sub>philippdubach · GitHub · ⭐ 14 · 2026-09-20</sub><br>pi 编程 agent 的模型路由器，先用 Jev 给每个任务分类，再在 OpenRouter 模型目录上按质量、成本和延迟构成的帕累托前沿选出拐点。<br><sub>相关: <a href="https://news.ycombinator.com/item?id=49775968">demo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/gmickel/flow-next/blob/main/plugins/flow-next/docs/judge.md"><img src="https://repository-images.githubusercontent.com/1123446919/416d2393-7e8d-4612-97f7-06e82b1a67e4" alt="flow-next 的 Jev 裁判" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/gmickel/flow-next/blob/main/plugins/flow-next/docs/judge.md">flow-next 的 Jev 裁判</a></b><br><sub>gmickel · GitHub · ⭐ 698 仓库 · 2025-12-26</sub><br>agent 化工程工作流 flow-next 中可选的 Jev 裁判，在每个决策点用一次请求回答范围很窄的路由、任务档位和记忆类问题。<br><sub><b>Jev 用法:</b> 由代码提供 state 和固定规则；不确定的答案由宿主处理，原有的评审、QA 和合并闸门照常运行。</sub><br><sub>相关: <a href="https://flow-next.dev">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/samuelfaj/distill/tree/main/crates/codegen/distill-workspace/src/jev"><img src="https://raw.githubusercontent.com/samuelfaj/distill/main/screenshot.png" alt="Distill 的 Jev 支持" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/samuelfaj/distill/tree/main/crates/codegen/distill-workspace/src/jev">Distill 的 Jev 支持</a></b><br><sub>samuelfaj · GitHub · ⭐ 683 仓库 · 2026-09-19</sub><br>Distill 中的 Jev 模块。Distill 是面向 Grok、Codex 和 OpenAI 兼容模型的省 token 编程 agent harness 和 TUI，这个模块负责选择模型档位和推理强度、路由有边界的辅助任务，并判断该保留哪些上下文。<br><sub>相关: <a href="https://github.com/samuelfaj/distill">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/BorisLeMeec/jev"><img src="https://raw.githubusercontent.com/BorisLeMeec/jev/main/docs/demo.gif" alt="jev (Claude Code plugin)" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/BorisLeMeec/jev">jev (Claude Code plugin)</a></b><br><sub>BorisLeMeec · GitHub · ⭐ 13 · 2026-09-17</sub><br>用 Go 写的 Claude Code 插件，接管搜索和大文件读取，用 Jev 找出相关文件并回答关于代码的有界问题，让整个文件永远不必进入 agent 的上下文。<br><sub>相关: <a href="https://www.reddit.com/r/PromptEngineering/comments/1wjmhj0/a_jev_claude_code_plugin_that_saves_30_token_usage/">discussion</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/vizuh/sabi"><img src="https://raw.githubusercontent.com/vizuh/sabi/main/docs/images/sabi-routing.svg" alt="Sabi" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/vizuh/sabi">Sabi</a></b><br><sub>vizuh · GitHub · ⭐ 13 · 2026-09-18</sub><br>面向编程 harness 的逐轮路由器，决定模型、推理力度和 provider：根据轨迹证据选择便宜、中档或强力档位，只在某一轮拿不准时才问 Jev。<br><sub><b>Jev 用法:</b> 可选的 Jev 评判器在合法的档位选项中做选择；超时、答案无效或缺少凭据时回退到确定性策略。每次 6k token 的判断约 $0.00025。</sub><br><sub>相关: <a href="https://www.npmjs.com/package/@vizuh/sabi">npm</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Ray0907/security-scan"><img src="https://opengraph.githubassets.com/1/Ray0907/security-scan" alt="security-scan" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Ray0907/security-scan">security-scan</a></b><br><sub>Ray0907 · GitHub · ⭐ 13 · 2026-01-18</sub><br>做只读安全扫描（依赖审计、Semgrep、密钥、IaC、GitHub Actions）的 agent skill，带一个可选的 Jev 步骤，为尚未审阅的发现建议结论。<br><sub><b>Jev 用法:</b> 每条脱敏后的 Semgrep 发现一个 Choice，在 confirmed、needs_validation 和 rejected 之间选择；建议单独存放，直到有人补上理由。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/kevinkern/status/2101032931456168098"><img src="https://pbs.twimg.com/amplify_video_thumb/2101032303396790272/img/RbVCCv2UgU7Jox4h.jpg" alt="用 Jev 做 Android 端到端测试" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/kevinkern/status/2101032931456168098">用 Jev 做 Android 端到端测试</a></b><br><sub>kevinkern · X · ♥ 12 · 2026-09-18</sub><br>在真实 Android 设备上做端到端测试：同样的提示词和 15 个测试步骤，Jev 浏览 Wikipedia 的速度比带视觉的 DeepSeek 快约 14.8 倍。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/mejiasd3v/pi-jev-router"><img src="https://opengraph.githubassets.com/1/mejiasd3v/pi-jev-router" alt="Jev Router for Pi" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/mejiasd3v/pi-jev-router">Jev Router for Pi</a></b><br><sub>mejiasd3v · GitHub · ⭐ 12 · 2026-09-17</sub><br>Pi 编程 agent 扩展，通过 Vercel AI Gateway 让 Jev 选定模型和推理强度，然后在整个会话中固定这一选择，生成仍使用你现有的 Pi provider。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/sting9k/seatworks"><img src="https://raw.githubusercontent.com/sting9k/seatworks/v2/docs/images/slp-graph.svg" alt="Seatworks" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/sting9k/seatworks">Seatworks</a></b><br><sub>sting9k · GitHub · ⭐ 12 · 2026-09-16</sub><br>Paseo 插件，运行一支由监督者、负责人、同伴、审查者和观察者组成的编程 agent 团队，并可选用经 OpenRouter 调用的 Jev 作为付费旁读者，标记工作方式上出现的问题。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/autonomous-ai/openharness/tree/main/store/agents/jev-guard"><img src="https://opengraph.githubassets.com/1/autonomous-ai/openharness" alt="Jev Guard (OpenHarness)" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/autonomous-ai/openharness/tree/main/store/agents/jev-guard">Jev Guard (OpenHarness)</a></b><br><sub>autonomous-ai · GitHub · ⭐ 562 仓库 · 2026-08-04</sub><br>OpenHarness 商店中的 Jev Guard agent，监视你的项目文件夹，每次编辑都运行测试，并让 Jev 为每次改动离目标多近、风险多大、可信度多高打分。<br><sub><b>Jev 用法:</b> Jev 对照 goal.json 逐次评判你自己的编辑；代码归你所有，Jev 只负责旁观。</sub><br><sub>相关: <a href="https://www.autonomous.ai/harness">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/iamtoomas/JevLint"><img src="https://opengraph.githubassets.com/1/iamtoomas/JevLint" alt="JevLint" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/iamtoomas/JevLint">JevLint</a></b><br><sub>iamtoomas · GitHub · ⭐ 11 · 2026-09-17</sub><br>语义 linter，对照用大白话写的编码规范检查源文件，报告每个文件违反某条规则的概率，适用于 agent 的“写-查-改”循环或 CI。<br><sub><b>Jev 用法:</b> 每条规则在文件级别做 Noul 判断，另有一个检查魔法字符串的插件。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/alexhawat/mergeCraft"><img src="https://raw.githubusercontent.com/alexhawat/mergeCraft/main/assets/brand/mark-light.svg" alt="mergeCraft" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/alexhawat/mergeCraft">mergeCraft</a></b><br><sub>alexhawat · GitHub · ⭐ 11 · 2026-07-27</sub><br>自托管、自带密钥的 AI PR 审查 GitHub Action，在生成式审查器和校验器运行之前加了一道 Jev 筛选闸门，对 diff 单元排序和过滤。<br><sub><b>Jev 用法:</b> 对切分后的 diff 单元提一组组问题，结果交给只在影子模式下运行的“排序加标注”策略；生成式审查器始终照常运行。</sub><br><sub>相关: <a href="https://github.com/alexhawat/mergeCraft/blob/main/docs/jev-gate-patterns.md">docs</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/opencrew-ai/opencrew"><img src="https://opengraph.githubassets.com/1/opencrew-ai/opencrew" alt="OpenCrew" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/opencrew-ai/opencrew">OpenCrew</a></b><br><sub>opencrew-ai · GitHub · ⭐ 11 · 2026-08-29</sub><br>本地的 Slack 风格指挥部，运行一组带审批闸门的 Claude Code agent，用 Jev 做快速路由判断，比如某条命令是否安全、某个计划是否完整。<br><sub><b>Jev 用法:</b> 每个类型化判断约 100 毫秒，取代一轮 Claude Code：确认回执、通道路由、快速模型聊天、只读命令审批和跳过审查者；答案不确定时仍走原来的路径。</sub><br><sub>相关: <a href="https://opencrew.run">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/madeye/pi-jev"><img src="https://pbs.twimg.com/media/HSk5Xyeb0AA2JSI.jpg?name=orig" alt="pi-jev" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/madeye/pi-jev">pi-jev</a></b><br><sub>madeye · GitHub · ⭐ 11 · 2026-09-18</sub><br>Pi 编程 agent 扩展，由 Jev 挑选要发送的文件片段，由 Qwen 或 DeepSeek 等本地模型写代码，并对完全相同的结果做缓存，以降低端到端延迟。<br><sub>相关: <a href="https://x.com/m0d8ye/status/2101101008650989747">demo</a></sub></td>
</tr>
</table>

<details><summary>还有 366 条</summary>

- **[omg.dev 的 Jev 端到端测试](https://github.com/BennyKok/omg.dev/blob/main/mobile/scripts/jev.ts)** · <sub>BennyKok · GitHub · ⭐ 535 仓库 · 2026-09-18</sub><br>为 omg.dev 移动应用做的端到端测试层，Jev 读取屏幕的无障碍树，判断某一步是否完成、是否走进了死胡同，以及下一步该点哪个元素。
- **[nanocodex 的 Jev 路由](https://github.com/gakonst/nanocodex/blob/master/js/managed/src/jev-reliability.ts)** · <sub>gakonst · GitHub · ⭐ 519 仓库 · 2026-07-15</sub><br>用 Rust 构建 OpenAI agent 的组件库，用 Jev 做线程级模型路由，借助一个固定词表的可靠性与故障分类器为每个线程选择后端。
- **[Azdaja](https://github.com/kubet/azdaja)** · <sub>kubet · GitHub · ⭐ 10 · 2026-08-11</sub><br>面向 Claude Code、Codex、Gemini CLI、OpenCode 和 Jcode 的递归语言模型层，把完整源码保存在本地 Python 求值器中，可选 Jev 判断和有预算限制的批处理。
- **[DeliveryGuard](https://github.com/wzf1997/delivery-harness)** · <sub>wzf1997 · GitHub · ⭐ 10 · 2026-08-22</sub><br>面向编程 agent、以证据驱动的交付闸门，覆盖规格、验收、修复和发布，可选的 Jev 适配器为普通交付候选额外提供一个基于摘要的自动评审信号。
- **[Helm](https://github.com/Jimuelle07/Helm)** · <sub>Jimuelle07 · GitHub · ⭐ 10 · 2026-09-20</sub><br>编程 agent 路由器兼监管器，可作为 Claude Code 插件、Gemini 扩展或 agent skill 安装，它会探测你装了哪些 agent，让 Jev 为每个任务挑选一个，并判断工人是否已完成任务。
- **[Lockstep](https://github.com/lockstep-team-agent/lockstep)** · <sub>lockstep-team-agent · GitHub · ⭐ 10 · 2026-06-07</sub><br>团队编程 agent 共享的决策记录，检查改动的代码是否可能与已采纳的决策相矛盾，其漏斗中的召回和复查两个阶段由 Jev 完成。
- **[pi-quiet-ask](https://github.com/HyunjunJeon/pi-quiet-ask)** · <sub>HyunjunJeon · GitHub · ⭐ 10 · 2026-09-17</sub><br>Pi 编程 agent 的规则引擎，规则包把 hook 绑定到 Jev 问题上，比如某条命令是否具有破坏性、输出是否泄露了密钥、某个说法是否经过验证；每个答案都会记录，出错时放行。
- **[phi Jev provider](https://github.com/pulseaiclub/phi/tree/main/internal/llm/jev)** · <sub>pulseaiclub · GitHub · ⭐ 493 仓库 · 2026-08-03</sub><br>精简的 Go 终端编程 agent，移植了 TypeSafe SDK 的同步 System One 接口，从而能向 Jev 提带类型的问题，重试策略与它的其他 provider 相同。
- **[Clean Code Review](https://github.com/frostney/clean-code-review)** · <sub>frostney · GitHub · ⭐ 9 · 2026-09-17</sub><br>公开 GitHub pull request 的评审工具：Jev 针对每个改动文件回答一组源自 Robert C. Martin《Clean Code》的问题，再由 Luna 根据这些答案写出评审；基于 eve 和 Next.js 构建。
- **[herdr-mcp](https://github.com/whshang/herdr-mcp)** · <sub>whshang · GitHub · ⭐ 9 · 2026-08-20</sub><br>MCP/OAuth 边缘层，让 ChatGPT 等 Web 端规划工具通过 Herdr 在本地机器上运行代码、Git 和测试；每轮结束后的语义判断优先走 Jev 路由，再回退到 LLM 和脚本。
- **[瞬时生成变量](https://x.com/eltokh7/status/2101016673109016622)** · <sub>eltokh7 · X · ♥ 9 · 2026-09-18</sub><br>Jev 几乎瞬间生成变量的演示，来自作者一系列 Jev 开发者工具实验。
- **[jev-commit](https://github.com/valentynkit/jev-commit)** · <sub>valentynkit · GitHub · ⭐ 9 · 2026-09-18</sub><br>pre-commit hook，一次调用就提交信息和暂存的 diff 向 Jev 问五个问题，例如空洞的提交信息、前后矛盾、调试残留和范围蔓延，每一千次提交约四美分。
- **[Lintus](https://github.com/virolea/lintus)** · <sub>virolea · GitHub · ⭐ 9 · 2026-09-20</sub><br>Ruby linter，规则是 YAML 文件里的自然语言问题；每条规则都以 Jev Noul 的形式对每个文件提问，可作用于整个代码树、改动过的文件，或在 pre-commit hook 中只检查暂存文件。
- **[musts](https://github.com/bitomule/musts)** · <sub>bitomule · GitHub · ⭐ 9 · 2026-05-13</sub><br>编程 agent 的验证循环，所有声明的检查都通过之前任务不会关闭，其中包括 <code>uses: jev</code> 检查，让 Jev 判断改动的文件是否违反某条文字规则。
- **[Pi Jev Router](https://github.com/win4r/pi-jev-router)** · <sub>win4r · GitHub · ⭐ 9 · 2026-09-20</sub><br>Pi Coding Agent 在任务边界处做模型路由的扩展：Jev 判断任务档位、上下文是否充足以及后果，再由代码从 Pi 实际可用的模型中挑选。
- **[pi-fast-jev-compaction](https://github.com/joelhooks/pi-fast-jev-compaction)** · <sub>joelhooks · GitHub · ⭐ 9 · 2026-09-18</sub><br>Pi 扩展，对话文本逐字保留，通过对每次工具调用问 Jev 两个 Noul（是否保留调用、是否保留结果）来裁剪过时的工具历史，必要时回退到 Pi 的摘要式压缩。
- **[VexJoy 的 Jev 路由](https://github.com/notque/vexjoy-agent/blob/main/scripts/jev-route.py)** · <sub>notque · GitHub · ⭐ 423 仓库 · 2026-09-17</sub><br>Claude Code 与 Codex 工具包 VexJoy 中的 Jev 路由器，把一条自然语言的 /do 请求匹配到 43 个专业 agent、skill 和工作流之一，在模型输出第一个 token 之前由 hook 注入。
- **[Smithers 的 Jev 流程](https://github.com/smithersai/smithers/blob/main/apps/server/src/jev.ts)** · <sub>smithersai · GitHub · ⭐ 419 仓库 · 2026-01-05</sub><br>代码库维护 agent Smithers 中的 Jev 集成：一个 Vercel AI Gateway 客户端，外加一组基于它的流程，用来给仓库 issue 打分、发现重复和复现报告、检查 wiki 引用并监看 agent 会话。
- **[Seedit 的 Jev 辅助脚本](https://github.com/bitsocialnet/seedit/tree/master/scripts/jev)** · <sub>bitsocialnet · GitHub · ⭐ 416 仓库 · 2023-08-25</sub><br>reddit 替代品 Seedit 仓库中可选的 Jev 开发辅助工具，用于浏览器基准测试、代码审查和翻译审查，在发布的应用之外运行。
- **[jevgate](https://jevgate.dev)** · <sub>remotehost · 应用 · ⬇ 804 · 2026-09-18</sub><br>Claude Code 和 Codex 的权限 hook，约 300 毫秒 内自动批准常规的 agent 请求，记录每一个决策，并把任何有风险或不明确的请求交给你平常的审查流程。
- **[Better TypeScript 语义检查](https://github.com/andrueandersoncs/better-typescript)** · <sub>andrueandersoncs · GitHub · ⭐ 8 · 2026-06-10</sub><br>面向 TypeScript 项目的 Go linter，其 semantic 命令用有边界的 TypeSafe 判断，把自然语言写的工程规范与工作区改动或某个 Git 区间进行比对检查。
- **[bounce-router](https://github.com/richet/bounce-router)** · <sub>richet · GitHub · ⭐ 8 · 2026-09-07</sub><br>架在 Claude Code、Codex 和 Muse 之上的 TUI，触发用量限制时在各服务商之间切换，可选的 Jev 层负责给出评审结论，并按等级把工作路由到不同的工人配置。
- **[Calliope CLI](https://github.com/calliopeai/calliope-cli)** · <sub>calliopeai · GitHub · ⭐ 8 · 2026-01-09</sub><br>支持多后端的终端编程 agent，其 judgments 功能会提出类型化问题，返回可用于分支判断的概率和置信度，可来自任意后端或原生 TypeSafe 引擎。
- **[JevPR](https://github.com/HexyeDEV/JevPR)** · <sub>HexyeDEV · GitHub · ⭐ 8 · 2026-09-20</sub><br>GitHub App，把每个新开或更新的 pull request 发给 Jev，得到 LOW、NORMAL 或 SPECIALIST 三档风险结论，再由确定性策略映射为自动批准、请求评审或一次 check run。
- **[MCode 增强包](https://github.com/drowzeys/keys-mcode-continuous-context-browser-decision-enhancement-pack)** · <sub>drowzeys · GitHub · ⭐ 8 · 2026-09-20</sub><br>给在 DGX Spark 上搭配本地 GLM 模型运行的 MiniMax Code CLI 打的一组补丁：上下文用量指示、持续上下文续期、一个上下文压缩的修复，以及一个接到本地 /v1/systemone 兼容策略上的 jev-ultrafast 浏览器 agent。
- **[omp-jev-compaction](https://github.com/jerryfane/omp-jev-compaction)** · <sub>jerryfane · GitHub · ⭐ 8 · 2026-09-18</sub><br>Oh My Pi 编程 agent 的上下文缩减扩展，用 Jev 给每次工具调用及其结果打分，把不再需要的截断成开头部分加一条恢复说明，从不改写文字。
- **[Pattern MCP](https://github.com/donaldrichard19-LVD/pattern-mcp)** · <sub>donaldrichard19-LVD · GitHub · ⭐ 8 · 2026-08-24</sub><br>MCP 服务器，在编程 agent 动手构建前对照产品需求检查 UI 组件库，带一个实验性的 Jev 打分器，对照检查清单给每个 Figma 组件页面打分。
- **[IFClite 评审通道的 Jev 客户端](https://github.com/LTplus-AG/ifc-lite/blob/main/scripts/review/lib/jev-client.mjs)** · <sub>LTplus-AG · GitHub · ⭐ 382 仓库 · 2026-01-10</sub><br>一个开源 IFC 工具包的 AI 代码评审通道，用 Jev 把评审问题与评测项做语义匹配并合并重复问题，没有 key 时平稳降级。
- **[Paxeer X 的 Jev 检查](https://github.com/Sidiora-Labs/Paxeer-X-Network/tree/main/tools/jev)** · <sub>Sidiora-Labs · GitHub · ⭐ 371 仓库 · 2026-08-14</sub><br>一个 agent 执行网络里的 CI 建议工具，用 Jev 检查 pull request 与 commit message 是否一致，并对 cargo-deny 安全公告、测试失败和 README 翻译漂移做分诊。
- **[any-auto](https://github.com/jjyr/any-auto)** · <sub>jjyr · GitHub · ⭐ 7 · 2026-08-20</sub><br>Pi 和 Antigravity 编程 agent 的自动审批守护进程：本地规则直接放行只读工具、拦截危险命令，其余请求交给 Jev、Pi、agy 或某个 API 模型等评审后端。
- **[bro](https://github.com/JustSuperHuman/bro-cli)** · <sub>JustSuperHuman · GitHub · ⭐ 7 · 2026-06-22</sub><br>启动器，可让 Claude Code、omp、Pi、Codex 或 DeepSeek Harness 对接任意模型服务商，有一个开关可在前面加上 Jev Router，逐轮选择 Haiku 或 Opus。
- **[Jevies](https://github.com/Ezbaze/jevies)** · <sub>Ezbaze · GitHub · ⭐ 7 · 2026-09-18</sub><br>用 Jev 来设计和审查 Jev 配置的 Python 辅助工具：建议该用 Noul、Score 还是 Choice，审查指令和选项，检查评分标准，并用预设规则测试输入。
- **[lcc](https://github.com/lucasmartins-ai/lcc)** · <sub>lucasmartins-ai · GitHub · ⭐ 7 · 2026-06-19</sub><br>本地上下文编译器（Local Context Compiler），在提示词上下文送进模型之前做清洗、去重和压缩；<code>lcc compact --provider jev</code> 让 Jev 给每个块打出保留概率，按块原样丢弃，不做摘要。
- **[omp-jev](https://github.com/thejorgg/omp-jev)** · <sub>thejorgg · GitHub · ⭐ 7 · 2026-09-17</sub><br>Oh My Pi 插件，给这个编程 agent 加上 Jev 路由判断，外加一个可选启用的检查点编排器，通过可编辑的 XDG 文件和 <code>/jev</code> 命令配置，默认关闭。
- **[pi-codemcp](https://github.com/yolonir/pi-codemcp)** · <sub>yolonir · GitHub · ⭐ 7 · 2026-07-17</sub><br>Pi 编程 agent 中面向 MCP 服务器的沙箱化 Code Mode；可选的 Jev 路由取代搜索，按子任务意图给已启用的工具打分，最多挑出八个，并附上组合使用的指引。
- **[zcode-gatekeeper](https://github.com/luoxiaoxin123/zcode-gatekeeper)** · <sub>luoxiaoxin123 · GitHub · ⭐ 7 · 2026-09-13</sub><br>ZCode 编程 agent 的外部工具调用审批器，仿照 Claude Code 自动模式设计：结合任务审查 shell、文件和 MCP 操作，对破坏性命令用确定性黑名单，并可选接入 Jev 后端。
- **[pi-jev-compaction](https://www.npmjs.com/package/pi-jev-compaction)** · <sub>each1024 · 软件包 · ⬇ 690 · 2026-09-18</sub><br>Pi 编程 agent 扩展，用 Jev 对工具调用和结果做保留、丢弃或截断的决定，取代 LLM 摘要式压缩，出错时回退到 Pi 内置的摘要。
- **[WrongStack 的 Jev 决策](https://github.com/WrongStack/WrongStack/blob/main/docs/jev-settings-and-activity.md)** · <sub>WrongStack · GitHub · ⭐ 331 仓库 · 2026-09-18</sub><br>编程 agent WrongStack 中的 Jev 集成：一个 agent 可调用的 jev 工具用于有界判断，另有基于 Jev 的专业 agent 分派、skill 推荐和记忆召回，每项功能都可单独配置。
- **[algal-skills](https://www.npmjs.com/package/algal-skills)** · <sub>benzguo · 软件包 · ⬇ 624 · 2026-09-19</sub><br>面向 Devin、Claude Code 和 Codex 的省 token agent skill，把原始工具输出挡在上下文之外，可选由 Jev 回答关于 diff、来源和草稿的类型化分诊问题。
- **[auto-model-router](https://github.com/fstandhartinger/auto-model-router)** · <sub>fstandhartinger · GitHub · ⭐ 6 · 2026-09-17</sub><br>兼顾成本、缓存和配额的 LLM 路由器，带一个 Claude Code 网关垫片：由 Jev 类模型（托管的 Jev 或本地的 Laya）对每一轮的主题、难度和工具需求分类，再选出能胜任的最便宜模型。
- **[Cairn](https://github.com/eas4ai/cairn)** · <sub>eas4ai · GitHub · ⭐ 6 · 2026-08-10</sub><br>基于 Git 的记录体系，把 AI 辅助开发与约定好的需求挂钩；在关键抉择点，编程 agent 可以先让 Jev 从五个维度给自己的草案打分再做决定。
- **[czip](https://github.com/Jilazem/Czip)** · <sub>Jilazem · GitHub · ⭐ 6 · 2026-09-16</sub><br>把 Claude Code、Codex、Grok 和 Hermes 的 agent 会话压缩成可检索的包，新会话直接查询它而不必重新加载历史；可选的 Jev 闸门负责决定会话合并以及保留哪些大体积工具输出。
- **[fast-jev-compaction-laya](https://github.com/kaiyes/fast-jev-compaction-laya)** · <sub>kaiyes · GitHub · ⭐ 6 · 2026-09-20</sub><br>无需 key 的 opencode 插件，通过询问 Apple Silicon 上的本地 Laya 服务器来决定每个旧工具调用是保留、截断还是丢弃，以此压缩上下文，助手自己的消息保持不变，每次决策约 7-15 毫秒。
- **[jev-compact](https://github.com/fatelei/jev-compact)** · <sub>fatelei · GitHub · ⭐ 6 · 2026-09-19</sub><br>Codex CLI 插件，在压缩之前让 Jev 给每个工具调用及其结果打分，然后把 Jev 标记为仍然需要、却被 Codex 内置摘要丢掉的输出原样重新注入。
- **[jev-tool-router](https://github.com/jackbarunz/jev-tool-router)** · <sub>jackbarunz · GitHub · ⭐ 6 · 2026-09-20</sub><br>Codex 的 MCP 路由器，只暴露一个很小的路由接口而不是几百个工具 schema，由 Jev 根据名称和描述挑选一个外部工具，拿不准时返回一份候选名单。
- **[letcode](https://github.com/letr007/letcode)** · <sub>letr007 · GitHub · ⭐ 6 · 2026-06-10</sub><br>用 Rust 写的 Opencode 风格终端编程 agent，带 Ratatui TUI；它的实验性自动权限模式可以改为询问 Jev（而不是聊天式审查模型）是否放行每一次工具调用。
- **[nouls](https://github.com/benomahony/nouls)** · <sub>benomahony · GitHub · ⭐ 6 · 2026-09-17</sub><br>语义 linter 兼语言服务器，用 tree-sitter 把文件拆成函数，针对每个函数向 Jev 提是非题，检查 docstring 与实现脱节、缺少授权校验、重试不幂等之类的问题。
- **[oko](https://x.com/bartlomein/status/2101436827819192584)** · <sub>bartlomein · X · ♥ 6 · 2026-09-19</sub><br>面向编程 agent 的仓库搜索，在本地搜索后由 Jev 给匹配结果排序，让 agent 少读些东西；在一项 108 个会话的试点中，agent token 最多减少 46%，耗时减少 18%。
- **[OwnCode](https://github.com/muratmirgun/owncode)** · <sub>muratmirgun · GitHub · ⭐ 6 · 2026-09-18</sub><br>用 Go 写的实验性终端编程 agent，带工具审批、并行的 Witch worker 和可插拔的上下文压缩，其中有一个实验性的 Jev 模式，通过 Compact Engine 给符合条件的工具输出打分并缩短。
- **[pi-jev（压缩与路由）](https://github.com/iefnaf/pi-jev)** · <sub>iefnaf · GitHub · ⭐ 6 · 2026-09-18</sub><br>一组 Pi 扩展，用 Jev 做两件事：删掉过时的工具输出来压缩上下文，其余内容原样保留；按难度把每一轮路由到更便宜或更强的模型。
- **[pi-jev-context](https://github.com/Nyarlathoteppppp/pi-jev-context)** · <sub>Nyarlathoteppppp · GitHub · ⭐ 6 · 2026-09-18</sub><br>Pi 上下文扩展，折叠重复的文件读取，让 Jev 在硬性保留规则的约束下过滤冗长的命令日志，并把原文存成可搜索的逐字片段，不改写旧消息，也不动缓存前缀。
- **[SAYACODE](https://github.com/saya-ch/sayacode)** · <sub>saya-ch · GitHub · ⭐ 6 · 2026-04-30</sub><br>基于 LangChain 和 LangGraph 的本地终端编程 agent，其 <code>jev</code> 信任级别会自动批准低风险工具调用，把拿不准的交给用户，并拒绝明显越权的操作，使用官方 TypeSafe SDK。
- **[softlint](https://github.com/blazejkustra/softlint)** · <sub>blazejkustra · GitHub · ⭐ 6 · 2026-09-19</sub><br>GitHub Action 兼 CLI，用 Jev 按英文规则检查 pull request 里的每一处改动，并标出违规的行；在示例 PR 中抓到了 10/10 处违规，每个 PR 约 $0.001。
- **[Switchyard](https://github.com/LeonardSEO/switchyard)** · <sub>LeonardSEO · GitHub · ⭐ 6 · 2026-09-14</sub><br>能感知订阅情况的模型路由器，支持 Pi、Oh My Pi 和 OpenCode，通过 OpenRouter Decisions 让 Jev 判断每个编程任务的类型和复杂度，再挑选能胜任的最便宜模型和推理力度。
- **[DSCODE 的 Jev 审批插件](https://github.com/qiz029/dscode/tree/main/plugins/jev)** · <sub>qiz029 · GitHub · ⭐ 298 仓库 · 2026-09-11</sub><br>终端 DeepSeek 编程 agent 的插件，通过 OpenRouter 的 Decisions API 用 Jev 而不是对话模型来回应自动权限审查。
- **[Jev UX linter 扩展](https://x.com/naobit_/status/2101682262857363563)** · <sub>naobit_ · X · ♥ 4 · 2026-09-20</sub><br>日本开发者做的 Chrome 扩展，把 Jev 当作 UX linter 来评估网站体验：对每个组件并行问 Jev 多个问题，例如点击它的结果是否可预期。
- **[OrchestKit 的 Jev 会话分类](https://github.com/yonatangross/orchestkit/tree/main/docs/audits/jev-session-category-heldout-2026-09-17)** · <sub>yonatangross · GitHub · ⭐ 281 仓库 · 2026-09-17</sub><br>对 OrchestKit 中可选启用的 Claude Code Jev 会话分类器做的留出集评测：在 150 个会话上，同样的标准下 Jev 与 Haiku 表现相当（80.0% 对 79.3%），速度快约 58 倍，输入 token 少约 34 倍。
- **[Roomote 的判断后端](https://github.com/RooCodeInc/Roomote/blob/develop/packages/cloud-agents/src/server/typesafe-judgment.ts)** · <sub>RooCodeInc · GitHub · ⭐ 253 仓库 · 2026-07-07</sub><br>可自托管的云端编程 agent，带一个可选的 Jev 判断后端，用于范围受限的辅助决策，另有一个影子模式，衡量自己部署的判断模型与 Jev 的一致程度。
- **[Bicameral](https://github.com/AbdelStark/bicameral)** · <sub>AbdelStark · GitHub · ⭐ 5 · 2026-09-16</sub><br>面向 Pi 的混合式编程 harness：任意 LLM 负责写代码，Jev 给工具调用和编辑打分，再由确定性策略把分数转成放行、确认、拦截、警告或纠偏。
- **[claude-jev](https://github.com/buchmark/claude-jev)** · <sub>buchmark · GitHub · ⭐ 5 · 2026-09-18</sub><br>Claude Code 插件，把 Claude 的评审意见、调试假设和设计方案交给 Jev 作为独立裁判过一遍，剔除概率低于阈值的误报。
- **[coderelay](https://github.com/AlkaidSTART/coderelay)** · <sub>AlkaidSTART · GitHub · ⭐ 5 · 2026-09-12</sub><br>路由器，扫描本机已安装的编程 agent CLI（Claude Code、Codex、pi、omp），把每个任务派给最合适的那个，依据本地规则和打分，或在 <code>jev</code> 模式下由 Jev 解读任务意图来决定。
- **[codex-jev-router](https://github.com/tiandee/codex-jev-router)** · <sub>tiandee · GitHub · ⭐ 5 · 2026-09-21</sub><br>OpenAI Codex CLI 的本地桥接工具，运行一个回环 Responses API 代理，每开启新一轮就让 Jev 选择 Codex 模型和推理强度，Jev 不可用时沿用当前模型。
- **[Cortex](https://github.com/amitvijapur/cortex)** · <sub>amitvijapur · GitHub · ⭐ 5 · 2026-04-27</sub><br>位于 Claude Code、Cursor、Codex 等工具中各类编程 agent 工作流系统之上的元路由器，为每个任务选择工作流、专家角色和投入力度，可选用 Jev 顾问做任务分类。
- **[DiffJury](https://github.com/raihankhan-rk/diffjury)** · <sub>raihankhan-rk · GitHub · ⭐ 5 · 2026-09-17</sub><br>Next.js app，抓取一个公开 GitHub PR（标题、正文、diff、贡献者），一次调用就返回 Jev 给出的合并风险结论，包括 Score 条形图、Noul 概率和建议的评审深度。
- **[DLQ Inspector](https://github.com/HalxDocs/dlq_inspector)** · <sub>HalxDocs · GitHub · ⭐ 5 · 2026-08-08</sub><br>本地优先的 CLI，用于检查并安全恢复 RabbitMQ 和 Redis Streams 中的死信队列消息，可选开启的 Jev 辅助能处理基于规则的分类器标记为 INVESTIGATE 的故障。
- **[every](https://github.com/sufianetaouil/every)** · <sub>sufianetaouil · GitHub · ⭐ 5 · 2026-09-17</sub><br>以是/否问题作为匹配模式的 grep：评判代码库中的每一个函数，并按回答“是”的概率排序；实测在 gin-gonic/gin 的 1,302 个函数上耗时 3.7 s，花费 $0.018。
- **[Jev Code Finder](https://github.com/Peu77/JevFind)** · <sub>Peu77 · GitHub · ⭐ 5 · 2026-09-19</sub><br>用于语义代码搜索的 Rust CLI 和 agent skill：用大白话描述一个概念，即可得到相关文件、行范围、置信度分数和代码片段。
- **[JevOps](https://github.com/endomorphosis/JevOps)** · <sub>endomorphosis · GitHub · ⭐ 5 · 2026-09-18</sub><br>从 Lean Refactor Arena 拆分出来的 Jev 闸门内核，重构和自编码器模块提出 Lean 候选，只有 Lean/Lake 验证器能决定是否接纳。
- **[Magic Jev Ball](https://x.com/acharyaagamya/status/2101129105676861621)** · <sub>acharyaagamya · X · ♥ 5 · 2026-09-19</sub><br>GitHub pull request 上的恶搞按钮：先检查 CI、diff 大小和审查情况，再让 Jev 在约 200 毫秒内回答“该不该批准”。
- **[Pi Jev Guard](https://github.com/Reindeer-AI/pi-jev-guard)** · <sub>Reindeer-AI · GitHub · ⭐ 5 · 2026-09-19</sub><br>Pi 扩展，在代码修改写入之前对照仓库里的 Markdown 规则检查，对每处违规报告具体是哪条指令、哪段行号范围，在强制模式下则直接拦截。
- **[pi-jev-context-curator](https://github.com/Shashank-H/pi-jev-context-curator)** · <sub>Shashank-H · GitHub · ⭐ 5 · 2026-09-18</sub><br>Pi 扩展，在每次调用 LLM 前整理上下文：对每个新的消息单元问 Jev 一个 Noul，看它对后续回复是否必不可少，并按内容指纹复用以往的判断。
- **[S1Code](https://github.com/mertcicekci0/S1Code)** · <sub>mertcicekci0 · GitHub · ⭐ 5 · 2026-09-18</sub><br>Rust 终端编程 agent，由 Claude 或 OpenAI 规划并写代码，可选的 Jev 集成负责在完全确定的动作之间做选择，并帮助决定哪些证据留在活动上下文中。
- **[pi-fabric 的 Jev 程序](https://github.com/monotykamary/pi-fabric/blob/main/docs/jev.md)** · <sub>monotykamary · GitHub · ⭐ 244 仓库 · 2026-09-17</sub><br>Pi 编程 agent 的可编程工具运行时 pi-fabric 中的 Jev 支持：推理模型写一段 TypeScript 程序，在 QuickJS 里观察、询问 Jev、执行并循环，不再额外占用 LLM 轮次。
- **[jev-kit](https://www.npmjs.com/package/jev-kit)** · <sub>nikheal25 · 软件包 · ⬇ 480 · 2026-09-20</sub><br>agent 优先的 CLI，适用于 Cursor、Claude Code、Codex 和 Pi，把日志、diff 或文件通过管道交给 Jev，用 Noul、Choice 或 Score 参数提问，并输出 JSON 供 agent 或 jq 处理。
- **[Milo](https://www.npmjs.com/package/usemilo)** · <sub>banana.man · 软件包 · ⬇ 466 · 2026-09-20</sub><br>面向 pi、Codex、Claude Code 等编程 harness 的路由网关：把模型设为 milo/auto，每个请求都会经 Jev 路由到 OpenRouter 上的快速、中档或前沿模型。
- **[LeanKG judge](https://github.com/FreePeak/LeanKG/tree/main/internal/judge)** · <sub>FreePeak · GitHub · ⭐ 220 仓库 · 2026-04-13</sub><br>面向 AI 编程 agent 的代码知识图谱，加了一层 System One 判断层，调用 Jev 或自托管的 Laya 服务器，其中还包括一条对话分类路径。
- **[@elyracode/jev-tools](https://www.npmjs.com/package/@elyracode/jev-tools)** · <sub>Knut W. Horne · 软件包 · ⬇ 405 · 2026-09-18</sub><br>Elyra 编程 agent 的扩展，新增一个 decide 工具，可向 Jev 提出是/否、Choice 和 Score 问题，另有一个可选开启的 bash 闸门，在运行看起来具有破坏性的命令前先询问。
- **[claude-code-jev](https://github.com/RahulBalakavi/claude-code-jev)** · <sub>RahulBalakavi · GitHub · ⭐ 4 · 2026-09-18</sub><br>实验性的 PreToolUse hook，通过 OpenRouter 让 Jev 来执行 Claude Code 的放行/拦截/询问权限闸门，实测每次调用 264 毫秒、$0.0000227，在 18 个用例的测试集上放行危险操作 0 次。
- **[dsh-jev](https://github.com/zhangxaochen/dsh-jev)** · <sub>zhangxaochen · GitHub · ⭐ 4 · 2026-09-18</sub><br>DeepSeek Harness 的插件套件，包括工具结果裁剪、循环防护、安全防护和无头模式下的询问处理；其 20 个任务的 DeepSWE A/B 试点结果显示既没有优势，也没有稳定的负面影响。
- **[fast-jev (OpenCode plugin)](https://github.com/nrdz-labs/fast-jev-opencode)** · <sub>nrdz-labs · GitHub · ⭐ 4 · 2026-09-19</sub><br>OpenCode V2 插件，在每次发出模型请求时依据 Jev 分数丢弃过时的工具调用、截断体积庞大的工具结果，不改动已存储的历史和 /compact，出错时放行。
- **[Hunch](https://github.com/Kelbie/hunch)** · <sub>Kelbie · GitHub · ⭐ 4 · 2026-09-18</sub><br>CLI 和 Agent Skill，把范围内的每个代码块发给 Jev，在整个仓库范围内回答一个大白话问题，返回带分数的源码位置，还能对 diff 反复执行用大白话写的评审规则。
- **[JEV OAS Sentinel](https://github.com/ShuhanSun/jev-oas-sentinel)** · <sub>ShuhanSun · GitHub · ⭐ 4 · 2026-09-19</sub><br>GitHub Action 和 CLI，用确定性的结构检查比较两份 OpenAPI 文档，并对变更后的描述、默认值、重试、分页、鉴权和错误行为做语义审查。
- **[Jev PR Labeler](https://github.com/1jehuang/jev-pr-labeler)** · <sub>1jehuang · GitHub · ⭐ 4 · 2026-09-19</sub><br>通过 OpenRouter 的 Decisions API，按类型、领域、平台和规模给 GitHub pull request 打标签，其中规模反映的是概念上的范围，而不是改动行数。
- **[jev-codes](https://github.com/Kushwho/jev-codes)** · <sub>Kushwho · GitHub · ⭐ 4 · 2026-09-18</sub><br>CLI 和 agent 命令，按可编辑的 YAML 编码规范包逐个片段审计 git diff，让 agent 只修复被标记的片段；500 行的 diff 几秒内审完，花费不到一美分。
- **[jev-e2e](https://github.com/perixtar/jev-e2e)** · <sub>perixtar · GitHub · ⭐ 4 · 2026-09-18</sub><br>用大白话写 Web app 的端到端测试：Jev 在页面上挑选控件，Playwright 执行步骤，每个用例最终以 PASS、FAIL 或 BLOCKED 结束并附带证据。
- **[jev-harness](https://github.com/Astro-Han/jev-harness)** · <sub>Astro-Han · GitHub · ⭐ 4 · 2026-09-20</sub><br>极简编程 agent，每个工具结果在主模型看到之前都先经过 Jev 过滤，并附带 A/B 测试框架：启用过滤时 30 个任务通过 25 个，不启用时通过 22 个。
- **[jev-pref](https://github.com/doeixd/jev-pref)** · <sub>doeixd · GitHub · ⭐ 4 · 2026-09-17</sub><br>linter，把 AGENTS.md 中的偏好转成语义规则，由 Jev 在代码片段、暂存文件或 pull request 上检查，再把发现的问题反馈给你的编程 agent，配置工作也由这个 agent 完成。
- **[jev-spec](https://github.com/nozomi-koborinai/jev-spec)** · <sub>nozomi-koborinai · GitHub · ⭐ 4 · 2026-09-20</sub><br>CLI，对照 Markdown 规格中的需求检查代码，每条需求向 Jev 问一个问题，概率低于你设定的阈值时让 pre-commit hook 或 CI 构建失败。
- **[nlgrep](https://github.com/YehuiTang0316/jev-nlgrep)** · <sub>YehuiTang0316 · GitHub · ⭐ 4 · 2026-09-20</sub><br>面向代码、文档、日志和文本的自然语言 grep：Jev 针对你用自然语言写的条件对每个候选回答一个 Noul，再由 TypeScript 套用阈值，返回排好序的文件和对应的源码行。
- **[PiJev](https://github.com/tonyzdev/pijev)** · <sub>tonyzdev · GitHub · ⭐ 4 · 2026-09-17</sub><br>基于 Pi 的终端编程 agent，由 Jev 筛选候选 skill、给文件片段排序、对工具故障做分诊，代码则由你的编程模型来写；在 SWE-bench 的 django 任务上，工具调用次数比原版 Pi 少。
- **[Taste Lint](https://github.com/mblode/taste-lint)** · <sub>mblode · GitHub · ⭐ 4 · 2026-09-19</sub><br>CLI，在发布前揪出 UI 代码、文案和 agent 指令中 AI 粗制滥造的痕迹（AI slop），在本地跑机械性检查，并通过 Vercel AI Gateway 为语义层面的品味规则加上 Jev 审查意见。
- **[tenet](https://github.com/zoidsh/tenet)** · <sub>zoidsh · GitHub · ⭐ 4 · 2026-09-17</sub><br>给 agent 写的代码设的提交时审查闸门，每条规则只需用自然语言写一次，Jev 按规则评判每次提交，速度快到 agent 能在你看到 diff 之前就修好违规。
- **[interlinked-cli 的 Jev 检查](https://github.com/QuentinCody/interlinked-cli/tree/main/src/harness/jev)** · <sub>QuentinCody · GitHub · ⭐ 177 仓库 · 2026-09-17</sub><br>interlinked 中可选开启的 Jev 检查。interlinked 是编程 agent 的本地防护层，这些检查会标记测试内容与标题不符的测试，以及声称某模块已上线、实际却没有任何地方引用它的文档。
- **[Glowbom OSS 的 Jev 工具](https://github.com/glowbom/glowbom-oss/tree/main/extras/jev)** · <sub>glowbom · GitHub · ⭐ 163 仓库 · 2023-04-07</sub><br>Project Book 编程 agent 工作流中的可选工具，让 agent 通过 OpenCode 向 Jev 询问一些小决策，例如构建和测试结果看起来是否正常、是否还需要再修一次。
- **[SpecWeave sw:jev](https://github.com/anton-abyzov/specweave/blob/develop/docs-site/docs/guides/jev-system-one.md)** · <sub>anton-abyzov · GitHub · ⭐ 163 仓库 · 2025-10-25</sub><br>面向 Claude Code、Codex 和 Cursor 的规格优先 AI 开发工具包，内置 sw:jev skill，借助 Jev 在约 250 毫秒内做封闭集合内的决策。
- **[Epistemic Protocols Route](https://github.com/jongwony/epistemic-protocols/tree/main/route)** · <sub>jongwony · GitHub · ⭐ 162 仓库 · 2025-12-25</sub><br>Claude Code 插件，根据会话上下文的缺陷把它路由到相应的认知协议，可选开启的 Jev 建议通道最多会提示三个协议。
- **[Context Diet](https://github.com/konstantinosbotonakis/codex-context-diet)** · <sub>konstantinosbotonakis · GitHub · ⭐ 3 · 2026-09-18</sub><br>Codex 插件，询问 Jev 会话还需要哪些体积庞大的工具结果（如测试日志、构建输出和大文件读取），其余的替换为截断后的开头部分加一行说明。
- **[deepseek-harness-jev-pre-compaction](https://github.com/wjw66/deepseek-harness-jev-pre-compaction)** · <sub>wjw66 · GitHub · ⭐ 3 · 2026-09-21</sub><br>DeepSeek Harness 的预压缩顾问，在达到压缩阈值之前，从模型可见的上下文中裁掉低价值的工具结果，原始事件仍保留在只追加日志里。
- **[dsh-jev-prune](https://github.com/yangyu666/dsh-jev-prune)** · <sub>yangyu666 · GitHub · ⭐ 3 · 2026-09-21</sub><br>DeepSeek Harness 插件，用 Jev 的保留/丢弃判断取代按大小裁剪工具结果和基于摘要的压缩，另有确定性的回执压缩，判断后端可插拔。
- **[fast-compaction-dsh](https://github.com/kolawong/fast-compaction-dsh)** · <sub>kolawong · GitHub · ⭐ 3 · 2026-09-20</sub><br>fast-jev-compaction 的 DeepSeek Harness 移植版，用逐次调用的保留、截断或丢弃决策取代有损的摘要，保留下来的内容全部原样保存。
- **[fast-dev-compaction](https://github.com/leonaaardob/fast-dev-compaction)** · <sub>leonaaardob · GitHub · ⭐ 3 · 2026-09-18</sub><br>fast-jev-compaction 的 Codex 移植版：在 Codex 压缩之前，由 Jev 给每个工具调用及其结果打分，压缩后再把保留下来的原始历史重新注入；作者称其为实验性的概念验证。
- **[jcm-router](https://github.com/adarshmishra07/jcm-router)** · <sub>adarshmishra07 · GitHub · ⭐ 3 · 2026-09-17</sub><br>位于 Claude Code 和 Anthropic API 之间的本地代理，用 Jev 为每条消息选择模型和推理强度；日志显示主对话中切换模型会因缓存重写损失 $19.53，因此它只对子 agent 做路由。
- **[Jev Auto Router](https://github.com/miniLV/Jev-Auto-Router)** · <sub>miniLV · GitHub · ⭐ 3 · 2026-08-01</sub><br>Codex 本地 Responses 代理的原型，由 Jev 为每次模型调用选择 GPT 模型和推理强度，之后再独立检查任务是否真的完成。
- **[Jev Codex Token Saver](https://github.com/jcressler/jev-codex-token-saver)** · <sub>jcressler · GitHub · ⭐ 3 · 2026-09-19</sub><br>Codex 插件，其 MCP 服务器在本地收集搜索和日志证据，让 Jev 给一个有界的候选包打相关性分数，只返回选中的原文片段，把大体积结果挡在上下文之外。
- **[Jev Workflows for Codex](https://github.com/integrate-your-mind/jev-codex-plugin)** · <sub>integrate-your-mind · GitHub · ⭐ 3 · 2026-09-18</sub><br>Codex 插件，包含一个 MCP 服务器、十二个生命周期适配器和三个 skill，会就工具、模型、skill 和策略征询 Jev，诊断失败的命令，并对照证据核查“已完成”的说法。
- **[jev-assist](https://github.com/glud123/jev-assist)** · <sub>glud123 · GitHub · ⭐ 3 · 2026-09-20</sub><br>agent skill 和 CLI，针对一句话描述的任务，让 Jev 对每个被跟踪的文件问同一个相关性问题，让编程 agent 从真正需要的少数几个文件开始；validate 命令会对照历史提交给排序结果打分。
- **[jev-classifier](https://github.com/felpsdev/jev-classifier)** · <sub>felpsdev · GitHub · ⭐ 3 · 2026-09-18</sub><br>本地网关和 MCP 工具，让 Jev 预测 Codex、Claude Code 或 OpenCode 等编程 agent 下一步该调用哪个工具，先作为记录下来的建议，在支持的情况下再作为实际选择。
- **[jev-flash-router](https://github.com/Ravinder82/jev-flash-router)** · <sub>Ravinder82 · GitHub · ⭐ 3 · 2026-09-18</sub><br>适用于 Cursor、Windsurf、Claude Desktop 和 Claude Code 的 MCP 服务器，让编程 agent 把小决策（比如该改哪个文件、某个 diff 会不会让测试挂掉）通过 OpenRouter 交给 Jev，约 150 毫秒 返回。
- **[jev-gate](https://github.com/MongLong0214/jev-gate)** · <sub>MongLong0214 · GitHub · ⭐ 3 · 2026-09-17</sub><br>实验性的 Claude Code 模型路由：由 Sonnet 负责协调，一个只读规划器拆解任务，Jev 为每个委派出去的规划和工人任务选择模型档位；目前尚未证实有成本收益。
- **[jev-judgment](https://github.com/HyunjunJeon/jev-judgment)** · <sub>HyunjunJeon · GitHub · ⭐ 3 · 2026-09-17</sub><br>Agent Skill，让编程 agent 在向用户提问之前、执行有风险或超出范围的操作之前，以及失败后决定是否重试时，先把封闭式问题发给 Jev，约 250 毫秒 返回，没有 key 时放行。
- **[jev-model-router (Claude Code)](https://github.com/satviksinha/jev-model-router)** · <sub>satviksinha · GitHub · ⭐ 3 · 2026-09-20</sub><br>Claude Code hook，每轮开始前询问 Jev 该由 Haiku 到 Fable 之间的哪个档位来回答、思考要多深，然后把这一轮的所有模型请求都发给选中的模型。
- **[jev-skill-gate](https://github.com/ShivamPansuriya/jev-skill-gate)** · <sub>ShivamPansuriya · GitHub · ⭐ 3 · 2026-09-17</sub><br>Claude Code hook，对照当前项目给每个已安装的 skill 打分，并通过 skillOverrides 隐藏其余的 skill；在装有 217 个 skill 的环境中把 12,750 个 token 降到 3,185 个，每个会话花费 $0.0009。
- **[jev.nvim](https://github.com/valentynkit/jev.nvim)** · <sub>valentynkit · GitHub · ⭐ 3 · 2026-09-18</sub><br>Neovim 插件，对当前 buffer 中每个 Treesitter 识别出的函数问同一个大白话问题，让 Jev 逐个打分，并把命中结果按概率排序列在 quickfix 中，分数以虚拟文本显示。
- **[jevtest](https://github.com/realZachi/jevtest)** · <sub>realZachi · GitHub · ⭐ 3 · 2026-09-19</sub><br>Vitest 和 Jest 的语义匹配器：用大白话写出期望，由 Jev 对一个窄范围问题给出的概率决定通过与否，通常耗时 150 毫秒 到 1.5 s。
- **[JMP](https://github.com/morcoan/JMP)** · <sub>morcoan · GitHub · ⭐ 3 · 2026-09-18</sub><br>本地桌面编程 agent：Jev 根据请求和真实历史选择下一个动作，选定的生成模型（DeepSeek、OpenAI 或本地 Bonsai）填充参数，再由 OpenHands 或 MCP 工具执行。
- **[Leanest](https://github.com/baronunread/leanest)** · <sub>baronunread · GitHub · ⭐ 3 · 2026-09-17</sub><br>本地优先的测试选择器，挡在现有测试运行器前面，跳过被判定不受代码改动影响的测试，默认使用 classifier.dev，也可以用 Jev/Laya。
- **[opencode-jev-orchestrator](https://github.com/aaronshaf/opencode-jev-orchestrator)** · <sub>aaronshaf · GitHub · ⭐ 3 · 2026-09-18</sub><br>OpenCode 插件，让会话固定在一个便宜的父模型上以保持缓存热度，只把难的轮次升级给临时子 agent 里更强的模型。
- **[semantic-assert](https://github.com/mondaychen/semantic-assert)** · <sub>mondaychen · GitHub · ⭐ 3 · 2026-09-19</sub><br>测试库，用于断言关于捕获到的 UI 或文本 state 的英文陈述（比如某条提示是否告诉用户如何恢复），默认由 Jev 评判，通过阈值写在代码里，另附 Playwright 辅助函数。
- **[software-factory](https://github.com/stratonext/software-factory)** · <sub>stratonext · GitHub · ⭐ 3 · 2026-09-21</sub><br>本地软件工厂，让需求沿着由编程 agent、shell 和 Jev 步骤组成的 YAML 流水线推进，其中 typesafe 步骤用带类型的问题评判 diff，再把它送去审查或打回重新编码。
- **[octomind evaluate](https://github.com/Muvon/octomind/blob/master/src/commands/evaluate.rs)** · <sub>Muvon · GitHub · ⭐ 140 仓库 · 2025-06-01</sub><br>CLI 优先的 AI 编程 agent 运行时，带一个 evaluate 命令，把 JSON state 和带类型的问题发给 Jev 这类评测模型，其中包括校准过的检查。
- **[5chan 的 Jev 开发辅助脚本](https://github.com/bitsocialnet/5chan/tree/master/scripts/jev)** · <sub>bitsocialnet · GitHub · ⭐ 132 仓库 · 2023-01-29</sub><br>一个点对点图片论坛的可选 Node 脚本，用 Jev 做浏览器测试规划和基准测试、盲审交接以及对比式翻译评测。
- **[pi-maestro-flow 的 JEV 分类器](https://github.com/catlog22/pi-maestro-flow/tree/master/packages/pi-maestro-teammate/src/classify)** · <sub>catlog22 · GitHub · ⭐ 126 仓库 · 2026-07-07</sub><br>Pi 编程 agent 的多 agent 编排，带一个统一的 JEV 分类器，把 provider 故障归入不同的重试类型，并把交接文件标记为必需、视情况而定或跳过。
- **[Claude Lane Stack 的 Jev skill](https://github.com/VKirill/claude-lane-stack/blob/main/bin/jev_decisions.py)** · <sub>VKirill · GitHub · ⭐ 116 仓库 · 2026-07-11</sub><br>面向 Claude Code 的单人多 agent 编程工厂，其中的 Jev skill 通过 TypeSafe 或 OpenRouter 审查 git diff 片段，并基于 DOM 表格做浏览器 QA。
- **[Radiant 决策](https://github.com/templetongroup/radiant/blob/master/server/decide.js)** · <sub>templetongroup · GitHub · ⭐ 106 仓库 · 2026-08-19</sub><br>本地 Mac 编程 harness，通过 OpenRouter 用 Jev 挑选一条消息需要哪些 MCP 服务器；起因是发现单个 Linear 服务器就给每次调用加了 69 个工具 schema 和 16.6k token。
- **[Harness MCP 的故障分诊](https://github.com/harness/mcp-server/blob/main/src/client/typesafe-client.ts)** · <sub>harness · GitHub · ⭐ 102 仓库 · 2025-05-14</sub><br>官方 Harness.io MCP 服务器，其 harness_diagnose 工具用单个 TypeSafe Choice 为流水线故障增加建议性的故障类别分诊。
- **[Eva 的 Jev 功能](https://github.com/vvedantb/eva/tree/main/packages/backend/convex/_jev)** · <sub>vvedantb · GitHub · ⭐ 101 仓库 · 2026-01-11</sub><br>云沙箱编程 agent 编排器，用 Jev 处理任务标签、问题分诊、草稿就绪判断、提及的紧急程度和 skill 标签，答案缺失时读取逻辑会回退处理。
- **[clear-head](https://github.com/VladyslavHontar/clear-head)** · <sub>VladyslavHontar · GitHub · ⭐ 2 · 2026-09-18</sub><br>Claude Code 的 Stop hook，把助手回答中的事实性说法与本次会话中它实际读过的工具输出进行比对，一旦说法被反驳或缺乏支撑就拦下这一轮。
- **[codex-jev-compaction](https://github.com/Wang-auspicious/codex-jev-compaction)** · <sub>Wang-auspicious · GitHub · ⭐ 2 · 2026-09-18</sub><br>Codex 插件，包含 skill、MCP 工具和 CLI，通过让 Jev 挑选哪些旧的只读工具记录需要原样保留，为下一个任务或会话构建紧凑、可追溯的交接包。
- **[git-jev-stage](https://github.com/ibrahemid/git-jev-stage)** · <sub>ibrahemid · GitHub · ⭐ 2 · 2026-09-18</sub><br>Git CLI，依据一句话描述的暂存意图对每个改动片段分类，展示暂存计划，确认后把选中的片段加入暂存区。
- **[guesswork](https://github.com/FindMalek/guesswork)** · <sub>FindMalek · GitHub · ⭐ 2 · 2026-09-18</sub><br>fish 风格的 zsh 行内自动补全，询问 Jev 你正在重新输入的是哪条最近的历史命令，因此缩写和模糊匹配也能生效，而不只是前缀匹配。
- **[JEV Codex Pilot](https://github.com/Charlyhno-eng/jev-codex-pilot)** · <sub>Charlyhno-eng · GitHub · ⭐ 2 · 2026-09-19</sub><br>带看板流程的本地控制中心，把软件工单转成 Codex 运行，按工单选择模型和推理强度，并压缩过长的对话线程，估计在混合负载下可减少 20-40% 的 token。
- **[Jev Frontend QA](https://github.com/Nainish-Rai/jev-frontend-qa)** · <sub>Nainish-Rai · GitHub · ⭐ 2 · 2026-09-17</sub><br>以证据驱动的前端 QA harness：Jev 负责挑选浏览器操作和目标，测试代码则依据 DOM、HTTP 和 SQLite 证据检查预先编写的契约，以一个合成的待办事项 app 作演示。
- **[Jev 原生工具路由器](https://github.com/micic-mihajlo/jev-tool-runner)** · <sub>micic-mihajlo · GitHub · ⭐ 2 · 2026-09-18</sub><br>Codex CLI 的封装层，在编程模型运行之前由 Jev 选出下一个原生工具调用，再由 Codex 在自身的审批和沙箱机制下执行。
- **[Jev Skill Router for Codex](https://github.com/droid-Q/jev-skill-router)** · <sub>droid-Q · GitHub · ⭐ 2 · 2026-09-18</sub><br>Codex 插件，让 Jev 挑选每个请求适用哪些 skill，把它们的路径和相关性概率传给 Codex，并附带一个本地分析看板。
- **[jev-browser-qa](https://github.com/jonymusky/jev-browser-qa)** · <sub>jonymusky · GitHub · ⭐ 2 · 2026-09-19</sub><br>浏览器 QA 工具：Playwright 负责驱动和录制，Jev 负责判断自然语言断言、修复定位器，并执行目标驱动的点击循环，附带面向 agent 的 JSON 流程 CLI 和运行看板。
- **[jev-builder-loop](https://github.com/rainbowpuffpuff/jev-builder-loop)** · <sub>rainbowpuffpuff · GitHub · ⭐ 2 · 2026-09-16</sub><br>Grok skill，在构建类 agent 循环的边界处把 Jev 当作判断传感器，把它给出的概率与先验结合来选择下一步动作，以交付一个已签名的 Android App Bundle 作为基准测试。
- **[Jev-chooses-a-LLM](https://github.com/Bodila51/Jev-chooses-a-LLM)** · <sub>Bodila51 · GitHub · ⭐ 2 · 2026-09-20</sub><br>通过 MCP 暴露的 Cursor 路由器，由 Jev 为每个任务选择成本优先、均衡或智能优先的路线，Cursor 再委派给对应的子 agent 或模型。
- **[jev-ci-selector](https://github.com/guilhem/jev-ci-selector)** · <sub>guilhem · GitHub · ⭐ 2 · 2026-09-19</sub><br>GitHub Action：你描述每个 CI 检查验证的内容，Jev 读取 PR diff 后输出布尔值，决定运行哪些 job，附带纯粹的策略引擎和影子模式。
- **[jev-codex-model-and-effort-router](https://github.com/gholtzap/jev-codex-model-and-effort-router)** · <sub>gholtzap · GitHub · ⭐ 2 · 2026-09-18</sub><br>macOS 上的 Codex 封装层，为对话线程中的第一个任务选择模型和推理强度并固定下来以保持缓存命中，附带一个用于路由设置的菜单栏 app。
- **[jev-harness](https://github.com/ismaelsoilet/jev-harness)** · <sub>ismaelsoilet · GitHub · ⭐ 2 · 2026-09-21</sub><br>编程 agent 的决策 harness，用 Jev 的 Choice、Score 和 Noul 闸门对测试失败（例如缺包或网络不稳定）进行分诊，并在前沿模型烧 token 之前掐断原地打转的死循环。
- **[jev-lint](https://github.com/zdenham/jev-lint)** · <sub>zdenham · GitHub · ⭐ 2 · 2026-09-19</sub><br>用大白话写项目规范的 linter，规范可以写在行内或 Markdown 里，用来检查 JavaScript 和 TypeScript 代码，Jev 以专为编程 agent 设计的紧凑格式报告可能的违规。
- **[jev-mode](https://github.com/ddfeyes/jev-mode)** · <sub>ddfeyes · GitHub · ⭐ 2 · 2026-09-18</sub><br>零依赖的 Python CLI，把编程 agent 的大批量语义判断（如工单分诊或文件打标签）从其上下文中移出去交给 Jev；在 1,000 次分诊判断上 token 用量减少了 77.8%。
- **[jev-rust-review](https://github.com/kindintelligence/jev-rust-review)** · <sub>kindintelligence · GitHub · ⭐ 2 · 2026-09-19</sub><br>用于 Rust 代码评审的 Claude Code 插件，先在改动行上运行 rustc、Clippy 和 cargo-semver-checks，再用 Jev 和 Claude 找出工具漏掉的问题，例如不具备取消安全性的 select! 分支或 split-lock 竞争。
- **[jev-scout](https://github.com/AkashPriyadarshii/jev-scout)** · <sub>AkashPriyadarshii · GitHub · ⭐ 2 · 2026-09-18</sub><br>Rust CLI 和 MCP 服务器，根据描述的需求从实时的注册表元数据中查找 GitHub 仓库和 Rust crate，再让 Jev 给契合度和维护状况信号打分来挑选候选，而不是让 LLM 去猜名字。
- **[jevopt](https://github.com/Ramneet-Singh/jevopt)** · <sub>Ramneet-Singh · GitHub · ⭐ 2 · 2026-09-20</sub><br>C/C++ 编译器驱动，把 Clang 的优化器与 Jev 搭配使用，在每个可自由决定的调用点上，依据 LLVM IR、原始源码和构建上下文询问 Jev 是否要内联。
- **[JevPromptCoach](https://github.com/CrowdLinker/JevPromptCoach)** · <sub>CrowdLinker · GitHub · ⭐ 2 · 2026-09-18</sub><br>Claude Code 插件，给你写给编程 agent 的提示词打分，并展示你的习惯是否在进步，不增加延迟；回填一整年的本地历史记录约花六美分。
- **[jevprune](https://github.com/ibrahemid/jevprune)** · <sub>ibrahemid · GitHub · ⭐ 2 · 2026-09-18</sub><br>Claude Code 插件和 CLI，在 agent 读取之前把冗长的命令输出过滤到只剩与任务描述相关的行；一次有记录的运行把 2,979 行的测试日志缩减到 54 行。
- **[limpet](https://github.com/noplan-inc/limpet)** · <sub>noplan-inc · GitHub · ⭐ 2 · 2026-09-17</sub><br>Claude Code 和 Codex 的 Stop hook：agent 每次想停下时，由 Jev 按你用自然语言写的规则打分，耗时约 0.7 秒，一旦违反规则就把 agent 打回去继续干活。
- **[pi-fast-jev-compaction](https://github.com/KamilPostrozny/pi-fast-jev-compaction)** · <sub>KamilPostrozny · GitHub · ⭐ 2 · 2026-09-18</sub><br>fast-jev-compaction 的 Pi 包移植版，利用 Pi 非破坏性的上下文 hook 丢弃不再需要的旧工具调用和结果，不改写正文，也不动已保存的对话记录。
- **[pi-fast-jev-compaction (QuentinDanblon)](https://github.com/QuentinDanblon/pi-fast-jev-compaction)** · <sub>QuentinDanblon · GitHub · ⭐ 2 · 2026-09-18</sub><br>fast-jev-compaction 在 Pi 编程 agent 上的移植，询问 Jev 每个旧工具调用及其结果是否仍然需要，丢弃或截断过时的部分，其余内容原样保留。
- **[pi-jev-compaction](https://github.com/nourhelmi/pi-jev-compaction)** · <sub>nourhelmi · GitHub · ⭐ 2 · 2026-09-18</sub><br>自动运行的 Pi 扩展，不再把过时的工具输出发给模型，同时保留对话，并且无需重跑命令就能取回原始输出；不使用摘要模型。
- **[pi-jev-context](https://github.com/kevinpita/pi-jev-context)** · <sub>kevinpita · GitHub · ⭐ 2 · 2026-09-18</sub><br>可选启用的 Pi 扩展，在后续的模型请求中隐藏较早且价值低的消息，同时保留完整的会话历史，并带有感知分支的缓存。
- **[siftr](https://github.com/Bentlybro/siftr)** · <sub>Bentlybro · GitHub · ⭐ 2 · 2026-09-19</sub><br>CLI 兼 MCP 服务器，为编程 agent 提供只读的搜索、读取、挑选和过滤工具，约 2 秒就能找到正确的文件和行；在 82% 的 SWE-bench Lite issue 上，正确文件都排在前 5 名。
- **[siftr](https://github.com/Bentlybro/jevgrep)** · <sub>Bentlybro · GitHub · ⭐ 2 · 2026-09-19</sub><br>CLI 兼 MCP 服务器，为编程 agent 提供四个只读 Jev 工具，分别用于语义搜索、聚焦读取、挑选测试文件和过滤日志，并在 SWE-bench Lite 上做了基准测试。
- **[Skillful](https://github.com/bestagentkits/jev-skillful)** · <sub>bestagentkits · GitHub · ⭐ 2 · 2026-09-17</sub><br>编程 agent 的能力路由器，把每条提示词与你已安装的 skill、MCP 服务器、子 agent 和斜杠命令做匹配，最多注入一条建议，并衡量它是否真的有帮助。
- **[Switchboard](https://github.com/ruban-24/switchboard)** · <sub>ruban-24 · GitHub · ⭐ 2 · 2026-09-20</sub><br>Claude Code 和 Codex 的本地路由器，用 Jev 评估新对话的任务，套用确定性的置信度规则选择模型和推理力度，并在后续追问中沿用这条路由。
- **[Typesafe Migration Guard](https://github.com/opaielsheikh/typesafe-migration-guard)** · <sub>opaielsheikh · GitHub · ⭐ 2 · 2026-09-17</sub><br>CI/CD 闸门，在数据库迁移 DDL 抵达 Supabase PostgreSQL 数据库之前做评估，以 HTTP 403 拦截 DROP TABLE 或 DROP COLUMN 这类破坏性操作。
- **[TypeSafe-as-a-Judge](https://github.com/E-FL/typesafe-as-a-judge)** · <sub>E-FL · GitHub · ⭐ 2 · 2026-09-21</sub><br>非官方的 Codex 与 Claude Code MCP 插件，为编程 agent 提供范围受限的 Jev 工具，用于分派工作、给候选排序、抽取信息、核验证据以及决定何时升级给人工审查，决定权仍在 agent 手里。
- **[typesafe-mod](https://github.com/BeLazy167/typesafe-mod)** · <sub>BeLazy167 · GitHub · ⭐ 2 · 2026-09-17</sub><br>Claude Code 函数 hook，为每条提示词给已安装的 skill 排序；agent 提出二选一的问题时，显示 Jev 对每个选项给出的概率，还可以选择自动作答。
- **[windows-save-token-jev-setup](https://github.com/455-dIAO/windows-save-token-jev-setup)** · <sub>455-dIAO · GitHub · ⭐ 2 · 2026-09-20</sub><br>Windows 版 Codex skill，负责安装并验证 save-token-jev hook：PreCompact hook 让 Jev 挑出值得保留的工具记录，SessionStart hook 在原生压缩之后把它们恢复回来。
- **[shell.online 的 Jev 评估](https://github.com/TeoSlayer/shell.online/tree/main/app/server/lib/jev)** · <sub>TeoSlayer · GitHub · ⭐ 99 仓库 · 2026-08-22</sub><br>把任意终端进程分享为加密浏览器链接的服务，新增可选启用的 Jev 建议性评估，只针对所有者从会话中明确公开的片段。
- **[deletion-test skill](https://github.com/obie/skills/tree/main/skills/deletion-test)** · <sub>obie · GitHub · ⭐ 95 仓库 · 2026-02-06</sub><br>Claude Code skill，检验一个模块能否根据其规格重新生成，在行为 diff 打分之后可选用 Jev 对存活的变异体做分诊。
- **[Snow App 的决策模型](https://github.com/MayDay-wpf/snow-app/blob/main/native/src/api/jev.rs)** · <sub>MayDay-wpf · GitHub · ⭐ 76 仓库 · 2026-06-10</sub><br>集 AI 聊天、终端和 SSH 于一体的开发者桌面应用，在 agent 审查循环中用 Jev 过滤搜索结果，并决定敏感命令能否不经确认直接执行。
- **[SztuCode 的 LLM + Jev agent 模式](https://github.com/rojim666/SztuCode/blob/main/packages/runtime-ts/src/jev.ts)** · <sub>rojim666 · GitHub · ⭐ 71 仓库 · 2026-07-24</sub><br>面向高校的本地优先编程与办公 agent，其实验模式让 LLM 负责推理，在关键的选择点上请 Jev 从备选的下一步动作中选一个。
- **[autoloop 的 Jev 路由](https://github.com/mikeyobrien/autoloop/blob/main/packages/harness/src/jev-routing.ts)** · <sub>mikeyobrien · GitHub · ⭐ 70 仓库 · 2026-03-28</sub><br>从 ralph-orchestrator 分出来的循环 harness，用于长时间运行的 agent 工作，可选开启 Jev 工作流选择，在置信度高于下限时把请求路由到某个预设或 no_match。
- **[PLang 的 Typesafe 决策器](https://github.com/PLangHQ/plang/blob/main/PLang/Services/Typesafe/TypesafeDecider.cs)** · <sub>PLangHQ · GitHub · ⭐ 65 仓库 · 2023-12-03</sub><br>一门自然语言编程语言，其构建器可以让 Jev 为每一步决定用哪个模块、方法和参数，每次请求批量提多个问题。
- **[SuperQode SystemOne Tune](https://x.com/Shashikant86/status/2101668569201160634)** · <sub>Shashikant86 · 文章 · ♥ 1 · 2026-09-20</sub><br>为类 Jev 模型打造的 SuperQode SystemOne harness 新增了基于 GEPA 的调优，能利用无标注的历史记录改进 Jev 在工具闸门和工单路由上的类型化答案，同时不会悄悄改写受信任的决策包。
- **[Mjolnir 的 Jev 轮次裁决](https://github.com/BrokkAi/mjolnir/tree/master/services/jev-proxy)** · <sub>BrokkAi · GitHub · ⭐ 63 仓库 · 2026-05-18</sub><br>面向 Codex、Claude Code 和其他 ACP 编程 agent 的元 harness，用 Jev 判断某一轮是需要用户输入还是属于后台工作，并给帮助搜索的条目排序。
- **[Parcha recall 的 Jev 判断](https://github.com/Parcha-ai/parcha-skills/tree/main/recall)** · <sub>Parcha-ai · GitHub · ⭐ 60 仓库 · 2026-07-13</sub><br>用于回忆过往编程 agent 会话的 agent skill，正在把基于正则的日期解析、重复检测和内容分诊迁移到 Jev 判断上，第一步是一个尚未启用的边界层和一个回放 harness。
- **[EntropyLab 的 Jev 对抗测试](https://github.com/OogaBoogaX/entropylab/blob/rock/test/adversarial/jev.mjs)** · <sub>OogaBoogaX · GitHub · ⭐ 58 仓库 · 2026-08-25</sub><br>一个离线比特币钱包计算器的定时 CI 任务，用恶意输入探索构建出的页面，并让 Jev 评判结果；没有 key 时降级为不变量检查。
- **[AIOS 判断闸门](https://github.com/rexleimo/aios/tree/main/scripts/lib/judgment)** · <sub>rexleimo · GitHub · ⭐ 54 仓库 · 2026-03-01</sub><br>面向长周期编程 agent 的本地优先控制平面，带一个可选的 System One 判断闸门，以 CLI 和 MCP 工具形式提供，除非显式启用否则保持关闭，出错时默认拒绝。
- **[SuperQode 的 Jev 决策 harness](https://github.com/SuperagenticAI/superqode/blob/main/docs/advanced/jev-tool-routing.md)** · <sub>SuperagenticAI · GitHub · ⭐ 53 仓库 · 2026-01-19</sub><br>基于 ACP、A2A 和 MCP 的编程 agent harness 层，加入一个用于工具路由和工具权限检查的 Jev 决策 harness，附带基准测试和可部署的 Jev 后端。
- **[PZ_Optimization Jev harness](https://github.com/xD3I/PZ_Optimization/blob/master/harness/typesafe_client.py)** · <sub>xD3I · GitHub · ⭐ 52 仓库 · 2026-09-15</sub><br>Project Zomboid 的性能补丁项目，其基准测试 harness 用 Jev 判断运行性能提升和画面一致性，并通过 OCR 加 Jev 操作游戏的 Workshop 界面，每步约 1.5 秒。
- **[ask-jev](https://github.com/omni-/ask-jev)** · <sub>omni- · GitHub · ⭐ 1 · 2026-09-16</sub><br>Codex 的 PowerShell hook，通过 :jev 命令对本地编程会话的执行记录做一次显式的建议性 Jev 审计，判断其中的说法是否有证据支撑。
- **[ask-jev](https://github.com/logicrw/ask-jev)** · <sub>logicrw · GitHub · ⭐ 1 · 2026-09-20</sub><br>只用标准库的 Python CLI，为编程 agent 和流水线提供失败时放行（fail-open）的建议性决策，以及逐字的段落选取，推理和行动的决定权仍留在调用方 agent 手里。
- **[Bouncer](https://github.com/clownware/bouncer)** · <sub>clownware · GitHub · ⭐ 1 · 2026-09-18</sub><br>Claude Code 的 PreToolUse hook，让 Jev 针对每次工具调用回答 YAML 策略里用大白话写的问题，约 100 毫秒 内决定放行或拒绝，每天成本约四美分，另有确定性的“绝不允许”规则。
- **[claude-jev-mod](https://github.com/chrishan17/claude-jev-mod)** · <sub>chrishan17 · GitHub · ⭐ 1 · 2026-09-19</sub><br>Claude Code 的 mod，向其他插件暴露 $.jev，让 hook 能向 Jev 提出 Choice、Score 和 Noul 问题并读取校准过的概率，支持包括 OpenRouter 和 Vercel AI Gateway 在内的六个 provider。
- **[Codex Jev Router](https://github.com/suenot/codex-jev-router)** · <sub>suenot · GitHub · ⭐ 1 · 2026-09-23</sub><br>使用 Jev 的 Choice 和 Noul 判断，通过本地置信度门槛选择 Codex 子代理的模型与推理档位；判断不确定时回退到 Sol。
- **[commentcop](https://github.com/ntedvs/commentcop)** · <sub>ntedvs · GitHub · ⭐ 1 · 2026-09-17</sub><br>CLI，读取 JS/TS 注释及其周围代码，从准确性和有用性两方面打分（满分 100），把最差的注释排在最前；检查 159 条注释花费约 $0.008。
- **[cursor-clijev-compaction](https://github.com/kleosr/cursor-clijev-compaction)** · <sub>kleosr · GitHub · ⭐ 1 · 2026-09-18</sub><br>Cursor CLI agent 的上下文恢复插件，记录工具调用及其结果，让 Jev 用原子化的 Noul 问题逐条打分，并在原生压缩之后把保留下来的事实原样重新注入。
- **[hush](https://github.com/emreozyoruk/hush)** · <sub>emreozyoruk · GitHub · ⭐ 1 · 2026-09-20</sub><br>GitHub Action，一次 Jev 调用即可给新 issue 打标签，并标记垃圾内容、需要更多信息和疑似重复，只有超过维护者设定的阈值才会执行对应动作，低于阈值则保持沉默；每个 issue 耗时 202-530 毫秒。
- **[Jev Context](https://github.com/zbush/jev-context)** · <sub>zbush · GitHub · ⭐ 1 · 2026-09-17</sub><br>本地的 Codex 代码搜索插件，运行 ripgrep 后对每个段落向 Jev 问一个是/否相关性问题，只返回很可能匹配的结果，并成对记录请求内容以衡量节省的 token。
- **[Jev for Amp](https://github.com/thesammykins/jev_ampcode)** · <sub>thesammykins · GitHub · ⭐ 1 · 2026-09-18</sub><br>Amp 编程 agent 的建议性插件，用一个 Jev Choice 依据给定的证据和优先级，对给定的备选方案（如不同实现思路）进行比较。
- **[Jev Issue Radar](https://github.com/Patrick-SCH03/jev-issue-radar)** · <sub>Patrick-SCH03 · GitHub · ⭐ 1 · 2026-09-20</sub><br>只读的 GitHub issue 分诊看板，检索候选的 issue 对，并排展示证据，说明两份报告是重复、相关、互不相同，还是描述不足。
- **[Jev Linter Action](https://github.com/sable-inc/jev-linter-action)** · <sub>sable-inc · GitHub · ⭐ 1 · 2026-09-21</sub><br>GitHub Action，用你自己写的是/否问题审查仓库文件，只有当 Jev 对每个预期答案的概率都达到阈值时才通过，支持 glob 和逐文件两种模式。
- **[Jev Model Router](https://github.com/Mandrilsquad1441/jev-model-router)** · <sub>Mandrilsquad1441 · GitHub · ⭐ 1 · 2026-09-18</sub><br>适用于 Claude Code、Claude 桌面 app 和 Codex 的插件：Jev 约 0.4 s 读懂任务，再按质量、OpenRouter 价格和速度对当前可用的模型排序，推荐一个模型和推理强度。
- **[Jev Review Action](https://github.com/fatwang2/jev-review-action)** · <sub>fatwang2 · GitHub · ⭐ 1 · 2026-09-18</sub><br>GitHub Action，依据固定版本的仓库证据审查目录提交，或用 Jev 对 pull request 分类，然后更新一条模板化的 PR 评论，全程不用文本生成模型。
- **[jev-crawlers](https://github.com/russfranky/jev-crawlers)** · <sub>russfranky · GitHub · ⭐ 1 · 2026-09-19</sub><br>Unix 风格的 bug 挖掘工具组（seed、expand、judge、verify、report、norms），通过管道传递 JSON 行，在沿着线索遍历仓库时让 Jev 评判每一个节点，每个节点约 $0.00006。
- **[jev-debtgate](https://github.com/smlayero/jev-debtgate)** · <sub>smlayero · GitHub · ⭐ 1 · 2026-09-21</sub><br>面向编程 agent 和 CI 的技术债闸门，从 diff 或文件中收集本地指标，向 Jev 提出一组固定的类型化问题，再套用策略返回放行、复核或拦截。
- **[jev-flash-review](https://github.com/TheBous/jev-flash-review)** · <sub>TheBous · GitHub · ⭐ 1 · 2026-09-17</sub><br>面向编程 agent 的基于规则的代码评审：一个本地 MCP 引擎加三个 skill，由 agent 提供 diff 和任务边界，Jev 逐条检查规则、引用作为证据的代码片段，并对问题做出裁定。
- **[jev-lens.nvim](https://github.com/rashedInt32/jev-lens.nvim)** · <sub>rashedInt32 · GitHub · ⭐ 1 · 2026-09-19</sub><br>Neovim 弹窗，在 Claude Code 编辑完成后显示 jev-lens 的结论：你是否需要看一眼、看哪些文件以及原因，并提供快捷键打开 diff 或清除被标记的残留代码。
- **[jev-oxlint](https://github.com/cephalization/jev-oxlint)** · <sub>cephalization · GitHub · ⭐ 1 · 2026-09-19</sub><br>根据一个 agent skill 构建项目专属的 Oxlint 插件，把确定性的 AST 检查与针对需要结合上下文判断的规则提出的窄范围 Jev 问题结合起来。
- **[jev-preflight](https://github.com/muse0509/jev-preflight)** · <sub>muse0509 · GitHub · ⭐ 1 · 2026-09-18</sub><br>Claude Code 插件，在每轮开始时给 Git 基线打快照，到 Stop 时在一次请求中从八个风险维度给脱敏后的本轮 diff 打分，风险高时要求 Claude 再排查一次。
- **[jev-router](https://github.com/heyman333/jev-router)** · <sub>heyman333 · GitHub · ⭐ 1 · 2026-09-20</sub><br>零依赖的 CLI 以及 Claude Code/Codex skill，把 agent 的窄范围判断（比如 184 个文件中哪些涉及鉴权）交给 Jev 而不是 LLM。
- **[jev-routing](https://github.com/nekowasabi/jev-routing)** · <sub>nekowasabi · GitHub · ⭐ 1 · 2026-09-18</sub><br>位于编程 agent CLI（Claude Code、Codex、Grok Build、Devin CLI）与上游 API 之间的 Go 代理，在转发每个请求之前用 Jev 丢弃或截断过时的工具调用和结果，并挑选下一个工具。
- **[jev-skill-router](https://github.com/shimo4228/jev-skill-router)** · <sub>shimo4228 · GitHub · ⭐ 1 · 2026-09-21</sub><br>Claude Code 插件，其 UserPromptSubmit hook 会询问 Jev 哪个已安装的 skill 适合当前提示词，并以影子模式记录建议；README 解释了为什么它不太可能对强模型有帮助。
- **[jevcumber](https://github.com/RubyBrewsday/jevcumber)** · <sub>RubyBrewsday · GitHub · ⭐ 1 · 2026-09-19</sub><br>只需要 .feature 文件的 Cucumber 运行器：对每个 Gherkin 步骤，Jev 根据页面上的内容挑选动作、控件和字面值，由 Playwright 执行，拿不准时拒绝瞎猜。
- **[jevis](https://github.com/jaewgwon/jevis)** · <sub>jaewgwon · GitHub · ⭐ 1 · 2026-09-19</sub><br>基于 Flutter integration_test 的 Dart 包，根据一个自然语言目标、一组注册好的允许 UI 操作和操作预算来运行 app 测试。
- **[JevKeep](https://github.com/hatt-io/jevkeep)** · <sub>hatt-io · GitHub · ⭐ 1 · 2026-09-18</sub><br>Codex 插件，在上下文压缩之前让 Jev 挑出有用的对话段落，压缩之后把它们的原文与 Codex 自己的摘要一起恢复，手动和自动压缩都适用。
- **[Jevonian](https://github.com/xinyao27/jevonian)** · <sub>xinyao27 · GitHub · ⭐ 1 · 2026-09-19</sub><br>位于编程 agent 与其服务商之间的本地代理，其 auto 路由在经过兼容性和配额筛选后，由 Jev 为每一轮选择模型和思考等级，并把每个决策记入本地成本台账。
- **[jevskill](https://github.com/lazniak/jevskill)** · <sub>lazniak · GitHub · ⭐ 1 · 2026-09-20</sub><br>适用于 Claude Code、Codex 等 20 多种 agent 的 agent skill，把依赖大量上下文的决策（比如哪些日志行重要）交给 Jev，每次约 325 毫秒、$0.000013；A/B 测试显示输入 token 减少了 99.3%。
- **[jevtriage](https://github.com/sathariels/jevtriage)** · <sub>sathariels · GitHub · ⭐ 1 · 2026-09-20</sub><br>GitHub Action 和 Python CLI，对每个 pull request 向 Jev 问一个 Choice（ready、needs_review 或 risky），只有置信度至少为 0.8 时才放行 ready，否则一律拒绝。
- **[Magic Jev](https://github.com/acharyaanusha/magic-jev)** · <sub>acharyaanusha · GitHub · ⭐ 1 · 2026-09-19</sub><br>Chrome 扩展，把 pull request 变成魔力 8 号球：点一下，Jev 就根据九个 PR 信号，在约 200 毫秒内从 20 句经典答语里挑一句，回答“该不该批准这个 PR”。
- **[Metis](https://github.com/Ayush0054/metis)** · <sub>Ayush0054 · GitHub · ⭐ 1 · 2026-09-17</sub><br>Python 库、CLI 和可复用的 GitHub Action，用 Jev 给新 issue 分诊，打上分类标签，并发回复追问缺失的细节。
- **[omp-typesafe](https://github.com/siddicky/omp-typesafe)** · <sub>siddicky · GitHub · ⭐ 1 · 2026-09-17</sub><br>omp 编程 agent 的审查插件，旁观会话并发布对抗性或建议性的批注，另外提供一个 typesafe_ask 工具，把 Noul、Choice 和 Score 开放给 agent 使用。
- **[Pi Jev Helm](https://github.com/Z761293629/pi-jev-helm)** · <sub>Z761293629 · GitHub · ⭐ 1 · 2026-09-18</sub><br>Pi 编程 agent 扩展，把每个新的工作单元经 OpenRouter 或 TypeSafe 发给 Jev 做任务分类，再把这次运行路由到显式配置的模型，出错时直接放行。
- **[pi-follow-through](https://github.com/Nabsku/pi-follow-through)** · <sub>Nabsku · GitHub · ⭐ 1 · 2026-09-19</sub><br>Pi 扩展，把一次已结束运行的请求、工具调用和最终答复发给 Jev，只有当 Jev 引用出一行确切证据、表明工作尚未完成且概率超过阈值时，才发送继续执行的提示。
- **[pi-jev-compaction](https://github.com/Wang-auspicious/pi-jev-compaction)** · <sub>Wang-auspicious · GitHub · ⭐ 1 · 2026-09-18</sub><br>Pi 编程 agent 的抽取式上下文压缩：Jev 评判完整的只读工具调用对，由代码丢弃不必要的部分，保留原文而不是生成摘要。
- **[PR Judge](https://github.com/juanegido/jev-pr-judge)** · <sub>juanegido · GitHub · ⭐ 1 · 2026-09-17</sub><br>Next.js 演示兼 GitHub Action，用一次并行的 Jev 调用判断 pull request 是否做到了它声称的事，再套用由代码维护的策略配置中的权重和硬性规则，并发布一条会原地更新的固定评论。
- **[pr-sieve](https://github.com/Thestral12/pr-sieve)** · <sub>Thestral12 · GitHub · ⭐ 1 · 2026-09-18</sub><br>GitHub Action，把 .jev.yml 当作 pull request 的语义 linter，把每条规则编译成一个 Jev 问题，再根据数值让检查失败、发评论或通过。
- **[Skill Dash](https://github.com/48Nauts-Operator/skill-dash)** · <sub>48Nauts-Operator · GitHub · ⭐ 1 · 2026-09-20</sub><br>本地仪表盘，让 Jev 从有用性、冗余度、清晰度和安全性四方面评判每个 Claude Code 或 Codex skill，给出保留、重写、合并或删除的结论；它也是一次 18,041 个 skill 普查背后的流水线。
- **[Switchloom](https://github.com/instructa/switchloom)** · <sub>instructa · GitHub · ⭐ 1 · 2026-07-17</sub><br>面向持久 Codex 任务的工作流提示词，把不同能力分配给不同模型，可选 Jev 路由；作者自己的基准测试结论是不建议采用。
- **[typeful-triage](https://github.com/cephalization/jev-triage)** · <sub>cephalization · GitHub · ⭐ 1 · 2026-09-17</sub><br>面向公开 GitHub 仓库的多人协作分诊仪表盘，Jev 对每个 issue 回答带类型的问题，比如类型、严重度、紧急程度、是否重复和下一步，每一次人工修正都会在之后的运行中反馈回去。
- **[TypeSafe Code Guard](https://github.com/greenyamao/Antigravity-mcp-semantic-search-with-TypeSafeAi)** · <sub>greenyamao · GitHub · ⭐ 1 · 2026-09-16</sub><br>面向 Antigravity、Cursor 和 Claude Code 的 MCP 服务器，用基于 15 行片段的语义代码发现取代 grep 大扫荡，并加了一道提交前的 diff 合理性检查。
- **[typesafe-agent-gates](https://github.com/ThiagaoBR/typesafe_agent_gates)** · <sub>ThiagaoBR · GitHub · ⭐ 1 · 2026-09-19</sub><br>面向无人值守编程 agent 的 LangChain 和 Deep Agents 中间件，用 Jev 做 shell 命令闸门、按严重度和紧急程度分诊 issue、识别合并请求，以及审查被削弱的测试。
- **[delegate](https://github.com/lahfir/claude-plugins/tree/main/delegate)** · <sub>lahfir · GitHub · ⭐ 49 仓库 · 2026-09-17</sub><br>Claude Code 插件，决定由谁来执行任务：当前会话、子 agent 还是外部 CLI harness。它检测已安装的 harness，维护一份由用户控制的允许列表，询问 Jev 哪一项合适，然后打印出对应命令。
- **[Forgewright 的 Jev skill 路由器](https://github.com/buiphucminhtam/forgewright/blob/main/scripts/runtime/jev_adapter.py)** · <sub>buiphucminhtam · GitHub · ⭐ 49 仓库 · 2026-03-06</sub><br>Forgewright AI 工程 harness 中可选、默认关闭的 Jev 适配器，在任务路由不明确时从严格限定的候选名单中挑选一个 skill，带预算上限、固定的模型版本，并可回退到本地路由器。
- **[cc-settings 的 Jev hook](https://github.com/darkroomengineering/cc-settings/blob/main/docs/hooks-reference.md)** · <sub>darkroomengineering · GitHub · ⭐ 45 仓库 · 2026-01-12</sub><br>团队共用的 Claude Code 和 Codex 配置，其中的 hook 使用 Jev：针对多文件提示词的委派检测、无人值守轮次的偏航熔断，以及逐字保留式压缩。在 1,102 条真实提示词上，阈值 0.7 的 Jev 正确触发 53 次，正则只有 10 次。
- **[Kit 的评测工具](https://github.com/speakeasy-api/kit/blob/main/docs/user/evaluations.md)** · <sub>speakeasy-api · GitHub · ⭐ 41 仓库 · 2026-08-24</sub><br>Kit 中的实验性评测工具。Kit 是只有一个 compose 工具的 Rust 编程 agent 运行时，agent 程序可以借助这个工具把一段 state 连同多个具名的 Noul、Choice 或 Score 问题发给 TypeSafe，并拿回具名的答案。
- **[lisptc 的 AGENTS.md 检查器](https://github.com/1hachem/lisptc/blob/main/scripts/check-agents.ts)** · <sub>1hachem · GitHub · ⭐ 38 仓库 · 2026-07-23</sub><br>面向 agent 的 Lisp monorepo lisptc 中的 CI 脚本，通过 OpenRouter 调用 Jev，标记出那些在讲解代码如何工作、而不是陈述规则和指引的 AGENTS.md 文件，按设定的概率阈值判为失败或给出警告。
- **[pi-approve-for-me](https://github.com/baggiiiie/pi-stuff/tree/main/packages/approve-for-me)** · <sub>baggiiiie · GitHub · ⭐ 38 仓库 · 2026-04-01</sub><br>给 bash 工具加闸门的 Pi 编程 agent 扩展：快速的 TypeSafe 风险评分让低风险命令自动执行，风险升高或内容有变的命令则先交给能理解上下文的 Jev 审查器，再交给人工确认。
- **[Xal 的 TypeSafe 插件](https://github.com/xal-sh/xal/blob/main/docs/providers.md)** · <sub>xal-sh · GitHub · ⭐ 37 仓库 · 2026-08-05</sub><br>Xal 终端编程 harness 内置的 TypeSafe 决策 provider；打开一个开关，就能启用 Jev 驱动的上下文压缩、Jev 预读取和一个通用的分类工具。
- **[KnoxCoder 的 Jev 层](https://github.com/knoxchat/knoxcoder/tree/main/extensions/knox/core/jev)** · <sub>knoxchat · GitHub · ⭐ 36 仓库 · 2026-07-17</sub><br>基于 VS Code 的编辑器 KnoxCoder 内置编程 agent 中的 Jev 模块：评判 agent 的每一轮，为工具调用和上下文段落把关，检测语义层面的死循环，为压缩重新给消息打分，并给 agent 轨迹打分。
- **[Conflux 的判断命令](https://github.com/tumf/conflux/blob/main/src/judge_command.rs)** · <sub>tumf · GitHub · ⭐ 27 仓库 · 2026-01-10</sub><br>Conflux 中的判断命令边界。Conflux 是一个规格驱动的编排器，在并行的 worktree 中运行 AI 编程 agent，这个边界以非权威观察者的身份，询问兼容 jev-cli 的命令各改动之间是否相互依赖。
- **[Koru 不变量闸门](https://github.com/korulang/koru/tree/main/invariants)** · <sub>korulang · GitHub · ⭐ 27 仓库 · 2025-12-28</sub><br>Koru 事件续延语言的 pre-commit 闸门：在声明了确定性检查的地方运行这些检查，需要判断的不变量则由 Jev 对照暂存的 diff 评判，除非设置 GATE_BLOCK=1，否则仅作建议。
- **[&jev 测试文件分类器](https://github.com/and-rs/dotfiles/blob/main/dot_config/nushell/execs/executable_%26jev)** · <sub>and-rs · GitHub · ⭐ 26 仓库 · 2023-11-13</sub><br>个人 dotfiles 仓库里的一个 Nushell 脚本，把每个源文件发给 Jev，返回它包含测试、fixture 或快照的概率。
- **[ThumbGate 的类型化问题](https://github.com/IgorGanapolsky/ThumbGate/blob/main/docs/agents/typesafe-typed-questions.md)** · <sub>IgorGanapolsky · GitHub · ⭐ 26 仓库 · 2026-03-03</sub><br>AI 编程 agent 的行动前防火墙，把 Jev 的问题格式映射到它的 PreToolUse 风险检查上（原子化的风险 Noul、一个风险类别 Choice、严重程度），并提供 --live 模式，让整套检查对着 Jev API 以影子方式运行。
- **[AIOSON jev:review](https://github.com/jaimevalasek/aioson/blob/main/.aioson/docs/jev-review.md)** · <sub>jaimevalasek · GitHub · ⭐ 25 仓库 · 2026-03-01</sub><br>AIOSON 软件项目 AI 运行框架中的 Jev 命令：jev:review 为 UI 交付的 QA 和原型评审加入类型化的语义判断，与 jev:judge 和 jev:agent-review 并列。
- **[Specflow 的 TypeSafe 建议功能](https://github.com/Hulupeep/Specflow/blob/main/docs/specs/typesafe-advisory/prd.md)** · <sub>Hulupeep · GitHub · ⭐ 25 仓库 · 2025-12-02</sub><br>面向编程 agent 的规格转契约工具包 Specflow 中的建议功能，在 duo-build 审查时询问 Jev：测试是否真正覆盖了验收标准，证据是否支撑“已完成”的说法。
- **[XM8M 验收顾问](https://github.com/bubio/xm8m/blob/main/scripts/ra_acceptance.py)** · <sub>bubio · GitHub · ⭐ 25 仓库 · 2023-02-20</sub><br>PC-8801 模拟器 XM8M 的验收台账，由 Jev 把操作者的测试报告分为一致、有问题、未运行或证据不足；这些建议从不决定是否验收。
- **[Jauvex](https://x.com/diegoaraos/status/2101782639854186747)** · <sub>diegoaraos · X · ▶ 97 · 2026-09-20</sub><br>双向语音聊天 app，可以在 Claude 和 Codex 编程 agent 工作时与其对话并加以引导，由 Jev 对指令和意图进行分类。
- **[Esposter 的 Jev 仓库自动化](https://github.com/Esposter/Esposter/tree/main/scripts/src/services/jev)** · <sub>Esposter · GitHub · ⭐ 23 仓库 · 2022-06-28</sub><br>Esposter Nuxt monorepo 里的仓库脚本，用 Jev 给 issue 分诊打标签，并读取 CodeRabbit 问题的严重程度和发布闸门，置信度下限为 0.6，在 checkout 之外写入时要求 0.85。
- **[dure jev](https://github.com/hebbianai/dure/blob/main/cli/lib/jev-command.mjs)** · <sub>hebbianai · GitHub · ⭐ 22 仓库 · 2026-07-30</sub><br>Dure 中的 CLI 命令。Dure 是一个跨项目协调 Claude Code、Codex 和 Pi agent 的开源工作区，这个命令可以在任意机器上，把包含类型化 Noul、Choice 和 Score 问题的 JSON 请求交给 TypeSafe Jev 评估。
- **[jev-auto](https://github.com/letta-ai/mods/tree/main/packages/jev-auto)** · <sub>letta-ai · GitHub · ⭐ 22 仓库 · 2026-06-23</sub><br>Letta Code 的 mod，通过 OpenRouter 使用 Jev，自动批准影响小的工具调用，遇到有风险或不明确的调用则询问人；默认关闭，仅作用于当前对话。
- **[Marionette 的 Jev 轮次判断](https://github.com/professorpalmer/marionette/tree/main/harness/jev)** · <sub>professorpalmer · GitHub · ⭐ 22 仓库 · 2026-07-03</sub><br>为基于 Puppetmaster 内核的桌面 AI 编程 harness Marionette 提供可选开启的 Jev 轮次判断：用一次 OpenRouter Decisions 调用选出要加载哪个 skill 正文，取代基于 token 重叠的检索。
- **[Shepherd 的 Jev 评判器](https://github.com/erwins-enkel/shepherd/blob/main/src/judge-typesafe.ts)** · <sub>erwins-enkel · GitHub · ⭐ 20 仓库 · 2026-05-30</sub><br>交互式 Claude Code 的自托管任务控制台 Shepherd 中与厂商无关的 Judge 接缝，由 TypeSafe SDK 支撑，每次 agent 停下时跑一次快速的 Jev choice 或 noul，不再为此派生一次 120 秒的 claude 调用。
- **[Vekil 的 Jev 策略路由](https://github.com/sozercan/vekil/blob/main/examples/policy-routing-typesafe.yaml)** · <sub>sozercan · GitHub · ⭐ 20 仓库 · 2026-02-12</sub><br>一份示例策略，用于 Go 编写的 AI 网关 Vekil（为 Claude Code 和 Codex CLI 代理 GitHub Copilot 及其他 provider）：由 Jev 把每个请求分到轻量或强力的模型路由。
- **[dsh-jev-decide](https://github.com/wingsky-1/dsh-plugin-hub/tree/main/packages/dsh-jev-decide)** · <sub>wingsky-1 · GitHub · ⭐ 19 仓库 · 2026-08-16</sub><br>DeepSeek Harness Web GUI 的插件，为 agent 提供一个 ws_jev_decide 工具，内置计划评审、风险检查、密钥泄露筛查等预设问题集，另有 key 管理、连接测试和决策历史。
- **[quoin-jev](https://github.com/agent-ix/quoin/tree/main/rust/crates/quoin-jev)** · <sub>agent-ix · GitHub · ⭐ 19 仓库 · 2026-06-14</sub><br>面向 Claude Code 的规格驱动开发套件 Quoin 中的 Rust crate，用一次批量 Jev 请求从验收标准强度的角度审视每条功能需求，并把答案转成类型化的规格审查意见。
- **[uploads.sh 的文件分类器](https://github.com/buildinternet/uploads/blob/main/apps/api/src/classifier.ts)** · <sub>buildinternet · GitHub · ⭐ 19 仓库 · 2026-07-06</sub><br>为编程 agent 托管 pull request 产物的文件服务 uploads.sh 中的实验性分类器：先由视觉模型描述图片，再由 Jev 从封闭枚举中为每个上传文件选出 kind、surface 和 screen。
- **[Magic Compose](https://github.com/SawyerHood/sawyer-plugins/tree/main/plugins/magic-compose)** · <sub>SawyerHood · GitHub · ⭐ 18 仓库 · 2026-09-10</sub><br>BB 插件，在新建线程的输入框里加了一根魔杖：你打字的同时，Jev 为这个编程 agent 线程选好项目、机器、模型、推理档位和环境，在你发送前就把各个选择器拨到位。
- **[Turbodiff 的 Jev 复杂度分类器](https://github.com/Ngineer101/turbodiff/tree/main/src/integrations/typesafe)** · <sub>Ngineer101 · GitHub · ⭐ 18 仓库 · 2026-08-02</sub><br>开源软件工厂 Turbodiff（负责规划、编码、提交和审查 pull request）中的任务复杂度分类器，由 Jev 为每个任务设定规划档位。
- **[zttp invariant advise](https://github.com/srdjan/zttp/blob/main/packages/runtime/src/invariant_cli.zig)** · <sub>srdjan · GitHub · ⭐ 18 仓库 · 2025-12-24</sub><br>Zig 写的 TypeScript 运行时兼 agent 编译器 zttp 中的一个选项：<code>zttp invariant author --advise</code> 询问 Jev 一条自然语言陈述是否符合所选的不变量类型；答案仅作建议，绝不当作证明。
- **[Fleet AI Gateway 的 Jev 路由](https://github.com/sbluemin/fleet-harness/tree/canary/runtime/fleet-console/features/ai-gateway/runtime/src/upstream/typesafe)** · <sub>sbluemin · GitHub · ⭐ 17 仓库 · 2026-03-17</sub><br>Fleet 中的 AI Gateway 路由。Fleet 是用于监管 Claude Code 等编程 agent 会话的本地优先控制台，在这里 Jev 可以依据任务、基准测试和配额余量数据，为委派出去的 agent 运行分配模型和推理强度。
- **[Kimi Code JevTriage](https://github.com/NitrogenT7/kimi-code-security/tree/main/packages/agent-core-v2/src/features/jev)** · <sub>NitrogenT7 · GitHub · ⭐ 17 仓库 · 2026-07-09</sub><br>Kimi Code CLI 编程 agent 的一个非官方安全研究变体中的 JevTriage 工具，根据漏洞报告的类型、端点、证据和声称的影响，让 Jev 对其进行分诊。
- **[o8 的判断裁判](https://github.com/hurttlocker/o8/tree/main/src/lib/judgment)** · <sub>hurttlocker · GitHub · ⭐ 17 仓库 · 2026-03-11</sub><br>编程 agent 集群控制室 o8 中的判断层，针对每个 diff 向 Jev 提一组锁定的是非题（是否只改文档、是否涉及鉴权、是否含 mock 数据、是否新增测试），每个问题都附有校准说明。
- **[Pi 的 Jev 扩展](https://github.com/bskimball/pi/tree/main/agent/extensions/jev)** · <sub>bskimball · GitHub · ⭐ 17 仓库 · 2026-07-26</sub><br>个人 Pi 编程 agent 配置中的一个扩展，基于文本 state 为 agent 提供仅作参考的 Choice、Score 和 Noul 分类器，后端是 TypeSafe 或 Cloudflare Workers AI。
- **[Attocode Intelligence 的 Jev 打分器](https://github.com/eren23/attocode/blob/main/packages/code-intel/src/attocode_intel/confidence/jev.py)** · <sub>eren23 · GitHub · ⭐ 16 仓库 · 2026-01-21</sub><br>代码库理解 MCP 服务器 Attocode Intelligence 中的置信度打分器，用 Jev 概率替代硬编码的规则置信度：在其规则准确率评测上 ECE 为 0.07，常量方案为 0.21。
- **[Fleet Prime 的意图路由器](https://github.com/Qredence/fleet-prime-agent/blob/main/web/server/src/typesafe/intent-router.ts)** · <sub>Qredence · GitHub · ⭐ 16 仓库 · 2026-08-10</sub><br>Fleet Prime 中的输入框意图路由器。Fleet Prime 是 Prime Agent 编程运行时的本地 Web 工作区，这个路由器询问 Jev 输入的文字是在请求 app 的某个内置命令，还是一个普通的编程请求。
- **[kpatch 的 Jev 过滤器](https://github.com/purseclab/kernelcveanalysis/tree/main/ingots_tools/kpatch/src/kpatch/filter/jev)** · <sub>purseclab · GitHub · ⭐ 16 仓库 · 2025-03-01</sub><br>Purdue PurSec Lab 内核 CVE 分析工具中的提交过滤器，就每个 Linux/Android 内核补丁向 Jev 提出与安全相关的问题，例如是否改动了引用计数、加锁、析构函数、权限或边界检查。
- **[Claude Flow Novice 的 Jev 影子试点](https://github.com/masharratt/claude-flow-novice/blob/main/.claude/cfn-scripts/jev-systemone.sh)** · <sub>masharratt · GitHub · ⭐ 14 仓库 · 2025-09-23</sub><br>Claude Code 编排工具包，在它的各个循环里以影子模式运行 Jev：预先分诊评审投票建议、复查被拒绝的破坏性命令，以及给夜间模式的报告条目打分。
- **[Loom 的 Jev 合并风险评分](https://github.com/rjwalters/loom/blob/main/loom-daemon/src/jev_merge_risk.rs)** · <sub>rjwalters · GitHub · ⭐ 14 仓库 · 2025-10-11</sub><br>agent 编排守护进程里为自动合并 PR 做的影子模式预评分：在做合并决定前，由 Jev 评估 diff 构成、影响范围、审查深度和可回滚性。
- **[pi-jev-router](https://github.com/sugarforever/yummy-pi-extensions/tree/main/pi-jev-router)** · <sub>sugarforever · GitHub · ⭐ 14 仓库 · 2026-09-05</sub><br>Pi 编程 agent 扩展，在每条提示词进入会话前问 Jev 是继续、分叉还是新开会话，让岔开的话题不混进长上下文。
- **[Varin 的 Jev 快速决策](https://github.com/Youzini-afk/Varin/blob/main/packages/pi-host/src/harness/typesafe-systemone.ts)** · <sub>Youzini-afk · GitHub · ⭐ 14 仓库 · 2026-08-01</sub><br>编程与研究 agent 工作区，其 Fast Decision 能力在主模型运行前调用 Jev 判断材料相关性、挑选下一份要读的内容，并给上下文打分。
- **[grill-me-with-jev](https://github.com/jon-devlapaz/tink-skills/tree/main/skills/grill-me-with-jev)** · <sub>jon-devlapaz · GitHub · ⭐ 13 仓库 · 2026-08-01</sub><br>agent skill，通过决策树式的面谈对工程计划做压力测试，用 Jev 建议每个疑虑是现在就问、先去调查，还是直接跳过。
- **[jev-assert](https://github.com/mthines/agent-skills/tree/main/skills/quality/jev-assert)** · <sub>mthines · GitHub · ⭐ 13 仓库 · 2026-04-23</sub><br>agent skill，把一条自然语言描述的 UI 预期转成结论：询问 Jev 在页面捕获的文本状态中该结果是否成立，用于自动化 UI 验证。
- **[Dev Command Center 的决策 provider](https://github.com/wharley/DevCommandCenter/blob/main/crates/dcc-infra/src/decision_provider.rs)** · <sub>wharley · GitHub · ⭐ 12 仓库 · 2026-01-29</sub><br>本地优先的编程 agent 桌面工作台，可选开启的决策 provider 会让 Jev 判断检索出的 ai-memory 候选中哪些是相关的。
- **[gray 的 Jev 精简扫描](https://github.com/vstaln/gray/blob/main/typesafe_scan.mjs)** · <sub>vstaln · GitHub · ⭐ 12 仓库 · 2026-08-24</sub><br>用 Jev 扫描 gray agent harness 代码库的脚本，先给各源码片段的可精简程度打分，再深入排名靠前的片段，判断臃肿类型并核查哪些内容不能删。
- **[IDA Pro MCP 的 Jev 智能分析](https://github.com/GrecAndrei/ida-pro-mcp/blob/master/src/ida_pro_mcp/host/intelligence/providers/jev.py)** · <sub>GrecAndrei · GitHub · ⭐ 12 仓库 · 2025-12-15</sub><br>用于 IDA Pro 逆向工程的 MCP 服务器，可选开启的 Jev provider 会为语义函数搜索的候选池打分，并重新排列下一批分析目标。
- **[jev-review-model](https://github.com/jasonvarga/dotfiles/tree/master/ai/jev)** · <sub>jasonvarga · GitHub · ⭐ 12 仓库 · 2020-11-22</sub><br>dotfiles 里的一个脚本，从 stdin 读取 PR diff，询问 Jev 该由 Opus 还是 Sonnet 来评审，或者两者皆可。
- **[pi-tool-supervisor 的 TypeSafe 后端](https://github.com/maplezzk/pi-extensions/tree/main/packages/pi-tool-supervisor)** · <sub>maplezzk · GitHub · ⭐ 12 仓库 · 2026-07-19</sub><br>Pi 编程 agent 监督器的代码审查后端，把规则文件里每一条编号条款变成一个针对 diff 的 Jev 问题；一次 3 条规则的审查约 US$0.00006、耗时 1-2 秒。
- **[Varro 的 Jev 自动批准](https://github.com/koltyakov/varro/blob/main/src/extension/jev-decisions.ts)** · <sub>koltyakov · GitHub · ⭐ 12 仓库 · 2026-04-17</sub><br>面向 OpenCode 的 VS Code 工作台，可以自动批准 agent 的权限请求：让 Jev 在放行、询问、拒绝之间选择，同时做破坏性和操纵性检查。
- **[KubeDojo 的 Jev epic 分诊](https://github.com/kube-dojo/kube-dojo.github.io/blob/main/scripts/jev_epic_triage.py)** · <sub>kube-dojo · GitHub · ⭐ 11 仓库 · 2025-12-02</sub><br>为构建一门免费 Kubernetes 课程的 AI agent 集群所写的派发前分诊脚本：Jev 审阅 PR 和 epic 的状态，脚本据此给出派发、并行度和评审模型家族的建议。
- **[sai 的 jev-audit 插件](https://github.com/jswysnemc/sai/tree/main/examples/lua-plugins/jev-audit)** · <sub>jswysnemc · GitHub · ⭐ 11 仓库 · 2026-07-20</sub><br>sai 终端 AI 助手的 Lua 插件，在自动批准模式下用一个 Jev Choice 审查待执行的工具操作，取代聊天模型审查者。
- **[Cloud Harness MCP 的 skill 推荐器](https://github.com/bestagentkits/cloud-harness-mcp/blob/main/apps/runner/src/typesafe-skill-suggester.ts)** · <sub>bestagentkits · GitHub · ⭐ 10 仓库 · 2026-08-16</sub><br>以 MCP 服务器形式提供的远程编程 harness，其 runner 在提示词提交时先问 Jev 某个入围的 skill 是否适合当前请求，再决定是否推荐。
- **[harlan-github-agent 的 Jev 分类](https://github.com/harlan-zw/harlan-agent-kit/blob/main/packages/harlan-github-agent/src/classification.ts)** · <sub>harlan-zw · GitHub · ⭐ 10 仓库 · 2026-01-11</sub><br>Claude Code agent 工具包，内含一个自主处理 GitHub 仓库的服务，把 Jev 分类作为一道边界，失败以返回值形式交回，调用方默认走安全路径。
- **[JEV 共享判断层](https://github.com/RisorseArtificiali/skills/tree/main/scripts/jev)** · <sub>RisorseArtificiali · GitHub · ⭐ 10 仓库 · 2026-08-28</sub><br>某个编程 agent skill 集合中的共享运行器，把目标 state 加上一组类型化问题转成一份校准过的评估，最早用于 pull request 评估。
- **[rift-typesafe](https://github.com/exYze/rift/tree/master/crates/rift-typesafe)** · <sub>exYze · GitHub · ⭐ 10 仓库 · 2026-09-17</sub><br>面向本地模型的 Rust 终端编程 agent Rift 中的 Jev 客户端 crate，用于那些原本要从文字中解析出来的集群决策，与聊天模型 provider 相互独立。
- **[Sigil 的 Jev 重排](https://github.com/Anmol-Srv/sigil/blob/master/src/lib/jev.js)** · <sub>Anmol-Srv · GitHub · ⭐ 10 仓库 · 2026-03-13</sub><br>面向编程 agent、通过 MCP 共享的本地优先记忆系统，在注入上下文之前用 Jev 决定保留哪些检索到的事实。
- **[Synapse 的 Jev 守卫接缝](https://github.com/JosephOIbrahim/Synapse/tree/master/harness/jev)** · <sub>JosephOIbrahim · GitHub · ⭐ 10 仓库 · 2026-02-06</sub><br>一个 Houdini AI 助手开发 harness 中的构建期守卫节点：Jev 把每个任务路由到某个模型档位，并把构建者的回执筛为 clear、referee 或 flag。
- **[Learn Ukrainian 的 TypeSafe 工具集](https://github.com/learn-ukrainian/learn-ukrainian.github.io/tree/main/scripts/typesafe)** · <sub>learn-ukrainian · GitHub · ⭐ 9 仓库 · 2025-12-21</sub><br>一个免费 A1-C2 乌克兰语课程仓库里的 agent 集群工具，用 Jev 在派发前给 issue 做就绪度分诊，并用于行级语义查找和 skill 推荐。
- **[Anvil 的 Jev 标注](https://github.com/fakoli/anvil/blob/main/bin/src/anvil/jev.py)** · <sub>fakoli · GitHub · ⭐ 8 仓库 · 2026-06-18</sub><br>面向多 agent 编程协作的本地优先项目状态层，可选用 Jev 对需求、任务和证据做标注，但这些标注永远不允许修改权威状态。
- **[DevOpsWorker 的移植 PR 分类器](https://github.com/SShadowS/DevOpsWorker/blob/main/src/sdk/port-classifier.ts)** · <sub>SShadowS · GitHub · ⭐ 8 仓库 · 2026-06-21</sub><br>多 agent 的 Azure DevOps 流水线，询问 Jev 某个 pull request 是否是另一个近期 PR 的移植版，以捕捉标题正则漏掉的情况；在 100 个 PR 中，这类漏判造成了 9 次移植被完整评审，花费 $29.30。
- **[fleet-core 的 TypeSafe 客户端](https://github.com/infiquetra/infiquetra-claude-plugins/blob/main/plugins/fleet-core/scripts/fleet_commons/typesafe_client.py)** · <sub>infiquetra · GitHub · ⭐ 8 仓库 · 2025-11-26</sub><br>一组 Claude Code 插件共用的 TypeSafe 客户端，在代码层面强制执行一条数据规则：任何 Jev 请求之前，state 都必须经过脱敏和截断，每个结论都会记录日志。
- **[jev-stop-guard](https://github.com/coil398/dotfiles/blob/master/etc/jev-stop-guard-codex-hook.py)** · <sub>coil398 · GitHub · ⭐ 8 仓库 · 2016-11-04</sub><br>Codex、Cursor 和 Devin CLI 的 Stop hook，询问 Jev 主 agent 是否在用户要求的工作还没做完时就停下了，证据充分时拦下这次停止。
- **[mikan Jev harness](https://github.com/geminixiang/mikan/blob/main/src/harness/jev.ts)** · <sub>geminixiang · GitHub · ⭐ 8 仓库 · 2026-03-11</sub><br>自托管的 Slack 编程 agent，凡是需要快速分类、路由或护栏决策的调用点都直接调用 Jev，而不是把它当成聊天模型提供方。
- **[sofar 的类型化评判校准](https://github.com/usesofar/sofar/blob/main/scripts/judge-calibration.mjs)** · <sub>usesofar · GitHub · ⭐ 8 仓库 · 2026-07-03</sub><br>面向编程 agent、基于事件溯源的记忆工具中的一个脚本，对照项目记录校准 Jev：判断各项决策是否属于长期约束、是否与任务相关，然后报告一致率和校准情况。
- **[SpecPi jev-advisor](https://github.com/TannerMidd/SpecPi/tree/main/extensions/jev-advisor)** · <sub>TannerMidd · GitHub · ⭐ 8 仓库 · 2026-09-19</sub><br>Pi 编程 agent harness SpecPi 中可选启用的 Jev 顾问扩展，评判能力、进度、保留、来源和不可信内容，每项功能都有开关，可选择采纳建议或只做记录。
- **[Meaning Diff](https://x.com/johnsandovaI/status/2102222760131101044)** · <sub>johnsandovaI · X · ▶ 31 · 2026-09-22</sub><br>开源补丁审查工具，看的是 diff 的含义而不是逐行改动；在一个有问题的结账流程上，它借助 Jev 在 343 毫秒内发现 agent 隐藏了支付失败、削弱了一条断言，还伪造了收据发送。
- **[面向 Pi、Tau 和记忆的 Jev](https://github.com/grahama1970/agent-skills/tree/main/skills/jev)** · <sub>grahama1970 · GitHub · ⭐ 7 仓库 · 2026-01-11</sub><br>agent skill，把 Jev 接在一个 Pi 扩展和一个 Tau 用的 Python 库后面，在主模型运行前挑选相关代码、记忆证据和 skill，另在错误分诊和 AI 检测类 skill 中加入影子 Jev 分类器。
- **[omp-fabric 的类型化判断](https://github.com/tickernelz/omp-fabric/blob/main/docs/judgment.md)** · <sub>tickernelz · GitHub · ⭐ 7 仓库 · 2026-09-06</sub><br>Oh My Pi 的可编程工具与 agent 运行时 Fabric 中的类型化判断通道：<code>judgment.ask</code> 把 choice、bool 和 score 问题发给 TypeSafe System One，由四个闸门读取答案。
- **[OpenGantry 的 Jev 预检](https://github.com/jeger-ai/opengantry/blob/main/src/cli/lib/contract/preflight-jev.ts)** · <sub>jeger-ai · GitHub · ⭐ 7 仓库 · 2026-05-11</sub><br>agent 治理 CLI OpenGantry 中的实验性预检：询问 Jev 编程 agent 的意图归哪个 manifest skill 管、哪些允许的目录与之相关，置信度低时回退到启发式规则。
- **[ora 答案审计](https://github.com/trancong12102/agentskills/blob/main/plugins/ora/scripts/audit-answers.py)** · <sub>trancong12102 · GitHub · ⭐ 7 仓库 · 2025-12-24</sub><br>Claude Code 研究插件 ora 中的审计脚本，对照证据检查记录下来的答案；配置 key 后还会问 Jev 答案是否带上了版本和日期、结论是否与证据矛盾。
- **[appstore-precheck 的 Jev 语义审查](https://github.com/berkayturk/appstore-precheck/blob/main/skills/appstore-precheck/references/typesafe.md)** · <sub>berkayturk · GitHub · ⭐ 6 仓库 · 2026-06-28</sub><br>appstore-precheck 中可选的建议性 Jev 检查环节。appstore-precheck 是检查 iOS App Store 被拒风险的 agent skill 和 Bash 扫描器，这一环节以影子模式审查在本地收集的源码、文案和政策证据包。
- **[Fleet 自动模式的 Jev 分类器](https://github.com/khang859/fleet/blob/main/src/shared/agent-decision-models.ts)** · <sub>khang859 · GitHub · ⭐ 6 仓库 · 2026-03-14</sub><br>Fleet 是一个可同时运行多个 AI 编程 agent 的桌面终端复用器，它提供一个选项，用 Jev 1.13 代替文本模型作为自动模式的分类器，对每条 agent 命令回答是或否。
- **[get-fable Reflex (Fable-Jev)](https://github.com/imMamdouhaboammar/get-fable/tree/master/src/core/reflex)** · <sub>imMamdouhaboammar · GitHub · ⭐ 6 仓库 · 2026-08-11</sub><br>get-fable 中的 Reflex 层。get-fable 是给现有编程 agent 用的 skill 与 harness 套件，这一层用 Jev 做带概率差值的语义任务路由，并做逐字保留式的对话压缩，丢弃已过时的工具结果。
- **[Goddard 的 Jev 评估功能](https://github.com/goddard-ai/goddard/blob/main/crates/waku-core/src/eval.rs)** · <sub>goddard-ai · GitHub · ⭐ 6 仓库 · 2026-09-13</sub><br>Goddard 中的评估模型客户端。Goddard 是一个用于编排 Codex、Claude、OpenCode 等编程 agent 的 Rust GUI，这个客户端用 Jev 生成每轮的状态标记，以及实验性的下一步操作预测标签。
- **[Lean Refactor Arena TypeSafe NCA](https://github.com/endomorphosis/lift_coding/blob/main/papers/completion/lean_refactor_arena/typesafe_nca.md)** · <sub>endomorphosis · GitHub · ⭐ 6 仓库 · 2026-01-12</sub><br>为 Lean Refactor Arena 搭的 harness，Jev 在其中充当闸门而不是生成器：用 Choice、Score 和 Noul 问题评判候选的 Lean 重构（比如是否引入了 sorry），lake compile 依然是最终裁判。
- **[Percussion CMS 的 issue 预筛](https://github.com/intersoftdatalabs-in/percussioncms/blob/main/scripts/typesafe-prescreen.py)** · <sub>intersoftdatalabs-in · GitHub · ⭐ 6 仓库 · 2023-09-27</sub><br>给 Percussion CMS 仓库维护者用的脚本，在基于规则的过滤之前先用 Jev 预筛 GitHub issue 清单，建议哪些跳过、哪些是一个 PR 就能搞定的规模、哪些可以关闭。
- **[pier 的 Jev 决策层](https://github.com/July24/pier/blob/master/packages/pier-ext/src/jev-core.ts)** · <sub>July24 · GitHub · ⭐ 6 仓库 · 2026-08-22</sub><br>Pi 编程 agent 扩展 pier（带 todo 循环，并在 herdr 终端窗格里运行可交互的子 agent）中可选的 Jev 决策层，用于诊断闸门、通知排序和摘录窗口。
- **[WatchTower jev-triage](https://github.com/amirfish1/watchtower/blob/main/scripts/jev-triage.py)** · <sub>amirfish1 · GitHub · ⭐ 6 仓库 · 2026-06-26</sub><br>为 WatchTower 编程 agent 集群队列写的只读脚本，对每个搁置中的进行中工单询问 Jev：它需要人类负责人处理，能由 agent 根据证据解决，还是需要外部人员介入。
- **[wcode 的 Jev agent 上下文决策](https://github.com/francis-du/wcode/blob/main/src/intelligence/jev.rs)** · <sub>francis-du · GitHub · ⭐ 6 仓库 · 2026-08-22</sub><br>编程 agent 的 MCP 控制面 wcode 中可选的 Jev 决策 provider，根据有界的仓库 state 判断能否开始编辑、是否需要更多检索或导航，以及该检查哪类风险。
- **[Agent Stack 的 Jev QA](https://github.com/JavierBertolino/agent-stack/blob/main/docs/jev.md)** · <sub>JavierBertolino · GitHub · ⭐ 5 仓库 · 2026-08-20</sub><br>Agent Stack 中的 QA 引擎。Agent Stack 是面向 Codex、Claude Code、Cursor 和 OpenCode 的多 agent 交付工作流，其中 Web 和移动端 QA agent 把检查点压缩成文本，由 Jev 返回功能、视图和业务三方面的判定。
- **[ai-config-kit 类型化决策](https://github.com/albrand/ai-config-kit/blob/main/skillsets/agent-runtime/shared/typed-decisions/scripts/jev.py)** · <sub>albrand · GitHub · ⭐ 5 仓库 · 2026-05-06</sub><br>一个与工具无关的 AI 编程 agent 运行框架中的 CLI，让 agent 就某个 diff 或 issue 向 Jev 提出是/否、单选或等级问题，再把答案分级并记入决策台账。
- **[ai-workflows 范围分类](https://github.com/dryvist/ai-workflows/blob/main/scripts/scope_classify.py)** · <sub>dryvist · GitHub · ⭐ 5 仓库 · 2026-02-15</sub><br>可复用的 GitHub Actions 步骤，依据仓库的评分规则用 Jev 的 Choice 决定一个 pull request 要跑多少 CI（完整或部分 CI、AI 评审、发布说明、e2e），并有确定性的“始终完整”覆盖规则。
- **[ce-ai 的 Jev 决策](https://github.com/mastepanoski/ce-ai/blob/main/src/decisions/jev.rs)** · <sub>mastepanoski · GitHub · ⭐ 5 仓库 · 2026-08-20</sub><br>ce-ai 中的 Jev 决策 provider。ce-ai 是一个 Rust CLI，在十种编程 agent harness 上编排 Compound Engineering 插件，这个 provider 在工作流各阶段回答模型档次、任务风险等问题。
- **[cli-ck 的 Jev 任务路由器](https://github.com/cli-ck/cli-ck/blob/main/src/features/ai-companion/ai/lib/jevTaskRouter.ts)** · <sub>cli-ck · GitHub · ⭐ 5 仓库 · 2026-06-25</sub><br>cli-ck 中的任务路由器。cli-ck 是基于 Tauri 的 AI 原生终端和开发工作区，这个路由器在每轮派发前让 Jev 为每个 agent 任务选择一个预先授权的模型档位。
- **[CodexBar Plasma 的 TODO 闸门](https://github.com/Lucenx9/codexbar-plasma/blob/main/scripts/todo_gate.py)** · <sub>Lucenx9 · GitHub · ⭐ 5 仓库 · 2026-06-25</sub><br>CodexBar KDE Plasma 小部件的仓库检查，通过 OpenRouter Decisions 询问 Jev 某次改动是否完成了 TODO.md 中的某一项，从而在同一次改动里把已完成的工作从清单中移除。
- **[kojo 的 Jev 推理强度分类器](https://github.com/loppo-llc/kojo/blob/main/internal/agent/auto_effort.go)** · <sub>loppo-llc · GitHub · ⭐ 5 仓库 · 2026-02-22</sub><br>kojo 中逐轮运行的推理强度分类器。kojo 是 Claude Code、Codex 和 Grok Build 的移动端遥控工具，支持持久化 agent，这个分类器询问 Jev 一条消息需要低、中还是高推理强度，失败时回退到 Claude。
- **[Kungfu Kanban 的 Jev 影子路由](https://github.com/LeahyCC/kungfu-kanban/blob/main/lib/jev.js)** · <sub>LeahyCC · GitHub · ⭐ 5 仓库 · 2026-07-17</sub><br>Kungfu Kanban 中的影子模型路由。Kungfu Kanban 是由 Claude Code agent 处理卡片的本地看板，Jev 给每张卡片的难度打分，并记录它会在 Haiku、Sonnet 和 Opus 中选哪个，供之后与实际结果对比。
- **[Light Skills 的 Jev 集成](https://github.com/LightDevCoder/skills/blob/main/docs/architecture/jev-integration-contract.md)** · <sub>LightDevCoder · GitHub · ⭐ 5 仓库 · 2026-07-23</sub><br>Light Skills agent skill 合集共用的 Jev 集成契约和评测，其中 project-init、ask-light 和 agent-config 这几个 skill 使用 Jev 的 Score、Noul 和 Choice 判断，最终决定权仍在代码手里。
- **[nestjs-hexagonal 的 Jev 语义规则](https://github.com/Softtor/nestjs-hexagonal/tree/main/skills/jev-eval)** · <sub>Softtor · GitHub · ⭐ 5 仓库 · 2026-03-26</sub><br>面向 NestJS 六边形/DDD 代码的 Claude Code 插件里的语义架构规则，由 Jev 检查文件在控制器是否够薄、实体是否贫血、基础设施是否渗入端口等方面的问题，并附带校准数据。
- **[Ortus 的 Jev 轮前闸门](https://github.com/who/ortus/blob/main/docs/judge.md)** · <sub>who · GitHub · ⭐ 5 仓库 · 2026-01-17</sub><br>Ortus 借助 Claude Code、Codex、Grok 或本地模型清空 bd issue 积压，这是其中可选的轮前闸门：Jev 按任务决定执行、跳过还是交给人处理，并评估操作的风险高低。
- **[RUNE 的 Jev 路由](https://github.com/dybala-21/rune/blob/main/rune/llm/jev.py)** · <sub>dybala-21 · GitHub · ⭐ 5 仓库 · 2026-03-20</sub><br>只在测试通过时才宣称完成的本地模型编程 agent RUNE 中的决策 API 路由：agent 行动前，由 Jev 回答范围受限的路由问题并给出文件角色提示。
- **[Sourdaw 的审查立场检查](https://github.com/jcosta33/sourdaw/blob/main/scripts/checkStancesRecord.ts)** · <sub>jcosta33 · GitHub · ⭐ 5 仓库 · 2026-03-16</sub><br>开源 DAW Sourdaw 中的审查流程脚本，针对 PR 审查包里的每条立场询问 Jev：它的自我承认是否点出了具体的失败模式，而不只是列出改动的文件；不合格的条目判为失败。
- **[XYZ Forge jev_triage](https://github.com/HiQS-Labs/XYZ-forge/blob/development/utils/py/jev_triage.py)** · <sub>HiQS-Labs · GitHub · ⭐ 5 仓库 · 2026-08-15</sub><br>把编程 agent 当劳动力来运营的系统 XYZ Forge 中的分诊分类器，根据退出码和 stderr 末尾内容，向 Jev 询问 agent 测试运行的状态、严重度和故障类别。
- **[kamchatka 的 Jev 支持](https://github.com/ljedrz/nachalnik/tree/master/kamchatka)** · <sub>ljedrz · GitHub · ⭐ 4 仓库 · 2026-09-18</sub><br>nachalnik Rust 运行时的终端 agent kamchatka 中的 Jev 集成：包括一个感知内容的上下文压缩示例，以及一个 --advise 模式，为每条拟执行的 shell 命令给出按颜色区分的安全评级。
- **[oc-auto-perms](https://github.com/OpeOginni/oc-plugins/tree/main/packages/oc-auto-perms)** · <sub>OpeOginni · GitHub · ⭐ 3 仓库 · 2026-09-17</sub><br>OpenCode 插件，用 Jev 按自然语言写的权限规则检查每个拟执行的工具操作，然后放行、拒绝或询问用户。
- **[Jackalope 的 Jev 支持](https://github.com/Jackalope-Dev/jackalope/blob/master/apps/desktop/src-tauri/src/commands/tasks/routing/jev.rs)** · <sub>Jackalope-Dev · GitHub · ⭐ 1 仓库 · 2026-09-16</sub><br>编程 agent 桌面工作区 Jackalope 中的 Jev 任务路由：每个候选 agent 和模型针对任务各得到一个推理契合度 Score 和一个工具支持 Noul，再由代码选出工人。
- **[Paseo 的 Jev 评估插件](https://github.com/HiepPP/hiep-paseo-plugin/tree/main/plugins/jev-evaluator)** · <sub>HiepPP · GitHub · ⭐ 1 仓库 · 2026-09-18</sub><br>Paseo 插件，经 Vercel AI Gateway 把 Jev 包装成 MCP 工具 jev_evaluate，提供给 Paseo 启动的 Codex 和 Claude agent，包括用它的 create_agent 创建的子 agent。
- **[用 Jev 为 deepagents 做上下文选择](https://x.com/HiroshiA_AI/status/2102214053489955208)** · <sub>HiroshiA_AI · X · ▶ 3 · 2026-09-22</sub><br>用基于 Jev 的上下文选择替换 LangChain deepagents 的 SummarizationMiddleware；在一个代码基准测试上，GLM-5.3 的成本降低 83.9%，Opus 4.8 降低 91.8%，12 个程序依然全部通过。
- **[Agent Handoff Gate](https://github.com/zsoXi/agent-handoff-gate)** · <sub>zsoXi · GitHub · 2026-09-17</sub><br>面向委派式编程工作的实验性协议，在工作 agent 的 PASS 或 BLOCKED 报告送达主 agent 之前先核查其背后的证据，附带 schema、Jev 集成契约和一个基准测试。
- **[agent-gate-loop](https://github.com/Ripwords/agent-gate-loop)** · <sub>Ripwords · GitHub · 2026-09-17</sub><br>可复用的 GitHub Action，把 issue 变成 pull request：AI agent 写出改动，再由护栏、你的检查、只读的 Claude 评审和 Jev 层层把关，最多重试 max_rounds 轮。
- **[Agent-Workflow 的 TypeSafe 路由](https://github.com/ngallodev-software/agent-workflow/blob/master/src/agent_workflow/semantic/typesafe.py)** · <sub>ngallodev-software · GitHub · 2026-09-19</sub><br>编程 agent 编排工具 Agent-Workflow 中可选的 TypeSafe provider，向 Jev 询问任务类别、是否缺少授权以及语义风险等建议性判断，最终决定权仍在确定性策略手里。
- **[check-risk](https://github.com/moezubair/check-risk)** · <sub>moezubair · GitHub · 2026-09-17</sub><br>CLI 和 GitHub Action，把一次 Git 改动转成可解释的风险分数、必需的检查项和评审人分组，结合了基于路径、依赖和 diff 的确定性规则与 Jev 语义信号。
- **[dsh-auto-mode](https://git.allen-software.com/allenh1/dsh-auto-mode)** · <sub>Hunter L. Allen · GitHub · 2026-09-17</sub><br>DeepSeek Harness 的自动模式权限预设：agent 每次在结束提示时留下的开放问题由 Jev 回答，拿不准时把这一轮交还给人。
- **[dsh-jev-tools](https://github.com/HorusJiang/dsh-jev-tools)** · <sub>HorusJiang · GitHub · 2026-09-20</sub><br>DeepSeek Harness 插件，用 Jev 把超过 2,000 token 的工具输出裁剪成与任务相关的片段、标记抓取页面中被注入的指令、推荐 skill，并对照证据核查“已完成”的说法。
- **[fast-jev-compaction-pi](https://github.com/joslynSmall/fast-jev-compaction-pi)** · <sub>joslynSmall · GitHub · 2026-09-20</sub><br>Pi 扩展，在上下文压缩之前运行，对每个已完成工具调用的证据决定保留、截断或丢弃，保留的部分原样保存，确保失败的测试日志、命令输出和精确的报错信息不丢失。
- **[foreman-jev](https://github.com/Shifty-Eye-Games/foreman-jev)** · <sub>Shifty-Eye-Games · GitHub · 2026-09-17</sub><br>实验性的监管器：Jev 通过 Vercel AI Gateway 监督一个 Codex 编程工人，由程序员指定的验收命令决定通过与否，另有一个只读的 Azure DevOps PR 评审流程。
- **[Formatho Jev Playground](https://www.formatho.com/tools/jev-playground)** · <sub>Formatho · 应用</sub><br>纯客户端的 System One API 请求构建器，可组合 state 以及 Noul、Choice 和 Score 问题，预览模拟的概率分布，并生成 typesafe_sdk 的 Python 代码。
- **[Graphlin](https://github.com/royosherove/graphlin)** · <sub>royosherove · GitHub · 2026-09-20</sub><br>在 Claude Code 或 Codex 探索和编辑你的代码时，在浏览器中实时展示架构图和活动图，可选用 Jev 对 agent 的活动分类。
- **[Herdr Jev Router](https://github.com/boriscardano/herdr-jev-router)** · <sub>boriscardano · GitHub · 2026-09-19</sub><br>Herdr agent.spawn 路径上的策略命令，在启动编程 agent 子进程之前，先检查缓存的服务商容量，向 Jev 请求类型化的选择并加以校验，然后写入一条脱敏的审计记录。
- **[Hey Jev, should I deploy?](https://heyjev.ai/shouldideploy)** · <sub>heyjev.ai · 应用</sub><br>部署前的直觉检查：用大白话描述你的部署，Jev 一次性回答 18 个类型化问题，网站再据此给出“上线”还是“等等”的结论。
- **[Highlighter](https://lab.saeed.sh/highlight)** · <sub>Saeed (stringsaeed) · 应用</sub><br>语法高亮工具：把代码切分成 token，由 Jev 判断语言、每个 token 的含义，以及它违反了九条 lint 规则中的哪几条。
- **[Jackalope](https://jackalope.dev)** · <sub>Jackalope · 应用 · 2026-09-06</sub><br>桌面工作区，可在 Git worktree 上并行运行 Codex、Claude Code、OpenCode 等编程 agent，由 Jev 为每个任务挑选 agent、执行基础评审检查并提供上下文。
- **[jev](https://github.com/sebastianbugal/jev)** · <sub>sebastianbugal · GitHub · 2026-09-18</sub><br>Claude Code 插件：你用大白话提问，Claude 通过 OpenRouter 把它转成类型化的 Jev 问题，你拿到一个带概率的类型化答案，置信度低的结果会被标注出来。
- **[用 Jev 做 LLM 模型路由](https://dev.classmethod.jp/en/articles/jev-for-llm-model-routing/)** · <sub>Classmethod DevelopersIO (Morinaga) · 文章 · 2026-09-17</sub><br>一个实验：把 NeMo Switchyard 式编程 agent 路由中的 LLM 分类器换成四档的 Jev Choice；40 次调用全部命中预期档位，中位延迟约 0.66 s，每次调用 $0.000025。
- **[Claude Code 的 Jev 模型路由器](https://github.com/davila7/claude-code-templates/tree/main/cli-tool/components/mods/productivity/jev-model-router)** · <sub>GitHub</sub><br>一个 hook，在一次请求中问一个档位 Choice、一个推理强度 Score 和一个风险 Noul，然后据此调整模型和推理强度。
- **[Jev Review](https://github.com/thiago-ss/jev-review)** · <sub>thiago-ss · GitHub · 2026-09-16</sub><br>自主的 pull request 评审机器人，把 PR 元数据和补丁作为有限的类型化问题交给 Jev，套用确定性的批准闸门，并把不确定或有风险的评审转给可信的负责人。
- **[Jev Turn Analysis](https://github.com/hobbs/jev-turn-analysis)** · <sub>hobbs · GitHub · 2026-09-20</sub><br>Rust CLI，读取已结束的 Claude Code 和 Codex 会话，用 Jev 从成功与否、验证情况和无效投入等方面打分，并对指令、skill 和工具提出修改建议。
- **[jev-fit](https://jev-fit.com)** · <sub>jev-fit · 应用</sub><br>托管的检查工具，读取你粘贴的软件点子，判断它适合用普通代码、Jev 还是推理型 LLM 来实现，置信度低时回答“不确定”。
- **[jev-free-router](https://github.com/Loule95450/jev-free-router)** · <sub>Loule95450 · GitHub · 2026-09-18</sub><br>OpenCode 的 provider 插件，每来一条新消息，Jev 就估算免费的 Zen 或 Go 目录中哪个模型最适合这个请求并路由过去，OpenAI 和 Anthropic 的模型被排除在外。
- **[jev-gates](https://github.com/rashedInt32/jev-gates)** · <sub>rashedInt32 · GitHub · 2026-09-18</sub><br>由 Jev 评判的 Claude Code hook 闸门，能拦下违反 CLAUDE.md 规则的编辑、超出范围的改动、没被回应的要求、虚假的“测试通过”说法，以及 diff 撑不起的提交信息；这些闸门从不做批准。
- **[jev-mcp (minhgv)](https://github.com/minhgv/jev-mcp)** · <sub>minhgv · GitHub · 2026-09-17</sub><br>MCP 服务器，把 Jev 放进 OpenCode、Cursor、Codex 和 CI 的编程循环，提供的工具可以决定重试、停止或模型档位，审查 diff，评估改动风险并检查需求。
- **[jev-router](https://github.com/hyspacex/jev-router)** · <sub>hyspacex · GitHub · 2026-09-19</sub><br>可自托管的模型路由器，面向编程 agent 和 OpenAI 兼容客户端，让 Jev 评估每个新任务，再套用 YAML 规则选择模型和推理强度，并在会话内固定下来。
- **[jev-router (daviddl9)](https://github.com/daviddl9/jev-router)** · <sub>daviddl9 · GitHub · 2026-09-21</sub><br>OMP 和 Pi 编程 agent 的路由扩展，由 Jev 为每一步选择工人档位，规划和评审留在强模型上，有边界的任务交给更便宜的工人。
- **[jev-router (flaviusapop)](https://github.com/flaviusapop/jev-router)** · <sub>flaviusapop · GitHub · 2026-09-18</sub><br>Claude Code、Codex、Grok CLI 和 opencode 的启动器，让 Jev 把每一轮路由到能完成它的最便宜模型和推理深度，只改写 model 字段，并沿用现有的登录状态。
- **[jev-router (gmaxxxie)](https://github.com/gmaxxxie/jev-router)** · <sub>gmaxxxie · GitHub · 2026-09-19</sub><br>Pi 扩展，用 Jev 对每条提示词分类，在现有的 Pi 登录下切换到能胜任的最便宜模型和思考深度，每次决策约 $0.00002、0.9 s。
- **[jev-router (ianlintner)](https://github.com/ianlintner/jev-router)** · <sub>ianlintner · GitHub · 2026-09-19</sub><br>回环的影子模式代理，在不改变线上路由的前提下，对比 Jev 的特征提取与 Switchyard 的 coding_agent 路由分类器，并导出 Prometheus 指标和 Grafana 看板。
- **[jev-skill-scout](https://github.com/karanb192/jev-skill-scout)** · <sub>karanb192 · GitHub · 2026-09-19</sub><br>审计 CLI，把 Claude Code 对话记录交给 Jev 回放，找出本该加载 skill 却没有加载的轮次，另有一个实时推荐 skill 的 mod；作者发现需要 skill 的轮次中有 72% 一个都没加载。
- **[JevCoder](https://github.com/aruniyer/jevcoder)** · <sub>aruniyer · GitHub · 2026-09-18</sub><br>Pi 编程 agent 扩展，由 Jev 选择每一个下一步动作（某个工具、编辑代码或结束），再由 Pi 模型填充参数，工具 schema 保持缓存稳定，附有 SWE-bench Verified 实验。
- **[jevgrep](https://github.com/allebee/jevgrep)** · <sub>allebee · GitHub · 2026-09-21</sub><br>流式的按语义 grep CLI，用于日志等文本，每一行向 Jev 问一个是/否问题，匹配结果在写入后约 0.7 s 打印出来，每 1,000 行约 $0.004，并附有与 Claude 的基准对比。
- **[JevGuard](https://github.com/Jhonnyr97/JevGuard)** · <sub>Jhonnyr97 · GitHub · 2026-09-21</sub><br>Claude Code 和 Codex CLI 插件，把 CLAUDE.md 或 AGENTS.md 转成项目规则，在 PreToolUse 和 Stop hook 中用 Jev 检查，而不是指望 agent 自己记得这些规则。
- **[jevmory](https://github.com/romiluz13/jevmory)** · <sub>romiluz13 · GitHub · 2026-09-19</sub><br>本地、零依赖的编程 agent 记忆系统，每条存储的事实都是一段原文引用，并由 Jev 按置信度评级，MEMORY.md 会对照会话证据接受审计，审计回执存入 SQLite。
- **[JevTest](https://github.com/CorieW/JevTest)** · <sub>CorieW · GitHub · 2026-09-17</sub><br>用于探索式浏览器测试的 TypeScript 库和 CLI：Jev 朝着目标选择操作并评判结果，Playwright 在隔离的会话中执行，最终由精确的断言决定通过与否。
- **[Moongate](https://github.com/brickfrog/moongate)** · <sub>brickfrog · GitHub · 2026-09-19</sub><br>用 MoonBit 写的 GitHub Action，按以 JSON 存储的语义规则检查 PR diff：Jev 对每条规则回答违规、合规或证据不足，再由你设的阈值决定标注和退出码。
- **[omp-jevens-classifier](https://github.com/STRML/omp-jevens-classifier)** · <sub>STRML · GitHub · 2026-09-16</sub><br>OMP 编程 agent 的权限闸门：在 yolo 模式下原本会不经查看就执行的 bash 命令和会派生进程的 eval 载荷，都先交给 Jev 判断，危险的那些会变成“运行还是拒绝”的确认提示。
- **[OpenCode 任务路由器](https://dev.to/lbobylev/routing-opencode-tasks-with-jev-2c4n)** · <sub>l3o6 · 文章 · 2026-09-18</sub><br>OpenCode 的一个工具，通过 OpenRouter 就每个任务向 Jev 提三个问题（协调、不确定性、后果），再对照一个由后果决定的阈值，选用强模型或弱模型。
- **[Pi Agent Foreman](https://github.com/alexshpunt/pi-agent-foreman)** · <sub>alexshpunt · GitHub · 2026-09-13</sub><br>Pi 扩展，每次运行结束后审查最后一轮对话，如果 agent 承认必要的工作还没做完就停下了，就发一条措辞坚决的指令让它把活干完。
- **[pi-jev-code](https://github.com/KamilPostrozny/pi-jev-code)** · <sub>KamilPostrozny · GitHub · 2026-09-17</sub><br>Pi 编程会话的 Jev 协处理器，你的 Pi 模型仍是唯一的编程 agent，它在此之外加上语义闸门、从基线到当前状态的 diff 审查和仅追加的遥测记录。
- **[pi-jev-compact](https://github.com/ilkerulusoy/pi-jev-compact)** · <sub>ilkerulusoy · GitHub · 2026-09-18</sub><br>Pi 编程 agent 的上下文压缩扩展，丢弃不再需要的工具调用和结果，其余部分原样保留而不做摘要。
- **[pi-jev-effort](https://github.com/namenu/pi-jev-effort)** · <sub>namenu · GitHub · 2026-09-21</sub><br>Pi 扩展，根据 Jev 对提示词难度的 Score（从极简单到困难）设定每条提示词的思考档位，上限受剩余额度约束，每次判断约 250 毫秒、$0.000015。
- **[pi-jev-harness](https://github.com/MoonTory/pi-jev-harness)** · <sub>MoonTory · GitHub · 2026-09-17</sub><br>Pi 扩展，由 Jev 为每一轮做路由、挑选要预取的文件、裁剪冗长的工具结果、检测死循环并守护工具调用，让主模型只把 token 花在生成上。
- **[pi-jev-permit](https://github.com/kurihada/pi-jev-permit)** · <sub>kurihada · GitHub · 2026-09-20</sub><br>Pi 编程 agent 的权限闸门，在本地硬性拒绝规则和只读快速通道之后，让 Jev 在每次 bash、write 和 edit 调用执行前做判断。
- **[pi-typesafe](https://github.com/twilwa/pi-typesafe)** · <sub>twilwa · GitHub · 2026-09-17</sub><br>Pi 编程 agent 的 Jev 边车，在 bash、write 和 edit 之前运行四项风险检查，编辑之后再运行四项 diff 质量检查，支持建议、拦截和影子三种模式。
- **[pi-typesafe-router](https://github.com/jekozyra/pi-typesafe-router)** · <sub>jekozyra · GitHub · 2026-09-18</sub><br>Pi 扩展，让 Jev 给每个请求分类并路由到三个配置好的模型之一，附带一个 doctor 命令，在启用路由前用合成请求测试分类器和各个模型。
- **[pkg-gate](https://github.com/hemanth/pkg-gate)** · <sub>hemanth · GitHub · 2026-09-17</sub><br>npm 的安装前安全闸门，在 preinstall、install 和 postinstall 脚本运行前，并行评估它们的意图、威胁严重度、是否访问密钥以及是否远程执行。
- **[Port Cleanup](https://github.com/epiphany-dynamics/port-cleanup)** · <sub>epiphany-dynamics · GitHub · 2026-09-19</sub><br>原生 macOS 工具，列出所有监听中的 TCP 端口及其进程和项目上下文，并建议哪些可以安全停止；每次停止都要你确认。
- **[Reflex](https://github.com/kaustav1996/reflex)** · <sub>kaustav1996 · GitHub · 2026-09-18</sub><br>基于 Pi 的编程 agent 兼个人助理，每个会改变状态的工具调用都要经过一次 Jev 请求（五个风险 Noul 加一个风险 Score），在代码中映射为放行、询问或拦截，模型档位也由 Jev 选择。
- **[sgrep](https://github.com/Lagnajit09/sgrep)** · <sub>Lagnajit09 · GitHub · 2026-09-19</sub><br>语义 grep，把代码库切成块，先用本地小型 embedding 模型预筛，再逐块问 Jev 是否匹配一条英文查询，按校准后的置信度排序。
- **[System One Search](https://github.com/cpaczek/s1s)** · <sub>cpaczek · GitHub · 2026-09-17</sub><br>代码导航工具，用 Jev 和仓库证据找出某个问题背后的文件、梳理某个主题、跨文件追踪它，并报告 harness 已经查看过哪些内容，回答中只给出真实存在的路径和引用。
- **[The Jev-enator](https://github.com/jakenbear/the-jev-enator)** · <sub>jakenbear · GitHub · 2026-09-20</sub><br>在 agent 循环内使用 Jev 的 Claude Code hook：PreToolUse 危险闸门拦截破坏性调用，PostToolUse 发出失败提示，另有可选的完成度检查，用录制好的 cassette 离线测试。
- **[typesafe-bash-guard](https://github.com/gowthamgts/pi-stuff/tree/main/extensions/typesafe-bash-guard)** · <sub>gowthamgts · GitHub · 2026-07-23</sub><br>个人合集里的一个 Pi 扩展，在执行前让 Jev 给 bash 工具调用和以 ! 开头的 shell 命令分类，拦住可能有害的命令，支持 1Password 的 op:// 密钥引用。
- **[typesafe-comment](https://github.com/Hexdigest123/typesafe-comment)** · <sub>Hexdigest123 · GitHub · 2026-09-17</sub><br>Python linter，从有用性、可读性、准确性、冗余度和覆盖度给代码注释打分，支持 Python、C、C++、JavaScript 等语言，低于阈值时以非零状态退出，让流水线拦下。
- **[typesafeai-review](https://github.com/rbalch/typesafeai-review)** · <sub>rbalch · GitHub · 2026-09-17</sub><br>以开发依赖形式发布的代码审查工具：代码负责运行检查和切分 diff，Jev 对每个 hunk 回答范围很窄的带类型问题，再由代码汇总出结论、分数和发现。
- **[zcode-jev](https://github.com/Zahrannnn/zcode-jev)** · <sub>Zahrannnn · GitHub · 2026-09-16</sub><br>编程 agent 的类型化判断层，从 PRD 接收一路到覆盖率、CI 分诊和发布都设有闸门，目前使用任意强制 JSON 输出的 LLM，Jev 后端已按文档中的约定写好，但还没有实际测试过。

</details>

还缺什么？[提交一个资源](https://github.com/Li-Evan/awesome-jev/issues/new/choose)。
