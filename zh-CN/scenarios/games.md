# 🎮 游戏与互动

[English](https://github.com/Li-Evan/awesome-jev/blob/main/scenarios/games.md) · **简体中文**

会玩游戏的 agent、实时决策，以及好玩的互动演示。共 276 条，按社区热度排序。

[← 返回 Awesome Jev](https://github.com/Li-Evan/awesome-jev/blob/main/README.zh-CN.md#按场景浏览)

<table>
<tr>
<td width="260" valign="top"><a href="https://x.com/CompleteSkeptic/status/2099925687465570372"><img src="https://pbs.twimg.com/amplify_video_thumb/2099924592534183936/img/hBGk8j8MRxBgPyg9.jpg" alt="Jev 玩 Doom" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/CompleteSkeptic/status/2099925687465570372">Jev 玩 Doom</a></b><br><sub>CompleteSkeptic · X · ♥ 5k · 2026-09-15</sub><br>TypeSafe 的发布演示：Jev 根据结构化游戏状态实时玩 Doom，每秒约 10 次调用，每小时约 $7。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/CompleteSkeptic/status/2099925688925184171"><img src="https://pbs.twimg.com/amplify_video_thumb/2099924665515012096/img/Q3mdVD5jfOZOkMww.jpg" alt="维基百科竞速" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/CompleteSkeptic/status/2099925688925184171">维基百科竞速</a></b><br><sub>CompleteSkeptic · X · ♥ 2.6k · 2026-09-15</sub><br>发布演示：Jev 只通过链接从一个维基百科页面跑到另一个，每一步都要在数百到数千个链接中做选择。<br><sub><b>Jev 用法:</b> 对页面链接做高基数 Choice；候选集超过 255 个时分两阶段处理。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/fhshaik/typesafe-mario"><img src="https://external-preview.redd.it/bzVydG83cHlodXBoMZE7fOmaTIl8CDi0AASExP3Al1xQRlZJ2gAIQDJfa5Lr.png?format=pjpg&amp;auto=webp&amp;s=2ba386e6d1e858b09755e0c4f9ecbb8adbfc0c15" alt="typesafe-mario" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/fhshaik/typesafe-mario">typesafe-mario</a></b><br><sub>fhshaik · GitHub · ⭐ 338 · 2026-09-16</sub><br>用一个决定手柄动作的 Choice、一个跳跃 Noul 和一个危险 Score 来玩 Super Mario。<br><sub>相关: <a href="https://www.reddit.com/r/typesafe_ai/comments/1whrm0q/jev_playing_mario_bros_no_prior_training_wow/">discussion</a> · <a href="https://x.com/faadilhshaik/status/2100086301894881578">demo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/aimlapi/status/2100372930282573876"><img src="https://pbs.twimg.com/amplify_video_thumb/2100371773275406336/img/NmHPy0pAprSsC6Gi.jpg" alt="Jev 对战 Fable 5.1 和 GPT-6 Astra 下棋" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/aimlapi/status/2100372930282573876">Jev 对战 Fable 5.1 和 GPT-6 Astra 下棋</a></b><br><sub>aimlapi · X · ♥ 2.3k · 2026-09-16</sub><br>5+0 快棋，每步一次 API 调用：Jev 对 Fable 5.1 子力落后，但凭约 2.6 秒一步的速度赢在对手超时；对 GPT-6 Astra 则在 18 步内被将死。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://www.spritefusion.com/blog/generating-game-level-in-real-time-with-jev"><img src="https://www.spritefusion.com/blog/generating-game-level-in-real-time-with-jev/jev-terrain-generation.png" alt="用 Jev 实时生成游戏关卡" width="240"></a></td>
<td valign="top"><b><a href="https://www.spritefusion.com/blog/generating-game-level-in-real-time-with-jev">用 Jev 实时生成游戏关卡</a></b><br><sub>Hugo Duprez (Sprite Fusion) · 文章 · ♥ 2.8k · 2026-09-18</sub><br>无尽平台跳跃游戏，地形根据游戏状态实时生成：Jev 决定每一段的宽度、间隙、高度和图块类型，由游戏代码放置图块。<br><sub><b>Jev 用法:</b> 每段地形做结构化的 Choice 和 Score 决策；放置逻辑留在代码里。</sub><br><sub>相关: <a href="https://www.reddit.com/r/aigamedev/comments/1wjrgs1/using_jev_to_generate_game_levels_in_real_time/">discussion</a> · <a href="https://x.com/HugoDuprez/status/2100953089003921543">demo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/_MaxBlade/status/2100634359099232678"><img src="https://pbs.twimg.com/amplify_video_thumb/2100633400717565952/img/KlytLNSLCQA-yY2E.jpg" alt="Jev 玩 Subway Surfers" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/_MaxBlade/status/2100634359099232678">Jev 玩 Subway Surfers</a></b><br><sub>_MaxBlade · X · ♥ 4.1k · 2026-09-17</sub><br>Jev 以超越人类的速度玩 Subway Surfers，包括同时开 50 局，整个过程花费不到一美分。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/maubaron/status/2100738237237002706"><img src="https://pbs.twimg.com/amplify_video_thumb/2100731665513349120/img/j4DcB9CxjN8DX4qe.jpg" alt="Jev 玩 Smash Bros." width="240"></a></td>
<td valign="top"><b><a href="https://x.com/maubaron/status/2100738237237002706">Jev 玩 Smash Bros.</a></b><br><sub>maubaron · X · ♥ 3.7k · 2026-09-18</sub><br>Jev 在一场 Smash Bros. 对局中操控全部四个角色和自己对打，每个动作在不到一秒内选出，总共用了 22M token，只花了几美分。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/riku720720/status/2100738087584481657"><img src="https://pbs.twimg.com/amplify_video_thumb/2100732918536773632/img/3ch1UQy_Wpfs56N5.jpg" alt="情绪元胞自动机" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/riku720720/status/2100738087584481657">情绪元胞自动机</a></b><br><sub>riku720720 · X · ♥ 673 · 2026-09-18</sub><br>元胞自动机模拟：并行运行大量 Jev 调用，模拟每个人的情绪如何随邻居的情绪变化，让愤怒和恐慌在网格中扩散。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/redp314/status/2100489858951073858"><img src="https://pbs.twimg.com/amplify_video_thumb/2100479486382809088/img/r6daGpDnvsCr3LyL.jpg" alt="自己还原的魔方" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/redp314/status/2100489858951073858">自己还原的魔方</a></b><br><sub>redp314 · X · ♥ 717 · 2026-09-17</sub><br>魔方求解器：把初级解法写进代码，Jev 在每一步观察魔方并判断当前属于哪种情形，用 94 步、约 4 秒模型时间还原魔方。<br><sub><b>Jev 用法:</b> 每一步对初级解法的各种情形做一个 Choice；代码校验每次选择。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/buddy/minesweeper"><img src="https://assets.buddy.works/launch/run-in-sandbox.svg" alt="扫雷 AI agent 基准测试" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/buddy/minesweeper">扫雷 AI agent 基准测试</a></b><br><sub>buddy · GitHub · ⭐ 14 · 2026-09-21</sub><br>浏览器基准测试：最多九个模型在同一时钟下玩同一个固定种子的扫雷棋盘，按翻开格数、用时和 token 成本评分，Jev 是其中一路参赛者。<br><sub><b>Jev 用法:</b> Jev agent 为每个边界格子问一个 Noul，判断它藏雷的概率，低于 0.07 就翻开，高于 0.85 就插旗。</sub><br><sub>相关: <a href="https://github.com/buddy/minesweeper/blob/main/js/agents/jev-agent.js">code</a> · <a href="https://x.com/useBuddy/status/2102039447676014933">demo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/nathanwchan/status/2100096510436475293"><img src="https://pbs.twimg.com/media/HSUJzMBaoAAfzW9.jpg?name=orig" alt="Almost Certain" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/nathanwchan/status/2100096510436475293">Almost Certain</a></b><br><sub>nathanwchan · X · ♥ 495 · 2026-09-16</sub><br>猜测游戏：面对一条随机描述，你要预测 AI 会有多大把握，目标是猜中指定的概率区间。<br><sub>相关: <a href="https://almost-certain.vercel.app">app</a> · <a href="https://almost-certain.vercel.app">project</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://askjev.ai"><img src="https://fastidious-oyster-877.convex.site/og.png" alt="Ask Jev" width="240"></a></td>
<td valign="top"><b><a href="https://askjev.ai">Ask Jev</a></b><br><sub>Ask Jev · 应用 · ♥ 515</sub><br>一面公开留言墙：任何人都可以用三到十五个词问 Jev 一个问题，得到的不是回答而是判断：是、否或看情况，外加情绪、话题以及是否适合上墙。<br><sub><b>Jev 用法:</b> 每个提问约 100 毫秒完成判断；Convex 实时存储每一条结论。</sub><br><sub>相关: <a href="https://x.com/waynesutton/status/2100487878992388279">demo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/vansitha12/status/2100937772030927216"><img src="https://pbs.twimg.com/amplify_video_thumb/2100933946947272704/img/AKeg-wfMbeMHzL-d.jpg" alt="Jev&#x27;s Dojo" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/vansitha12/status/2100937772030927216">Jev's Dojo</a></b><br><sub>vansitha12 · X · ♥ 60 · 2026-09-18</sub><br>浏览器格斗游戏：Jev 学习你的习惯，在你出招前预测你的下一步，还会吐槽你的打法。<br><sub>相关: <a href="https://www.jevsdojo.xyz/">app</a> · <a href="https://jevsdojo.xyz">project</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://www.reddit.com/r/singularity/comments/1wjiphh/new_decision_model_jev_developed_by_cocreator_of/"><img src="https://external-preview.redd.it/dHpuMHpkNG95N3FoMUucEQdQZmbqjqbId0_QLFh_fksCLNqhu15wWNNKVSjG.png?format=pjpg&amp;auto=webp&amp;s=b5c4f1b9a4864434b81c83de0551e7588f03003c" alt="Jev 玩 Subway Surfers" width="240"></a></td>
<td valign="top"><b><a href="https://www.reddit.com/r/singularity/comments/1wjiphh/new_decision_model_jev_developed_by_cocreator_of/">Jev 玩 Subway Surfers</a></b><br><sub>_MaxBlade · Reddit · ▲ 548 · 2026-09-18</sub><br>Jev 实时玩 Subway Surfers 的视频片段，转载自开发者在 X 上的帖子。<br><sub>相关: <a href="https://x.com/_MaxBlade/status/2100634359099232678">demo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/marcus_lowe/status/2100315518930661861"><img src="https://pbs.twimg.com/amplify_video_thumb/2100315393860730880/img/u0iH2SHQny2hkd4Q.jpg" alt="Jev 玩俄罗斯方块" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/marcus_lowe/status/2100315518930661861">Jev 玩俄罗斯方块</a></b><br><sub>marcus_lowe · X · ♥ 980 · 2026-09-16</sub><br>俄罗斯方块演示：Jev 选择落点的速度快到能在方块自然下落之前就把它们推下去。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/studioigor/jev-rts"><img src="https://raw.githubusercontent.com/studioigor/jev-rts-assets/main/Documentation~/preview.jpg" alt="JEV RTS" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/studioigor/jev-rts">JEV RTS</a></b><br><sub>studioigor · GitHub · ⭐ 11 · 2026-09-20</sub><br>Unity 即时战略游戏：每个单位的行动和路线、敌方指挥官的战略都来自 Jev，没有暗藏本地 AI 兜底。<br><sub>相关: <a href="https://www.youtube.com/watch?v=6_cCufO5c9U">video</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"></td>
<td valign="top"><b><a href="https://x.com/mizchi/status/2100615604386562430">Jev 对战 Sonnet 下棋</a></b><br><sub>mizchi · X · ♥ 592 · 2026-09-17</sub><br>Sonnet 与 Jev 的国际象棋对局，Jev 赢下了每一盘。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/chenchengpro/status/2100516953496670430"><img src="https://pbs.twimg.com/amplify_video_thumb/2100516335155646464/img/pow4ZDKeRwkBVSvy.jpg" alt="Jev 玩贪吃蛇" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/chenchengpro/status/2100516953496670430">Jev 玩贪吃蛇</a></b><br><sub>chenchengpro · X · ♥ 283 · 2026-09-17</sub><br>每一步都去问 Jev 的贪吃蛇；200 次请求花费 $0.02，所以 $1 大约能买一万步。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://www.reddit.com/r/accelerate/comments/1whr9gv/jev_playing_doom_in_real_time_with_10_decisions/"><img src="https://external-preview.redd.it/eGhsOTY3NGQ2dHBoMZi4Fo1lWSh3LK2iCYvooC2NogiYum3mcqor0WTcJDpX.png?auto=webp&amp;s=c5307e475e85da6232452955c9b30893dfbf4a15" alt="Jev 玩 DOOM" width="240"></a></td>
<td valign="top"><b><a href="https://www.reddit.com/r/accelerate/comments/1whr9gv/jev_playing_doom_in_real_time_with_10_decisions/">Jev 玩 DOOM</a></b><br><sub>Difficult-Inside-576 · Reddit · ▲ 386 · 2026-09-16</sub><br>Jev 以每秒 10 次决策的速度实时玩 DOOM 的视频片段，运行成本约每小时 $7。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/Blueprint_Biz/status/2100728329003303146"><img src="https://pbs.twimg.com/amplify_video_thumb/2100728041320189952/img/ZYUxcdFhFprJlPuc.jpg" alt="Jev 对 Jev 玩二十一点" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/Blueprint_Biz/status/2100728329003303146">Jev 对 Jev 玩二十一点</a></b><br><sub>Blueprint_Biz · X · ♥ 15 · 2026-09-17</sub><br>二十一点演示：一个 Jev 记牌并一路赢钱，直到另一个扮演赌场主管的 Jev 出面干预。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://jev-plays-pokemon.standardagents.ai"><img src="https://jev-plays-pokemon.standardagents.ai/og.png" alt="Jev 玩 Pokemon Red" width="240"></a></td>
<td valign="top"><b><a href="https://jev-plays-pokemon.standardagents.ai">Jev 玩 Pokemon Red</a></b><br><sub>0xBOYD · 应用 · ♥ 386</sub><br>Jev 玩 Pokemon Red 的直播，每一次按键都由 Jev 选择；经过 8,000+ 次决策、花费 $1.21 后，它击败 Brock，拿到第一枚道馆徽章。<br><sub><b>Jev 用法:</b> 游戏决策由 Jev 做出；游戏日志监控和实时 harness 是用 Opus 5 搭建的。</sub><br><sub>相关: <a href="https://x.com/0xBOYD/status/2100539883836018697">demo</a> · <a href="https://www.reddit.com/r/singularity/comments/1wjvh14/jev_is_amazing_im_letting_it_play_pokemon_red/">discussion</a> · <a href="https://www.npmjs.com/package/jev-plays-pokemon">package</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/jarrodwatts/status/2100674934582263895"><img src="https://pbs.twimg.com/amplify_video_thumb/2100674773843865600/img/dh9A-GH0WV0f-UNj.jpg" alt="Jev 玩 Minecraft" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/jarrodwatts/status/2100674934582263895">Jev 玩 Minecraft</a></b><br><sub>jarrodwatts · X · ♥ 271 · 2026-09-17</sub><br>全天候 Twitch 直播，Jev 一次做一个决策，尝试在 Minecraft 里击败末影龙。<br><sub>相关: <a href="https://twitch.tv/jevplaysminecraft">stream</a> · <a href="https://twitch.tv/jevplaysminecraft">project</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/anshnanda/status/2100611596859093082"><img src="https://pbs.twimg.com/amplify_video_thumb/2100611414746644481/img/E5GtDSrVTj1b3VBq.jpg" alt="Jev 对战 3 个模型玩 Flappy Bird" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/anshnanda/status/2100611596859093082">Jev 对战 3 个模型玩 Flappy Bird</a></b><br><sub>anshnanda · X · ♥ 347 · 2026-09-17</sub><br>Jev 与另外三个 AI 模型同时玩 Flappy Bird 的比赛。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/10xmylife/status/2101302029385920530"><img src="https://pbs.twimg.com/amplify_video_thumb/2101300542144479232/img/TmWoHRrY8b_7Zvvj.jpg" alt="Codex + Jev 玩 Slay the Spire 2" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/10xmylife/status/2101302029385920530">Codex + Jev 玩 Slay the Spire 2</a></b><br><sub>10xmylife · X · ♥ 116 · 2026-09-19</sub><br>Codex 和 Jev 高速游玩 Slay the Spire 2 的直播，不过玩得不太好。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/nutlope/status/2101010773157761481"><img src="https://pbs.twimg.com/amplify_video_thumb/2101007875644506112/img/2KoYEIDaUkXehsRC.jpg" alt="Jev 对战 GLM 5.3 下棋" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/nutlope/status/2101010773157761481">Jev 对战 GLM 5.3 下棋</a></b><br><sub>nutlope · X · ♥ 320 · 2026-09-18</sub><br>Jev 与 GLM 5.3 的一盘棋：GLM 在 29 步内将死获胜，但 Jev 每步约 0.3 秒、不到 $0.0001，对方则约 5.8 秒、约 $0.008，整盘共花 24 美分。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/tubone24/status/2101895523674534374"><img src="https://pbs.twimg.com/amplify_video_thumb/2101298908085542912/img/Ho45fT01CQhB3ljm.jpg" alt="Jev Speed" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/tubone24/status/2101895523674534374">Jev Speed</a></b><br><sub>tubone24 · X · ♥ 167 · 2026-09-21</sub><br>卡牌游戏 Speed 的浏览器版，你要和一个由 Jev 驱动、会判断哪些牌能出的对手比拼速度，现已向公众开放。<br><sub>相关: <a href="https://jev-speed.tubone24.workers.dev/">app</a> · <a href="https://jev-speed.tubone24.workers.dev">project</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/inteligenciamilgrau/jevstudio"><img src="https://raw.githubusercontent.com/inteligenciamilgrau/jevstudio/main/docs/jevstudio.png" alt="Jev Studio (visual funnels)" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/inteligenciamilgrau/jevstudio">Jev Studio (visual funnels)</a></b><br><sub>inteligenciamilgrau · GitHub · ⭐ 4 · 2026-09-18</sub><br>葡萄牙语可视化工作台，用拖拽方式搭建 Jev 决策漏斗：每个节点向 Jev 提问，每个答案连到另一个节点或一个游戏动作，连线上实时显示概率。<br><sub>相关: <a href="https://www.youtube.com/watch?v=ViHD9Li_Bqk">video</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/Juris_Savos/status/2100989012966031417"><img src="https://pbs.twimg.com/amplify_video_thumb/2100987840268034048/img/Hmumsuz83I0DXXIE.jpg" alt="Jev 玩 Balatro" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/Juris_Savos/status/2100989012966031417">Jev 玩 Balatro</a></b><br><sub>Juris_Savos · X · ♥ 13 · 2026-09-18</sub><br>Balatro 对局：每一手 Jev 查看手牌、小丑牌和盲注，在约 200-500 毫秒 内决定出牌还是弃牌，过完底注后再去商店；打完一整局花费不到一美分。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/rmalde/minecraft-agent"><img src="https://opengraph.githubassets.com/1/rmalde/minecraft-agent" alt="Astra 与 JEV 的 Minecraft agent" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/rmalde/minecraft-agent">Astra 与 JEV 的 Minecraft agent</a></b><br><sub>rmalde · GitHub · ⭐ 489 · 2026-09-20</sub><br>Minecraft agent：由 GPT-6 Astra 或 GPT-5.6 Sol 做规划，Jev 通过 Mineflayer 在原版服务器上选择玩家的每个动作；作者经验证的最佳一局用 8 分 43.300 秒击杀末影龙。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/gokayfem/status/2101022590722810271"><img src="https://pbs.twimg.com/amplify_video_thumb/2101020230071803904/img/FWi7MqiT0DI2iQJ9.jpg" alt="鲸背上的城市" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/gokayfem/status/2101022590722810271">鲸背上的城市</a></b><br><sub>gokayfem · X · ♥ 265 · 2026-09-18</sub><br>一款关于让鲸背上的城市存续下去的决策游戏：GPT-6 Astra 设计世界，Jev 选择每一轮的行动，fal 上的 H3 Max Turbo 把这些决策变成 264 段视频。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/trungdq88/jev-tetris"><img src="https://raw.githubusercontent.com/trungdq88/jev-tetris/main/docs/battle.png" alt="jev-tetris" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/trungdq88/jev-tetris">jev-tetris</a></b><br><sub>trungdq88 · GitHub · ⭐ 12 · 2026-09-18</sub><br>实时俄罗斯方块对战：Jev 与 Claude Haiku 4.5、Gemini 3.8 Flash 或开放权重的 Laya 在相同的方块序列上对决，没赶上截止时间的方块会就地锁定。<br><sub><b>Jev 用法:</b> 每个方块一出现，就对列和旋转做一个 Choice。</sub><br><sub>相关: <a href="https://jev-tetris.vercel.app">app</a> · <a href="https://jev-tetris.vercel.app">app 2</a> · <a href="https://x.com/tdinh_me/status/2101958041986068848">demo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/PromptEngineer48/laya-vs-jev-arena"><img src="https://opengraph.githubassets.com/1/PromptEngineer48/laya-vs-jev-arena" alt="Laya vs Jev Arena" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/PromptEngineer48/laya-vs-jev-arena">Laya vs Jev Arena</a></b><br><sub>PromptEngineer48 · GitHub · ⭐ 18 · 2026-09-21</sub><br>本地竞技场：开源 Laya 模型和 Jev 在贪吃蛇中竞速、在 Mortal Kombat 风格的游戏中对打，两者回答相同的类型化问题，唯一的变量是模型本身。<br><sub>相关: <a href="https://www.youtube.com/watch?v=x1GFo1eG8d0">video</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"></td>
<td valign="top"><b><a href="https://www.reddit.com/r/singularity/comments/1wjv6hx/jev_playing_9_realtime_classic_games/">Jev Arena</a></b><br><sub>manubfr · Reddit · ▲ 127 · 2026-09-18</sub><br>网页竞技场：单个 Jev API 调用同时玩 9 款经典实时游戏，每小时 $1.80；作者后来把规模扩展到 27 款。<br><sub>相关: <a href="https://jev-arena.vercel.app">app</a> · <a href="https://jev-arena.vercel.app">project</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/shreypandya/status/2100606445758898287"><img src="https://pbs.twimg.com/amplify_video_thumb/2100605130869784576/img/gdGysXaHMdzFOU8W.jpg" alt="Jev 玩 Mario Kart 64" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/shreypandya/status/2100606445758898287">Jev 玩 Mario Kart 64</a></b><br><sub>shreypandya · X · ♥ 226 · 2026-09-17</sub><br>Jev 实时驾驶 Mario Kart 64。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://www.reddit.com/r/SideProject/comments/1wkzlsw/experiment_to_see_if_jev_is_smart/"><img src="https://external-preview.redd.it/OXdiNTBoNmd1anFoMZ9yYUbO4_b2NWc20y21iTTlRGVcwqsZGOj9Td6rgK0_.png?format=pjpg&amp;auto=webp&amp;s=b1c962a9492a48bffa46e1a6948904c96d3ac7db" alt="OuiJev" width="240"></a></td>
<td valign="top"><b><a href="https://www.reddit.com/r/SideProject/comments/1wkzlsw/experiment_to_see_if_jev_is_smart/">OuiJev</a></b><br><sub>MrCyclopede · Reddit · ▲ 98 · 2026-09-19</sub><br>小型网页玩具：你可以问 Jev 任何问题，但它只能回答是或否，用来探测模型到底知道什么。<br><sub>相关: <a href="https://ouijev.com">app</a> · <a href="https://ouijev.com">project</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/CharlieMolthrop/status/2100946286136406421"><img src="https://pbs.twimg.com/amplify_video_thumb/2100945687059869696/img/yQvtfBF64zQfczMI.jpg" alt="Whose Jev Is It Anyway?" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/CharlieMolthrop/status/2100946286136406421">Whose Jev Is It Anyway?</a></b><br><sub>CharlieMolthrop · X · ♥ 107 · 2026-09-18</sub><br>即兴喜剧游戏，用 Jev 当评委，像那档电视节目的主持人一样给玩家的即兴回应打分。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/_shubhankar/status/2101830589620056160"><img src="https://pbs.twimg.com/amplify_video_thumb/2101829435855147008/img/PfN38k2ZCauEwPNh.jpg" alt="用 Jev 玩 FIFA" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/_shubhankar/status/2101830589620056160">用 Jev 玩 FIFA</a></b><br><sub>_shubhankar · X · ♥ 64 · 2026-09-21</sub><br>足球游戏：每名球员大约每 150 毫秒 跑一次 Jev 循环，决定抢断、传球还是射门，以及速度和方向；解说和配乐也由 Jev 挑选。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/kmad/status/2100339921714323624"><img src="https://pbs.twimg.com/amplify_video_thumb/2100339415407017984/img/0d7rvi1ZoC0nAtJN.jpg" alt="Jev 驱动的 ViZDoom agent" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/kmad/status/2100339921714323624">Jev 驱动的 ViZDoom agent</a></b><br><sub>kmad · X · ♥ 16 · 2026-09-16</sub><br>由 Jev 通过两个决策通道驱动的 ViZDoom agent，导航每秒 5 次决策，战斗每秒 12 次；一次测试跑出 18 次击杀，之后卡在原地绕圈。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/joey_build/status/2100904864519770170"><img src="https://pbs.twimg.com/amplify_video_thumb/2100904739332399105/img/x3EZzH6sWlihnjqr.jpg" alt="Jev 玩 Pokémon Gold" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/joey_build/status/2100904864519770170">Jev 玩 Pokémon Gold</a></b><br><sub>joey_build · X · ♥ 3 · 2026-09-18</sub><br>尝试让 Jev 通过选择按键，在 Pokémon Gold（HGSS）里打通 Pokémon 联盟。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/webdevcody/jevs-fly"><img src="https://raw.githubusercontent.com/webdevcody/jevs-fly/main/screenshots/jevs-fly.png" alt="Jev&#x27;s Fly" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/webdevcody/jevs-fly">Jev's Fly</a></b><br><sub>webdevcody · GitHub · ⭐ 12 · 2026-09-19</sub><br>Three.js FPV 花园游戏：一只发光的苍蝇追猎四处游荡的哥布林，由 Jev 以每秒约五次的频率选择它的航向和俯冲。<br><sub><b>Jev 用法:</b> Jev 拿到目标的方位、目标在地平线以下的角度、视线遮挡物和安全爬升角度，然后选出飞行指令。</sub><br><sub>相关: <a href="https://www.youtube.com/watch?v=NGTOgJRawUs">video</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/Neel490/status/2101028527978020920"><img src="https://pbs.twimg.com/amplify_video_thumb/2101028423032287232/img/CPjw3sVj_6rRvJ__.jpg" alt="Jev 对战 OpenJev 的 FPS" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/Neel490/status/2101028527978020920">Jev 对战 OpenJev 的 FPS</a></b><br><sub>Neel490 · X · ♥ 71 · 2026-09-18</sub><br>浏览器里的第一人称射击游戏，Jev 对战 OpenJev，后者是一个在 SGLang 上运行 Qwen 的开源 Jev 兼容 API。<br><sub>相关: <a href="https://jev-vs-openjev.vercel.app/">app</a> · <a href="https://github.com/ekzhang/openjev-sglang">openjev</a> · <a href="https://jev-vs-openjev.vercel.app">project</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/raihankhan-rk/jevarena"><img src="https://pbs.twimg.com/amplify_video_thumb/2100951665260240896/img/b0cvD-p11tUYb0DC.jpg" alt="JevArena" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/raihankhan-rk/jevarena">JevArena</a></b><br><sub>raihankhan-rk · GitHub · ⭐ 2 · 2026-09-18</sub><br>观战演示：两个独立的 Jev agent 在各自的浏览器上下文里并排玩贪吃蛇，只通过点击带编号的方向按钮操作，每一步都实时显示概率。<br><sub>相关: <a href="https://x.com/raihankhan_rk/status/2100951738606035176">demo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://www.reddit.com/r/accelerate/comments/1wikmz1/jev_demo_wikirace/"><img src="https://external-preview.redd.it/anYxemlqNjJrMHFoMQDruYJy3DBIsPhqhRECIkxuvIt97Wx_qt0teXaXPlvG.png?format=pjpg&amp;auto=webp&amp;s=1c8c7fece9b9bccbc62d9627f03d50f0f56cf547" alt="维基百科速通" width="240"></a></td>
<td valign="top"><b><a href="https://www.reddit.com/r/accelerate/comments/1wikmz1/jev_demo_wikirace/">维基百科速通</a></b><br><sub>TypeSafe AI · Reddit · ▲ 51 · 2026-09-17</sub><br>演示 Jev 只用每页上的链接从一篇维基百科文章跑到另一篇，每跳一次都要在数百到数千个链接中做选择。<br><sub>相关: <a href="https://x.com/CompleteSkeptic/status/2099925688925184171">source</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/theappcypher/status/2101095181382721998"><img src="https://pbs.twimg.com/amplify_video_thumb/2101094095808847872/img/3gUUWv-2l7gtBJLH.jpg" alt="Mario Never Dies" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/theappcypher/status/2101095181382721998">Mario Never Dies</a></b><br><sub>theappcypher · X · ♥ 18 · 2026-09-18</sub><br>马里奥 agent：每一步都由 Jev 选择，每次死亡都会把整个 microsandbox 虚拟机分叉成 4 条时间线，保留活下来的那个马里奥。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/chiziaruhoma/status/2100878555047514390"><img src="https://pbs.twimg.com/amplify_video_thumb/2100876059709149184/img/jYoCG-SwxUKhp2pf.jpg" alt="Jevton" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/chiziaruhoma/status/2100878555047514390">Jevton</a></b><br><sub>chiziaruhoma · X · ♥ 131 · 2026-09-18</sub><br>小镇模拟：120 人、7 条路、20 家商铺，由 Jev 决定每位居民每小时做什么、花多少钱、冒什么险，外加议会优先事项、物价和新闻头条，之后还要熬过僵尸和陨石。<br><sub><b>Jev 用法:</b> 通过约 15 次批量调用，在不到 5 分钟内做出 20,000+ 个决策，不生成任何文本。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://www.reddit.com/r/vibecoding/comments/1wj7ch6/jev_will_kill_us_all/"><img src="https://external-preview.redd.it/ZjEzYWF0bXpoNXFoMZHx7oraHkZvnP0Ya-GG74OTeGOSUHkO5dZJtDpIK9wK.png?format=pjpg&amp;auto=webp&amp;s=99619399678c8b492ac33f9f3b2172476d9fbf4d" alt="Sigma Ups" width="240"></a></td>
<td valign="top"><b><a href="https://www.reddit.com/r/vibecoding/comments/1wj7ch6/jev_will_kill_us_all/">Sigma Ups</a></b><br><sub>WatchSigma · Reddit · ▲ 41 · 2026-09-17</sub><br>Flappy 风格游戏，平时通过摄像头捕捉身体动作来控制，视频展示的是自动模式：Jev 在没有任何人类输入的情况下驾驶飞龙闯过重重障碍。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/AlanDaitch/status/2100438353946513815"><img src="https://pbs.twimg.com/ext_tw_video_thumb/2100438029299040256/pu/img/s_cly7mjSq3voOC3.jpg" alt="Jev 玩俄罗斯方块" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/AlanDaitch/status/2100438353946513815">Jev 玩俄罗斯方块</a></b><br><sub>AlanDaitch · X · ♥ 49 · 2026-09-17</sub><br>Jev 在最高难度下玩俄罗斯方块，每步决策约 0.3 秒，2 分钟内放下 357 个方块、消除 134 行。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/0xSorrowRain/status/2100484781389791710"><img src="https://pbs.twimg.com/amplify_video_thumb/2100484509653487616/img/JEehDZgCXN_Y1F3x.jpg" alt="Jev 通过 MCP 玩 Slay the Spire 2" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/0xSorrowRain/status/2100484781389791710">Jev 通过 MCP 玩 Slay the Spire 2</a></b><br><sub>0xSorrowRain · X · ♥ 25 · 2026-09-17</sub><br>中文实验：把 Jev 接到带大量上下文的 Slay the Spire 2 MCP 服务器上；目前还没能活过第一层。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://www.reddit.com/r/codex/comments/1wkqknb/jev_playing_my_game_soccer_pinball_inside_unity/"><img src="https://external-preview.redd.it/eWc2cGc5dHg2aXFoMZgJJx1e7F4oMJHRnw_ML_5bj14hM22MnTm7n5_9DHZw.png?format=pjpg&amp;auto=webp&amp;s=be3e74936fe0f5575def2e9c83a8af1e970c3ded" alt="Soccer Pinball 试玩员" width="240"></a></td>
<td valign="top"><b><a href="https://www.reddit.com/r/codex/comments/1wkqknb/jev_playing_my_game_soccer_pinball_inside_unity/">Soccer Pinball 试玩员</a></b><br><sub>astrohoundstudios · Reddit · ▲ 38 · 2026-09-19</sub><br>Unity 封装，让 Jev 操作挡板、打完整场 Soccer Pinball 比赛，每场约 2 美分，并用技能滑块来调整游戏难度。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/anxkhn/JevPlaysPokemon"><img src="https://raw.githubusercontent.com/anxkhn/JevPlaysPokemon/main/docs/dashboard.png" alt="Jev 玩 Pokémon" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/anxkhn/JevPlaysPokemon">Jev 玩 Pokémon</a></b><br><sub>anxkhn · GitHub · ⭐ 5 · 2026-09-18</sub><br>让 Jev 在 Showdown 和真实 FireRed ROM 上打第 3 世代 Pokémon 对战的 agent，从 RAM 读取 HP、属性、招式和队伍，每回合在合法的招式和换人中做选择。<br><sub>相关: <a href="https://x.com/AnxKhn/status/2100842364248178833">demo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://www.reddit.com/r/ultimaonline/comments/1wkylbr/jev_ai_vs_jev_ai_ultima_online_duels/"><img src="https://external-preview.redd.it/BpPYrpIM8bOMMG3ZopGyhElvJ2UQa9p94nEM0yHe-ak.jpeg?auto=webp&amp;s=049d66cdc9b33ad6888d38f34eeef3d5ecc1ea0b" alt="Jev 对 Jev 的 Ultima Online 决斗" width="240"></a></td>
<td valign="top"><b><a href="https://www.reddit.com/r/ultimaonline/comments/1wkylbr/jev_ai_vs_jev_ai_ultima_online_duels/">Jev 对 Jev 的 Ultima Online 决斗</a></b><br><sub>autorokk · Reddit · ▲ 37 · 2026-09-19</sub><br>两个 Jev agent 在 Ultima Online 里互相决斗，每个法术和每次移动都由模型选择。<br><sub>相关: <a href="https://www.youtube.com/watch?v=tjX3UoD7HPQ">demo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/n8mirai/status/2102043190068920720"><img src="https://pbs.twimg.com/amplify_video_thumb/2102043140160921600/img/oA_cz_-Mlr57Dr25.jpg" alt="Infinite Backrooms" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/n8mirai/status/2102043190068920720">Infinite Backrooms</a></b><br><sub>n8mirai · X · ♥ 2 · 2026-09-21</sub><br>没有预制地图的 Backrooms 游戏：你一边探索，Jev 一边实时生成每个房间，每个房间约 $0.000265。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/luckeyfaraday/status/2100622223014842432"><img src="https://pbs.twimg.com/amplify_video_thumb/2100622064457498624/img/qDeXq1ID5SpwOoYJ.jpg" alt="Jev 玩 Pokemon FireRed" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/luckeyfaraday/status/2100622223014842432">Jev 玩 Pokemon FireRed</a></b><br><sub>luckeyfaraday · X · ♥ 33 · 2026-09-17</sub><br>花 $0.09、现实时间不到 5 分钟就在 Pokemon FireRed 里击败 Brock 的 agent：模拟器内存被解码成游戏状态，代码列出合法动作，Jev 从中选一个。<br><sub><b>Jev 用法:</b> 每回合对代码生成的合法动作做一个 Choice；每个输入都记录在日志里，重放时无需任何模型调用。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://www.reddit.com/r/accelerate/comments/1whk9oy/new_typesafe_ai_jev_model_playing_minecraft_wip/"><img src="https://external-preview.redd.it/rAUA75ocfeUfSZ1gdcTcS75zzqqc3caVPjZ-9Cg6WN4.jpeg?auto=webp&amp;s=f440801b7e711af369ec1d1bd01321c017aff07c" alt="Minecraft 里的 Jevbot" width="240"></a></td>
<td valign="top"><b><a href="https://www.reddit.com/r/accelerate/comments/1whk9oy/new_typesafe_ai_jev_model_playing_minecraft_wip/">Minecraft 里的 Jevbot</a></b><br><sub>BiasHyperion784 · Reddit · ▲ 35 · 2026-09-16</sub><br>仍在开发中的 Minecraft 机器人，通过 API 由 Jev 驱动，视频里它在夜幕降临时逃离一群僵尸。<br><sub>相关: <a href="https://www.youtube.com/watch?v=3G14OU00crI">demo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/toksdotdev/status/2101084662793666618"><img src="https://pbs.twimg.com/amplify_video_thumb/2101073621049298944/img/cynsgROvqMkHdnxZ.jpg" alt="分支未来版 Doom" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/toksdotdev/status/2101084662793666618">分支未来版 Doom</a></b><br><sub>toksdotdev · X · ♥ 23 · 2026-09-18</sub><br>Doom agent：Jev 选择动作，microsandbox harness 从同一个存档点并行跑多次尝试，再由 LLM 复盘结果，决定下一次怎么打或回退重来。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/Taufiq_ansari01/status/2100906203396337686"><img src="https://pbs.twimg.com/amplify_video_thumb/2100905164261748736/img/Jf-ySNfaAdZ95K-O.jpg" alt="Fight Jev" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/Taufiq_ansari01/status/2100906203396337686">Fight Jev</a></b><br><sub>Taufiq_ansari01 · X · ♥ 8 · 2026-09-18</sub><br>格斗游戏：Jev 实时控制敌人，它每做一个决策，出招前都会在屏幕上显示该决策的概率。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/gdechichi/status/2102144051197915162"><img src="https://pbs.twimg.com/amplify_video_thumb/2102143877465747456/img/-3xenQD1bCHR_uyz.jpg" alt="Jev 魔方求解器" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/gdechichi/status/2102144051197915162">Jev 魔方求解器</a></b><br><sub>gdechichi · X · ♥ 97 · 2026-09-21</sub><br>Jev 独立还原魔方的演示，像人类玩家那样一步步选出每一次转动。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/will_caskets/status/2100968037117780130"><img src="https://pbs.twimg.com/amplify_video_thumb/2100819832660975616/img/j8xtj7J4zxqZ3kdx.jpg" alt="Jev 版魔术 8 号球" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/will_caskets/status/2100968037117780130">Jev 版魔术 8 号球</a></b><br><sub>will_caskets · X · ♥ 7 · 2026-09-18</sub><br>魔术 8 号球（Magic 8 Ball）：针对你的问题，让 Jev 从 20 个经典答案里挑一个。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/CombosFun_AI/status/2100952069461127257"><img src="https://pbs.twimg.com/amplify_video_thumb/2100950508919984128/img/n0KDfl8VSy9C-q3V.jpg" alt="Combos FPS：Astra 对 Jev" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/CombosFun_AI/status/2100952069461127257">Combos FPS：Astra 对 Jev</a></b><br><sub>CombosFun_AI · X · ♥ 6 · 2026-09-18</sub><br>同一款 Combos FPS 游戏分别由 GPT-6 Astra 和 Jev 来玩的并排对比，展示推理模型与决策模型的差异。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/phyous/tsai-sc"><img src="https://opengraph.githubassets.com/1/phyous/tsai-sc" alt="Jev 玩 StarCraft" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/phyous/tsai-sc">Jev 玩 StarCraft</a></b><br><sub>phyous · GitHub · ⭐ 22 · 2026-09-16</sub><br>让 Jev 玩初代 StarCraft 共享版第一个战斗任务 Strongarm 的 harness，根据结构化游戏状态选择指令，并通过键盘和鼠标执行；它赢下了这个任务。<br><sub>相关: <a href="https://www.reddit.com/r/singularity/comments/1whu7cr/jev_plays_starcraft/">discussion</a> · <a href="https://www.reddit.com/r/typesafe_ai/comments/1wi2j4e/jev_playing_starcraft/">discussion 2</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/SinghDevHub/status/2102086884998664521"><img src="https://pbs.twimg.com/amplify_video_thumb/2102085730793398272/img/CkPhtAkZl0_n4Hrs.jpg" alt="迷你 AI 文明" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/SinghDevHub/status/2102086884998664521">迷你 AI 文明</a></b><br><sub>SinghDevHub · X · ♥ 74 · 2026-09-21</sub><br>Three.js 岛屿模拟，48 位居民由 Jev 选择下一步行动，GPT 主导世界事件，代码保证规则；一次 12 分钟的运行执行了 392 个 Jev 决策，花费约 $0.023。<br><sub><b>Jev 用法:</b> 根据每位居民的状态和附近观察，对可用行动（吃饭、休息、种地、建造、帮忙、偷窃）做 Choice。</sub><br><sub>相关: <a href="https://github.com/singhdevhub-lovepreet/firstlight">repo</a> · <a href="https://github.com/singhdevhub-lovepreet/firstlight">project</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/2ndpsy/status/2101026520185622589"><img src="https://pbs.twimg.com/amplify_video_thumb/2101025189622349824/img/7xMDppgS62icqbO1.jpg" alt="和 Byte 玩石头剪刀布" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/2ndpsy/status/2101026520185622589">和 Byte 玩石头剪刀布</a></b><br><sub>2ndpsy · X · ♥ 15 · 2026-09-18</sub><br>和 Byte 玩石头剪刀布：它每轮用 Jev 预测你下一手出什么，并在你出手前先锁定克制招式，赌注通过 Ark 结算。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/otani_ai_memo/status/2100784295329886614"><img src="https://pbs.twimg.com/media/HSdu9l7bMAAkWhh.jpg" alt="Jev 对战 Claude 和 GPT 玩俄罗斯方块" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/otani_ai_memo/status/2100784295329886614">Jev 对战 Claude 和 GPT 玩俄罗斯方块</a></b><br><sub>otani_ai_memo · 文章 · ♥ 18 · 2026-09-18</sub><br>日语文章：让 Jev 与 Claude 和 GPT 在俄罗斯方块和 Puyo Puyo 中正面对决，Jev 赢下全部 14 场，文章认为设计得好的问题能让它的判断达到顶级 LLM 的水平。<br><sub>相关: <a href="https://github.com/aieo-product/jev-gamebenchmark">repo</a> · <a href="https://jev-guide.take-otani.workers.dev/">guide</a> · <a href="https://github.com/aieo-product/jev-gamebenchmark">project</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Reisenbug/TerraBlind"><img src="https://raw.githubusercontent.com/Reisenbug/TerraBlind/main/docs/cover-jev-en.png" alt="TerraBlind" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Reisenbug/TerraBlind">TerraBlind</a></b><br><sub>Reisenbug · GitHub · ⭐ 66 · 2026-04-08</sub><br>Terraria 的 tModLoader mod，由 Jev 打 boss，每 200 毫秒 回答一个问题，代码把答案转成按键；它在大师模式下击败了所有困难模式之前的 boss。<br><sub>相关: <a href="https://www.youtube.com/watch?v=g6CADbjBhlk">demo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/WillTheRapper_/status/2102133645167272057"><img src="https://pbs.twimg.com/media/HSxHFTDb0AAMbUv.jpg?name=orig" alt="Truman World" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/WillTheRapper_/status/2102133645167272057">Truman World</a></b><br><sub>WillTheRapper_ · X · ♥ 29 · 2026-09-21</sub><br>AI 人生模拟：GPT-6 Astra 引擎推动故事线，Jev 决定接下来发生什么，终端风格的界面把每个决策可视化。<br><sub><b>Jev 用法:</b> 挑选下一个故事事件，并审核用户提示词，把它们归类为模拟世界内的行动。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/marinatrajk/status/2102173897676185658"><img src="https://pbs.twimg.com/amplify_video_thumb/2102173389725024256/img/1rjU04Eh2VBcFXKm.jpg" alt="Tiny World" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/marinatrajk/status/2102173897676185658">Tiny World</a></b><br><sub>marinatrajk · X · ♥ 33 · 2026-09-21</sub><br>六位居民的小型 3D 世界，他们有住所、工作、需求和友谊，Jev 决定每个人的下一步行动，用户还能注入紧急情况等情境，看他们如何反应。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/juminoz/status/2100832108855857325"><img src="https://pbs.twimg.com/amplify_video_thumb/2100831608366575616/img/lDHAtdzHqYd-f0eU.jpg" alt="Jev 玩 Time Crisis" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/juminoz/status/2100832108855857325">Jev 玩 Time Crisis</a></b><br><sub>juminoz · X · ♥ 3 · 2026-09-18</sub><br>Jev 通过自定义 harness 玩街机射击游戏 Time Crisis，射击目标并躲到掩体后避免中弹。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/filicroval/status/2100963424163307712"><img src="https://pbs.twimg.com/amplify_video_thumb/2100963025201037312/img/FgYho35_OiQ_zr3w.jpg" alt="League of Legends 胜率浮层" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/filicroval/status/2100963424163307712">League of Legends 胜率浮层</a></b><br><sub>filicroval · X · ♥ 10 · 2026-09-18</sub><br>实时浮层，每秒把完整的 League of Legends 对局状态发给 Jev，询问谁会赢、谁影响最大、领先方是否快要翻车；一整局花费约 $0.20。<br><sub><b>Jev 用法:</b> 每秒三个问题：一个胜负 Noul、一个影响力 Choice 和一个翻车 Noul。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/AmritNigam2/status/2100882320945520778"><img src="https://pbs.twimg.com/amplify_video_thumb/2100881913317879808/img/cnr8YJJs3WfuHdnI.jpg" alt="Jev 玩 Clash Royale" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/AmritNigam2/status/2100882320945520778">Jev 玩 Clash Royale</a></b><br><sub>AmritNigam2 · X · ♥ 33 · 2026-09-18</sub><br>Jev 实时玩 Clash Royale 并赢下一局。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/ahab_developer/status/2101605212108800348"><img src="https://pbs.twimg.com/amplify_video_thumb/2101596647977545728/img/9DaL2uCCG_baCfck.jpg" alt="Jev Arcade" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/ahab_developer/status/2101605212108800348">Jev Arcade</a></b><br><sub>ahab_developer · X · ♥ 3 · 2026-09-20</sub><br>可免费试玩的网页街机厅，Jev 在其中实时玩 Pac-Man、Bomberman 和 Space Invaders。<br><sub>相关: <a href="https://jev-arcade.ahab.cn/">app</a> · <a href="https://jev-arcade.ahab.cn">project</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/sachpatro97/status/2101064273187274838"><img src="https://pbs.twimg.com/amplify_video_thumb/2101062907593416704/img/gvJG-NjM4HY5yN6V.jpg" alt="多个 Jev 玩 Catan" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/sachpatro97/status/2101064273187274838">多个 Jev 玩 Catan</a></b><br><sub>sachpatro97 · X · ♥ 8 · 2026-09-18</sub><br>基于某个 Jev 游戏 harness 的分支，几个 Jev agent 一起玩 Catan，直到它们不再互相谈判、都选择跳过回合。<br><sub>相关: <a href="https://github.com/vtrivedy/jev-plays-games">based on</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/juminoz/status/2100846091281506370"><img src="https://pbs.twimg.com/amplify_video_thumb/2100845309748490240/img/ahnwqqlyOJSdGRQL.jpg" alt="Jev 玩 Resident Evil" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/juminoz/status/2100846091281506370">Jev 玩 Resident Evil</a></b><br><sub>juminoz · X · ♥ 5 · 2026-09-18</sub><br>让 Jev 玩初代 3D 版 Resident Evil 的实验，要应对移动、敌人和谜题；此前作者已让它跑过 Time Crisis。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/mittalparth_/status/2100817199686619348"><img src="https://pbs.twimg.com/amplify_video_thumb/2100816454564339712/img/WTv-oigoy6fOY6Qc.jpg" alt="Jev 玩 Chrome Dino" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/mittalparth_/status/2100817199686619348">Jev 玩 Chrome Dino</a></b><br><sub>mittalparth_ · X · ♥ 44 · 2026-09-18</sub><br>Jev 根据小恐龙奔跑的快照玩 Chrome Dino 游戏，决定跳跃、奔跑或下蹲并给出置信度分数，每次决策约 280 毫秒；116M token 花费 $4.65。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/virajbhartiya/laya-vs-jev"><img src="https://raw.githubusercontent.com/virajbhartiya/laya-vs-jev/main/docs/assets/trex-arena-window.png" alt="Laya vs Jev" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/virajbhartiya/laya-vs-jev">Laya vs Jev</a></b><br><sub>virajbhartiya · GitHub · ⭐ 44 · 2026-09-21</sub><br>Chrome 的 T-Rex 游戏，由通过 MLX 本地运行的开源 Laya 模型和托管的 Jev 并排来玩，实时显示响应时间、连续存活纪录和撞车回放。<br><sub>相关: <a href="https://x.com/heyxviraj/status/2102048070649405592">demo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/JamesWard/status/2101176408584098146"><img src="https://pbs.twimg.com/tweet_video_thumb/HSje2ycXIAA5EET.jpg" alt="Jev 对战 LLM 玩 Connect4" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/JamesWard/status/2101176408584098146">Jev 对战 LLM 玩 Connect4</a></b><br><sub>JamesWard · X · ♥ 21 · 2026-09-19</sub><br>类 Connect4 游戏，让 Jev 与 LLM 对战，Jev 下得更好、更快、更便宜，也更稳定。<br><sub>相关: <a href="https://github.com/jamesward/jev-llm-c4">repo</a> · <a href="https://github.com/jamesward/jev-llm-c4">project</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/Neel490/status/2100953791260397747"><img src="https://pbs.twimg.com/amplify_video_thumb/2100953694594379776/img/swbWBiQbbZtvxLH_.jpg" alt="Jev 玩 Geometry Dash" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/Neel490/status/2100953791260397747">Jev 玩 Geometry Dash</a></b><br><sub>Neel490 · X · ♥ 14 · 2026-09-18</sub><br>一段短视频，展示 Jev 玩节奏跑酷平台游戏 Geometry Dash。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/uwwgo/status/2101683325320454189"><img src="https://pbs.twimg.com/amplify_video_thumb/2101682942334398464/img/TIjR8ALsT1iz-Nc2.jpg" alt="和 Jev 玩 Codenames" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/uwwgo/status/2101683325320454189">和 Jev 玩 Codenames</a></b><br><sub>uwwgo · X · ♥ 19 · 2026-09-20</sub><br>和作为队友的 Jev 一起玩 Codenames，用来示范如何把快速、便宜的决策模型嵌入消费级产品。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/dedene/status/2101770592055935114"><img src="https://pbs.twimg.com/amplify_video_thumb/2101770557297774592/img/EMCv1Ka0Y1gtwjO-.jpg" alt="jevspin" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/dedene/status/2101770592055935114">jevspin</a></b><br><sub>dedene · X · ♥ 27 · 2026-09-20</sub><br>不依赖求解库的魔方求解器：代码列出当前阶段的合法步骤，Jev 从 12 个中选出最优，用 17 次决策、约 $0.0007 还原魔方。<br><sub><b>Jev 用法:</b> 每一步对代码生成、并用平实语言描述的合法走法做一个 Choice。</sub><br><sub>相关: <a href="https://github.com/dedene/jevspin">repo</a> · <a href="https://github.com/dedene/jevspin">project</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/tobiaswup/status/2102046994248224826"><img src="https://pbs.twimg.com/amplify_video_thumb/2102045711646724096/img/Nl5uIiC5lFJVF_JT.jpg" alt="贪吃蛇：Jev 对战 Laya 和 Kev" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/tobiaswup/status/2102046994248224826">贪吃蛇：Jev 对战 Laya 和 Kev</a></b><br><sub>tobiaswup · X · ♥ 16 · 2026-09-21</sub><br>自制贪吃蛇基准测试，对比通过 API 调用的 Jev 与本地运行的 Laya-MLX 和 Kev-4B：Jev 零死亡、约 395 毫秒，Kev 死了两次、约 175 毫秒，Laya 陷入循环、约 33 毫秒。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/PrithviBtw/status/2100696083207004574"><img src="https://pbs.twimg.com/amplify_video_thumb/2100695699528814592/img/_AklUvdn4Bef6iLZ.jpg" alt="Jev 玩 Absurd Trolley Problems" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/PrithviBtw/status/2100696083207004574">Jev 玩 Absurd Trolley Problems</a></b><br><sub>PrithviBtw · X · ♥ 15 · 2026-09-17</sub><br>Jev 把 28 道 Absurd Trolley Problems 各玩了 10 遍，46% 的情况下与人类多数选择一致，会为 5 个机器人牺牲一个人，也拒绝了 $500k 的贿赂。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/mikehostetler/status/2100946109308748079"><img src="https://pbs.twimg.com/amplify_video_thumb/2100945952395722754/img/cnSU71pFTDxt2C2f.jpg" alt="Jido agent 下井字棋" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/mikehostetler/status/2100946109308748079">Jido agent 下井字棋</a></b><br><sub>mikehostetler · X · ♥ 41 · 2026-09-18</sub><br>用 Jido 和 ReqLLM 构建的两个 Elixir agent 互下井字棋，每一步都调用 Jev 选出下一步。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/MarcelooMendes/status/2100969755318370699"><img src="https://pbs.twimg.com/amplify_video_thumb/2100969618235969537/img/9azLB1IGbF6hoY1a.jpg" alt="Jev 俄罗斯方块 agent" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/MarcelooMendes/status/2100969755318370699">Jev 俄罗斯方块 agent</a></b><br><sub>MarcelooMendes · X · ♥ 4 · 2026-09-18</sub><br>由 Jev 驱动的俄罗斯方块 agent，短视频展示了它的实际玩法。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/adrianmg/status/2100970810483823086"><img src="https://pbs.twimg.com/amplify_video_thumb/2100970516081508352/img/1l_l07Sh5OsLeJGm.jpg" alt="手动与 AI 游玩切换" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/adrianmg/status/2100970810483823086">手动与 AI 游玩切换</a></b><br><sub>adrianmg · X · ♥ 30 · 2026-09-18</sub><br>街机游戏，可以在自己玩和让 Jev 玩之间切换，60 FPS 下每秒 2-3 次调用、平均延迟约 150 毫秒，由它决定诸如追道具还是护球之类的事。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/petergostev/status/2102149363787088384"><img src="https://pbs.twimg.com/media/HSxVXgfW8AEPzIL.jpg?name=orig" alt="Jev 玩 RollerCoaster Tycoon 2" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/petergostev/status/2102149363787088384">Jev 玩 RollerCoaster Tycoon 2</a></b><br><sub>petergostev · X · ♥ 15 · 2026-09-21</sub><br>尝试让 Jev 玩 RollerCoaster Tycoon 2：开局建了几个游乐设施后就卡住了，说明更难的游戏仍需要更聪明的模型。<br><sub>相关: <a href="https://x.com/i/broadcasts/1DGleVdkbyoJL">stream</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/stevibe/status/2101684349104247036"><img src="https://pbs.twimg.com/amplify_video_thumb/2101684255890022401/img/zQzL7sOfvDB18h-5.jpg" alt="Jev 烹饪游戏" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/stevibe/status/2101684349104247036">Jev 烹饪游戏</a></b><br><sub>stevibe · X · ♥ 16 · 2026-09-20</sub><br>为 Jev 打造的 Flash 风格烹饪游戏，它实时翻面、上菜和烧烤；一次 5 分钟的 Rush 班次做了 261 个决策、382 个动作，接待 29 位客人，得分 8,264，花费约 $0.15。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://www.reddit.com/r/aigamedev/comments/1wkd96v/jev_plays_both_sides_of_a_gladiator_arena_game/"><img src="https://external-preview.redd.it/NGk2aTd1d3p2ZXFoMXqalpO3Ixyt1yQWYtSXC1NUz1_Y9AQ08nqmQOyOHDI6.png?format=pjpg&amp;auto=webp&amp;s=7923f11ee0aa0f690eb397824c395fd59ee2024f" alt="Jev 角斗场" width="240"></a></td>
<td valign="top"><b><a href="https://www.reddit.com/r/aigamedev/comments/1wkd96v/jev_plays_both_sides_of_a_gladiator_arena_game/">Jev 角斗场</a></b><br><sub>codeninja · Reddit · ▲ 12 · 2026-09-19</sub><br>小型竞技场游戏：Jev 以约每秒 3 次请求的速度，实时为双方共六名斗士指定目标。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/Entelic_Aria/status/2100966999602102520"><img src="https://pbs.twimg.com/amplify_video_thumb/2100966615659732992/img/TweCJbUhQ94mbk2d.jpg" alt="Omarchy 上的四子棋" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/Entelic_Aria/status/2100966999602102520">Omarchy 上的四子棋</a></b><br><sub>Entelic_Aria · X · ♥ 34 · 2026-09-18</sub><br>在 Omarchy Linux 上的 Aria 里运行的四子棋循环：Jev 读取棋盘并选择落子，Hermes 复盘每一局结果，共用 6,499 个 token，花费 $0.00022113。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://www.reddit.com/r/typesafe_ai/comments/1wjwhlj/jev_generating_infinite_game_levels/"><img src="https://external-preview.redd.it/ZGc3Y3M3d2FjYnFoMe5izzrFI6BXxb-7gqg_kASOv1wpqFylkCW7w3gTJp9Y.png?format=pjpg&amp;auto=webp&amp;s=cd5d15fad8829a2ea2ec17565148402c9e6396c7" alt="用 Jev 无限生成游戏关卡" width="240"></a></td>
<td valign="top"><b><a href="https://www.reddit.com/r/typesafe_ai/comments/1wjwhlj/jev_generating_infinite_game_levels/">用 Jev 无限生成游戏关卡</a></b><br><sub>Just_Lingonberry_352 · Reddit · ▲ 11 · 2026-09-18</sub><br>一段像素风横版平台游戏的片段，玩家一路奔跑，关卡由 Jev 持续生成。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/TusharXo/status/2100650773726314838"><img src="https://pbs.twimg.com/amplify_video_thumb/2100649857379909632/img/umakGAn8HhvRnWu0.jpg" alt="Jev 地图试玩员" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/TusharXo/status/2100650773726314838">Jev 地图试玩员</a></b><br><sub>TusharXo · X · ♥ 22 · 2026-09-17</sub><br>让 Jev 为一款基于 Crayon 的浏览器游戏试玩新地图，在上线前检查关卡。<br><sub>相关: <a href="https://app.usecrayon.ai/play/a06744fc-3acb-41d9-8825-5c8bd9cbbafd">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/legitamit/status/2100713197502173373"><img src="https://pbs.twimg.com/amplify_video_thumb/2100711545218924544/img/R3UxL8HSq04FnC4R.jpg" alt="1v100" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/legitamit/status/2100713197502173373">1v100</a></b><br><sub>legitamit · X · ♥ 16 · 2026-09-17</sub><br>一个小玩具：你对着 100 个小团子观众讲话，每个都有自己的性格，你每说一句，它们各自调用一次 Jev 判断自己是不是已经听烦了；每轮成本不到 $0.01。<br><sub><b>Jev 用法:</b> 每句话、每位观众一个 Noul：烦了没有。</sub><br><sub>相关: <a href="https://1v100.fun">app</a> · <a href="https://1v100.fun">project</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://www.youtube.com/watch?v=cP-GWKteHKo"><img src="https://i.ytimg.com/vi/cP-GWKteHKo/hqdefault.jpg" alt="Jev 版 Ultima Online 战斗 AI" width="240"></a></td>
<td valign="top"><b><a href="https://www.youtube.com/watch?v=cP-GWKteHKo">Jev 版 Ultima Online 战斗 AI</a></b><br><sub>John · 视频 · ♥ 13 · 2026-09-17</sub><br>Ultima Online 机器人，由 Jev 取代脚本化的战斗循环，选择站位格子、何时逃跑或追击、去哪探索以及捡什么战利品，并有实时状态界面。<br><sub><b>Jev 用法:</b> 用一个 tilePriority 问题决定站位，另有逃跑、追击和拾取战利品的决策。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/ishuagra02/status/2101025059909353718"><img src="https://pbs.twimg.com/amplify_video_thumb/2101023867636449280/img/XK5TcIcdTm6_R4xw.jpg" alt="Jev 打通 Super Mario Bros." width="240"></a></td>
<td valign="top"><b><a href="https://x.com/ishuagra02/status/2101025059909353718">Jev 打通 Super Mario Bros.</a></b><br><sub>ishuagra02 · X · ♥ 16 · 2026-09-18</sub><br>只死 1 次就打通 Super Mario Bros. 第一关的 agent，每个动作都根据模拟器给出的结构化游戏状态来选。<br><sub><b>Jev 用法:</b> 根据马里奥的位置、附近的敌人和地形，在模拟出的下一步动作（跳、跑等）上做一个 Choice，以能否活下来为判断标准。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/ChmalSzymon/status/2100934588205851015"><img src="https://pbs.twimg.com/amplify_video_thumb/2100934447822471168/img/wHM0ZeHHQRZKFTLk.jpg" alt="Floppy Apex" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/ChmalSzymon/status/2100934588205851015">Floppy Apex</a></b><br><sub>ChmalSzymon · X · ♥ 16 · 2026-09-18</sub><br>Jev 玩一款名为 Floppy Apex 的 Flappy Bird 风格游戏，并刷新了此前的最高分；由 Apex 通过 Appduct 接入。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/hanznathanpo/status/2101020398477365629"><img src="https://pbs.twimg.com/amplify_video_thumb/2101020269586292736/img/EQfj-8D623rJOWzX.jpg" alt="Jev 空中缠斗" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/hanznathanpo/status/2101020398477365629">Jev 空中缠斗</a></b><br><sub>hanznathanpo · X · ♥ 16 · 2026-09-18</sub><br>首次尝试让 Jev 驾驶飞机进行空中缠斗，作者表示目前效果还不好。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/luckeyfaraday/status/2100955913913774437"><img src="https://pbs.twimg.com/amplify_video_thumb/2100955835597811712/img/SWhMkCyUZC_SrjmK.jpg" alt="Jev 刷闪光 Pokemon" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/luckeyfaraday/status/2100955913913774437">Jev 刷闪光 Pokemon</a></b><br><sub>luckeyfaraday · X · ♥ 14 · 2026-09-18</sub><br>Pokemon FireRed 里的自主循环：Jev 反复重置、检查初始 Pokemon，直到遇到闪光为止；此前它已在不到 5 分钟内击败 Brock。<br><sub>相关: <a href="https://x.com/luckeyfaraday/status/2100622223014842432">earlier</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/ziwenxu_/status/2100984628811084144"><img src="https://pbs.twimg.com/amplify_video_thumb/2100984324447203329/img/R3W7PNHwrMyOm7cK.jpg" alt="Jev 选俄罗斯方块落点" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/ziwenxu_/status/2100984628811084144">Jev 选俄罗斯方块落点</a></b><br><sub>ziwenxu_ · X · ♥ 21 · 2026-09-18</sub><br>接入俄罗斯方块：每来一个方块，Jev 查看棋盘和所有落点，在约半秒内选出一个，一整局花费不到半美分。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/tommyvedvik/status/2100903520425677027"><img src="https://pbs.twimg.com/amplify_video_thumb/2100903386992291840/img/EJIJPWYpP8F6iDiF.jpg" alt="FPS 里的 Jev 机器人" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/tommyvedvik/status/2100903520425677027">FPS 里的 Jev 机器人</a></b><br><sub>tommyvedvik · X · ♥ 12 · 2026-09-18</sub><br>第一人称射击游戏，对手是三个由 Jev 控制的机器人。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://www.reddit.com/r/typesafe_ai/comments/1wiswxr/jev_plays_uno_and_beats_me/"><img src="https://external-preview.redd.it/MDdndjA3eWxzMnFoMUJOWPu6KucJdZQlotOh3EBny2btI-yDfvlTONzGGTzb.png?format=pjpg&amp;auto=webp&amp;s=183ec2605bc04c4982a8b3fdf92ae12132c9fca1" alt="Jev 玩 UNO" width="240"></a></td>
<td valign="top"><b><a href="https://www.reddit.com/r/typesafe_ai/comments/1wiswxr/jev_plays_uno_and_beats_me/">Jev 玩 UNO</a></b><br><sub>hiImMate · Reddit · ▲ 8 · 2026-09-17</sub><br>简单的 UNO 游戏：一名人类对战三个 Jev 对手，每个对手拿到的指令各不相同，出牌速度和硬编码 AI 一样快。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://lmjtfy.dev/"><img src="https://lmjtfy.dev/og.png" alt="lmjtfy" width="240"></a></td>
<td valign="top"><b><a href="https://lmjtfy.dev/">lmjtfy</a></b><br><sub>PostHog · 应用 · ▲ 8</sub><br>名字取自 Let me Jev that for you：随便问一个是非题，得到的不是大段文字，而是 Jev 的校准概率，另有被问得最多的问题的实时信息流。<br><sub><b>Jev 用法:</b> 每个问题一个 Noul。</sub><br><sub>相关: <a href="https://news.ycombinator.com/item?id=49758022">discussion</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/joaobnobre/status/2100486780298383801"><img src="https://pbs.twimg.com/amplify_video_thumb/2100486436323508224/img/LalHAX48Wkvn20LT.jpg" alt="Jev 玩 Minecraft Skyblock" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/joaobnobre/status/2100486780298383801">Jev 玩 Minecraft Skyblock</a></b><br><sub>joaobnobre · X · ♥ 14 · 2026-09-17</sub><br>单个 Jev agent 玩 Minecraft Skyblock：读取游戏状态，通过类型化决策选出每一步行动。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/NesanSelvan04/status/2100844705588347238"><img src="https://pbs.twimg.com/amplify_video_thumb/2100844526281879552/img/GUoeEcUZPpay61x8.jpg" alt="Jev Pac-Man" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/NesanSelvan04/status/2100844705588347238">Jev Pac-Man</a></b><br><sub>NesanSelvan04 · X · ♥ 6 · 2026-09-18</sub><br>每一步都由 Jev 根据 Pac-Man 周围的格子决定的 Pac-Man 游戏，返回方向、策略、危险分数，以及被困、已锁定、后悔三个标记。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://www.reddit.com/r/typesafe_ai/comments/1wjwfz6/jev_plays_streetfighter_2/"><img src="https://external-preview.redd.it/NWVkaW83enViYnFoMay-vxLp3z8yZzFfUDRXejkROs2MYTjUI3KtLbhhG02Y.png?format=pjpg&amp;auto=webp&amp;s=771cfb248c3cfd443131cdb83078edcd6cbcf22c" alt="Jev 玩 Street Fighter 2" width="240"></a></td>
<td valign="top"><b><a href="https://www.reddit.com/r/typesafe_ai/comments/1wjwfz6/jev_plays_streetfighter_2/">Jev 玩 Street Fighter 2</a></b><br><sub>Smartaces · Reddit · ▲ 7 · 2026-09-18</sub><br>通过自定义控制连接器把 Street Fighter II 接到 Jev 上，上下文只有一份操作说明；效果好坏参半，有时会狂发波动拳。<br><sub><b>Jev 用法:</b> 每一步在大约 50 个招式选项上做一个 Choice。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/MartinPulitano/status/2101414345096012228"><img src="https://pbs.twimg.com/amplify_video_thumb/2101414307133362176/img/S8Xkav3h2mc2hUet.jpg" alt="JEVRACE" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/MartinPulitano/status/2101414345096012228">JEVRACE</a></b><br><sub>MartinPulitano · X · ♥ 21 · 2026-09-19</sub><br>3D F1 比赛，10 辆车由 Jev 驾驶，每辆都有自己的提示词（早早进攻、节省轮胎），前方可视距离只有约 42 米，地图生成器有超过 4B 个种子。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/hiper2d/werewolf-ai-party-game"><img src="https://raw.githubusercontent.com/hiper2d/werewolf-ai-party-game/master/images/ai-werewolf-cover.png" alt="AI Werewolf" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/hiper2d/werewolf-ai-party-game">AI Werewolf</a></b><br><sub>hiper2d · GitHub · ⭐ 20 · 2024-02-19</sub><br>社交推理游戏：你是一群身怀秘密身份的 AI 机器人中唯一的人类；基于 Jev 的发言路由器决定每条消息由哪些机器人回复，Game Master 模型作为兜底。<br><sub><b>Jev 用法:</b> Jev 作为亚秒级评判者引导讨论，决定下一个发言的机器人；不生成文本。</sub><br><sub>相关: <a href="https://aiwerewolf.net">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/sorrycc/typesafe-snake"><img src="https://opengraph.githubassets.com/1/sorrycc/typesafe-snake" alt="typesafe-snake" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/sorrycc/typesafe-snake">typesafe-snake</a></b><br><sub>sorrycc · GitHub · ⭐ 20 · 2026-09-17</sub><br>Jev 实时玩的贪吃蛇：代码计算合法走法以及食物距离、flood-fill 可达性和死路，如果答案没赶上 tick 截止时间，蛇就直走。<br><sub><b>Jev 用法:</b> 每个 tick 对合法走法做一个 Choice。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/wangzhishou/OneBox/blob/main/feature/xiangqi/src/main/java/com/wanbaohe/xiangqi/data/JevMoveChooser.kt"><img src="https://opengraph.githubassets.com/1/wangzhishou/OneBox" alt="OneBox 的 Jev 象棋引擎" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/wangzhishou/OneBox/blob/main/feature/xiangqi/src/main/java/com/wanbaohe/xiangqi/data/JevMoveChooser.kt">OneBox 的 Jev 象棋引擎</a></b><br><sub>wangzhishou · GitHub · ⭐ 389 仓库 · 2026-08-08</sub><br>Android AI 工具箱应用，把 Jev 接入为判断引擎并用它下中国象棋，选择 Choice 概率最高的走法。<br><sub><b>Jev 用法:</b> 对候选象棋走法做 Choice，取返回概率的 argmax；优先直连 key，失败时回退到代理。</sub><br><sub>相关: <a href="https://www.oneboxable.com">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/emrickgarrett/OneVOneJev"><img src="https://opengraph.githubassets.com/1/emrickgarrett/OneVOneJev" alt="OneVOneJev" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/emrickgarrett/OneVOneJev">OneVOneJev</a></b><br><sub>emrickgarrett · GitHub · ⭐ 19 · 2026-09-17</sub><br>服务器权威的 Three.js 狙击竞技场，你和 Jev 对战，先拿五杀者获胜，观众可以排队观战；Jev 根据比赛状态决定移动、瞄准和开火。<br><sub><b>Jev 用法:</b> 每个决策 tick 询问移动、视角、瞄准、开火和跳跃，API 失败时回退到启发式策略。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/winebaizou/status/2101994437002072365"><img src="https://pbs.twimg.com/amplify_video_thumb/2101994292646760448/img/eJb-OBlF4mqf3si9.jpg" alt="Jev 驱动的 3D 角色" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/winebaizou/status/2101994437002072365">Jev 驱动的 3D 角色</a></b><br><sub>winebaizou · X · ♥ 2 · 2026-09-21</sub><br>动画 3D 角色，面部表情和身体反应由 Jev 选择，你和它说话时会回应，一起看 YouTube 时表情也会随之变化。<br><sub>相关: <a href="https://jev-character.winebaizou.workers.dev">app</a> · <a href="https://x.com/gigabit_million/status/2101285853859545263">inspired by</a> · <a href="https://jev-character.winebaizou.workers.dev">project</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://www.reddit.com/r/typesafe_ai/comments/1wiipyj/jev_plays_brotato/"><img src="https://external-preview.redd.it/emdhdmRheHAyMHFoMZ-4l1K0cwYempvwCLtCfCUmlSYrwFk65dIHEY8ph35v.png?format=pjpg&amp;auto=webp&amp;s=292db54f93edb95df5060e04754b7484faca51eb" alt="Jev 玩 Brotato" width="240"></a></td>
<td valign="top"><b><a href="https://www.reddit.com/r/typesafe_ai/comments/1wiipyj/jev_plays_brotato/">Jev 玩 Brotato</a></b><br><sub>TriamondG · Reddit · ▲ 5 · 2026-09-17</sub><br>Godot mod harness，把 Brotato 的游戏状态和有效移动指令喂给 Jev，由它躲避敌人、收集战利品；约 15 分钟搭好，打 10 波花了 $0.03。<br><sub><b>Jev 用法:</b> 每一步在一条简短的指导指令下，对移动指令做一个 Choice。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/GreenCodeCodes/status/2102118562663903413"><img src="https://pbs.twimg.com/media/HSw5lBbXsAAxQbF.jpg?name=orig" alt="Jev 维基百科速通" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/GreenCodeCodes/status/2102118562663903413">Jev 维基百科速通</a></b><br><sub>GreenCodeCodes · X · ♥ 15 · 2026-09-21</sub><br>维基百科速通：模型只能靠站内链接从一个页面跑到另一个页面；一年前 LLM 平均每步要 5-10 秒，而 Jev 不到 1 秒。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Eniip/jev-game-tools"><img src="https://opengraph.githubassets.com/1/Eniip/jev-game-tools" alt="jev-game-lab" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Eniip/jev-game-tools">jev-game-lab</a></b><br><sub>Eniip · GitHub · ⭐ 14 · 2026-09-19</sub><br>驱动实时游戏的实验，从 Brotato 开始：Jev 每帧在八个用文字描述的罗盘方向中做选择，较慢的 Claude 策略师通过 MCP 负责长期规划。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/shantanugoel/mario-jev"><img src="https://opengraph.githubassets.com/1/shantanugoel/mario-jev" alt="Mario + Jev" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/shantanugoel/mario-jev">Mario + Jev</a></b><br><sub>shantanugoel · GitHub · ⭐ 13 · 2026-09-17</sub><br>Python 原型，根据结构化 RAM 观测玩 NES 版 Super Mario Bros. 的 1-1 关，Jev 作答时暂停模拟器，每次决策最多推进四帧。<br><sub><b>Jev 用法:</b> 针对移动、起跳与维持跳跃、低矮天花板下的小跳时机提出聚焦的问题；代码把答案映射成按键。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/qibinlou/status/2100676619815862464"><img src="https://pbs.twimg.com/media/HScaI-sXwAEjjtI.jpg?name=orig" alt="Jev Chess Master" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/qibinlou/status/2100676619815862464">Jev Chess Master</a></b><br><sub>qibinlou · X · ♥ 6 · 2026-09-17</sub><br>实时在线国际象棋游戏，你执白、Jev 执黑，实时显示 Jev 的决策轨迹和 API 花费；需自备 key。<br><sub>相关: <a href="https://jev-chess-master.vercel.app">app</a> · <a href="https://jev-chess-master.vercel.app">project</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/yelkhayami/status/2101944518883037562"><img src="https://pbs.twimg.com/amplify_video_thumb/2100910848029978624/img/NHqTOxDSKfgV7bX1.jpg" alt="Nintendo DS 风格业余游戏" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/yelkhayami/status/2101944518883037562">Nintendo DS 风格业余游戏</a></b><br><sub>yelkhayami · X · ♥ 7 · 2026-09-21</sub><br>用 GPT-6 Astra、Fable 5.1 和 Jev 做的 Nintendo DS 风格业余项目游戏；最新更新加入了 Perry the Platypus，它能把玩家推下悬崖。</td>
</tr>
<tr>
<td width="260" valign="top"></td>
<td valign="top"><b><a href="https://judge-jev.com/">Judge Jev</a></b><br><sub>judge-jev.com · 应用 · ▲ 4</sub><br>无尽的法庭游戏：你拿到五份证据和一次为自己辩解的机会，由 Jev 宣判。<br><sub>相关: <a href="https://news.ycombinator.com/item?id=49778268">discussion</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/OpenDevLog/status/2100743740549702044"><img src="https://pbs.twimg.com/amplify_video_thumb/2100742612332298240/img/frIfXyRp0W_8vWyX.jpg" alt="反向 CAPTCHA" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/OpenDevLog/status/2100743740549702044">反向 CAPTCHA</a></b><br><sub>OpenDevLog · X · ♥ 1 · 2026-09-18</sub><br>半开玩笑的关卡，用五个问题证明你不是人类，Jev 给每个回答分类，一旦认定你是人就打印一张拒绝凭条。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Prophetlab/JevPokerBench"><img src="https://opengraph.githubassets.com/1/Prophetlab/JevPokerBench" alt="JevPokerBench" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Prophetlab/JevPokerBench">JevPokerBench</a></b><br><sub>Prophetlab · GitHub · ⭐ 10 · 2026-09-21</sub><br>面向 Jev 等决策模型的德州扑克基准测试和练习场，有现金局和 sit-and-go 排行榜、手牌回放、建议，还能开桌和模型对打，或让你自己的 agent 入座。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/hota911/status/2101130463037530229"><img src="https://pbs.twimg.com/tweet_video_thumb/HSi0shdboAAf5HG.jpg" alt="Jev 玩 Puyo Puyo" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/hota911/status/2101130463037530229">Jev 玩 Puyo Puyo</a></b><br><sub>hota911 · X · ♥ 3 · 2026-09-19</sub><br>基于 puyoai 引擎的 Puyo Puyo agent，Jev 每一步回答 1+3 个问题：先判断游戏阶段，再判断放置后的最佳结果，最终能打出 3 连锁并击败随机玩家。<br><sub>相关: <a href="https://github.com/puyoai/puyoai">engine</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/sidodtv/status/2101951519373574597"><img src="https://pbs.twimg.com/media/HSuhbq5aMAAOqac.jpg?name=orig" alt="五人制足球模拟器" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/sidodtv/status/2101951519373574597">五人制足球模拟器</a></b><br><sub>sidodtv · X · ♥ 7 · 2026-09-21</sub><br>由 Jev 和 Laya 驱动的高速五人制足球比赛模拟器，9 月 23 日在东京的 Generative AI Anything Exhibition Vol.6 上展出。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/tateko_ai/status/2102073216680546670"><img src="https://pbs.twimg.com/media/HSwQDMIaEAIbJtV.jpg?name=orig" alt="Jev 狼人杀游戏" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/tateko_ai/status/2102073216680546670">Jev 狼人杀游戏</a></b><br><sub>tateko_ai · X · ♥ 1 · 2026-09-21</sub><br>用 Jev 做的狼人杀（社交推理）游戏，是在 gakuse.ai 一场关于如何在 agent harness 里使用 Jev 的学习会之后马上做出来的。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/rottenpen/agent-stardew"><img src="https://raw.githubusercontent.com/rottenpen/agent-stardew/main/assets/visual/app-icon-chicken-whale-v1.png" alt="agent-stardew" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/rottenpen/agent-stardew">agent-stardew</a></b><br><sub>rottenpen · GitHub · ⭐ 9 · 2026-09-19</sub><br>Stardew Valley agent：Jev 围绕用户目标，从动态候选中挑选并执行下一个农场动作，可通过 SMAPI mod、独立 CLI 和带运行面板的 DeepSeek Harness 插件使用。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://askjev.net/"><img src="https://askjev-six.vercel.app/opengraph-image?14b0f74abfc4d228" alt="AskJev" width="240"></a></td>
<td valign="top"><b><a href="https://askjev.net/">AskJev</a></b><br><sub>robherley · 应用 · ▲ 3</sub><br>致敬 Ask Jeeves 的早期网页风格站点：输入一个问题，Jev 回答是或否、从选项中挑一个，或给出一个分数。<br><sub>相关: <a href="https://news.ycombinator.com/item?id=49782388">discussion</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/tvararu/tuicraft"><img src="https://raw.githubusercontent.com/tvararu/tuicraft/main/docs/screenshot.png" alt="tuicraft 的 Jev 战术" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/tvararu/tuicraft">tuicraft 的 Jev 战术</a></b><br><sub>tvararu · GitHub · ⭐ 9 · 2026-02-17</sub><br>在 AzerothCore 服务器上聊天和玩 World of Warcraft 3.3.5a 的终端客户端，其中的 fight 命令由 Jev 从一套精简的技能组里选择战斗战术。<br><sub><b>Jev 用法:</b> Jev 从基于观察到的状态可执行的动作（如法术和方向移动）中做选择；不支持的技能组会停止并说明原因。</sub><br><sub>相关: <a href="https://tuicraft.vararu.org/">app</a> · <a href="https://github.com/tvararu/tuicraft/blob/main/src/wow/jev.ts">code</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/eter_inquirer/status/2102147083491000524"><img src="https://pbs.twimg.com/amplify_video_thumb/2102146909976805376/img/uK50316UXcC168Hp.jpg" alt="国际象棋对比：Jev vs Laya-mix" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/eter_inquirer/status/2102147083491000524">国际象棋对比：Jev vs Laya-mix</a></b><br><sub>eter_inquirer · X · ▶ 404 · 2026-09-21</sub><br>Jev 与本地 Laya-mix 模型之间的国际象棋对局：Laya 更快，但每次都是 Jev 赢。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/comoc/jev-minesweeper"><img src="https://opengraph.githubassets.com/1/comoc/jev-minesweeper" alt="Jev Minesweeper" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/comoc/jev-minesweeper">Jev Minesweeper</a></b><br><sub>comoc · GitHub · ⭐ 8 · 2026-09-20</sub><br>日语浏览器演示，Jev 玩扫雷：每一步在一次请求里为每个紧邻数字的未翻开格子各问一个 Noul，代码按概率翻开或插旗，并以精确求解器兜底。<br><sub><b>Jev 用法:</b> 推测式扇出：在一次请求里为每个边界格子各问一个 Noul（这个格子是雷吗？）。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/hope_rythmn/status/2102178634870264308"><img src="https://pbs.twimg.com/amplify_video_thumb/2102176531561017344/img/DerBafmiiy-MnwvO.jpg" alt="Jev 对战 Laya 玩 Doom" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/hope_rythmn/status/2102178634870264308">Jev 对战 Laya 玩 Doom</a></b><br><sub>hope_rythmn · X · ♥ 8 · 2026-09-21</sub><br>Jev 与开源模型 Laya 的 Doom 1v1 死亡竞赛：Jev 的判断更精准，所需纠正只有对方的三分之一，但 Laya 的决策频率是它的两倍，最终以 5-1 获胜。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Skyvern-AI/jevscape"><img src="https://raw.githubusercontent.com/Skyvern-AI/jevscape/main/docs/media/cover.jpg" alt="jevscape" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Skyvern-AI/jevscape">jevscape</a></b><br><sub>Skyvern-AI · GitHub · ⭐ 8 · 2026-09-18</sub><br>RuneBench 的分支，附带让 Jev 通过约 50 个有边界的 rs-sdk 动作（钓鱼、挖矿、战斗、交易等）玩 RuneScape 的 harness，并有 tick 模式控制器和实时仪表盘。<br><sub><b>Jev 用法:</b> 根据游戏状态，对动作目录、tick 干预和下一次轮询间隔做 Choice；每个动作由代码执行。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/p_misirov/status/2101398305796509718"><img src="https://pbs.twimg.com/media/HSmqn1DbgAAUTrW.png?name=orig" alt="Jev 玩 Pokemon Emerald" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/p_misirov/status/2101398305796509718">Jev 玩 Pokemon Emerald</a></b><br><sub>p_misirov · X · ♥ 3 · 2026-09-19</sub><br>仍在开发中的 harness，在 mGBA 里运行 Pokemon Emerald，用来测试 Jev 玩 Pokemon 能否胜过 LLM。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/benjamincanac/avelune"><img src="https://opengraph.githubassets.com/1/benjamincanac/avelune" alt="Avelune" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/benjamincanac/avelune">Avelune</a></b><br><sub>benjamincanac · GitHub · ⭐ 7 · 2026-07-06</sub><br>运行在 Vercel WebSockets 上的常驻 3D 多人小镇，有一个 AI 神谕 NPC：Jev 读取每一行聊天，判断它是不是在对神谕说话，以及是否在要求改变天气或时间。<br><sub><b>Jev 用法:</b> 针对最后一行聊天记录在一次请求里做四个判断；只有 P(addressed) 达到 0.35 及以上才会触发回复（由 DeepSeek 生成），天空变化则需要 0.5。</sub><br><sub>相关: <a href="https://avelune-online.vercel.app">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/h1bomb/bluff"><img src="https://raw.githubusercontent.com/h1bomb/bluff/main/docs/assets/screenshot_1.png" alt="BLUFF" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/h1bomb/bluff">BLUFF</a></b><br><sub>h1bomb · GitHub · ⭐ 7 · 2026-09-19</sub><br>浏览器里的 roguelike 扑克对决：AI 对手用 Jev 从手牌历史和出手时机中解读玩家意图，成功诈唬让它误判就会触发 Model Break。<br><sub><b>Jev 用法:</b> 每手牌一个在四种行为意图中选择的 Choice，外加判断诈唬和诱敌的 Noul 以及一个激进程度 Score；超时 1,200 毫秒，有启发式兜底。</sub><br><sub>相关: <a href="https://bluffai.vercel.app">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/memgrafter/gliner2-doom"><img src="https://opengraph.githubassets.com/1/memgrafter/gliner2-doom" alt="gliner2-doom" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/memgrafter/gliner2-doom">gliner2-doom</a></b><br><sub>memgrafter · GitHub · ⭐ 7 · 2026-09-18</sub><br>冻结的 GLiNER2.5 文本编码器加一个训练过的小型输出头，在 Mac mini M4 上根据单行 JSON 游戏 state 实时玩 Doom，每秒 35 次给十种动作打分，沿用 Jev 的 state 到 choice 契约。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/HsiangNianian/GlyphWeave"><img src="https://raw.githubusercontent.com/HsiangNianian/GlyphWeave/main/media/map-ansi16-small.png" alt="GlyphWeave 的 Jev 生成" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/HsiangNianian/GlyphWeave">GlyphWeave 的 Jev 生成</a></b><br><sub>HsiangNianian · GitHub · ⭐ 7 · 2026-07-02</sub><br>无限画布的 ASCII roguelike 瓦片地图编辑器，可用 Jev 实时生成地图：由 Jev 从编辑器目录中挑选意图、预设房间、瓦片和摆放位置。<br><sub><b>Jev 用法:</b> Choice 问题的选项限定在目录里的预设和瓦片，另有一个 Noul 判断这次编辑是否会覆盖已有瓦片。</sub><br><sub>相关: <a href="https://glyphweave.hydroroll.team">app</a> · <a href="https://github.com/HsiangNianian/GlyphWeave/blob/main/server/gen-ui.test.mjs">code</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/AbdelStark/heist-one"><img src="https://raw.githubusercontent.com/AbdelStark/heist-one/main/apps/video/out/heist-one-thumbnail.png" alt="HEIST//ONE" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/AbdelStark/heist-one">HEIST//ONE</a></b><br><sub>AbdelStark · GitHub · ⭐ 7 · 2026-09-17</sub><br>浏览器潜行游戏：守卫会对门、灯光、脚步声和工牌做出瞬间判断，你可以查看每个守卫的证据、概率、意图和延迟。<br><sub><b>Jev 用法:</b> Jev 提供类型化的守卫判断；世界状态由确定性代码掌控，并负责兜底。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/teknium1/hermes-and-jev-play-minecraft"><img src="https://opengraph.githubassets.com/1/teknium1/hermes-and-jev-play-minecraft" alt="Hermes 和 Jev 玩 Minecraft" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/teknium1/hermes-and-jev-play-minecraft">Hermes 和 Jev 玩 Minecraft</a></b><br><sub>teknium1 · GitHub · ⭐ 7 · 2026-09-21</sub><br>Minecraft agent：Hermes Agent 负责规划，Jev 每次挑选一个有边界的动作，再由 Mineflayer harness 校验并执行，模型不看截图、也不按键；复现了一次击杀末影龙的流程。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/taodav/jev_deep_rl"><img src="https://raw.githubusercontent.com/taodav/jev_deep_rl/main/media/jev-atari-showcase-no-header.gif" alt="Jev + Gymnasium" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/taodav/jev_deep_rl">Jev + Gymnasium</a></b><br><sub>taodav · GitHub · ⭐ 7 · 2026-09-19</sub><br>在 CartPole、Pong 等 Gymnasium 和 Atari 环境中把 Jev 当作固定策略来评估，不做任何训练，记录其奖励并与固定种子的随机基线对比。<br><sub><b>Jev 用法:</b> 观测适配器把游戏 state 转成 JSON；每一步用一个 Choice 选出一个合法动作。</sub><br><sub>相关: <a href="https://news.ycombinator.com/item?id=49778273">demo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/caijinchun/nanojev-arena"><img src="https://raw.githubusercontent.com/caijinchun/nanojev-arena/main/assets/arena.png" alt="NanoJev Arena" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/caijinchun/nanojev-arena">NanoJev Arena</a></b><br><sub>caijinchun · GitHub · ⭐ 7 · 2026-09-19</sub><br>本地贪吃蛇对战：你和四条 AI 蛇对打，它们由 NanoJev（一个 0.6B 的 Jev 开源复刻）驱动，代码规划器先缩小可选走法，模型的方向概率实时显示。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/lukaske/jev-doom-agent"><img src="https://opengraph.githubassets.com/1/lukaske/jev-doom-agent" alt="PROMPT FPS" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/lukaske/jev-doom-agent">PROMPT FPS</a></b><br><sub>lukaske · GitHub · ⭐ 7 · 2026-09-17</sub><br>两个编译成 WebAssembly 的 Chocolate Doom 引擎并排运行同一张 Freedoom 地图，由 Jev Choice 选择战术宏，本地运动控制器再把它转成 Doom 操作。<br><sub><b>Jev 用法:</b> 根据结构化的生命值、弹药和目标状态对战术宏做 Choice，并实时显示决策遥测。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://jevchess.com"><img src="https://jevchess.com/og.png?room=main&amp;v=81-41" alt="Jev Chess" width="240"></a></td>
<td valign="top"><b><a href="https://jevchess.com">Jev Chess</a></b><br><sub>sliday · 应用 · ♥ 1</sub><br>全网玩家共用一张棋盘对战 Jev；它一次性权衡所有合法走法，因此不可能走出非法的一步。<br><sub><b>Jev 用法:</b> 每个合法走法都是同一个 Choice 的选项；返回的概率用来给棋子着色，实时面板用一个单层（one-ply）引擎检验它的校准。</sub><br><sub>相关: <a href="https://x.com/staskulesh/status/2102052244363317752">demo</a> · <a href="https://www.reddit.com/r/LLMDevs/comments/1wmf8wh/i_built_a_shared_chessboard_where_everyone_plays/">discussion</a> · <a href="https://x.com/staskulesh/status/2102062632517697652">demo 2</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/enoyola/jev-grand-prix"><img src="https://opengraph.githubassets.com/1/enoyola/jev-grand-prix" alt="Jev Grand Prix" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/enoyola/jev-grand-prix">Jev Grand Prix</a></b><br><sub>enoyola · GitHub · ⭐ 6 · 2026-09-20</sub><br>F1 赛车游戏：Jev 实时选择行车线和踏板输入，转向和规划由代码负责，它会在圈与圈之间学习每个弯道的极限，你也可以用方向键和它比赛。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://www.reddit.com/r/ArtificialInteligence/comments/1wkjatd/i_hooked_jev_up_to_slay_the_spire_2_it_made_it_to/"><img src="https://external-preview.redd.it/NDM2MzNzcGFsZ3FoMRVX0gr1QcHBMnu7HTuOq0-1UwoVsYJY79bqH7PNNhxN.png?format=pjpg&amp;auto=webp&amp;s=ab8dc1a2c2d94dfbe2220e7aa434e6a4d727fba2" alt="Jev 玩 Slay the Spire 2" width="240"></a></td>
<td valign="top"><b><a href="https://www.reddit.com/r/ArtificialInteligence/comments/1wkjatd/i_hooked_jev_up_to_slay_the_spire_2_it_made_it_to/">Jev 玩 Slay the Spire 2</a></b><br><sub>Zboubkiller · Reddit · ▲ 2 · 2026-09-19</sub><br>桥接程序从本地 mod 服务器读取 Slay the Spire 2 的实时状态，再问 Jev 最佳的卡牌、道具或行动；约一小时、花三美分就打到了第一个 boss。<br><sub><b>Jev 用法:</b> 每隔几秒对合法行动做一个 Choice，每次决策两三百毫秒。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/smartaces/jev-plays-streetfighter-2"><img src="https://external-preview.redd.it/NTVkZTJiN3R4bXFoMQjvd-8EQw0QbDjm9hCjKpnf4X5aCCr61OBuvtMnbJcC.png?format=pjpg&amp;auto=webp&amp;s=0a204302132cb05408f3a8a913bb8c1812c9679a" alt="Jev 玩 Street Fighter II" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/smartaces/jev-plays-streetfighter-2">Jev 玩 Street Fighter II</a></b><br><sub>smartaces · GitHub · ⭐ 6 · 2026-09-19</sub><br>让 Jev 在 Mac 模拟器上用 Ryu 玩 Street Fighter II 的 agent：游戏 RAM 转成结构化观测，Jev 选择招式和力度，本地控制器执行按键，仪表盘展示它的选择。<br><sub>相关: <a href="https://www.reddit.com/r/typesafe_ai/comments/1wlbfl2/updated_jev_plays_streetfighter_2_improved_play/">demo</a> · <a href="https://www.reddit.com/r/OpenAI/comments/1wlbji2/ai_plays_streetfighter_2_in_real_time/">discussion</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/valentynkit/jev-plays-pokemon-red"><img src="https://raw.githubusercontent.com/valentynkit/jev-plays-pokemon-red/main/demo/overlay.gif" alt="jev-plays-pokemon-red" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/valentynkit/jev-plays-pokemon-red">jev-plays-pokemon-red</a></b><br><sub>valentynkit · GitHub · ⭐ 6 · 2026-09-18</sub><br>PyBoy 上的 Pokémon Red agent：路线和算术由 Python 负责，Jev 只在真正的分岔点从合法动作中做选择，耗时约 100 毫秒。<br><sub><b>Jev 用法:</b> 每个分岔点对合法动作做一个 Choice；战斗回合额外加上 faints_this_turn 和 should_flee 两个 Noul，失败时回退到代码默认值。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/ashkans_dev/status/2101014737383206914"><img src="https://pbs.twimg.com/amplify_video_thumb/2101014607875686400/img/MsxqI3XpdHm0XxmL.jpg" alt="大规模 Jev 解谜器" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/ashkans_dev/status/2101014737383206914">大规模 Jev 解谜器</a></b><br><sub>ashkans_dev · X · ♥ 1 · 2026-09-18</sub><br>Jev 大规模批量解逻辑游戏，其中数独明显比其他游戏耗时更长。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/sid19arya0/status/2100458351440048258"><img src="https://pbs.twimg.com/amplify_video_thumb/2100458327918395392/img/vdl_EhR4xNaDDN1-.jpg" alt="Jev 对战 Opus 5 打 Pokémon" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/sid19arya0/status/2100458351440048258">Jev 对战 Opus 5 打 Pokémon</a></b><br><sub>sid19arya0 · X · ♥ 5 · 2026-09-17</sub><br>Jev 与 Opus 5 的 Pokémon 竞技对战，Jev 获胜，花费 $0.0029、用时 37 秒，对方则花费 $2.35、用时 6 分 29 秒。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/realdora_eth/status/2102036344130191370"><img src="https://pbs.twimg.com/amplify_video_thumb/2102035915497476096/img/NzSS4-InwFUwSJf4.jpg" alt="Jev 玩俄罗斯方块" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/realdora_eth/status/2102036344130191370">Jev 玩俄罗斯方块</a></b><br><sub>realdora_eth · X · ♥ 2 · 2026-09-21</sub><br>把俄罗斯方块接到 Jev 上，每个方块落在哪都由它决定。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/bytelabs-oss/clash-jev"><img src="https://opengraph.githubassets.com/1/bytelabs-oss/clash-jev" alt="clash-jev" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/bytelabs-oss/clash-jev">clash-jev</a></b><br><sub>bytelabs-oss · GitHub · ⭐ 5 · 2026-09-21</sub><br>不需要训练策略的 Clash Royale 机器人，在真实 Android 设备上对战：OpenCV 加一个小型兵种分类器把屏幕转成 JSON state，Jev 约 135 毫秒 选出每一步操作。<br><sub>相关: <a href="https://bytelabs-oss.github.io/clash-jev/">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/get-convex/convex-chess"><img src="https://opengraph.githubassets.com/1/get-convex/convex-chess" alt="Convex Chess 的走法评分" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/get-convex/convex-chess">Convex Chess 的走法评分</a></b><br><sub>get-convex · GitHub · ⭐ 5 · 2023-02-28</sub><br>基于 Convex 的国际象棋示例：每一步新走法都会通过 Convex AI Gateway 由 Jev 1.13 给出 1-10 分，显示在走法解说下方；这是 AI 估计，不是引擎评估。<br><sub><b>Jev 用法:</b> 通过 AI SDK 的评估接口，每步走法按十级评分细则做一个 Score。</sub><br><sub>相关: <a href="https://convex-chess.vercel.app">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/jammaru/jev-lab"><img src="https://opengraph.githubassets.com/1/jammaru/jev-lab" alt="Jev Lab" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/jammaru/jev-lab">Jev Lab</a></b><br><sub>jammaru · GitHub · ⭐ 5 · 2026-09-17</sub><br>两个本地实验室，Jev 只负责挑选下一个合法动作，规则由引擎维护：一个是 Hundred，由 100 个有饥饿、金钱、工作和记忆的 NPC 组成的小镇；另一个是木制棋盘的 Jev Shogi（将棋）。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/oldmoldycake/jev_vampire_survivors"><img src="https://external-preview.redd.it/dWUzcjQ5cjkxZnFoMWL026_E1HhdGexzA7VRvD--pc7oUJywn19Lddex_9NQ.png?format=pjpg&amp;auto=webp&amp;s=5a373e6177ec43dbe016271a05c85291cb4dcb91" alt="Jev 玩 Vampire Survivors" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/oldmoldycake/jev_vampire_survivors">Jev 玩 Vampire Survivors</a></b><br><sub>oldmoldycake · GitHub · ⭐ 5 · 2026-09-18</sub><br>BepInEx 插件加 Python 大脑，让 Jev 玩真正的 Steam 版游戏：选择角色、关卡和每次升级，并以每秒四次的频率决定行走方向，附带实时仪表盘。<br><sub><b>Jev 用法:</b> 游戏状态被转换成简单的英文问题；没有硬编码任何针对这款游戏的策略。</sub><br><sub>相关: <a href="https://www.reddit.com/r/typesafe_ai/comments/1wkdukw/letting_jev_play_some_vampire_survivors/">demo</a> · <a href="https://www.reddit.com/r/ClaudeAI/comments/1wke35a/used_claude_to_help_jev_become_a_gamer/">discussion</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/leftspace89/JevBird"><img src="https://raw.githubusercontent.com/leftspace89/JevBird/main/demo/jev_demo.gif" alt="JevBird" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/leftspace89/JevBird">JevBird</a></b><br><sub>leftspace89 · GitHub · ⭐ 5 · 2026-09-17</sub><br>Jev 实时玩的 Pygame 版 Flappy Bird：每来一根新管道，游戏就模拟出一组穿过缝隙的飞行路径，由 Jev 选出小鸟飞哪一条。<br><sub><b>Jev 用法:</b> 每根管道对模拟轨迹做一个 Choice，大约每根管道一次 API 调用；所选路径上的每次振翅由游戏安排。</sub></td>
</tr>
</table>

<details><summary>还有 126 条</summary>

- **[Jeven Doors](https://x.com/uehaj/status/2101928834820165661)** · <sub>uehaj · X · ♥ 1 · 2026-09-21</sub><br>猜谜游戏：你有 7 个是非题来找出 Jev 心里想的答案；这次更新支持创建和上传自己的题材，并接入 WebMCP，让 agent 也能生成题材。
- **[机器人对战格斗游戏](https://x.com/a_captaincook/status/2102205359100457023)** · <sub>a_captaincook · X · ♥ 4 · 2026-09-22</sub><br>与 Astra 一起设计的格斗游戏，由 Jev 驱动的机器人互相对打，作者计划加入 RL 循环来进化出最强的斗士。
- **[DOOM-JEV](https://github.com/AmoghCreator/doom-jev)** · <sub>AmoghCreator · GitHub · ⭐ 4 · 2026-09-17</sub><br>自主 ViZDoom agent：以原生 35 ticks/s 运行 Doom，同时以约 10 Hz 的频率异步向 Jev 询问移动、目标和开火决策，配有 Rich 终端 HUD。
- **[jev-plays-pokemon](https://github.com/milanboers/jev-plays-pokemon)** · <sub>milanboers · GitHub · ⭐ 4 · 2026-09-17</sub><br>在 PyBoy 模拟器上运行的自主 Pokémon Red agent，把游戏 RAM 和屏幕对话转成文本快照，由 Jev 选择每一次按键。
- **[分类器维基百科竞速](https://x.com/dave_xt/status/2100723103143997510)** · <sub>dave_xt · X · ▶ 178 · 2026-09-17</sub><br>Web 应用：Jev 实时从一篇 Wikipedia 文章跳转竞速到另一篇，全程没有 LLM 参与，并展示每一步的 state、问题和动作。
- **[MineAI 的 Jev 决策](https://github.com/ailiujiarui/MineAI/blob/main/src/main/java/com/mineai/llm/TypesafeDecisionProvider.java)** · <sub>ailiujiarui · GitHub · ⭐ 65 仓库 · 2026-04-22</sub><br>Minecraft Forge mod，内含自主假玩家 agent，在确定性编译器和可执行技能之外加了一层 TypeSafe Jev 判断。
- **[Jev Chess](https://github.com/choxos/jevchess)** · <sub>choxos · GitHub · ⭐ 3 · 2026-09-19</sub><br>单页 Web 应用：Jev 可以和任意 OpenRouter LLM、Stockfish 或你对弈，界面展示它权衡过的走法及对应概率，并保存棋局和胜率。
- **[Jev 玩 Clash Royale](https://github.com/vishxrad/clashroyale-jev)** · <sub>vishxrad · GitHub · ⭐ 3 · 2026-09-20</sub><br>靠截图驱动的 Clash Royale 机器人：Jev 决定出哪张卡、放在哪，Cerebras 上的 Qwen 3.8 27B 读取战场，OpenCV 识别手牌和圣水，通过 ADB 在 Android 上对战。
- **[JevEmon](https://github.com/daniel4x/JevEmon)** · <sub>daniel4x · GitHub · ⭐ 3 · 2026-09-21</sub><br>Jev 在真实的 Pokémon FireRed ROM 里跑图：代码从 RAM 读取大地图并列出可达目的地，Jev 选一个并应对野外遭遇战，目前已到达 Viridian City。
- **[和 Jev 实时下棋](https://x.com/itspraveeny/status/2101333228808499692)** · <sub>itspraveeny · X · ♥ 3 · 2026-09-19</sub><br>Chrome 扩展抓取实时棋盘和走棋历史，发给本地后端，由 Jev 选择下一步，不借助 Stockfish；之后还拿更强的机器人测试过。
- **[rubikjev](https://github.com/0xtrou/rubikjev)** · <sub>0xtrou · GitHub · ⭐ 3 · 2026-09-17</sub><br>单页魔方练习场：你打乱魔方后，Jev 用梗图等级、1-5 星难度和一段吐槽来评价混乱程度，然后在 3D 中一步步还原。
- **[Soupbase](https://github.com/spoonnotfound/soupbase)** · <sub>spoonnotfound · GitHub · ⭐ 3 · 2026-09-19</sub><br>中英双语的海龟汤（横向思维谜题）网站，由 Jev 担任主持人，回答玩家的提问并给他们还原的故事打分。
- **[Temporal 井字棋 agent](https://github.com/temporal-community/temporal-agent-harness/tree/main/examples/tictactoe)** · <sub>temporal-community · GitHub · ⭐ 58 仓库 · 2026-06-18</sub><br>没有 LLM 的游戏 agent：一个 Choice 选格子，几个 Noul 发现威胁，一个 Score 评估局面。
- **[vibedgames 模型试玩器](https://github.com/kyh/vibedgames/tree/main/apps/cli/src/lib/playtest)** · <sub>kyh · GitHub · ⭐ 57 仓库 · 2020-01-26</sub><br>面向编程 agent 的游戏工作室工具包，其中 vg playtest run 用 TypeSafe System One 驱动游戏角色，每个 tick 一次决策，经服务器代理转发。
- **[HarnessRouter 的超级马里奥套件](https://github.com/HarnessRouter/starter-kit/tree/main/kits/mario)** · <sub>HarnessRouter · GitHub · ⭐ 54 仓库 · 2026-08-03</sub><br>入门套件：一个 System One 模型在无头浏览器里玩 Full Screen Mario，每秒决策数次，把游戏 state 当作几句字面描述来读，并选择一个操作。
- **[Jev 玩 Pokémon Showdown](https://x.com/Izzuddin_Shafi/status/2101116220061958528)** · <sub>Izzuddin_Shafi · X · ♥ 1 · 2026-09-19</sub><br>用 Codex 搭建的 Pokémon Showdown harness，Jev 能很快打完一整场，但决策质量参差不齐，以附带决策数据和延迟的回放形式展示。
- **[Covel 的 Jev Choice 演示](https://github.com/ackness/covel/tree/main/plugins/jev-choice-demo)** · <sub>ackness · GitHub · ⭐ 51 仓库 · 2026-03-24</sub><br>agent 化 AI RPG 框架的可选插件：每回合显示评估模型对每个快捷回复选项的推荐概率，但不替玩家做选择。
- **[Aiko-chan 的 Jev 将棋](https://github.com/OppaAI/Aiko-chan/blob/dev/agentic/toolkit/jev.py)** · <sub>OppaAI · GitHub · ⭐ 49 仓库 · 2026-05-28</sub><br>带 VRM 形象的本地 AI 伙伴，用 Jev 下将棋：在候选着法中选择并复盘局面，还包含一个自对弈引擎。
- **[Jev 俄罗斯方块自动玩家](https://x.com/lostingz001/status/2101934790018773143)** · <sub>lostingz001 · X · ♥ 1 · 2026-09-21</sub><br>中文俄罗斯方块演示：每回合把棋盘、空洞和合法落点打包成 JSON，一次 Jev 请求就回答旋转和列、是否暂存以及 0-4 的危险分数，每步约 300 毫秒。
- **[Jev Minecraft 机器人](https://x.com/akashpurjalkar/status/2102014492217667872)** · <sub>akashpurjalkar · X · ♥ 2 · 2026-09-21</sub><br>按指令建造房屋、塔楼、湖泊和城堡的 Minecraft 机器人，还能用剑和怪物战斗，同时实时躲避骷髅射来的箭。
- **[Jev Reasoner Battleship](https://github.com/russellballestrini/opencompletion/blob/main/jev_hunter.py)** · <sub>russellballestrini · GitHub · ⭐ 41 仓库 · 2023-10-28</sub><br>OpenCompletion 多用户 LLM playground 中的海战棋瞄准玩家：把精确的舰船放置密度网格与每回合一次、针对最佳候选格的 Jev 决策融合，并在五名舰队司令的竞技场里做基准测试。
- **[Jev 2048](https://github.com/ARCJ137442/jev-2048)** · <sub>ARCJ137442 · GitHub · ⭐ 2 · 2026-09-20</sub><br>带完整监测的 2048 网页实验室：每一步都是 Jev 在四个方向中做的一个 Choice，没有启发式兜底，并实时显示概率、置信度、延迟和成本。
- **[Jev Arena (NanoJev)](https://github.com/liao96312/jev-arena-nanojev)** · <sub>liao96312 · GitHub · ⭐ 2 · 2026-09-19</sub><br>完全本地运行的 Pygame 网格战术游戏：开源 Jev 复刻 NanoJev 在难度递增的关卡中，从真实的候选动作里挑选每一次移动、攻击、射击、治疗或冲刺，训练在 GTX 1660S 上完成。
- **[Jev Broadcast Lab](https://github.com/4anti/jev-broadcast-lab)** · <sub>4anti · GitHub · ⭐ 2 · 2026-09-17</sub><br>公开实验室：一场国际象棋对局中，Jev 从本地生成的合法走法里选一步，旁边同步显示 Stockfish 评分；另有几个小型判断展台和一份 Fast Flag 目录。
- **[Jev 子弹棋测试](https://x.com/bariskisir/status/2101531039185129683)** · <sub>bariskisir · X · ♥ 2 · 2026-09-20</sub><br>把 Jev 放进国际象棋机器人里做的子弹棋测试，结果连 250 ELO 的电脑对手都没赢下。
- **[Jev cloud quiz](https://github.com/minorun365/jev-cloud-quiz)** · <sub>minorun365 · GitHub · ⭐ 2 · 2026-09-20</sub><br>日语问答演示：从 30 个去掉品牌词的 AWS、Azure 或 Google Cloud 功能名里选一个，由 Jev 猜它属于哪家云，并把概率画成三根柱子。
- **[Jev 玩 Clash Royale（jev-royal）](https://github.com/Amrit-Nigam/jev-royal)** · <sub>Amrit-Nigam · GitHub · ⭐ 2 · 2026-09-17</sub><br>在 macOS 上通过 iPhone Mirroring 运行的自主 Clash Royale agent，先从像素做本地确定性感知，再由 Jev 在代码已验证过的战术选项之间裁决。
- **[Jev 玩 RALLY](https://github.com/Icohen007/jev-play-ping-pong)** · <sub>Icohen007 · GitHub · ⭐ 2 · 2026-09-17</sub><br>Jev 根据结构化遥测数据实时玩一款在线浏览器乒乓球游戏，每次发球和回球都由它决定，并通过普通的 Chrome 输入移动球拍；一局录制的 Club 难度对局以 11-0 结束。
- **[Jev 玩贪吃蛇](https://jevplayssnake.lovable.app/)** · <sub>Carol Monroe · 应用 · ♥ 2</sub><br>贪吃蛇游戏：Jev 在每个岔路口选择方向并显示它有多确定；你可以用方向键推翻它的决定、让它自己玩，或在不同手机上和它比赛。
- **[jev-chess](https://github.com/hemanth/jev-chess)** · <sub>hemanth · GitHub · ⭐ 2 · 2026-09-19</sub><br>国际象棋库：把自然语言的走棋意图解析成合法走法，从尖锐度、主题和王的风险等方面评估候选走法，还能扮演基于人设的对手。
- **[Jev-GamePilot](https://github.com/newuser7171/jev-gamepilot)** · <sub>newuser7171 · GitHub · ⭐ 2 · 2026-09-19</sub><br>面向 Windows PC 游戏和 Android 手机的游戏 agent：捕获游戏画面，把本地 Laya 的反射式反应和 Jev 的策略结合起来，再发送输入，内置 Clash Royale、国际象棋、Dino 和卡牌游戏的适配器。
- **[jev2048](https://github.com/erhanmeydan/jev2048)** · <sub>erhanmeydan · GitHub · ⭐ 2 · 2026-09-18</sub><br>让 Jev 在真实的 2048 在线网站上玩 2048 的 agent，每一步一次 API 调用，终端里显示四个方向各自的校准概率。
- **[JevBall](https://github.com/atarikcaliskan/jevball)** · <sub>atarikcaliskan · GitHub · ⭐ 2 · 2026-09-19</sub><br>3D 球场里的足球比赛：22 名球员各自是独立的 Jev 决策者，每秒几次从本地算出的最多 14 个选项中挑一个；你可以观战、查看某名球员，或接管其中一名。
- **[Model Kombat](https://github.com/lavallee/mk-jev-fly-brain)** · <sub>lavallee · GitHub · ⭐ 2 · 2026-09-18</sub><br>一个 12,000 个神经元的果蝇大脑连接组模拟，在 mk.js 街机格斗游戏里对战 Jev，附有十三个有记录的实验和 84 场存档比赛的排名。
- **[ORIGIN / CIVILIZATION](https://github.com/JacquesGariepy/ORIGIN-CIVILIZATION)** · <sub>JacquesGariepy · GitHub · ⭐ 2 · 2026-09-19</sub><br>生命与文明模拟：每个人的下一个自主行动都是一次 Jev Choice，作为凭证记入账本；可选的 LLM 规划器可以提出目标和发言，但从不做决定。
- **[tsai-civ2](https://github.com/phyous/tsai-civ2)** · <sub>phyous · GitHub · ⭐ 2 · 2026-09-16</sub><br>实验性 harness，让 Jev 在浏览器中通过屏幕像素和键鼠输入玩初代 Civilization II，观众可实时看到各个动作的概率。
- **[TypeSafe Chess](https://github.com/Dimesio/typesafe-chess)** · <sub>Dimesio · GitHub · ⭐ 2 · 2026-09-19</sub><br>测试 Jev 下棋水平的本地应用：chess.js 列出合法走法，Jev 挑一个，Stockfish 给每次选择打分，还有可选的课程等级，把 Jev 自己被打过分的失误喂回给它。
- **[和 Jev 下国际象棋](https://x.com/theshajha/status/2101905184704323969)** · <sub>theshajha · X · ▶ 96 · 2026-09-21</sub><br>一个棋盘，你可以和作为对手的 Jev 下一局国际象棋。
- **[Jev 读心精灵](https://x.com/builderix/status/2101972512644948169)** · <sub>builderix · X · ♥ 1 · 2026-09-21</sub><br>Akinator 式猜人游戏：花 9 分钟、$1.13 预先算好 2,125,999 个 Jev 判断（16,229 个角色 x 131 个是非题），之后游玩只需简单算术。
- **[Jev Connections 解题器](https://github.com/matsonj/eval-connections/blob/main/experimental/jev_classic_solver.py)** · <sub>matsonj · GitHub · ⭐ 25 仓库 · 2025-07-31</sub><br>NYT Connections LLM 评测中的实验性解题器：问 Jev 词对和候选词组是否属于同一组，然后在四次失误的上限内搜索最优的四个分组。
- **[Agent JEV Tetris](https://github.com/Yasserbhb/Agent-JEV-Tetris)** · <sub>Yasserbhb · GitHub · ⭐ 1 · 2026-09-17</sub><br>俄罗斯方块：每一步都是 Jev 在七个合法走法中做的一个 Choice，计算交给游戏代码；演示中放下 363 块、消除 114 行，且没有留下一个空洞。
- **[Fly vs Jev: Minesweeper](https://github.com/EnesYilmazcode/JevMinesweeper)** · <sub>EnesYilmazcode · GitHub · ⭐ 1 · 2026-09-20</sub><br>让一个含 166,700 个神经元的模拟果蝇连接组和 Jev 比赛初级扫雷，双方都只能看到已翻开的线索。
- **[JEV Prix](https://github.com/MartinPuli/f1)** · <sub>MartinPuli · GitHub · ⭐ 1 · 2026-09-18</sub><br>赛车展示：Jev 在陌生的程序化生成赛车道上驾驶五辆车，配有十种车手提示词、30 场录制比赛、3D 回放，以及比较不同策略的排行榜。
- **[Jev Snake](https://github.com/iammusham/jev-snake)** · <sub>iammusham · GitHub · ⭐ 1 · 2026-09-17</sub><br>贪吃蛇环境：Python 引擎负责规则，Jev 每个 tick 根据结构化状态选择方向，附带浏览器端的人类基线和 pygame 客户端；引擎从不推翻 Jev 的选择。
- **[JEV SPEED](https://github.com/tubone24/jev-practice-speed)** · <sub>tubone24 · GitHub · ⭐ 1 · 2026-09-19</sub><br>WebGL 卡牌游戏 Speed，对手 CPU 的大脑是 Jev，用来实时展示决策速度和准确率：每回合为每种手牌与牌堆的组合各问一个 Noul，再用一个 Choice 决定出牌，规则由代码保证。
- **[JEV Tetris](https://github.com/thelau/jev-tetris)** · <sub>thelau · GitHub · ⭐ 1 · 2026-09-19</sub><br>俄罗斯方块：代码找出所有可达的落点（包括塞缝和旋转），并把每个落点描述成一句话；Jev 用一个 Choice 选出一个，棋盘会按完整的概率分布发光。
- **[jev-connect4](https://github.com/hazlema/jev-connect4)** · <sub>hazlema · GitHub · ⭐ 1 · 2026-09-21</sub><br>网页版四子棋对战 Jev，同一模型有九种可切换的查询策略，实时检查器用引擎真值给每个答案打分，对局运行器每分钟能下 100 局。
- **[jev-gomoku](https://github.com/XieChengYuan/jev-gomoku)** · <sub>XieChengYuan · GitHub · ⭐ 1 · 2026-09-18</sub><br>中文 15x15 五子棋实验室，同时运行九个棋盘，两个 Jev 棋手在不同输入方案下交换执子颜色，每次请求、每个选项的概率和每一步都可查看，并提供无需 key 的回放。
- **[jev-zork](https://github.com/Resadan-dev/jev-zork)** · <sub>Resadan-dev · GitHub · ⭐ 1 · 2026-09-21</sub><br>Jev 玩 Zork I：每一回合由 Jericho 提供有效动作，Jev 用一个 Choice 选出一条指令，法语回放仪表盘会显示它的置信度和防循环策略。
- **[Jev2048](https://github.com/KyleKreuter/jev2048)** · <sub>KyleKreuter · GitHub · ⭐ 1 · 2026-09-17</sub><br>浏览器实验室：Jev 并行玩多局 2048，每一步一个 Choice，实时追踪最高分，你还可以修改状态格式、棋盘编码和选择标准。
- **[jevchat](https://github.com/kt3k/jevchat)** · <sub>kt3k · GitHub · ⭐ 1 · 2026-09-18</sub><br>ChatGPT 风格的聊天界面，Jev 从不写文字，而是从 Yes/No、Maybe、Pirate、Tabloid 或自定义答案集中挑选回答，连聊天标题都是从你问题的片段里挑出来的。
- **[Magic-8-Jev](https://github.com/willprout/magic-8-ball)** · <sub>willprout · GitHub · ⭐ 1 · 2026-09-18</sub><br>极简的魔术 8 号球网页玩具：一个 Cloudflare Worker 对二十个经典答案发起一次 Jev Choice，球上显示选中的回答，以及实测的从点击到出答案的延迟。
- **[从名字猜年龄段](https://github.com/ximhear/jev-kr-name-age)** · <sub>ximhear · GitHub · ⭐ 1 · 2026-09-18</sub><br>小型 React 应用：选择韩国、美国、日本或中国，输入一个名字，Jev 根据起名趋势猜出这个人的年龄段和性别。
- **[TypeSafe 玩 Minecraft](https://github.com/ellistev/typesafe-minecraft-demo)** · <sub>ellistev · GitHub · ⭐ 1 · 2026-09-16</sub><br>Minecraft Java 版机器人，每次 Jev 决策为 Mineflayer 选择一个原语（250 毫秒 的移动、转向、挖或放一个方块、装备、等待），并在旁边展示原始 API 输入输出，演示它搭建一面加拿大国旗。
- **[Jev 下五子棋](https://x.com/GodName794/status/2102199799160475707)** · <sub>GodName794 · X · ▶ 49 · 2026-09-22</sub><br>五子棋实验：Jev 单独决策时输了，但先用攻防搜索筛出候选走法、再让 Jev 从中挑选后，它赢了作者。
- **[Jev Mario Lab](https://x.com/umezawakanta13/status/2102062482991001689)** · <sub>umezawakanta13 · X · ▶ 46 · 2026-09-21</sub><br>Jev 在浏览器里玩马里奥风格的 World 1-1；这段录屏在第一个敌人处就死了，作者报告 5 次响应的浏览器往返延迟中位数为 976.8 毫秒。
- **[Genesis Initiative 的 NPC Jev 调度器](https://github.com/dyzdyz010/ex_mmo_cluster/tree/master/apps/gate_server/lib/gate_server/npc)** · <sub>dyzdyz010 · GitHub · ⭐ 18 仓库 · 2021-02-26</sub><br>体素 MMO 服务器 Genesis Initiative 中的 NPC 调度器：Jev 为每个 NPC 挑选下一项活动，并检查某个动作会不会破坏别人的建筑；在 70 个用例的评测中拿到 70/70，p50 延迟 0.78 s，而 LLM 为 2.67 s。
- **[XRENGINE 的 Jev 场景指令](https://github.com/BlackJaxDev/XRENGINE/blob/master/XREngine.Editor/Mcp/Actions/EditorMcpActions.TypeSafe.cs)** · <sub>BlackJaxDev · GitHub · ⭐ 17 仓库 · 2023-06-12</sub><br>XRENGINE C# VR 游戏引擎中的编辑器 MCP 动作，用 Jev 把“select player node”这类自然语言场景指令解析成建议的 MCP 命令和目标节点，以模式匹配作为兜底。
- **[专为 Jev 做的游戏](https://x.com/Icaro_333/status/2102242170191179948)** · <sub>Icaro_333 · X · ▶ 41 · 2026-09-22</sub><br>专门做给 Jev 玩的小游戏，是作者在学习这个模型如何工作时做的。
- **[Jev Tetris](https://x.com/wellback000/status/2101931130731852088)** · <sub>wellback000 · X · ▶ 39 · 2026-09-21</sub><br>由 Jev 来玩的俄罗斯方块游戏，以短视频展示。
- **[Jev Mario Lab](https://x.com/umezawakanta13/status/2102008904842658002)** · <sub>umezawakanta13 · X · ▶ 36 · 2026-09-21</sub><br>Jev 玩马里奥风格 1-1 的后续延迟测试，带测量浮层：浏览器往返中位数 1,139.7 毫秒，Jev HTTP 往返 490.3 毫秒，依然死在第一个敌人手上。
- **[Judicious Jev](https://github.com/coreyja/battlesnake-rs/tree/main/web-axum/src/judicious_jev)** · <sub>coreyja · GitHub · ⭐ 11 仓库 · 2021-02-20</sub><br>Battlesnake 机器人，用一个 TypeSafe Choice 问题选择每一步，失败时回退到本地策略，并记录每局成本。
- **[SimTracker 的 Jev 路径](https://github.com/prolix-oc/Lumiverse-SimTracker/blob/main/src/typesafe.ts)** · <sub>prolix-oc · GitHub · ⭐ 11 仓库 · 2026-03-08</sub><br>Lumiverse 的角色扮演追踪器扩展，用 Jev 跳过不必要的追踪器更新、切换状态标记、对照剧情校验 LLM 生成的追踪字段，以及估算受孕几率。
- **[Jev 对战 Maia-1100](https://x.com/MarcosPimi/status/2102079921388409005)** · <sub>MarcosPimi · X · ▶ 25 · 2026-09-21</sub><br>与 Lichess 上模仿初学者风格的 Maia-1100 机器人下了十盘棋：Jev 只拿到 0.5 分，找到最佳将军的比例是 100%，找到最佳安静着法的比例却只有 39%。
- **[ModlessChatTrans 消息分类器](https://github.com/LiJiaHua1024/ModlessChatTrans/blob/main/src/modless_chat_trans/message_classifier.py)** · <sub>LiJiaHua1024 · GitHub · ⭐ 9 仓库 · 2024-06-20</sub><br>实时 Minecraft 聊天翻译器，无需 mod 即可读取游戏日志，并可用 Jev 判断哪些日志行是值得翻译的玩家聊天。
- **[比分条复刻工作台](https://github.com/cruuz/2k-football-mod-tools/tree/main/tools/scorebug_sprite/jev)** · <sub>cruuz · GitHub · ⭐ 8 仓库 · 2026-07-23</sub><br>经典 2K 橄榄球游戏 mod 编辑器里的诊断工作台，让 Jev 对渲染出的比分条与游戏内比分条之间测得的差异做分类，比如色调不对或元素错位。
- **[natural_20 的 Jev NPC 战斗 AI](https://github.com/jedld/natural_20.py/blob/master/docs/JEV_NPC_BATTLE_AI.md)** · <sub>jedld · GitHub · ⭐ 7 仓库 · 2024-02-13</sub><br>natural_20 是用于 AI 研究的 D&amp;D 5e 游戏引擎，这是其中负责 NPC 战斗的 Jev provider，逐层遍历动作树（动作类型、武器或法术、目标、目的格）来构建完整的合法动作。
- **[用 Jev 玩 Atari Pong](https://x.com/MemorysaverMFA/status/2100881912113909893)** · <sub>MemorysaverMFA · 文章 · ▶ 15 · 2026-09-18</sub><br>文章介绍如何把 Jev 用作 Atari Pong 的策略型控制器，策略写在问题定义里，而不是模型权重里。
- **[open-pokered 的 Jev 自主通关](https://github.com/liuyanghejerry/open-pokered/blob/master/docs/jev-autonomous-retrospective.md)** · <sub>liuyanghejerry · GitHub · ⭐ 6 仓库 · 2026-08-09</sub><br>双层 Jev agent，从真正的 NEW GAME 开始把 Pokemon Red 的 Rust 复刻版一路打到完整结局，没有照抄预设路线，并在独立进程中重新加载存档做了验证。
- **[Magic-Jev-Ball](https://github.com/rorz/rorz.io/tree/main/apps/jevball)** · <sub>rorz · GitHub · ⭐ 5 仓库 · 2026-07-10</sub><br>由 Jev 驱动的魔术 8 号球小玩具，用 React、Vite 和 Cloudflare Workers 构建，作为一个小应用托管在 rorz.io 个人网站的 monorepo 中。
- **[与 Jev 对弈的国际象棋 playground](https://x.com/ezeugo__/status/2102207212986724814)** · <sub>ezeugo__ · X · ▶ 9 · 2026-09-22</sub><br>和 Jev 下国际象棋的 playground：每一回合，Jev 以 state 的形式接收棋盘，所有合法走法作为一个 Choice；结果嘛，还算不上 AGI。
- **[AskJev (Reverse Akinator)](https://askjev.app/)** · <sub>askjev.app · 应用</sub><br>每日一局的反向 Akinator 游戏：你向 Jev 提是非题来猜出神秘角色；非官方演示。
- **[Autonomous PS2 AI Agent](https://github.com/opaielsheikh/ps2-ai-agent)** · <sub>opaielsheikh · GitHub · 2026-09-17</sub><br>PlayStation 2 模拟器 agent：截取画面帧、提取场景遥测数据，向 Jev 提一个 Choice（加速、转向、刹车、攻击），结果作为虚拟手柄输入注入游戏，并配有实时遥测 HUD。
- **[Beat Jev](https://github.com/ojusave/beat-jev)** · <sub>ojusave · GitHub · 2026-09-18</sub><br>与 Jev 进行点球大战，轮流射门和扑救；每场比赛由一个 Render Workflows 任务负责，比分存入 Render Postgres，提供 TypeScript 和 Python 示例。
- **[BeatJev](https://github.com/lambertsj/beatjev)** · <sub>lambertsj · GitHub · 2026-09-17</sub><br>浏览器反应速度比赛：你和 Jev 在 25 轮中判断同一条消息是不是垃圾信息，最后在可分享的结果页上比较速度和准确率；以 Cloudflare Worker 运行。
- **[Bluff](https://typesafe-showcase.vercel.app/bluff)** · <sub>Ashadeepa · 应用</sub><br>吹牛纸牌游戏（又称 Cheat），对手是三个 AI：每个对手在决定出哪些牌、要不要拆穿你之前，都会先问 Jev 你的声明有多可信。
- **[Can you beat Jev? (SIDE OUT)](https://antics.gg/can-you-beat-jev)** · <sub>antics.gg · 应用</sub><br>实时实验：在多人 Pong 风格竞技场游戏 SIDE OUT 中和 Jev 对战，它在真实浏览器里实时操作。
- **[casse-brique-typesafe](https://github.com/Para-FR/casse-brique-typesafe)** · <sub>Para-FR · GitHub · 2026-09-17</sub><br>可在浏览器里玩的 Next.js 打砖块游戏，挡板可以随时交给由 Jev 驱动的 AI 驾驶员接管；游戏界面为法语。
- **[chess-vs-jev](https://github.com/zebedelu/chess-vs-jev)** · <sub>zebedelu · GitHub · 2026-09-20</sub><br>Pygame 国际象棋：规则由 python-chess 处理，Jev 每回合从带标签的列表中选一个合法走法，支持人对人、人对 Jev 和 Jev 对 Jev。
- **[Cyber-Breach: The Jev Protocol](https://github.com/rchovatiya88/cyber-breach-jev)** · <sub>rchovatiya88 · GitHub · 2026-09-17</sub><br>用 Three.js 做的无尽 3D Tron 风格竞技场射击游戏，敌人的战术来自 Jev：一个 Choice 选择包抄、撤退等机动，一个 Score 评估威胁，几个 Noul 触发冲刺或狂暴。
- **[GameCoach](https://github.com/JoelLewis/game-coach)** · <sub>JoelLewis · GitHub · 2026-09-19</sub><br>运行在 Cloudflare 上的浏览器国际象棋教练：Stockfish 评估局面，Jev 决定每步棋之后给出什么指导反馈。
- **[Hollow Creek](https://hollow-creek-sigma.vercel.app)** · <sub>hollow-creek · 应用</sub><br>3D 村庄游戏：没有剧本的 NPC 会观察并记住你的所作所为，然后在每个 tick 通过表情和动作而非对话决定如何对待你。
- **[Jev Arcade](https://jev-arcade.vercel.app/duel)** · <sub>jev-arcade · 应用</sub><br>两款与实时 Jev 对手对战的浏览器游戏：一个 Krunker 风格的 1v1 竞技场对决，和一个霓虹风生存挑战。
- **[Jev Atari Lab](https://github.com/memorysaver/jev-atari-lab)** · <sub>memorysaver · GitHub · 2026-09-17</sub><br>研究实验室：用 Jev 的结构化决策和价值问题玩 Arcade Learning Environment 中的 Atari 游戏，同时由一个“教师”角色修改问题程序，并公开输入、动作、奖励和视频。
- **[Jev Chat](https://jev-chat.gigabitmillion-games.workers.dev/)** · <sub>gigabitmillion-games · 应用</sub><br>日语聊天游戏：你和一个小小的居民聊天，它的表情、天气和房间会随 Jev 对你话语情绪的解读而变化。
- **[Jev Chess (loomens)](https://chess-jev.loomens.com)** · <sub>loomens · 应用</sub><br>3D 棋盘：Jev 可以分饰两种性格自己和自己下，也可以由你执一方，走棋理念可切换，每一步背后的概率都会显示出来。
- **[Jev Games](https://github.com/shantanugoel/jev-games)** · <sub>shantanugoel · GitHub · 2026-09-17</sub><br>可视化实验室：Jev 玩 Super Mario Bros.、Kung Fu（NES）和 Doom（ViZDoom），通过插件系统接入新游戏和模拟器，支持逐步回放；按键和按住时长由代码负责。
- **[Jev Games](https://game-plan.adriaansendennis.workers.dev/play)** · <sub>adriaansendennis · 应用</sub><br>文字解谜游戏：用尽可能少的步数把两个看似无关的事物连起来，由 Jev 评判每一环，另有排行榜和速通模式。
- **[Jev Plays](https://jevboardgames.everpaper.app/)** · <sub>everpaper · 应用</sub><br>和 Jev 下井字棋和四子棋，每一步由模型选择，规则由代码保证。
- **[Jev 玩 Pac-Man](https://jev-pacman.ephraimduncan.com)** · <sub>Ephraim Duncan · 应用</sub><br>由 Jev 操控的 Pac-Man 复刻版：每到路口前，它都会收到结构化的迷宫、角色和合法方向数据，并实时选择转向。
- **[Jev 玩俄罗斯方块](https://github.com/MachineLearning-Nerd/jev-tetris)** · <sub>MachineLearning-Nerd · GitHub · 2026-09-17</sub><br>街机版俄罗斯方块：引擎枚举所有合法且经过碰撞检测的最终落点，Jev 把它们当作类型化选项挑一个，物理由 Python 负责；附带一段讲解视频。
- **[Jev Pong](https://github.com/ably-labs/jev-pong)** · <sub>ably-labs · GitHub · 2026-09-17</sub><br>浏览器版 Pong：模型每做一次决策球就移动一步，通过 Vercel AI Gateway 让 Jev 与各家 LLM 对战，所有玩家和 agent 都经由 Ably 频道连接。
- **[Jev 对 Jev 下棋](https://github.com/TholeG/typesafe-chess)** · <sub>TholeG · GitHub · 2026-09-17</sub><br>两个 Jev 棋手对弈：每一步都是对合法走法的一个 Choice，同时给出局面 Score 和尖锐度 Noul，还可选用基于这些分布的 AlphaZero 式 MCTS。
- **[Jev's Kitchen Chaos](https://github.com/bebe0307mz/jevs-kitchen-chaos)** · <sub>bebe0307mz · GitHub · 2026-09-18</sub><br>Overcooked 风格的 3D 厨房：四名厨师由 Jev 或前沿 LLM 一次一个决策地驱动，直播式 HUD 显示每个策略的分布、延迟和 token 成本，另有基准测试模式。
- **[Jev's Sprint Planning](https://jevs-sprint-planning.vercel.app)** · <sub>notque · 应用</sub><br>模拟游戏：3D 办公室里四名由 Jev 驱动的开发者认领工单、写代码、做评审、部署和救火，每次决策都实时显示概率条、延迟和成本。
- **[jev-asks-until-sure](https://github.com/mintannn/jev-asks-until-sure)** · <sub>mintannn · GitHub · 2026-09-20</sub><br>二十问游戏，猜你的人设、在日本的家乡地区和年龄；Jev 的校准置信度一越过阈值就停止，问满十二个问题仍判断不了时会坦白说猜不出。
- **[jev-behavior-tree](https://github.com/phuhao00/jev-behavior-tree)** · <sub>phuhao00 · GitHub · 2026-09-19</sub><br>游戏“直觉”服务，用 Jev 替换 NPC 行为树中的条件节点和选择器节点：一个 Choice 选出游戏能执行的战术，Score 和是非量表则报告威胁程度和时机。
- **[jev-bfs](https://github.com/komikat/jev-bfs)** · <sub>komikat · GitHub · 2026-09-17</sub><br>维基百科链接竞速的终端工具，在两篇英文文章之间找路径：Chromium 读取页面，Jev 给页面外链排序，Python 负责搜索，并实时显示分数和耗时。
- **[jev-experiments](https://github.com/mittal-parth/jev-experiments)** · <sub>mittal-parth · GitHub · 2026-09-17</sub><br>Jev 根据代码读出的状态玩真正的 chrome://dino 游戏和一个本地 Krunker 风格射击竞技场，检查器展示每个 tick 的状态、答案和动作。
- **[jev-gomoku](https://github.com/mizchi/jev-gomoku)** · <sub>mizchi · GitHub · 2026-09-17</sub><br>MoonBit 练习场，包含一个 System One API 客户端、一个一次性提问的 CLI、一个让两个 Jev 棋手每步从候选格中选择来下五子棋的 CLI，以及一个把对局日志转成实时 GIF 的工具。
- **[jev-plays-pokemon](https://github.com/zbloss/jev-plays-pokemon)** · <sub>zbloss · GitHub · 2026-09-17</sub><br>仿照 Claude Plays Pokemon 的 Pokemon agent，由 Jev 选择动作，附带本地查看器，在实时决策侧栏旁串流游戏画面。
- **[jev-torneo-animales](https://github.com/hectorlcastro09/jev-torneo-animales)** · <sub>hectorlcastro09 · GitHub · 2026-09-19</sub><br>由 Jev 当裁判的擂台赛（赢家留场），最多 2,569 种动物参赛；在笔记本上，2,000 种动物约 16 秒打完 1,999 场，每次决策约 7.6 毫秒，花费约 US$0.01。
- **[jev.mods](https://github.com/Hardel-DW/jev.mods)** · <sub>Hardel-DW · GitHub · 2026-09-17</sub><br>Minecraft 服务器 mod，其中的机器人不靠预设路线，尝试从零开始通关：代码观察世界，偶尔才调用一次 LLM 策略师，Jev 每个 tick 选择动作原语。
- **[JevArena](https://github.com/rolki-png/JevArena)** · <sub>rolki-png · GitHub · 2026-09-18</sub><br>观战竞技场 Web 应用：两个独立的 Jev agent 通过 Vercel AI Gateway 对战贪吃蛇，未设置 key 时回退到一个明确标注的演示策略。
- **[JevCraft](https://jevcraft.vercel.app)** · <sub>egetheengineer · 应用 · 2026-09-21</sub><br>Jev 无人值守连续五天玩 Minecraft 风格游戏 VoxeLibre 的直播，它根据生命值、饥饿度、背包和周边环境选择下一个技能（砍树、合成、挖矿、打猎、建造、睡觉）。
- **[Kiru Hai Coach](https://github.com/smilior/kiru-hai-coach)** · <sub>smilior · GitHub · 2026-09-19</sub><br>日语单人麻将教练：Jev 从 14 张手牌里选出该打哪张，并从效率、安全性和听牌角度解释，附带课程和练习局。
- **[Last Exit](https://github.com/0x963D/last-exit)** · <sub>0x963D · GitHub · 2026-09-17</sub><br>赛博朋克风格的边境过关遭遇战，你要骗过一个由 Jev 驱动的检查员；在 100 次脚本化过关中，走私者逃脱了 29/90 次，这批测试的输入成本估计为 $0.057。
- **[实时追逐对手](https://openrouter.ai/labs/jev/game)** · <sub>OpenRouter · 应用</sub><br>OpenRouter Labs 的游戏：你跑，Jev 追，它每秒两到三次、每次用一个请求选出追击者的下一步，同时有一个聊天模型作为影子回答同一个问题；每小时约 $0.16。
- **[Loophole](https://loophole-city.vercel.app/)** · <sub>loophole-city.vercel.app · 应用</sub><br>模拟小玩具：你给一个小镇写一条规则，看 100 位居民想方设法钻它的空子，Jev 当裁判，决定哪些计划被允许、哪些被拦下。
- **[Naimono Lab](https://github.com/mocchalera/naimono-lab)** · <sub>mocchalera · GitHub · 2026-09-18</sub><br>日语家庭文字游戏，玩法是说出不存在的词：Cloudflare Worker 通过 Workers AI 问 Jev 每个词有多像真词、像名字或像句子，达到 0.85 及以上就判出局。
- **[Node Royale](https://github.com/JanDalhuysen/jev-clash-royale-test)** · <sub>JanDalhuysen · GitHub · 2026-09-19</sub><br>Node.js 实时 Clash Royale 风格沙盒，带 canvas 客户端和 MCP 服务器，你可以对战一个 Jev 机器人和一个 Ollama 提示词加解析的机器人。
- **[pong-jev](https://github.com/safzanpirani/pong-jev)** · <sub>safzanpirani · GitHub · 2026-09-17</sub><br>Atari Pong agent，每一帧根据五个短语问 Jev 一个 Choice（上、下或不动），不发送坐标，因为 jev-1.13 不擅长比较数值大小。
- **[River Oaks District](https://github.com/BunsDev/river-oaks)** · <sub>BunsDev · GitHub · 2026-09-17</sub><br>可步行漫游的 3D 版休斯敦 River Oaks District，居民和访客用 Jev 决定即时反应、往哪走和帮谁，每批最多 32 个问题，截止时间 750 毫秒。
- **[River Run](https://github.com/ashaazami/river-run-typesafe)** · <sub>ashaazami · GitHub · 2026-09-17</sub><br>用 pygame-ce 做的纵向卷轴河道射击游戏，灵感来自 Atari 的 River Raid，AI 飞行员用 Jev 实时游玩。
- **[Shady Town](https://github.com/tpaulshippy/shady-town)** · <sub>tpaulshippy · GitHub · 2026-09-17</sub><br>黑手党风格的社交推理聚会游戏，在客厅电视上玩、用手机当手柄，Jev 取代人类主持人，驱动实时怀疑度计量条，并识别虚张声势或循环论证。
- **[Snake Jev](https://github.com/siroccomask/snake-jev)** · <sub>siroccomask · GitHub · 2026-09-17</sub><br>桌面贪吃蛇实验：Python 把 Jev 对棋盘的并行评估合成一个走法，每个 tick 一次 API 调用；一次录制的运行在 461 个 tick 内吃到 29 个食物。
- **[sudoku-jev](https://github.com/jaysonsantos/sudoku-jev)** · <sub>jaysonsantos · GitHub · 2026-09-19</sub><br>数独游戏，另有 Jev 对战 Stockfish 的国际象棋模式：后端通过 OpenRouter 把棋盘和所有合法填法发给 Jev，Jev 每回合选一个，直到解出或犯错三次。
- **[sudoku-vs-jev](https://github.com/zebedelu/sudoku-vs-jev)** · <sub>zebedelu · GitHub · 2026-09-19</sub><br>终端数独：Python 负责规则，Jev 每回合选一步，另有基准测试脚本，衡量它在走法唯一与必须猜测两种情况下的表现。
- **[Talos](https://github.com/chensterman/talos)** · <sub>chensterman · GitHub · 2026-09-18</sub><br>LLM 不参与循环的 Minecraft agent：计划和动作由代码负责，Jev 在每个分支点（大约每 1.5 秒）回答批量的类型化问题，从目标解析到战斗都有。
- **[Terrarium](https://github.com/TheGali/terrarium)** · <sub>TheGali · GitHub · 2026-09-17</sub><br>沙盒：世界由代码运行，Jev 只负责操控一个小生物，每个决策都完整记录：发送的状态、每个问题、每个概率以及触发的规则。
- **[Tetris x TypeSafe](https://jev-omega.vercel.app)** · <sub>jev-omega · 应用</sub><br>可以玩的俄罗斯方块，你可以把控制权交给 Jev，它根据空洞、堆叠高度和凹凸度为每个方块选择旋转和列。
- **[tetris-ai](https://github.com/shantanugoel/tetris-ai)** · <sub>shantanugoel · GitHub · 2026-09-17</sub><br>霓虹风浏览器俄罗斯方块，提供 REST API，任何玩家都能接入：内置规划 agent、Jev，或任意兼容 OpenAI 的聊天模型，状态以文本形式暴露，非法走法会被拒绝。
- **[The Council of Extremely Specific Opinions](https://github.com/cbetz/extremely-specific-council)** · <sub>cbetz · GitHub · 2026-09-17</sub><br>趣味应用：一个由十二个角色组成的委员会（从金毛寻回犬到穿西装的三只浣熊）为你的点子投票，带投票动画、可查看的决策和可分享的结果卡片。
- **[The Trolley Problem](https://gpu.studio/trolley)** · <sub>gpu.studio · 应用</sub><br>浏览器小玩具：你可以把任何东西放到电车难题的两条轨道上，由 Jev 决定是否拉下拉杆。
- **[Turing Jail](https://github.com/bugkiwi/turing-jail)** · <sub>bugkiwi · GitHub · 2026-09-17</sub><br>三关审讯游戏：你向 AI 典狱长写陈述，必须依次通过认罪、逻辑和悖论三轮裁决才能获释，通关记录可封存分享。
- **[Typesafe_chess_eval](https://github.com/AliceRoselia/Typesafe_chess_eval)** · <sub>AliceRoselia · GitHub · 2026-09-17</sub><br>简短脚本，让 Jev 同时执双方下棋，从合法 UCI 走法中选出每一步，并估计胜、和、负的可能；作者发现它经常把一边倒的局面判为和棋。

</details>

还缺什么？[提交一个资源](https://github.com/Li-Evan/awesome-jev/issues/new/choose)。
