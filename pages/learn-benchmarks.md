# 📚 Learn: Benchmarks and Case Studies

**English** · [简体中文](https://github.com/Li-Evan/awesome-jev/blob/main/zh-CN/pages/learn-benchmarks.md)

Official docs and cookbooks, plus the best guides, analyses, benchmarks, and talks from the community. 173 entries, ranked by community traction.

[← Back to Awesome Jev](https://github.com/Li-Evan/awesome-jev#benchmarks-and-case-studies)

[Official Docs](https://github.com/Li-Evan/awesome-jev/blob/main/pages/learn-official-docs.md) (15) · [Official SDKs and Tools](https://github.com/Li-Evan/awesome-jev/blob/main/pages/learn-official-tools.md) (3) · [Announcements](https://github.com/Li-Evan/awesome-jev/blob/main/pages/learn-announcements.md) (2) · [Patterns](https://github.com/Li-Evan/awesome-jev/blob/main/pages/learn-patterns.md) (4) · [Official Cookbooks](https://github.com/Li-Evan/awesome-jev/blob/main/pages/learn-cookbooks.md) (18) · [Examples and Skills](https://github.com/Li-Evan/awesome-jev/blob/main/pages/learn-examples.md) (74) · [Guides](https://github.com/Li-Evan/awesome-jev/blob/main/pages/learn-guides.md) (76) · [Techniques and Analysis](https://github.com/Li-Evan/awesome-jev/blob/main/pages/learn-techniques.md) (102) · **Benchmarks and Case Studies** · [Talks and Videos](https://github.com/Li-Evan/awesome-jev/blob/main/pages/learn-videos.md) (178) · [Discussions](https://github.com/Li-Evan/awesome-jev/blob/main/pages/learn-discussions.md) (20)

<table>
<tr>
<td width="260" valign="top"><a href="https://github.com/NousResearch/hermes-agent/blob/main/evals/compaction/results/SCORECARD-2026-09-19-jev.md"><img src="https://raw.githubusercontent.com/NousResearch/hermes-agent/main/assets/banner.png" alt="Hermes Agent compaction scorecard" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/NousResearch/hermes-agent/blob/main/evals/compaction/results/SCORECARD-2026-09-19-jev.md">Hermes Agent compaction scorecard</a></b><br><sub>NousResearch · GitHub · ⭐ 247.9k repo · 2025-07-22</sub><br>Tests a Jev-based context-compaction plugin against Hermes' own compressor and recommends against it: far cheaper and faster per compaction, but it kept twice the context and ranked tool results no better than recency.<br><sub><b>How it uses Jev:</b> The Jev arm ranks which history and tool results to keep during compaction; the scorecard compares it with Hermes' built-in compressor.</sub><br><sub>Also: <a href="https://x.com/Teknium/status/2101398453578555898">demo</a> · <a href="https://hermes-agent.nousresearch.com">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://www.langchain.com/blog/jev-agent-evals-langsmith"><img src="https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/6aae04c2c9a23c30549b7035_jev-judge-hero-dark-2400x1260.png" alt="Can Jev Be a Better Agent Evaluator?" width="240"></a></td>
<td valign="top"><b><a href="https://www.langchain.com/blog/jev-agent-evals-langsmith">Can Jev Be a Better Agent Evaluator?</a></b><br><sub>LangChain · Article · ♥ 2.9k · 2026-09-20</sub><br>LangChain tests Jev as a judge against LLM judges for agent evaluation in LangSmith, comparing accuracy, repeatability, latency and cost.<br><sub>Also: <a href="https://x.com/LangChain/status/2101454284927959080">demo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://webmcp.com/benchmark"><img src="https://webmcp.com/blog/img/windtunnel-model-comparison-light.png" alt="WindTunnel" width="240"></a></td>
<td valign="top"><b><a href="https://webmcp.com/benchmark">WindTunnel</a></b><br><sub>Idan Levin (webmcp.com) · Article · ♥ 2.1k</sub><br>WebMCP browser-agent benchmark of 49 tasks on 8 real sites across 21 configurations, where Jev + Mercury 2.5 tops the composite score, solving 49/49 tasks at $0.0011 median cost per task.<br><sub><b>How it uses Jev:</b> Jev picks actions over the WebMCP interface; 141/147 attempts passed versus 76/147 for the DOM configuration.</sub><br><sub>Also: <a href="https://x.com/0xidanlevin/status/2100937437325205568">demo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/MaxRovensky/status/2100706874173575199"><img src="https://pbs.twimg.com/amplify_video_thumb/2100706798533566466/img/RAbrmONSdYbkfjAN.jpg" alt="Trolley problems: humans vs robots" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/MaxRovensky/status/2100706874173575199">Trolley problems: humans vs robots</a></b><br><sub>MaxRovensky · X · ♥ 1.5k · 2026-09-17</sub><br>Video of Jev working through trolley problems, where it chose to sacrifice a human to save robots.</td>
</tr>
<tr>
<td width="260" valign="top"></td>
<td valign="top"><b><a href="https://x.com/h_nilforoshan/status/2100409794276520341">HiringCafe resume-job relevance benchmark</a></b><br><sub>h_nilforoshan · X · ♥ 808 · 2026-09-17</sub><br>Thread benchmarking Jev on resume-to-job-description relevance scoring for HiringCafe, a job search app serving 2.5 million monthly active users.<br><sub>Also: <a href="https://hiringcafe.com">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/liorshkiller/status/2100936106615140757"><img src="https://pbs.twimg.com/media/HSgGI1wWQAAY5zl.jpg?name=orig" alt="Code review benchmark" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/liorshkiller/status/2100936106615140757">Code review benchmark</a></b><br><sub>liorshkiller · X · ♥ 210 · 2026-09-18</sub><br>Benchmark of Jev scoring raw Git diffs against a GLM + Grok + Gemini ensemble reviewer: zero false positives, ~50x faster, ~100x cheaper, with 75% bug recall.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://benchmarkheaven.com/jev-models"><img src="https://benchmarkheaven.com/brand/og-launch.png?v=1" alt="JevBench" width="240"></a></td>
<td valign="top"><b><a href="https://benchmarkheaven.com/jev-models">JevBench</a></b><br><sub>Benchmark Heaven (Florian S) · App · ♥ 999 · 2026-09-19</sub><br>Benchmark of Jev-class decision models that ranks Jev, its open rebuilds, and instruction models on intelligence, calibration, speed, and cost, 25% each as a geometric mean; Jev led at 75.3 with SemIf second at 74.6.<br><sub>Also: <a href="https://x.com/airesearch12/status/2101311769113178270">x</a> · <a href="https://news.ycombinator.com/item?id=49786635">discussion</a> · <a href="https://x.com/airesearch12/status/2101311992984199580">demo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/OpenRouter/status/2101412965765529853"><img src="https://pbs.twimg.com/media/HSm39ISbsAAEPfg.png?name=orig" alt="OpenRouter Ori Eval judging test" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/OpenRouter/status/2101412965765529853">OpenRouter Ori Eval judging test</a></b><br><sub>OpenRouter · X · ♥ 965 · 2026-09-19</sub><br>OpenRouter's Ori Eval comparison of Jev with popular LLMs as a judge: Jev was more than 5x faster than the next fastest model, and its slowest requests beat every other model's median.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/grichadev/status/2100437998571860087"><img src="https://pbs.twimg.com/media/HSY_7aXbIAAxJoj.png?name=orig" alt="Jev in a security pipeline" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/grichadev/status/2100437998571860087">Jev in a security pipeline</a></b><br><sub>grichadev · X · ♥ 924 · 2026-09-17</sub><br>Results table from a production security pipeline: Jev reached 99.3% accuracy at 0.259s latency and $0.026 per 1K, versus Gemini and open models that were slower and costlier.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/crislenta/status/2100457614073327754"><img src="https://pbs.twimg.com/amplify_video_thumb/2100457262372560897/img/zSIVGvaQhEZLMd9-.jpg" alt="500 real-time agents in 3D" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/crislenta/status/2100457614073327754">500 real-time agents in 3D</a></b><br><sub>crislenta · X · ♥ 655 · 2026-09-17</sub><br>Benchmark running 500 real-time agents in parallel in a 3D environment, reporting 500ms average latency and 35 API calls/s with no optimizations.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/nikhilmudholkar/status/2100604560335139083"><img src="https://pbs.twimg.com/media/HSbYODoWoAAKjJR.jpg?name=orig" alt="Industrial email classification benchmark" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/nikhilmudholkar/status/2100604560335139083">Industrial email classification benchmark</a></b><br><sub>nikhilmudholkar · X · ♥ 439 · 2026-09-17</sub><br>Benchmark on 1,565 German and English supplier emails in 10 categories: Jev scored 96.4% vs Gemini's 97.5% and 98.5%, at $0.08 per 1,000 emails, and none of its 737 answers at 99%+ confidence were wrong.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/xjuntaro/status/2101989210362454268"><img src="https://pbs.twimg.com/media/HSvEC5qa8AAHqx3.jpg?name=orig" alt="Jev vs BERT on Kaggle" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/xjuntaro/status/2101989210362454268">Jev vs BERT on Kaggle</a></b><br><sub>xjuntaro · X · ♥ 556 · 2026-09-21</sub><br>Kaggle experiment finding zero-training Jev slightly below a fine-tuned BERT but on par with Fable and Astra and ahead of TF-IDF logistic regression, with Noul plus a tuned threshold scoring best.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/stash_pomichter/status/2101149600044224698"><img src="https://pbs.twimg.com/amplify_video_thumb/2101149070140014592/img/DdmO54VKkiBapiqs.jpg" alt="Jev robotics benchmark" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/stash_pomichter/status/2101149600044224698">Jev robotics benchmark</a></b><br><sub>stash_pomichter · X · ♥ 479 · 2026-09-19</sub><br>Benchmark giving Jev a robot body across 120 real and simulated navigation and spatial-reasoning tasks, graded on speed, cost, tokens, collisions and path quality against Dimcode, Astra, Fable, Opus and 5.6.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/NFT_Chen/status/2101253568774697099"><img src="https://pbs.twimg.com/amplify_video_thumb/2101252015779373056/img/an3uKosWqfYtwDq9.jpg" alt="Jev vs DeepSeek ticket routing" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/NFT_Chen/status/2101253568774697099">Jev vs DeepSeek ticket routing</a></b><br><sub>NFT_Chen · X · ♥ 170 · 2026-09-19</sub><br>Side-by-side routing of 500 real e-commerce support tickets: Jev cleared them in 83 seconds for $0.01, while DeepSeek V4.1 Flash had done 173 for $0.06 when stopped.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://quicqdev.github.io/Jev-vs-ML/"><img src="https://quicqdev.github.io/Jev-vs-ML/assets/benchmark-release-blue.png" alt="Jev vs. classical ML" width="240"></a></td>
<td valign="top"><b><a href="https://quicqdev.github.io/Jev-vs-ML/">Jev vs. classical ML</a></b><br><sub>QuicqDev · Article · ▲ 104 · 2026-09-20</sub><br>Eight datasets against eleven classical pipelines, strong on text such as IMDb reviews and weak on tabular data, with notebooks.<br><sub>Also: <a href="https://github.com/QuicqDev/Jev-vs-ML">repo</a> · <a href="https://www.reddit.com/r/LLMDevs/comments/1wlc11f/jev_vs_classical_ml_results_from_8_classification/">discussion</a> · <a href="https://www.reddit.com/r/LLMDevs/comments/1wlc11f/jev_vs_classical_ml_results_from_8_classification/">discussion 2</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/nateherk/status/2101368457698697511"><img src="https://pbs.twimg.com/media/HSmPYhAXQAAOaLo.jpg" alt="Jev on 12 real use cases" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/nateherk/status/2101368457698697511">Jev on 12 real use cases</a></b><br><sub>nateherk · Article · ♥ 163 · 2026-09-19</sub><br>Hands-on review across 12 automations: 1,000 emails through seven decision rules for about nine cents in six seconds after parallelizing, plus comments, meetings, clips and a BTC paper trader.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/Khazix0918/status/2100614133171552435"><img src="https://pbs.twimg.com/media/HSbgXI-agAAkxpB.png?name=orig" alt="AIHOT pre-filter comparison" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/Khazix0918/status/2100614133171552435">AIHOT pre-filter comparison</a></b><br><sub>Khazix0918 · X · ♥ 199 · 2026-09-17</sub><br>Benchmark of an is-this-AI-related pre-filter for AIHOT: Jev at a 30% threshold scored 98.91% versus 100% for GLM 5.3 Flash, and cost less than DeepSeek V4.1 Flash but twice Qwen3.7 Flash.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/enhanced_jp/status/2100741417593430233"><img src="https://pbs.twimg.com/media/HSbNhZvaUAEhxJx.jpg" alt="Rewriting rules changes Jev&#x27;s answers" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/enhanced_jp/status/2100741417593430233">Rewriting rules changes Jev's answers</a></b><br><sub>enhanced_jp · Article · ♥ 63 · 2026-09-18</sub><br>Japanese study of Jev as a judgment layer for a design harness, showing how clearer brand-guideline wording flips its answers; 9 test types, 650 calls and 4,819 judgments.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/iammrduncan/typesafe-ai-benchmark"><img src="https://opengraph.githubassets.com/1/iammrduncan/typesafe-ai-benchmark" alt="typesafe-ai-benchmark" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/iammrduncan/typesafe-ai-benchmark">typesafe-ai-benchmark</a></b><br><sub>iammrduncan · GitHub · ⭐ 37 · 2026-09-16</sub><br>Side-by-side benchmark of Qwen 3.8 27B structured output on Cerebras versus Jev across seven synthetic workloads, recording mistakes, latency, tokens, and estimated cost.<br><sub>Also: <a href="https://x.com/iamMrDuncan/status/2100467548298899918">demo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://www.reddit.com/r/accelerate/comments/1wik61b/tested_typesafeai_s_claim_that_their_new_model/"><img src="https://preview.redd.it/as1ajixqf0qh1.jpg?width=968&amp;format=pjpg&amp;auto=webp&amp;s=519a8b120c6b94bad81e9442e7deaafde9501f80" alt="Jev vs. Terra on knowledge benchmarks" width="240"></a></td>
<td valign="top"><b><a href="https://www.reddit.com/r/accelerate/comments/1wik61b/tested_typesafeai_s_claim_that_their_new_model/">Jev vs. Terra on knowledge benchmarks</a></b><br><sub>N8Programs · Reddit · ▲ 69 · 2026-09-17</sub><br>Compares Jev with GPT-5.6 Terra (reasoning off) on multiple-choice benchmarks such as MMLU, GPQA, WinoGrande, and HellaSwag; Jev is Terra-tier except on math.<br><sub>Also: <a href="https://x.com/N8Programs/status/2100088523403432357">source</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/kubornetes/status/2101709350264025407"><img src="https://res.cloudinary.com/zenn/image/upload/s--Z-HoZ4JJ--/c_fit%2Cg_north_west%2Cl_text:notosansjp-medium.otf_55:Jev%252C%2520Gemini%252C%2520DistilBERT%252C%2520LightGBM%25E3%2581%25AE%25E5%2588%2586%25E9%25A1%259E%25E6%2580%25A7%25E8%2583%25BD%25E3%2582%2592%25E6%25AF%2594%25E8%25BC%2583%25E3%2581%2597%25E3%2581%25A6%25E3%2581%25BF%25E3%2581%259F%2Cw_1010%2Cx_90%2Cy_100/g_south_west%2Cl_text:notosansjp-medium.otf_37:kubotaka%2Cx_203%2Cy_121/g_south_west%2Ch_90%2Cl_fetch:aHR0cHM6Ly9zdGF0aWMuemVubi5zdHVkaW8vdXNlci11cGxvYWQvYXZhdGFyLzU4YTA5ZTA2NzAuanBlZw==%2Cr_max%2Cw_90%2Cx_87%2Cy_95/v1627283836/default/og-base-w1200-v2.png?_a=BACMTiAE" alt="Jev vs Gemini, DistilBERT and LightGBM" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/kubornetes/status/2101709350264025407">Jev vs Gemini, DistilBERT and LightGBM</a></b><br><sub>kubornetes · X · ♥ 204 · 2026-09-20</sub><br>Japanese classification benchmark comparing Jev with Gemini, DistilBERT and LightGBM, concluding Jev is a safe default for classification tasks; experiment code is on GitHub.<br><sub>Also: <a href="https://zenn.dev/xxkuboxx/articles/e232d267a76f43">article</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/libukai/status/2100984923926728920"><img src="https://pbs.twimg.com/amplify_video_thumb/2100977858718113792/img/1cfiUtsApbmw3_sp.jpg" alt="Jev vs Gemini Flash Lite news tagging" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/libukai/status/2100984923926728920">Jev vs Gemini Flash Lite news tagging</a></b><br><sub>libukai · X · ♥ 163 · 2026-09-18</sub><br>Comparison on a 1,000-article test set of People's Daily news tagged for Hubei relevance: Jev took 0.35 s per article versus 3 s for Gemini Flash Lite, disagreeing on about 15%.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/everythingmeta/status/2101058921989390395"><img src="https://pbs.twimg.com/media/HSh0glmbQAAr0xv.jpg" alt="Jev on real-world search tasks at Parallel" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/everythingmeta/status/2101058921989390395">Jev on real-world search tasks at Parallel</a></b><br><sub>everythingmeta · Article · ♥ 159 · 2026-09-18</sub><br>Parallel's test of Jev on search reranking and related tasks, where zero-shot Jev matched at least one of their fine-tuned internal rerankers on NDCG@10.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/maxim-saplin/llm_chess"><img src="https://github.com/user-attachments/assets/4375a8a8-e226-4ed1-820f-86006d0404e2" alt="LLM Chess: Jev results" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/maxim-saplin/llm_chess">LLM Chess: Jev results</a></b><br><sub>maxim-saplin · GitHub · ⭐ 131 · 2026-09-17</sub><br>Long-running chess benchmark for LLMs that added Jev: across 80 games against a random player and Komodo Dragon it made zero illegal moves, winning 8 and drawing 22.<br><sub><b>How it uses Jev:</b> Jev picks each move from the legal options; about $0.0015 per game and an Elo estimate of about 243.</sub><br><sub>Also: <a href="https://maxim-saplin.github.io/llm_chess/">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/get-convex/convex-evals"><img src="https://raw.githubusercontent.com/get-convex/convex-evals/main/docs/assets/visualizer.png" alt="Convex decision model evals" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/get-convex/convex-evals">Convex decision model evals</a></b><br><sub>get-convex · GitHub · ⭐ 128 · 2025-01-10</sub><br>Benchmark of 106 decision questions drawn from 90 Convex coding evals that compares Jev via OpenRouter's decisions API against language models, recording probabilities, confidence and cost.<br><sub>Also: <a href="https://convex-evals.netlify.app/">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/vinilana/jev-eval-agent"><img src="https://opengraph.githubassets.com/1/vinilana/jev-eval-agent" alt="jev-eval-agent" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/vinilana/jev-eval-agent">jev-eval-agent</a></b><br><sub>vinilana · GitHub · ⭐ 103 · 2026-09-17</sub><br>Experiment with a personal-assistant agent and 100 mocked tools that counts the steps needed when the LLM picks tools itself versus when Jev picks the tool and the LLM only fills arguments.<br><sub><b>How it uses Jev:</b> Two-stage pruning over the tool catalog before every model step.</sub><br><sub>Also: <a href="https://x.com/oviniciuslana/status/2100610517886771393">demo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://www.reddit.com/r/LLMDevs/comments/1wkukle/i_tested_jev_on_nasa_kepler_signals/"><img src="https://external-preview.redd.it/YWw1cmdnb3Z5aXFoMcOMmaLg4COKusRl8Y9ue1_gcaRiXHaXsbLqmx3IvjD1.png?format=pjpg&amp;auto=webp&amp;s=aceae8acf90db6f7547287ef56382e02c1fd417e" alt="Jev on NASA Kepler signals" width="240"></a></td>
<td valign="top"><b><a href="https://www.reddit.com/r/LLMDevs/comments/1wkukle/i_tested_jev_on_nasa_kepler_signals/">Jev on NASA Kepler signals</a></b><br><sub>This_Cell_1829 · Reddit · ▲ 34 · 2026-09-19</sub><br>Test of Jev on 8,054 Kepler Objects of Interest, choosing confirmed planet, false positive, or candidate from 21 measurements; 54.2% vs a 64.4% rule baseline, 72.5% after reformatting inputs.<br><sub><b>How it uses Jev:</b> One Choice per signal over three labels; numbers were bucketed into labels in code for the second run.</sub><br><sub>Also: <a href="https://gist.github.com/ipaulsmith/e5c3ae3a492a455435d5bfc161404312">data</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/GoSailGlobal/status/2100877682972258619"><img src="https://pbs.twimg.com/amplify_video_thumb/2100877620292583424/img/7Ztuku-R01C1GvlU.jpg" alt="Jev reranking benchmark" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/GoSailGlobal/status/2100877682972258619">Jev reranking benchmark</a></b><br><sub>GoSailGlobal · X · ♥ 71 · 2026-09-18</sub><br>Benchmark of Jev as a search reranker on 33,047 Agent Skills Hub entries: alone it lifted NDCG@10 by only 0.012 over bge-m3, while RRF fusion of both reached 0.864.<br><sub><b>How it uses Jev:</b> Reranks bge-m3's top 30 results; also tested as a relevance judge against Haiku.</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/fstandhartinger/jevbench"><img src="https://raw.githubusercontent.com/fstandhartinger/jevbench/main/results/v1.2/charts/main-score.png" alt="JevBench" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/fstandhartinger/jevbench">JevBench</a></b><br><sub>fstandhartinger · GitHub · ⭐ 69 · 2026-09-19</sub><br>Third-party benchmark that runs 534 frozen decision questions and folds intelligence, calibration, speed, and cost into one score across Jev, open reimplementations, classifiers, and LLM baselines.<br><sub>Also: <a href="https://benchmarkheaven.com/jev-models">results</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/ShengyaoZhuang/status/2101212268440723895"><img src="https://pbs.twimg.com/media/HSj9xNobQAEf2w7.jpg?name=orig" alt="Jev as a reranker on DL19/DL20" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/ShengyaoZhuang/status/2101212268440723895">Jev as a reranker on DL19/DL20</a></b><br><sub>ShengyaoZhuang · X · ♥ 64 · 2026-09-19</sub><br>IR researchers test Jev as a pointwise, pairwise, setwise and listwise reranker over the top 100 BM25 results on TREC DL19 and DL20 and find it good and cheap.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/danielgshea/jev-as-a-judge"><img src="https://raw.githubusercontent.com/danielgshea/jev-as-a-judge/main/assets/benchmark-jev-luna-terra-sonnet-oracle/6d08df72-c878-458c-b7c5-a7824ee6e721/does-pass-accuracy.svg" alt="Jev as a judge" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/danielgshea/jev-as-a-judge">Jev as a judge</a></b><br><sub>danielgshea · GitHub · ⭐ 62 · 2026-09-17</sub><br>Experiment comparing Jev with GPT-5.6 Luna, GPT-5.6 Terra and Claude Sonnet 4.6 as judges of the same fixed agent runs, measuring binary accuracy, score reliability, cost and latency.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/GoSailGlobal/status/2100973279771246861"><img src="https://pbs.twimg.com/media/HSgn1l4aQAEqqvx.jpg" alt="Six experiments on Jev&#x27;s real limits" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/GoSailGlobal/status/2100973279771246861">Six experiments on Jev's real limits</a></b><br><sub>GoSailGlobal · Article · ♥ 50 · 2026-09-18</sub><br>Chinese write-up of six experiments across five open-source repos: Jev hits 0.83 AUC on tables with meaningful columns but 0.46 on hashed CTR data, and works best as a feature added to a baseline.<br><sub>Also: <a href="https://github.com/zhuyansen/jev-cold-start-prior">repo</a> · <a href="https://github.com/zhuyansen/jev-search-rerank-eval">repo2</a> · <a href="https://github.com/zhuyansen/jev-support-pulse">repo3</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/punk2898/status/2102218153766125851"><img src="https://pbs.twimg.com/media/HSuELanbUAAN3Kr.jpg" alt="$200 test of Jev" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/punk2898/status/2102218153766125851">$200 test of Jev</a></b><br><sub>punk2898 · Article · ♥ 16 · 2026-09-22</sub><br>Chinese evaluation that spent $200 running Jev against GPT-4.1-mini and GPT-5.6 Sol, Terra and Luna on 2,390 questions, including Chinese-language tasks, concluding the 100x cheaper claim roughly holds but 100x faster does not.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/malleshpai/status/2102207238236500096"><img src="https://pbs.twimg.com/media/HSyJp8GXsAAho-G.jpg" alt="Calibrating Jev" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/malleshpai/status/2102207238236500096">Calibrating Jev</a></b><br><sub>malleshpai · Article · ♥ 48 · 2026-09-22</sub><br>Economist's calibration study across five labeled tasks (about 37,000 items, 24 phrasings each), finding Jev's probabilities often overconfident and improved by an online Foster-Hart correction.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://www.reddit.com/r/machinelearningnews/comments/1wk8lwj/typed_decisions_jev_and_a_frozen_149m_encoder_on/"><img src="https://external-preview.redd.it/yYnCg7p4fjziFlw0ScTc8TfP2KiLGEV0p-BNnYEsjoM.png?auto=webp&amp;s=3d68cc22011896ecaf00d6c5e70f6cddd97feebb" alt="Typed Decisions benchmark" width="240"></a></td>
<td valign="top"><b><a href="https://www.reddit.com/r/machinelearningnews/comments/1wk8lwj/typed_decisions_jev_and_a_frozen_149m_encoder_on/">Typed Decisions benchmark</a></b><br><sub>asankhs · Reddit · ▲ 14 · 2026-09-19</sub><br>New 400-case benchmark for typed decisions where Jev scores 0.727, near the 0.735 teacher ceiling, against 0.646 for a frozen 149M ModernBERT encoder with small heads.<br><sub>Also: <a href="https://latentnode.pages.dev/articles/typed-decisions">article</a> · <a href="https://latentnode.pages.dev/articles/typed-decisions">project</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://news.ycombinator.com/item?id=49788402"><img src="https://archestra.ai/blog/2026-09-21-jev-model-comparison.webp" alt="Jev on 100 agent tool calls" width="240"></a></td>
<td valign="top"><b><a href="https://news.ycombinator.com/item?id=49788402">Jev on 100 agent tool calls</a></b><br><sub>arseny_info · Hacker News · ▲ 11 · 2026-09-21</sub><br>Archestra compares Jev, Sonnet 5, and open-weight models on 100 real Claude Code tool calls for its information-flow annotator, where always answering benign already scores 79%.<br><sub>Also: <a href="https://archestra.ai/blog/we-tested-jev-on-100-real-agent-calls">article</a> · <a href="https://archestra.ai/blog/we-tested-jev-on-100-real-agent-calls">project</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/silverstein/minutes/blob/main/tooling/voice-evals/jev.mjs"><img src="https://raw.githubusercontent.com/silverstein/minutes/main/docs/assets/demo.gif" alt="Minutes Jev voice evals" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/silverstein/minutes/blob/main/tooling/voice-evals/jev.mjs">Minutes Jev voice evals</a></b><br><sub>silverstein · GitHub · ⭐ 1.5k repo · 2026-03-18</sub><br>Synthetic qualification script in the Minutes meeting-memory app that tests Jev on seven Choice decisions its voice path needs, such as attendee constraints, semantic recall, verified pastes, stale targets and prompt injection.<br><sub>Also: <a href="https://useminutes.app">app</a> · <a href="https://github.com/silverstein/minutes">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/GoSailGlobal/status/2101259812709535800"><img src="https://pbs.twimg.com/media/HSksmBCbsAAlqY2.jpg" alt="Jev vs the BERT family" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/GoSailGlobal/status/2101259812709535800">Jev vs the BERT family</a></b><br><sub>GoSailGlobal · Article · ♥ 14 · 2026-09-19</sub><br>Chinese open experiment comparing Jev with zero-shot BERT-family classifiers on AG News, SST-2, Banking77, TweetEval, PAWS and a post-launch arXiv set, with 95% confidence intervals; Jev wins all 7 evaluation sets.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/stas_sorokin_/status/2101994942818115738"><img src="https://pbs.twimg.com/media/HSvJOjSWEAEtkH7.jpg?name=orig" alt="1,000 papers sorted then audited" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/stas_sorokin_/status/2101994942818115738">1,000 papers sorted then audited</a></b><br><sub>stas_sorokin_ · X · ♥ 6 · 2026-09-21</sub><br>Open rebuild of a Jev paper map: Jev sorted 1,000 AI papers into 24 topics for $0.0585, and Opus 5 as judge agreed on 85 of 100 labels at 153x the cost and 1.9s versus 57ms per paper.<br><sub><b>How it uses Jev:</b> One Choice over 24 topics per paper; its probability flags which labels an expensive model should recheck.</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/dreadnode/status/2102131162386710885"><img src="https://pbs.twimg.com/media/HSxDXD_WsAAL9_r.jpg?name=orig" alt="Jev on ScopeJudge" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/dreadnode/status/2102131162386710885">Jev on ScopeJudge</a></b><br><sub>dreadnode · X · ♥ 25 · 2026-09-21</sub><br>Security firm dreadnode ran Jev against its ScopeJudge benchmark for agent scope violations and found it competitive with leading LLM judges, at pennies per thousand checks and 130 ms average responses.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Zaious/jev-capability-atlas"><img src="https://opengraph.githubassets.com/1/Zaious/jev-capability-atlas" alt="Jev Capability Atlas" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Zaious/jev-capability-atlas">Jev Capability Atlas</a></b><br><sub>Zaious · GitHub · ⭐ 24 · 2026-09-18</sub><br>Bilingual, mostly Traditional Chinese evidence map of where Jev's calibrated-decision claim holds and where it breaks, built from real API-call receipts, test suites, and guides for agents.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/snakajima/bus20"><img src="https://opengraph.githubassets.com/1/snakajima/bus20" alt="Bus 2.0 dispatch benchmark" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/snakajima/bus20">Bus 2.0 dispatch benchmark</a></b><br><sub>snakajima · GitHub · ⭐ 21 · 2018-08-27</sub><br>Benchmark of online dispatch for an on-demand shared shuttle comparing Jev, local Laya, Claude, OpenAI and Gemini policies; its Jev notes show why arithmetic belongs in code (157.6 min² vs a 16.2 reference).<br><sub>Also: <a href="https://github.com/snakajima/bus20/blob/master/docs/jev-native.md">notes</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://nearhere.events/blog/typesafe-jev-mistral-gemini-event-validation"><img src="https://external-preview.redd.it/NzBRO0R5S7MxmGwz2RGsa-J3bzfP125gTZDRmnpWI-0.jpeg?auto=webp&amp;s=3fba8ca1c31a53433859005bc9aa4f74a6e5dea4" alt="Jev vs Mistral and Gemini for event validation" width="240"></a></td>
<td valign="top"><b><a href="https://nearhere.events/blog/typesafe-jev-mistral-gemini-event-validation">Jev vs Mistral and Gemini for event validation</a></b><br><sub>Near Here · Article · ▲ 7 · 2026-09-16</sub><br>Use-case study pitting Jev against Mistral Small 4 and Gemini 3.5 Flash-Lite at rejecting unsuitable local-event listings; Jev scored 96% (48/50) at 0.59s and $0.043 per 1,000 decisions.<br><sub><b>How it uses Jev:</b> Native Choice with probabilities on a listing's title and description.</sub><br><sub>Also: <a href="https://www.reddit.com/r/typesafe_ai/comments/1whtaq4/near_here_got_early_access_to_typesafe_jev_so_we/">discussion</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/backnotprop/status/2101713396966338575"><img src="https://pbs.twimg.com/media/HSrISHhaIAEDxM7.jpg?name=orig" alt="Jev jailbreak benchmark" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/backnotprop/status/2101713396966338575">Jev jailbreak benchmark</a></b><br><sub>backnotprop · X · ♥ 20 · 2026-09-20</sub><br>Prompt-injection benchmark pitting Jev against standard guardrail classifiers including Meta's: it wins an open suite and the newest attack set, loses on older sets and cannot hold a tight false-alarm budget.<br><sub>Also: <a href="https://backnotprop.com/blog/jev-guardrails">article</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/ilijabogunovic/status/2102075332014624819"><img src="https://pbs.twimg.com/media/HSwP1Z3XoAADcnY.png?name=orig" alt="Jev on LLM-Wikirace" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/ilijabogunovic/status/2102075332014624819">Jev on LLM-Wikirace</a></b><br><sub>ilijabogunovic · X · ♥ 19 · 2026-09-21</sub><br>Researchers ran Jev on their LLM-Wikirace benchmark (450 games, 8 hours, under $1 total) and found it fast and cheap but short on the world knowledge and planning of frontier LLMs.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/ShenSeanChen/status/2102234040535494876"><img src="https://pbs.twimg.com/amplify_video_thumb/2102216562342309888/img/30v3t9WGnQzugfFu.jpg" alt="Judgment arena" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/ShenSeanChen/status/2102234040535494876">Judgment arena</a></b><br><sub>ShenSeanChen · X · ♥ 18 · 2026-09-22</sub><br>Video that explains System 1 vs System 2 and races Jev against Claude Opus, Haiku 4.5 and GPT-5.4 Mini on 15 human-labelled questions; Opus got one more right but took 10x longer and cost 146x more.<br><sub>Also: <a href="https://github.com/ShenSeanChen/waku-agent">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/yibie/laya-jev-lab"><img src="https://pbs.twimg.com/media/HSo34y_W4AA1A3-.jpg" alt="laya-jev-lab" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/yibie/laya-jev-lab">laya-jev-lab</a></b><br><sub>yibie · GitHub · ⭐ 2 · 2026-09-20</sub><br>Independent measurements of Jev versus the open-weight Laya on an M4 Max, where Jev scored 78% and Laya 57% on 40 Chinese support tickets, plus a local-first cascade matching Jev's accuracy at about 1.8x the speed.<br><sub>Also: <a href="https://x.com/yibie/status/2101553680889598094">write-up</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/AbdelStark/jev-benchmarks"><img src="https://opengraph.githubassets.com/1/AbdelStark/jev-benchmarks" alt="jev-benchmarks" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/AbdelStark/jev-benchmarks">jev-benchmarks</a></b><br><sub>AbdelStark · GitHub · ⭐ 16 · 2026-09-17</sub><br>Probability-aware benchmark comparing Jev with GLiNER2.5 on zero-shot text classification, measuring calibration, coverage at a fixed error budget and latency on three BTZSC datasets.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/145k4/status/2100933101966758250"><img src="https://pbs.twimg.com/amplify_video_thumb/2100932546401812480/img/fPV392wDj1Xr1DHo.jpg" alt="Choice vs Noul trolley problems" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/145k4/status/2100933101966758250">Choice vs Noul trolley problems</a></b><br><sub>145k4 · X · ♥ 14 · 2026-09-18</sub><br>Runs a series of trolley problems through Jev as both a Choice and a Noul to test whether the question type changes its judgment.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/erendikmenn/jev-rag-benchmark"><img src="https://raw.githubusercontent.com/erendikmenn/jev-rag-benchmark/main/assets/benchmark/retrieval-errors.png" alt="jev-rag-benchmark" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/erendikmenn/jev-rag-benchmark">jev-rag-benchmark</a></b><br><sub>erendikmenn · GitHub · ⭐ 14 · 2026-09-19</sub><br>Reproducible benchmark of Jev as the reranker in a small RAG system on 1,044 Turkish XQuAD questions, measuring quality, latency and cost with the same 20 candidates given to every reranker.<br><sub>Also: <a href="https://x.com/ErenAILab/status/2101629475502817699">demo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/QuicqDev/Jev-vs-ML"><img src="https://opengraph.githubassets.com/1/QuicqDev/Jev-vs-ML" alt="Jev-vs-ML" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/QuicqDev/Jev-vs-ML">Jev-vs-ML</a></b><br><sub>QuicqDev · GitHub · ⭐ 13 · 2026-09-20</sub><br>Benchmark of Jev 1.13.0 against 11 classical classification pipelines on eight datasets with three seeds: Jev reaches 96.3% balanced accuracy on IMDb versus 88.4%, while classical models lead on tabular data.<br><sub>Also: <a href="https://quicqdev.github.io/Jev-vs-ML/">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://fatliverfreddy.substack.com/p/a-different-kind-of-model-for-ai"><img src="https://substackcdn.com/image/fetch/$s_!VnMM!,w_1200,h_675,c_fill,f_jpg,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6ee590d4-310d-43ca-b093-6d5960d53672_1734x907.png" alt="A different kind of model for AI observability" width="240"></a></td>
<td valign="top"><b><a href="https://fatliverfreddy.substack.com/p/a-different-kind-of-model-for-ai">A different kind of model for AI observability</a></b><br><sub>Avital Tamir · Article · ▲ 4 · 2026-09-18</sub><br>Labels 10,000 agent traces for status and sentiment in about 17 minutes for under a dollar and compares accuracy with an evaluation model.<br><sub>Also: <a href="https://news.ycombinator.com/item?id=49751140">discussion</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/hhilbig/polsci-open-bench"><img src="https://raw.githubusercontent.com/hhilbig/polsci-open-bench/main/output/figures/fig-jev-cost-latency.png" alt="polsci-open-bench" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/hhilbig/polsci-open-bench">polsci-open-bench</a></b><br><sub>hhilbig · GitHub · ⭐ 11 · 2026-04-27</sub><br>Benchmark of local and commercial LLMs on 33 political science classification tasks where Jev 1.13 scores a mean F1 of 0.661 versus 0.714 for Claude Opus 5, at $0.036 per 1,000 items and 0.27 s median latency.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://huggingface.co/datasets/Praveenrajus/jev-bench"><img src="https://huggingface.co/datasets/Praveenrajus/jev-bench/resolve/main/results/jev-1.13.0/figures/calibration_map.png" alt="jev-bench" width="240"></a></td>
<td valign="top"><b><a href="https://huggingface.co/datasets/Praveenrajus/jev-bench">jev-bench</a></b><br><sub>Praveenrajus · Hugging Face · ♥ 1 · 2026-09-20</sub><br>Human-labeled datasets reformatted into System One questions (22 configs, 166,054 rows), keeping human label distributions where they exist, with accuracy and calibration results for jev-1.13.0.<br><sub>Also: <a href="https://github.com/uspraveen/Jevify">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/brandonjcarl/status/2102064833256387016"><img src="https://pbs.twimg.com/media/HSwIy4gWgAAHsT-.jpg" alt="Putting Jev through the gauntlet" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/brandonjcarl/status/2102064833256387016">Putting Jev through the gauntlet</a></b><br><sub>brandonjcarl · Article · ♥ 1 · 2026-09-21</sub><br>Test of Jev across five areas and 25 subareas from elementary to PhD level: Jev scored 76% against DeepSeek v4.1 Flash's 93% at roughly 50 times lower cost, strongest at text classification.<br><sub>Also: <a href="https://essays.brandoncarl.com">blog</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://www.ramonov.com/blog/64-tiny-benchmarks-for-jev/"><img src="https://ramonov.com/og-default.png" alt="64 tiny benchmarks for Jev" width="240"></a></td>
<td valign="top"><b><a href="https://www.ramonov.com/blog/64-tiny-benchmarks-for-jev/">64 tiny benchmarks for Jev</a></b><br><sub>George Ramonov · Article · ▲ 3 · 2026-09-19</sub><br>Informal eval that sends 64 off-label questions to jev-1.13.0 50 times each (3,200 calls) and charts how stable the returned distributions are, including where the one-shot answer flips.<br><sub>Also: <a href="https://news.ycombinator.com/item?id=49777995">discussion</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"></td>
<td valign="top"><b><a href="https://mikulskibartosz.name/typesafe-jev-guess-what-i-drew">Jev guesses what I drew</a></b><br><sub>Bartosz Mikulski · Article · ▲ 3 · 2026-09-19</sub><br>Experiment that turns 400 hand-drawn sketches into text and asks Jev to name them: it beat chance by a wide margin, lost to Claude Sonnet 5, and answered airplane for more than half.<br><sub>Also: <a href="https://news.ycombinator.com/item?id=49768633">discussion</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://backnotprop.com/blog/jev-guardrails/"><img src="https://backnotprop.com/blog/jev-guardrails/og.png" alt="Jev jailbreak benchmark" width="240"></a></td>
<td valign="top"><b><a href="https://backnotprop.com/blog/jev-guardrails/">Jev jailbreak benchmark</a></b><br><sub>Mike Ramos · Article · ▲ 3 · 2026-09-20</sub><br>Pits one Noul per message against four local injection detectors, finding strong ranking but little recall at a 1% false-positive rate.<br><sub>Also: <a href="https://news.ycombinator.com/item?id=49777476">discussion</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://usenym.com/technical-blog/rebuilding-our-agent-with-jev"><img src="https://usenym.com/technical-blog/wren-jev-social-20260920.jpg" alt="Rebuilding Nym&#x27;s agent around Jev" width="240"></a></td>
<td valign="top"><b><a href="https://usenym.com/technical-blog/rebuilding-our-agent-with-jev">Rebuilding Nym's agent around Jev</a></b><br><sub>Nym · Article · ▲ 3 · 2026-09-20</sub><br>Replaces seven LLM reviewers and tool selection with Jev, falling back to a larger model when unsure, for a 4.1 to 5.7x speedup.<br><sub>Also: <a href="https://news.ycombinator.com/item?id=49779979">discussion</a> · <a href="https://usenym.com">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://www.southbridge.ai/blog/jev-entity-resolution"><img src="https://www.southbridge.ai/images/og/jev-entity-resolution.png" alt="System One models in high-throughput data pipelines" width="240"></a></td>
<td valign="top"><b><a href="https://www.southbridge.ai/blog/jev-entity-resolution">System One models in high-throughput data pipelines</a></b><br><sub>Southbridge AI · Article · ▲ 3 · 2026-09-20</sub><br>Entity resolution with Jev doing the bulk work and an LLM reviewing, at 226x lower cost; rewriting criteria as "what counts as sufficient evidence" fixed the dev set.<br><sub>Also: <a href="https://news.ycombinator.com/item?id=49771931">discussion</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/LargitData1/status/2101679703673454669"><img src="https://pbs.twimg.com/media/HSqqjJebkAA1Xbm.jpg?name=orig" alt="RAG agent routing benchmark" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/LargitData1/status/2101679703673454669">RAG agent routing benchmark</a></b><br><sub>LargitData1 · X · ♥ 8 · 2026-09-20</sub><br>Chinese benchmark of 100 multi-turn dialogs on whether an agent picks the right source (knowledge base, docs, web, tools, ask user): Gemma 4 31B 77.0%, Jev 61.4%, djev-spark 32.2%, SemIf 24.0%, Laya 0%.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/akafukusou/status/2100643727178092903"><img src="https://pbs.twimg.com/amplify_video_thumb/2100642936119836672/img/iQ5xCV_Yd2Z9QfUN.jpg" alt="Jev retrieval on QASPER" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/akafukusou/status/2100643727178092903">Jev retrieval on QASPER</a></b><br><sub>akafukusou · X · ♥ 7 · 2026-09-17</sub><br>Retrieval test on 34 QASPER questions where Jev beat pgvector with OpenAI text-embedding-3-small 17-3 (14 ties) on gold evidence coverage.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/carlaiau/jev-reranking"><img src="https://opengraph.githubassets.com/1/carlaiau/jev-reranking" alt="jev-reranking" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/carlaiau/jev-reranking">jev-reranking</a></b><br><sub>carlaiau · GitHub · ⭐ 7 · 2026-03-13</sub><br>Zero-shot reranking experiments comparing Jev with monoBERT and published TREC runs on MS MARCO and TREC-1 WSJ; on TREC DL 2021 documents Jev scored MAP 0.2790 and P@10 0.8930.<br><sub><b>How it uses Jev:</b> Scores overlapping windows of each document for relevance and keeps the highest window score (MaxP).</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/mahlernim/jev-korean-benchmark"><img src="https://raw.githubusercontent.com/mahlernim/jev-korean-benchmark/main/docs/figures/korean-check.png" alt="Jev in Korean" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/mahlernim/jev-korean-benchmark">Jev in Korean</a></b><br><sub>mahlernim · GitHub · ⭐ 6 · 2026-09-17</sub><br>Frozen, reproducible 100-question sample check of Jev on Korean text: reading comprehension scored 96 in Korean versus 97 in English, while fine-grained meaning judgments scored 76 versus 80.<br><sub>Also: <a href="https://ahn-lab.org/jev-korean-benchmark/">site</a> · <a href="https://ahn-lab.org/jev-korean-benchmark">write-up</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://backnotprop.com/blog/jev-poker/"><img src="https://backnotprop.com/blog/jev-poker/og.png" alt="Jev is the fish at the poker table" width="240"></a></td>
<td valign="top"><b><a href="https://backnotprop.com/blog/jev-poker/">Jev is the fish at the poker table</a></b><br><sub>Mike Ramos (backnotprop) · Article · ▲ 2 · 2026-09-17</sub><br>Poker probe showing Jev swinging 15 to 30 points when the same hand is relabelled and betting against a known made flush in 16 of 16 runs, as a warning against deploying it unevaluated.<br><sub>Also: <a href="https://news.ycombinator.com/item?id=49745212">discussion</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/wondertwins/jev-benchmark"><img src="https://raw.githubusercontent.com/wondertwins/jev-benchmark/main/runs/media/v2_jev_vs_sf0_tactical_filter_s4_jev-latest.gif" alt="jev-benchmark" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/wondertwins/jev-benchmark">jev-benchmark</a></b><br><sub>wondertwins · GitHub · ⭐ 6 · 2026-09-16</sub><br>Two Jev benchmarks: chess, where it plays at roughly 950 Elo only with code-supplied tactical facts, and deciding which game NPC a speech-to-text player is addressing, at F1 0.96 with precision 1.0.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/zhuyansen/jev-search-rerank-eval"><img src="https://opengraph.githubassets.com/1/zhuyansen/jev-search-rerank-eval" alt="jev-search-rerank-eval" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/zhuyansen/jev-search-rerank-eval">jev-search-rerank-eval</a></b><br><sub>zhuyansen · GitHub · ⭐ 6 · 2026-09-18</sub><br>Graded relevance evaluation of Jev Score reranking against keyword, BM25, bge-m3, embedding, and fusion baselines on 9,831 labeled pairs and 164 Chinese and English queries over the Agent Skills Hub catalog.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/teyhouse/jev-secret-detection"><img src="https://raw.githubusercontent.com/teyhouse/jev-secret-detection/main/assets/screenshot.png" alt="jev-secret-detection" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/teyhouse/jev-secret-detection">jev-secret-detection</a></b><br><sub>teyhouse · GitHub · ▲ 2 · 2026-09-17</sub><br>Benchmark of how well Jev spots real, usable secret credentials in 100 file snippets plus edge and config sets, reporting accuracy, AUC, and recall with no regex or provider verification.<br><sub><b>How it uses Jev:</b> One Noul per snippet compared against the expected label.</sub><br><sub>Also: <a href="https://www.reddit.com/r/LLMDevs/comments/1wiu1ej/typesafe_jev_secret_detection_test/">discussion</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/goodrahstar/pdf-race"><img src="https://opengraph.githubassets.com/1/goodrahstar/pdf-race" alt="PDF Race" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/goodrahstar/pdf-race">PDF Race</a></b><br><sub>goodrahstar · GitHub · ⭐ 6 · 2026-09-20</sub><br>Race of three document pipelines on 12 arXiv papers: Docling with Jev, Docling with Gemini 3.8 Flash, and Gemini reading the PDF; all scored 12/12, but the Jev lane cost $0.0022 versus $0.0882.<br><sub><b>How it uses Jev:</b> Jev's median decision was 388 ms per document versus 3,134 ms for Gemini on the same parsed text.</sub><br><sub>Also: <a href="https://pdf-race.vercel.app">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/gemanor/jev-code-review-benchmark"><img src="https://raw.githubusercontent.com/gemanor/jev-code-review-benchmark/main/docs/results/comparison.png" alt="Jev code review benchmark" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/gemanor/jev-code-review-benchmark">Jev code review benchmark</a></b><br><sub>gemanor · GitHub · ⭐ 5 · 2026-09-17</sub><br>Benchmark of Jev, Gemini Flash and Claude Fable checking Python code against four review rules over 360 calls each: Jev cost 45x less than Flash with a 0.75 s median, but scored 98% correctness versus 100%.<br><sub>Also: <a href="https://news.ycombinator.com/item?id=49744021">demo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/anessbelbati/jev-rerank-bench"><img src="https://raw.githubusercontent.com/anessbelbati/jev-rerank-bench/main/docs/readme-header.png" alt="jev-rerank-bench" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/anessbelbati/jev-rerank-bench">jev-rerank-bench</a></b><br><sub>anessbelbati · GitHub · ⭐ 5 · 2026-09-16</sub><br>Reranking benchmark of Jev against Cohere Rerank 4, ZeroEntropy zerank-2 and a chat-model baseline on 14 datasets; Jev's rubric averaged 0.692 against 0.691 for Cohere Pro, with no clear winner.<br><sub>Also: <a href="https://anessbelbati.com/lab/jev-reranking">write-up</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/identityTorn/status/2100475121324728615"><img src="https://pbs.twimg.com/media/HSZizHpasAABVQJ.jpg?name=orig" alt="Jev vs fine-tuned Qwen classifier" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/identityTorn/status/2100475121324728615">Jev vs fine-tuned Qwen classifier</a></b><br><sub>identityTorn · X · ♥ 3 · 2026-09-17</sub><br>Field note comparing zero-shot Jev with a fine-tuned Qwen classifier on an internal benchmark: within ~5 points of recall at matched precision, for about $70/mo at full volume.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/ielab/llm-rankers/tree/main/jev"><img src="https://opengraph.githubassets.com/1/ielab/llm-rankers" alt="llm-rankers Jev experiments" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/ielab/llm-rankers/tree/main/jev">llm-rankers Jev experiments</a></b><br><sub>ielab · GitHub · ⭐ 212 repo · 2023-10-14</sub><br>Zero-shot TREC DL19/DL20 experiments using Jev as a pointwise, pairwise, setwise and listwise reranker; listwise Score over all 100 BM25 passages in one request reached nDCG@10 0.728 on DL19 at $0.0009 per query.<br><sub><b>How it uses Jev:</b> Score questions beat Choice questions everywhere; all 100 candidates fit in a single request because output is free.</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/chunxiaoxx/nautilus-compass/blob/main/docs/wall/GENESIS_HOSTED_JEV_CALIBRATION.md"><img src="https://opengraph.githubassets.com/1/chunxiaoxx/nautilus-compass" alt="Hosted Jev calibration study" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/chunxiaoxx/nautilus-compass/blob/main/docs/wall/GENESIS_HOSTED_JEV_CALIBRATION.md">Hosted Jev calibration study</a></b><br><sub>chunxiaoxx · GitHub · ⭐ 207 repo · 2026-04-27</sub><br>Reproducible calibration study of hosted jev-1.13.0 on 240 seeded questions (92.2% accuracy, Brier 0.048, ECE 0.041 on Noul items), plus a 200-question adversarial follow-up with ECE 0.012.<br><sub>Also: <a href="https://github.com/chunxiaoxx/nautilus-compass/blob/main/docs/wall/GENESIS_HOSTED_JEV_ADVCAL.md">adversarial</a> · <a href="https://github.com/chunxiaoxx/nautilus-compass/tree/main/runtime/jev_advcal_20260922">code</a> · <a href="https://github.com/chunxiaoxx/nautilus-compass">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/scienthoon/jev-ood-calibration"><img src="https://opengraph.githubassets.com/1/scienthoon/jev-ood-calibration" alt="Does Jev know when it does not know?" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/scienthoon/jev-ood-calibration">Does Jev know when it does not know?</a></b><br><sub>scienthoon · GitHub · ⭐ 4 · 2026-09-19</sub><br>Calibration test of Jev on 900 rule-generated support tickets it cannot have seen plus three public benchmarks, with raw responses: near calibrated on the public sets, overconfident where the rule is unknowable.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/chenmingtang830/jevarena"><img src="https://jevarena-lab.vercel.app/og-image.png" alt="JevArena" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/chenmingtang830/jevarena">JevArena</a></b><br><sub>chenmingtang830 · GitHub · ⭐ 4 · 2026-09-19</sub><br>Bring-your-own-key arena that pits Jev against another judge model from OpenRouter on your question and takes your vote before revealing which was which, along with latency and cost.<br><sub>Also: <a href="https://jevarena-lab.vercel.app">app</a> · <a href="https://jevarena-lab.vercel.app">app 2</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://www.reddit.com/r/LocalLLM/comments/1wl0wyr/benchmarked_typesafes_decision_model_jev_vs/"><img src="https://external-preview.redd.it/nGd0jUCYN79vEjP-jsIWFeaYmT1rlyOztmJb1MN8jcM.png?auto=webp&amp;s=212db4efbf345f508cce40389cae7198a105d8f9" alt="DecaState Jev vs frontier LLMs" width="240"></a></td>
<td valign="top"><b><a href="https://www.reddit.com/r/LocalLLM/comments/1wl0wyr/benchmarked_typesafes_decision_model_jev_vs/">DecaState Jev vs frontier LLMs</a></b><br><sub>Super_Public_8335 · Reddit · ▲ 1 · 2026-09-19</sub><br>Benchmark of Jev against four frontier LLMs on 36 support-triage decisions from US-West and Singapore: about 176x cheaper and 9x faster than GPT-6 Astra, with 0 type errors.<br><sub>Also: <a href="https://github.com/tempomesh/DecaState">repo</a> · <a href="https://github.com/tempomesh/decastate">project</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://idlerambling.substack.com/p/does-jev-have-politics-yes"><img src="https://substackcdn.com/image/fetch/$s_!59CN!,w_1200,h_675,c_fill,f_jpg,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9ecaa9e3-e48f-441a-aa60-c8bfb02c6734_1790x1458.png" alt="Does Jev have politics? (Yes)" width="240"></a></td>
<td valign="top"><b><a href="https://idlerambling.substack.com/p/does-jev-have-politics-yes">Does Jev have politics? (Yes)</a></b><br><sub>Idle Rambling · Article · ▲ 1 · 2026-09-20</sub><br>Runs Political Compass propositions through Jev as Choice questions and finds stable political positions that match most LLMs, arguing it is a new probabilistic mask on the same underlying model.<br><sub>Also: <a href="https://news.ycombinator.com/item?id=49781262">discussion</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/goya4140/jev-reward-model-evaluation"><img src="https://raw.githubusercontent.com/goya4140/jev-reward-model-evaluation/main/assets/headline_comparison.svg" alt="Jev 1.13 as a Reward Model" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/goya4140/jev-reward-model-evaluation">Jev 1.13 as a Reward Model</a></b><br><sub>goya4140 · GitHub · ⭐ 3 · 2026-09-20</sub><br>Reproducible evaluation of Jev 1.13 as a reward model, LLM judge and process verifier across eight benchmark tracks and 40,940 examples, with an interactive report of 54 SOTA comparisons.<br><sub>Also: <a href="https://goya4140.github.io/jev-reward-model-evaluation/">report</a> · <a href="https://goya4140.github.io/jev-reward-model-evaluation">write-up</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/RINNECODER/jev-behavior-study"><img src="https://opengraph.githubassets.com/1/RINNECODER/jev-behavior-study" alt="jev-behavior-study" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/RINNECODER/jev-behavior-study">jev-behavior-study</a></b><br><sub>RINNECODER · GitHub · ⭐ 3 · 2026-09-16</sub><br>Independent field guide to Jev 1.13.0 behavior from 11,621 text-study requests, 3 Snake studies, and a 3D City lab, showing where framing changes answers and harder tasks fail.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/jmanhype/jev-dspy-lab"><img src="https://opengraph.githubassets.com/1/jmanhype/jev-dspy-lab" alt="jev-dspy-lab" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/jmanhype/jev-dspy-lab">jev-dspy-lab</a></b><br><sub>jmanhype · GitHub · ⭐ 3 · 2026-09-17</sub><br>Companion lab for DSPy pipelines that records and replays TypeSafe calls to measure Jev calibration, selective risk, confidence-gated abstention, latency, tokens, and modeled cost offline.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/SamuelSacco/jev-exploration"><img src="https://opengraph.githubassets.com/1/SamuelSacco/jev-exploration" alt="jev-exploration" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/SamuelSacco/jev-exploration">jev-exploration</a></b><br><sub>SamuelSacco · GitHub · ⭐ 3 · 2026-09-17</sub><br>Evidence ledger of Jev claims that recomputes public calibration results against sample-size noise and runs an 800-item difficulty gradient, finding the probabilities are not calibrated at any difficulty.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/anisselbd/jev-phishing-bench"><img src="https://opengraph.githubassets.com/1/anisselbd/jev-phishing-bench" alt="jev-phishing-bench" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/anisselbd/jev-phishing-bench">jev-phishing-bench</a></b><br><sub>anisselbd · GitHub · ⭐ 3 · 2026-09-16</sub><br>Reproducible benchmark of Jev versus Claude Haiku 4.5 on whether an email agent should click the link in 2,000 emails, where Jev scored 62.6% accuracy to Haiku's 81.3%, with a calibration audit.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/jevals/jevals-data"><img src="https://repository-images.githubusercontent.com/1376455544/1e0c26c8-9ea1-4d3a-a162-dec02fa78fe1" alt="Jevals" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/jevals/jevals-data">Jevals</a></b><br><sub>jevals · GitHub · ▲ 1 · 2026-09-18</sub><br>Independent benchmark data comparing Jev with six LLMs on PubMedQA, Banking77 and HelpSteer2 against human labels, covering accuracy, calibration, cost and latency.<br><sub><b>How it uses Jev:</b> Release 2026-09-18: Jev tied the best LLM on PubMedQA yes/no at 1/28 of the price and tied for second on Banking77; no model beat guessing on HelpSteer2.</sub><br><sub>Also: <a href="https://jevals.com">app</a> · <a href="https://jevals.com/">app 2</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://www.southbridge.ai/blog/jev-watching-the-agents"><img src="https://www.southbridge.ai/images/og/jev-watching-the-agents.png" alt="Models watching models" width="240"></a></td>
<td valign="top"><b><a href="https://www.southbridge.ai/blog/jev-watching-the-agents">Models watching models</a></b><br><sub>Southbridge AI · Article · ▲ 1 · 2026-09-19</sub><br>Flags risky calls across 220,000 agent tool calls, shows that encoding tricks slip past it, and finds worded scales beat 1-to-100 ratings.<br><sub>Also: <a href="https://news.ycombinator.com/item?id=49783694">discussion</a> · <a href="https://x.com/hrishioa/status/2101842370052669903">post</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/miptgirl/miptgirl_medium/tree/main/jev"><img src="https://opengraph.githubassets.com/1/miptgirl/miptgirl_medium" alt="Jev classification benchmarks" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/miptgirl/miptgirl_medium/tree/main/jev">Jev classification benchmarks</a></b><br><sub>miptgirl · GitHub · ⭐ 109 repo · 2023-01-28</sub><br>Notebooks benchmarking Jev on Banking77 intent classification and StackExchange data against GPT models; on 1,000 Banking77 samples Jev scored 0.790 accuracy versus 0.862 for gpt-5.6-luna.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/TokenTrim/jev-agent-failure-benchmark"><img src="https://raw.githubusercontent.com/TokenTrim/jev-agent-failure-benchmark/main/figures/whowhen_jev_vs_llm.png" alt="jev-agent-failure-benchmark" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/TokenTrim/jev-agent-failure-benchmark">jev-agent-failure-benchmark</a></b><br><sub>TokenTrim · GitHub · ⭐ 2 · 2026-09-17</sub><br>Benchmark of Jev on the 6,257 text traces of Who&amp;When Pro, attributing multi-agent failures to an agent, step and error type; Jev beat GPT-5.4 on every axis for ~$1.28 total.<br><sub><b>How it uses Jev:</b> Three Choice questions per trace over candidate agents, steps and error types.</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/jgridifier/jev-research-eval"><img src="https://opengraph.githubassets.com/1/jgridifier/jev-research-eval" alt="jev-research-eval" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/jgridifier/jev-research-eval">jev-research-eval</a></b><br><sub>jgridifier · GitHub · ⭐ 2 · 2026-09-17</sub><br>Reproducible eval harness and field note for research-browser tasks run with jev-ultrafast, with 11 baseline cases, human and quant stress suites, QC grades, a suite runner and a report generator.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/TokenTrim/jev-routing-experiment"><img src="https://raw.githubusercontent.com/TokenTrim/jev-routing-experiment/main/results/llmrb_frontier.png" alt="jev-routing-experiment" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/TokenTrim/jev-routing-experiment">jev-routing-experiment</a></b><br><sub>TokenTrim · GitHub · ⭐ 2 · 2026-09-17</sub><br>Tests Jev as an LLM router on LLMRouterBench and RouterArena; a Jev-difficulty plus retrieval router scored 62.4% vs 60.3% for the best single model, but a no-Jev ablation matched it.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Gaurav-Gosain/jev-sec-bench"><img src="https://raw.githubusercontent.com/Gaurav-Gosain/jev-sec-bench/main/docs/overview.png" alt="jev-sec-bench" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Gaurav-Gosain/jev-sec-bench">jev-sec-bench</a></b><br><sub>Gaurav-Gosain · GitHub · ⭐ 2 · 2026-09-16</sub><br>Blind security benchmarks for jev-1.13.0 with a Go runner and TUI: 96.5% accuracy on all 662 deepset prompt-injection messages at a plain 0.50 cut, plus 200 vulnerable-code pairs.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/dhruv_ko/status/2102185971332878453"><img src="https://pbs.twimg.com/media/HSx241aacAAAYyH.jpg" alt="Jev vs LLMs, BERT and Laya" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/dhruv_ko/status/2102185971332878453">Jev vs LLMs, BERT and Laya</a></b><br><sub>dhruv_ko · Article · ♥ 1 · 2026-09-21</sub><br>Healthcare voice-AI team benchmarks Jev against Claude Sonnet 5, GPT-5-mini, a fine-tuned BERT and two open-weight models on 1,500 examples, finding near-frontier accuracy at 1/50th the cost.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/nekuda-ai/WindTunnel/tree/main/experiments/jev"><img src="https://raw.githubusercontent.com/nekuda-ai/WindTunnel/main/assets/charts/balanced-leaderboard.svg" alt="WindTunnel Jev experiments" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/nekuda-ai/WindTunnel/tree/main/experiments/jev">WindTunnel Jev experiments</a></b><br><sub>nekuda-ai · GitHub · ⭐ 76 repo · 2026-07-27</sub><br>WebMCP benchmark runs where Jev picks browser actions and Mercury writes arguments and answers: via WebMCP the pair solved 49/49 tasks at a $0.0011 median per run, versus 25/49 through DOM control.<br><sub>Also: <a href="https://github.com/nekuda-ai/WindTunnel">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/phuryn/experiments/tree/main/jev-decisions-api"><img src="https://opengraph.githubassets.com/1/phuryn/experiments" alt="Is Jev cheaper and better?" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/phuryn/experiments/tree/main/jev-decisions-api">Is Jev cheaper and better?</a></b><br><sub>phuryn · GitHub · ⭐ 52 repo · 2026-06-10</sub><br>Reproducible invoice-classification test on 50 documents built so surface cues mislead: Jev scored 50/50 at $0.025 per 1,000 decisions, tied with Claude Haiku 4.5, while two open models scored 48/50.<br><sub>Also: <a href="https://github.com/phuryn/experiments">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Adkid-Zephyr/chinese-workflow-decision-bench"><img src="https://raw.githubusercontent.com/Adkid-Zephyr/chinese-workflow-decision-bench/main/assets/xiaohongshu-scorecard-3x4.png" alt="chinese-workflow-decision-bench" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Adkid-Zephyr/chinese-workflow-decision-bench">chinese-workflow-decision-bench</a></b><br><sub>Adkid-Zephyr · GitHub · ⭐ 1 · 2026-09-21</sub><br>Feishu-style Chinese message classification benchmark with 64 frozen synthetic scenarios, where Jev classified 64/64 on a single Choice versus 20/64 for Laya, with latencies and raw responses published.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/shibadogcap/kyotsu-ai-bench"><img src="https://opengraph.githubassets.com/1/shibadogcap/kyotsu-ai-bench" alt="Common Test AI comparison" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/shibadogcap/kyotsu-ai-bench">Common Test AI comparison</a></b><br><sub>shibadogcap · GitHub · ⭐ 1 · 2026-09-16</sub><br>Static dashboard comparing Jev with OpenAI luna, terra, and sol variants on 836 questions across 23 subjects of Japan's 2026 university entrance Common Test, including speed and cost.<br><sub>Also: <a href="https://jev-luna-kyotsu-bench.shibadogcap.com">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://huggingface.co/spaces/aahf/JevBenchmark"><img src="https://huggingface.co/spaces/aahf/JevBenchmark/resolve/main/assets/cost_quality.png" alt="Jev Benchmark (ads)" width="240"></a></td>
<td valign="top"><b><a href="https://huggingface.co/spaces/aahf/JevBenchmark">Jev Benchmark (ads)</a></b><br><sub>aahf · App · ♥ 1 · 2026-09-17</sub><br>Research article comparing Jev with GPT-5.6 Sol and four XGBoost baselines on four synthetic ad outcomes: similar aggregate quality at about 64x lower estimated API cost and 5.4x lower median latency.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/CompleteDotTech/paper-package"><img src="https://opengraph.githubassets.com/1/CompleteDotTech/paper-package" alt="Jev research paper package" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/CompleteDotTech/paper-package">Jev research paper package</a></b><br><sub>CompleteDotTech · GitHub · ⭐ 1 · 2026-09-18</sub><br>Reproducible research package on improving Jev decisions: entity-matching macro-F1 rose from 0.9605 to 0.9859 on 413 DBLP-ACM pairs, while SciFact relation verification showed no resolved gain.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/jjd-lab/jev-synthetic-survey"><img src="https://jjd-lab.github.io/jev-synthetic-survey/assets/og.png" alt="Jev synthetic survey" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/jjd-lab/jev-synthetic-survey">Jev synthetic survey</a></b><br><sub>jjd-lab · GitHub · ⭐ 1 · 2026-09-20</sub><br>Study running Jev and GPT-4.1 as the same 300 synthetic respondents over 24,596 Twin-2K-500 cells, finding that asking yes/no items as a Noul mattered more than the model gap, at a thirty-fourth of the cost.<br><sub>Also: <a href="https://jjd-lab.github.io/jev-synthetic-survey/">article</a> · <a href="https://jjd-lab.github.io/jev-synthetic-survey">write-up</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/henrylove0/status/2102239256093794663"><img src="https://pbs.twimg.com/media/HSynVzubYAAgXmA.png?name=orig" alt="Jev vs Laya head to head" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/henrylove0/status/2102239256093794663">Jev vs Laya head to head</a></b><br><sub>henrylove0 · X · ♥ 1 · 2026-09-22</sub><br>Side-by-side run of Jev against the open Laya model showing Laya is much faster while Jev makes much better judgments.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/cruzex100/status/2102202098968666432"><img src="https://pbs.twimg.com/media/HSyFqylbgAAxJYA.jpg?name=orig" alt="Jev vs Laya smoke test" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/cruzex100/status/2102202098968666432">Jev vs Laya smoke test</a></b><br><sub>cruzex100 · X · ♥ 1 · 2026-09-22</sub><br>Quick side-by-side of Jev and the open Laya model: accuracy 0.727 for Jev, soft accuracy 0.580 vs 0.471, ECE 0.144 vs 0.213, latency ~710ms vs ~30-40ms, and ~$0.0004 vs ~$0 per decision.</td>
</tr>
<tr>
<td width="260" valign="top"></td>
<td valign="top"><b><a href="https://gist.github.com/ipaulsmith/e5c3ae3a492a455435d5bfc161404312">Jev x NASA Kepler</a></b><br><sub>ipaulsmith · GitHub · ⭐ 1</sub><br>Retrospective test of Jev 1.13 on 8,054 historical Kepler Objects of Interest with archive dispositions hidden, matching 72.5% of them against 64.4% for a fixed 3-rule baseline.<br><sub><b>How it uses Jev:</b> Publishes the exact requests, metrics, baseline and caveats.</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/themsquared/jev-benchmark"><img src="https://webofmike.com/images/og-default.png" alt="jev-benchmark" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/themsquared/jev-benchmark">jev-benchmark</a></b><br><sub>themsquared · GitHub · ⭐ 1 · 2026-09-17</sub><br>Reproducible benchmark of Jev classifying agent tool calls as readonly, destructive, privileged or exfiltration, measuring accuracy, latency and whether its confidence is worth routing on, with raw results committed.<br><sub>Also: <a href="https://webofmike.com/jev-benchmark/">writeup</a> · <a href="https://webofmike.com/jev-benchmark">write-up</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/baibizhe/jev-decision-benchmarks"><img src="https://opengraph.githubassets.com/1/baibizhe/jev-decision-benchmarks" alt="jev-decision-benchmarks" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/baibizhe/jev-decision-benchmarks">jev-decision-benchmarks</a></b><br><sub>baibizhe · GitHub · ⭐ 1 · 2026-09-19</sub><br>Independent evaluation of Jev 1.13 on MetaTool, When2Call, and BFCL V4 tool-selection and abstention tasks, with bilingual comparison tables against ChatGPT, Claude, Qwen, and others.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/4esv/jev-eval"><img src="https://raw.githubusercontent.com/4esv/jev-eval/main/results/confidence.png" alt="jev-eval" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/4esv/jev-eval">jev-eval</a></b><br><sub>4esv · GitHub · ⭐ 1 · 2026-09-18</sub><br>Harness that benchmarks Jev against any OpenRouter model or local checkpoint on labeled classification data for accuracy, calibration, latency, and cost, with results versus GPT-5.6 Terra, open-jev, Kev-0.8B, and Laya.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/copyleftdev/jev-labs"><img src="https://opengraph.githubassets.com/1/copyleftdev/jev-labs" alt="jev-labs" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/copyleftdev/jev-labs">jev-labs</a></b><br><sub>copyleftdev · GitHub · ⭐ 1 · 2026-09-19</sub><br>TLA+-verified consensus kernel around Jev, generated into Rust and run through 1,680 simulated pharmacy decisions under seeded chaos against the live API, with zero wrong verdicts and more escalations as evidence degrades.<br><sub>Also: <a href="https://www.youtube.com/watch?v=C_l8FI1oddE">video</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/zsavage8/padflow-jev-evals"><img src="https://opengraph.githubassets.com/1/zsavage8/padflow-jev-evals" alt="padflow-jev-evals" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/zsavage8/padflow-jev-evals">padflow-jev-evals</a></b><br><sub>zsavage8 · GitHub · ⭐ 1 · 2026-09-17</sub><br>Public benchmark of typed decisions a land-development SaaS makes in production, such as routing incoming documents to projects, with JSON schemas, anonymized labeled rows and a runner for OpenAI-compatible models.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/markfive-proto/typesafe-vs-deepseek"><img src="https://opengraph.githubassets.com/1/markfive-proto/typesafe-vs-deepseek" alt="typesafe-vs-deepseek" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/markfive-proto/typesafe-vs-deepseek">typesafe-vs-deepseek</a></b><br><sub>markfive-proto · GitHub · ⭐ 1 · 2026-09-18</sub><br>Side-by-side comparison of Jev and DeepSeek flash on speed, tokens, cost and accuracy across invoice extraction, email classification and reranking, plus fraud, guardrail and reconciliation pipelines.<br><sub>Also: <a href="https://typesafe-vs-deepseek.vercel.app">app</a> · <a href="https://typesafe-vs-deepseek.vercel.app">app 2</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/alp82/goodwatch-monorepo/tree/main/docs/benchmarks/fingerprint/jev"><img src="https://opengraph.githubassets.com/1/alp82/goodwatch-monorepo" alt="GoodWatch Jev fingerprint experiment" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/alp82/goodwatch-monorepo/tree/main/docs/benchmarks/fingerprint/jev">GoodWatch Jev fingerprint experiment</a></b><br><sub>alp82 · GitHub · ⭐ 38 repo · 2026-09-17</sub><br>Case study from the GoodWatch movie-discovery app testing Jev for 74 per-title trait scores: 10 to 25 times faster but a 2.65-point mean gap to reviewed Qwen scores, so the team decided not to adopt it.<br><sub><b>How it uses Jev:</b> Compared ten-level and six-level Score ladders, presence Nouls and batch sizes from 1 to 222 questions per request.</sub><br><sub>Also: <a href="https://github.com/alp82/goodwatch-monorepo">repo</a> · <a href="https://github.com/alp82/goodwatch-monorepo/blob/main/docs/adr/0001-no-jev-for-fingerprint-scoring.md">adr</a> · <a href="https://goodwatch.app/">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/hakari-bench/hakari-bench/blob/main/docs/typesafe_reranker_evaluation.md"><img src="https://opengraph.githubassets.com/1/hakari-bench/hakari-bench" alt="HAKARI-Bench Jev reranker" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/hakari-bench/hakari-bench/blob/main/docs/typesafe_reranker_evaluation.md">HAKARI-Bench Jev reranker</a></b><br><sub>hakari-bench · GitHub · ⭐ 32 repo · 2026-04-30</sub><br>Jev integration in HAKARI-Bench, a lightweight IR benchmark over 35+ benchmark groups, that ranks documents by Noul relevance probabilities in listwise or pointwise mode with jev-1.13.0 pinned.<br><sub>Also: <a href="https://github.com/hakari-bench/hakari-bench">repo</a> · <a href="https://huggingface.co/spaces/hakari-bench/leaderboard">leaderboard</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/brcampidelli/chimera-agent/blob/main/bench/jev_decisions/RESULTS.md"><img src="https://opengraph.githubassets.com/1/brcampidelli/chimera-agent" alt="Chimera Jev governance benchmark" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/brcampidelli/chimera-agent/blob/main/bench/jev_decisions/RESULTS.md">Chimera Jev governance benchmark</a></b><br><sub>brcampidelli · GitHub · ⭐ 26 repo · 2026-06-30</sub><br>Preregistered benchmark in the Chimera agent repo comparing Jev (a danger Noul plus a block/review/allow Choice) with a DeepSeek judge and verbalized probabilities; Jev reached 0.903 AUROC on ambiguous items.<br><sub>Also: <a href="https://github.com/brcampidelli/chimera-agent">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/ucsandman/claude-harness/blob/main/labs/claude-mods/experiments/jev/FINDINGS.md"><img src="https://opengraph.githubassets.com/1/ucsandman/claude-harness" alt="Jev skill suggestion on real transcripts" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/ucsandman/claude-harness/blob/main/labs/claude-mods/experiments/jev/FINDINGS.md">Jev skill suggestion on real transcripts</a></b><br><sub>ucsandman · GitHub · ⭐ 24 repo · 2026-08-13</sub><br>Measurement of Jev picking the right skill per turn over 407 skills and 356 turns mined from 838 Claude Code transcripts: 73.3% wrong loads vs 96.5% for a keyword baseline, with first-call recall identified as the ceiling.<br><sub>Also: <a href="https://github.com/ucsandman/claude-harness">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/ibm-client-engineering/output-drift-financial-llms/blob/main/paper/arxiv_dfah_bench_v3/v3_extension.tex"><img src="https://opengraph.githubassets.com/1/ibm-client-engineering/output-drift-financial-llms" alt="DFAH-Bench Jev gate condition" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/ibm-client-engineering/output-drift-financial-llms/blob/main/paper/arxiv_dfah_bench_v3/v3_extension.tex">DFAH-Bench Jev gate condition</a></b><br><sub>ibm-client-engineering · GitHub · ⭐ 18 repo · 2025-11-02</sub><br>Research extension of IBM Client Engineering's DFAH-Bench for financial agents that compares action gates: structural checks alone, an LLM's allow/block/review JSON judgment, and Jev's typed choice with class probabilities.<br><sub>Also: <a href="https://github.com/ibm-client-engineering/output-drift-financial-llms">repo</a> · <a href="https://ibm-client-engineering.github.io/output-drift-financial-llms/">site</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/getaskclaw/amber/tree/main/decision-axis"><img src="https://opengraph.githubassets.com/1/getaskclaw/amber" alt="AMBER decision-axis evals" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/getaskclaw/amber/tree/main/decision-axis">AMBER decision-axis evals</a></b><br><sub>getaskclaw · GitHub · ⭐ 15 repo · 2026-08-20</sub><br>Evaluation pipeline in the AMBER replay benchmark for decision models such as Jev, reporting per-family accuracy, calibration bins, ECE, threshold sweeps and cost/latency from HMAC-signed records.<br><sub>Also: <a href="https://github.com/getaskclaw/amber">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/XiaoConstantine/sgrep/tree/main/bench/jev"><img src="https://raw.githubusercontent.com/XiaoConstantine/sgrep/main/docs/static/architecture.jpg" alt="sgrep Jev rerank benchmark" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/XiaoConstantine/sgrep/tree/main/bench/jev">sgrep Jev rerank benchmark</a></b><br><sub>XiaoConstantine · GitHub · ⭐ 15 repo · 2025-11-25</sub><br>Isolated benchmark in sgrep, a local semantic search tool for codebases and coding-agent history, that routes Jev through its reranking boundary and compares it with local Jina, ColBERT and other rerankers on a pinned dspy-go index.<br><sub>Also: <a href="https://github.com/XiaoConstantine/sgrep">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/daiwk/auto-research/tree/main/src/auto_research/system_one"><img src="https://opengraph.githubassets.com/1/daiwk/auto-research" alt="auto-research System One" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/daiwk/auto-research/tree/main/src/auto_research/system_one">auto-research System One</a></b><br><sub>daiwk · GitHub · ⭐ 14 repo · 2026-07-13</sub><br>Research module that implements the Choice/Score/Noul contract and runs Banking77 and public-suite evaluations of Jev against a local calibrated scorer and the NanoJev, Nimble and Laya checkpoints.<br><sub><b>How it uses Jev:</b> Dependency-free TypeSafe HTTP provider behind the same contracts as the local and open-checkpoint backends, plus a catalog of 48 community implementations.</sub><br><sub>Also: <a href="https://github.com/daiwk/auto-research">repo</a> · <a href="https://github.com/daiwk/auto-research/blob/main/docs/system-one/README.md">docs</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://huggingface.co/datasets/emretheus/jev-rag-benchmark"><img src="https://cdn-thumbnails.huggingface.co/social-thumbnails/datasets/emretheus/jev-rag-benchmark.png" alt="Jev RAG Benchmark" width="240"></a></td>
<td valign="top"><b><a href="https://huggingface.co/datasets/emretheus/jev-rag-benchmark">Jev RAG Benchmark</a></b><br><sub>emretheus · Hugging Face · ⬇ 21 · 2026-09-20</sub><br>Frozen-candidate RAG evaluation of Jev 1.13 as reranker against OpenJev and an NVIDIA cross-encoder: on SciFact Jev reaches 79.29% nDCG@10 vs 78.70%, at about 4 s vs 307 ms p50 latency.<br><sub>Also: <a href="https://github.com/emretheus/jev-rag-benchmark">project</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/bryansparks/armature/tree/main/examples/decision-typesafe"><img src="https://raw.githubusercontent.com/bryansparks/armature/main/demo-hero.gif" alt="Armature TypeSafe decision A/B" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/bryansparks/armature/tree/main/examples/decision-typesafe">Armature TypeSafe decision A/B</a></b><br><sub>bryansparks · GitHub · ⭐ 9 repo · 2026-05-07</sub><br>A/B benchmark inside the Armature agent harness on 20 labeled code-review statements: Jev scored 0.87 overall versus 0.98 for a qwen3.6-27b judge, at 260 ms versus 20,591 ms per call.<br><sub>Also: <a href="https://armature.now">app</a> · <a href="https://github.com/bryansparks/armature">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/ensemblr-hq/ensemblr/blob/master/docs/considerations/jev-decision-layer.md"><img src="https://raw.githubusercontent.com/ensemblr-hq/ensemblr/master/assets/wordmark.gif" alt="Ensemblr Jev decision layer study" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/ensemblr-hq/ensemblr/blob/master/docs/considerations/jev-decision-layer.md">Ensemblr Jev decision layer study</a></b><br><sub>ensemblr-hq · Docs · ⭐ 8 repo · 2026-06-04</sub><br>Design proposal and spike for using Jev in a desktop orchestrator for Pi and Claude Code to pick agent roles, rate difficulty and flag duplicates; rejected after a corrected rerun that still did not support production use.<br><sub>Also: <a href="https://github.com/ensemblr-hq/ensemblr">repo</a> · <a href="https://github.com/ensemblr-hq/ensemblr/blob/master/docs/considerations/jev-spike-runbook.md">runbook</a> · <a href="https://www.ensemblr.dev">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/hevmind/status/2101110454785614219"><img src="https://hevmind.com/og-image.png" alt="Jev as a reranker (hev mind)" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/hevmind/status/2101110454785614219">Jev as a reranker (hev mind)</a></b><br><sub>hevmind · X · ▶ 32 · 2026-09-19</sub><br>Untuned Jev reranker reaches 0.501 mean nDCG@10 versus Voyage rerank-3's 0.504, with a prompt tuned only on SciFact's train split.<br><sub>Also: <a href="https://hevmind.com/writing/jev-as-a-reranker/">article</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/fstandhartinger/model-market-comparison/tree/main/ops/ux-2026-09-12/jevbench"><img src="https://raw.githubusercontent.com/fstandhartinger/model-market-comparison/main/public/brand/wordmark.svg" alt="JevBench (Benchmark Heaven)" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/fstandhartinger/model-market-comparison/tree/main/ops/ux-2026-09-12/jevbench">JevBench (Benchmark Heaven)</a></b><br><sub>fstandhartinger · GitHub · ⭐ 5 repo · 2026-06-15</sub><br>Benchmark for Jev and Jev-like decision models inside Benchmark Heaven, an LLM price and benchmark comparison site, with public and held-out task splits reported separately.<br><sub>Also: <a href="https://github.com/fstandhartinger/model-market-comparison">repo</a> · <a href="https://benchmarkheaven.com">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://zenn.dev/acrosstudioblog/articles/a62c066d5d9938"><img src="https://res.cloudinary.com/zenn/image/upload/s--DfX5i98Y--/c_fit%2Cg_north_west%2Cl_text:notosansjp-medium.otf_55:%25E6%2596%2587%25E7%25AB%25A0%25E3%2582%2592%25E7%2594%259F%25E6%2588%2590%25E3%2581%2597%25E3%2581%25AA%25E3%2581%2584AI%25E3%2580%258CJev%25E3%2580%258D%25E3%2582%2592%25E6%2597%25A5%25E6%259C%25AC%25E8%25AA%259E%25E3%2581%25A748%25E5%259B%259E%25E8%25A9%25A6%25E3%2581%2597%25E3%2581%259F%25E3%2580%2582%25E9%2580%259F%25E3%2581%2595%25E3%2582%2588%25E3%2582%258A%25E9%259D%25A2%25E7%2599%25BD%25E3%2581%258B%25E3%2581%25A3%25E3%2581%259F%25E3%2581%25AE%25E3%2581%25AF%25E3%2580%258C%25E8%25BF%25B7%25E3%2581%2584%25E3%2580%258D%2Cw_1010%2Cx_90%2Cy_100/g_south_west%2Cl_text:notosansjp-medium.otf_34:%25E3%2582%25B7%25E3%2583%25B3%25E3%2582%25A6%25E3%2583%2595%25E3%2583%25A0%2528wooheum%2520xin%2529%2Cx_220%2Cy_108/bo_3px_solid_rgb:d6e3ed%2Cg_south_west%2Ch_90%2Cl_fetch:aHR0cHM6Ly9zdGF0aWMuemVubi5zdHVkaW8vdXNlci11cGxvYWQvYXZhdGFyLzQxMjhmMzRjMjIuanBlZw==%2Cr_20%2Cw_90%2Cx_92%2Cy_102/co_rgb:6e7b85%2Cg_south_west%2Cl_text:notosansjp-medium.otf_30:Acrosstudio%25E3%2583%2586%25E3%2583%2583%25E3%2582%25AF%25E3%2583%2596%25E3%2583%25AD%25E3%2582%25B0%2Cx_220%2Cy_160/bo_4px_solid_white%2Cg_south_west%2Ch_50%2Cl_fetch:aHR0cHM6Ly9zdGF0aWMuemVubi5zdHVkaW8vdXNlci11cGxvYWQvYXZhdGFyLzgwMjc2NjQyOTMuanBlZw==%2Cr_max%2Cw_50%2Cx_139%2Cy_84/v1627283836/default/og-base-w1200-v2.png?_a=BACMTiAE" alt="48 Japanese calls to Jev" width="240"></a></td>
<td valign="top"><b><a href="https://zenn.dev/acrosstudioblog/articles/a62c066d5d9938">48 Japanese calls to Jev</a></b><br><sub>Wooheum Xin (Acrosstudio) · Article · 2026-09-18</sub><br>Japanese test of 16 synthetic support messages sent 3 times each via OpenRouter with three questions per call: 48 calls at a median 286 ms for about $0.00146 total, with low confidence where labels disagreed.</td>
</tr>
<tr>
<td width="260" valign="top"></td>
<td valign="top"><b><a href="https://evals.typesafe.ai/agent_trace_observability">Agent Trace Observability workflow eval</a></b><br><sub>TypeSafe AI · Docs</sub><br>Official workflow eval for triaging finished support-agent traces into follow-ups; Jev scores 71.6% at $0.0003 and 0.5 s per case versus Opus 5's 75.2% at $0.1033 and 27.4 s.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://lindfors.no/blog/a-first-look-at-typesafes-jev/"><img src="https://lindfors.no/og/a-first-look-at-typesafes-jev.png" alt="An early-access test of Jev" width="240"></a></td>
<td valign="top"><b><a href="https://lindfors.no/blog/a-first-look-at-typesafes-jev/">An early-access test of Jev</a></b><br><sub>Emil Lindfors · Article · 2026-09-18</sub><br>Scores Norwegian documents with Score questions at about $0.22 per thousand and finds that longer, more detailed questions hurt calibration.<br><sub><b>How it uses Jev:</b> Score questions over 24 Norwegian public-hearing responses.</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/jourdanlabs/assay-001"><img src="https://opengraph.githubassets.com/1/jourdanlabs/assay-001" alt="ASSAY-001" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/jourdanlabs/assay-001">ASSAY-001</a></b><br><sub>jourdanlabs · GitHub · 2026-09-17</sub><br>Pre-registered check of Jev's calibration and type-safety claims: calibrated on CLINC150 (ECE 0.0204), overconfident on Banking77 (ECE 0.0936), and zero type errors across 8,576 responses, with full logs.<br><sub>Also: <a href="https://donttrustme.ai/assay-001.html">article</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"></td>
<td valign="top"><b><a href="https://donttrustme.ai/assay-001.html">ASSAY-001: Jev calibration</a></b><br><sub>donttrustme.ai (JourdanLabs) · Article · 2026-09-17</sub><br>Pre-registered check of Jev's calibration and type-safety claims on Banking77 and CLINC150: calibrated on CLINC150 (ECE 0.0204) but overconfident on Banking77 (ECE 0.0936), with zero type errors in 8,576 responses.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://frederickparsons.substack.com/p/can-a-fast-ai-gate-catch-chemistry"><img src="https://substackcdn.com/image/fetch/$s_!WNmT!,w_1200,h_675,c_fill,f_jpg,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbafd27fe-42f4-4a3d-8ee9-16131e778995_1663x795.png" alt="Can a fast AI gate catch chemistry mistakes?" width="240"></a></td>
<td valign="top"><b><a href="https://frederickparsons.substack.com/p/can-a-fast-ai-gate-catch-chemistry">Can a fast AI gate catch chemistry mistakes?</a></b><br><sub>Frederick Parsons · Article · 2026-09-19</sub><br>A literature-claim gate that stopped all 42 bad claims at a 95% threshold, with an honest account of where molecule checks failed.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://zenn.dev/nwn/articles/824026c76116e0"><img src="https://res.cloudinary.com/zenn/image/upload/s--nA63RXC3--/c_fit%2Cg_north_west%2Cl_text:notosansjp-medium.otf_55:TypeSafe%25E3%2581%25AEJev%25E3%2582%2592%25E6%25AD%25A3%25E3%2581%2597%25E3%2581%258F%25E9%25A9%259A%25E3%2581%258F%25E3%2580%2581%25E3%2581%259D%25E3%2582%258C%25E3%2581%25A3%25E3%2581%25A6LLM%25E3%2581%25A7%25E3%2581%25A7%25E3%2581%258D%25E3%2581%25BE%25E3%2581%259B%25E3%2582%2593%25E3%2581%258B%25EF%25BC%259F%2Cw_1010%2Cx_90%2Cy_100/g_south_west%2Cl_text:notosansjp-medium.otf_37:%25E3%2583%25A8%2Cx_203%2Cy_121/g_south_west%2Ch_90%2Cl_fetch:aHR0cHM6Ly9zdGF0aWMuemVubi5zdHVkaW8vdXNlci11cGxvYWQvYXZhdGFyLzllY2U3NmI3N2IuanBlZw==%2Cr_max%2Cw_90%2Cx_87%2Cy_95/v1627283836/default/og-base-w1200-v2.png?_a=BACMTiAE" alt="Can&#x27;t an LLM do what Jev does?" width="240"></a></td>
<td valign="top"><b><a href="https://zenn.dev/nwn/articles/824026c76116e0">Can't an LLM do what Jev does?</a></b><br><sub>nwn · Article · 2026-09-17</sub><br>Japanese article that reproduces Jev's parallel-decision trick with first-token logits on Gemma3 270M (77x faster than JSON output) and compares Jev with LLMs on a public Mario-playing harness.</td>
</tr>
<tr>
<td width="260" valign="top"></td>
<td valign="top"><b><a href="https://evals.typesafe.ai/customer_service">Customer Service workflow eval</a></b><br><sub>TypeSafe AI · Docs</sub><br>Official workflow eval for choosing a support assistant's next actions on a customer turn; Jev scores 76.0% at $0.0001 and 0.4 s per case versus Opus 5's 72.4% at $0.0579 and 16.6 s.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/willkelly/jev-evaluation"><img src="https://opengraph.githubassets.com/1/willkelly/jev-evaluation" alt="Evaluating jev" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/willkelly/jev-evaluation">Evaluating jev</a></b><br><sub>willkelly · GitHub · 2026-09-20</sub><br>Pre-registered adversarial evaluation of jev-1.13.0 with nine experiments and 28 predictions fixed before any data, run as 123,805 requests for $12.69, plus a 13-rule prompting guide drawn from the results.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/thodoh1/FinancialPredictionJev"><img src="https://opengraph.githubassets.com/1/thodoh1/FinancialPredictionJev" alt="FinancialPredictionJev" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/thodoh1/FinancialPredictionJev">FinancialPredictionJev</a></b><br><sub>thodoh1 · GitHub · 2026-09-16</sub><br>Single Python script that asks a Jev Noul whether SPY closes up the next day from yfinance data, then scores accuracy, Brier score, ROC-AUC and calibration against a baseline.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://kasra.blog/blog/classification-and-jev/"><img src="https://images.kasra.blog/images/wp-content/2026/09/jev-side-quests-og-v5.png" alt="Fine-tuning side quests Jev could have removed" width="240"></a></td>
<td valign="top"><b><a href="https://kasra.blog/blog/classification-and-jev/">Fine-tuning side quests Jev could have removed</a></b><br><sub>Kasra Rahjerdi · Article · 2026-09-18</sub><br>Filters 120,633 training examples with three Nouls in 23 minutes for $3.47.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://thoughts.jock.pl/p/jev-typesafe-system-one-model-benchmark-2026"><img src="https://substackcdn.com/image/fetch/$s_!aY6v!,w_1200,h_675,c_fill,f_jpg,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F880b6867-fc92-4181-9cac-73aeaf966630_2048x2048.png" alt="I ran 40 tickets through Jev and four models" width="240"></a></td>
<td valign="top"><b><a href="https://thoughts.jock.pl/p/jev-typesafe-system-one-model-benchmark-2026">I ran 40 tickets through Jev and four models</a></b><br><sub>Pawel Jozefiak · Article · 2026-09-21</sub><br>Runs 40 support tickets through Jev and four text models: Jev answered in 370 ms for two hundredths of a cent, was 10x faster and 329x cheaper than Claude Fable 5.1, and beat it on customer annoyance.</td>
</tr>
<tr>
<td width="260" valign="top"></td>
<td valign="top"><b><a href="https://evals.typesafe.ai/invoice_processing">Invoice Processing workflow eval</a></b><br><sub>TypeSafe AI · Docs</sub><br>Official workflow eval for deciding whether and how an invoice can be paid; Jev scores 61.8% at $0.0011 and 0.5 s per case versus Opus 5's 78.4% at $0.4856 and 92.1 s.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://vercel.com/blog/ai-gateway-jev-model-launch"><img src="https://assets.vercel.com/image/upload/contentful/image/e5382hct74si/22MYVE2v97ZfHKIqNx5Sw6/d0e7b0b67c61e51ff3b8ca27ce16cf87/sep-og-blog-jev-launch_2x.jpg" alt="Jev adoption on Vercel AI Gateway" width="240"></a></td>
<td valign="top"><b><a href="https://vercel.com/blog/ai-gateway-jev-model-launch">Jev adoption on Vercel AI Gateway</a></b><br><sub>Vercel · Article · 2026-09-18</sub><br>First-day adoption data from Vercel AI Gateway: within 24 hours nearly 13% of paid teams were using Jev, about 2x the GPT-5.6 family and more than 6x Fable 5.1's share.<br><sub>Also: <a href="https://news.ycombinator.com/item?id=49774164">discussion</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://www.mindstudio.ai/blog/jev-system-one-model-classification"><img src="https://i.mscdn.ai/o/iZl0kkZU2R9KXyy7/a/3V2ICO3oSq2QZPii/generated-images/1f03e98a-0622-4dcb-b094-a54da1a98c90.png?fm=auto&amp;w=1200&amp;h=630&amp;fit=crop" alt="Jev AI Tested" width="240"></a></td>
<td valign="top"><b><a href="https://www.mindstudio.ai/blog/jev-system-one-model-classification">Jev AI Tested</a></b><br><sub>MindStudio (Luis Chavez-Mattos) · Article · 2026-09-18</sub><br>Hands-on test of Jev 1.13.0 on eight synthetic cases covering ticket routing, negation, prompt injection, an 'other' option, and latency, with notes on where it holds up and where it does not.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://huggingface.co/datasets/clduab11/jev-calibration-statistics"><img src="https://huggingface.co/datasets/clduab11/jev-calibration-statistics/resolve/main/calibration.png" alt="Jev calibration statistics" width="240"></a></td>
<td valign="top"><b><a href="https://huggingface.co/datasets/clduab11/jev-calibration-statistics">Jev calibration statistics</a></b><br><sub>clduab11 · Hugging Face · 2026-09-21</sub><br>Confidence statistics from a retrieval benchmark judged by jev-1.13.0: its scores separate answer-bearing passages (AUROC 0.899), yet the Jev-judged pipeline scored 0.612 vs 0.740 with no judge.<br><sub>Also: <a href="https://github.com/clduab11/jev-test">project</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/ghubnab99/jev-enterprise-decision-fabric"><img src="https://opengraph.githubassets.com/1/ghubnab99/jev-enterprise-decision-fabric" alt="Jev Enterprise Decision Fabric" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/ghubnab99/jev-enterprise-decision-fabric">Jev Enterprise Decision Fabric</a></b><br><sub>ghubnab99 · GitHub · 2026-09-19</sub><br>Experimental .NET architecture that routes many semantic decisions through one validated path, with a labelled 111-case benchmark of Jev versus a structured-output Claude baseline on agent actions and a decision inspector.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/vehas/thaiexam-jev-charts"><img src="https://opengraph.githubassets.com/1/vehas/thaiexam-jev-charts" alt="Jev on ThaiExam" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/vehas/thaiexam-jev-charts">Jev on ThaiExam</a></b><br><sub>vehas · GitHub · 2026-09-17</sub><br>Chart pages comparing jev-1.13.0 with 110 other models on Thai standardized exams: 70.7% accuracy on 567 questions at 0.35 s and $0.000029 per question, with 7.5 pp calibration error.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/hegargarcia/jev-playground"><img src="https://opengraph.githubassets.com/1/hegargarcia/jev-playground" alt="Jev Playground" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/hegargarcia/jev-playground">Jev Playground</a></b><br><sub>hegargarcia · GitHub · 2026-09-17</sub><br>Benchmark playground that pits Jev against Luna, Haiku and Gemini at choosing moves in explicit-state games, where game code owns the rules and legal actions and each model only picks among them.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://huggingface.co/spaces/emretheus/jev-rag-benchmark-leaderboard"><img src="https://cdn-thumbnails.huggingface.co/social-thumbnails/spaces/emretheus/jev-rag-benchmark-leaderboard.png" alt="Jev RAG benchmark leaderboard" width="240"></a></td>
<td valign="top"><b><a href="https://huggingface.co/spaces/emretheus/jev-rag-benchmark-leaderboard">Jev RAG benchmark leaderboard</a></b><br><sub>emretheus · App · 2026-09-20</sub><br>Static leaderboard of real runs comparing Jev 1.13, OpenJev and an NVIDIA cross-encoder as rerankers on English XQuAD and SciFact RAG tasks.<br><sub>Also: <a href="https://github.com/emretheus/jev-rag-benchmark">project</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://medium.com/data-science-collective/i-tested-typesafes-jev-a-470-cheaper-decision-model-against-claude-gpt-6-kimi-minimax-and-d36ed152e861"><img src="https://miro.medium.com/v2/resize:fit:700/1*2bVSI4gUCmeUCE_-7obOAA.jpeg" alt="Jev vs Claude, GPT-6, Kimi, MiniMax and DeepSeek" width="240"></a></td>
<td valign="top"><b><a href="https://medium.com/data-science-collective/i-tested-typesafes-jev-a-470-cheaper-decision-model-against-claude-gpt-6-kimi-minimax-and-d36ed152e861">Jev vs Claude, GPT-6, Kimi, MiniMax and DeepSeek</a></b><br><sub>Manjunath Janardhan · Article · 2026-09-19</sub><br>Runs the same 200 typed decisions through Jev and five frontier LLMs, comparing accuracy and cost and checking how each handles cases where human raters disagree.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/mameli/jev-vs-luna"><img src="https://raw.githubusercontent.com/mameli/jev-vs-luna/main/assets/benchmark-overview.png" alt="Jev vs Luna" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/mameli/jev-vs-luna">Jev vs Luna</a></b><br><sub>mameli · GitHub · 2026-09-18</sub><br>Reproducible benchmark comparing Jev via OpenRouter's Decisions API with GPT-5.6 Luna on classifying reviews by topic, sentiment, stars, reply need, and product defects, with accuracy, latency, and cost.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://towardsdatascience.com/a-new-kind-of-model-for-ai-decision-making/"><img src="https://assets.insightmediagroup.io/media/1789719149842_24br2e.webp" alt="Jev vs OpenAI on intent classification" width="240"></a></td>
<td valign="top"><b><a href="https://towardsdatascience.com/a-new-kind-of-model-for-ai-decision-making/">Jev vs OpenAI on intent classification</a></b><br><sub>Mariya Mansurova (Towards Data Science) · Article · 2026-09-21</sub><br>Compares Jev with two OpenAI models on the 77-class Banking77 intent dataset: 79.0% accuracy vs 83.9% and 86.2%, almost 2x faster, with well-calibrated confidence; cutting to 7 labels closes the gap.<br><sub>Also: <a href="https://github.com/miptgirl/miptgirl_medium/tree/main/jev">code</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"></td>
<td valign="top"><b><a href="https://www.reddit.com/r/ClaudeAI/comments/1wj3lsw/i_thought_id_found_a_model_5000x_cheaper_than/">Jev web form filling benchmark</a></b><br><sub>imaxalpha · Reddit · 2026-09-17</sub><br>Harness testing Jev on three real web forms, from a 13-step insurance wizard to a Lever job application; at $0.001-$0.006 per form it finished 0 of 13 steps and 7 of 11 fields.<br><sub><b>How it uses Jev:</b> Per-step action Choice without planning; the rerun shows why multi-step forms need a planner.</sub><br><sub>Also: <a href="https://gist.github.com/Tienduyvo/83c28649595e909d675e4fc60efe85e0">data</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/andreaserradev-gbj/jev-access-day"><img src="https://raw.githubusercontent.com/andreaserradev-gbj/jev-access-day/main/demo/assets/og-card.png" alt="jev-access-day" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/andreaserradev-gbj/jev-access-day">jev-access-day</a></b><br><sub>andreaserradev-gbj · GitHub · 2026-09-19</sub><br>Learning scaffold with an eval harness comparing Jev against an LLM stand-in on 24 real operational decisions, with numbers reproducible from committed run files and an interactive results page.<br><sub>Also: <a href="https://jev-access-day.vercel.app/">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/marcosmartinez/jev-acento"><img src="https://raw.githubusercontent.com/marcosmartinez/jev-acento/main/figures/reliability_paired_es.png" alt="jev-acento" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/marcosmartinez/jev-acento">jev-acento</a></b><br><sub>marcosmartinez · GitHub · 2026-09-20</sub><br>Pre-registered audit of Jev on Spanish over 3,200 paired human-labeled items: a Spanish state cost accuracy on every dataset, up to 6.4 pp on XNLI, while Spanish instructions changed nothing; includes a CLI to rerun it.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Gaurav-Gosain/jev-alpha-bench"><img src="https://opengraph.githubassets.com/1/Gaurav-Gosain/jev-alpha-bench" alt="jev-alpha-bench" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Gaurav-Gosain/jev-alpha-bench">jev-alpha-bench</a></b><br><sub>Gaurav-Gosain · GitHub · 2026-09-16</sub><br>Two studies on whether Jev predicts stock returns from news headlines or price candles: same-day rank IC of +0.24 falls to -0.008 by the next close, and a long-short book loses 18 bps a trade after costs.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/thijmenkam/jev-benchmarks"><img src="https://opengraph.githubassets.com/1/thijmenkam/jev-benchmarks" alt="jev-benchmarks (thijmenkam)" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/thijmenkam/jev-benchmarks">jev-benchmarks (thijmenkam)</a></b><br><sub>thijmenkam · GitHub · 2026-09-17</sub><br>Reproducible harness that asks Jev and frontier LLMs identical typed questions about the same state and scores accuracy, calibration, consistency, latency, cost, and schema validity, with a 150-call-per-model run.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/jujumilk3/jev-calibration-audit"><img src="https://opengraph.githubassets.com/1/jujumilk3/jev-calibration-audit" alt="jev-calibration-audit" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/jujumilk3/jev-calibration-audit">jev-calibration-audit</a></b><br><sub>jujumilk3 · GitHub · 2026-09-18</sub><br>Independent API-only calibration audit of Jev in seven experiments (~7,000 calls): removing the abstain option drops accuracy on unanswerable items from 0.950 to 0.000, while Korean leaves calibration unchanged.<br><sub><b>How it uses Jev:</b> Also finds no option-order bias and no interference from bundling 16 questions.</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/nikkoxgonzales/jev-certify"><img src="https://raw.githubusercontent.com/nikkoxgonzales/jev-certify/main/docs/risk-coverage.svg" alt="jev-certify" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/nikkoxgonzales/jev-certify">jev-certify</a></b><br><sub>nikkoxgonzales · GitHub · 2026-09-21</sub><br>Toolkit and CLINC150 study that turns Jev's probabilities into routing thresholds via conformal risk control and audits them with prediction-powered inference: 2,412 decisions for $0.23, including where the bound breaks.</td>
</tr>
</table>

<details><summary>23 more</summary>

- **[jev-demos](https://github.com/Bud-ro/jev-demos)** · <sub>Bud-ro · GitHub · 2026-09-17</sub><br>Dart maze experiments testing Jev's spatial lookahead: asked for up to 100 future moves per request it solved zero mazes, but with adjacent-tile hints and one next-move question it solved 6/10 5x5 mazes.
- **[jev-eval](https://github.com/Shogo-nfrealmusic/jev-eval)** · <sub>Shogo-nfrealmusic · GitHub · 2026-09-18</sub><br>Third-party comparison of Jev with gpt-4o-mini and Claude Sonnet 4.5 under identical conditions on routing 60 synthetic booking inquiries in 4 languages for a photo-shoot service in Japan.
- **[jev-headline-bench](https://github.com/Gaurav-Gosain/jev-headline-bench)** · <sub>Gaurav-Gosain · GitHub · 2026-09-16</sub><br>Tests whether jev-1.13.0, seeing only the two headlines, can pick the winner of real Upworthy A/B tests: 64.5% on 10,984 randomized experiments, rising to 74.7% when the difference was decisive.
- **[jev-measured](https://github.com/WallerChen/jev-measured)** · <sub>WallerChen · GitHub · 2026-09-19</sub><br>Reproducible measurements of cost, latency and raw output from the live Jev API via OpenRouter across eight use cases, plus a small head-to-head on 27 support tickets; the whole run cost under one cent.
- **[jev-orderby-bench](https://github.com/yodablocks/jev-orderby-bench)** · <sub>yodablocks · GitHub · 2026-09-19</sub><br>Independent measurement of whether SQL ORDER BY over a Jev probability gives a defensible order: jev-1.13.0 passed six pre-registered gates on 360 labeled rows but failed four of six on graded product relevance.
- **[jev-packs](https://github.com/dtduc-git/jev-packs)** · <sub>dtduc-git · GitHub · 2026-09-19</sub><br>Registry of Jev question packs (questions, golden cases, pinned models, measured evidence) plus Jev Bench, which scores jev-1.13.0, claude-sonnet-5 and a local Qwen on the same labels with accuracy, ECE, cost and latency.
- **[jev-report](https://github.com/HackSing/jev-report)** · <sub>HackSing · GitHub · 2026-09-17</sub><br>Independent Chinese research report on Jev: a 52-page PDF that traces vendor numbers to their sources, plus 50 Chinese test cases where 86 of 90 judgments were correct (95.6%) with ECE 0.070.
- **[jev-shadcn-lint-eval](https://github.com/blas0/jev-shadcn-lint-eval)** · <sub>blas0 · GitHub · 2026-09-17</sub><br>Second eval for shadcn-ui/lint that asks Jev whether each of 131 rule test cases is right and whether its message says what to change; Jev caught 91% of real violations but was weaker on clean code.
- **[jev-spam-eval](https://github.com/bitnovus/jev-spam-eval)** · <sub>bitnovus · GitHub · 2026-09-17</sub><br>Zero-shot ham/spam/phishing classification with Jev: 98.64% on 5,733 emails from written category definitions versus 98.87% for a TF-IDF model trained on ~4,600 labels per fold.
- **[jev-trace-classifier](https://github.com/sypherin/jev-trace-classifier)** · <sub>sypherin · GitHub · 2026-09-17</sub><br>Tests whether a Jev Noul can tell agent-written from human-written pages on all 4,579 collusion.wiki pages, head-to-head with a local Qwen model; Jev reached 0.741 accuracy against a 77.6% majority baseline.
- **[Jev: 62.6% asked once, 95% split five ways](https://www.beri.net/article/typesafe-jev-typed-decision-model-calibration-decomposition-shadow-eval)** · <sub>Rajesh Beri · Article · 2026-09-21</sub><br>Roundup of independent tests: Jev ran 12-27x cheaper than Claude Haiku 4.5 on a 2,000-email phishing test, scored 62.6% with one question and 95.0% split into five, and showed miscalibrated probabilities.
- **[Mini-Vibe Check](https://every.to/also-true-for-humans/mini-vibe-check-typesafe-s-jev-judged-everything-i-ve-written-in-0-7-seconds)** · <sub>Mike Taylor (Every) · Article · 2026-09-15</sub><br>Hands-on review where Jev made 777 judgments over 37 of the author's articles in 0.7 seconds for a quarter of a cent, catching six of seven planted defects to Fable's seven.
- **[One judge call or twelve dimension scores?](https://agentjournal.dev/blog/llm-judge-vs-feature-extraction/)** · <sub>ikkun · Article · 2026-09-17</sub><br>Measures a single direct Jev question per row against 12-14 Jev-scored dimensions with locally fitted weights on three classification tasks, using 34.1M input tokens for $1.43.
- **[Security Incidents workflow eval](https://evals.typesafe.ai/security_incidents)** · <sub>TypeSafe AI · Docs</sub><br>Official workflow eval for deciding whether a security alert is closed, escalated or contained; Jev scores 61.7% at $0.0001 and 0.3 s per case versus Opus 5's 66.2% at $0.0574 and 15.1 s.
- **[SHADE-Arena Jev monitor](https://github.com/nican2018/shade-arena-jev-monitor)** · <sub>nican2018 · GitHub · 2026-09-17</sub><br>SHADE-Arena fork evaluating Jev as a monitor for covert agent sabotage against Gemini 2.5 Flash and Pro; as a per-action gate Jev reached AUC 0.97 on 353 tool calls, but only 0.78 on whole transcripts.
- **[Six things I tried with Jev](https://isaacflath.com/writing/six-things-i-tried-with-jev)** · <sub>Isaac Flath · Article · 2026-09-16</sub><br>Six experiments swapping Gemini for Jev, from script fact-checking (24/24 correct, 0.41 s median) and news-feed ranking to PDF passage reranking (right passage first 7 times vs once) and agent-failure review.
- **[smoking-extraction-benchmark](https://github.com/vclic/smoking-extraction-benchmark)** · <sub>vclic · GitHub · 2026-09-18</sub><br>Paired benchmark on 1,000 synthetic outpatient notes comparing Jev 1.13.0 with OpenAI structured outputs on ten smoking-history fields: 92.4% vs 98.7% complete extraction, plus cost and latency.
- **[Testing Jev on public and private data](https://amankumar.ai/blogs/jev-measured)** · <sub>Aman Kumar · Article · 2026-09-18</sub><br>Measures Jev over 16,000 calls against gpt-5.4-mini and gpt-5.6-luna on four public datasets and a few thousand real pipeline decisions, showing where it wins, where it breaks and how to set thresholds.
- **[Typed judgments or agentic loops?](https://blog.r6i.it/typesafe-jev-vs-agentic-loop.html)** · <sub>samreghenzi · Article · 2026-09-21</sub><br>Hierarchical Choices with fan-out against a GPT tool-calling agent, cutting average latency from 9.62 s to 1.38 s.
- **[TypeSafe Jev played chess](https://dev.to/maximsaplin/typesafe-jev-played-chess-and-landed-next-to-reasoning-models-28ga)** · <sub>Maxim Saplin · Article · 2026-09-17</sub><br>Runs Jev through the LLM Chess benchmark with legal moves as a Choice, landing around #59 at Elo ~243 next to mid-pack reasoning models for ~$0.0015 per game.
- **[TypeSafe Jev vs Claude Code: 4 models, 2 real jobs](https://primeline.cc/blog/typesafe-jev-pre-registered-test)** · <sub>Robin (PrimeLine) · Article · 2026-09-18</sub><br>Pre-registered test of Jev, GPT-5.6, Opus 5 and Haiku 4.5 on two real Claude Code jobs, where the ranking flips between the jobs and the author explains why.
- **[typesafe-oracles](https://github.com/trophee-bot/typesafe-oracles)** · <sub>trophee-bot · GitHub · 2026-09-16</sub><br>Measurement rig for typed oracles; on a commit-message versus diff reconciliation task over two repos, Jev matched Haiku 4.5 on accuracy while running ~4x faster at ~26x lower cost with a usable confidence signal.
- **[We tested Jev on search reranking and classification](https://parallel.ai/blog/testing-jev)** · <sub>Vlad Shulman (Parallel) · Article · 2026-09-18</sub><br>Search API company tests Jev zero-shot on reranking, topic classification and query freshness: it matched a custom reranker at NDCG@10 of 0.7 but trailed specialized internal classifiers.

</details>

Missing something? [Suggest a resource](https://github.com/Li-Evan/awesome-jev/issues/new/choose).
