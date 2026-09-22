# 🧬 开源模型与兼容服务

[English](https://github.com/Li-Evan/awesome-jev/blob/main/pages/open-models.md) · **简体中文**

模仿 Jev 接口的社区模型和服务。它们的准确率和校准都是自报数据，普遍不如 Jev，请用自己的数据评估。共 240 条，按社区热度排序。

[← 返回 Awesome Jev](https://github.com/Li-Evan/awesome-jev/blob/main/README.zh-CN.md#开源模型与兼容服务)

<table>
<tr>
<td width="260" valign="top"><a href="https://github.com/vllm-project/vllm/pull/57250"><img src="https://opengraph.githubassets.com/1/vllm-project/vllm" alt="vLLM 的 DiffusionGemma Jev 模式" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/vllm-project/vllm/pull/57250">vLLM 的 DiffusionGemma Jev 模式</a></b><br><sub>mmastrac · GitHub · ⭐ 92.4k · 2026-09-16</sub><br>一个仍处于 open 状态的 vLLM pull request，新增结构化生成模式，把 DiffusionGemma 变成类 Jev 模型，并附带 /v1/systemone 端点的原型服务器。<br><sub><b>Jev 用法:</b> 在输出格式中固定画布位置，读取 token logprobs 推导出答案和置信度，熵较高时重新采样。</sub><br><sub>相关: <a href="https://news.ycombinator.com/item?id=49734375">demo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://huggingface.co/harshatheg/Qwen-2.5-1B-RLCD"><img src="https://cdn-thumbnails.huggingface.co/social-thumbnails/models/harshatheg/Qwen-2.5-1B-RLCD.png" alt="Qwen-2.5-1B-RLCD" width="240"></a></td>
<td valign="top"><b><a href="https://huggingface.co/harshatheg/Qwen-2.5-1B-RLCD">Qwen-2.5-1B-RLCD</a></b><br><sub>harshatheg · Hugging Face · ♥ 524 · 2026-09-16</sub><br>面向 Apple Silicon 的并行约束解码引擎，基于原版 Qwen2.5-1.5B 一次回答多字段决策 schema，只发布代码，没有训练好的 RLCD 权重。<br><sub><b>Jev 用法:</b> Jev 风格接口：在各字段间广播 KV cache，并在允许值上切片 logits；报告在 M4 Max 上延迟比自回归 JSON 低 5.6 倍到 7.0 倍。</sub><br><sub>相关: <a href="https://huggingface.co/spaces/drinkmoonshine/parallel-constrained-decoding">demo</a> · <a href="https://x.com/TravisJChauvin/status/2101081157421121725">post</a> · <a href="https://x.com/harshagundal/status/2100044305536889015">demo 2</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/NandhaKishorM/laya"><img src="https://raw.githubusercontent.com/NandhaKishorM/laya/main/assets/laya_vs_jev_full.png" alt="Laya" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/NandhaKishorM/laya">Laya</a></b><br><sub>NandhaKishorM · GitHub · ⭐ 12k · 2026-09-18</sub><br>基于 ModernBERT 式编码器的开放本地非自回归决策模型，从 421M 的英文检查点到多语言检查点都有，回答 Choice、Score 和 Noul 问题每个问题 33 毫秒，并带有按请求分流的路由器。<br><sub>相关: <a href="https://www.reddit.com/r/accelerate/comments/1wk0yq7/laya_421m_open_source_and_local_model_takes_on/">discussion</a> · <a href="https://huggingface.co/spaces/convaiinnovations/laya-demo">app</a> · <a href="https://huggingface.co/convaiinnovations/laya">model</a> · <a href="https://dev.to/nandakishor_m_6cc0adfde9f/i-built-non-autoregressive-decision-models-a-year-ago-then-a-frontier-lab-called-it-a-18me">article</a> · <a href="https://www.reddit.com/r/LocalLLaMA/comments/1wjieap/made_the_horizontal_opensource_model_for_jev_with/">discussion 2</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/taroleo/status/2101106887840370919"><img src="https://pbs.twimg.com/amplify_video_thumb/2101102823408807936/img/k_uNGVHacO6DG6mC.jpg" alt="蒸馏出的 4B 本地决策模型" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/taroleo/status/2101106887840370919">蒸馏出的 4B 本地决策模型</a></b><br><sub>taroleo · X · ♥ 3k · 2026-09-19</sub><br>在一台 DGX Spark 上用 26 小时把 DeepSeek V4 Flash 的判断蒸馏成 Jev 式 4B 本地模型，以 1/20 的体量胜过老师模型的即时模式，每次决策约 22 毫秒。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/atomic_chat_hq/status/2102160983409955244"><img src="https://pbs.twimg.com/amplify_video_thumb/2102158998103363584/img/AStT6MxzhJzruHIE.jpg" alt="Laya 对战 Jev：Tetris" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/atomic_chat_hq/status/2102160983409955244">Laya 对战 Jev：Tetris</a></b><br><sub>atomic_chat_hq · X · ♥ 2.8k · 2026-09-21</sub><br>一场 Tetris 对决：在 16GB MacBook Air 上本地运行的开放权重 Laya 模型，决策速度快 11 倍，击败了云端 Jev。<br><sub>相关: <a href="https://atomic.chat">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/wdobry/laya-playground"><img src="https://brainfunctioncollapse.com/laya/og.png" alt="Laya playground" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/wdobry/laya-playground">Laya playground</a></b><br><sub>wdobry · GitHub · ⭐ 71 · 2026-09-20</sub><br>本地网站，为开源 Laya 决策模型提供游戏、基准测试和 agent skill，并在同样的 500 个带标签样本上与托管版 Jev 对比。<br><sub><b>Jev 用法:</b> 开箱即用时 Jev 更准确；Laya 在简单问题上与之持平，而且在笔记本上作答快好几倍。</sub><br><sub>相关: <a href="https://brainfunctioncollapse.com/laya">app</a> · <a href="https://brainfunctioncollapse.com/laya">app 2</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/mizorewww/laya-mlx"><img src="https://raw.githubusercontent.com/mizorewww/laya-mlx/main/docs/assets/snake-demo.gif" alt="Laya-MLX" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/mizorewww/laya-mlx">Laya-MLX</a></b><br><sub>mizorewww · GitHub · ⭐ 4.3k · 2026-09-19</sub><br>Apple Silicon 上开放 Laya 类型化决策检查点的原生 MLX 运行时：简短英文决策中位耗时 13.4 毫秒，多语言检查点为 7.4 毫秒，无需 PyTorch 或云端 API；以贪吃蛇做了演示。<br><sub>相关: <a href="https://x.com/mizorewww/status/2101473552956555427">demo</a> · <a href="https://pypi.org/project/laya-mlx/">pypi</a> · <a href="https://x.com/tdinh_me/status/2101919182824804560">demo 2</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/TheoLeeCJ/SemIf"><img src="https://raw.githubusercontent.com/TheoLeeCJ/SemIf/master/demo/assets/semif-phase1-replay.gif" alt="SemIf (formerly OpenJev)" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/TheoLeeCJ/SemIf">SemIf (formerly OpenJev)</a></b><br><sub>TheoLeeCJ · GitHub · ⭐ 3.4k · 2026-09-16</sub><br>独立的类 Jev 项目，在家用 RTX 3090 上从冻结的 4B 开放模型读取选项 logits 来回答语义 if 问题，附带浏览器演示，不生成文本。<br><sub>相关: <a href="https://openjev.com">app</a> · <a href="https://www.reddit.com/r/LocalLLaMA/comments/1whzy7j/qwen35_4b_grabbing_logits_is_almost_jev_or_even/">discussion</a> · <a href="https://openjev.com">app 2</a> · <a href="https://x.com/mygtmhire/status/2100666488625734103">demo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/jaredpalmer/kev"><img src="https://raw.githubusercontent.com/jaredpalmer/kev/main/docs/playground.png" alt="Kev" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/jaredpalmer/kev">Kev</a></b><br><sub>jaredpalmer · GitHub · ⭐ 2.7k · 2026-09-17</sub><br>基于 Qwen3.5 的开放 0.8B 到 9B 决策模型，发布了权重和一个兼容 <code>/v1/systemone</code> 的服务器，官方 SDK 可以直接指向它。<br><sub>相关: <a href="https://x.com/jaredpalmer/status/2101028325472841920">demo</a> · <a href="https://news.ycombinator.com/item?id=49783999">discussion</a> · <a href="https://huggingface.co/collections/jaredpalmer">model</a> · <a href="https://news.ycombinator.com/item?id=49783999">discussion 2</a> · <a href="https://huggingface.co/datasets/jaredpalmer/kev-suites">model 2</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/wmoto_ai/status/2100454049359577516"><img src="https://pbs.twimg.com/amplify_video_thumb/2100453978958118912/img/yOW2Lupx9RoG03zB.jpg" alt="本地 Jev 实验" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/wmoto_ai/status/2100454049359577516">本地 Jev 实验</a></b><br><sub>wmoto_ai · X · ♥ 388 · 2026-09-17</sub><br>演示一套自制的 Jev 风格决策方案在本地 LLM 上运行，作者表示速度还有提升空间。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/featherless-ai/simple-jev"><img src="https://raw.githubusercontent.com/featherless-ai/simple-jev/main/imgs/Simple-Jev-Logo.png" alt="simple-jev" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/featherless-ai/simple-jev">simple-jev</a></b><br><sub>featherless-ai · GitHub · ⭐ 461 · 2026-09-18</sub><br>把任意 Hugging Face 模型变成决策端点，并提供 <code>/v1/systemone</code> 别名（概率未经校准）。<br><sub>相关: <a href="https://simple-jev.featherless.ai">site</a> · <a href="https://x.com/picocreator/status/2101006253829046539">demo</a> · <a href="https://x.com/Richelle_Ji/status/2101064292242219407">demo 2</a> · <a href="https://x.com/vintcessun/status/2101896965181395175">demo 3</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/skeptrune/status/2101209390992994570"><img src="https://pbs.twimg.com/amplify_video_thumb/2101204678604455936/img/-Sg1h83wAYEc959c.jpg" alt="deepseek-v4.1-flash-jev" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/skeptrune/status/2101209390992994570">deepseek-v4.1-flash-jev</a></b><br><sub>skeptrune · X · ♥ 1.4k · 2026-09-19</sub><br>一个让 DeepSeek V4.1 Flash 表现得像 Jev 的端点：借助 SGLang 的打分 API，在固定答案集合上返回概率，而不是生成文本。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/TianyuCodings/NanoJev"><img src="https://opengraph.githubassets.com/1/TianyuCodings/NanoJev" alt="NanoJev" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/TianyuCodings/NanoJev">NanoJev</a></b><br><sub>TianyuCodings · GitHub · ⭐ 1.9k · 2026-09-17</sub><br>开放的 0.6B Jev 复刻模型，针对四款特定游戏训练，附带权重和数据；不能作为通用替代品。<br><sub>相关: <a href="https://x.com/QingQ77/status/2101125879766421755">demo</a> · <a href="https://huggingface.co/c-tianyu/nanojev">model</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/bespokelabsai/nimble"><img src="https://raw.githubusercontent.com/bespokelabsai/nimble/main/assets/diagrams/nimble-infographic.svg" alt="Bespoke Nimble" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/bespokelabsai/nimble">Bespoke Nimble</a></b><br><sub>bespokelabsai · GitHub · ⭐ 1.5k · 2026-09-18</sub><br>面向 Jev 式类型化决策的开放数据、训练配方和 Qwen3.5-9B LoRA 模型，用翻转单个事实构造的对比负样本训练；报告与 Jev 的一致率为 90.1%，基础版 Qwen 为 66.4%。<br><sub>相关: <a href="https://x.com/madiator/status/2100990591215783946">demo</a> · <a href="https://huggingface.co/bespokelabs/bespoke-nimble-9b">model</a> · <a href="https://news.ycombinator.com/item?id=49757009">discussion</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/vinnylarouge/jevlike"><img src="https://raw.githubusercontent.com/vinnylarouge/jevlike/main/docs/architecture.svg" alt="Jevlike" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/vinnylarouge/jevlike">Jevlike</a></b><br><sub>vinnylarouge · GitHub · ⭐ 1.2k · 2026-09-16</sub><br>与 Jev 形态相同的独立入门模型：一个小型单遍打分器，把文本加 N 个选项映射为每个选项一个概率，附 Doom 和国际象棋视觉演示，以及一个 Wikispeedia 预测下一次点击的示例。<br><sub>相关: <a href="https://x.com/vinnylarouge/status/2100170846346097083">demo</a> · <a href="https://news.ycombinator.com/item?id=49731282">discussion</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://www.youtube.com/watch?v=bcGO7xre46o"><img src="https://i.ytimg.com/vi/bcGO7xre46o/hqdefault.jpg" alt="llama.cpp 的 Jev 模式" width="240"></a></td>
<td valign="top"><b><a href="https://www.youtube.com/watch?v=bcGO7xre46o">llama.cpp 的 Jev 模式</a></b><br><sub>Codacus · 视频 · ♥ 1.2k · 2026-09-21</sub><br>llama.cpp 的一个分支，为 llama-server 新增一个端点：输入指令、schema 和 state，返回每个字段及其置信度分数；在 2 GB 模型上批量处理时每次决策 17.3 毫秒。<br><sub>相关: <a href="https://github.com/thecodacus/llama.cpp/tree/parallel-decision">repo</a> · <a href="https://github.com/thecodacus/decision-playground">playground</a> · <a href="https://huggingface.co/harshatheg/Qwen-2.5-1B-RLCD">model</a> · <a href="https://github.com/thecodacus/llama.cpp">project</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"></td>
<td valign="top"><b><a href="https://x.com/KUMAN_R/status/2101473262693994936">两天冒出六个 Jev 克隆</a></b><br><sub>KUMAN_R · X · ♥ 756 · 2026-09-20</sub><br>日语总结，对比六个开放 Jev 克隆的架构：Laya、DiffusionGemmaJev、Bespoke Nimble、SemIf（原名 OpenJev）、Jevlike 和 Kev-0.5B。<br><sub>相关: <a href="https://www.latent.space/p/ainews-here-are-6-clones-of-jev-in">article</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://huggingface.co/cua-ai/cua-s1-forms"><img src="https://cdn-thumbnails.huggingface.co/social-thumbnails/models/cua-ai/cua-s1-forms.png" alt="cua-s1-forms" width="240"></a></td>
<td valign="top"><b><a href="https://huggingface.co/cua-ai/cua-s1-forms">cua-s1-forms</a></b><br><sub>cua-ai · Hugging Face · ♥ 102 · 2026-09-18</sub><br>极小的类 Jev 选项打分器（706,048 个参数，2.8 MB），一次并行计算就为每个表单字段评估填写、勾选、点击或跳过，作为 cua-driver 的决策层。<br><sub><b>Jev 用法:</b> 输入/输出契约与 Jev 相同；在自己的表单填写评测上报告 99.7%，Jev 为 83.6%。</sub><br><sub>相关: <a href="https://github.com/trycua/cua/tree/main/libs/cua-s1">repo</a> · <a href="https://x.com/be_arsh/status/2101026864341164110">demo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/mizorewww/laya-coreml"><img src="https://raw.githubusercontent.com/mizorewww/laya-coreml/main/docs/assets/snake-demo.gif" alt="Laya-CoreML" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/mizorewww/laya-coreml">Laya-CoreML</a></b><br><sub>mizorewww · GitHub · ⭐ 989 · 2026-09-19</sub><br>类 Jev 的 Laya 模型到 Apple Core ML 和神经引擎的开放权重移植，在本地提供 System One 契约，附一个根据实时概率玩贪吃蛇的演示。<br><sub><b>Jev 用法:</b> 在 Choice、Score 和 Noul 上实现 system_one；在 M3 Max 上用 ANE FP16 做一次简短决策，P50 约 4.98 毫秒。</sub><br><sub>相关: <a href="https://pypi.org/project/laya-coreml/">pypi</a> · <a href="https://huggingface.co/aac6fef/laya-multilingual-coreml-ane">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/Lonely__MH/status/2101823975349244095"><img src="https://pbs.twimg.com/amplify_video_thumb/2101708973036785664/img/DgCMkHUOuz-yVIOi.jpg" alt="Laya-MLX 对比 Jev 准确率测试" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/Lonely__MH/status/2101823975349244095">Laya-MLX 对比 Jev 准确率测试</a></b><br><sub>Lonely__MH · X · ♥ 102 · 2026-09-21</sub><br>在 M2 Pro 上做了两轮、每轮 100 道决策题：本地 Laya-MLX 每题 13.7 毫秒，但准确率只有约 50%；云端 Jev 更慢，但准确得多。<br><sub>相关: <a href="https://github.com/mizorewww/laya-mlx">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Zefan-Cai/Open-Jev"><img src="https://cdn-thumbnails.huggingface.co/social-thumbnails/models/ZefanCai/Open-Jev-9B.png" alt="Open-Jev" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Zefan-Cai/Open-Jev">Open-Jev</a></b><br><sub>Zefan-Cai · GitHub · ⭐ 118 · 2026-09-20</sub><br>基于 Qwen3.5-2B、Qwen3.5-9B 和 Qwen3.8-27B 的开放概率决策模型，无需生成就能给给定候选项打分，以 LoRA adapter 形式发布，附带训练好的决策头、数据集和基准测试。<br><sub>相关: <a href="https://zefan-cai.github.io/open-jev">site</a> · <a href="https://huggingface.co/ZefanCai/Open-Jev-9B">model</a> · <a href="https://huggingface.co/ZefanCai/Open-Jev-2B">model 2</a> · <a href="https://x.com/Zefan_Cai/status/2101782158658695388">demo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/githubnext/localjev"><img src="https://opengraph.githubassets.com/1/githubnext/localjev" alt="LocalJev" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/githubnext/localjev">LocalJev</a></b><br><sub>githubnext · GitHub · ⭐ 707 · 2026-09-18</sub><br>GitHub Next 出品的 Bun 服务器，提供本地的 Jev 兼容 /v1/systemone API，后端是 DiffusionGemma，靠提示词让模型输出 JSON 概率而非读取 logits，并做了 1,200 次请求的对比评测。<br><sub>相关: <a href="https://news.ycombinator.com/item?id=49766255">discussion</a> · <a href="https://x.com/GitHubNext/status/2101193436816920798">demo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/BystAnd3rs/status/2101648153984528700"><img src="https://pbs.twimg.com/amplify_video_thumb/2101647092817305600/img/WGklbFZGYL0CnWBd.jpg" alt="Laya 对战 Jev：贪吃蛇大战" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/BystAnd3rs/status/2101648153984528700">Laya 对战 Jev：贪吃蛇大战</a></b><br><sub>BystAnd3rs · X · ♥ 158 · 2026-09-20</sub><br>用 Codex 搭建的贪吃蛇对决，在 M5 Pro 上让本地 Laya 与 Jev API 对战：Laya 的决策时间中位数为 15.3 毫秒，Jev 为 298.1 毫秒。<br><sub>相关: <a href="https://github.com/mizorewww/laya-mlx">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/incoai/splash"><img src="https://opengraph.githubassets.com/1/incoai/splash" alt="Splash" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/incoai/splash">Splash</a></b><br><sub>incoai · GitHub · ⭐ 579 · 2026-09-18</sub><br>面向编程 agent 的本地 Apple silicon 推理引擎，同时提供兼容 TypeSafe 的 /v1/systemone 端点，从 logits 回答 noul、choice 和 score 问题，可配合官方 SDK 使用。<br><sub>相关: <a href="https://inco.ai/blog/splash/">article</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"></td>
<td valign="top"><b><a href="https://news.ycombinator.com/item?id=49777106">在 M4 Mac 上用 CoreML 运行 Laya</a></b><br><sub>putna · Hacker News · ▲ 167 · 2026-09-20</sub><br>在 M4 Mac 上通过 CoreML 调用神经引擎、离线运行多语言 Laya 决策模型的方法，附贪吃蛇演示，速度约每秒 45 次决策。<br><sub>相关: <a href="https://gist.github.com/fordnox/e592d0f68b543fd044be8e6d040863a0">gist</a> · <a href="https://gist.github.com/fordnox/e592d0f68b543fd044be8e6d040863a0">project</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://huggingface.co/AlexWortega/openjev"><img src="https://huggingface.co/AlexWortega/openjev/resolve/main/assets/radar_openjev.png" alt="openjev" width="240"></a></td>
<td valign="top"><b><a href="https://huggingface.co/AlexWortega/openjev">openjev</a></b><br><sub>Alex Wortega · Hugging Face · ♥ 431 · 2026-09-16</sub><br>训练成单一 NLI cross-encoder 的 Qwen3.5 checkpoint，取蕴含得分最高者作为答案，零样本用于重排、评分、护栏，以及根据文本或像素玩 Doom。<br><sub><b>Jev 用法:</b> 通过对关于 state 的陈述做蕴含判断，给出类 Jev 的判断；4B v2 从像素输入玩 Doom 平均每局击杀 10.4 个，另外还提供 35B-A3B 的 head。</sub><br><sub>相关: <a href="https://x.com/justALEXWORTEGA/status/2100341039986798930">demo</a> · <a href="https://www.reddit.com/r/LocalLLaMA/comments/1wib9kj/openjev/">discussion</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/SiliconLabAI/OpenJev"><img src="https://opengraph.githubassets.com/1/SiliconLabAI/OpenJev" alt="OpenJev (SiliconLabAI)" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/SiliconLabAI/OpenJev">OpenJev (SiliconLabAI)</a></b><br><sub>SiliconLabAI · GitHub · ⭐ 67 · 2026-09-20</sub><br>开放的 System One 风格决策 playground，接收 state 和类型化问题，可通过 LLM 微型打分器、对 OpenAI 兼容模型的一次结构化 JSON 调用，或开放的 Mapika/decider 权重来作答。<br><sub>相关: <a href="https://www.youtube.com/watch?v=xtXq279B4Go">video</a> · <a href="https://www.youtube.com/watch?v=xtXq279B4Go">video 2</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/theAlexQuach/status/2101397697454649684"><img src="https://pbs.twimg.com/media/HSmoWsEaQAEYMBV.jpg?name=orig" alt="支持图像的开源 Jev 替代品" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/theAlexQuach/status/2101397697454649684">支持图像的开源 Jev 替代品</a></b><br><sub>theAlexQuach · X · ♥ 177 · 2026-09-19</sub><br>测试能接收图像的开源类 Jev 模型，发现 DiffusionGemma（通过一个 vLLM PR）和 reflex 位于视觉决策的 Pareto 前沿。<br><sub>相关: <a href="https://github.com/vllm-project/vllm/pull/57250">vllm-pr</a> · <a href="https://github.com/kshetrajna12/reflex">reflex</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/wfzyx/von"><img src="https://external-preview.redd.it/VW75dC3ID5HFYYIWiSOP1LncNeZEjQCbaTdR9KcPGvI.png?auto=webp&amp;s=bb6e8f3dc6956150a4710c2fe60ee80968b33d3f" alt="Von" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/wfzyx/von">Von</a></b><br><sub>wfzyx · GitHub · ⭐ 381 · 2026-09-18</sub><br>约 395M 参数的开放非自回归决策模型，公开权重、训练代码和 System One 形态的 API，在本地几十毫秒内回答 Choice、Noul 和 Score 问题。<br><sub>相关: <a href="https://news.ycombinator.com/item?id=49781612">discussion</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://www.reddit.com/r/LocalLLM/comments/1wjv46i/i_have_created_open_source_jev_and_trained_it_to/"><img src="https://external-preview.redd.it/M3RzbGFlaGwyYnFoMXuP6V8vNBO5_YLg7eGU503KPrTQWjhN5GEpCDWeUnnY.png?format=pjpg&amp;auto=webp&amp;s=e22eb092e7b5afa83d5188c0b5e8e92e3dca3b1d" alt="Brain DOOM 决策策略" width="240"></a></td>
<td valign="top"><b><a href="https://www.reddit.com/r/LocalLLM/comments/1wjv46i/i_have_created_open_source_jev_and_trained_it_to/">Brain DOOM 决策策略</a></b><br><sub>mkschreder2 · Reddit · ▲ 119 · 2026-09-18</sub><br>本地运行的 Jev 式策略，实时玩 DOOM：冻结的 MiniLM 编码器读取观察文本，一个训练好的小型头部选择动作，每次决策 58.3 毫秒。<br><sub>相关: <a href="https://github.com/swedishembedded/brain/tree/main/samples/decision/doom">repo</a> · <a href="https://github.com/mkschreder/restful-doom">game-server</a> · <a href="https://github.com/swedishembedded/brain/tree/main/samples/decision/doom">project</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/0xLogicrw/status/2101545266507551141"><img src="https://pbs.twimg.com/media/HSowRg-W4AAdElX.jpg?name=orig" alt="OpenJEV 的四大流派" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/0xLogicrw/status/2101545266507551141">OpenJEV 的四大流派</a></b><br><sub>0xLogicrw · X · ♥ 233 · 2026-09-20</sub><br>中文对比 8 个开放的类 Jev 项目（SemIf、Simple Jev、Laya、Von、Verdict、Kev、Nimble、OpenJev），归为四种思路，并列出各自报告的准确率和延迟。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/nico-martin/open-jev"><img src="https://pbs.twimg.com/amplify_video_thumb/2101924588837896193/img/vb3r7XPYfWQwfrBV.jpg" alt="open-jev (nico-martin)" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/nico-martin/open-jev">open-jev (nico-martin)</a></b><br><sub>nico-martin · GitHub · ⭐ 19 · 2026-09-20</sub><br>面向浏览器的 TypeScript 库，通过 Transformers.js 在 WebGPU 或 WebAssembly 上于设备端运行 Kev 等开放的 Jev 形态类型化决策模型，为每个问题返回校准分布。<br><sub>相关: <a href="https://www.npmjs.com/package/open-jev">npm</a> · <a href="https://x.com/nicodotdev/status/2101925770432008665">demo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/razorback16/openjev"><img src="https://external-preview.redd.it/vdZrJPXw6MSvl0ZZRNggdJnJjOT14qhqZDKUAr_MuuE.png?auto=webp&amp;s=a01efcc5d87a9abbba518b4fcd3b7260501a06c4" alt="OpenJev" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/razorback16/openjev">OpenJev</a></b><br><sub>razorback16 · GitHub · ⭐ 287 · 2026-09-18</sub><br>开放的 System One 决策服务器，兼容 Jev 的通信 API，TypeSafe SDK 无需修改即可使用，通过 vLLM 或 MLX 从 DiffusionGemma 26B-A4B 的概率中读出类型化答案，也支持关于图像的问题。<br><sub>相关: <a href="https://codiv.ai">app</a> · <a href="https://www.reddit.com/r/LocalLLaMA/comments/1wjlyzr/still_on_the_jev_waitlist_i_hosted_openjev_its/">discussion</a> · <a href="https://codiv.ai">app 2</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Mapika/decider"><img src="https://opengraph.githubassets.com/1/Mapika/decider" alt="decider" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Mapika/decider">decider</a></b><br><sub>Mapika · GitHub · ⭐ 282 · 2026-09-16</sub><br>从 Qwen3.5 微调得到的开放 System One 式模型，包括一个 2B 模型和一个 35B 混合专家模型，一次前向传播为每个类型化问题返回概率分布，在十个文字游戏和 Super Mario Bros. 上做了演示。<br><sub>相关: <a href="https://huggingface.co/mapika/decider-2b">model</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/ekzhang/openjev-sglang"><img src="https://i.imgur.com/wHM3jxV.gif" alt="openjev-sglang" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/ekzhang/openjev-sglang">openjev-sglang</a></b><br><sub>ekzhang · GitHub · ⭐ 259 · 2026-09-17</sub><br>兼容端点，在 SGLang 上提供一个开放的混合专家（MoE）模型服务，附带 BoolQ 和 MMLU-Pro 对比。<br><sub>相关: <a href="https://www.reddit.com/r/typesafe/comments/1wmhbuu/ekzhangopenjevsglang_jevcompatible_api_endpoint/">discussion</a> · <a href="https://x.com/ekzhang1/status/2100651678110515383">demo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Heman10x-NGU/openJev-verdict-2.0"><img src="https://raw.githubusercontent.com/Heman10x-NGU/openJev-verdict-2.0/main/assets/v1.4/benchmark-leaderboard-chart.png" alt="openJev-verdict-2.0" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Heman10x-NGU/openJev-verdict-2.0">openJev-verdict-2.0</a></b><br><sub>Heman10x-NGU · GitHub · ⭐ 249 · 2026-09-19</sub><br>基于 ModernBERT 的 151M 非自回归决策模型，分布头和置信度头相互独立，公开权重，保存了评测产物，并有浏览器内 WebGPU 演示；其基准测试结果为自行报告。<br><sub>相关: <a href="https://www.reddit.com/r/typesafe/comments/1wm8avg/heman10xnguopenjevverdict20_calibrated_151m/">discussion</a> · <a href="https://heman10x-ngu.github.io/openJev-verdict-2.0/">docs</a> · <a href="https://heman10x-ngu.github.io/openJev-verdict-2.0">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Rizzo-AI-Academy/rizzo-flow"><img src="https://raw.githubusercontent.com/Rizzo-AI-Academy/rizzo-flow/main/assets/rizzo_flow_logo.png" alt="Rizzo Flow" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Rizzo-AI-Academy/rizzo-flow">Rizzo Flow</a></b><br><sub>Rizzo-AI-Academy · GitHub · ⭐ 240 · 2026-09-21</sub><br>本地开放模型决策服务器，读取答案 token 的概率而非生成文本，对外提供 Jev 兼容的 Choice、Score 和 Noul HTTP API，外加一个数值原语；不声称质量与 Jev 相当。<br><sub>相关: <a href="https://rizzo-ai-academy.github.io/rizzo-flow/">site</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/ruvnet/RuVector/tree/main/npm/packages/typesafe"><img src="https://repository-images.githubusercontent.com/1099547803/948d2495-1db9-47f6-9ea1-f7f977343e5f" alt="@ruvector/typesafe" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/ruvnet/RuVector/tree/main/npm/packages/typesafe">@ruvector/typesafe</a></b><br><sub>ruvnet · 软件包 · ⭐ 4.5k 仓库 · 2025-11-19</sub><br>基于句向量的本地、无需联网的类型化决策，接受 Jev 的 /v1/systemone 请求和响应格式，返回校准的置信度和弃权概率质量（abstain mass）。<br><sub><b>Jev 用法:</b> 原生 napi-rs 核心，带 WASM 回退；发布门槛要求 p95 在原生下为 50 毫秒、WASM 下为 150 毫秒。</sub><br><sub>相关: <a href="https://www.npmjs.com/package/@ruvector/typesafe">npm</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/hr98w/jev-visual"><img src="https://raw.githubusercontent.com/hr98w/jev-visual/main/docs/images/jev-visual-en.png" alt="Jev Visual" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/hr98w/jev-visual">Jev Visual</a></b><br><sub>hr98w · GitHub · ⭐ 224 · 2026-09-17</sub><br>Apple Silicon 上的教学用类 Jev 视觉推理：在 MLX 上运行的 Qwen3.5-0.8B 基于共享上下文和 logits 回答关于一张图片的选择、是/否和打分问题，附分拣工厂、Breakout 和手势演示。<br><sub>相关: <a href="https://x.com/hr98w/status/2100646513412292873">demo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://www.reddit.com/r/MachineLearning/comments/1wl13eu/programasweights_compile_english_function/"><img src="https://preview.redd.it/a5zxim8w8kqh1.png?width=2122&amp;format=png&amp;auto=webp&amp;s=c009655b083bddd316687c2fdef0365c9334c82e" alt="ProgramAsWeights" width="240"></a></td>
<td valign="top"><b><a href="https://www.reddit.com/r/MachineLearning/comments/1wl13eu/programasweights_compile_english_function/">ProgramAsWeights</a></b><br><sub>yuntiandeng · Reddit · ▲ 74 · 2026-09-19</sub><br>研究项目：把一段英文函数描述编译成冻结 Qwen3-0.6B 的 LoRA adapter，得到可在 CPU 上运行、无需 API 的本地文本分类器。<br><sub>相关: <a href="https://github.com/programasweights/programasweights-python">repo</a> · <a href="https://huggingface.co/programasweights/models">models</a> · <a href="https://github.com/programasweights/programasweights-python">project</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/AstroHanRay/status/2101709185155231895"><img src="https://pbs.twimg.com/media/HSrFNeXbEAArB6H.jpg?name=orig" alt="训练你自己的类 Jev 模型" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/AstroHanRay/status/2101709185155231895">训练你自己的类 Jev 模型</a></b><br><sub>AstroHanRay · X · ♥ 132 · 2026-09-20</sub><br>在 Qwen3.5-4B 加 rank-8 LoRA 上用 RLCD 训练 Jev 风格判断模型（32K 个问题、9 GPU 小时、约 $42），在 120 题的 JevBench 上与 Jev 打平。<br><sub>相关: <a href="https://huggingface.co/AstroHan/decision-head-qwen3.5-4b-rlcd-32k">model</a> · <a href="https://huggingface.co/astrohan/decision-head-qwen3.5-4b-rlcd-32k">project</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/logan-markewich/jeff"><img src="https://opengraph.githubassets.com/1/logan-markewich/jeff" alt="Jeff" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/logan-markewich/jeff">Jeff</a></b><br><sub>logan-markewich · GitHub · ⭐ 206 · 2026-09-19</sub><br>基于 400M 参数编码器的兼容服务器，附与 Jev 的基准对比。<br><sub>相关: <a href="https://x.com/LoganMarkewich/status/2101142971223781587">demo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/receptron/laya"><img src="https://opengraph.githubassets.com/1/receptron/laya" alt="@receptron/laya" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/receptron/laya">@receptron/laya</a></b><br><sub>receptron · GitHub · ⭐ 205 · 2026-09-19</sub><br>Node.js 和 TypeScript 包，通过 ONNX Runtime 运行 Convai Innovations 推出的开放、兼容 Jev 的决策模型 Laya，一次前向传播就返回 choice、score 和 noul 答案。<br><sub>相关: <a href="https://www.npmjs.com/package/@receptron/laya">npm</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/zhilinjerrywag/status/2101962974898397246"><img src="https://pbs.twimg.com/media/HSurH4YWYAESh8q.jpg" alt="Mev" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/zhilinjerrywag/status/2101962974898397246">Mev</a></b><br><sub>zhilinjerrywag · 文章 · ♥ 38 · 2026-09-21</sub><br>用于职位与候选人匹配的 0.4B 参数决策模型，基于 Laya 微调约 45 分钟；它与 Kev-4B 打平（Spearman 0.733 对 0.730），但 Jev 仍以 0.818 排名第一。<br><sub><b>Jev 用法:</b> 接口与 Jev 相同：用一个 Noul 判断是否推荐，用五级 Score 评估匹配强度，并与零样本的 Jev 做对比。</sub><br><sub>相关: <a href="https://github.com/NandhaKishorM/laya">base-model</a> · <a href="https://metix.ai/">company</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://www.youtube.com/watch?v=JsVM4vgspEU"><img src="https://i.ytimg.com/vi/JsVM4vgspEU/hqdefault.jpg" alt="我免费做了一个 Jev" width="240"></a></td>
<td valign="top"><b><a href="https://www.youtube.com/watch?v=JsVM4vgspEU">我免费做了一个 Jev</a></b><br><sub>Micah · 视频 · ♥ 129 · 2026-09-19</sub><br>在一张 RTX 5090 上用 27B 老师模型蒸馏 Qwen3 0.6B，做出一个免费的 Jev 式模型，再通过 ViZDoom 玩 Doom；与老师模型的一致率从 54% 升到 93%。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/NotXf1le/choosekit"><img src="https://raw.githubusercontent.com/NotXf1le/choosekit/master/benchmarks/supergpqa-benchmark.svg" alt="choosekit" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/NotXf1le/choosekit">choosekit</a></b><br><sub>NotXf1le · GitHub · ⭐ 18 · 2026-09-19</sub><br>库，用 llama.cpp、Ollama 或 OpenRouter 模型给有限的选项集合打分，返回带概率分布的类型化决策，另有一个 MCP 服务器和对比 Jev 1.13 的 SuperGPQA 基准测试。<br><sub>相关: <a href="https://www.reddit.com/r/LLMDevs/comments/1wkc9hp/i_tried_jevstyle_decisions_with_local_qwen_same/">discussion</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/mmastrac/djev-spark"><img src="https://raw.githubusercontent.com/mmastrac/djev-spark/main/docs/playground.jpg" alt="djev-spark" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/mmastrac/djev-spark">djev-spark</a></b><br><sub>mmastrac · GitHub · ⭐ 169 · 2026-09-18</sub><br>容器配方，在 DGX Spark 上以 NVFP4 精度部署 DiffusionGemma 26B-A4B，对外提供 Jev 的 /v1/systemone API，把打过补丁的 vLLM 结构化读取与一个独立的决策服务器配合使用。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/kunpengtalk/OmniStudio"><img src="https://raw.githubusercontent.com/kunpengtalk/OmniStudio/main/docs/images/screenshot-jev.png" alt="OmniStudio 的 JEV 判断功能" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/kunpengtalk/OmniStudio">OmniStudio 的 JEV 判断功能</a></b><br><sub>kunpengtalk · GitHub · ⭐ 147 · 2026-09-09</sub><br>本地优先的桌面 LLM 工作台，其中的 JEV 类型化判断页面可通过 laya-mlx 在本地运行 Laya，也可连接云端，并暴露兼容 TypeSafe 的端点供官方 SDK 使用。<br><sub><b>Jev 用法:</b> 返回带概率分布的 Noul、Choice 和 Score 答案；SDK 只需修改 TYPESAFE_BASE_URL 和 TYPESAFE_API_KEY。</sub><br><sub>相关: <a href="https://omnilabs.vibeadmin.cn/#/omnistudio">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/yoheinakajima/glance"><img src="https://pbs.twimg.com/amplify_video_thumb/2102213606414921728/img/cLKQS-9p31mko41V.jpg" alt="Glance" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/yoheinakajima/glance">Glance</a></b><br><sub>yoheinakajima · GitHub · ⭐ 7 · 2026-09-21</sub><br>一个 harness，用于向开放的视觉语言模型（默认 Qwen3-VL-4B）就一张图片提出类型化的是/否、单选和评分问题，从一次前向传播中读取校准概率，请求格式仿照 Jev。<br><sub>相关: <a href="https://glance.yohei.me">app</a> · <a href="https://x.com/yoheinakajima/status/2102213665361690906">demo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Yinsongxu/LLM2Jev"><img src="https://raw.githubusercontent.com/Yinsongxu/LLM2Jev/main/assets/llm2jev-banner.jpeg" alt="LLM2Jev" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Yinsongxu/LLM2Jev">LLM2Jev</a></b><br><sub>Yinsongxu · GitHub · ⭐ 126 · 2026-09-19</sub><br>把本地语言模型变成 Jev 风格决策引擎的工具包，通过 Transformers 或 SGLang 从 prefill logits 中读取 Choice、Score 和 Noul 答案，提供 /v1/systemone 端点并支持图像输入。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/kshetrajna12/reflex"><img src="https://opengraph.githubassets.com/1/kshetrajna12/reflex" alt="reflex" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/kshetrajna12/reflex">reflex</a></b><br><sub>kshetrajna12 · GitHub · ⭐ 110 · 2026-09-17</sub><br>基于原版 Qwen3.5 的开放 Jev 复刻，在 /v1/systemone 服务器后用一次批处理前向回答 Choice、Score 和 Noul 问题，附带 WebGPU 演示和用于得到可信概率的 LoRA 配方；每次请求约 200 毫秒。<br><sub>相关: <a href="https://kshetrajna12.github.io/reflex">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/sabeel111/OpenSourceJev"><img src="https://external-preview.redd.it/NGQzMnA1dW4yaHFoMfp6xNCARVGeYVpoP66WhgS8I5hNmzYWXyIRArIESs6K.png?format=pjpg&amp;auto=webp&amp;s=2d4092332a97f0aebb7b7e82f599bf681e05877f" alt="OpenSourceJev" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/sabeel111/OpenSourceJev">OpenSourceJev</a></b><br><sub>sabeel111 · GitHub · ⭐ 24 · 2026-09-19</sub><br>研究实验：基于 llama.cpp 和 Qwen 运行本地 System One 风格决策引擎，把下一个 token 的 logits 投影到答案选项上，在消费级硬件上做校准的类型化决策。<br><sub>相关: <a href="https://www.reddit.com/r/LocalLLM/comments/1wkl8c9/my_version_of_jev_running_locally_playing_doom/">discussion</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/daseinlabs/open-jev"><img src="https://raw.githubusercontent.com/daseinlabs/open-jev/main/docs/media/doom-recording.gif" alt="openjev (daseinlabs)" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/daseinlabs/open-jev">openjev (daseinlabs)</a></b><br><sub>daseinlabs · GitHub · ⭐ 94 · 2026-09-17</sub><br>单次前向的选项打分器，在 Apple Silicon 上通过 MLX 运行本地 Gemma 3 4B：上下文只 prefill 一次，一次前向传播给所有选项打分，并提供兼容 System One 的端点。<br><sub><b>Jev 用法:</b> 记录了零样本下的过度自信问题，并提供可选的按任务微调。</sub><br><sub>相关: <a href="https://news.ycombinator.com/item?id=49737236">demo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Davipar/djev-dev"><img src="https://raw.githubusercontent.com/Davipar/djev-dev/main/docs/assets/djev-dev-cover.png" alt="djev dev" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Davipar/djev-dev">djev dev</a></b><br><sub>Davipar · GitHub · ⭐ 93 · 2026-09-19</sub><br>基于 DiffusionGemma 和 vLLM 的类型化决策开放实现，从去噪后的答案位置读取标签概率，支持图像输入、图像选项和实时摄像头采样。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/theoleecj/status/2100212661619503176"><img src="https://pbs.twimg.com/amplify_video_thumb/2100211213582143488/img/Bzldvxr0IbvhDHAw.jpg" alt="OpenJev" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/theoleecj/status/2100212661619503176">OpenJev</a></b><br><sub>theoleecj · X · ♥ 15 · 2026-09-16</sub><br>Jev 风格带概率类型化决策的开源设备端推理，基于 Qwen 3 4B、0.6B 和 0.8B，能在 Chrome 中运行。<br><sub>相关: <a href="https://github.com/theoleecj/openjev">repo</a> · <a href="https://openjev.com">app</a> · <a href="https://github.com/theoleecj/openjev">project</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Heman10x-NGU/Verdict-open-jev"><img src="https://raw.githubusercontent.com/Heman10x-NGU/Verdict-open-jev/main/assets/v1.4/benchmark-leaderboard-chart.png" alt="OpenJev (Verdict)" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Heman10x-NGU/Verdict-open-jev">OpenJev (Verdict)</a></b><br><sub>Heman10x-NGU · GitHub · ⭐ 67 · 2026-09-17</sub><br>受 Jev 和 RLCD 启发的开放 151M 参数 ModernBERT 决策引擎，一次非自回归前向可在 35 毫秒 内评估类型化问题，附带 JevBench 审计和浏览器内的 WebGPU playground。<br><sub>相关: <a href="https://huggingface.co/heman10x/rlcd-modernbert-151m">huggingface</a> · <a href="https://huggingface.co/heman10x/rlcd-modernbert-151m">model</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/deepopen-com/deepopen"><img src="https://raw.githubusercontent.com/deepopen-com/deepopen/main/%E6%89%93%E6%A6%9C.png" alt="DeepOpen" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/deepopen-com/deepopen">DeepOpen</a></b><br><sub>deepopen-com · GitHub · ⭐ 59 · 2026-09-21</sub><br>基于 Laya 的开放 System 1 决策引擎，附中文技术白皮书，有一个按文字/语言在英文、多语言和类型化决策检查点之间分流的路由器，并在 CLINC150 和 Banking77 上做了训练实验。<br><sub><b>Jev 用法:</b> 一次非自回归计算回答类型化的 Choice/Score/Noul 问题；报告在 T4 上每次请求 33 毫秒。</sub><br><sub>相关: <a href="https://deepopen.com">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/shi3z/deepseekv4.1-A100-custom"><img src="https://raw.githubusercontent.com/shi3z/deepseekv4.1-A100-custom/main/assets/dashboard.jpg" alt="DeepSeek-V4.1 A100 Jev 模式" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/shi3z/deepseekv4.1-A100-custom">DeepSeek-V4.1 A100 Jev 模式</a></b><br><sub>shi3z · GitHub · ⭐ 54 · 2026-09-11</sub><br>面向 A100 GPU 的定制 DeepSeek-V4.1-Flash 运行时，带一个 Jev Mode，并行给候选打分而不是解码 JSON，报告在 30 字段提取上最高提速 2,854 倍，耗时 24 毫秒。<br><sub><b>Jev 用法:</b> 非自回归的候选对数概率打分，配合常驻 GPU 的前缀树；附一个对比官方 Jev 与本地模式的脚本。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/bnsd55/jevmlx"><img src="https://opengraph.githubassets.com/1/bnsd55/jevmlx" alt="jevmlx" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/bnsd55/jevmlx">jevmlx</a></b><br><sub>bnsd55 · GitHub · ⭐ 54 · 2026-09-17</sub><br>面向 Apple Silicon 的本地 Jev 式决策层，一次 prefill 就用 MLX 模型的 logits 给 boolean、enum 和多选字段的每个允许选项打分，返回符合 schema 的 JSON 及各字段概率。<br><sub><b>Jev 用法:</b> 提供兼容 System One 的端点和基准测试运行器。</sub><br><sub>相关: <a href="https://news.ycombinator.com/item?id=49743108">discussion</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://www.reddit.com/r/LocalLLM/comments/1wkrk48/laya_vision_is_open_source_jev_for_images/"><img src="https://external-preview.redd.it/UtFOem1Lybo3LMdOVLun0w9gD1TIz-RsVEPJK1E931Q.png?auto=webp&amp;s=b4618d2ffc0db450df912f1f3046530e58b7384b" alt="Laya Vision" width="240"></a></td>
<td valign="top"><b><a href="https://www.reddit.com/r/LocalLLM/comments/1wkrk48/laya_vision_is_open_source_jev_for_images/">Laya Vision</a></b><br><sub>Fickle-Ad-866 · Reddit · ▲ 18 · 2026-09-19</sub><br>基于 SmolVLM 256M 的开放 Jev 式图像决策模型，针对截图、照片和 GUI 元素，在一组固定选项上返回概率。<br><sub>相关: <a href="https://huggingface.co/thaitea/laya-vision-smolvlm-256m">model</a> · <a href="https://huggingface.co/thaitea/laya-vision-smolvlm-256m">project</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://huggingface.co/com-kotobalabs/open-jev-deberta-v3-large"><img src="https://cdn-thumbnails.huggingface.co/social-thumbnails/models/com-kotobalabs/open-jev-deberta-v3-large.png" alt="open-jev-deberta-v3-large" width="240"></a></td>
<td valign="top"><b><a href="https://huggingface.co/com-kotobalabs/open-jev-deberta-v3-large">open-jev-deberta-v3-large</a></b><br><sub>com-kotobalabs · Hugging Face · ♥ 52 · 2026-09-18</sub><br>基于 DeBERTa-v3-large 的开放 Jev 形态模型，一次前向即可回答关于同一 state 的任意数量 choice、score 和 noul 问题；域内准确率 0.854，域外 0.690，10 个问题耗时 28 毫秒。<br><sub>相关: <a href="https://github.com/kotoba-lang/typed-decisions">repo</a> · <a href="https://huggingface.co/onnx-community/open-jev-deberta-v3-large-ONNX">model</a> · <a href="https://huggingface.co/spaces/hugging-apps/open-jev-deberta-v3-large-demo">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/deepanwadhwa/OpenDecision"><img src="https://opengraph.githubassets.com/1/deepanwadhwa/OpenDecision" alt="OpenDecision" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/deepanwadhwa/OpenDecision">OpenDecision</a></b><br><sub>deepanwadhwa · GitHub · ⭐ 52 · 2026-09-17</sub><br>仿照 Jev 的开源本地语义决策引擎，可针对结构化 state 和文档回答 Choice、Noul 和 Score 问题，外加判断支持/矛盾（supports/contradicts）的 Relation，演示中用它玩 Doom。<br><sub>相关: <a href="https://deepanwadhwa.github.io/OpenDecision/">link</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/ikermoel/open-alternative-jev"><img src="https://raw.githubusercontent.com/ikermoel/open-alternative-jev/main/benchmarks/figures/race.png" alt="Open Alternative to Jev" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/ikermoel/open-alternative-jev">Open Alternative to Jev</a></b><br><sub>ikermoel · GitHub · ⭐ 47 · 2026-09-18</sub><br>Python 库，通过 Transformers 或 vLLM 从开放权重模型中读取选项 token 概率，一次给出类型化、校准的 Choice、Score 和 Noul 决策，支持温度缩放并附带基准测试。<br><sub>相关: <a href="https://news.ycombinator.com/item?id=49750584">discussion</a> · <a href="https://huggingface.co/spaces/IkerMoel/open-alternative-jev">app</a> · <a href="https://huggingface.co/spaces/IkerMoel/open-alternative-jev">app 2</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/SAGAR-TAMANG/sarvam-jev"><img src="https://opengraph.githubassets.com/1/SAGAR-TAMANG/sarvam-jev" alt="sarvam-jev" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/SAGAR-TAMANG/sarvam-jev">sarvam-jev</a></b><br><sub>SAGAR-TAMANG · GitHub · ⭐ 46 · 2026-09-18</sub><br>基于 Sarvam 印度语言模型 sarvam-1 的开放 Jev 风格推理引擎，从字母选项的 logits 读取类型化答案而非生成 JSON，多个问题复用同一次 state prefill，可在浏览器中运行。<br><sub>相关: <a href="https://sarvam-jev.feynmanpi.com/">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://www.reddit.com/r/LocalLLaMA/comments/1wle746/a_local_jevstyle_decision_head_onto_qwen_25_15b/"><img src="https://external-preview.redd.it/Wnrv8UVeht99poU3UQZOPTnOFzLoeyTHKvwoGiakktY.png?auto=webp&amp;s=8ff20f37c26e39ed193b6ae02021c976d1429eda" alt="AES" width="240"></a></td>
<td valign="top"><b><a href="https://www.reddit.com/r/LocalLLaMA/comments/1wle746/a_local_jevstyle_decision_head_onto_qwen_25_15b/">AES</a></b><br><sub>CryOrganic8886 · Reddit · ▲ 15 · 2026-09-20</sub><br>在 Qwen2.5-1.5B-Instruct 上做的概念验证决策头，只跑一次 prefill，用 FP32 SwiGLU 探针和向量相似度给候选答案打分，而不是生成 token。<br><sub><b>Jev 用法:</b> 在开放权重上本地复刻 Noul、Choice 和 Score 式的输出。</sub><br><sub>相关: <a href="https://huggingface.co/Brinij/aes">model</a> · <a href="https://huggingface.co/brinij/aes">project</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/r-ms/mini-jev"><img src="https://raw.githubusercontent.com/r-ms/mini-jev/main/docs/figures/accuracy_by_k.svg" alt="mini-Jev" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/r-ms/mini-jev">mini-Jev</a></b><br><sub>r-ms · GitHub · ⭐ 42 · 2026-09-17</sub><br>预注册实验：在冻结的 Qwen3-4B 上实现 Jev 风格的类型化决策接口，把 schema 字段转成字母选项题，一次读取选项字母的 logits，并与语法约束 JSON 做对比。<br><sub>相关: <a href="https://news.ycombinator.com/item?id=49748643">discussion</a> · <a href="https://huggingface.co/datasets/Mikhail/mini-jev-runs">model</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://huggingface.co/DoccyHealth/Solomon"><img src="https://cdn-thumbnails.huggingface.co/social-thumbnails/models/DoccyHealth/Solomon.png" alt="Solomon" width="240"></a></td>
<td valign="top"><b><a href="https://huggingface.co/DoccyHealth/Solomon">Solomon</a></b><br><sub>Doccy (Archer Hume) · Hugging Face · ♥ 42 · 2026-09-21</sub><br>Qwen3.8-27B 的 LoRA adapter 和训练好的答案头，把一份文档加结构化问题转成每个决策一个概率，并指向支撑判断的句子，不生成文本。<br><sub>相关: <a href="https://archerhume.com/posts/jevs-architecture-unmasked">post</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/snellingio/system-one"><img src="https://raw.githubusercontent.com/snellingio/system-one/main/docs/assets/how-system-one-lite-works-v3.png" alt="System One Lite" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/snellingio/system-one">System One Lite</a></b><br><sub>snellingio · GitHub · ⭐ 41 · 2026-09-16</sub><br>用本地语言模型做约束决策的概念验证 HTTP 服务，通过读取固定答案位置上的分数来回答声明好的 Choice、Score 和 Noul 问题，不做生成。<br><sub>相关: <a href="https://news.ycombinator.com/item?id=49727643">discussion</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/lkarlslund/laya.cpp"><img src="https://external-preview.redd.it/cuDWXinMwBubvEi2uiDGctxhmXkdqtLzEbHzFCRaYOE.png?auto=webp&amp;s=f6c0009f9fb9794743802edd125c55efc41d42f3" alt="laya.cpp" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/lkarlslund/laya.cpp">laya.cpp</a></b><br><sub>lkarlslund · GitHub · ⭐ 40 · 2026-09-20</sub><br>基于 ggml 的 Jev 式 Laya 类型化决策模型独立 C++ 推理实现，带有针对 NVIDIA RTX GPU 优化的 CUDA kernel 和 Vulkan FP32 后端，覆盖 english、multilingual 和 typed-decisions 三个检查点。<br><sub>相关: <a href="https://www.reddit.com/r/LocalLLaMA/comments/1wlmkm9/layacpp_optimized_laya_nearinstant_decision_making/">demo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/intikhab49/open-jev-typed-decision-engine"><img src="https://raw.githubusercontent.com/intikhab49/open-jev-typed-decision-engine/main/docs/header.svg" alt="Open Jev typed decision engine" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/intikhab49/open-jev-typed-decision-engine">Open Jev typed decision engine</a></b><br><sub>intikhab49 · GitHub · ⭐ 39 · 2026-09-19</sub><br>150M 参数编码器实现的开放 Jev 复刻，一次非自回归前向即可回答 noul、choice 和 score 问题，得分 0.697（Jev 为 0.727），在 Colab T4 上 30 分钟即可训练完成。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/iapp-technology/openthai-systemone"><img src="https://raw.githubusercontent.com/iapp-technology/openthai-systemone/main/docs/assets/fb_launch_v3_1x1.png" alt="OpenThai-SystemOne" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/iapp-technology/openthai-systemone">OpenThai-SystemOne</a></b><br><sub>iapp-technology · GitHub · ⭐ 38 · 2026-09-20</sub><br>开放的泰语和英语 System One 模型，由 Qwen3.5-0.8B 主干加 256 路 slot head 构成，遵循 TypeSafe 的 /v1/systemone 约定，一次前向回答 choice、score 和 noul 问题。<br><sub>相关: <a href="https://www.reddit.com/r/LocalLLM/comments/1wlkjk8/i_trained_an_open_08b_system_one_decision_model/">discussion</a> · <a href="https://huggingface.co/iapp/OpenThai-SystemOne">model</a> · <a href="https://huggingface.co/iapp/OpenThai-SystemOne">model 2</a> · <a href="https://huggingface.co/spaces/hugging-apps/openthai-systemone-demo">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/zhengxuyu/litjev"><img src="https://opengraph.githubassets.com/1/zhengxuyu/litjev" alt="LitJev" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/zhengxuyu/litjev">LitJev</a></b><br><sub>zhengxuyu · GitHub · ⭐ 37 · 2026-09-17</sub><br>基于假设的 Jev 决策层复现，通过从输出头读取选项分数，把现成的 Qwen checkpoint 变成类型化的 Choice、Score 和 Noul 端点，附带 API 和浏览器前端。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/TypeLLM/TypeLLM"><img src="https://github.com/user-attachments/assets/b1f2dbc6-21b7-4222-a0fb-dacfe1650797" alt="TypeLLM" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/TypeLLM/TypeLLM">TypeLLM</a></b><br><sub>TypeLLM · GitHub · ⭐ 37 · 2026-09-17</sub><br>受 Jev 启发的 SGLang 扩展，让开放的自回归 LLM 按 JSON Schema 输出类型化结果（string、integer、number、boolean、enum），支持单 token 选项、共享前缀 KV 复用和依赖图。<br><sub>相关: <a href="https://typellm.ai">homepage</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://huggingface.co/spaces/pngwn/open-jev"><img src="https://cdn-thumbnails.huggingface.co/social-thumbnails/spaces/pngwn/open-jev.png" alt="Open Jev" width="240"></a></td>
<td valign="top"><b><a href="https://huggingface.co/spaces/pngwn/open-jev">Open Jev</a></b><br><sub>pngwn · 应用 · ♥ 35 · 2026-09-17</sub><br>基于 Qwen3.5-4B LoRA 打分器的 Hugging Face Space，对调用方给出的选项输出经温度缩放的概率来回答类型化问题，state 只编码一次，并行做出决策。<br><sub>相关: <a href="https://huggingface.co/pngwn/system-one-qwen3.5-4b-scorer">model</a> · <a href="https://huggingface.co/pngwn/system-one-qwen3.5-4b-scorer-v2b">model_v2b</a> · <a href="https://huggingface.co/datasets/pngwn/open-jev-laya-bench">model 2</a> · <a href="https://huggingface.co/datasets/pngwn/typed-decisions-v2-system-one">model 3</a> · <a href="https://huggingface.co/pngwn/system-one-qwen3.5-4b-scorer-v2b">model 4</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/taeold/djev-run"><img src="https://github.com/user-attachments/assets/2e9a5321-f8a9-4734-b6f2-4d6f47193390" alt="djev-run" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/taeold/djev-run">djev-run</a></b><br><sub>taeold · GitHub · ⭐ 32 · 2026-09-20</sub><br>部署配方，在 Google Cloud Run 上用 RTX PRO 6000 Blackwell GPU 部署 DiffusionGemma-Jev，对外提供兼容 TypeSafe 的 API，另附一个零依赖的贪吃蛇演示，直接从浏览器调用它。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://huggingface.co/spaces/drinkmoonshine/parallel-constrained-decoding"><img src="https://cdn-thumbnails.huggingface.co/social-thumbnails/spaces/drinkmoonshine/parallel-constrained-decoding.png" alt="Parallel Constrained Decision Engine" width="240"></a></td>
<td valign="top"><b><a href="https://huggingface.co/spaces/drinkmoonshine/parallel-constrained-decoding">Parallel Constrained Decision Engine</a></b><br><sub>drinkmoonshine · 应用 · ♥ 31 · 2026-09-16</sub><br>并行约束解码的 Gradio 演示，在 Apple Silicon 上基于 Qwen2.5-1.5B 一次填完多字段 JSON 决策 schema，定位为 Jev 的开放替代品。<br><sub>相关: <a href="https://news.ycombinator.com/item?id=49734345">discussion</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/zhihz/openjev"><img src="https://raw.githubusercontent.com/zhihz/openjev/main/docs/images/demo-en.png" alt="Open JEV" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/zhihz/openjev">Open JEV</a></b><br><sub>zhihz · GitHub · ⭐ 29 · 2026-09-16</sub><br>受 Jev 启发的研究预览版，在本地针对上下文、问题和候选答案做中英双语概率决策，目前后端是冻结的 Qwen3-4B-Instruct，并附带 Web 界面。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/KaLM-Embedding/KaLM-Jev"><img src="https://opengraph.githubassets.com/1/KaLM-Embedding/KaLM-Jev" alt="KaLM-Jev" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/KaLM-Embedding/KaLM-Jev">KaLM-Jev</a></b><br><sub>KaLM-Embedding · GitHub · ⭐ 28 · 2026-09-21</sub><br>基于 KaLM-Reranker-V1-R2 检查点（Nano、Small、Large 三种尺寸）的本地 Choice、Score 和 Noul 判断服务，返回结构化判断而不生成答案文本。<br><sub>相关: <a href="https://huggingface.co/spaces/Yuki131/KaLM-Jev">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/IamBusy/OpenJev-Vision"><img src="https://raw.githubusercontent.com/IamBusy/OpenJev-Vision/main/reports/vision-v01/demo.png" alt="OpenJev-Vision" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/IamBusy/OpenJev-Vision">OpenJev-Vision</a></b><br><sub>IamBusy · GitHub · ⭐ 28 · 2026-09-19</sub><br>面向视觉概率决策的开放研究工具包，图像只编码一次，基于共享概率回答多个结构化问题，附带合成数据、Oxford-IIIT Pet 和 CLEVR 数据以及训练好的权重。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/mithalouni/system-one-open"><img src="https://opengraph.githubassets.com/1/mithalouni/system-one-open" alt="system-one-open" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/mithalouni/system-one-open">system-one-open</a></b><br><sub>mithalouni · GitHub · ⭐ 28 · 2026-09-17</sub><br>基于 Gemma 4 E2B（attention LoRA）和 Gemma 3 270M 的开放 Jev 风格决策模型，在 Modal 上训练和部署；在 TypeSafe 公开评测的严格子集上报告 76.7%，Jev 为 86.9%。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/leesk212/JEV-CPU"><img src="https://raw.githubusercontent.com/leesk212/JEV-CPU/main/assets/jev-cpu-demo.gif" alt="JEV-CPU" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/leesk212/JEV-CPU">JEV-CPU</a></b><br><sub>leesk212 · GitHub · ⭐ 12 · 2026-09-19</sub><br>SemIf 的 CPU 移植版，带 Web UI，约 1 s 内从 Qwen3-0.6B 的 logits 读出类型化选项概率，涵盖内容审核、事故严重程度和信用风险等八个领域。<br><sub>相关: <a href="https://leesk212.github.io/JEV-CPU/">app</a> · <a href="https://huggingface.co/Meanblock/JEV-CPU">model</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/fidecastro/jevify"><img src="https://opengraph.githubassets.com/1/fidecastro/jevify" alt="jevify (fidecastro)" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/fidecastro/jevify">jevify (fidecastro)</a></b><br><sub>fidecastro · GitHub · ⭐ 25 · 2026-09-19</sub><br>适配器，把任何在 OpenAI 兼容端点后提供 logprobs 的模型，或一个进程内的小模型，包装成类 Jev 端点：从下一个 token 的分布中读出类型化答案，按 Jev 的 API 格式返回。<br><sub>相关: <a href="https://www.reddit.com/r/OpenSourceeAI/comments/1wl9m9n/jevify_super_simple_way_to_serve_llms_as_a/">discussion</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/zeredy879/minojev"><img src="https://raw.githubusercontent.com/zeredy879/minojev/main/assets/banner.svg" alt="minojev" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/zeredy879/minojev">minojev</a></b><br><sub>zeredy879 · GitHub · ⭐ 25 · 2026-09-18</sub><br>冻结语言模型并训练小型决策头的库，一次前向传播即可从隐藏状态读出类型化、校准的选项、布尔值和分数分布，在笔记本 CPU 上就能复现。<br><sub>相关: <a href="https://zeredy879.github.io/minojev/">docs</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/sgoedecke/system-one"><img src="https://opengraph.githubassets.com/1/sgoedecke/system-one" alt="System One" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/sgoedecke/system-one">System One</a></b><br><sub>sgoedecke · GitHub · ⭐ 25 · 2026-09-17</sub><br>极简代码，通过批量单 token 选项推理把任意开放 LLM 变成 Jev 风格、兼容 typesafe-sdk 的分类器；用 Qwen3-8B 玩 Doom 每个动作 172 毫秒，而用工具调用要 600 毫秒。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/AndrewPrifer/jimothy"><img src="https://github.com/user-attachments/assets/b0781bef-61ab-47e5-96c6-2c034ad5cae3" alt="Jimothy" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/AndrewPrifer/jimothy">Jimothy</a></b><br><sub>AndrewPrifer · GitHub · ⭐ 24 · 2026-09-20</sub><br>把 Jev 的答案蒸馏成可在浏览器或 Node.js 中运行的小型快速本地分类器，提供校准概率和推荐的截断阈值。<br><sub><b>Jev 用法:</b> 通过 AI Gateway 调用的 Jev 充当老师：它在无标签数据行上缓存的答案成为 MiniLM 或 TF-IDF 学生分类器的训练数据。</sub><br><sub>相关: <a href="https://x.com/AndrewPrifer/status/2102162296739099126">demo</a> · <a href="https://jimothy-r63s.vercel.app">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/rorshopping/jev-on-a-laptop"><img src="https://opengraph.githubassets.com/1/rorshopping/jev-on-a-laptop" alt="jev-on-a-laptop" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/rorshopping/jev-on-a-laptop">jev-on-a-laptop</a></b><br><sub>rorshopping · GitHub · ⭐ 23 · 2026-09-16</sub><br>非官方研究，在 Apple Silicon 笔记本上用原版 Qwen 1.5B-8B 模型复现 Jev 式并行约束解码，其中 7B 的一致率达到 73.8%，Jev 为 86.6%，每次决策 0.4-2 s。<br><sub><b>Jev 用法:</b> 只 prefill 一次，在一次前向传播中评估所有类型化字段；发现置信度并不能可靠地标出错误。</sub><br><sub>相关: <a href="https://huggingface.co/spaces/rorshopping/parallel-constrained-decisions">demo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/karminski/Jev-Quantum"><img src="https://raw.githubusercontent.com/karminski/Jev-Quantum/main/assets/images/cover.png" alt="Jev Quantum" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/karminski/Jev-Quantum">Jev Quantum</a></b><br><sub>karminski · GitHub · ⭐ 22 · 2026-09-21</sub><br>用 Rust 写的、兼容 Jev 协议的随机基线，支持 noul、choice 和 score，但会忽略提示词，用快速伪随机数生成器作答，可在 agent 路由评测中用作 mock 或下限。<br><sub>相关: <a href="https://x.com/karminski3/status/2101941770003361893">demo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://huggingface.co/notnotsamuel/LFM2.5-350M-RLCD"><img src="https://cdn-thumbnails.huggingface.co/social-thumbnails/models/notnotsamuel/LFM2.5-350M-RLCD.png" alt="LFM2.5-350M-RLCD" width="240"></a></td>
<td valign="top"><b><a href="https://huggingface.co/notnotsamuel/LFM2.5-350M-RLCD">LFM2.5-350M-RLCD</a></b><br><sub>notnotsamuel · Hugging Face · ♥ 22 · 2026-09-16</sub><br>仅推理的并行结构化解码，基于未改动的 Liquid LFM2.5-350M 权重，通过分叉 attention 和卷积状态来批量为允许值打分，速度快 8-63 倍，字段准确率约 60%。<br><sub>相关: <a href="https://huggingface.co/monotykamary/LFM2.5-2.6B-RLCD">related</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/r33drichards/laya-vision"><img src="https://opengraph.githubassets.com/1/r33drichards/laya-vision" alt="Laya Vision" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/r33drichards/laya-vision">Laya Vision</a></b><br><sub>r33drichards · GitHub · ⭐ 21 · 2026-09-19</sub><br>开放 Laya 模型的研究分支，把文本编码器换成 SmolVLM-256M，这样一次前向传播就能根据图像加可选文本读出类型化的 choice、score 和 noul 决策。<br><sub>相关: <a href="https://news.ycombinator.com/item?id=49767430">discussion</a> · <a href="https://huggingface.co/thaitea/laya-vision-smolvlm-256m">model</a> · <a href="https://huggingface.co/spaces/thaitea/laya-vision-demo">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/JoshuaSP/open-jev"><img src="https://raw.githubusercontent.com/JoshuaSP/open-jev/main/assets/json-canvas.png" alt="open-jev (DiffusionGemma)" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/JoshuaSP/open-jev">open-jev (DiffusionGemma)</a></b><br><sub>JoshuaSP · GitHub · ⭐ 21 · 2026-09-16</sub><br>用 DiffusionGemma 26B-A4B 扩散模型做类型化 JSON 决策的实验性 harness：先自由去噪，再选出可能性最高的允许 token，并在 Every 的 TypeSafe lab 任务上做了基准测试。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/OmniJev/PlayJev"><img src="https://raw.githubusercontent.com/OmniJev/PlayJev/main/docs/assets/board.webp" alt="PlayJev" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/OmniJev/PlayJev">PlayJev</a></b><br><sub>OmniJev · GitHub · ⭐ 21 · 2026-09-17</sub><br>把 Qwen3.5-0.8B 微调成类 Jev 的多模态模型，从原始像素玩十款浏览器游戏：输入一帧、输出一步操作并给出每个选项的概率，在 H200 上耗时 43 毫秒。<br><sub>相关: <a href="https://omnijev.github.io/PlayJev/">app</a> · <a href="https://huggingface.co/omnijev/playjev-0.8b">model</a> · <a href="https://omnijev.github.io/PlayJev">app 2</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/mmastrac/djev"><img src="https://opengraph.githubassets.com/1/mmastrac/djev" alt="djev" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/mmastrac/djev">djev</a></b><br><sub>mmastrac · GitHub · ⭐ 20 · 2026-09-21</sub><br>来自一个 vLLM pull request 的示例服务器，从 DiffusionGemma 获取 Jev 式结构化决策：先用答案模板初始化扩散画布，去噪一步后读取各槽位的分布。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Argos1111/jev_local"><img src="https://cdn-thumbnails.huggingface.co/social-thumbnails/models/argos1111/modernbert-ja-310m-jev.png" alt="Jev Local" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Argos1111/jev_local">Jev Local</a></b><br><sub>Argos1111 · GitHub · ⭐ 20 · 2026-09-18</sub><br>非官方的本地 /v1/systemone 服务器，支持文本、JSON 和图像，通过 LFM2.5 或 Sarashina 模型的首 token logprobs，或一个微调过的日语 ModernBERT 交叉编码器来回答 Choice、Score 和 Noul。<br><sub>相关: <a href="https://huggingface.co/argos1111/modernbert-ja-310m-jev">model</a> · <a href="https://huggingface.co/argos1111/sarashina2.2-vision-3b-mmproj-jev-f16">model 2</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/hawkymisc/typed-decision-bert"><img src="https://opengraph.githubassets.com/1/hawkymisc/typed-decision-bert" alt="JevBERT (typed-decision-bert)" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/hawkymisc/typed-decision-bert">JevBERT (typed-decision-bert)</a></b><br><sub>hawkymisc · GitHub · ⭐ 20 · 2026-09-21</sub><br>非官方概念验证：把 BERT 式编码器决策引擎放在 Jev 形态的 /v1/systemone API 后面，回答 noul、choice 和 score 问题，附公开结果和与真实 Jev 的基准对比。<br><sub>相关: <a href="https://x.com/hawkymisc/status/2102062149841588395">demo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/0xBakeer/arbiter"><img src="https://raw.githubusercontent.com/0xBakeer/arbiter/main/docs/media/how-it-works.gif" alt="arbiter" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/0xBakeer/arbiter">arbiter</a></b><br><sub>0xBakeer · GitHub · ⭐ 19 · 2026-09-20</sub><br>类型化决策模型（如 Laya 或你自己的模型）的服务层，可运行在 NVIDIA GPU 或 Apple Silicon 上，对外提供兼容 Jev 的 API，附带编程 agent 集成和 PR 风险关卡等示例。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/mpnikhil/dev-0.4b"><img src="https://opengraph.githubassets.com/1/mpnikhil/dev-0.4b" alt="dev-0.4b" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/mpnikhil/dev-0.4b">dev-0.4b</a></b><br><sub>mpnikhil · GitHub · ⭐ 19 · 2026-09-21</sub><br>基于 ModernBERT-large 的开放 399M 参数决策模型，面向开发者工具和编程 agent，一次前向传播回答路由、是/否和 1-5 分评级问题（在 Apple Silicon 上约 28 毫秒）。<br><sub><b>Jev 用法:</b> 沿用 Jev 和 Kev 的做法，在池化后的候选片段上使用单一的通用选择头；报告 Banking77 上 91.33%、BoolQ 上 85.20%。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/PsiACE/dohnuts"><img src="https://raw.githubusercontent.com/PsiACE/dohnuts/main/assets/dohnuts-logo.png" alt="Dohnuts" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/PsiACE/dohnuts">Dohnuts</a></b><br><sub>PsiACE · GitHub · ⭐ 18 · 2026-09-21</sub><br>小型多模态 System One 式模型，其中 0.8B 检查点能在消费级 GPU 上运行，一次前向传播回答关于文本或图像的 choice、noul 和 score 问题，并附训练和评测工具包。<br><sub>相关: <a href="https://dohnuts.ai/">site</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/arinltte/kevMac"><img src="https://external-preview.redd.it/ejRpYTBkYXN5cnFoMf6puSmljth1cgrGzuZwp2ZyyReZNPXgGD-ASmeljkJx.png?format=pjpg&amp;auto=webp&amp;s=6f4c1b33aa72bf2c5f1b0325b7e2e577be7bf2d8" alt="kevMac" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/arinltte/kevMac">kevMac</a></b><br><sub>arinltte · GitHub · ⭐ 18 · 2026-09-20</sub><br>在 Apple Silicon 上本地运行开放 Kev 决策模型的 Mac 应用：粘贴一份文档，以表单形式构建是/否、选择或打分问题，就能看到校准后的概率条；kev-0.6b 在 M4 上约 0.2 s 出答案。<br><sub><b>Jev 用法:</b> 把表单转换为本地 Kev 服务器（kev-0.6b 到 kev-9b 检查点）的 /v1/systemone 契约。</sub><br><sub>相关: <a href="https://www.reddit.com/r/vibecoding/comments/1wlyw27/experience_jev_locally_with_mac/">demo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/zhangcy122/OpenJev"><img src="https://opengraph.githubassets.com/1/zhangcy122/OpenJev" alt="OpenJevPro" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/zhangcy122/OpenJev">OpenJevPro</a></b><br><sub>zhangcy122 · GitHub · ⭐ 18 · 2026-09-20</sub><br>用约束 logprob 校准，把 Qwen3、DeepSeek、Gemma 和 gpt-oss 等开放权重 LLM 变成类型化 Choice、Noul 和 Score 决策服务的框架。<br><sub>相关: <a href="https://openjev.pro">site</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/hunkim/solar-mini4-jev"><img src="https://raw.githubusercontent.com/hunkim/solar-mini4-jev/main/bench/infographic_grok46_judge.png" alt="solar-mini4-jev" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/hunkim/solar-mini4-jev">solar-mini4-jev</a></b><br><sub>hunkim · GitHub · ⭐ 16 · 2026-09-21</sub><br>即插即用的封装，以 Jev System One API 的形式提供 Upstage Solar Mini4 服务，附带自带 key 的托管端点和正面对比基准测试。<br><sub><b>Jev 用法:</b> 以 Grok 4.6 作为评判，在 447 个答案字段中 Solar Mini4 错了 7 个，Jev 错了 26 个，但 Jev 快约 3.2 倍。</sub><br><sub>相关: <a href="https://solar-mini4-jev.vercel.app">app</a> · <a href="https://hunkim.github.io/solar-mini4-jev/">docs</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://www.reddit.com/r/LocalLLM/comments/1wlf4sv/opensource_jevstyle_typed_decision_model_that/"><img src="https://external-preview.redd.it/xjC6fykTq043HwezoQzDqEkNKkN-0dxncWqXwHYZK6s.png?auto=webp&amp;s=3f997e52f1b20af5ea33ad2aaea3df6fbd79202d" alt="VEJI-V2" width="240"></a></td>
<td valign="top"><b><a href="https://www.reddit.com/r/LocalLLM/comments/1wlf4sv/opensource_jevstyle_typed_decision_model_that/">VEJI-V2</a></b><br><sub>stopwwIII · Reddit · ▲ 5 · 2026-09-20</sub><br>MIT 许可的非自回归类型化决策模型：在冻结的多语言 MiniLM 上加一个 3.3M 参数的头，联合为选项打分、引用证据片段，并且可以弃权。<br><sub><b>Jev 用法:</b> 长 state 只编译一次，之后针对它回答多个类型化问题；在 522 个问题上报告测试准确率 82.95%。</sub><br><sub>相关: <a href="https://huggingface.co/loaiabdalslam/VEJI-V2">model</a> · <a href="https://huggingface.co/loaiabdalslam/veji-v2">project</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/olanotolu/jevbetter"><img src="https://raw.githubusercontent.com/olanotolu/jevbetter/main/docs/architecture.png" alt="jevbetter" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/olanotolu/jevbetter">jevbetter</a></b><br><sub>olanotolu · GitHub · ⭐ 14 · 2026-09-16</sub><br>从零构建的单遍选项打分器，采用哈希 n-gram 编码器、感知竞争选项的注意力、门控头和温度缩放，用 jevlike 数据格式训练，并与 jevlike 正面对比。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/abhishek085/open-spark-jev"><img src="https://raw.githubusercontent.com/abhishek085/open-spark-jev/main/docs/assets/nokast-logo.png" alt="Open Spark Jev" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/abhishek085/open-spark-jev">Open Spark Jev</a></b><br><sub>abhishek085 · GitHub · ⭐ 14 · 2026-09-20</sub><br>开放的本地决策模型 spark-s1，受 Jev 启发、基于 Qwen3 为 NVIDIA DGX Spark 打造，提供 Jev 兼容 API、架构说明，以及数据生成和评测工具。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/mohitsoni48/TurboLLM/tree/main/turbollm/web/src/screens/jev"><img src="https://opengraph.githubassets.com/1/mohitsoni48/TurboLLM" alt="TurboLLM 的 Jev 模式" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/mohitsoni48/TurboLLM/tree/main/turbollm/web/src/screens/jev">TurboLLM 的 Jev 模式</a></b><br><sub>mohitsoni48 · GitHub · ⭐ 275 仓库 · 2026-06-12</sub><br>本地 LLM 运行器，会把 NLI cross-encoder 模型识别为本地 Jev 模型，并通过 /v1/systemone、/v1/classify 和 /v1/rerank 提供服务，附带 JSON 优先的 playground。<br><sub>相关: <a href="https://turbollm.dev">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/kikoncuo/jevfire"><img src="https://raw.githubusercontent.com/kikoncuo/jevfire/main/assets/hero.png" alt="JEVfire" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/kikoncuo/jevfire">JEVfire</a></b><br><sub>kikoncuo · GitHub · ⭐ 13 · 2026-09-16</sub><br>受 Jev 启发、面向 vLLM 上 CUDA LLM 的并行决策方案，用模型自带的输出头给单 token 标签打分，再用代码拼出 JSON，附游戏演示，包括浏览器内的 Mario，每个动作 71 毫秒。<br><sub><b>Jev 用法:</b> 无需重新训练，也不需要第二个模型；schema 固定了键名和允许的值。</sub><br><sub>相关: <a href="https://kikoncuo.github.io/jevfire/learn.html">site</a> · <a href="https://kikoncuo.github.io/jevfire">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/ChristianAlexander/laya_ex"><img src="https://opengraph.githubassets.com/1/ChristianAlexander/laya_ex" alt="laya_ex" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/ChristianAlexander/laya_ex">laya_ex</a></b><br><sub>ChristianAlexander · GitHub · ⭐ 13 · 2026-09-20</sub><br>Elixir 库，为 Convai Innovations 开放的 Laya 决策模型提供原生 Nx 和 Bumblebee 运行时，首次加载时会下载官方 checkpoint。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://huggingface.co/datasets/ZefanCai/Open-Jev"><img src="https://cdn-thumbnails.huggingface.co/social-thumbnails/datasets/ZefanCai/Open-Jev.png" alt="Open-Jev datasets" width="240"></a></td>
<td valign="top"><b><a href="https://huggingface.co/datasets/ZefanCai/Open-Jev">Open-Jev datasets</a></b><br><sub>ZefanCai · Hugging Face · ♥ 13 · 2026-09-20</sub><br>来自独立项目 Open-Jev 的十二个冻结的类型化决策数据配置，大多为合成数据（是/否、选择、多标签、数值和序数），附带清单、原始记录和重建代码。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/genai-craft/openvons"><img src="https://opengraph.githubassets.com/1/genai-craft/openvons" alt="openvons" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/genai-craft/openvons">openvons</a></b><br><sub>genai-craft · GitHub · ⭐ 13 · 2026-09-17</sub><br>开放决策层，让 LLM、VLM 和 ASR 模型从有限选项集（含“以上都不是”）中做选择，并把校准概率划分为执行、确认和拒绝三档；包含日语语音指令。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/stephanj/parallelConstraintDecoding"><img src="https://external-preview.redd.it/IXd1hZpg6SpsXqnxAePniddWNOv3rlbrwQhwMZZfaig.png?auto=webp&amp;s=3ce2634792342b174000165911a5fe4b774d8df9" alt="parallelConstraintDecoding" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/stephanj/parallelConstraintDecoding">parallelConstraintDecoding</a></b><br><sub>stephanj · GitHub · ⭐ 13 · 2026-09-17</sub><br>并行约束解码的 Java 和 Python 实现，在 llama.cpp 模型上用两次前向填完由布尔值和枚举组成的 JSON schema，给出每个字段的置信度，并附带基准测试 Web 应用。<br><sub>相关: <a href="https://www.reddit.com/r/java/comments/1wjhn9h/parallel_constraint_decoding_using_java_and/">discussion</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://huggingface.co/pngwn/system-one-qwen3.5-4b-scorer"><img src="https://cdn-thumbnails.huggingface.co/social-thumbnails/models/pngwn/system-one-qwen3.5-4b-scorer.png" alt="system-one-qwen3.5-4b-scorer" width="240"></a></td>
<td valign="top"><b><a href="https://huggingface.co/pngwn/system-one-qwen3.5-4b-scorer">system-one-qwen3.5-4b-scorer</a></b><br><sub>pngwn · Hugging Face · ♥ 13 · 2026-09-16</sub><br>基于 Qwen3.5-4B-Base 的开放 Jev 形态决策模型，带打分头，一次前向即可针对是/否、Choice 和 Score 问题返回只覆盖调用方所给选项的分布。<br><sub><b>Jev 用法:</b> 为每个 (state, question, option) 三元组打分，再按问题做 softmax；附带训练代码。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/nokia-applied-research/AnyJev"><img src="https://raw.githubusercontent.com/nokia-applied-research/AnyJev/main/assets/banner.png" alt="AnyJev" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/nokia-applied-research/AnyJev">AnyJev</a></b><br><sub>nokia-applied-research · GitHub · ⭐ 12 · 2026-09-21</sub><br>库，无需训练、只需一次 prefill 就能把任意 transformers 或 vLLM 模型变成 Jev 式的 Choice、Score 和 Noul 决策模型，并通过循环移位边缘化解决选项顺序导致的结果翻转。<br><sub>相关: <a href="https://pypi.org/project/anyjev/">pypi</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Yeachan-Heo/ifllm-learn"><img src="https://raw.githubusercontent.com/Yeachan-Heo/ifllm-learn/main/docs/demo-overview.svg" alt="ifllm-learn" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Yeachan-Heo/ifllm-learn">ifllm-learn</a></b><br><sub>Yeachan-Heo · GitHub · ⭐ 12 · 2026-09-20</sub><br>基于 SemIf 和 MLX-LM 的研究工具包，用带标签样本把本地 LoRA 适配器微调成类型化决策模型，并在客服路由、超范围检测和合同清单上做了有实测数据的演示。<br><sub><b>Jev 用法:</b> 在 Apple Silicon 上本地训练 Jev 式类型化决策；与 TypeSafe 无关，也不是 Jev 训练方法的复刻。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/pst2154/Nemotron_Jev"><img src="https://opengraph.githubassets.com/1/pst2154/Nemotron_Jev" alt="Nemotron Diffusion Decision Lab" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/pst2154/Nemotron_Jev">Nemotron Diffusion Decision Lab</a></b><br><sub>pst2154 · GitHub · ⭐ 12 · 2026-09-18</sub><br>实验性容器，把稠密的 Nemotron-Labs-Diffusion-14B 模型封装在 TypeSafe 形式的 API 后面提供服务，并附带一个在浏览器里查看 Choice、Noul 和 Score 分布的探索工具。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/zwliJay/jev-forge"><img src="https://raw.githubusercontent.com/zwliJay/jev-forge/main/docs/assets/jevforge-demo.gif" alt="JevForge" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/zwliJay/jev-forge">JevForge</a></b><br><sub>zwliJay · GitHub · ⭐ 11 · 2026-09-19</sub><br>Jev 式决策模型的端到端技术栈：合成决策数据、训练校准的 Qwen3.5-0.8B 候选打分器、固定的 Mind2Web 和分布外评测、初步的 RLCD，以及兼容 Jev 的服务部署。<br><sub>相关: <a href="https://jay-forge-web.vercel.app/">app</a> · <a href="https://jev-forge.vercel.app">app 2</a> · <a href="https://huggingface.co/datasets/AndeyTait/JevForge-Mind2Web">model</a> · <a href="https://huggingface.co/AndeyTait/JevForge-0.8B">model 2</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Micha0827/snapjudge"><img src="https://raw.githubusercontent.com/Micha0827/snapjudge/main/assets/snaprun.gif" alt="snapjudge" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Micha0827/snapjudge">snapjudge</a></b><br><sub>Micha0827 · GitHub · ⭐ 10 · 2026-09-18</sub><br>兼容 TypeSafe 的服务器，在 Apple Silicon 上通过 MLX 从本地 Qwen 模型的 logits 读取 Choice、Score 和 Noul 概率；Qwen3.8-27B 在 20 个公开用例上与 Jev 的一致率达到 81.2%。<br><sub>相关: <a href="https://www.reddit.com/r/LocalLLM/comments/1wlr8sp/i_rebuilt_the_jev_interface_with_local_qwen/">discussion</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/komorra/Eugeniusz"><img src="https://raw.githubusercontent.com/komorra/Eugeniusz/main/docs/assets/eugeniusz-banner.png" alt="Eugeniusz" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/komorra/Eugeniusz">Eugeniusz</a></b><br><sub>komorra · GitHub · ⭐ 9 · 2026-09-17</sub><br>MIT 许可的 C++17 库，提供 C ABI，在本地评估文本并返回一个选项、评分量表分数或真值概率，作为 Jev 决策接口的独立替代方案，可用于 C、C#、Python、Unity 和 Unreal。<br><sub><b>Jev 用法:</b> 在本地 Qwen 模型上仿照 Choice/Score/Noul 接口；并不复现 Jev 的训练、延迟或准确率。</sub><br><sub>相关: <a href="https://www.reddit.com/r/aigamedev/comments/1wjihg8/i_let_a_local_ai_play_hexen_eugeniusz_yolo/">demo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/liushiliushi/JevTuner"><img src="https://raw.githubusercontent.com/liushiliushi/JevTuner/main/images/jevtuner_method_drawio.png" alt="JevTuner" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/liushiliushi/JevTuner">JevTuner</a></b><br><sub>liushiliushi · GitHub · ⭐ 9 · 2026-09-21</sub><br>让语言模型做出 Jev 式封闭集合决策的训练方法，一次前向传播给每个候选打分，并用 token 化的 Brier 损失调优整个分布。<br><sub><b>Jev 用法:</b> 把 ConfTuner 训练 token logit 概率的思路应用到 state 加问题的决策任务上。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://huggingface.co/mradermacher/jevify-gemma4-26b-a4b-GGUF"><img src="https://cdn-thumbnails.huggingface.co/social-thumbnails/models/mradermacher/jevify-gemma4-26b-a4b-GGUF.png" alt="jevify-gemma4-26b-a4b GGUF" width="240"></a></td>
<td valign="top"><b><a href="https://huggingface.co/mradermacher/jevify-gemma4-26b-a4b-GGUF">jevify-gemma4-26b-a4b GGUF</a></b><br><sub>mradermacher · Hugging Face · ⬇ 803 · 2026-09-20</sub><br>静态 GGUF 量化版本（Q2_K 到 Q8_0），对应 jevify-gemma4-26b-a4b，也就是支撑本地、兼容 Jev 的 jevify 决策 API 的 Gemma 4 模型。<br><sub>相关: <a href="https://github.com/kushalpatil07/jevify">project</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/chengyongru/fastjev"><img src="https://raw.githubusercontent.com/chengyongru/fastjev/main/assets/fastjev-logo.svg" alt="FastJev" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/chengyongru/fastjev">FastJev</a></b><br><sub>chengyongru · GitHub · ⭐ 8 · 2026-09-20</sub><br>SemIf 的一个以 SDK 为先、独立维护的分支，用于自托管开放的 Jev 实现，通过 Torch、vLLM、MLX 或 llama.cpp 运行固定版本的开放模型来处理 Choice、Boolean 和 Score。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/kerryrm/systemANE"><img src="https://opengraph.githubassets.com/1/kerryrm/systemANE" alt="systemANE" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/kerryrm/systemANE">systemANE</a></b><br><sub>kerryrm · GitHub · ⭐ 8 · 2026-09-20</sub><br>在 Apple Neural Engine 上实现 System One 风格引擎的概念验证，基于 22.6M 参数编码器提供 Choice、Boolean 和 Score 原语，拿不准的情况升级给 Apple 的 Foundation Models。<br><sub><b>Jev 用法:</b> 在 CLINC150 上报告准确率 93.3%、ECE 0.041，每个决策 1.4 毫秒。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/aabolfazl/typesafe-local"><img src="https://raw.githubusercontent.com/aabolfazl/typesafe-local/main/docs/diagrams/03-encode-once-ask-many.png" alt="typesafe-local" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/aabolfazl/typesafe-local">typesafe-local</a></b><br><sub>aabolfazl · GitHub · ⭐ 8 · 2026-09-18</sub><br>兼容 TypeSafe API 形式的本地 MLX 服务器，文档只编码一次，每个问题作为短后缀追加，读取 logits 而不做生成；在 M4 Pro 上四个问题约 200 毫秒。<br><sub><b>Jev 用法:</b> 测量校准和选项顺序对答案的影响；API 形式与 TypeSafe 一致，同一个客户端两边都能用。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/siliconkernel/vllm-jev-decison"><img src="https://raw.githubusercontent.com/siliconkernel/vllm-jev-decison/main/assets/en/architecture.svg" alt="vllm-jev-decison" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/siliconkernel/vllm-jev-decison">vllm-jev-decison</a></b><br><sub>siliconkernel · GitHub · ⭐ 8 · 2026-09-18</sub><br>vLLM 插件，为类 Jev 的类型化决策增加仅分类模式，从有限 JSON Schema 中为候选标签打分，返回类型化值、概率和弃权结果，不做生成。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/thecodacus/decision-playground"><img src="https://opengraph.githubassets.com/1/thecodacus/decision-playground" alt="Decision Playground" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/thecodacus/decision-playground">Decision Playground</a></b><br><sub>thecodacus · GitHub · ⭐ 7 · 2026-09-19</sub><br>纯浏览器端的 playground 和竞技场游戏，面向 llama-server 的 Jev 式 /v1/decision 端点，在同一个模型上对比一次并行决策计算与语法约束的聊天生成，并让 agent 每秒多次选择操控动作。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/jlt-commons/lev"><img src="https://opengraph.githubassets.com/1/jlt-commons/lev" alt="Lev" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/jlt-commons/lev">Lev</a></b><br><sub>jlt-commons · GitHub · ⭐ 7 · 2026-09-19</sub><br>用 Clojure 编写、运行在 Chez Scheme 上的 System One 决策引擎，在笔记本 CPU 上以约 100 毫秒 的速度提供 Laya ModernBERT/mmBERT 编码器服务，另有一个基于 llama.cpp 的思考器，其答案按 token 对数概率打分。<br><sub><b>Jev 用法:</b> 针对 state 回答类型化问题并返回校准概率；开启思考的 MiniCPM5-2B 在对抗性的 authored144 集上得分 95%，而编码器只有 61-67%。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/scienthoon/luce"><img src="https://raw.githubusercontent.com/scienthoon/luce/main/media/live_triage.gif" alt="Luce" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/scienthoon/luce">Luce</a></b><br><sub>scienthoon · GitHub · ⭐ 7 · 2026-09-20</sub><br>构建特定任务校准决策模型的配方：描述任务，让 LLM 教师合成或标注数据，在 Qwen 上训练 LoRA 加决策头，评估校准效果，再对外提供类型化概率。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/kyegomez/open-jev"><img src="https://opengraph.githubassets.com/1/kyegomez/open-jev" alt="Open Jev" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/kyegomez/open-jev">Open Jev</a></b><br><sub>kyegomez · GitHub · ⭐ 7 · 2026-09-21</sub><br>对 Jev 背后思路的非官方 PyTorch 重建，权重为随机初始化：state 只编码一次，每个问题都通过小型类型化读出头在一次并行前向传播中得到回答。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/RJMSWD/QwenJev"><img src="https://raw.githubusercontent.com/RJMSWD/QwenJev/main/examples/support_ticket.png" alt="Qwen Choice" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/RJMSWD/QwenJev">Qwen Choice</a></b><br><sub>RJMSWD · GitHub · ⭐ 7 · 2026-09-21</sub><br>基于 Qwen3.5-4B 的本地 Jev 风格视觉判断：输入图像、问题和选项，一次前向即返回选项及其概率，在 RTX A6000 上约 169 毫秒。<br><sub><b>Jev 用法:</b> 使用原始 BF16 权重，关闭思考，不做训练或量化。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://huggingface.co/spaces/mobarmg/jev-schema-scorer"><img src="https://cdn-thumbnails.huggingface.co/social-thumbnails/spaces/mobarmg/jev-schema-scorer.png" alt="按 schema 条件化的候选打分器演示" width="240"></a></td>
<td valign="top"><b><a href="https://huggingface.co/spaces/mobarmg/jev-schema-scorer">按 schema 条件化的候选打分器演示</a></b><br><sub>mobarmg · 应用 · ♥ 7 · 2026-09-17</sub><br>交互式演示：基于 DeBERTa-v3-large 标量头的打分器在推理时读取你自己定义的 choice、noul 和 score schema，并把分组 logits 解码成类型化答案。<br><sub>相关: <a href="https://huggingface.co/mobarmg/jev-schema-scorer-deberta-v3-large">model</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/jiangxiluning/Visual-Jev"><img src="https://raw.githubusercontent.com/jiangxiluning/Visual-Jev/master/demo/assets/semif-phase1-replay.gif" alt="Visual-Jev" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/jiangxiluning/Visual-Jev">Visual-Jev</a></b><br><sub>jiangxiluning · GitHub · ⭐ 7 · 2026-09-22</sub><br>SemIf（原名 OpenJev）的副本，SemIf 是 Jev 类型化决策接口的开源复刻；这个版本增加了可选的图像输入，把 Qwen3.5-4B 作为视觉语言模型运行，支持直接、串行和共享三种打分方式。<br><sub>相关: <a href="https://github.com/TheoLeeCJ/SemIf">upstream</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/hyprstream/hyprstream/tree/main/crates/hyprstream-decision-stub"><img src="https://raw.githubusercontent.com/hyprstream/hyprstream/main/architecture.png" alt="HyprStream 决策服务" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/hyprstream/hyprstream/tree/main/crates/hyprstream-decision-stub">HyprStream 决策服务</a></b><br><sub>hyprstream · GitHub · ⭐ 127 仓库 · 2025-01-06</sub><br>一个自我改进的 AI 运行时，正在构建自己的 System One 决策服务，包含一个决策头和一个 /v1/systemone 门面，原版的 TypeSafe Python 和 JS SDK 可以直接对接它运行。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://huggingface.co/collections/llm-semantic-router/decision-10-6ab12177bd0002394d8409f9"><img src="https://cdn-thumbnails.huggingface.co/social-thumbnails/collections/llm-semantic-router/decision-10-6ab12177bd0002394d8409f9.png" alt="Decision 1.0" width="240"></a></td>
<td valign="top"><b><a href="https://huggingface.co/collections/llm-semantic-router/decision-10-6ab12177bd0002394d8409f9">Decision 1.0</a></b><br><sub>vLLM Semantic Router · Hugging Face · ♥ 6 · 2026-09-22</sub><br>vLLM Semantic Router 团队推出的 Apache-2.0 开放决策模型合集，包括 572M 编码器和 1.88B 到 4.21B 的解码器，一次计算即可回答 Choice、Noul 和 Score，支持 50 种语言，另附一个 Studio Space。<br><sub>相关: <a href="https://huggingface.co/llm-semantic-router/Decision-1.0-Kai">model</a> · <a href="https://huggingface.co/spaces/llm-semantic-router/decision-studio">space</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Astro-Han/decision-head-rlcd"><img src="https://opengraph.githubassets.com/1/Astro-Han/decision-head-rlcd" alt="decision-head-rlcd" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Astro-Han/decision-head-rlcd">decision-head-rlcd</a></b><br><sub>Astro-Han · GitHub · ⭐ 6 · 2026-09-20</sub><br>实验：用 rank-8 LoRA 和 RLCD 在 32,000 个类型化决策上训练 Qwen3.5-4B，检验类 Jev 模型的泛化能力从何而来；结论是泛化程度跟随训练数据的覆盖面。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://huggingface.co/lewislululu/jevon"><img src="https://cdn-thumbnails.huggingface.co/social-thumbnails/models/lewislululu/jevon.png" alt="Jevon" width="240"></a></td>
<td valign="top"><b><a href="https://huggingface.co/lewislululu/jevon">Jevon</a></b><br><sub>lewislululu · Hugging Face · ♥ 6 · 2026-09-19</sub><br>极小的 20M 参数决策模型，为迷宫和贪吃蛇回答关于网格的类型化问题（往哪走、北边是否通畅、离目标多远），在 NanoJev 基础上围绕规划深度重建。<br><sub>相关: <a href="https://github.com/lewislulu/jevon-arcade">project</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://huggingface.co/monotykamary/LFM2.5-2.6B-RLCD"><img src="https://cdn-thumbnails.huggingface.co/social-thumbnails/models/monotykamary/LFM2.5-2.6B-RLCD.png" alt="LFM2.5-2.6B-RLCD" width="240"></a></td>
<td valign="top"><b><a href="https://huggingface.co/monotykamary/LFM2.5-2.6B-RLCD">LFM2.5-2.6B-RLCD</a></b><br><sub>monotykamary · Hugging Face · ♥ 6 · 2026-09-16</sub><br>实验性的并行约束解码包，基于未改动的 LFM2.5-2.6B 权重，在 12 个开发用例上比自回归生成 JSON 快约 9.9 倍，但在全新审计用例上字段准确率只有 72.2%。<br><sub><b>Jev 用法:</b> 瞄准 Jev 快速的有限选项交互模式；明确声明未校准，也不是对 RLCD 训练的复现。</sub><br><sub>相关: <a href="https://huggingface.co/notnotsamuel/LFM2.5-350M-RLCD">related</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/jagsan-cyber/reflex-gate"><img src="https://opengraph.githubassets.com/1/jagsan-cyber/reflex-gate" alt="ReflexGate" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/jagsan-cyber/reflex-gate">ReflexGate</a></b><br><sub>jagsan-cyber · GitHub · ⭐ 6 · 2026-09-19</sub><br>面向本地 agent 循环的离线 Go 网关，提供循环退出、参数提取和安全扫描端点，外加用于类型化 noul 和 choice 分诊的 Jev 兼容 /v1/systemone，附带 Windows 图形界面。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/hemanth/webml-kit"><img src="https://opengraph.githubassets.com/1/hemanth/webml-kit" alt="webml-kit" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/hemanth/webml-kit">webml-kit</a></b><br><sub>hemanth · GitHub · ⭐ 6 · 2026-04-20</sub><br>框架无关的工具包，通过 WebGPU/WASM 在浏览器中运行 ML 模型，新增 Jev 风格的决策任务，从 Qwen 或 OpenJev GGUF 等本地模型读取类型化 Choice、Noul 和 Score 答案。<br><sub>相关: <a href="https://hemanth.github.io/webml-kit/">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/leehanchung/SMILE-factory/tree/main/research/jev"><img src="https://opengraph.githubassets.com/1/leehanchung/SMILE-factory" alt="RE Jev 研究项目" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/leehanchung/SMILE-factory/tree/main/research/jev">RE Jev 研究项目</a></b><br><sub>leehanchung · GitHub · ⭐ 106 仓库 · 2023-05-07</sub><br>构建类 Jev 决策模型的研究交接文档，涵盖设计标准、架构、训练数据计划、GLiNER2 基准测试和校准规程；目前还没有训练任何模型。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/mattn/tensai/blob/main/internal/llm/systemone.go"><img src="https://opengraph.githubassets.com/1/mattn/tensai" alt="tensai 的 System One 端点" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/mattn/tensai/blob/main/internal/llm/systemone.go">tensai 的 System One 端点</a></b><br><sub>mattn · GitHub · ⭐ 106 仓库 · 2026-08-19</sub><br>小巧的纯 Go 神经网络框架，通过读取每个问题后带标签的 logits，用任意已加载的模型处理 Jev 形态的 System One 请求，Jev API 客户端可以直接指向它。<br><sub>相关: <a href="https://mattn.github.io/tensai/">docs</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://huggingface.co/mradermacher/jevify-gemma4-e4b-GGUF"><img src="https://cdn-thumbnails.huggingface.co/social-thumbnails/models/mradermacher/jevify-gemma4-e4b-GGUF.png" alt="jevify-gemma4-e4b GGUF" width="240"></a></td>
<td valign="top"><b><a href="https://huggingface.co/mradermacher/jevify-gemma4-e4b-GGUF">jevify-gemma4-e4b GGUF</a></b><br><sub>mradermacher · Hugging Face · ⬇ 506 · 2026-09-20</sub><br>静态 GGUF 量化版本（Q2_K 到 Q8_0），对应 jevify-gemma4-e4b，也就是支撑本地、兼容 Jev 的 jevify 决策 API 的 Gemma 4 E4B 模型。<br><sub>相关: <a href="https://github.com/kushalpatil07/jevify">project</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/hwfengcs/any2jev"><img src="https://raw.githubusercontent.com/hwfengcs/any2jev/main/docs/vs.gif" alt="any2jev" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/hwfengcs/any2jev">any2jev</a></b><br><sub>hwfengcs · GitHub · ⭐ 5 · 2026-09-21</sub><br>转换工具，把任意 Hugging Face 因果语言模型训练成 Jev 式决策模型，一次前向传播回答类型化问题，给出校准概率且不生成任何 token，以 Qwen3-0.6B 做了演示。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/yzfly/edgejev"><img src="https://opengraph.githubassets.com/1/yzfly/edgejev" alt="EdgeJev" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/yzfly/edgejev">EdgeJev</a></b><br><sub>yzfly · GitHub · ⭐ 5 · 2026-09-20</sub><br>离线 CPU 运行时，把 laya、kev、NanoJev、PlayJev 等开放 Jev 复刻转换为 ONNX 并做 INT8 量化，通过协议兼容的本地服务器提供服务；在 4 个 CPU 核上每个问题 15.6 毫秒。<br><sub>相关: <a href="https://pypi.org/project/edgejev/">pypi</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/yohanargentina-oss/Foq"><img src="https://raw.githubusercontent.com/yohanargentina-oss/Foq/main/assets/chart_memory_paradox.png" alt="Foq" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/yohanargentina-oss/Foq">Foq</a></b><br><sub>yohanargentina-oss · GitHub · ⭐ 5 · 2026-09-19</sub><br>本地运行的开源 Jev 替代品，一次前馈计算就对类型化的 boolean、choice、score 和 Pydantic 问题返回校准概率，报告约 25 毫秒，并附与 Laya 的基准对比。<br><sub>相关: <a href="https://foq.fr">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://huggingface.co/vagmi/jev-lite"><img src="https://cdn-thumbnails.huggingface.co/social-thumbnails/models/vagmi/jev-lite.png" alt="jev-lite" width="240"></a></td>
<td valign="top"><b><a href="https://huggingface.co/vagmi/jev-lite">jev-lite</a></b><br><sub>vagmi · Hugging Face · ♥ 5 · 2026-09-19</sub><br>QLoRA 适配器，把 Gemma 4 E4B 变成 System One 决策模型，从选项字母处的 logits 读出答案，因此不可能答出给定选项之外的内容。<br><sub>相关: <a href="https://github.com/vagmi/jevlite">project</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/NVentimiglia/laya-mcp"><img src="https://opengraph.githubassets.com/1/NVentimiglia/laya-mcp" alt="Laya MCP" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/NVentimiglia/laya-mcp">Laya MCP</a></b><br><sub>NVentimiglia · GitHub · ⭐ 5 · 2026-09-19</sub><br>面向 Claude Code、Copilot CLI 和 Cursor 的 MCP 服务器和 agent 插件，在本地运行开放的 Laya 决策模型，为 agent 提供五个工具，一次前向传播返回标签、概率或分数。<br><sub><b>Jev 用法:</b> 用本地的 convaiinnovations/laya 检查点做 Jev 式类型化决策，以 0.85 的置信度阈值决定自动执行还是升级处理。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/afshinm/laya-mps"><img src="https://opengraph.githubassets.com/1/afshinm/laya-mps" alt="Laya MPS" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/afshinm/laya-mps">Laya MPS</a></b><br><sub>afshinm · GitHub · ⭐ 5 · 2026-09-21</sub><br>通过 PyTorch MPS 在 Apple Silicon 上运行开放的 Laya 模型做 Jev 式类型化决策，在 M5 Pro 上中位延迟约 32 毫秒，占用 2.1 GiB 内存。<br><sub><b>Jev 用法:</b> 用一个约 843 MB、针对客服、发票、安全事件和 agent 轨迹调优的模型做 Choice、Score 和真值概率决策。</sub><br><sub>相关: <a href="https://news.ycombinator.com/item?id=49787265">demo</a> · <a href="https://www.reddit.com/r/LocalLLM/comments/1wm64ih/run_jevstyle_typed_decisions_locally_on_apple/">discussion</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/wmoto-ai/local-decision-playground"><img src="https://opengraph.githubassets.com/1/wmoto-ai/local-decision-playground" alt="Local Decision Playground" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/wmoto-ai/local-decision-playground">Local Decision Playground</a></b><br><sub>wmoto-ai · GitHub · ⭐ 5 · 2026-09-17</sub><br>零依赖的日语 Web 应用，用于把本地 vLLM 模型当作受 Jev 启发的分类器来试用：它把生成限制在声明的选项内，并把这些选项的 logprobs 归一化为相对概率，图像同样适用。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://huggingface.co/samatv256/mini-Jev"><img src="https://cdn-thumbnails.huggingface.co/social-thumbnails/models/samatv256/mini-Jev.png" alt="ODM Mini" width="240"></a></td>
<td valign="top"><b><a href="https://huggingface.co/samatv256/mini-Jev">ODM Mini</a></b><br><sub>samatv256 · Hugging Face · ♥ 5 · 2026-09-21</sub><br>基于冻结 Qwen3-0.6B 的开放权重 Choice 决策头，为候选 agent 动作排序并返回概率、置信度和 margin，用于工具选择（语义 Choice 准确率 72.97%）。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/xingwudao/OpenJev"><img src="https://opengraph.githubassets.com/1/xingwudao/OpenJev" alt="OpenJev" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/xingwudao/OpenJev">OpenJev</a></b><br><sub>xingwudao · GitHub · ⭐ 5 · 2026-09-18</sub><br>独立开发、受 Jev 启发的决策 API，提供 Choice、Score 和 Noul 原语、本地 mock 服务器以及 Python 和 TypeScript SDK；mock 返回的概率是合成的，真实推理尚在计划中。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/stephanj/pcdServer"><img src="https://raw.githubusercontent.com/stephanj/pcdServer/main/docs/images/pcd-playground.png" alt="PCD Server" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/stephanj/pcdServer">PCD Server</a></b><br><sub>stephanj · GitHub · ⭐ 5 · 2026-09-18</sub><br>面向本地 GGUF 模型的原生 C++ 并行约束解码 REST 服务器：输入文本和取值受限的字段，它为每个字段选出一个允许值，以 Jev 的风格返回 JSON 及每个决策的概率。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/rupeshpoojary9/poorjev"><img src="https://raw.githubusercontent.com/rupeshpoojary9/poorjev/main/docs/reliability_before_after.png" alt="poorjev" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/rupeshpoojary9/poorjev">poorjev</a></b><br><sub>rupeshpoojary9 · GitHub · ⭐ 5 · 2026-09-19</sub><br>本地 System One 风格决策层，在零样本 NLI 模型上实现 Jev 的类型化 Choice、Score 和 Noul 接口，借助温度缩放和保形弃权（conformal abstention）把 ECE 从 0.170 降到 0.071。<br><sub>相关: <a href="https://www.reddit.com/r/learnmachinelearning/comments/1wksf4i/poorjev_an_open_local_system_one_decision_layer/">discussion</a></sub></td>
</tr>
</table>

<details><summary>还有 90 条</summary>

- **[ruling](https://github.com/bradAGI/ruling)** · <sub>bradAGI · GitHub · ⭐ 5 · 2026-09-18</sub><br>对 Jev 类型化决策接口的开放权重复刻，在 Apple Silicon Mac 上用 MLX 和 4-bit Qwen3.5 checkpoint 运行，约 119 毫秒 出结果；一个 19 GB 的 MoE 模型在 TypeSafe 的评测数据上达到了 Jev 的准确率。
- **[verdict](https://github.com/khimaros/verdict)** · <sub>khimaros · GitHub · ⭐ 5 · 2026-09-20</sub><br>自托管服务器，通过一次前向读取每个选项标签的概率，把任意 llama-server 或 llama-swap 端点变成 Jev 兼容的 System One API，Jev 客户端只需修改 base URL。
- **[eve-rlcd](https://github.com/anthony-maio/eve-rlcd)** · <sub>anthony-maio · GitHub · ⭐ 4 · 2026-09-18</sub><br>受 Jev 启发的 0.6B 决策模型，基于 Qwen3-0.6B-Base，用对/错反馈做强化学习训练，让选项概率与准确率相匹配；包含训练循环、消融实验、评测和开放权重。
- **[hearim](https://github.com/ziozzang/hearim)** · <sub>ziozzang · GitHub · ⭐ 4 · 2026-09-21</sub><br>Go 网关，在 Ollama、llama.cpp、vLLM 等普通 LLM 后端上提供 Jev 的 /v1/systemone 契约，把每个问题当作单 token 选择，根据 logprobs 打分。
- **[Jev-Compatible](https://github.com/David-Lolly/Jev-Compatible)** · <sub>David-Lolly · GitHub · ⭐ 4 · 2026-09-21</sub><br>HTTP 网关，通过给候选 token 打分来回答 noul、choice 和 score 问题，把现有的 SGLang 或 vLLM 部署变成兼容 Jev 的决策服务，无需训练或改动模型。
- **[jev-rs](https://github.com/yijunyu/jev-rs)** · <sub>yijunyu · GitHub · ⭐ 4 · 2026-09-21</sub><br>Rust 引擎，一次 prefill 就能用 llama-server 背后的任意 GGUF 模型回答 Noul、Choice 和 Score 问题，与 Jev 的 /v1/systemone 在协议层兼容，并以 MCP 工具的形式提供。
- **[Jev-Style-Qwen3.5-2B-Decision (GGUF)](https://huggingface.co/chaoliangUNSW/Jev-Style-Qwen3.5-2B-Decision-GGUF)** · <sub>chaoliangUNSW · Hugging Face · ♥ 4 · 2026-09-21</sub><br>一个 Jev 式 Qwen3.5-2B 决策模型的 GGUF 构建，适用于 LM Studio 和 llama.cpp，从单个 token 位置读出校准的选项概率；Q4_K_M（1.3 GB）仍保持 82.4% 的准确率。
- **[qwen-rlcd](https://github.com/shamazharikh/qwen-rlcd)** · <sub>shamazharikh · GitHub · ⭐ 4 · 2026-09-16</sub><br>基于 Qwen3.5-0.8B-Base 的 Jev 风格决策模型原型：state 只 prefill 一次，为每个问题-答案分支分叉缓存并读出校准分布；推理已可用，训练暂停。
- **[System One Gemma](https://github.com/akash-kamat/system-one-gemma)** · <sub>akash-kamat · GitHub · ⭐ 4 · 2026-09-17</sub><br>开放的 Jev 风格决策模型，在 Gemma 3 270M 上加一个线性打分头，一次批处理前向为每个选项序列打分，再经 softmax 得到校准的 Choice、Noul 和 Score 答案。
- **[mlx-omarchy 的 Laya 推理服务](https://github.com/joshuaswarren/mlx-omarchy/tree/main/serve/mlx_omarchy_laya)** · <sub>joshuaswarren · GitHub · ⭐ 64 仓库 · 2026-08-31</sub><br>面向 Apple Silicon Linux 的 MLX GPU 后端，移植开放的 Laya 类型化决策模型并通过自带的 decisions 端点提供服务，已在 M1 Max 上通过 6/6 项数值校验。
- **[jev-local](https://github.com/us/jev-local)** · <sub>us · GitHub · ⭐ 3 · 2026-09-18</sub><br>兼容 /v1/systemone API 的本地服务器，用开放权重以概率回答类型化的 noul、choice 和 score 问题，官方 SDK 可以直接指向它；默认打分器是一个确定性的桩实现。
- **[jevify](https://github.com/Mintzs/jevify)** · <sub>Mintzs · GitHub · ⭐ 3 · 2026-09-18</sub><br>实验性推理引擎，基于模型分数构造 JSON，让现有 LLM（默认 Qwen2.5-1.5B-Instruct）回答 Jev 式的分类、是/否和评分量表问题；概率未经校准。
- **[Laya Go](https://github.com/neko233-com/laya-go)** · <sub>neko233-com · GitHub · ⭐ 3 · 2026-09-21</sub><br>为 Laya 提供的 Go 服务器，附管理后台、agent CLI 和 MCP 工具；Laya 是开放的 System 1 决策模型，对结构化特征打分并返回排序后的概率，不生成文本。
- **[local-jev](https://github.com/amithgc/local-jev)** · <sub>amithgc · GitHub · ⭐ 3 · 2026-09-21</sub><br>离线服务器，兼容 TypeSafe System One 的通信格式，官方 SDK 无需修改即可使用，用小型开放模型回答类型化问题；在 JevBench 的 231 道公开题上报告得分 80.5%。
- **[omo-jevlike-router](https://github.com/islee23520/omo-jevlike-router)** · <sub>islee23520 · GitHub · ⭐ 3 · 2026-09-18</sub><br>OmO agent 的 skill 路由器，用冻结的 Qwen2.5-0.5B 加一个小型 Jev 风格选项头，一次前向传播给整个 skill 目录打分，把系统提示词精简到 top-K 个 skill。
- **[open-jev demo](https://huggingface.co/spaces/nico-martin/open-jev-demo)** · <sub>nico-martin · 应用 · ♥ 3 · 2026-09-21</sub><br>open-jev npm 包的浏览器演示，通过 Transformers.js 用 Kev 和 open-jev ONNX 模型在本地运行类型化决策，不需要服务器或 API key。
- **[systemone-lite](https://github.com/fritzprix/systemone-lite)** · <sub>fritzprix · GitHub · ⭐ 3 · 2026-09-19</sub><br>System One API 的玩具级本地近似实现，后端是小型因果语言模型（默认 Qwen2.5-0.5B），在共享 KV 缓存的 state 上只为选项 token 打分，可选用微调后的 checkpoint。
- **[Tiny-Jev](https://huggingface.co/lostargon/Tiny-Jev)** · <sub>lostargon · Hugging Face · ♥ 3 · 2026-09-21</sub><br>基于 Qwen3-0.6B 的开放 0.6B System One 模型，以校准概率回答类型化问题：同类测试准确率 95.8%、ECE 0.004，分布外 93.5%。
- **[typed-decisions](https://github.com/kotoba-lang/typed-decisions)** · <sub>kotoba-lang · GitHub · ⭐ 3 · 2026-09-18</sub><br>对 Jev 形态（一个 state 配多个 Choice、Score 和 Noul 问题，一次前向作答）的轻量复现，覆盖 ModernBERT、DeBERTa 和 LLaDA-MoE，并实测延迟、校准和训练成本。
- **[把 Qwen3.8 用作 Jev 兼容端点](https://github.com/PixelML/club-170hx/tree/main/results/2026-09-20-qwen3.8-27b-w4a16-jev-1card-vllm)** · <sub>PixelML · GitHub · ⭐ 57 仓库 · 2026-08-30</sub><br>基准测试配方：在单张 CMP 170HX 卡上用 vLLM 把原版 Qwen3.8-27B W4A16 checkpoint 作为免训练的 Jev 兼容 /v1/systemone 端点提供服务，并附校准结果。
- **[ggmlc 的 Laya 引擎](https://github.com/monatis/ggmlc/tree/main/examples/laya)** · <sub>monatis · GitHub · ⭐ 46 仓库 · 2026-08-22</sub><br>神经网络编译器 ggmlc 中的一个示例，把开放的 Jev 替代品 Laya 编译成独立的 C++ 决策引擎，使用 GGUF 权重并提供兼容 TypeSafe 的 /v1/systemone 服务器；在 RTX 4050 笔记本 GPU 上每次决策约 25 毫秒。
- **[cu-Jev](https://github.com/dtunai/cu-Jev)** · <sub>dtunai · GitHub · ⭐ 2 · 2026-09-20</sub><br>C/CUDA 决策引擎，用手写 kernel 把开放的 Qwen3.5 检查点（0.8B 到 9B）变成兼容 Jev 的 /v1/systemone API，运行时不依赖 PyTorch，并附可复现的基准测试。
- **[Jev Distill Corpus v3](https://huggingface.co/datasets/SargeDev/jev-distill-corpus-v3)** · <sub>SargeDev · Hugging Face · ♥ 2 · 2026-09-21</sub><br>包含 740,957 行数据的类型化决策语料，采用 System One 的 noul/choice/score schema，大部分是覆盖 53 个领域的合成场景，由 Jev 1.13 通过 OpenRouter 标注，用于训练小型本地评判模型。
- **[jev-browser-local](https://github.com/rorshopping/jev-browser-local)** · <sub>rorshopping · GitHub · ⭐ 2 · 2026-09-18</sub><br>在 RTX 2060 SUPER 上把 jev-browser 跑在完全本地的 Jev 式决策引擎上，用 Qwen2.5-1.5B 做决策、Qwen2.5-0.5B 负责输入文字，附带一个保持浏览器常驻的分支、显存保护和运行轨迹。
- **[Laya 对比 Jev 基准测试](https://huggingface.co/datasets/Luni/laya-jev-benchmark)** · <sub>Luni · Hugging Face · ♥ 2 · 2026-09-19</sub><br>在 RTX 5090 上对照 Jev 公布的数据独立检验 Laya：原始 Laya 在 PhishNChips 钓鱼识别上接近随机水平（0.505），经过 Platt 校准后达到 0.611，Jev 为 0.626。
- **[metask-jev](https://github.com/metask-ai/metask-jev)** · <sub>metask-ai · GitHub · ⭐ 2 · 2026-09-21</sub><br>基于 Qwen3.5 的开放权重 Jev 级类型化决策模型，一次前向传播即可读出每个选项的校准概率；metask-jev-4b 在 JevBench 上报告 80.1%，Jev 1.13.0 为 75.3%。
- **[OpenJev (GPT-AGI)](https://github.com/GPT-AGI/OpenJev)** · <sub>GPT-AGI · GitHub · ⭐ 2 · 2026-09-20</sub><br>开源的 Jev 兼容决策引擎，在 /v1/systemone 接口后用开放权重模型一次前向回答 Choice、Score 和 Noul 问题，附带 Claude Code 风格的 REPL 和迷宫演示。
- **[Visual Jev](https://github.com/andrueandersoncs/visual-jev)** · <sub>andrueandersoncs · GitHub · ⭐ 2 · 2026-09-19</sub><br>基于 Qwen3-VL 主干、开放且本地运行的原生图像类型化决策，把关于图像的 Choice、Score 和 Noul 问题作为校准分布来回答，不生成文本。
- **[rlx-kev](https://github.com/MIT-RLX/rlx-models/tree/main/crates/rlx-kev)** · <sub>MIT-RLX · GitHub · ⭐ 34 仓库 · 2026-05-22</sub><br>Kev 的 Rust 移植版。Kev 是小型类 Jev System One 决策模型，采用 Qwen3.5 主干、合并后的 LoRA 和 pointer head，原生运行在 RLX 多后端 ML 编译器与运行时上。
- **[System One Mini](https://huggingface.co/DavidHatley/system-one-mini)** · <sub>David Hatley · Hugging Face · ⬇ 151 · 2026-09-16</sub><br>研究原型：69.3M 参数的 DistilBERT 编码器加五个类型化分类头，针对合成的软件诊断摘要做固定决策；明确声明不是 Jev 的复现。
- **[Jev-Gate Student B](https://huggingface.co/SargeDev/jev-gate-student-b)** · <sub>SargeDev · Hugging Face · ⬇ 111 · 2026-09-21</sub><br>在 Qwen2.5-0.5B 上的 LoRA，从 Jev 蒸馏成本地记忆相关性评判模型，输出校准的 P(relevant)，决定哪些向量召回的记忆可以进入 agent 上下文。
- **[bonzi-1.7b-v1-jev](https://huggingface.co/NicolaiMTLassen/bonzi-1.7b-v1-jev)** · <sub>NicolaiMTLassen · Hugging Face · ♥ 1 · 2026-09-20</sub><br>Bonsai 1.7B GGUF 的配方和测量数据（不含权重），把它作为 Jev 式类型化决策函数运行，一次前向传播为每个选项返回一个概率。
- **[bonzi-27b-v2-jev](https://huggingface.co/NicolaiMTLassen/bonzi-27b-v2-jev)** · <sub>NicolaiMTLassen · Hugging Face · ♥ 1 · 2026-09-20</sub><br>Ternary Bonsai 2 27B GGUF 的配方和测量数据（不含权重），把它作为 Jev 式类型化决策函数运行，每个决策只需一次前向传播。
- **[从零构建一个 Jev](https://huggingface.co/azharmo/build-jev-from-scratch)** · <sub>azharmo · Hugging Face · ♥ 1 · 2026-09-20</sub><br>对 System One 接口的 3.1M 参数玩具级重建，附训练、评测和服务代码以及一篇文章；准确率低是设计使然，但校准达到 ECE 0.027。
- **[Cerebellum-2B](https://github.com/mkeco/Cerebellum-2B)** · <sub>mkeco · GitHub · ⭐ 1 · 2026-09-19</sub><br>基于 Qwen3.5-2B 的开放权重 2B 决策模型，一次前向传播就从候选集中选出工具路由和 DOM 动作，定位为 Jev 的开放替代品，提供 BF16、FP8 和 INT8 权重。
- **[DecisionBridge](https://github.com/grishahq/decisionbridge)** · <sub>grishahq · GitHub · ⭐ 1 · 2026-09-17</sub><br>受 Jev 启发的适配器，把现有 LLM（OpenAI、Anthropic、OpenRouter、本地 MLX）变成给出显式选项分数的决策函数，可选用带标签样本做校准，并可设置人工复核阈值。
- **[INSTRUCT_JEV](https://github.com/ctaxnagomi/instruct-jev)** · <sub>ctaxnagomi · GitHub · ⭐ 1 · 2026-09-19</sub><br>指令语料，包含 119 条 Choice、Noul 和 Score 数据，整理自 TypeSafe 公开的 Jev 文档，以 HuggingFace 数据集形式发布。
- **[Jev-Omni](https://huggingface.co/akhilaaa3/Jev-Omni)** · <sub>akhilaaa3 · Hugging Face · ♥ 1 · 2026-09-20</sub><br>基于 Gemma 4 12B 的多模态决策分类器，针对文本、图像、音频和视频问题为每个选项返回一个概率；在 DecisionBench Medium 上 87.57%，在 JevBench 上 86.15%。
- **[jevify-gemma4-26b-a4b](https://huggingface.co/kushalpatil/jevify-gemma4-26b-a4b)** · <sub>kushalpatil · Hugging Face · ♥ 1 · 2026-09-20</sub><br>经过微调（LoRA，已合并）的 Gemma 4 26B-A4B，能对类型化问题给出诚实的概率；它是 jevify 背后的模型，jevify 是一个本地、兼容 Jev 的 /v1/systemone 决策 API。
- **[jevinf](https://github.com/zerodegress/jevinf)** · <sub>zerodegress · GitHub · ⭐ 1 · 2026-09-19</sub><br>类 Jev 决策模型的推理引擎，把每条候选路径拆成分段前向计算并复用前缀，对外提供 Jev 的线上协议，在 MPS 上配合 NanoJev 实测快 2.57 倍。
- **[jevlike-esp32](https://github.com/david-cermak/jevlike-esp32)** · <sub>david-cermak · GitHub · ⭐ 1 · 2026-09-18</sub><br>实验：把在 Python 中训练的 jevlike 文本打分器导出为 ESP-IDF 固件，包含 C 语言打分器和主机端校验，在 ESP32 微控制器上运行单遍选项决策。
- **[jevlite 数据集](https://huggingface.co/datasets/vagmi/jevlite_dataset)** · <sub>vagmi · Hugging Face · ♥ 1 · 2026-09-20</sub><br>合成数据集，包含针对 978 个程序 state（工单、SIEM 告警、发票、agent 对话记录、代码审查）的 5,866 个类型化问题，附完整的老师模型分布，用于训练 jev-lite。
- **[open-system-one-bench](https://huggingface.co/datasets/dylantom2012/open-system-one-bench)** · <sub>dylantom2012 · Hugging Face · ♥ 1 · 2026-09-21</sub><br>六套技术栈在 10,000 个分类与路由决策上的逐条预测，包括 typesafe/jev 和 Laya 在相同条目上的结果，无需花 API 费用即可重跑显著性检验。
- **[openjev-experiments](https://github.com/zefir1990/openjev-experiments)** · <sub>zefir1990 · GitHub · ⭐ 1 · 2026-09-17</sub><br>自包含脚本，在本地运行 Qwen3.5-4B cross-encoder AlexWortega/openjev，用于自然语言推理和多选重排，并提供 CLI。
- **[PocketJev](https://github.com/NullPo-jp/PocketJev)** · <sub>NullPo-jp · GitHub · ⭐ 1 · 2026-09-17</sub><br>实验性 iOS 应用，通过 MLX 在设备端运行 Qwen3-VL，把一帧摄像头画面、一个问题和 2-26 个选项转成从下一个 token logits 读出的相对分数，耗时约一秒，不保存照片。
- **[System One：只编码一次，并行决策](https://huggingface.co/spaces/jasonkneen/open-jev)** · <sub>jasonkneen · 应用 · ♥ 1 · 2026-09-18</sub><br>展示 pngwn 的 System One 打分器为何便宜的推理路径：state 只编码一次，所有选项并行打分，并与生成相同答案的 instruct 模型并排对比。
- **[System One 训练数据对](https://huggingface.co/datasets/shreyanbr/system-one-training-pairs)** · <sub>shreyanbr · Hugging Face · ⬇ 93 · 2026-09-19</sub><br>DeBERTa System One cross-encoder 的训练包：金标准前提-假设对、Claude Haiku 4.5 蒸馏标签、固定的 Banking77 和工具选择数据划分，以及微调代码。
- **[jevify-gemma4-e4b](https://huggingface.co/kushalpatil/jevify-gemma4-e4b)** · <sub>kushalpatil · Hugging Face · ⬇ 85 · 2026-09-20</sub><br>经过微调（LoRA，已合并）的 Gemma 4 E4B，能对类型化问题给出诚实的概率，由 jevify 作为本地、兼容 Jev 的 /v1/systemone 决策 API 提供服务。
- **[AINode System One API](https://github.com/getainode/ainode/blob/main/ainode/api/systemone.py)** · <sub>getainode · GitHub · ⭐ 15 仓库 · 2026-04-12</sub><br>兼容 System One 的 decide API，属于面向 NVIDIA GPU 的自托管 AI 平台 AINode，在 110 个带标签的决策上与本地 35B 聊天模型做了对比：托管版 Jev 准确率 0.964、Brier 0.024，在 0.9 阈值下 80 个中错 0 个。
- **[hedos 的 System One 网关](https://github.com/theiskaa/hedos/blob/main/gateway/src/handlers/systemone.rs)** · <sub>theiskaa · GitHub · ⭐ 14 仓库 · 2026-07-05</sub><br>无界面的本地模型引擎，其网关暴露 TypeSafe 的 POST /v1/systemone，因此指向它的 TypeSafe SDK 会从一个具备 judge 能力的本地模型拿到答案。
- **[leCore holographic System One](https://github.com/AnOversizedMooseWithSocks/leCore/blob/main/holographic/agents_and_reasoning/holographic_systemone.py)** · <sub>AnOversizedMooseWithSocks · GitHub · ⭐ 11 仓库 · 2026-06-08</sub><br>在纯 NumPy 向量引擎里原生实现 Jev 的“state + 类型化问题”约定，形式是一个 few-shot 原型分类器：遇到平票时弃权，未校准前不返回概率。
- **[SparkStation 决策模型](https://github.com/kshetrajna12/sparkstation/blob/main/supervisor/launchers/reflex_launcher.py)** · <sub>kshetrajna12 · GitHub · ⭐ 8 仓库 · 2025-10-27</sub><br>面向 NVIDIA DGX Spark 的模型集群管理器，在其 OpenAI 兼容网关旁边，通过兼容 TypeSafe Jev 的 POST /v1/systemone 端点提供 Reflex 等决策模型服务。
- **[AgentKthx 的 JEV API 模式](https://github.com/VTSTech/AgentKthx/blob/main/docs/JEV_API_MODE.md)** · <sub>VTSTech · GitHub · ⭐ 5 仓库 · 2026-03-20</sub><br>本地优先的 agent 框架 AgentKthx 中的一个模式，通过包装约束提示词并解析决策信封，用任意聊天 LLM（Ollama、ZAI、OpenRouter、llama-server）模拟 Jev 的 System One 决策格式。
- **[System One (distilled)](https://huggingface.co/shreyanbr/system-one-distilled)** · <sub>shreyanbr · Hugging Face · ⬇ 25 · 2026-09-19</sub><br>针对 Jev /v1/systemone schema 的 70.8M DeBERTa-v3-xsmall cross-encoder，用 Claude Haiku 4.5 的答案训练，用来比较蒸馏与金标准标签的效果。
- **[jev-0.5b](https://huggingface.co/jaswanthsanjay88/jev-0.5b)** · <sub>jaswanthsanjay88 · Hugging Face · ⬇ 22 · 2026-09-19</sub><br>基于 Qwen2.5-0.5B、只做 prefill 的 Jev 式决策模型：一个 LoRA 适配器加指针读出头，配合块因果注意力，一次计算回答多个问题，对外提供 /v1/systemone API。
- **[jev-my-bro 治理数据集](https://huggingface.co/datasets/JonusNattapong/jev-my-bro-dataset)** · <sub>JonusNattapong · Hugging Face · ⬇ 17 · 2026-09-21</sub><br>英语/泰语数据集，包含 8,508 个案例和 34,032 个类型化决策，判断 agent 操作应当执行、询问用户还是拒绝，是否需要复核、是否被禁止，以及风险有多高。
- **[System One (gold)](https://huggingface.co/shreyanbr/system-one-gold)** · <sub>shreyanbr · Hugging Face · ⬇ 16 · 2026-09-19</sub><br>针对 Jev /v1/systemone schema 的 70.8M DeBERTa-v3-xsmall cross-encoder，用各数据集自带的标签训练，是一项 Jev 对比 Haiku 基准研究中的金标准监督组。
- **[System One (zeroshot)](https://huggingface.co/shreyanbr/system-one-zeroshot)** · <sub>shreyanbr · Hugging Face · ⬇ 15 · 2026-09-19</sub><br>实现 Jev /v1/systemone schema 的 70.8M DeBERTa-v3-xsmall cross-encoder 的无监督基线，一次批处理前向回答 Choice、Score 和 Noul。
- **[jev-qwen3.5-4b-legal-lora](https://huggingface.co/Nebulaw1/jev-qwen3.5-4b-legal-lora)** · <sub>Nebulaw1 · Hugging Face · ⬇ 1 · 2026-09-20</sub><br>Qwen3.5-4B-Base 上的 QLoRA 适配器，用于有限选项的中文法律判断，一次前向传播给候选字母打分，而不是生成法律推理，附评测和推理脚本。
- **[AgentJev](https://huggingface.co/aimeigaoshou/agent-jev)** · <sub>aimeigaoshou · Hugging Face · 2026-09-21</sub><br>开放的 0.6B agent 决策模型，带共享前缀缓存，能为“下一步用哪个工具”这类问题返回概率分布；在 2,000 道 Typed Decisions 题上 top-1 准确率为 79.25%，Jev 1.13.0 为 72.7%。
- **[bonzi-27b-v1-jev](https://huggingface.co/NicolaiMTLassen/bonzi-27b-v1-jev)** · <sub>NicolaiMTLassen · Hugging Face · 2026-09-20</sub><br>Bonsai 1 27B GGUF 的配方和测量数据（不含权重），把它作为 Jev 式类型化决策函数运行，一次前向传播为每个选项返回一个概率。
- **[bonzi-4b-v1-jev](https://huggingface.co/NicolaiMTLassen/bonzi-4b-v1-jev)** · <sub>NicolaiMTLassen · Hugging Face · 2026-09-20</sub><br>Bonsai 1 4B GGUF 的配方和测量数据（不含权重），把它作为 Jev 式类型化决策函数运行，一次前向传播为每个选项返回一个概率。
- **[bonzi-8b-ternary-v1-jev](https://huggingface.co/NicolaiMTLassen/bonzi-8b-ternary-v1-jev)** · <sub>NicolaiMTLassen · Hugging Face · 2026-09-20</sub><br>Ternary Bonsai 1 8B GGUF 的配方和测量数据（不含权重），把它作为 Jev 式类型化决策函数运行，一次前向传播为每个选项返回一个概率。
- **[bonzi-8b-v1-jev](https://huggingface.co/NicolaiMTLassen/bonzi-8b-v1-jev)** · <sub>NicolaiMTLassen · Hugging Face · 2026-09-20</sub><br>Bonsai 1 8B GGUF 的配方和测量数据（不含权重），把它作为 Jev 式类型化决策函数运行，一次前向传播为每个选项返回一个概率。
- **[jev-agent-lab](https://github.com/michael54/jev-agent-lab)** · <sub>michael54 · GitHub · 2026-09-19</sub><br>可复现的 Runpod 部署，把开放的 Jev 式 SemIf 模型与官方 Jev 客户端放在一起，附 agent 决策案例、延迟测量和一份 Jev 对比 SemIf 的报告。
- **[jev-gemma-4-E2B-it-choice-64](https://huggingface.co/ohtaman/jev-gemma-4-E2B-it-choice-64)** · <sub>ohtaman · Hugging Face · 2026-09-22</sub><br>面向浏览器的 Gemma 4 E2B ONNX 产物，把输出投影限制在 64 个固定答案 token 上，无需微调就把它变成纯文本的固定标签打分器。
- **[jev-local-lab 决策头](https://huggingface.co/mchen04/jev-local-lab-decision-heads)** · <sub>mchen04 · Hugging Face · 2026-09-21</sub><br>极小的训练头（0.2 到 1.3M 参数），在一台 24 GB 的 Mac mini 上从 4-bit Qwen2.5-1.5B 中读出结构化决策，作为一个文档齐全的业余项目发布，并如实写明局限。
- **[jev-my-bro](https://huggingface.co/JonusNattapong/jev-my-bro)** · <sub>JonusNattapong · Hugging Face · 2026-09-21</sub><br>可自托管的英语/泰语决策模型，用于 agent 和工具治理，判断某个操作是执行、请求批准、拒绝还是升级处理；v0.2 报告准确率 73.78%。
- **[jev-typed-decisions-causal-0.6b](https://huggingface.co/abidlabs/jev-typed-decisions-causal-0.6b)** · <sub>abidlabs · Hugging Face · 2026-09-21</sub><br>Qwen3-0.6B-Base 上的 LoRA 适配器，采用 pngwn 的 typed-decisions 实验中 arm-B 缓存因果类型化打分器的配方训练，是一个冻结 LM head 的类 Jev 复刻。
- **[Jev-Vision](https://huggingface.co/SeanLiu/Jev-Vision)** · <sub>SeanLiu · Hugging Face · 2026-09-21</sub><br>开放权重的视觉决策模型（在 Qwen3-VL-8B 上加 LoRA 和类型化头），通过兼容 Jev 的 /v1/systemone API 回答关于截图和图像的类型化问题，每个屏幕步骤 150-190 毫秒。
- **[jevify-qwen3-vl-2b (Tier 0)](https://huggingface.co/Praveenrajus/jevify-qwen3-vl-2b)** · <sub>Praveenrajus · Hugging Face · 2026-09-21</sub><br>无需训练的 Jevify 配方，用 Qwen3-VL-2B 回答关于图像的类型化问题，从同一个位置读出每个允许的答案，并使用在验证集上拟合的校准。
- **[jevify-qwen3-vl-2b-t2](https://huggingface.co/Praveenrajus/jevify-qwen3-vl-2b-t2)** · <sub>Praveenrajus · Hugging Face · 2026-09-22</sub><br>Tier 2 的 Jevify 视觉模型：在 Qwen3-VL-2B 上加一个 rank-16 解码器 LoRA，在 A-OKVQA 上针对受限答案读出、用严格评分规则（proper scoring rules）训练，用于回答关于图像的类型化问题。
- **[jevify-qwen3.5-2b](https://huggingface.co/Praveenrajus/jevify-qwen3.5-2b)** · <sub>Praveenrajus · Hugging Face · 2026-09-21</sub><br>Qwen3.5-2B 的 Jevify 决策头，针对一个 state 回答 choice、score 和 noul 问题，返回校准的概率分布，不生成文本。
- **[jevify-qwen3.5-4b](https://huggingface.co/Praveenrajus/jevify-qwen3.5-4b)** · <sub>Praveenrajus · Hugging Face · 2026-09-21</sub><br>Qwen3.5-4B 的 Jevify 决策头，读取 state，回答 choice、score 和 noul 问题并返回校准的分布，只发布加在基础模型之上的决策头。
- **[jevify-qwen3.5-4b-t2](https://huggingface.co/Praveenrajus/jevify-qwen3.5-4b-t2)** · <sub>Praveenrajus · Hugging Face · 2026-09-22</sub><br>面向 Qwen3.5-4B 的 Tier 2 Jevify 模型，在决策头之上再加一个 LoRA 适配器，返回校准的 choice、score 和 noul 分布。
- **[JevOne](https://huggingface.co/juspay/jev-one)** · <sub>juspay · Hugging Face · 2026-09-21</sub><br>基于 Qwen3.6-35B-A3B 的类型化决策模型，通过兼容 TypeSafe 的 /v1/systemone API 提供服务，采用单 token 候选读出、正反两种选项顺序评估以及校准。
- **[jevons-lfm25-1.2b-systemone](https://huggingface.co/gopalanj/jevons-lfm25-1.2b-systemone)** · <sub>gopalanj · Hugging Face · 2026-09-20</sub><br>LFM2.5-1.2B 上的种子 LoRA，用于 jevons：一个本地 System One 服务器，从 logits 给允许的结果打分，再用代码组装 choice、概率、置信度、noul 和 score。
- **[jqv](https://github.com/Octalab-Inc/jqv)** · <sub>Octalab-Inc · GitHub · 2026-09-21</sub><br>在原版 Qwen3 上重建 Jev 的推理结构：共享一次 state prefill，用块注意力掩码隔离各个问题分支，并用温度校准选项字母的 logits，对外提供 /v1/systemone。
- **[Laya 玩 Doom](https://medium.com/@christian.graham_49279/laya-a-free-local-alternative-to-jev-and-it-can-even-play-doom-ish-42e2292e541e)** · <sub>Christian Graham · 文章 · 2026-09-18</sub><br>让开放的 421M 参数 Jev 替代品 Laya 在本地玩 Doom 来测试它，并加入专门的射击问题和带日志的规则覆盖，修复误射和卡死循环。
- **[layaForWeb](https://medium.com/@visrow/jev-vs-laya-live-demo-i-ran-a-421-million-parameter-ai-decision-model-inside-a-browser-tab-no-84b86bed1f10)** · <sub>Vishal Mysore · 文章 · 2026-09-21</sub><br>借助 ONNX Runtime Web 和 WebAssembly，在浏览器标签页里运行 421M 参数的开放 Laya 决策模型，并与 Jev 的 playground 并排展示；浏览器版本在全部 14 个问题上的首选答案都与 PyTorch 一致。
- **[local-system-one-student](https://huggingface.co/Mannedood/local-system-one-student)** · <sub>Mannedood · Hugging Face · 2026-09-18</sub><br>从本地 LLM 蒸馏出的 149M ModernBERT 编码器，针对一个固定 schema（编程 agent 的下一步）复现 Jev 的接口，在 19 毫秒 内返回工具选择、紧急程度和破坏性操作标记。
- **[open-system-one demo](https://huggingface.co/spaces/dylantom2012/open-system-one-demo)** · <sub>dylantom2012 · 应用 · 2026-09-21</sub><br>对比 0.1 毫秒 的训练版决策头与零样本 cross-encoder 的演示，出自一项将 Jev 与纯 CPU 开放替代方案对比的独立基准测试。
- **[open-system-one results explorer](https://huggingface.co/spaces/dylantom2012/open-system-one)** · <sub>dylantom2012 · 应用 · 2026-09-21</sub><br>一项独立基准测试的交互式结果浏览器：在 10,000 个决策上对比 TypeSafe 的 Jev 与纯 CPU 的开放技术栈。
- **[smalljev](https://github.com/isHeSatoshi/smalljev)** · <sub>isHeSatoshi · GitHub · 2026-09-20</sub><br>基于 MiniCPM5-2B-Base 的开放 Jev 风格决策模型，带 LoRA adapter 和原生决策头，约 2.5B 参数，一次前向即可作答、不生成 token，目标是在手机上运行。
- **[System One (phase2 student)](https://huggingface.co/lafalce/system-one-model)** · <sub>lafalce · Hugging Face · 2026-09-19</sub><br>基于 ModernBERT-base 加 LoRA 和两层打分头的本地决策模型，接受 JSON 或文本形式的 state，一次前向回答类型化 choice、score 和 noul 问题。
- **[System One vs Laya vs DeepSeek](https://huggingface.co/spaces/henrybit/jev-vs-deepseek)** · <sub>henrybit · 应用 · 2026-09-22</sub><br>中文 Space，在同一 state 和类型化问题上对比三条决策路径：pngwn 的开放 System One 打分器、Laya，以及通过 chat completions 返回 JSON 的 DeepSeek。
- **[system-one-270m](https://huggingface.co/kaivoss/system-one-270m)** · <sub>kaivoss · Hugging Face · 2026-09-21</sub><br>基于 Gemma 3 270M 的开放 System One 复现，接收 state 和带调用方选项的类型化问题，返回一个选项及其校准概率，从不输出自由文本。
- **[system-one-270m-data](https://huggingface.co/datasets/kaivoss/system-one-270m-data)** · <sub>kaivoss · Hugging Face · 2026-09-21</sub><br>包含 25,002 个类型化决策的合成数据集，每个决策带有针对调用方选项的软目标分布，以字母选项提示词的形式呈现，用于训练开放的 system-one-270m 模型。
- **[system-one-adapter (Rust)](https://github.com/codeitlikemiley/system-one-adapter-rust)** · <sub>codeitlikemiley · GitHub · 2026-09-16</sub><br>system-one-adapter 的 Rust 移植版：以 LLM API 为后端、可直接替换 TypeSafe system_one 调用的实现，问题、答案、重试和错误类型都保持兼容，便于比较成本、速度和质量。
- **[tiny-jev](https://github.com/karimatayuta/tiny-jev)** · <sub>karimatayuta · GitHub · 2026-09-18</sub><br>面向日语文本的小型本地判断模型，基于 Qwen3 的是/否分数并通过 LoRA 训练，返回 choice、score 和 noul 答案；在业务数据和校准到位之前会选择弃权。

</details>

还缺什么？[提交一个资源](https://github.com/Li-Evan/awesome-jev/issues/new/choose)。
