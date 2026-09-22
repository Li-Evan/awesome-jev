# 🌐 浏览器与电脑操控

[English](https://github.com/Li-Evan/awesome-jev/blob/main/scenarios/browser.md) · **简体中文**

在真实浏览器、桌面和手机上点击、输入和导航的 agent。共 128 条，按社区热度排序。

[← 返回 Awesome Jev](https://github.com/Li-Evan/awesome-jev/blob/main/README.zh-CN.md#按场景浏览)

<table>
<tr>
<td width="260" valign="top"><a href="https://github.com/browser-use/jev-ultrafast"><img src="https://raw.githubusercontent.com/browser-use/jev-ultrafast/main/docs/banner.svg" alt="jev-ultrafast" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/browser-use/jev-ultrafast">jev-ultrafast</a></b><br><sub>browser-use · GitHub · ⭐ 16.6k · 2026-09-16</sub><br>浏览器 agent：每一步在一次请求里从页面元素表中选出操作和目标，并为每种操作预先推测一个目标，只有需要输入文字时才调用小型 LLM。<br><sub>相关: <a href="https://x.com/innoiso/status/2101128674779263220">demo</a> · <a href="https://news.ycombinator.com/item?id=49735979">discussion</a> · <a href="https://browser-use.com/ultrafast">website</a> · <a href="https://www.youtube.com/watch?v=NFKHLhAvj1g">video</a> · <a href="https://agentbreaking.com/blog/browser-use-jev-ultrafast-guide/">write-up</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/Saccc_c/status/2100864907046768890"><img src="https://pbs.twimg.com/amplify_video_thumb/2100853279089647616/img/H6altwjZQ28_1bfY.jpg" alt="Jev Use for Codex" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/Saccc_c/status/2100864907046768890">Jev Use for Codex</a></b><br><sub>Saccc_c · X · ♥ 1.8k · 2026-09-18</sub><br>以 Jev 为决策层的 Codex 电脑操控，演示中添加 Mac 日历事件比 Codex 内置的电脑操控更快更流畅，token 成本相近。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/thdxr/status/2100288951978164647"><img src="https://pbs.twimg.com/amplify_video_thumb/2100286679386873857/img/vlw6EBlSVZ9uAoHc.jpg" alt="OpenCode 用 Jev 做浏览器操控" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/thdxr/status/2100288951978164647">OpenCode 用 Jev 做浏览器操控</a></b><br><sub>thdxr · X · ♥ 3.7k · 2026-09-16</sub><br>面向应用测试的快速浏览器自动化预览，把 Jev 与 OpenCode 的 browser-use CLI 搭配使用。<br><sub>相关: <a href="https://x.com/Neriousy/status/2100287208166969746">demo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/awlevin/typesafe-computer-use"><img src="https://raw.githubusercontent.com/awlevin/typesafe-computer-use/main/docs/banner.svg" alt="typesafe-computer-use" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/awlevin/typesafe-computer-use">typesafe-computer-use</a></b><br><sub>awlevin · GitHub · ⭐ 769 · 2026-09-16</sub><br>macOS 电脑操控 agent：先对屏幕做 OCR，再让 Jev 从提取出的控件中判定下一步动作并点击，每步约 $0.0002，只有自由文本字段才调用写作模型。<br><sub><b>Jev 用法:</b> 每一步在最多 255 个确定性提取的动作上做一个 Choice，并按其置信度设门槛。</sub><br><sub>相关: <a href="https://news.ycombinator.com/item?id=49733647">discussion</a> · <a href="https://x.com/awlevin/status/2100262612428894676">demo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/milind-soni/tiptour-macos"><img src="https://raw.githubusercontent.com/milind-soni/tiptour-macos/main/gemnew.png" alt="TipTour" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/milind-soni/tiptour-macos">TipTour</a></b><br><sub>milind-soni · GitHub · ⭐ 644 · 2026-04-08</sub><br>macOS 菜单栏电脑操控应用，默认模式接收一个以点击为主的文字任务，让 Jev 在本地检测到的屏幕控件中做选择，然后执行并验证每个动作。<br><sub>相关: <a href="https://www.supamaus.com/">site</a> · <a href="https://x.com/milindlabs/status/2100631847155994852">demo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/SUOHA_AI/status/2101640575812239406"><img src="https://pbs.twimg.com/amplify_video_thumb/2101632970717007872/img/lcQeA281BT79Pjt5.jpg" alt="Jev + DeepSeek 表单填写 agent" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/SUOHA_AI/status/2101640575812239406">Jev + DeepSeek 表单填写 agent</a></b><br><sub>SUOHA_AI · X · ♥ 173 · 2026-09-20</sub><br>浏览器 agent，在一个陌生网站上用 38 秒填完一份 16 题的申请表，Jev 选择每个动作，DeepSeek V4.1 Flash 撰写文字答案。<br><sub><b>Jev 用法:</b> 每个页面做一次点击、勾选或提交的 Choice；小型 LLM 只填写文本字段。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/savboj/status/2100545295201288678"><img src="https://pbs.twimg.com/amplify_video_thumb/2100545038677655552/img/PSyeykC06q5OLVVu.jpg" alt="极速电脑操控" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/savboj/status/2100545295201288678">极速电脑操控</a></b><br><sub>savboj · X · ♥ 1.3k · 2026-09-17</sub><br>电脑操控演示：Jev 选择每个动作的速度快到任务眨眼间就完成，号称比 LLM 快 100 倍。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/SUOHA_AI/status/2102091983292358839"><img src="https://pbs.twimg.com/amplify_video_thumb/2102088489231609856/img/AJle7-1PDPdXWJ6d.jpg" alt="自动完成认证模拟考试" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/SUOHA_AI/status/2102091983292358839">自动完成认证模拟考试</a></b><br><sub>SUOHA_AI · X · ♥ 755 · 2026-09-21</sub><br>浏览器自动化在一个从未见过的页面上用 21 秒完成了阿里云 AI 工程师模拟考试，回答 25 道题，准确率 80%，由 Jev 决定每一步，DeepSeek 负责填写文字。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/camsoft2000/status/2100648648434434298"><img src="https://pbs.twimg.com/amplify_video_thumb/2100648485695451136/img/kZ4JFKvjuPY7i6iz.jpg" alt="Jev + AXe 控制 iOS 模拟器" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/camsoft2000/status/2100648648434434298">Jev + AXe 控制 iOS 模拟器</a></b><br><sub>camsoft2000 · X · ♥ 1.3k · 2026-09-17</sub><br>演示 Jev 配合 AXe CLI 驱动 iOS 模拟器，操作应用的速度比 LLM 快得多，成本只是其零头。<br><sub>相关: <a href="https://github.com/cameroncooke/AXe">axe</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/cline/plugins/tree/main/plugins/jev-browser"><img src="https://github.com/user-attachments/assets/063c98fa-0067-40fb-af96-3714d8e017a5" alt="Cline jev-browser plugin" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/cline/plugins/tree/main/plugins/jev-browser">Cline jev-browser plugin</a></b><br><sub>cline · GitHub · ♥ 689 · 2026-05-31</sub><br>Cline 官方合集中的插件，基于结构化 DOM 观察，通过 Vercel AI Gateway 把有边界的 Playwright 浏览器步骤委托给 Jev，表单值由另一个文本模型填写。<br><sub>相关: <a href="https://github.com/cline/plugins">repo</a> · <a href="https://x.com/cline/status/2101056078872256935">demo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/kylejeong/status/2100622054945095934"><img src="https://pbs.twimg.com/amplify_video_thumb/2100495119065722880/img/7A1mijkU3Z_Zj7PM.jpg" alt="Stagehand + Jev 浏览器 agent" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/kylejeong/status/2100622054945095934">Stagehand + Jev 浏览器 agent</a></b><br><sub>kylejeong · X · ♥ 763 · 2026-09-17</sub><br>运行在远程浏览器上的浏览器 agent：Jev 从页面的无障碍树中选出每一步动作，由 Stagehand 执行；演示任务花费 $0.001。<br><sub><b>Jev 用法:</b> 以无障碍树为 state，以候选动作为问题，每一步一次决策。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/trycua/cua/tree/main/libs/cua-driver/examples/jev-use"><img src="https://raw.githubusercontent.com/trycua/cua/main/img/card-cua-fleets-wide.gif" alt="Cua jev-use" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/trycua/cua/tree/main/libs/cua-driver/examples/jev-use">Cua jev-use</a></b><br><sub>trycua · GitHub · ⭐ 25.8k 仓库 · 2026-09-18</sub><br>Cua Driver 中处于公开预览阶段的示例：Jev 从有限的候选 ID 中选择下一步浏览器动作，driver 负责观察页面、执行动作并验证结果，提供 Python 和 TypeScript 版本。<br><sub><b>Jev 用法:</b> Jev 看到的是候选 ID、描述以及精简的 DOM 或视觉区域观察，从不接触截图字节；答案必须是提供的某个 ID。</sub><br><sub>相关: <a href="https://github.com/trycua/cua">repo</a> · <a href="https://cua.ai">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/ndrezn/status/2101046780989215005"><img src="https://pbs.twimg.com/amplify_video_thumb/2101046492945387521/img/-lkFln33BamAm3cB.jpg" alt="用 LangChain 和 Jev 做浏览器操控" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/ndrezn/status/2101046780989215005">用 LangChain 和 Jev 做浏览器操控</a></b><br><sub>ndrezn · X · ♥ 103 · 2026-09-18</sub><br>基于 LangChain 和 Jev 搭建的浏览器 agent，能玩维基百科游戏（Wikipedia Game），也能处理找便宜机票这类日常任务。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/sarah_edo/status/2102025642862600634"><img src="https://pbs.twimg.com/ext_tw_video_thumb/2102025557969862656/pu/img/TDga5vamGpk6CRqZ.jpg" alt="WebMCP 侧边栏" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/sarah_edo/status/2102025642862600634">WebMCP 侧边栏</a></b><br><sub>sarah_edo · X · ♥ 845 · 2026-09-21</sub><br>Chrome 扩展侧边栏，驱动任意网站的 WebMCP 工具：每敲一个键，Jev 就选出相关的页面工具、填好参数并显示有多大把握，演示场景是网上买菜。<br><sub><b>Jev 用法:</b> 每次按键在页面的 WebMCP 工具上做一个 Choice，同时带置信度地填充参数。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://jev-browser-use.val.run"><img src="https://pbs.twimg.com/amplify_video_thumb/2100321453455425537/img/hVYy_d3Nuw9XhSwg.jpg" alt="Jev Browser Use" width="240"></a></td>
<td valign="top"><b><a href="https://jev-browser-use.val.run">Jev Browser Use</a></b><br><sub>Steve Krouse · 应用 · ♥ 240 · 2026-09-16</sub><br>描述一个任务，就能看着 Jev 驱动一个实时的 Kernel 云浏览器：给页面上每个链接打分，在“观察-选择-执行”循环中挑出下一次点击。<br><sub><b>Jev 用法:</b> 给页面上每个链接打分，再由一个 Choice 选出一个交给 Kernel 点击。</sub><br><sub>相关: <a href="https://x.com/stevekrouse/status/2100321685081559542">demo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/aibuilderclub_/status/2101316543317684368"><img src="https://pbs.twimg.com/amplify_video_thumb/2101316420290441216/img/7RW7_i5vB12EHIKy.jpg" alt="jev-browser" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/aibuilderclub_/status/2101316543317684368">jev-browser</a></b><br><sub>aibuilderclub_ · X · ♥ 402 · 2026-09-19</sub><br>面向 agent 的通用浏览器 skill：给定网站和任务，它打开浏览器，由 Jev 根据屏幕上的内容挑选每一次点击。<br><sub><b>Jev 用法:</b> 每一步在页面上可点击的元素中做一个 Choice。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/nicobailon/surf-cli"><img src="https://raw.githubusercontent.com/nicobailon/surf-cli/main/surf-banner.png" alt="Surf" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/nicobailon/surf-cli">Surf</a></b><br><sub>nicobailon · GitHub · ⭐ 622 · 2025-12-28</sub><br>零配置、供 AI agent 控制 Chrome 的 CLI，带一个可选的 semantic.act 模式：反复观察页面，让 Jev 从 Surf 允许的动作菜单中选出下一步并执行。<br><sub><b>Jev 用法:</b> 有界、目标驱动的控制，需用 --allow-semantic 显式开启；本地输入值永远不会发给 Jev。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/hqmank/status/2101529876469522673"><img src="https://pbs.twimg.com/amplify_video_thumb/2101529643073282048/img/HECGbREA0M-UMqNT.jpg" alt="jev-browser" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/hqmank/status/2101529876469522673">jev-browser</a></b><br><sub>hqmank · X · ♥ 403 · 2026-09-20</sub><br>通用浏览器自动化 skill，把 Jev 与 Playwright 控制的 Chrome 搭配，可跨 agent 使用，演示中在 Antigravity CLI 和 Codex 里查找相关文章和招聘信息。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Sac-Y/Jev-cu"><img src="https://opengraph.githubassets.com/1/Sac-Y/Jev-cu" alt="Jev-cu" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Sac-Y/Jev-cu">Jev-cu</a></b><br><sub>Sac-Y · GitHub · ⭐ 551 · 2026-09-18</sub><br>中文 Codex skill，把电脑操控中“下一次点哪里”的决策交给 Jev：它从屏幕文本候选中选出元素、动作、是否完成和风险，由 Codex Computer Use 读取和执行，不发送任何截图。<br><sub><b>Jev 用法:</b> 默认只做演练（dry-run）；删除、发送、付款和安装会停在确认步骤，应用必须在白名单上。</sub><br><sub>相关: <a href="https://x.com/Saccc_c/status/2101152089598791845">demo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/mormonnegro/status/2100408498446111031"><img src="https://pbs.twimg.com/amplify_video_thumb/2100406900772732928/img/Gh4W4M-xUTPc4I3X.jpg" alt="无头 Chromium 维基百科 agent" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/mormonnegro/status/2100408498446111031">无头 Chromium 维基百科 agent</a></b><br><sub>mormonnegro · X · ♥ 213 · 2026-09-17</sub><br>无头 Chromium agent，由 Jev 挑选每一个要点击的链接，在 Wikipedia 上用 20 秒从“Café”跑到“Inteligencia artificial”。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/razaanstha/ulka"><img src="https://pbs.twimg.com/amplify_video_thumb/2100645348309921792/img/-BZE38QFdJJ67AJa.jpg" alt="Ulka" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/razaanstha/ulka">Ulka</a></b><br><sub>razaanstha · GitHub · ⭐ 21 · 2026-09-17</sub><br>实验性浏览器 agent 扩展：FX 负责编排任务，Jev 从 Chromium 的无障碍树中选出受约束的动作，运行时负责校验目标、请求批准并记录证据。<br><sub>相关: <a href="https://news.ycombinator.com/item?id=49752776">discussion</a> · <a href="https://x.com/razaanstha/status/2100708222847853043">demo</a> · <a href="https://x.com/razaanstha/status/2100645675591520612">demo 2</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/wy-coliney/jev-browser-use"><img src="https://raw.githubusercontent.com/wy-coliney/jev-browser-use/main/assets/hero.png" alt="Jev Browser Use" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/wy-coliney/jev-browser-use">Jev Browser Use</a></b><br><sub>wy-coliney · GitHub · ⭐ 338 · 2026-09-18</sub><br>Codex 浏览器 skill，借助你现有的浏览器连接，由 Jev 处理导航、点击、切换和滚动，Codex 负责文本输入和最终检查，在作者的 EZCollegeApp 工作流中快约 5-10 倍。<br><sub><b>Jev 用法:</b> 通过 TypeSafe 或 OpenRouter Decisions 把页面状态和允许的候选发给 Jev；由浏览器连接执行。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/droidrun/mobile-jev"><img src="https://opengraph.githubassets.com/1/droidrun/mobile-jev" alt="mobile-jev" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/droidrun/mobile-jev">mobile-jev</a></b><br><sub>droidrun · GitHub · ⭐ 331 · 2026-09-17</sub><br>Android agent，把“操作加推测目标”的模式用到真实手机上。<br><sub>相关: <a href="https://mobilerun.ai">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/wobsoriano/touchpress"><img src="https://pbs.twimg.com/amplify_video_thumb/2100812811287031808/img/4TPBFtSzCOnjlkbR.jpg" alt="touchpress" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/wobsoriano/touchpress">touchpress</a></b><br><sub>wobsoriano · GitHub · ⭐ 28 · 2026-09-06</sub><br>移动应用端到端测试库，其 act 步骤可以交给 Jev 这类评估模型驱动，从当前屏幕提供的动作中选出每一步。<br><sub><b>Jev 用法:</b> 把 use.evaluationModel 设为 typeSafeAi.evaluationModel('jev-latest') 或 'typesafe-ai/jev-latest'；它会在 act 中替代语言模型。</sub><br><sub>相关: <a href="https://x.com/wobsoriano/status/2100813615410634997">demo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/shhivv/third-hand"><img src="https://opengraph.githubassets.com/1/shhivv/third-hand" alt="Third Hand" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/shhivv/third-hand">Third Hand</a></b><br><sub>shhivv · GitHub · ⭐ 285 · 2026-09-19</sub><br>macOS 菜单栏电脑操控助手：按 Control-Space 接收指令，读取当前聚焦应用的无障碍控件，然后输入、点击并检查结果，每一步决策都由 Jev 做出。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/jkudish/jev-browser"><img src="https://raw.githubusercontent.com/jkudish/jev-browser/main/assets/github-demo.gif" alt="jev-browser" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/jkudish/jev-browser">jev-browser</a></b><br><sub>jkudish · GitHub · ⭐ 231 · 2026-09-17</sub><br>无头浏览器驱动，可作为 MCP 服务器、CLI 或库使用，用一个 Choice 决定下一步动作，用 Noul 判断是否完成或卡住。<br><sub>相关: <a href="https://x.com/jkudish/status/2100704171020493247">demo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/SSHCodes/status/2101026313871970721"><img src="https://pbs.twimg.com/amplify_video_thumb/2101026173631217664/img/icEy9hbMZ8lMNbQV.jpg" alt="浏览器 agent 压力测试" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/SSHCodes/status/2101026313871970721">浏览器 agent 压力测试</a></b><br><sub>SSHCodes · X · ♥ 26 · 2026-09-18</sub><br>一次不作弊的浏览器操控测试，Jev 完成了大约 5 个动作后就崩了，作者的结论是它不适合做浏览器 agent。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://www.youtube.com/watch?v=VQPs9_US1xw"><img src="https://i.ytimg.com/vi/VQPs9_US1xw/hqdefault.jpg" alt="Jev 浏览器控制系统" width="240"></a></td>
<td valign="top"><b><a href="https://www.youtube.com/watch?v=VQPs9_US1xw">Jev 浏览器控制系统</a></b><br><sub>Marcin AI · 视频 · ♥ 43 · 2026-09-18</sub><br>围绕 Jev 构建的浏览器控制系统，几乎实时地下在线国际象棋、浏览网站、在 Amazon 购物，并接受语音命令，决策都由 Jev 做出。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://www.youtube.com/watch?v=JsNQwFB9N1Q"><img src="https://i.ytimg.com/vi/JsNQwFB9N1Q/hqdefault.jpg" alt="rtrvr.ai" width="240"></a></td>
<td valign="top"><b><a href="https://www.youtube.com/watch?v=JsNQwFB9N1Q">rtrvr.ai</a></b><br><sub>Retriever AI · 视频 · ♥ 31 · 2026-09-17</sub><br>在 rtrvr.ai 浏览器 agent 里用真实网页任务测试 Jev，讲清它在哪些地方好用、哪些地方吃力，以及它今后如何与更大的模型搭配。<br><sub>相关: <a href="https://rtrvr.ai/blog/jev-browser-agent-benchmark">benchmark</a> · <a href="https://rtrvr.ai/extension">app</a> · <a href="https://rtrvr.ai">project</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/shhivv/arc-cua"><img src="https://opengraph.githubassets.com/1/shhivv/arc-cua" alt="arc-cua" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/shhivv/arc-cua">arc-cua</a></b><br><sub>shhivv · GitHub · ⭐ 127 · 2026-09-20</sub><br>面向电脑操控 agent 的动作层：规划器把有边界的桌面子任务交给 Jev，由 Jev 逐步运行 UI 循环，带新鲜度防护，完成后再交还控制权。<br><sub>相关: <a href="https://tryisle.com">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/plateaukao/einkbro/blob/main/app/src/main/java/info/plateaukao/einkbro/data/remote/JevReaderRepository.kt"><img src="https://repository-images.githubusercontent.com/253150295/e0705e24-5fef-4c71-9c4e-93f1f8c91d8b" alt="EinkBro Jev reader" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/plateaukao/einkbro/blob/main/app/src/main/java/info/plateaukao/einkbro/data/remote/JevReaderRepository.kt">EinkBro Jev reader</a></b><br><sub>plateaukao · GitHub · ⭐ 2k 仓库 · 2020-04-05</sub><br>E-Ink 安卓浏览器 EinkBro 用 Jev 给页面区块分类，生成干净的阅读视图，只丢弃高置信度判定为非正文的内容。<br><sub><b>Jev 用法:</b> 对每个候选区块，基于文本、标签、role、class 和链接比例提问；判断不确定或失败时，Readability 的结果保持不变。</sub><br><sub>相关: <a href="https://plateaukao.github.io/einkbro">docs</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/agent-labs-dev/fastbrowse"><img src="https://raw.githubusercontent.com/agent-labs-dev/fastbrowse/main/assets/wordmark.svg" alt="fastbrowse" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/agent-labs-dev/fastbrowse">fastbrowse</a></b><br><sub>agent-labs-dev · GitHub · ⭐ 94 · 2026-09-17</sub><br>实验性浏览器 agent，把页面索引成候选动作供 Jev 挑选，由 LLM 负责规划和阅读，要求答案中的每个论断都引用页面原文，有实质后果的操作需要授权。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/APUS-AI-Lab/fast-browser-use"><img src="https://raw.githubusercontent.com/APUS-AI-Lab/fast-browser-use/main/docs/banner.svg" alt="Fast Browser Use" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/APUS-AI-Lab/fast-browser-use">Fast Browser Use</a></b><br><sub>APUS-AI-Lab · GitHub · ⭐ 90 · 2026-09-19</sub><br>面向 Claude Code、Codex 和 Cursor 的本地浏览器操控 agent skill，用 Qwen3.5 权重复现 Jev 的 System One 范式，把可见元素当作单 token 选项打分。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/savka777/jev-use"><img src="https://raw.githubusercontent.com/savka777/jev-use/main/docs/banner.png" alt="jev-use" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/savka777/jev-use">jev-use</a></b><br><sub>savka777 · GitHub · ⭐ 86 · 2026-09-19</sub><br>原生 macOS 电脑操控应用：按住快捷键，说出或输入你想做的事，它通过读取 Accessibility 树在屏幕上执行操作，不需要截图，也不需要视觉模型。<br><sub><b>Jev 用法:</b> Jev 从 Accessibility 元素中挑选下一步屏幕操作；由 macOS 执行。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/sdras/jev-webmcp-extension"><img src="https://raw.githubusercontent.com/sdras/jev-webmcp-extension/main/icons/screenshot.jpg" alt="Jev × WebMCP" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/sdras/jev-webmcp-extension">Jev × WebMCP</a></b><br><sub>sdras · GitHub · ⭐ 85 · 2026-09-19</sub><br>Chrome 侧边栏扩展，发现页面暴露的 WebMCP 工具，在你输入时用 Jev 挑选并填好正确的工具调用，显示置信度和延迟，无需针对站点做任何配置。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/lahfir/agent-desktop/tree/main/scripts/jev"><img src="https://raw.githubusercontent.com/lahfir/agent-desktop/main/docs/architecture.png" alt="Agent Desktop Jev skill" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/lahfir/agent-desktop/tree/main/scripts/jev">Agent Desktop Jev skill</a></b><br><sub>lahfir · GitHub · ⭐ 1.4k 仓库 · 2026-09-17</sub><br>agent-desktop Rust 电脑操控（computer use）CLI 的 Jev skill，根据一个目标驱动桌面应用：读取无障碍树，每轮选出一个操作和目标，无障碍树不进入 agent 的上下文。<br><sub><b>Jev 用法:</b> 每轮在同一次请求中询问操作（CLICK、TYPE_TEXT、DRILL、DONE 等）以及该操作的目标。</sub><br><sub>相关: <a href="https://github.com/lahfir/agent-desktop">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/sahibzada-allahyar/gliner2-ultrafast"><img src="https://raw.githubusercontent.com/sahibzada-allahyar/gliner2-ultrafast/main/docs/demo.gif" alt="GLiNER Browser Use" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/sahibzada-allahyar/gliner2-ultrafast">GLiNER Browser Use</a></b><br><sub>sahibzada-allahyar · GitHub · ⭐ 67 · 2026-09-18</sub><br>改编自 Browser Use 的 Jev Ultrafast 的浏览器自动化，把决策层换成本地开放权重的 GLiNER2 来给页面控件打分，输入值由小型文本模型负责。<br><sub>相关: <a href="https://github.com/browser-use/jev-ultrafast">upstream</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Ying-Kai-Liao/jev-browser"><img src="https://opengraph.githubassets.com/1/Ying-Kai-Liao/jev-browser" alt="jev-browser" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Ying-Kai-Liao/jev-browser">jev-browser</a></b><br><sub>Ying-Kai-Liao · GitHub · ⭐ 67 · 2026-09-16</sub><br>浏览器自动化库、CLI 和 MCP 服务器，由调用方 LLM 说明每一步的目标，Jev 选出元素、动作和值，Playwright 负责执行。<br><sub><b>Jev 用法:</b> 每轮一次约 300 毫秒的请求，询问哪个元素、什么动作、什么值，以及这一步是否已完成、受阻、出错或即将执行不可逆操作。</sub><br><sub>相关: <a href="https://github.com/user-attachments/assets/2e688df9-4985-4854-8ebe-ba97c9d13d68">video</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/FluidInference/FluidUse"><img src="https://opengraph.githubassets.com/1/FluidInference/FluidUse" alt="FluidUse" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/FluidInference/FluidUse">FluidUse</a></b><br><sub>FluidInference · GitHub · ⭐ 62 · 2026-09-21</sub><br>Apple 芯片上的本地电脑操控：通过 Accessibility API 读取 Mac 应用中的表单并在设备端填写。附带 Jev 风格 laya 模型的 Core ML 移植版，在 Neural Engine 上每个短问题 3.7 毫秒。<br><sub><b>Jev 用法:</b> LayaManager 在设备端回答关于文本 state 的类型化 choice/score/noul 问题；表单由 CUA-S1-FORMS 专用模型处理。</sub><br><sub>相关: <a href="https://huggingface.co/FluidInference/laya-coreml">model</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/yikangy873-gif/jev-desktop"><img src="https://opengraph.githubassets.com/1/yikangy873-gif/jev-desktop" alt="Jev Desktop for Codex" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/yikangy873-gif/jev-desktop">Jev Desktop for Codex</a></b><br><sub>yikangy873-gif · GitHub · ⭐ 60 · 2026-09-19</sub><br>为 Codex Computer Use 增加有边界决策循环的插件，适用于浏览器标签页和原生 macOS 应用：Codex 设定目标和允许的动作，Jev 每一步选出操作和目标，由 Computer Use 执行。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/webbrain-one/webbrain/blob/main/src/chrome/src/agent/systemone-fast.js"><img src="https://raw.githubusercontent.com/webbrain-one/webbrain/main/assets/webbrain-demo.gif" alt="WebBrain 的 System One agent" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/webbrain-one/webbrain/blob/main/src/chrome/src/agent/systemone-fast.js">WebBrain 的 System One agent</a></b><br><sub>webbrain-one · GitHub · ⭐ 1.1k 仓库 · 2026-04-06</sub><br>开源的 Chrome/Firefox 浏览器 agent WebBrain 在 agent 循环里把 Jev 用作快速分类器和评判者，证据会先脱敏，并设有置信度阈值。<br><sub><b>Jev 用法:</b> 快速、评判和证据分成独立模块，分类器阈值 0.85，浏览器阈值 0.90。</sub><br><sub>相关: <a href="https://webbrain.one">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/gergomoricz/status/2100301843507159443"><img src="https://pbs.twimg.com/amplify_video_thumb/2100301754411659264/img/EHQ6OuvTeyHuSC4M.jpg" alt="Jev 浏览器操控演示" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/gergomoricz/status/2100301843507159443">Jev 浏览器操控演示</a></b><br><sub>gergomoricz · X · ♥ 28 · 2026-09-16</sub><br>录屏：由 Jev 驱动的浏览器 agent 实时点击浏览网页。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/affirmitv/ghosthands"><img src="https://opengraph.githubassets.com/1/affirmitv/ghosthands" alt="ghosthands" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/affirmitv/ghosthands">ghosthands</a></b><br><sub>affirmitv · GitHub · ⭐ 49 · 2026-08-27</sub><br>通过一块 $4 的 USB-HID 微控制器驱动真实屏幕的 GUI 自动化，由 Jev 从带索引的控件表中选出操作和元素；一次点击步骤约 $0.0001、0.4 秒。<br><sub><b>Jev 用法:</b> 快速通道是经 OpenRouter decisions 端点的一次 Jev 调用；没有元素表的屏幕交给小型视觉 LLM 处理。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/ipenywis/laya-ultrafast"><img src="https://opengraph.githubassets.com/1/ipenywis/laya-ultrafast" alt="Laya Ultrafast" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/ipenywis/laya-ultrafast">Laya Ultrafast</a></b><br><sub>ipenywis · GitHub · ⭐ 48 · 2026-09-21</sub><br>Browser Use 的 jev-ultrafast 浏览器 agent 的本地移植版，不调用托管的 Jev，而是在 Apple Silicon 上通过 MLX 运行开放的 Laya 模型来做决策。<br><sub>相关: <a href="https://github.com/browser-use/jev-ultrafast">original</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/ndrezn/ts-browser-agent"><img src="https://raw.githubusercontent.com/ndrezn/ts-browser-agent/main/docs/wiki_game.gif" alt="ts-browser-agent" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/ndrezn/ts-browser-agent">ts-browser-agent</a></b><br><sub>ndrezn · GitHub · ⭐ 30 · 2026-09-18</sub><br>基于 langchain-typesafe 和 LangChain 的 create_agent 构建的浏览器 agent，以 Jev 为模型、浏览器动作为工具，演示了从 LangChain 词条一路玩维基百科游戏到 Microphone 词条。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/nottecore/status/2101021237417787819"><img src="https://pbs.twimg.com/amplify_video_thumb/2101020534754422784/img/j_5WSNZVx35w--DS.jpg" alt="Jevmaxxing" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/nottecore/status/2101021237417787819">Jevmaxxing</a></b><br><sub>nottecore · X · ♥ 12 · 2026-09-18</sub><br>基于 Notte 云会话的浏览器 agent：输入一个任务，Jev 从页面的动作空间中挑选每个动作，并可逐步回放每次决策。<br><sub><b>Jev 用法:</b> 每一步在新提取的动作空间上做一个 Choice。</sub><br><sub>相关: <a href="http://jevmaxxing.com">app</a> · <a href="https://github.com/nottelabs/notte-jevmaxxing">repo</a> · <a href="https://github.com/nottelabs/notte-jevmaxxing">project</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/jcpsimmons/jev-macos-loop"><img src="https://raw.githubusercontent.com/jcpsimmons/jev-macos-loop/master/docs/media/jev-finder-batch-demo.gif" alt="Jev macOS Loop" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/jcpsimmons/jev-macos-loop">Jev macOS Loop</a></b><br><sub>jcpsimmons · GitHub · ⭐ 19 · 2026-09-18</sub><br>面向 Apple 芯片上原生 macOS 应用的电脑操控 agent，在本地用 OmniParser CoreML、Vision OCR 和无障碍数据找到控件，再让 Jev 选出下一步动作；7.39 秒整理完 9 个文件。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/varun_mathur/status/2102232629902819580"><img src="https://pbs.twimg.com/amplify_video_thumb/2102229039784022016/img/rG7JcDFdZW-Pa16S.jpg" alt="Hyperspace agentic OS 在 Amazon 下单" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/varun_mathur/status/2102232629902819580">Hyperspace agentic OS 在 Amazon 下单</a></b><br><sub>varun_mathur · X · ♥ 5 · 2026-09-22</sub><br>Hyperspace 的 agentic OS 在 MacBook 上结合 Jev 和前沿模型，约 30 秒内自主在 Amazon 上买了一本书。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/chy4pro/jev-for-chrome"><img src="https://raw.githubusercontent.com/chy4pro/jev-for-chrome/main/docs/demo.gif" alt="Jev for Chrome" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/chy4pro/jev-for-chrome">Jev for Chrome</a></b><br><sub>chy4pro · GitHub · ⭐ 16 · 2026-09-18</sub><br>社区制作的 jev-ultrafast Manifest V3 移植版，驱动你正在看的标签页，Jev 在一次请求中选出操作和元素，小型文本模型写入输入值，可经由 OpenRouter、TypeSafe 或 Cloudflare 调用。</td>
</tr>
<tr>
<td width="260" valign="top"></td>
<td valign="top"><b><a href="https://www.npmjs.com/package/@mlola/decision-jev">@mlola/decision-jev</a></b><br><sub>MLola · 软件包 · ⬇ 1.4k · 2026-09-17</sub><br>MLola Browser Runtime 的 Jev 快速路径决策提供方，每个决策周期只发一次请求，并在任何浏览器操作执行前校验响应。<br><sub><b>Jev 用法:</b> 每个决策周期一次请求，在动态动作空间上同时带操作头和推测性目标头。</sub><br><sub>相关: <a href="https://mlola.com/browser-runtime">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/romaluev/jev-ego"><img src="https://opengraph.githubassets.com/1/romaluev/jev-ego" alt="jev-ego" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/romaluev/jev-ego">jev-ego</a></b><br><sub>romaluev · GitHub · ⭐ 13 · 2026-09-17</sub><br>面向 ego lite 浏览器的 TypeScript 浏览器 agent，给可操作元素编号，让编程 agent 或 Jev 每一步只用一次请求选出 CLICK、TYPE_TEXT 或 SELECT。<br><sub><b>Jev 用法:</b> 每一步在编号元素表和操作上做一个 Choice，沿用 jev-ultrafast 的动作空间。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/yegor/status/2101368226911232406"><img src="https://pbs.twimg.com/amplify_video_thumb/2101367134278344704/img/WJyEFS976FdNKAnB.jpg" alt="可以对话的浏览器" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/yegor/status/2101368226911232406">可以对话的浏览器</a></b><br><sub>yegor · X · ♥ 4 · 2026-09-19</sub><br>一个能直接对话的独立浏览器，快速决策交给 Jev，其余一切由本地 LLM 处理；演示中以超人速度订酒店、玩 Wikirace。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/grabbou/jevil"><img src="https://opengraph.githubassets.com/1/grabbou/jevil" alt="jevil" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/grabbou/jevil">jevil</a></b><br><sub>grabbou · GitHub · ⭐ 12 · 2026-09-17</sub><br>移动端 QA agent 的概念验证：通过 agent-device 读取 iOS 或 Android 应用，请 Jev 选择下一步动作并执行，最后保存报告、决策轨迹和录屏。<br><sub><b>Jev 用法:</b> 每一步在可用动作加 qa_pass、qa_fail 和 incomplete 上做一个 Choice，后三者会结束运行并设定状态。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/jiawei686/jev-ultrafast-mcp"><img src="https://raw.githubusercontent.com/jiawei686/jev-ultrafast-mcp/main/assets/social-preview.png" alt="jev-ultrafast-mcp" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/jiawei686/jev-ultrafast-mcp">jev-ultrafast-mcp</a></b><br><sub>jiawei686 · GitHub · ⭐ 9 · 2026-09-19</sub><br>MCP 服务器，在一次工具调用中接收整个浏览器任务（URL、目标和检查项），由决策模型通过 CDP 驱动 Chrome，只选择页面上实际存在的元素，并能把流程作为无需模型的宏回放。<br><sub>相关: <a href="https://pypi.org/project/jev-ultrafast-mcp/">pypi</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/fellowship-dev/navvi"><img src="https://raw.githubusercontent.com/fellowship-dev/navvi/main/docs/navvi-logo.png" alt="Navvi" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/fellowship-dev/navvi">Navvi</a></b><br><sub>fellowship-dev · GitHub · ⭐ 9 · 2026-03-20</sub><br>MCP 服务器，把一次浏览器任务变成可复用的爬虫：Jev 在代码找出的控件和字段之间做选择，Navvi 保存选择器、指纹和导航轨迹，用于回放和修复。<br><sub><b>Jev 用法:</b> 在代码找出的候选项上做类型化决策；由一个能生成文本的后备模型负责理解提示词和生成要输入的值。README 对比了 Haiku 和 Jev 的编译运行。</sub><br><sub>相关: <a href="https://pypi.org/project/navvi/">pypi</a> · <a href="https://github.com/fellowship-dev/navvi/blob/main/src/chooser/jev.ts">code</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/ranjan2829/AskJev"><img src="https://opengraph.githubassets.com/1/ranjan2829/AskJev" alt="AskJev" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/ranjan2829/AskJev">AskJev</a></b><br><sub>ranjan2829 · GitHub · ⭐ 8 · 2026-09-17</sub><br>Claude Desktop 扩展加 Chrome 插件，根据自然英语请求驱动 Brave 或 Chrome，由 Jev 决定页面上的每个操作，并有防护机制冻结付款、删除等不可逆点击。<br><sub><b>Jev 用法:</b> Jev 用 Noul、Choice 和 Score 问题挑选页面操作，并评估风险和不可逆性；Claude 不负责规划。</sub><br><sub>相关: <a href="https://x.com/manofsteel3129/status/2101090226856931776">demo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Nancy-Chauhan/hearth-jev-rental-search"><img src="https://raw.githubusercontent.com/Nancy-Chauhan/hearth-jev-rental-search/main/jev_ultrafast/static/backdrop.jpg" alt="Hearth" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Nancy-Chauhan/hearth-jev-rental-search">Hearth</a></b><br><sub>Nancy-Chauhan · GitHub · ⭐ 8 · 2026-09-20</sub><br>本地 agent，根据一条自然语言请求驱动真实的 Chrome 浏览 Craigslist、Facebook Marketplace、Redfin 和 Zillow，由 Jev 选择每个动作，最后返回一份只读的租房候选清单。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/jekhov/jekhov"><img src="https://opengraph.githubassets.com/1/jekhov/jekhov" alt="Jekhov" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/jekhov/jekhov">Jekhov</a></b><br><sub>jekhov · GitHub · ⭐ 8 · 2026-09-18</sub><br>库和 CLI，让 Jev 从筛选后的无障碍树候选中挑选目标元素或弃权，从而让已知的 Playwright 工作流更健壮，工作流本身保持确定性。<br><sub><b>Jev 用法:</b> 在与动作兼容的候选上做一个 Choice，另外单独估计匹配无歧义的概率；动作只在校准过的关卡之后执行，公开网站上只以影子模式运行。</sub></td>
</tr>
<tr>
<td width="260" valign="top"></td>
<td valign="top"><b><a href="https://x.com/ChrisAdcockMD/status/2101126098603888862">Grok Bot Ultrafast integration</a></b><br><sub>ChrisAdcockMD · X · ♥ 2 · 2026-09-19</sub><br>Grok Bot 对 Ultrafast 方法的集成，让机器人用 Jev 驱动本机上真实的 Chrome，并标出现有机器人决策中哪些可以交给 Jev。<br><sub>相关: <a href="https://x.ai/bot/sM_Xi4OF09cGU8KGyLvlC">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/himomohi/aside-jev"><img src="https://raw.githubusercontent.com/himomohi/aside-jev/main/docs/assets/aside-jev-hero.png" alt="Aside Jev" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/himomohi/aside-jev">Aside Jev</a></b><br><sub>himomohi · GitHub · ⭐ 6 · 2026-09-17</sub><br>MCP 服务器、skill 和浏览器扩展，让 Aside 浏览器 agent 把动作选择交给 Jev，由它从应用定义的候选表中选出下一步动作。<br><sub><b>Jev 用法:</b> Jev 从候选表返回一个动作 ID；由 Aside 执行并验证。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/tontoko/jev-browser"><img src="https://opengraph.githubassets.com/1/tontoko/jev-browser" alt="Jev Browser" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/tontoko/jev-browser">Jev Browser</a></b><br><sub>tontoko · GitHub · ⭐ 6 · 2026-09-17</sub><br>Playwright 自动化核心，带类型化 SDK、常驻 CLI 和 MCP 服务器，由 Jev 在真实页面元素上选择动作、匹配表单字段和提取内容，而不是生成选择器。<br><sub><b>Jev 用法:</b> 在提供的元素候选上并行做多个 Choice；由 Playwright 执行，确定性断言负责验证。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/forvela/jev-agent-browser"><img src="https://raw.githubusercontent.com/forvela/jev-agent-browser/main/media/huggingface-filter-demo.gif" alt="jev-agent-browser" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/forvela/jev-agent-browser">jev-agent-browser</a></b><br><sub>forvela · GitHub · ⭐ 6 · 2026-09-19</sub><br>为上层 agent 提供的有边界浏览器执行：Jev 选出每个类型化动作交给 agent-browser 执行，遇到歧义、重复或卡住的状态时，以结构化交接的形式返回给上层 agent。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/parkers0405/neoism/blob/main/neoism-agent/crates/neoism-agent-server/src/computer_use/typesafe.rs"><img src="https://raw.githubusercontent.com/parkers0405/neoism/241e6daaea1249d2eff6ca94b91dbacc2c426b0f/docs/images/terminal.png" alt="Neoism 的 TypeSafe 电脑操控模式" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/parkers0405/neoism/blob/main/neoism-agent/crates/neoism-agent-server/src/computer_use/typesafe.rs">Neoism 的 TypeSafe 电脑操控模式</a></b><br><sub>parkers0405 · GitHub · ⭐ 119 仓库 · 2026-04-27</sub><br>终端优先的 IDE，其 agent 可以用 Jev 驱动浏览器：从观察到的 DOM 候选项中选出下一步动作，再针对这个具体动作单独做一次风险检查。<br><sub><b>Jev 用法:</b> 一次请求同时完成 Choice 和 done 判断，门槛为 0.85 置信度和 0.75 选中概率；随后再发一个限定范围的 Noul 风险请求。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/dom-actions/doma/tree/main/src/services/chat/jev"><img src="https://opengraph.githubassets.com/1/dom-actions/doma" alt="DomA Jev assist" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/dom-actions/doma/tree/main/src/services/chat/jev">DomA Jev assist</a></b><br><sub>dom-actions · GitHub · ⭐ 104 仓库 · 2026-09-09</sub><br>开源浏览器自动化扩展，在其截图操作循环中增加可选的 Jev 辅助，从 set-of-mark 标注的元素中做选择。<br><sub>相关: <a href="https://www.domactions.com/docs/en/">docs</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/GoldenLoaf24h/browserclaw"><img src="https://opengraph.githubassets.com/1/GoldenLoaf24h/browserclaw" alt="BrowserClaw" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/GoldenLoaf24h/browserclaw">BrowserClaw</a></b><br><sub>GoldenLoaf24h · GitHub · ⭐ 5 · 2026-09-10</sub><br>Chrome MV3 扩展加原生消息 MCP 服务器，让 AI agent 驱动你日常已登录的 Chrome，其中包括一个 chrome_act_toward_goal 工具，由 Jev 微循环在剪枝后的 DOM 树上挑选动作。<br><sub>相关: <a href="https://www.reddit.com/r/AI_Agents/comments/1wkmp2z/why_calling_cloud_llms_for_every_browser_click_is/">discussion</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Nguy-n-Th-Huy/Browzy"><img src="https://opengraph.githubassets.com/1/Nguy-n-Th-Huy/Browzy" alt="Browzy" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Nguy-n-Th-Huy/Browzy">Browzy</a></b><br><sub>Nguy-n-Th-Huy · GitHub · ⭐ 5 · 2026-09-09</sub><br>Claude in Chrome 扩展的净室复刻，去掉了域名黑名单，带一个 beta 版 Jev 模式：由 LLM 准备计划，Jev 挑选每一个完整的浏览器动作。<br><sub><b>Jev 用法:</b> 每个周期问三个独立问题：执行哪个完整动作、目标是否可能已完成、进展是否卡住。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/pumpkinredbean/bside"><img src="https://opengraph.githubassets.com/1/pumpkinredbean/bside" alt="bside" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/pumpkinredbean/bside">bside</a></b><br><sub>pumpkinredbean · GitHub · ⭐ 5 · 2026-09-17</sub><br>驱动 Aside 浏览器，每个 tick 由 Jev 选择动作、元素并检查目标是否达成；在一个五步的 Wikipedia 任务上耗时 52.8 秒、约 $0.0018，而前沿 LLM 需要 72.9 秒和 $0.039。<br><sub><b>Jev 用法:</b> 在枚举的动作 schema 和页面元素引用上做 Choice，因此不会点击不存在的元素；也提供 MCP 服务器。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/buluoray/JevOnly"><img src="https://opengraph.githubassets.com/1/buluoray/JevOnly" alt="JevOnly" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/buluoray/JevOnly">JevOnly</a></b><br><sub>buluoray · GitHub · ⭐ 5 · 2026-09-19</sub><br>完全不用 LLM 的浏览器 agent：代码根据页面和目标枚举所有选项，Jev 只负责挑选下一步动作，带验证、撤销和不可逆动作关卡。<br><sub><b>Jev 用法:</b> 每一步一次请求，在代码枚举的选项上回答“完成了吗？”“偏离路径了吗？”“下一步做什么？”；字段值只能是事实、目标中的片段或从页面复制的值。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/filedcom/playjev"><img src="https://raw.githubusercontent.com/filedcom/playjev/main/docs/public/playjev-golden-logo.png" alt="PlayJev" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/filedcom/playjev">PlayJev</a></b><br><sub>filedcom · GitHub · ⭐ 5 · 2026-09-20</sub><br>TypeScript 库，给 Playwright 加上用纯英文指令驱动的浏览器自动化，类似 Stagehand，但点击、导航、填表和选项都由 Jev 来选，而不是交给生成式 LLM。<br><sub>相关: <a href="https://www.reddit.com/r/LLM/comments/1wli7sk/i_built_browser_automation_with_jev_and_its/">discussion</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/vinilana/jev-browser"><img src="https://opengraph.githubassets.com/1/vinilana/jev-browser" alt="Jev Browser (hybrid harness)" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/vinilana/jev-browser">Jev Browser (hybrid harness)</a></b><br><sub>vinilana · GitHub · ⭐ 4 · 2026-09-17</sub><br>TypeScript 浏览器 harness：OpenRouter 上的 LLM 把目标拆成可验证的子目标，Jev 选择每个动作和 DOM 字段，需要时由 OpenRouter 撰写字段文字，Playwright 负责执行。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Tongyun1/Jev-in-the-Loop"><img src="https://raw.githubusercontent.com/Tongyun1/Jev-in-the-Loop/main/docs/media/demo-hotel.gif" alt="Jev-in-the-Loop" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Tongyun1/Jev-in-the-Loop">Jev-in-the-Loop</a></b><br><sub>Tongyun1 · GitHub · ⭐ 4 · 2026-09-21</sub><br>在本地 Chrome 中快速完成浏览器工作的 Codex 插件：Codex 规划任务并准备文字，Jev 挑选每一个下一步动作及其目标。<br><sub><b>Jev 用法:</b> 每一步一次 TypeSafe 请求，返回动作、目标和准备好的输入；不需要单独的文本模型 key。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/NobleSpartan6/otto"><img src="https://opengraph.githubassets.com/1/NobleSpartan6/otto" alt="Otto" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/NobleSpartan6/otto">Otto</a></b><br><sub>NobleSpartan6 · GitHub · ⭐ 4 · 2026-09-17</sub><br>早期 alpha 阶段的桌面电脑操控（computer use）agent，支持 macOS 和 Windows，通过原生无障碍控件和本地 OCR 工作，把 Jev 的决策与可选的 GPT-6 Astra 规划器结合起来。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/paulsmith/computer-use-jev"><img src="https://opengraph.githubassets.com/1/paulsmith/computer-use-jev" alt="computer-use-jev" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/paulsmith/computer-use-jev">computer-use-jev</a></b><br><sub>paulsmith · GitHub · ⭐ 3 · 2026-09-16</sub><br>Go 库，通过 Accessibility API 驱动原生 macOS 应用，以 Jev 为决策循环，每一步选择下一个动作、目标元素、输入文本以及是否完成。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/ZephyrDeng/ego-jev"><img src="https://raw.githubusercontent.com/ZephyrDeng/ego-jev/main/docs/banner.svg" alt="ego-jev" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/ZephyrDeng/ego-jev">ego-jev</a></b><br><sub>ZephyrDeng · GitHub · ⭐ 3 · 2026-09-21</sub><br>agent skill，为 ego lite 浏览器加上 Jev 内循环：每个 DOM 步骤给可交互元素编号，一次约 0.4 秒的 Jev 调用选出操作和目标；登录和付款交给规划器。<br><sub>相关: <a href="https://skills.sh/ZephyrDeng/ego-jev">skill</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/kyrylosyzonenko/jev-browse"><img src="https://raw.githubusercontent.com/kyrylosyzonenko/jev-browse/main/assets/demo.gif" alt="jev-browse" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/kyrylosyzonenko/jev-browse">jev-browse</a></b><br><sub>kyrylosyzonenko · GitHub · ⭐ 3 · 2026-09-16</sub><br>浏览器 agent，所有决策由 Jev 做出，所有动作由 Vercel 的 agent-browser 执行；在 10 个任务上 30/30 次运行全部通过，每个任务 4.4 秒、$0.0009，而 Claude Code 为 9.4 秒、$0.0679。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/0x7067/jev-browse"><img src="https://raw.githubusercontent.com/0x7067/jev-browse/main/docs/banner.svg" alt="jev-browse (0x7067)" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/0x7067/jev-browse">jev-browse (0x7067)</a></b><br><sub>0x7067 · GitHub · ⭐ 3 · 2026-09-18</sub><br>带索引动作空间的 TypeScript 浏览器 agent，Jev 选出操作和元素，小型 LLM 只在 TYPE_TEXT 时写文字；可安装到 Pi、Claude Code、Codex 和 MCP harness 上。<br><sub><b>Jev 用法:</b> 演示：在 Google Flights 上查苏黎世到伦敦的航班，用时 17.6 秒。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Friedjof/jev-mobile"><img src="https://opengraph.githubassets.com/1/Friedjof/jev-mobile" alt="jev-mobile" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Friedjof/jev-mobile">jev-mobile</a></b><br><sub>Friedjof · GitHub · ⭐ 3 · 2026-09-17</sub><br>持久运行的 Android 子 agent，通过 Mobile MCP 在 USB 连接的手机上运行“观察、决策、执行、验证”循环，由 Jev 在技术上合法的动作中选择，从不生成坐标或代码。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/antiyro/jevdroid"><img src="https://opengraph.githubassets.com/1/antiyro/jevdroid" alt="JevDroid" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/antiyro/jevdroid">JevDroid</a></b><br><sub>antiyro · GitHub · ⭐ 3 · 2026-09-18</sub><br>Python 框架：Jev 读取 Android 无障碍树，朝着目标挑选每一次点按、滑动或应用启动，通过 ADB 或 UIAutomator2 执行，带权限和预算控制；每次决策中位耗时 314 毫秒。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/iuhoay/skills/tree/main/chrome-devtools"><img src="https://opengraph.githubassets.com/1/iuhoay/skills" alt="chrome-devtools skill" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/iuhoay/skills/tree/main/chrome-devtools">chrome-devtools skill</a></b><br><sub>iuhoay · GitHub · ⭐ 53 仓库 · 2026-02-11</sub><br>编程 agent skill，封装 chrome-devtools，在拍一张简短的页面快照后，批量向 TypeSafe Jev 提出关于页面的问题，而不是把整个 DOM 灌进上下文。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/agentsea/nautilo/tree/main/packages/agent/src/tools/browser"><img src="https://nautilo.ai/docs/operator/first-nautilo/writer-review.png" alt="Nautilo 的 Jev 浏览器决策" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/agentsea/nautilo/tree/main/packages/agent/src/tools/browser">Nautilo 的 Jev 浏览器决策</a></b><br><sub>agentsea · GitHub · ⭐ 51 仓库 · 2026-09-16</sub><br>Nautilo（可自托管的多人 agent 工作区）里的日常浏览器任务委派：Genie 把一段浏览器操作交给 Jev Choice 模型，由它在每次观察页面后选出下一步动作，卡住时再交回。<br><sub><b>Jev 用法:</b> 一个登记在模型目录中的 Choice 模型（通过 OpenRouter 调用 Jev）每一步在最新的页面目标和动作模板之间做选择；可选配进度/成功判定条件。</sub><br><sub>相关: <a href="https://nautilo.ai">app</a> · <a href="https://github.com/agentsea/nautilo">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/vstorm-co/agenticos/tree/main/backend/app/agents/capabilities/browser_choice"><img src="https://repository-images.githubusercontent.com/1318197751/15610d40-b4eb-458a-8808-cfc811544b1c" alt="AgenticOS browser_choice" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/vstorm-co/agenticos/tree/main/backend/app/agents/capabilities/browser_choice">AgenticOS browser_choice</a></b><br><sub>vstorm-co · GitHub · ⭐ 45 仓库 · 2026-07-31</sub><br>自托管 agent 平台 AgenticOS 中的浏览器能力，把页面读成一张带编号的可操作元素表，再问决策模型用哪个操作和元素，因此页面文字无法注入新动作。<br><sub><b>Jev 用法:</b> 每一步是在服务器构建的 DOM 选项上做类型受限的选择，可以回答 BLOCKED，并设有 min_confidence 下限；只有要填写的字段值才会交给 LLM。</sub><br><sub>相关: <a href="https://vstorm-co.github.io/agenticos/">app</a> · <a href="https://github.com/vstorm-co/agenticos">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/EastStarAI/sanad-agent/tree/main/.agents/skills/jev-dual-brain-automation"><img src="https://raw.githubusercontent.com/EastStarAI/sanad-agent/main/client/assets/brand/sanad-wordmark-horizontal.svg" alt="Jev Dual-Brain automation skill" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/EastStarAI/sanad-agent/tree/main/.agents/skills/jev-dual-brain-automation">Jev Dual-Brain automation skill</a></b><br><sub>EastStarAI · GitHub · ⭐ 45 仓库 · 2026-08-01</sub><br>Sanad Agent 仓库中用于浏览器和 Flutter 桌面 UI 自动化的 agent skill：Jev 在亚秒级循环中挑选 DOM 候选并验证目标，一旦检测循环的熔断器触发，就由前沿模型接手。<br><sub><b>Jev 用法:</b> 在 DOM/UI 树候选上做 Choice（约 700 毫秒），外加一个检查目标的 Noul；强模型负责处理障碍并重新委派。</sub><br><sub>相关: <a href="https://github.com/EastStarAI/sanad-agent">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/ZHUBoer/ego-jev"><img src="https://opengraph.githubassets.com/1/ZHUBoer/ego-jev" alt="ego-jev" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/ZHUBoer/ego-jev">ego-jev</a></b><br><sub>ZHUBoer · GitHub · ⭐ 2 · 2026-09-19</sub><br>agent skill，通过 Ego Lite 在真实 Chromium 中完成浏览器任务，调用 Jev 做语义目标选择、过滤、排序、分类和证据检查，需要精确的工作留给代码。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/jiangkoumo/ego-jev"><img src="https://opengraph.githubassets.com/1/jiangkoumo/ego-jev" alt="ego-jev (jiangkoumo)" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/jiangkoumo/ego-jev">ego-jev (jiangkoumo)</a></b><br><sub>jiangkoumo · GitHub · ⭐ 2 · 2026-09-19</sub><br>agent skill，用 Jev 驱动 ego lite 浏览器：每一步输入一张带索引的屏幕元素表，输出一个操作加目标，作者测试中比逐步调用 LLM 的循环快约 2 倍。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/ZihuaEvan/GUI_JEV"><img src="https://opengraph.githubassets.com/1/ZihuaEvan/GUI_JEV" alt="GUI JEV Harness" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/ZihuaEvan/GUI_JEV">GUI JEV Harness</a></b><br><sub>ZihuaEvan · GitHub · ⭐ 2 · 2026-09-21</sub><br>截图进、坐标出的 GUI 定位 harness：视觉模型描述网格图块，Jev 在每一层递归中选一个图块，由概率和差距阈值决定继续下钻还是拒绝。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/dougsong/jev-android"><img src="https://opengraph.githubassets.com/1/dougsong/jev-android" alt="jev-android" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/dougsong/jev-android">jev-android</a></b><br><sub>dougsong · GitHub · ⭐ 2 · 2026-09-20</sub><br>Android UI 自动化的 Kotlin SDK，由 Jev 或 DeepSeek 从屏幕上的实际控件中挑选动作，由无障碍服务执行，附示例应用。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/aidil2105/jev-browser-pilot"><img src="https://opengraph.githubassets.com/1/aidil2105/jev-browser-pilot" alt="jev-browser-pilot" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/aidil2105/jev-browser-pilot">jev-browser-pilot</a></b><br><sub>aidil2105 · GitHub · ⭐ 2 · 2026-09-18</sub><br>面向浏览器和桌面自动化的有边界决策层：代码负责观察、列出候选动作、执行和验证，模型只负责挑选下一个候选。<br><sub><b>Jev 用法:</b> 每一步在代码构建的候选 ID 上做一个 Choice，带置信度路由和审计记录。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/brnyxx/jev-ra"><img src="https://raw.githubusercontent.com/brnyxx/jev-ra/main/assets/hero.png" alt="jev-ra" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/brnyxx/jev-ra">jev-ra</a></b><br><sub>brnyxx · GitHub · ⭐ 2 · 2026-09-18</sub><br>面向 Claude Code、Codex 及其他 MCP 客户端的浏览器操控层，每一步由 Jev 选出操作和目标元素，在 Wikipedia 和 Google Flights 任务上实测比 browser-use 快 7-8 倍。<br><sub><b>Jev 用法:</b> 每步一次约 300 毫秒的往返；调用方 agent 负责规划、提供文字，并在升级时接手。</sub><br><sub>相关: <a href="https://brnyxx.github.io/jev-ra/">site</a> · <a href="https://brnyxx.github.io/jev-ra">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/sightmap/jev-turbo"><img src="https://raw.githubusercontent.com/sightmap/jev-turbo/main/docs/demo.gif" alt="jev-turbo" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/sightmap/jev-turbo">jev-turbo</a></b><br><sub>sightmap · GitHub · ⭐ 2 · 2026-09-17</sub><br>Go 浏览器 agent，每一步由 Jev 从一小组命名的页面动作中挑选，并判断目标是否达成；分别在有和没有站点地图的情况下运行，以衡量地图带来的变化。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/coco-research/jev-use"><img src="https://raw.githubusercontent.com/coco-research/jev-use/main/docs/readme/hero-dark.png" alt="jev-use" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/coco-research/jev-use">jev-use</a></b><br><sub>coco-research · GitHub · ⭐ 2 · 2026-09-20</sub><br>用 Rust 和 Tauri 编写、处于 pre-alpha 阶段的 macOS 语音控制层，通过无障碍树读取应用，按语音目标执行操作，完全在本地运行。<br><sub><b>Jev 用法:</b> Jev 是回退决策层而不是路由器，位于本地的“命令还是听写”分流之后。</sub></td>
</tr>
<tr>
<td width="260" valign="top"></td>
<td valign="top"><b><a href="https://x.com/EvanLing888/status/2101175502396641613">Jev 与 Chrome DevTools MCP 发帖对比</a></b><br><sub>EvanLing888 · X · ▶ 92 · 2026-09-19</sub><br>中文对比：用 Jev 驱动的浏览器 agent 发布一条社交帖子（约 33 秒，2 个动作，已验证），对比 Chrome DevTools MCP（约 196 秒，出现输入错误和重复内容）。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/hua-bang/pulse-agent/tree/master/apps/canvas-workspace/src/plugins/main/webview-page-control/page-run"><img src="https://raw.githubusercontent.com/hua-bang/pulse-agent/master/architecture/en/pulse-canvas-engine.svg" alt="Pulse Agent page-run" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/hua-bang/pulse-agent/tree/master/apps/canvas-workspace/src/plugins/main/webview-page-control/page-run">Pulse Agent page-run</a></b><br><sub>hua-bang · GitHub · ⭐ 29 仓库 · 2026-01-26</sub><br>Pulse Agent 画布工作区里的 webview 页面控制循环：读取页面快照，向 Jev 询问下一步动作，以及目标是否已完成、运行是否卡住。<br><sub><b>Jev 用法:</b> 每一步一个覆盖候选页面动作的 Choice，加两个 Noul（goal_done、stuck），请求控制在 28,000 字节的预算内。</sub><br><sub>相关: <a href="https://github.com/hua-bang/pulse-agent">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/andresguc1/hal-test/tree/main/research/jev-decision-provider"><img src="https://repository-images.githubusercontent.com/1122580217/88b6c18f-cde9-4f89-896f-7a5ae4de8539" alt="HAL-TEST Jev selector healing" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/andresguc1/hal-test/tree/main/research/jev-decision-provider">HAL-TEST Jev selector healing</a></b><br><sub>andresguc1 · GitHub · ⭐ 21 仓库 · 2025-12-25</sub><br>可视化 Playwright 自动化框架 HAL-TEST 的概念验证：测试选择器失效时用 Jev 挑选替代元素，再根据置信度自动修复、给出建议或交给人工复核。<br><sub>相关: <a href="https://github.com/andresguc1/hal-test">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/zurfyx/jev-browser-skill"><img src="https://raw.githubusercontent.com/zurfyx/jev-browser-skill/main/docs/demo.gif" alt="Jev Browser Skill" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/zurfyx/jev-browser-skill">Jev Browser Skill</a></b><br><sub>zurfyx · GitHub · ⭐ 1 · 2026-09-19</sub><br>面向 Claude Code 和 Codex 的参考浏览器 skill，只有三个简短的无依赖文件：给出网站和目标，Jev 就一路点击、输入、选择到达目标，另有一个逐步讲解的配套网站。<br><sub><b>Jev 用法:</b> 沿用 jev-ultrafast 的做法：每一步一次请求，选出操作和目标元素。</sub><br><sub>相关: <a href="https://jev-browser.vercel.app">app</a> · <a href="https://jev-browser.vercel.app">app 2</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/xunaoo/status/2101940075072459255"><img src="https://pbs.twimg.com/media/HSuXK_yboAAatTI.jpg?name=orig" alt="在浏览器 agent 中接入 Jev" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/xunaoo/status/2101940075072459255">在浏览器 agent 中接入 Jev</a></b><br><sub>xunaoo · X · ♥ 1 · 2026-09-21</sub><br>把 Jev 接入浏览器 agent 的实践记录：单个决策步骤从 2 秒降到 0.2 秒，十次模型调用减为两次，但准确率下降了 6 个点。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/xinwang-nwpu/jev-mobile"><img src="https://raw.githubusercontent.com/xinwang-nwpu/jev-mobile/main/docx/demo.gif" alt="jev-mobile" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/xinwang-nwpu/jev-mobile">jev-mobile</a></b><br><sub>xinwang-nwpu · GitHub · ⭐ 1 · 2026-09-21</sub><br>Android 自动化 agent，每一步在无障碍树上发一次 Jev 请求，同时选出动作和目标元素，通过 ADB 执行，并并行检查目标是否完成。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/krw82/jev-playwright-mcp"><img src="https://opengraph.githubassets.com/1/krw82/jev-playwright-mcp" alt="jev-playwright-mcp" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/krw82/jev-playwright-mcp">jev-playwright-mcp</a></b><br><sub>krw82 · GitHub · ⭐ 1 · 2026-09-17</sub><br>Playwright MCP 的即插即用代理，保留相同的工具，并增加 Jev 页面状态分诊（登录墙、验证码、付费墙）、提示词注入防护、基于目标的快照裁剪和高风险动作拦截。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/ElshinQ/jevaluate"><img src="https://opengraph.githubassets.com/1/ElshinQ/jevaluate" alt="Jevaluate" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/ElshinQ/jevaluate">Jevaluate</a></b><br><sub>ElshinQ · GitHub · ⭐ 1 · 2026-09-19</sub><br>像真人一样测试网页应用：Jev 从一小组候选中挑选下一次点击，置信度低于 80% 时停下交给人，DeepSeek 视觉模型检查每个页面截图；附带评测脚本、UI 文本评判器和一个 agent skill。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/dtduc-git/jevnav"><img src="https://raw.githubusercontent.com/dtduc-git/jevnav/main/docs/architecture.png" alt="jevnav" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/dtduc-git/jevnav">jevnav</a></b><br><sub>dtduc-git · GitHub · ⭐ 1 · 2026-09-21</sub><br>面向编程 agent 的浏览器自动化，以事实形式返回页面结构和计算样式，由 Jev 以校准的概率挑选每个元素，拦截高风险动作，并能在 CI 中离线回放整个运行过程。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/Divine_machine/status/2102206020504224249"><img src="https://pbs.twimg.com/media/HSw6tlNXMAE6g7d.jpg?name=orig" alt="Jev Desktop" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/Divine_machine/status/2102206020504224249">Jev Desktop</a></b><br><sub>Divine_machine · X · ▶ 48 · 2026-09-22</sub><br>开源的 Windows 电脑操控循环：LLM 设定目标，Jev Desktop 通过 UI Automation 读取应用状态，Jev 选择每个动作，由 driver 执行，点击之间不需要任何 LLM 轮次。<br><sub>相关: <a href="https://github.com/jacks3tr/jev-desktop">repo</a> · <a href="https://github.com/jacks3tr/jev-desktop">project</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/kernel/browser-loop/tree/main/packages/browser-loop/examples/jev-system-one"><img src="https://opengraph.githubassets.com/1/kernel/browser-loop" alt="Browser Loop Jev agent" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/kernel/browser-loop/tree/main/packages/browser-loop/examples/jev-system-one">Browser Loop Jev agent</a></b><br><sub>kernel · GitHub · ⭐ 10 仓库 · 2026-04-18</sub><br>面向 Kernel 云浏览器的浏览器 agent 循环示例，每一步由 Jev 从页面特定的点击、输入、选择、滚动和等待候选中选出操作和目标。<br><sub><b>Jev 用法:</b> 在一次请求中做推测性的操作和目标 Choice，DONE 和 BLOCKED 作为显式选项，只有输入值时才用小型文本模型。</sub><br><sub>相关: <a href="https://www.kernel.sh">app</a> · <a href="https://github.com/kernel/browser-loop">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/silbercue/public-browser/blob/master/examples/jev-loop.mjs"><img src="https://raw.githubusercontent.com/Silbercue/public-browser/master/.github/assets/benchmark-2026-09-light.svg" alt="Public Browser 的 Jev 循环" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/silbercue/public-browser/blob/master/examples/jev-loop.mjs">Public Browser 的 Jev 循环</a></b><br><sub>Silbercue · GitHub · ⭐ 10 仓库 · 2026-04-07</sub><br>基于 Public Browser Chrome 库的示例循环：每一步调用一次 Jev，从页面的无障碍引用中选出下一步动作，只有输入类动作才让 gpt-4.1-nano 写文本，在六张基准测试卡片上运行。<br><sub>相关: <a href="https://github.com/Silbercue/public-browser">repo</a> · <a href="https://www.npmjs.com/package/public-browser">npm</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/JoshuaWangTW/RustBrowser/blob/master/src/jev.rs"><img src="https://opengraph.githubassets.com/1/JoshuaWangTW/RustBrowser" alt="RustBrowser 的 Jev 规划器" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/JoshuaWangTW/RustBrowser/blob/master/src/jev.rs">RustBrowser 的 Jev 规划器</a></b><br><sub>JoshuaWangTW · GitHub · ⭐ 10 仓库 · 2026-06-03</sub><br>面向 LLM、节省 token 的网页抓取工具兼 MCP 服务器，其规划器根据页面索引好的动作空间，问 Jev 下一步用哪个操作、作用于哪个目标。<br><sub><b>Jev 用法:</b> 每次请求问两个 Choice 问题（操作和目标），输入最多 6,000 个字符的页面文本，沿用 jev-ultrafast 的做法；答案是带置信度的建议。</sub><br><sub>相关: <a href="https://github.com/JoshuaWangTW/RustBrowser">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/SomeshSampat2/android-control/tree/main/src/android_mcp/jev"><img src="https://opengraph.githubassets.com/1/SomeshSampat2/android-control" alt="Android Control Jev fast mode" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/SomeshSampat2/android-control/tree/main/src/android_mcp/jev">Android Control Jev fast mode</a></b><br><sub>SomeshSampat2 · GitHub · ⭐ 8 仓库 · 2026-04-11</sub><br>让 AI 助手控制安卓设备的 MCP 服务器，带 Jev 快速模式：逐步推进目标、按描述点击元素，并在约 0.3 秒内回答关于屏幕的是/否问题。<br><sub><b>Jev 用法:</b> Jev 只在代码提供的屏幕候选项中挑选，因此无法凭空编造元素名或坐标。</sub><br><sub>相关: <a href="https://github.com/SomeshSampat2/android-control">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/glim-sh/cuttle/tree/main/packages/cuttle/internal/jev"><img src="https://opengraph.githubassets.com/1/glim-sh/cuttle" alt="cuttle jev-browse" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/glim-sh/cuttle/tree/main/packages/cuttle/internal/jev">cuttle jev-browse</a></b><br><sub>glim-sh · GitHub · ⭐ 7 仓库 · 2026-07-09</sub><br>cuttle 隐身 agent 浏览器的实验性 <code>cuttle jev-browse</code> 模式，一步一步朝任务推进，由 Jev 而不是 LLM 选择下一个要操作的元素。<br><sub><b>Jev 用法:</b> 每个页面快照在可见元素上做一次决策，用内置的 playwright-cli 执行；完成、受阻或步数用尽时停止。</sub><br><sub>相关: <a href="https://github.com/glim-sh/cuttle">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/dttxorg/deepseekeyes/tree/main/src/jev"><img src="https://raw.githubusercontent.com/dttxorg/deepseekeyes/main/assets/deepseekeyes-banner.png" alt="DeepSeekEyes Jev control" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/dttxorg/deepseekeyes/tree/main/src/jev">DeepSeekEyes Jev control</a></b><br><sub>dttxorg · GitHub · ⭐ 7 仓库 · 2026-08-14</sub><br>DeepSeek Harness 的视觉与电脑操控运行时 DeepSeekEyes 中可选的 Jev 控制层：Jev 在浏览器或原生应用中选出下一个操作和语义目标，由 DeepSeekEyes 执行并验证。<br><sub><b>Jev 用法:</b> 每一步都针对最新的 stateId 重新观察；输入的文本来自预先准备的槽位，低置信度或有风险的动作会停下来等待升级处理。</sub><br><sub>相关: <a href="https://github.com/dttxorg/deepseekeyes">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/kyleslight/shun/blob/main/src/main/jev-client.ts"><img src="https://raw.githubusercontent.com/kyleslight/shun/main/resources/screenshot-main.png" alt="Shun 的电脑操控加速" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/kyleslight/shun/blob/main/src/main/jev-client.ts">Shun 的电脑操控加速</a></b><br><sub>kyleslight · GitHub · ⭐ 6 仓库 · 2026-08-21</sub><br>本地优先、面向消费级 GPU 模型的桌面编程 harness Shun 中的电脑操控加速：在有凭证时，通过 TypeSafe、Vercel AI Gateway 或 OpenRouter 把动作选择路由给 Jev。<br><sub><b>Jev 用法:</b> Jev 选择下一步动作并判断是否完成，受最低动作置信度和完成置信度门槛约束，步数和超时都有上限。</sub><br><sub>相关: <a href="https://shunagent.com">app</a> · <a href="https://github.com/kyleslight/shun">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/eriestra/browser-use-olympics"><img src="https://opengraph.githubassets.com/1/eriestra/browser-use-olympics" alt="Browser Use Olympics" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/eriestra/browser-use-olympics">Browser Use Olympics</a></b><br><sub>eriestra · GitHub · 2026-09-17</sub><br>浏览器 agent 基准测试，一个提示词、五个项目、服务端计时，另附 almond-fastloop：约 200 行、无依赖的电脑操控循环，由 Jev 根据 Chrome DevTools 状态选出下一步动作。<br><sub>相关: <a href="https://sites.almond.build/browser-use-olympics/">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/phanngoc/browser-ai"><img src="https://opengraph.githubassets.com/1/phanngoc/browser-ai" alt="browser-ai" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/phanngoc/browser-ai">browser-ai</a></b><br><sub>phanngoc · GitHub · 2026-09-19</sub><br>只用 Go 标准库的浏览器 agent，通过 CDP 驱动 Chrome，可经管道启动，也可附着到你正在用的浏览器上；Jev 从带索引的动作空间中选出每个动作，小型 LLM 只负责填写字段值。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/aryaminus/cua"><img src="https://opengraph.githubassets.com/1/aryaminus/cua" alt="cua" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/aryaminus/cua">cua</a></b><br><sub>aryaminus · GitHub · 2026-09-18</sub><br>电脑操控系统：LLM 只探索一次 UI 流程，把它编译成类型化产物，之后无需模型即可确定性地重放；探索卡住时由经 OpenRouter Decisions 调用的 Jev 发出标记。<br><sub>相关: <a href="https://cua-aryaminus.netlify.app">site</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"></td>
<td valign="top"><b><a href="https://www.xiaohongshu.com/explore/6aaf844a000000001103379c">CUA + Jev 电脑操控</a></b><br><sub>北京月薪5k · X · 2026-09-20</sub><br>中文视频笔记，展示由开源 Cua agent 驱动、Jev 负责决策的电脑操控，作者称比 Codex 的电脑操控更便宜。</td>
</tr>
<tr>
<td width="260" valign="top"></td>
<td valign="top"><b><a href="https://cua.ai/docs/how-to-guides/driver/jev-use">Cua jev-use</a></b><br><sub>Cua · 文章</sub><br>有边界的电脑操控：由一个 Choice 从应用暴露的动作中选一个或弃权，再由 driver 执行。<br><sub>相关: <a href="https://github.com/trycua/cua">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/phd-peter/ego-jev"><img src="https://opengraph.githubassets.com/1/phd-peter/ego-jev" alt="ego-jev" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/phd-peter/ego-jev">ego-jev</a></b><br><sub>phd-peter · GitHub · 2026-09-18</sub><br>把 ego-lite 浏览器控制与 Jev 结合的有边界浏览器循环，Jev 只能从当前页面快照中挑选受支持的操作和一个不透明目标，绝不能给出选择器或坐标。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Tom-R-Main/Footwork"><img src="https://opengraph.githubassets.com/1/Tom-R-Main/Footwork" alt="Footwork" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Tom-R-Main/Footwork">Footwork</a></b><br><sub>Tom-R-Main · GitHub · 2026-09-21</sub><br>双过程浏览器 agent，把快速的 Jev System 1 决策放在 browser-use 深思熟虑的 LLM 循环前面，配有由代码掌控的仲裁器、基于证据的验证和 Rust 热路径。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/mhingston/jev-agent-browser"><img src="https://opengraph.githubassets.com/1/mhingston/jev-agent-browser" alt="Jev Agent Browser (mhingston)" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/mhingston/jev-agent-browser">Jev Agent Browser (mhingston)</a></b><br><sub>mhingston · GitHub · 2026-09-19</sub><br>TypeScript 边车程序，把精简的无障碍快照和目标交给 Jev 选出下一步浏览器动作，在代码中校验后交给 Vercel 的 agent-browser 执行，可经由 TypeSafe、AI Gateway 或 Cloudflare 调用。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/KesavanKing/jev-browser"><img src="https://opengraph.githubassets.com/1/KesavanKing/jev-browser" alt="Jev Browser" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/KesavanKing/jev-browser">Jev Browser</a></b><br><sub>KesavanKing · GitHub · 2026-09-17</sub><br>本地浏览器自动化界面，把一个 URL 和一个目标转成有边界的动作：Jev 在观察到的目标上选择点击、输入、选择、等待、完成或受阻，文本模型只用于填写字段值。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/abeatrix/cline-plugin-jev-browser"><img src="https://opengraph.githubassets.com/1/abeatrix/cline-plugin-jev-browser" alt="Jev Browser for Cline" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/abeatrix/cline-plugin-jev-browser">Jev Browser for Cline</a></b><br><sub>abeatrix · GitHub · 2026-09-18</sub><br>Cline 插件，为 agent 提供一个隔离的 Playwright Chromium 浏览器，通过 Vercel AI Gateway 把有边界的浏览器目标委托给 Jev，并自动截取操作前后的截图。<br><sub><b>Jev 用法:</b> 一次评估从带索引的 DOM 目标中同时选出操作和目标，与滚动、等待和停止一起比较；输入文本由文本模型提供。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/jal-co/jev-agent-browser"><img src="https://opengraph.githubassets.com/1/jal-co/jev-agent-browser" alt="jev-agent-browser" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/jal-co/jev-agent-browser">jev-agent-browser</a></b><br><sub>jal-co · GitHub · 2026-09-17</sub><br>适配器：Jev 选择下一步浏览器操作和目标，由 Agent Browser 执行，支持 HTML 和 ARIA 控件、文本输入、下拉选择、滚动和等待，并为 Pi 提供 JSON-lines 服务器。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/MahmoudAdelbghany/jev-browser"><img src="https://opengraph.githubassets.com/1/MahmoudAdelbghany/jev-browser" alt="jev-browser" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/MahmoudAdelbghany/jev-browser">jev-browser</a></b><br><sub>MahmoudAdelbghany · GitHub · 2026-09-17</sub><br>浏览器 MCP 服务器，由 Jev 在约 300 毫秒内选出下一步动作，驱动它的 agent 只在升级时介入；在 12 个任务的测试集上，准确率与 Playwright MCP 相同，速度快 1.5 倍、成本低 1.6 倍。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/imanshu03/jev-browser-use"><img src="https://opengraph.githubassets.com/1/imanshu03/jev-browser-use" alt="jev-browser-use" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/imanshu03/jev-browser-use">jev-browser-use</a></b><br><sub>imanshu03 · GitHub · 2026-09-21</sub><br>浏览器 agent，通过 CDP、Chromium 或 Vercel 的 agent-browser 执行自然语言任务，由 Jev 选择操作、目标和文本值，代码在执行前检查置信度和页面新鲜度。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/eronmmer/jev-cua"><img src="https://opengraph.githubassets.com/1/eronmmer/jev-cua" alt="jev-cua" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/eronmmer/jev-cua">jev-cua</a></b><br><sub>eronmmer · GitHub · 2026-09-20</sub><br>本地 Codex 和 Waku 插件，提供带防护的 Mac 电脑操控：启动应用、读取 Accessibility 状态、点击、输入和滚动，并为审核过的浏览器流程提供更快的编译路径。<br><sub><b>Jev 用法:</b> Jev 负责快速路径上的策略决策，高风险按键设有审批关卡，并保证最多执行一次。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/rashedInt32/jev-reach"><img src="https://opengraph.githubassets.com/1/rashedInt32/jev-reach" alt="jev-reach" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/rashedInt32/jev-reach">jev-reach</a></b><br><sub>rashedInt32 · GitHub · 2026-09-20</sub><br>为 chrome-devtools-mcp 增加一个 reach 工具：Jev 以每次约 300 毫秒的速度挑选每一次点击，把浏览器带到你想要的位置，agent 只需在那里调用一次 devtools，而不是每次点击都耗一轮。<br><sub>相关: <a href="https://www.reddit.com/r/ClaudeCode/comments/1wljx18/i_gave_chromedevtoolsmcp_one_more_tool_so_my/">demo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/msalvalaggio/jev-reflex"><img src="https://opengraph.githubassets.com/1/msalvalaggio/jev-reflex" alt="jev-reflex" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/msalvalaggio/jev-reflex">jev-reflex</a></b><br><sub>msalvalaggio · GitHub · 2026-09-18</sub><br>MCP 服务器，让 Claude 把整个浏览器任务交给 Jev，由 Jev 在约 100 毫秒内做出每一次点击、输入或选择决策，Claude 负责规划和验证。<br><sub><b>Jev 用法:</b> 每一步是在页面元素上的一个 Choice，因此不会选中页面上不存在的元素。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Xopher00/jevdevice"><img src="https://opengraph.githubassets.com/1/Xopher00/jevdevice" alt="jevdevice" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Xopher00/jevdevice">jevdevice</a></b><br><sub>Xopher00 · GitHub · 2026-09-19</sub><br>MCP harness，把一个自然语言目标转成在 Android 手机上通过 adb 或本地 shell 执行的恰好一个经过验证的动作，由 Jev（或本地 Laya）从实时发现的候选中挑选或拒绝。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/laihenyi/pi-Jev-browser"><img src="https://opengraph.githubassets.com/1/laihenyi/pi-Jev-browser" alt="Pi Jev Browser" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/laihenyi/pi-Jev-browser">Pi Jev Browser</a></b><br><sub>laihenyi · GitHub · 2026-09-19</sub><br>面向 Pi 的浏览器和 macOS 桌面 agent：Jev 根据结构化的页面观察（从不用截图）选出每一步动作，在有界循环中运行，带隔离的 Playwright 工具、卡死检测和交还给人的机制。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/hitakshia/solari-reflex"><img src="https://opengraph.githubassets.com/1/hitakshia/solari-reflex" alt="solari-reflex" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/hitakshia/solari-reflex">solari-reflex</a></b><br><sub>hitakshia · GitHub · 2026-09-18</sub><br>面向 Solari 浏览器和 Linux 桌面的电脑操控提速层：每一步只有一次结构化观察、一次 Jev 决策和一次经过验证的动作，不用截图。<br><sub><b>Jev 用法:</b> 一次 Stripe Checkout 运行耗时 60.2 秒、花费 $0.011，而通过 Solari 的 MCP 调用 Codex 需要 194.9 秒；在 LibreOffice Calc 里录入 30 笔报销耗时 24.2 秒。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Clawbuilders/web-qa-jev-agent"><img src="https://opengraph.githubassets.com/1/Clawbuilders/web-qa-jev-agent" alt="web-qa-jev-agent" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Clawbuilders/web-qa-jev-agent">web-qa-jev-agent</a></b><br><sub>Clawbuilders · GitHub · 2026-09-18</sub><br>Cloudflare Worker，借助 Browser Rendering 像 QA 测试员一样爬取 Web 应用，用 Jev 给发现的问题做分诊，再用视觉模型确认哪些是真问题，并提交去重后的 GitHub issue。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://yappy.biz/jev/"><img src="https://yappy.biz/assets/research/yappy-vs-heyclicky.png" alt="Yappy" width="240"></a></td>
<td valign="top"><b><a href="https://yappy.biz/jev/">Yappy</a></b><br><sub>Mitosis Labs · 应用 · 2026-09-19</sub><br>macOS 语音 agent，用 Jev 选择每一步电脑操控动作，只有打字时才调用聊天模型；在一次求职申请任务上实测 1 分 54 秒、$0.24，而某竞品是 13 分 14 秒、$4.24。<br><sub><b>Jev 用法:</b> 每一步由 Jev 从窗口的无障碍表中选出操作和目标控件；置信度下降时由完整 agent 接管。</sub><br><sub>相关: <a href="https://yappy.biz">app</a></sub></td>
</tr>
</table>

还缺什么？[提交一个资源](https://github.com/Li-Evan/awesome-jev/issues/new/choose)。
