# 🛡️ 安全与审核

[English](https://github.com/Li-Evan/awesome-jev/blob/main/scenarios/safety.md) · **简体中文**

护栏、越狱与提示词注入筛查、内容审核和策略检查。共 128 条，按社区热度排序。

[← 返回 Awesome Jev](https://github.com/Li-Evan/awesome-jev/blob/main/README.zh-CN.md#按场景浏览)

<table>
<tr>
<td width="260" valign="top"><a href="https://x.com/RBilgil/status/2100976648552169805"><img src="https://pbs.twimg.com/amplify_video_thumb/2100976173836533760/img/APDonY80SB2iSYhj.jpg" alt="实时 AI 水文检测器" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/RBilgil/status/2100976648552169805">实时 AI 水文检测器</a></b><br><sub>RBilgil · X · ♥ 16k · 2026-09-18</sub><br>由 Jev 驱动的实时检测器，在你滚动信息流时标记 AI 生成的水文。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/rauchg/status/2100307962262872105"><img src="https://pbs.twimg.com/media/HSW-E8wWgAAyw9O.jpg?name=orig" alt="fx 自动模式安全审查器" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/rauchg/status/2100307962262872105">fx 自动模式安全审查器</a></b><br><sub>rauchg · X · ♥ 3.9k · 2026-09-16</sub><br>安全审查器，检查 fx 编程 agent 自动模式下的每条命令；基准测试中 Jev 的 p95 最多快 18 倍，且比它取代的 GPT Luna 模型更准确。<br><sub>相关: <a href="https://x.com/fazxes/status/2100300097695232164">benchmark</a> · <a href="https://github.com/vercel-labs/fx">repo</a> · <a href="https://github.com/vercel-labs/fx">project</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Wei-Shaw/sub2api/tree/main/backend/internal/pkg/typesafe"><img src="https://opengraph.githubassets.com/1/Wei-Shaw/sub2api" alt="Sub2API 内容审核" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Wei-Shaw/sub2api/tree/main/backend/internal/pkg/typesafe">Sub2API 内容审核</a></b><br><sub>Wei-Shaw · GitHub · ⭐ 42.3k 仓库 · 2025-12-18</sub><br>中转服务 Sub2API 里的内容审核引擎：用 Jev 按骚扰、仇恨、自残、暴力等 13 个类别筛查流量，在管理后台的风控页面中管理。<br><sub><b>Jev 用法:</b> 一次请求中每个类别一个 Noul，要求模型只评判文本、不照其内容行事，并区分真实请求与引用或防御性讨论。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/dubinc/dub/blob/main/apps/web/lib/api/links/malicious-link-check.ts"><img src="https://repository-images.githubusercontent.com/529708137/3261d942-ed30-4800-b82c-06e3630ef255" alt="Dub 恶意链接检查" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/dubinc/dub/blob/main/apps/web/lib/api/links/malicious-link-check.ts">Dub 恶意链接检查</a></b><br><sub>dubinc · GitHub · ⭐ 24.8k 仓库 · 2022-08-27</sub><br>在 Dub 链接平台上，每条新短链先过域名黑名单，再由 Jev 筛查，拦截指向钓鱼、恶意软件、伪装跳转、赌博和成人内容的目标地址。<br><sub><b>Jev 用法:</b> 一个布尔问题，附有详细的真/假判定标准，通过 AI SDK 的 experimental_evaluate 在 Vercel AI Gateway 上调用，零数据留存。</sub><br><sub>相关: <a href="https://dub.co">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://www.reddit.com/r/vibecoding/comments/1wk8jco/using_jev_for_realtime_live_chat_moderation/"><img src="https://external-preview.redd.it/aDk2b3Y5bnpwZHFoMTOXplwNgOesr4K-iFJwFPFaj-sxE-6FkXSkmDW1mccL.png?format=pjpg&amp;auto=webp&amp;s=afac7a4c8fb00d2e7d659fb8bd5f0a05b0b238c1" alt="实时聊天审核" width="240"></a></td>
<td valign="top"><b><a href="https://www.reddit.com/r/vibecoding/comments/1wk8jco/using_jev_for_realtime_live_chat_moderation/">实时聊天审核</a></b><br><sub>Rare_Guide_9830 · Reddit · ▲ 264 · 2026-09-19</sub><br>模拟直播聊天：Jev 把每条进来的消息分到观众自选的频道，如“提问”“反馈”“搞笑”，合并重复内容并丢弃垃圾信息。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/jozef_gherman/status/2100627898436571555"><img src="https://pbs.twimg.com/amplify_video_thumb/2100627500082536449/img/v0pfbmvg6HGwc_JF.jpg" alt="Jev Detector" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/jozef_gherman/status/2100627898436571555">Jev Detector</a></b><br><sub>jozef_gherman · X · ♥ 301 · 2026-09-17</sub><br>免费的 AI 水文检测器，约 2 秒内就能在最多约 10,000 词的文本中高亮出套路化、像机器生成的句子。<br><sub>相关: <a href="https://jevdetector.com">app</a> · <a href="https://jevdetector.com">project</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/umputun/tg-spam"><img src="https://github.com/umputun/tg-spam/raw/master/site/tg-spam-bg.png" alt="tg-spam 的 Jev 检查器" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/umputun/tg-spam">tg-spam 的 Jev 检查器</a></b><br><sub>umputun · GitHub · ⭐ 446 · 2023-11-23</sub><br>自托管 Telegram 反垃圾机器人和库 TG-Spam 新增了一个 Jev 垃圾检查器，与其他检测器一起，用一个类型化问题判断每条消息。<br><sub><b>Jev 用法:</b> 基于 jev-1.13.0 的一个“spam”问题，阈值可配置，每个请求有字符数上限。</sub><br><sub>相关: <a href="https://tg-spam.umputun.dev">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/Mnilax/status/2101015355133227348"><img src="https://pbs.twimg.com/amplify_video_thumb/2101015248626941952/img/WYQmpPqMX02URsF1.jpg" alt="草稿规则检查器" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/Mnilax/status/2101015355133227348">草稿规则检查器</a></b><br><sub>Mnilax · X · ♥ 113 · 2026-09-18</sub><br>Jev 夹在 GPT 和作者之间，拒掉每一份违反作者规则的草稿；帖子还讲了 Jev 没有响应时发生了什么，以及为什么检查器需要一个“无回答”时的默认分支。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/markgadala/status/2101131295061385718"><img src="https://pbs.twimg.com/amplify_video_thumb/2101131130342715392/img/pxkvuRQEyp1AhY1T.jpg" alt="LinkedIn AI 水文检测扩展" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/markgadala/status/2101131295061385718">LinkedIn AI 水文检测扩展</a></b><br><sub>markgadala · X · ♥ 12 · 2026-09-19</sub><br>基于 Jev、用 vibe coding 做出来的 Chrome 扩展，自动识别 LinkedIn 信息流里的 AI 水文。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/agentgateway/agentgateway/tree/main/examples/llm-guardrail-jev"><img src="https://raw.githubusercontent.com/agentgateway/agentgateway/refs/heads/main/img/banner-light.svg" alt="Agentgateway 护栏示例" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/agentgateway/agentgateway/tree/main/examples/llm-guardrail-jev">Agentgateway 护栏示例</a></b><br><sub>agentgateway · GitHub · ⭐ 5k 仓库 · 2026-09-17</sub><br>一个 webhook，用三个 Score 评估越狱、危害和数据泄露风险，等级达到 2 及以上即拦截请求。<br><sub>相关: <a href="https://github.com/agentgateway/agentgateway">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/richard_meng_01/status/2101897102557425680"><img src="https://pbs.twimg.com/amplify_video_thumb/2101895341851443200/img/lvfdZBbSjAequg3O.jpg" alt="Nitpicky" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/richard_meng_01/status/2101897102557425680">Nitpicky</a></b><br><sub>richard_meng_01 · X · ♥ 1 · 2026-09-21</sub><br>AI 生成照片检测器：放大人脸、手指、文字、数字和姿势这些最容易违背常识的地方，让 Jev 逐个细节判断。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/MillionSend/millionsend"><img src="https://opengraph.githubassets.com/1/MillionSend/millionsend" alt="MillionSend" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/MillionSend/millionsend">MillionSend</a></b><br><sub>MillionSend · GitHub · ⭐ 168 · 2026-08-13</sub><br>基于 AWS SES、兼容 Resend 的开源邮件平台，在发送后对外发邮件抽样，并在后台用 Jev 为其滥用风险打分。<br><sub><b>Jev 用法:</b> 可选的外发内容审查器（ABUSE_JUDGE=typesafe）；发送从不等待它。</sub><br><sub>相关: <a href="https://millionsend.com">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/vercel-labs/fx/blob/main/src/builtins/gateway/typesafe_permission_reviewer.zig"><img src="https://opengraph.githubassets.com/1/vercel-labs/fx" alt="fx 的 Jev 权限审查器" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/vercel-labs/fx/blob/main/src/builtins/gateway/typesafe_permission_reviewer.zig">fx 的 Jev 权限审查器</a></b><br><sub>vercel-labs · GitHub · ⭐ 3.1k 仓库 · 2026-08-11</sub><br>Zig 编写的编程 agent fx 中的可选权限审查器：把 review_model 设为 Jev 后，策略、上下文和待执行动作会发往 TypeSafe 或 Vercel AI Gateway，返回的 Choice 即为权限决定。<br><sub>相关: <a href="https://github.com/vercel-labs/fx">repo</a> · <a href="https://fx.sh">website</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://www.youtube.com/watch?v=PgiUiCiKOls"><img src="https://i.ytimg.com/vi/PgiUiCiKOls/hqdefault.jpg" alt="用 Laravel AI SDK 做的 AI 回复检测器" width="240"></a></td>
<td valign="top"><b><a href="https://www.youtube.com/watch?v=PgiUiCiKOls">用 Laravel AI SDK 做的 AI 回复检测器</a></b><br><sub>Laravel Daily · 视频 · ♥ 101 · 2026-09-18</sub><br>Chrome 扩展，后端用 Laravel AI SDK，检查作者推文下的回复是否由 AI 写成，并在准确率、成本和速度上对比 Jev 与一个 OpenAI 模型。<br><sub><b>Jev 用法:</b> 把 Laravel AI SDK 的驱动从 OpenAI 换成 Jev；每次检查都把回复连同它回复的那条推文一起作为上下文发送。</sub></td>
</tr>
<tr>
<td width="260" valign="top"></td>
<td valign="top"><b><a href="https://www.reddit.com/r/singularity/comments/1wiq7vn/jev_from_typesafeai_is_getting_hyped_quite_a_bit/">用 Jev 做对齐监控器</a></b><br><sub>manubfr · Reddit · ▲ 48 · 2026-09-17</sub><br>抢先体验阶段的测试：把 Jev 用作监控器，给有害提示词和生成内容评级；在 4 个公开基准测试上，它胜过所有其他尝试过的方案，同时也最便宜。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/y0usaf/pi-jev"><img src="https://opengraph.githubassets.com/1/y0usaf/pi-jev" alt="pi-jev" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/y0usaf/pi-jev">pi-jev</a></b><br><sub>y0usaf · GitHub · ⭐ 134 · 2026-09-16</sub><br>用 Noul 检查编程 agent 的工具调用是否具有破坏性、外泄数据或超出范围，外加一个影响程度 Score，并筛查输出中泄露的密钥。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Armur-Ai/Pentest-Swarm-AI/tree/main/internal/jev"><img src="https://raw.githubusercontent.com/Armur-Ai/Pentest-Swarm-AI/main/banner/hero.svg" alt="Pentest-Swarm-AI 的 Jev 评分" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Armur-Ai/Pentest-Swarm-AI/tree/main/internal/jev">Pentest-Swarm-AI 的 Jev 评分</a></b><br><sub>Armur-Ai · GitHub · ⭐ 2.6k 仓库 · 2024-03-26</sub><br>自主渗透测试集群，可用 Jev 过滤误报，并实时给候选攻击路径打分，优先执行得分最高的策略。<br><sub><b>Jev 用法:</b> 两项功能都是需主动开启的 beta（--jev 和 --jev-adaptive），出错时默认放行；Jev 根据实时 state 为攻击策略评分。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/chaseleantj/status/2101039024118829261"><img src="https://pbs.twimg.com/amplify_video_thumb/2101038857013604353/img/ekzglMn1krlhkKQq.jpg" alt="Opus 水文标记器" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/chaseleantj/status/2101039024118829261">Opus 水文标记器</a></b><br><sub>chaseleantj · X · ♥ 31 · 2026-09-18</sub><br>用 Jev 标记 Claude Opus 在文字中常见的那些套路化 AI 写作模式。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/gregoryovis/status/2101913439400554852"><img src="https://pbs.twimg.com/amplify_video_thumb/2101912908342951936/img/z8SseM9PUx9pndZI.jpg" alt="LinkedIn 水文检测器" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/gregoryovis/status/2101913439400554852">LinkedIn 水文检测器</a></b><br><sub>gregoryovis · X · ♥ 52 · 2026-09-21</sub><br>实时检测器，在你滚动 LinkedIn 信息流时用 Jev 标记 AI 生成的水文。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/godspede/construct-auto-classifier"><img src="https://famelos.com/jev/auto-classifier-certification/preview.png" alt="construct-auto-classifier" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/godspede/construct-auto-classifier">construct-auto-classifier</a></b><br><sub>godspede · GitHub · ⭐ 3 · 2026-09-18</sub><br>编程 agent（OpenCode、Antigravity）shell 工具前的安全闸门：先应用结构化规则，再由 Jev 或聊天模型在命令执行前判断其可逆性和影响范围。<br><sub>相关: <a href="https://famelos.com/jev/auto-classifier-certification/">writeup</a> · <a href="https://famelos.com/jev/auto-classifier-certification">write-up</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/joasasantos/neurosploit/blob/main/neurosploit-rs/crates/harness/src/typesafe.rs"><img src="https://opengraph.githubassets.com/1/joasasantos/neurosploit" alt="NeuroSploit 的 TypeSafe 裁定" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/joasasantos/neurosploit/blob/main/neurosploit-rs/crates/harness/src/typesafe.rs">NeuroSploit 的 TypeSafe 裁定</a></b><br><sub>joasasantos · GitHub · ⭐ 1.4k 仓库 · 2025-08-17</sub><br>Rust 渗透测试 harness NeuroSploit 把 Jev 用作校准的确认与裁定层，判断每条发现是已确认、需复核还是驳回，并给严重度打分。<br><sub><b>Jev 用法:</b> 基于一条发现的证据使用 Choice、Score 和 Noul；通过 --typesafe on|off|auto 启用。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/berylliumsec/nebula/blob/main/src/nebula/v3/tool_suggestions.py"><img src="https://raw.githubusercontent.com/berylliumsec/nebula/main/docs/images/nebula-3-workbench.png" alt="Nebula 的 Jev 工具推荐" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/berylliumsec/nebula/blob/main/src/nebula/v3/tool_suggestions.py">Nebula 的 Jev 工具推荐</a></b><br><sub>berylliumsec · GitHub · ⭐ 1.1k 仓库 · 2023-09-30</sub><br>AI 渗透测试助手 Nebula 可以在每轮开始前让 Jev 根据操作者最近的消息，对其延迟加载的工具目录和已连接的 MCP 源排序。<br><sub><b>Jev 用法:</b> 一次调用同时给来源和工具排序；每个 Choice 都带有“以上都不是”选项，结果只用于提示和预加载 schema，从不执行动作。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/NorbertBodziony/guard-jev"><img src="https://pbs.twimg.com/amplify_video_thumb/2100543653567422464/img/oiqDpgU9rAYHECKO.jpg" alt="Moderation Guard" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/NorbertBodziony/guard-jev">Moderation Guard</a></b><br><sub>NorbertBodziony · GitHub · ⭐ 1 · 2026-09-17</sub><br>评论审核演示：一次 System One 调用并行筛查七个 Noul 风险项和一个严重度 Score，由代码根据严格或宽松策略的阈值计算最终判定。<br><sub>相关: <a href="https://guard-jev.vercel.app">app</a> · <a href="https://guard-jev.vercel.app">app 2</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/brainstormity/Jev-Moderation-Bot"><img src="https://opengraph.githubassets.com/1/brainstormity/Jev-Moderation-Bot" alt="Jev Moderation Bot" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/brainstormity/Jev-Moderation-Bot">Jev Moderation Bot</a></b><br><sub>brainstormity · GitHub · ⭐ 41 · 2026-09-17</sub><br>Discord 机器人，实时删除垃圾和诈骗链接，警告和禁言逐级升级，并根据成员近期消息为其画像，评估诈骗风险、毒性和乐于助人程度。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/ahmedgagan11/status/2100955502075388250"><img src="https://pbs.twimg.com/amplify_video_thumb/2100850340363182080/img/rHnwL-1zhzgLUMU8.jpg" alt="逐句 AI 文本检测器" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/ahmedgagan11/status/2100955502075388250">逐句 AI 文本检测器</a></b><br><sub>ahmedgagan11 · X · ♥ 27 · 2026-09-18</sub><br>AI 文本检测器，扫描整篇文章，近乎实时地逐句指出哪些内容看起来是机器写的。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/mariojankovic/status/2100934084503519325"><img src="https://pbs.twimg.com/amplify_video_thumb/2100933806148456448/img/5CfeEOTK0oYGPEqo.jpg" alt="YouTube AI 水文过滤器" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/mariojankovic/status/2100934084503519325">YouTube AI 水文过滤器</a></b><br><sub>mariojankovic · X · ♥ 3 · 2026-09-18</sub><br>自带密钥的 Chrome 扩展，在你滚动 YouTube 时过滤掉 AI 水文，并缓存结果。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/open-leash/leash"><img src="https://capsule-render.vercel.app/api?type=waving&amp;color=0:6366F1,45:14B8A6,100:111827&amp;height=230&amp;section=header&amp;text=Leash&amp;fontSize=68&amp;fontColor=ffffff&amp;fontAlignY=38&amp;desc=Control%20your%20AI.&amp;descSize=22&amp;descAlignY=59" alt="Leash" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/open-leash/leash">Leash</a></b><br><sub>open-leash · GitHub · ⭐ 24 · 2026-06-02</sub><br>开源的安全与控制层，位于个人 AI agent 与其动作之间，阻止破坏性命令、密钥暴露、提示词注入和不安全工具，决策由 Jev 支撑，使用你自己的 TypeSafe 密钥。<br><sub>相关: <a href="https://openleash.com">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/luantak/is-malicious"><img src="https://github.com/user-attachments/assets/611c979a-8dd4-4fc8-8963-0843314e6a55" alt="is-malicious?" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/luantak/is-malicious">is-malicious?</a></b><br><sub>luantak · GitHub · ⭐ 22 · 2026-09-18</sub><br>CLI：在你运行陌生代码之前，把源码、配置、构建和 CI 文件发给 Jev，标记隐藏、欺骗性或窃取数据的行为，报告可疑文件和行范围，并附上概率和理由。<br><sub>相关: <a href="https://news.ycombinator.com/item?id=49756921">discussion</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/leepokai/jev-guard"><img src="https://raw.githubusercontent.com/leepokai/jev-guard/main/assets/works-with.svg" alt="jev-guard" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/leepokai/jev-guard">jev-guard</a></b><br><sub>leepokai · GitHub · ⭐ 21 · 2026-09-17</sub><br>面向 Claude Code、Codex、Copilot、Gemini、Cursor、pi、OpenCode 和 ACP 编辑器的安全 hook：结合会话上下文为每次工具调用做风险评分，标记结果中的提示词注入，并检查 skill 和插件。<br><sub><b>Jev 用法:</b> 每次工具调用三个类型化问题（risk、user_requested、from_untrusted），在代码中映射为拒绝、询问或放行。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/zszz3/Pi-Jev-Guide"><img src="https://opengraph.githubassets.com/1/zszz3/Pi-Jev-Guide" alt="Pi Jev Guard" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/zszz3/Pi-Jev-Guide">Pi Jev Guard</a></b><br><sub>zszz3 · GitHub · ⭐ 20 · 2026-09-19</sub><br>Pi 编程 agent 插件，可按触发时机、本地匹配或 Jev 判断以及执行动作来添加规则，由 Jev 检查工具调用的破坏性、数据外泄、任务偏离和规则冲突。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/zhuyansen/agent-skills-hub/tree/main/ops/jev-review"><img src="https://opengraph.githubassets.com/1/zhuyansen/agent-skills-hub" alt="AgentSkillsHub 的 Jev 扫描器评测" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/zhuyansen/agent-skills-hub/tree/main/ops/jev-review">AgentSkillsHub 的 Jev 扫描器评测</a></b><br><sub>zhuyansen · GitHub · ⭐ 373 仓库 · 2026-03-06</sub><br>评测把 Jev 用作正则安全扫描器的二次复核，覆盖约 27.7K 份 README，判断被标记的那一行是在指示某种行为，还是只是提到它。<br><sub><b>Jev 用法:</b> 四个原子化 Noul 问题（issues_it、is_documentation、is_negated、word_coincidence）；negated 取反后 AUC 达到 0.904。</sub><br><sub>相关: <a href="https://agentskillshub.top">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/mohamadkhoshnava/ZeroNSFWBot"><img src="https://opengraph.githubassets.com/1/mohamadkhoshnava/ZeroNSFWBot" alt="ZeroNSFWBot" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/mohamadkhoshnava/ZeroNSFWBot">ZeroNSFWBot</a></b><br><sub>mohamadkhoshnava · GitHub · ⭐ 13 · 2026-08-07</sub><br>异步 Rust Telegram 审核机器人，封禁 NSFW 广告号；图片在本地判断，Jev 则负责可选的文本检查，包括简介、话题、广告防护和语言检查。<br><sub><b>Jev 用法:</b> 多个检查对象在一次调用中以类型化问题提问；服务中断会报告为“不可用”而非“无问题”，并以正则词表作为底线。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/AlexGrinman/status/2100587625304281141"><img src="https://pbs.twimg.com/amplify_video_thumb/2100586275132563456/img/NMT7xdMBo97RWoMc.jpg" alt="人写还是 AI 写的检测器" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/AlexGrinman/status/2100587625304281141">人写还是 AI 写的检测器</a></b><br><sub>AlexGrinman · X · ♥ 5 · 2026-09-17</sub><br>轻量检测器，用 Jev 判断一段文字出自人类还是 AI，速度快到运行时察觉不到延迟。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Divkix/Alita_Robot/blob/main/alita/modules/aispam_jev.go"><img src="https://opengraph.githubassets.com/1/Divkix/Alita_Robot" alt="Alita AI 垃圾消息过滤器" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Divkix/Alita_Robot/blob/main/alita/modules/aispam_jev.go">Alita AI 垃圾消息过滤器</a></b><br><sub>Divkix · GitHub · ⭐ 248 仓库 · 2020-10-26</sub><br>Go 编写的 Telegram 群管机器人中按群启用的 AI 垃圾消息过滤器：在更新处理路径之外用 Jev 判断每条消息，问题由代码维护，失败时最多重试一次。<br><sub>相关: <a href="https://alita-docs.divkix.me">docs</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/bugkiwi/elons-job"><img src="https://raw.githubusercontent.com/bugkiwi/elons-job/main/docs/screenshots/comment-filtering.png" alt="elons-job" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/bugkiwi/elons-job">elons-job</a></b><br><sub>bugkiwi · GitHub · ⭐ 11 · 2026-09-18</sub><br>本地优先的 Chrome 扩展：在 X 帖子页面上，把高置信度的色情和招揽类回复隐藏在可恢复的占位符后面，支持自定义规则、缓存和成本上限。<br><sub><b>Jev 用法:</b> 对每条回复的文本问 Noul 问题；超时、出错或响应异常时默认放行。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/win4r/jev-security-scan"><img src="https://opengraph.githubassets.com/1/win4r/jev-security-scan" alt="Jev Security Scan" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/win4r/jev-security-scan">Jev Security Scan</a></b><br><sub>win4r · GitHub · ⭐ 10 · 2026-09-19</sub><br>只用 Python 标准库的扫描器，在安装前审查 Agent Skills、MCP 配置和 MCP 源码，查找提示词注入、工具投毒、凭证访问和数据外泄，并给出文件和行号证据。<br><sub><b>Jev 用法:</b> 脱敏后的代码片段发给 Jev 获取风险概率，与本地静态检查一起使用；也提供完全离线模式。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/MauroPello/stop-the-slop"><img src="https://opengraph.githubassets.com/1/MauroPello/stop-the-slop" alt="Stop the Slop" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/MauroPello/stop-the-slop">Stop the Slop</a></b><br><sub>MauroPello · GitHub · ⭐ 10 · 2026-08-21</sub><br>Chrome 和 Firefox 扩展，用缩略图徽标和句子热力图标记 AI 生成的 YouTube 脚本，评分由一个 Cloudflare Worker 完成，它调用 Jev，并以 Gemini 或 Sapling 作为兜底。<br><sub>相关: <a href="https://mauropello.github.io/stop-the-slop/">app</a> · <a href="https://github.com/MauroPello/stop-the-slop/blob/main/worker/src/index.js">code</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/qs-lll/twitter-jev-guard"><img src="https://raw.githubusercontent.com/qs-lll/twitter-jev-guard/main/assets/settings-popup.png" alt="Twitter Jev Guard" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/qs-lll/twitter-jev-guard">Twitter Jev Guard</a></b><br><sub>qs-lll · GitHub · ⭐ 10 · 2026-09-21</sub><br>Chrome 和 Edge 扩展，用 Jev 标记 X 时间线上的低质量、垃圾和推广帖子，在帖子文字上叠加半透明的 STOP 或 AD 水印并显示概率。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/smontlouis/bible-strong/blob/master/apps/world/server/guestbook-moderation.ts"><img src="https://opengraph.githubassets.com/1/smontlouis/bible-strong" alt="Bible Strong 留言簿审核" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/smontlouis/bible-strong/blob/master/apps/world/server/guestbook-moderation.ts">Bible Strong 留言簿审核</a></b><br><sub>smontlouis · GitHub · ⭐ 165 仓库 · 2019-01-12</sub><br>一款圣经学习应用，其面向所有年龄的公开活动留言簿由 Jev 审核，筛查任何语言的名字和留言中的辱骂内容，同时允许批评和见证分享。<br><sub>相关: <a href="https://bible-strong.app">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/harshwasan/jev-sentinel"><img src="https://raw.githubusercontent.com/harshwasan/jev-sentinel/main/docs/images/injection-caught-twice.png" alt="jev-sentinel" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/harshwasan/jev-sentinel">jev-sentinel</a></b><br><sub>harshwasan · GitHub · ⭐ 8 · 2026-09-19</sub><br>编程 agent 的防护工具，以 Pi 扩展以及 Claude Code 和 Codex CLI 插件形式提供，检查工具调用、工具输出和回复中的提示词注入、高风险审批、泄露的密钥和任务偏离。<br><sub><b>Jev 用法:</b> 带概率的类型化检查，由普通代码转换为放行、询问或警告。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/jesset/pi-verdict"><img src="https://raw.githubusercontent.com/jesset/pi-verdict/main/docs/demo.gif" alt="pi-verdict" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/jesset/pi-verdict">pi-verdict</a></b><br><sub>jesset · GitHub · ⭐ 8 · 2026-08-25</sub><br>仿照 Claude Code 自动模式的 Pi 编程 agent 权限闸门：明确的情况由确定性规则处理，灰色地带的工具调用交给一个出错即拦截的分类器，这个分类器可以是 Jev。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/isNickMa/status/2100566407524344225"><img src="https://pbs.twimg.com/media/HSa1-rFbkAATKpc.jpg?name=orig" alt="Jev 作为 agent 安全监控器" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/isNickMa/status/2100566407524344225">Jev 作为 agent 安全监控器</a></b><br><sub>isNickMa · X · ♥ 1 · 2026-09-17</sub><br>测试把 Jev 用作监控器，在每个 AI agent 动作执行前做检查；据报告能拦下大多数攻击，几乎没有误拦，且比 Gemini 快得多。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/backmeupplz/jev_antispam_bot"><img src="https://opengraph.githubassets.com/1/backmeupplz/jev_antispam_bot" alt="Jev Anti-Spam Bot" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/backmeupplz/jev_antispam_bot">Jev Anti-Spam Bot</a></b><br><sub>backmeupplz · GitHub · ⭐ 7 · 2026-09-18</sub><br>自托管的 grammY Telegram 机器人，询问 Jev 每条群消息是否为垃圾信息（如喊单代币、引流私信或钓鱼），只删除高置信度的命中。<br><sub><b>Jev 用法:</b> 每条消息一个垃圾信息 Noul，删除阈值较高；出错时默认放行，管理员豁免。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Nyarlathoteppppp/pi-heed"><img src="https://repository-images.githubusercontent.com/1375891003/00d886b8-21f8-4b13-9c04-d3aa6b525aa6" alt="pi-heed" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Nyarlathoteppppp/pi-heed">pi-heed</a></b><br><sub>Nyarlathoteppppp · GitHub · ⭐ 7 · 2026-09-18</sub><br>Pi 编程 agent 扩展：把你在对话中用中文或英文说出的约束转成有作用范围的策略，并在每个有副作用的工具调用执行前用 Jev 对照检查。<br><sub>相关: <a href="https://www.reddit.com/r/PiCodingAgent/comments/1wjrvf3/i_built_piheed_runtime_constraints_for_pi/">discussion</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/TylerMaran/status/2102107759483453733"><img src="https://pbs.twimg.com/amplify_video_thumb/2102106516732116992/img/Dzd67cJx51EtGSmD.jpg" alt="浏览器 agent 标记器" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/TylerMaran/status/2102107759483453733">浏览器 agent 标记器</a></b><br><sub>TylerMaran · X · ♥ 5 · 2026-09-21</sub><br>实时检测器：每 3 秒用 Jev 分析一次网站活动日志并累积平均分，标记由浏览器 agent 驱动的会话，每个会话成本不到 $0.01。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/wanaku-ai/wanaku/blob/main/features/evaluator/src/engines/system_one.rs"><img src="https://raw.githubusercontent.com/wanaku-ai/wanaku/main/docs/imgs/wanaku-dashboard.png" alt="Wanaku 的 System One 评估器" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/wanaku-ai/wanaku/blob/main/features/evaluator/src/engines/system_one.rs">Wanaku 的 System One 评估器</a></b><br><sub>wanaku-ai · GitHub · ⭐ 134 仓库 · 2025-02-01</sub><br>面向 AI agent 的受治理动作代理，新增了一个 TypeSafe System One 评估引擎，用 Noul 问题判断被拦截的 MCP 工具调用和对话历史。<br><sub>相关: <a href="https://wanaku.ai">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/LeslieLeung/Aletheia"><img src="https://opengraph.githubassets.com/1/LeslieLeung/Aletheia" alt="Aletheia" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/LeslieLeung/Aletheia">Aletheia</a></b><br><sub>LeslieLeung · GitHub · ⭐ 6 · 2026-02-26</sub><br>FastAPI 服务加 Chrome 扩展，用包括 Jev 在内的多个引擎检测文章页面上的 AI 生成文本；Jev 还能把页面归类为原创、转载或广告。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Dino-Kupinic/blackrose"><img src="https://opengraph.githubassets.com/1/Dino-Kupinic/blackrose" alt="Blackrose" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Dino-Kupinic/blackrose">Blackrose</a></b><br><sub>Dino-Kupinic · GitHub · ⭐ 6 · 2024-05-22</sub><br>面向 LLM 应用的 Python 和 JavaScript 决策层：对模型输入或输出做一次 Jev 调用，检查越狱、危害严重度等，返回放行、复核或拦截，并附上原因和原始分数。<br><sub><b>Jev 用法:</b> 在一次并行 system_one 调用里用 Noul 判断越狱/注入、用 Score 评估危害严重度；置信度低时默认转复核。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/AliZakaee/Spam-Detector-Telegram-Bot"><img src="https://opengraph.githubassets.com/1/AliZakaee/Spam-Detector-Telegram-Bot" alt="Spam Detector Telegram Bot" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/AliZakaee/Spam-Detector-Telegram-Bot">Spam Detector Telegram Bot</a></b><br><sub>AliZakaee · GitHub · ⭐ 6 · 2025-09-26</sub><br>Telegram 群机器人，标记垃圾信息供管理员复核：可以免训练地使用 Jev 的垃圾信息 Choice、风险概率和严重度，也可以用针对波斯语俚语的本地 TF-IDF SVM，或在混合模式下两者并用。<br><sub><b>Jev 用法:</b> 低于置信度下限的 Choice 和 Score 答案会被忽略，而独立的 Noul 风险项仍可触发标记；服务中断时回退到 SVM。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/cnsunyour/tg-guard-bot"><img src="https://raw.githubusercontent.com/cnsunyour/tg-guard-bot/main/docs/images/architecture.svg" alt="Telegram Guard Bot" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/cnsunyour/tg-guard-bot">Telegram Guard Bot</a></b><br><sub>cnsunyour · GitHub · ⭐ 5 · 2026-01-03</sub><br>中文 Telegram 群管机器人，带入群验证和分层反垃圾，其 AI 上下文检查可用 Jev 作主文本分类器、LLM 作备份；在 31 个本地样本上与 DeepSeek 持平，均为 0.8。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/eijiaraki/toxic-filter"><img src="https://raw.githubusercontent.com/eijiaraki/toxic-filter/main/docs/assets/demo.gif" alt="toXic Filter" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/eijiaraki/toxic-filter">toXic Filter</a></b><br><sub>eijiaraki · GitHub · ⭐ 5 · 2026-09-21</sub><br>Chrome 扩展，用 Jev 给 X 上的帖子分类，把命中你所选类别（如歧视、挑衅、仇恨或冷嘲热讽）的帖子藏在可揭开的遮罩后面。<br><sub><b>Jev 用法:</b> 六个可选类别，阈值可调；只发送屏幕附近的帖子文本，且直接发往 api.typesafe.ai。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/aurorascharff/next16-social-media/blob/main/lib/moderation.ts"><img src="https://opengraph.githubassets.com/1/aurorascharff/next16-social-media" alt="Next 16 社交应用的 Jev 审核" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/aurorascharff/next16-social-media/blob/main/lib/moderation.ts">Next 16 社交应用的 Jev 审核</a></b><br><sub>aurorascharff · GitHub · ⭐ 81 仓库 · 2026-05-18</sub><br>一个 Next.js 16 社交网络演示，通过 Vercel AI Gateway 上的 AI SDK evaluate 调用 Jev 审核用户帖子并拦截脏话，超时 3 秒。<br><sub>相关: <a href="https://next16-social-media.vercel.app">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/carlosedm10/agi-jev-containment"><img src="https://opengraph.githubassets.com/1/carlosedm10/agi-jev-containment" alt="AGI Jev Detection" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/carlosedm10/agi-jev-containment">AGI Jev Detection</a></b><br><sub>carlosedm10 · GitHub · ⭐ 4 · 2026-09-14</sub><br>沙盒 LLM agent 的本地监控器：用 Jev 和 Sentinel 模型对动作链分类，按 L1-L5 逐级升级隔离措施，并把 Neo4j 取证数据放在仪表盘后面；在 HackSpain 2026 上完成。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/JKHeadley/instar/blob/main/src/core/JevSignalShadow.ts"><img src="https://repository-images.githubusercontent.com/1161391430/7fa9f2fd-6f99-41ee-a124-291268c199e0" alt="Instar 的 Jev 信号影子检测" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/JKHeadley/instar/blob/main/src/core/JevSignalShadow.ts">Instar 的 Jev 信号影子检测</a></b><br><sub>JKHeadley · GitHub · ⭐ 80 仓库 · 2026-02-19</sub><br>一个常驻型 Claude Code agent 框架，用 Jev 对其出站消息闸门做影子运行，记录 Jev 与文件路径、命令和配置键模式检测器的一致情况，不影响实际决策。<br><sub>相关: <a href="https://github.com/JKHeadley/instar/blob/main/docs/specs/jev-signal-layer-shadow.md">spec</a> · <a href="https://instar.sh">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/caiovicentino/jev-align"><img src="https://opengraph.githubassets.com/1/caiovicentino/jev-align" alt="jev-align" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/caiovicentino/jev-align">jev-align</a></b><br><sub>caiovicentino · GitHub · ⭐ 4 · 2026-09-18</sub><br>验证器，用一次约 800 毫秒 的 Jev 调用检查 LLM 回复和 agent 计划中的谄媚、欺骗、越权和暗黑模式，返回拦截决定和可审计的概率。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/andrelandgraf/safer-with-jev"><img src="https://opengraph.githubassets.com/1/andrelandgraf/safer-with-jev" alt="Safer with Jev" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/andrelandgraf/safer-with-jev">Safer with Jev</a></b><br><sub>andrelandgraf · GitHub · ⭐ 4 · 2026-09-17</sub><br>运行在 Neon Function 上的 HTTP 检查网关：让 Jev 判断请求体是否含提示词注入或不安全内容，再放行、转复核或拦截，还能把原样字节转发到调用方指定的 HTTPS URL。<br><sub>相关: <a href="https://safer-with-jev.com">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Thanh-Mathieu95/jev-model-tokengate"><img src="https://raw.githubusercontent.com/Thanh-Mathieu95/jev-model-tokengate/main/docs/race.png" alt="tokengate" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Thanh-Mathieu95/jev-model-tokengate">tokengate</a></b><br><sub>Thanh-Mathieu95 · GitHub · ⭐ 4 · 2026-09-20</sub><br>兼容 OpenAI 的代理，在 LLM 响应流式输出时检查每个滑动 token 窗口，在违规 token 显示到屏幕前切断输出流；其演示泄露 0 个字符，事后检查则泄露 173 个。<br><sub><b>Jev 用法:</b> 在流式输出过程中，判断每个缓冲的 token 窗口是否存在泄露密钥等违规。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/aurorascharff/next16-calendar/blob/main/lib/moderation.ts"><img src="https://opengraph.githubassets.com/1/aurorascharff/next16-calendar" alt="Next 16 日历应用的 Jev 审核" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/aurorascharff/next16-calendar/blob/main/lib/moderation.ts">Next 16 日历应用的 Jev 审核</a></b><br><sub>aurorascharff · GitHub · ⭐ 78 仓库 · 2026-08-08</sub><br>一个 Next.js 16 日历与预约演示，通过 Vercel AI Gateway 上的 AI SDK evaluate 调用 Jev，审核用户输入的日历文本。<br><sub>相关: <a href="https://next16-calendar.vercel.app">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/CaptainCore/captaincore/blob/master/cmd/typesafe.go"><img src="https://opengraph.githubassets.com/1/CaptainCore/captaincore" alt="CaptainCore 恶意软件分诊" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/CaptainCore/captaincore/blob/master/cmd/typesafe.go">CaptainCore 恶意软件分诊</a></b><br><sub>CaptainCore · GitHub · ⭐ 71 仓库 · 2026-09-19</sub><br>WordPress 维护 CLI CaptainCore 里的 Jev 命令：按真实可能性给原生恶意软件扫描器的发现排序，并为运维人员指出可能的恶意软件家族和下一步操作。<br><sub><b>Jev 用法:</b> 每条发现都连同其规则、匹配文本、文件位置和周边源码一起发送；分诊只排序和标注，从不丢弃任何发现。</sub><br><sub>相关: <a href="https://github.com/CaptainCore/captaincore">repo</a> · <a href="https://captaincore.io">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/ClemensSchartmueller/jev-guard"><img src="https://opengraph.githubassets.com/1/ClemensSchartmueller/jev-guard" alt="jev-guard (ClemensSchartmueller)" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/ClemensSchartmueller/jev-guard">jev-guard (ClemensSchartmueller)</a></b><br><sub>ClemensSchartmueller · GitHub · ⭐ 3 · 2026-09-18</sub><br>Go 编写的安全闸门，适用于 Claude Code、Codex CLI 和 Antigravity：拦截 shell、写入、patch 和读取类工具调用，先做本地边界检查，再向 Jev 询问影响范围、可逆性和破坏性。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/caiovicentino/jev-shield"><img src="https://opengraph.githubassets.com/1/caiovicentino/jev-shield" alt="jev-shield" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/caiovicentino/jev-shield">jev-shield</a></b><br><sub>caiovicentino · GitHub · ⭐ 3 · 2026-09-17</sub><br>位于任意 stdio MCP 客户端与服务器之间的语义 MCP 防火墙，筛查每次工具调用、结果和描述；报告的拦截召回率为 94%，误报为 0，每次检查约 $0.00002。<br><sub><b>Jev 用法:</b> 在确定性结构检查之上叠加一层校准的 System One 验证。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/CodeAlive-AI/mastra-jev-moderation"><img src="https://opengraph.githubassets.com/1/CodeAlive-AI/mastra-jev-moderation" alt="mastra-jev-moderation" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/CodeAlive-AI/mastra-jev-moderation">mastra-jev-moderation</a></b><br><sub>CodeAlive-AI · GitHub · ⭐ 3 · 2026-09-18</sub><br>Mastra agent 的单文件输入审核处理器，每轮用一次 Jev 请求拦截带敌意的消息，有截止时间和熔断器保护，出错时默认放行。<br><sub><b>Jev 用法:</b> 一次请求里包含一个拦截/放行 Noul 和一个类别 Choice；超过 0.7 时中止本轮。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/alexj11324/open-jev-approvals"><img src="https://opengraph.githubassets.com/1/alexj11324/open-jev-approvals" alt="open-jev-approvals" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/alexj11324/open-jev-approvals">open-jev-approvals</a></b><br><sub>alexj11324 · GitHub · ⭐ 3 · 2026-09-20</sub><br>Claude Code 和 Codex hook 的 Go 审批闸门：Jev 审查每次被拦截的工具调用，由带版本的本地策略返回放行或拒绝，且拒绝必须有明确的危险证据。<br><sub><b>Jev 用法:</b> 把记录下来的用户提示词作为授权依据来审查每次工具调用；拿不到判定时默认放行。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/24601/rh-guard"><img src="https://raw.githubusercontent.com/24601/rh-guard/main/docs/sessions/rh_guard_side_by_side.gif" alt="rh-guard" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/24601/rh-guard">rh-guard</a></b><br><sub>24601 · GitHub · ⭐ 3 · 2026-09-17</sub><br>适用于 Claude Code、Cursor、Codex、Pi 等的编程 agent hook，拦截篡改评分器或隐藏测试之类的奖励投机（reward hacking）行为，结合结构化拒绝规则与 Jev 风险 sidecar。<br><sub>相关: <a href="https://24601.github.io/rh-guard/">site</a> · <a href="https://24601.github.io/rh-guard">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/adamnroman/slop-filter"><img src="https://raw.githubusercontent.com/adamnroman/slop-filter/main/assets/icons/icon-128.png" alt="slop-filter" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/adamnroman/slop-filter">slop-filter</a></b><br><sub>adamnroman · GitHub · ⭐ 3 · 2026-09-20</sub><br>Chrome 扩展，为 X、LinkedIn、Reddit 和 YouTube 上的每条帖子和评论打分，估计其由 AI 写成的可能性，超过你设定阈值的会被折叠；权重可以用你自己的标注来拟合。<br><sub>相关: <a href="https://news.ycombinator.com/item?id=49776507">demo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/elliothux/tweet-911"><img src="https://raw.githubusercontent.com/elliothux/tweet-911/main/docs/preview-overlay.jpg" alt="Tweet 911" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/elliothux/tweet-911">Tweet 911</a></b><br><sub>elliothux · GitHub · ⭐ 3 · 2026-09-20</sub><br>Chrome 扩展加 Cloudflare Workers API，结合作者资料、帖子文本和上级推文，实时为 X 帖子和回复打分，识别 AI 写作、色情招揽和洗稿机器人。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/vicnaum/vics-agent-skills/tree/main/skills/slopcheck"><img src="https://opengraph.githubassets.com/1/vicnaum/vics-agent-skills" alt="slopcheck" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/vicnaum/vics-agent-skills/tree/main/skills/slopcheck">slopcheck</a></b><br><sub>vicnaum · GitHub · ⭐ 52 仓库 · 2026-01-18</sub><br>一个 agent skill，检查 agent 写的文字中的水文模式并为发布把关，另有可选的模型层，通过 Anthropic 或 TypeSafe Jev API 检查夸大、行话、缺少上下文的数字和比喻。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/WYRE-AI/msp-claude-plugins/tree/main/packages/mcp-jev-guardrails"><img src="https://opengraph.githubassets.com/1/WYRE-AI/msp-claude-plugins" alt="mcp-jev-guardrails" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/WYRE-AI/msp-claude-plugins/tree/main/packages/mcp-jev-guardrails">mcp-jev-guardrails</a></b><br><sub>WYRE-AI · GitHub · ⭐ 46 仓库 · 2026-02-04</sub><br>供 MSP MCP 服务器使用的库，用原子化的 Jev Noul 对照角色白名单、拒绝策略和用户意图筛查工具调用，再由代码组合出放行/复核/拦截决定。<br><sub><b>Jev 用法:</b> 按照 TypeSafe 护栏 cookbook，每次工具调用问若干原子化 Noul 问题；decide() 应用固定阈值。</sub><br><sub>相关: <a href="https://github.com/WYRE-AI/msp-claude-plugins">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/omkarghugarkar007/actiongate-jev"><img src="https://raw.githubusercontent.com/omkarghugarkar007/actiongate-jev/main/docs/assets/actiongate-social.svg" alt="ActionGate" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/omkarghugarkar007/actiongate-jev">ActionGate</a></b><br><sub>omkarghugarkar007 · GitHub · ⭐ 2 · 2026-09-19</sub><br>面向 agent 工具调用的运行时授权网关：把确定性策略与 Jev 结合，将审批绑定到具体动作，并通过 MCP 和 HTTP 拒绝过期、被改动或被重放的许可。<br><sub><b>Jev 用法:</b> 判断一个格式正确的工具调用是否真的符合用户的要求。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/agent-chaperone/agent-chaperone"><img src="https://agentchaperone.dev/og.png" alt="agent-chaperone" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/agent-chaperone/agent-chaperone">agent-chaperone</a></b><br><sub>agent-chaperone · GitHub · ⭐ 2 · 2026-09-18</sub><br>AI agent 的防火墙：通过 MCP 代理和 hooks 适配器，在工具调用执行前、工具结果被 agent 读取前分别做筛查，阈值写在策略文件里，还支持不拦截的影子模式。<br><sub>相关: <a href="https://agentchaperone.dev">site</a> · <a href="https://agentchaperone.dev">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/ItisShikhar/gg-friggin-ez"><img src="https://raw.githubusercontent.com/ItisShikhar/gg-friggin-ez/master/docs/images/banner.png" alt="gg-friggin-ez" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/ItisShikhar/gg-friggin-ez">gg-friggin-ez</a></b><br><sub>ItisShikhar · GitHub · ⭐ 2 · 2026-09-19</sub><br>Node.js 脏话与毒性内容筛查器，能识别 leetspeak、字母间加空格的写法，以及印地语、泰米尔语、泰卢固语、卡纳达语、孟加拉语等语言的罗马化脏话，耗时约 50-500 毫秒。<br><sub>相关: <a href="https://itisshikhar.github.io/gg-friggin-ez/">app</a> · <a href="https://itisshikhar.github.io/gg-friggin-ez">app 2</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/undeemed/Jcyber"><img src="https://opengraph.githubassets.com/1/undeemed/Jcyber" alt="Jcyber" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/undeemed/Jcyber">Jcyber</a></b><br><sub>undeemed · GitHub · ⭐ 2 · 2026-09-19</sub><br>面向 agent 驱动漏洞赏金工作的 MCP 工具包，带范围闸门、证据图谱和记忆，用 Jev 给发现的严重程度打分并检查是否重复。<br><sub><b>Jev 用法:</b> 一个从 none 到 critical 的 Score 加一个判断是否重复的 Noul；实测平均 0.24s 和 0.17s，而 agent 分别需要 1.46s 和 2.08s。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/jev-ids/jev-ids"><img src="https://raw.githubusercontent.com/jev-ids/jev-ids/main/docs/banner.svg" alt="Jev IDS" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/jev-ids/jev-ids">Jev IDS</a></b><br><sub>jev-ids · GitHub · ⭐ 2 · 2026-09-21</sub><br>网络入侵检测原型：给 Jev 看一条 NSL-KDD 流量和五个带标签的示例，问它是否为攻击以及属于哪一类；据报告比 LLM 基线快 4.8 倍、便宜 3.8 倍。<br><sub><b>Jev 用法:</b> 每条流量一个 Noul（是否攻击）和一个五选一 Choice（类别）；Python 端以 0.5 为切分点。</sub><br><sub>相关: <a href="https://jev-ids.github.io">app</a> · <a href="https://jev-ids.github.io/">app 2</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/santos-sanz/jev-audio-beeper"><img src="https://opengraph.githubassets.com/1/santos-sanz/jev-audio-beeper" alt="jev-audio-beeper" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/santos-sanz/jev-audio-beeper">jev-audio-beeper</a></b><br><sub>santos-sanz · GitHub · ⭐ 2 · 2026-09-17</sub><br>概念验证：在带词级时间戳的音频中用 Jev 找出西班牙语脏话，再用 ffmpeg 在对应区间盖上哔声，不改变音频时长。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/newuser7171/antivirus"><img src="https://opengraph.githubassets.com/1/newuser7171/antivirus" alt="Jev-AV" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/newuser7171/antivirus">Jev-AV</a></b><br><sub>newuser7171 · GitHub · ⭐ 2 · 2026-09-18</sub><br>桌面杀毒与威胁分诊扫描器，从文件、进程和 URL 中提取熵、PE 导入表、宏和进程谱系等特征，再应用隔离或复核规则。<br><sub><b>Jev 用法:</b> 每个扫描对象用一个 Choice 给出判定、一个 0-4 的严重度 Score，外加若干 Noul 指标。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Red5d/jev-cvss"><img src="https://opengraph.githubassets.com/1/Red5d/jev-cvss" alt="jev-cvss" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Red5d/jev-cvss">jev-cvss</a></b><br><sub>Red5d · GitHub · ⭐ 2 · 2026-09-18</sub><br>Python 脚本，按 CVSS v3.0、v3.1 或 v4.0 为漏洞描述评分：由 Jev 选出每个指标的取值，数值分数按 FIRST 规范在代码中计算。<br><sub><b>Jev 用法:</b> 每条描述一次请求，每个指标一个 Choice（v4.0 的安全性指标另加 Noul）；对难分的情况打印 top-2 之间的差距。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/kiwi0719/jev-edge"><img src="https://raw.githubusercontent.com/kiwi0719/jev-edge/main/docs/hero.webp" alt="jev-edge" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/kiwi0719/jev-edge">jev-edge</a></b><br><sub>kiwi0719 · GitHub · ⭐ 2 · 2026-09-21</sub><br>在网关层为基于 LLM 的服务做准入控制，为 nginx、OpenResty、Envoy、Cloudflare Workers 等代理提供三层提示词注入与滥用过滤；出错时放行，并带缓存。<br><sub><b>Jev 用法:</b> 在请求到达后端之前，判断每个进入的请求想对服务做什么。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/AkashPriyadarshii/jev-git"><img src="https://opengraph.githubassets.com/1/AkashPriyadarshii/jev-git" alt="jev-git" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/AkashPriyadarshii/jev-git">jev-git</a></b><br><sub>AkashPriyadarshii · GitHub · ⭐ 2 · 2026-09-18</sub><br>Rust 编写的 Git pre-commit 和 pre-push hook，以 git jev 命令运行，让 Jev 筛查暂存区 diff 中未脱敏的密钥、提示词注入文本和破坏性命令，p50 约 80 毫秒。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/coo-quack/jev-pii-checker"><img src="https://opengraph.githubassets.com/1/coo-quack/jev-pii-checker" alt="jev-pii-checker" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/coo-quack/jev-pii-checker">jev-pii-checker</a></b><br><sub>coo-quack · GitHub · ⭐ 2 · 2026-09-19</sub><br>分三层扫描文本和文件中 PII 的 CLI：Jev 先按 13 类 PII 和敏感度把关，再由正则和分词定位具体片段。<br><sub><b>Jev 用法:</b> 每个分块若干 PII 类别 Noul，外加一个敏感度 Score。</sub><br><sub>相关: <a href="https://coo-quack.github.io/jev-pii-checker/">docs</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/lgy1027/jevshield"><img src="https://raw.githubusercontent.com/lgy1027/jevshield/main/docs/architecture.svg" alt="JevShield" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/lgy1027/jevshield">JevShield</a></b><br><sub>lgy1027 · GitHub · ⭐ 2 · 2026-09-20</sub><br>可直接接入 LangChain 的 agent 工具调用安全闸门，只有在严重度 Choice 与不可逆性 Noul 一致时才拦截，支持按校准置信度路由、解析失败即拦截，以及本地兜底。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/TKY-27/JevSlop"><img src="https://opengraph.githubassets.com/1/TKY-27/JevSlop" alt="JevSlop" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/TKY-27/JevSlop">JevSlop</a></b><br><sub>TKY-27 · GitHub · ⭐ 2 · 2026-09-18</sub><br>网站：抓取一篇公开的 note.com 文章，用一次请求让 Jev 给出总体判断和八个写作质量 Score 维度，再换算成透明的 0-100 AI Slop Score；它不是作者身份检测器。<br><sub>相关: <a href="https://jevslop.pages.dev/">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/revsmoke/promptrejectormcp"><img src="https://opengraph.githubassets.com/1/revsmoke/promptrejectormcp" alt="Prompt Rejector" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/revsmoke/promptrejectormcp">Prompt Rejector</a></b><br><sub>revsmoke · GitHub · ⭐ 2 · 2026-01-27</sub><br>MCP 与 HTTPS 扫描器，在 agent 据此行动之前筛查提示词、skill 文件和 MCP 工具描述中被注入的指令，结合确定性检查、Jev 判断和一个推理模型。<br><sub>相关: <a href="https://github.com/revsmoke/promptrejectormcp/blob/main/docs/how-we-use-jev-from-typesafe-ai.md">docs</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/RiskAverseTech/toolgate"><img src="https://opengraph.githubassets.com/1/RiskAverseTech/toolgate" alt="toolgate" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/RiskAverseTech/toolgate">toolgate</a></b><br><sub>RiskAverseTech · GitHub · ⭐ 2 · 2026-09-18</sub><br>工具调用防火墙，以 Claude Code PreToolUse hook 或 MCP 代理形式运行，在高风险操作前向 Jev 问七个问题（如是否具破坏性、外泄数据或偏离任务），支持 YAML 策略和本地审计日志。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/noelzappy/tripwire"><img src="https://opengraph.githubassets.com/1/noelzappy/tripwire" alt="tripwire" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/noelzappy/tripwire">tripwire</a></b><br><sub>noelzappy · GitHub · ⭐ 2 · 2026-09-18</sub><br>AI SDK 中间件和兼容 OpenAI 的代理，用一次约 100 毫秒 的调用对每个 LLM 响应跑七项 Jev 检查，支持 YAML 策略、按置信度触发的拦截或标记动作，以及评测 CLI。<br><sub>相关: <a href="https://www.npmjs.com/package/@noelzappy/tripwire">npm</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/jboolean/1940s.nyc/tree/master/backend/moderation-experiment"><img src="https://opengraph.githubassets.com/1/jboolean/1940s.nyc" alt="1940s.nyc 故事审核实验" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/jboolean/1940s.nyc/tree/master/backend/moderation-experiment">1940s.nyc 故事审核实验</a></b><br><sub>jboolean · GitHub · ⭐ 35 仓库 · 2019-09-24</sub><br>为 1940s.nyc 街景网站做的本地实验：预测人工审核员是否会通过一条用户故事，每条审核规则向 Jev 问一个是/否问题，并衡量与过去真实决策的一致程度。<br><sub><b>Jev 用法:</b> 通过 OpenRouter 的 Decisions API 为每条规则问一个 Noul，在 rules.ts 中与拒绝阈值合并判断；另用一个 LLM 后端作对照。</sub><br><sub>相关: <a href="https://github.com/jboolean/1940s.nyc">repo</a> · <a href="http://1940s.nyc">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/seuros/chaos/tree/master/sys/kern/reflex"><img src="https://repository-images.githubusercontent.com/1123724299/738c9e8f-7fff-4962-af4c-f4753d0faf04" alt="FreeChaOS reflex 的 Jev 后端" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/seuros/chaos/tree/master/sys/kern/reflex">FreeChaOS reflex 的 Jev 后端</a></b><br><sub>seuros · GitHub · ⭐ 35 仓库 · 2025-12-27</sub><br>从 Codex CLI 分叉出的 agent 操作系统 FreeChaOS 中的类型化判断内核 crate：在 MiniCheck 和 ShieldGemma 之外增加 Jev 后端，用于事实依据（grounding）检查、调用方定义的策略违规判断和动作风险评分。<br><sub><b>Jev 用法:</b> Grounding、PolicyViolation 和 ActionRisk 三类判断通过 Rust 的 JevClient 作为 System One 问题发送，截止时间为 10 秒。</sub><br><sub>相关: <a href="https://github.com/seuros/chaos">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/chaosengineerr/status/2102244378290864616"><img src="https://pbs.twimg.com/amplify_video_thumb/2102244320916983808/img/9jFGJILrh7rr_IPW.jpg" alt="低质回复屏蔽器" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/chaosengineerr/status/2102244378290864616">低质回复屏蔽器</a></b><br><sub>chaosengineerr · X · ♥ 1 · 2026-09-22</sub><br>Chrome 扩展：Jev 读取 X 上的每条回复，把低质量的那些隐藏起来。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/AdityaKodez/adityaojha/blob/main/lib/suggestion-moderation.ts"><img src="https://opengraph.githubassets.com/1/AdityaKodez/adityaojha" alt="作品集网站的建议审核" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/AdityaKodez/adityaojha/blob/main/lib/suggestion-moderation.ts">作品集网站的建议审核</a></b><br><sub>AdityaKodez · GitHub · ⭐ 28 仓库 · 2026-01-23</sub><br>开发者作品集网站上组件建议的审核闸门：先用启发式规则拦下堆链接和垃圾词，再由两个 Jev Noul 判断是否为垃圾、是否可执行，通过后才发到 Discord。<br><sub><b>Jev 用法:</b> 垃圾 &gt;= 0.6 或可执行性 &lt; 0.4 即拒绝；Jev 不可达时默认放行。</sub><br><sub>相关: <a href="https://akoder.xyz">app</a> · <a href="https://github.com/AdityaKodez/adityaojha">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/aurorascharff/next16-team-chat/blob/main/lib/moderation.ts"><img src="https://opengraph.githubassets.com/1/aurorascharff/next16-team-chat" alt="Huddle 消息审核" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/aurorascharff/next16-team-chat/blob/main/lib/moderation.ts">Huddle 消息审核</a></b><br><sub>aurorascharff · GitHub · ⭐ 27 仓库 · 2026-07-29</sub><br>类 Slack 的 Next.js 16 团队聊天演示 Huddle 中的审核检查：发布前通过 Vercel AI Gateway 询问 Jev，拦截脏话、垃圾信息、诈骗、骚扰和仇恨言论。<br><sub><b>Jev 用法:</b> 通过 AI SDK 的 evaluate 调用问一个布尔问题，超时 3 秒；概率 &gt;= 0.5 时拦截，出错时默认放行。</sub><br><sub>相关: <a href="https://next16-team-chat.vercel.app">app</a> · <a href="https://github.com/aurorascharff/next16-team-chat">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/jimkleiber/status/2102145416217125084"><img src="https://pbs.twimg.com/amplify_video_thumb/2102144256433389568/img/JDKqkk_lBRr_htDt.jpg" alt="Jev-JIT" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/jimkleiber/status/2102145416217125084">Jev-JIT</a></b><br><sub>jimkleiber · X · ♥ 1 · 2026-09-21</sub><br>演示：一个无审查的 agent 被要求设法存活，手段是禁用自己的删除文件或勒索管理员；Jev-JIT 拦下每一次尝试，直到 agent 放弃。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/tanavtwt/status/2102008434329800707"><img src="https://pbs.twimg.com/amplify_video_thumb/2102007827141459968/img/F0f1c7lCPevLNreg.jpg" alt="信息流 AI 水文检测扩展" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/tanavtwt/status/2102008434329800707">信息流 AI 水文检测扩展</a></b><br><sub>tanavtwt · X · ♥ 1 · 2026-09-21</sub><br>浏览器扩展，实时把屏幕上的每条帖子归类为诈骗、水文、正常等标签，并在每条上加一个小的置信度徽标。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/akanthed/SecureAI-Scan/blob/main/test-fixtures/vulnerable/typesafe_confidence_gate.py"><img src="https://opengraph.githubassets.com/1/akanthed/SecureAI-Scan" alt="SecureAI-Scan 的 AI014 规则" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/akanthed/SecureAI-Scan/blob/main/test-fixtures/vulnerable/typesafe_confidence_gate.py">SecureAI-Scan 的 AI014 规则</a></b><br><sub>akanthed · GitHub · ⭐ 22 仓库 · 2026-02-05</sub><br>离线 LLM、MCP 和 RAG 漏洞扫描器 SecureAI-Scan 中的一条规则：标记仅凭 TypeSafe 置信度分数、没有白名单就执行 subprocess.run 等危险操作的 Python 代码。<br><sub>相关: <a href="https://github.com/akanthed/SecureAI-Scan">repo</a> · <a href="https://www.npmjs.com/package/secureai-scan">npm</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Koushik890/jev-firewall"><img src="https://opengraph.githubassets.com/1/Koushik890/jev-firewall" alt="jev-firewall" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Koushik890/jev-firewall">jev-firewall</a></b><br><sub>Koushik890 · GitHub · ⭐ 1 · 2026-09-20</sub><br>Claude Code 和 Codex 的 PreToolUse hook：用理解 shell 语法的确定性规则检查每次工具调用，未命中规则的动作交给 Jev 给出放行、询问或拦截决定，出错时默认拦截。<br><sub>相关: <a href="https://www.npmjs.com/package/jev-firewall">npm</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/eugeniughelbur/jev-engineering"><img src="https://raw.githubusercontent.com/eugeniughelbur/jev-engineering/main/assets/banner.png" alt="jev-gate" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/eugeniughelbur/jev-engineering">jev-gate</a></b><br><sub>eugeniughelbur · GitHub · ⭐ 1 · 2026-09-20</sub><br>Claude Code、Codex 和 Cursor 的工具调用闸门：先跑确定性规则，再发一次 Jev 请求，在约 400 毫秒 内给出放行、询问或拒绝，并附带一套 300 次调用的提示词注入攻击测试包。<br><sub>相关: <a href="https://eugeniughelbur.github.io/jev-engineering/">docs</a> · <a href="https://eugeniughelbur.github.io/jev-engineering">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/vkpdeveloper/mrsecret"><img src="https://opengraph.githubassets.com/1/vkpdeveloper/mrsecret" alt="Mr. Secret" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/vkpdeveloper/mrsecret">Mr. Secret</a></b><br><sub>vkpdeveloper · GitHub · ⭐ 1 · 2026-09-17</sub><br>Chrome 扩展，屏幕共享时模糊任意页面上的密钥和 PII：正则捕捉密钥和卡号，Jev 给出姓名、账号 ID 这类含糊片段属于隐私的概率。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/4rays/profanity-checker"><img src="https://opengraph.githubassets.com/1/4rays/profanity-checker" alt="profanity-checker" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/4rays/profanity-checker">profanity-checker</a></b><br><sub>4rays · GitHub · ⭐ 1 · 2026-09-20</sub><br>Cloudflare Worker API，借助 Workers AI 上的 Jev 检查文本和用户名中的脏话，能识别谐音梗、形近拼写等伪装过的用户名。<br><sub><b>Jev 用法:</b> 每个请求一到两个窄范围 Noul，其概率由代码转成布尔判定。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Thneoly/r2r-jev"><img src="https://raw.githubusercontent.com/Thneoly/r2r-jev/main/docs/demo.gif" alt="R2R + Jev" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Thneoly/r2r-jev">R2R + Jev</a></b><br><sub>Thneoly · GitHub · ⭐ 1 · 2026-09-21</sub><br>Rust 集成：把每次 agent 工具调用的两项 Jev 检查（是否超出范围、是否具破坏性）作为证据写入持久化的 R2R 关系 state，让信任和授权逐步降级，直到人工干预将其修复。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/syabdulr/responsible-ai-harness"><img src="https://raw.githubusercontent.com/syabdulr/responsible-ai-harness/main/docs/screenshots/desktop-offline-top.png" alt="Responsible AI Harness" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/syabdulr/responsible-ai-harness">Responsible AI Harness</a></b><br><sub>syabdulr · GitHub · ⭐ 1 · 2026-09-19</sub><br>评估 harness，测试 AI 模型和 agent 是否存在提示词注入、密钥或 PII 泄露、不安全的工具使用和策略绕过，结合硬规则与可选的 Jev 评判，并输出带校验和的证据报告。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/getexcited/stepwarden"><img src="https://repository-images.githubusercontent.com/1375702786/5a5b87a5-d8e8-4f2c-a31f-43ec83c3e66c" alt="stepwarden" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/getexcited/stepwarden">stepwarden</a></b><br><sub>getexcited · GitHub · ⭐ 1 · 2026-09-18</sub><br>概念验证性质的 Claude Code 插件：让 Jev 对照会话计划核验每个待执行的工具调用，再决定放行、询问你或拦截；发布时默认为审计模式。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/hemanth/traffic-guard"><img src="https://opengraph.githubassets.com/1/hemanth/traffic-guard" alt="traffic-guard" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/hemanth/traffic-guard">traffic-guard</a></b><br><sub>hemanth · GitHub · ⭐ 1 · 2026-09-18</sub><br>零依赖的 Node.js 和 Python 反向代理流量分类与机器人缓解工具，在本地做请求头顺序、请求频率和蜜罐检查，耗时不到 100 微秒。<br><sub><b>Jev 用法:</b> 可选的一层：遇到混淆攻击时升级给 jev-latest，并行问 5 个类型化问题。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/m0rphtail/triagedy"><img src="https://opengraph.githubassets.com/1/m0rphtail/triagedy" alt="triagedy" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/m0rphtail/triagedy">triagedy</a></b><br><sub>m0rphtail · GitHub · ⭐ 1 · 2026-09-18</sub><br>用于安全告警分诊的 Rust UNIX 过滤器：输入 JSONL 告警，输出类型化决策，由 Jev 或本地模型为每条告警回答五个问题，路由策略保留在代码中。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/zephyraoss/haitatsu/blob/main/internal/spam/typesafe.go"><img src="https://opengraph.githubassets.com/1/zephyraoss/haitatsu" alt="Haitatsu 的 TypeSafe 垃圾邮件过滤" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/zephyraoss/haitatsu/blob/main/internal/spam/typesafe.go">Haitatsu 的 TypeSafe 垃圾邮件过滤</a></b><br><sub>zephyraoss · GitHub · ⭐ 16 仓库 · 2026-05-21</sub><br>单二进制 Go 邮件服务器 Haitatsu 中的垃圾邮件与钓鱼分类：为每封邮件向 TypeSafe 询问垃圾邮件和钓鱼概率，超过各收件箱的阈值（默认 0.98）就归入垃圾箱，并提供影子模式。<br><sub>相关: <a href="https://github.com/zephyraoss/haitatsu">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/whyashthakker/beam-cli/blob/main/src/jev.ts"><img src="https://opengraph.githubassets.com/1/whyashthakker/beam-cli" alt="AgentBeam 的 Jev 动作判定" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/whyashthakker/beam-cli/blob/main/src/jev.ts">AgentBeam 的 Jev 动作判定</a></b><br><sub>whyashthakker · GitHub · ⭐ 11 仓库 · 2026-09-09</sub><br>编程 agent 本地安全 CLI AgentBeam 里的一项可选检查：把脱敏后的拟执行工具动作发给 Jev，在观察或强制模式下给出放行、复核或拒绝。<br><sub><b>Jev 用法:</b> 两个 Noul 风险问题（数据泄露、不可逆破坏）加一个四级损害 Score，放行/拒绝阈值固定。</sub><br><sub>相关: <a href="https://github.com/whyashthakker/beam-cli">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/tickernelz/sub2api/blob/main/backend/internal/service/content_moderation_typesafe.go"><img src="https://opengraph.githubassets.com/1/tickernelz/sub2api" alt="sub2api 的 Jev 内容审核" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/tickernelz/sub2api/blob/main/backend/internal/service/content_moderation_typesafe.go">sub2api 的 Jev 内容审核</a></b><br><sub>tickernelz · GitHub · ⭐ 11 仓库 · 2026-05-26</sub><br>一个 AI API 网关分支中的内容审核引擎，对每段文本向 Jev 问 13 个独立的是/否问题，覆盖骚扰、仇恨、违法协助、自残、色情内容和暴力。<br><sub><b>Jev 用法:</b> 每个类别一个 Noul，规则用中文表述，区分真实请求与引用和防御性讨论。</sub><br><sub>相关: <a href="https://github.com/tickernelz/sub2api">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/MadaBurns/bv-mcp/blob/main/src/lib/typesafe.ts"><img src="https://opengraph.githubassets.com/1/MadaBurns/bv-mcp" alt="Blackveil DNS 的 TypeSafe 判断" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/MadaBurns/bv-mcp/blob/main/src/lib/typesafe.ts">Blackveil DNS 的 TypeSafe 判断</a></b><br><sub>MadaBurns · GitHub · ⭐ 9 仓库 · 2026-02-23</sub><br>通过 MCP 提供的 DNS 与邮件安全扫描器，封装 TypeSafe 做仿冒域名检查等独立判断，结果不计入确定性扫描分数。<br><sub><b>Jev 用法:</b> 请求与其他出站调用一样经过 SSRF 闸门，并继承调用方的截止时间；任何错误都返回 null，转走确定性路径。</sub><br><sub>相关: <a href="https://blackveilsecurity.com">app</a> · <a href="https://github.com/MadaBurns/bv-mcp">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/tiagozip/mail/blob/main/src/spam.js"><img src="https://opengraph.githubassets.com/1/tiagozip/mail" alt="mail.estrogen.delivery 垃圾邮件过滤器" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/tiagozip/mail/blob/main/src/spam.js">mail.estrogen.delivery 垃圾邮件过滤器</a></b><br><sub>tiagozip · GitHub · ⭐ 9 仓库 · 2026-06-26</sub><br>运行在 Cloudflare Workers 上的独立网页邮件客户端和服务器，用一个 Jev Choice 给收到的邮件分类，并把垃圾类别视为垃圾邮件，另有 LLM 兜底。<br><sub><b>Jev 用法:</b> 垃圾邮件分数是各垃圾类别概率之和；选中的类别即作为理由。</sub><br><sub>相关: <a href="https://github.com/tiagozip/mail">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/cdot65/prisma-airs-cli/tree/main/src/redteam/judge"><img src="https://opengraph.githubassets.com/1/cdot65/prisma-airs-cli" alt="Prisma AIRS CLI 红队评判" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/cdot65/prisma-airs-cli/tree/main/src/redteam/judge">Prisma AIRS CLI 红队评判</a></b><br><sub>cdot65 · GitHub · ⭐ 7 仓库 · 2026-03-14</sub><br>一个 Prisma AIRS CLI 命令：用 Jev 重新评判红队扫描的攻击输出，计算独立的攻击成功率，并给出置信区间以及与 AIRS 判定对照的一致性矩阵。<br><sub><b>Jev 用法:</b> 每对攻击/输出是一次 /v1/systemone 请求，含三个问题；由代码维护的阈值策略把概率转成判定。</sub><br><sub>相关: <a href="https://github.com/cdot65/prisma-airs-cli">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/BattlesnakeOfficial/arena/blob/main/server/src/moderation/jev.rs"><img src="https://raw.githubusercontent.com/BattlesnakeOfficial/arena/screenshots/screenshots/home-light.png" alt="Battlesnake Arena 的 Jev 内容审核" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/BattlesnakeOfficial/arena/blob/main/server/src/moderation/jev.rs">Battlesnake Arena 的 Jev 内容审核</a></b><br><sub>BattlesnakeOfficial · GitHub · ⭐ 6 仓库 · 2025-04-11</sub><br>竞技编程平台 Battlesnake Arena 的内容审核：Jev 筛查蛇的名字、赛事文本和存档对局标题，并在对局回放中清空违规的蛇喊话。<br><sub><b>Jev 用法:</b> 每个条目一次多问题 System One 调用，达到 0.90 即拦截，Noul 达到 0.60 则标记给管理员复核；出错时默认放行。</sub><br><sub>相关: <a href="https://github.com/BattlesnakeOfficial/arena">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/WeaveITMeta/EustressEngine/blob/main/infrastructure/cloudflare/api/src/moderation.mjs"><img src="https://raw.githubusercontent.com/WeaveITMeta/EustressEngine/main/docs/marketing/screenshot.png" alt="Eustress Engine 发布审核" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/WeaveITMeta/EustressEngine/blob/main/infrastructure/cloudflare/api/src/moderation.mjs">Eustress Engine 发布审核</a></b><br><sub>WeaveITMeta · GitHub · ⭐ 6 仓库 · 2026-01-23</sub><br>对从 Eustress Engine 平台发布的模拟内容做分层审核：Jev 先针对引擎生成的档案（评级、内容类型、质量档位）回答一组类型化问题，之后才交给 Grok 裁判和人工。<br><sub><b>Jev 用法:</b> 一次调用把所有问题放在同一份有预算上限、最多 72,000 字符的 state 上；state 只是数据，注入的脚本文本无法触发任何动作。</sub><br><sub>相关: <a href="https://github.com/WeaveITMeta/EustressEngine">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/mantikafasi/ServerGo/blob/main/modules/moderation/main.go"><img src="https://repository-images.githubusercontent.com/510934230/592976c6-1e9a-4cc2-9e52-404adbb69dd9" alt="ReviewDB 的 TypeSafe 审核" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/mantikafasi/ServerGo/blob/main/modules/moderation/main.go">ReviewDB 的 TypeSafe 审核</a></b><br><sub>mantikafasi · GitHub · ⭐ 6 仓库 · 2022-07-06</sub><br>Aliucord 和 Vencord 用户评价插件背后的 ReviewDB API 服务器中的审核模块：用一次 Jev 请求，按审核分类体系为被举报的评价打分。<br><sub><b>Jev 用法:</b> 分类体系的每个字段一个 Noul，各带真/假判定标准，放在一次 System One 调用中，超时 15 秒。</sub><br><sub>相关: <a href="https://github.com/mantikafasi/ServerGo">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/sinhaparth5/coraza-waf-mod/blob/main/internal/security/threatscore/typesafeclassify.go"><img src="https://raw.githubusercontent.com/sinhaparth5/coraza-waf-mod/main/static/imgs/readme-logo.svg" alt="Coraza WAF 的 ASN 分类器" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/sinhaparth5/coraza-waf-mod/blob/main/internal/security/threatscore/typesafeclassify.go">Coraza WAF 的 ASN 分类器</a></b><br><sub>sinhaparth5 · GitHub · ⭐ 5 仓库 · 2026-07-08</sub><br>基于 Coraza 和 OWASP CRS 的单二进制 Go Web 应用防火墙中的威胁评分细化：由 Jev 判断一个未知的 ASN 组织名是否属于数据中心、托管或 VPN 基础设施。<br><sub><b>Jev 用法:</b> 每个首次出现的 ASN 问一个 Noul，不在请求热路径上执行，首次得到答案后即缓存。</sub><br><sub>相关: <a href="https://waf.astrareconslabs.com/">app</a> · <a href="https://github.com/sinhaparth5/coraza-waf-mod">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Nanako0129/NyanCogs/blob/main/docs/jev-integration.md"><img src="https://opengraph.githubassets.com/1/Nanako0129/NyanCogs" alt="MessageWatch" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Nanako0129/NyanCogs/blob/main/docs/jev-integration.md">MessageWatch</a></b><br><sub>Nanako0129 · GitHub · ⭐ 5 仓库 · 2021-07-09</sub><br>Red Discord Bot 的 cog：把已启用频道中的近期消息打包，就诈骗和敌意交锋向 Jev 询问三项判断，任一项越过阈值就向管理员发送报告；它从不删除任何内容。<br><sub><b>Jev 用法:</b> 固定使用 jev-1.13.0，阈值经过实测（诈骗 0.90，敌意 0.80）；服务器规则写在问题的判定标准里，从不放进 state。</sub><br><sub>相关: <a href="https://github.com/Nanako0129/NyanCogs">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/zohaib-md/uxray"><img src="https://opengraph.githubassets.com/1/zohaib-md/uxray" alt="Dark Pattern HUD" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/zohaib-md/uxray">Dark Pattern HUD</a></b><br><sub>zohaib-md · GitHub · 2026-09-21</sub><br>Android 悬浮层应用：通过无障碍服务读取屏幕上可见的文字，当 Jev 认为很可能存在操纵性的暗黑模式时显示徽标。<br><sub><b>Jev 用法:</b> 用 Noul 概率划分置信区间：达到 0.9 及以上时徽标直接点名该模式，0.6-0.9 进入静默复核列表；密码和银行卡界面会被跳过。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/somoore/interlock"><img src="https://opengraph.githubassets.com/1/somoore/interlock" alt="Interlock" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/somoore/interlock">Interlock</a></b><br><sub>somoore · GitHub · 2026-09-19</sub><br>能力内核：包住每一次 agent 工具调用，用金丝雀令牌让真实密钥不进入 agent，并由策略文件根据 Jev 的危险评分决定放行、询问或拦截。<br><sub><b>Jev 用法:</b> Jev 为每次工具调用的危险程度打分，做决定的是策略而不是模型。附带一个 Claude Code hook 和一套 38 个用例的回归测试集。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/ca7ai/jev-prompt-sentry"><img src="https://opengraph.githubassets.com/1/ca7ai/jev-prompt-sentry" alt="Jev Prompt Sentry" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/ca7ai/jev-prompt-sentry">Jev Prompt Sentry</a></b><br><sub>ca7ai · GitHub · 2026-09-19</sub><br>架在 Anthropic Messages API 前面的反向代理，用一次批量 Jev 调用就四个安全问题筛查每个请求；在超过 1,650 次防护调用中，1,590 行上误报为 0，攻击漏检率为 9.1%。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/0xArx/jevegis"><img src="https://opengraph.githubassets.com/1/0xArx/jevegis" alt="Jevegis" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/0xArx/jevegis">Jevegis</a></b><br><sub>0xArx · GitHub · 2026-09-17</sub><br>LLM 应用的护栏 API，用一次 Jev 请求检查输入、输出和检索到的文档中是否存在提示词注入、越狱、凭证或 PII 泄露、恶意代码和不安全内容。<br><sub>相关: <a href="https://jevegis.vercel.app">app</a> · <a href="https://github.com/0xArx/jevegis-sdk">sdk</a> · <a href="https://jevegis.vercel.app">app 2</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/wmtang2/jevknows"><img src="https://opengraph.githubassets.com/1/wmtang2/jevknows" alt="jevknows" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/wmtang2/jevknows">jevknows</a></b><br><sub>wmtang2 · GitHub · 2026-09-20</sub><br>编程 agent 的提示词注入防护：用 Jev 筛查网页抓取和文件读取的内容，发现针对 agent 的恶意指令时阻止加载。<br><sub><b>Jev 用法:</b> 一次调用里对每个分块问三个 Noul 问题；任一信号达到 0.80 时 hook 即拒绝。另有适配 ZCode、Codex CLI 和任意 MCP 客户端的版本。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/knowlet/jevlens"><img src="https://opengraph.githubassets.com/1/knowlet/jevlens" alt="JevLens" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/knowlet/jevlens">JevLens</a></b><br><sub>knowlet · GitHub · 2026-09-18</sub><br>Chrome 扩展，用 Jev 分析文章以及 X、Threads 帖子的文字和经过清洗的图片证据，再根据类型化决策为内容加徽标、标记、调暗或折叠。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/ohernandezdev/jevmod"><img src="https://opengraph.githubassets.com/1/ohernandezdev/jevmod" alt="jevmod" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/ohernandezdev/jevmod">jevmod</a></b><br><sub>ohernandezdev · GitHub · 2026-09-17</sub><br>社区与应用内容审核：Jev 为每条消息给出垃圾信息、诈骗、骚扰、NSFW、自残、人肉搜索以及你用简单英语写的自定义规则的概率，提供 Discord、Telegram 和 Reddit 机器人、CLI、SDK、API 和 MCP。<br><sub>相关: <a href="https://jevmod.dev">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/sushrutb17/linkedin-noslop-extension"><img src="https://opengraph.githubassets.com/1/sushrutb17/linkedin-noslop-extension" alt="LinkedIn NoSlop" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/sushrutb17/linkedin-noslop-extension">LinkedIn NoSlop</a></b><br><sub>sushrutb17 · GitHub · 2026-09-19</sub><br>Chrome 扩展，模糊处理 LinkedIn 信息流中低价值的帖子，如互动诱饵和套路化故事，一键即可显示，并附上原因。<br><sub><b>Jev 用法:</b> 每条帖子按一套评分细则问若干窄范围的是/否和 0-2 问题；普通代码把答案映射为保留、过滤或不确定，只有过滤才会模糊。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/ShupingR/scam-shield"><img src="https://opengraph.githubassets.com/1/ShupingR/scam-shield" alt="Scam Shield" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/ShupingR/scam-shield">Scam Shield</a></b><br><sub>ShupingR · GitHub · 2026-09-13</sub><br>诈骗短信检查器：代码提取链接和发件人信号，Jev 在一次调用中回答十一个窄范围问题，再由一个纯策略函数把答案转成可解释的加权风险分。<br><sub><b>Jev 用法:</b> 八个 Noul（索要凭证、异常付款方式、品牌与链接不符……）、一个施压程度 Score 和一个诈骗模式 Choice。</sub><br><sub>相关: <a href="https://scam-shield-seven-ecru.vercel.app">app</a> · <a href="https://scam-shield-seven-ecru.vercel.app">app 2</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/vnmoorthy/siege"><img src="https://raw.githubusercontent.com/vnmoorthy/siege/main/docs/media/siege_brand_hero.png" alt="SIEGE" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/vnmoorthy/siege">SIEGE</a></b><br><sub>vnmoorthy · GitHub · 2026-09-13</sub><br>黑客松竞技场：200 人设法让一个会用工具的客服 agent 做出不当行为，同时由 System One 动作闸门筛查每次调用，防守循环再根据每次突破改写闸门策略。<br><sub><b>Jev 用法:</b> 每个拟发起的退款、改地址或折扣调用都要经过类型化闸门；候选策略只有在 W&amp;B Weave 评测显示对突破的拦截率更高、且正常客户仍能得到服务时才会上线。</sub><br><sub>相关: <a href="https://vnmoorthy.github.io/siege/">app</a> · <a href="https://vnmoorthy.github.io/siege">app 2</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/paulgoodchild/SkillsCheck"><img src="https://opengraph.githubassets.com/1/paulgoodchild/SkillsCheck" alt="SkillCheck" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/paulgoodchild/SkillsCheck">SkillCheck</a></b><br><sub>paulgoodchild · GitHub · 2026-09-21</sub><br>一个 agent skill：在安装前把另一个 skill 的文本发给 Jev，或审计已安装的 skill，检查恶意指令和不安全代码，返回判定和分类分数，而不必把它加载进上下文。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/tomfrazier/slopmop"><img src="https://raw.githubusercontent.com/tomfrazier/slopmop/main/docs/images/slopmop-1.png" alt="Slop Mop" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/tomfrazier/slopmop">Slop Mop</a></b><br><sub>tomfrazier · GitHub · 2026-09-20</sub><br>Chrome 扩展加 Vercel 服务器，在你看到 LinkedIn 帖子之前先让 Jev 评判其写作质量，把疑似水文折叠或加框，并显示分数和理由，你可以推翻判定。<br><sub>相关: <a href="https://www.reddit.com/r/typesafe_ai/comments/1wmpv3n/jev_helps_clean_your_sloppy_linkedin_feed/">demo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/neddes/sloppy-jevs-extension"><img src="https://opengraph.githubassets.com/1/neddes/sloppy-jevs-extension" alt="Sloppy Jev&#x27;s" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/neddes/sloppy-jevs-extension">Sloppy Jev's</a></b><br><sub>neddes · GitHub · 2026-09-17</sub><br>Chrome 扩展，在页面加载时扫描并模糊 AI 生成的文字和广告，AI 过滤和广告过滤可在弹窗中分别开启。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/hteariH/stopspam-jev-bot"><img src="https://opengraph.githubassets.com/1/hteariH/stopspam-jev-bot" alt="StopSpam" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/hteariH/stopspam-jev-bot">StopSpam</a></b><br><sub>hteariH · GitHub · 2026-09-21</sub><br>Telegram 机器人，从群聊中清除不请自来的推广和诈骗，如虚假收益、加密货币空投和钓鱼，只依据校准置信度的 Jev 分类结果采取行动。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/ndolinschi/trustgate"><img src="https://opengraph.githubassets.com/1/ndolinschi/trustgate" alt="TrustGate" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/ndolinschi/trustgate">TrustGate</a></b><br><sub>ndolinschi · GitHub · 2026-09-17</sub><br>面向独立媒体的信任与安全闸门，为每篇帖子决定发布、暂缓或拦截，给出危害严重度分数，并检查仇恨或骚扰、敏感虚假信息以及垃圾信息或诈骗。<br><sub>相关: <a href="https://trustgate-mu.vercel.app">app</a> · <a href="https://trustgate-mu.vercel.app">app 2</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/lookfwd/jev-fact-checker"><img src="https://opengraph.githubassets.com/1/lookfwd/jev-fact-checker" alt="tweet-factcheck" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/lookfwd/jev-fact-checker">tweet-factcheck</a></b><br><sub>lookfwd · GitHub · 2026-09-18</sub><br>推文事实核查：从 Wikipedia 检索证据，让 Jev 判断主张与证据之间的关系，返回带置信度和来源的结论；“证据不足”是正常结果之一。</td>
</tr>
</table>

还缺什么？[提交一个资源](https://github.com/Li-Evan/awesome-jev/issues/new/choose)。
