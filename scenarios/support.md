# 🎧 Customer Support and Sales

**English** · [简体中文](https://github.com/Li-Evan/awesome-jev/blob/main/zh-CN/scenarios/support.md)

Ticket routing, email triage, lead scoring, and CRM automation. 44 entries, ranked by community traction.

[← Back to Awesome Jev](https://github.com/Li-Evan/awesome-jev#browse-by-scenario)

<table>
<tr>
<td width="260" valign="top"><a href="https://x.com/romanbuildsaas/status/2100891604735099103"><img src="https://pbs.twimg.com/amplify_video_thumb/2100891566340501504/img/agvkcRfNWmnGbRI5.jpg" alt="Lead and outreach scoring" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/romanbuildsaas/status/2100891604735099103">Lead and outreach scoring</a></b><br><sub>romanbuildsaas · X · ♥ 3.3k · 2026-09-18</sub><br>Scoring of 700 high-intent leads and personalized outreach messages in 40 seconds for $0.09, predicting each message's performance with a confidence score and flagging lead-message mismatches.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://www.youtube.com/watch?v=CupCEehe2OQ"><img src="https://i.ytimg.com/vi/CupCEehe2OQ/hqdefault.jpg" alt="Sales Copilot with Jev" width="240"></a></td>
<td valign="top"><b><a href="https://www.youtube.com/watch?v=CupCEehe2OQ">Sales Copilot with Jev</a></b><br><sub>Kelvin Cleto · YouTube · ♥ 1.9k · 2026-09-20</sub><br>Portuguese walkthrough of a sales-meeting copilot that tracks calls and playbook steps, where Jev answers cheap decision questions before any LLM call to cut costs.<br><sub><b>How it uses Jev:</b> Probability questions about the meeting state gate the expensive LLM calls.</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/twentyhq/twenty/tree/main/packages/twenty-server/src/modules/workflow/workflow-executor/workflow-actions/classify"><img src="https://repository-images.githubusercontent.com/572984571/ef151ee9-3060-418b-bf88-cb689ab78c7b" alt="Twenty Classify workflow action" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/twentyhq/twenty/tree/main/packages/twenty-server/src/modules/workflow/workflow-executor/workflow-actions/classify">Twenty Classify workflow action</a></b><br><sub>twentyhq · GitHub · ⭐ 57.2k repo · 2022-12-01</sub><br>Classify step in the open-source Twenty CRM's workflows that asks Jev choice, score or boolean questions about a record, so later steps can branch on the answers and probabilities.<br><sub><b>How it uses Jev:</b> Jev is registered as the 'evaluation' model kind (jev-latest via @ai-sdk/typesafe-ai, 200 ms median latency listed).</sub><br><sub>Also: <a href="https://twenty.com">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/getanyapi-com/lurk"><img src="https://opengraph.githubassets.com/1/getanyapi-com/lurk" alt="lurk" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/getanyapi-com/lurk">lurk</a></b><br><sub>getanyapi-com · GitHub · ⭐ 97 · 2026-09-10</sub><br>Self-hostable Reddit buyer-intent finder that infers what your product solves and has Jev judge every title, post and comment it scans against your product.<br><sub><b>How it uses Jev:</b> Jev via OpenRouter or Vercel AI Gateway scores each item; an LLM handles product profiling and clustering.</sub><br><sub>Also: <a href="https://x.com/mxfp4/status/2101070906852298910">demo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/Box/status/2100993278955188320"><img src="https://pbs.twimg.com/amplify_video_thumb/2100986163511357440/img/o0Yzl7VqISwchxkk.jpg" alt="Box incident triage" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/Box/status/2100993278955188320">Box incident triage</a></b><br><sub>Box · X · ♥ 31 · 2026-09-18</sub><br>Box workflow that pulls an incident report, asks Jev whether it is customer-facing and how severe it is, moves the file to Escalate, Monitor or Review, and sends low-confidence cases to a human.<br><sub><b>How it uses Jev:</b> A Noul for customer-facing plus a severity Score, with a confidence threshold for human review.</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/tarasshyn/status/2101043617649340678"><img src="https://pbs.twimg.com/amplify_video_thumb/2101043565207916544/img/jTZjaCWwP1d9sx6D.jpg" alt="RedReplier buying-signal scoring" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/tarasshyn/status/2101043617649340678">RedReplier buying-signal scoring</a></b><br><sub>tarasshyn · X · ♥ 463 · 2026-09-18</sub><br>Scored 1,759,932 buying signals from 1.7 million mentions across Reddit, X, Bluesky, Hacker News and Facebook in 53 seconds for $0.65, ranking intent, product fit and competitor mentions.</td>
</tr>
<tr>
<td width="260" valign="top"></td>
<td valign="top"><b><a href="https://x.com/t0t0_build/status/2101082444577567162">WhatsApp customer group monitor</a></b><br><sub>t0t0_build · X · ♥ 280 · 2026-09-18</sub><br>Monitors 25+ WhatsApp groups with clients in real time, with Jev judging whether anything needs attention, such as urgent problems or unresolved orders, and only then asking an LLM to write a notification.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/sotak/status/2100701152824185319"><img src="https://pbs.twimg.com/amplify_video_thumb/2100700282434826240/img/H7dKngwXowyoEgJ6.jpg" alt="Real-time Clippy" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/sotak/status/2100701152824185319">Real-time Clippy</a></b><br><sub>sotak · X · ♥ 176 · 2026-09-17</sub><br>In-product Clippy that watches how someone uses an app and appears only when Jev judges they are hesitating, confused or stuck, with its reactions also chosen by Jev.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/razeden0/status/2102119174466396250"><img src="https://pbs.twimg.com/amplify_video_thumb/2102119097077006336/img/qrIQdb9RSULrBTqB.jpg" alt="Grok and Jev lead screener" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/razeden0/status/2102119174466396250">Grok and Jev lead screener</a></b><br><sub>razeden0 · X · ♥ 172 · 2026-09-21</sub><br>Lead-qualification pipeline where Jev answers 6 questions on each of 3,412 leads (20,472 decisions in 15.7 seconds for $0.41) and Grok 4.7 only drafts outreach for the leads worth reading.<br><sub><b>How it uses Jev:</b> Six yes/no, pick-one or score questions per lead gate what the LLM reads.</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/pierreeliottlal/status/2100912453999587657"><img src="https://pbs.twimg.com/amplify_video_thumb/2100911836891660288/img/gqUn5ZSLBlAEMZMT.jpg" alt="Outreach signals that book demos" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/pierreeliottlal/status/2100912453999587657">Outreach signals that book demos</a></b><br><sub>pierreeliottlal · X · ♥ 114 · 2026-09-18</sub><br>Sales analysis in which Jev read a dataset of thousands of outreach messages and found which intent signals generated the most booked demos, in 40 seconds for under $0.20.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/nifinet/status/2102065255694409940"><img src="https://pbs.twimg.com/media/HSwI_zwaQAA9uYF.jpg" alt="signal-ranker" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/nifinet/status/2102065255694409940">signal-ranker</a></b><br><sub>nifinet · Article · ♥ 105 · 2026-09-21</sub><br>Build guide for an open-source outbound bot where Claude Code pulls lead signals (job reposts, funding, tenders) and Jev ranks who to contact first, with judgments kept separate from a tunable policy file.<br><sub><b>How it uses Jev:</b> judge.py asks Jev for probabilities per lead signal; policy.py turns them into a sort order without further calls.</sub><br><sub>Also: <a href="https://yourmax.ai/">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://www.reddit.com/r/laravel/comments/1wjw2w1/detecting_spam_and_autoreplies_with_jev_and_the/"><img src="https://external-preview.redd.it/Up6svHbkrdKcDREH0Bxoz5U1BdqUtnTWYrPaM5OkqBI.jpeg?auto=webp&amp;s=a662330e21133bc799704e99bd9c97b2df961b97" alt="Spam and auto-reply detection in There There" width="240"></a></td>
<td valign="top"><b><a href="https://www.reddit.com/r/laravel/comments/1wjw2w1/detecting_spam_and_autoreplies_with_jev_and_the/">Spam and auto-reply detection in There There</a></b><br><sub>freekmurze · Reddit · ▲ 30 · 2026-09-18</sub><br>Walkthrough of using the Laravel AI SDK Jev support to flag spam and auto-replies in the There There help desk, with Noul, Choice, and Score examples in PHP.<br><sub><b>How it uses Jev:</b> Noul for spam and auto-reply probability on incoming messages.</sub><br><sub>Also: <a href="https://freek.dev/3194-detecting-spam-and-auto-replies-with-jev-and-the-laravel-ai-sdk">article</a> · <a href="https://freek.dev/3194-detecting-spam-and-auto-replies-with-jev-and-the-laravel-ai-sdk">project</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/merefield/discourse-chatbot"><img src="https://raw.githubusercontent.com/merefield/discourse-chatbot/main/images/surety.webp" alt="discourse-chatbot" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/merefield/discourse-chatbot">discourse-chatbot</a></b><br><sub>merefield · GitHub · ⭐ 84 · 2023-02-06</sub><br>RAG chatbot plugin for Discourse topics, chat and customer support that can use System One forum-scope judgments for blocked-question matching and tool selection, with embedding fallback.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/ENowoslawski/status/2100999124099195377"><img src="https://pbs.twimg.com/amplify_video_thumb/2100998985074835456/img/3FY78J6we-v6cyXz.jpg" alt="Instant Clay workflows" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/ENowoslawski/status/2100999124099195377">Instant Clay workflows</a></b><br><sub>ENowoslawski · X · ♥ 65 · 2026-09-18</sub><br>Demo of Jev building Clay go-to-market workflows almost instantly.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/ZeroGold/call-coach-ai"><img src="https://github.com/user-attachments/assets/b1d3768f-ae61-45a7-a68b-644367ef24ab" alt="Call Coach" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/ZeroGold/call-coach-ai">Call Coach</a></b><br><sub>ZeroGold · GitHub · ⭐ 35 · 2026-09-20</sub><br>Live sales-call assistant that sends the conversation to Jev after every sentence and shows the rep a suggested next action and buying stage with a confidence score, from a microphone or a sample call.<br><sub>Also: <a href="https://www.reddit.com/r/LLMDevs/comments/1wltrsa/i_built_an_opensource_app_that_uses_jev_to_coach/">discussion</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/sotak/status/2100927660029247538"><img src="https://pbs.twimg.com/amplify_video_thumb/2100925956978294784/img/grFanN32FuhiSULl.jpg" alt="Inline Manual adaptive help" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/sotak/status/2100927660029247538">Inline Manual adaptive help</a></b><br><sub>sotak · X · ♥ 23 · 2026-09-18</sub><br>Real-time in-app support for InlineManual.com that detects where a user is struggling and adds explanations, suggestions or actions directly into the UI, with no chatbot.<br><sub>Also: <a href="https://inlinemanual.com">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/AIsaOneHQ/status/2100894473085489510"><img src="https://pbs.twimg.com/amplify_video_thumb/2100886600880111616/img/Y6PwJ2mf_8-BWChg.jpg" alt="Worth Replying" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/AIsaOneHQ/status/2100894473085489510">Worth Replying</a></b><br><sub>AIsaOneHQ · X · ♥ 15 · 2026-09-18</sub><br>Takes a company's domain and finds X users already discussing the problems its product solves; on typesafe.ai it found 150 tweets and made 750 Jev decisions in 18.8s for $0.007.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/yoanbernabeu/demo-symfony-typesafe"><img src="https://raw.githubusercontent.com/yoanbernabeu/demo-symfony-typesafe/main/docs/qualification.jpg" alt="Symfony support triage demo" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/yoanbernabeu/demo-symfony-typesafe">Symfony support triage demo</a></b><br><sub>yoanbernabeu · GitHub · ⭐ 2 · 2026-09-19</sub><br>French Symfony AI demo that qualifies real requests sent to French public services with one Jev call each: the requester's intent among six, urgency, and whether it is a bug to forward to developers.<br><sub>Also: <a href="https://x.com/yOyO38/status/2101705862008001011">demo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/GoSailGlobal/status/2100957577958097199"><img src="https://pbs.twimg.com/amplify_video_thumb/2100957554293751809/img/Jfl8lu536UlBOyqr.jpg" alt="jev-support-pulse" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/GoSailGlobal/status/2100957577958097199">jev-support-pulse</a></b><br><sub>GoSailGlobal · X · ♥ 6 · 2026-09-18</sub><br>Chinese experiment labeling 170,400 2017 tweets to seven brands' support accounts with Jev for $1.84: at equal false alarms it caught 17 outages about 4.1 hours before the brand admitted them, versus 10 for tweet volume.<br><sub>Also: <a href="https://github.com/zhuyansen/jev-support-pulse">repo</a> · <a href="https://github.com/zhuyansen/jev-support-pulse">project</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/warmbly/warmbly/tree/main/internal/pkg/typesafe"><img src="https://raw.githubusercontent.com/warmbly/warmbly/main/docs/assets/dashboard-campaigns.png" alt="Warmbly TypeSafe client" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/warmbly/warmbly/tree/main/internal/pkg/typesafe">Warmbly TypeSafe client</a></b><br><sub>warmbly · GitHub · ⭐ 308 repo · 2026-01-17</sub><br>Open-source cold outreach and email warmup platform that uses TypeSafe judgments for inbox tagging, reply intent classification, draft gating, bounce causes and form submission triage.<br><sub>Also: <a href="https://warmbly.com">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/malekoo/status/2100439840575684910"><img src="https://pbs.twimg.com/media/HSZCwYKWMAAC4Tr.jpg?name=orig" alt="Jev in-app help for a Mac app" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/malekoo/status/2100439840575684910">Jev in-app help for a Mac app</a></b><br><sub>malekoo · X · ♥ 5 · 2026-09-17</sub><br>In-app help for a Mac app that works with no model loaded: Jev reads the question against the built-in manual and picks the matching article or none, scoring 42/42 with a median 0.93 s.<br><sub><b>How it uses Jev:</b> Choice over manual articles plus a no-match option, with the whole manual as state.</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/DECRUX9812/openjev"><img src="https://opengraph.githubassets.com/1/DECRUX9812/openjev" alt="open-Jev (DECRUX9812)" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/DECRUX9812/openjev">open-Jev (DECRUX9812)</a></b><br><sub>DECRUX9812 · GitHub · ⭐ 3 · 2026-09-18</sub><br>Local, zero-cost reimplementation of a Jev decision layer that answers seven typed questions about a job posting on your CPU, separating in-house IT requisitions from small businesses that are sales leads.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Nine-Minds/alga-psa/blob/main/ee/server/src/services/smartSearch/typesafeClient.ts"><img src="https://www.nineminds.com/imported-media/Overview%20Dashboard.png" alt="Alga PSA smart ticket search" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Nine-Minds/alga-psa/blob/main/ee/server/src/services/smartSearch/typesafeClient.ts">Alga PSA smart ticket search</a></b><br><sub>Nine-Minds · GitHub · ⭐ 141 repo · 2024-11-04</sub><br>Open-source MSP service desk whose smart search has Jev rerank the filtered Tickets and Projects lists, so "customer can't print" can surface "Xerox reports offline".<br><sub>Also: <a href="https://github.com/Nine-Minds/alga-psa/blob/main/docs/plans/2026-09-20-jev-smart-ticket-search-plan.md">plan</a> · <a href="https://www.nineminds.com/alga-psa">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/liulangjietou/customer_work/tree/main/customer-work-starter/src/main/java/com/richard/fyoung/customerwork/capability/typesafe"><img src="https://github.com/user-attachments/assets/75a324d7-4e2e-4383-b049-c3cfc7802ee5" alt="customer-work Jev decisions" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/liulangjietou/customer_work/tree/main/customer-work-starter/src/main/java/com/richard/fyoung/customerwork/capability/typesafe">customer-work Jev decisions</a></b><br><sub>liulangjietou · GitHub · ⭐ 133 repo · 2026-06-13</sub><br>Enterprise customer-service agent platform on AgentScope Java that adds Jev structured decisions to the main conversation path and refund flow, with a circuit breaker and shadow display in the admin console.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/zeetakou/status/2101945022782284192"><img src="https://pbs.twimg.com/amplify_video_thumb/2101930224544104448/img/KJiNk6RfkI8mPRNs.jpg" alt="Telemarketing AI with Jev" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/zeetakou/status/2101945022782284192">Telemarketing AI with Jev</a></b><br><sub>zeetakou · X · ♥ 2 · 2026-09-21</sub><br>Outbound calling agent on the GPT Live API that dials a lead list and transfers promising prospects, now testing Jev for calls like whether a lead is promising, when to hand off, and redial priority.<br><sub><b>How it uses Jev:</b> In-call and post-call judgments: prospect quality, hand-off now or not, redial priority.</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/UiPath/uipath-python/tree/main/packages/uipath/samples/ticket-triage-agent"><img src="https://opengraph.githubassets.com/1/UiPath/uipath-python" alt="UiPath ticket triage agent" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/UiPath/uipath-python/tree/main/packages/uipath/samples/ticket-triage-agent">UiPath ticket triage agent</a></b><br><sub>UiPath · GitHub · ⭐ 98 repo · 2025-01-31</sub><br>Sample UiPath agent for two-tier support ticket triage where Jev routes each ticket fast, escalating to Action Center human review or an LLM-drafted auto-reply.<br><sub>Also: <a href="https://uipath.github.io/uipath-python/">docs</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/zhayujie/status/2102009189765881894"><img src="https://pbs.twimg.com/amplify_video_thumb/2102007612569190400/img/Yv_-w6zdmBlVS5Mu.jpg" alt="CowAgent ticket analysis tool" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/zhayujie/status/2102009189765881894">CowAgent ticket analysis tool</a></b><br><sub>zhayujie · X · ♥ 1 · 2026-09-21</sub><br>Batch support-ticket analysis tool that CowAgent built on Jev, making one call per ticket that returns 7 judgments with probabilities in about 500ms.<br><sub><b>How it uses Jev:</b> Seven typed questions per ticket in one request.</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/GhrezaKh74/JevTicktRouter"><img src="https://raw.githubusercontent.com/GhrezaKh74/JevTicktRouter/master/docs/screenshots/00-architecture.png" alt="JevTicketRouter" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/GhrezaKh74/JevTicktRouter">JevTicketRouter</a></b><br><sub>GhrezaKh74 · GitHub · ⭐ 1 · 2026-09-17</sub><br>Support-ticket triage app on .NET 10 and React 19 that asks Jev five batched questions about a Persian or English ticket, then lets a deterministic rule engine decide routing, escalation and redaction.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/timbuildwithai/status/2102167332172767392"><img src="https://pbs.twimg.com/media/HSxlNgsWMAAzwJr.jpg?name=orig" alt="n8n lead qualification with Jev" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/timbuildwithai/status/2102167332172767392">n8n lead qualification with Jev</a></b><br><sub>timbuildwithai · X · ♥ 1 · 2026-09-21</sub><br>Lead-qualification workflow in n8n where Jev returns probabilities for need, budget, timing and buying intent, a JS step scores and routes each lead HOT/WARM/COLD, and OpenAI only writes the reply.<br><sub><b>How it uses Jev:</b> Four Nouls per lead turned into a deterministic score in code.</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/TheEleventhAvatar/triage-bot"><img src="https://github.com/user-attachments/assets/9912dc0f-2033-40c7-a149-58a14093dec8" alt="triage-bot" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/TheEleventhAvatar/triage-bot">triage-bot</a></b><br><sub>TheEleventhAvatar · GitHub · ⭐ 1 · 2026-09-19</sub><br>Support-ticket bot where Jev routes each ticket to a general, account, billing or technical agent and decides whether a human should take over, then Cerebras drafts the reply; both calls are timed separately.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/damien-schneider/reflet/blob/main/packages/backend/convex/feedback/triage_evaluation.ts"><img src="https://opengraph.githubassets.com/1/damien-schneider/reflet" alt="Reflet feedback triage" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/damien-schneider/reflet/blob/main/packages/backend/convex/feedback/triage_evaluation.ts">Reflet feedback triage</a></b><br><sub>damien-schneider · GitHub · ⭐ 37 repo · 2026-01-17</sub><br>Feedback triage in Reflet, an open-source product feedback and roadmap platform: Jev decides whether a submission is actionable, withholds junk from the public board, flags items for review and auto-tags them.<br><sub><b>How it uses Jev:</b> Boolean usefulness/junk/needsReview questions plus per-tag questions via the AI SDK evaluate call; junk &gt;= 0.5 is withheld and tags need 0.65, max 3.</sub><br><sub>Also: <a href="https://www.reflet.app">app</a> · <a href="https://github.com/damien-schneider/reflet">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/calagopus/bot/blob/main/src/ai/decisions.rs"><img src="https://opengraph.githubassets.com/1/calagopus/bot" alt="Calagopus bot support triage" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/calagopus/bot/blob/main/src/ai/decisions.rs">Calagopus bot support triage</a></b><br><sub>calagopus · GitHub · ⭐ 17 repo · 2025-12-28</sub><br>AI support triage in the Rust Discord bot for the Calagopus community that uses Jev to decide whether a message needs an answer at all and whether a drafted answer holds anything worth posting.<br><sub>Also: <a href="https://github.com/calagopus/bot">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/abhegd/status/2102195682257854602"><img src="https://pbs.twimg.com/amplify_video_thumb/2102194961856798720/img/WhzCgL1LVnYAq-R9.jpg" alt="Self-sorting in-app feedback" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/abhegd/status/2102195682257854602">Self-sorting in-app feedback</a></b><br><sub>abhegd · X · ▶ 60 · 2026-09-22</sub><br>Layoutstack demo where typed or spoken (ElevenLabs) in-app feedback is classified by Jev and filed into the right inbox, shipped with a cookbook to remix it with a coding agent.<br><sub>Also: <a href="https://www.layoutstack.com/demo/in-appfeedback">app</a> · <a href="https://layoutstack.com/demo/in-appfeedback">project</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/upasana1105/UP_Demos/blob/main/it-helpdesk-assistant/judgment_base_agent/backends/typesafe.py"><img src="https://opengraph.githubassets.com/1/upasana1105/UP_Demos" alt="IT Helpdesk judgment backend" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/upasana1105/UP_Demos/blob/main/it-helpdesk-assistant/judgment_base_agent/backends/typesafe.py">IT Helpdesk judgment backend</a></b><br><sub>upasana1105 · GitHub · ⭐ 9 repo · 2026-02-02</sub><br>Enterprise IT helpdesk agent demo on the Gemini agent platform with a judgment layer that can run its Choice, Noul and Score primitives on TypeSafe System One.<br><sub>Also: <a href="https://github.com/upasana1105/UP_Demos">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/rszhd/signalscout/blob/dev/packages/engine/src/ai/provider.ts"><img src="https://opengraph.githubassets.com/1/rszhd/signalscout" alt="SignalScout" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/rszhd/signalscout/blob/dev/packages/engine/src/ai/provider.ts">SignalScout</a></b><br><sub>rszhd · GitHub · ⭐ 8 repo · 2026-09-08</sub><br>Open-source intent monitoring that searches Reddit, X, LinkedIn, YouTube, TikTok and Instagram for people describing a problem your product solves and scores each conversation for fit and buyer intent.<br><sub><b>How it uses Jev:</b> The AI SDK TypeSafe provider supplies an evaluation model (jev-latest, $0.042 per million input tokens) for the scoring questions.</sub><br><sub>Also: <a href="https://github.com/rszhd/signalscout">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/sumitrevolt/leadgenrationaivoiceagent/blob/main/app/platform/typesafe_integration.py"><img src="https://opengraph.githubassets.com/1/sumitrevolt/leadgenrationaivoiceagent" alt="LeadGen AI TypeSafe integration" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/sumitrevolt/leadgenrationaivoiceagent/blob/main/app/platform/typesafe_integration.py">LeadGen AI TypeSafe integration</a></b><br><sub>sumitrevolt · GitHub · ⭐ 1 repo · 2026-09-17</sub><br>Experimental Jev layer in LeadGen AI, a marketing and voice-calling SaaS for small Indian businesses, that picks specialization labels for agent roles and validates worker outputs such as cold emails.<br><sub>Also: <a href="https://github.com/sumitrevolt/leadgenrationaivoiceagent">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/promptgtm-shared/clay-jev-people-ranker"><img src="https://opengraph.githubassets.com/1/promptgtm-shared/clay-jev-people-ranker" alt="clay-jev-people-ranker" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/promptgtm-shared/clay-jev-people-ranker">clay-jev-people-ranker</a></b><br><sub>promptgtm-shared · GitHub · 2026-09-21</sub><br>Agent skill and Python workflow that pulls people from Clay CLI with deterministic filters, then has Jev judge whether each person really fits the target role, such as current operating founders, before enrichment.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/minghanminghan/jev-demo"><img src="https://opengraph.githubassets.com/1/minghanminghan/jev-demo" alt="jev demo" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/minghanminghan/jev-demo">jev demo</a></b><br><sub>minghanminghan · GitHub · 2026-09-17</sub><br>Customer-service chatbot routed by Jev that asks every level of its routing tree in one call per turn and hands off to a human on request, frustration or low confidence.<br><sub><b>How it uses Jev:</b> Speculative fan-out over all tree levels plus a wants-human Noul and a frustration Score in the same request.</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://www.reddit.com/r/SaaS/comments/1wlcpq3/jev_is_insane_for_outbound/"><img src="https://external-preview.redd.it/MDV4czc2Z3JibnFoMWrhC3ZnxXXVSY4h_1Pyuu4bCsFhZrPnFj7vZea_6f45.png?format=pjpg&amp;auto=webp&amp;s=92f8c2805fba08f7d164b31a7d9ed7cb61b0c450" alt="Jev outbound lead triage" width="240"></a></td>
<td valign="top"><b><a href="https://www.reddit.com/r/SaaS/comments/1wlcpq3/jev_is_insane_for_outbound/">Jev outbound lead triage</a></b><br><sub>adgrow · Reddit · 2026-09-20</sub><br>Outbound experiment where Jev made 7,068 decisions on 462 leads in 47 seconds for about $0.06, choosing hook, angle, and CTA and skipping 190 leads not worth emailing.<br><sub><b>How it uses Jev:</b> ICP-fit and signal Nouls per lead, plus Choices over hooks and among four drafted messages.</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://treg.to/jev"><img src="https://treg.to/media/og.png" alt="Jev recipes on Treg" width="240"></a></td>
<td valign="top"><b><a href="https://treg.to/jev">Jev recipes on Treg</a></b><br><sub>Treg (superdesigndev) · App</sub><br>Interactive guide to Jev with a live LLM-versus-Jev race and copyable GTM automation recipes built on Treg, such as signup fraud screening, buying-signal triage, and viral content monitoring.<br><sub>Also: <a href="https://github.com/superdesigndev/treg">repo</a> · <a href="https://x.com/jasonzhou1993/status/2101988970565603489">demo</a> · <a href="https://github.com/superdesigndev/treg">project</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/EtienneLescot/jev-router"><img src="https://raw.githubusercontent.com/EtienneLescot/jev-router/main/screenshot.png" alt="Jev Router Demo" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/EtienneLescot/jev-router">Jev Router Demo</a></b><br><sub>EtienneLescot · GitHub · 2026-09-18</sub><br>Browser demo where two Jev calls triage a support ticket (department, urgency, frustration) and size the task, and plain code routes it to an agent or a human and picks the model tier and reasoning depth.<br><sub>Also: <a href="https://etiennelescot.github.io/jev-router/">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/ndolinschi/lanebreak"><img src="https://opengraph.githubassets.com/1/ndolinschi/lanebreak" alt="LaneBreak" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/ndolinschi/lanebreak">LaneBreak</a></b><br><sub>ndolinschi · GitHub · 2026-09-17</sub><br>Support-ticket router that picks the owning team and priority, and flags refund intent, churn risk and tickets that should skip bots for a human.<br><sub>Also: <a href="https://lanebreak.vercel.app">app</a> · <a href="https://lanebreak.vercel.app">app 2</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://openrouter.ai/labs/jev/triage"><img src="https://openrouter.ai/dynamic-og?title=Support+message+triage&amp;description=Classify+support+messages+with+structured+decisions.&amp;v=2" alt="Support message triage" width="240"></a></td>
<td valign="top"><b><a href="https://openrouter.ai/labs/jev/triage">Support message triage</a></b><br><sub>OpenRouter · App</sub><br>OpenRouter Labs recipe that asks Jev five yes-or-no questions about each of 95 support messages (refund, angry, bug, needs a person) and races it against a chat model: 475 answers in 1.2 s for $0.0014 a run.<br><sub><b>How it uses Jev:</b> Five Nouls per message, batched in one run.</sub><br><sub>Also: <a href="https://openrouter.ai/typesafe/jev">model</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/brandonbryant12/transcript-scorecard"><img src="https://opengraph.githubassets.com/1/brandonbryant12/transcript-scorecard" alt="Transcript Scorecard" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/brandonbryant12/transcript-scorecard">Transcript Scorecard</a></b><br><sub>brandonbryant12 · GitHub · 2026-09-16</sub><br>Proof of concept that replays a support call turn by turn and re-scores it against a weighted employee scorecard with a live evaluation per new turn, persisting evidence, confidence and score history in SQLite.</td>
</tr>
</table>

Missing something? [Suggest a resource](https://github.com/Li-Evan/awesome-jev/issues/new/choose).
