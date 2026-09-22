# 🔌 用 Jev 开发: 社区 SDK

[English](https://github.com/Li-Evan/awesome-jev/blob/main/pages/build-community-sdks.md) · **简体中文**

从你的技术栈调用 Jev 的方式：托管访问、框架适配、可观测性和社区 SDK。共 107 条，按社区热度排序。

[← 返回 Awesome Jev](https://github.com/Li-Evan/awesome-jev/blob/main/README.zh-CN.md#社区-sdk)

[模型访问](https://github.com/Li-Evan/awesome-jev/blob/main/zh-CN/pages/build-model-access.md) (68) · [框架适配](https://github.com/Li-Evan/awesome-jev/blob/main/zh-CN/pages/build-frameworks.md) (174) · [可观测性](https://github.com/Li-Evan/awesome-jev/blob/main/zh-CN/pages/build-observability.md) (14) · **社区 SDK**

<table>
<tr>
<td width="260" valign="top"><a href="https://github.com/zcoder-run/rust-sysone"><img src="https://opengraph.githubassets.com/1/zcoder-run/rust-sysone" alt="rust-sysone" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/zcoder-run/rust-sysone">rust-sysone</a></b><br><sub>zcoder-run · GitHub · ⭐ 4 · 2026-09-19</sub><br>早期的非官方 System One API Rust 客户端，作者也写了 genai crate，提供链式调用的 Request 构造器和类型化的 Noul、Choice 和 Score 问题。<br><sub>相关: <a href="https://www.youtube.com/watch?v=pU73lYF7R1I">video</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/http4k/http4k/tree/master/connect/ai/typesafe"><img src="https://kotlin.link/awesome-kotlin.svg" alt="http4k 的 TypeSafe 连接器" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/http4k/http4k/tree/master/connect/ai/typesafe">http4k 的 TypeSafe 连接器</a></b><br><sub>http4k · GitHub · ⭐ 2.8k 仓库 · 2017-03-23</sub><br>http4k Kotlin 工具包的 TypeSafe 连接器，带类型化的 System One 客户端和一个 fake 实现，把 Jev 的 Noul、Choice 和 Score 问题暴露为 http4k action。<br><sub>相关: <a href="https://http4k.org">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/obie/ruby_decision_model"><img src="https://opengraph.githubassets.com/1/obie/ruby_decision_model" alt="ruby_decision_model" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/obie/ruby_decision_model">ruby_decision_model</a></b><br><sub>obie · GitHub · ⭐ 49 · 2026-09-18</sub><br>仅用标准库的 Ruby 客户端，面向 Jev 这类决策模型，一个 Client 默认对接 OpenRouter，也可用 TypeSafe 原生 API，并解析选项、概率、评分和用量。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/dannote/jev"><img src="https://opengraph.githubassets.com/1/dannote/jev" alt="Jev for OTP" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/dannote/jev">Jev for OTP</a></b><br><sub>dannote · GitHub · ⭐ 28 · 2026-09-17</sub><br>把 Jev 当作 OTP 对等进程的 Elixir 客户端：GenServer 发送 state 和类型化问题，每个答案以消息的形式到达，可直接模式匹配，同时可有上百个调用在途。<br><sub>相关: <a href="https://hex.pm/packages/jev">hex</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/krzyzanowskim/TypeSafe"><img src="https://pbs.twimg.com/media/HSmaEbYX0AAvCsn.png?name=orig" alt="TypeSafe Swift SDK" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/krzyzanowskim/TypeSafe">TypeSafe Swift SDK</a></b><br><sub>krzyzanowskim · GitHub · ⭐ 27 · 2026-09-19</sub><br>TypeSafe System One API 的 SwiftPM 客户端，Noul、Choice、Score 问题的行为与官方 JavaScript SDK 保持一致，附带一个小型演示 app。<br><sub>相关: <a href="https://x.com/krzyzanowskim/status/2101380130752831644">demo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/carldaws/hunch"><img src="https://opengraph.githubassets.com/1/carldaws/hunch" alt="Hunch" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/carldaws/hunch">Hunch</a></b><br><sub>carldaws · GitHub · ⭐ 14 · 2026-09-18</sub><br>用于概率控制流的 Ruby 和 Rails gem，把 Jev 的答案变成 Ruby 值，提供 chance、pick 和 rate 调用，以及 likely? 这类分级谓词，可直接基于判断做分支。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/ainame/swift-typesafe"><img src="https://opengraph.githubassets.com/1/ainame/swift-typesafe" alt="swift-typesafe" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/ainame/swift-typesafe">swift-typesafe</a></b><br><sub>ainame · GitHub · ⭐ 13 · 2026-09-18</sub><br>非官方的 Swift 6.4 SDK，跟随 Python SDK 0.7.0 的 API，带一个生成类型化答案的 @QuestionSet 宏，支持动态问题和 Linux。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/cequence-io/openai-scala-client/tree/master/typesafe-client"><img src="https://opengraph.githubassets.com/1/cequence-io/openai-scala-client" alt="openai-scala-client 的 TypeSafe 模块" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/cequence-io/openai-scala-client/tree/master/typesafe-client">openai-scala-client 的 TypeSafe 模块</a></b><br><sub>cequence-io · GitHub · ⭐ 248 仓库 · 2026-09-16</sub><br>异步 openai-scala-client 中的 TypeSafe 模块，把共享 state 和类型化问题发给 Jev，附有按置信度把关的路由、语义查找和 OpenAI 风格适配器的示例。<br><sub>相关: <a href="https://github.com/cequence-io/openai-scala-client">repo</a> · <a href="https://github.com/cequence-io/openai-scala-client/tree/master/openai-examples/src/main/scala/io/cequence/openaiscala/examples/typesafe">examples</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/atharvamhaske/typesafe-sdk-go"><img src="https://raw.githubusercontent.com/atharvamhaske/typesafe-sdk-go/main/images/test.png" alt="typesafe-sdk-go (atharvamhaske)" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/atharvamhaske/typesafe-sdk-go">typesafe-sdk-go (atharvamhaske)</a></b><br><sub>atharvamhaske · GitHub · ⭐ 12 · 2026-09-18</sub><br>非官方 Go SDK，与官方 Python 和 JavaScript SDK 遵循同一传输协议，支持类型化的 Choice、Score、Noul 问题、类型化的答案联合类型和模型发现。<br><sub>相关: <a href="https://x.com/AtharvaXDevs/status/2102067600947834960">demo</a> · <a href="https://typesafe-sdk-go.mintlify.site/">docs</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Twister915/typesafe-ai"><img src="https://opengraph.githubassets.com/1/Twister915/typesafe-ai" alt="typesafe-ai (Rust)" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Twister915/typesafe-ai">typesafe-ai (Rust)</a></b><br><sub>Twister915 · GitHub · ⭐ 11 · 2026-09-16</sub><br>System One 的类型化 Rust 客户端，可选异步 reqwest 或阻塞 ureq 后端，重试过程可观测，把 Noul、Choice 和 Score 答案反序列化为带用量数据的 Rust 枚举。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Tangerg/typesafe-sdk-go"><img src="https://opengraph.githubassets.com/1/Tangerg/typesafe-sdk-go" alt="Go SDK" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Tangerg/typesafe-sdk-go">Go SDK</a></b><br><sub>Tangerg · GitHub · ⭐ 9 · 2026-09-18</sub><br>System One 端点的社区版 Go 客户端。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/cablehead/jev.nu"><img src="https://opengraph.githubassets.com/1/cablehead/jev.nu" alt="jev.nu" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/cablehead/jev.nu">jev.nu</a></b><br><sub>cablehead · GitHub · ⭐ 8 · 2026-09-18</sub><br>单文件的 Nushell 模块，用于 System One API：把内容通过管道传入、提出问题，得到可以在 shell 里过滤和排序的数值答案，附分步教程。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/NSStudent/JevSwiftSDK"><img src="https://opengraph.githubassets.com/1/NSStudent/JevSwiftSDK" alt="Swift SDK" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/NSStudent/JevSwiftSDK">Swift SDK</a></b><br><sub>NSStudent · GitHub · ⭐ 8 · 2026-09-19</sub><br>社区版 Swift 客户端，默认使用 <code>jev-latest</code>。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/captain-corgi/typesafe-sdk-go"><img src="https://opengraph.githubassets.com/1/captain-corgi/typesafe-sdk-go" alt="typesafe-sdk-go" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/captain-corgi/typesafe-sdk-go">typesafe-sdk-go</a></b><br><sub>captain-corgi · GitHub · ⭐ 8 · 2026-09-20</sub><br>社区版 TypeSafe API Go SDK，运行时零依赖，功能与 Python SDK v0.7.0 对齐，返回静态类型的 Noul、Choice 和 Score 答案。<br><sub>相关: <a href="https://captain-corgi.github.io/typesafe-sdk-go/">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/okooo5km/jev"><img src="https://opengraph.githubassets.com/1/okooo5km/jev" alt="jev (okooo5km)" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/okooo5km/jev">jev (okooo5km)</a></b><br><sub>okooo5km · GitHub · ⭐ 7 · 2026-09-18</sub><br>单文件、仅用标准库的 Python CLI 兼 Agent Skill，可在 shell 中通过 TypeSafe API 或 OpenRouter 做 yes、pick 和 score 决策，带校准概率、语义 grep 和批处理模式。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/inanna-malick/jev-dsl"><img src="https://opengraph.githubassets.com/1/inanna-malick/jev-dsl" alt="jev-dsl" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/inanna-malick/jev-dsl">jev-dsl</a></b><br><sub>inanna-malick · GitHub · ⭐ 7 · 2026-09-17</sub><br>早期 alpha 阶段的 Haskell DSL，用一个表达式写出一组带标签的 Jev 问题，推断其类型，渲染出精确的请求 JSON，并按相同标签解码答案。<br><sub><b>Jev 用法:</b> Choice 的答案通过穷尽的带标签处理函数来消费，这些处理函数携带对应选项的载荷。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/ticofab/scala-jev-sdk"><img src="https://opengraph.githubassets.com/1/ticofab/scala-jev-sdk" alt="scala-jev-sdk" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/ticofab/scala-jev-sdk">scala-jev-sdk</a></b><br><sub>ticofab · GitHub · ⭐ 6 · 2026-09-19</sub><br>System One API 的 Scala 3 客户端，不捆绑任何 effect 系统：交给它任意 sttp 后端（Future、阻塞式、cats-effect、ZIO），即可读取类型化的 Noul、Choice 和 Score 答案。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/joshmn/typesafe-sdk"><img src="https://opengraph.githubassets.com/1/joshmn/typesafe-sdk" alt="typesafe-sdk (Ruby)" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/joshmn/typesafe-sdk">typesafe-sdk (Ruby)</a></b><br><sub>joshmn · GitHub · ⭐ 6 · 2026-09-16</sub><br>社区版 System One API Ruby 客户端，构建 Noul、Choice 和 Score 问题，可附带结构化指令，默认使用 jev-latest。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/saibimajdi/typesafeai-dotnet-sdk"><img src="https://opengraph.githubassets.com/1/saibimajdi/typesafeai-dotnet-sdk" alt="typesafeai-dotnet-sdk" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/saibimajdi/typesafeai-dotnet-sdk">typesafeai-dotnet-sdk</a></b><br><sub>saibimajdi · GitHub · ⭐ 6 · 2026-09-16</sub><br>社区版 TypeSafe System One API .NET SDK，针对文本或 JSON state 提出类型化的 Noul、Choice 和 Score 问题，返回有概率支撑的结构化答案。<br><sub>相关: <a href="https://saibimajdi.github.io/typesafeai-dotnet-sdk/">docs</a> · <a href="https://saibimajdi.github.io/typesafeai-dotnet-sdk">link</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/fbettag/aquila"><img src="https://opengraph.githubassets.com/1/fbettag/aquila" alt="Aquila" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/fbettag/aquila">Aquila</a></b><br><sub>fbettag · GitHub · ⭐ 5 · 2025-09-27</sub><br>用于编排兼容 OpenAI 的 Responses 和 Chat Completions API 的 Elixir 库，也能向 TypeSafe System One 提出类型化的 choice、score 和 noul 问题，附带录制/回放测试夹具以实现确定性测试。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/devbackend/jevgo"><img src="https://opengraph.githubassets.com/1/devbackend/jevgo" alt="jevgo" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/devbackend/jevgo">jevgo</a></b><br><sub>devbackend · GitHub · ⭐ 5 · 2026-09-21</sub><br>非官方、仅用标准库的 System One API Go 客户端，一次调用发送 state 和一个由类型化 Noul、Choice 和 Score 问题组成的 map，返回模型版本、用量和请求 ID。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/nshkrdotcom/typesafe_sdk"><img src="https://raw.githubusercontent.com/nshkrdotcom/typesafe_sdk/main/assets/typesafe_sdk.svg" alt="typesafe_sdk (Elixir)" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/nshkrdotcom/typesafe_sdk">typesafe_sdk (Elixir)</a></b><br><sub>nshkrdotcom · GitHub · ⭐ 5 · 2026-09-17</sub><br>面向 Jev 类型化问题和概率答案的 Elixir SDK，最终版 0.4.1 已指向与服务商无关的后继项目 system_one_sdk，后者提供批处理、遥测和 OTP 集成。<br><sub>相关: <a href="https://github.com/nshkrdotcom/system_one_sdk">successor</a> · <a href="https://hex.pm/packages/typesafe_sdk">hex</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Stumble/jev-go"><img src="https://opengraph.githubassets.com/1/Stumble/jev-go" alt="jev-go" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Stumble/jev-go">jev-go</a></b><br><sub>Stumble · GitHub · ⭐ 4 · 2026-09-17</sub><br>Jev System One API 的社区版 Go SDK 和 CLI，可直接调用 TypeSafe 或经由 Vercel AI Gateway，附带一个适配 skill 和供编程 agent 集成时参考的 AGENTS.md 指南。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/pambrose/jev4k"><img src="https://opengraph.githubassets.com/1/pambrose/jev4k" alt="jev4k" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/pambrose/jev4k">jev4k</a></b><br><sub>pambrose · GitHub · ⭐ 4 · 2026-09-20</sub><br>Kotlin DSL 和客户端，声明类型化的 Jev 问题（包括以枚举为值的选项），一次请求发出，并以类型化值读回答案；已发布到 Maven Central。<br><sub>相关: <a href="https://jev4k.com">site</a> · <a href="https://jev4k.com">link</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/alterhq/typesafe-sdk-swift"><img src="https://opengraph.githubassets.com/1/alterhq/typesafe-sdk-swift" alt="TypeSafe AI Swift SDK" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/alterhq/typesafe-sdk-swift">TypeSafe AI Swift SDK</a></b><br><sub>alterhq · GitHub · ⭐ 4 · 2026-09-15</sub><br>非官方、无依赖的 Swift 6 客户端，支持在 macOS、iOS、tvOS 和 watchOS 上提出 Choice、Score 和 Noul 问题，移植自官方 SDK，具备严格并发检查、重试和后端代理配置。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/kisshan13/typesafe-ai-go"><img src="https://opengraph.githubassets.com/1/kisshan13/typesafe-ai-go" alt="TypeSafe Go SDK (kisshan13)" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/kisshan13/typesafe-ai-go">TypeSafe Go SDK (kisshan13)</a></b><br><sub>kisshan13 · GitHub · ⭐ 4 · 2026-09-20</sub><br>社区版 System One API Go 客户端，提供原始请求 struct、链式问题构造器、重试和示例，默认使用 jev-latest。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/gilljon/typesafe-ai-rs"><img src="https://opengraph.githubassets.com/1/gilljon/typesafe-ai-rs" alt="typesafe-ai-rs" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/gilljon/typesafe-ai-rs">typesafe-ai-rs</a></b><br><sub>gilljon · GitHub · ⭐ 4 · 2026-09-17</sub><br>独立开发的 System One API Rust 客户端，提供异步和阻塞两种客户端，支持类型化的 Noul、Choice、Score 问题、模型发现、重试和取消。<br><sub>相关: <a href="https://docs.rs/typesafe-ai-rs">docs</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/y0usaf/typesafe-cli"><img src="https://opengraph.githubassets.com/1/y0usaf/typesafe-cli" alt="typesafe-cli" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/y0usaf/typesafe-cli">typesafe-cli</a></b><br><sub>y0usaf · GitHub · ⭐ 4 · 2026-09-16</sub><br>Jev 的命令行工具：输入一段 state 和类型化问题，以数字形式输出 Noul 概率、带置信度的 Choice 选择和 Score 位置，一次约 0.3 s 的往返就能问多个问题。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/virolea/jev"><img src="https://opengraph.githubassets.com/1/virolea/jev" alt="jev (Ruby)" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/virolea/jev">jev (Ruby)</a></b><br><sub>virolea · GitHub · ⭐ 3 · 2026-09-19</sub><br>Jev API 的 Ruby gem，提供 ask、choose 和 score 方法，分别对应 Noul、Choice 和 Score 问题，针对同一个 state 并行评估。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/gudcks0305/jev-java"><img src="https://opengraph.githubassets.com/1/gudcks0305/jev-java" alt="Jev Java" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/gudcks0305/jev-java">Jev Java</a></b><br><sub>gudcks0305 · GitHub · ⭐ 3 · 2026-09-19</sub><br>非官方的 Java 17+ Jev SDK，可经由 TypeSafe、OpenRouter、Vercel AI Gateway 或 Cloudflare 调用，支持声明式 record 输出，并可选支持 Spring Boot 和 WebClient。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Olti1947/jev-java"><img src="https://opengraph.githubassets.com/1/Olti1947/jev-java" alt="Jev Java SDK" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Olti1947/jev-java">Jev Java SDK</a></b><br><sub>Olti1947 · GitHub · ⭐ 3 · 2026-09-18</sub><br>符合 Java 习惯的 Java 17+ System One API 客户端，可通过 Maven 和 Gradle 获取，每个原语都接受纯字符串或结构化的 instructions 和 criteria，并提供 Rubric 和 ScoreLevel 辅助类。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Gaurav-Gosain/jev-go"><img src="https://opengraph.githubassets.com/1/Gaurav-Gosain/jev-go" alt="jev-go (Gaurav-Gosain)" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Gaurav-Gosain/jev-go">jev-go (Gaurav-Gosain)</a></b><br><sub>Gaurav-Gosain · GitHub · ⭐ 3 · 2026-09-16</sub><br>System One API 的 Go 客户端，提供类型化的 Noul、Choice 和 Score 问题与答案、常见结构的构造函数和批处理辅助函数。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/elue-dev/jev_elixir"><img src="https://external-preview.redd.it/H7x1s1uO-DHxBlxVk8E9TndaY2laC_-actLTnK0i4f8.png?auto=webp&amp;s=9b569bd26ace5f9fc499e5387541164e1efa6bac" alt="jev_elixir" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/elue-dev/jev_elixir">jev_elixir</a></b><br><sub>elue-dev · GitHub · ⭐ 3 · 2026-09-21</sub><br>小巧的 Elixir Jev 客户端，提供 Jev.ask?/2 这类返回真正布尔值的辅助函数，通过 TypeSafe 或 OpenRouter 的 Decisions API 支持 Noul、Choice 和 Score。<br><sub>相关: <a href="https://www.reddit.com/r/elixir/comments/1wmnxzb/i_built_a_small_elixir_client_for_jev_with/">demo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/InsaneArts/typesafe-sdk-swift"><img src="https://opengraph.githubassets.com/1/InsaneArts/typesafe-sdk-swift" alt="TypeSafe AI Swift SDK" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/InsaneArts/typesafe-sdk-swift">TypeSafe AI Swift SDK</a></b><br><sub>InsaneArts · GitHub · ⭐ 3 · 2026-09-17</sub><br>无依赖的 Swift 6 社区 SDK，支持 macOS 13 和 iOS 16，答案类型从你的问题推断而来，多个答案以类型化元组返回。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/sd109/typesafe-go"><img src="https://opengraph.githubassets.com/1/sd109/typesafe-go" alt="TypeSafe Go" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/sd109/typesafe-go">TypeSafe Go</a></b><br><sub>sd109 · GitHub · ⭐ 3 · 2026-09-19</sub><br>Go 工具集，包含仅用标准库的 TypeSafe 客户端、qgrep（类似 grep、用自然语言问题检索文本的 CLI），以及一个针对 Kubernetes pod 日志提问的 kubectl 插件。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/geilt/typesafe-cli"><img src="https://opengraph.githubassets.com/1/geilt/typesafe-cli" alt="typesafe-cli (geilt)" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/geilt/typesafe-cli">typesafe-cli (geilt)</a></b><br><sub>geilt · GitHub · ⭐ 3 · 2026-09-17</sub><br>只用标准库的 Python CLI，同时也是给 Claude、Codex 和 Grok 用的 agent skill，用类型化的 Choice、Score 和 Noul 问题评估一段 state，并输出结构化答案。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Premo-Cloud/typesafe-sdk-java"><img src="https://opengraph.githubassets.com/1/Premo-Cloud/typesafe-sdk-java" alt="typesafe-sdk-java" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Premo-Cloud/typesafe-sdk-java">typesafe-sdk-java</a></b><br><sub>Premo-Cloud · GitHub · ⭐ 3 · 2026-09-18</sub><br>社区版 System One API Java 17+ 客户端，只依赖 Jackson，附带一个提供 TypeSafeClient bean 的 Spring Boot starter。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/codeitlikemiley/typesafe-sdk-rust"><img src="https://opengraph.githubassets.com/1/codeitlikemiley/typesafe-sdk-rust" alt="typesafe-sdk-rust" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/codeitlikemiley/typesafe-sdk-rust">typesafe-sdk-rust</a></b><br><sub>codeitlikemiley · GitHub · ⭐ 3 · 2026-09-16</sub><br>与 Python typesafe-sdk 0.6.0 契约一致的 Rust 客户端，支持异步和可选的阻塞调用，提供类型化的问题和答案封装，并附有给编程 agent 看的 AGENTS.md。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/hardkoded/typesafe-sdk-dotnet"><img src="https://external-preview.redd.it/tthHFZd6glTBd08_ONWbLfaWSCVKu5vk9pgLfdyltOo.png?auto=webp&amp;s=c67973361c59a5979b398167925110122ecf1e52" alt="TypeSafe.AI.Sdk (.NET)" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/hardkoded/typesafe-sdk-dotnet">TypeSafe.AI.Sdk (.NET)</a></b><br><sub>hardkoded · GitHub · ⭐ 3 · 2026-09-20</sub><br>JavaScript TypeSafe SDK 的非官方 .NET 移植版，目标框架为 net10.0 和 netstandard2.0，提供 Choice、Score 和 Noul 问题构建器以及类型化答案。<br><sub>相关: <a href="https://www.reddit.com/r/dotnet/comments/1wlp12g/net_devs_should_also_join_the_jev_hype/">demo</a> · <a href="https://hardkoded.github.io/typesafe-sdk-dotnet/">docs</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/jamesward/zio-typesafe-ai"><img src="https://opengraph.githubassets.com/1/jamesward/zio-typesafe-ai" alt="zio-typesafe-ai" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/jamesward/zio-typesafe-ai">zio-typesafe-ai</a></b><br><sub>jamesward · GitHub · ⭐ 3 · 2026-09-17</sub><br>基于 Scala 3 和 ZIO 的 Jev System One API 客户端，一次往返就能问多个类型化的 Noul、Choice 和 Score 问题，并以与问题结构一致的 NamedTuple 返回答案。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/mhrlife/goai-kit/tree/master/jev"><img src="https://opengraph.githubassets.com/1/mhrlife/goai-kit" alt="goai-kit jev" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/mhrlife/goai-kit/tree/master/jev">goai-kit jev</a></b><br><sub>mhrlife · GitHub · ⭐ 45 仓库 · 2025-05-18</sub><br>goai-kit LLM 库中独立的 Jev Go 客户端，只用标准库：经 OpenRouter 或 TypeSafe 提出类型化的 Noul、Choice 和 Score 问题并获取答案，支持 context 取消和按可重试性分类的 HTTP 错误。<br><sub>相关: <a href="https://github.com/mhrlife/goai-kit">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/mzainzulifqar/jev-php-sdk"><img src="https://opengraph.githubassets.com/1/mzainzulifqar/jev-php-sdk" alt="Jev SDK for PHP" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/mzainzulifqar/jev-php-sdk">Jev SDK for PHP</a></b><br><sub>mzainzulifqar · GitHub · ⭐ 2 · 2026-09-18</sub><br>与框架无关的 PHP 8.1+ System One API 客户端，兼容任意 PSR-18 HTTP 客户端和 Laravel 8-13，提供 Noul、Score 和 Choice 问题构造器。<br><sub>相关: <a href="https://packagist.org/packages/mzainzulifqar/jev-php-sdk">packagist</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/AboveColin/jevclient"><img src="https://opengraph.githubassets.com/1/AboveColin/jevclient" alt="jevclient" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/AboveColin/jevclient">jevclient</a></b><br><sub>AboveColin · GitHub · ⭐ 2 · 2026-09-17</sub><br>基于 aiohttp 的异步 Python Jev 客户端，把 Noul、Choice 和 Score 问题合并到一个请求中；实测 3 个问题耗时 712 毫秒，100 个问题耗时 714 毫秒。<br><sub>相关: <a href="https://pypi.org/project/jevclient/">pypi</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/fgn/jevgo"><img src="https://opengraph.githubassets.com/1/fgn/jevgo" alt="jevgo" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/fgn/jevgo">jevgo</a></b><br><sub>fgn · GitHub · ⭐ 2 · 2026-09-17</sub><br>无依赖的 System One API Go 客户端，覆盖与官方 SDK 相同的接口，支持函数式选项、context 取消和可选的 Langfuse 追踪。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/simxnherrera/jevr"><img src="https://opengraph.githubassets.com/1/simxnherrera/jevr" alt="jevr" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/simxnherrera/jevr">jevr</a></b><br><sub>simxnherrera · GitHub · ⭐ 2 · 2026-09-18</sub><br>R 客户端，通过 TypeSafe 或 OpenRouter 把 state 和类型化问题发给 Jev，以 R 对象返回答案、概率、置信度和用量。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/javiergradiche/ruby_llm-providers-typesafe"><img src="https://opengraph.githubassets.com/1/javiergradiche/ruby_llm-providers-typesafe" alt="RubyLLM 提供方" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/javiergradiche/ruby_llm-providers-typesafe">RubyLLM 提供方</a></b><br><sub>javiergradiche · GitHub · ⭐ 2 · 2026-09-18</sub><br>为 RubyLLM 库加入 Jev 提供方。<br><sub>相关: <a href="https://rubygems.org/gems/ruby_llm-providers-typesafe">rubygems</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/innocentdiaz/s1_ruby"><img src="https://raw.githubusercontent.com/innocentdiaz/s1_ruby/master/preview.png" alt="s1-ruby" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/innocentdiaz/s1_ruby">s1-ruby</a></b><br><sub>innocentdiaz · GitHub · ⭐ 2 · 2026-09-18</sub><br>把 System One 度量做成语言原语的 Ruby gem，提供 noul、choice 和 score 三类问题、量表、批处理，以及一个由自身规格测试套件覆盖的 TypeSafe 提供方，另有配套的 Rails 包。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/2389-research/typesafe-go"><img src="https://opengraph.githubassets.com/1/2389-research/typesafe-go" alt="typesafe-go (2389-research)" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/2389-research/typesafe-go">typesafe-go (2389-research)</a></b><br><sub>2389-research · GitHub · ⭐ 2 · 2026-09-17</sub><br>零依赖的 System One Go 客户端，每个问题都是一个带类型的 handle，通过它读回答案，由编译器检查答案的形状。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/typesafe-sdk-csharp/typesafe-sdk"><img src="https://opengraph.githubassets.com/1/typesafe-sdk-csharp/typesafe-sdk" alt="TypeSafe.AI (.NET SDK)" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/typesafe-sdk-csharp/typesafe-sdk">TypeSafe.AI (.NET SDK)</a></b><br><sub>typesafe-sdk-csharp · GitHub · ⭐ 2 · 2026-09-20</sub><br>非官方的 System One .NET SDK（NuGet 包名 TypeSafe.AI），使用兼容 NativeAOT 的源码生成 JSON，提供用于构建 Noul、Choice 和 Score 的 Questions.Build 构建器、基于 Polly 的容错、依赖注入和 OpenTelemetry。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Hawxy/TypeSafeAI.Net"><img src="https://opengraph.githubassets.com/1/Hawxy/TypeSafeAI.Net" alt="TypeSafeAI.Net" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Hawxy/TypeSafeAI.Net">TypeSafeAI.Net</a></b><br><sub>Hawxy · GitHub · ⭐ 2 · 2026-09-17</sub><br>社区版 System One API .NET SDK，支持类型化问题集、重试、HttpClientFactory 和 DI、AOT 安全，并提供 Microsoft.Extensions.AI 的护栏、路由、工具和评估器适配器。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/sunholo-data/ailang/blob/dev/examples/runnable/decide_jev.ail"><img src="https://repository-images.githubusercontent.com/1064514521/5c945465-b033-4839-9357-182fc39a2503" alt="AILANG decide_jev" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/sunholo-data/ailang/blob/dev/examples/runnable/decide_jev.ail">AILANG decide_jev</a></b><br><sub>sunholo-data · GitHub · ⭐ 34 仓库 · 2025-09-26</sub><br>可运行的探索性示例，在纯 AILANG（为 AI 编写代码设计的 effect 类型语言）中通过 OpenRouter 的 Decisions API 调用 Jev，把 Noul、Choice 和 Score 建模为保留完整分布的类型化问题和答案。<br><sub>相关: <a href="https://github.com/sunholo-data/ailang">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/maruel/genai/tree/main/providers/typesafe"><img src="https://opengraph.githubassets.com/1/maruel/genai" alt="genai 的 typesafe 提供方" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/maruel/genai/tree/main/providers/typesafe">genai 的 typesafe 提供方</a></b><br><sub>maruel · GitHub · ⭐ 32 仓库 · 2025-03-06</sub><br>Go AI 包 maruel/genai 的 TypeSafe 提供方：Noul、Choice 和 Score 问题以 Go struct 字段声明，答案连同置信度和完整分布解码回同一个 struct。<br><sub>相关: <a href="https://github.com/maruel/genai">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/anilsenay/jev"><img src="https://opengraph.githubassets.com/1/anilsenay/jev" alt="jev (Go)" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/anilsenay/jev">jev (Go)</a></b><br><sub>anilsenay · GitHub · ⭐ 1 · 2026-09-17</sub><br>System One API 的非官方 Go 客户端，答案直接以你自己的 Go 类型返回，例如在 Intent 枚举上做 Choice 就得到一个 Intent，无法作答的问题会在请求发出前就报错。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/guillemus/jev-go"><img src="https://opengraph.githubassets.com/1/guillemus/jev-go" alt="jev-go" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/guillemus/jev-go">jev-go</a></b><br><sub>guillemus · GitHub · ⭐ 1 · 2026-09-17</sub><br>极简的非官方 Jev API Go SDK，支持 Noul、Choice 和 Score 问题、结构化输入、自定义客户端配置和模型列表。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/kyledickey/jev-go"><img src="https://opengraph.githubassets.com/1/kyledickey/jev-go" alt="jev-go" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/kyledickey/jev-go">jev-go</a></b><br><sub>kyledickey · GitHub · ⭐ 1 · 2026-09-19</sub><br>Jev API 的 Go SDK，提供类型化的 Noul、Choice 和 Score 问题与答案类型、携带状态码和原始响应体的 APIError，以及一个 examples/basic 示例程序。<br><sub>相关: <a href="https://docs.typesafe.ai">link</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/abeldzan/jev-rs"><img src="https://opengraph.githubassets.com/1/abeldzan/jev-rs" alt="jev-rs" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/abeldzan/jev-rs">jev-rs</a></b><br><sub>abeldzan · GitHub · ⭐ 1 · 2026-09-18</sub><br>异步优先的 TypeSafe API Rust 客户端，提供类型化的 System One 问题与答案、模型发现、可配置重试、结构化错误和可选的阻塞式客户端。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/luigivis/jev-sdk-java"><img src="https://opengraph.githubassets.com/1/luigivis/jev-sdk-java" alt="jev-sdk-java" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/luigivis/jev-sdk-java">jev-sdk-java</a></b><br><sub>luigivis · GitHub · ⭐ 1 · 2026-09-21</sub><br>非官方的 Java 21 Jev System One API 客户端，用枚举、sealed interface 和 record 为请求建模，只要请求能编译通过，API 就会接受。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Solido/jev_dart"><img src="https://opengraph.githubassets.com/1/Solido/jev_dart" alt="jev_dart" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Solido/jev_dart">jev_dart</a></b><br><sub>Solido · GitHub · ⭐ 1 · 2026-09-19</sub><br>纯 Dart 编写的 Jev 客户端，可用于 CLI、服务器和 Flutter 应用，在原生平台上使用连接池化的 HTTP/2 传输，在 Web 上使用 HTTP/1.1。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/AbdelStark/s1-rs"><img src="https://opengraph.githubassets.com/1/AbdelStark/s1-rs" alt="s1" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/AbdelStark/s1-rs">s1</a></b><br><sub>AbdelStark · GitHub · ⭐ 1 · 2026-09-16</sub><br>Rust 的类型化 System One 层，从 enum 和 struct 推导出 Choice、Score 和 Noul 问题，新增一个 enum 变体后，match 在补上处理之前无法通过编译；附带一个不走网络的测试用假客户端。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/mattneel/typesafe"><img src="https://opengraph.githubassets.com/1/mattneel/typesafe" alt="TypeSafe (Elixir)" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/mattneel/typesafe">TypeSafe (Elixir)</a></b><br><sub>mattneel · GitHub · ⭐ 1 · 2026-09-16</sub><br>基于 Req、Zoi 和 Telemetry 的社区版 Elixir 客户端，一次请求发送 Choice、Noul 和 Score 问题，返回带概率的 struct，另有测试辅助和一个 schema mix 任务。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/SergeAx/typesafe-sdk-go"><img src="https://opengraph.githubassets.com/1/SergeAx/typesafe-sdk-go" alt="TypeSafe AI Go SDK (sergeax)" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/SergeAx/typesafe-sdk-go">TypeSafe AI Go SDK (sergeax)</a></b><br><sub>SergeAx · GitHub · ⭐ 1 · 2026-09-17</sub><br>Go 1.23 的 System One API 客户端，一次请求可发送 Noul、Choice 和 Score 问题，重试会遵循 Retry-After，错误可用 errors.Is 匹配，并使用 slog 记录日志。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/stacklok/typesafe-go"><img src="https://opengraph.githubassets.com/1/stacklok/typesafe-go" alt="TypeSafe Go (Stacklok)" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/stacklok/typesafe-go">TypeSafe Go (Stacklok)</a></b><br><sub>stacklok · GitHub · ⭐ 1 · 2026-09-21</sub><br>由 Stacklok 维护、注重安全、仅用标准库的 System One API Go 客户端，凭证选项需显式提供，构造时不会隐式读取环境变量、写日志或发起网络调用。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/binnash/typesafe-sdk"><img src="https://opengraph.githubassets.com/1/binnash/typesafe-sdk" alt="TypeSafe PHP SDK" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/binnash/typesafe-sdk">TypeSafe PHP SDK</a></b><br><sub>binnash · GitHub · ⭐ 1 · 2026-09-17</sub><br>System One API 的 PHP 8.2+ SDK，基于 PSR-18 HTTP 客户端，支持 Noul、Choice 和 Score 问题、重试、日志，并提供 Laravel 集成。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/unimtx/typesafe-sdk-go"><img src="https://opengraph.githubassets.com/1/unimtx/typesafe-sdk-go" alt="TypeSafe SDK for Go" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/unimtx/typesafe-sdk-go">TypeSafe SDK for Go</a></b><br><sub>unimtx · GitHub · ⭐ 1 · 2026-09-19</sub><br>社区版 System One API Go 客户端，只用标准库，支持类型化的 Choice、Score 和 Noul 问题、context、重试和结构化错误。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/JedimEmO/typesafe-client"><img src="https://opengraph.githubassets.com/1/JedimEmO/typesafe-client" alt="typesafe-client" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/JedimEmO/typesafe-client">typesafe-client</a></b><br><sub>JedimEmO · GitHub · ⭐ 1 · 2026-09-16</sub><br>非官方的 System One API 异步 Rust 客户端，每添加一个问题都会返回一个带类型的 key，因此把 Choice 答案当作是/否概率来读取会直接编译失败。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/zhirschtritt/typesafe-go"><img src="https://opengraph.githubassets.com/1/zhirschtritt/typesafe-go" alt="typesafe-go" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/zhirschtritt/typesafe-go">typesafe-go</a></b><br><sub>zhirschtritt · GitHub · ⭐ 1 · 2026-09-16</sub><br>非官方、零依赖的 System One Go 客户端，支持模型发现，可配置重试、base URL、默认模型和单次请求覆盖。<br><sub>相关: <a href="https://pkg.go.dev/github.com/zhirschtritt/typesafe-go">docs</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/cole-gillespie/typesafe-go"><img src="https://opengraph.githubassets.com/1/cole-gillespie/typesafe-go" alt="typesafe-go (cole-gillespie)" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/cole-gillespie/typesafe-go">typesafe-go (cole-gillespie)</a></b><br><sub>cole-gillespie · GitHub · ⭐ 1 · 2026-09-17</sub><br>非官方、零依赖的 Go SDK，参照官方 TypeScript 和 Python 客户端设计，提供类型化答案、重试和 context 取消。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/AbdelStark/typesafe-rs"><img src="https://opengraph.githubassets.com/1/AbdelStark/typesafe-rs" alt="typesafe-rs" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/AbdelStark/typesafe-rs">typesafe-rs</a></b><br><sub>AbdelStark · GitHub · ⭐ 1 · 2026-09-16</sub><br>延迟优先的社区版 System One Rust 客户端，支持异步请求、可选的阻塞接口和本地 mock 测试，环境变量、重试和错误类型都与官方 SDK 一致。<br><sub>相关: <a href="https://docs.rs/typesafe-rs/latest/typesafe_rs/">docs</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/yunusey/typesafe-sdk-cpp"><img src="https://opengraph.githubassets.com/1/yunusey/typesafe-sdk-cpp" alt="typesafe-sdk-cpp" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/yunusey/typesafe-sdk-cpp">typesafe-sdk-cpp</a></b><br><sub>yunusey · GitHub · ⭐ 1 · 2026-09-18</sub><br>非官方的 TypeSafe API C++23 客户端，从 Rust SDK 移植而来，把关于某段 state 的具名问题发送到 /v1/systemone，并返回类型化答案。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/dwisiswant0/typesafe-sdk-go"><img src="https://opengraph.githubassets.com/1/dwisiswant0/typesafe-sdk-go" alt="typesafe-sdk-go (dwisiswant0)" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/dwisiswant0/typesafe-sdk-go">typesafe-sdk-go (dwisiswant0)</a></b><br><sub>dwisiswant0 · GitHub · ⭐ 1 · 2026-09-18</sub><br>TypeSafe API 的 Go 客户端，在一次请求中发送多个具名的 Noul、Choice 和 Score 问题，state 和判断标准可以是字符串、JSON 对象或 Go struct。<br><sub>相关: <a href="https://go.dw1.io/typesafe-sdk-go?godoc=1">docs</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Butochnikov/typesafe-sdk-php"><img src="https://opengraph.githubassets.com/1/Butochnikov/typesafe-sdk-php" alt="typesafe-sdk-php" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Butochnikov/typesafe-sdk-php">typesafe-sdk-php</a></b><br><sub>Butochnikov · GitHub · ⭐ 1 · 2026-09-17</sub><br>社区版 System One PHP 8.2+ 客户端，返回类型化的 Noul、Choice 和 Score 答案，支持同步调用和基于 Guzzle promise 的异步请求、重试以及 PSR-3 日志。<br><sub>相关: <a href="https://github.com/butochnikov/laravel-typesafe-jev">laravel</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/afurm/typesafe-sdk-ruby"><img src="https://framerusercontent.com/images/RtIGTDwO43jR4ZDilesXiR5znc.jpg" alt="typesafe-sdk-ruby" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/afurm/typesafe-sdk-ruby">typesafe-sdk-ruby</a></b><br><sub>afurm · GitHub · ⭐ 1 · 2026-09-20</sub><br>官方 JavaScript SDK 0.6.0 的非官方 Ruby 移植版，提供类型化答案对象、重试、超时、取消和可配置的日志。<br><sub>相关: <a href="https://typesafe.ai">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/marandaneto/typesafe-sdk-swift"><img src="https://opengraph.githubassets.com/1/marandaneto/typesafe-sdk-swift" alt="typesafe-sdk-swift" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/marandaneto/typesafe-sdk-swift">typesafe-sdk-swift</a></b><br><sub>marandaneto · GitHub · ⭐ 1 · 2026-09-18</sub><br>官方 JS 和 Python SDK 的实验性 Swift 6 移植版，使用 Swift Package Manager、async/await 和 URLSession，在各 Apple 平台上都没有第三方运行时依赖。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/vinnie357/typesafe_sdk_ex"><img src="https://opengraph.githubassets.com/1/vinnie357/typesafe_sdk_ex" alt="typesafe_sdk_ex" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/vinnie357/typesafe_sdk_ex">typesafe_sdk_ex</a></b><br><sub>vinnie357 · GitHub · ⭐ 1 · 2026-09-17</sub><br>基于 Req 构建、参照官方 JS SDK 设计的 Elixir SDK，提供 Noul、Choice 和 Score 问题辅助函数、system_one/3、模型列表和类型化错误返回。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/tryAGI/TypeSafeAI"><img src="https://opengraph.githubassets.com/1/tryAGI/TypeSafeAI" alt="TypeSafeAI (.NET, tryAGI)" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/tryAGI/TypeSafeAI">TypeSafeAI (.NET, tryAGI)</a></b><br><sub>tryAGI · GitHub · ⭐ 1 · 2026-09-21</sub><br>支持 NativeAOT 的 .NET SDK，传输层由官方 OpenAPI 定义生成，另有手写的类型化问题、批处理、路由、依赖注入和 Microsoft.Extensions.AI 集成。<br><sub>相关: <a href="https://tryagi.github.io/TypeSafeAI/">docs</a> · <a href="https://tryagi.github.io/TypeSafeAI">link</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/maddygoround/typesafeai-cli"><img src="https://opengraph.githubassets.com/1/maddygoround/typesafeai-cli" alt="typesafeai-cli" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/maddygoround/typesafeai-cli">typesafeai-cli</a></b><br><sub>maddygoround · GitHub · ⭐ 1 · 2026-09-18</sub><br>Jev 的 Python CLI，人或 agent 都可以运行它，针对 JSON state 文件提出 Noul、Choice 和 Score 问题，提供 decide、screen 和 verify 流程、失败即拒绝（fail-closed）的答案以及可安装的 agent skill。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/chez-shanpu/typesafeai-go"><img src="https://opengraph.githubassets.com/1/chez-shanpu/typesafeai-go" alt="typesafeai-go" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/chez-shanpu/typesafeai-go">typesafeai-go</a></b><br><sub>chez-shanpu · GitHub · ⭐ 1 · 2026-09-17</sub><br>独立开发的 TypeSafe AI API Go 客户端，发送 Noul、Choice 和 Score 问题，并以对应的 Go 类型返回答案。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/andrueandersoncs/lion/tree/main/packages/typesafe-ai"><img src="https://opengraph.githubassets.com/1/andrueandersoncs/lion" alt="@lionlang/typesafe-ai" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/andrueandersoncs/lion/tree/main/packages/typesafe-ai">@lionlang/typesafe-ai</a></b><br><sub>andrueandersoncs · GitHub · ⭐ 16 仓库 · 2025-12-11</sub><br>绑定库，把 Jev 的每个问题原语以及 System One 和 models API 暴露为 Lion 中的函数；Lion 是一种基于 JSON 的 Lisp，其求值器运行在 Effect v4 上。<br><sub>相关: <a href="https://github.com/andrueandersoncs/lion">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"></td>
<td valign="top"><b><a href="https://gitlab.com/porky11/jev">Rust 客户端</a></b><br><sub>porky11 · GitHub · ⬇ 68 · 2026-09-17</sub><br>发布为 <code>jev</code> 的社区版 Rust crate。<br><sub>相关: <a href="https://crates.io/crates/jev">crates</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/sethbang/venice-py/blob/main/src/venice_ai/resources/decisions.py"><img src="https://raw.githubusercontent.com/sethbang/venice-py/main/website/static/img/venice-py-banner.png" alt="venice-py 的 Decisions 资源" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/sethbang/venice-py/blob/main/src/venice_ai/resources/decisions.py">venice-py 的 Decisions 资源</a></b><br><sub>sethbang · GitHub · ⭐ 13 仓库 · 2025-06-02</sub><br>Venice.ai 的非官方异步 Python SDK，其中的 Decisions 资源对接 Venice 的 System One 模型，返回经过校验、带概率的 Noul、Choice 和 Score 答案。<br><sub>相关: <a href="https://github.com/sethbang/venice-py">repo</a> · <a href="https://venice-docs.sbang.dev/">docs</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/MelloB1989/karma/tree/main/ai/jev"><img src="https://raw.githubusercontent.com/MelloB1989/karma/main/docs/karma.png" alt="Karma 的 Jev 包" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/MelloB1989/karma/tree/main/ai/jev">Karma 的 Jev 包</a></b><br><sub>MelloB1989 · GitHub · ⭐ 9 仓库 · 2024-11-30</sub><br>Karma 工具库中的 Jev Go 客户端，提供类型化问题和答案、批处理、重试、错误类型，以及一个 guard 子包。<br><sub>相关: <a href="https://github.com/MelloB1989/karma">repo</a> · <a href="https://docs.mellob.in">docs</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Muvon/octolib/blob/master/src/evaluation/providers/typesafe.rs"><img src="https://opengraph.githubassets.com/1/Muvon/octolib" alt="octolib 的 evaluation 模块" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Muvon/octolib/blob/master/src/evaluation/providers/typesafe.rs">octolib 的 evaluation 模块</a></b><br><sub>Muvon · GitHub · ⭐ 8 仓库 · 2025-08-28</sub><br>把 30+ 个 AI 提供方统一到一个 provider:model 字符串之后的 Rust 库，新增面向 TypeSafe Jev 的结构化 evaluation 模块，可直接调用，也可经 Cloudflare AI Gateway 计费。<br><sub><b>Jev 用法:</b> octolib::evaluate 针对一个 state 构建 Noul 和 Choice 问题，例如判断一条客服消息的紧急程度和所属部门。</sub><br><sub>相关: <a href="https://octomind.run/product/octolib">app</a> · <a href="https://github.com/Muvon/octolib">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/roze-team/roze/blob/main/crates/roze-ai/src/typesafe_system_one.rs"><img src="https://opengraph.githubassets.com/1/roze-team/roze" alt="Roze 的 System One 客户端" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/roze-team/roze/blob/main/crates/roze-ai/src/typesafe_system_one.rs">Roze 的 System One 客户端</a></b><br><sub>roze-team · GitHub · ⭐ 7 仓库 · 2026-06-06</sub><br>Roze Rust 服务框架 roze-ai crate 中的 TypeSafe System One API 类型化 Rust 客户端，提供 Noul、Choice 和 Score 问题类型及请求校验。<br><sub>相关: <a href="https://github.com/roze-team/roze">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/model-clis/jev"><img src="https://opengraph.githubassets.com/1/model-clis/jev" alt="Jev CLI" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/model-clis/jev">Jev CLI</a></b><br><sub>model-clis · GitHub · 2026-09-18</sub><br>无状态的 Rust CLI 加一个 agent skill，把 Jev 的判断变成 shell 原语：stdout 输出稳定的 JSON，退出码可供脚本和 CI 分支。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/lhotwll217/jev-cli"><img src="https://opengraph.githubassets.com/1/lhotwll217/jev-cli" alt="jev-cli (lhotwll217)" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/lhotwll217/jev-cli">jev-cli (lhotwll217)</a></b><br><sub>lhotwll217 · GitHub · 2026-09-18</sub><br>TypeSafe System One API 的轻量 CLI，输入 JSON、输出类型化决策，适合临时实验、评测循环和 agent harness，密钥保存在操作系统的凭证存储中。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/bariskisir/JevSharp"><img src="https://raw.githubusercontent.com/bariskisir/JevSharp/master/assets/jevsharp-logo.svg" alt="JevSharp" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/bariskisir/JevSharp">JevSharp</a></b><br><sub>bariskisir · GitHub · 2026-09-21</sub><br>面向 .NET 10 的 SDK，可通过 TypeSafe、OpenRouter、Vercel AI Gateway 及兼容端点调用 Jev 做决策，支持依赖注入、故障转移、重试和日志。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/kunobi-ninja/kunobi-jev"><img src="https://opengraph.githubassets.com/1/kunobi-ninja/kunobi-jev" alt="kunobi-jev" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/kunobi-ninja/kunobi-jev">kunobi-jev</a></b><br><sub>kunobi-ninja · GitHub · 2026-09-17</sub><br>System One API 的 Rust 客户端，noul、choice 和 score 构造器会在发送前强制检查 255 个选项和 2-10 个等级的上限，另有归一化评分和对选项排序的辅助函数。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/lu-zero/systemone"><img src="https://opengraph.githubassets.com/1/lu-zero/systemone" alt="systemone" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/lu-zero/systemone">systemone</a></b><br><sub>lu-zero · GitHub · 2026-09-18</sub><br>与运行时无关的 TypeSafe systemone API Rust 客户端，提供一个 derive 宏和一个基于 facet 反射的 crate，可从 Rust enum 生成 Choice 的标签和描述。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/tinyhumansai/tinyjevclient"><img src="https://opengraph.githubassets.com/1/tinyhumansai/tinyjevclient" alt="TinyJevClient" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/tinyhumansai/tinyjevclient">TinyJevClient</a></b><br><sub>tinyhumansai · GitHub · 2026-09-17</sub><br>System One API 的类型化 Rust 客户端，会对照原始请求校验响应，并在答案之外返回延迟、尝试次数和用量；也可配合 OpenRouter 使用。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/oceanByte/tsai-cli"><img src="https://opengraph.githubassets.com/1/oceanByte/tsai-cli" alt="tsai" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/oceanByte/tsai-cli">tsai</a></b><br><sub>oceanByte · GitHub · 2026-09-17</sub><br>TypeSafe System One API 的非官方命令行封装，适用于 shell 管道、临时 CI 关卡、pre-commit hook，以及需要 Jev 判断但不想引入客户端库的编程 agent。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/dotnetvibecoderz/vibe_sdk/tree/main/TypeSafeSDK"><img src="https://opengraph.githubassets.com/1/dotnetvibecoderz/vibe_sdk" alt="TypeSafe .NET SDK (Gravicode)" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/dotnetvibecoderz/vibe_sdk/tree/main/TypeSafeSDK">TypeSafe .NET SDK (Gravicode)</a></b><br><sub>DotNetVibeCoderz · GitHub · 2026-09-19</sub><br>强类型的 .NET 10 System One API 客户端，附带本地模拟器、CLI、REST API、Blazor 应用、notebook 和一个 WPF 棋盘游戏演示，文档有印尼语和英语两种。<br><sub>相关: <a href="https://github.com/dotnetvibecoderz/vibe_sdk">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/ufec/typesafe-sdk-kotlin"><img src="https://opengraph.githubassets.com/1/ufec/typesafe-sdk-kotlin" alt="TypeSafe AI Kotlin SDK" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/ufec/typesafe-sdk-kotlin">TypeSafe AI Kotlin SDK</a></b><br><sub>ufec · GitHub · 2026-09-18</sub><br>官方 JavaScript SDK 0.6.0 的 Kotlin 移植版，面向 Android 和 JVM，答案类型由问题推导，重试策略与上游一致，并支持 HTTP 和 SOCKS5 代理。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/hfiguera/typesafe_ai"><img src="https://opengraph.githubassets.com/1/hfiguera/typesafe_ai" alt="TypeSafe for Elixir" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/hfiguera/typesafe_ai">TypeSafe for Elixir</a></b><br><sub>hfiguera · GitHub · 2026-09-16</sub><br>面向延迟敏感应用、基于 Mint 的 Elixir 客户端，提供受监督的 HTTP/1 和 HTTP/2 连接、有界并发与队列、请求截止时间、重试、遥测和可选的连接池。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://dev.to/jamilxt/i-built-the-first-java-sdk-for-jev-typesafes-system-one-model-2m37"><img src="https://media2.dev.to/dynamic/image/width=1200,height=627,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Farticles%2Fbel61ixedyfbdjbymetl.png" alt="typesafe-ai-java" width="240"></a></td>
<td valign="top"><b><a href="https://dev.to/jamilxt/i-built-the-first-java-sdk-for-jev-typesafes-system-one-model-2m37">typesafe-ai-java</a></b><br><sub>jamilxt · 文章 · 2026-09-20</sub><br>讲述如何为 Jev 构建非官方 JVM 客户端的文章：已发布到 Maven Central，包含纯 Java 核心以及 Kotlin 和 Spring starter 模块，并附有真实 API 测试结果。<br><sub>相关: <a href="https://github.com/jamilxt/typesafe-ai-java">repo</a> · <a href="https://github.com/jamilxt/typesafe-ai-java">project</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/hnegishi/typesafe-ai-ruby"><img src="https://opengraph.githubassets.com/1/hnegishi/typesafe-ai-ruby" alt="typesafe-ai-ruby" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/hnegishi/typesafe-ai-ruby">typesafe-ai-ruby</a></b><br><sub>hnegishi · GitHub · 2026-09-19</sub><br>System One API 的 Ruby 客户端，除标准库外零依赖，可发送 Choice、Score 和 Noul 问题，返回带概率和置信度的答案。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/noahbclarkson/typesafe-api-rs"><img src="https://opengraph.githubassets.com/1/noahbclarkson/typesafe-api-rs" alt="typesafe-api (Rust)" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/noahbclarkson/typesafe-api-rs">typesafe-api (Rust)</a></b><br><sub>noahbclarkson · GitHub · 2026-09-20</sub><br>强类型的 System One API Rust 客户端：一个判断只需用 Rust 类型描述一次，它既是请求也是解析后的答案，提供基于名称、类型化和 derive 三层接口。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Shubham510/typesafe-go"><img src="https://opengraph.githubassets.com/1/Shubham510/typesafe-go" alt="typesafe-go" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Shubham510/typesafe-go">typesafe-go</a></b><br><sub>Shubham510 · GitHub · 2026-09-18</sub><br>非官方、零依赖的 System One API Go 客户端，让 Go 服务无需 Python 或 Node sidecar 就能用 Choice、Score 和 Noul 问题调用 Jev，支持单次调用重试和模型列表。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/dfa1/typesafe-java"><img src="https://opengraph.githubassets.com/1/dfa1/typesafe-java" alt="typesafe-java" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/dfa1/typesafe-java">typesafe-java</a></b><br><sub>dfa1 · GitHub · 2026-09-19</sub><br>TypeSafe API 的 Java 21 客户端和 CLI，可发送任意 JSON state 以及 Noul、Choice 和 Score 问题，支持映射到类型化 record，附带 testkit 模块和用于 CI 检查的 uber-jar。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/nirgal-soft/typesafe-rs"><img src="https://opengraph.githubassets.com/1/nirgal-soft/typesafe-rs" alt="typesafe-rs" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/nirgal-soft/typesafe-rs">typesafe-rs</a></b><br><sub>nirgal-soft · GitHub · 2026-09-19</sub><br>TypeSafe API 的异步 Rust 客户端，外加一个 JSON 优先的 CLI，发送 Noul、Choice 和 Score 问题，返回 JSON 并带有明确定义的退出码。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/valksor/typesafe-sdk-go"><img src="https://opengraph.githubassets.com/1/valksor/typesafe-sdk-go" alt="typesafe-sdk-go" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/valksor/typesafe-sdk-go">typesafe-sdk-go</a></b><br><sub>valksor · GitHub · 2026-09-17</sub><br>地道的 System One API Go 客户端，目标是与官方 JS 和 Python SDK 1:1 对齐：相同的传输协议、环境变量配置、重试语义和类型化错误。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/RadixILS-Dev/typesafe-sdk-go"><img src="https://opengraph.githubassets.com/1/RadixILS-Dev/typesafe-sdk-go" alt="typesafe-sdk-go" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/RadixILS-Dev/typesafe-sdk-go">typesafe-sdk-go</a></b><br><sub>RadixILS-Dev · GitHub · 2026-09-18</sub><br>TypeSafe API 的 Go 客户端，遵循 Python SDK v0.6.0 的传输格式和重试行为，接口更小、更贴近 Go 原生风格。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/valksor/typesafe-sdk-php"><img src="https://opengraph.githubassets.com/1/valksor/typesafe-sdk-php" alt="typesafe-sdk-php" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/valksor/typesafe-sdk-php">typesafe-sdk-php</a></b><br><sub>valksor · GitHub · 2026-09-17</sub><br>严格类型的 System One API PHP 客户端，目标是与官方 JS 和 Python SDK 1:1 对齐，包括重试语义、请求元数据和类型化错误。<br><sub>相关: <a href="https://packagist.org/packages/valksor/typesafe-sdk-php">packagist</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Fox-Islam/typesafe-sdk-php"><img src="https://opengraph.githubassets.com/1/Fox-Islam/typesafe-sdk-php" alt="typesafe-sdk-php" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Fox-Islam/typesafe-sdk-php">typesafe-sdk-php</a></b><br><sub>Fox-Islam · GitHub · 2026-09-17</sub><br>System One API 的 PHP 8.3 客户端，支持类型化的 Noul、Choice 和 Score 问题，一次调用即可在 TypeSafe 和 OpenRouter 的 decisions 端点之间切换，可用任意 PSR-18 传输层，并提供 Laravel service provider。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/mattneel/typesafe.zig"><img src="https://opengraph.githubassets.com/1/mattneel/typesafe.zig" alt="typesafe.zig" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/mattneel/typesafe.zig">typesafe.zig</a></b><br><sub>mattneel · GitHub · 2026-09-17</sub><br>非官方 Zig 客户端，Noul、Choice 和 Score 答案以编译期确定类型的 struct 返回，所以 Choice 答案就是你自己的 enum，问题 id 拼错会直接编译失败。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/typesend/typesafe_ai"><img src="https://opengraph.githubassets.com/1/typesend/typesafe_ai" alt="typesafe_api" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/typesend/typesafe_ai">typesafe_api</a></b><br><sub>typesend · GitHub · 2026-09-16</sub><br>非官方的类型化 System One API Elixir 客户端，带离线测试桩，所有示例无需 key 即可运行，支持并发扇出和以 atom 为 key 的答案。<br><sub>相关: <a href="https://typesafe-api.hexdocs.pm/readme.html">docs</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/community-ports/typesafeai-sdk-rust-community"><img src="https://repository-images.githubusercontent.com/1376724675/9e1b5e33-ff5f-4b1b-be8a-3795aca2701b" alt="typesafeai-sdk-rust-community" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/community-ports/typesafeai-sdk-rust-community">typesafeai-sdk-rust-community</a></b><br><sub>community-ports · GitHub · 2026-09-19</sub><br>官方 Python SDK 的 Rust 移植版，新增用于类型化问题的 derive 宏、类型化的函数调用路由、复合打分、用于测试的 mock 传输层，以及并发批处理和重排辅助函数。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/jonesmelton/verdict"><img src="https://opengraph.githubassets.com/1/jonesmelton/verdict" alt="verdict (OCaml)" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/jonesmelton/verdict">verdict (OCaml)</a></b><br><sub>jonesmelton · GitHub · 2026-09-18</sub><br>基于 OCaml 5.2+ 和 Eio 的 System One API 客户端，每个问题 handle 都携带自己的答案类型，支持有界请求、TLS 和重试。</td>
</tr>
</table>

还缺什么？[提交一个资源](https://github.com/Li-Evan/awesome-jev/issues/new/choose)。
