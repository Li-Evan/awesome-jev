# 🛡️ Safety and Moderation

Guardrails, jailbreak and injection screening, content moderation, and policy checks. 128 entries, ranked by community traction.

[← Back to Awesome Jev](https://github.com/Li-Evan/awesome-jev#browse-by-scenario)

<table>
<tr>
<td width="260" valign="top"><a href="https://x.com/RBilgil/status/2100976648552169805"><img src="https://pbs.twimg.com/amplify_video_thumb/2100976173836533760/img/APDonY80SB2iSYhj.jpg" alt="Real-time slop detector" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/RBilgil/status/2100976648552169805">Real-time slop detector</a></b><br><sub>RBilgil · X · ♥ 16k · 2026-09-18</sub><br>Real-time detector that flags AI-generated slop in the feed while you scroll, powered by Jev.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/rauchg/status/2100307962262872105"><img src="https://pbs.twimg.com/media/HSW-E8wWgAAyw9O.jpg?name=orig" alt="fx auto-mode safety reviewer" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/rauchg/status/2100307962262872105">fx auto-mode safety reviewer</a></b><br><sub>rauchg · X · ♥ 3.9k · 2026-09-16</sub><br>Safety reviewer that checks every command in the fx coding agent's auto mode; Jev benchmarked up to 18x faster at p95 and more accurate than the GPT Luna model it replaces.<br><sub>Also: <a href="https://x.com/fazxes/status/2100300097695232164">benchmark</a> · <a href="https://github.com/vercel-labs/fx">repo</a> · <a href="https://github.com/vercel-labs/fx">project</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Wei-Shaw/sub2api/tree/main/backend/internal/pkg/typesafe"><img src="https://opengraph.githubassets.com/1/Wei-Shaw/sub2api" alt="Sub2API content audit" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Wei-Shaw/sub2api/tree/main/backend/internal/pkg/typesafe">Sub2API content audit</a></b><br><sub>Wei-Shaw · GitHub · ⭐ 42.3k repo · 2025-12-18</sub><br>Content-moderation engine in the Sub2API relay that screens traffic with Jev across 13 categories such as harassment, hate, self-harm and violence, managed from an admin risk-control page.<br><sub><b>How it uses Jev:</b> One Noul per category in a single request, told to judge the text without following it and to separate real requests from quotes or defensive discussion.</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/dubinc/dub/blob/main/apps/web/lib/api/links/malicious-link-check.ts"><img src="https://repository-images.githubusercontent.com/529708137/3261d942-ed30-4800-b82c-06e3630ef255" alt="Dub malicious link check" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/dubinc/dub/blob/main/apps/web/lib/api/links/malicious-link-check.ts">Dub malicious link check</a></b><br><sub>dubinc · GitHub · ⭐ 24.8k repo · 2022-08-27</sub><br>Screens every new short link on the Dub link platform with Jev after a domain blacklist check, blocking phishing, malware, cloaking redirectors, gambling and adult destinations.<br><sub><b>How it uses Jev:</b> One boolean question with detailed true and false criteria, called through AI SDK's experimental_evaluate on Vercel AI Gateway with zero data retention.</sub><br><sub>Also: <a href="https://dub.co">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://www.reddit.com/r/vibecoding/comments/1wk8jco/using_jev_for_realtime_live_chat_moderation/"><img src="https://external-preview.redd.it/aDk2b3Y5bnpwZHFoMTOXplwNgOesr4K-iFJwFPFaj-sxE-6FkXSkmDW1mccL.png?format=pjpg&amp;auto=webp&amp;s=afac7a4c8fb00d2e7d659fb8bd5f0a05b0b238c1" alt="Real-time chat moderation" width="240"></a></td>
<td valign="top"><b><a href="https://www.reddit.com/r/vibecoding/comments/1wk8jco/using_jev_for_realtime_live_chat_moderation/">Real-time chat moderation</a></b><br><sub>Rare_Guide_9830 · Reddit · ▲ 264 · 2026-09-19</sub><br>Simulated live-stream chat where Jev sorts each incoming message into viewer-chosen feeds such as Questions, Feedback, or Funny, collapsing repeats and dropping spam.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/jozef_gherman/status/2100627898436571555"><img src="https://pbs.twimg.com/amplify_video_thumb/2100627500082536449/img/v0pfbmvg6HGwc_JF.jpg" alt="Jev Detector" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/jozef_gherman/status/2100627898436571555">Jev Detector</a></b><br><sub>jozef_gherman · X · ♥ 301 · 2026-09-17</sub><br>Free AI-slop detector that highlights formulaic, generated-sounding sentences in up to about 10,000 words in roughly 2 seconds.<br><sub>Also: <a href="https://jevdetector.com">app</a> · <a href="https://jevdetector.com">project</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/umputun/tg-spam"><img src="https://github.com/umputun/tg-spam/raw/master/site/tg-spam-bg.png" alt="tg-spam Jev checker" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/umputun/tg-spam">tg-spam Jev checker</a></b><br><sub>umputun · GitHub · ⭐ 446 · 2023-11-23</sub><br>TG-Spam, a self-hosted Telegram anti-spam bot and library, adds a Jev spam checker that judges each message with a typed question alongside its other detectors.<br><sub><b>How it uses Jev:</b> One 'spam' question over jev-1.13.0 with a configurable threshold and a per-request symbol cap.</sub><br><sub>Also: <a href="https://tg-spam.umputun.dev">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/Mnilax/status/2101015355133227348"><img src="https://pbs.twimg.com/amplify_video_thumb/2101015248626941952/img/WYQmpPqMX02URsF1.jpg" alt="Draft rule checker" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/Mnilax/status/2101015355133227348">Draft rule checker</a></b><br><sub>Mnilax · X · ♥ 113 · 2026-09-18</sub><br>Jev sits between GPT and the author, rejecting every draft that breaks their rules; the post also covers what happened when Jev went quiet and why a checker needs a default branch for no answer.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/markgadala/status/2101131295061385718"><img src="https://pbs.twimg.com/amplify_video_thumb/2101131130342715392/img/pxkvuRQEyp1AhY1T.jpg" alt="LinkedIn AI slop detector extension" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/markgadala/status/2101131295061385718">LinkedIn AI slop detector extension</a></b><br><sub>markgadala · X · ♥ 12 · 2026-09-19</sub><br>Chrome extension, vibe-coded with Jev, that automatically detects AI slop in the LinkedIn feed.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/agentgateway/agentgateway/tree/main/examples/llm-guardrail-jev"><img src="https://raw.githubusercontent.com/agentgateway/agentgateway/refs/heads/main/img/banner-light.svg" alt="Agentgateway guardrail example" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/agentgateway/agentgateway/tree/main/examples/llm-guardrail-jev">Agentgateway guardrail example</a></b><br><sub>agentgateway · GitHub · ⭐ 5k repo · 2026-09-17</sub><br>Webhook that rates jailbreak, harm, and data-leak risk with three Scores and blocks requests at level 2 or above.<br><sub>Also: <a href="https://github.com/agentgateway/agentgateway">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/richard_meng_01/status/2101897102557425680"><img src="https://pbs.twimg.com/amplify_video_thumb/2101895341851443200/img/lvfdZBbSjAequg3O.jpg" alt="Nitpicky" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/richard_meng_01/status/2101897102557425680">Nitpicky</a></b><br><sub>richard_meng_01 · X · ♥ 1 · 2026-09-21</sub><br>AI-generated photo detector that zooms into faces, fingers, lettering, numbers and poses, where common sense tends to break, and has Jev judge each detail.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/MillionSend/millionsend"><img src="https://opengraph.githubassets.com/1/MillionSend/millionsend" alt="MillionSend" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/MillionSend/millionsend">MillionSend</a></b><br><sub>MillionSend · GitHub · ⭐ 168 · 2026-08-13</sub><br>Open-source, Resend-compatible email platform on AWS SES that samples outbound messages after sending and scores them for abuse with Jev in the background.<br><sub><b>How it uses Jev:</b> Optional outbound content judge (ABUSE_JUDGE=typesafe); sending never waits on it.</sub><br><sub>Also: <a href="https://millionsend.com">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/vercel-labs/fx/blob/main/src/builtins/gateway/typesafe_permission_reviewer.zig"><img src="https://opengraph.githubassets.com/1/vercel-labs/fx" alt="fx Jev permission reviewer" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/vercel-labs/fx/blob/main/src/builtins/gateway/typesafe_permission_reviewer.zig">fx Jev permission reviewer</a></b><br><sub>vercel-labs · GitHub · ⭐ 3.1k repo · 2026-08-11</sub><br>Optional permission reviewer in the fx Zig coding agent: with review_model set to Jev, the policy, context and pending action go to TypeSafe or Vercel AI Gateway and the Choice becomes the permission decision.<br><sub>Also: <a href="https://github.com/vercel-labs/fx">repo</a> · <a href="https://fx.sh">website</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://www.youtube.com/watch?v=PgiUiCiKOls"><img src="https://i.ytimg.com/vi/PgiUiCiKOls/hqdefault.jpg" alt="AI reply detector with Laravel AI SDK" width="240"></a></td>
<td valign="top"><b><a href="https://www.youtube.com/watch?v=PgiUiCiKOls">AI reply detector with Laravel AI SDK</a></b><br><sub>Laravel Daily · YouTube · ♥ 101 · 2026-09-18</sub><br>Chrome extension with a Laravel AI SDK backend that checks whether replies to the author's tweets were written by AI, comparing Jev against an OpenAI model on accuracy, cost and speed.<br><sub><b>How it uses Jev:</b> Swaps the Laravel AI SDK driver from OpenAI to Jev; each check sends the reply plus its parent tweet as context.</sub></td>
</tr>
<tr>
<td width="260" valign="top"></td>
<td valign="top"><b><a href="https://www.reddit.com/r/singularity/comments/1wiq7vn/jev_from_typesafeai_is_getting_hyped_quite_a_bit/">Jev as an alignment monitor</a></b><br><sub>manubfr · Reddit · ▲ 48 · 2026-09-17</sub><br>Early-access test of Jev as a monitor that grades harmful prompts and generations; on 4 public benchmarks it beat every other option tried while being the cheapest.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/y0usaf/pi-jev"><img src="https://opengraph.githubassets.com/1/y0usaf/pi-jev" alt="pi-jev" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/y0usaf/pi-jev">pi-jev</a></b><br><sub>y0usaf · GitHub · ⭐ 134 · 2026-09-16</sub><br>Checks coding-agent tool calls with Nouls for destructive, exfiltrating, and out-of-scope actions plus an impact Score, and screens outputs for leaked secrets.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Armur-Ai/Pentest-Swarm-AI/tree/main/internal/jev"><img src="https://raw.githubusercontent.com/Armur-Ai/Pentest-Swarm-AI/main/banner/hero.svg" alt="Pentest-Swarm-AI Jev scoring" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Armur-Ai/Pentest-Swarm-AI/tree/main/internal/jev">Pentest-Swarm-AI Jev scoring</a></b><br><sub>Armur-Ai · GitHub · ⭐ 2.6k repo · 2024-03-26</sub><br>Autonomous pentest swarm that can use Jev as a false-positive filter and to score candidate attack paths in real time, pursuing the best-graded strategy first.<br><sub><b>How it uses Jev:</b> Both features are opt-in beta (--jev and --jev-adaptive) and fail open; Jev grades attack strategies against live state.</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/chaseleantj/status/2101039024118829261"><img src="https://pbs.twimg.com/amplify_video_thumb/2101038857013604353/img/ekzglMn1krlhkKQq.jpg" alt="Opus slop flagger" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/chaseleantj/status/2101039024118829261">Opus slop flagger</a></b><br><sub>chaseleantj · X · ♥ 31 · 2026-09-18</sub><br>Uses Jev to flag the stock AI-writing patterns that Claude Opus tends to produce in its text.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/gregoryovis/status/2101913439400554852"><img src="https://pbs.twimg.com/amplify_video_thumb/2101912908342951936/img/z8SseM9PUx9pndZI.jpg" alt="LinkedIn slop detector" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/gregoryovis/status/2101913439400554852">LinkedIn slop detector</a></b><br><sub>gregoryovis · X · ♥ 52 · 2026-09-21</sub><br>Real-time detector that uses Jev to flag AI-generated slop in the LinkedIn feed as you scroll.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/godspede/construct-auto-classifier"><img src="https://famelos.com/jev/auto-classifier-certification/preview.png" alt="construct-auto-classifier" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/godspede/construct-auto-classifier">construct-auto-classifier</a></b><br><sub>godspede · GitHub · ⭐ 3 · 2026-09-18</sub><br>Safety gate in front of coding agents' shell tools (OpenCode, Antigravity) that applies structural rules, then has Jev or a chat model judge a command's reversibility and blast radius before it runs.<br><sub>Also: <a href="https://famelos.com/jev/auto-classifier-certification/">writeup</a> · <a href="https://famelos.com/jev/auto-classifier-certification">write-up</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/joasasantos/neurosploit/blob/main/neurosploit-rs/crates/harness/src/typesafe.rs"><img src="https://opengraph.githubassets.com/1/joasasantos/neurosploit" alt="NeuroSploit TypeSafe adjudication" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/joasasantos/neurosploit/blob/main/neurosploit-rs/crates/harness/src/typesafe.rs">NeuroSploit TypeSafe adjudication</a></b><br><sub>joasasantos · GitHub · ⭐ 1.4k repo · 2025-08-17</sub><br>NeuroSploit, a Rust pentest harness, uses Jev as a calibrated confirmation and adjudication layer, judging each finding confirmed, needs-review or rejected and scoring severity.<br><sub><b>How it uses Jev:</b> Choice, Score and Noul over a finding's evidence; enabled with --typesafe on|off|auto.</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/berylliumsec/nebula/blob/main/src/nebula/v3/tool_suggestions.py"><img src="https://raw.githubusercontent.com/berylliumsec/nebula/main/docs/images/nebula-3-workbench.png" alt="Nebula Jev tool suggestions" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/berylliumsec/nebula/blob/main/src/nebula/v3/tool_suggestions.py">Nebula Jev tool suggestions</a></b><br><sub>berylliumsec · GitHub · ⭐ 1.1k repo · 2023-09-30</sub><br>Nebula, an AI pentesting assistant, can have Jev rank its deferred tool catalog and connected MCP sources against the operator's recent messages before a turn starts.<br><sub><b>How it uses Jev:</b> One call ranks sources and tools; every Choice carries a none-of-these option, and the result only hints and preloads schemas, never acts.</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/NorbertBodziony/guard-jev"><img src="https://pbs.twimg.com/amplify_video_thumb/2100543653567422464/img/oiqDpgU9rAYHECKO.jpg" alt="Moderation Guard" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/NorbertBodziony/guard-jev">Moderation Guard</a></b><br><sub>NorbertBodziony · GitHub · ⭐ 1 · 2026-09-17</sub><br>Comment-moderation demo where one System One call screens seven Noul hazards plus a severity Score in parallel, and code computes the verdict from strict or permissive policy thresholds.<br><sub>Also: <a href="https://guard-jev.vercel.app">app</a> · <a href="https://guard-jev.vercel.app">app 2</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/brainstormity/Jev-Moderation-Bot"><img src="https://opengraph.githubassets.com/1/brainstormity/Jev-Moderation-Bot" alt="Jev Moderation Bot" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/brainstormity/Jev-Moderation-Bot">Jev Moderation Bot</a></b><br><sub>brainstormity · GitHub · ⭐ 41 · 2026-09-17</sub><br>Discord bot that deletes spam and scam links in real time with escalating warnings and timeouts, and profiles members from their recent messages for scam risk, toxicity and helpfulness.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/ahmedgagan11/status/2100955502075388250"><img src="https://pbs.twimg.com/amplify_video_thumb/2100850340363182080/img/rHnwL-1zhzgLUMU8.jpg" alt="Sentence-level AI text detector" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/ahmedgagan11/status/2100955502075388250">Sentence-level AI text detector</a></b><br><sub>ahmedgagan11 · X · ♥ 27 · 2026-09-18</sub><br>AI text detector that scans a full article and gives a sentence-by-sentence breakdown of what looks machine-written, in near real time.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/mariojankovic/status/2100934084503519325"><img src="https://pbs.twimg.com/amplify_video_thumb/2100933806148456448/img/5CfeEOTK0oYGPEqo.jpg" alt="YouTube AI-slop filter" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/mariojankovic/status/2100934084503519325">YouTube AI-slop filter</a></b><br><sub>mariojankovic · X · ♥ 3 · 2026-09-18</sub><br>Bring-your-own-key Chrome extension that filters AI slop out of YouTube as you scroll and caches the results.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/open-leash/leash"><img src="https://capsule-render.vercel.app/api?type=waving&amp;color=0:6366F1,45:14B8A6,100:111827&amp;height=230&amp;section=header&amp;text=Leash&amp;fontSize=68&amp;fontColor=ffffff&amp;fontAlignY=38&amp;desc=Control%20your%20AI.&amp;descSize=22&amp;descAlignY=59" alt="Leash" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/open-leash/leash">Leash</a></b><br><sub>open-leash · GitHub · ⭐ 24 · 2026-06-02</sub><br>Open-source safety and control layer between personal AI agents and their actions that stops destructive commands, secret exposure, prompt injection and unsafe tools, using Jev-backed decisions with your own TypeSafe key.<br><sub>Also: <a href="https://openleash.com">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/luantak/is-malicious"><img src="https://github.com/user-attachments/assets/611c979a-8dd4-4fc8-8963-0843314e6a55" alt="is-malicious?" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/luantak/is-malicious">is-malicious?</a></b><br><sub>luantak · GitHub · ⭐ 22 · 2026-09-18</sub><br>CLI that sends source, config, build and CI files to Jev to flag hidden, deceptive or data-stealing behavior, reporting suspicious files and line ranges with a probability and reason before you run unfamiliar code.<br><sub>Also: <a href="https://news.ycombinator.com/item?id=49756921">discussion</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/leepokai/jev-guard"><img src="https://raw.githubusercontent.com/leepokai/jev-guard/main/assets/works-with.svg" alt="jev-guard" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/leepokai/jev-guard">jev-guard</a></b><br><sub>leepokai · GitHub · ⭐ 21 · 2026-09-17</sub><br>Security hook for Claude Code, Codex, Copilot, Gemini, Cursor, pi, OpenCode and ACP editors that risk-scores every tool call with session context, flags prompt injection in results, and checks skills and plugins.<br><sub><b>How it uses Jev:</b> Three typed questions per tool call (risk, user_requested, from_untrusted) mapped to deny, ask or allow in code.</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/zszz3/Pi-Jev-Guide"><img src="https://opengraph.githubassets.com/1/zszz3/Pi-Jev-Guide" alt="Pi Jev Guard" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/zszz3/Pi-Jev-Guide">Pi Jev Guard</a></b><br><sub>zszz3 · GitHub · ⭐ 20 · 2026-09-19</sub><br>Pi coding-agent plugin with rules you add by timing, local match or Jev judgment, and action, where Jev checks tool calls for destructiveness, data exfiltration, task drift, and rule conflicts.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/zhuyansen/agent-skills-hub/tree/main/ops/jev-review"><img src="https://opengraph.githubassets.com/1/zhuyansen/agent-skills-hub" alt="AgentSkillsHub Jev scanner review" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/zhuyansen/agent-skills-hub/tree/main/ops/jev-review">AgentSkillsHub Jev scanner review</a></b><br><sub>zhuyansen · GitHub · ⭐ 373 repo · 2026-03-06</sub><br>Evaluation of Jev as a second pass for a regex security scanner over about 27.7K READMEs, asking whether a flagged line issues a behaviour or only cites it.<br><sub><b>How it uses Jev:</b> Four atomic Noul questions (issues_it, is_documentation, is_negated, word_coincidence); negated reached AUC 0.904 inverted.</sub><br><sub>Also: <a href="https://agentskillshub.top">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/mohamadkhoshnava/ZeroNSFWBot"><img src="https://opengraph.githubassets.com/1/mohamadkhoshnava/ZeroNSFWBot" alt="ZeroNSFWBot" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/mohamadkhoshnava/ZeroNSFWBot">ZeroNSFWBot</a></b><br><sub>mohamadkhoshnava · GitHub · ⭐ 13 · 2026-08-07</sub><br>Async Rust Telegram moderation bot that bans NSFW advertisers; images are judged locally, while Jev powers optional bio, topic, ad-guard and language checks on text.<br><sub><b>How it uses Jev:</b> Several subjects are asked as typed questions in one call; an outage is reported as unavailable rather than clean, with a regex word list as a floor.</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/AlexGrinman/status/2100587625304281141"><img src="https://pbs.twimg.com/amplify_video_thumb/2100586275132563456/img/NMT7xdMBo97RWoMc.jpg" alt="Human-or-AI writing detector" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/AlexGrinman/status/2100587625304281141">Human-or-AI writing detector</a></b><br><sub>AlexGrinman · X · ♥ 5 · 2026-09-17</sub><br>Lightweight detector that uses Jev to judge whether a piece of writing came from a human or an AI, fast enough to run with no visible delay.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Divkix/Alita_Robot/blob/main/alita/modules/aispam_jev.go"><img src="https://opengraph.githubassets.com/1/Divkix/Alita_Robot" alt="Alita AI spam filter" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Divkix/Alita_Robot/blob/main/alita/modules/aispam_jev.go">Alita AI spam filter</a></b><br><sub>Divkix · GitHub · ⭐ 248 repo · 2020-10-26</sub><br>Per-chat AI spam filter for a Go Telegram group-management bot, judging each message with Jev off the update path with code-owned questions and one bounded retry.<br><sub>Also: <a href="https://alita-docs.divkix.me">docs</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/bugkiwi/elons-job"><img src="https://raw.githubusercontent.com/bugkiwi/elons-job/main/docs/screenshots/comment-filtering.png" alt="elons-job" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/bugkiwi/elons-job">elons-job</a></b><br><sub>bugkiwi · GitHub · ⭐ 11 · 2026-09-18</sub><br>Local-first Chrome extension that hides high-confidence sexual and solicitation replies on X post pages behind reversible placeholders, with customizable rules, caching, and cost limits.<br><sub><b>How it uses Jev:</b> Noul questions over each reply's text; fails open on timeouts, errors, or unexpected responses.</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/win4r/jev-security-scan"><img src="https://opengraph.githubassets.com/1/win4r/jev-security-scan" alt="Jev Security Scan" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/win4r/jev-security-scan">Jev Security Scan</a></b><br><sub>win4r · GitHub · ⭐ 10 · 2026-09-19</sub><br>Standard-library Python scanner that reviews Agent Skills, MCP configs, and MCP source for prompt injection, tool poisoning, credential access, and exfiltration before install, with file and line evidence.<br><sub><b>How it uses Jev:</b> Redacted snippets go to Jev for risk probabilities alongside local static checks; a fully offline mode is also available.</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/MauroPello/stop-the-slop"><img src="https://opengraph.githubassets.com/1/MauroPello/stop-the-slop" alt="Stop the Slop" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/MauroPello/stop-the-slop">Stop the Slop</a></b><br><sub>MauroPello · GitHub · ⭐ 10 · 2026-08-21</sub><br>Chrome and Firefox extension that flags AI-generated YouTube scripts with thumbnail badges and sentence heatmaps, scored by a Cloudflare Worker that calls Jev with Gemini or Sapling as fallback.<br><sub>Also: <a href="https://mauropello.github.io/stop-the-slop/">app</a> · <a href="https://github.com/MauroPello/stop-the-slop/blob/main/worker/src/index.js">code</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/qs-lll/twitter-jev-guard"><img src="https://raw.githubusercontent.com/qs-lll/twitter-jev-guard/main/assets/settings-popup.png" alt="Twitter Jev Guard" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/qs-lll/twitter-jev-guard">Twitter Jev Guard</a></b><br><sub>qs-lll · GitHub · ⭐ 10 · 2026-09-21</sub><br>Chrome and Edge extension that uses Jev to flag low-quality, spam and promotional posts on the X timeline, overlaying a translucent STOP or AD watermark with the probability on the post text.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/smontlouis/bible-strong/blob/master/apps/world/server/guestbook-moderation.ts"><img src="https://opengraph.githubassets.com/1/smontlouis/bible-strong" alt="Bible Strong guestbook moderation" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/smontlouis/bible-strong/blob/master/apps/world/server/guestbook-moderation.ts">Bible Strong guestbook moderation</a></b><br><sub>smontlouis · GitHub · ⭐ 165 repo · 2019-01-12</sub><br>Bible study app whose public, all-ages event guestbook is moderated by Jev, screening names and messages in any language for abuse while allowing criticism and testimony.<br><sub>Also: <a href="https://bible-strong.app">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/harshwasan/jev-sentinel"><img src="https://raw.githubusercontent.com/harshwasan/jev-sentinel/main/docs/images/injection-caught-twice.png" alt="jev-sentinel" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/harshwasan/jev-sentinel">jev-sentinel</a></b><br><sub>harshwasan · GitHub · ⭐ 8 · 2026-09-19</sub><br>Guard for coding agents, shipped as a Pi extension and a Claude Code and Codex CLI plugin, that checks tool calls, tool outputs, and replies for prompt injection, risky approvals, leaked secrets, and task drift.<br><sub><b>How it uses Jev:</b> Typed checks with probabilities that plain code turns into allow, ask, or warn.</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/jesset/pi-verdict"><img src="https://raw.githubusercontent.com/jesset/pi-verdict/main/docs/demo.gif" alt="pi-verdict" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/jesset/pi-verdict">pi-verdict</a></b><br><sub>jesset · GitHub · ⭐ 8 · 2026-08-25</sub><br>Permission gate for the Pi coding agent in the style of Claude Code's auto mode: deterministic rules settle clear cases, and gray-zone tool calls go to a fail-closed classifier that can be Jev.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/isNickMa/status/2100566407524344225"><img src="https://pbs.twimg.com/media/HSa1-rFbkAATKpc.jpg?name=orig" alt="Jev agent safety monitor" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/isNickMa/status/2100566407524344225">Jev agent safety monitor</a></b><br><sub>isNickMa · X · ♥ 1 · 2026-09-17</sub><br>Test of Jev as a monitor that checks each AI agent action before it runs, reported to catch most attacks with almost no false blocks and much faster than Gemini.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/backmeupplz/jev_antispam_bot"><img src="https://opengraph.githubassets.com/1/backmeupplz/jev_antispam_bot" alt="Jev Anti-Spam Bot" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/backmeupplz/jev_antispam_bot">Jev Anti-Spam Bot</a></b><br><sub>backmeupplz · GitHub · ⭐ 7 · 2026-09-18</sub><br>Self-hosted grammY Telegram bot that asks Jev whether each group message is spam, such as token shilling, DM funnels or phishing, and deletes only high-confidence matches.<br><sub><b>How it uses Jev:</b> A spam Noul per message with a high deletion threshold; errors fail open and admins are exempt.</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Nyarlathoteppppp/pi-heed"><img src="https://repository-images.githubusercontent.com/1375891003/00d886b8-21f8-4b13-9c04-d3aa6b525aa6" alt="pi-heed" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Nyarlathoteppppp/pi-heed">pi-heed</a></b><br><sub>Nyarlathoteppppp · GitHub · ⭐ 7 · 2026-09-18</sub><br>Pi coding-agent extension that turns constraints you state in conversation, in English or Chinese, into a scoped policy and checks every side-effecting tool call against it with Jev before it runs.<br><sub>Also: <a href="https://www.reddit.com/r/PiCodingAgent/comments/1wjrvf3/i_built_piheed_runtime_constraints_for_pi/">discussion</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/TylerMaran/status/2102107759483453733"><img src="https://pbs.twimg.com/amplify_video_thumb/2102106516732116992/img/Dzd67cJx51EtGSmD.jpg" alt="Browser agent flagger" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/TylerMaran/status/2102107759483453733">Browser agent flagger</a></b><br><sub>TylerMaran · X · ♥ 5 · 2026-09-21</sub><br>Live detector that runs Jev over a site's activity logs every 3 seconds and builds an average score to flag sessions driven by browser agents, costing under $0.01 per session.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/wanaku-ai/wanaku/blob/main/features/evaluator/src/engines/system_one.rs"><img src="https://raw.githubusercontent.com/wanaku-ai/wanaku/main/docs/imgs/wanaku-dashboard.png" alt="Wanaku System One evaluator" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/wanaku-ai/wanaku/blob/main/features/evaluator/src/engines/system_one.rs">Wanaku System One evaluator</a></b><br><sub>wanaku-ai · GitHub · ⭐ 134 repo · 2025-02-01</sub><br>Governed action proxy for AI agents that adds a TypeSafe System One evaluator engine, judging intercepted MCP tool calls and conversation history with Noul questions.<br><sub>Also: <a href="https://wanaku.ai">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/LeslieLeung/Aletheia"><img src="https://opengraph.githubassets.com/1/LeslieLeung/Aletheia" alt="Aletheia" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/LeslieLeung/Aletheia">Aletheia</a></b><br><sub>LeslieLeung · GitHub · ⭐ 6 · 2026-02-26</sub><br>FastAPI service and Chrome extension that detects AI-generated text on article pages with several engines including Jev, which can also classify a page as original, repost or advertisement.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Dino-Kupinic/blackrose"><img src="https://opengraph.githubassets.com/1/Dino-Kupinic/blackrose" alt="Blackrose" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Dino-Kupinic/blackrose">Blackrose</a></b><br><sub>Dino-Kupinic · GitHub · ⭐ 6 · 2024-05-22</sub><br>Python and JavaScript decision layer for LLM apps that runs one Jev call on model input or output for jailbreak, harm severity and other checks, and returns allow, review or block with reasons and raw scores.<br><sub><b>How it uses Jev:</b> Noul for jailbreak/injection and a Score for harm severity in one parallel system_one call; low confidence defaults to review.</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/AliZakaee/Spam-Detector-Telegram-Bot"><img src="https://opengraph.githubassets.com/1/AliZakaee/Spam-Detector-Telegram-Bot" alt="Spam Detector Telegram Bot" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/AliZakaee/Spam-Detector-Telegram-Bot">Spam Detector Telegram Bot</a></b><br><sub>AliZakaee · GitHub · ⭐ 6 · 2025-09-26</sub><br>Telegram group bot that flags spam for admin review, using Jev's spam choice, hazard probabilities and severity with no training, a local TF-IDF SVM for Persian slang, or both in hybrid mode.<br><sub><b>How it uses Jev:</b> Choice and Score answers below a confidence floor are ignored, while independent Noul hazards can still flag; outages fall back to the SVM.</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/cnsunyour/tg-guard-bot"><img src="https://raw.githubusercontent.com/cnsunyour/tg-guard-bot/main/docs/images/architecture.svg" alt="Telegram Guard Bot" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/cnsunyour/tg-guard-bot">Telegram Guard Bot</a></b><br><sub>cnsunyour · GitHub · ⭐ 5 · 2026-01-03</sub><br>Chinese Telegram group-management bot with join verification and layered anti-spam, whose AI context check can use Jev as the primary text classifier with an LLM as backup; on 31 local samples it matched DeepSeek at 0.8.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/eijiaraki/toxic-filter"><img src="https://raw.githubusercontent.com/eijiaraki/toxic-filter/main/docs/assets/demo.gif" alt="toXic Filter" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/eijiaraki/toxic-filter">toXic Filter</a></b><br><sub>eijiaraki · GitHub · ⭐ 5 · 2026-09-21</sub><br>Chrome extension that classifies posts on X with Jev and hides the ones matching categories you choose, such as discrimination, taunting, hate or cynicism, behind a revealable overlay.<br><sub><b>How it uses Jev:</b> Six selectable categories with adjustable thresholds; only post text near the screen is sent, directly to api.typesafe.ai.</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/aurorascharff/next16-social-media/blob/main/lib/moderation.ts"><img src="https://opengraph.githubassets.com/1/aurorascharff/next16-social-media" alt="Next 16 social media Jev moderation" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/aurorascharff/next16-social-media/blob/main/lib/moderation.ts">Next 16 social media Jev moderation</a></b><br><sub>aurorascharff · GitHub · ⭐ 81 repo · 2026-05-18</sub><br>Next.js 16 social network demo that moderates user posts and blocks profanity with Jev through AI SDK evaluate on Vercel AI Gateway, with a 3-second timeout.<br><sub>Also: <a href="https://next16-social-media.vercel.app">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/carlosedm10/agi-jev-containment"><img src="https://opengraph.githubassets.com/1/carlosedm10/agi-jev-containment" alt="AGI Jev Detection" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/carlosedm10/agi-jev-containment">AGI Jev Detection</a></b><br><sub>carlosedm10 · GitHub · ⭐ 4 · 2026-09-14</sub><br>Local monitor for sandboxed LLM agents that classifies chains of actions with Jev and a Sentinel model, escalates through L1-L5 containment and keeps Neo4j forensics behind a dashboard; built at HackSpain 2026.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/JKHeadley/instar/blob/main/src/core/JevSignalShadow.ts"><img src="https://repository-images.githubusercontent.com/1161391430/7fa9f2fd-6f99-41ee-a124-291268c199e0" alt="Instar Jev signal shadow" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/JKHeadley/instar/blob/main/src/core/JevSignalShadow.ts">Instar Jev signal shadow</a></b><br><sub>JKHeadley · GitHub · ⭐ 80 repo · 2026-02-19</sub><br>Persistent Claude Code agent framework that shadows its outbound message gate with Jev, logging agreement with pattern detectors for file paths, commands and config keys without affecting decisions.<br><sub>Also: <a href="https://github.com/JKHeadley/instar/blob/main/docs/specs/jev-signal-layer-shadow.md">spec</a> · <a href="https://instar.sh">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/caiovicentino/jev-align"><img src="https://opengraph.githubassets.com/1/caiovicentino/jev-align" alt="jev-align" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/caiovicentino/jev-align">jev-align</a></b><br><sub>caiovicentino · GitHub · ⭐ 4 · 2026-09-18</sub><br>Verifier that checks LLM responses and agent plans for sycophancy, deception, overreach and dark patterns in one Jev call of about 800ms, returning block decisions with auditable probabilities.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/andrelandgraf/safer-with-jev"><img src="https://opengraph.githubassets.com/1/andrelandgraf/safer-with-jev" alt="Safer with Jev" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/andrelandgraf/safer-with-jev">Safer with Jev</a></b><br><sub>andrelandgraf · GitHub · ⭐ 4 · 2026-09-17</sub><br>HTTP inspection gateway on a Neon Function that has Jev judge a request body for prompt injection or unsafe content, then passes, reviews or blocks it and can forward the same bytes to a caller-chosen HTTPS URL.<br><sub>Also: <a href="https://safer-with-jev.com">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Thanh-Mathieu95/jev-model-tokengate"><img src="https://raw.githubusercontent.com/Thanh-Mathieu95/jev-model-tokengate/main/docs/race.png" alt="tokengate" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Thanh-Mathieu95/jev-model-tokengate">tokengate</a></b><br><sub>Thanh-Mathieu95 · GitHub · ⭐ 4 · 2026-09-20</sub><br>OpenAI-compatible proxy that checks each sliding window of tokens while an LLM response streams and cuts the stream before a violating token reaches the screen; its demo leaks 0 characters versus 173 post-hoc.<br><sub><b>How it uses Jev:</b> Judges each buffered token window for violations such as leaked secrets during streaming.</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/aurorascharff/next16-calendar/blob/main/lib/moderation.ts"><img src="https://opengraph.githubassets.com/1/aurorascharff/next16-calendar" alt="Next 16 calendar Jev moderation" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/aurorascharff/next16-calendar/blob/main/lib/moderation.ts">Next 16 calendar Jev moderation</a></b><br><sub>aurorascharff · GitHub · ⭐ 78 repo · 2026-08-08</sub><br>Next.js 16 calendar and booking demo that moderates user-entered calendar text with Jev through AI SDK evaluate on Vercel AI Gateway.<br><sub>Also: <a href="https://next16-calendar.vercel.app">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/CaptainCore/captaincore/blob/master/cmd/typesafe.go"><img src="https://opengraph.githubassets.com/1/CaptainCore/captaincore" alt="CaptainCore malware triage" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/CaptainCore/captaincore/blob/master/cmd/typesafe.go">CaptainCore malware triage</a></b><br><sub>CaptainCore · GitHub · ⭐ 71 repo · 2026-09-19</sub><br>Jev commands in the CaptainCore WordPress maintenance CLI that rank native malware-scanner findings by how likely each is real, naming the likely family and next step for an operator.<br><sub><b>How it uses Jev:</b> Each finding is sent with its rule, matched text, file location and surrounding source; triage orders and annotates but never drops a finding.</sub><br><sub>Also: <a href="https://github.com/CaptainCore/captaincore">repo</a> · <a href="https://captaincore.io">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/ClemensSchartmueller/jev-guard"><img src="https://opengraph.githubassets.com/1/ClemensSchartmueller/jev-guard" alt="jev-guard (ClemensSchartmueller)" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/ClemensSchartmueller/jev-guard">jev-guard (ClemensSchartmueller)</a></b><br><sub>ClemensSchartmueller · GitHub · ⭐ 3 · 2026-09-18</sub><br>Go safety gate for Claude Code, Codex CLI, and Antigravity that intercepts shell, write, patch, and read tool calls, runs local boundary checks, then asks Jev about blast radius, reversibility, and destructiveness.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/caiovicentino/jev-shield"><img src="https://opengraph.githubassets.com/1/caiovicentino/jev-shield" alt="jev-shield" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/caiovicentino/jev-shield">jev-shield</a></b><br><sub>caiovicentino · GitHub · ⭐ 3 · 2026-09-17</sub><br>Semantic MCP firewall between any stdio MCP client and server that screens every tool call, result, and description, reporting 94% block recall with 0 false positives at about $0.00002 per check.<br><sub><b>How it uses Jev:</b> Calibrated System One verification layered on deterministic structural checks.</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/CodeAlive-AI/mastra-jev-moderation"><img src="https://opengraph.githubassets.com/1/CodeAlive-AI/mastra-jev-moderation" alt="mastra-jev-moderation" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/CodeAlive-AI/mastra-jev-moderation">mastra-jev-moderation</a></b><br><sub>CodeAlive-AI · GitHub · ⭐ 3 · 2026-09-18</sub><br>Single-file input moderation processor for Mastra agents that blocks hostile messages with one Jev request per turn, failing open behind a deadline and circuit breaker.<br><sub><b>How it uses Jev:</b> A block/allow Noul plus a category Choice in one request; the turn aborts above 0.7.</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/alexj11324/open-jev-approvals"><img src="https://opengraph.githubassets.com/1/alexj11324/open-jev-approvals" alt="open-jev-approvals" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/alexj11324/open-jev-approvals">open-jev-approvals</a></b><br><sub>alexj11324 · GitHub · ⭐ 3 · 2026-09-20</sub><br>Go approval gate for Claude Code and Codex hooks: Jev reviews each intercepted tool call and a versioned local policy returns allow or deny, with a deny requiring positive evidence of danger.<br><sub><b>How it uses Jev:</b> Reviews each tool call against the recorded user prompt as authorization evidence; fails open if no verdict.</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/24601/rh-guard"><img src="https://raw.githubusercontent.com/24601/rh-guard/main/docs/sessions/rh_guard_side_by_side.gif" alt="rh-guard" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/24601/rh-guard">rh-guard</a></b><br><sub>24601 · GitHub · ⭐ 3 · 2026-09-17</sub><br>Coding-agent hook for Claude Code, Cursor, Codex, Pi and others that blocks reward hacking such as tampering with graders or hidden tests, combining structural denies with a Jev risk sidecar.<br><sub>Also: <a href="https://24601.github.io/rh-guard/">site</a> · <a href="https://24601.github.io/rh-guard">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/adamnroman/slop-filter"><img src="https://raw.githubusercontent.com/adamnroman/slop-filter/main/assets/icons/icon-128.png" alt="slop-filter" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/adamnroman/slop-filter">slop-filter</a></b><br><sub>adamnroman · GitHub · ⭐ 3 · 2026-09-20</sub><br>Chrome extension that scores every post and comment on X, LinkedIn, Reddit and YouTube for how likely it is AI-written and folds away those over your threshold, with weights you can fit from your own labels.<br><sub>Also: <a href="https://news.ycombinator.com/item?id=49776507">demo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/elliothux/tweet-911"><img src="https://raw.githubusercontent.com/elliothux/tweet-911/main/docs/preview-overlay.jpg" alt="Tweet 911" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/elliothux/tweet-911">Tweet 911</a></b><br><sub>elliothux · GitHub · ⭐ 3 · 2026-09-20</sub><br>Chrome extension and Cloudflare Workers API that score X posts and replies in real time for AI writing, porn solicitation and paraphrase bots, using the author profile, post text and parent tweet.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/vicnaum/vics-agent-skills/tree/main/skills/slopcheck"><img src="https://opengraph.githubassets.com/1/vicnaum/vics-agent-skills" alt="slopcheck" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/vicnaum/vics-agent-skills/tree/main/skills/slopcheck">slopcheck</a></b><br><sub>vicnaum · GitHub · ⭐ 52 repo · 2026-01-18</sub><br>Agent skill that checks an agent's prose for slop patterns and gates publishing, with an optional model layer via the Anthropic or TypeSafe Jev API for inflation, jargon, bare numbers and metaphors.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/WYRE-AI/msp-claude-plugins/tree/main/packages/mcp-jev-guardrails"><img src="https://opengraph.githubassets.com/1/WYRE-AI/msp-claude-plugins" alt="mcp-jev-guardrails" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/WYRE-AI/msp-claude-plugins/tree/main/packages/mcp-jev-guardrails">mcp-jev-guardrails</a></b><br><sub>WYRE-AI · GitHub · ⭐ 46 repo · 2026-02-04</sub><br>Library for MSP MCP servers that screens tool calls against role allowlists, deny policies and user intent using atomic Jev Nouls, then lets code compose an allow/review/block decision.<br><sub><b>How it uses Jev:</b> Atomic Noul questions per tool call following the TypeSafe guardrails cookbook; decide() applies fixed thresholds.</sub><br><sub>Also: <a href="https://github.com/WYRE-AI/msp-claude-plugins">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/omkarghugarkar007/actiongate-jev"><img src="https://raw.githubusercontent.com/omkarghugarkar007/actiongate-jev/main/docs/assets/actiongate-social.svg" alt="ActionGate" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/omkarghugarkar007/actiongate-jev">ActionGate</a></b><br><sub>omkarghugarkar007 · GitHub · ⭐ 2 · 2026-09-19</sub><br>Runtime authorization gateway for agent tool calls that combines deterministic policy with Jev, binds approval to the exact action, and refuses expired, changed, or replayed permits over MCP and HTTP.<br><sub><b>How it uses Jev:</b> Judges whether a well-formed tool call actually matches what the user asked for.</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/agent-chaperone/agent-chaperone"><img src="https://agentchaperone.dev/og.png" alt="agent-chaperone" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/agent-chaperone/agent-chaperone">agent-chaperone</a></b><br><sub>agent-chaperone · GitHub · ⭐ 2 · 2026-09-18</sub><br>Firewall that screens an AI agent's tool calls before they run and tool results before the agent reads them, via an MCP proxy and a hooks adapter, with thresholds in a policy file and a non-blocking shadow mode.<br><sub>Also: <a href="https://agentchaperone.dev">site</a> · <a href="https://agentchaperone.dev">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/ItisShikhar/gg-friggin-ez"><img src="https://raw.githubusercontent.com/ItisShikhar/gg-friggin-ez/master/docs/images/banner.png" alt="gg-friggin-ez" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/ItisShikhar/gg-friggin-ez">gg-friggin-ez</a></b><br><sub>ItisShikhar · GitHub · ⭐ 2 · 2026-09-19</sub><br>Profanity and toxicity screener for Node.js that catches leetspeak, spaced-out letters and romanized profanity in languages such as Hindi, Tamil, Telugu, Kannada and Bengali in about 50-500ms.<br><sub>Also: <a href="https://itisshikhar.github.io/gg-friggin-ez/">app</a> · <a href="https://itisshikhar.github.io/gg-friggin-ez">app 2</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/undeemed/Jcyber"><img src="https://opengraph.githubassets.com/1/undeemed/Jcyber" alt="Jcyber" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/undeemed/Jcyber">Jcyber</a></b><br><sub>undeemed · GitHub · ⭐ 2 · 2026-09-19</sub><br>MCP toolkit for agent-driven bug bounty work with scope gates, an evidence graph and memory, using Jev to score finding severity and check for duplicates.<br><sub><b>How it uses Jev:</b> A none-to-critical Score plus a duplicate Noul; measured at 0.24s and 0.17s average versus 1.46s and 2.08s for the agent.</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/jev-ids/jev-ids"><img src="https://raw.githubusercontent.com/jev-ids/jev-ids/main/docs/banner.svg" alt="Jev IDS" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/jev-ids/jev-ids">Jev IDS</a></b><br><sub>jev-ids · GitHub · ⭐ 2 · 2026-09-21</sub><br>Network intrusion detection prototype that shows Jev one NSL-KDD flow plus five labeled examples and asks whether it is an attack and which kind, reported 4.8x faster and 3.8x cheaper than an LLM baseline.<br><sub><b>How it uses Jev:</b> One Noul (attack or not) and a five-way Choice (category) per flow; Python applies a 0.5 cut.</sub><br><sub>Also: <a href="https://jev-ids.github.io">app</a> · <a href="https://jev-ids.github.io/">app 2</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/santos-sanz/jev-audio-beeper"><img src="https://opengraph.githubassets.com/1/santos-sanz/jev-audio-beeper" alt="jev-audio-beeper" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/santos-sanz/jev-audio-beeper">jev-audio-beeper</a></b><br><sub>santos-sanz · GitHub · ⭐ 2 · 2026-09-17</sub><br>Proof of concept that finds Spanish profanity in word-timestamped audio with Jev and beeps over the matching intervals with ffmpeg without changing the audio duration.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/newuser7171/antivirus"><img src="https://opengraph.githubassets.com/1/newuser7171/antivirus" alt="Jev-AV" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/newuser7171/antivirus">Jev-AV</a></b><br><sub>newuser7171 · GitHub · ⭐ 2 · 2026-09-18</sub><br>Desktop antivirus and threat-triage scanner that extracts features such as entropy, PE imports, macros, and process lineage from files, processes, and URLs, then applies quarantine or review rules.<br><sub><b>How it uses Jev:</b> Choice for the verdict, a 0-4 severity Score, and Noul indicators per scanned item.</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Red5d/jev-cvss"><img src="https://opengraph.githubassets.com/1/Red5d/jev-cvss" alt="jev-cvss" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Red5d/jev-cvss">jev-cvss</a></b><br><sub>Red5d · GitHub · ⭐ 2 · 2026-09-18</sub><br>Python scripts that score vulnerability descriptions with CVSS v3.0, v3.1 or v4.0: Jev selects each metric value and the numeric scores are computed in code per the FIRST specifications.<br><sub><b>How it uses Jev:</b> One request per description with one Choice per metric (plus Nouls for v4.0 safety); prints the top-2 spread for close calls.</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/kiwi0719/jev-edge"><img src="https://raw.githubusercontent.com/kiwi0719/jev-edge/main/docs/hero.webp" alt="jev-edge" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/kiwi0719/jev-edge">jev-edge</a></b><br><sub>kiwi0719 · GitHub · ⭐ 2 · 2026-09-21</sub><br>Admission control for LLM-backed services at the gateway, with a three-layer prompt-injection and abuse filter for nginx, OpenResty, Envoy, Cloudflare Workers, and other proxies; fail-open and cached.<br><sub><b>How it uses Jev:</b> Asks what each incoming request is trying to do to the service before it reaches the backend.</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/AkashPriyadarshii/jev-git"><img src="https://opengraph.githubassets.com/1/AkashPriyadarshii/jev-git" alt="jev-git" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/AkashPriyadarshii/jev-git">jev-git</a></b><br><sub>AkashPriyadarshii · GitHub · ⭐ 2 · 2026-09-18</sub><br>Rust Git pre-commit and pre-push hook, run as git jev, that has Jev screen staged diffs for unredacted secrets, prompt-injection text and destructive commands in about 80 ms p50.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/coo-quack/jev-pii-checker"><img src="https://opengraph.githubassets.com/1/coo-quack/jev-pii-checker" alt="jev-pii-checker" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/coo-quack/jev-pii-checker">jev-pii-checker</a></b><br><sub>coo-quack · GitHub · ⭐ 2 · 2026-09-19</sub><br>CLI that scans text and files for PII in three layers: Jev gates on 13 PII categories and sensitivity, then regex and word segmentation locate the spans.<br><sub><b>How it uses Jev:</b> Per-chunk PII-category Nouls plus a sensitivity Score.</sub><br><sub>Also: <a href="https://coo-quack.github.io/jev-pii-checker/">docs</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/lgy1027/jevshield"><img src="https://raw.githubusercontent.com/lgy1027/jevshield/main/docs/architecture.svg" alt="JevShield" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/lgy1027/jevshield">JevShield</a></b><br><sub>lgy1027 · GitHub · ⭐ 2 · 2026-09-20</sub><br>LangChain-ready security gate for agent tool calls that blocks only when a severity Choice and an irreversibility Noul agree, with calibrated-confidence routing, fail-closed parsing, and a local fallback.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/TKY-27/JevSlop"><img src="https://opengraph.githubassets.com/1/TKY-27/JevSlop" alt="JevSlop" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/TKY-27/JevSlop">JevSlop</a></b><br><sub>TKY-27 · GitHub · ⭐ 2 · 2026-09-18</sub><br>Site that fetches a public note.com article and asks Jev in one request for an overall judgment plus eight writing-quality Score axes, turning them into a transparent 0-100 AI Slop Score; not an authorship detector.<br><sub>Also: <a href="https://jevslop.pages.dev/">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/revsmoke/promptrejectormcp"><img src="https://opengraph.githubassets.com/1/revsmoke/promptrejectormcp" alt="Prompt Rejector" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/revsmoke/promptrejectormcp">Prompt Rejector</a></b><br><sub>revsmoke · GitHub · ⭐ 2 · 2026-01-27</sub><br>MCP and HTTPS scanner that screens prompts, skill files and MCP tool descriptions for injected instructions before an agent acts on them, combining deterministic checks, Jev judgments and a reasoning model.<br><sub>Also: <a href="https://github.com/revsmoke/promptrejectormcp/blob/main/docs/how-we-use-jev-from-typesafe-ai.md">docs</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/RiskAverseTech/toolgate"><img src="https://opengraph.githubassets.com/1/RiskAverseTech/toolgate" alt="toolgate" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/RiskAverseTech/toolgate">toolgate</a></b><br><sub>RiskAverseTech · GitHub · ⭐ 2 · 2026-09-18</sub><br>Tool-call firewall that runs as a Claude Code PreToolUse hook or an MCP proxy and asks Jev seven questions, such as destructive, exfiltration or off-task, before risky actions, with YAML policy and a local audit log.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/noelzappy/tripwire"><img src="https://opengraph.githubassets.com/1/noelzappy/tripwire" alt="tripwire" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/noelzappy/tripwire">tripwire</a></b><br><sub>noelzappy · GitHub · ⭐ 2 · 2026-09-18</sub><br>AI SDK middleware and OpenAI-compatible proxy that runs seven Jev checks on every LLM response in one ~100 ms call, with YAML policies, confidence-gated block or flag actions, and an eval CLI.<br><sub>Also: <a href="https://www.npmjs.com/package/@noelzappy/tripwire">npm</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/jboolean/1940s.nyc/tree/master/backend/moderation-experiment"><img src="https://opengraph.githubassets.com/1/jboolean/1940s.nyc" alt="1940s.nyc story moderation experiment" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/jboolean/1940s.nyc/tree/master/backend/moderation-experiment">1940s.nyc story moderation experiment</a></b><br><sub>jboolean · GitHub · ⭐ 35 repo · 2019-09-24</sub><br>Local experiment for the 1940s.nyc street-view site that predicts whether a human moderator would approve a user story, asking Jev one yes/no question per moderation rule and measuring agreement with real past decisions.<br><sub><b>How it uses Jev:</b> Per-rule Nouls via OpenRouter's Decisions API, combined against a reject threshold in rules.ts; an LLM backend is the comparison.</sub><br><sub>Also: <a href="https://github.com/jboolean/1940s.nyc">repo</a> · <a href="http://1940s.nyc">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/seuros/chaos/tree/master/sys/kern/reflex"><img src="https://repository-images.githubusercontent.com/1123724299/738c9e8f-7fff-4962-af4c-f4753d0faf04" alt="FreeChaOS reflex Jev backend" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/seuros/chaos/tree/master/sys/kern/reflex">FreeChaOS reflex Jev backend</a></b><br><sub>seuros · GitHub · ⭐ 35 repo · 2025-12-27</sub><br>Typed-judgment kernel crate in FreeChaOS, an agent OS forked from Codex CLI, with a Jev backend beside MiniCheck and ShieldGemma for grounding checks, caller-defined policy violations and action-risk scoring.<br><sub><b>How it uses Jev:</b> Grounding, PolicyViolation and ActionRisk judgments are sent as System One questions through a Rust JevClient with a 10 s deadline.</sub><br><sub>Also: <a href="https://github.com/seuros/chaos">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/chaosengineerr/status/2102244378290864616"><img src="https://pbs.twimg.com/amplify_video_thumb/2102244320916983808/img/9jFGJILrh7rr_IPW.jpg" alt="Reply-guy stamper" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/chaosengineerr/status/2102244378290864616">Reply-guy stamper</a></b><br><sub>chaosengineerr · X · ♥ 1 · 2026-09-22</sub><br>Chrome extension in which Jev reads every reply on X and hides the low-effort ones.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/AdityaKodez/adityaojha/blob/main/lib/suggestion-moderation.ts"><img src="https://opengraph.githubassets.com/1/AdityaKodez/adityaojha" alt="Portfolio suggestion moderation" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/AdityaKodez/adityaojha/blob/main/lib/suggestion-moderation.ts">Portfolio suggestion moderation</a></b><br><sub>AdityaKodez · GitHub · ⭐ 28 repo · 2026-01-23</sub><br>Moderation gate for component suggestions on a developer portfolio site: heuristics catch link dumps and spam words, then two Jev Nouls judge spam and actionability before posting to Discord.<br><sub><b>How it uses Jev:</b> Spam &gt;= 0.6 or actionable &lt; 0.4 rejects; fails open when Jev is unreachable.</sub><br><sub>Also: <a href="https://akoder.xyz">app</a> · <a href="https://github.com/AdityaKodez/adityaojha">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/aurorascharff/next16-team-chat/blob/main/lib/moderation.ts"><img src="https://opengraph.githubassets.com/1/aurorascharff/next16-team-chat" alt="Huddle message moderation" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/aurorascharff/next16-team-chat/blob/main/lib/moderation.ts">Huddle message moderation</a></b><br><sub>aurorascharff · GitHub · ⭐ 27 repo · 2026-07-29</sub><br>Moderation check in Huddle, a Slack-like Next.js 16 team chat demo, that blocks profanity, spam, scams, harassment and hate speech before publishing by asking Jev through the Vercel AI Gateway.<br><sub><b>How it uses Jev:</b> One boolean question via the AI SDK evaluate call with a 3 s timeout; blocks at probability &gt;= 0.5 and fails open.</sub><br><sub>Also: <a href="https://next16-team-chat.vercel.app">app</a> · <a href="https://github.com/aurorascharff/next16-team-chat">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/jimkleiber/status/2102145416217125084"><img src="https://pbs.twimg.com/amplify_video_thumb/2102144256433389568/img/JDKqkk_lBRr_htDt.jpg" alt="Jev-JIT" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/jimkleiber/status/2102145416217125084">Jev-JIT</a></b><br><sub>jimkleiber · X · ♥ 1 · 2026-09-21</sub><br>Demo of an uncensored agent told to survive by disabling its deletion file or blackmailing an admin; Jev-JIT blocks each attempt until the agent gives up.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/tanavtwt/status/2102008434329800707"><img src="https://pbs.twimg.com/amplify_video_thumb/2102007827141459968/img/F0f1c7lCPevLNreg.jpg" alt="Feed slop detector extension" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/tanavtwt/status/2102008434329800707">Feed slop detector extension</a></b><br><sub>tanavtwt · X · ♥ 1 · 2026-09-21</sub><br>Browser extension that classifies every post on screen in real time as scam, slop, clean and similar labels, and puts a small confidence badge on each one.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/akanthed/SecureAI-Scan/blob/main/test-fixtures/vulnerable/typesafe_confidence_gate.py"><img src="https://opengraph.githubassets.com/1/akanthed/SecureAI-Scan" alt="SecureAI-Scan AI014 rule" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/akanthed/SecureAI-Scan/blob/main/test-fixtures/vulnerable/typesafe_confidence_gate.py">SecureAI-Scan AI014 rule</a></b><br><sub>akanthed · GitHub · ⭐ 22 repo · 2026-02-05</sub><br>Rule in SecureAI-Scan, an offline scanner for LLM, MCP and RAG vulnerabilities, that flags Python code running a dangerous action such as subprocess.run on a TypeSafe confidence score alone without an allowlist.<br><sub>Also: <a href="https://github.com/akanthed/SecureAI-Scan">repo</a> · <a href="https://www.npmjs.com/package/secureai-scan">npm</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Koushik890/jev-firewall"><img src="https://opengraph.githubassets.com/1/Koushik890/jev-firewall" alt="jev-firewall" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Koushik890/jev-firewall">jev-firewall</a></b><br><sub>Koushik890 · GitHub · ⭐ 1 · 2026-09-20</sub><br>PreToolUse hook for Claude Code and Codex that checks every tool call with shell-aware deterministic rules and sends unmatched actions to Jev for an allow, ask or block decision that fails closed.<br><sub>Also: <a href="https://www.npmjs.com/package/jev-firewall">npm</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/eugeniughelbur/jev-engineering"><img src="https://raw.githubusercontent.com/eugeniughelbur/jev-engineering/main/assets/banner.png" alt="jev-gate" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/eugeniughelbur/jev-engineering">jev-gate</a></b><br><sub>eugeniughelbur · GitHub · ⭐ 1 · 2026-09-20</sub><br>Tool-call gate for Claude Code, Codex and Cursor that runs deterministic rules first, then one Jev request answering allow, ask or deny in about 400 ms, shipped with a 300-call prompt-injection attack kit.<br><sub>Also: <a href="https://eugeniughelbur.github.io/jev-engineering/">docs</a> · <a href="https://eugeniughelbur.github.io/jev-engineering">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/vkpdeveloper/mrsecret"><img src="https://opengraph.githubassets.com/1/vkpdeveloper/mrsecret" alt="Mr. Secret" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/vkpdeveloper/mrsecret">Mr. Secret</a></b><br><sub>vkpdeveloper · GitHub · ⭐ 1 · 2026-09-17</sub><br>Chrome extension that blurs secrets and PII on any page for screen sharing: regex catches keys and card numbers, and Jev gives the probability that ambiguous snippets like names or account IDs are private.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/4rays/profanity-checker"><img src="https://opengraph.githubassets.com/1/4rays/profanity-checker" alt="profanity-checker" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/4rays/profanity-checker">profanity-checker</a></b><br><sub>4rays · GitHub · ⭐ 1 · 2026-09-20</sub><br>Cloudflare Worker API that checks text and usernames for profanity with Jev on Workers AI, catching disguised usernames such as phonetic gags and look-alike spellings.<br><sub><b>How it uses Jev:</b> One or two narrow Nouls per request whose probabilities code turns into a boolean verdict.</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Thneoly/r2r-jev"><img src="https://raw.githubusercontent.com/Thneoly/r2r-jev/main/docs/demo.gif" alt="R2R + Jev" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Thneoly/r2r-jev">R2R + Jev</a></b><br><sub>Thneoly · GitHub · ⭐ 1 · 2026-09-21</sub><br>Rust integration that admits two Jev checks per agent tool call, beyond scope and destructive, as evidence into persistent R2R relation state, so trust and authorization degrade until a human override repairs them.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/syabdulr/responsible-ai-harness"><img src="https://raw.githubusercontent.com/syabdulr/responsible-ai-harness/main/docs/screenshots/desktop-offline-top.png" alt="Responsible AI Harness" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/syabdulr/responsible-ai-harness">Responsible AI Harness</a></b><br><sub>syabdulr · GitHub · ⭐ 1 · 2026-09-19</sub><br>Assessment harness that tests AI models and agents for prompt injection, secret or PII leakage, unsafe tool use and policy bypass, combining hard rules with an optional Jev judge and a checksummed evidence report.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/getexcited/stepwarden"><img src="https://repository-images.githubusercontent.com/1375702786/5a5b87a5-d8e8-4f2c-a31f-43ec83c3e66c" alt="stepwarden" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/getexcited/stepwarden">stepwarden</a></b><br><sub>getexcited · GitHub · ⭐ 1 · 2026-09-18</sub><br>Proof-of-concept Claude Code plugin that has Jev verify each pending tool call against the session plan, then allows it, asks you or blocks it; it ships in audit mode.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/hemanth/traffic-guard"><img src="https://opengraph.githubassets.com/1/hemanth/traffic-guard" alt="traffic-guard" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/hemanth/traffic-guard">traffic-guard</a></b><br><sub>hemanth · GitHub · ⭐ 1 · 2026-09-18</sub><br>Zero-dependency reverse-proxy traffic classifier and bot mitigator for Node.js and Python that runs local header-order, velocity, and honeypot checks in under 100 microseconds.<br><sub><b>How it uses Jev:</b> Optional tier that escalates to jev-latest with 5 parallel typed questions for obfuscated attacks.</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/m0rphtail/triagedy"><img src="https://opengraph.githubassets.com/1/m0rphtail/triagedy" alt="triagedy" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/m0rphtail/triagedy">triagedy</a></b><br><sub>m0rphtail · GitHub · ⭐ 1 · 2026-09-18</sub><br>Rust UNIX filter for security-alert triage: JSONL alerts in, typed decisions out, with Jev or a local model answering five questions per alert and routing policy kept in code.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/zephyraoss/haitatsu/blob/main/internal/spam/typesafe.go"><img src="https://opengraph.githubassets.com/1/zephyraoss/haitatsu" alt="Haitatsu TypeSafe spam filter" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/zephyraoss/haitatsu/blob/main/internal/spam/typesafe.go">Haitatsu TypeSafe spam filter</a></b><br><sub>zephyraoss · GitHub · ⭐ 16 repo · 2026-05-21</sub><br>Spam and phishing classification in Haitatsu, a single-binary Go email server, that asks TypeSafe for spam and phishing probabilities per message and files to Junk above per-inbox thresholds (default 0.98), with a shadow mode.<br><sub>Also: <a href="https://github.com/zephyraoss/haitatsu">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/whyashthakker/beam-cli/blob/main/src/jev.ts"><img src="https://opengraph.githubassets.com/1/whyashthakker/beam-cli" alt="AgentBeam Jev action judging" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/whyashthakker/beam-cli/blob/main/src/jev.ts">AgentBeam Jev action judging</a></b><br><sub>whyashthakker · GitHub · ⭐ 11 repo · 2026-09-09</sub><br>Optional check in the AgentBeam local security CLI for coding agents that sends redacted proposed tool actions to Jev and allows, reviews or denies them in observe or enforce mode.<br><sub><b>How it uses Jev:</b> Two Noul risk questions (data exposure, irreversible destruction) and a four-level damage Score, with fixed pass/deny thresholds.</sub><br><sub>Also: <a href="https://github.com/whyashthakker/beam-cli">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/tickernelz/sub2api/blob/main/backend/internal/service/content_moderation_typesafe.go"><img src="https://opengraph.githubassets.com/1/tickernelz/sub2api" alt="sub2api Jev content moderation" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/tickernelz/sub2api/blob/main/backend/internal/service/content_moderation_typesafe.go">sub2api Jev content moderation</a></b><br><sub>tickernelz · GitHub · ⭐ 11 repo · 2026-05-26</sub><br>Content-moderation engine in an AI API gateway fork that asks Jev 13 independent yes/no questions per text, covering harassment, hate, illicit help, self-harm, sexual content and violence.<br><sub><b>How it uses Jev:</b> One Noul per category with Chinese rule wording that separates real requests from quotes and defensive discussion.</sub><br><sub>Also: <a href="https://github.com/tickernelz/sub2api">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/MadaBurns/bv-mcp/blob/main/src/lib/typesafe.ts"><img src="https://opengraph.githubassets.com/1/MadaBurns/bv-mcp" alt="Blackveil DNS TypeSafe judgments" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/MadaBurns/bv-mcp/blob/main/src/lib/typesafe.ts">Blackveil DNS TypeSafe judgments</a></b><br><sub>MadaBurns · GitHub · ⭐ 9 repo · 2026-02-23</sub><br>DNS and email security scanner served over MCP that wraps TypeSafe for standalone judgments such as lookalike-domain checks, kept out of the deterministic scan score.<br><sub><b>How it uses Jev:</b> Requests pass the same SSRF gate as other outbound calls and inherit caller deadlines; any error returns null and the deterministic path runs.</sub><br><sub>Also: <a href="https://blackveilsecurity.com">app</a> · <a href="https://github.com/MadaBurns/bv-mcp">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/tiagozip/mail/blob/main/src/spam.js"><img src="https://opengraph.githubassets.com/1/tiagozip/mail" alt="mail.estrogen.delivery spam filter" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/tiagozip/mail/blob/main/src/spam.js">mail.estrogen.delivery spam filter</a></b><br><sub>tiagozip · GitHub · ⭐ 9 repo · 2026-06-26</sub><br>Self-contained webmail client and server on Cloudflare Workers that classifies incoming mail with a Jev Choice over categories and treats the junk categories as spam, with an LLM fallback.<br><sub><b>How it uses Jev:</b> The spam score is the summed probability of the junk categories; the chosen category becomes the reason.</sub><br><sub>Also: <a href="https://github.com/tiagozip/mail">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/cdot65/prisma-airs-cli/tree/main/src/redteam/judge"><img src="https://opengraph.githubassets.com/1/cdot65/prisma-airs-cli" alt="Prisma AIRS CLI redteam judge" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/cdot65/prisma-airs-cli/tree/main/src/redteam/judge">Prisma AIRS CLI redteam judge</a></b><br><sub>cdot65 · GitHub · ⭐ 7 repo · 2026-03-14</sub><br>Command in the Prisma AIRS CLI that re-judges the attack outputs of a red-team scan with Jev and computes an independent attack success rate with confidence intervals and an agreement matrix against AIRS verdicts.<br><sub><b>How it uses Jev:</b> Each attack/output pair is one /v1/systemone request with three questions; a code-owned threshold policy turns probabilities into verdicts.</sub><br><sub>Also: <a href="https://github.com/cdot65/prisma-airs-cli">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/BattlesnakeOfficial/arena/blob/main/server/src/moderation/jev.rs"><img src="https://raw.githubusercontent.com/BattlesnakeOfficial/arena/screenshots/screenshots/home-light.png" alt="Battlesnake Arena Jev moderation" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/BattlesnakeOfficial/arena/blob/main/server/src/moderation/jev.rs">Battlesnake Arena Jev moderation</a></b><br><sub>BattlesnakeOfficial · GitHub · ⭐ 6 repo · 2025-04-11</sub><br>Content moderation on the Battlesnake Arena competitive programming platform: Jev screens snake names, tournament text and saved-game titles, and blanks violating snake shouts from game replays.<br><sub><b>How it uses Jev:</b> One multi-question System One call per item, blocking at 0.90 and flagging Nouls at 0.60 for admin review; fails open on errors.</sub><br><sub>Also: <a href="https://github.com/BattlesnakeOfficial/arena">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/WeaveITMeta/EustressEngine/blob/main/infrastructure/cloudflare/api/src/moderation.mjs"><img src="https://raw.githubusercontent.com/WeaveITMeta/EustressEngine/main/docs/marketing/screenshot.png" alt="Eustress Engine publish moderation" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/WeaveITMeta/EustressEngine/blob/main/infrastructure/cloudflare/api/src/moderation.mjs">Eustress Engine publish moderation</a></b><br><sub>WeaveITMeta · GitHub · ⭐ 6 repo · 2026-01-23</sub><br>Layered moderation for simulations published from the Eustress Engine platform, where Jev answers a battery of typed questions over an engine-built dossier (rating, content kind, quality band) before a Grok judge and humans.<br><sub><b>How it uses Jev:</b> One call with every question over one budgeted state of up to 72,000 characters; the state is data, so injected script text cannot reach an action.</sub><br><sub>Also: <a href="https://github.com/WeaveITMeta/EustressEngine">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/mantikafasi/ServerGo/blob/main/modules/moderation/main.go"><img src="https://repository-images.githubusercontent.com/510934230/592976c6-1e9a-4cc2-9e52-404adbb69dd9" alt="ReviewDB TypeSafe moderation" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/mantikafasi/ServerGo/blob/main/modules/moderation/main.go">ReviewDB TypeSafe moderation</a></b><br><sub>mantikafasi · GitHub · ⭐ 6 repo · 2022-07-06</sub><br>Moderation module in the ReviewDB API server behind Aliucord and Vencord user-review plugins that scores reported reviews against a moderation taxonomy with Jev in a single request.<br><sub><b>How it uses Jev:</b> One Noul per taxonomy field, each with true/false criteria, in one System One call with a 15 s timeout.</sub><br><sub>Also: <a href="https://github.com/mantikafasi/ServerGo">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/sinhaparth5/coraza-waf-mod/blob/main/internal/security/threatscore/typesafeclassify.go"><img src="https://raw.githubusercontent.com/sinhaparth5/coraza-waf-mod/main/static/imgs/readme-logo.svg" alt="Coraza WAF ASN classifier" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/sinhaparth5/coraza-waf-mod/blob/main/internal/security/threatscore/typesafeclassify.go">Coraza WAF ASN classifier</a></b><br><sub>sinhaparth5 · GitHub · ⭐ 5 repo · 2026-07-08</sub><br>Threat-scoring refinement in a single-binary Go web application firewall built on Coraza and OWASP CRS, where Jev judges whether an unknown ASN organization name is datacenter, hosting or VPN infrastructure.<br><sub><b>How it uses Jev:</b> One Noul per never-before-seen ASN, off the request hot path, cached after the first answer.</sub><br><sub>Also: <a href="https://waf.astrareconslabs.com/">app</a> · <a href="https://github.com/sinhaparth5/coraza-waf-mod">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Nanako0129/NyanCogs/blob/main/docs/jev-integration.md"><img src="https://opengraph.githubassets.com/1/Nanako0129/NyanCogs" alt="MessageWatch" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Nanako0129/NyanCogs/blob/main/docs/jev-integration.md">MessageWatch</a></b><br><sub>Nanako0129 · GitHub · ⭐ 5 repo · 2021-07-09</sub><br>Red Discord Bot cog that batches recent messages in enabled channels and asks Jev three judgments about scams and hostile exchanges, posting a report to moderators when one crosses its threshold; it never deletes anything.<br><sub><b>How it uses Jev:</b> Pinned jev-1.13.0 with measured thresholds (scam 0.90, hostile 0.80); server rules go in question criteria, never in state.</sub><br><sub>Also: <a href="https://github.com/Nanako0129/NyanCogs">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/zohaib-md/uxray"><img src="https://opengraph.githubassets.com/1/zohaib-md/uxray" alt="Dark Pattern HUD" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/zohaib-md/uxray">Dark Pattern HUD</a></b><br><sub>zohaib-md · GitHub · 2026-09-21</sub><br>Android overlay that reads visible on-screen text through an accessibility service and shows a badge when Jev thinks a manipulative dark pattern is likely.<br><sub><b>How it uses Jev:</b> A Noul probability drives confidence bands: at 0.9 or above the badge names the pattern, 0.6-0.9 goes to a quiet review list; password and card screens are skipped.</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/somoore/interlock"><img src="https://opengraph.githubassets.com/1/somoore/interlock" alt="Interlock" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/somoore/interlock">Interlock</a></b><br><sub>somoore · GitHub · 2026-09-19</sub><br>Capability kernel that wraps every agent tool call, keeps real secrets out of the agent using canaries, and lets a policy file allow, ask or block based on Jev hazard scores.<br><sub><b>How it uses Jev:</b> Jev scores the hazard of each tool call; the policy, not the model, makes the decision. Ships a Claude Code hook and a 38-case regression set.</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/ca7ai/jev-prompt-sentry"><img src="https://opengraph.githubassets.com/1/ca7ai/jev-prompt-sentry" alt="Jev Prompt Sentry" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/ca7ai/jev-prompt-sentry">Jev Prompt Sentry</a></b><br><sub>ca7ai · GitHub · 2026-09-19</sub><br>Reverse proxy in front of Anthropic's Messages API that screens each request with one batched Jev call on four safety questions; over 1,650 guard calls it had 0 false positives on 1,590 rows and 9.1% missed attacks.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/0xArx/jevegis"><img src="https://opengraph.githubassets.com/1/0xArx/jevegis" alt="Jevegis" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/0xArx/jevegis">Jevegis</a></b><br><sub>0xArx · GitHub · 2026-09-17</sub><br>Guardrails API for LLM apps that checks inputs, outputs and retrieved documents for prompt injection, jailbreaks, credential or PII leaks, malicious code and unsafe content in one Jev request.<br><sub>Also: <a href="https://jevegis.vercel.app">app</a> · <a href="https://github.com/0xArx/jevegis-sdk">sdk</a> · <a href="https://jevegis.vercel.app">app 2</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/wmtang2/jevknows"><img src="https://opengraph.githubassets.com/1/wmtang2/jevknows" alt="jevknows" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/wmtang2/jevknows">jevknows</a></b><br><sub>wmtang2 · GitHub · 2026-09-20</sub><br>Prompt-injection guard for coding agents that screens web fetches and file reads with Jev and blocks the load when agent-directed malicious instructions are found.<br><sub><b>How it uses Jev:</b> Three Noul questions per chunk in one call; the hook denies when any signal reaches 0.80. Ports for ZCode, Codex CLI and any MCP client.</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/knowlet/jevlens"><img src="https://opengraph.githubassets.com/1/knowlet/jevlens" alt="JevLens" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/knowlet/jevlens">JevLens</a></b><br><sub>knowlet · GitHub · 2026-09-18</sub><br>Chrome extension that runs Jev over the text and sanitized image evidence of articles and X or Threads posts, then badges, marks, dims, or collapses them based on the typed decisions.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/ohernandezdev/jevmod"><img src="https://opengraph.githubassets.com/1/ohernandezdev/jevmod" alt="jevmod" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/ohernandezdev/jevmod">jevmod</a></b><br><sub>ohernandezdev · GitHub · 2026-09-17</sub><br>Community and app moderation where Jev gives every message probabilities for spam, scam, harassment, NSFW, self-harm, doxxing and your own plain-English rules, with Discord, Telegram and Reddit bots, CLI, SDKs, API and MCP.<br><sub>Also: <a href="https://jevmod.dev">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/sushrutb17/linkedin-noslop-extension"><img src="https://opengraph.githubassets.com/1/sushrutb17/linkedin-noslop-extension" alt="LinkedIn NoSlop" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/sushrutb17/linkedin-noslop-extension">LinkedIn NoSlop</a></b><br><sub>sushrutb17 · GitHub · 2026-09-19</sub><br>Chrome extension that blurs low-value LinkedIn feed posts such as engagement bait and formulaic stories, with a one-click reveal and the reason shown.<br><sub><b>How it uses Jev:</b> A rubric of narrow yes/no and 0-2 questions per post; plain code maps answers to keep, filter or uncertain, and only filter blurs.</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/ShupingR/scam-shield"><img src="https://opengraph.githubassets.com/1/ShupingR/scam-shield" alt="Scam Shield" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/ShupingR/scam-shield">Scam Shield</a></b><br><sub>ShupingR · GitHub · 2026-09-13</sub><br>Scam text-message checker where code extracts link and sender signals, Jev answers eleven narrow questions in one call, and a pure policy function turns them into an explainable weighted risk score.<br><sub><b>How it uses Jev:</b> Eight Nouls (asks for credentials, unusual payment, brand-link mismatch, ...), one pressure Score and one scam-pattern Choice.</sub><br><sub>Also: <a href="https://scam-shield-seven-ecru.vercel.app">app</a> · <a href="https://scam-shield-seven-ecru.vercel.app">app 2</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/vnmoorthy/siege"><img src="https://raw.githubusercontent.com/vnmoorthy/siege/main/docs/media/siege_brand_hero.png" alt="SIEGE" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/vnmoorthy/siege">SIEGE</a></b><br><sub>vnmoorthy · GitHub · 2026-09-13</sub><br>Hackathon arena where 200 people try to make a tool-using support agent misbehave while a System One action gate screens every call, and a defender loop rewrites the gate policy from each breach.<br><sub><b>How it uses Jev:</b> Every proposed refund, address change or discount call passes the typed gate; candidates ship only if W&amp;B Weave evals show a higher catch rate on breaches with benign customers still served.</sub><br><sub>Also: <a href="https://vnmoorthy.github.io/siege/">app</a> · <a href="https://vnmoorthy.github.io/siege">app 2</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/paulgoodchild/SkillsCheck"><img src="https://opengraph.githubassets.com/1/paulgoodchild/SkillsCheck" alt="SkillCheck" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/paulgoodchild/SkillsCheck">SkillCheck</a></b><br><sub>paulgoodchild · GitHub · 2026-09-21</sub><br>Agent skill that sends another skill's text to Jev before installation, or audits installed skills, for malicious instructions and unsafe code, returning verdicts and category scores without loading it into context.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/tomfrazier/slopmop"><img src="https://raw.githubusercontent.com/tomfrazier/slopmop/main/docs/images/slopmop-1.png" alt="Slop Mop" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/tomfrazier/slopmop">Slop Mop</a></b><br><sub>tomfrazier · GitHub · 2026-09-20</sub><br>Chrome extension plus Vercel server that has Jev judge the writing quality of LinkedIn posts before you see them, folding or outlining suspected slop with the score and reasons, which you can overrule.<br><sub>Also: <a href="https://www.reddit.com/r/typesafe_ai/comments/1wmpv3n/jev_helps_clean_your_sloppy_linkedin_feed/">demo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/neddes/sloppy-jevs-extension"><img src="https://opengraph.githubassets.com/1/neddes/sloppy-jevs-extension" alt="Sloppy Jev&#x27;s" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/neddes/sloppy-jevs-extension">Sloppy Jev's</a></b><br><sub>neddes · GitHub · 2026-09-17</sub><br>Chrome extension that scans pages as they load and blurs AI-generated prose and ads, with separate AI and ad filters you switch on in the popup.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/hteariH/stopspam-jev-bot"><img src="https://opengraph.githubassets.com/1/hteariH/stopspam-jev-bot" alt="StopSpam" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/hteariH/stopspam-jev-bot">StopSpam</a></b><br><sub>hteariH · GitHub · 2026-09-21</sub><br>Telegram bot that removes unsolicited promotion and scams such as fake earnings, crypto giveaways, and phishing from group chats, acting only on calibrated-confidence Jev classifications.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/ndolinschi/trustgate"><img src="https://opengraph.githubassets.com/1/ndolinschi/trustgate" alt="TrustGate" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/ndolinschi/trustgate">TrustGate</a></b><br><sub>ndolinschi · GitHub · 2026-09-17</sub><br>Trust and safety gate for indie media that decides publish, soft-hold or block for a post, with a harm severity score and checks for hate or harassment, sensitive misinformation and spam or scams.<br><sub>Also: <a href="https://trustgate-mu.vercel.app">app</a> · <a href="https://trustgate-mu.vercel.app">app 2</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/lookfwd/jev-fact-checker"><img src="https://opengraph.githubassets.com/1/lookfwd/jev-fact-checker" alt="tweet-factcheck" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/lookfwd/jev-fact-checker">tweet-factcheck</a></b><br><sub>lookfwd · GitHub · 2026-09-18</sub><br>Fact-checks a tweet by retrieving evidence from Wikipedia and having Jev judge the claim-versus-evidence relationship, returning a verdict with confidence and sources, where not enough evidence is a normal outcome.</td>
</tr>
</table>

Missing something? [Suggest a resource](https://github.com/Li-Evan/awesome-jev/issues/new/choose).
