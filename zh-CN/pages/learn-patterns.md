# 📚 学习资料: 设计模式

[English](https://github.com/Li-Evan/awesome-jev/blob/main/pages/learn-patterns.md) · **简体中文**

官方文档和 cookbook，以及社区里最好的教程、分析、评测和演讲。共 4 条。

[← 返回 Awesome Jev](https://github.com/Li-Evan/awesome-jev/blob/main/README.zh-CN.md#设计模式)

[官方文档](https://github.com/Li-Evan/awesome-jev/blob/main/zh-CN/pages/learn-official-docs.md) (15) · [官方 SDK 与工具](https://github.com/Li-Evan/awesome-jev/blob/main/zh-CN/pages/learn-official-tools.md) (3) · [官方公告](https://github.com/Li-Evan/awesome-jev/blob/main/zh-CN/pages/learn-announcements.md) (2) · **设计模式** · [官方 Cookbook](https://github.com/Li-Evan/awesome-jev/blob/main/zh-CN/pages/learn-cookbooks.md) (18) · [示例与 Skill](https://github.com/Li-Evan/awesome-jev/blob/main/zh-CN/pages/learn-examples.md) (74) · [教程](https://github.com/Li-Evan/awesome-jev/blob/main/zh-CN/pages/learn-guides.md) (76) · [技巧与分析](https://github.com/Li-Evan/awesome-jev/blob/main/zh-CN/pages/learn-techniques.md) (103) · [评测与案例](https://github.com/Li-Evan/awesome-jev/blob/main/zh-CN/pages/learn-benchmarks.md) (173) · [视频与演讲](https://github.com/Li-Evan/awesome-jev/blob/main/zh-CN/pages/learn-videos.md) (178) · [社区讨论](https://github.com/Li-Evan/awesome-jev/blob/main/zh-CN/pages/learn-discussions.md) (20)

<table>
<tr>
<td width="260" valign="top"><a href="https://docs.typesafe.ai/patterns/fan-out"><img src="https://ts-docs.mintlify.app/mintlify-assets/_next/image?url=%2F_mintlify%2Fapi%2Fog%3Fdivision%3DPatterns%26title%3DSpeculative%2Bfan-out%26description%3DSend%2Bmany%2Bquestions%2Bin%2Ba%2Bsingle%2Bcall%252C%2Bincluding%2Bspeculative%2Bones%252C%2Band%2Blet%2Byour%2Bcode%2Bdecide%2Bwhat%2527s%2Brelevant.%26theme%3Df0580ae664a0195833f0555d&amp;w=1200&amp;q=100" alt="推测式扇出" width="240"></a></td>
<td valign="top"><b><a href="https://docs.typesafe.ai/patterns/fan-out">推测式扇出</a></b><br><sub>TypeSafe AI · 文档</sub><br>把可能用到的问题（包括只在某个分支才需要的）在一次请求里全部问完，再让代码只读取相关的答案。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://docs.typesafe.ai/patterns/confidence-routing"><img src="https://ts-docs.mintlify.app/mintlify-assets/_next/image?url=%2F_mintlify%2Fapi%2Fog%3Fdivision%3DPatterns%26title%3DConfidence-gated%2Brouting%26description%3DUse%2Bconfidence%2Bas%2Ba%2Bsecond%2Baxis.%2BThe%2Banswer%2Btells%2Byou%2Bwhat%253B%2Bconfidence%2Btells%2Byou%2Bwhether%2Bto%2Bact.%26theme%3Df0580ae664a0195833f0555d&amp;w=1200&amp;q=100" alt="置信度门控路由" width="240"></a></td>
<td valign="top"><b><a href="https://docs.typesafe.ai/patterns/confidence-routing">置信度门控路由</a></b><br><sub>TypeSafe AI · 文档</sub><br>把置信度当作第二个维度，对转账等风险更高的动作设置更严格的阈值。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://docs.typesafe.ai/patterns/composite-scoring"><img src="https://ts-docs.mintlify.app/mintlify-assets/_next/image?url=%2F_mintlify%2Fapi%2Fog%3Fdivision%3DPatterns%26title%3DComposite%2Bscoring%26description%3DBreak%2Ba%2Bcomplex%2Bjudgment%2Binto%2Batomic%2Bscores%252C%2Bcombine%2Bwith%2Bweights%2Byou%2Bcontrol%2Bin%2Bcode.%26theme%3Df0580ae664a0195833f0555d&amp;w=1200&amp;q=100" alt="组合评分" width="240"></a></td>
<td valign="top"><b><a href="https://docs.typesafe.ai/patterns/composite-scoring">组合评分</a></b><br><sub>TypeSafe AI · 文档</sub><br>对每个维度分别打分，再在代码里加权合并，这样调整优先级时无需改动问题。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://docs.typesafe.ai/patterns/intent-routing"><img src="https://ts-docs.mintlify.app/mintlify-assets/_next/image?url=%2F_mintlify%2Fapi%2Fog%3Fdivision%3DPatterns%26title%3DIntent%2Brouting%26description%3DClassify%2Bincoming%2Brequests%2Band%2Broute%2Beach%2Bto%2Bthe%2Boptimal%2Bhandler%253A%2Bdeterministic%2Blogic%252C%2Ba%2Bspecialist%2BLLM%252C%2Bor%2Ba%2Bhuman.%26theme%3Df0580ae664a0195833f0555d&amp;w=1200&amp;q=100" alt="意图路由" width="240"></a></td>
<td valign="top"><b><a href="https://docs.typesafe.ai/patterns/intent-routing">意图路由</a></b><br><sub>TypeSafe AI · 文档</sub><br>用一个 Choice 和一个复杂度 Score 给请求分类，再把每个请求交给代码、专门的 LLM 或人工。</td>
</tr>
</table>

还缺什么？[提交一个资源](https://github.com/Li-Evan/awesome-jev/issues/new/choose)。
