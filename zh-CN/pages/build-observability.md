# 🔌 用 Jev 开发: 可观测性

[English](https://github.com/Li-Evan/awesome-jev/blob/main/pages/build-observability.md) · **简体中文**

从你的技术栈调用 Jev 的方式：托管访问、框架适配、可观测性和社区 SDK。共 14 条，按社区热度排序。

[← 返回 Awesome Jev](https://github.com/Li-Evan/awesome-jev/blob/main/README.zh-CN.md#可观测性)

[模型访问](https://github.com/Li-Evan/awesome-jev/blob/main/zh-CN/pages/build-model-access.md) (68) · [框架适配](https://github.com/Li-Evan/awesome-jev/blob/main/zh-CN/pages/build-frameworks.md) (174) · **可观测性** · [社区 SDK](https://github.com/Li-Evan/awesome-jev/blob/main/zh-CN/pages/build-community-sdks.md) (107)

<table>
<tr>
<td width="260" valign="top"><a href="https://github.com/comet-ml/opik/tree/main/sdks/python/src/opik/integrations/typesafe"><img src="https://raw.githubusercontent.com/comet-ml/opik/refs/heads/main/apps/opik-documentation/documentation/static/img/opik-logo.svg" alt="Opik 的 TypeSafe 集成" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/comet-ml/opik/tree/main/sdks/python/src/opik/integrations/typesafe">Opik 的 TypeSafe 集成</a></b><br><sub>comet-ml · GitHub · ⭐ 22.2k 仓库 · 2023-05-10</sub><br>Opik Python SDK 的集成，包装同步和异步 TypeSafe 客户端，让每次 Jev 调用都在 Opik 的 LLM 可观测性与评测平台中被追踪。<br><sub>相关: <a href="https://www.comet.com/docs/opik/">docs</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Arize-ai/phoenix/tree/main/docs/phoenix/integrations/llm-providers/typesafe"><img src="https://repository-images.githubusercontent.com/564072810/f3666cdf-cb3e-4056-8a25-27cb3e6b5848" alt="Phoenix 的 TypeSafe 追踪" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Arize-ai/phoenix/tree/main/docs/phoenix/integrations/llm-providers/typesafe">Phoenix 的 TypeSafe 追踪</a></b><br><sub>Arize-ai · 文档 · ⭐ 11.6k 仓库 · 2022-11-09</sub><br>面向 TypeSafe Python 和 TypeScript SDK 的 OpenInference 埋点，把每次 System One 调用的 state、问题和类型化答案记录为 Arize Phoenix 中的 span。<br><sub>相关: <a href="https://pypi.org/project/openinference-instrumentation-typesafe">pypi</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://langfuse.com/integrations/model-providers/typesafe"><img src="https://langfuse.com/api/og?title=Observability+for+TypeSafe+Jev+with+Langfuse&amp;description=Trace+TypeSafe+Jev+System+One+decisions+with+Langfuse+using+OpenInference+auto-instrumentation.+No+client+wrapper+required.&amp;section=Integrations" alt="Langfuse 的 TypeSafe 集成" width="240"></a></td>
<td valign="top"><b><a href="https://langfuse.com/integrations/model-providers/typesafe">Langfuse 的 TypeSafe 集成</a></b><br><sub>Langfuse · 文档 · ⭐ 244 · 2026-09-19</sub><br>集成指南和 notebook，介绍如何通过 OpenInference 自动埋点在 Langfuse 中追踪 Jev System One 调用，无需包装客户端。<br><sub>相关: <a href="https://github.com/langfuse/langfuse-docs/blob/main/content/integrations/model-providers/typesafe.mdx">repo</a> · <a href="https://github.com/langfuse/langfuse-docs/blob/main/cookbook/integration_typesafe.ipynb">cookbook</a> · <a href="https://langfuse.com/blog/2026-09-18-using-typesafes-jev-for-evals">blog</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Arize-ai/openinference/tree/main/python/instrumentation/openinference-instrumentation-typesafe"><img src="https://opengraph.githubassets.com/1/Arize-ai/openinference" alt="OpenInference 的 TypeSafe 埋点" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Arize-ai/openinference/tree/main/python/instrumentation/openinference-instrumentation-typesafe">OpenInference 的 TypeSafe 埋点</a></b><br><sub>Arize-ai · GitHub · ⭐ 1.2k 仓库 · 2023-12-26</sub><br>面向 TypeSafe Python SDK 的 OpenTelemetry 埋点，追踪每次 Jev System One 调用的 state、模型、问题和类型化答案，可配合任意 OTel 后端使用。<br><sub>相关: <a href="https://arize-ai.github.io/openinference/">docs</a> · <a href="https://pypi.org/project/openinference-instrumentation-typesafe">pypi</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/andududu/jeview"><img src="https://raw.githubusercontent.com/andududu/jeview/main/docs/side-by-side.png" alt="Jeview" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/andududu/jeview">Jeview</a></b><br><sub>andududu · GitHub · ⭐ 21 · 2026-09-21</sub><br>非官方的本地网关，位于你的代码和 TypeSafe 之间，转发每一个 Jev 请求，把每次调用存入 SQLite，并在调用发生时把它们实时画在地图上。<br><sub>相关: <a href="https://www.reddit.com/r/vibecoding/comments/1wmmjs5/i_built_a_free_jev_visualizer_after_burning_5bn/">demo</a> · <a href="https://www.reddit.com/r/typesafe_ai/comments/1wmmlj7/i_built_a_free_jev_visualizer_after_burning_5bn/">discussion</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/pydantic/genai-prices/blob/main/prices/providers/typesafe.yml"><img src="https://opengraph.githubassets.com/1/pydantic/genai-prices" alt="genai-prices 的 TypeSafe 提供方" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/pydantic/genai-prices/blob/main/prices/providers/typesafe.yml">genai-prices 的 TypeSafe 提供方</a></b><br><sub>pydantic · GitHub · ⭐ 378 仓库 · 2025-06-21</sub><br>Pydantic 用于计算 LLM API 成本的库，扩展了 TypeSafe 定价，让发往 /v1/systemone 的 Jev 调用能被识别并按输入 token 计费。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/lmnr-ai/lmnr-python/tree/main/src/lmnr/opentelemetry_lib/opentelemetry/instrumentation/typesafe"><img src="https://opengraph.githubassets.com/1/lmnr-ai/lmnr-python" alt="Laminar 的 TypeSafe 埋点" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/lmnr-ai/lmnr-python/tree/main/src/lmnr/opentelemetry_lib/opentelemetry/instrumentation/typesafe">Laminar 的 TypeSafe 埋点</a></b><br><sub>lmnr-ai · GitHub · ⭐ 56 仓库 · 2024-06-14</sub><br>Laminar Python SDK 中的 OpenTelemetry 埋点，把 TypeSafe SDK 对 Jev 的 system_one 调用与其他 LLM 调用一起追踪为 span。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/braintrustdata/braintrust-sdk-javascript/blob/main/js/src/wrappers/typesafe.ts"><img src="https://raw.githubusercontent.com/braintrustdata/braintrust-sdk-javascript/main/braintrust-logo.svg" alt="Braintrust 的 TypeSafe 埋点" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/braintrustdata/braintrust-sdk-javascript/blob/main/js/src/wrappers/typesafe.ts">Braintrust 的 TypeSafe 埋点</a></b><br><sub>braintrustdata · GitHub · ⭐ 27 仓库 · 2023-07-17</sub><br>Braintrust JavaScript SDK 针对 @typesafe-ai/sdk 的埋点：wrapTypeSafe 和自动埋点把每次 systemOne 调用追踪为 Braintrust span，同时也追踪 AI SDK 的 evaluate 调用。<br><sub>相关: <a href="https://github.com/braintrustdata/braintrust-sdk-javascript">repo</a> · <a href="https://www.braintrust.dev">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/braintrustdata/braintrust-sdk-python/tree/main/py/src/braintrust/integrations/typesafe"><img src="https://raw.githubusercontent.com/braintrustdata/braintrust-sdk-python/main/braintrust-logo.svg" alt="Braintrust Python SDK 的 TypeSafe 集成" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/braintrustdata/braintrust-sdk-python/tree/main/py/src/braintrust/integrations/typesafe">Braintrust Python SDK 的 TypeSafe 集成</a></b><br><sub>braintrustdata · GitHub · ⭐ 19 仓库 · 2026-02-20</sub><br>Braintrust Python 追踪与评测 SDK 的内置集成，自动为 typesafe-sdk 的 system_one 调用埋点，让 Jev 的请求和答案以 Braintrust span 的形式出现。<br><sub>相关: <a href="https://github.com/braintrustdata/braintrust-sdk-python">repo</a> · <a href="https://www.braintrust.dev">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/lmnr-ai/lmnr-ts/tree/main/packages/lmnr/src/opentelemetry-lib/instrumentation/typesafe"><img src="https://opengraph.githubassets.com/1/lmnr-ai/lmnr-ts" alt="Laminar 的 TypeSafe 埋点" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/lmnr-ai/lmnr-ts/tree/main/packages/lmnr/src/opentelemetry-lib/instrumentation/typesafe">Laminar 的 TypeSafe 埋点</a></b><br><sub>lmnr-ai · GitHub · ⭐ 12 仓库 · 2024-06-22</sub><br>Laminar TypeScript SDK 中的 OpenTelemetry 埋点，为 TypeSafe SDK 的 systemOne 调用打补丁，把 Jev 的请求、响应和错误记录为 span。<br><sub>相关: <a href="https://github.com/lmnr-ai/lmnr-ts">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Coolhand-Labs/coolhand-ruby/blob/main/lib/coolhand/default_intercept_addresses.yml"><img src="https://opengraph.githubassets.com/1/Coolhand-Labs/coolhand-ruby" alt="Coolhand Ruby 的 TypeSafe 监控" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Coolhand-Labs/coolhand-ruby/blob/main/lib/coolhand/default_intercept_addresses.yml">Coolhand Ruby 的 TypeSafe 监控</a></b><br><sub>Coolhand-Labs · GitHub · ⭐ 10 仓库 · 2025-09-30</sub><br>Ruby gem，把 LLM API 调用记录到 Coolhand 分析平台，默认会拦截 TypeSafe Jev System One 请求以及其他提供方的请求。<br><sub>相关: <a href="https://coolhandlabs.com">app</a> · <a href="https://github.com/Coolhand-Labs/coolhand-ruby">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/spenceclark/Vessel/blob/main/src/Vessel/Formats/TypeSafeSystemOneAdapter.cs"><img src="https://raw.githubusercontent.com/spenceclark/Vessel/main/docs/assets/main_screen.png" alt="Vessel 的 System One 适配器" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/spenceclark/Vessel/blob/main/src/Vessel/Formats/TypeSafeSystemOneAdapter.cs">Vessel 的 System One 适配器</a></b><br><sub>spenceclark · GitHub · ⭐ 6 仓库 · 2026-08-27</sub><br>Vessel（本地优先的 LLM 流量可观测性代理）中的适配器，捕获直接发送或经 OpenRouter Decisions 发送的 TypeSafe System One 请求，并展示其类型化问题、答案和 token 用量。<br><sub>相关: <a href="https://vesselproxy.app/">app</a> · <a href="https://github.com/spenceclark/Vessel">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://arize.com/docs/phoenix/integrations/llm-providers/typesafe/typesafe-python"><img src="https://arizeai-433a7140.mintlify.app/mintlify-assets/_next/image?url=%2F_mintlify%2Fapi%2Fog%3Fdivision%3DTypeSafe%2BAI%26title%3DTypeSafe%2BAI%2BTracing%2B%2528Python%2529%26description%3DInstrument%2BTypeSafe%2BAI%2BSDK%2Bcalls%2Bin%2BPython%26theme%3D39bdea6277da2fa182a39f32&amp;w=1200&amp;q=100" alt="Arize Phoenix" width="240"></a></td>
<td valign="top"><b><a href="https://arize.com/docs/phoenix/integrations/llm-providers/typesafe/typesafe-python">Arize Phoenix</a></b><br><sub>Arize · 文章</sub><br>面向 Python 和 TypeScript 的 OpenInference 埋点，记录 Jev 的输入、输出和 token 数。<br><sub>相关: <a href="https://pypi.org/project/openinference-instrumentation-typesafe/">pypi</a> · <a href="https://github.com/Arize-ai/openinference/tree/main/python/instrumentation/openinference-instrumentation-typesafe">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://arize.com/docs/phoenix/integrations/llm-providers/typesafe"><img src="https://arizeai-433a7140.mintlify.app/mintlify-assets/_next/image?url=%2F_mintlify%2Fapi%2Fog%3Fdivision%3DTypeSafe%2BAI%26title%3DTypeSafe%2BAI%26description%3DTypeSafe%2BAI%2Bis%2Ba%2Bmodel%2Bprovider%2Bthat%2Banswers%2Btyped%2Bquestions%2Babout%2Bstructured%2Bstate%252C%2Breturning%2Bschema-validated%2Bresults%2Binstead%2Bof%2Bfree-form%2Btext.%26theme%3D39bdea6277da2fa182a39f32&amp;w=1200&amp;q=100" alt="Phoenix 的 TypeSafe AI 集成" width="240"></a></td>
<td valign="top"><b><a href="https://arize.com/docs/phoenix/integrations/llm-providers/typesafe">Phoenix 的 TypeSafe AI 集成</a></b><br><sub>Arize Phoenix · 文档</sub><br>Arize Phoenix 的集成文档，介绍如何在 Python 和 TypeScript 中追踪 TypeSafe AI 调用，只需一行设置代码，每个 Jev 决策就会被记录为一条 trace。<br><sub>相关: <a href="https://x.com/ArizePhoenix/status/2101068055782797731">x</a></sub></td>
</tr>
</table>

还缺什么？[提交一个资源](https://github.com/Li-Evan/awesome-jev/issues/new/choose)。
