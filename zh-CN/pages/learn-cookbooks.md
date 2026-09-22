# 📚 学习资料: 官方 Cookbook

[English](https://github.com/Li-Evan/awesome-jev/blob/main/pages/learn-cookbooks.md) · **简体中文**

官方文档和 cookbook，以及社区里最好的教程、分析、评测和演讲。共 18 条。

[← 返回 Awesome Jev](https://github.com/Li-Evan/awesome-jev/blob/main/README.zh-CN.md#官方-cookbook)

[官方文档](https://github.com/Li-Evan/awesome-jev/blob/main/zh-CN/pages/learn-official-docs.md) (15) · [官方 SDK 与工具](https://github.com/Li-Evan/awesome-jev/blob/main/zh-CN/pages/learn-official-tools.md) (3) · [官方公告](https://github.com/Li-Evan/awesome-jev/blob/main/zh-CN/pages/learn-announcements.md) (2) · [设计模式](https://github.com/Li-Evan/awesome-jev/blob/main/zh-CN/pages/learn-patterns.md) (4) · **官方 Cookbook** · [示例与 Skill](https://github.com/Li-Evan/awesome-jev/blob/main/zh-CN/pages/learn-examples.md) (74) · [教程](https://github.com/Li-Evan/awesome-jev/blob/main/zh-CN/pages/learn-guides.md) (76) · [技巧与分析](https://github.com/Li-Evan/awesome-jev/blob/main/zh-CN/pages/learn-techniques.md) (102) · [评测与案例](https://github.com/Li-Evan/awesome-jev/blob/main/zh-CN/pages/learn-benchmarks.md) (173) · [视频与演讲](https://github.com/Li-Evan/awesome-jev/blob/main/zh-CN/pages/learn-videos.md) (178) · [社区讨论](https://github.com/Li-Evan/awesome-jev/blob/main/zh-CN/pages/learn-discussions.md) (20)

<table>
<tr>
<td width="260" valign="top"><a href="https://docs.typesafe.ai/cookbooks/hierarchical_classification"><img src="https://ts-docs.mintlify.app/mintlify-assets/_next/image?url=%2F_mintlify%2Fapi%2Fog%3Fdivision%3DClassification%26title%3DHierarchical%2Bclassification%26description%3DClassifies%2Bdocuments%2Bthrough%2Bdeep%2Bpatent%252C%2Bretail%2Bproduct%252C%2Bbiomedical%252C%2Band%2Bsource-code%2Bhierarchies%2Busing%2Bparallel%2Bbeam%2Bsearch%2Bover%2BTypeSafe%2BChoice%2Bprobabilities.%26theme%3Df0580ae664a0195833f0555d&amp;w=1200&amp;q=100" alt="层级分类" width="240"></a></td>
<td valign="top"><b><a href="https://docs.typesafe.ai/cookbooks/hierarchical_classification">层级分类</a></b><br><sub>TypeSafe AI · 文档</sub><br>以每个节点一个 Choice、并在概率上做 beam search 的方式，遍历专利分类号、零售商品、MeSH 和源码树等深层分类体系。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://docs.typesafe.ai/cookbooks/classification_using_confidence"><img src="https://ts-docs.mintlify.app/mintlify-assets/_next/image?url=%2F_mintlify%2Fapi%2Fog%3Fdivision%3DClassification%26title%3DClassification%2Busing%2Bconfidence%26description%3DClassify%2BSEC%2Bannual%2Breports%2Binto%2B75%2Bindustry%2Bgroups%2Bwith%2Bone%2BChoice%2Beach%252C%2Bthen%2Bread%2Bthe%2Banswer%2527s%2Bown%2Bconfidence%2Bto%2Bdecide%2Bwhether%2Bto%2Breport%2Bthat%2Bgroup%2Bor%2Bthe%2Bbr%26theme%3Df0580ae664a0195833f0555d&amp;w=1200&amp;q=100" alt="基于置信度的分类" width="240"></a></td>
<td valign="top"><b><a href="https://docs.typesafe.ai/cookbooks/classification_using_confidence">基于置信度的分类</a></b><br><sub>TypeSafe AI · 文档</sub><br>把 60 份 SEC 文件归入 75 个行业组，置信度低于 0.9 时回退到更宽泛的大类，把 39 个正确答案变成 48 个有用答案。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://docs.typesafe.ai/demos/smart-home"><img src="https://ts-docs.mintlify.app/mintlify-assets/_next/image?url=%2F_mintlify%2Fapi%2Fog%3Fdivision%3DDemos%26title%3DSmart%2Bhome%2Bassistant%2Bdemo%26description%3DDemo%2Bcode%253A%2Ba%2Bsmart%2Bhome%2Bassistant%2Bthat%2Buses%2BTypeSafe%2Bto%2Bevaluate%2Buser%2Brequests.%26theme%3Df0580ae664a0195833f0555d&amp;w=1200&amp;q=100" alt="智能家居助手演示" width="240"></a></td>
<td valign="top"><b><a href="https://docs.typesafe.ai/demos/smart-home">智能家居助手演示</a></b><br><sub>TypeSafe AI · 文档 · ▲ 34</sub><br>用一长串推测式扇出的 Choice 解析家居指令，外加一个 Noul 识别复合请求，交给 LLM 拆分。<br><sub>相关: <a href="https://docs.typesafe.ai/patterns/fan-out">pattern</a> · <a href="https://www.reddit.com/r/homeassistant/comments/1wjmqj0/upcoming_revolution_for_smart_home_control_with/">discussion</a> · <a href="https://www.reddit.com/r/accelerate/comments/1wifrk4/jev_demo/">discussion 2</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://docs.typesafe.ai/cookbooks/function_calling"><img src="https://ts-docs.mintlify.app/mintlify-assets/_next/image?url=%2F_mintlify%2Fapi%2Fog%3Fdivision%3DHow-to%26title%3DFunction%2Bcalling%26description%3DTurns%2Bnatural-language%2Btrading%2Brequests%2Binto%2Bcalls%2Bto%2Bordinary%2Btyped%2Bfunctions%2Bby%2Bmapping%2Bfunction%2Bnames%2Band%2Bclosed-set%2Barguments%2Bto%2Bconfidence-aware%2BTypeSafe%2Bq%26theme%3Df0580ae664a0195833f0555d&amp;w=1200&amp;q=100" alt="函数调用" width="240"></a></td>
<td valign="top"><b><a href="https://docs.typesafe.ai/cookbooks/function_calling">函数调用</a></b><br><sub>TypeSafe AI · 文档</sub><br>把交易请求映射到十个普通的类型化函数上：用 Choice 选择函数和封闭集合参数，用 Noul 判断请求里说了哪些参数。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://docs.typesafe.ai/cookbooks/skill_suggestion"><img src="https://ts-docs.mintlify.app/mintlify-assets/_next/image?url=%2F_mintlify%2Fapi%2Fog%3Fdivision%3DHow-to%26title%3DSkill%2Bsuggestion%26description%3DPicks%2Bat%2Bmost%2Bone%2Bskill%2Bfor%2Ban%2Bagent%2Bturn%2Bout%2Bof%2Bthe%2B182%2Bin%2BNous%2BResearch%2527s%2BHermes%2Bcatalog%252C%2Busing%2Btwo%2BTypeSafe%2Brequests%2Bto%2Brank%2Band%2Bre-check%2Bthe%2Btop%2Bcandidates.%26theme%3Df0580ae664a0195833f0555d&amp;w=1200&amp;q=100" alt="Skill 推荐" width="240"></a></td>
<td valign="top"><b><a href="https://docs.typesafe.ai/cookbooks/skill_suggestion">Skill 推荐</a></b><br><sub>TypeSafe AI · 文档</sub><br>每轮用两次请求从 182 个 agent skill 中最多挑一个，把加载错误 skill 的比例从 16.8% 降到 7.3%。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://docs.typesafe.ai/cookbooks/rerank_typesafe"><img src="https://ts-docs.mintlify.app/mintlify-assets/_next/image?url=%2F_mintlify%2Fapi%2Fog%3Fdivision%3DHow-to%26title%3DRe-ranking%26description%3DBuilds%2B30-passage%2BBM25%2Bshortlists%2Bfor%2B40%2BCLERC%2Blegal%2Bqueries%252C%2Bthen%2Buses%2Bone%2BTypeSafe%2Bquestion%2Bper%2Bquery-candidate%2Bpair%2Bto%2Braise%2Btop-1%2Baccuracy%2Bfrom%2B5%2525%2Bto%2B18%2525%2Ban%26theme%3Df0580ae664a0195833f0555d&amp;w=1200&amp;q=100" alt="重排" width="240"></a></td>
<td valign="top"><b><a href="https://docs.typesafe.ai/cookbooks/rerank_typesafe">重排</a></b><br><sub>TypeSafe AI · 文档</sub><br>每个查询-段落对用一个 Noul 给 BM25 候选打分，把法律检索的 top-10 准确率从 38% 提升到 62%，总花费约 $0.06。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://docs.typesafe.ai/cookbooks/semantic_find"><img src="https://ts-docs.mintlify.app/mintlify-assets/_next/image?url=%2F_mintlify%2Fapi%2Fog%3Fdivision%3DHow-to%26title%3DLine-by-line%2Bsearch%26description%3DBuild%2Bsemantic%2Bsearch%2Bfor%2BGitHub%2527s%2BTerms%2Bof%2BService.%2BIn%2Bone%2Brequest%252C%2Bscore%2B218%2Bline%2Bids%2Bagainst%2Ba%2Bplain-language%2Bquery%2Bwith%2Ba%2BChoice%2Bquestion%252C%2Band%2Buse%2Ba%2BNoul%2Bqu%26theme%3Df0580ae664a0195833f0555d&amp;w=1200&amp;q=100" alt="逐行搜索" width="240"></a></td>
<td valign="top"><b><a href="https://docs.typesafe.ai/cookbooks/semantic_find">逐行搜索</a></b><br><sub>TypeSafe AI · 文档</sub><br>用一个 Choice 给一份服务条款文档的 218 行排序，并用一个 Noul 判断文档里是否根本没有答案。<br><sub>相关: <a href="https://x.com/dotpem/status/2100389272004198844">demo</a> · <a href="https://www.reddit.com/r/typesafe/comments/1wjy4f9/semantic_search_without_embeddings_218_lines/">discussion</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://docs.typesafe.ai/cookbooks/classifying_rag_passages"><img src="https://ts-docs.mintlify.app/mintlify-assets/_next/image?url=%2F_mintlify%2Fapi%2Fog%3Fdivision%3DHow-to%26title%3DClassifying%2BRAG%2Bpassages%26description%3DScore%2Beach%2Bretrieved%2Bpassage%2Bwith%2Bone%2BTypeSafe%2Brequest%252C%2Bthen%2Bdecide%2Bin%2Bcode%2Bwhich%2Bones%2Breach%2Bthe%2Banswering%2Bmodel.%26theme%3Df0580ae664a0195833f0555d&amp;w=1200&amp;q=100" alt="RAG 段落分类" width="240"></a></td>
<td valign="top"><b><a href="https://docs.typesafe.ai/cookbooks/classifying_rag_passages">RAG 段落分类</a></b><br><sub>TypeSafe AI · 文档</sub><br>对每个检索到的段落跑四个 Noul，剔除提示词注入和跑题文本，并标出与问题相矛盾的段落。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://docs.typesafe.ai/cookbooks/date_extraction_cookbook"><img src="https://ts-docs.mintlify.app/mintlify-assets/_next/image?url=%2F_mintlify%2Fapi%2Fog%3Fdivision%3DExtraction%26title%3DDate%2Bextraction%26description%3DExtracts%2Babsolute%2Band%2Brelative%2Bdates%2Bby%2Basking%2BTypeSafe%2Bfor%2Bthe%2Bparts%2Bnamed%2Bin%2Ba%2Bdocument%252C%2Bthen%2Bresolving%2Band%2Bvalidating%2Bthem%2Bin%2Bcode%2Bwith%2Bconfidence-based%2Brevi%26theme%3Df0580ae664a0195833f0555d&amp;w=1200&amp;q=100" alt="日期提取" width="240"></a></td>
<td valign="top"><b><a href="https://docs.typesafe.ai/cookbooks/date_extraction_cookbook">日期提取</a></b><br><sub>TypeSafe AI · 文档</sub><br>用 Choice 读取日期的各个部分，所有日历计算交给代码，低置信度的日期送人工复核。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://docs.typesafe.ai/cookbooks/pre_parsed_value_extraction_cookbook"><img src="https://ts-docs.mintlify.app/mintlify-assets/_next/image?url=%2F_mintlify%2Fapi%2Fog%3Fdivision%3DExtraction%26title%3DPre-parsed%2Bvalue%2Bextraction%26description%3DUses%2Bregexes%2Bto%2Bfind%2Bcandidate%2Bemails%252C%2Bphone%2Bnumbers%252C%2Band%2Bamounts%252C%2Bthen%2Bhas%2BTypeSafe%2Bselect%2Bthe%2Brequested%2Bspan%2Bso%2Bcode%2Bcan%2Bnormalize%2Ba%2Bverbatim%2Bvalue.%26theme%3Df0580ae664a0195833f0555d&amp;w=1200&amp;q=100" alt="预解析值提取" width="240"></a></td>
<td valign="top"><b><a href="https://docs.typesafe.ai/cookbooks/pre_parsed_value_extraction_cookbook">预解析值提取</a></b><br><sub>TypeSafe AI · 文档</sub><br>先用正则表达式找出邮箱、电话号码和金额，再让一个 Choice 选出所需的那个，因此值永远不会是编造的。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://docs.typesafe.ai/cookbooks/citation_check"><img src="https://ts-docs.mintlify.app/mintlify-assets/_next/image?url=%2F_mintlify%2Fapi%2Fog%3Fdivision%3DHow-to%26title%3DDouble-checking%2Bcitations%26description%3DCatch%2Bwrong%2Bor%2Bhallucinated%2Bcitations%2Bby%2Bchecking%2Bagainst%2Bthe%2Bsource%2Bdocument.%2BOne%2BChoice%2Bquestion%2Bdecides%2Bwhether%2Bthe%2Bquote%2527s%2Bcontext%2Bsupports%2Bthe%2Bclaim.%26theme%3Df0580ae664a0195833f0555d&amp;w=1200&amp;q=100" alt="复核引用" width="240"></a></td>
<td valign="top"><b><a href="https://docs.typesafe.ai/cookbooks/citation_check">复核引用</a></b><br><sub>TypeSafe AI · 文档</sub><br>把精确字符串匹配与一个“支持 / 矛盾 / 未提及”的 Choice 结合起来，揪出编造和误用的引用。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://docs.typesafe.ai/cookbooks/llm_guardrails"><img src="https://ts-docs.mintlify.app/mintlify-assets/_next/image?url=%2F_mintlify%2Fapi%2Fog%3Fdivision%3DHow-to%26title%3DGuardrails%2Bfor%2BLLMs%26description%3DScreen%2Bevery%2Bmessage%2Bgoing%2Binto%2Band%2Bout%2Bof%2Ban%2BLLM%2Bapp%2Bwith%2Bone%2BTypeSafe%2Brequest%252C%2Bthresholding%2Bhazard%2Bprobabilities%2Band%2Bseverity%2Bto%2Bpass%252C%2Breview%252C%2Bblock%252C%2Bor%2Broute%26theme%3Df0580ae664a0195833f0555d&amp;w=1200&amp;q=100" alt="LLM 护栏" width="240"></a></td>
<td valign="top"><b><a href="https://docs.typesafe.ai/cookbooks/llm_guardrails">LLM 护栏</a></b><br><sub>TypeSafe AI · 文档</sub><br>用风险类 Noul 和一个严重程度 Score 筛查输入和输出，再通过代码掌控的策略把概率映射为放行、复核或拦截。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://docs.typesafe.ai/cookbooks/sde_cascade"><img src="https://ts-docs.mintlify.app/mintlify-assets/_next/image?url=%2F_mintlify%2Fapi%2Fog%3Fdivision%3DExtraction%26title%3DSDE%2Bcascade%26description%3DUses%2Ba%2B2-stage%2Bstructured-data-extraction%2Bcascade%2B%2528mini%2B%25E2%2586%2592%2Bverify%2B%25E2%2586%2592%2Breasoning%2529%2Bto%2Bget%2Bmost%2Bof%2Bthe%2Bquality%2Bof%2Ba%2Bbig%2Breasoning%2Bmodel%2Bat%2Ba%2Bfraction%2Bof%2Bthe%2Bcost.%26theme%3Df0580ae664a0195833f0555d&amp;w=1200&amp;q=100" alt="SDE 级联" width="240"></a></td>
<td valign="top"><b><a href="https://docs.typesafe.ai/cookbooks/sde_cascade">SDE 级联</a></b><br><sub>TypeSafe AI · 文档</sub><br>小型 LLM 提取字段，Jev 逐一检查每个字段有无幻觉和格式错误，只有存疑的情况才升级给推理模型。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://docs.typesafe.ai/cookbooks/entity_alignment"><img src="https://ts-docs.mintlify.app/mintlify-assets/_next/image?url=%2F_mintlify%2Fapi%2Fog%3Fdivision%3DHow-to%26title%3DKnowledge%2Bgraph%2Bentity%2Balignment%26description%3DDecides%2Bwhich%2Bof%2B450%2Bcandidate%2Bpairs%2Bfrom%2Btwo%2Bbeer%2Bcatalogues%2Bdescribe%2Bthe%2Bsame%2Bproduct%2Busing%2Bone%2BScore%2Bquestion%2Bplus%2Bthree%2Bcompanion%2BNouls%2Bthat%2Bsurface%2Bwhich%2Bf%26theme%3Df0580ae664a0195833f0555d&amp;w=1200&amp;q=100" alt="知识图谱实体对齐" width="240"></a></td>
<td valign="top"><b><a href="https://docs.typesafe.ai/cookbooks/entity_alignment">知识图谱实体对齐</a></b><br><sub>TypeSafe AI · 文档</sub><br>用一个三级 Score 判断哪些商品对是同一个，三个等级直接对应动作：合并、交给策展人、保持不关联。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://docs.typesafe.ai/cookbooks/autoresearch_feature_discovery"><img src="https://ts-docs.mintlify.app/mintlify-assets/_next/image?url=%2F_mintlify%2Fapi%2Fog%3Fdivision%3DClassification%26title%3DAutoresearch%2Bfeature%2Bdiscovery%26description%3DRuns%2Ban%2Bautoresearch%2Bloop%2Bthat%2Bproposes%2BTypeSafe%2Bquestions%252C%2Bconverts%2Bfree%2Btext%2Binto%2Bnumeric%2Bfeatures%252C%2Band%2Buses%2Bmodel%2Berrors%2Bto%2Bimprove%2Ba%2Bsupervised%2BCatBoost%2Breg%26theme%3Df0580ae664a0195833f0555d&amp;w=1200&amp;q=100" alt="Autoresearch 特征发现" width="240"></a></td>
<td valign="top"><b><a href="https://docs.typesafe.ai/cookbooks/autoresearch_feature_discovery">Autoresearch 特征发现</a></b><br><sub>TypeSafe AI · 文档</sub><br>LLM 提出问题，Jev 为每一行数据作答，CatBoost 从这些答案中学习，把留出集上的葡萄酒评分误差（RMSE）从 3.09 降到 1.77。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://docs.typesafe.ai/cookbooks/parallel_questions"><img src="https://ts-docs.mintlify.app/mintlify-assets/_next/image?url=%2F_mintlify%2Fapi%2Fog%3Fdivision%3DBatching%26title%3DParallel%2Bquestions%26description%3DRuns%2Ba%2B13-question%2Bregulatory%2Bbriefing%2Bover%2Bthe%2BGDPR%2BWikipedia%2Barticle%252C%2Bshowing%2Bthat%2Bbatching%2Bevery%2Bquestion%2Binto%2Bone%2BTypeSafe%2Bcall%2Bis%2B12.2x%2Bcheaper%2Band%2B10.0x%2Bf%26theme%3Df0580ae664a0195833f0555d&amp;w=1200&amp;q=100" alt="并行提问" width="240"></a></td>
<td valign="top"><b><a href="https://docs.typesafe.ai/cookbooks/parallel_questions">并行提问</a></b><br><sub>TypeSafe AI · 文档</sub><br>把针对同一份长文档的 13 个问题合并成一次请求，便宜 12.2 倍、快 10.0 倍，答案没有任何变化。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://docs.typesafe.ai/cookbooks/consistency_noul_cookbook"><img src="https://ts-docs.mintlify.app/mintlify-assets/_next/image?url=%2F_mintlify%2Fapi%2Fog%3Fdivision%3DSelf-consistency%26title%3DSelf-consistency%253A%2Bnouls%26description%3DRoute%2Buncertain%2Bprobabilities%2Bto%2Bhuman%2Breview%2Bwhile%2Bkeeping%2Bthe%2Bunderlying%2Bnoul%2Bvalues%2Bvisible.%26theme%3Df0580ae664a0195833f0555d&amp;w=1200&amp;q=100" alt="用 Noul 做自一致性" width="240"></a></td>
<td valign="top"><b><a href="https://docs.typesafe.ai/cookbooks/consistency_noul_cookbook">用 Noul 做自一致性</a></b><br><sub>TypeSafe AI · 文档</sub><br>把一套 14 个问题的保险分流评分表重复跑 15 次，并与几款 LLM 比较答案稳定性、延迟和成本。<br><sub>相关: <a href="https://docs.typesafe.ai/cookbooks/consistency_choice_cookbook">choices</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://docs.typesafe.ai/cookbooks/consistency_choice_cookbook"><img src="https://ts-docs.mintlify.app/mintlify-assets/_next/image?url=%2F_mintlify%2Fapi%2Fog%3Fdivision%3DSelf-consistency%26title%3DSelf-consistency%253A%2Bchoices%26description%3DAdd%2Ban%2Buncertain%2Boutcome%2Bto%2Bmoderation%2Bdecisions%2Band%2Bcompare%2Blabel%2Bagreement%2Bwith%2Bthe%2Bshare%2Bof%2Bautomatic%2Bactions.%26theme%3Df0580ae664a0195833f0555d&amp;w=1200&amp;q=100" alt="用 Choice 做自一致性" width="240"></a></td>
<td valign="top"><b><a href="https://docs.typesafe.ai/cookbooks/consistency_choice_cookbook">用 Choice 做自一致性</a></b><br><sub>TypeSafe AI · 文档</sub><br>给审核决策增加一个“不确定”结果，在标签一致率和自动处理的案例占比之间做权衡。<br><sub>相关: <a href="https://docs.typesafe.ai/cookbooks/consistency_noul_cookbook">nouls</a></sub></td>
</tr>
</table>

还缺什么？[提交一个资源](https://github.com/Li-Evan/awesome-jev/issues/new/choose)。
