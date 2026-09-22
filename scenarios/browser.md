# 🌐 Browser and Computer Use

**English** · [简体中文](https://github.com/Li-Evan/awesome-jev/blob/main/zh-CN/scenarios/browser.md)

Agents that click, type, and navigate real browsers, desktops, and phones. 128 entries, ranked by community traction.

[← Back to Awesome Jev](https://github.com/Li-Evan/awesome-jev#browse-by-scenario)

<table>
<tr>
<td width="260" valign="top"><a href="https://github.com/browser-use/jev-ultrafast"><img src="https://raw.githubusercontent.com/browser-use/jev-ultrafast/main/docs/banner.svg" alt="jev-ultrafast" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/browser-use/jev-ultrafast">jev-ultrafast</a></b><br><sub>browser-use · GitHub · ⭐ 16.6k · 2026-09-16</sub><br>Browser agent that picks each step's operation and target from an element table in one request, with a speculative target per operation and a small LLM only for typed text.<br><sub>Also: <a href="https://x.com/innoiso/status/2101128674779263220">demo</a> · <a href="https://news.ycombinator.com/item?id=49735979">discussion</a> · <a href="https://browser-use.com/ultrafast">website</a> · <a href="https://www.youtube.com/watch?v=NFKHLhAvj1g">video</a> · <a href="https://agentbreaking.com/blog/browser-use-jev-ultrafast-guide/">write-up</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/Saccc_c/status/2100864907046768890"><img src="https://pbs.twimg.com/amplify_video_thumb/2100853279089647616/img/H6altwjZQ28_1bfY.jpg" alt="Jev Use for Codex" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/Saccc_c/status/2100864907046768890">Jev Use for Codex</a></b><br><sub>Saccc_c · X · ♥ 1.8k · 2026-09-18</sub><br>Computer use for Codex with Jev as the decision layer, shown adding a Mac calendar event faster and more smoothly than Codex's built-in computer use at similar token cost.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/thdxr/status/2100288951978164647"><img src="https://pbs.twimg.com/amplify_video_thumb/2100286679386873857/img/vlw6EBlSVZ9uAoHc.jpg" alt="OpenCode browser use with Jev" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/thdxr/status/2100288951978164647">OpenCode browser use with Jev</a></b><br><sub>thdxr · X · ♥ 3.7k · 2026-09-16</sub><br>Preview of fast browser automation for app testing that pairs Jev with OpenCode's browser-use CLI.<br><sub>Also: <a href="https://x.com/Neriousy/status/2100287208166969746">demo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/awlevin/typesafe-computer-use"><img src="https://raw.githubusercontent.com/awlevin/typesafe-computer-use/main/docs/banner.svg" alt="typesafe-computer-use" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/awlevin/typesafe-computer-use">typesafe-computer-use</a></b><br><sub>awlevin · GitHub · ⭐ 769 · 2026-09-16</sub><br>Computer-use agent for macOS that OCRs the screen, has Jev classify the next action from the extracted controls and clicks, for about $0.0002 a step, calling a writing model only for free-text fields.<br><sub><b>How it uses Jev:</b> A Choice over up to 255 deterministically extracted actions per step, gated on its confidence.</sub><br><sub>Also: <a href="https://news.ycombinator.com/item?id=49733647">discussion</a> · <a href="https://x.com/awlevin/status/2100262612428894676">demo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/milind-soni/tiptour-macos"><img src="https://raw.githubusercontent.com/milind-soni/tiptour-macos/main/gemnew.png" alt="TipTour" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/milind-soni/tiptour-macos">TipTour</a></b><br><sub>milind-soni · GitHub · ⭐ 644 · 2026-04-08</sub><br>Menu bar computer-use app for macOS whose default mode takes a typed click-based task, has Jev choose among locally detected on-screen controls, then executes and validates each action.<br><sub>Also: <a href="https://www.supamaus.com/">site</a> · <a href="https://x.com/milindlabs/status/2100631847155994852">demo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/SUOHA_AI/status/2101640575812239406"><img src="https://pbs.twimg.com/amplify_video_thumb/2101632970717007872/img/lcQeA281BT79Pjt5.jpg" alt="Jev + DeepSeek form-filling agent" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/SUOHA_AI/status/2101640575812239406">Jev + DeepSeek form-filling agent</a></b><br><sub>SUOHA_AI · X · ♥ 173 · 2026-09-20</sub><br>Browser agent that filled a 16-question application form on an unfamiliar site in 38 seconds, with Jev choosing each action and DeepSeek V4.1 Flash writing the text answers.<br><sub><b>How it uses Jev:</b> Choice of click, check or submit per page; a small LLM only fills text fields.</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/savboj/status/2100545295201288678"><img src="https://pbs.twimg.com/amplify_video_thumb/2100545038677655552/img/PSyeykC06q5OLVVu.jpg" alt="Fast computer use" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/savboj/status/2100545295201288678">Fast computer use</a></b><br><sub>savboj · X · ♥ 1.3k · 2026-09-17</sub><br>Computer-use demo where Jev picks each action so quickly that the task finishes in a blink, pitched as 100x faster than an LLM.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/SUOHA_AI/status/2102091983292358839"><img src="https://pbs.twimg.com/amplify_video_thumb/2102088489231609856/img/AJle7-1PDPdXWJ6d.jpg" alt="Automated mock certification exam" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/SUOHA_AI/status/2102091983292358839">Automated mock certification exam</a></b><br><sub>SUOHA_AI · X · ♥ 755 · 2026-09-21</sub><br>Browser automation that completed an Alibaba Cloud AI engineer mock exam on an unseen page in 21 seconds, answering 25 questions at 80% accuracy, with Jev deciding each step and DeepSeek filling text.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/camsoft2000/status/2100648648434434298"><img src="https://pbs.twimg.com/amplify_video_thumb/2100648485695451136/img/kZ4JFKvjuPY7i6iz.jpg" alt="Jev + AXe iOS Simulator control" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/camsoft2000/status/2100648648434434298">Jev + AXe iOS Simulator control</a></b><br><sub>camsoft2000 · X · ♥ 1.3k · 2026-09-17</sub><br>Demo of Jev with the AXe CLI driving the iOS Simulator, operating apps much faster and at a fraction of the cost of an LLM.<br><sub>Also: <a href="https://github.com/cameroncooke/AXe">axe</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/cline/plugins/tree/main/plugins/jev-browser"><img src="https://github.com/user-attachments/assets/063c98fa-0067-40fb-af96-3714d8e017a5" alt="Cline jev-browser plugin" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/cline/plugins/tree/main/plugins/jev-browser">Cline jev-browser plugin</a></b><br><sub>cline · GitHub · ♥ 689 · 2026-05-31</sub><br>Plugin in Cline's official collection that delegates bounded Playwright browser steps to Jev through Vercel AI Gateway using structured DOM observations, with a separate text model filling form values.<br><sub>Also: <a href="https://github.com/cline/plugins">repo</a> · <a href="https://x.com/cline/status/2101056078872256935">demo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/kylejeong/status/2100622054945095934"><img src="https://pbs.twimg.com/amplify_video_thumb/2100495119065722880/img/7A1mijkU3Z_Zj7PM.jpg" alt="Stagehand + Jev browser agent" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/kylejeong/status/2100622054945095934">Stagehand + Jev browser agent</a></b><br><sub>kylejeong · X · ♥ 763 · 2026-09-17</sub><br>Browser agent on a remote browser where Jev picks each next action from the page's accessibility tree and Stagehand executes it; the demo task cost $0.001.<br><sub><b>How it uses Jev:</b> Accessibility tree as state, candidate actions as the question, one decision per step.</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/trycua/cua/tree/main/libs/cua-driver/examples/jev-use"><img src="https://raw.githubusercontent.com/trycua/cua/main/img/card-cua-fleets-wide.gif" alt="Cua jev-use" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/trycua/cua/tree/main/libs/cua-driver/examples/jev-use">Cua jev-use</a></b><br><sub>trycua · GitHub · ⭐ 25.8k repo · 2026-09-18</sub><br>Public-preview recipe in Cua Driver where Jev chooses the next browser action from bounded candidate IDs while the driver observes the page, performs the action and verifies the result, in Python and TypeScript.<br><sub><b>How it uses Jev:</b> Jev sees candidate IDs, descriptions and a compact DOM or visual-region observation, never screenshot bytes; answers must be a supplied ID.</sub><br><sub>Also: <a href="https://github.com/trycua/cua">repo</a> · <a href="https://cua.ai">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/ndrezn/status/2101046780989215005"><img src="https://pbs.twimg.com/amplify_video_thumb/2101046492945387521/img/-lkFln33BamAm3cB.jpg" alt="LangChain browser use with Jev" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/ndrezn/status/2101046780989215005">LangChain browser use with Jev</a></b><br><sub>ndrezn · X · ♥ 103 · 2026-09-18</sub><br>Browser agent built with LangChain and Jev that plays the Wikipedia Game and handles routine tasks like finding cheap flights.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/sarah_edo/status/2102025642862600634"><img src="https://pbs.twimg.com/ext_tw_video_thumb/2102025557969862656/pu/img/TDga5vamGpk6CRqZ.jpg" alt="WebMCP side panel" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/sarah_edo/status/2102025642862600634">WebMCP side panel</a></b><br><sub>sarah_edo · X · ♥ 845 · 2026-09-21</sub><br>Chrome extension side panel that drives any site's WebMCP tools: on every keystroke Jev picks the relevant page tool, fills in its arguments and shows how sure it is, demoed on grocery shopping.<br><sub><b>How it uses Jev:</b> Choice over the page's WebMCP tools per keystroke, plus argument filling with confidence.</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://jev-browser-use.val.run"><img src="https://pbs.twimg.com/amplify_video_thumb/2100321453455425537/img/hVYy_d3Nuw9XhSwg.jpg" alt="Jev Browser Use" width="240"></a></td>
<td valign="top"><b><a href="https://jev-browser-use.val.run">Jev Browser Use</a></b><br><sub>Steve Krouse · App · ♥ 240 · 2026-09-16</sub><br>Describe a task and watch Jev drive a live Kernel cloud browser, scoring every link on the page and picking the next click in an observe-choose-act loop.<br><sub><b>How it uses Jev:</b> Scores every link on the page, then a Choice picks one for Kernel to click.</sub><br><sub>Also: <a href="https://x.com/stevekrouse/status/2100321685081559542">demo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/aibuilderclub_/status/2101316543317684368"><img src="https://pbs.twimg.com/amplify_video_thumb/2101316420290441216/img/7RW7_i5vB12EHIKy.jpg" alt="jev-browser" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/aibuilderclub_/status/2101316543317684368">jev-browser</a></b><br><sub>aibuilderclub_ · X · ♥ 402 · 2026-09-19</sub><br>General browser skill for agents: given a website and a task, it opens a browser and Jev picks every click from what is on the screen.<br><sub><b>How it uses Jev:</b> One Choice per step over the clickable elements on the page.</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/nicobailon/surf-cli"><img src="https://raw.githubusercontent.com/nicobailon/surf-cli/main/surf-banner.png" alt="Surf" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/nicobailon/surf-cli">Surf</a></b><br><sub>nicobailon · GitHub · ⭐ 622 · 2025-12-28</sub><br>Surf, a zero-config CLI for AI agents to control Chrome, has an optional semantic.act mode that repeatedly observes the page, asks Jev to pick the next action from Surf's allowed menu, and executes it.<br><sub><b>How it uses Jev:</b> Bounded, goal-driven control opted in with --allow-semantic; local input values are never sent to Jev.</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/hqmank/status/2101529876469522673"><img src="https://pbs.twimg.com/amplify_video_thumb/2101529643073282048/img/HECGbREA0M-UMqNT.jpg" alt="jev-browser" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/hqmank/status/2101529876469522673">jev-browser</a></b><br><sub>hqmank · X · ♥ 403 · 2026-09-20</sub><br>General browser automation skill that pairs Jev with Playwright-controlled Chrome and works across agents, demoed in Antigravity CLI and Codex finding related articles and job openings.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Sac-Y/Jev-cu"><img src="https://opengraph.githubassets.com/1/Sac-Y/Jev-cu" alt="Jev-cu" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Sac-Y/Jev-cu">Jev-cu</a></b><br><sub>Sac-Y · GitHub · ⭐ 551 · 2026-09-18</sub><br>Chinese Codex skill that hands computer use's next-click decision to Jev: it picks the element, action, completion and risk from on-screen text candidates while Codex Computer Use reads and acts, with no screenshots sent.<br><sub><b>How it uses Jev:</b> Dry-run by default; deletes, sends, payments and installs stop at confirm, and apps must be on an allowlist.</sub><br><sub>Also: <a href="https://x.com/Saccc_c/status/2101152089598791845">demo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/mormonnegro/status/2100408498446111031"><img src="https://pbs.twimg.com/amplify_video_thumb/2100406900772732928/img/Gh4W4M-xUTPc4I3X.jpg" alt="Headless Chromium Wikipedia agent" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/mormonnegro/status/2100408498446111031">Headless Chromium Wikipedia agent</a></b><br><sub>mormonnegro · X · ♥ 213 · 2026-09-17</sub><br>Headless Chromium agent where Jev picks each link to follow, racing on Wikipedia from 'Café' to 'Inteligencia artificial' in 20 seconds.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/razaanstha/ulka"><img src="https://pbs.twimg.com/amplify_video_thumb/2100645348309921792/img/-BZE38QFdJJ67AJa.jpg" alt="Ulka" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/razaanstha/ulka">Ulka</a></b><br><sub>razaanstha · GitHub · ⭐ 21 · 2026-09-17</sub><br>Experimental browser-agent extension where FX orchestrates tasks, Jev picks constrained actions from Chromium's accessibility tree, and a runtime validates targets, asks for approvals, and records evidence.<br><sub>Also: <a href="https://news.ycombinator.com/item?id=49752776">discussion</a> · <a href="https://x.com/razaanstha/status/2100708222847853043">demo</a> · <a href="https://x.com/razaanstha/status/2100645675591520612">demo 2</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/wy-coliney/jev-browser-use"><img src="https://raw.githubusercontent.com/wy-coliney/jev-browser-use/main/assets/hero.png" alt="Jev Browser Use" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/wy-coliney/jev-browser-use">Jev Browser Use</a></b><br><sub>wy-coliney · GitHub · ⭐ 338 · 2026-09-18</sub><br>Codex browser skill where Jev handles navigation, clicks, toggles and scrolling over your existing browser connection while Codex keeps text input and final checks, ~5-10x faster in the author's EZCollegeApp workflows.<br><sub><b>How it uses Jev:</b> Sends page state and permitted candidates to Jev through TypeSafe or OpenRouter Decisions; the browser connection executes.</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/droidrun/mobile-jev"><img src="https://opengraph.githubassets.com/1/droidrun/mobile-jev" alt="mobile-jev" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/droidrun/mobile-jev">mobile-jev</a></b><br><sub>droidrun · GitHub · ⭐ 331 · 2026-09-17</sub><br>Android agent that applies the operation-plus-speculative-target pattern to a real phone.<br><sub>Also: <a href="https://mobilerun.ai">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/wobsoriano/touchpress"><img src="https://pbs.twimg.com/amplify_video_thumb/2100812811287031808/img/4TPBFtSzCOnjlkbR.jpg" alt="touchpress" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/wobsoriano/touchpress">touchpress</a></b><br><sub>wobsoriano · GitHub · ⭐ 28 · 2026-09-06</sub><br>End-to-end testing library for mobile apps whose act step can be driven by an evaluation model such as Jev, picking each move from the actions the current screen offers.<br><sub><b>How it uses Jev:</b> Set use.evaluationModel to typeSafeAi.evaluationModel('jev-latest') or 'typesafe-ai/jev-latest'; it replaces the language model for act.</sub><br><sub>Also: <a href="https://x.com/wobsoriano/status/2100813615410634997">demo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/shhivv/third-hand"><img src="https://opengraph.githubassets.com/1/shhivv/third-hand" alt="Third Hand" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/shhivv/third-hand">Third Hand</a></b><br><sub>shhivv · GitHub · ⭐ 285 · 2026-09-19</sub><br>Menu bar computer-use assistant for macOS that takes an instruction via Control-Space, reads the focused app's accessible controls, and types, clicks, and checks results with Jev making each decision.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/jkudish/jev-browser"><img src="https://raw.githubusercontent.com/jkudish/jev-browser/main/assets/github-demo.gif" alt="jev-browser" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/jkudish/jev-browser">jev-browser</a></b><br><sub>jkudish · GitHub · ⭐ 231 · 2026-09-17</sub><br>Headless browser driver usable as an MCP server, CLI, or library, with a Choice for the next action and Nouls for done or stuck.<br><sub>Also: <a href="https://x.com/jkudish/status/2100704171020493247">demo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/SSHCodes/status/2101026313871970721"><img src="https://pbs.twimg.com/amplify_video_thumb/2101026173631217664/img/icEy9hbMZ8lMNbQV.jpg" alt="Browser-agent stress test" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/SSHCodes/status/2101026313871970721">Browser-agent stress test</a></b><br><sub>SSHCodes · X · ♥ 26 · 2026-09-18</sub><br>Non-cheated browser-use test in which Jev completed about 5 actions before collapsing, with the author concluding it is not suited to browser agents.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://www.youtube.com/watch?v=VQPs9_US1xw"><img src="https://i.ytimg.com/vi/VQPs9_US1xw/hqdefault.jpg" alt="Jev browser control system" width="240"></a></td>
<td valign="top"><b><a href="https://www.youtube.com/watch?v=VQPs9_US1xw">Jev browser control system</a></b><br><sub>Marcin AI · YouTube · ♥ 43 · 2026-09-18</sub><br>Browser control system built around Jev that plays online chess almost in real time, browses sites, shops on Amazon, and takes spoken commands while Jev makes the decisions.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://www.youtube.com/watch?v=JsNQwFB9N1Q"><img src="https://i.ytimg.com/vi/JsNQwFB9N1Q/hqdefault.jpg" alt="rtrvr.ai" width="240"></a></td>
<td valign="top"><b><a href="https://www.youtube.com/watch?v=JsNQwFB9N1Q">rtrvr.ai</a></b><br><sub>Retriever AI · YouTube · ♥ 31 · 2026-09-17</sub><br>Tests Jev inside the rtrvr.ai browser agent on real web tasks, reporting where it worked, where it struggled, and how it will sit next to larger models.<br><sub>Also: <a href="https://rtrvr.ai/blog/jev-browser-agent-benchmark">benchmark</a> · <a href="https://rtrvr.ai/extension">app</a> · <a href="https://rtrvr.ai">project</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/shhivv/arc-cua"><img src="https://opengraph.githubassets.com/1/shhivv/arc-cua" alt="arc-cua" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/shhivv/arc-cua">arc-cua</a></b><br><sub>shhivv · GitHub · ⭐ 127 · 2026-09-20</sub><br>Action layer for computer-use agents where a planner hands bounded desktop subtasks to Jev, which runs the UI loop step by step with a freshness guard before returning control.<br><sub>Also: <a href="https://tryisle.com">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/plateaukao/einkbro/blob/main/app/src/main/java/info/plateaukao/einkbro/data/remote/JevReaderRepository.kt"><img src="https://repository-images.githubusercontent.com/253150295/e0705e24-5fef-4c71-9c4e-93f1f8c91d8b" alt="EinkBro Jev reader" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/plateaukao/einkbro/blob/main/app/src/main/java/info/plateaukao/einkbro/data/remote/JevReaderRepository.kt">EinkBro Jev reader</a></b><br><sub>plateaukao · GitHub · ⭐ 2k repo · 2020-04-05</sub><br>EinkBro, an E-Ink Android browser, uses Jev to classify page blocks for an uncluttered reader view, dropping only high-confidence non-article content.<br><sub><b>How it uses Jev:</b> Per-candidate questions over text, tag, role, class and link ratio; an uncertain or failed judgment leaves Readability untouched.</sub><br><sub>Also: <a href="https://plateaukao.github.io/einkbro">docs</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/agent-labs-dev/fastbrowse"><img src="https://raw.githubusercontent.com/agent-labs-dev/fastbrowse/main/assets/wordmark.svg" alt="fastbrowse" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/agent-labs-dev/fastbrowse">fastbrowse</a></b><br><sub>agent-labs-dev · GitHub · ⭐ 94 · 2026-09-17</sub><br>Experimental browser agent that indexes the page into candidate actions for Jev to pick, lets an LLM plan and read, and makes every claim in an answer cite a verbatim page quote, with consequential actions needing authorization.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/APUS-AI-Lab/fast-browser-use"><img src="https://raw.githubusercontent.com/APUS-AI-Lab/fast-browser-use/main/docs/banner.svg" alt="Fast Browser Use" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/APUS-AI-Lab/fast-browser-use">Fast Browser Use</a></b><br><sub>APUS-AI-Lab · GitHub · ⭐ 90 · 2026-09-19</sub><br>Local browser-use agent skill for Claude Code, Codex and Cursor that reproduces Jev's System One paradigm with Qwen3.5 weights, scoring visible elements as single-token choices.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/savka777/jev-use"><img src="https://raw.githubusercontent.com/savka777/jev-use/main/docs/banner.png" alt="jev-use" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/savka777/jev-use">jev-use</a></b><br><sub>savka777 · GitHub · ⭐ 86 · 2026-09-19</sub><br>Native macOS computer-use app: hold a shortcut, say or type what you want, and it performs on-screen actions by reading the Accessibility tree, with no screenshots or vision model.<br><sub><b>How it uses Jev:</b> Jev picks the next on-screen action from the Accessibility elements; macOS performs it.</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/sdras/jev-webmcp-extension"><img src="https://raw.githubusercontent.com/sdras/jev-webmcp-extension/main/icons/screenshot.jpg" alt="Jev × WebMCP" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/sdras/jev-webmcp-extension">Jev × WebMCP</a></b><br><sub>sdras · GitHub · ⭐ 85 · 2026-09-19</sub><br>Chrome side-panel extension that discovers the WebMCP tools a page exposes and uses Jev to pick and fill the right tool call as you type, showing confidence and latency with no site-specific setup.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/lahfir/agent-desktop/tree/main/scripts/jev"><img src="https://raw.githubusercontent.com/lahfir/agent-desktop/main/docs/architecture.png" alt="Agent Desktop Jev skill" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/lahfir/agent-desktop/tree/main/scripts/jev">Agent Desktop Jev skill</a></b><br><sub>lahfir · GitHub · ⭐ 1.4k repo · 2026-09-17</sub><br>Jev skill for the agent-desktop Rust computer-use CLI that drives a desktop app from one goal by reading the accessibility tree and picking one operation and target per turn, keeping the tree out of the agent's context.<br><sub><b>How it uses Jev:</b> Each turn asks for an operation (CLICK, TYPE_TEXT, DRILL, DONE, ...) and the target for that operation in the same request.</sub><br><sub>Also: <a href="https://github.com/lahfir/agent-desktop">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/sahibzada-allahyar/gliner2-ultrafast"><img src="https://raw.githubusercontent.com/sahibzada-allahyar/gliner2-ultrafast/main/docs/demo.gif" alt="GLiNER Browser Use" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/sahibzada-allahyar/gliner2-ultrafast">GLiNER Browser Use</a></b><br><sub>sahibzada-allahyar · GitHub · ⭐ 67 · 2026-09-18</sub><br>Browser automation adapted from Browser Use's Jev Ultrafast that swaps the decision layer for local open-weight GLiNER2 scoring page controls, with a small text model for typed values.<br><sub>Also: <a href="https://github.com/browser-use/jev-ultrafast">upstream</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Ying-Kai-Liao/jev-browser"><img src="https://opengraph.githubassets.com/1/Ying-Kai-Liao/jev-browser" alt="jev-browser" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Ying-Kai-Liao/jev-browser">jev-browser</a></b><br><sub>Ying-Kai-Liao · GitHub · ⭐ 67 · 2026-09-16</sub><br>Browser automation library, CLI, and MCP server where the calling LLM states each step's goal and Jev picks the element, action, and value while Playwright executes.<br><sub><b>How it uses Jev:</b> One ~300 ms request per round asks which element, action, and value, and whether the step is done, blocked, erroring, or about to do something irreversible.</sub><br><sub>Also: <a href="https://github.com/user-attachments/assets/2e688df9-4985-4854-8ebe-ba97c9d13d68">video</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/FluidInference/FluidUse"><img src="https://opengraph.githubassets.com/1/FluidInference/FluidUse" alt="FluidUse" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/FluidInference/FluidUse">FluidUse</a></b><br><sub>FluidInference · GitHub · ⭐ 62 · 2026-09-21</sub><br>Local computer use on Apple silicon: reads forms in Mac apps via the Accessibility API and fills them on-device. Ships a Core ML port of the Jev-style laya model at 3.7 ms per short question on the Neural Engine.<br><sub><b>How it uses Jev:</b> LayaManager answers typed choice/score/noul questions about a text state on-device; forms use the CUA-S1-FORMS specialist.</sub><br><sub>Also: <a href="https://huggingface.co/FluidInference/laya-coreml">model</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/yikangy873-gif/jev-desktop"><img src="https://opengraph.githubassets.com/1/yikangy873-gif/jev-desktop" alt="Jev Desktop for Codex" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/yikangy873-gif/jev-desktop">Jev Desktop for Codex</a></b><br><sub>yikangy873-gif · GitHub · ⭐ 60 · 2026-09-19</sub><br>Plugin that adds a bounded decision loop to Codex Computer Use for browser tabs and native macOS apps: Codex sets the goal and allowed actions, Jev picks an operation and target per step, and Computer Use executes it.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/webbrain-one/webbrain/blob/main/src/chrome/src/agent/systemone-fast.js"><img src="https://raw.githubusercontent.com/webbrain-one/webbrain/main/assets/webbrain-demo.gif" alt="WebBrain System One agent" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/webbrain-one/webbrain/blob/main/src/chrome/src/agent/systemone-fast.js">WebBrain System One agent</a></b><br><sub>webbrain-one · GitHub · ⭐ 1.1k repo · 2026-04-06</sub><br>WebBrain, an open browser agent for Chrome and Firefox, uses Jev as a fast classifier and judge in its agent loop, with redacted evidence and confidence thresholds.<br><sub><b>How it uses Jev:</b> Separate fast, judge and evidence modules with a 0.85 classifier and 0.90 browser threshold.</sub><br><sub>Also: <a href="https://webbrain.one">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/gergomoricz/status/2100301843507159443"><img src="https://pbs.twimg.com/amplify_video_thumb/2100301754411659264/img/EHQ6OuvTeyHuSC4M.jpg" alt="Jev browser-use demo" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/gergomoricz/status/2100301843507159443">Jev browser-use demo</a></b><br><sub>gergomoricz · X · ♥ 28 · 2026-09-16</sub><br>Screen recording of a browser agent driven by Jev clicking through web pages in real time.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/affirmitv/ghosthands"><img src="https://opengraph.githubassets.com/1/affirmitv/ghosthands" alt="ghosthands" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/affirmitv/ghosthands">ghosthands</a></b><br><sub>affirmitv · GitHub · ⭐ 49 · 2026-08-27</sub><br>GUI automation that drives a real screen over a $4 USB-HID microcontroller, with Jev picking the operation and element from an indexed control table; a click step costs about $0.0001 and 0.4 s.<br><sub><b>How it uses Jev:</b> Fast lane is one Jev call through OpenRouter's decisions endpoint; a small vision LLM handles screens with no element table.</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/ipenywis/laya-ultrafast"><img src="https://opengraph.githubassets.com/1/ipenywis/laya-ultrafast" alt="Laya Ultrafast" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/ipenywis/laya-ultrafast">Laya Ultrafast</a></b><br><sub>ipenywis · GitHub · ⭐ 48 · 2026-09-21</sub><br>Local port of Browser Use's jev-ultrafast browser agent that makes its decisions with the open Laya model through MLX on Apple Silicon instead of hosted Jev.<br><sub>Also: <a href="https://github.com/browser-use/jev-ultrafast">original</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/ndrezn/ts-browser-agent"><img src="https://raw.githubusercontent.com/ndrezn/ts-browser-agent/main/docs/wiki_game.gif" alt="ts-browser-agent" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/ndrezn/ts-browser-agent">ts-browser-agent</a></b><br><sub>ndrezn · GitHub · ⭐ 30 · 2026-09-18</sub><br>Browser agent built on langchain-typesafe and LangChain's create_agent, with Jev as the model and browser actions as tools, shown playing the Wikipedia Game from LangChain to Microphone.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/nottecore/status/2101021237417787819"><img src="https://pbs.twimg.com/amplify_video_thumb/2101020534754422784/img/j_5WSNZVx35w--DS.jpg" alt="Jevmaxxing" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/nottecore/status/2101021237417787819">Jevmaxxing</a></b><br><sub>nottecore · X · ♥ 12 · 2026-09-18</sub><br>Browser agent on Notte cloud sessions: type a task and Jev picks every action from the page's action space, with a step-by-step replay of each decision.<br><sub><b>How it uses Jev:</b> One Choice per step over a freshly extracted action space.</sub><br><sub>Also: <a href="http://jevmaxxing.com">app</a> · <a href="https://github.com/nottelabs/notte-jevmaxxing">repo</a> · <a href="https://github.com/nottelabs/notte-jevmaxxing">project</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/jcpsimmons/jev-macos-loop"><img src="https://raw.githubusercontent.com/jcpsimmons/jev-macos-loop/master/docs/media/jev-finder-batch-demo.gif" alt="Jev macOS Loop" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/jcpsimmons/jev-macos-loop">Jev macOS Loop</a></b><br><sub>jcpsimmons · GitHub · ⭐ 19 · 2026-09-18</sub><br>Computer-use agent for native macOS apps on Apple silicon that finds controls locally with OmniParser CoreML, Vision OCR and accessibility data, then lets Jev pick the next action; 9 files sorted in 7.39 s.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/varun_mathur/status/2102232629902819580"><img src="https://pbs.twimg.com/amplify_video_thumb/2102229039784022016/img/rG7JcDFdZW-Pa16S.jpg" alt="Hyperspace agentic-os Amazon order" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/varun_mathur/status/2102232629902819580">Hyperspace agentic-os Amazon order</a></b><br><sub>varun_mathur · X · ♥ 5 · 2026-09-22</sub><br>Hyperspace's agentic OS on a MacBook, combining Jev with a frontier model, autonomously orders a book on Amazon in about 30 seconds.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/chy4pro/jev-for-chrome"><img src="https://raw.githubusercontent.com/chy4pro/jev-for-chrome/main/docs/demo.gif" alt="Jev for Chrome" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/chy4pro/jev-for-chrome">Jev for Chrome</a></b><br><sub>chy4pro · GitHub · ⭐ 16 · 2026-09-18</sub><br>Community Manifest V3 port of jev-ultrafast that drives the tab you are looking at, with Jev picking the operation and element in one request and a small text model writing typed values, via OpenRouter, TypeSafe or Cloudflare.</td>
</tr>
<tr>
<td width="260" valign="top"></td>
<td valign="top"><b><a href="https://www.npmjs.com/package/@mlola/decision-jev">@mlola/decision-jev</a></b><br><sub>MLola · Package · ⬇ 1.4k · 2026-09-17</sub><br>Jev fast-path decision provider for the MLola Browser Runtime, sending one request per decision cycle and validating the response before any browser action runs.<br><sub><b>How it uses Jev:</b> One request per decision cycle carrying the operation head plus speculative target heads over a dynamic action space.</sub><br><sub>Also: <a href="https://mlola.com/browser-runtime">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/romaluev/jev-ego"><img src="https://opengraph.githubassets.com/1/romaluev/jev-ego" alt="jev-ego" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/romaluev/jev-ego">jev-ego</a></b><br><sub>romaluev · GitHub · ⭐ 13 · 2026-09-17</sub><br>TypeScript browser agent for the ego lite browser that numbers actionable elements so a coding agent or Jev can pick CLICK, TYPE_TEXT, or SELECT with one request per step.<br><sub><b>How it uses Jev:</b> A Choice over the numbered element table and operation per step, following the jev-ultrafast action space.</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/yegor/status/2101368226911232406"><img src="https://pbs.twimg.com/amplify_video_thumb/2101367134278344704/img/WJyEFS976FdNKAnB.jpg" alt="Talk-to browser" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/yegor/status/2101368226911232406">Talk-to browser</a></b><br><sub>yegor · X · ♥ 4 · 2026-09-19</sub><br>Standalone browser you can talk to, with Jev making the fast decisions and a local LLM handling everything else, shown booking a hotel and playing Wikirace at superhuman speed.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/grabbou/jevil"><img src="https://opengraph.githubassets.com/1/grabbou/jevil" alt="jevil" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/grabbou/jevil">jevil</a></b><br><sub>grabbou · GitHub · ⭐ 12 · 2026-09-17</sub><br>Mobile QA agent proof of concept: it reads an iOS or Android app through agent-device, asks Jev to choose the next action, performs it, and saves a report, decision trace and recording.<br><sub><b>How it uses Jev:</b> One Choice per step over the available actions plus qa_pass, qa_fail and incomplete, which ends the run and sets its status.</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/jiawei686/jev-ultrafast-mcp"><img src="https://raw.githubusercontent.com/jiawei686/jev-ultrafast-mcp/main/assets/social-preview.png" alt="jev-ultrafast-mcp" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/jiawei686/jev-ultrafast-mcp">jev-ultrafast-mcp</a></b><br><sub>jiawei686 · GitHub · ⭐ 9 · 2026-09-19</sub><br>MCP server that takes a whole browser task (URL, goal and checks) in one tool call and has a decision model drive Chrome over CDP, picking only elements the page has and replaying flows as model-free macros.<br><sub>Also: <a href="https://pypi.org/project/jev-ultrafast-mcp/">pypi</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/fellowship-dev/navvi"><img src="https://raw.githubusercontent.com/fellowship-dev/navvi/main/docs/navvi-logo.png" alt="Navvi" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/fellowship-dev/navvi">Navvi</a></b><br><sub>fellowship-dev · GitHub · ⭐ 9 · 2026-03-20</sub><br>MCP server that turns a browser task into a reusable scraper: Jev chooses among controls and fields found by code, and Navvi saves selectors, fingerprints and a navigation trace for replay and repair.<br><sub><b>How it uses Jev:</b> Typed decisions over code-found candidates; a text-capable fallback handles prompt interpretation and values to type. The README compares compile runs of Haiku and Jev.</sub><br><sub>Also: <a href="https://pypi.org/project/navvi/">pypi</a> · <a href="https://github.com/fellowship-dev/navvi/blob/main/src/chooser/jev.ts">code</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/ranjan2829/AskJev"><img src="https://opengraph.githubassets.com/1/ranjan2829/AskJev" alt="AskJev" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/ranjan2829/AskJev">AskJev</a></b><br><sub>ranjan2829 · GitHub · ⭐ 8 · 2026-09-17</sub><br>Claude Desktop extension and Chrome add-on that drives Brave or Chrome from plain-English requests, with Jev deciding each on-page action and a guard freezing irreversible clicks such as payments or deletions.<br><sub><b>How it uses Jev:</b> Jev picks page actions with Noul, Choice and Score questions and rates risk and irreversibility; Claude is not the planner.</sub><br><sub>Also: <a href="https://x.com/manofsteel3129/status/2101090226856931776">demo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Nancy-Chauhan/hearth-jev-rental-search"><img src="https://raw.githubusercontent.com/Nancy-Chauhan/hearth-jev-rental-search/main/jev_ultrafast/static/backdrop.jpg" alt="Hearth" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Nancy-Chauhan/hearth-jev-rental-search">Hearth</a></b><br><sub>Nancy-Chauhan · GitHub · ⭐ 8 · 2026-09-20</sub><br>Local agent that drives a real Chrome browser across Craigslist, Facebook Marketplace, Redfin and Zillow from one plain-language request, with Jev choosing each action, and returns a read-only rental shortlist.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/jekhov/jekhov"><img src="https://opengraph.githubassets.com/1/jekhov/jekhov" alt="Jekhov" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/jekhov/jekhov">Jekhov</a></b><br><sub>jekhov · GitHub · ⭐ 8 · 2026-09-18</sub><br>Library and CLI that make known Playwright workflows more resilient by letting Jev pick the target element from filtered accessibility-tree candidates, or abstain, while the workflow stays deterministic.<br><sub><b>How it uses Jev:</b> One Choice over action-compatible candidates plus a separate estimate that the match is unambiguous; actions run only behind calibrated gates, and public-site runs are shadow-only.</sub></td>
</tr>
<tr>
<td width="260" valign="top"></td>
<td valign="top"><b><a href="https://x.com/ChrisAdcockMD/status/2101126098603888862">Grok Bot Ultrafast integration</a></b><br><sub>ChrisAdcockMD · X · ♥ 2 · 2026-09-19</sub><br>Grok Bot integration of the Ultrafast approach that lets bots use Jev to drive the real Chrome on the machine and flags which existing bot decisions Jev could take over.<br><sub>Also: <a href="https://x.ai/bot/sM_Xi4OF09cGU8KGyLvlC">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/himomohi/aside-jev"><img src="https://raw.githubusercontent.com/himomohi/aside-jev/main/docs/assets/aside-jev-hero.png" alt="Aside Jev" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/himomohi/aside-jev">Aside Jev</a></b><br><sub>himomohi · GitHub · ⭐ 6 · 2026-09-17</sub><br>MCP server, skill and browser extension that let Aside browser agents hand action selection to Jev, which picks the next action from an application-defined candidate table.<br><sub><b>How it uses Jev:</b> Jev returns an action ID from the candidate table; Aside executes and verifies it.</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/tontoko/jev-browser"><img src="https://opengraph.githubassets.com/1/tontoko/jev-browser" alt="Jev Browser" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/tontoko/jev-browser">Jev Browser</a></b><br><sub>tontoko · GitHub · ⭐ 6 · 2026-09-17</sub><br>Playwright automation core with a typed SDK, persistent CLI and MCP server where Jev chooses actions, matches form fields and extracts content from real page elements instead of generating selectors.<br><sub><b>How it uses Jev:</b> Parallel Choices over supplied element candidates; Playwright executes and deterministic assertions verify.</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/forvela/jev-agent-browser"><img src="https://raw.githubusercontent.com/forvela/jev-agent-browser/main/media/huggingface-filter-demo.gif" alt="jev-agent-browser" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/forvela/jev-agent-browser">jev-agent-browser</a></b><br><sub>forvela · GitHub · ⭐ 6 · 2026-09-19</sub><br>Bounded browser execution for parent agents in which Jev picks each typed action that agent-browser runs, and ambiguity, repetition or stuck states come back to the parent as a structured handoff.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/parkers0405/neoism/blob/main/neoism-agent/crates/neoism-agent-server/src/computer_use/typesafe.rs"><img src="https://raw.githubusercontent.com/parkers0405/neoism/241e6daaea1249d2eff6ca94b91dbacc2c426b0f/docs/images/terminal.png" alt="Neoism TypeSafe computer mode" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/parkers0405/neoism/blob/main/neoism-agent/crates/neoism-agent-server/src/computer_use/typesafe.rs">Neoism TypeSafe computer mode</a></b><br><sub>parkers0405 · GitHub · ⭐ 119 repo · 2026-04-27</sub><br>Terminal-first IDE whose agent can drive the browser with Jev, choosing the next action from observed DOM candidates, then running a separate risk check on the exact action.<br><sub><b>How it uses Jev:</b> Choice plus done in one request, gated at 0.85 confidence and 0.75 selected probability; a scoped Noul risk request follows.</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/dom-actions/doma/tree/main/src/services/chat/jev"><img src="https://opengraph.githubassets.com/1/dom-actions/doma" alt="DomA Jev assist" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/dom-actions/doma/tree/main/src/services/chat/jev">DomA Jev assist</a></b><br><sub>dom-actions · GitHub · ⭐ 104 repo · 2026-09-09</sub><br>Open-source browser automation extension that adds an optional Jev assist inside its screenshot act loops, choosing among set-of-mark elements.<br><sub>Also: <a href="https://www.domactions.com/docs/en/">docs</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/GoldenLoaf24h/browserclaw"><img src="https://opengraph.githubassets.com/1/GoldenLoaf24h/browserclaw" alt="BrowserClaw" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/GoldenLoaf24h/browserclaw">BrowserClaw</a></b><br><sub>GoldenLoaf24h · GitHub · ⭐ 5 · 2026-09-10</sub><br>Chrome MV3 extension and native-messaging MCP server that lets AI agents drive your everyday logged-in Chrome, including a chrome_act_toward_goal tool where a Jev micro-loop picks actions over a pruned DOM tree.<br><sub>Also: <a href="https://www.reddit.com/r/AI_Agents/comments/1wkmp2z/why_calling_cloud_llms_for_every_browser_click_is/">discussion</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Nguy-n-Th-Huy/Browzy"><img src="https://opengraph.githubassets.com/1/Nguy-n-Th-Huy/Browzy" alt="Browzy" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Nguy-n-Th-Huy/Browzy">Browzy</a></b><br><sub>Nguy-n-Th-Huy · GitHub · ⭐ 5 · 2026-09-09</sub><br>Clean-room reimplementation of the Claude in Chrome extension without a domain blocklist, with a beta Jev mode where an LLM prepares the plan and Jev picks each complete browser action.<br><sub><b>How it uses Jev:</b> Each cycle asks three independent questions: which complete action to take, whether the goal may be complete, and whether progress is stuck.</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/pumpkinredbean/bside"><img src="https://opengraph.githubassets.com/1/pumpkinredbean/bside" alt="bside" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/pumpkinredbean/bside">bside</a></b><br><sub>pumpkinredbean · GitHub · ⭐ 5 · 2026-09-17</sub><br>Drives the Aside browser with Jev picking the action, element and goal-met check each tick; on a five-step Wikipedia task it took 52.8 s and about $0.0018 versus 72.9 s and $0.039 for a frontier LLM.<br><sub><b>How it uses Jev:</b> Choices over an enumerated action schema and on-page element refs, so it cannot click elements that do not exist; also exposes an MCP server.</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/buluoray/JevOnly"><img src="https://opengraph.githubassets.com/1/buluoray/JevOnly" alt="JevOnly" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/buluoray/JevOnly">JevOnly</a></b><br><sub>buluoray · GitHub · ⭐ 5 · 2026-09-19</sub><br>Browser agent with no LLM anywhere: code enumerates every option from the page and the goal, and Jev only picks the next action, with verification, undo and an irreversible-action gate.<br><sub><b>How it uses Jev:</b> One request per step answers done?, off path? and which action next? over code-enumerated options; field values can only be facts, spans of the goal or values copied from the page.</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/filedcom/playjev"><img src="https://raw.githubusercontent.com/filedcom/playjev/main/docs/public/playjev-golden-logo.png" alt="PlayJev" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/filedcom/playjev">PlayJev</a></b><br><sub>filedcom · GitHub · ⭐ 5 · 2026-09-20</sub><br>TypeScript library that adds plain-English browser automation to Playwright, like Stagehand but with Jev choosing clicks, navigation, form fills, and options instead of a generative LLM.<br><sub>Also: <a href="https://www.reddit.com/r/LLM/comments/1wli7sk/i_built_browser_automation_with_jev_and_its/">discussion</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/vinilana/jev-browser"><img src="https://opengraph.githubassets.com/1/vinilana/jev-browser" alt="Jev Browser (hybrid harness)" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/vinilana/jev-browser">Jev Browser (hybrid harness)</a></b><br><sub>vinilana · GitHub · ⭐ 4 · 2026-09-17</sub><br>TypeScript browser harness where an OpenRouter LLM splits goals into verifiable subgoals, Jev chooses each action and DOM field, OpenRouter writes field text when needed, and Playwright acts.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Tongyun1/Jev-in-the-Loop"><img src="https://raw.githubusercontent.com/Tongyun1/Jev-in-the-Loop/main/docs/media/demo-hotel.gif" alt="Jev-in-the-Loop" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Tongyun1/Jev-in-the-Loop">Jev-in-the-Loop</a></b><br><sub>Tongyun1 · GitHub · ⭐ 4 · 2026-09-21</sub><br>Codex plugin for fast browser work in local Chrome: Codex plans the task and prepares text, while Jev picks each next action and its target.<br><sub><b>How it uses Jev:</b> One TypeSafe request per step returns the action, target and prepared input; no separate text-model key needed.</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/NobleSpartan6/otto"><img src="https://opengraph.githubassets.com/1/NobleSpartan6/otto" alt="Otto" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/NobleSpartan6/otto">Otto</a></b><br><sub>NobleSpartan6 · GitHub · ⭐ 4 · 2026-09-17</sub><br>Early-alpha desktop computer-use agent for macOS and Windows that works through native accessibility controls and local OCR, combining Jev decisions with an optional GPT-6 Astra planner.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/paulsmith/computer-use-jev"><img src="https://opengraph.githubassets.com/1/paulsmith/computer-use-jev" alt="computer-use-jev" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/paulsmith/computer-use-jev">computer-use-jev</a></b><br><sub>paulsmith · GitHub · ⭐ 3 · 2026-09-16</sub><br>Go library that drives native macOS apps through the Accessibility API with Jev as the decision loop, choosing the next action, target element, text input and completion each step.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/ZephyrDeng/ego-jev"><img src="https://raw.githubusercontent.com/ZephyrDeng/ego-jev/main/docs/banner.svg" alt="ego-jev" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/ZephyrDeng/ego-jev">ego-jev</a></b><br><sub>ZephyrDeng · GitHub · ⭐ 3 · 2026-09-21</sub><br>Agent skill that gives the ego lite browser a Jev inner loop: each DOM step numbers the interactive elements and one Jev call of about 0.4 s picks the operation and target; logins and payments go to the planner.<br><sub>Also: <a href="https://skills.sh/ZephyrDeng/ego-jev">skill</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/kyrylosyzonenko/jev-browse"><img src="https://raw.githubusercontent.com/kyrylosyzonenko/jev-browse/main/assets/demo.gif" alt="jev-browse" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/kyrylosyzonenko/jev-browse">jev-browse</a></b><br><sub>kyrylosyzonenko · GitHub · ⭐ 3 · 2026-09-16</sub><br>Browser agent where Jev makes every decision and Vercel's agent-browser performs every action; on 10 tasks it passed 30/30 runs at 4.4 s and $0.0009 per task, versus 9.4 s and $0.0679 for Claude Code.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/0x7067/jev-browse"><img src="https://raw.githubusercontent.com/0x7067/jev-browse/main/docs/banner.svg" alt="jev-browse (0x7067)" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/0x7067/jev-browse">jev-browse (0x7067)</a></b><br><sub>0x7067 · GitHub · ⭐ 3 · 2026-09-18</sub><br>TypeScript browser agent with an indexed action space where Jev picks an operation and element and a small LLM writes text only for TYPE_TEXT; it installs on Pi, Claude Code, Codex and MCP harnesses.<br><sub><b>How it uses Jev:</b> Demo: Zürich to London on Google Flights in 17.6 seconds.</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Friedjof/jev-mobile"><img src="https://opengraph.githubassets.com/1/Friedjof/jev-mobile" alt="jev-mobile" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Friedjof/jev-mobile">jev-mobile</a></b><br><sub>Friedjof · GitHub · ⭐ 3 · 2026-09-17</sub><br>Durable Android sub-agent that runs an observe, decide, act and verify loop on a USB-connected phone through Mobile MCP, with Jev choosing among technically valid actions and never generating coordinates or code.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/antiyro/jevdroid"><img src="https://opengraph.githubassets.com/1/antiyro/jevdroid" alt="JevDroid" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/antiyro/jevdroid">JevDroid</a></b><br><sub>antiyro · GitHub · ⭐ 3 · 2026-09-18</sub><br>Python framework where Jev reads the Android accessibility tree and picks each tap, swipe or app launch toward a goal, executed over ADB or UIAutomator2 with permissions and budgets; 314 ms median per decision.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/iuhoay/skills/tree/main/chrome-devtools"><img src="https://opengraph.githubassets.com/1/iuhoay/skills" alt="chrome-devtools skill" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/iuhoay/skills/tree/main/chrome-devtools">chrome-devtools skill</a></b><br><sub>iuhoay · GitHub · ⭐ 53 repo · 2026-02-11</sub><br>Coding-agent skill that wraps chrome-devtools and, after a short page snapshot, batches TypeSafe Jev questions about the page instead of dumping the whole DOM into context.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/agentsea/nautilo/tree/main/packages/agent/src/tools/browser"><img src="https://nautilo.ai/docs/operator/first-nautilo/writer-review.png" alt="Nautilo Jev browser decisions" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/agentsea/nautilo/tree/main/packages/agent/src/tools/browser">Nautilo Jev browser decisions</a></b><br><sub>agentsea · GitHub · ⭐ 51 repo · 2026-09-16</sub><br>Routine-browser delegation in the Nautilo self-hosted multiplayer agent workspace: a Genie hands a browser segment to a Jev Choice model that picks the next action after every page observation, handing back when stuck.<br><sub><b>How it uses Jev:</b> A catalogued Choice model (Jev via OpenRouter) chooses among fresh page targets and action templates each step; optional progress/success predicates.</sub><br><sub>Also: <a href="https://nautilo.ai">app</a> · <a href="https://github.com/agentsea/nautilo">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/vstorm-co/agenticos/tree/main/backend/app/agents/capabilities/browser_choice"><img src="https://repository-images.githubusercontent.com/1318197751/15610d40-b4eb-458a-8808-cfc811544b1c" alt="AgenticOS browser_choice" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/vstorm-co/agenticos/tree/main/backend/app/agents/capabilities/browser_choice">AgenticOS browser_choice</a></b><br><sub>vstorm-co · GitHub · ⭐ 45 repo · 2026-07-31</sub><br>Browser capability in the AgenticOS self-hosted agent platform that reads a page into a numbered table of actionable elements and asks a decision model which operation and element to use, so page text cannot inject new actions.<br><sub><b>How it uses Jev:</b> Each step is a type-constrained choice over server-built DOM options, with BLOCKED as an answer and a min_confidence floor; only typed field values reach an LLM.</sub><br><sub>Also: <a href="https://vstorm-co.github.io/agenticos/">app</a> · <a href="https://github.com/vstorm-co/agenticos">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/EastStarAI/sanad-agent/tree/main/.agents/skills/jev-dual-brain-automation"><img src="https://raw.githubusercontent.com/EastStarAI/sanad-agent/main/client/assets/brand/sanad-wordmark-horizontal.svg" alt="Jev Dual-Brain automation skill" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/EastStarAI/sanad-agent/tree/main/.agents/skills/jev-dual-brain-automation">Jev Dual-Brain automation skill</a></b><br><sub>EastStarAI · GitHub · ⭐ 45 repo · 2026-08-01</sub><br>Agent skill in the Sanad Agent repo for browser and Flutter desktop UI automation: Jev picks DOM candidates and verifies goals in a sub-second loop, and a frontier model takes over when a loop-detecting circuit breaker trips.<br><sub><b>How it uses Jev:</b> Choice over DOM/UI-tree candidates (~700ms) plus a Noul goal check; the strong model handles obstacles and re-delegates.</sub><br><sub>Also: <a href="https://github.com/EastStarAI/sanad-agent">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/ZHUBoer/ego-jev"><img src="https://opengraph.githubassets.com/1/ZHUBoer/ego-jev" alt="ego-jev" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/ZHUBoer/ego-jev">ego-jev</a></b><br><sub>ZHUBoer · GitHub · ⭐ 2 · 2026-09-19</sub><br>Agent skill that completes browser tasks in a real Chromium via Ego Lite and calls Jev for semantic target selection, filtering, ranking, classification, and evidence checks, keeping exact work in code.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/jiangkoumo/ego-jev"><img src="https://opengraph.githubassets.com/1/jiangkoumo/ego-jev" alt="ego-jev (jiangkoumo)" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/jiangkoumo/ego-jev">ego-jev (jiangkoumo)</a></b><br><sub>jiangkoumo · GitHub · ⭐ 2 · 2026-09-19</sub><br>Agent skill that drives the ego lite browser with Jev: one indexed table of on-screen elements goes in and one operation plus target comes out per step, about 2x faster than a per-step LLM loop in the author's tests.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/ZihuaEvan/GUI_JEV"><img src="https://opengraph.githubassets.com/1/ZihuaEvan/GUI_JEV" alt="GUI JEV Harness" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/ZihuaEvan/GUI_JEV">GUI JEV Harness</a></b><br><sub>ZihuaEvan · GitHub · ⭐ 2 · 2026-09-21</sub><br>Screenshot-in, coordinate-out GUI grounding harness in which a vision model describes grid tiles and Jev picks one tile per recursion level, with probability and margin gates deciding whether to descend or refuse.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/dougsong/jev-android"><img src="https://opengraph.githubassets.com/1/dougsong/jev-android" alt="jev-android" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/dougsong/jev-android">jev-android</a></b><br><sub>dougsong · GitHub · ⭐ 2 · 2026-09-20</sub><br>Kotlin SDK for Android UI automation where Jev or DeepSeek picks actions from the actual controls on screen and an accessibility service executes them, with a sample app.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/aidil2105/jev-browser-pilot"><img src="https://opengraph.githubassets.com/1/aidil2105/jev-browser-pilot" alt="jev-browser-pilot" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/aidil2105/jev-browser-pilot">jev-browser-pilot</a></b><br><sub>aidil2105 · GitHub · ⭐ 2 · 2026-09-18</sub><br>Bounded decision layer for browser and desktop automation where code observes, lists candidate actions, executes, and verifies, and the model only picks the next candidate.<br><sub><b>How it uses Jev:</b> One Choice over code-built candidate IDs per step, with confidence routing and an audit trail.</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/brnyxx/jev-ra"><img src="https://raw.githubusercontent.com/brnyxx/jev-ra/main/assets/hero.png" alt="jev-ra" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/brnyxx/jev-ra">jev-ra</a></b><br><sub>brnyxx · GitHub · ⭐ 2 · 2026-09-18</sub><br>Browser-use layer for Claude Code, Codex, and other MCP clients where Jev picks the operation and target element each step, measured 7-8x faster than browser-use on Wikipedia and Google Flights tasks.<br><sub><b>How it uses Jev:</b> One ~300 ms round trip per step; the calling agent plans, supplies text, and takes over on escalation.</sub><br><sub>Also: <a href="https://brnyxx.github.io/jev-ra/">site</a> · <a href="https://brnyxx.github.io/jev-ra">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/sightmap/jev-turbo"><img src="https://raw.githubusercontent.com/sightmap/jev-turbo/main/docs/demo.gif" alt="jev-turbo" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/sightmap/jev-turbo">jev-turbo</a></b><br><sub>sightmap · GitHub · ⭐ 2 · 2026-09-17</sub><br>Go browser agent where Jev picks every step from a short list of named page actions and says whether the goal is met, run with and without a site map to measure what the map changes.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/coco-research/jev-use"><img src="https://raw.githubusercontent.com/coco-research/jev-use/main/docs/readme/hero-dark.png" alt="jev-use" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/coco-research/jev-use">jev-use</a></b><br><sub>coco-research · GitHub · ⭐ 2 · 2026-09-20</sub><br>Pre-alpha voice control layer for macOS in Rust and Tauri that reads apps through the accessibility tree and acts on spoken goals, running locally.<br><sub><b>How it uses Jev:</b> Jev is the fallback decision layer rather than the router, behind a local command-or-dictation split.</sub></td>
</tr>
<tr>
<td width="260" valign="top"></td>
<td valign="top"><b><a href="https://x.com/EvanLing888/status/2101175502396641613">Jev vs Chrome DevTools MCP posting</a></b><br><sub>EvanLing888 · X · ▶ 92 · 2026-09-19</sub><br>Chinese comparison of publishing a social post via a Jev-driven browser agent (about 33 seconds, 2 actions, verified) versus Chrome DevTools MCP (about 196 seconds, input mistakes and duplicated content).</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/hua-bang/pulse-agent/tree/master/apps/canvas-workspace/src/plugins/main/webview-page-control/page-run"><img src="https://raw.githubusercontent.com/hua-bang/pulse-agent/master/architecture/en/pulse-canvas-engine.svg" alt="Pulse Agent page-run" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/hua-bang/pulse-agent/tree/master/apps/canvas-workspace/src/plugins/main/webview-page-control/page-run">Pulse Agent page-run</a></b><br><sub>hua-bang · GitHub · ⭐ 29 repo · 2026-01-26</sub><br>Webview page-control loop in the Pulse Agent canvas workspace that reads a page snapshot and asks Jev for the next action plus whether the goal is done or the run is stuck.<br><sub><b>How it uses Jev:</b> One Choice over candidate page actions and two Nouls (goal_done, stuck) per step, within a 28,000-byte request budget.</sub><br><sub>Also: <a href="https://github.com/hua-bang/pulse-agent">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/andresguc1/hal-test/tree/main/research/jev-decision-provider"><img src="https://repository-images.githubusercontent.com/1122580217/88b6c18f-cde9-4f89-896f-7a5ae4de8539" alt="HAL-TEST Jev selector healing" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/andresguc1/hal-test/tree/main/research/jev-decision-provider">HAL-TEST Jev selector healing</a></b><br><sub>andresguc1 · GitHub · ⭐ 21 repo · 2025-12-25</sub><br>Proof of concept for HAL-TEST, a visual Playwright automation framework, that uses Jev to pick a replacement when a test selector breaks, then auto-heals, suggests or sends to human review based on confidence.<br><sub>Also: <a href="https://github.com/andresguc1/hal-test">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/zurfyx/jev-browser-skill"><img src="https://raw.githubusercontent.com/zurfyx/jev-browser-skill/main/docs/demo.gif" alt="Jev Browser Skill" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/zurfyx/jev-browser-skill">Jev Browser Skill</a></b><br><sub>zurfyx · GitHub · ⭐ 1 · 2026-09-19</sub><br>Reference browser skill for Claude Code and Codex in three short dependency-free files: name a site and a goal, and Jev clicks, types, and selects its way there, with a step-by-step explainer site.<br><sub><b>How it uses Jev:</b> Follows jev-ultrafast: one request per step picks the operation and target element.</sub><br><sub>Also: <a href="https://jev-browser.vercel.app">app</a> · <a href="https://jev-browser.vercel.app">app 2</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/xunaoo/status/2101940075072459255"><img src="https://pbs.twimg.com/media/HSuXK_yboAAatTI.jpg?name=orig" alt="Jev inside a browser agent" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/xunaoo/status/2101940075072459255">Jev inside a browser agent</a></b><br><sub>xunaoo · X · ♥ 1 · 2026-09-21</sub><br>Field note from adding Jev to a browser agent: one decision step went from 2 s to 0.2 s and ten model calls became two, but accuracy dropped 6 points.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/xinwang-nwpu/jev-mobile"><img src="https://raw.githubusercontent.com/xinwang-nwpu/jev-mobile/main/docx/demo.gif" alt="jev-mobile" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/xinwang-nwpu/jev-mobile">jev-mobile</a></b><br><sub>xinwang-nwpu · GitHub · ⭐ 1 · 2026-09-21</sub><br>Android automation agent that makes one Jev request per step over the accessibility tree to pick both the action and the target element, runs it over ADB, and checks in parallel whether the goal is done.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/krw82/jev-playwright-mcp"><img src="https://opengraph.githubassets.com/1/krw82/jev-playwright-mcp" alt="jev-playwright-mcp" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/krw82/jev-playwright-mcp">jev-playwright-mcp</a></b><br><sub>krw82 · GitHub · ⭐ 1 · 2026-09-17</sub><br>Drop-in proxy for Playwright MCP that keeps the same tools and adds Jev page-state triage (login wall, captcha, paywall), prompt-injection shielding, goal-based snapshot pruning and risky-action gating.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/ElshinQ/jevaluate"><img src="https://opengraph.githubassets.com/1/ElshinQ/jevaluate" alt="Jevaluate" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/ElshinQ/jevaluate">Jevaluate</a></b><br><sub>ElshinQ · GitHub · ⭐ 1 · 2026-09-19</sub><br>Tests a web app like a person: Jev picks each next click from a short list and stops for a human below 80% confidence, while DeepSeek vision checks each page screenshot; includes eval scripts, a UI text judge and an agent skill.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/dtduc-git/jevnav"><img src="https://raw.githubusercontent.com/dtduc-git/jevnav/main/docs/architecture.png" alt="jevnav" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/dtduc-git/jevnav">jevnav</a></b><br><sub>dtduc-git · GitHub · ⭐ 1 · 2026-09-21</sub><br>Browser automation for coding agents that returns page structure and computed styles as facts, has Jev pick each element with a calibrated probability, gates risky actions and replays whole runs offline in CI.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/Divine_machine/status/2102206020504224249"><img src="https://pbs.twimg.com/media/HSw6tlNXMAE6g7d.jpg?name=orig" alt="Jev Desktop" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/Divine_machine/status/2102206020504224249">Jev Desktop</a></b><br><sub>Divine_machine · X · ▶ 48 · 2026-09-22</sub><br>Open-source Windows computer-use loop: an LLM sets the goal, Jev Desktop reads app state through UI Automation, Jev picks each action and the driver executes it with no LLM turn between clicks.<br><sub>Also: <a href="https://github.com/jacks3tr/jev-desktop">repo</a> · <a href="https://github.com/jacks3tr/jev-desktop">project</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/kernel/browser-loop/tree/main/packages/browser-loop/examples/jev-system-one"><img src="https://opengraph.githubassets.com/1/kernel/browser-loop" alt="Browser Loop Jev agent" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/kernel/browser-loop/tree/main/packages/browser-loop/examples/jev-system-one">Browser Loop Jev agent</a></b><br><sub>kernel · GitHub · ⭐ 10 repo · 2026-04-18</sub><br>Example browser-agent loop for Kernel cloud browsers where Jev picks the operation and target from page-specific click, type, select, scroll and wait candidates each step.<br><sub><b>How it uses Jev:</b> Speculative operation and target Choices in one request, with DONE and BLOCKED as explicit options and a small text model only for typed values.</sub><br><sub>Also: <a href="https://www.kernel.sh">app</a> · <a href="https://github.com/kernel/browser-loop">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/silbercue/public-browser/blob/master/examples/jev-loop.mjs"><img src="https://raw.githubusercontent.com/Silbercue/public-browser/master/.github/assets/benchmark-2026-09-light.svg" alt="Public Browser Jev loop" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/silbercue/public-browser/blob/master/examples/jev-loop.mjs">Public Browser Jev loop</a></b><br><sub>Silbercue · GitHub · ⭐ 10 repo · 2026-04-07</sub><br>Example loop on the Public Browser Chrome library in which one Jev call per step picks the next action from the page's accessibility refs and gpt-4.1-nano writes text only for type actions, run on six benchmark cards.<br><sub>Also: <a href="https://github.com/Silbercue/public-browser">repo</a> · <a href="https://www.npmjs.com/package/public-browser">npm</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/JoshuaWangTW/RustBrowser/blob/master/src/jev.rs"><img src="https://opengraph.githubassets.com/1/JoshuaWangTW/RustBrowser" alt="RustBrowser Jev planner" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/JoshuaWangTW/RustBrowser/blob/master/src/jev.rs">RustBrowser Jev planner</a></b><br><sub>JoshuaWangTW · GitHub · ⭐ 10 repo · 2026-06-03</sub><br>Token-lean web fetcher and MCP server for LLMs whose planner asks Jev which operation and target to take next from the page's indexed action space.<br><sub><b>How it uses Jev:</b> Two Choice questions per request (operation and target) over up to 6,000 characters of page text, following the jev-ultrafast technique; answers are recommendations with confidence.</sub><br><sub>Also: <a href="https://github.com/JoshuaWangTW/RustBrowser">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/SomeshSampat2/android-control/tree/main/src/android_mcp/jev"><img src="https://opengraph.githubassets.com/1/SomeshSampat2/android-control" alt="Android Control Jev fast mode" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/SomeshSampat2/android-control/tree/main/src/android_mcp/jev">Android Control Jev fast mode</a></b><br><sub>SomeshSampat2 · GitHub · ⭐ 8 repo · 2026-04-11</sub><br>MCP server that lets AI assistants control Android devices, with a Jev fast mode that drives goals step by step, taps elements by description and answers yes/no questions about the screen in ~0.3 s.<br><sub><b>How it uses Jev:</b> Jev picks among code-supplied on-screen candidates, so it cannot invent element names or coordinates.</sub><br><sub>Also: <a href="https://github.com/SomeshSampat2/android-control">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/glim-sh/cuttle/tree/main/packages/cuttle/internal/jev"><img src="https://opengraph.githubassets.com/1/glim-sh/cuttle" alt="cuttle jev-browse" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/glim-sh/cuttle/tree/main/packages/cuttle/internal/jev">cuttle jev-browse</a></b><br><sub>glim-sh · GitHub · ⭐ 7 repo · 2026-07-09</sub><br>Experimental <code>cuttle jev-browse</code> mode of the cuttle stealth agent browser that walks toward a task one step at a time, with Jev choosing the next element to act on instead of an LLM.<br><sub><b>How it uses Jev:</b> One decision per page snapshot over the visible elements, executed with the bundled playwright-cli; stops when done, blocked or out of steps.</sub><br><sub>Also: <a href="https://github.com/glim-sh/cuttle">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/dttxorg/deepseekeyes/tree/main/src/jev"><img src="https://raw.githubusercontent.com/dttxorg/deepseekeyes/main/assets/deepseekeyes-banner.png" alt="DeepSeekEyes Jev control" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/dttxorg/deepseekeyes/tree/main/src/jev">DeepSeekEyes Jev control</a></b><br><sub>dttxorg · GitHub · ⭐ 7 repo · 2026-08-14</sub><br>Optional Jev control layer in DeepSeekEyes, a vision and computer-use runtime for DeepSeek Harness: Jev picks the next operation and semantic target in browser or native apps while DeepSeekEyes executes and verifies.<br><sub><b>How it uses Jev:</b> Each step is re-observed against the latest stateId; typed text comes from prepared slots, and low-confidence or risky actions stop for escalation.</sub><br><sub>Also: <a href="https://github.com/dttxorg/deepseekeyes">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/kyleslight/shun/blob/main/src/main/jev-client.ts"><img src="https://raw.githubusercontent.com/kyleslight/shun/main/resources/screenshot-main.png" alt="Shun computer-use acceleration" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/kyleslight/shun/blob/main/src/main/jev-client.ts">Shun computer-use acceleration</a></b><br><sub>kyleslight · GitHub · ⭐ 6 repo · 2026-08-21</sub><br>Computer-use acceleration in Shun, a local-first desktop coding harness for consumer-GPU models, that routes action choices to Jev through TypeSafe, Vercel AI Gateway or OpenRouter when a credential exists.<br><sub><b>How it uses Jev:</b> Jev picks the next action and judges completion, gated by minimum action and completion confidences, with bounded steps and timeouts.</sub><br><sub>Also: <a href="https://shunagent.com">app</a> · <a href="https://github.com/kyleslight/shun">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/eriestra/browser-use-olympics"><img src="https://opengraph.githubassets.com/1/eriestra/browser-use-olympics" alt="Browser Use Olympics" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/eriestra/browser-use-olympics">Browser Use Olympics</a></b><br><sub>eriestra · GitHub · 2026-09-17</sub><br>Benchmark for browser-using agents with one prompt, five events and a server-side clock, plus almond-fastloop, a ~200-line dependency-free computer-use loop where Jev picks the next action from Chrome DevTools state.<br><sub>Also: <a href="https://sites.almond.build/browser-use-olympics/">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/phanngoc/browser-ai"><img src="https://opengraph.githubassets.com/1/phanngoc/browser-ai" alt="browser-ai" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/phanngoc/browser-ai">browser-ai</a></b><br><sub>phanngoc · GitHub · 2026-09-19</sub><br>Stdlib-only Go browser agent that drives Chrome over CDP, launched over a pipe or attached to your real browser, where Jev picks each action from an indexed action space and a small LLM only types field values.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/aryaminus/cua"><img src="https://opengraph.githubassets.com/1/aryaminus/cua" alt="cua" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/aryaminus/cua">cua</a></b><br><sub>aryaminus · GitHub · 2026-09-18</sub><br>Computer-use system where an LLM discovers a UI flow once and compiles it into a typed artifact that replays deterministically with no model; Jev, via OpenRouter Decisions, flags when discovery is stuck.<br><sub>Also: <a href="https://cua-aryaminus.netlify.app">site</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"></td>
<td valign="top"><b><a href="https://www.xiaohongshu.com/explore/6aaf844a000000001103379c">CUA + Jev computer control</a></b><br><sub>北京月薪5k · X · 2026-09-20</sub><br>Chinese video note showing computer control driven by the open-source Cua agent with Jev making the decisions, which the author says is cheaper than Codex computer use.</td>
</tr>
<tr>
<td width="260" valign="top"></td>
<td valign="top"><b><a href="https://cua.ai/docs/how-to-guides/driver/jev-use">Cua jev-use</a></b><br><sub>Cua · Article</sub><br>Bounded computer use where a Choice picks one of the actions the app exposes, or abstains, and the driver executes it.<br><sub>Also: <a href="https://github.com/trycua/cua">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/phd-peter/ego-jev"><img src="https://opengraph.githubassets.com/1/phd-peter/ego-jev" alt="ego-jev" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/phd-peter/ego-jev">ego-jev</a></b><br><sub>phd-peter · GitHub · 2026-09-18</sub><br>Bounded browser loop joining ego-lite browser control with Jev, which may pick only a supported operation and an opaque target from the current page snapshot, never selectors or coordinates.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Tom-R-Main/Footwork"><img src="https://opengraph.githubassets.com/1/Tom-R-Main/Footwork" alt="Footwork" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Tom-R-Main/Footwork">Footwork</a></b><br><sub>Tom-R-Main · GitHub · 2026-09-21</sub><br>Dual-process browser agent that puts fast Jev System 1 decisions in front of browser-use's deliberate LLM loop, with a code-owned arbiter, evidence-based verification and Rust hot paths.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/mhingston/jev-agent-browser"><img src="https://opengraph.githubassets.com/1/mhingston/jev-agent-browser" alt="Jev Agent Browser (mhingston)" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/mhingston/jev-agent-browser">Jev Agent Browser (mhingston)</a></b><br><sub>mhingston · GitHub · 2026-09-19</sub><br>TypeScript sidecar that gives Jev a compact accessibility snapshot and a goal to pick the next browser action, validates it in code and has Vercel's agent-browser run it, via TypeSafe, AI Gateway or Cloudflare.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/KesavanKing/jev-browser"><img src="https://opengraph.githubassets.com/1/KesavanKing/jev-browser" alt="Jev Browser" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/KesavanKing/jev-browser">Jev Browser</a></b><br><sub>KesavanKing · GitHub · 2026-09-17</sub><br>Local browser automation UI that turns a URL and a goal into bounded actions: Jev picks click, type, select, wait, done or blocked on observed targets, and a text model is used only for field values.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/abeatrix/cline-plugin-jev-browser"><img src="https://opengraph.githubassets.com/1/abeatrix/cline-plugin-jev-browser" alt="Jev Browser for Cline" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/abeatrix/cline-plugin-jev-browser">Jev Browser for Cline</a></b><br><sub>abeatrix · GitHub · 2026-09-18</sub><br>Cline plugin that gives the agent an isolated Playwright Chromium browser and delegates bounded browser goals to Jev through Vercel AI Gateway, with automatic before and after screenshots.<br><sub><b>How it uses Jev:</b> One evaluation picks an operation and target together from indexed DOM targets, compared against scroll, wait and stop; a text model supplies typed text.</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/jal-co/jev-agent-browser"><img src="https://opengraph.githubassets.com/1/jal-co/jev-agent-browser" alt="jev-agent-browser" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/jal-co/jev-agent-browser">jev-agent-browser</a></b><br><sub>jal-co · GitHub · 2026-09-17</sub><br>Adapter where Jev chooses the next browser operation and target and Agent Browser executes it, supporting HTML and ARIA controls, text entry, selects, scrolling and waits, with a JSON-lines server for Pi.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/MahmoudAdelbghany/jev-browser"><img src="https://opengraph.githubassets.com/1/MahmoudAdelbghany/jev-browser" alt="jev-browser" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/MahmoudAdelbghany/jev-browser">jev-browser</a></b><br><sub>MahmoudAdelbghany · GitHub · 2026-09-17</sub><br>Browser MCP server where Jev picks the next action in ~300 ms and the driving agent only steps in on escalations; 1.5x faster and 1.6x cheaper than Playwright MCP at the same accuracy on a 12-task suite.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/imanshu03/jev-browser-use"><img src="https://opengraph.githubassets.com/1/imanshu03/jev-browser-use" alt="jev-browser-use" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/imanshu03/jev-browser-use">jev-browser-use</a></b><br><sub>imanshu03 · GitHub · 2026-09-21</sub><br>Browser agent that runs plain-language tasks over CDP, Chromium, or Vercel's agent-browser, with Jev choosing operations, targets, and text values and code checking confidence and page freshness before acting.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/eronmmer/jev-cua"><img src="https://opengraph.githubassets.com/1/eronmmer/jev-cua" alt="jev-cua" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/eronmmer/jev-cua">jev-cua</a></b><br><sub>eronmmer · GitHub · 2026-09-20</sub><br>Local Codex and Waku plugin for guarded Mac computer use that launches apps, reads Accessibility state, clicks, types and scrolls, with a faster compiled path for reviewed browser flows.<br><sub><b>How it uses Jev:</b> Jev handles fast-path policy decisions, with approval gates on risky keys and at-most-once execution.</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/rashedInt32/jev-reach"><img src="https://opengraph.githubassets.com/1/rashedInt32/jev-reach" alt="jev-reach" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/rashedInt32/jev-reach">jev-reach</a></b><br><sub>rashedInt32 · GitHub · 2026-09-20</sub><br>Adds one tool, reach, to chrome-devtools-mcp: Jev walks the browser to the spot you want by picking each click in about 300 ms, so the agent makes one devtools call there instead of one turn per click.<br><sub>Also: <a href="https://www.reddit.com/r/ClaudeCode/comments/1wljx18/i_gave_chromedevtoolsmcp_one_more_tool_so_my/">demo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/msalvalaggio/jev-reflex"><img src="https://opengraph.githubassets.com/1/msalvalaggio/jev-reflex" alt="jev-reflex" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/msalvalaggio/jev-reflex">jev-reflex</a></b><br><sub>msalvalaggio · GitHub · 2026-09-18</sub><br>MCP server that lets Claude hand a whole browser task to Jev, which makes each click, type or select decision in about 100 ms while Claude plans and verifies.<br><sub><b>How it uses Jev:</b> Each step is a Choice over the page's elements, so it cannot pick an element that is not on the page.</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Xopher00/jevdevice"><img src="https://opengraph.githubassets.com/1/Xopher00/jevdevice" alt="jevdevice" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Xopher00/jevdevice">jevdevice</a></b><br><sub>Xopher00 · GitHub · 2026-09-19</sub><br>MCP harness that turns a plain-language goal into exactly one verified action on an Android phone over adb or a local shell, with Jev (or local Laya) picking from live-discovered candidates or declining.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/laihenyi/pi-Jev-browser"><img src="https://opengraph.githubassets.com/1/laihenyi/pi-Jev-browser" alt="Pi Jev Browser" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/laihenyi/pi-Jev-browser">Pi Jev Browser</a></b><br><sub>laihenyi · GitHub · 2026-09-19</sub><br>Browser and macOS desktop agent for Pi where Jev chooses each action from a structured page observation, never a screenshot, in a bounded loop with isolated Playwright tools, stuck detection and hand-back to a human.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/hitakshia/solari-reflex"><img src="https://opengraph.githubassets.com/1/hitakshia/solari-reflex" alt="solari-reflex" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/hitakshia/solari-reflex">solari-reflex</a></b><br><sub>hitakshia · GitHub · 2026-09-18</sub><br>Speed layer for computer use on Solari browsers and Linux desktops: each step is one structured observation, one Jev decision and one verified action, with no screenshots.<br><sub><b>How it uses Jev:</b> A Stripe Checkout run took 60.2 s and $0.011 versus 194.9 s for Codex through Solari's MCP; 30 expenses in LibreOffice Calc took 24.2 s.</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Clawbuilders/web-qa-jev-agent"><img src="https://opengraph.githubassets.com/1/Clawbuilders/web-qa-jev-agent" alt="web-qa-jev-agent" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Clawbuilders/web-qa-jev-agent">web-qa-jev-agent</a></b><br><sub>Clawbuilders · GitHub · 2026-09-18</sub><br>Cloudflare Worker that crawls a web app like a QA tester with Browser Rendering, triages findings with Jev, confirms real ones with a vision model and files deduplicated GitHub issues.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://yappy.biz/jev/"><img src="https://yappy.biz/assets/research/yappy-vs-heyclicky.png" alt="Yappy" width="240"></a></td>
<td valign="top"><b><a href="https://yappy.biz/jev/">Yappy</a></b><br><sub>Mitosis Labs · App · 2026-09-19</sub><br>Voice agent for macOS that uses Jev to pick each computer-use step and calls a chat model only for typing; measured 1m 54s and $0.24 on a job application versus a competitor's 13m 14s and $4.24.<br><sub><b>How it uses Jev:</b> Each step, Jev picks the operation and target control from the window's accessibility table; the full agent takes over when confidence drops.</sub><br><sub>Also: <a href="https://yappy.biz">app</a></sub></td>
</tr>
</table>

Missing something? [Suggest a resource](https://github.com/Li-Evan/awesome-jev/issues/new/choose).
