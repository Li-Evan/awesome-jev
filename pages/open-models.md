# 🧬 Open Models and Compatible Servers

Community models and servers that imitate Jev's interface. Their accuracy and calibration are self-reported and generally below Jev's, so evaluate them on your own data. 240 entries, ranked by community traction.

[← Back to Awesome Jev](https://github.com/Li-Evan/awesome-jev#open-models-and-compatible-servers)

<table>
<tr>
<td width="260" valign="top"><a href="https://github.com/vllm-project/vllm/pull/57250"><img src="https://opengraph.githubassets.com/1/vllm-project/vllm" alt="vLLM DiffusionGemma Jev mode" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/vllm-project/vllm/pull/57250">vLLM DiffusionGemma Jev mode</a></b><br><sub>mmastrac · GitHub · ⭐ 92.4k · 2026-09-16</sub><br>Open vLLM pull request adding a structured generation mode that turns DiffusionGemma into a Jev-like model, with a prototype server for the /v1/systemone endpoint.<br><sub><b>How it uses Jev:</b> Fixes canvas positions in the output format and reads token logprobs to derive the answer and confidence, resampling when entropy is high.</sub><br><sub>Also: <a href="https://news.ycombinator.com/item?id=49734375">demo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://huggingface.co/harshatheg/Qwen-2.5-1B-RLCD"><img src="https://cdn-thumbnails.huggingface.co/social-thumbnails/models/harshatheg/Qwen-2.5-1B-RLCD.png" alt="Qwen-2.5-1B-RLCD" width="240"></a></td>
<td valign="top"><b><a href="https://huggingface.co/harshatheg/Qwen-2.5-1B-RLCD">Qwen-2.5-1B-RLCD</a></b><br><sub>harshatheg · Hugging Face · ♥ 524 · 2026-09-16</sub><br>Parallel constrained decoding engine for Apple Silicon that answers multi-field decision schemas in one pass over stock Qwen2.5-1.5B, shipped as code only with no trained RLCD weights.<br><sub><b>How it uses Jev:</b> Jev-style interface: KV-cache broadcast across fields and logit slicing over allowed values; reports 5.6x to 7.0x lower latency than autoregressive JSON on an M4 Max.</sub><br><sub>Also: <a href="https://huggingface.co/spaces/drinkmoonshine/parallel-constrained-decoding">demo</a> · <a href="https://x.com/TravisJChauvin/status/2101081157421121725">post</a> · <a href="https://x.com/harshagundal/status/2100044305536889015">demo 2</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/NandhaKishorM/laya"><img src="https://raw.githubusercontent.com/NandhaKishorM/laya/main/assets/laya_vs_jev_full.png" alt="Laya" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/NandhaKishorM/laya">Laya</a></b><br><sub>NandhaKishorM · GitHub · ⭐ 12k · 2026-09-18</sub><br>Open, local non-autoregressive decision models on ModernBERT-style encoders, from a 421M English checkpoint to multilingual ones, answering Choice, Score and Noul questions in 33 ms per question with a per-request router.<br><sub>Also: <a href="https://www.reddit.com/r/accelerate/comments/1wk0yq7/laya_421m_open_source_and_local_model_takes_on/">discussion</a> · <a href="https://huggingface.co/spaces/convaiinnovations/laya-demo">app</a> · <a href="https://huggingface.co/convaiinnovations/laya">model</a> · <a href="https://dev.to/nandakishor_m_6cc0adfde9f/i-built-non-autoregressive-decision-models-a-year-ago-then-a-frontier-lab-called-it-a-18me">article</a> · <a href="https://www.reddit.com/r/LocalLLaMA/comments/1wjieap/made_the_horizontal_opensource_model_for_jev_with/">discussion 2</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/taroleo/status/2101106887840370919"><img src="https://pbs.twimg.com/amplify_video_thumb/2101102823408807936/img/k_uNGVHacO6DG6mC.jpg" alt="Distilled 4B local decision model" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/taroleo/status/2101106887840370919">Distilled 4B local decision model</a></b><br><sub>taroleo · X · ♥ 3k · 2026-09-19</sub><br>Distillation of DeepSeek V4 Flash judgments into a Jev-style 4B local model over 26 hours on a DGX Spark, beating the teacher's instant mode at 1/20 the size with about 22ms per decision.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/atomic_chat_hq/status/2102160983409955244"><img src="https://pbs.twimg.com/amplify_video_thumb/2102158998103363584/img/AStT6MxzhJzruHIE.jpg" alt="Laya vs Jev at Tetris" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/atomic_chat_hq/status/2102160983409955244">Laya vs Jev at Tetris</a></b><br><sub>atomic_chat_hq · X · ♥ 2.8k · 2026-09-21</sub><br>Tetris showdown in which the open-weights Laya model, running locally on a 16GB MacBook Air, beats cloud Jev by making decisions 11 times faster.<br><sub>Also: <a href="https://atomic.chat">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/wdobry/laya-playground"><img src="https://brainfunctioncollapse.com/laya/og.png" alt="Laya playground" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/wdobry/laya-playground">Laya playground</a></b><br><sub>wdobry · GitHub · ⭐ 71 · 2026-09-20</sub><br>Local website with games, a benchmark and an agent skill for the open-source Laya decision model, comparing it with hosted Jev on the same 500 labelled examples.<br><sub><b>How it uses Jev:</b> Jev is more accurate out of the box; Laya matches it on simple questions and answers several times faster from a laptop.</sub><br><sub>Also: <a href="https://brainfunctioncollapse.com/laya">app</a> · <a href="https://brainfunctioncollapse.com/laya">app 2</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/mizorewww/laya-mlx"><img src="https://raw.githubusercontent.com/mizorewww/laya-mlx/main/docs/assets/snake-demo.gif" alt="Laya-MLX" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/mizorewww/laya-mlx">Laya-MLX</a></b><br><sub>mizorewww · GitHub · ⭐ 4.3k · 2026-09-19</sub><br>Native MLX runtime for the open Laya typed-decision checkpoints on Apple Silicon: 13.4 ms median per short English decision and 7.4 ms with the multilingual checkpoint, with no PyTorch or cloud API; demoed on Snake.<br><sub>Also: <a href="https://x.com/mizorewww/status/2101473552956555427">demo</a> · <a href="https://pypi.org/project/laya-mlx/">pypi</a> · <a href="https://x.com/tdinh_me/status/2101919182824804560">demo 2</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/TheoLeeCJ/SemIf"><img src="https://raw.githubusercontent.com/TheoLeeCJ/SemIf/master/demo/assets/semif-phase1-replay.gif" alt="SemIf (formerly OpenJev)" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/TheoLeeCJ/SemIf">SemIf (formerly OpenJev)</a></b><br><sub>TheoLeeCJ · GitHub · ⭐ 3.4k · 2026-09-16</sub><br>Independent Jev-like project that answers semantic if-questions by reading option logits from a frozen 4B open model on a home RTX 3090, with a browser demo and no text generation.<br><sub>Also: <a href="https://openjev.com">app</a> · <a href="https://www.reddit.com/r/LocalLLaMA/comments/1whzy7j/qwen35_4b_grabbing_logits_is_almost_jev_or_even/">discussion</a> · <a href="https://openjev.com">app 2</a> · <a href="https://x.com/mygtmhire/status/2100666488625734103">demo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/jaredpalmer/kev"><img src="https://raw.githubusercontent.com/jaredpalmer/kev/main/docs/playground.png" alt="Kev" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/jaredpalmer/kev">Kev</a></b><br><sub>jaredpalmer · GitHub · ⭐ 2.7k · 2026-09-17</sub><br>Open 0.8B to 9B decision models on Qwen3.5 with released weights and a server compatible with <code>/v1/systemone</code>, so the official SDKs can point at it.<br><sub>Also: <a href="https://x.com/jaredpalmer/status/2101028325472841920">demo</a> · <a href="https://news.ycombinator.com/item?id=49783999">discussion</a> · <a href="https://huggingface.co/collections/jaredpalmer">model</a> · <a href="https://news.ycombinator.com/item?id=49783999">discussion 2</a> · <a href="https://huggingface.co/datasets/jaredpalmer/kev-suites">model 2</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/wmoto_ai/status/2100454049359577516"><img src="https://pbs.twimg.com/amplify_video_thumb/2100453978958118912/img/yOW2Lupx9RoG03zB.jpg" alt="Local Jev experiment" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/wmoto_ai/status/2100454049359577516">Local Jev experiment</a></b><br><sub>wmoto_ai · X · ♥ 388 · 2026-09-17</sub><br>Demo of a homemade Jev-style decision setup running on a local LLM, with the author noting its speed still has room to improve.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/featherless-ai/simple-jev"><img src="https://raw.githubusercontent.com/featherless-ai/simple-jev/main/imgs/Simple-Jev-Logo.png" alt="simple-jev" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/featherless-ai/simple-jev">simple-jev</a></b><br><sub>featherless-ai · GitHub · ⭐ 461 · 2026-09-18</sub><br>Turns any Hugging Face model into a decision endpoint with a <code>/v1/systemone</code> alias (probabilities are not calibrated).<br><sub>Also: <a href="https://simple-jev.featherless.ai">site</a> · <a href="https://x.com/picocreator/status/2101006253829046539">demo</a> · <a href="https://x.com/Richelle_Ji/status/2101064292242219407">demo 2</a> · <a href="https://x.com/vintcessun/status/2101896965181395175">demo 3</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/skeptrune/status/2101209390992994570"><img src="https://pbs.twimg.com/amplify_video_thumb/2101204678604455936/img/-Sg1h83wAYEc959c.jpg" alt="deepseek-v4.1-flash-jev" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/skeptrune/status/2101209390992994570">deepseek-v4.1-flash-jev</a></b><br><sub>skeptrune · X · ♥ 1.4k · 2026-09-19</sub><br>Endpoint that makes DeepSeek V4.1 Flash behave like Jev by using SGLang's scoring API to return probabilities over a fixed answer set instead of generated text.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/TianyuCodings/NanoJev"><img src="https://opengraph.githubassets.com/1/TianyuCodings/NanoJev" alt="NanoJev" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/TianyuCodings/NanoJev">NanoJev</a></b><br><sub>TianyuCodings · GitHub · ⭐ 1.9k · 2026-09-17</sub><br>Open 0.6B Jev replica trained for four specific games, with weights and data; not a general-purpose substitute.<br><sub>Also: <a href="https://x.com/QingQ77/status/2101125879766421755">demo</a> · <a href="https://huggingface.co/c-tianyu/nanojev">model</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/bespokelabsai/nimble"><img src="https://raw.githubusercontent.com/bespokelabsai/nimble/main/assets/diagrams/nimble-infographic.svg" alt="Bespoke Nimble" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/bespokelabsai/nimble">Bespoke Nimble</a></b><br><sub>bespokelabsai · GitHub · ⭐ 1.5k · 2026-09-18</sub><br>Open data, recipe, and Qwen3.5-9B LoRA model for Jev-style typed decisions, trained on contrastive negatives made by flipping one fact; reports 90.1% agreement with Jev versus 66.4% for base Qwen.<br><sub>Also: <a href="https://x.com/madiator/status/2100990591215783946">demo</a> · <a href="https://huggingface.co/bespokelabs/bespoke-nimble-9b">model</a> · <a href="https://news.ycombinator.com/item?id=49757009">discussion</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/vinnylarouge/jevlike"><img src="https://raw.githubusercontent.com/vinnylarouge/jevlike/main/docs/architecture.svg" alt="Jevlike" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/vinnylarouge/jevlike">Jevlike</a></b><br><sub>vinnylarouge · GitHub · ⭐ 1.2k · 2026-09-16</sub><br>Independent starter model with the same shape as Jev: a small one-pass scorer mapping text plus N options to one probability per option, with Doom and chess vision demos and a Wikispeedia next-click example.<br><sub>Also: <a href="https://x.com/vinnylarouge/status/2100170846346097083">demo</a> · <a href="https://news.ycombinator.com/item?id=49731282">discussion</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://www.youtube.com/watch?v=bcGO7xre46o"><img src="https://i.ytimg.com/vi/bcGO7xre46o/hqdefault.jpg" alt="Jev mode for llama.cpp" width="240"></a></td>
<td valign="top"><b><a href="https://www.youtube.com/watch?v=bcGO7xre46o">Jev mode for llama.cpp</a></b><br><sub>Codacus · YouTube · ♥ 1.2k · 2026-09-21</sub><br>Fork of llama.cpp adding a llama-server endpoint that takes instructions, a schema, and state and returns every field with a confidence score; 17.3 ms per decision in bulk on a 2 GB model.<br><sub>Also: <a href="https://github.com/thecodacus/llama.cpp/tree/parallel-decision">repo</a> · <a href="https://github.com/thecodacus/decision-playground">playground</a> · <a href="https://huggingface.co/harshatheg/Qwen-2.5-1B-RLCD">model</a> · <a href="https://github.com/thecodacus/llama.cpp">project</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"></td>
<td valign="top"><b><a href="https://x.com/KUMAN_R/status/2101473262693994936">Six Jev clones in two days</a></b><br><sub>KUMAN_R · X · ♥ 756 · 2026-09-20</sub><br>Japanese summary comparing the architectures of six open Jev clones: Laya, DiffusionGemmaJev, Bespoke Nimble, SemIf (formerly OpenJev), Jevlike and Kev-0.5B.<br><sub>Also: <a href="https://www.latent.space/p/ainews-here-are-6-clones-of-jev-in">article</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://huggingface.co/cua-ai/cua-s1-forms"><img src="https://cdn-thumbnails.huggingface.co/social-thumbnails/models/cua-ai/cua-s1-forms.png" alt="cua-s1-forms" width="240"></a></td>
<td valign="top"><b><a href="https://huggingface.co/cua-ai/cua-s1-forms">cua-s1-forms</a></b><br><sub>cua-ai · Hugging Face · ♥ 102 · 2026-09-18</sub><br>Tiny Jev-like option scorer (706,048 parameters, 2.8 MB) that rates fill, check, click or skip for every form field in one parallel pass, built as the decision layer for cua-driver.<br><sub><b>How it uses Jev:</b> Same input/output contract as Jev; reports 99.7% on its own form-filling eval against Jev's 83.6%.</sub><br><sub>Also: <a href="https://github.com/trycua/cua/tree/main/libs/cua-s1">repo</a> · <a href="https://x.com/be_arsh/status/2101026864341164110">demo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/mizorewww/laya-coreml"><img src="https://raw.githubusercontent.com/mizorewww/laya-coreml/main/docs/assets/snake-demo.gif" alt="Laya-CoreML" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/mizorewww/laya-coreml">Laya-CoreML</a></b><br><sub>mizorewww · GitHub · ⭐ 989 · 2026-09-19</sub><br>Open-weight port of the Jev-like Laya model to Apple Core ML and the Neural Engine, serving the System One contract locally, with a Snake demo playing on live probabilities.<br><sub><b>How it uses Jev:</b> Implements system_one over Choice, Score and Noul; about 4.98 ms P50 for one short decision on an M3 Max with ANE FP16.</sub><br><sub>Also: <a href="https://pypi.org/project/laya-coreml/">pypi</a> · <a href="https://huggingface.co/aac6fef/laya-multilingual-coreml-ane">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/Lonely__MH/status/2101823975349244095"><img src="https://pbs.twimg.com/amplify_video_thumb/2101708973036785664/img/DgCMkHUOuz-yVIOi.jpg" alt="Laya-MLX vs Jev accuracy test" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/Lonely__MH/status/2101823975349244095">Laya-MLX vs Jev accuracy test</a></b><br><sub>Lonely__MH · X · ♥ 102 · 2026-09-21</sub><br>Two rounds of 100 decision questions on an M2 Pro: local Laya-MLX answered in 13.7ms per question but at about 50% accuracy, while cloud Jev was slower but far more accurate.<br><sub>Also: <a href="https://github.com/mizorewww/laya-mlx">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Zefan-Cai/Open-Jev"><img src="https://cdn-thumbnails.huggingface.co/social-thumbnails/models/ZefanCai/Open-Jev-9B.png" alt="Open-Jev" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Zefan-Cai/Open-Jev">Open-Jev</a></b><br><sub>Zefan-Cai · GitHub · ⭐ 118 · 2026-09-20</sub><br>Open probability-decision models on Qwen3.5-2B, Qwen3.5-9B, and Qwen3.8-27B that score supplied candidates without generation, released as LoRA adapters with a trained decision head, a dataset, and benchmarks.<br><sub>Also: <a href="https://zefan-cai.github.io/open-jev">site</a> · <a href="https://huggingface.co/ZefanCai/Open-Jev-9B">model</a> · <a href="https://huggingface.co/ZefanCai/Open-Jev-2B">model 2</a> · <a href="https://x.com/Zefan_Cai/status/2101782158658695388">demo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/githubnext/localjev"><img src="https://opengraph.githubassets.com/1/githubnext/localjev" alt="LocalJev" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/githubnext/localjev">LocalJev</a></b><br><sub>githubnext · GitHub · ⭐ 707 · 2026-09-18</sub><br>Bun server from GitHub Next that exposes a local Jev-compatible /v1/systemone API backed by DiffusionGemma, prompting for JSON probabilities instead of reading logits, with a 1,200-request bake-off.<br><sub>Also: <a href="https://news.ycombinator.com/item?id=49766255">discussion</a> · <a href="https://x.com/GitHubNext/status/2101193436816920798">demo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/BystAnd3rs/status/2101648153984528700"><img src="https://pbs.twimg.com/amplify_video_thumb/2101647092817305600/img/WGklbFZGYL0CnWBd.jpg" alt="Laya vs Jev Snake battle" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/BystAnd3rs/status/2101648153984528700">Laya vs Jev Snake battle</a></b><br><sub>BystAnd3rs · X · ♥ 158 · 2026-09-20</sub><br>Snake duel built with Codex between local Laya and the Jev API on an M5 Pro: median decision time 15.3 ms for Laya versus 298.1 ms for Jev.<br><sub>Also: <a href="https://github.com/mizorewww/laya-mlx">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/incoai/splash"><img src="https://opengraph.githubassets.com/1/incoai/splash" alt="Splash" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/incoai/splash">Splash</a></b><br><sub>incoai · GitHub · ⭐ 579 · 2026-09-18</sub><br>Local Apple silicon inference engine for coding agents that also serves a TypeSafe-compatible /v1/systemone endpoint, answering noul, choice and score questions from logits and working with the official SDK.<br><sub>Also: <a href="https://inco.ai/blog/splash/">article</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"></td>
<td valign="top"><b><a href="https://news.ycombinator.com/item?id=49777106">Laya on Mac M4 CoreML</a></b><br><sub>putna · Hacker News · ▲ 167 · 2026-09-20</sub><br>Recipe for running the multilingual Laya decision model offline on an M4 Mac through CoreML on the Neural Engine, with a snake demo, at about 45 decisions per second.<br><sub>Also: <a href="https://gist.github.com/fordnox/e592d0f68b543fd044be8e6d040863a0">gist</a> · <a href="https://gist.github.com/fordnox/e592d0f68b543fd044be8e6d040863a0">project</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://huggingface.co/AlexWortega/openjev"><img src="https://huggingface.co/AlexWortega/openjev/resolve/main/assets/radar_openjev.png" alt="openjev" width="240"></a></td>
<td valign="top"><b><a href="https://huggingface.co/AlexWortega/openjev">openjev</a></b><br><sub>Alex Wortega · Hugging Face · ♥ 431 · 2026-09-16</sub><br>Qwen3.5 checkpoints trained as a single NLI cross-encoder whose argmax entailment picks the answer, used zero-shot for reranking, grading, guarding and playing Doom from text or pixels.<br><sub><b>How it uses Jev:</b> Jev-like judgments via entailment over statements about the state; 4B v2 averages 10.4 Doom kills per episode from pixels, and 35B-A3B heads are included.</sub><br><sub>Also: <a href="https://x.com/justALEXWORTEGA/status/2100341039986798930">demo</a> · <a href="https://www.reddit.com/r/LocalLLaMA/comments/1wib9kj/openjev/">discussion</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/SiliconLabAI/OpenJev"><img src="https://opengraph.githubassets.com/1/SiliconLabAI/OpenJev" alt="OpenJev (SiliconLabAI)" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/SiliconLabAI/OpenJev">OpenJev (SiliconLabAI)</a></b><br><sub>SiliconLabAI · GitHub · ⭐ 67 · 2026-09-20</sub><br>Open System One-style decision playground that answers a state and typed questions through LLM micro-scorers, one structured JSON call to an OpenAI-compatible model, or the open Mapika/decider weights.<br><sub>Also: <a href="https://www.youtube.com/watch?v=xtXq279B4Go">video</a> · <a href="https://www.youtube.com/watch?v=xtXq279B4Go">video 2</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/theAlexQuach/status/2101397697454649684"><img src="https://pbs.twimg.com/media/HSmoWsEaQAEYMBV.jpg?name=orig" alt="Open vision Jev alternatives" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/theAlexQuach/status/2101397697454649684">Open vision Jev alternatives</a></b><br><sub>theAlexQuach · X · ♥ 177 · 2026-09-19</sub><br>Tests open-source Jev-like models that accept images, finding DiffusionGemma (via a vLLM PR) and reflex on the Pareto front for vision decisions.<br><sub>Also: <a href="https://github.com/vllm-project/vllm/pull/57250">vllm-pr</a> · <a href="https://github.com/kshetrajna12/reflex">reflex</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/wfzyx/von"><img src="https://external-preview.redd.it/VW75dC3ID5HFYYIWiSOP1LncNeZEjQCbaTdR9KcPGvI.png?auto=webp&amp;s=bb6e8f3dc6956150a4710c2fe60ee80968b33d3f" alt="Von" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/wfzyx/von">Von</a></b><br><sub>wfzyx · GitHub · ⭐ 381 · 2026-09-18</sub><br>Open non-autoregressive decision model of about 395M parameters with public weights, training code and a System One-shaped API, answering Choice, Noul and Score questions locally in tens of milliseconds.<br><sub>Also: <a href="https://news.ycombinator.com/item?id=49781612">discussion</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://www.reddit.com/r/LocalLLM/comments/1wjv46i/i_have_created_open_source_jev_and_trained_it_to/"><img src="https://external-preview.redd.it/M3RzbGFlaGwyYnFoMXuP6V8vNBO5_YLg7eGU503KPrTQWjhN5GEpCDWeUnnY.png?format=pjpg&amp;auto=webp&amp;s=e22eb092e7b5afa83d5188c0b5e8e92e3dca3b1d" alt="Brain DOOM decision policy" width="240"></a></td>
<td valign="top"><b><a href="https://www.reddit.com/r/LocalLLM/comments/1wjv46i/i_have_created_open_source_jev_and_trained_it_to/">Brain DOOM decision policy</a></b><br><sub>mkschreder2 · Reddit · ▲ 119 · 2026-09-18</sub><br>Local Jev-style policy that plays DOOM in real time: a frozen MiniLM encoder reads the observation text and a small trained head picks actions, at 58.3 ms per decision.<br><sub>Also: <a href="https://github.com/swedishembedded/brain/tree/main/samples/decision/doom">repo</a> · <a href="https://github.com/mkschreder/restful-doom">game-server</a> · <a href="https://github.com/swedishembedded/brain/tree/main/samples/decision/doom">project</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/0xLogicrw/status/2101545266507551141"><img src="https://pbs.twimg.com/media/HSowRg-W4AAdElX.jpg?name=orig" alt="Four schools of OpenJEV" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/0xLogicrw/status/2101545266507551141">Four schools of OpenJEV</a></b><br><sub>0xLogicrw · X · ♥ 233 · 2026-09-20</sub><br>Chinese comparison of 8 open Jev-like projects (SemIf, Simple Jev, Laya, Von, Verdict, Kev, Nimble, OpenJev) grouped into four approaches, with reported accuracy and latency.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/nico-martin/open-jev"><img src="https://pbs.twimg.com/amplify_video_thumb/2101924588837896193/img/vb3r7XPYfWQwfrBV.jpg" alt="open-jev (nico-martin)" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/nico-martin/open-jev">open-jev (nico-martin)</a></b><br><sub>nico-martin · GitHub · ⭐ 19 · 2026-09-20</sub><br>Browser-focused TypeScript library that runs open Jev-shaped typed-decision models such as Kev on-device through Transformers.js, on WebGPU or WebAssembly, returning a calibrated distribution per question.<br><sub>Also: <a href="https://www.npmjs.com/package/open-jev">npm</a> · <a href="https://x.com/nicodotdev/status/2101925770432008665">demo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/razorback16/openjev"><img src="https://external-preview.redd.it/vdZrJPXw6MSvl0ZZRNggdJnJjOT14qhqZDKUAr_MuuE.png?auto=webp&amp;s=a01efcc5d87a9abbba518b4fcd3b7260501a06c4" alt="OpenJev" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/razorback16/openjev">OpenJev</a></b><br><sub>razorback16 · GitHub · ⭐ 287 · 2026-09-18</sub><br>Open System One decision server that speaks Jev's wire API, so TypeSafe SDKs work unchanged, reading typed answers off DiffusionGemma 26B-A4B probabilities via vLLM or MLX, including questions about images.<br><sub>Also: <a href="https://codiv.ai">app</a> · <a href="https://www.reddit.com/r/LocalLLaMA/comments/1wjlyzr/still_on_the_jev_waitlist_i_hosted_openjev_its/">discussion</a> · <a href="https://codiv.ai">app 2</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Mapika/decider"><img src="https://opengraph.githubassets.com/1/Mapika/decider" alt="decider" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Mapika/decider">decider</a></b><br><sub>Mapika · GitHub · ⭐ 282 · 2026-09-16</sub><br>Open System One-style models fine-tuned from Qwen3.5, a 2B and a 35B mixture-of-experts, that return a probability distribution for every typed question in one forward pass, demoed on ten text games and Super Mario Bros.<br><sub>Also: <a href="https://huggingface.co/mapika/decider-2b">model</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/ekzhang/openjev-sglang"><img src="https://i.imgur.com/wHM3jxV.gif" alt="openjev-sglang" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/ekzhang/openjev-sglang">openjev-sglang</a></b><br><sub>ekzhang · GitHub · ⭐ 259 · 2026-09-17</sub><br>Compatible endpoint that serves an open mixture-of-experts model on SGLang, with BoolQ and MMLU-Pro comparisons.<br><sub>Also: <a href="https://www.reddit.com/r/typesafe/comments/1wmhbuu/ekzhangopenjevsglang_jevcompatible_api_endpoint/">discussion</a> · <a href="https://x.com/ekzhang1/status/2100651678110515383">demo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Heman10x-NGU/openJev-verdict-2.0"><img src="https://raw.githubusercontent.com/Heman10x-NGU/openJev-verdict-2.0/main/assets/v1.4/benchmark-leaderboard-chart.png" alt="openJev-verdict-2.0" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Heman10x-NGU/openJev-verdict-2.0">openJev-verdict-2.0</a></b><br><sub>Heman10x-NGU · GitHub · ⭐ 249 · 2026-09-19</sub><br>ModernBERT-based 151M non-autoregressive decision model with separate distribution and confidence heads, public weights, saved evaluation artifacts and an in-browser WebGPU demo; its benchmark results are self-reported.<br><sub>Also: <a href="https://www.reddit.com/r/typesafe/comments/1wm8avg/heman10xnguopenjevverdict20_calibrated_151m/">discussion</a> · <a href="https://heman10x-ngu.github.io/openJev-verdict-2.0/">docs</a> · <a href="https://heman10x-ngu.github.io/openJev-verdict-2.0">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Rizzo-AI-Academy/rizzo-flow"><img src="https://raw.githubusercontent.com/Rizzo-AI-Academy/rizzo-flow/main/assets/rizzo_flow_logo.png" alt="Rizzo Flow" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Rizzo-AI-Academy/rizzo-flow">Rizzo Flow</a></b><br><sub>Rizzo-AI-Academy · GitHub · ⭐ 240 · 2026-09-21</sub><br>Local open-model decision server that reads answer-token probabilities instead of generating text, behind a Jev-compatible Choice, Score and Noul HTTP API plus a numeric primitive; no quality parity with Jev is claimed.<br><sub>Also: <a href="https://rizzo-ai-academy.github.io/rizzo-flow/">site</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/ruvnet/RuVector/tree/main/npm/packages/typesafe"><img src="https://repository-images.githubusercontent.com/1099547803/948d2495-1db9-47f6-9ea1-f7f977343e5f" alt="@ruvector/typesafe" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/ruvnet/RuVector/tree/main/npm/packages/typesafe">@ruvector/typesafe</a></b><br><sub>ruvnet · Package · ⭐ 4.5k repo · 2025-11-19</sub><br>Local, network-free typed decisions over sentence embeddings that accept Jev's /v1/systemone request and response shape, returning calibrated confidence and an abstain mass.<br><sub><b>How it uses Jev:</b> Native napi-rs core with a WASM fallback; release gates target p95 of 50 ms native and 150 ms WASM.</sub><br><sub>Also: <a href="https://www.npmjs.com/package/@ruvector/typesafe">npm</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/hr98w/jev-visual"><img src="https://raw.githubusercontent.com/hr98w/jev-visual/main/docs/images/jev-visual-en.png" alt="Jev Visual" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/hr98w/jev-visual">Jev Visual</a></b><br><sub>hr98w · GitHub · ⭐ 224 · 2026-09-17</sub><br>Educational Jev-like visual inference on Apple Silicon: Qwen3.5-0.8B on MLX answers choice, yes/no and score questions about one image from shared context and logits, with sorting-factory, Breakout and gesture demos.<br><sub>Also: <a href="https://x.com/hr98w/status/2100646513412292873">demo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://www.reddit.com/r/MachineLearning/comments/1wl13eu/programasweights_compile_english_function/"><img src="https://preview.redd.it/a5zxim8w8kqh1.png?width=2122&amp;format=png&amp;auto=webp&amp;s=c009655b083bddd316687c2fdef0365c9334c82e" alt="ProgramAsWeights" width="240"></a></td>
<td valign="top"><b><a href="https://www.reddit.com/r/MachineLearning/comments/1wl13eu/programasweights_compile_english_function/">ProgramAsWeights</a></b><br><sub>yuntiandeng · Reddit · ▲ 74 · 2026-09-19</sub><br>Research project that compiles an English function description into a LoRA adapter for a frozen Qwen3-0.6B, giving local text classifiers that run on a CPU without an API.<br><sub>Also: <a href="https://github.com/programasweights/programasweights-python">repo</a> · <a href="https://huggingface.co/programasweights/models">models</a> · <a href="https://github.com/programasweights/programasweights-python">project</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/AstroHanRay/status/2101709185155231895"><img src="https://pbs.twimg.com/media/HSrFNeXbEAArB6H.jpg?name=orig" alt="Train your own Jev-like model" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/AstroHanRay/status/2101709185155231895">Train your own Jev-like model</a></b><br><sub>AstroHanRay · X · ♥ 132 · 2026-09-20</sub><br>Trains a Jev-style judgment model with RLCD on Qwen3.5-4B plus a rank-8 LoRA (32K questions, 9 GPU hours, about $42), tying Jev on the 120-question JevBench.<br><sub>Also: <a href="https://huggingface.co/AstroHan/decision-head-qwen3.5-4b-rlcd-32k">model</a> · <a href="https://huggingface.co/astrohan/decision-head-qwen3.5-4b-rlcd-32k">project</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/logan-markewich/jeff"><img src="https://opengraph.githubassets.com/1/logan-markewich/jeff" alt="Jeff" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/logan-markewich/jeff">Jeff</a></b><br><sub>logan-markewich · GitHub · ⭐ 206 · 2026-09-19</sub><br>Compatible server built on a 400M-parameter encoder, with benchmark comparisons against Jev.<br><sub>Also: <a href="https://x.com/LoganMarkewich/status/2101142971223781587">demo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/receptron/laya"><img src="https://opengraph.githubassets.com/1/receptron/laya" alt="@receptron/laya" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/receptron/laya">@receptron/laya</a></b><br><sub>receptron · GitHub · ⭐ 205 · 2026-09-19</sub><br>Node.js and TypeScript package that runs Laya, the open Jev-compatible decision model by Convai Innovations, through ONNX Runtime and returns choice, score, and noul answers in one forward pass.<br><sub>Also: <a href="https://www.npmjs.com/package/@receptron/laya">npm</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/zhilinjerrywag/status/2101962974898397246"><img src="https://pbs.twimg.com/media/HSurH4YWYAESh8q.jpg" alt="Mev" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/zhilinjerrywag/status/2101962974898397246">Mev</a></b><br><sub>zhilinjerrywag · Article · ♥ 38 · 2026-09-21</sub><br>Decision model with 0.4B parameters for job and candidate matching, fine-tuned from Laya in about 45 minutes; it ties Kev-4B (Spearman 0.733 vs 0.730) but Jev still ranks best at 0.818.<br><sub><b>How it uses Jev:</b> Same interface as Jev: a Noul for recommend and a five-level Score for match strength, compared zero-shot against Jev.</sub><br><sub>Also: <a href="https://github.com/NandhaKishorM/laya">base-model</a> · <a href="https://metix.ai/">company</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://www.youtube.com/watch?v=JsVM4vgspEU"><img src="https://i.ytimg.com/vi/JsVM4vgspEU/hqdefault.jpg" alt="I built Jev for free" width="240"></a></td>
<td valign="top"><b><a href="https://www.youtube.com/watch?v=JsVM4vgspEU">I built Jev for free</a></b><br><sub>Micah · YouTube · ♥ 129 · 2026-09-19</sub><br>Builds a free Jev-style model by distilling Qwen3 0.6B from a 27B teacher on one RTX 5090, then plays Doom through ViZDoom; agreement with the teacher rose from 54% to 93%.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/NotXf1le/choosekit"><img src="https://raw.githubusercontent.com/NotXf1le/choosekit/master/benchmarks/supergpqa-benchmark.svg" alt="choosekit" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/NotXf1le/choosekit">choosekit</a></b><br><sub>NotXf1le · GitHub · ⭐ 18 · 2026-09-19</sub><br>Library that scores a finite set of choices with llama.cpp, Ollama, or OpenRouter models and returns typed decisions with probability distributions, plus an MCP server and a SuperGPQA benchmark against Jev 1.13.<br><sub>Also: <a href="https://www.reddit.com/r/LLMDevs/comments/1wkc9hp/i_tried_jevstyle_decisions_with_local_qwen_same/">discussion</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/mmastrac/djev-spark"><img src="https://raw.githubusercontent.com/mmastrac/djev-spark/main/docs/playground.jpg" alt="djev-spark" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/mmastrac/djev-spark">djev-spark</a></b><br><sub>mmastrac · GitHub · ⭐ 169 · 2026-09-18</sub><br>Container recipe that serves DiffusionGemma 26B-A4B in NVFP4 on a DGX Spark behind Jev's /v1/systemone API, pairing patched vLLM structured reads with a separate decision server.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/kunpengtalk/OmniStudio"><img src="https://raw.githubusercontent.com/kunpengtalk/OmniStudio/main/docs/images/screenshot-jev.png" alt="OmniStudio JEV judgments" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/kunpengtalk/OmniStudio">OmniStudio JEV judgments</a></b><br><sub>kunpengtalk · GitHub · ⭐ 147 · 2026-09-09</sub><br>Local-first desktop LLM workbench with a JEV typed-judgment page that runs Laya locally via laya-mlx or connects to the cloud, exposing a TypeSafe-compatible endpoint for the official SDKs.<br><sub><b>How it uses Jev:</b> Noul, Choice and Score answers with probability distributions; SDKs only need TYPESAFE_BASE_URL and TYPESAFE_API_KEY changed.</sub><br><sub>Also: <a href="https://omnilabs.vibeadmin.cn/#/omnistudio">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/yoheinakajima/glance"><img src="https://pbs.twimg.com/amplify_video_thumb/2102213606414921728/img/cLKQS-9p31mko41V.jpg" alt="Glance" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/yoheinakajima/glance">Glance</a></b><br><sub>yoheinakajima · GitHub · ⭐ 7 · 2026-09-21</sub><br>Harness for asking an open vision-language model (Qwen3-VL-4B by default) typed yes/no, pick-one and rating questions about an image, reading calibrated probabilities from one forward pass, with Jev-style request shapes.<br><sub>Also: <a href="https://glance.yohei.me">app</a> · <a href="https://x.com/yoheinakajima/status/2102213665361690906">demo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Yinsongxu/LLM2Jev"><img src="https://raw.githubusercontent.com/Yinsongxu/LLM2Jev/main/assets/llm2jev-banner.jpeg" alt="LLM2Jev" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Yinsongxu/LLM2Jev">LLM2Jev</a></b><br><sub>Yinsongxu · GitHub · ⭐ 126 · 2026-09-19</sub><br>Toolkit that turns local language models into Jev-style decision engines by reading Choice, Score and Noul answers from prefill logits via Transformers or SGLang, with a /v1/systemone endpoint and image input.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/kshetrajna12/reflex"><img src="https://opengraph.githubassets.com/1/kshetrajna12/reflex" alt="reflex" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/kshetrajna12/reflex">reflex</a></b><br><sub>kshetrajna12 · GitHub · ⭐ 110 · 2026-09-17</sub><br>Open Jev re-creation on stock Qwen3.5 that answers Choice, Score and Noul questions in one batched pass behind a /v1/systemone server, with a WebGPU demo and a LoRA recipe for honest probabilities; ~200 ms per request.<br><sub>Also: <a href="https://kshetrajna12.github.io/reflex">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/sabeel111/OpenSourceJev"><img src="https://external-preview.redd.it/NGQzMnA1dW4yaHFoMfp6xNCARVGeYVpoP66WhgS8I5hNmzYWXyIRArIESs6K.png?format=pjpg&amp;auto=webp&amp;s=2d4092332a97f0aebb7b7e82f599bf681e05877f" alt="OpenSourceJev" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/sabeel111/OpenSourceJev">OpenSourceJev</a></b><br><sub>sabeel111 · GitHub · ⭐ 24 · 2026-09-19</sub><br>Research experiment that runs a local System One-style decision engine on llama.cpp and Qwen, projecting next-token logits onto answer options for calibrated typed decisions on consumer hardware.<br><sub>Also: <a href="https://www.reddit.com/r/LocalLLM/comments/1wkl8c9/my_version_of_jev_running_locally_playing_doom/">discussion</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/daseinlabs/open-jev"><img src="https://raw.githubusercontent.com/daseinlabs/open-jev/main/docs/media/doom-recording.gif" alt="openjev (daseinlabs)" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/daseinlabs/open-jev">openjev (daseinlabs)</a></b><br><sub>daseinlabs · GitHub · ⭐ 94 · 2026-09-17</sub><br>One-pass option scorer with a local Gemma 3 4B on Apple Silicon via MLX that prefills the context once, scores every option in a single forward pass, and exposes a System One-compatible endpoint.<br><sub><b>How it uses Jev:</b> Documents zero-shot overconfidence and offers optional per-task finetuning.</sub><br><sub>Also: <a href="https://news.ycombinator.com/item?id=49737236">demo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Davipar/djev-dev"><img src="https://raw.githubusercontent.com/Davipar/djev-dev/main/docs/assets/djev-dev-cover.png" alt="djev dev" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Davipar/djev-dev">djev dev</a></b><br><sub>Davipar · GitHub · ⭐ 93 · 2026-09-19</sub><br>Open implementation of typed decisions on DiffusionGemma and vLLM that reads label probabilities from denoised answer positions, with image inputs, image choices and live camera sampling.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/theoleecj/status/2100212661619503176"><img src="https://pbs.twimg.com/amplify_video_thumb/2100211213582143488/img/Bzldvxr0IbvhDHAw.jpg" alt="OpenJev" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/theoleecj/status/2100212661619503176">OpenJev</a></b><br><sub>theoleecj · X · ♥ 15 · 2026-09-16</sub><br>Open-source on-device inference for Jev-style typed decisions with probabilities, built on Qwen 3 4B, 0.6B and 0.8B, and able to run in Chrome.<br><sub>Also: <a href="https://github.com/theoleecj/openjev">repo</a> · <a href="https://openjev.com">app</a> · <a href="https://github.com/theoleecj/openjev">project</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Heman10x-NGU/Verdict-open-jev"><img src="https://raw.githubusercontent.com/Heman10x-NGU/Verdict-open-jev/main/assets/v1.4/benchmark-leaderboard-chart.png" alt="OpenJev (Verdict)" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Heman10x-NGU/Verdict-open-jev">OpenJev (Verdict)</a></b><br><sub>Heman10x-NGU · GitHub · ⭐ 67 · 2026-09-17</sub><br>Open 151M-parameter ModernBERT decision engine inspired by Jev and RLCD that evaluates typed questions in one non-autoregressive pass in under 35 ms, with a JevBench audit and an in-browser WebGPU playground.<br><sub>Also: <a href="https://huggingface.co/heman10x/rlcd-modernbert-151m">huggingface</a> · <a href="https://huggingface.co/heman10x/rlcd-modernbert-151m">model</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/deepopen-com/deepopen"><img src="https://raw.githubusercontent.com/deepopen-com/deepopen/main/%E6%89%93%E6%A6%9C.png" alt="DeepOpen" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/deepopen-com/deepopen">DeepOpen</a></b><br><sub>deepopen-com · GitHub · ⭐ 59 · 2026-09-21</sub><br>Laya-based open System 1 decision engine with a Chinese technical whitepaper, a script/language router over English, multilingual and typed-decision checkpoints, and training experiments on CLINC150 and Banking77.<br><sub><b>How it uses Jev:</b> Answers typed Choice/Score/Noul questions in one non-autoregressive pass; reports 33 ms per request on a T4.</sub><br><sub>Also: <a href="https://deepopen.com">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/shi3z/deepseekv4.1-A100-custom"><img src="https://raw.githubusercontent.com/shi3z/deepseekv4.1-A100-custom/main/assets/dashboard.jpg" alt="DeepSeek-V4.1 A100 Jev Mode" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/shi3z/deepseekv4.1-A100-custom">DeepSeek-V4.1 A100 Jev Mode</a></b><br><sub>shi3z · GitHub · ⭐ 54 · 2026-09-11</sub><br>Custom DeepSeek-V4.1-Flash runtime for A100 GPUs with a Jev Mode that scores candidates in parallel instead of decoding JSON, reporting up to 2,854x speedup on 30-field extraction in 24 ms.<br><sub><b>How it uses Jev:</b> Non-autoregressive candidate log-probability scoring with a persistent GPU prefix tree; includes a script comparing official Jev with the local mode.</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/bnsd55/jevmlx"><img src="https://opengraph.githubassets.com/1/bnsd55/jevmlx" alt="jevmlx" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/bnsd55/jevmlx">jevmlx</a></b><br><sub>bnsd55 · GitHub · ⭐ 54 · 2026-09-17</sub><br>Local Jev-style decision layer for Apple Silicon that scores every allowed option of boolean, enum and multi-select fields from MLX model logits in one prefill and returns schema-valid JSON with per-field probabilities.<br><sub><b>How it uses Jev:</b> Offers a System One-compatible endpoint and a benchmark runner.</sub><br><sub>Also: <a href="https://news.ycombinator.com/item?id=49743108">discussion</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://www.reddit.com/r/LocalLLM/comments/1wkrk48/laya_vision_is_open_source_jev_for_images/"><img src="https://external-preview.redd.it/UtFOem1Lybo3LMdOVLun0w9gD1TIz-RsVEPJK1E931Q.png?auto=webp&amp;s=b4618d2ffc0db450df912f1f3046530e58b7384b" alt="Laya Vision" width="240"></a></td>
<td valign="top"><b><a href="https://www.reddit.com/r/LocalLLM/comments/1wkrk48/laya_vision_is_open_source_jev_for_images/">Laya Vision</a></b><br><sub>Fickle-Ad-866 · Reddit · ▲ 18 · 2026-09-19</sub><br>Open Jev-style decision model for images built on SmolVLM 256M, returning probabilities over a fixed set of choices for screenshots, photos, and GUI elements.<br><sub>Also: <a href="https://huggingface.co/thaitea/laya-vision-smolvlm-256m">model</a> · <a href="https://huggingface.co/thaitea/laya-vision-smolvlm-256m">project</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://huggingface.co/com-kotobalabs/open-jev-deberta-v3-large"><img src="https://cdn-thumbnails.huggingface.co/social-thumbnails/models/com-kotobalabs/open-jev-deberta-v3-large.png" alt="open-jev-deberta-v3-large" width="240"></a></td>
<td valign="top"><b><a href="https://huggingface.co/com-kotobalabs/open-jev-deberta-v3-large">open-jev-deberta-v3-large</a></b><br><sub>com-kotobalabs · Hugging Face · ♥ 52 · 2026-09-18</sub><br>Open Jev-shaped model on DeBERTa-v3-large that answers any number of choice, score and noul questions about one state in a single pass; 0.854 in-domain and 0.690 out-of-domain accuracy, 28 ms for 10 questions.<br><sub>Also: <a href="https://github.com/kotoba-lang/typed-decisions">repo</a> · <a href="https://huggingface.co/onnx-community/open-jev-deberta-v3-large-ONNX">model</a> · <a href="https://huggingface.co/spaces/hugging-apps/open-jev-deberta-v3-large-demo">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/deepanwadhwa/OpenDecision"><img src="https://opengraph.githubassets.com/1/deepanwadhwa/OpenDecision" alt="OpenDecision" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/deepanwadhwa/OpenDecision">OpenDecision</a></b><br><sub>deepanwadhwa · GitHub · ⭐ 52 · 2026-09-17</sub><br>Open-source local semantic decision engine modeled on Jev that answers Choice, Noul and Score questions plus a supports/contradicts Relation over structured state and documents, demoed playing Doom.<br><sub>Also: <a href="https://deepanwadhwa.github.io/OpenDecision/">link</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/ikermoel/open-alternative-jev"><img src="https://raw.githubusercontent.com/ikermoel/open-alternative-jev/main/benchmarks/figures/race.png" alt="Open Alternative to Jev" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/ikermoel/open-alternative-jev">Open Alternative to Jev</a></b><br><sub>ikermoel · GitHub · ⭐ 47 · 2026-09-18</sub><br>Python library that reads option-token probabilities from open-weights models through Transformers or vLLM to give typed, calibrated Choice, Score and Noul decisions in one pass, with temperature scaling and benchmarks.<br><sub>Also: <a href="https://news.ycombinator.com/item?id=49750584">discussion</a> · <a href="https://huggingface.co/spaces/IkerMoel/open-alternative-jev">app</a> · <a href="https://huggingface.co/spaces/IkerMoel/open-alternative-jev">app 2</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/SAGAR-TAMANG/sarvam-jev"><img src="https://opengraph.githubassets.com/1/SAGAR-TAMANG/sarvam-jev" alt="sarvam-jev" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/SAGAR-TAMANG/sarvam-jev">sarvam-jev</a></b><br><sub>SAGAR-TAMANG · GitHub · ⭐ 46 · 2026-09-18</sub><br>Open Jev-style inference engine on Sarvam's Indic sarvam-1 model that reads typed answers from lettered-option logits instead of generating JSON, reusing one state prefill across questions, in the browser.<br><sub>Also: <a href="https://sarvam-jev.feynmanpi.com/">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://www.reddit.com/r/LocalLLaMA/comments/1wle746/a_local_jevstyle_decision_head_onto_qwen_25_15b/"><img src="https://external-preview.redd.it/Wnrv8UVeht99poU3UQZOPTnOFzLoeyTHKvwoGiakktY.png?auto=webp&amp;s=8ff20f37c26e39ed193b6ae02021c976d1429eda" alt="AES" width="240"></a></td>
<td valign="top"><b><a href="https://www.reddit.com/r/LocalLLaMA/comments/1wle746/a_local_jevstyle_decision_head_onto_qwen_25_15b/">AES</a></b><br><sub>CryOrganic8886 · Reddit · ▲ 15 · 2026-09-20</sub><br>Proof-of-concept decision head on Qwen2.5-1.5B-Instruct that runs one prefill pass and scores candidate answers via an FP32 SwiGLU probe and embedding similarity instead of generating tokens.<br><sub><b>How it uses Jev:</b> Reimplements Noul, Choice, and Score style outputs locally on open weights.</sub><br><sub>Also: <a href="https://huggingface.co/Brinij/aes">model</a> · <a href="https://huggingface.co/brinij/aes">project</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/r-ms/mini-jev"><img src="https://raw.githubusercontent.com/r-ms/mini-jev/main/docs/figures/accuracy_by_k.svg" alt="mini-Jev" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/r-ms/mini-jev">mini-Jev</a></b><br><sub>r-ms · GitHub · ⭐ 42 · 2026-09-17</sub><br>Pre-registered experiment showing a Jev-style typed-decision interface on frozen Qwen3-4B by turning schema fields into lettered questions and reading option-letter logits in one pass, compared with grammar-constrained JSON.<br><sub>Also: <a href="https://news.ycombinator.com/item?id=49748643">discussion</a> · <a href="https://huggingface.co/datasets/Mikhail/mini-jev-runs">model</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://huggingface.co/DoccyHealth/Solomon"><img src="https://cdn-thumbnails.huggingface.co/social-thumbnails/models/DoccyHealth/Solomon.png" alt="Solomon" width="240"></a></td>
<td valign="top"><b><a href="https://huggingface.co/DoccyHealth/Solomon">Solomon</a></b><br><sub>Doccy (Archer Hume) · Hugging Face · ♥ 42 · 2026-09-21</sub><br>LoRA adapter and trained answer heads for Qwen3.8-27B that turn a document plus structured questions into one probability per decision, with pointers to supporting sentences and no text generation.<br><sub>Also: <a href="https://archerhume.com/posts/jevs-architecture-unmasked">post</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/snellingio/system-one"><img src="https://raw.githubusercontent.com/snellingio/system-one/main/docs/assets/how-system-one-lite-works-v3.png" alt="System One Lite" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/snellingio/system-one">System One Lite</a></b><br><sub>snellingio · GitHub · ⭐ 41 · 2026-09-16</sub><br>Proof-of-concept HTTP service for constrained decisions with a local language model that answers declared Choice, Score, and Noul questions by reading scores at a fixed answer position, with no generation.<br><sub>Also: <a href="https://news.ycombinator.com/item?id=49727643">discussion</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/lkarlslund/laya.cpp"><img src="https://external-preview.redd.it/cuDWXinMwBubvEi2uiDGctxhmXkdqtLzEbHzFCRaYOE.png?auto=webp&amp;s=f6c0009f9fb9794743802edd125c55efc41d42f3" alt="laya.cpp" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/lkarlslund/laya.cpp">laya.cpp</a></b><br><sub>lkarlslund · GitHub · ⭐ 40 · 2026-09-20</sub><br>Standalone C++ inference for the Jev-style Laya typed-decision models using ggml, with optimized CUDA kernels for NVIDIA RTX GPUs and a Vulkan FP32 backend, covering the english, multilingual and typed-decisions checkpoints.<br><sub>Also: <a href="https://www.reddit.com/r/LocalLLaMA/comments/1wlmkm9/layacpp_optimized_laya_nearinstant_decision_making/">demo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/intikhab49/open-jev-typed-decision-engine"><img src="https://raw.githubusercontent.com/intikhab49/open-jev-typed-decision-engine/main/docs/header.svg" alt="Open Jev typed decision engine" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/intikhab49/open-jev-typed-decision-engine">Open Jev typed decision engine</a></b><br><sub>intikhab49 · GitHub · ⭐ 39 · 2026-09-19</sub><br>Open 150M-parameter encoder reproduction of Jev that answers noul, choice, and score questions in one non-autoregressive pass, scoring 0.697 against Jev's 0.727 and training on a Colab T4 in 30 minutes.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/iapp-technology/openthai-systemone"><img src="https://raw.githubusercontent.com/iapp-technology/openthai-systemone/main/docs/assets/fb_launch_v3_1x1.png" alt="OpenThai-SystemOne" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/iapp-technology/openthai-systemone">OpenThai-SystemOne</a></b><br><sub>iapp-technology · GitHub · ⭐ 38 · 2026-09-20</sub><br>Open Thai and English System One model built from a Qwen3.5-0.8B tower with a 256-way slot head, answering choice, score, and noul questions in one pass behind TypeSafe's /v1/systemone contract.<br><sub>Also: <a href="https://www.reddit.com/r/LocalLLM/comments/1wlkjk8/i_trained_an_open_08b_system_one_decision_model/">discussion</a> · <a href="https://huggingface.co/iapp/OpenThai-SystemOne">model</a> · <a href="https://huggingface.co/iapp/OpenThai-SystemOne">model 2</a> · <a href="https://huggingface.co/spaces/hugging-apps/openthai-systemone-demo">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/zhengxuyu/litjev"><img src="https://opengraph.githubassets.com/1/zhengxuyu/litjev" alt="LitJev" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/zhengxuyu/litjev">LitJev</a></b><br><sub>zhengxuyu · GitHub · ⭐ 37 · 2026-09-17</sub><br>Hypothesis-based reproduction of the Jev decision layer that turns off-the-shelf Qwen checkpoints into typed Choice, Score and Noul endpoints by reading option scores from the output head, with an API and browser front end.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/TypeLLM/TypeLLM"><img src="https://github.com/user-attachments/assets/b1f2dbc6-21b7-4222-a0fb-dacfe1650797" alt="TypeLLM" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/TypeLLM/TypeLLM">TypeLLM</a></b><br><sub>TypeLLM · GitHub · ⭐ 37 · 2026-09-17</sub><br>Jev-inspired SGLang extension that gives open autoregressive LLMs typed outputs (string, integer, number, boolean, enum) from a JSON Schema, with single-token choices, shared-prefix KV reuse and dependency graphs.<br><sub>Also: <a href="https://typellm.ai">homepage</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://huggingface.co/spaces/pngwn/open-jev"><img src="https://cdn-thumbnails.huggingface.co/social-thumbnails/spaces/pngwn/open-jev.png" alt="Open Jev" width="240"></a></td>
<td valign="top"><b><a href="https://huggingface.co/spaces/pngwn/open-jev">Open Jev</a></b><br><sub>pngwn · App · ♥ 35 · 2026-09-17</sub><br>Hugging Face Space for a Qwen3.5-4B LoRA scorer that answers typed questions with a temperature-scaled probability over the caller's options, encoding the state once and deciding in parallel.<br><sub>Also: <a href="https://huggingface.co/pngwn/system-one-qwen3.5-4b-scorer">model</a> · <a href="https://huggingface.co/pngwn/system-one-qwen3.5-4b-scorer-v2b">model_v2b</a> · <a href="https://huggingface.co/datasets/pngwn/open-jev-laya-bench">model 2</a> · <a href="https://huggingface.co/datasets/pngwn/typed-decisions-v2-system-one">model 3</a> · <a href="https://huggingface.co/pngwn/system-one-qwen3.5-4b-scorer-v2b">model 4</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/taeold/djev-run"><img src="https://github.com/user-attachments/assets/2e9a5321-f8a9-4734-b6f2-4d6f47193390" alt="djev-run" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/taeold/djev-run">djev-run</a></b><br><sub>taeold · GitHub · ⭐ 32 · 2026-09-20</sub><br>Deployment recipe that serves DiffusionGemma-Jev on Google Cloud Run with an RTX PRO 6000 Blackwell GPU behind a TypeSafe-compatible API, plus a zero-dependency Snake demo calling it from the browser.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://huggingface.co/spaces/drinkmoonshine/parallel-constrained-decoding"><img src="https://cdn-thumbnails.huggingface.co/social-thumbnails/spaces/drinkmoonshine/parallel-constrained-decoding.png" alt="Parallel Constrained Decision Engine" width="240"></a></td>
<td valign="top"><b><a href="https://huggingface.co/spaces/drinkmoonshine/parallel-constrained-decoding">Parallel Constrained Decision Engine</a></b><br><sub>drinkmoonshine · App · ♥ 31 · 2026-09-16</sub><br>Gradio demo of parallel constrained decoding that fills multi-field JSON decision schemas in one pass over Qwen2.5-1.5B on Apple Silicon, pitched as an open alternative to Jev.<br><sub>Also: <a href="https://news.ycombinator.com/item?id=49734345">discussion</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/zhihz/openjev"><img src="https://raw.githubusercontent.com/zhihz/openjev/main/docs/images/demo-en.png" alt="Open JEV" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/zhihz/openjev">Open JEV</a></b><br><sub>zhihz · GitHub · ⭐ 29 · 2026-09-16</sub><br>Research preview inspired by Jev that makes local bilingual English and Chinese probability decisions over context, questions and candidate answers, currently on a frozen Qwen3-4B-Instruct backend with a web UI.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/KaLM-Embedding/KaLM-Jev"><img src="https://opengraph.githubassets.com/1/KaLM-Embedding/KaLM-Jev" alt="KaLM-Jev" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/KaLM-Embedding/KaLM-Jev">KaLM-Jev</a></b><br><sub>KaLM-Embedding · GitHub · ⭐ 28 · 2026-09-21</sub><br>Local Choice, Score, and Noul judgment service built on KaLM-Reranker-V1-R2 checkpoints in Nano, Small, and Large sizes, returning structured judgments without generating answer text.<br><sub>Also: <a href="https://huggingface.co/spaces/Yuki131/KaLM-Jev">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/IamBusy/OpenJev-Vision"><img src="https://raw.githubusercontent.com/IamBusy/OpenJev-Vision/main/reports/vision-v01/demo.png" alt="OpenJev-Vision" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/IamBusy/OpenJev-Vision">OpenJev-Vision</a></b><br><sub>IamBusy · GitHub · ⭐ 28 · 2026-09-19</sub><br>Open research toolkit for visual probabilistic decisions that encodes an image once and answers several structured questions from shared probabilities, with synthetic, Oxford-IIIT Pet, and CLEVR data and trained weights.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/mithalouni/system-one-open"><img src="https://opengraph.githubassets.com/1/mithalouni/system-one-open" alt="system-one-open" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/mithalouni/system-one-open">system-one-open</a></b><br><sub>mithalouni · GitHub · ⭐ 28 · 2026-09-17</sub><br>Open Jev-style decision model built on Gemma 4 E2B (attention LoRA) and Gemma 3 270M, trained and served on Modal; reports 76.7% on TypeSafe's public eval strict subset versus 86.9% for Jev.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/leesk212/JEV-CPU"><img src="https://raw.githubusercontent.com/leesk212/JEV-CPU/main/assets/jev-cpu-demo.gif" alt="JEV-CPU" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/leesk212/JEV-CPU">JEV-CPU</a></b><br><sub>leesk212 · GitHub · ⭐ 12 · 2026-09-19</sub><br>CPU port of SemIf with a web UI that reads typed option probabilities from Qwen3-0.6B logits in about 1 s, covering eight domains such as moderation, incident severity and credit risk.<br><sub>Also: <a href="https://leesk212.github.io/JEV-CPU/">app</a> · <a href="https://huggingface.co/Meanblock/JEV-CPU">model</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/fidecastro/jevify"><img src="https://opengraph.githubassets.com/1/fidecastro/jevify" alt="jevify (fidecastro)" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/fidecastro/jevify">jevify (fidecastro)</a></b><br><sub>fidecastro · GitHub · ⭐ 25 · 2026-09-19</sub><br>Adapter that serves any model with logprobs behind an OpenAI-compatible endpoint, or a small in-process model, as a Jev-like endpoint by reading typed answers off the next-token distribution in Jev's API shape.<br><sub>Also: <a href="https://www.reddit.com/r/OpenSourceeAI/comments/1wl9m9n/jevify_super_simple_way_to_serve_llms_as_a/">discussion</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/zeredy879/minojev"><img src="https://raw.githubusercontent.com/zeredy879/minojev/main/assets/banner.svg" alt="minojev" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/zeredy879/minojev">minojev</a></b><br><sub>zeredy879 · GitHub · ⭐ 25 · 2026-09-18</sub><br>Library that freezes a language model and trains a small decision head to read typed, calibrated choice, boolean and score distributions from hidden states in one forward pass, reproducible on a laptop CPU.<br><sub>Also: <a href="https://zeredy879.github.io/minojev/">docs</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/sgoedecke/system-one"><img src="https://opengraph.githubassets.com/1/sgoedecke/system-one" alt="System One" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/sgoedecke/system-one">System One</a></b><br><sub>sgoedecke · GitHub · ⭐ 25 · 2026-09-17</sub><br>Minimal code that turns any open LLM into a Jev-style, typesafe-sdk-compatible classifier via batched single-token choice inference; with Qwen3-8B it plays Doom at 172 ms per action versus 600 ms with tool calls.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/AndrewPrifer/jimothy"><img src="https://github.com/user-attachments/assets/b0781bef-61ab-47e5-96c6-2c034ad5cae3" alt="Jimothy" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/AndrewPrifer/jimothy">Jimothy</a></b><br><sub>AndrewPrifer · GitHub · ⭐ 24 · 2026-09-20</sub><br>Distills Jev answers into small, fast local classifiers that run in the browser or Node.js, with calibrated probabilities and a recommended cutoff.<br><sub><b>How it uses Jev:</b> Jev via AI Gateway acts as the teacher: its cached answers on unlabeled rows become training data for MiniLM or TF-IDF student classifiers.</sub><br><sub>Also: <a href="https://x.com/AndrewPrifer/status/2102162296739099126">demo</a> · <a href="https://jimothy-r63s.vercel.app">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/rorshopping/jev-on-a-laptop"><img src="https://opengraph.githubassets.com/1/rorshopping/jev-on-a-laptop" alt="jev-on-a-laptop" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/rorshopping/jev-on-a-laptop">jev-on-a-laptop</a></b><br><sub>rorshopping · GitHub · ⭐ 23 · 2026-09-16</sub><br>Unofficial study reproducing Jev-style parallel constrained decoding on stock Qwen 1.5B-8B models on an Apple Silicon laptop, where 7B reached 73.8% agreement against Jev's 86.6% at 0.4-2 s per decision.<br><sub><b>How it uses Jev:</b> Prefills once and evaluates all typed fields in one forward pass; finds confidence does not reliably flag errors.</sub><br><sub>Also: <a href="https://huggingface.co/spaces/rorshopping/parallel-constrained-decisions">demo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/karminski/Jev-Quantum"><img src="https://raw.githubusercontent.com/karminski/Jev-Quantum/main/assets/images/cover.png" alt="Jev Quantum" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/karminski/Jev-Quantum">Jev Quantum</a></b><br><sub>karminski · GitHub · ⭐ 22 · 2026-09-21</sub><br>Jev-protocol-compatible random baseline in Rust that speaks noul, choice and score but ignores the prompt and answers from a fast pseudo-random generator, for use as a mock or a lower bound in agent-routing evals.<br><sub>Also: <a href="https://x.com/karminski3/status/2101941770003361893">demo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://huggingface.co/notnotsamuel/LFM2.5-350M-RLCD"><img src="https://cdn-thumbnails.huggingface.co/social-thumbnails/models/notnotsamuel/LFM2.5-350M-RLCD.png" alt="LFM2.5-350M-RLCD" width="240"></a></td>
<td valign="top"><b><a href="https://huggingface.co/notnotsamuel/LFM2.5-350M-RLCD">LFM2.5-350M-RLCD</a></b><br><sub>notnotsamuel · Hugging Face · ♥ 22 · 2026-09-16</sub><br>Inference-only parallel structured decoding on unchanged Liquid LFM2.5-350M weights, branching attention and convolution state to score allowed values in a batch, 8-63x faster with field accuracy around 60%.<br><sub>Also: <a href="https://huggingface.co/monotykamary/LFM2.5-2.6B-RLCD">related</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/r33drichards/laya-vision"><img src="https://opengraph.githubassets.com/1/r33drichards/laya-vision" alt="Laya Vision" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/r33drichards/laya-vision">Laya Vision</a></b><br><sub>r33drichards · GitHub · ⭐ 21 · 2026-09-19</sub><br>Research fork of the open Laya model that swaps its text encoder for SmolVLM-256M, so typed choice, score, and noul decisions can be read from an image plus optional text in one forward pass.<br><sub>Also: <a href="https://news.ycombinator.com/item?id=49767430">discussion</a> · <a href="https://huggingface.co/thaitea/laya-vision-smolvlm-256m">model</a> · <a href="https://huggingface.co/spaces/thaitea/laya-vision-demo">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/JoshuaSP/open-jev"><img src="https://raw.githubusercontent.com/JoshuaSP/open-jev/main/assets/json-canvas.png" alt="open-jev (DiffusionGemma)" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/JoshuaSP/open-jev">open-jev (DiffusionGemma)</a></b><br><sub>JoshuaSP · GitHub · ⭐ 21 · 2026-09-16</sub><br>Experimental harness for typed JSON decisions with the DiffusionGemma 26B-A4B diffusion model that denoises freely and then picks the most likely allowed tokens, benchmarked on Every's TypeSafe lab tasks.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/OmniJev/PlayJev"><img src="https://raw.githubusercontent.com/OmniJev/PlayJev/main/docs/assets/board.webp" alt="PlayJev" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/OmniJev/PlayJev">PlayJev</a></b><br><sub>OmniJev · GitHub · ⭐ 21 · 2026-09-17</sub><br>Qwen3.5-0.8B fine-tuned as a Jev-like multimodal model that plays ten browser games from raw pixels, one frame in and one move out with a probability per option, in 43 ms on an H200.<br><sub>Also: <a href="https://omnijev.github.io/PlayJev/">app</a> · <a href="https://huggingface.co/omnijev/playjev-0.8b">model</a> · <a href="https://omnijev.github.io/PlayJev">app 2</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/mmastrac/djev"><img src="https://opengraph.githubassets.com/1/mmastrac/djev" alt="djev" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/mmastrac/djev">djev</a></b><br><sub>mmastrac · GitHub · ⭐ 20 · 2026-09-21</sub><br>Example server from a vLLM pull request that gets Jev-style structured decisions from DiffusionGemma by seeding the diffusion canvas with the answer template and reading slot distributions after one denoise step.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Argos1111/jev_local"><img src="https://cdn-thumbnails.huggingface.co/social-thumbnails/models/argos1111/modernbert-ja-310m-jev.png" alt="Jev Local" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Argos1111/jev_local">Jev Local</a></b><br><sub>Argos1111 · GitHub · ⭐ 20 · 2026-09-18</sub><br>Unofficial local /v1/systemone server for text, JSON and images that answers Choice, Score and Noul via first-token logprobs of LFM2.5 or Sarashina models, or a fine-tuned Japanese ModernBERT cross-encoder.<br><sub>Also: <a href="https://huggingface.co/argos1111/modernbert-ja-310m-jev">model</a> · <a href="https://huggingface.co/argos1111/sarashina2.2-vision-3b-mmproj-jev-f16">model 2</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/hawkymisc/typed-decision-bert"><img src="https://opengraph.githubassets.com/1/hawkymisc/typed-decision-bert" alt="JevBERT (typed-decision-bert)" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/hawkymisc/typed-decision-bert">JevBERT (typed-decision-bert)</a></b><br><sub>hawkymisc · GitHub · ⭐ 20 · 2026-09-21</sub><br>Unofficial proof of concept of a BERT-style encoder decision engine behind a Jev-shaped /v1/systemone API for noul, choice, and score questions, with published results and a benchmark against real Jev.<br><sub>Also: <a href="https://x.com/hawkymisc/status/2102062149841588395">demo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/0xBakeer/arbiter"><img src="https://raw.githubusercontent.com/0xBakeer/arbiter/main/docs/media/how-it-works.gif" alt="arbiter" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/0xBakeer/arbiter">arbiter</a></b><br><sub>0xBakeer · GitHub · ⭐ 19 · 2026-09-20</sub><br>Serving layer for typed-decision models such as Laya or your own on NVIDIA GPUs or Apple Silicon behind a Jev-compatible API, with coding-agent integrations and examples like a PR risk gate.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/mpnikhil/dev-0.4b"><img src="https://opengraph.githubassets.com/1/mpnikhil/dev-0.4b" alt="dev-0.4b" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/mpnikhil/dev-0.4b">dev-0.4b</a></b><br><sub>mpnikhil · GitHub · ⭐ 19 · 2026-09-21</sub><br>Open 399M-parameter decision model on ModernBERT-large for developer tools and coding agents, answering routing, yes/no and 1-5 rating questions in one forward pass (~28 ms on Apple Silicon).<br><sub><b>How it uses Jev:</b> Follows Jev and Kev with a single universal choice head over pooled candidate spans; reports 91.33% on Banking77 and 85.20% on BoolQ.</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/PsiACE/dohnuts"><img src="https://raw.githubusercontent.com/PsiACE/dohnuts/main/assets/dohnuts-logo.png" alt="Dohnuts" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/PsiACE/dohnuts">Dohnuts</a></b><br><sub>PsiACE · GitHub · ⭐ 18 · 2026-09-21</sub><br>Small multimodal System One style models, with a 0.8B checkpoint that runs on a consumer GPU, answering choice, noul and score questions about text or images in one forward pass, plus training and eval toolkit.<br><sub>Also: <a href="https://dohnuts.ai/">site</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/arinltte/kevMac"><img src="https://external-preview.redd.it/ejRpYTBkYXN5cnFoMf6puSmljth1cgrGzuZwp2ZyyReZNPXgGD-ASmeljkJx.png?format=pjpg&amp;auto=webp&amp;s=6f4c1b33aa72bf2c5f1b0325b7e2e577be7bf2d8" alt="kevMac" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/arinltte/kevMac">kevMac</a></b><br><sub>arinltte · GitHub · ⭐ 18 · 2026-09-20</sub><br>Mac app that runs the open Kev decision models locally on Apple Silicon: paste a document, build yes/no, choice or score questions as forms and see calibrated probability bars; kev-0.6b answers in ~0.2 s on an M4.<br><sub><b>How it uses Jev:</b> Converts forms into the /v1/systemone contract of a local Kev server (kev-0.6b to kev-9b checkpoints).</sub><br><sub>Also: <a href="https://www.reddit.com/r/vibecoding/comments/1wlyw27/experience_jev_locally_with_mac/">demo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/zhangcy122/OpenJev"><img src="https://opengraph.githubassets.com/1/zhangcy122/OpenJev" alt="OpenJevPro" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/zhangcy122/OpenJev">OpenJevPro</a></b><br><sub>zhangcy122 · GitHub · ⭐ 18 · 2026-09-20</sub><br>Framework that turns open-weight LLMs such as Qwen3, DeepSeek, Gemma and gpt-oss into typed Choice, Noul and Score decision services using constrained logprob calibration.<br><sub>Also: <a href="https://openjev.pro">site</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/hunkim/solar-mini4-jev"><img src="https://raw.githubusercontent.com/hunkim/solar-mini4-jev/main/bench/infographic_grok46_judge.png" alt="solar-mini4-jev" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/hunkim/solar-mini4-jev">solar-mini4-jev</a></b><br><sub>hunkim · GitHub · ⭐ 16 · 2026-09-21</sub><br>Drop-in wrapper that serves Upstage Solar Mini4 through the Jev System One API shape, with a hosted bring-your-own-key endpoint and a head-to-head benchmark.<br><sub><b>How it uses Jev:</b> Under a Grok 4.6 judge, Solar Mini4 missed 7 of 447 answer fields and Jev missed 26, while Jev was about 3.2x faster.</sub><br><sub>Also: <a href="https://solar-mini4-jev.vercel.app">app</a> · <a href="https://hunkim.github.io/solar-mini4-jev/">docs</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://www.reddit.com/r/LocalLLM/comments/1wlf4sv/opensource_jevstyle_typed_decision_model_that/"><img src="https://external-preview.redd.it/xjC6fykTq043HwezoQzDqEkNKkN-0dxncWqXwHYZK6s.png?auto=webp&amp;s=3f997e52f1b20af5ea33ad2aaea3df6fbd79202d" alt="VEJI-V2" width="240"></a></td>
<td valign="top"><b><a href="https://www.reddit.com/r/LocalLLM/comments/1wlf4sv/opensource_jevstyle_typed_decision_model_that/">VEJI-V2</a></b><br><sub>stopwwIII · Reddit · ▲ 5 · 2026-09-20</sub><br>MIT-licensed non-autoregressive typed decision model: a 3.3M-parameter head on a frozen multilingual MiniLM that scores options jointly, cites evidence spans, and can abstain.<br><sub><b>How it uses Jev:</b> Compiles long state once, then answers many typed questions against it; reports 82.95% test accuracy on 522 questions.</sub><br><sub>Also: <a href="https://huggingface.co/loaiabdalslam/VEJI-V2">model</a> · <a href="https://huggingface.co/loaiabdalslam/veji-v2">project</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/olanotolu/jevbetter"><img src="https://raw.githubusercontent.com/olanotolu/jevbetter/main/docs/architecture.png" alt="jevbetter" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/olanotolu/jevbetter">jevbetter</a></b><br><sub>olanotolu · GitHub · ⭐ 14 · 2026-09-16</sub><br>One-pass option scorer built from scratch with a hashed n-gram encoder, rival-aware attention, a gated head and temperature scaling, trained on the jevlike data format and benchmarked head-to-head against it.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/abhishek085/open-spark-jev"><img src="https://raw.githubusercontent.com/abhishek085/open-spark-jev/main/docs/assets/nokast-logo.png" alt="Open Spark Jev" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/abhishek085/open-spark-jev">Open Spark Jev</a></b><br><sub>abhishek085 · GitHub · ⭐ 14 · 2026-09-20</sub><br>Open local decision model, spark-s1, inspired by Jev and built on Qwen3 for NVIDIA DGX Spark, with a Jev-compatible API, architecture notes, data generation and evaluation tooling.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/mohitsoni48/TurboLLM/tree/main/turbollm/web/src/screens/jev"><img src="https://opengraph.githubassets.com/1/mohitsoni48/TurboLLM" alt="TurboLLM Jev mode" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/mohitsoni48/TurboLLM/tree/main/turbollm/web/src/screens/jev">TurboLLM Jev mode</a></b><br><sub>mohitsoni48 · GitHub · ⭐ 275 repo · 2026-06-12</sub><br>Local LLM runner that detects NLI cross-encoder models as local Jev models and serves them through /v1/systemone, /v1/classify and /v1/rerank, with a JSON-first playground.<br><sub>Also: <a href="https://turbollm.dev">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/kikoncuo/jevfire"><img src="https://raw.githubusercontent.com/kikoncuo/jevfire/main/assets/hero.png" alt="JEVfire" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/kikoncuo/jevfire">JEVfire</a></b><br><sub>kikoncuo · GitHub · ⭐ 13 · 2026-09-16</sub><br>Jev-inspired parallel decisions for CUDA LLMs on vLLM that score single-token labels with the model's own head and assemble JSON in code, with game demos including in-browser Mario at 71 ms per action.<br><sub><b>How it uses Jev:</b> No retraining or second model; the schema fixes keys and allowed values.</sub><br><sub>Also: <a href="https://kikoncuo.github.io/jevfire/learn.html">site</a> · <a href="https://kikoncuo.github.io/jevfire">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/ChristianAlexander/laya_ex"><img src="https://opengraph.githubassets.com/1/ChristianAlexander/laya_ex" alt="laya_ex" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/ChristianAlexander/laya_ex">laya_ex</a></b><br><sub>ChristianAlexander · GitHub · ⭐ 13 · 2026-09-20</sub><br>Elixir library that provides a native Nx and Bumblebee runtime for the open Laya decision model by Convai Innovations, downloading the official checkpoint on first load.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://huggingface.co/datasets/ZefanCai/Open-Jev"><img src="https://cdn-thumbnails.huggingface.co/social-thumbnails/datasets/ZefanCai/Open-Jev.png" alt="Open-Jev datasets" width="240"></a></td>
<td valign="top"><b><a href="https://huggingface.co/datasets/ZefanCai/Open-Jev">Open-Jev datasets</a></b><br><sub>ZefanCai · Hugging Face · ♥ 13 · 2026-09-20</sub><br>Twelve frozen, mostly synthetic typed-decision data configs (yes/no, choice, multi-label, numeric and ordinal) with manifests, raw records and reconstruction code from the independent Open-Jev project.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/genai-craft/openvons"><img src="https://opengraph.githubassets.com/1/genai-craft/openvons" alt="openvons" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/genai-craft/openvons">openvons</a></b><br><sub>genai-craft · GitHub · ⭐ 13 · 2026-09-17</sub><br>Open decision layer that makes LLMs, VLMs, and ASR models pick from a finite option set with none-of-the-above, splitting calibrated probabilities into execute, confirm, and reject; includes Japanese voice commands.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/stephanj/parallelConstraintDecoding"><img src="https://external-preview.redd.it/IXd1hZpg6SpsXqnxAePniddWNOv3rlbrwQhwMZZfaig.png?auto=webp&amp;s=3ce2634792342b174000165911a5fe4b774d8df9" alt="parallelConstraintDecoding" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/stephanj/parallelConstraintDecoding">parallelConstraintDecoding</a></b><br><sub>stephanj · GitHub · ⭐ 13 · 2026-09-17</sub><br>Java and Python implementations of parallel constrained decoding that fill a JSON schema of booleans and enums in two forward passes on llama.cpp models, with per-field confidence and a benchmark web app.<br><sub>Also: <a href="https://www.reddit.com/r/java/comments/1wjhn9h/parallel_constraint_decoding_using_java_and/">discussion</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://huggingface.co/pngwn/system-one-qwen3.5-4b-scorer"><img src="https://cdn-thumbnails.huggingface.co/social-thumbnails/models/pngwn/system-one-qwen3.5-4b-scorer.png" alt="system-one-qwen3.5-4b-scorer" width="240"></a></td>
<td valign="top"><b><a href="https://huggingface.co/pngwn/system-one-qwen3.5-4b-scorer">system-one-qwen3.5-4b-scorer</a></b><br><sub>pngwn · Hugging Face · ♥ 13 · 2026-09-16</sub><br>Open Jev-shaped decision model on Qwen3.5-4B-Base with a scoring head that returns a distribution over exactly the caller's options for yes/no, Choice and Score questions in one pass.<br><sub><b>How it uses Jev:</b> Scores each (state, question, option) triple and softmaxes per question; training code included.</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/nokia-applied-research/AnyJev"><img src="https://raw.githubusercontent.com/nokia-applied-research/AnyJev/main/assets/banner.png" alt="AnyJev" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/nokia-applied-research/AnyJev">AnyJev</a></b><br><sub>nokia-applied-research · GitHub · ⭐ 12 · 2026-09-21</sub><br>Library that turns any transformers or vLLM model into a Jev-style Choice, Score, and Noul decision model from one prefill with no training, fixing option-order flips via cyclic-shift marginalization.<br><sub>Also: <a href="https://pypi.org/project/anyjev/">pypi</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Yeachan-Heo/ifllm-learn"><img src="https://raw.githubusercontent.com/Yeachan-Heo/ifllm-learn/main/docs/demo-overview.svg" alt="ifllm-learn" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Yeachan-Heo/ifllm-learn">ifllm-learn</a></b><br><sub>Yeachan-Heo · GitHub · ⭐ 12 · 2026-09-20</sub><br>Research toolkit built on SemIf and MLX-LM that fine-tunes local LoRA adapters into typed decision models from labeled examples, with measured demos on support routing, out-of-scope detection and contract checklists.<br><sub><b>How it uses Jev:</b> Jev-style typed decisions trained locally on Apple Silicon; independent of TypeSafe and not a reimplementation of Jev training.</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/pst2154/Nemotron_Jev"><img src="https://opengraph.githubassets.com/1/pst2154/Nemotron_Jev" alt="Nemotron Diffusion Decision Lab" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/pst2154/Nemotron_Jev">Nemotron Diffusion Decision Lab</a></b><br><sub>pst2154 · GitHub · ⭐ 12 · 2026-09-18</sub><br>Experimental container that serves the dense Nemotron-Labs-Diffusion-14B model behind a TypeSafe-shaped API, with a browser explorer for Choice, Noul and Score distributions.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/zwliJay/jev-forge"><img src="https://raw.githubusercontent.com/zwliJay/jev-forge/main/docs/assets/jevforge-demo.gif" alt="JevForge" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/zwliJay/jev-forge">JevForge</a></b><br><sub>zwliJay · GitHub · ⭐ 11 · 2026-09-19</sub><br>End-to-end stack for Jev-style decision models: synthesizing decision data, training a calibrated Qwen3.5-0.8B candidate scorer, fixed Mind2Web and out-of-distribution evals, preliminary RLCD, and Jev-compatible serving.<br><sub>Also: <a href="https://jay-forge-web.vercel.app/">app</a> · <a href="https://jev-forge.vercel.app">app 2</a> · <a href="https://huggingface.co/datasets/AndeyTait/JevForge-Mind2Web">model</a> · <a href="https://huggingface.co/AndeyTait/JevForge-0.8B">model 2</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Micha0827/snapjudge"><img src="https://raw.githubusercontent.com/Micha0827/snapjudge/main/assets/snaprun.gif" alt="snapjudge" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Micha0827/snapjudge">snapjudge</a></b><br><sub>Micha0827 · GitHub · ⭐ 10 · 2026-09-18</sub><br>TypeSafe-compatible server that reads Choice, Score, and Noul probabilities from the logits of local Qwen models on Apple Silicon via MLX; Qwen3.8-27B reaches 81.2% agreement with Jev on 20 public cases.<br><sub>Also: <a href="https://www.reddit.com/r/LocalLLM/comments/1wlr8sp/i_rebuilt_the_jev_interface_with_local_qwen/">discussion</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/komorra/Eugeniusz"><img src="https://raw.githubusercontent.com/komorra/Eugeniusz/main/docs/assets/eugeniusz-banner.png" alt="Eugeniusz" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/komorra/Eugeniusz">Eugeniusz</a></b><br><sub>komorra · GitHub · ⭐ 9 · 2026-09-17</sub><br>MIT-licensed C++17 library with a C ABI that evaluates text locally and returns a choice, rubric score or truth probability, as an independent alternative to the Jev decision interface for C, C#, Python, Unity and Unreal.<br><sub><b>How it uses Jev:</b> Mirrors the Choice/Score/Noul interface on local Qwen models; it does not reproduce Jev's training, latency or accuracy.</sub><br><sub>Also: <a href="https://www.reddit.com/r/aigamedev/comments/1wjihg8/i_let_a_local_ai_play_hexen_eugeniusz_yolo/">demo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/liushiliushi/JevTuner"><img src="https://raw.githubusercontent.com/liushiliushi/JevTuner/main/images/jevtuner_method_drawio.png" alt="JevTuner" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/liushiliushi/JevTuner">JevTuner</a></b><br><sub>liushiliushi · GitHub · ⭐ 9 · 2026-09-21</sub><br>Training method for language models to make Jev-style closed-set decisions, scoring every candidate in one forward pass and tuning the full distribution with a tokenized Brier loss.<br><sub><b>How it uses Jev:</b> Applies the ConfTuner idea of training token-logit probabilities to state-plus-question decision tasks.</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://huggingface.co/mradermacher/jevify-gemma4-26b-a4b-GGUF"><img src="https://cdn-thumbnails.huggingface.co/social-thumbnails/models/mradermacher/jevify-gemma4-26b-a4b-GGUF.png" alt="jevify-gemma4-26b-a4b GGUF" width="240"></a></td>
<td valign="top"><b><a href="https://huggingface.co/mradermacher/jevify-gemma4-26b-a4b-GGUF">jevify-gemma4-26b-a4b GGUF</a></b><br><sub>mradermacher · Hugging Face · ⬇ 803 · 2026-09-20</sub><br>Static GGUF quantizations (Q2_K to Q8_0) of jevify-gemma4-26b-a4b, the Gemma 4 model behind the local Jev-compatible jevify decision API.<br><sub>Also: <a href="https://github.com/kushalpatil07/jevify">project</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/chengyongru/fastjev"><img src="https://raw.githubusercontent.com/chengyongru/fastjev/main/assets/fastjev-logo.svg" alt="FastJev" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/chengyongru/fastjev">FastJev</a></b><br><sub>chengyongru · GitHub · ⭐ 8 · 2026-09-20</sub><br>SDK-first, independently maintained fork of SemIf for self-hosting an open Jev implementation, running pinned open models for Choice, Boolean, and Score via Torch, vLLM, MLX, or llama.cpp.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/kerryrm/systemANE"><img src="https://opengraph.githubassets.com/1/kerryrm/systemANE" alt="systemANE" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/kerryrm/systemANE">systemANE</a></b><br><sub>kerryrm · GitHub · ⭐ 8 · 2026-09-20</sub><br>Proof of concept of a System One-style engine on Apple's Neural Engine with Choice, Boolean, and Score primitives over a 22.6M-parameter encoder, escalating unsure cases to Apple's Foundation Models.<br><sub><b>How it uses Jev:</b> Reports 93.3% accuracy and ECE 0.041 on CLINC150 at 1.4 ms per decision.</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/aabolfazl/typesafe-local"><img src="https://raw.githubusercontent.com/aabolfazl/typesafe-local/main/docs/diagrams/03-encode-once-ask-many.png" alt="typesafe-local" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/aabolfazl/typesafe-local">typesafe-local</a></b><br><sub>aabolfazl · GitHub · ⭐ 8 · 2026-09-18</sub><br>Local MLX server with TypeSafe's API shape that encodes a document once, appends each question as a short suffix and reads logits instead of generating; four questions take ~200 ms on an M4 Pro.<br><sub><b>How it uses Jev:</b> Measures how calibration and option order affect the answers; the API shape matches TypeSafe so the same client works against either.</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/siliconkernel/vllm-jev-decison"><img src="https://raw.githubusercontent.com/siliconkernel/vllm-jev-decison/main/assets/en/architecture.svg" alt="vllm-jev-decison" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/siliconkernel/vllm-jev-decison">vllm-jev-decison</a></b><br><sub>siliconkernel · GitHub · ⭐ 8 · 2026-09-18</sub><br>Plugin for vLLM that adds a classification-only mode for Jev-like typed decisions, scoring candidate labels from a finite JSON Schema to return typed values, probabilities, and abstention with no generation.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/thecodacus/decision-playground"><img src="https://opengraph.githubassets.com/1/thecodacus/decision-playground" alt="Decision Playground" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/thecodacus/decision-playground">Decision Playground</a></b><br><sub>thecodacus · GitHub · ⭐ 7 · 2026-09-19</sub><br>Browser-only playground and arena game for llama-server's Jev-style /v1/decision endpoint, comparing one parallel decision pass with grammar-constrained chat on the same model and letting agents pick controls several times a second.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/jlt-commons/lev"><img src="https://opengraph.githubassets.com/1/jlt-commons/lev" alt="Lev" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/jlt-commons/lev">Lev</a></b><br><sub>jlt-commons · GitHub · ⭐ 7 · 2026-09-19</sub><br>System One decision engine in Clojure on Chez Scheme that serves Laya ModernBERT/mmBERT encoders at about 100 ms on a laptop CPU, plus a llama.cpp thinker whose answers are scored by token log probabilities.<br><sub><b>How it uses Jev:</b> Serves typed questions over a state with calibrated probabilities; MiniCPM5-2B with thinking scored 95% on the adversarial authored144 set versus 61-67% for the encoders.</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/scienthoon/luce"><img src="https://raw.githubusercontent.com/scienthoon/luce/main/media/live_triage.gif" alt="Luce" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/scienthoon/luce">Luce</a></b><br><sub>scienthoon · GitHub · ⭐ 7 · 2026-09-20</sub><br>Recipe for task-specific calibrated decision models: describe the task, have an LLM teacher synthesize or annotate data, train a LoRA plus decision head on Qwen, evaluate calibration and serve typed probabilities.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/kyegomez/open-jev"><img src="https://opengraph.githubassets.com/1/kyegomez/open-jev" alt="Open Jev" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/kyegomez/open-jev">Open Jev</a></b><br><sub>kyegomez · GitHub · ⭐ 7 · 2026-09-21</sub><br>Unofficial PyTorch reconstruction of the ideas behind Jev with random weights: the state is encoded once and every question is answered through small typed readout heads in one parallel forward pass.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/RJMSWD/QwenJev"><img src="https://raw.githubusercontent.com/RJMSWD/QwenJev/main/examples/support_ticket.png" alt="Qwen Choice" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/RJMSWD/QwenJev">Qwen Choice</a></b><br><sub>RJMSWD · GitHub · ⭐ 7 · 2026-09-21</sub><br>Local Jev-style visual judgment on Qwen3.5-4B: an image, a question and options go in, and one forward pass returns the choice with probabilities in about 169 ms on an RTX A6000.<br><sub><b>How it uses Jev:</b> Uses the original BF16 weights with thinking off and no training or quantization.</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://huggingface.co/spaces/mobarmg/jev-schema-scorer"><img src="https://cdn-thumbnails.huggingface.co/social-thumbnails/spaces/mobarmg/jev-schema-scorer.png" alt="Schema-conditioned candidate scorer demo" width="240"></a></td>
<td valign="top"><b><a href="https://huggingface.co/spaces/mobarmg/jev-schema-scorer">Schema-conditioned candidate scorer demo</a></b><br><sub>mobarmg · App · ♥ 7 · 2026-09-17</sub><br>Interactive demo of a DeBERTa-v3-large scalar-head scorer that reads your own choice, noul and score schema at inference time and decodes grouped logits into typed answers.<br><sub>Also: <a href="https://huggingface.co/mobarmg/jev-schema-scorer-deberta-v3-large">model</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/jiangxiluning/Visual-Jev"><img src="https://raw.githubusercontent.com/jiangxiluning/Visual-Jev/master/demo/assets/semif-phase1-replay.gif" alt="Visual-Jev" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/jiangxiluning/Visual-Jev">Visual-Jev</a></b><br><sub>jiangxiluning · GitHub · ⭐ 7 · 2026-09-22</sub><br>Copy of the SemIf (formerly OpenJev) open reimplementation of Jev's typed-decision interface that adds an optional image input, running Qwen3.5-4B as a vision-language model for direct, serial and shared scoring.<br><sub>Also: <a href="https://github.com/TheoLeeCJ/SemIf">upstream</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/hyprstream/hyprstream/tree/main/crates/hyprstream-decision-stub"><img src="https://raw.githubusercontent.com/hyprstream/hyprstream/main/architecture.png" alt="HyprStream decision service" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/hyprstream/hyprstream/tree/main/crates/hyprstream-decision-stub">HyprStream decision service</a></b><br><sub>hyprstream · GitHub · ⭐ 127 repo · 2025-01-06</sub><br>Self-improving AI runtime building its own System One decision service, with a decision head and a /v1/systemone facade that the stock TypeSafe Python and JS SDKs run against.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://huggingface.co/collections/llm-semantic-router/decision-10-6ab12177bd0002394d8409f9"><img src="https://cdn-thumbnails.huggingface.co/social-thumbnails/collections/llm-semantic-router/decision-10-6ab12177bd0002394d8409f9.png" alt="Decision 1.0" width="240"></a></td>
<td valign="top"><b><a href="https://huggingface.co/collections/llm-semantic-router/decision-10-6ab12177bd0002394d8409f9">Decision 1.0</a></b><br><sub>vLLM Semantic Router · Hugging Face · ♥ 6 · 2026-09-22</sub><br>Apache-2.0 collection of open decision models from the vLLM Semantic Router team, 572M encoders and 1.88B to 4.21B decoders that answer Choice, Noul, and Score in one pass across 50 languages, plus a Studio Space.<br><sub>Also: <a href="https://huggingface.co/llm-semantic-router/Decision-1.0-Kai">model</a> · <a href="https://huggingface.co/spaces/llm-semantic-router/decision-studio">space</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Astro-Han/decision-head-rlcd"><img src="https://opengraph.githubassets.com/1/Astro-Han/decision-head-rlcd" alt="decision-head-rlcd" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Astro-Han/decision-head-rlcd">decision-head-rlcd</a></b><br><sub>Astro-Han · GitHub · ⭐ 6 · 2026-09-20</sub><br>Experiment training Qwen3.5-4B with a rank-8 LoRA and RLCD on 32,000 typed decisions to test where a Jev-like model's generalisation comes from; it finds generalisation tracks training-data coverage.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://huggingface.co/lewislululu/jevon"><img src="https://cdn-thumbnails.huggingface.co/social-thumbnails/models/lewislululu/jevon.png" alt="Jevon" width="240"></a></td>
<td valign="top"><b><a href="https://huggingface.co/lewislululu/jevon">Jevon</a></b><br><sub>lewislululu · Hugging Face · ♥ 6 · 2026-09-19</sub><br>Tiny 20M-parameter decision model that answers typed questions about a grid (which way to move, is north clear, how far is the goal) for maze and snake, rebuilt from NanoJev around planning depth.<br><sub>Also: <a href="https://github.com/lewislulu/jevon-arcade">project</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://huggingface.co/monotykamary/LFM2.5-2.6B-RLCD"><img src="https://cdn-thumbnails.huggingface.co/social-thumbnails/models/monotykamary/LFM2.5-2.6B-RLCD.png" alt="LFM2.5-2.6B-RLCD" width="240"></a></td>
<td valign="top"><b><a href="https://huggingface.co/monotykamary/LFM2.5-2.6B-RLCD">LFM2.5-2.6B-RLCD</a></b><br><sub>monotykamary · Hugging Face · ♥ 6 · 2026-09-16</sub><br>Experimental parallel constrained decoding package on unchanged LFM2.5-2.6B weights, about 9.9x faster than autoregressive JSON on 12 dev cases but only 72.2% field accuracy on fresh audit cases.<br><sub><b>How it uses Jev:</b> Targets Jev's fast finite-choice interaction pattern; explicitly uncalibrated and not a reproduction of RLCD training.</sub><br><sub>Also: <a href="https://huggingface.co/notnotsamuel/LFM2.5-350M-RLCD">related</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/jagsan-cyber/reflex-gate"><img src="https://opengraph.githubassets.com/1/jagsan-cyber/reflex-gate" alt="ReflexGate" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/jagsan-cyber/reflex-gate">ReflexGate</a></b><br><sub>jagsan-cyber · GitHub · ⭐ 6 · 2026-09-19</sub><br>Offline Go gateway for local agent loops with loop-exit, argument-extraction, and safety-scan endpoints plus a Jev-compatible /v1/systemone for typed noul and choice triage, with a Windows GUI.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/hemanth/webml-kit"><img src="https://opengraph.githubassets.com/1/hemanth/webml-kit" alt="webml-kit" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/hemanth/webml-kit">webml-kit</a></b><br><sub>hemanth · GitHub · ⭐ 6 · 2026-04-20</sub><br>Framework-agnostic toolkit for running ML models in the browser over WebGPU/WASM that adds a Jev-style decision task, reading typed Choice, Noul and Score answers from local models such as Qwen or OpenJev GGUFs.<br><sub>Also: <a href="https://hemanth.github.io/webml-kit/">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/leehanchung/SMILE-factory/tree/main/research/jev"><img src="https://opengraph.githubassets.com/1/leehanchung/SMILE-factory" alt="RE Jev research project" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/leehanchung/SMILE-factory/tree/main/research/jev">RE Jev research project</a></b><br><sub>leehanchung · GitHub · ⭐ 106 repo · 2023-05-07</sub><br>Research handoff for building a Jev-like decision model, covering design criteria, architecture, a training data plan, GLiNER2 benchmark and calibration protocols; no model has been trained yet.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/mattn/tensai/blob/main/internal/llm/systemone.go"><img src="https://opengraph.githubassets.com/1/mattn/tensai" alt="tensai System One endpoint" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/mattn/tensai/blob/main/internal/llm/systemone.go">tensai System One endpoint</a></b><br><sub>mattn · GitHub · ⭐ 106 repo · 2026-08-19</sub><br>Tiny pure-Go neural-network framework that serves Jev-shaped System One requests from any loaded model by reading labeled logits after each question, so Jev API clients can point at it.<br><sub>Also: <a href="https://mattn.github.io/tensai/">docs</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://huggingface.co/mradermacher/jevify-gemma4-e4b-GGUF"><img src="https://cdn-thumbnails.huggingface.co/social-thumbnails/models/mradermacher/jevify-gemma4-e4b-GGUF.png" alt="jevify-gemma4-e4b GGUF" width="240"></a></td>
<td valign="top"><b><a href="https://huggingface.co/mradermacher/jevify-gemma4-e4b-GGUF">jevify-gemma4-e4b GGUF</a></b><br><sub>mradermacher · Hugging Face · ⬇ 506 · 2026-09-20</sub><br>Static GGUF quantizations (Q2_K to Q8_0) of jevify-gemma4-e4b, the Gemma 4 E4B model behind the local Jev-compatible jevify decision API.<br><sub>Also: <a href="https://github.com/kushalpatil07/jevify">project</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/hwfengcs/any2jev"><img src="https://raw.githubusercontent.com/hwfengcs/any2jev/main/docs/vs.gif" alt="any2jev" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/hwfengcs/any2jev">any2jev</a></b><br><sub>hwfengcs · GitHub · ⭐ 5 · 2026-09-21</sub><br>Converter that trains any Hugging Face causal LM into a Jev-style decision model answering typed questions in one forward pass with calibrated probabilities and zero generated tokens, demoed on Qwen3-0.6B.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/yzfly/edgejev"><img src="https://opengraph.githubassets.com/1/yzfly/edgejev" alt="EdgeJev" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/yzfly/edgejev">EdgeJev</a></b><br><sub>yzfly · GitHub · ⭐ 5 · 2026-09-20</sub><br>Offline CPU runtime that converts open Jev reimplementations such as laya, kev, NanoJev and PlayJev to ONNX with INT8 quantization behind a protocol-compatible local server; 15.6 ms per question on 4 CPU cores.<br><sub>Also: <a href="https://pypi.org/project/edgejev/">pypi</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/yohanargentina-oss/Foq"><img src="https://raw.githubusercontent.com/yohanargentina-oss/Foq/main/assets/chart_memory_paradox.png" alt="Foq" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/yohanargentina-oss/Foq">Foq</a></b><br><sub>yohanargentina-oss · GitHub · ⭐ 5 · 2026-09-19</sub><br>Local, open-source Jev alternative that returns calibrated probabilities on typed boolean, choice, score and Pydantic questions in one feed-forward pass, reported at about 25 ms, with benchmarks against Laya.<br><sub>Also: <a href="https://foq.fr">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://huggingface.co/vagmi/jev-lite"><img src="https://cdn-thumbnails.huggingface.co/social-thumbnails/models/vagmi/jev-lite.png" alt="jev-lite" width="240"></a></td>
<td valign="top"><b><a href="https://huggingface.co/vagmi/jev-lite">jev-lite</a></b><br><sub>vagmi · Hugging Face · ♥ 5 · 2026-09-19</sub><br>QLoRA adapter that turns Gemma 4 E4B into a System One decision model, reading answers from the logits at the option letters so it cannot answer outside the given options.<br><sub>Also: <a href="https://github.com/vagmi/jevlite">project</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/NVentimiglia/laya-mcp"><img src="https://opengraph.githubassets.com/1/NVentimiglia/laya-mcp" alt="Laya MCP" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/NVentimiglia/laya-mcp">Laya MCP</a></b><br><sub>NVentimiglia · GitHub · ⭐ 5 · 2026-09-19</sub><br>MCP server and agent plugin for Claude Code, Copilot CLI and Cursor that runs the open Laya decision model locally and gives agents five tools returning a label, probability or score in one forward pass.<br><sub><b>How it uses Jev:</b> Jev-style typed decisions from the local convaiinnovations/laya checkpoint, with a 0.85 confidence threshold for automate versus escalate.</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/afshinm/laya-mps"><img src="https://opengraph.githubassets.com/1/afshinm/laya-mps" alt="Laya MPS" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/afshinm/laya-mps">Laya MPS</a></b><br><sub>afshinm · GitHub · ⭐ 5 · 2026-09-21</sub><br>Runs the open Laya model for Jev-style typed decisions on Apple Silicon via PyTorch MPS, at about 32 ms median latency and 2.1 GiB of RAM on an M5 Pro.<br><sub><b>How it uses Jev:</b> Choice, Score and truth-probability decisions from an ~843 MB model tuned for customer service, invoices, security incidents and agent traces.</sub><br><sub>Also: <a href="https://news.ycombinator.com/item?id=49787265">demo</a> · <a href="https://www.reddit.com/r/LocalLLM/comments/1wm64ih/run_jevstyle_typed_decisions_locally_on_apple/">discussion</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/wmoto-ai/local-decision-playground"><img src="https://opengraph.githubassets.com/1/wmoto-ai/local-decision-playground" alt="Local Decision Playground" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/wmoto-ai/local-decision-playground">Local Decision Playground</a></b><br><sub>wmoto-ai · GitHub · ⭐ 5 · 2026-09-17</sub><br>Dependency-free web app, in Japanese, for trying a local vLLM model as a Jev-inspired classifier: it restricts generation to the declared options and normalizes their logprobs into relative probabilities, including for images.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://huggingface.co/samatv256/mini-Jev"><img src="https://cdn-thumbnails.huggingface.co/social-thumbnails/models/samatv256/mini-Jev.png" alt="ODM Mini" width="240"></a></td>
<td valign="top"><b><a href="https://huggingface.co/samatv256/mini-Jev">ODM Mini</a></b><br><sub>samatv256 · Hugging Face · ♥ 5 · 2026-09-21</sub><br>Open-weight Choice decision head on frozen Qwen3-0.6B that ranks candidate agent actions and returns probabilities, confidence and margin for tool selection (72.97% semantic Choice accuracy).</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/xingwudao/OpenJev"><img src="https://opengraph.githubassets.com/1/xingwudao/OpenJev" alt="OpenJev" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/xingwudao/OpenJev">OpenJev</a></b><br><sub>xingwudao · GitHub · ⭐ 5 · 2026-09-18</sub><br>Independent Jev-inspired decision API with Choice, Score and Noul primitives, a local mock server and Python and TypeScript SDKs; mock probabilities are synthetic and real inference is planned.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/stephanj/pcdServer"><img src="https://raw.githubusercontent.com/stephanj/pcdServer/main/docs/images/pcd-playground.png" alt="PCD Server" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/stephanj/pcdServer">PCD Server</a></b><br><sub>stephanj · GitHub · ⭐ 5 · 2026-09-18</sub><br>Native C++ REST server for Parallel Constrained Decoding with local GGUF models: give it text and bounded fields and it picks one allowed value per field, returning JSON plus each decision's probabilities, Jev-style.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/rupeshpoojary9/poorjev"><img src="https://raw.githubusercontent.com/rupeshpoojary9/poorjev/main/docs/reliability_before_after.png" alt="poorjev" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/rupeshpoojary9/poorjev">poorjev</a></b><br><sub>rupeshpoojary9 · GitHub · ⭐ 5 · 2026-09-19</sub><br>Local System One-style decision layer that implements Jev's typed Choice, Score and Noul interface on zero-shot NLI models, with temperature scaling and conformal abstention cutting ECE from 0.170 to 0.071.<br><sub>Also: <a href="https://www.reddit.com/r/learnmachinelearning/comments/1wksf4i/poorjev_an_open_local_system_one_decision_layer/">discussion</a></sub></td>
</tr>
</table>

<details><summary>90 more</summary>

- **[ruling](https://github.com/bradAGI/ruling)** · <sub>bradAGI · GitHub · ⭐ 5 · 2026-09-18</sub><br>Open-weight recreation of Jev's typed-decision interface that runs on an Apple Silicon Mac with MLX and a 4-bit Qwen3.5 checkpoint, answering in about 119 ms; a 19 GB MoE model reaches Jev's accuracy on TypeSafe's evaluation rows.
- **[verdict](https://github.com/khimaros/verdict)** · <sub>khimaros · GitHub · ⭐ 5 · 2026-09-20</sub><br>Self-hosted server that turns any llama-server or llama-swap endpoint into a Jev-compatible System One API by reading the probability on each option label in one forward pass, so Jev clients only change the base URL.
- **[eve-rlcd](https://github.com/anthony-maio/eve-rlcd)** · <sub>anthony-maio · GitHub · ⭐ 4 · 2026-09-18</sub><br>Jev-inspired 0.6B decision model on Qwen3-0.6B-Base trained with RL from right/wrong feedback so its option probabilities match accuracy; includes training loop, ablation, eval and open weights.
- **[hearim](https://github.com/ziozzang/hearim)** · <sub>ziozzang · GitHub · ⭐ 4 · 2026-09-21</sub><br>Go gateway that serves the Jev /v1/systemone contract on ordinary LLM backends like Ollama, llama.cpp and vLLM by scoring each question as a single-token choice from logprobs.
- **[Jev-Compatible](https://github.com/David-Lolly/Jev-Compatible)** · <sub>David-Lolly · GitHub · ⭐ 4 · 2026-09-21</sub><br>HTTP gateway that turns an existing SGLang or vLLM deployment into a Jev-compatible decision service by scoring candidate tokens for noul, choice, and score questions, with no training or model changes.
- **[jev-rs](https://github.com/yijunyu/jev-rs)** · <sub>yijunyu · GitHub · ⭐ 4 · 2026-09-21</sub><br>Rust engine that answers Noul, Choice, and Score questions from any GGUF model behind llama-server in one prefill, wire-compatible with Jev's /v1/systemone and exposed as an MCP tool.
- **[Jev-Style-Qwen3.5-2B-Decision (GGUF)](https://huggingface.co/chaoliangUNSW/Jev-Style-Qwen3.5-2B-Decision-GGUF)** · <sub>chaoliangUNSW · Hugging Face · ♥ 4 · 2026-09-21</sub><br>GGUF builds of a Jev-style Qwen3.5-2B decision model for LM Studio and llama.cpp that reads calibrated option probabilities from one token position; Q4_K_M (1.3 GB) keeps 82.4% accuracy.
- **[qwen-rlcd](https://github.com/shamazharikh/qwen-rlcd)** · <sub>shamazharikh · GitHub · ⭐ 4 · 2026-09-16</sub><br>Prototype Jev-style decision model on Qwen3.5-0.8B-Base that prefills the state once, forks the cache per question-answer branch and reads calibrated distributions; inference works, training is on hold.
- **[System One Gemma](https://github.com/akash-kamat/system-one-gemma)** · <sub>akash-kamat · GitHub · ⭐ 4 · 2026-09-17</sub><br>Open Jev-style decision model that puts a linear scoring head on Gemma 3 270M, scoring every option's sequence in one batched forward pass and softmaxing into calibrated Choice, Noul and Score answers.
- **[mlx-omarchy Laya serving](https://github.com/joshuaswarren/mlx-omarchy/tree/main/serve/mlx_omarchy_laya)** · <sub>joshuaswarren · GitHub · ⭐ 64 repo · 2026-08-31</sub><br>MLX GPU backend for Apple Silicon Linux that ports and serves the open Laya typed-decision model through its own decisions endpoint, qualified on an M1 Max with 6/6 numerical gates.
- **[jev-local](https://github.com/us/jev-local)** · <sub>us · GitHub · ⭐ 3 · 2026-09-18</sub><br>Local server compatible with the /v1/systemone API that answers typed noul, choice and score questions with probabilities from open weights, so the official SDK can point at it; the default scorer is a deterministic stub.
- **[jevify](https://github.com/Mintzs/jevify)** · <sub>Mintzs · GitHub · ⭐ 3 · 2026-09-18</sub><br>Experimental inference engine that makes an existing LLM (Qwen2.5-1.5B-Instruct by default) answer Jev-style classification, yes/no and rubric questions by building JSON from model scores; probabilities are uncalibrated.
- **[Laya Go](https://github.com/neko233-com/laya-go)** · <sub>neko233-com · GitHub · ⭐ 3 · 2026-09-21</sub><br>Go server with an admin dashboard, agent CLI and MCP tool for Laya, open System 1 decision models that score structured features and return ranked probabilities without generating text.
- **[local-jev](https://github.com/amithgc/local-jev)** · <sub>amithgc · GitHub · ⭐ 3 · 2026-09-21</sub><br>Offline server that speaks TypeSafe's System One wire format so the official SDK works unchanged, answering typed questions with small open models; reports 80.5% on JevBench's 231 public items.
- **[omo-jevlike-router](https://github.com/islee23520/omo-jevlike-router)** · <sub>islee23520 · GitHub · ⭐ 3 · 2026-09-18</sub><br>Skill router for the OmO agent that scores the whole skill catalog in one forward pass with a frozen Qwen2.5-0.5B plus a small Jev-style option head, trimming the system prompt to the top-K skills.
- **[open-jev demo](https://huggingface.co/spaces/nico-martin/open-jev-demo)** · <sub>nico-martin · App · ♥ 3 · 2026-09-21</sub><br>Browser demo of the open-jev npm package running typed decisions locally with Kev and open-jev ONNX models through Transformers.js, no server or API key.
- **[systemone-lite](https://github.com/fritzprix/systemone-lite)** · <sub>fritzprix · GitHub · ⭐ 3 · 2026-09-19</sub><br>Toy local approximation of the System One API backed by a small causal LM (Qwen2.5-0.5B by default), scoring only option tokens over a shared KV-cached state, with optional fine-tuned checkpoints.
- **[Tiny-Jev](https://huggingface.co/lostargon/Tiny-Jev)** · <sub>lostargon · Hugging Face · ♥ 3 · 2026-09-21</sub><br>Open 0.6B System One model on Qwen3-0.6B that answers typed questions with calibrated probabilities: 95.8% accuracy and 0.004 ECE on in-family tests, 93.5% out of distribution.
- **[typed-decisions](https://github.com/kotoba-lang/typed-decisions)** · <sub>kotoba-lang · GitHub · ⭐ 3 · 2026-09-18</sub><br>Lightweight reproduction of the Jev shape, one state with many Choice, Score, and Noul questions answered in one pass, on ModernBERT, DeBERTa, and LLaDA-MoE with measured latency, calibration, and training cost.
- **[Qwen3.8 as Jev-compatible endpoint](https://github.com/PixelML/club-170hx/tree/main/results/2026-09-20-qwen3.8-27b-w4a16-jev-1card-vllm)** · <sub>PixelML · GitHub · ⭐ 57 repo · 2026-08-30</sub><br>Benchmark recipe serving a stock Qwen3.8-27B W4A16 checkpoint as a no-train Jev-compatible /v1/systemone endpoint on one CMP 170HX card with vLLM, including calibration results.
- **[ggmlc Laya engine](https://github.com/monatis/ggmlc/tree/main/examples/laya)** · <sub>monatis · GitHub · ⭐ 46 repo · 2026-08-22</sub><br>Example in the ggmlc neural-network compiler that compiles the open Jev alternative Laya into a standalone C++ decision engine with GGUF weights and a TypeSafe-compatible /v1/systemone server; ~25 ms per decision on an RTX 4050 Laptop.
- **[cu-Jev](https://github.com/dtunai/cu-Jev)** · <sub>dtunai · GitHub · ⭐ 2 · 2026-09-20</sub><br>C/CUDA decision engine that turns open Qwen3.5 checkpoints (0.8B to 9B) into a Jev-compatible /v1/systemone API with hand-written kernels and no PyTorch at runtime, plus reproducible benchmarks.
- **[Jev Distill Corpus v3](https://huggingface.co/datasets/SargeDev/jev-distill-corpus-v3)** · <sub>SargeDev · Hugging Face · ♥ 2 · 2026-09-21</sub><br>Typed-decision corpus of 740,957 rows in the System One noul/choice/score schema, largely synthetic scenarios across 53 domains labeled by Jev 1.13 via OpenRouter, for training small local judges.
- **[jev-browser-local](https://github.com/rorshopping/jev-browser-local)** · <sub>rorshopping · GitHub · ⭐ 2 · 2026-09-18</sub><br>Runs jev-browser on a fully local Jev-style decision engine on an RTX 2060 SUPER, with Qwen2.5-1.5B for decisions and Qwen2.5-0.5B for typing, a warm-browser fork, VRAM guard, and run traces.
- **[Laya vs Jev benchmark](https://huggingface.co/datasets/Luni/laya-jev-benchmark)** · <sub>Luni · Hugging Face · ♥ 2 · 2026-09-19</sub><br>Independent check of Laya against Jev's published numbers on an RTX 5090: raw Laya sits near chance on PhishNChips phishing (0.505) but reaches 0.611 after Platt calibration, vs Jev's 0.626.
- **[metask-jev](https://github.com/metask-ai/metask-jev)** · <sub>metask-ai · GitHub · ⭐ 2 · 2026-09-21</sub><br>Open-weight Jev-class typed-decision models on Qwen3.5 that read calibrated per-option probabilities in one forward pass; metask-jev-4b reports 80.1% on JevBench versus 75.3% for Jev 1.13.0.
- **[OpenJev (GPT-AGI)](https://github.com/GPT-AGI/OpenJev)** · <sub>GPT-AGI · GitHub · ⭐ 2 · 2026-09-20</sub><br>Open-source Jev-compatible decision engine that answers Choice, Score and Noul questions from open-weight models in one forward pass behind /v1/systemone, with a Claude Code style REPL and a maze demo.
- **[Visual Jev](https://github.com/andrueandersoncs/visual-jev)** · <sub>andrueandersoncs · GitHub · ⭐ 2 · 2026-09-19</sub><br>Open, local image-native typed decisions on a Qwen3-VL backbone, answering Choice, Score and Noul questions about images as calibrated distributions without generating text.
- **[rlx-kev](https://github.com/MIT-RLX/rlx-models/tree/main/crates/rlx-kev)** · <sub>MIT-RLX · GitHub · ⭐ 34 repo · 2026-05-22</sub><br>Rust port of Kev, a small Jev-like System One decision model with a Qwen3.5 backbone, merged LoRA and pointer head, running natively on the RLX multi-backend ML compiler and runtime.
- **[System One Mini](https://huggingface.co/DavidHatley/system-one-mini)** · <sub>David Hatley · Hugging Face · ⬇ 151 · 2026-09-16</sub><br>Research prototype with a 69.3M-parameter DistilBERT encoder and five typed classification heads for fixed decisions over synthetic software-diagnosis summaries; explicitly not a Jev reproduction.
- **[Jev-Gate Student B](https://huggingface.co/SargeDev/jev-gate-student-b)** · <sub>SargeDev · Hugging Face · ⬇ 111 · 2026-09-21</sub><br>LoRA on Qwen2.5-0.5B distilled from Jev into a local memory-relevance judge that outputs a calibrated P(relevant) to decide which vector-recalled memories enter an agent context.
- **[bonzi-1.7b-v1-jev](https://huggingface.co/NicolaiMTLassen/bonzi-1.7b-v1-jev)** · <sub>NicolaiMTLassen · Hugging Face · ♥ 1 · 2026-09-20</sub><br>Recipe and measurements (no weights) for running Bonsai 1.7B GGUF as a Jev-style typed decision function that returns a probability per option from one forward pass.
- **[bonzi-27b-v2-jev](https://huggingface.co/NicolaiMTLassen/bonzi-27b-v2-jev)** · <sub>NicolaiMTLassen · Hugging Face · ♥ 1 · 2026-09-20</sub><br>Recipe and measurements (no weights) for running Ternary Bonsai 2 27B GGUF as a Jev-style typed decision function with one forward pass per decision.
- **[Build a Jev from scratch](https://huggingface.co/azharmo/build-jev-from-scratch)** · <sub>azharmo · Hugging Face · ♥ 1 · 2026-09-20</sub><br>Toy 3.1M-parameter reconstruction of the System One interface with training, eval and serving code plus an article; accuracy is low by design but calibration reaches ECE 0.027.
- **[Cerebellum-2B](https://github.com/mkeco/Cerebellum-2B)** · <sub>mkeco · GitHub · ⭐ 1 · 2026-09-19</sub><br>Open-weight 2B decision model built on Qwen3.5-2B that picks tool routes and DOM actions from a candidate set in a single forward pass, pitched as an open alternative to Jev, with BF16, FP8 and INT8 weights.
- **[DecisionBridge](https://github.com/grishahq/decisionbridge)** · <sub>grishahq · GitHub · ⭐ 1 · 2026-09-17</sub><br>Jev-inspired adapter that turns existing LLMs (OpenAI, Anthropic, OpenRouter, local MLX) into decision functions with explicit option scores, optional calibration on labeled examples and human-review thresholds.
- **[INSTRUCT_JEV](https://github.com/ctaxnagomi/instruct-jev)** · <sub>ctaxnagomi · GitHub · ⭐ 1 · 2026-09-19</sub><br>Instruction corpus of 119 Choice, Noul and Score rows compiled from TypeSafe's public Jev documentation, published as a HuggingFace dataset.
- **[Jev-Omni](https://huggingface.co/akhilaaa3/Jev-Omni)** · <sub>akhilaaa3 · Hugging Face · ♥ 1 · 2026-09-20</sub><br>Multimodal decision classifier on Gemma 4 12B that returns a probability per option for text, image, audio and video questions; 87.57% on DecisionBench Medium and 86.15% on JevBench.
- **[jevify-gemma4-26b-a4b](https://huggingface.co/kushalpatil/jevify-gemma4-26b-a4b)** · <sub>kushalpatil · Hugging Face · ♥ 1 · 2026-09-20</sub><br>Gemma 4 26B-A4B fine-tuned (LoRA, merged) to give honest probabilities on typed questions; the model behind jevify, a local Jev-compatible /v1/systemone decision API.
- **[jevinf](https://github.com/zerodegress/jevinf)** · <sub>zerodegress · GitHub · ⭐ 1 · 2026-09-19</sub><br>Inference engine for Jev-like decision models that runs each candidate path as segmented forwards with prefix reuse and serves the Jev wire contract, measured 2.57x faster on MPS with NanoJev.
- **[jevlike-esp32](https://github.com/david-cermak/jevlike-esp32)** · <sub>david-cermak · GitHub · ⭐ 1 · 2026-09-18</sub><br>Experiment that exports a jevlike text scorer, trained in Python, as ESP-IDF firmware with a C scorer and a host-side check, running one-pass option decisions on an ESP32 microcontroller.
- **[jevlite dataset](https://huggingface.co/datasets/vagmi/jevlite_dataset)** · <sub>vagmi · Hugging Face · ♥ 1 · 2026-09-20</sub><br>Synthetic set of 5,866 typed questions about 978 program states (tickets, SIEM alerts, invoices, agent transcripts, code reviews) with full teacher distributions, used to train jev-lite.
- **[open-system-one-bench](https://huggingface.co/datasets/dylantom2012/open-system-one-bench)** · <sub>dylantom2012 · Hugging Face · ♥ 1 · 2026-09-21</sub><br>Per-item predictions for 10,000 classification and routing decisions from six stacks, including typesafe/jev and Laya on identical items, so significance tests can be rerun without API spend.
- **[openjev-experiments](https://github.com/zefir1990/openjev-experiments)** · <sub>zefir1990 · GitHub · ⭐ 1 · 2026-09-17</sub><br>Self-contained script that runs AlexWortega/openjev, a Qwen3.5-4B cross-encoder, locally for natural language inference, multiple-choice reranking and a CLI.
- **[PocketJev](https://github.com/NullPo-jp/PocketJev)** · <sub>NullPo-jp · GitHub · ⭐ 1 · 2026-09-17</sub><br>Experimental iOS app that runs Qwen3-VL on-device via MLX and turns a camera frame, a question and 2-26 options into relative scores read from next-token logits in about a second, with no photos saved.
- **[System One: encode once, decide in parallel](https://huggingface.co/spaces/jasonkneen/open-jev)** · <sub>jasonkneen · App · ♥ 1 · 2026-09-18</sub><br>Space showing the inference path that makes pngwn's System One scorer cheap, encoding the state once and scoring all options in parallel, next to the instruct model generating the same answers.
- **[System One training pairs](https://huggingface.co/datasets/shreyanbr/system-one-training-pairs)** · <sub>shreyanbr · Hugging Face · ⬇ 93 · 2026-09-19</sub><br>Training bundle for a DeBERTa System One cross-encoder: gold premise-hypothesis pairs, Claude Haiku 4.5 distillation labels, fixed Banking77 and tool-selection splits, and the fine-tuning code.
- **[jevify-gemma4-e4b](https://huggingface.co/kushalpatil/jevify-gemma4-e4b)** · <sub>kushalpatil · Hugging Face · ⬇ 85 · 2026-09-20</sub><br>Gemma 4 E4B fine-tuned (LoRA, merged) to give honest probabilities on typed questions, served by jevify as a local Jev-compatible /v1/systemone decision API.
- **[AINode System One API](https://github.com/getainode/ainode/blob/main/ainode/api/systemone.py)** · <sub>getainode · GitHub · ⭐ 15 repo · 2026-04-12</sub><br>System One-compatible decide API in AINode, a self-hosted AI platform for NVIDIA GPUs, benchmarked on 110 labeled decisions: hosted Jev scored 0.964 accuracy, Brier 0.024 and 0 of 80 wrong at a 0.9 gate vs a local 35B chat model.
- **[hedos System One gateway](https://github.com/theiskaa/hedos/blob/main/gateway/src/handlers/systemone.rs)** · <sub>theiskaa · GitHub · ⭐ 14 repo · 2026-07-05</sub><br>Headless local model engine whose gateway exposes TypeSafe's POST /v1/systemone, so a TypeSafe SDK pointed at it gets answers from a local judge-capable model.
- **[leCore holographic System One](https://github.com/AnOversizedMooseWithSocks/leCore/blob/main/holographic/agents_and_reasoning/holographic_systemone.py)** · <sub>AnOversizedMooseWithSocks · GitHub · ⭐ 11 repo · 2026-06-08</sub><br>Native implementation of Jev's state-plus-typed-questions contract inside a pure-NumPy vector engine, as a few-shot prototype classifier that abstains on ties and returns no probability until calibrated.
- **[SparkStation decision models](https://github.com/kshetrajna12/sparkstation/blob/main/supervisor/launchers/reflex_launcher.py)** · <sub>kshetrajna12 · GitHub · ⭐ 8 repo · 2025-10-27</sub><br>Model fleet manager for NVIDIA DGX Spark that serves decision models such as Reflex over a TypeSafe-Jev-compatible POST /v1/systemone endpoint next to its OpenAI-compatible gateway.
- **[AgentKthx JEV API mode](https://github.com/VTSTech/AgentKthx/blob/main/docs/JEV_API_MODE.md)** · <sub>VTSTech · GitHub · ⭐ 5 repo · 2026-03-20</sub><br>Mode in the AgentKthx local-first agent framework that emulates Jev's System One decision shape with any chat LLM (Ollama, ZAI, OpenRouter, llama-server) by wrapping a constrained prompt and parsing a decision envelope.
- **[System One (distilled)](https://huggingface.co/shreyanbr/system-one-distilled)** · <sub>shreyanbr · Hugging Face · ⬇ 25 · 2026-09-19</sub><br>A 70.8M DeBERTa-v3-xsmall cross-encoder for the Jev /v1/systemone schema, trained on Claude Haiku 4.5's answers to compare distillation against gold labels.
- **[jev-0.5b](https://huggingface.co/jaswanthsanjay88/jev-0.5b)** · <sub>jaswanthsanjay88 · Hugging Face · ⬇ 22 · 2026-09-19</sub><br>Prefill-only Jev-style decision model on Qwen2.5-0.5B: a LoRA adapter plus pointer readout head with block-causal attention to answer several questions in one pass behind a /v1/systemone API.
- **[jev-my-bro governance dataset](https://huggingface.co/datasets/JonusNattapong/jev-my-bro-dataset)** · <sub>JonusNattapong · Hugging Face · ⬇ 17 · 2026-09-21</sub><br>English/Thai dataset of 8,508 cases and 34,032 typed decisions on whether an agent operation should execute, ask the user or be rejected, needs review, is prohibited, and how risky it is.
- **[System One (gold)](https://huggingface.co/shreyanbr/system-one-gold)** · <sub>shreyanbr · Hugging Face · ⬇ 16 · 2026-09-19</sub><br>A 70.8M DeBERTa-v3-xsmall cross-encoder for the Jev /v1/systemone schema trained on each dataset's own labels, the gold-supervised arm of a Jev versus Haiku benchmarking study.
- **[System One (zeroshot)](https://huggingface.co/shreyanbr/system-one-zeroshot)** · <sub>shreyanbr · Hugging Face · ⬇ 15 · 2026-09-19</sub><br>Unsupervised baseline of a 70.8M DeBERTa-v3-xsmall cross-encoder implementing the Jev /v1/systemone schema, answering Choice, Score and Noul in one batched pass.
- **[jev-qwen3.5-4b-legal-lora](https://huggingface.co/Nebulaw1/jev-qwen3.5-4b-legal-lora)** · <sub>Nebulaw1 · Hugging Face · ⬇ 1 · 2026-09-20</sub><br>QLoRA adapter on Qwen3.5-4B-Base for finite-choice Chinese legal judgments that scores candidate letters in one forward pass instead of generating legal reasoning, with evaluation and inference scripts.
- **[AgentJev](https://huggingface.co/aimeigaoshou/agent-jev)** · <sub>aimeigaoshou · Hugging Face · 2026-09-21</sub><br>Open 0.6B agent decision model with shared-prefix caching that returns distributions for questions like which tool is next; 79.25% top-1 on 2,000 Typed Decisions questions vs 72.7% for Jev 1.13.0.
- **[bonzi-27b-v1-jev](https://huggingface.co/NicolaiMTLassen/bonzi-27b-v1-jev)** · <sub>NicolaiMTLassen · Hugging Face · 2026-09-20</sub><br>Recipe and measurements (no weights) for running Bonsai 1 27B GGUF as a Jev-style typed decision function that returns a probability per option from one forward pass.
- **[bonzi-4b-v1-jev](https://huggingface.co/NicolaiMTLassen/bonzi-4b-v1-jev)** · <sub>NicolaiMTLassen · Hugging Face · 2026-09-20</sub><br>Recipe and measurements (no weights) for running Bonsai 1 4B GGUF as a Jev-style typed decision function that returns a probability per option from one forward pass.
- **[bonzi-8b-ternary-v1-jev](https://huggingface.co/NicolaiMTLassen/bonzi-8b-ternary-v1-jev)** · <sub>NicolaiMTLassen · Hugging Face · 2026-09-20</sub><br>Recipe and measurements (no weights) for running Ternary Bonsai 1 8B GGUF as a Jev-style typed decision function that returns a probability per option from one forward pass.
- **[bonzi-8b-v1-jev](https://huggingface.co/NicolaiMTLassen/bonzi-8b-v1-jev)** · <sub>NicolaiMTLassen · Hugging Face · 2026-09-20</sub><br>Recipe and measurements (no weights) for running Bonsai 1 8B GGUF as a Jev-style typed decision function that returns a probability per option from one forward pass.
- **[jev-agent-lab](https://github.com/michael54/jev-agent-lab)** · <sub>michael54 · GitHub · 2026-09-19</sub><br>Reproducible Runpod deployment of the open Jev-style SemIf model alongside an official Jev client, with agent decision cases, latency measurements and a Jev vs SemIf comparison report.
- **[jev-gemma-4-E2B-it-choice-64](https://huggingface.co/ohtaman/jev-gemma-4-E2B-it-choice-64)** · <sub>ohtaman · Hugging Face · 2026-09-22</sub><br>Browser-oriented ONNX artifact of Gemma 4 E2B with its output projection restricted to 64 fixed answer tokens, turning it into a text-only fixed-label scorer without fine-tuning.
- **[jev-local-lab decision heads](https://huggingface.co/mchen04/jev-local-lab-decision-heads)** · <sub>mchen04 · Hugging Face · 2026-09-21</sub><br>Tiny trained heads (0.2 to 1.3M parameters) that read structured decisions from a 4-bit Qwen2.5-1.5B on a 24 GB Mac mini, released as a documented side project with honest limits.
- **[jev-my-bro](https://huggingface.co/JonusNattapong/jev-my-bro)** · <sub>JonusNattapong · Hugging Face · 2026-09-21</sub><br>Self-hosted English/Thai decision model for agent and tool governance that decides whether to execute, ask for approval, reject or escalate an operation; v0.2 reports 73.78% accuracy.
- **[jev-typed-decisions-causal-0.6b](https://huggingface.co/abidlabs/jev-typed-decisions-causal-0.6b)** · <sub>abidlabs · Hugging Face · 2026-09-21</sub><br>LoRA adapters on Qwen3-0.6B-Base trained with the arm-B cached causal typed scorer recipe from pngwn's typed-decisions experiment, a Jev-like reproduction with a frozen LM head.
- **[Jev-Vision](https://huggingface.co/SeanLiu/Jev-Vision)** · <sub>SeanLiu · Hugging Face · 2026-09-21</sub><br>Open-weight vision decision model (LoRA plus typed heads on Qwen3-VL-8B) that answers typed questions about screenshots and images through a Jev-compatible /v1/systemone API, 150-190 ms per screen step.
- **[jevify-qwen3-vl-2b (Tier 0)](https://huggingface.co/Praveenrajus/jevify-qwen3-vl-2b)** · <sub>Praveenrajus · Hugging Face · 2026-09-21</sub><br>Training-free Jevify recipe that uses Qwen3-VL-2B to answer typed questions about images, reading every allowed answer from one position with a validation-fitted calibration.
- **[jevify-qwen3-vl-2b-t2](https://huggingface.co/Praveenrajus/jevify-qwen3-vl-2b-t2)** · <sub>Praveenrajus · Hugging Face · 2026-09-22</sub><br>Tier 2 Jevify vision model: Qwen3-VL-2B with a rank-16 decoder LoRA trained on the restricted answer readout with proper scoring rules on A-OKVQA, for typed questions about images.
- **[jevify-qwen3.5-2b](https://huggingface.co/Praveenrajus/jevify-qwen3.5-2b)** · <sub>Praveenrajus · Hugging Face · 2026-09-21</sub><br>Jevify decision heads for Qwen3.5-2B that answer choice, score and noul questions about a state with calibrated probability distributions, without generating text.
- **[jevify-qwen3.5-4b](https://huggingface.co/Praveenrajus/jevify-qwen3.5-4b)** · <sub>Praveenrajus · Hugging Face · 2026-09-21</sub><br>Jevify decision heads for Qwen3.5-4B that read a state, answer choice, score and noul questions and return calibrated distributions, shipping only the heads added on top of the base model.
- **[jevify-qwen3.5-4b-t2](https://huggingface.co/Praveenrajus/jevify-qwen3.5-4b-t2)** · <sub>Praveenrajus · Hugging Face · 2026-09-22</sub><br>Tier 2 Jevify model for Qwen3.5-4B that adds a LoRA adapter on top of the decision heads to return calibrated choice, score and noul distributions.
- **[JevOne](https://huggingface.co/juspay/jev-one)** · <sub>juspay · Hugging Face · 2026-09-21</sub><br>Typed decision model on Qwen3.6-35B-A3B served through a TypeSafe-compatible /v1/systemone API, with single-token candidate readout, forward and reverse option-order evaluation and calibration.
- **[jevons-lfm25-1.2b-systemone](https://huggingface.co/gopalanj/jevons-lfm25-1.2b-systemone)** · <sub>gopalanj · Hugging Face · 2026-09-20</sub><br>Seed LoRA on LFM2.5-1.2B for jevons, a local System One server that scores allowed outcomes from logits and assembles choice, probabilities, confidence, noul and score in code.
- **[jqv](https://github.com/Octalab-Inc/jqv)** · <sub>Octalab-Inc · GitHub · 2026-09-21</sub><br>Reconstruction of Jev's inference structure on stock Qwen3, with one shared state prefill, isolated question branches behind a block attention mask, and option-letter logits calibrated by temperature, behind /v1/systemone.
- **[Laya plays Doom](https://medium.com/@christian.graham_49279/laya-a-free-local-alternative-to-jev-and-it-can-even-play-doom-ish-42e2292e541e)** · <sub>Christian Graham · Article · 2026-09-18</sub><br>Tests Laya, an open 421M-parameter Jev alternative, by having it play Doom locally, adding a dedicated shoot question and logged rule overrides to fix misfires and stuck loops.
- **[layaForWeb](https://medium.com/@visrow/jev-vs-laya-live-demo-i-ran-a-421-million-parameter-ai-decision-model-inside-a-browser-tab-no-84b86bed1f10)** · <sub>Vishal Mysore · Article · 2026-09-21</sub><br>Runs the open 421M-parameter Laya decision model inside a browser tab via ONNX Runtime Web and WebAssembly, shown next to Jev's playground; the browser build matched PyTorch's top answer on all 14 questions.
- **[local-system-one-student](https://huggingface.co/Mannedood/local-system-one-student)** · <sub>Mannedood · Hugging Face · 2026-09-18</sub><br>A 149M ModernBERT encoder distilled from local LLMs that reproduces Jev's interface for one fixed schema, a coding agent's next step, returning tool choice, urgency and destructive-action flags in 19 ms.
- **[open-system-one demo](https://huggingface.co/spaces/dylantom2012/open-system-one-demo)** · <sub>dylantom2012 · App · 2026-09-21</sub><br>Demo comparing a 0.1 ms trained decision head with a zero-shot cross-encoder, from an independent benchmark of Jev against open CPU-only alternatives.
- **[open-system-one results explorer](https://huggingface.co/spaces/dylantom2012/open-system-one)** · <sub>dylantom2012 · App · 2026-09-21</sub><br>Interactive explorer for an independent benchmark of TypeSafe's Jev against open CPU-only stacks on 10,000 decisions.
- **[smalljev](https://github.com/isHeSatoshi/smalljev)** · <sub>isHeSatoshi · GitHub · 2026-09-20</sub><br>Open Jev-style decision model built on MiniCPM5-2B-Base with a LoRA adapter and native decision heads, about 2.5B parameters answering in one forward pass with no generated tokens, aimed at phones.
- **[System One (phase2 student)](https://huggingface.co/lafalce/system-one-model)** · <sub>lafalce · Hugging Face · 2026-09-19</sub><br>Local decision model from ModernBERT-base with LoRA and a two-layer scoring head that takes JSON or text state and answers typed choice, score and noul questions in one pass.
- **[System One vs Laya vs DeepSeek](https://huggingface.co/spaces/henrybit/jev-vs-deepseek)** · <sub>henrybit · App · 2026-09-22</sub><br>Chinese-language Space comparing three decision paths on the same state and typed questions: pngwn's open System One scorer, Laya, and DeepSeek via chat completions returning JSON.
- **[system-one-270m](https://huggingface.co/kaivoss/system-one-270m)** · <sub>kaivoss · Hugging Face · 2026-09-21</sub><br>Open System One reproduction on Gemma 3 270M that takes state plus a typed question with caller-supplied options and returns one option with a calibrated probability, never free text.
- **[system-one-270m-data](https://huggingface.co/datasets/kaivoss/system-one-270m-data)** · <sub>kaivoss · Hugging Face · 2026-09-21</sub><br>Synthetic set of 25,002 typed decisions with soft target distributions over caller-supplied options, rendered as lettered prompts, for training the open system-one-270m model.
- **[system-one-adapter (Rust)](https://github.com/codeitlikemiley/system-one-adapter-rust)** · <sub>codeitlikemiley · GitHub · 2026-09-16</sub><br>Rust port of system-one-adapter: a drop-in replacement for TypeSafe's system_one call backed by LLM APIs, with compatible question, answer, retry and error types for comparing cost, speed and quality.
- **[tiny-jev](https://github.com/karimatayuta/tiny-jev)** · <sub>karimatayuta · GitHub · 2026-09-18</sub><br>Small local judgment model for Japanese text that returns choice, score, and noul answers from Qwen3 yes/no scores with LoRA training, abstaining until business data and calibration are in place.

</details>

Missing something? [Suggest a resource](https://github.com/Li-Evan/awesome-jev/issues/new/choose).
