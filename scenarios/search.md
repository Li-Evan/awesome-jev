# 🔎 Search and RAG

**English** · [简体中文](https://github.com/Li-Evan/awesome-jev/blob/main/zh-CN/scenarios/search.md)

Reranking, retrieval filtering, semantic search, and knowledge graphs. 86 entries, ranked by community traction.

[← Back to Awesome Jev](https://github.com/Li-Evan/awesome-jev#browse-by-scenario)

<table>
<tr>
<td width="260" valign="top"><a href="https://x.com/Saboo_Shubham_/status/2101576462042366114"><img src="https://pbs.twimg.com/amplify_video_thumb/2101576307352203264/img/THdpZUHOSRsSoTVr.jpg" alt="Semantic Find (⌘F) extension" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/Saboo_Shubham_/status/2101576462042366114">Semantic Find (⌘F) extension</a></b><br><sub>Saboo_Shubham_ · X · ♥ 2.3k · 2026-09-20</sub><br>Open-source Chrome extension that replaces Find on page with semantic matching, highlighting passages that mean what you typed in near real time.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/superagents-lab/jev-search"><img src="https://raw.githubusercontent.com/superagents-lab/jev-search/main/public/og-home.png" alt="jev-search" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/superagents-lab/jev-search">jev-search</a></b><br><sub>superagents-lab · GitHub · ⭐ 387 · 2026-09-17</sub><br>Natural-language web search that picks the time range and query with Choices and keeps each source only if its Noul passes (needs a Search1API key).<br><sub>Also: <a href="https://jev.s1.dev">app</a> · <a href="https://jev.s1.dev">app 2</a> · <a href="https://x.com/fatwang2ai/status/2100653998378516518">demo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/venturetwins/status/2101341075684434245"><img src="https://pbs.twimg.com/amplify_video_thumb/2101339712464326656/img/A8yq5IoXQuhJAi32.jpg" alt="Zillow natural-language search" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/venturetwins/status/2101341075684434245">Zillow natural-language search</a></b><br><sub>venturetwins · X · ♥ 949 · 2026-09-19</sub><br>Scans thousands of Zillow listings and classifies them by things the site has no filter for, like architecture, renovation status or distance to freeways, in under 20 seconds for $0.18.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/volcengine/OpenViking/blob/main/openviking/models/rerank/jev_rerank.py"><img src="https://raw.githubusercontent.com/volcengine/OpenViking/main/docs/images/ov-logo.png" alt="OpenViking reranker" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/volcengine/OpenViking/blob/main/openviking/models/rerank/jev_rerank.py">OpenViking reranker</a></b><br><sub>volcengine · GitHub · ⭐ 38.4k repo · 2026-01-05</sub><br>Rerank provider for a context database that scores every document with a Noul in one request.<br><sub><b>How it uses Jev:</b> Merged but not yet released at the time of curation.</sub><br><sub>Also: <a href="https://openviking.ai">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/vectorize-io/hindsight/blob/main/hindsight-api-slim/hindsight_api/engine/cross_encoder.py"><img src="https://raw.githubusercontent.com/vectorize-io/hindsight/main/hindsight-docs/static/img/hindsight-github-banner.png" alt="Hindsight Jev reranker" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/vectorize-io/hindsight/blob/main/hindsight-api-slim/hindsight_api/engine/cross_encoder.py">Hindsight Jev reranker</a></b><br><sub>vectorize-io · GitHub · ⭐ 24.9k repo · 2025-10-30</sub><br>Reranker provider in the Hindsight agent-memory system that asks Jev one question with every recall candidate as an option, so the answer is the ranking, in a single request.<br><sub><b>How it uses Jev:</b> Enabled with HINDSIGHT_API_RERANKER_PROVIDER=typesafe (jev-latest by default) and can optionally cut the irrelevant tail; shipped in 0.10.1.</sub><br><sub>Also: <a href="https://github.com/vectorize-io/hindsight/blob/main/hindsight-docs/blog/2026-09-21-version-0-10-1.md">docs</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/VisheshBaghell/status/2100536228827496721"><img src="https://pbs.twimg.com/amplify_video_thumb/2100535993141239808/img/Q_giQHiIdU-aAvI6.jpg" alt="Upweight" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/VisheshBaghell/status/2100536228827496721">Upweight</a></b><br><sub>VisheshBaghell · X · ♥ 73 · 2026-09-17</sub><br>Hacker News front page you re-rank with six sliders (technical depth, drama, practical utility, AI slop, novelty, career relevance), with each story's Jev scores shown; Firecrawl does the reading.<br><sub><b>How it uses Jev:</b> Six Score questions per story, combined locally by the slider weights.</sub><br><sub>Also: <a href="https://upweight.vercel.app">app</a> · <a href="https://upweight.vercel.app">project</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/lancedb/lancedb/blob/main/python/python/lancedb/rerankers/typesafe.py"><img src="https://github.com/user-attachments/assets/92dad0a2-2a37-4ce1-b783-0d1b4f30a00c" alt="LanceDB reranker" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/lancedb/lancedb/blob/main/python/python/lancedb/rerankers/typesafe.py">LanceDB reranker</a></b><br><sub>lancedb · GitHub · ⭐ 11.5k repo · 2023-02-28</sub><br>Asks one Noul per query-document pair and stores an absolute relevance probability you can threshold.<br><sub><b>How it uses Jev:</b> Merged but not yet released at the time of curation.</sub><br><sub>Also: <a href="https://lancedb.com/docs">docs</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/robbyczgw-cla/hermes-web-search-plus"><img src="https://raw.githubusercontent.com/robbyczgw-cla/hermes-web-search-plus/main/docs/assets/web-search-plus-v3-hero.jpg" alt="Web Search Plus Jev" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/robbyczgw-cla/hermes-web-search-plus">Web Search Plus Jev</a></b><br><sub>robbyczgw-cla · GitHub · ⭐ 414 · 2026-03-17</sub><br>Web Search Plus, a Hermes agent plugin for multi-provider search and page extraction, adds optional Jev decisions at gated seams, off by default and confidence-thresholded.<br><sub><b>How it uses Jev:</b> Code runs first; Jev is consulted only for optional seams and falls back to unchanged behaviour without a key.</sub><br><sub>Also: <a href="https://websearchplus.xyz">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/iannuttall/status/2100884132272181594"><img src="https://pbs.twimg.com/media/HSfWoEQWcAAalX9.jpg?name=orig" alt="keep.md search and tagging" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/iannuttall/status/2100884132272181594">keep.md search and tagging</a></b><br><sub>iannuttall · X · ♥ 303 · 2026-09-18</sub><br>Test of Jev on Cloudflare Workers inside keep.md: search reranking 7x faster than the current hybrid, and content tagging 50x faster than GLM 4.7 Flash with no failures.<br><sub>Also: <a href="https://keep.md">app</a> · <a href="https://keep.md">project</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/aaayandev/status/2102137061490794730"><img src="https://pbs.twimg.com/amplify_video_thumb/2102131502578290688/img/ygqNpGaKAhekXxH1.jpg" alt="YC startup semantic search" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/aaayandev/status/2102137061490794730">YC startup semantic search</a></b><br><sub>aaayandev · X · ♥ 230 · 2026-09-21</sub><br>Search engine over 6000+ Y Combinator startups that answers free-form queries (color, niche, competitor, age, image) in under a second, built with Jev for $2.7 in total testing costs.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/s3ththompson/status/2100975114753892550"><img src="https://pbs.twimg.com/amplify_video_thumb/2100974992653500416/img/7rTO_q-ntbWDGTuR.jpg" alt="Physical library index search" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/s3ththompson/status/2100975114753892550">Physical library index search</a></b><br><sub>s3ththompson · X · ♥ 171 · 2026-09-18</sub><br>Searches the author's physical books by checking an entire book index in parallel in 300ms, e.g. pointing "Who invented photography?" to page 98 under Niepce.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/noperator/siftrank"><img src="https://opengraph.githubassets.com/1/noperator/siftrank" alt="SiftRank" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/noperator/siftrank">SiftRank</a></b><br><sub>noperator · GitHub · ⭐ 202 · 2025-02-13</sub><br>CLI and agent skill for finding the most relevant items in large datasets by iterative ranking, which added a --provider jev option alongside Chat Completions APIs.<br><sub>Also: <a href="https://x.com/noperator/status/2101538373546484216">demo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/SaaiArora/status/2100807349363741132"><img src="https://pbs.twimg.com/amplify_video_thumb/2100806240406487040/img/CMyCF6BobyP4feED.jpg" alt="Intent-aware search in Replicas" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/SaaiArora/status/2100807349363741132">Intent-aware search in Replicas</a></b><br><sub>SaaiArora · X · ♥ 30 · 2026-09-18</sub><br>Experiment powering the global search in the Replicas app with Jev so results and actions follow what the user means.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/hotchpotch/jev-reranker"><img src="https://cdn-uploads.huggingface.co/production/uploads/627c91ff4d0858f003553787/uU_-MZJAuzixqmkxGVO24.webp" alt="jev-reranker" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/hotchpotch/jev-reranker">jev-reranker</a></b><br><sub>hotchpotch · GitHub · ⭐ 10 · 2026-09-19</sub><br>Python library that uses Jev to score retrieved documents for usefulness as answer evidence, rerank them and drop those under a threshold before generation, handling concurrency, long candidate lists and retries.<br><sub>Also: <a href="https://huggingface.co/blog/hotchpotch/introducing-jev-reranker">write-up</a> · <a href="https://x.com/hotchpotch/status/2101315373366906895">demo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Ontos-AI/knowhere/blob/main/apps/worker/scripts/page_memory/eval_jev_toc_anchor_confirm.py"><img src="https://opengraph.githubassets.com/1/Ontos-AI/knowhere" alt="Knowhere TOC anchor eval" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Ontos-AI/knowhere/blob/main/apps/worker/scripts/page_memory/eval_jev_toc_anchor_confirm.py">Knowhere TOC anchor eval</a></b><br><sub>Ontos-AI · GitHub · ⭐ 3.4k repo · 2026-04-30</sub><br>Offline eval in the Knowhere document-parsing system comparing Jev against the current model at confirming a table-of-contents start page during PDF parsing.<br><sub><b>How it uses Jev:</b> A per-page Choice of true/false on cached page text; Jev cannot take screenshots, so both arms get the same text.</sub><br><sub>Also: <a href="https://knowhereto.ai">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/zetaalphavector/RAGElo"><img src="https://raw.githubusercontent.com/zetaalphavector/RAGElo/master/docs/images/RAGElo_logo.png" alt="RAGElo Jev evaluators" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/zetaalphavector/RAGElo">RAGElo Jev evaluators</a></b><br><sub>zetaalphavector · GitHub · ⭐ 131 · 2023-10-10</sub><br>Elo-based toolkit for evaluating RAG agents that can use Jev via TypeSafe or Vercel AI Gateway as a retrieval relevance judge and pairwise answer evaluator.<br><sub><b>How it uses Jev:</b> jev asks whether a document would be used in a report on the topic; jev_rdnam keeps the expected grade as a fractional score.</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/xerj-org/xerj/tree/main/benchmarks/systemone-gate"><img src="https://raw.githubusercontent.com/xerj-org/xerj/main/docs/media/demo-poster.png" alt="XERJ systemone gate" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/xerj-org/xerj/tree/main/benchmarks/systemone-gate">XERJ systemone gate</a></b><br><sub>xerj-org · GitHub · ⭐ 2.3k repo · 2026-06-30</sub><br>XERJ, a local AI search engine, exposes a Jev-compatible /v1/systemone endpoint so the off-the-shelf jev-reranker client reranks a search index against it unmodified.<br><sub><b>How it uses Jev:</b> An acceptance gate runs jev-reranker's listwise and relevance presets over an SMS spam index on a XERJ node with no patches.</sub><br><sub>Also: <a href="https://xerj.org">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/zaidmukaddam/status/2100910232255992032"><img src="https://pbs.twimg.com/amplify_video_thumb/2100910214530953216/img/pZDYHLcrOl_f0pWI.jpg" alt="Cascade Search" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/zaidmukaddam/status/2100910232255992032">Cascade Search</a></b><br><sub>zaidmukaddam · X · ♥ 95 · 2026-09-18</sub><br>In-browser search bar where a 27K-parameter model parses queries like "open bugs from sam since last week" into typed filters in 0.25 ms and asks Jev only about words it is unsure of.<br><sub>Also: <a href="https://cascade.scira.ai">app</a> · <a href="https://cascade.scira.ai">project</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/byenzyme/enzyme"><img src="https://repository-images.githubusercontent.com/920398699/6e344f34-0504-4959-b6ce-49b8d6cb5c20" alt="Enzyme" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/byenzyme/enzyme">Enzyme</a></b><br><sub>byenzyme · GitHub · ⭐ 82 · 2025-01-22</sub><br>Local-first compile step for Markdown knowledge bases whose enzyme compile uses Jev via OpenRouter Decisions to scan the vault and write the program that decides where catalyst questions are learned from.<br><sub>Also: <a href="https://memory.enzyme.garden">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/jexp/neo4jev"><img src="https://opengraph.githubassets.com/1/jexp/neo4jev" alt="neo4jev" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/jexp/neo4jev">neo4jev</a></b><br><sub>jexp · GitHub · ⭐ 81 · 2026-09-16</sub><br>Demo that navigates a Neo4j graph one hop at a time toward a natural-language goal, with Jev choosing which relationship to follow and a beam search keeping the best paths.<br><sub><b>How it uses Jev:</b> A Choice over outgoing relationships plus a goal-reached Noul in the same call, so each hop is one round-trip.</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/neural_avb/status/2100881974780993668"><img src="https://pbs.twimg.com/amplify_video_thumb/2100879106078568449/img/nCefxS323PhF_n7f.jpg" alt="Paper Breakdown recommendations" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/neural_avb/status/2100881974780993668">Paper Breakdown recommendations</a></b><br><sub>neural_avb · X · ♥ 65 · 2026-09-18</sub><br>Adds Jev curation on top of the content-based and collaborative-filtering recommender in Paper Breakdown, at $0.0019 per user for ~70 recs.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/AYi_AInotes/status/2102198099498135812"><img src="https://pbs.twimg.com/amplify_video_thumb/2101673555813453825/img/nfWWuk_nW1mtGBW2.jpg" alt="Margin" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/AYi_AInotes/status/2102198099498135812">Margin</a></b><br><sub>AYi_AInotes · X · ♥ 29 · 2026-09-22</sub><br>Tool that imports years of X bookmarks and lets you search them in plain language, with Jev scoring every saved tweet in parallel and returning a relevance-ranked list in seconds.<br><sub><b>How it uses Jev:</b> Scores each bookmarked tweet against the query.</sub><br><sub>Also: <a href="https://x.com/alexchristou_/status/2101674202361221376">demo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/mukiwu/jev-search-mcp"><img src="https://opengraph.githubassets.com/1/mukiwu/jev-search-mcp" alt="jev-search" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/mukiwu/jev-search-mcp">jev-search</a></b><br><sub>mukiwu · GitHub · ⭐ 59 · 2026-03-23</sub><br>Claude Code plugin in the muki-ai-plugins marketplace that answers WebSearch with Jev-ranked results, where Jev chooses sources and time window, falling back to the built-in tool.<br><sub>Also: <a href="https://github.com/mukiwu/muki-ai-plugins">marketplace</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/kbhuw/jev-sift"><img src="https://opengraph.githubassets.com/1/kbhuw/jev-sift" alt="jev-sift" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/kbhuw/jev-sift">jev-sift</a></b><br><sub>kbhuw · GitHub · ⭐ 45 · 2026-09-18</sub><br>Agent plugin and MCP tool that sends batches of files, public web pages, text, or tool descriptions to Jev with a query and returns relevance probabilities, so the agent opens only items worth reading.<br><sub>Also: <a href="https://x.com/kushbhuwalka/status/2101064922813895154">demo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/konbakuyomu/smartsearch/blob/main/src/smart_search/jev.py"><img src="https://raw.githubusercontent.com/konbakuyomu/smartsearch/main/assets/branding/smart-search.png" alt="Smart Search Jev" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/konbakuyomu/smartsearch/blob/main/src/smart_search/jev.py">Smart Search Jev</a></b><br><sub>konbakuyomu · GitHub · ⭐ 838 repo · 2026-05-10</sub><br>Smart Search, a desktop app that pulls current web information into AI conversations, uses Jev for typed judgments while keeping execution and the allowed action set in code.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/dorkitude/webctl"><img src="https://pbs.twimg.com/media/HSx-UqEaIAEjR4L.jpg?name=orig" alt="webctl" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/dorkitude/webctl">webctl</a></b><br><sub>dorkitude · GitHub · ⭐ 37 · 2026-09-20</sub><br>Web search CLI for agents that queries three search backends, has Jev score each result set against the query and goal, and dedupes the high-scoring subset so the agent reads far less.<br><sub>Also: <a href="https://x.com/dorkitude/status/2102194028704092585">demo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/rodydavis/status/2101802283256463699"><img src="https://pbs.twimg.com/media/HSsZnCSaMAABhjv.jpg" alt="Embedded databases plus Jev reranking" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/rodydavis/status/2101802283256463699">Embedded databases plus Jev reranking</a></b><br><sub>rodydavis · Article · ♥ 27 · 2026-09-20</sub><br>Architecture write-up pairing SQLite, DuckDB and LadyBugDB for hybrid candidate retrieval with Jev as the reranker, aiming for sub-second RAG results instead of sending 20 to 50 passages to a frontier LLM.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/kentcdodds/kody/blob/main/packages/worker/src/mcp/tools/search-jev-rerank.ts"><img src="https://opengraph.githubassets.com/1/kentcdodds/kody" alt="Kody Jev search rerank" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/kentcdodds/kody/blob/main/packages/worker/src/mcp/tools/search-jev-rerank.ts">Kody Jev search rerank</a></b><br><sub>kentcdodds · GitHub · ⭐ 663 repo · 2026-09-18</sub><br>Optional second stage for Kody's MCP search that widens hybrid lexical and vector recall on ambiguous queries, then reranks and filters candidates with Jev via Workers AI.<br><sub><b>How it uses Jev:</b> Score questions per candidate through Cloudflare AI Gateway, with an adaptive keep cutoff and fallback to hybrid order on low confidence.</sub><br><sub>Also: <a href="https://x.com/kodykoala/status/2100943346575253515">demo</a> · <a href="https://github.com/kentcdodds/kody">repo</a> · <a href="https://kody.codes">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/bolau_/status/2102127429418360895"><img src="https://pbs.twimg.com/media/HSw20LaXUAAI3w6.jpg?name=orig" alt="SF food permit map" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/bolau_/status/2102127429418360895">SF food permit map</a></b><br><sub>bolau_ · X · ♥ 32 · 2026-09-21</sub><br>Map of permit and health-inspection records for every food and beverage business in San Francisco, where Jev answers questions about the records in seconds.</td>
</tr>
<tr>
<td width="260" valign="top"></td>
<td valign="top"><b><a href="https://www.reddit.com/r/AI_Agents/comments/1wkusec/building_an_internet_scanner_with_jev/">Tripwire internet scanner</a></b><br><sub>Calm_Apple7505 · Reddit · ▲ 7 · 2026-09-19</sub><br>Early-access tool that scans Reddit, X, and LinkedIn posts and filters them by concepts defined in natural language instead of keywords.<br><sub>Also: <a href="https://tripwire.easytech-agency.net/">app</a> · <a href="https://tripwire.easytech-agency.net">project</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/owengretzinger/status/2101397416826053104"><img src="https://www.boardy.ai/opengraph-image" alt="Boardy match reranking" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/owengretzinger/status/2101397416826053104">Boardy match reranking</a></b><br><sub>owengretzinger · X · ♥ 15 · 2026-09-19</sub><br>Boardy, an AI superconnector, reports that Jev has already reranked over 1 million people-matches in production.<br><sub>Also: <a href="https://boardy.ai">app</a> · <a href="https://boardy.ai">project</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/serverpod/starguide"><img src="https://opengraph.githubassets.com/1/serverpod/starguide" alt="Starguide" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/serverpod/starguide">Starguide</a></b><br><sub>serverpod · GitHub · ⭐ 16 · 2025-05-27</sub><br>Serverpod's documentation chatbot where Jev picks the doc and website pages that answer a question, judges whether they contain the answer so vector search can be skipped, and rates whether the final answer resolved it.<br><sub><b>How it uses Jev:</b> Pages are Choice options via the jev_dart package; two Nouls cover answer coverage and resolution.</sub><br><sub>Also: <a href="https://pub.dev/packages/jev_dart">package</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/sensahin/transcript-lens"><img src="https://opengraph.githubassets.com/1/sensahin/transcript-lens" alt="Transcript Lens" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/sensahin/transcript-lens">Transcript Lens</a></b><br><sub>sensahin · GitHub · ⭐ 16 · 2026-09-19</sub><br>Next.js app with a Turkish interface for exploring YouTube transcripts by meaning, where Jev classifies each block without rewriting it to surface chapters, key passages, and topic mentions.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://news.ycombinator.com/item?id=49777691"><img src="https://www.hazumi.news/hazumi-news-og.png" alt="Hazumi News" width="240"></a></td>
<td valign="top"><b><a href="https://news.ycombinator.com/item?id=49777691">Hazumi News</a></b><br><sub>jrhey · Hacker News · ▲ 5 · 2026-09-20</sub><br>Hacker News reader that uses Jev to filter large discussion threads down to the comments worth reading.<br><sub>Also: <a href="https://www.hazumi.news/best">app</a> · <a href="https://hazumi.news">project</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Zabaca/lattice"><img src="https://opengraph.githubassets.com/1/Zabaca/lattice" alt="Lattice Jev reranker" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Zabaca/lattice">Lattice Jev reranker</a></b><br><sub>Zabaca · GitHub · ⭐ 15 · 2025-11-27</sub><br>Optional reranking stage in Lattice, a local-first retrieval engine for markdown knowledge bases, that sends the fused top hits to Jev in one request and scores each by the probability it answers the query.<br><sub>Also: <a href="https://zabaca.com/products/lattice/">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/hraness/wordcell"><img src="https://raw.githubusercontent.com/hraness/wordcell/main/assets/agent-skill.svg" alt="Wordcell" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/hraness/wordcell">Wordcell</a></b><br><sub>hraness · GitHub · ⭐ 14 · 2026-07-22</sub><br>Local Markdown knowledge base for coding agents with an optional Jev reranking lane; on SciFact it put a relevant result first for 161 of 300 queries versus 101 with exact search alone.<br><sub><b>How it uses Jev:</b> Pinned jev-1.13.0 reranks a bounded window of search candidates; exact matches stay first and provider failures keep the baseline order.</sub><br><sub>Also: <a href="https://wordcell.io">app</a> · <a href="https://github.com/hraness/wordcell/blob/main/docs/reranking.md">docs</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/colophon-group/jobseek/blob/main/apps/web/src/lib/ai-filter/jev-client.ts"><img src="https://opengraph.githubassets.com/1/colophon-group/jobseek" alt="Job Seek Jev AI filter" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/colophon-group/jobseek/blob/main/apps/web/src/lib/ai-filter/jev-client.ts">Job Seek Jev AI filter</a></b><br><sub>colophon-group · GitHub · ⭐ 199 repo · 2026-02-18</sub><br>Open-source job search built from 5,300+ career sites that adds a Jev AI filter classifying each posting as accepted or rejected against a user's criteria.<br><sub><b>How it uses Jev:</b> One Choice per job posting in a batched request, resistant to injected text in descriptions.</sub><br><sub>Also: <a href="https://jseek.co/">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/marc2332/findme"><img src="https://opengraph.githubassets.com/1/marc2332/findme" alt="findme" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/marc2332/findme">findme</a></b><br><sub>marc2332 · GitHub · ⭐ 9 · 2026-09-19</sub><br>Rust CLI that finds a file or folder from a natural-language memory of it by walking the directory tree and asking Jev which entries at each level look most promising.<br><sub><b>How it uses Jev:</b> Sends entry names and light metadata per level, keeps the highest-scoring directories and descends, respecting .gitignore.</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/hev/reranker"><img src="https://opengraph.githubassets.com/1/hev/reranker" alt="hev reranker" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/hev/reranker">hev reranker</a></b><br><sub>hev · GitHub · ⭐ 9 · 2026-09-17</sub><br>Recipe and 90-line Python wrapper that uses Jev as a calibrated reranker for up to 30 documents per call, with nDCG@10 results against hosted and open rerankers on BEIR shortlists.<br><sub><b>How it uses Jev:</b> One Noul relevance question per document in a single request; the probability serves as both sort key and prune threshold.</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/chenmingtang830/jevgraph"><img src="https://raw.githubusercontent.com/chenmingtang830/jevgraph/main/docs/assets/jevgraph-overview.svg" alt="JevGraph" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/chenmingtang830/jevgraph">JevGraph</a></b><br><sub>chenmingtang830 · GitHub · ⭐ 9 · 2026-09-20</sub><br>Document-to-graph pipeline that parses PDF, DOCX, PPTX, or text locally and asks Jev one closed-set relation question per candidate entity pair, exporting edges with probabilities and page evidence.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/magnus919/SlopSearX"><img src="https://opengraph.githubassets.com/1/magnus919/SlopSearX" alt="SlopSearX" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/magnus919/SlopSearX">SlopSearX</a></b><br><sub>magnus919 · GitHub · ⭐ 9 · 2026-06-09</sub><br>Stateless meta search engine for AI agents and drop-in SearXNG replacement that asks Jev which specialist engines can add distinctive evidence for each query.<br><sub><b>How it uses Jev:</b> Every specialist engine at or above a 0.65 threshold is added with no count cap; explicit scopes never call Jev, and failures keep the deterministic routing.</sub><br><sub>Also: <a href="https://github.com/magnus919/SlopSearX/blob/main/docs/JEV_ROUTING.md">docs</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/zaidmukaddam/cascade-search"><img src="https://raw.githubusercontent.com/zaidmukaddam/cascade-search/main/eval/results/m2.png" alt="cascade-search" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/zaidmukaddam/cascade-search">cascade-search</a></b><br><sub>zaidmukaddam · GitHub · ⭐ 8 · 2026-09-17</sub><br>In-browser search query parser: a 27,193-parameter model labels every word with a role and calibrated confidence in about 0.25 ms, and only the uncertain words are escalated to Jev.<br><sub><b>How it uses Jev:</b> Both tiers feed one compiler so the app gets the same typed filter whichever tier answered; a separate cascade-search-jev package provides the escalation.</sub><br><sub>Also: <a href="https://cascade.scira.ai">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/gigabit_million/status/2102200033307422821"><img src="https://pbs.twimg.com/amplify_video_thumb/2101941990254632960/img/gx4NHU9mxvfHKA3y.jpg" alt="Fuzzy content search" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/gigabit_million/status/2102200033307422821">Fuzzy content search</a></b><br><sub>gigabit_million · X · ♥ 1 · 2026-09-22</sub><br>Search site over the author's own published content where Jev scores each item against a vague query and shows the scores, which makes the ranking easy to inspect.<br><sub><b>How it uses Jev:</b> Score per content item against the free-text query.</sub><br><sub>Also: <a href="https://gigabit-search.gigabitmillion-games.workers.dev/">app</a> · <a href="https://gigabit-search.gigabitmillion-games.workers.dev">project</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/PixelML/av"><img src="https://opengraph.githubassets.com/1/PixelML/av" alt="av" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/PixelML/av">av</a></b><br><sub>PixelML · GitHub · ⭐ 7 · 2026-02-14</sub><br>Video memory CLI for agents that indexes captions and transcripts for search and Q&amp;A; with a TypeSafe key, <code>av ask</code> has Jev filter and rank retrieved scenes and check whether the answer is supported.<br><sub><b>How it uses Jev:</b> Per-hit relevance probability times retrieval score for ranking, plus a separate Noul on whether the answer is supported; falls back to raw retrieval if Jev fails.</sub><br><sub>Also: <a href="https://agentic.video">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/larguesa/jev-search"><img src="https://opengraph.githubassets.com/1/larguesa/jev-search" alt="jev-search" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/larguesa/jev-search">jev-search</a></b><br><sub>larguesa · GitHub · ⭐ 6 · 2026-09-19</sub><br>Dependency-free Python CLI for semantic line search over documents, notes, and knowledge bases via Jev on OpenRouter, meant to complement exact keyword search for agents.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/kenn-io/docbank/tree/main/document/typesafe"><img src="https://opengraph.githubassets.com/1/kenn-io/docbank" alt="docbank Jev reranking" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/kenn-io/docbank/tree/main/document/typesafe">docbank Jev reranking</a></b><br><sub>kenn-io · GitHub · ⭐ 101 repo · 2026-07-07</sub><br>Local-first document vault for people and agents that adds a TypeSafe Jev reranking provider for search over document names and extracted text.<br><sub>Also: <a href="https://docbank.ai">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/tornikegomareli/FindSFSymbols"><img src="https://opengraph.githubassets.com/1/tornikegomareli/FindSFSymbols" alt="FindSFSymbols" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/tornikegomareli/FindSFSymbols">FindSFSymbols</a></b><br><sub>tornikegomareli · GitHub · ⭐ 5 · 2026-09-20</sub><br>Mac app for finding SF Symbols by plain description: on-device word vectors shortlist 48 symbols, then Jev answers 48 yes/no questions in one request and the scores drive a physics pile where good matches float up.<br><sub><b>How it uses Jev:</b> One Noul per shortlisted symbol in a single request; without a key the app uses on-device matching only.</sub><br><sub>Also: <a href="https://tornikegomareli.github.io/FindSFSymbols/">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/danielwanwx/research-engine"><img src="https://opengraph.githubassets.com/1/danielwanwx/research-engine" alt="Research Engine" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/danielwanwx/research-engine">Research Engine</a></b><br><sub>danielwanwx · GitHub · ⭐ 5 · 2026-06-28</sub><br>Evidence-first research runtime for AI agents that routes a question to research packs and read-only connectors; an optional <code>jev-triage</code> command asks Jev how relevant already-collected public evidence rows are.<br><sub><b>How it uses Jev:</b> Up to eight allowlisted public rows per request get advisory Noul relevance probabilities; Jev never adds or removes evidence.</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/robbyczgw-cla/web-search-plus-mcp"><img src="https://raw.githubusercontent.com/robbyczgw-cla/web-search-plus-mcp/main/docs/assets/web-search-plus-logo.png" alt="web-search-plus-mcp" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/robbyczgw-cla/web-search-plus-mcp">web-search-plus-mcp</a></b><br><sub>robbyczgw-cla · GitHub · ⭐ 5 · 2026-03-13</sub><br>MCP server that gives agents web search across 15 search and 9 extract providers with original sources; optional, off-by-default Jev confirms news-type searches, scores extracted bodies and fills in missing language.<br><sub>Also: <a href="https://websearchplus.xyz">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/iAmAustinPiazza/status/2102112514846740749"><img src="https://pbs.twimg.com/amplify_video_thumb/2102112331350102016/img/G-DKU2luzlCVeboq.jpg" alt="Semantic object filter" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/iAmAustinPiazza/status/2102112514846740749">Semantic object filter</a></b><br><sub>iAmAustinPiazza · X · ♥ 1 · 2026-09-21</sub><br>Small interactive demo where you type a phrase such as things you can wear in winter and Jev picks out the matching objects on screen.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/keltokhy/jselect"><img src="https://opengraph.githubassets.com/1/keltokhy/jselect" alt="jselect" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/keltokhy/jselect">jselect</a></b><br><sub>keltokhy · GitHub · ⭐ 3 · 2026-09-19</sub><br>Python context selector that asks Jev whether each passage in your files or records is useful evidence for a task, then picks diverse verbatim passages with source links within a token budget.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/WiktorB2004/llama-index-jev"><img src="https://opengraph.githubassets.com/1/WiktorB2004/llama-index-jev" alt="llama-index-jev" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/WiktorB2004/llama-index-jev">llama-index-jev</a></b><br><sub>WiktorB2004 · GitHub · ⭐ 3 · 2026-09-18</sub><br>LlamaIndex reranker and router; reranking lifts nDCG@5 on NFCorpus from 0.340 to 0.396.<br><sub>Also: <a href="https://wiktorb2004.github.io/llama-index-jev">docs</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/snaga/status/2101901648184643707"><img src="https://pbs.twimg.com/media/HSt0LTabQAAACdr.jpg?name=orig" alt="Hacker News personal recommender" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/snaga/status/2101901648184643707">Hacker News personal recommender</a></b><br><sub>snaga · X · ▶ 138 · 2026-09-21</sub><br>Experiment that has Jev pick which Hacker News front-page stories match the author's interests each morning, with the composite-judgment design written up in a gist.<br><sub>Also: <a href="https://gist.github.com/snaga/12c62ad587d59e4817e00d3ec1846f47">gist</a> · <a href="https://gist.github.com/snaga/12c62ad587d59e4817e00d3ec1846f47">project</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Zafer-Liu/book-learning/blob/main/study/jev_gate.py"><img src="https://opengraph.githubassets.com/1/Zafer-Liu/book-learning" alt="Book Learning Jev retrieval gate" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Zafer-Liu/book-learning/blob/main/study/jev_gate.py">Book Learning Jev retrieval gate</a></b><br><sub>Zafer-Liu · GitHub · ⭐ 43 repo · 2026-04-23</sub><br>Retrieval gate in the self-hosted BOOKNOTE textbook RAG study assistant: Jev scores each fused candidate chunk for relevance and screens it for prompt injection before it reaches the answer, failing open to the ungated results.<br><sub><b>How it uses Jev:</b> One fanned-out call per query with a 0-3 relevance Score and an injection Noul per chunk; keeps chunks with relevance &gt;= 2.0 and injection &lt; 0.5.</sub><br><sub>Also: <a href="https://github.com/Zafer-Liu/book-learning">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/shinpr/jev-reranker"><img src="https://raw.githubusercontent.com/shinpr/jev-reranker/main/assets/banner.jpg" alt="Jev Reranker" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/shinpr/jev-reranker">Jev Reranker</a></b><br><sub>shinpr · GitHub · ⭐ 2 · 2026-09-20</sub><br>Rust CLI, installed from npm, that reads a JSON array of search results from stdin and uses Jev to rerank them, drop candidates with no usable evidence, or extract query-specific passages for your LLM.<br><sub>Also: <a href="https://norsica.jp/blog/what-retrieval-still-hasnt-decided">article</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/abhishekmamdapure/jev-information-extraction"><img src="https://opengraph.githubassets.com/1/abhishekmamdapure/jev-information-extraction" alt="jev-information-extraction" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/abhishekmamdapure/jev-information-extraction">jev-information-extraction</a></b><br><sub>abhishekmamdapure · GitHub · ⭐ 2 · 2026-09-20</sub><br>Upload a PDF and ask questions such as the GST number or invoice total; Jev ranks the extracted text chunks that answer each one and the app shows each match, its probability and its location on the page.<br><sub>Also: <a href="https://jev-information-extraction-fibby-prod-telegram.up.railway.app/">app</a> · <a href="https://jev-information-extraction-fibby-prod-telegram.up.railway.app">app 2</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Chia1104/chia1104.dev/blob/develop/packages/ai/src/rerank/jev.ts"><img src="https://repository-images.githubusercontent.com/485318015/26c450f3-6246-4b7d-b8a5-7a658a79989e" alt="chia1104.dev Jev reranker" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Chia1104/chia1104.dev/blob/develop/packages/ai/src/rerank/jev.ts">chia1104.dev Jev reranker</a></b><br><sub>Chia1104 · GitHub · ⭐ 32 repo · 2022-04-25</sub><br>Search reranker in the chia1104.dev personal site and CMS monorepo that makes one Jev call per query: a Choice over candidate posts and a Noul on whether any candidate actually answers it, working across languages.<br><sub><b>How it uses Jev:</b> The Choice picks the best candidate id; the Noul separates a real answer from the closest irrelevant hit, since choice probabilities always sum to 1.</sub><br><sub>Also: <a href="https://chia1104.dev">app</a> · <a href="https://github.com/Chia1104/chia1104.dev">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/jreyesdev/status/2102218598668488983"><img src="https://pbs.twimg.com/media/HSyURXUaUAEVMKX.jpg?name=orig" alt="Sanity content agent without LLM queries" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/jreyesdev/status/2102218598668488983">Sanity content agent without LLM queries</a></b><br><sub>jreyesdev · X · ▶ 60 · 2026-09-22</sub><br>Demo pairing Jev with the Sanity CMS where answers are pre-written at ingest, so the agent selects an answer, skips retrieval when it can and responds in under a second instead of 4+.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/tedliou/decision-model-playground"><img src="https://opengraph.githubassets.com/1/tedliou/decision-model-playground" alt="decision-model-playground" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/tedliou/decision-model-playground">decision-model-playground</a></b><br><sub>tedliou · GitHub · ⭐ 1 · 2026-09-19</sub><br>Local browser playground where Laya or Jev picks the best-matching vervecode.dev article for a question, showing every option's raw probability, a no-match option and load and inference timings.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/raahelpie/hn-for-me"><img src="https://external-preview.redd.it/cGZkd252YzFheXFoMeTpqXMSfpCE94rmVlGr8pZ7_z3kfZQqelwwzt-Id7ds.png?format=pjpg&amp;auto=webp&amp;s=e90f071fd20387c7898145a4feed6ca91dc9360f" alt="Hacker News For Me" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/raahelpie/hn-for-me">Hacker News For Me</a></b><br><sub>raahelpie · GitHub · ⭐ 1 · 2026-09-20</sub><br>Personal Hacker News reader that screens new stories against your saved interests and shows only the relevant ones in an HN-style feed.<br><sub><b>How it uses Jev:</b> Runs on Codiv's OpenJev model by default, with TypeSafe Jev as a switchable provider; thresholds of 0.7 for titles and 0.9 for article relevance.</sub><br><sub>Also: <a href="https://news.ycombinator.com/item?id=49788260">demo</a> · <a href="https://www.reddit.com/r/SideProject/comments/1wmruft/hn_for_me_hacker_news_stories_curated_by_jev/">discussion</a> · <a href="https://x.com/RaahelSaidWhat/status/2102162969656475973">demo 2</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/ajanm007/jevrag"><img src="https://opengraph.githubassets.com/1/ajanm007/jevrag" alt="JevRAG" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/ajanm007/jevrag">JevRAG</a></b><br><sub>ajanm007 · GitHub · ⭐ 1 · 2026-09-20</sub><br>Decision layer for RAG pipelines that replaces hardcoded thresholds with calibrated gates for evidence sufficiency, chunk boundaries, context selection, answer abstention, and cache trust, evaluated on HotpotQA.<br><sub><b>How it uses Jev:</b> Jev is the first swappable backend behind the five decision primitives.</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/kylemclaren/jevsearch"><img src="https://opengraph.githubassets.com/1/kylemclaren/jevsearch" alt="jevsearch" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/kylemclaren/jevsearch">jevsearch</a></b><br><sub>kylemclaren · GitHub · ⭐ 1 · 2026-09-21</sub><br>Drop-in shadcn/ui block for site search that shows keyword hits on the first keystroke, then re-ranks them by the visitor's intent with Jev a moment later, keeping keyword order if the call fails.<br><sub>Also: <a href="https://jevsearch.fly.dev">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/avshalomd/longjev"><img src="https://raw.githubusercontent.com/avshalomd/longjev/main/results/social/longjev_pipeline.png" alt="longjev" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/avshalomd/longjev">longjev</a></b><br><sub>avshalomd · GitHub · ⭐ 1 · 2026-09-18</sub><br>Experimental wrapper with the same system_one(state, questions) call as Jev that accepts inputs beyond Jev's 32K-token limit by scoring every chunk, keeping the best ones and asking Jev over what remains.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/komikat/psearch"><img src="https://opengraph.githubassets.com/1/komikat/psearch" alt="psearch" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/komikat/psearch">psearch</a></b><br><sub>komikat · GitHub · ⭐ 1 · 2026-09-17</sub><br>Web search CLI and MCP server for terminals and agents: Parallel Search seeds pages, local Chromium fetches them concurrently, and Jev scores the evidence and picks links for a breadth-first queue.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/micahchoo/qualitative-query"><img src="https://raw.githubusercontent.com/micahchoo/qualitative-query/main/docs/img/query-builder.png" alt="Qualitative Query" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/micahchoo/qualitative-query">Qualitative Query</a></b><br><sub>micahchoo · GitHub · ⭐ 1 · 2026-09-19</sub><br>Obsidian plugin that answers saved questions with original passages from your notes, then saves them into a note linked back to the sources, without generating an answer.<br><sub><b>How it uses Jev:</b> Local search finds candidate passages and Jev scores which of them actually answer the question.</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/baekenough/second-brain/tree/main/internal/jev"><img src="https://raw.githubusercontent.com/baekenough/second-brain/main/docs/diagrams/01-system-runtime-topology.png" alt="second-brain Jev classifier" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/baekenough/second-brain/tree/main/internal/jev">second-brain Jev classifier</a></b><br><sub>baekenough · GitHub · ⭐ 15 repo · 2026-04-14</sub><br>Ingestion classifier in second-brain, an LLM-curated private search engine over Slack, GitHub, Drive and personal messages, that asks Jev to assign each SMS, Gmail or call transcript a segment and a retention score.<br><sub><b>How it uses Jev:</b> A segment Choice and a retention Score per document; request and response bodies are never logged.</sub><br><sub>Also: <a href="https://github.com/baekenough/second-brain">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/jonnyparris/dodo/blob/main/src/browser/web-fetch.ts"><img src="https://raw.githubusercontent.com/jonnyparris/dodo/main/assets/dodo.svg" alt="Dodo Jev web tools" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/jonnyparris/dodo/blob/main/src/browser/web-fetch.ts">Dodo Jev web tools</a></b><br><sub>jonnyparris · GitHub · ⭐ 13 repo · 2026-03-28</sub><br>Coding agent on Cloudflare Workers whose read-only web tools use Jev to rank candidate URLs before fetching and to check whether a fetched page answers the query.<br><sub><b>How it uses Jev:</b> browser_triage ranks URLs from metadata alone; browser_markdown returns a calibrated Noul verdict so the agent can decide whether to keep browsing.</sub><br><sub>Also: <a href="https://github.com/jonnyparris/dodo">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Mr-remon219/search-boost/tree/master/lib/jev"><img src="https://opengraph.githubassets.com/1/Mr-remon219/search-boost" alt="SearchBoost Jev evidence loop" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Mr-remon219/search-boost/tree/master/lib/jev">SearchBoost Jev evidence loop</a></b><br><sub>Mr-remon219 · GitHub · ⭐ 9 repo · 2026-08-17</sub><br>Multi-engine web search and evidence synthesis for coding agents (MCP server, Pi extension, DeepSeek Harness bundle) with an experimental adaptive_search loop that uses Jev to research targets in batches.<br><sub>Also: <a href="https://github.com/Mr-remon219/search-boost">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/jialuohu/codex-toolbox/tree/main/plugins/typesafe-tools"><img src="https://opengraph.githubassets.com/1/jialuohu/codex-toolbox" alt="typesafe-tools Codex plugin" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/jialuohu/codex-toolbox/tree/main/plugins/typesafe-tools">typesafe-tools Codex plugin</a></b><br><sub>jialuohu · GitHub · ⭐ 9 repo · 2026-07-02</sub><br>Codex plugin with an MCP server and skill that use bounded Jev evaluations to rank public research passages and check whether sources support a claim, behind spending caps and pilot gates.<br><sub>Also: <a href="https://github.com/jialuohu/codex-toolbox">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/dabit3/macos-experiments/tree/main/turbo-rerank"><img src="https://raw.githubusercontent.com/dabit3/macos-experiments/main/turbo-rerank/screenshots/turbo-rerank-home.jpg" alt="Turbo Rerank" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/dabit3/macos-experiments/tree/main/turbo-rerank">Turbo Rerank</a></b><br><sub>dabit3 · GitHub · ⭐ 8 repo · 2026-09-07</sub><br>Search workspace demo that reranks 50 candidates in one ~170 ms Jev request, raising top-1 accuracy from 50% to 100% on a 40-query labeled benchmark.<br><sub><b>How it uses Jev:</b> One request judges every candidate against the query plus an answer-exists check, optionally split into parallel batches.</sub><br><sub>Also: <a href="https://github.com/dabit3/macos-experiments">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/serpapi/tutorials/tree/master/python_projects/jev-serpapi-fact-checker"><img src="https://opengraph.githubassets.com/1/serpapi/tutorials" alt="Jev and SerpApi fact checker" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/serpapi/tutorials/tree/master/python_projects/jev-serpapi-fact-checker">Jev and SerpApi fact checker</a></b><br><sub>serpapi · GitHub · ⭐ 6 repo · 2025-09-05</sub><br>Tutorial CLI from SerpApi that checks a statement or yes/no question against up to five Google organic snippets and gets a verdict from Jev through OpenRouter's Decisions API.<br><sub>Also: <a href="https://github.com/serpapi/tutorials">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/The-40-Thieves/obsidian-tc/blob/main/packages/server/src/gateway/typesafe.ts"><img src="https://opengraph.githubassets.com/1/The-40-Thieves/obsidian-tc" alt="obsidian-tc Jev citation judge" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/The-40-Thieves/obsidian-tc/blob/main/packages/server/src/gateway/typesafe.ts">obsidian-tc Jev citation judge</a></b><br><sub>The-40-Thieves · GitHub · ⭐ 5 repo · 2026-05-18</sub><br>Opt-in Jev judge provider in obsidian-tc, a governed Obsidian MCP server with fused retrieval and vault memory, used only to decide whether inferred citations between notes hold up.<br><sub><b>How it uses Jev:</b> One Noul with true/false criteria per citation, pinned to a versioned model, with bounded retries.</sub><br><sub>Also: <a href="https://github.com/The-40-Thieves/obsidian-tc">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Aias/pattern-languages/blob/master/src/lib/pattern-search.ts"><img src="https://opengraph.githubassets.com/1/Aias/pattern-languages" alt="Patterns of Design search" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Aias/pattern-languages/blob/master/src/lib/pattern-search.ts">Patterns of Design search</a></b><br><sub>Aias · GitHub · ⭐ 5 repo · 2019-09-05</sub><br>Search on the patternsof.design pattern-language site where Jev scores how much practical guidance each design pattern gives for what the user wants to build, directly or by analogy.<br><sub><b>How it uses Jev:</b> One Score per pattern against the query, 64 patterns per request, with a 0.5 match probability cut.</sub><br><sub>Also: <a href="https://patternsof.design">app</a> · <a href="https://github.com/Aias/pattern-languages">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/jokull/ensk"><img src="https://opengraph.githubassets.com/1/jokull/ensk" alt="ensk" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/jokull/ensk">ensk</a></b><br><sub>jokull · GitHub · 2026-09-18</sub><br>English-Icelandic dictionary on Cloudflare Workers that combines D1 full-text search and Vectorize semantic recall, then has Jev via Workers AI rerank the shortlist and decide whether any entry truly matches.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Eliovp-BV/Jev-Radar"><img src="https://raw.githubusercontent.com/Eliovp-BV/Jev-Radar/main/docs/media/radar-demo.gif" alt="Jev Radar" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Eliovp-BV/Jev-Radar">Jev Radar</a></b><br><sub>Eliovp-BV · GitHub · 2026-09-19</sub><br>Local research workspace where Jev steers an investigation over public sources, asking the same research questions across records to build an evidence-linked comparison with every decision inspectable.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/jh1373/jev-search"><img src="https://opengraph.githubassets.com/1/jh1373/jev-search" alt="Jev Search for Obsidian" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/jh1373/jev-search">Jev Search for Obsidian</a></b><br><sub>jh1373 · GitHub · 2026-09-18</sub><br>Obsidian plugin that searches the vault offline with BM25 and then, only after you approve what gets sent, reranks the top results with Jev.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/sudeshkar/jev-corrective-rag"><img src="https://opengraph.githubassets.com/1/sudeshkar/jev-corrective-rag" alt="jev-corrective-rag" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/sudeshkar/jev-corrective-rag">jev-corrective-rag</a></b><br><sub>sudeshkar · GitHub · 2026-09-20</sub><br>Corrective RAG where the retrieve-or-not, chunk-grading and groundedness gates are Jev calls instead of LLM judges, averaging 0.75 LLM calls per query with 7x fewer LLM calls and 4x lower p50 latency.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/kierandotai/jev-scout"><img src="https://opengraph.githubassets.com/1/kierandotai/jev-scout" alt="jev-scout" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/kierandotai/jev-scout">jev-scout</a></b><br><sub>kierandotai · GitHub · 2026-09-19</sub><br>MCP server for agent web research that has Jev judge every query, search result, and fetched page for relevance and credibility, with session budgets, SSRF-guarded fetching, and a live decision dashboard.<br><sub><b>How it uses Jev:</b> One call per search result (relevance, credibility, worth fetching) and one per fetched page (answered, content class, steering risk); a hand-labeled 25-item study reports 88% relevance and 96% credibility.</sub><br><sub>Also: <a href="https://github.com/kierandotai/jev-scout/blob/main/docs/accuracy/2026-09-19-jev-golden-set-study.md">study</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/ArielBubis/Jevflix"><img src="https://opengraph.githubassets.com/1/ArielBubis/Jevflix" alt="Jevflix" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/ArielBubis/Jevflix">Jevflix</a></b><br><sub>ArielBubis · GitHub · 2026-09-21</sub><br>Movie recommender that narrows 4,800 films to a shortlist with FAISS and BM25, then has Jev parse your constraints and pick one film, using its confidence to answer instantly or ask a follow-up.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://www.theunwindai.com/p/get-started-with-jev-for-free"><img src="https://beehiiv-images-production.s3.amazonaws.com/uploads/asset/file/9ff9d5e8-2f74-4ee2-b95f-2bacfdda1e77/ChatGPT_Image_Sep_20__2026__01_04_29_AM.png?t=1789891484" alt="Needle" width="240"></a></td>
<td valign="top"><b><a href="https://www.theunwindai.com/p/get-started-with-jev-for-free">Needle</a></b><br><sub>The Unwind AI (Shubham Saboo, Gargi Gupta) · Article · 2026-09-20</sub><br>Open-source Chrome extension for searching by meaning instead of words: ask a question and Jev scores the page's sentences and highlights the ones that match your intent, with no generated answer.<br><sub><b>How it uses Jev:</b> Jev scores each source sentence against the query and the top passages are highlighted in place.</sub><br><sub>Also: <a href="https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/advanced_llm_apps/needle">repo</a> · <a href="https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/advanced_llm_apps/needle">project</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Shifros/Search-Function-Test"><img src="https://opengraph.githubassets.com/1/Shifros/Search-Function-Test" alt="Search-Function-Test" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Shifros/Search-Function-Test">Search-Function-Test</a></b><br><sub>Shifros · GitHub · 2026-09-17</sub><br>Chat-style search prototype for a Q&amp;A site of 825 articles on Australian business registration, where a Jev Choice picks the article that best answers the query, or none, across four shards.<br><sub>Also: <a href="https://search-function-test.vercel.app">app</a> · <a href="https://search-function-test.vercel.app">app 2</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/liou666/senseek"><img src="https://raw.githubusercontent.com/liou666/senseek/main/assets/senseek/senseek-logo.svg" alt="Senseek" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/liou666/senseek">Senseek</a></b><br><sub>liou666 · GitHub · 2026-09-20</sub><br>Browser extension that searches the page you are reading by meaning from a Ctrl+F-style box and jumps to ranked passages, using your own Jev API key with no backend.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/tylergibbs1/sift"><img src="https://opengraph.githubassets.com/1/tylergibbs1/sift" alt="Sift" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/tylergibbs1/sift">Sift</a></b><br><sub>tylergibbs1 · GitHub · 2026-09-17</sub><br>Chrome extension that re-ranks Google results so answers rise to the top and sales pages and SEO filler fold away.<br><sub><b>How it uses Jev:</b> One parallel call per result with four Nouls (answers the query, promotional, SEO filler, discussion) and a depth Score, combined into a weighted rank.</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/TrainLCD/Functions/blob/dev/src/agent/rerank.ts"><img src="https://opengraph.githubassets.com/1/TrainLCD/Functions" alt="TrainLCD Jev support" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/TrainLCD/Functions/blob/dev/src/agent/rerank.ts">TrainLCD Jev support</a></b><br><sub>TrainLCD · GitHub · 2026-09-17</sub><br>Jev integration in the Cloudflare Worker behind the TrainLCD transit app: a per-candidate Noul reranks the stations its AI chat suggests, and a separate module triages user feedback by spam, category and priority.<br><sub>Also: <a href="https://github.com/TrainLCD/Functions/pull/33">pr</a> · <a href="https://github.com/TrainLCD/Functions">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/TyrellD1/typesafe-ai_smoke-test"><img src="https://opengraph.githubassets.com/1/TyrellD1/typesafe-ai_smoke-test" alt="typesafe-ai_smoke-test" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/TyrellD1/typesafe-ai_smoke-test">typesafe-ai_smoke-test</a></b><br><sub>TyrellD1 · GitHub · 2026-09-17</sub><br>Small router that asks Jev two yes/no questions per prompt to send it to a work store, a life store or both, with a 30-case hand-written eval where all 30 routed correctly.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://yesno.coderai.dev"><img src="https://yesno.coderai.dev/og-image.png" alt="Yes / No" width="240"></a></td>
<td valign="top"><b><a href="https://yesno.coderai.dev">Yes / No</a></b><br><sub>Coder AI · App</sub><br>Free, no-sign-up tool that answers any question with Yes, No or Maybe from a Jev Noul, pulling in live web search when current facts are needed.</td>
</tr>
</table>

Missing something? [Suggest a resource](https://github.com/Li-Evan/awesome-jev/issues/new/choose).
