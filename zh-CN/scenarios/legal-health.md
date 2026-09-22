# 🔬 法律、医疗与科研

[English](https://github.com/Li-Evan/awesome-jev/blob/main/scenarios/legal-health.md) · **简体中文**

合规检查、医学与科学筛查，以及科研工作流。共 28 条，按社区热度排序。

[← 返回 Awesome Jev](https://github.com/Li-Evan/awesome-jev/blob/main/README.zh-CN.md#按场景浏览)

<table>
<tr>
<td width="260" valign="top"><a href="https://1kpapers.com"><img src="https://www.1kpapers.com/opengraph-image.png?opengraph-image.1mk7bn86uhq5h.png" alt="1kpapers" width="240"></a></td>
<td valign="top"><b><a href="https://1kpapers.com">1kpapers</a></b><br><sub>nutlope · 应用 · ♥ 2k · 2026-09-17</sub><br>按主题梳理 2025-2026 年 1,018 篇 AI 研究论文的网站，每篇论文先由 DeepSeek V4 Flash 总结，再由 Jev 分到 24 个主题中，总花费 $0.08。<br><sub><b>Jev 用法:</b> 每篇论文一个 Choice，输入标题加摘要加 24 个主题选项，中位延迟 256 毫秒。</sub><br><sub>相关: <a href="https://x.com/nutlope/status/2100426999546184123">demo</a> · <a href="https://x.com/nutlope/status/2100426999546184123">demo 2</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/Paiky16/status/2101628198928982219"><img src="https://praneeth16.github.io/jev/og.png" alt="结合 GEPA 检测药物不良反应" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/Paiky16/status/2101628198928982219">结合 GEPA 检测药物不良反应</a></b><br><sub>Paiky16 · X · ♥ 138 · 2026-09-20</sub><br>用 Jev 标记医学文献中报告疑似药物不良反应的句子，再用 GEPA 提示词优化把 F1 从 69.1% 提升到 79.7%，误报从 47 个降到 22 个。<br><sub>相关: <a href="https://praneeth16.github.io/blog/adapting-jev-with-gepa">article</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/rheum_ai/status/2100454043361722798"><img src="https://pbs.twimg.com/amplify_video_thumb/2100452479016321024/img/nAyq81QFzA6UzPqM.jpg" alt="实时临床问诊分类器" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/rheum_ai/status/2100454043361722798">实时临床问诊分类器</a></b><br><sub>rheum_ai · X · ♥ 432 · 2026-09-17</sub><br>原型：在临床问诊过程中把环境记录（ambient scribe）的转录稿喂给 Jev，实时遍历医学本体、分类症状、更新鉴别诊断并标出危险信号。</td>
</tr>
<tr>
<td width="260" valign="top"></td>
<td valign="top"><b><a href="https://x.com/juanmacias/status/2100463318209048850">在西班牙法律语料上测试 Jev</a></b><br><sub>juanmacias · 文章 · ♥ 87 · 2026-09-17</sub><br>为期一天的实地测试，在西班牙法律语料上用 Jev 给出的概率替换手工搭建的正则分类器，并报告哪些站得住、哪些出了问题，以及团队自己的标签哪里错了。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/rothken/status/2102151333193363791"><img src="https://lawanalyzer.com/social-card.png" alt="LawAnalyzer" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/rothken/status/2102151333193363791">LawAnalyzer</a></b><br><sub>rothken · X · ♥ 51 · 2026-09-21</sub><br>一家律所 AI 实验室推出的免费测试版构建套件，用于在 Jev 上搭建法律分析小程序，输出可复用的 JSON 和 Jev 代码，律师和学生可以保存并改编。<br><sub>相关: <a href="https://lawanalyzer.com/">app</a> · <a href="https://lawanalyzer.com">project</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/luwill/research-skills/tree/main/lit-search/src/litsearch"><img src="https://opengraph.githubassets.com/1/luwill/research-skills" alt="lit-search 的 Jev 筛选" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/luwill/research-skills/tree/main/lit-search/src/litsearch">lit-search 的 Jev 筛选</a></b><br><sub>luwill · GitHub · ⭐ 844 仓库 · 2026-01-13</sub><br>这个 research-skills 合集中的 lit-search skill 把文献纳入/排除标准编译成 Jev 问题，并给每条记录筛出一个结论。<br><sub><b>Jev 用法:</b> 每条记录一次请求、一个 Verdict，只打分一次并写入 jev_scores.jsonl，之后调整阈值、分拣和评测都复用同一批分数，无需新的网络调用。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/choxos/jev-reviewer"><img src="https://raw.githubusercontent.com/choxos/jev-reviewer/main/documentation/tour.gif" alt="Jev Reviewer" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/choxos/jev-reviewer">Jev Reviewer</a></b><br><sub>choxos · GitHub · ⭐ 32 · 2026-09-18</sub><br>用于系统综述的浏览器内数据提取工具，回答提取表单或 RoB 2、ROBINS-I、QUADAS-2、TIDieR 模板中的问题，并给出来自试验报告的原文引述和页码位置。<br><sub><b>Jev 用法:</b> Jev 选出候选行 ID，再由代码复制原文，所以每个答案都是可核对的引文。</sub><br><sub>相关: <a href="https://x.com/ASofiMahmudi/status/2100985031703269425">demo</a> · <a href="https://jevreviewer.xera.ac">app</a> · <a href="https://jevreviewer.xera.ac">app 2</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/stella/stella/blob/main/apps/api/src/lib/workflow/decisions/system-one.ts"><img src="https://opengraph.githubassets.com/1/stella/stella" alt="stella 的 System One 决策" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/stella/stella/blob/main/apps/api/src/lib/workflow/decisions/system-one.ts">stella 的 System One 决策</a></b><br><sub>stella · GitHub · ⭐ 250 仓库 · 2026-05-03</sub><br>开源法律工作台，只在代码做不了判断时才问 Jev，比如引用法院如何对待某个判决、某段文字确定了哪个选项、某个问题指的是哪个提取出的日期。<br><sub>相关: <a href="https://stll.app">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/JunMa11/MedJev"><img src="https://opengraph.githubassets.com/1/JunMa11/MedJev" alt="MedJev" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/JunMa11/MedJev">MedJev</a></b><br><sub>JunMa11 · GitHub · ⭐ 11 · 2026-09-22</sub><br>基于开放的 Kev 代码构建的类 Jev 模型，在医院内部用一张消费级 GPU 从自由文本病历中提取可直接入表的临床变量，并附一个本地应用，将其与托管版 Jev 和基础版 Qwen3.5-0.8B 对比。<br><sub><b>Jev 用法:</b> 每份病历包含 Noul、Choice 和 Score 字段（入院、诊断方式、症状严重程度）；托管版 Jev 作为基线。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/fighthealthinsurance/fighthealthinsurance/blob/main/fighthealthinsurance/ml/typesafe.py"><img src="https://opengraph.githubassets.com/1/fighthealthinsurance/fighthealthinsurance" alt="Fight Health Insurance 申诉打分" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/fighthealthinsurance/fighthealthinsurance/blob/main/fighthealthinsurance/ml/typesafe.py">Fight Health Insurance 申诉打分</a></b><br><sub>fighthealthinsurance · GitHub · ⭐ 156 仓库 · 2023-03-16</sub><br>帮助人们对医疗保险拒赔提出申诉的 Django 应用，按 TypeSafe 质量分给生成的申诉草稿排序，并按后端追踪打分的健康状况。<br><sub><b>Jev 用法:</b> 脱敏后的申诉文件只通过 https 发送；从不读取错误响应体。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/DevaiahShrithan/status/2102097862805053950"><img src="https://pbs.twimg.com/media/HSwmC5JawAArib5.jpg" alt="让 Jev 读完每一篇 AI 论文" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/DevaiahShrithan/status/2102097862805053950">让 Jev 读完每一篇 AI 论文</a></b><br><sub>DevaiahShrithan · 文章 · ♥ 6 · 2026-09-21</sub><br>把 1993 到 2026 年的 464,720 篇 arXiv AI 摘要交给 Jev，每篇问五个问题（是否声称达到 SOTA、是否发布代码、是否像 LLM 写的、论文类型、炒作程度），描绘 AI 论文的变化。<br><sub><b>Jev 用法:</b> 每篇摘要两个 Noul、一个 Choice 和一个 Score，每次请求 16 篇摘要，单次调用得到 80 个答案。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/JamesANZ/medical-mcp/tree/main/src/rank"><img src="https://opengraph.githubassets.com/1/JamesANZ/medical-mcp" alt="Medical MCP 的 JEV 重排器" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/JamesANZ/medical-mcp/tree/main/src/rank">Medical MCP 的 JEV 重排器</a></b><br><sub>JamesANZ · GitHub · ⭐ 113 仓库 · 2025-07-14</sub><br>提供 FDA、WHO、PubMed 和 RxNorm 数据的 MCP 服务器，可以用 Jev 重排文献检索结果，根据问题判断每篇摘要是保留、降级还是丢弃。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/sboghossian/legal-ai-model-router"><img src="https://opengraph.githubassets.com/1/sboghossian/legal-ai-model-router" alt="Legal AI Model Router" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/sboghossian/legal-ai-model-router">Legal AI Model Router</a></b><br><sub>sboghossian · GitHub · ⭐ 5 · 2026-07-14</sub><br>一组 Claude Code skill，为法律起草、信息提取、法律研究、审阅或翻译推荐该用哪个 LLM，并可选接入 Jev 分类器，判断任务所属的垂直领域、风险高低以及是否属于法律工作。<br><sub><b>Jev 用法:</b> 每次调用约 $0.00002、约 700 毫秒；在固定测试集上 11/11，阿拉伯语、法语和英语表现相当。只是可选组件，从不作为依赖。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/MarissaFamularo/citation-verifier"><img src="https://opengraph.githubassets.com/1/MarissaFamularo/citation-verifier" alt="Paper Trellis Citation Verifier" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/MarissaFamularo/citation-verifier">Paper Trellis Citation Verifier</a></b><br><sub>MarissaFamularo · GitHub · ⭐ 5 · 2026-09-17</sub><br>面向同行评审者和作者的工具，把稿件中的每个引用句与被引论文配对，由 Claude 找出支持段落、Jev 评估它是否支持该论断，最后记录人工结论。<br><sub>相关: <a href="https://verify.papertrellis.com">app</a> · <a href="https://verify.papertrellis.com">app 2</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/doitrous/hx"><img src="https://opengraph.githubassets.com/1/doitrous/hx" alt="Hx" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/doitrous/hx">Hx</a></b><br><sub>doitrous · GitHub · ⭐ 3 · 2026-09-20</sub><br>面向病史、体格检查和手术记录的自动打勾清单：按病历需要展开相应问题，用 Jev 对照医生写下的内容逐项打勾，并显示哪些还没记录。<br><sub>相关: <a href="https://hx.semicoded.com">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/thenewpotato/privacy-facts"><img src="https://opengraph.githubassets.com/1/thenewpotato/privacy-facts" alt="Privacy Facts" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/thenewpotato/privacy-facts">Privacy Facts</a></b><br><sub>thenewpotato · GitHub · ⭐ 2 · 2026-09-18</sub><br>Web 应用，把粘贴进来的隐私政策 URL 或文本变成类似营养成分表的标签，用大白话回答问题，每条都附 Jev 置信度分数和可展开的原文摘录。<br><sub>相关: <a href="https://tigrw.com/privacy-facts/">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/endomorphosis/ipfs_datasets_py/blob/main/ipfs_datasets_py/logic/integrations/typesafe_advisor.py"><img src="https://opengraph.githubassets.com/1/endomorphosis/ipfs_datasets_py" alt="IPFS Datasets 的 TypeSafe 公式检查" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/endomorphosis/ipfs_datasets_py/blob/main/ipfs_datasets_py/logic/integrations/typesafe_advisor.py">IPFS Datasets 的 TypeSafe 公式检查</a></b><br><sub>endomorphosis · GitHub · ⭐ 23 仓库 · 2024-04-07</sub><br>建议性的 TypeSafe lint，位于 IPFS Datasets 逻辑模块中，给从法律文本自动形式化得到的公式打分，判断它是否准确表达了原条款，并检查引用，但不会改写公式，也不会认定证明成立。<br><sub>相关: <a href="https://github.com/endomorphosis/ipfs_datasets_py">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/PistachioAIHQ/jev-synergy-screening"><img src="https://opengraph.githubassets.com/1/PistachioAIHQ/jev-synergy-screening" alt="Jev × Cohen ADHD 摘要筛选" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/PistachioAIHQ/jev-synergy-screening">Jev × Cohen ADHD 摘要筛选</a></b><br><sub>PistachioAIHQ · GitHub · ⭐ 1 · 2026-09-16</sub><br>系统综述筛选演示，让 Jev 决定一项 ADHD 药物综述中 MEDLINE 标题和摘要的纳入或排除，并以 Cohen et al. 2006 的标签评分；在 200 篇摘要的集合上准确率 92.0%、召回率 80.0%。<br><sub><b>Jev 用法:</b> 把 Choice 和 Noul 资格问题合成纳入/排除决策，每次调用约 523 毫秒。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/longkou1988/cnki-skills/tree/main/skills/cnki-jev"><img src="https://opengraph.githubassets.com/1/longkou1988/cnki-skills" alt="cnki-jev" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/longkou1988/cnki-skills/tree/main/skills/cnki-jev">cnki-jev</a></b><br><sub>longkou1988 · GitHub · ⭐ 16 仓库 · 2026-09-09</sub><br>面向 Codex 和 Claude Code 的知网（CNKI）文献工作流 skill 包的可选扩展，用 Jev 按纳入标准预筛论文，把复杂判断交回给 LLM 或人工复核者。<br><sub>相关: <a href="https://github.com/longkou1988/cnki-skills">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/healthkey-ai/promop/blob/dev/omop_core/mapping/suggestions.py"><img src="https://opengraph.githubassets.com/1/healthkey-ai/promop" alt="PRomop 的 Jev 概念排序" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/healthkey-ai/promop/blob/dev/omop_core/mapping/suggestions.py">PRomop 的 Jev 概念排序</a></b><br><sub>healthkey-ai · GitHub · ⭐ 9 仓库 · 2025-09-16</sub><br>基于 OMOP 的肿瘤患者病历平台，在映射源术语时可以用 Jev 给候选标准词表概念（例如 LOINC 编码）排序，替代 Anthropic 或与其并用。<br><sub>相关: <a href="https://github.com/healthkey-ai/promop">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/rlfordon/citation-verifier/tree/main/scratch/jev"><img src="https://opengraph.githubassets.com/1/rlfordon/citation-verifier" alt="Citation Verifier 中的 Jev 实验" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/rlfordon/citation-verifier/tree/main/scratch/jev">Citation Verifier 中的 Jev 实验</a></b><br><sub>rlfordon · GitHub · ⭐ 6 仓库 · 2026-02-07</sub><br>在一个法律引文核查工具中做的实验，测试 Jev 能否预筛被引用的法院判决是否支持诉状中的论点，并在 95 条人工标注的论断上测量成本和耗时。<br><sub><b>Jev 用法:</b> 每条论断针对论点、诉状原句和整份判决提出七个原子问题；用作影子评分标准和自动放行（auto-green）关卡。</sub><br><sub>相关: <a href="https://github.com/rlfordon/citation-verifier">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/johnhughes3/LegalForecastBench/blob/main/docs/jev-mode.md"><img src="https://opengraph.githubassets.com/1/johnhughes3/LegalForecastBench" alt="LegalForecastBench 的 Jev 模式" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/johnhughes3/LegalForecastBench/blob/main/docs/jev-mode.md">LegalForecastBench 的 Jev 模式</a></b><br><sub>johnhughes3 · GitHub · ⭐ 5 仓库 · 2026-09-17</sub><br>一个预测联邦驳回起诉动议（motion to dismiss）裁决的基准测试中的官方 Jev 条件：Jev 拿到一份案件记录（全文或 LLM 摘要），并用按诉求-被告计算的 micro-Brier 指标评分。<br><sub><b>Jev 用法:</b> 每个预测单元一个 Boolean 问题；原生的 yes 概率即为 probability_fully_dismissed。</sub><br><sub>相关: <a href="https://github.com/johnhughes3/LegalForecastBench">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/bnistor4/fotocopiatrice"><img src="https://opengraph.githubassets.com/1/bnistor4/fotocopiatrice" alt="Fotocopiatrice" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/bnistor4/fotocopiatrice">Fotocopiatrice</a></b><br><sub>bnistor4 · GitHub · 2026-09-21</sub><br>静态网站，读取意大利众议院就 2025 年预算法提交的全部 5,082 条修正案，找出完全相同或改写后等价的文本，并展示是谁签署的；Jev 分析共调用 12,206 次，花费 $0.84。<br><sub>相关: <a href="https://fotocopiatrice.vercel.app/">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/lab-dados/jev-anotacao-sentencas"><img src="https://opengraph.githubassets.com/1/lab-dados/jev-anotacao-sentencas" alt="Jev 法院判决标注" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/lab-dados/jev-anotacao-sentencas">Jev 法院判决标注</a></b><br><sub>lab-dados · GitHub · 2026-09-16</sub><br>FGV Direito SP 的实验，对 120 份圣保罗民事法院判决标注 12 个变量：Jev 准确率 96.6%，耗时 0.32 s，每千份判决 $0.25；Gemini 3.8 Flash 准确率 98.8%，花费 $6.56。<br><sub>相关: <a href="https://lab-dados.github.io/jev-anotacao-sentencas/">report</a> · <a href="https://lab-dados.github.io/jev-anotacao-sentencas">write-up</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/JacobLinCool/jev-paper-judge"><img src="https://jev-paper-judge.jacob.workers.dev/og.png" alt="Jev Paper Judge" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/JacobLinCool/jev-paper-judge">Jev Paper Judge</a></b><br><sub>JacobLinCool · GitHub · 2026-09-17</sub><br>上传研究论文 PDF，几秒内就能得到关于可读性和完整性的结构化评判，另有未定义缩写、未被引用的图表等机械检查。<br><sub>相关: <a href="https://jev-paper-judge.jacob.workers.dev">app</a> · <a href="https://jev-paper-judge.jacob.workers.dev">app 2</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/mttrbrts/jev-folio-recursive-classifier"><img src="https://opengraph.githubassets.com/1/mttrbrts/jev-folio-recursive-classifier" alt="jev-folio-recursive-classifier" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/mttrbrts/jev-folio-recursive-classifier">jev-folio-recursive-classifier</a></b><br><sub>mttrbrts · GitHub · 2026-09-19</sub><br>分类器，把 OCR 后的法律协议沿 FOLIO 文档类型本体逐层向下归类，每层一个 Jev Choice，用 beam 保留多条候选路径，并按置信度决定是否在叶节点停止。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/LYchoon/paper-radar-jev"><img src="https://opengraph.githubassets.com/1/LYchoon/paper-radar-jev" alt="Paper Radar" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/LYchoon/paper-radar-jev">Paper Radar</a></b><br><sub>LYchoon · GitHub · 2026-09-20</sub><br>Python CLI，抓取最新的 arXiv 论文，按可配置的研究画像给相关性打分，并每天输出 Markdown 和 JSON 格式的排名。<br><sub><b>Jev 用法:</b> 每篇论文用一个 Noul，以 P(True) 作为相关性分数。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/ndolinschi/pulselane"><img src="https://opengraph.githubassets.com/1/ndolinschi/pulselane" alt="PulseLane" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/ndolinschi/pulselane">PulseLane</a></b><br><sub>ndolinschi · GitHub · 2026-09-17</sub><br>诊所接诊分诊演示，根据主诉和生命体征给出 ESI 式的急迫程度分级，选择服务科室，并标出危险急症、口译需求和隔离防护措施。<br><sub>相关: <a href="https://pulselane-topaz.vercel.app">app</a> · <a href="https://pulselane-topaz.vercel.app">app 2</a></sub></td>
</tr>
</table>

还缺什么？[提交一个资源](https://github.com/Li-Evan/awesome-jev/issues/new/choose)。
