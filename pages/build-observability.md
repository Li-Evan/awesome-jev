# 🔌 Build with Jev: Observability

Ways to call Jev from your stack: hosted access, framework adapters, observability, and community SDKs. 14 entries, ranked by community traction.

[← Back to Awesome Jev](https://github.com/Li-Evan/awesome-jev#observability)

[Model Access](https://github.com/Li-Evan/awesome-jev/blob/main/pages/build-model-access.md) (68) · [Framework Adapters](https://github.com/Li-Evan/awesome-jev/blob/main/pages/build-frameworks.md) (174) · **Observability** · [Community SDKs](https://github.com/Li-Evan/awesome-jev/blob/main/pages/build-community-sdks.md) (107)

<table>
<tr>
<td width="260" valign="top"><a href="https://github.com/comet-ml/opik/tree/main/sdks/python/src/opik/integrations/typesafe"><img src="https://raw.githubusercontent.com/comet-ml/opik/refs/heads/main/apps/opik-documentation/documentation/static/img/opik-logo.svg" alt="Opik TypeSafe integration" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/comet-ml/opik/tree/main/sdks/python/src/opik/integrations/typesafe">Opik TypeSafe integration</a></b><br><sub>comet-ml · GitHub · ⭐ 22.2k repo · 2023-05-10</sub><br>Opik Python SDK integration that wraps sync and async TypeSafe clients so every Jev call is traced in Opik's LLM observability and evaluation platform.<br><sub>Also: <a href="https://www.comet.com/docs/opik/">docs</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Arize-ai/phoenix/tree/main/docs/phoenix/integrations/llm-providers/typesafe"><img src="https://repository-images.githubusercontent.com/564072810/f3666cdf-cb3e-4056-8a25-27cb3e6b5848" alt="Phoenix TypeSafe tracing" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Arize-ai/phoenix/tree/main/docs/phoenix/integrations/llm-providers/typesafe">Phoenix TypeSafe tracing</a></b><br><sub>Arize-ai · Docs · ⭐ 11.6k repo · 2022-11-09</sub><br>OpenInference instrumentation for the TypeSafe Python and TypeScript SDKs that records each System One call's state, questions and typed answers as spans in Arize Phoenix.<br><sub>Also: <a href="https://pypi.org/project/openinference-instrumentation-typesafe">pypi</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://langfuse.com/integrations/model-providers/typesafe"><img src="https://langfuse.com/api/og?title=Observability+for+TypeSafe+Jev+with+Langfuse&amp;description=Trace+TypeSafe+Jev+System+One+decisions+with+Langfuse+using+OpenInference+auto-instrumentation.+No+client+wrapper+required.&amp;section=Integrations" alt="Langfuse TypeSafe integration" width="240"></a></td>
<td valign="top"><b><a href="https://langfuse.com/integrations/model-providers/typesafe">Langfuse TypeSafe integration</a></b><br><sub>Langfuse · Docs · ⭐ 244 · 2026-09-19</sub><br>Integration guide and notebook for tracing Jev System One calls in Langfuse via OpenInference auto-instrumentation, with no client wrapper.<br><sub>Also: <a href="https://github.com/langfuse/langfuse-docs/blob/main/content/integrations/model-providers/typesafe.mdx">repo</a> · <a href="https://github.com/langfuse/langfuse-docs/blob/main/cookbook/integration_typesafe.ipynb">cookbook</a> · <a href="https://langfuse.com/blog/2026-09-18-using-typesafes-jev-for-evals">blog</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Arize-ai/openinference/tree/main/python/instrumentation/openinference-instrumentation-typesafe"><img src="https://opengraph.githubassets.com/1/Arize-ai/openinference" alt="OpenInference TypeSafe instrumentation" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Arize-ai/openinference/tree/main/python/instrumentation/openinference-instrumentation-typesafe">OpenInference TypeSafe instrumentation</a></b><br><sub>Arize-ai · GitHub · ⭐ 1.2k repo · 2023-12-26</sub><br>OpenTelemetry instrumentation for the TypeSafe Python SDK that traces each Jev System One call's state, model, questions and typed answers, usable with any OTel backend.<br><sub>Also: <a href="https://arize-ai.github.io/openinference/">docs</a> · <a href="https://pypi.org/project/openinference-instrumentation-typesafe">pypi</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/andududu/jeview"><img src="https://raw.githubusercontent.com/andududu/jeview/main/docs/side-by-side.png" alt="Jeview" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/andududu/jeview">Jeview</a></b><br><sub>andududu · GitHub · ⭐ 21 · 2026-09-21</sub><br>Unofficial local gateway that sits between your code and TypeSafe, forwards every Jev request, stores each call in SQLite, and draws calls on a live map as they happen.<br><sub>Also: <a href="https://www.reddit.com/r/vibecoding/comments/1wmmjs5/i_built_a_free_jev_visualizer_after_burning_5bn/">demo</a> · <a href="https://www.reddit.com/r/typesafe_ai/comments/1wmmlj7/i_built_a_free_jev_visualizer_after_burning_5bn/">discussion</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/pydantic/genai-prices/blob/main/prices/providers/typesafe.yml"><img src="https://opengraph.githubassets.com/1/pydantic/genai-prices" alt="genai-prices TypeSafe provider" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/pydantic/genai-prices/blob/main/prices/providers/typesafe.yml">genai-prices TypeSafe provider</a></b><br><sub>pydantic · GitHub · ⭐ 378 repo · 2025-06-21</sub><br>Pydantic library for calculating LLM API costs, extended with TypeSafe pricing so Jev calls to /v1/systemone are matched and billed per input token.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/lmnr-ai/lmnr-python/tree/main/src/lmnr/opentelemetry_lib/opentelemetry/instrumentation/typesafe"><img src="https://opengraph.githubassets.com/1/lmnr-ai/lmnr-python" alt="Laminar TypeSafe instrumentation" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/lmnr-ai/lmnr-python/tree/main/src/lmnr/opentelemetry_lib/opentelemetry/instrumentation/typesafe">Laminar TypeSafe instrumentation</a></b><br><sub>lmnr-ai · GitHub · ⭐ 56 repo · 2024-06-14</sub><br>OpenTelemetry instrumentation in the Laminar Python SDK that traces TypeSafe SDK system_one calls to Jev as spans alongside other LLM calls.</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/braintrustdata/braintrust-sdk-javascript/blob/main/js/src/wrappers/typesafe.ts"><img src="https://raw.githubusercontent.com/braintrustdata/braintrust-sdk-javascript/main/braintrust-logo.svg" alt="Braintrust TypeSafe instrumentation" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/braintrustdata/braintrust-sdk-javascript/blob/main/js/src/wrappers/typesafe.ts">Braintrust TypeSafe instrumentation</a></b><br><sub>braintrustdata · GitHub · ⭐ 27 repo · 2023-07-17</sub><br>Braintrust JavaScript SDK instrumentation for @typesafe-ai/sdk: wrapTypeSafe and auto-instrumentation trace every systemOne call into Braintrust spans, alongside tracing for the AI SDK evaluate call.<br><sub>Also: <a href="https://github.com/braintrustdata/braintrust-sdk-javascript">repo</a> · <a href="https://www.braintrust.dev">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/braintrustdata/braintrust-sdk-python/tree/main/py/src/braintrust/integrations/typesafe"><img src="https://raw.githubusercontent.com/braintrustdata/braintrust-sdk-python/main/braintrust-logo.svg" alt="Braintrust Python TypeSafe integration" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/braintrustdata/braintrust-sdk-python/tree/main/py/src/braintrust/integrations/typesafe">Braintrust Python TypeSafe integration</a></b><br><sub>braintrustdata · GitHub · ⭐ 19 repo · 2026-02-20</sub><br>Built-in integration in Braintrust's Python tracing and evals SDK that auto-instruments typesafe-sdk system_one calls so Jev requests and answers show up as Braintrust spans.<br><sub>Also: <a href="https://github.com/braintrustdata/braintrust-sdk-python">repo</a> · <a href="https://www.braintrust.dev">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/lmnr-ai/lmnr-ts/tree/main/packages/lmnr/src/opentelemetry-lib/instrumentation/typesafe"><img src="https://opengraph.githubassets.com/1/lmnr-ai/lmnr-ts" alt="Laminar TypeSafe instrumentation" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/lmnr-ai/lmnr-ts/tree/main/packages/lmnr/src/opentelemetry-lib/instrumentation/typesafe">Laminar TypeSafe instrumentation</a></b><br><sub>lmnr-ai · GitHub · ⭐ 12 repo · 2024-06-22</sub><br>OpenTelemetry instrumentation in Laminar's TypeScript SDK that patches the TypeSafe SDK's systemOne calls to record Jev requests, responses and errors as spans.<br><sub>Also: <a href="https://github.com/lmnr-ai/lmnr-ts">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Coolhand-Labs/coolhand-ruby/blob/main/lib/coolhand/default_intercept_addresses.yml"><img src="https://opengraph.githubassets.com/1/Coolhand-Labs/coolhand-ruby" alt="Coolhand Ruby TypeSafe monitoring" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Coolhand-Labs/coolhand-ruby/blob/main/lib/coolhand/default_intercept_addresses.yml">Coolhand Ruby TypeSafe monitoring</a></b><br><sub>Coolhand-Labs · GitHub · ⭐ 10 repo · 2025-09-30</sub><br>Ruby gem that logs LLM API calls to the Coolhand analytics platform and intercepts TypeSafe Jev System One requests by default alongside other providers.<br><sub>Also: <a href="https://coolhandlabs.com">app</a> · <a href="https://github.com/Coolhand-Labs/coolhand-ruby">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/spenceclark/Vessel/blob/main/src/Vessel/Formats/TypeSafeSystemOneAdapter.cs"><img src="https://raw.githubusercontent.com/spenceclark/Vessel/main/docs/assets/main_screen.png" alt="Vessel System One adapter" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/spenceclark/Vessel/blob/main/src/Vessel/Formats/TypeSafeSystemOneAdapter.cs">Vessel System One adapter</a></b><br><sub>spenceclark · GitHub · ⭐ 6 repo · 2026-08-27</sub><br>Adapter in Vessel, a local-first observability proxy for LLM traffic, that captures TypeSafe System One requests sent directly or via OpenRouter Decisions and shows their typed questions, answers and token usage.<br><sub>Also: <a href="https://vesselproxy.app/">app</a> · <a href="https://github.com/spenceclark/Vessel">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://arize.com/docs/phoenix/integrations/llm-providers/typesafe/typesafe-python"><img src="https://arizeai-433a7140.mintlify.app/mintlify-assets/_next/image?url=%2F_mintlify%2Fapi%2Fog%3Fdivision%3DTypeSafe%2BAI%26title%3DTypeSafe%2BAI%2BTracing%2B%2528Python%2529%26description%3DInstrument%2BTypeSafe%2BAI%2BSDK%2Bcalls%2Bin%2BPython%26theme%3D39bdea6277da2fa182a39f32&amp;w=1200&amp;q=100" alt="Arize Phoenix" width="240"></a></td>
<td valign="top"><b><a href="https://arize.com/docs/phoenix/integrations/llm-providers/typesafe/typesafe-python">Arize Phoenix</a></b><br><sub>Arize · Article</sub><br>OpenInference instrumentation for Python and TypeScript that records Jev inputs, outputs, and token counts.<br><sub>Also: <a href="https://pypi.org/project/openinference-instrumentation-typesafe/">pypi</a> · <a href="https://github.com/Arize-ai/openinference/tree/main/python/instrumentation/openinference-instrumentation-typesafe">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://arize.com/docs/phoenix/integrations/llm-providers/typesafe"><img src="https://arizeai-433a7140.mintlify.app/mintlify-assets/_next/image?url=%2F_mintlify%2Fapi%2Fog%3Fdivision%3DTypeSafe%2BAI%26title%3DTypeSafe%2BAI%26description%3DTypeSafe%2BAI%2Bis%2Ba%2Bmodel%2Bprovider%2Bthat%2Banswers%2Btyped%2Bquestions%2Babout%2Bstructured%2Bstate%252C%2Breturning%2Bschema-validated%2Bresults%2Binstead%2Bof%2Bfree-form%2Btext.%26theme%3D39bdea6277da2fa182a39f32&amp;w=1200&amp;q=100" alt="Phoenix TypeSafe AI integration" width="240"></a></td>
<td valign="top"><b><a href="https://arize.com/docs/phoenix/integrations/llm-providers/typesafe">Phoenix TypeSafe AI integration</a></b><br><sub>Arize Phoenix · Docs</sub><br>Arize Phoenix integration docs for tracing TypeSafe AI calls in Python and TypeScript, so each Jev decision is recorded as a trace with a line of setup code.<br><sub>Also: <a href="https://x.com/ArizePhoenix/status/2101068055782797731">x</a></sub></td>
</tr>
</table>

Missing something? [Suggest a resource](https://github.com/Li-Evan/awesome-jev/issues/new/choose).
