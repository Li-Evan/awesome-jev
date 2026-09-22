# Jev 速查表

[English](cheatsheet.md) · **简体中文**

> 本页由英文版翻译而来，以英文版和官方文档为准。

一页纸的 Jev 开发实战指南，内容提炼自 [TypeSafe 官方文档](https://docs.typesafe.ai)。本页与文档有出入时，以文档为准。

2026-09-21 最后核对，对照版本为 `jev-1.13.0`、`typesafe-sdk` 0.7.0（Python）和 `@typesafe-ai/sdk` 0.6.0（JavaScript）。

- [心智模型](#心智模型)
- [一次完整请求](#一次完整请求)
- [选择原语](#选择原语)
- [写好问题](#写好问题)
- [设计 state](#设计-state)
- [根据概率和置信度做决定](#根据概率和置信度做决定)
- [组合招式](#组合招式)
- [限制与定价](#限制与定价)
- [Jev 1.13 的已知短板](#jev-113-的已知短板)
- [什么时候不该用 Jev](#什么时候不该用-jev)
- [SDK 代码片段](#sdk-代码片段)
- [Jev 适合哪些场景](#jev-适合哪些场景)

## 心智模型

- Jev 是 **System One** 模型：它做快速、范围窄的判断，不生成文本，不写代码，也不解释自己。
- 你发送一份 **state**（证据）和多个带类型的**问题**（判断）。每个问题都针对同一份 state 并行、独立地评估，所以问题之间看不到彼此的答案。
- 你拿回的是**带概率的类型化答案**。控制流归你的代码：由它来分支、排序、按阈值判断和升级。
- 文档给的经验法则：好问题是懂行的人拿到合适的上下文后，几秒钟内就能做出的直觉判断。如果需要反复斟酌，就把它拆开。

## 一次完整请求

```bash
curl -X POST https://api.typesafe.ai/v1/systemone \
  -H "Authorization: Bearer $TYPESAFE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "jev-latest",
    "state": "I was charged twice for order A-104. Please fix this today.",
    "questions": {
      "department": {
        "type": "choice",
        "instructions": "Which team should handle this message?",
        "criteria": {"billing": "Payments and refunds", "technical": "Bugs and integrations", "other": null}
      },
      "frustration": {
        "type": "score",
        "instructions": "How frustrated does the customer sound?",
        "criteria": ["Calm, just stating facts", "Frustrated but civil", "Very angry, strong language"]
      },
      "is_urgent": {"type": "noul", "instructions": "The message asks for action within a specific time frame."}
    }
  }'
```

响应里的键和你提问时用的键一致：

```json
{
  "model": "jev-1.13.0",
  "answers": {
    "department": {"type": "choice", "choice": "billing", "confidence": 0.9, "probabilities": {"billing": 0.95, "technical": 0.03, "other": 0.02}},
    "frustration": {"type": "score", "score": 1.2, "confidence": 0.7, "legend": {"0": "Calm, just stating facts", "1": "Frustrated but civil", "2": "Very angry, strong language"}, "probabilities": {"0": 0.05, "1": 0.7, "2": 0.25}},
    "is_urgent": {"type": "noul", "noul": 0.97}
  },
  "usage": {"input_tokens": 180, "output_tokens": 20}
}
```

上面的数字只是示意。响应结构与 [API 参考](https://docs.typesafe.ai/api)一致。

## 选择原语

| 你需要 | 原语 | 返回 | 你的代码通常会 |
| --- | --- | --- | --- |
| 从固定、无序的集合中选一个选项 | [Choice](https://docs.typesafe.ai/primitives/choice) | `choice`、`probabilities`、`confidence` | 对选项做 `match` / `switch` |
| 在有序等级上的位置 | [Score](https://docs.typesafe.ai/primitives/score) | `score`（按概率加权的等级索引）、`legend`、`probabilities`、`confidence` | 和阈值比较、排序、加权 |
| 某个条件是否成立 | [Noul](https://docs.typesafe.ai/primitives/noul) | `noul` = P(yes)，取值 0 到 1 | `if p > threshold` |

- Choice 的概率总和始终为 1，所以总会有*某个*选项胜出。可以加一个 `other` 或 `none` 选项，或者另外用一个 Noul 问“文档到底有没有回答这个问题”。
- Score 可能落在两个等级之间（例如 `1.2`）。可以四舍五入、和阈值比较，或者直接看分布。
- Noul 为 0.5 表示“是和否的可能性相同”，**而不是**“中等强度”。要衡量程度，用 Score。
- 多标签？每个标签问一个 Noul，而不是用一个 Choice。
- Noul 没有 `confidence` 字段：那一个概率已经说明了一切。

## 写好问题

- **一个问题只做一个判断**。“这是垃圾信息吗？”里藏着好几个判断。分别问发件人、请求内容和施压手段，再在代码里组合。
- **一个 Noul 只判断一个条件**。把“生气*并且*要求退款”拆成两个问题。
- **用肯定的方式提问**。优先问“消息里包含个人数据吗”，而不是“消息里不含个人数据吗”。做校验时，让*失败*的情况对应 `true`（“这个字段是幻觉吗？”）。
- **Score 的等级要写成具体情境**，从低到高排列，每一级单独读也能看懂。避免只写数字（`["0", "1", "2"]`），也避免一个等级混入多个维度。
- **判断写在 `instructions` 里，答案空间写在 `criteria` 里**。两者都接受字符串或 JSON 结构（定义、对比、排除项、示例）。见[进阶：结构](https://docs.typesafe.ai/primitives/advanced)。
- **问题 ID 永远不会发给模型**。`is_urgent` 对 Jev 毫无意义；完整的含义必须写在 instructions 里。
- **用反引号包住的路径指向 state 里的嵌套字段**，例如 `` `ticket.messages[0].text` ``。

## 设计 state

- 每个请求一份 state，可以是字符串、JSON 对象或数组。上下文分好几部分时，用带名字的 JSON 字段效果最好。
- 需要*相互比较*的内容都放进同一份 state：消息、订单记录和政策。
- 只发问题需要的内容。无关内容越多，准确率越低，所以先在代码里过滤和检索。
- 优先用你自己的最新数据，而不是模型可能“知道”的东西。
- 把 state 当作可能带有对抗性的数据。注入的文本会左右答案。
- 目前只支持文本。图片、音频和表格要先转成文本或结构化字段。英文效果最好；其他语言（包括中日韩语言）请用自己的数据测试。

## 根据概率和置信度做决定

- **三条路径**可以作为起点：高置信度自动执行，中等置信度请求确认或复核，低置信度交给人工或兜底系统。
- **阈值随风险调整**。只读操作可以在比转账更低的置信度下执行。[置信度门控路由](https://docs.typesafe.ai/patterns/confidence-routing)模式在同一个 Choice 里演示了这两种情况。
- **Noul 用一个不确定区间**，例如 0.30 到 0.70 送去复核，而不是在 0.5 一刀切。
- 多个答案共同决定一个动作时，**以最弱的一环为准**：取它们中最低的置信度。
- **置信度描述的是分布，不是正确性**。用你自己的标注数据调阈值；调好之后固定一个带版本号的模型 ID（例如 `jev-1.13.0`），因为 `jev-latest` 会变。
- 只需要最优选项？取 argmax。要做统计？用 `probabilities`，不要用 `confidence`。

## 组合招式

| 招式 | 具体做法 | 参考 |
| --- | --- | --- |
| 推测式扇出 | 在一个请求里问完所有*可能*用到的问题；代码只读取相关的答案 | [扇出](https://docs.typesafe.ai/patterns/fan-out)、[并行问题](https://docs.typesafe.ai/cookbooks/parallel_questions) |
| 用第二个维度做路由 | 答案决定*做什么*，置信度决定*要不要做* | [置信度门控路由](https://docs.typesafe.ai/patterns/confidence-routing)、[意图路由](https://docs.typesafe.ai/patterns/intent-routing) |
| 原子化打分，在代码里加权 | 多个 Score 加一个公式，改公式无需重新跑推理 | [组合评分](https://docs.typesafe.ai/patterns/composite-scoring) |
| 只选择，不生成 | 用正则或 LLM 找出候选；Jev 选出正确的那个；代码做规范化 | [预解析值提取](https://docs.typesafe.ai/cookbooks/pre_parsed_value_extraction_cookbook)、[结构恢复](https://docs.typesafe.ai/cookbooks/autoformat) |
| 模型负责读，代码负责算 | Jev 读出日期的各个部分或字段值；代码做算术 | [日期提取](https://docs.typesafe.ai/cookbooks/date_extraction_cookbook) |
| 按概率排序 | 每个“查询-候选”对问一个 Noul，按 `noul` 排序 | [重排](https://docs.typesafe.ai/cookbooks/rerank_typesafe) |
| 先把关，再决定 | 在主 Choice 之前或同时，用一个便宜的 Noul 问“这里有没有相关内容” | [逐行搜索](https://docs.typesafe.ai/cookbooks/semantic_find)、[Skill 推荐](https://docs.typesafe.ai/cookbooks/skill_suggestion) |
| 沿分类体系逐层走 | 每个节点一个 Choice，在概率上做 beam search | [层级分类](https://docs.typesafe.ai/cookbooks/hierarchical_classification) |
| 拿不准时退一步 | 置信度低时只报告父类别 | [利用置信度做分类](https://docs.typesafe.ai/cookbooks/classification_using_confidence) |
| 校验并升级 | 便宜模型负责提取，Jev 逐个字段校验，存疑的情况交给更强的模型或人工 | [SDE 级联](https://docs.typesafe.ai/cookbooks/sde_cascade)、[引用核查](https://docs.typesafe.ai/cookbooks/citation_check) |
| 把判断当特征 | 把文本转成 Noul 列和 Score 列，再训练传统模型 | [Autoresearch 特征发现](https://docs.typesafe.ai/cookbooks/autoresearch_feature_discovery) |
| 等级即动作 | 让每个 Score 等级对应一个动作（合并、复核、保持不变），这样就不用拟合阈值 | [实体对齐](https://docs.typesafe.ai/cookbooks/entity_alignment) |

## 限制与定价

以下数据摘自 2026-09-21 的[模型](https://docs.typesafe.ai/models)和 [API](https://docs.typesafe.ai/api) 页面。依赖这些数字之前，请先去核对。

| 项目 | 值 |
| --- | --- |
| 端点 | `POST https://api.typesafe.ai/v1/systemone`（`GET /v1/models` 列出模型） |
| 认证 | `Authorization: Bearer $TYPESAFE_API_KEY` |
| 当前模型 | `jev-1.13.0`；别名 `jev-latest` 和 `jev-preview` 都指向它 |
| 价格 | 每百万输入 token $0.042；输出 token 免费 |
| 速率限制 | 每秒 250,000 token，每分钟 1,200 个请求（动态调整；超出时返回 `429`） |
| 上下文 | 每个请求 64k token；state 加上最长的一个问题共 32k |
| Choice 选项 | 每个问题最多 255 个 |
| Score 等级 | 每个问题 2 到 10 个 |
| 延迟 | 据文档，大多数查询约 100 ms |
| 输入 | 仅文本 |
| 定制 | 不支持微调；通过 state、instructions、criteria 和问题拆解来塑造行为 |
| SDK 环境变量 | `TYPESAFE_API_KEY`、`TYPESAFE_BASE_URL`、`TYPESAFE_DEFAULT_MODEL`、`TYPESAFE_LOG_LEVEL` |

## Jev 1.13 的已知短板

整理自 [Jev 1.13 能力参差](https://docs.typesafe.ai/model-jaggedness/jev-1.13)。每一项都可以在代码里绕过。

| 短板 | 应对办法 |
| --- | --- |
| 对范围限定词、否定词和隐含条件按字面理解 | 写明确切的条件；把边界情况放进 `criteria` |
| 计数、算术、数字格式（十六进制、二进制、颜色） | 在代码里计数和计算；每一项单独一个问题 |
| 比较日期和时间窗口 | 用 Choice 提取日期的各个部分，在代码里计算 |
| 双重否定和多跳问题 | 拆成直接的问题 |
| state 很大且充满无关细节 | 先过滤，或跑一个相关性 Noul |
| state 里有对抗性或自我论证的文本 | 写明确的 criteria；测试边界情况 |
| instructions 与 criteria 相互矛盾 | 让 `true` 始终表示“是” |
| 等价的问题不一定给出一致答案（Noul 与是/否 Choice，一个问题与它的否定形式） | 不要把 Noul 的阈值套用到 Choice 上；每个问题单独校准 |
| 生成文本 | 在别处生成候选；让 Jev 来选 |

## 什么时候不该用 Jev

- 答案是文本：回复、摘要、代码、解释。
- 代码能精确算出来：算术、日期、查表、正则表达式、固定规则。
- 任务需要较长的推理（“分析并确定最佳行动方案”）。把它拆开，或者交给推理模型。
- 你打算搭一个 agent `while` 循环，而普通控制流就能表达它。
- 你把护栏 Noul 当作安全边界。它只能作为多个信号中的一个。
- 你需要在浏览器里调用 API。密钥要留在服务端。

## SDK 代码片段

Python（`pip install typesafe-sdk` 或 `uv add typesafe-sdk`，Python 3.10+）。客户端读取 `TYPESAFE_API_KEY`，默认使用 `jev-latest`。

```python
from typesafe_sdk import Choice, Noul, Score, TypeSafeClient

client = TypeSafeClient()

response = client.system_one(
    state={"message": "I was charged twice for order A-104. Please fix this today."},
    questions={
        "department": Choice(
            instructions="Which team should handle `message`?",
            criteria={"billing": "Payments and refunds", "technical": "Bugs and integrations", "other": None},
        ),
        "frustration": Score(
            instructions="How frustrated does the customer sound in `message`?",
            criteria=["Calm, just stating facts", "Frustrated but civil", "Very angry, strong language"],
        ),
        "is_urgent": Noul(instructions="`message` asks for action within a specific time frame."),
    },
)

department = response.choices["department"]
if department.confidence < 0.5:
    print("send to a human")
else:
    print(department.choice, response.scores["frustration"].score, response.nouls["is_urgent"].noul)
```

Python 异步版：

```python
import asyncio

from typesafe_sdk import AsyncTypeSafeClient, Noul


async def main() -> None:
    async with AsyncTypeSafeClient() as client:
        response = await client.system_one(
            state="Can I get a refund for a cancelled flight?",
            questions={"asks_refund": Noul(instructions="The message asks for a refund.")},
        )
        print(response.nouls["asks_refund"].noul)


asyncio.run(main())
```

JavaScript 或 TypeScript（`npm install @typesafe-ai/sdk`，Node.js 20+）。密钥放在服务端。

```ts
import { choice, noul, TypeSafeClient } from "@typesafe-ai/sdk";

const client = new TypeSafeClient();

const response = await client.systemOne({
  state: { message: "I was charged twice. Please fix this ASAP." },
  questions: {
    category: choice("What is `message` about?", { billing: null, technical: null, other: null }),
    urgent: noul("`message` asks for action within a specific time frame."),
  },
});

console.log(response.answers.category.choice, response.answers.urgent.noul);
```

## Jev 适合哪些场景

文档里的[用例地图](https://docs.typesafe.ai/concepts/use-case-map)列出了 18 个领域的想法。它们可以归结为少数几种决策形态：

| 决策形态 | 常用原语 | 示例 |
| --- | --- | --- |
| 分类 | Choice | 意图、主题、部门、风险类型 |
| 检测 | Noul | 垃圾信息、欺诈、紧急程度、越狱、个人数据 |
| 打分 | Score | 严重程度、相关性、质量、不满程度 |
| 路由 | Choice 加置信度 | 客服队列、模型路由、工具选择、升级 |
| 搜索、检索、排序 | 每个候选一个 Noul 或 Score，或在行 ID 上做 Choice | RAG 上下文选择、重排、语义查找 |
| 校验 | 一组 Noul 或 Choice | 引用是否有依据、工具调用错误、违反规则、幻觉字段 |
| 结构化提取 | 在候选或组成部分上做 Choice | 日期、金额、联系方式、商品属性 |
| 特征提取 | Noul 列和 Score 列 | 购买意向、流失信号、竞争压力 |
