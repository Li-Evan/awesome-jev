# 📚 Learn: Techniques and Analysis

**English** · [简体中文](https://github.com/Li-Evan/awesome-jev/blob/main/zh-CN/pages/learn-techniques.md)

Official docs and cookbooks, plus the best guides, analyses, benchmarks, and talks from the community. 102 entries, ranked by community traction.

[← Back to Awesome Jev](https://github.com/Li-Evan/awesome-jev#techniques-and-analysis)

[Official Docs](https://github.com/Li-Evan/awesome-jev/blob/main/pages/learn-official-docs.md) (15) · [Official SDKs and Tools](https://github.com/Li-Evan/awesome-jev/blob/main/pages/learn-official-tools.md) (3) · [Announcements](https://github.com/Li-Evan/awesome-jev/blob/main/pages/learn-announcements.md) (2) · [Patterns](https://github.com/Li-Evan/awesome-jev/blob/main/pages/learn-patterns.md) (4) · [Official Cookbooks](https://github.com/Li-Evan/awesome-jev/blob/main/pages/learn-cookbooks.md) (18) · [Examples and Skills](https://github.com/Li-Evan/awesome-jev/blob/main/pages/learn-examples.md) (74) · [Guides](https://github.com/Li-Evan/awesome-jev/blob/main/pages/learn-guides.md) (76) · **Techniques and Analysis** · [Benchmarks and Case Studies](https://github.com/Li-Evan/awesome-jev/blob/main/pages/learn-benchmarks.md) (173) · [Talks and Videos](https://github.com/Li-Evan/awesome-jev/blob/main/pages/learn-videos.md) (178) · [Discussions](https://github.com/Li-Evan/awesome-jev/blob/main/pages/learn-discussions.md) (20)

<table>
<tr>
<td width="260" valign="top"><a href="https://x.com/CompleteSkeptic/status/2099925682726002904"><img src="https://pbs.twimg.com/amplify_video_thumb/2099925575637057536/img/l4J_ZhkaxAe8FJXv.jpg" alt="Jev launch thread" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/CompleteSkeptic/status/2099925682726002904">Jev launch thread</a></b><br><sub>CompleteSkeptic · Hacker News · ♥ 75k · 2026-09-15</sub><br>Founder Diogo Almeida's launch thread introducing Jev and the RLCD training method, claiming 20-200x faster and 40-400x cheaper decisions than frontier chat models.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/akshay_pachaar/status/2101037514945597645"><img src="https://pbs.twimg.com/media/HShfvSbaMAAZt9E.png" alt="Jev Clearly Explained" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/akshay_pachaar/status/2101037514945597645">Jev Clearly Explained</a></b><br><sub>akshay_pachaar · Article · ♥ 5k · 2026-09-18</sub><br>X article explaining Jev as a millisecond decision layer: how typed questions replace generate-parse-retry LLM calls, and where it sits next to an LLM in an application.</td>
</tr>
<tr>
<td width="260" valign="top"></td>
<td valign="top"><b><a href="https://x.com/NathanFlurry/status/2100036101809619314">Jev as a smart switch statement</a></b><br><sub>NathanFlurry · X · ♥ 7.5k · 2026-09-16</sub><br>Hype-free explainer arguing Jev is a very smart switch statement: it classifies, routes, scores and verifies over predefined options but cannot write code or text.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/k_grajeda/status/2099952715430596710"><img src="https://pbs.twimg.com/media/HSSGbsVXAAEi9jw.png?name=orig" alt="LLM vs Jev at prompt difficulty" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/k_grajeda/status/2099952715430596710">LLM vs Jev at prompt difficulty</a></b><br><sub>k_grajeda · X · ♥ 5.7k · 2026-09-15</sub><br>Simplified side-by-side showing how an LLM and Jev classify a prompt's difficulty: token-by-token text versus probabilities for every option computed in parallel.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/0xSuman/status/2100030221189874015"><img src="https://pbs.twimg.com/media/HSTOW1GagAA0xlK.jpg?name=orig" alt="Generating text with Jev" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/0xSuman/status/2100030221189874015">Generating text with Jev</a></b><br><sub>0xSuman · X · ♥ 4.2k · 2026-09-16</sub><br>Hack that makes Jev write text by asking one Choice question per character position, with a STOP option, and reading off the most likely letters.<br><sub><b>How it uses Jev:</b> One Choice per character over the alphabet plus STOP.</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/NielsRogge/status/2100239244501430438"><img src="https://pbs.twimg.com/media/HSWLYi3WcAAOPBs.jpg?name=orig" alt="How Jev-style decoding works" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/NielsRogge/status/2100239244501430438">How Jev-style decoding works</a></b><br><sub>NielsRogge · X · ♥ 3.8k · 2026-09-16</sub><br>Visual explanation, based on the open Qwen2.5-RLCD model, of reading field probabilities from a cached single decoder pass instead of generating JSON token by token.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/theo/status/2100762304862384257"><img src="https://pbs.twimg.com/amplify_video_thumb/2100694537672998912/img/OF8vottg6-45ZgNl.jpg" alt="Critique of Jev compaction" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/theo/status/2100762304862384257">Critique of Jev compaction</a></b><br><sub>theo · X · ♥ 2.6k · 2026-09-18</sub><br>Critique arguing per-tool-call filtering with Jev is a poor compaction strategy, since compaction should reconstruct history and the model lacks context on what came before.<br><sub>Also: <a href="https://github.com/tamaratran/fast-jev-compaction">related</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"></td>
<td valign="top"><b><a href="https://x.com/MichaelLee04/status/2100003037150683593">Jev as a decision primitive</a></b><br><sub>MichaelLee04 · X · ♥ 3.1k · 2026-09-15</sub><br>Notes from ~5,000 requests (about $2) on classification, routing and intent: p50 ~150ms and p95 ~350ms make per-turn checks viable, and Jev rewards splitting queries into independent questions.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/akshay_pachaar/status/2101309986156712025"><img src="https://pbs.twimg.com/amplify_video_thumb/2101309969044054016/img/33Ud7QFDU8aMgYlW.jpg" alt="LLMs vs. Jev, clearly explained" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/akshay_pachaar/status/2101309986156712025">LLMs vs. Jev, clearly explained</a></b><br><sub>akshay_pachaar · X · ♥ 2.9k · 2026-09-19</sub><br>Explains that Jev does not generate faster, it does not generate at all: independent Choice, Score and Noul questions, like urgency, owning team and command risk for a failed deploy, are evaluated in parallel.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/servasyy_ai/status/2101132667056185544"><img src="https://pbs.twimg.com/media/HSi3JD0bcAEhil0.jpg" alt="What Jev can really do" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/servasyy_ai/status/2101132667056185544">What Jev can really do</a></b><br><sub>servasyy_ai · Article · ♥ 779 · 2026-09-19</sub><br>Chinese-language reality check on Jev that explains what it is and is not, sorts demos that actually work by use case, and lays out the caveats behind the speed and accuracy claims.</td>
</tr>
<tr>
<td width="260" valign="top"></td>
<td valign="top"><b><a href="https://x.com/paarangatrai/status/2100113737097367896">LLMs generate, Jev decides</a></b><br><sub>paarangatrai · X · ♥ 2.3k · 2026-09-16</sub><br>Explainer using a risky-account example: instead of prompting an LLM for a verdict, you declare risk levels and a manual-review flag up front and get back probabilities such as risk = high (96%).</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/gregisenberg/status/2101018750916948237"><img src="https://pbs.twimg.com/amplify_video_thumb/2101018301409202176/img/HP2Ycx2G3KjqvxJw.jpg" alt="Businesses Jev unlocks" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/gregisenberg/status/2101018750916948237">Businesses Jev unlocks</a></b><br><sub>gregisenberg · X · ♥ 1.5k · 2026-09-18</sub><br>Plain-language explanation of Jev as a sorter (1,700 emails for 18 cents) plus startup ideas built on putting it at the front of expensive queues, such as instant quotes and lead scoring.<br><sub>Also: <a href="https://www.youtube.com/watch?v=4mTLpuQpB80">video</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"></td>
<td valign="top"><b><a href="https://x.com/swill1ams/status/2100421326389354624">Custom Jev-style models for existing workflows</a></b><br><sub>swill1ams · X · ♥ 1.4k · 2026-09-17</sub><br>Thread arguing that companies can put a cheap parallel-constrained-decoding classifier, trained on past decisions, in front of the LLM review steps they already run, letting confident items pass and sending the rest on.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/0xMovez/status/2102049863449858053"><img src="https://pbs.twimg.com/media/HSv6c7rXwAAOMVI.jpg?name=orig" alt="Jev Harness blueprint summary" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/0xMovez/status/2102049863449858053">Jev Harness blueprint summary</a></b><br><sub>0xMovez · X · ♥ 1.3k · 2026-09-21</sub><br>Thread summarizing a 12-page TypeSafe PDF on a Jev harness for coding agents, e.g. Opus to Sonnet to Opus hand-offs costing 6.19 vs 4.15 for pure Opus, and reading and search taking 56.2% of tool turns.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://tech.layerx.co.jp/entry/2026/09/18/185816"><img src="https://cdn.image.st-hatena.com/image/scale/5ed4f6e73205d082af7a8a0518536c4ad98d0eb3/backend=imagemagick;version=1;width=1300/https%3A%2F%2Fcdn-ak.f.st-hatena.com%2Fimages%2Ffotolife%2Fy%2Fyuu2634%2F20260918%2F20260918191032.png" alt="LayerX internal Jev study session" width="240"></a></td>
<td valign="top"><b><a href="https://tech.layerx.co.jp/entry/2026/09/18/185816">LayerX internal Jev study session</a></b><br><sub>LayerX (pon) · Article · ♥ 959 · 2026-09-18</sub><br>Japanese write-up of a 30-minute internal study session on Jev at LayerX that drew more than 50 engineers and produced more than 50 ideas for building it into their products.<br><sub>Also: <a href="https://x.com/hatebu100/status/2101094920778129466">x</a> · <a href="https://x.com/LayerX_tech/status/2100887864594895154">demo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/ryanvogel/status/2100218045549412499"><img src="https://pbs.twimg.com/amplify_video_thumb/2100217973000617984/img/AFareJummI08B_QB.jpg" alt="An LLM from a classifier" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/ryanvogel/status/2100218045549412499">An LLM from a classifier</a></b><br><sub>ryanvogel · X · ♥ 889 · 2026-09-16</sub><br>Builds an autoregressive text generator out of Jev: 29 yes/no questions per character pick the next key (a-z, space, comma, period), and the text is fed back in to repeat.<br><sub><b>How it uses Jev:</b> 29 Noul questions per character; the highest-probability key is appended.</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/omarsar0/status/2100693601021997193"><img src="https://pbs.twimg.com/media/HScpisJbEAAMxZb.jpg?name=orig" alt="Things to try with Jev" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/omarsar0/status/2100693601021997193">Things to try with Jev</a></b><br><sub>omarsar0 · X · ♥ 679 · 2026-09-17</sub><br>Practitioner list of promising Jev uses: LLM-as-a-judge evals, routing in agent harnesses, subagent creation, and dynamic harness generation, with the author using it as a router for a meta harness.</td>
</tr>
<tr>
<td width="260" valign="top"></td>
<td valign="top"><b><a href="https://x.com/da_fant/status/2100659471257366766">How Jev makes agents cheaper</a></b><br><sub>da_fant · X · ♥ 634 · 2026-09-17</sub><br>Thread listing where Jev speeds agents up, from model routing, computer use and action-safety review to deciding whether each event should wake an expensive orchestrator, go to a subagent, or be queued.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/anderslie/status/2100388704644919662"><img src="https://pbs.twimg.com/amplify_video_thumb/2100384704868601856/img/TSBG-jeFfuLlRSOS.jpg" alt="Jev-like API on open weights" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/anderslie/status/2100388704644919662">Jev-like API on open weights</a></b><br><sub>anderslie · X · ♥ 567 · 2026-09-17</sub><br>Explains how Jev-style speed can come from inference: prefill shared state once, fork the context per question, and read logits constrained to choice labels on any open-weight LLM.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/trycua/status/2101437979180904640"><img src="https://pbs.twimg.com/media/HSnHzhdWoAEwmrh.jpg" alt="Jev and the future of computer use" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/trycua/status/2101437979180904640">Jev and the future of computer use</a></b><br><sub>trycua · Article · ♥ 559 · 2026-09-19</sub><br>Cua's deep dive on which decisions inside a computer-use agent need a general LLM, turning screens into scored candidate actions for text-only decision models like Jev and their CUA-S1-FORMS.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/mvanhorn/status/2100788572316139655"><img src="https://pbs.twimg.com/media/HSdxN5LbUAAMq_w.png" alt="WTF is Jev" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/mvanhorn/status/2100788572316139655">WTF is Jev</a></b><br><sub>mvanhorn · X · ♥ 418 · 2026-09-18</sub><br>Explainer article framing Jev as multiple-choice rather than essay-writing AI, and cataloguing nine patterns developers built with it in the first 72 hours.<br><sub>Also: <a href="https://x.com/i/article/2100772231462961152">article</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://archerhume.com/posts/jevs-architecture-unmasked/"><img src="https://archerhume.com/og-image/jevs-architecture-unmasked.png" alt="Jev&#x27;s Architecture Unmasked" width="240"></a></td>
<td valign="top"><b><a href="https://archerhume.com/posts/jevs-architecture-unmasked/">Jev's Architecture Unmasked</a></b><br><sub>Archer Hume · Article · ♥ 437 · 2026-09-17</sub><br>Architecture teardown that probes Jev with 10,000 API calls to infer how it is built, from shared state with isolated question branches to option interaction and confidence readout.<br><sub>Also: <a href="https://news.ycombinator.com/item?id=49766351">discussion</a> · <a href="https://x.com/iwashi86/status/2100713337436930288">demo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"></td>
<td valign="top"><b><a href="https://x.com/jiayuan_jy/status/2100876273061102006">Skeptical notes after a day with Jev</a></b><br><sub>jiayuan_jy · X · ♥ 339 · 2026-09-18</sub><br>Chinese notes from a day of testing: Jev reads as a faster general classifier that suits bounded, low-latency choices like DOM actions or compaction, but cannot replace parameterized agent tool calls.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/Bewinxed/status/2100519569307640097"><img src="https://pbs.twimg.com/amplify_video_thumb/2100519508943228928/img/Vl5XWMF9MjLBasxD.jpg" alt="Making Jev generate text" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/Bewinxed/status/2100519569307640097">Making Jev generate text</a></b><br><sub>Bewinxed · X · ♥ 320 · 2026-09-17</sub><br>Hack that makes Jev produce text despite being non-generative, managing up to 20 words for $0.5.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/Sumanth_077/status/2101639788961112279"><img src="https://pbs.twimg.com/media/HSqGNyCacAAhUYd.jpg" alt="Jev Clearly Explained" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/Sumanth_077/status/2101639788961112279">Jev Clearly Explained</a></b><br><sub>Sumanth_077 · Article · ♥ 324 · 2026-09-20</sub><br>Explainer on the many small decisions inside an agent run (model choice, risky tool calls, loops, completion) and how Jev answers them with typed probabilities instead of generated text.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/JoshARosen/status/2101645894818857272"><img src="https://pbs.twimg.com/media/HSqLJdJWoAA4aNR.jpg" alt="Jev in the Wild" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/JoshARosen/status/2101645894818857272">Jev in the Wild</a></b><br><sub>JoshARosen · Article · ♥ 182 · 2026-09-20</sub><br>Survey of early architecture patterns in Jev projects, such as model, skill and tool routing, supervisors and security layers, all inserting Jev at one decision point in otherwise conventional software.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/aparnadhinak/status/2100979688072224957"><img src="https://pbs.twimg.com/media/HSgtobXaEAAaDhD.jpg" alt="Will TypeSafe&#x27;s Jev change how we build AI applications?" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/aparnadhinak/status/2100979688072224957">Will TypeSafe's Jev change how we build AI applications?</a></b><br><sub>aparnadhinak · Article · ♥ 197 · 2026-09-18</sub><br>Arize AI analysis of what a decide-only model buys and costs you, with an eye on LLM-as-a-judge evaluations and the architecture choices it implies.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/annabellschfr/status/2100962787094597807"><img src="https://pbs.twimg.com/media/HSgRvklXgAA33Rx.jpg" alt="Jev the savant" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/annabellschfr/status/2100962787094597807">Jev the savant</a></b><br><sub>annabellschfr · Article · ♥ 64 · 2026-09-18</sub><br>Explainer on where Jev fits in pipelines and eval harnesses, walking through Choice, Score and Noul with a worked example that asks three judgments about a finished agent run in one request.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/Kedr_bit/status/2102132700119191832"><img src="https://pbs.twimg.com/media/HSxGi5rWgAAbZhF.jpg?name=orig" alt="Making Jev speak" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/Kedr_bit/status/2102132700119191832">Making Jev speak</a></b><br><sub>Kedr_bit · X · ♥ 151 · 2026-09-21</sub><br>Chat experiment that coaxes Jev into replying in words, producing short, garbled but amusing conversations.</td>
</tr>
<tr>
<td width="260" valign="top"></td>
<td valign="top"><b><a href="https://x.com/DalinHuang/status/2101839381589884965">Where Jev pays off in production</a></b><br><sub>DalinHuang · X · ♥ 27 · 2026-09-21</sub><br>Chinese field notes: swapping Gemini Flash or GPT Luna judgments for Jev cut cost 20 to 60x and latency by an order of magnitude, with a pattern of escalating answers below 80% confidence to a small generative model.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://www.reddit.com/r/LocalLLaMA/comments/1wkd1dz/digitlogitsbased_classifier_with_llamacpp/"><img src="https://external-preview.redd.it/WB3qVqzuW2bIGtkMVrOZ0TihcSnHaV-pareGCkJDiXs.png?auto=webp&amp;s=19b1cd738d385b0222b357df4dc720a2fdb24a88" alt="Digit-logits classifier with llama.cpp" width="240"></a></td>
<td valign="top"><b><a href="https://www.reddit.com/r/LocalLLaMA/comments/1wkd1dz/digitlogitsbased_classifier_with_llamacpp/">Digit-logits classifier with llama.cpp</a></b><br><sub>rhinodevil · Reddit · ▲ 10 · 2026-09-19</sub><br>Technique from the mt_llm library for using a small local LLM as a classifier by reading the logits of digit tokens instead of relying on llama.cpp grammars.<br><sub>Also: <a href="https://github.com/RhinoDevel/mt_llm">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"></td>
<td valign="top"><b><a href="https://news.ycombinator.com/item?id=49791782">Use any LLM like Jev</a></b><br><sub>theanonymousone · Hacker News · ▲ 10 · 2026-09-21</sub><br>Recipe for running any GGUF in llama.cpp with one predicted token and top logprobs to get Jev-style class probabilities, with notes on where calibrated probabilities still differ.<br><sub>Also: <a href="https://www.reddit.com/r/LocalLLaMA/comments/1wlxpaw/you_can_use_any_llm_just_like_jev/">reddit</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://sereja.tech/blog/typesafe-system-one-jev/"><img src="https://sereja.tech/images/blog/typesafe-system-one-jev-general-reader.png" alt="Jev explainer (Russian)" width="240"></a></td>
<td valign="top"><b><a href="https://sereja.tech/blog/typesafe-system-one-jev/">Jev explainer (Russian)</a></b><br><sub>serejaris · Article · ⭐ 25 · 2026-09-17</sub><br>Russian-language blog explainer on TypeSafe's Jev: how a model that picks from given options helps route requests, steer assistant actions and check results, citing the launch post, docs, workflow evals and early third-party tests.<br><sub>Also: <a href="https://github.com/serejaris/sereja.tech/blob/main/content/blog/typesafe-system-one-jev.md">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://anthonymaio.substack.com/p/jev-the-language-model-that-wont"><img src="https://substackcdn.com/image/fetch/$s_!mqdS!,w_1200,h_675,c_fill,f_jpg,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F85790540-64fc-479b-92ea-a0b2baecc21f_1672x941.png" alt="Jev: The Language Model That Won&#x27;t Talk" width="240"></a></td>
<td valign="top"><b><a href="https://anthonymaio.substack.com/p/jev-the-language-model-that-wont">Jev: The Language Model That Won't Talk</a></b><br><sub>Anthony Maio · Article · ♥ 22 · 2026-09-16</sub><br>Essay arguing that Jev's real claim is not price but that generated language may be the wrong interface between a model and the software that must act on its output.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://medium.com/@gemanor/most-people-on-the-internet-miss-what-jev-is-about-ad0a983537d5"><img src="https://miro.medium.com/v2/resize:fit:700/0*m5fn7rELknSeGCVp.png" alt="Most people miss what Jev is about" width="240"></a></td>
<td valign="top"><b><a href="https://medium.com/@gemanor/most-people-on-the-internet-miss-what-jev-is-about-ad0a983537d5">Most people miss what Jev is about</a></b><br><sub>Gabriel L. Manor · Article · ▲ 6 · 2026-09-18</sub><br>Essay arguing that cheap classification is the boring part of Jev, and walking through three harness designs where a typed, confidence-scored System One model sits next to an LLM.<br><sub>Also: <a href="https://news.ycombinator.com/item?id=49754461">discussion</a> · <a href="https://github.com/gemanor/jev-code-review-benchmark">benchmark</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://sgnt.ai/p/jev/"><img src="https://sgnt.ai/jev-at-home.png" alt="You could have built Jev" width="240"></a></td>
<td valign="top"><b><a href="https://sgnt.ai/p/jev/">You could have built Jev</a></b><br><sub>sgnt.ai · Article · ▲ 6 · 2026-09-18</sub><br>Short illustrated explainer arguing Jev is most likely an LLM that returns a single token, with pseudocode and comparisons to other projects that do the same, so you can reason about it from first principles.<br><sub>Also: <a href="https://news.ycombinator.com/item?id=49755430">discussion</a> · <a href="https://x.com/ekzhang1/status/2101117003415105696">x</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://sebastianraschka.com/blog/2026/jev-classification-generalization.html"><img src="https://sebastianraschka.com/images/blog/2026/jev-classification-generalization/jev.png" alt="It&#x27;s easy to dismiss Jev as just a classifier" width="240"></a></td>
<td valign="top"><b><a href="https://sebastianraschka.com/blog/2026/jev-classification-generalization.html">It's easy to dismiss Jev as just a classifier</a></b><br><sub>Sebastian Raschka · Article · ▲ 4 · 2026-09-20</sub><br>Short note on why Jev's generalization matters, with speculation on an encoder-style architecture and training setup, plus Choice and Noul API examples.<br><sub>Also: <a href="https://news.ycombinator.com/item?id=49787418">discussion</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://thefinancialengineer.substack.com/p/typesafes-jev-is-about-to-change"><img src="https://substackcdn.com/image/fetch/$s_!gJGj!,w_1200,h_675,c_fill,f_jpg,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2da657fe-df1c-4bb2-b059-f373a69dec96_1376x768.jpeg" alt="Jev Is About to Change the AI Economy" width="240"></a></td>
<td valign="top"><b><a href="https://thefinancialengineer.substack.com/p/typesafes-jev-is-about-to-change">Jev Is About to Change the AI Economy</a></b><br><sub>Anton Zagrebelny · Article · ▲ 4 · 2026-09-17</sub><br>Essay on how free output tokens and many questions per call break per-token credit metering, and where metering and entitlement enforcement should live once Jev sits beside LLMs.<br><sub>Also: <a href="https://news.ycombinator.com/item?id=49747584">discussion</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"></td>
<td valign="top"><b><a href="https://rajveerbachkaniwala.com/blog/2026/09/19/jev-is-to-tool-use-what-rag-is-to-context/">Jev is to tool use what RAG is to context</a></b><br><sub>Rajveer Bachkaniwala · Article · ▲ 4 · 2026-09-19</sub><br>Short essay framing Jev as the mirror image of RAG: the developer fixes up front which options, including tools, the model may pick, instead of which context it reads.<br><sub>Also: <a href="https://news.ycombinator.com/item?id=49770295">discussion</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://inlevel9.com/en/issues/jev-judgment-not-writing"><img src="https://inlevel9.com/api/og/en/jev-judgment-not-writing?v=6-inlevel9-5" alt="Jev can&#x27;t write a line, but 13% of paid teams use it" width="240"></a></td>
<td valign="top"><b><a href="https://inlevel9.com/en/issues/jev-judgment-not-writing">Jev can't write a line, but 13% of paid teams use it</a></b><br><sub>Oswarld (Kwangseob Ahn) · Article · ▲ 3 · 2026-09-21</sub><br>Newsletter essay on what pricing 'judgment' instead of text reveals about Jev, and why the author is building a model that does only five things.<br><sub>Also: <a href="https://news.ycombinator.com/item?id=49784782">discussion</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"></td>
<td valign="top"><b><a href="https://typesafe.ai/blog/bitterest-lesson">The Bitterest Lesson</a></b><br><sub>TypeSafe AI · Article · ▲ 3 · 2026-09-10</sub><br>Official essay extending Sutton's bitter lesson: choosing the right task to optimize matters more than data, which matters more than compute and algorithms.<br><sub>Also: <a href="https://news.ycombinator.com/item?id=49749834">discussion</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://www.seangoedecke.com/two-techniques-for-working-with-system-one-models/"><img src="https://www.seangoedecke.com/static/70f6abb1474ff212395a43c8a17194f8/fcda8/turns.png" alt="Two techniques for working with System One models" width="240"></a></td>
<td valign="top"><b><a href="https://www.seangoedecke.com/two-techniques-for-working-with-system-one-models/">Two techniques for working with System One models</a></b><br><sub>Sean Goedecke · Article · ▲ 3 · 2026-09-18</sub><br>Layered goals, where a slow loop picks the goal and a fast loop picks actions, plus tournament sampling over batches of options, shown on a Doom agent built with an open-model imitation.<br><sub>Also: <a href="https://news.ycombinator.com/item?id=49755005">discussion</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://stackness.dev/blog/what-is-a-system-one-model-and-where-does-it-go-in-your-stack"><img src="https://cdn.stackness.dev/images/1/1765c1b4-9761-43cb-8c5a-ea646ad17ad2.png" alt="Where a System One model goes in your stack" width="240"></a></td>
<td valign="top"><b><a href="https://stackness.dev/blog/what-is-a-system-one-model-and-where-does-it-go-in-your-stack">Where a System One model goes in your stack</a></b><br><sub>Sergei Gordeichuk · Article · ▲ 3 · 2026-09-18</sub><br>Argues a System One model is a new slot beside the LLM rather than a replacement, separating what TypeSafe has demonstrated from what it has only asserted, and what must be true before adopting it.<br><sub>Also: <a href="https://news.ycombinator.com/item?id=49760138">discussion</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/erik-dunteman/ChatJev"><img src="https://opengraph.githubassets.com/1/erik-dunteman/ChatJev" alt="ChatJev" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/erik-dunteman/ChatJev">ChatJev</a></b><br><sub>erik-dunteman · GitHub · ⭐ 7 · 2026-09-20</sub><br>Small experiment that puts Jev in an autoregressive loop, offering candidate next tokens as Choice options to make the non-generative model produce text one token at a time.</td>
</tr>
<tr>
<td width="260" valign="top"></td>
<td valign="top"><b><a href="https://navinpai.github.io/decoding-jev/">Decoding Jev</a></b><br><sub>Navin Pai · Article · ▲ 2</sub><br>Visual technical deep dive into how Jev likely differs from an LLM: transformer inference that reads typed probabilities directly, proper scoring rules, policy gradients, and what RLCD changes.<br><sub>Also: <a href="https://news.ycombinator.com/item?id=49776494">discussion</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://bernoulli.app/articles/is-jev-confident"><img src="https://bernoulli.app/og-confidence.png" alt="Is Jev confident?" width="240"></a></td>
<td valign="top"><b><a href="https://bernoulli.app/articles/is-jev-confident">Is Jev confident?</a></b><br><sub>Stanislav Yurin · Article · ▲ 2 · 2026-09-18</sub><br>Reverse-engineers how Choice confidence is computed from hundreds of thousands of live answers and shows how padding the option list inflates it.<br><sub>Also: <a href="https://news.ycombinator.com/item?id=49765813">discussion</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"></td>
<td valign="top"><b><a href="https://blog.nimendra.xyz/blog/jev-decision-layer-for-production-ai/">Jev is the missing piece in production AI systems</a></b><br><sub>Nimendra · Article · ▲ 2 · 2026-09-17</sub><br>Walks through a 2 AM production incident to show Jev as a bounded decision layer that picks the owning team, urgency, and whether to auto-act before an incident agent or LLM starts reasoning.<br><sub>Also: <a href="https://news.ycombinator.com/item?id=49737892">discussion</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://patmcguinness.substack.com/p/jev-makes-fast-and-cheap-decisions"><img src="https://substackcdn.com/image/fetch/$s_!3sHt!,w_1200,h_675,c_fill,f_jpg,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb92400f8-6f41-44c7-9233-a2449f4c413e_936x537.png" alt="Jev makes fast and cheap decisions" width="240"></a></td>
<td valign="top"><b><a href="https://patmcguinness.substack.com/p/jev-makes-fast-and-cheap-decisions">Jev makes fast and cheap decisions</a></b><br><sub>Patrick McGuinness · Article · ♥ 6 · 2026-09-18</sub><br>Newsletter analysis framing Jev as a classifier-style production model rather than a general model, covering its design and early community builds such as a self-driving simulator and open rebuilds.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/y0usaf/jev-lm"><img src="https://opengraph.githubassets.com/1/y0usaf/jev-lm" alt="jev-lm" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/y0usaf/jev-lm">jev-lm</a></b><br><sub>y0usaf · GitHub · ⭐ 5 · 2026-09-16</sub><br>Word-level language model that uses Jev as its output layer, with an n-gram drafter and Noul chunk verification; on held-out text Jev scored 6.92 bits/token against 6.18 for a unigram table.<br><sub><b>How it uses Jev:</b> A 229-option next-word Choice plus a done Noul per round trip, about 0.25 s median.</sub></td>
</tr>
<tr>
<td width="260" valign="top"></td>
<td valign="top"><b><a href="https://x.com/sermakarevich/status/2101374291640213785">State-tone sensitivity test</a></b><br><sub>sermakarevich · X · ♥ 4 · 2026-09-19</sub><br>Shows Jev's answers depend heavily on the tone of the state: the same question about Python type annotations dropped from 0.97 to 0.07 confidence with a team-dislikes-them state.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Siddhant-K-code/distill/tree/main/research/context-is-a-build-artifact"><img src="https://opengraph.githubassets.com/1/Siddhant-K-code/distill" alt="Context Is a Build Artifact" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Siddhant-K-code/distill/tree/main/research/context-is-a-build-artifact">Context Is a Build Artifact</a></b><br><sub>Siddhant-K-code · GitHub · ⭐ 180 repo · 2025-12-31</sub><br>Preregistered study design, with an offline pilot harness and TypeSafe adapter, testing whether byte-stable context compilation improves Jev decision consistency, calibration and cost.<br><sub>Also: <a href="https://github.com/Siddhant-K-code/distill">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://stacktoheap.com/blog/2026/09/21/the-state-machine-is-the-agent/"><img src="https://stacktoheap.com/images/jev-state-machine-hero.png" alt="Jev at the branches" width="240"></a></td>
<td valign="top"><b><a href="https://stacktoheap.com/blog/2026/09/21/the-state-machine-is-the-agent/">Jev at the branches</a></b><br><sub>StackToHeap · Article · ▲ 1 · 2026-09-21</sub><br>A state machine owns the plan and the legal transitions while Jev only chooses among open branches, with stricter margins on risky moves.<br><sub>Also: <a href="https://news.ycombinator.com/item?id=49784636">discussion</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/adhyaay-karnwal/jev-chat"><img src="https://opengraph.githubassets.com/1/adhyaay-karnwal/jev-chat" alt="jev-chat" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/adhyaay-karnwal/jev-chat">jev-chat</a></b><br><sub>adhyaay-karnwal · GitHub · ⭐ 3 · 2026-09-17</sub><br>Research decoder that builds a chatbot from Jev Choices over a hierarchical codebook of phrases and words, with a paper comparing stepwise decoding against selecting a complete reply.<br><sub><b>How it uses Jev:</b> Speculative fan-out asks for the next unit and hypothetical follow-ups in one state; naive autoregression loops, while selection stays grammatical.</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/cookiespiggy/agentic-rl/blob/main/25-%E5%88%A4%E5%88%AB%E8%83%BD%E5%8A%9B%E5%A4%96%E7%BD%AE-%E4%BB%80%E4%B9%88%E6%97%B6%E5%80%99%E4%B8%8D%E8%AF%A5%E7%94%A8RL.md"><img src="https://raw.githubusercontent.com/cookiespiggy/agentic-rl/main/assets/25-01-playground-overview.png" alt="When not to use RL after Jev" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/cookiespiggy/agentic-rl/blob/main/25-%E5%88%A4%E5%88%AB%E8%83%BD%E5%8A%9B%E5%A4%96%E7%BD%AE-%E4%BB%80%E4%B9%88%E6%97%B6%E5%80%99%E4%B8%8D%E8%AF%A5%E7%94%A8RL.md">When not to use RL after Jev</a></b><br><sub>cookiespiggy · GitHub · ⭐ 107 repo · 2026-06-03</sub><br>Chapter of a Chinese agentic RL tutorial arguing that discriminative tasks can be outsourced to Jev while policy tasks still need RL, with gradient sweeps measuring its resolution.<br><sub>Also: <a href="https://github.com/cookiespiggy/agentic-rl">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"></td>
<td valign="top"><b><a href="https://x.com/hhkkmon/status/2100443314957038010">System 1 and System 2 agents thread</a></b><br><sub>hhkkmon · X · ♥ 2 · 2026-09-17</sub><br>Explainer thread arguing many agent LLM calls are "expensive if statements", proposing a System 1 layer for routing, judging and guardrails, and listing open Jev-like recreations.</td>
</tr>
<tr>
<td width="260" valign="top"></td>
<td valign="top"><b><a href="https://jev.kuhung.me">Understanding Jev</a></b><br><sub>kuhung · Article · ⭐ 2 · 2026-09-18</sub><br>Bilingual Chinese-English long-form essay on Jev's one-step decisions, with local tests, failure modes and production limits, plus a micro-decision demo.<br><sub>Also: <a href="https://github.com/kuhung/understanding-jev">repo</a> · <a href="https://askjev.kuhung.me">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/BENZEMA_zzzzzz/status/2102068540530638964"><img src="https://pbs.twimg.com/media/HSwMMToacAAsAh3.jpg?name=orig" alt="Review of public Jev trading repos" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/BENZEMA_zzzzzz/status/2102068540530638964">Review of public Jev trading repos</a></b><br><sub>BENZEMA_zzzzzz · X · ▶ 57 · 2026-09-21</sub><br>Thread reviewing three public Jev trading repos that trade short BTC windows on Kalshi or Polymarket, finding useful code but no independently verifiable trading edge.</td>
</tr>
<tr>
<td width="260" valign="top"></td>
<td valign="top"><b><a href="https://x.com/theanandprasad/status/2102199067057307900">Jev-like decisions from open LLMs</a></b><br><sub>theanandprasad · X · ▶ 49 · 2026-09-22</sub><br>Thread explaining how to get Jev-style fast decisions from a cheap open-source LLM without training, by ending the prompt at "Answer:" and comparing the logits of the allowed answer tokens.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/ranjankumar/status/2101953564834934999"><img src="https://pbs.twimg.com/tweet_video_thumb/HSujm_1bMAAdo_K.jpg" alt="Where Jev belongs in an agent harness" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/ranjankumar/status/2101953564834934999">Where Jev belongs in an agent harness</a></b><br><sub>ranjankumar · X · ▶ 47 · 2026-09-21</sub><br>Argues that Jev's ordering can be trusted but its confidence numbers cannot, so routing and ranking can use it directly while threshold gates such as approving a transfer need calibration first.<br><sub>Also: <a href="https://ranjankumar.in/jev-system-one-model-agent-harness-placement">article</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/ZataZhang/ZataTree/tree/hugo/content/post/DeepLearning/models_and_strategies/Jev：不写字的决策模型，和它真正适合解决的问题"><img src="https://opengraph.githubassets.com/1/ZataZhang/ZataTree" alt="Jev: the decision model that does not write" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/ZataZhang/ZataTree/tree/hugo/content/post/DeepLearning/models_and_strategies/Jev：不写字的决策模型，和它真正适合解决的问题">Jev: the decision model that does not write</a></b><br><sub>ZataZhang · Article · ⭐ 8 repo · 2026-09-20</sub><br>Chinese long-form explainer on a personal knowledge blog covering where the Jev and System One names come from, how its typed outputs differ from LLM generation, and which problems it actually fits.<br><sub>Also: <a href="https://github.com/ZataZhang/ZataTree">repo</a> · <a href="https://www.zata.cc/">site</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/shimo4228/contemplative-agent/blob/main/rfcs/0040-jev-system-one-local-decision-backend.md"><img src="https://opengraph.githubassets.com/1/shimo4228/contemplative-agent" alt="Jev as a local decision backend (RFC)" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/shimo4228/contemplative-agent/blob/main/rfcs/0040-jev-system-one-local-decision-backend.md">Jev as a local decision backend (RFC)</a></b><br><sub>shimo4228 · GitHub · ⭐ 6 repo · 2026-03-08</sub><br>RFC and operator-run eval arm in the Contemplative Agent project on moving its judgment-only LLM calls to Jev or local Jev-like models, keeping Jev numbers out of the public tree under TypeSafe's customer agreement.<br><sub>Also: <a href="https://github.com/shimo4228/contemplative-agent">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/0xthe0/status/2102213100174741995"><img src="https://pbs.twimg.com/media/HSrq8uWXoAAQ7FF.jpg" alt="Jev pruning is not memory" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/0xthe0/status/2102213100174741995">Jev pruning is not memory</a></b><br><sub>0xthe0 · X · ▶ 24 · 2026-09-22</sub><br>Critique of Jev-based context compaction for Claude Code: pruning a 1M-token session to 86K in a second is scoring and deleting, and one replay dropped 16 fragments that were needed later.<br><sub>Also: <a href="https://x.com/0xthe0/status/2101751238509400153">article</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"></td>
<td valign="top"><b><a href="https://typesafe.ai/blog/ai-too-good-to-be-true-too-bad-to-be-useful-typesafe-ai">AI: too good to be true, too bad to be useful</a></b><br><sub>TypeSafe AI · Article · 2026-06-19</sub><br>Official post with Diogo Almeida's AI Council talk arguing that preference-optimized chat models are the wrong fit for automation and making the case for decision models.<br><sub>Also: <a href="https://www.youtube.com/watch?v=o-y1HJ6buGQ">video</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://qiita.com/GeneLab_999/items/116aa006fbf93b68d791"><img src="https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-user-contents.imgix.net%2Fhttps%253A%252F%252Fcdn.qiita.com%252Fassets%252Fpublic%252Farticle-ogp-background-afbab5eb44e0b055cce1258705637a91.png%3Fixlib%3Drb-4.1.1%26w%3D1200%26blend64%3DaHR0cHM6Ly9xaWl0YS11c2VyLXByb2ZpbGUtaW1hZ2VzLmltZ2l4Lm5ldC9odHRwcyUzQSUyRiUyRnFpaXRhLWltYWdlLXN0b3JlLnMzLmFwLW5vcnRoZWFzdC0xLmFtYXpvbmF3cy5jb20lMkYwJTJGMzkwODk4MSUyRnByb2ZpbGUtaW1hZ2VzJTJGMTc4NzU1NDY5OD9peGxpYj1yYi00LjEuMSZhcj0xJTNBMSZmaXQ9Y3JvcCZtYXNrPWVsbGlwc2UmYmc9RkZGRkZGJmZtPXBuZzMyJnM9OGVkMDdmYzA3YzdlYmNlNzQ2YTA3MGFhY2ViYzNlZjk%26blend-x%3D120%26blend-y%3D467%26blend-w%3D82%26blend-h%3D82%26blend-mode%3Dnormal%26s%3D74b1732623ee7ae4a142be36aba01640?ixlib=rb-4.1.1&amp;w=1200&amp;fm=jpg&amp;mark64=aHR0cHM6Ly9xaWl0YS11c2VyLWNvbnRlbnRzLmltZ2l4Lm5ldC9-dGV4dD9peGxpYj1yYi00LjEuMSZ3PTk2MCZoPTMyNCZ0eHQ9SmV2JUUzJTgxJUEzJUUzJTgxJUE2JUUzJTgxJUFBJUUzJTgyJTkzJUUzJTgxJUEwJUVGJUJDJTlGJTIwJUUyJTgwJTk0JTIwJUU2JTk2JTg3JUU3JUFCJUEwJUUzJTgyJTkyJUU2JTlCJUI4JUUzJTgxJThCJUUzJTgxJUFBJUUzJTgxJTg0QUklRTMlODElQUIlRTMlODAlODFMTE0lRTMlODElQUVpZiVFNiU5NiU4NyVFNSU4OCVBNCVFNSVBRSU5QSVFMyU4MiU5MiVFNCVCQiVCQiVFMyU4MSU5QiVFMyU4MiU4OSVFMyU4MiU4QyVFMyU4MiU4QiVFMyU4MSU4QiZ0eHQtYWxpZ249bGVmdCUyQ3RvcCZ0eHQtY29sb3I9JTIzMUUyMTIxJnR4dC1mb250PUhpcmFnaW5vJTIwU2FucyUyMFc2JnR4dC1zaXplPTU2JnR4dC1wYWQ9MCZzPWFjNTdiZDkzMzEwYTBjNzI2MzU2NTNlZDQ3NDYzMjI3&amp;mark-x=120&amp;mark-y=112&amp;blend64=aHR0cHM6Ly9xaWl0YS11c2VyLWNvbnRlbnRzLmltZ2l4Lm5ldC9-dGV4dD9peGxpYj1yYi00LjEuMSZ3PTgzOCZoPTU4JnR4dD0lNDBHZW5lTGFiXzk5OSZ0eHQtY29sb3I9JTIzMUUyMTIxJnR4dC1mb250PUhpcmFnaW5vJTIwU2FucyUyMFc2JnR4dC1zaXplPTM2JnR4dC1wYWQ9MCZzPWQ5MDQ1MWRmNGZkZGQwNWUzOGQyNjg4ZTlkOTg1ZTll&amp;blend-x=242&amp;blend-y=480&amp;blend-w=838&amp;blend-h=46&amp;blend-fit=crop&amp;blend-crop=left%2Cbottom&amp;blend-mode=normal&amp;s=11a9ae24aa2246524298dba956a6d7bb" alt="Can Jev take over an LLM&#x27;s if-statements?" width="240"></a></td>
<td valign="top"><b><a href="https://qiita.com/GeneLab_999/items/116aa006fbf93b68d791">Can Jev take over an LLM's if-statements?</a></b><br><sub>GeneLab_999 · Article · 2026-09-17</sub><br>Japanese analysis that checks, using only the public SDK and documented examples without calling the API, which code branches Jev can replace, and reports two contradictions between official docs.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://digidai.github.io/2026/09/21/typesafe-jev-jevable-decision-models/"><img src="https://digidai.github.io/images/articles/typesafe-jev-jevable-decision-models/cover-v1.jpg?v=2026-09-21" alt="From model launch to Jevable&#x27;s early projects" width="240"></a></td>
<td valign="top"><b><a href="https://digidai.github.io/2026/09/21/typesafe-jev-jevable-decision-models/">From model launch to Jevable's early projects</a></b><br><sub>Gene Dai · Article · 2026-09-21</sub><br>Long read that uses the 194 early projects listed on Jevable to show the common split of work, where Jev chooses among options other software supplies, and what the low token price leaves out.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://zenn.dev/watany/articles/36e11a20ce3743"><img src="https://res.cloudinary.com/zenn/image/upload/s--p7nC-kx3--/c_fit%2Cg_north_west%2Cl_text:notosansjp-medium.otf_55:Jev%25E3%2581%25A7%25E3%2583%258F%25E3%2583%25BC%25E3%2583%258D%25E3%2582%25B9%25E3%2582%25A8%25E3%2583%25B3%25E3%2582%25B8%25E3%2583%258B%25E3%2582%25A2%25E3%2583%25AA%25E3%2583%25B3%25E3%2582%25B0%2Cw_1010%2Cx_90%2Cy_100/g_south_west%2Cl_text:notosansjp-medium.otf_37:watany%2Cx_203%2Cy_121/g_south_west%2Ch_90%2Cl_fetch:aHR0cHM6Ly9zdGF0aWMuemVubi5zdHVkaW8vdXNlci11cGxvYWQvYXZhdGFyLzJiYjJiYTdkZjkuanBlZw==%2Cr_max%2Cw_90%2Cx_87%2Cy_95/v1627283836/default/og-base-w1200-v2.png?_a=BACMTiAE" alt="Harness engineering with Jev" width="240"></a></td>
<td valign="top"><b><a href="https://zenn.dev/watany/articles/36e11a20ce3743">Harness engineering with Jev</a></b><br><sub>watany · Article · 2026-09-18</sub><br>Japanese post on using Jev as a deterministic-leaning piece of an agent harness, with notes on getting access via the waitlist, Vercel AI Gateway, or Cloudflare.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://qiita.com/hisashi-ito/items/3d8d26ea591009e7a58e"><img src="https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-user-contents.imgix.net%2Fhttps%253A%252F%252Fcdn.qiita.com%252Fassets%252Fpublic%252Farticle-ogp-background-afbab5eb44e0b055cce1258705637a91.png%3Fixlib%3Drb-4.1.1%26w%3D1200%26blend64%3DaHR0cHM6Ly9xaWl0YS11c2VyLXByb2ZpbGUtaW1hZ2VzLmltZ2l4Lm5ldC9odHRwcyUzQSUyRiUyRnFpaXRhLWltYWdlLXN0b3JlLnMzLmFwLW5vcnRoZWFzdC0xLmFtYXpvbmF3cy5jb20lMkYwJTJGODgzMTYlMkZwcm9maWxlLWltYWdlcyUyRjE3MDgwODAxMjM_aXhsaWI9cmItNC4xLjEmYXI9MSUzQTEmZml0PWNyb3AmbWFzaz1lbGxpcHNlJmJnPUZGRkZGRiZmbT1wbmczMiZzPTdlYWZmOGJmYjU1NzNlNDAzOGMxMjM3ZWUzMjQ4MWNl%26blend-x%3D120%26blend-y%3D467%26blend-w%3D82%26blend-h%3D82%26blend-mode%3Dnormal%26s%3D21470933a45a0ec36724c827775f7517?ixlib=rb-4.1.1&amp;w=1200&amp;fm=jpg&amp;mark64=aHR0cHM6Ly9xaWl0YS11c2VyLWNvbnRlbnRzLmltZ2l4Lm5ldC9-dGV4dD9peGxpYj1yYi00LjEuMSZ3PTk2MCZoPTMyNCZ0eHQ9SmV2JUVGJUJDJTg4VHlwZVNhZmUlMjBBSSVFRiVCQyU4OSVFMyU4MSVBRiVFMyU4MSVCRiVFMyU4MiU5MyVFMyU4MSVBQSVFMyU4MSVBOSVFMyU4MSU4NiVFMyU4MiU4NCVFMyU4MSVBMyVFMyU4MSVBNiVFNCVCRCVCRiVFMyU4MSVBMyVFMyU4MSVBNiVFMyU4MSU4NCVFMyU4MiU4QiVFMyU4MSVBRSVFMyU4MSU4QiVFRiVCQyU5RiZ0eHQtYWxpZ249bGVmdCUyQ3RvcCZ0eHQtY29sb3I9JTIzMUUyMTIxJnR4dC1mb250PUhpcmFnaW5vJTIwU2FucyUyMFc2JnR4dC1zaXplPTU2JnR4dC1wYWQ9MCZzPWJjMTljMjZjY2VkZjM0YmIyYmQ3ZjI0OWM0NmFhNTRh&amp;mark-x=120&amp;mark-y=112&amp;blend64=aHR0cHM6Ly9xaWl0YS11c2VyLWNvbnRlbnRzLmltZ2l4Lm5ldC9-dGV4dD9peGxpYj1yYi00LjEuMSZ3PTgzOCZoPTU4JnR4dD0lNDBoaXNhc2hpLWl0byZ0eHQtY29sb3I9JTIzMUUyMTIxJnR4dC1mb250PUhpcmFnaW5vJTIwU2FucyUyMFc2JnR4dC1zaXplPTM2JnR4dC1wYWQ9MCZzPTU4ZmY0ZGQwMDRlY2ZjMDkxZGM3Y2ZkZWFhMWRlMTU5&amp;blend-x=242&amp;blend-y=480&amp;blend-w=838&amp;blend-h=46&amp;blend-fit=crop&amp;blend-crop=left%2Cbottom&amp;blend-mode=normal&amp;s=7ac19a0ac6f09481b52bbb2f0895087b" alt="How is everyone using Jev?" width="240"></a></td>
<td valign="top"><b><a href="https://qiita.com/hisashi-ito/items/3d8d26ea591009e7a58e">How is everyone using Jev?</a></b><br><sub>hisashi-ito · Article · 2026-09-18</sub><br>Japanese survey that counts public Jev projects on GitHub and X through the sixth day after launch and charts what people are using it for.</td>
</tr>
<tr>
<td width="260" valign="top"></td>
<td valign="top"><b><a href="https://docs.bswen.com/blog/2026-09-18-jev-system-one-smart-if/">Is Jev a 'smart if'?</a></b><br><sub>BSWEN (Cowrie Dev) · Article · 2026-09-19</sub><br>Hands-on Jev Playground tests showing that Jev does not execute user-written rules the way deterministic if/else code does, and that its best role is a low-latency decision layer inside agents.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://flowtivity.ai/blog/jev-typesafe-ai-decision-model/"><img src="https://flowtivity.ai/api/blog/media/blog/1789561319551-hero-8ugxup.svg" alt="Is the 200x Faster Decision Model Too Good to Be True?" width="240"></a></td>
<td valign="top"><b><a href="https://flowtivity.ai/blog/jev-typesafe-ai-decision-model/">Is the 200x Faster Decision Model Too Good to Be True?</a></b><br><sub>AJ Awan (Flowtivity) · Article · 2026-09-16</sub><br>Claim-by-claim audit of TypeSafe's 200x faster, 400x cheaper launch figures, with pricing math and the skeptical pushback from Hacker News.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://cobusgreyling.medium.com/jev-by-typesafe-ai-4846aaca3186"><img src="https://cdn-images-1.medium.com/max/1024/1*4ZmFqv_O6qa2pr_rWu1Skw.png" alt="Jev by TypeSafe AI" width="240"></a></td>
<td valign="top"><b><a href="https://cobusgreyling.medium.com/jev-by-typesafe-ai-4846aaca3186">Jev by TypeSafe AI</a></b><br><sub>Cobus Greyling · Article · 2026-09-21</sub><br>Essay on Jev as machine-native intelligence and how to adopt it: shadow an existing decision, gate on confidence, target high-frequency forks, and pair it with LLMs rather than replace them.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://dev.to/miruky/jev-does-not-replace-the-llm-it-changes-who-owns-the-decision-3n6"><img src="https://media2.dev.to/dynamic/image/width=1200,height=627,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Farticles%2Fan164emsrub8iv34h66e.png" alt="Jev changes who owns the decision" width="240"></a></td>
<td valign="top"><b><a href="https://dev.to/miruky/jev-does-not-replace-the-llm-it-changes-who-owns-the-decision-3n6">Jev changes who owns the decision</a></b><br><sub>miruky · Article · 2026-09-19</sub><br>Review of Jev's API contract and SDK behavior with mocked responses, pinning down what 'zero hallucinations' means and splitting work between Jev, the LLM, and code that keeps policy and exact calculations.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://medium.com/@thealonemusk/jev-doesnt-chat-that-might-be-the-point-2f12663c661f"><img src="https://cdn-images-1.medium.com/max/1024/1*0-D3Ied-psYthZzWJZsOag.png" alt="Jev Doesn&#x27;t Chat. That Might Be the Point." width="240"></a></td>
<td valign="top"><b><a href="https://medium.com/@thealonemusk/jev-doesnt-chat-that-might-be-the-point-2f12663c661f">Jev Doesn't Chat. That Might Be the Point.</a></b><br><sub>Ashutosh Jha · Article · 2026-09-18</sub><br>Claim-by-claim critique of the System One launch: naming, architecture, economics, the Doom demo's structured-state caveat, and why prompt-injection resistance matters for a decision layer.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://www.aibuilderclub.com/blog/jev-engineering-guide"><img src="https://www.aibuilderclub.com/images/blog/jev-engineering-three-role-loop.png" alt="Jev engineering guide" width="240"></a></td>
<td valign="top"><b><a href="https://www.aibuilderclub.com/blog/jev-engineering-guide">Jev engineering guide</a></b><br><sub>AI Jason (AI Builder Club) · Article · 2026-09-22</sub><br>Agent pattern where an LLM writes, Jev decides, and code acts, shown through a Claude Code guard hook, a model router, and a log-triage cron; a replay of 600 log entries cost $0.00029 at a 302 ms median.<br><sub><b>How it uses Jev:</b> Typed Choice/Score/Noul forks with thresholds in code; only the uncertain case escalates to Claude Code.</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://qiita.com/ryu-ki/items/e3fe99b5f6704d08a19b"><img src="https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-user-contents.imgix.net%2Fhttps%253A%252F%252Fcdn.qiita.com%252Fassets%252Fpublic%252Farticle-ogp-background-afbab5eb44e0b055cce1258705637a91.png%3Fixlib%3Drb-4.1.1%26w%3D1200%26blend64%3DaHR0cHM6Ly9xaWl0YS11c2VyLXByb2ZpbGUtaW1hZ2VzLmltZ2l4Lm5ldC9odHRwcyUzQSUyRiUyRnMzLWFwLW5vcnRoZWFzdC0xLmFtYXpvbmF3cy5jb20lMkZxaWl0YS1pbWFnZS1zdG9yZSUyRjAlMkYzOTIxODAyJTJGMzM4YjUwMmZkNzA3YWQ4YjkwYWU3MWRkYzgwNGFhNTdjYmNlM2JjZiUyRmxhcmdlLnBuZyUzRjE3ODA3MTQyMDI_aXhsaWI9cmItNC4xLjEmYXI9MSUzQTEmZml0PWNyb3AmbWFzaz1lbGxpcHNlJmJnPUZGRkZGRiZmbT1wbmczMiZzPTRiYTY3MTIxMTc3N2QzNzQ5NTIxMjc5NmMyNmJiNTk1%26blend-x%3D120%26blend-y%3D462%26blend-w%3D90%26blend-h%3D90%26blend-mode%3Dnormal%26mark64%3DaHR0cHM6Ly9xaWl0YS1vcmdhbml6YXRpb24taW1hZ2VzLmltZ2l4Lm5ldC9odHRwcyUzQSUyRiUyRnMzLWFwLW5vcnRoZWFzdC0xLmFtYXpvbmF3cy5jb20lMkZxaWl0YS1vcmdhbml6YXRpb24taW1hZ2UlMkY1NTdmMmM4MGU4N2IwMjhhMjU3ZTIwMjQzZmU4ZTYzNWYxNzFiNDE1JTJGb3JpZ2luYWwuanBnJTNGMTc4Mjg4MTcwMD9peGxpYj1yYi00LjEuMSZ3PTQ0Jmg9NDQmZml0PWNyb3AmbWFzaz1jb3JuZXJzJmNvcm5lci1yYWRpdXM9OCZiZz1GRkZGRkYmYm9yZGVyPTIlMkNGRkZGRkYmZm09cG5nMzImcz1kNThhMjUwOWQ0ZDUwMGE5MmU0MTIwZTc1OGZmNzEzMQ%26mark-x%3D186%26mark-y%3D515%26mark-w%3D40%26mark-h%3D40%26s%3Db305af80e267c0831201b587d6085c96?ixlib=rb-4.1.1&amp;w=1200&amp;fm=jpg&amp;mark64=aHR0cHM6Ly9xaWl0YS11c2VyLWNvbnRlbnRzLmltZ2l4Lm5ldC9-dGV4dD9peGxpYj1yYi00LjEuMSZ3PTk2MCZoPTMyNCZ0eHQ9JUUzJTgwJTkwSmV2JUUzJTgwJTkxJUU2JTk2JTg3JUU3JUFCJUEwJUUzJTgyJTkyJUU4JUJGJTk0JUUzJTgxJTk1JUUzJTgxJUFBJUUzJTgxJTg0JUU1JTg4JUE0JUU2JTk2JUFEJUUzJTgzJUEyJUUzJTgzJTg3JUUzJTgzJUFCJTIwSmV2JTIwJUUzJTgxJUE4JUUzJTgxJUFGJUVGJUJDJTlGJUUzJTgwJTlDJUUzJTgyJUI3JUUzJTgyJUI5JUUzJTgzJTg2JUUzJTgzJUEwJUU5JTgxJThCJUU3JTk0JUE4JUUzJTgxJUE3JUUzJTgxJUFFJUU2JUI0JUJCJUU3JTk0JUE4JUU2JTk2JUI5JUU2JUIzJTk1JUUzJTgxJUFCJUUzJTgxJUE0JUUzJTgxJTg0JUUzJTgxJUE2JUUzJTgyJTgyJUU2JTgzJUIzJUU1JTgzJThGJUUzJTgxJTk3JUUzJTgxJUE2JUUzJTgxJUJGJUUzJTgyJThCJUUzJTgwJTlDJnR4dC1hbGlnbj1sZWZ0JTJDdG9wJnR4dC1jb2xvcj0lMjMxRTIxMjEmdHh0LWZvbnQ9SGlyYWdpbm8lMjBTYW5zJTIwVzYmdHh0LXNpemU9NTYmdHh0LXBhZD0wJnM9NzlhNmQwZDVkMjM0NjViYzJiMGExNzlhMmQyMDY3ZWY&amp;mark-x=120&amp;mark-y=112&amp;blend64=aHR0cHM6Ly9xaWl0YS11c2VyLWNvbnRlbnRzLmltZ2l4Lm5ldC9-dGV4dD9peGxpYj1yYi00LjEuMSZ3PTgzOCZoPTU4JnR4dD0lNDByeXUta2kmdHh0LWNvbG9yPSUyMzFFMjEyMSZ0eHQtZm9udD1IaXJhZ2lubyUyMFNhbnMlMjBXNiZ0eHQtc2l6ZT0zNiZ0eHQtcGFkPTAmcz1iZTI4YjM3MDJlNmVlMTE3YTVmODA3MWNkZmE5MWI2Mg&amp;blend-x=242&amp;blend-y=454&amp;blend-w=838&amp;blend-h=46&amp;blend-fit=crop&amp;blend-crop=left%2Cbottom&amp;blend-mode=normal&amp;txt64=VElTSeagquW8j-S8muekvg&amp;txt-x=242&amp;txt-y=539&amp;txt-width=838&amp;txt-clip=end%2Cellipsis&amp;txt-color=%231E2121&amp;txt-font=Hiragino%20Sans%20W6&amp;txt-size=28&amp;s=f8d06f197ddc5be1166c8224419079f7" alt="Jev for system operations" width="240"></a></td>
<td valign="top"><b><a href="https://qiita.com/ryu-ki/items/e3fe99b5f6704d08a19b">Jev for system operations</a></b><br><sub>ryu-ki · Article · 2026-09-18</sub><br>Japanese summary of what the docs say about Jev, followed by ideas for applying it to system operations work such as alert handling.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://zenn.dev/meijin/articles/jev-impressions"><img src="https://res.cloudinary.com/zenn/image/upload/s--W4LKp311--/c_fit%2Cg_north_west%2Cl_text:notosansjp-medium.otf_55:Jev%2520%25E6%2589%2580%25E6%2584%259F%2520%25E3%2583%2580%25E3%2583%25A9%25E3%2583%2580%25E3%2583%25A9%25E3%2581%25A8%25E6%259B%25B8%25E3%2581%258F%2Cw_1010%2Cx_90%2Cy_100/g_south_west%2Cl_text:notosansjp-medium.otf_37:meijin%2Cx_203%2Cy_121/g_south_west%2Ch_90%2Cl_fetch:aHR0cHM6Ly9saDMuZ29vZ2xldXNlcmNvbnRlbnQuY29tL2EtL0FPaDE0R2pPWmtyWk1nS3djRXl5a2w1X2lVTFZFVmtVVUpkNzkzcjlfejhERjRzPXMyNTAtYw==%2Cr_max%2Cw_90%2Cx_87%2Cy_95/v1627283836/default/og-base-w1200-v2.png?_a=BACMTiAE" alt="Jev impressions" width="240"></a></td>
<td valign="top"><b><a href="https://zenn.dev/meijin/articles/jev-impressions">Jev impressions</a></b><br><sub>meijin · Article · 2026-09-18</sub><br>Japanese notes on where Jev fits: pairing with an LLM that reads the state while Jev picks the next action in tools like Browser Use, and choosing the next UI from user context with an LLM fallback.</td>
</tr>
<tr>
<td width="260" valign="top"></td>
<td valign="top"><b><a href="https://simonwillison.net/2026/Sep/21/jev/">Jev introduces a new shape of LLM</a></b><br><sub>Simon Willison · Article · 2026-09-21</sub><br>Explains Jev as a 'decision model' that returns numbers rather than text, covers its pricing and question types, notes experiments with BM25-then-Jev search reranking, and raises black-box and bias concerns.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://medium.com/@creativeaininja/typesafes-jev-makes-ai-decisions-fast-enough-to-play-doom-68fdcce1159a"><img src="https://miro.medium.com/v2/resize:fit:700/1*7UqArSYtCxH4sok--XJFZA.png" alt="Jev makes AI decisions fast enough to play Doom" width="240"></a></td>
<td valign="top"><b><a href="https://medium.com/@creativeaininja/typesafes-jev-makes-ai-decisions-fast-enough-to-play-doom-68fdcce1159a">Jev makes AI decisions fast enough to play Doom</a></b><br><sub>Kristopher Dunham · Article · 2026-09-17</sub><br>Explains how millisecond typed decisions enable real-time control loops such as TypeSafe's Doom demo and a community Super Mario agent, where game state goes in as structured text rather than pixels.<br><sub>Also: <a href="https://github.com/fhshaik/typesafe-mario">related</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"></td>
<td valign="top"><b><a href="https://www.seangoedecke.com/jev-means-structured-output-is-interesting-again/">Jev means structured output is interesting again</a></b><br><sub>Sean Goedecke · Article · 2026-09-16</sub><br>Why a decision model has steady latency, and how far prefill plus single-token constrained decoding gets you with open models.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/myokoym/misereru-slide-jev"><img src="https://opengraph.githubassets.com/1/myokoym/misereru-slide-jev" alt="Jev research deck" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/myokoym/misereru-slide-jev">Jev research deck</a></b><br><sub>myokoym · GitHub · 2026-09-17</sub><br>Ongoing Japanese research on Jev and System One models maintained as Markdown slides, a presentation script and an article, backed by a ledger of sources, third-party verification and caveats.<br><sub>Also: <a href="https://myokoym.github.io/misereru-slide-jev/">slides</a> · <a href="https://myokoym.github.io/misereru-slide-jev">write-up</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://lilting.ch/en/articles/typesafe-ai-jev-system-one-model"><img src="https://lilting.ch/og/images/hero/ogp.ogp.jpg" alt="Jev vs auto-regressive LLMs and MDLM" width="240"></a></td>
<td valign="top"><b><a href="https://lilting.ch/en/articles/typesafe-ai-jev-system-one-model">Jev vs auto-regressive LLMs and MDLM</a></b><br><sub>lilting channel · Article · 2026-09-17</sub><br>Technical comparison of Jev's single-pass parallel sampler with token-by-token autoregressive decoding and masked diffusion language models, alongside pricing and RLCD calibration.</td>
</tr>
<tr>
<td width="260" valign="top"></td>
<td valign="top"><b><a href="https://wonderwhy-er.medium.com/typesafe-jev-wont-train-on-your-data-it-can-still-learn-from-it-563f0ad591b6">Jev won't train on your data</a></b><br><sub>Eduard Ruzga · Article · 2026-09-19</sub><br>Examines Jev's cheaper-faster-less-general trade-off and TypeSafe's customer agreement, asking what 'derived telemetry' allows when the vendor says it will not train on your data.</td>
</tr>
<tr>
<td width="260" valign="top"></td>
<td valign="top"><b><a href="https://zhuanlan.zhihu.com/p/2085057727869593002">Jev zero-hallucination deep-dive</a></b><br><sub>Zhihu · Article</sub><br>Chinese deep-dive that examines TypeSafe Jev's 'zero hallucination' System One claims and how far they hold up.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://www.turingpost.com/p/what-is-jev-rlcd"><img src="https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,quality=80,width=1200,onerror=redirect/uploads/asset/file/73da3503-3fd3-4221-98a3-d07a8c8d8398/guide2_1_.jpg?t=1789781447" alt="Jev, RLCD, and the reinvention of the AI classifier" width="240"></a></td>
<td valign="top"><b><a href="https://www.turingpost.com/p/what-is-jev-rlcd">Jev, RLCD, and the reinvention of the AI classifier</a></b><br><sub>Turing Post (Ksenia Se) · Article · 2026-09-19</sub><br>Guide that dissects what is known about Jev and RLCD, traces the older research ideas it combines, and lists open-source alternatives and 12 related papers.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://pearpages.com/blog/2026/09/16/jev-sorted-what-typesafes-system-one-model-actually-is-and-what-is-still-just-a-claim"><img src="https://pearpages.com/assets/images/og-c2daec938fe24aa01d8d6904d87cb17d.webp" alt="Jev, Sorted" width="240"></a></td>
<td valign="top"><b><a href="https://pearpages.com/blog/2026/09/16/jev-sorted-what-typesafes-system-one-model-actually-is-and-what-is-still-just-a-claim">Jev, Sorted</a></b><br><sub>Pere Pages · Article · 2026-09-16</sub><br>Reads the primary sources behind the launch claims and concludes Jev is a narrower, more interesting frontier-trained classifier for software, with every benchmark still vendor-reported.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://aiwithmike.substack.com/p/jev-three-days-in-what-is-known-what"><img src="https://substackcdn.com/image/fetch/$s_!ArAN!,w_1200,h_675,c_fill,f_jpg,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F35dc9b92-6756-4ae9-a779-a232ad7c1992_1024x559.jpeg" alt="Jev, three days in" width="240"></a></td>
<td valign="top"><b><a href="https://aiwithmike.substack.com/p/jev-three-days-in-what-is-known-what">Jev, three days in</a></b><br><sub>Mike Erlihson · Article · 2026-09-18</sub><br>Takes stock three days after launch, separating what has been independently measured about Jev from what is guessed, and where it fits.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://www.linkedin.com/pulse/qu%C3%A9-es-jev-el-modelo-system-one-de-typesafe-ai-que-en-kraayenbrink-g65ff/"><img src="https://media.licdn.com/dms/image/v2/D4D12AQGc13qIPizL8Q/article-cover_image-shrink_720_1280/B4DaDCI.CLIAAQ-/0/1789963526522?e=2147483647&amp;v=beta&amp;t=L_Pc-zhjp2Ac7fdpe-6kwPPqvZCvxOEdBc4gmB2zrWM" alt="Qué es Jev" width="240"></a></td>
<td valign="top"><b><a href="https://www.linkedin.com/pulse/qu%C3%A9-es-jev-el-modelo-system-one-de-typesafe-ai-que-en-kraayenbrink-g65ff/">Qué es Jev</a></b><br><sub>Jon Kraayenbrink · Article · 2026-09-21</sub><br>Spanish explainer of the System One idea, real costs versus an LLM, and what people are building, based on indexing 295 public Jev projects from 269 people between September 15 and 21.</td>
</tr>
<tr>
<td width="260" valign="top"></td>
<td valign="top"><b><a href="https://juejin.cn/post/7687793891199418374">Stop hyping Jev</a></b><br><sub>stormzhang · Article · 2026-09-21</sub><br>Chinese contrarian take: Jev is useful for routing, guardrails, and batch document work, but it matches DeepSeek Flash on capability, 'no hallucinations' is a redefinition, and open rebuilds appeared within 48 hours.</td>
</tr>
<tr>
<td width="260" valign="top"></td>
<td valign="top"><b><a href="https://juejin.cn/post/7687825526383624207">Testing Jev's probability calibration</a></b><br><sub>Hogwarts Testing (霍格沃兹测试开发) · Article · 2026-09-21</sub><br>Chinese article on how QA engineers should test an AI decision system like Jev, checking not just whether answers are right but whether stated confidence such as 95% matches real accuracy.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://www.completeskeptic.com/p/the-bitterest-lesson"><img src="https://substackcdn.com/image/fetch/$s_!Whnc!,w_1200,h_675,c_fill,f_jpg,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F89cfa8bd-40b0-4c8d-a0d1-90435054c92a_1894x1016.png" alt="The Bitterest Lesson" width="240"></a></td>
<td valign="top"><b><a href="https://www.completeskeptic.com/p/the-bitterest-lesson">The Bitterest Lesson</a></b><br><sub>Diogo Almeida · Article · 2026-09-10</sub><br>Essay by TypeSafe's CEO, also published on the TypeSafe blog, arguing that compute-driven progress is wasted when models are trained for the wrong task, the thesis behind building decision models for software.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://warmersun.com/jev/"><img src="https://here.now/og/jovial-cottage-dwgn.jpg" alt="Typed Decisions, Not Chat" width="240"></a></td>
<td valign="top"><b><a href="https://warmersun.com/jev/">Typed Decisions, Not Chat</a></b><br><sub>Warmer Sun · Article · 2026-09-17</sub><br>Independent technical walkthrough of Jev that separates TypeSafe's launch claims from what the public evidence actually establishes, with an inspectable audit trail.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://actionbox.cloud/blog/typesafe-ai-jev-review/"><img src="https://actionbox.cloud/blog/images/typesafe-jev-intelligence-cost.webp" alt="TypeSafe AI Jev review" width="240"></a></td>
<td valign="top"><b><a href="https://actionbox.cloud/blog/typesafe-ai-jev-review/">TypeSafe AI Jev review</a></b><br><sub>ActionBox (Suson Sapkota) · Article · 2026-09-15</sub><br>Early-access review that checks the Playground, raw API, and SDK examples, then compares Jev with rules, classifiers, rerankers, and LLM judges and examines the limits of the launch benchmarks.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://www.theneuron.ai/explainer-articles/typesafe-jev-system-one-models-explained/"><img src="https://cdn.theneuron.ai/TypeSafe%20JEV%20Structured%20Decisions%20Beyond%20Chat.png?w=1024" alt="TypeSafe JEV explained" width="240"></a></td>
<td valign="top"><b><a href="https://www.theneuron.ai/explainer-articles/typesafe-jev-system-one-models-explained/">TypeSafe JEV explained</a></b><br><sub>Grant Harvey (The Neuron) · Article · 2026-09-16</sub><br>Plain-language explainer on why software decisions may not need a chatbot, covering the parallel System One design, RLCD calibration, enterprise fit and the strongest counterargument.</td>
</tr>
<tr>
<td width="260" valign="top"></td>
<td valign="top"><b><a href="https://www.developersdigest.tech/blog/typesafe-jev-system-one-models-release-guide-2026">TypeSafe Jev, benchmarked and priced</a></b><br><sub>Developers Digest · Article · 2026-09-16</sub><br>Release-week technical rundown of Jev's primitives, parallel sampler and RLCD training, published workflow evals with their caveats, pricing and the API, SDK and agent-skill surface.</td>
</tr>
<tr>
<td width="260" valign="top"></td>
<td valign="top"><b><a href="https://docs.typesafe.ai/patterns">TypeSafe patterns</a></b><br><sub>TypeSafe AI · Docs</sub><br>Official guide to architectural patterns for building with Jev: speculative fan-out, confidence-gated routing, composite scoring and intent routing.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/dnakhoa/jev-deferred-crispification"><img src="https://opengraph.githubassets.com/1/dnakhoa/jev-deferred-crispification" alt="What Jev Is Missing" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/dnakhoa/jev-deferred-crispification">What Jev Is Missing</a></b><br><sub>dnakhoa · GitHub · 2026-09-16</sub><br>Position paper arguing that per-hop calibration does not compose across decision pipelines and that typed answers destroy vagueness, proposing Hidden-Markov and fuzzy primitives and an architecture called BSF-S1.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://note.com/kagawatomo/n/n5425654d0f5d"><img src="https://assets.st-note.com/production/uploads/images/314812501/rectangle_large_type_2_ec7e04d489da5232ca3084c4c3ab514e.png?fit=bounds&amp;quality=85&amp;width=1280" alt="What TypeSafe is building with Jev" width="240"></a></td>
<td valign="top"><b><a href="https://note.com/kagawatomo/n/n5425654d0f5d">What TypeSafe is building with Jev</a></b><br><sub>香川友志 (kagawatomo) · Article · 2026-09-18</sub><br>Long-form Japanese analysis of what Jev is and is not, the founders' background, and TypeSafe's bet on embedding classification, routing, scoring, approval, and verification decisions into software.</td>
</tr>
<tr>
<td width="260" valign="top"></td>
<td valign="top"><b><a href="https://ranjankumar.in/jev-system-one-model-agent-harness-placement">Where Jev belongs in an agent harness</a></b><br><sub>Ranjan Kumar · Article · 2026-09-21</sub><br>Long analysis arguing that Jev's ordering can be trusted but its confidence numbers need a local fit, and showing where a decision model belongs in an agent harness and how to set thresholds on your own data.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://dev.to/extractdata/jev-the-model-that-cannot-write-a-word-and-where-it-fits-in-web-scraping-does-it-45jb"><img src="https://media2.dev.to/dynamic/image/width=1200,height=627,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fextract.zyte.com%2Fapi%2Fmedia%2Ffile%2Fcnt-1347-01-cover.png" alt="Where Jev fits in web scraping" width="240"></a></td>
<td valign="top"><b><a href="https://dev.to/extractdata/jev-the-model-that-cannot-write-a-word-and-where-it-fits-in-web-scraping-does-it-45jb">Where Jev fits in web scraping</a></b><br><sub>Ayan Pahwa (Zyte) · Article · 2026-09-21</sub><br>Argues Jev cannot extract fields because it never writes a string, and shows the one scraping job it earns: a gate in front of extraction, with a requests and BeautifulSoup example.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://qiita.com/Isaka-code/items/8944ef8b521517f92da0"><img src="https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-user-contents.imgix.net%2Fhttps%253A%252F%252Fcdn.qiita.com%252Fassets%252Fpublic%252Farticle-ogp-background-afbab5eb44e0b055cce1258705637a91.png%3Fixlib%3Drb-4.1.1%26w%3D1200%26blend64%3DaHR0cHM6Ly9xaWl0YS11c2VyLXByb2ZpbGUtaW1hZ2VzLmltZ2l4Lm5ldC9odHRwcyUzQSUyRiUyRnFpaXRhLWltYWdlLXN0b3JlLnMzLmFwLW5vcnRoZWFzdC0xLmFtYXpvbmF3cy5jb20lMkYwJTJGMjYyNzAxNSUyRnByb2ZpbGUtaW1hZ2VzJTJGMTczODM4MDAyOD9peGxpYj1yYi00LjEuMSZhcj0xJTNBMSZmaXQ9Y3JvcCZtYXNrPWVsbGlwc2UmYmc9RkZGRkZGJmZtPXBuZzMyJnM9NjM3MmNhMjU1NmQ2M2IyNzUyZjAwMWY3OWFjNjBiMDY%26blend-x%3D120%26blend-y%3D467%26blend-w%3D82%26blend-h%3D82%26blend-mode%3Dnormal%26s%3D6d046f33d6fa0f0f44d8a349b9b12d4a?ixlib=rb-4.1.1&amp;w=1200&amp;fm=jpg&amp;mark64=aHR0cHM6Ly9xaWl0YS11c2VyLWNvbnRlbnRzLmltZ2l4Lm5ldC9-dGV4dD9peGxpYj1yYi00LjEuMSZ3PTk2MCZoPTMyNCZ0eHQ9SmV2JUUzJTgxJUFGJUUzJTgxJUE5JUUzJTgxJTkzJUUzJTgxJUE3JUU0JUJEJUJGJUUzJTgxJTg2JUUzJTgxJUI5JUUzJTgxJThEJUUzJTgxJThCJUVGJUJDJTlGJTIwTExNJUUzJTgzJUJCJUU2JUE5JTlGJUU2JUEyJUIwJUU1JUFEJUE2JUU3JUJGJTkyJUUzJTgzJUJCJUUzJTgzJUFCJUUzJTgzJUJDJUUzJTgzJUFCJUUzJTgzJTk5JUUzJTgzJUJDJUUzJTgyJUI5JUUzJTgxJUE4JUUzJTgxJUFFJUU0JUJEJUJGJUUzJTgxJTg0JUU1JTg4JTg2JUUzJTgxJTkxJnR4dC1hbGlnbj1sZWZ0JTJDdG9wJnR4dC1jb2xvcj0lMjMxRTIxMjEmdHh0LWZvbnQ9SGlyYWdpbm8lMjBTYW5zJTIwVzYmdHh0LXNpemU9NTYmdHh0LXBhZD0wJnM9NjMxOWY5NjgyMGYwYjgyYjIzZDMxNTQ0MmViZmQ3NmM&amp;mark-x=120&amp;mark-y=112&amp;blend64=aHR0cHM6Ly9xaWl0YS11c2VyLWNvbnRlbnRzLmltZ2l4Lm5ldC9-dGV4dD9peGxpYj1yYi00LjEuMSZ3PTgzOCZoPTU4JnR4dD0lNDBJc2FrYS1jb2RlJnR4dC1jb2xvcj0lMjMxRTIxMjEmdHh0LWZvbnQ9SGlyYWdpbm8lMjBTYW5zJTIwVzYmdHh0LXNpemU9MzYmdHh0LXBhZD0wJnM9ODVjZDg3YWRkMzg5ZjgxODZjMGNkMjdjNGI3NTdmZDc&amp;blend-x=242&amp;blend-y=480&amp;blend-w=838&amp;blend-h=46&amp;blend-fit=crop&amp;blend-crop=left%2Cbottom&amp;blend-mode=normal&amp;s=d5aabfc779d3a385cf32a5f83b19950f" alt="Where should you use Jev?" width="240"></a></td>
<td valign="top"><b><a href="https://qiita.com/Isaka-code/items/8944ef8b521517f92da0">Where should you use Jev?</a></b><br><sub>Isaka-code · Article · 2026-09-19</sub><br>Japanese guide to choosing between rule-based code, classic machine learning, Jev, and LLMs, with the conditions under which Jev is the right tool.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://zenn.dev/1amageek/articles/typesafe-jev-system-one-model"><img src="https://res.cloudinary.com/zenn/image/upload/s--wzI_Yk5V--/c_fit%2Cg_north_west%2Cl_text:notosansjp-medium.otf_55:%25E6%2596%2587%25E5%25AD%2597%25E5%2588%2597%25E3%2582%2592%25E6%258D%25A8%25E3%2581%25A6%25E3%2581%259F%25E3%2583%25A2%25E3%2583%2587%25E3%2583%25AB%25E3%2580%2582Jev%25E3%2581%25AF%25E3%2581%25AA%25E3%2581%259C%25E6%25A1%2581%25E3%2581%25A7%25E9%2580%259F%25E3%2581%2584%25E3%2581%25AE%25E3%2581%258B%2Cw_1010%2Cx_90%2Cy_100/g_south_west%2Cl_text:notosansjp-medium.otf_37:1amageek%2Cx_203%2Cy_121/g_south_west%2Ch_90%2Cl_fetch:aHR0cHM6Ly9saDMuZ29vZ2xldXNlcmNvbnRlbnQuY29tL2EtL0FPaDE0R2dBNEpHWllReTFQVmxXNDFOeHBqZ1Z6a0J3TW9ocjFTQjBMLWgtPXMyNTAtYw==%2Cr_max%2Cw_90%2Cx_87%2Cy_95/v1627283836/default/og-base-w1200-v2.png?_a=BACMTiAE" alt="Why Jev is orders of magnitude faster" width="240"></a></td>
<td valign="top"><b><a href="https://zenn.dev/1amageek/articles/typesafe-jev-system-one-model">Why Jev is orders of magnitude faster</a></b><br><sub>1amageek · Article · 2026-09-17</sub><br>Japanese analysis of why dropping string generation makes Jev so much faster, and what the speed comparisons in the launch actually compare.</td>
</tr>
<tr>
<td width="260" valign="top"></td>
<td valign="top"><b><a href="https://juejin.cn/post/7686808742222856211">Why JEV matters: practical patterns</a></b><br><sub>前端小小栈 · Article · 2026-09-19</sub><br>Chinese overview of patterns for a decision model with pseudocode: agent routing, RAG relevance scoring, code-review risk gates, and SQL-style row judgments.</td>
</tr>
<tr>
<td width="260" valign="top"></td>
<td valign="top"><b><a href="https://www.reddit.com/r/LLMDevs/comments/1wlfmaa/why_jev_might_finally_kill_the_text_prompt/">Why Jev might kill the text prompt</a></b><br><sub>dpopa · Reddit · 2026-09-20</sub><br>Essay arguing that chat boxes exist because autoregressive models are too slow for UI event loops, and that 50-100ms decisions allow direct-manipulation AI interfaces.</td>
</tr>
</table>

Missing something? [Suggest a resource](https://github.com/Li-Evan/awesome-jev/issues/new/choose).
