# 🦾 机器人与仿真

[English](https://github.com/Li-Evan/awesome-jev/blob/main/scenarios/robotics.md) · **简体中文**

具身控制、驾驶模拟器，以及物理世界中的决策。共 61 条，按社区热度排序。

[← 返回 Awesome Jev](https://github.com/Li-Evan/awesome-jev/blob/main/README.zh-CN.md#按场景浏览)

<table>
<tr>
<td width="260" valign="top"><a href="https://x.com/leojrr/status/2101161666410893328"><img src="https://pbs.twimg.com/amplify_video_thumb/2101161072447180800/img/sRIOALT11TUpdAdU.jpg" alt="红绿灯控制" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/leojrr/status/2101161666410893328">红绿灯控制</a></b><br><sub>leojrr · X · ♥ 7k · 2026-09-19</sub><br>一个城市仿真，由 Jev 控制所有红绿灯；关掉 Jev 后，平均等待时间上升超过 600%。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/dimentary/status/2101018760371171420"><img src="https://pbs.twimg.com/amplify_video_thumb/2101017646154366976/img/02bH3Hxy9l0qEffS.jpg" alt="Jev 作为 MuJoCo 机械臂策略" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/dimentary/status/2101018760371171420">Jev 作为 MuJoCo 机械臂策略</a></b><br><sub>dimentary · X · ♥ 624 · 2026-09-18</sub><br>在 MuJoCo 中测试把 Jev 当作实时机械臂策略，根据文本形式的几何和接触信息，把每次更新拆成两次调用（先决定下一步做什么，再决定机械臂和夹爪如何移动）。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/openroboto-ai/jev-robot-control"><img src="https://raw.githubusercontent.com/openroboto-ai/jev-robot-control/main/media/final.png" alt="Jev 机器人控制" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/openroboto-ai/jev-robot-control">Jev 机器人控制</a></b><br><sub>openroboto-ai · GitHub · ⭐ 39 · 2026-09-19</sub><br>MuJoCo 实验：Jev 1.13、GPT-6 Astra 和 GPT-4.1 mini 通过选择运动方向和夹爪指令，操控 xArm7 把苹果放到盘子上；Jev 完成任务花费 $0.018825，对比的是 $5.933624。<br><sub>相关: <a href="https://x.com/openroboto/status/2101310974359941332">demo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://www.reddit.com/r/accelerate/comments/1wik4t9/i_rebuilt_tesla_full_self_driving_with_jev_in/"><img src="https://external-preview.redd.it/NnFjcHlrc2RmMHFoMWOYn9FxnzoyIXI3Fx4N6aO51f8iDw5FJT-WW_D6Hmfc.png?format=pjpg&amp;auto=webp&amp;s=ec0df8401debabb28f2f4bb0ee67fd44c0ea5411" alt="Jevpilot" width="240"></a></td>
<td valign="top"><b><a href="https://www.reddit.com/r/accelerate/comments/1wik4t9/i_rebuilt_tesla_full_self_driving_with_jev_in/">Jevpilot</a></b><br><sub>jpschroeder · Reddit · ▲ 182 · 2026-09-17</sub><br>3D 城市中的模拟自动驾驶演示，Jev 操控汽车并按逐向导航行驶，Justin Schroeder 称他不到一小时就做出来了。<br><sub>相关: <a href="https://x.com/jpschroeder/status/2100347770867458384">demo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/Raptor_zip/status/2101091398447505567"><img src="https://pbs.twimg.com/amplify_video_thumb/2101070240444772353/img/Ci_PCLcMigmoAdks.jpg" alt="Jev 控制双臂机器人" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/Raptor_zip/status/2101091398447505567">Jev 控制双臂机器人</a></b><br><sub>Raptor_zip · X · ♥ 432 · 2026-09-18</sub><br>双臂机器人，Jev 负责三层控制器中的决策层，IK 和物理计算留在代码中，响应时间 500 毫秒，每次试验约 0.5 日元。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/standardagents/jevpilot"><img src="https://raw.githubusercontent.com/standardagents/jevpilot/main/docs/try-jevpilot.svg" alt="JevPilot" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/standardagents/jevpilot">JevPilot</a></b><br><sub>standardagents · GitHub · ⭐ 160 · 2026-09-17</sub><br>Three.js 驾驶模拟器，由 Jev 作为自动驾驶仪选择运动和方向。<br><sub>相关: <a href="https://jevpilot.standardagents.ai">app</a> · <a href="https://jevpilot.standardagents.ai">app 2</a> · <a href="https://x.com/jpschroeder/status/2100698502531514761">demo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/SigGravitas/status/2100325221932958134"><img src="https://pbs.twimg.com/amplify_video_thumb/2100323655389474816/img/LLOAJ3wie1phk45K.jpg" alt="Jev 实时驾驶" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/SigGravitas/status/2100325221932958134">Jev 实时驾驶</a></b><br><sub>SigGravitas · X · ♥ 288 · 2026-09-16</sub><br>把 Jev 接到驾驶模拟器的原始控制上，模拟器不会因为它思考而暂停，Jev 实时操控一辆行驶中的车。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/MarianPogran/status/2101179679319241076"><img src="https://pbs.twimg.com/amplify_video_thumb/2101178753284014080/img/gtLhgbb1fSiGyTRY.jpg" alt="AgileX 机械臂上的 Jev 对 Astra" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/MarianPogran/status/2101179679319241076">AgileX 机械臂上的 Jev 对 Astra</a></b><br><sub>MarianPogran · X · ♥ 274 · 2026-09-19</sub><br>真实 AgileX 机械臂执行“把红色方块放进盒子”：Jev 用 27 秒完成，GPT-6 Astra 用了 1 分 11 秒，且成本低得多，机械臂速度限制在 10%。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/DXhusni/status/2100746693033816557"><img src="https://pbs.twimg.com/amplify_video_thumb/2100744327521824768/img/QudyKboQq-vCGHpy.jpg" alt="无视觉的空间控制" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/DXhusni/status/2100746693033816557">无视觉的空间控制</a></b><br><sub>DXhusni · X · ♥ 217 · 2026-09-18</sub><br>一个循环：把目标、当前几何与接触状态、可用控制及其预测效果、上一步结果交给 Jev，它就能在没有视觉的情况下零样本完成空间操作任务。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/metrox_eth/status/2101021471644733867"><img src="https://pbs.twimg.com/amplify_video_thumb/2101021391575457792/img/x227ubbFebYxck1p.jpg" alt="MOSS 捡垃圾" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/metrox_eth/status/2101021471644733867">MOSS 捡垃圾</a></b><br><sub>metrox_eth · X · ♥ 109 · 2026-09-18</sub><br>为 MOSS 机器人回放真实 Jev 决策的仿真：Jev 根据“捡起易拉罐”这样的指令选择目标，收到“捡起瓶子”时随即切换。<br><sub>相关: <a href="https://www.showrobotics.ai/moss-jev/">page</a> · <a href="https://showrobotics.ai/moss-jev">project</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/FBddcz/embodied-jev"><img src="https://raw.githubusercontent.com/FBddcz/embodied-jev/main/docs/workbench-desktop.png" alt="EmbodiedJev" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/FBddcz/embodied-jev">EmbodiedJev</a></b><br><sub>FBddcz · GitHub · ⭐ 165 · 2026-09-20</sub><br>模拟 MuJoCo Franka Panda 机械臂的浏览器工作台，由 Jev、Claude、OpenAI 兼容 API 或本地 MiniCPM5-2B 为抓取、堆叠和避障任务选择受限动作，成功与否由物理引擎判定。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/IsaacSin12/status/2100833538224668699"><img src="https://pbs.twimg.com/amplify_video_thumb/2100829039040802816/img/74S2rGSiTL_J7C5V.jpg" alt="MuJoCo 中的 MakerMods 机械臂" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/IsaacSin12/status/2100833538224668699">MuJoCo 中的 MakerMods 机械臂</a></b><br><sub>IsaacSin12 · X · ♥ 151 · 2026-09-18</sub><br>MuJoCo 中的 MakerMods Metal 机械臂，Jev 以 JSON 形式读取场景并选择受限动作（悬停、下降、抓取、抬起、放置），9 次决策完成任务，每次约 150 毫秒。<br><sub><b>Jev 用法:</b> 在受限动作上做类型化 Choice 并给出置信度分数；无法映射到场景的任务会拒绝执行。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/gabrycina/status/2100545285659480128"><img src="https://pbs.twimg.com/amplify_video_thumb/2100540294093504512/img/zuv5OwJUB-Tv7f-j.jpg" alt="Jev 让机械臂用上了钩子" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/gabrycina/status/2100545285659480128">Jev 让机械臂用上了钩子</a></b><br><sub>gabrycina · X · ♥ 150 · 2026-09-17</sub><br>让机械臂把够不着的红色方块放进绿色盒子：Jev 抓起一个钩子把方块拖近，放下钩子后完成任务，全程没有编写任何工具使用逻辑。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/RomanSlack/jev-drone"><img src="https://raw.githubusercontent.com/RomanSlack/jev-drone/main/docs/climb.png" alt="jev-drone" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/RomanSlack/jev-drone">jev-drone</a></b><br><sub>RomanSlack · GitHub · ⭐ 119 · 2026-09-16</sub><br>只靠摄像头的自主四旋翼，飞越 MuJoCo 中设有五个站点的障碍飞行场地，Jev 根据深度图提取的场景特征以约 2.5 Hz 判断每个情境意味着什么，时间敏感的控制留在代码中。<br><sub>相关: <a href="https://x.com/RomanSlack1/status/2100335978229690683">demo</a> · <a href="https://jev-drone.vercel.app">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://www.reddit.com/r/developersIndia/comments/1wjqwg2/experimenting_with_the_new_jev_model_as_a_real/"><img src="https://external-preview.redd.it/YnloMmNra3phYXFoMaCH-vwZSCX2hwQkWiNrTAK6JEGFvhs9LLeMHZLHmHVD.png?format=pjpg&amp;auto=webp&amp;s=822b9d622e88464e3874eb59484a4eb793323be9" alt="Jev 自动驾驶决策层" width="240"></a></td>
<td valign="top"><b><a href="https://www.reddit.com/r/developersIndia/comments/1wjqwg2/experimenting_with_the_new_jev_model_as_a_real/">Jev 自动驾驶决策层</a></b><br><sub>Admirable-Leek5672 · Reddit · ▲ 32 · 2026-09-18</sub><br>驾驶仿真，Jev 读取结构化的环境数据，在行人、信号灯和障碍物周围决定变道、刹车、加速或停车。<br><sub><b>Jev 用法:</b> 每个 tick 根据结构化 state 在驾驶动作中做一个 Choice。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/DaniiarAbdiev/status/2100851116498186415"><img src="https://pbs.twimg.com/amplify_video_thumb/2100849500084666368/img/PdH3lz3bR3uvw0kY.jpg" alt="Jev 机械臂抓取放置" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/DaniiarAbdiev/status/2100851116498186415">Jev 机械臂抓取放置</a></b><br><sub>DaniiarAbdiev · X · ♥ 30 · 2026-09-18</sub><br>配两个 USB 摄像头的 SO-101 机械臂，Jev 以每秒约 2 次决策的速度选择下一步动作，失手后还能把球捡回来放进碗里。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/npceo_/status/2102154533971677481"><img src="https://pbs.twimg.com/amplify_video_thumb/2102153758243495937/img/rYDhh2iFvXpWB9ZA.jpg" alt="Jev 自动驾驶测试" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/npceo_/status/2102154533971677481">Jev 自动驾驶测试</a></b><br><sub>npceo_ · X · ♥ 83 · 2026-09-21</sub><br>让 Jev 在一个用于训练自动驾驶汽车、尚未发布的世界模型中开车的实验，由本地分割模型提供它看到的画面。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://www.youtube.com/watch?v=MZgAj3OZVPo"><img src="https://i.ytimg.com/vi/MZgAj3OZVPo/hqdefault.jpg" alt="Jev 在 JFK 机场做空管" width="240"></a></td>
<td valign="top"><b><a href="https://www.youtube.com/watch?v=MZgAj3OZVPo">Jev 在 JFK 机场做空管</a></b><br><sub>Agent Zero · 视频 · ♥ 71 · 2026-09-19</sub><br>Agent Zero 的演示，模拟 JFK 机场：实时语音模型与飞行员通话，每一条放行许可背后的判断都由 Jev 做出。<br><sub><b>Jev 用法:</b> 在实时控制回路中，为每条放行许可做类型化判断。</sub><br><sub>相关: <a href="https://agent-zero.ai">site</a> · <a href="https://github.com/agent0ai/agent-zero">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/crypto_dev_1/status/2102081831042416935"><img src="https://pbs.twimg.com/amplify_video_thumb/2102080818143244288/img/L59xykXX-_Xpa7Nh.jpg" alt="语音控制的机械臂" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/crypto_dev_1/status/2102081831042416935">语音控制的机械臂</a></b><br><sub>crypto_dev_1 · X · ♥ 52 · 2026-09-21</sub><br>西班牙语演示：机械臂能听懂“张开手”“伸向天花板”“尽量伸远”这类口头指令，由 Jev 把短语映射为机械臂动作。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Dimweaker/jev-libero"><img src="https://raw.githubusercontent.com/Dimweaker/jev-libero/main/docs/media/banner.svg" alt="jev-libero" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Dimweaker/jev-libero">jev-libero</a></b><br><sub>Dimweaker · GitHub · ⭐ 51 · 2026-09-19</sub><br>在 LIBERO 任务上做机器人操作，比如关微波炉或把汤放进篮子，提供 27 种细粒度控制输入、本地物理预演，以及每个决策的交互式回放。<br><sub><b>Jev 用法:</b> Jev 每一步从预演过的控制输入中挑选；每个演示任务需要 14 到 40 次决策。</sub><br><sub>相关: <a href="https://dimweaker.github.io/jev-libero/">app</a> · <a href="https://dimweaker.github.io/jev-libero">app 2</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/lykycy123/RoboJEV"><img src="https://raw.githubusercontent.com/lykycy123/RoboJEV/main/site/media/banner.svg" alt="RoboJEV" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/lykycy123/RoboJEV">RoboJEV</a></b><br><sub>lykycy123 · GitHub · ⭐ 29 · 2026-09-20</sub><br>MuJoCo 实验室，Jev 根据结构化的模拟器 state 控制 Franka Panda 机械臂，先选意图，再选 X/Y/Z 方向和夹爪指令，完成抓取放置、推动和堆叠。<br><sub><b>Jev 用法:</b> 两阶段 Choice（先意图，再运动和夹爪）；由笛卡尔控制器执行，成败由物理检查判定，而不是由模型判定。</sub><br><sub>相关: <a href="https://lykycy123.github.io/RoboJEV/">app</a> · <a href="https://lykycy123.github.io/RoboJEV">app 2</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/cipherwrk/status/2100965547454374316"><img src="https://pbs.twimg.com/amplify_video_thumb/2100965500314615808/img/19kMbu9jghFUkaBs.jpg" alt="Jev 驾驶模拟器" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/cipherwrk/status/2100965547454374316">Jev 驾驶模拟器</a></b><br><sub>cipherwrk · X · ♥ 4 · 2026-09-18</sub><br>自动驾驶仿真，Jev 接收实时环境数据，在突发障碍物、行人、车流和红灯面前决定变道、刹车、加速或减速。<br><sub><b>Jev 用法:</b> 每个 tick 在变道、刹车、加速和减速中做一个 Choice。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/homebrewrobots/status/2102079871388201146"><img src="https://pbs.twimg.com/amplify_video_thumb/2102078211416793089/img/w9GvS61PlfVN-yZc.jpg" alt="人形机器人叠杯纠错" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/homebrewrobots/status/2102079871388201146">人形机器人叠杯纠错</a></b><br><sub>homebrewrobots · X · ♥ 23 · 2026-09-21</sub><br>人形机器人在叠杯子金字塔时，有杯子被挪动后能自行纠正：Jev 从 6 个恢复选项（放下手中的杯子、重新规划、完成）中做出选择，置信度 65%。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/YuanKJing/Jev-as-Policy"><img src="https://raw.githubusercontent.com/YuanKJing/Jev-as-Policy/main/media/jev-carry-block.png" alt="Jev as Policy" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/YuanKJing/Jev-as-Policy">Jev as Policy</a></b><br><sub>YuanKJing · GitHub · ⭐ 22 · 2026-09-21</sub><br>复现 Jev as Policy 控制结构的 MuJoCo 工作室：Jev 把文本 state 转成意图和电机选择，交给本地 IK 执行，让 Franka Panda 把方块搬过障碍。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/JakeTheRabbit/HA-Irrigation-Strategy"><img src="https://raw.githubusercontent.com/JakeTheRabbit/HA-Irrigation-Strategy/main/img/operator-dashboard.png" alt="作物调控灌溉的 Jev 检查" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/JakeTheRabbit/HA-Irrigation-Strategy">作物调控灌溉的 Jev 检查</a></b><br><sub>JakeTheRabbit · GitHub · ⭐ 19 · 2025-04-24</sub><br>Home Assistant 作物调控（crop steering）灌溉控制器，可选的 Jev 检查通过 Cloudflare Workers AI 运行，能否决看似由探头或供水故障引起的自动设定点变更，并以有界的小步调整 P2 灌溉量。<br><sub><b>Jev 用法:</b> 在爬坡进入平台期时以及 P2 阶段每小时咨询一次；灌溉从不等待它，没有答案就不做改动。</sub><br><sub>相关: <a href="https://jaketherabbit.github.io/HA-Irrigation-Strategy/dashboard.html?demo=1">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/eltokh7/status/2100971356691247377"><img src="https://pbs.twimg.com/amplify_video_thumb/2100835422456737792/img/qB9WJb7Mdvq7HVkb.jpg" alt="Jev 操控苍蝇" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/eltokh7/status/2100971356691247377">Jev 操控苍蝇</a></b><br><sub>eltokh7 · X · ♥ 16 · 2026-09-18</sub><br>让 Jev 操控一只模拟苍蝇的实验。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/khordoo/jev-reflex-autonomy-lab"><img src="https://raw.githubusercontent.com/khordoo/jev-reflex-autonomy-lab/main/docs/media/reflex-dashboard.png" alt="Jev Reflex Autonomy Lab" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/khordoo/jev-reflex-autonomy-lab">Jev Reflex Autonomy Lab</a></b><br><sub>khordoo · GitHub · ⭐ 15 · 2026-09-18</sub><br>多无人机仿真，最多十五架无人机由 Jev 作为 System 1 反射层操控，置信度下降时可以向较慢的 OpenRouter 规划器求助。<br><sub><b>Jev 用法:</b> 每个 tick 为每架无人机做 Jev 决策；低于置信度阈值时，System 2 模型发送一次性指导，Jev 仍继续操控。</sub><br><sub>相关: <a href="https://news.ycombinator.com/item?id=49759706">discussion</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/vinilana/live-jev"><img src="https://opengraph.githubassets.com/1/vinilana/live-jev" alt="Jev Self-Driving Sim" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/vinilana/live-jev">Jev Self-Driving Sim</a></b><br><sub>vinilana · GitHub · ⭐ 15 · 2026-09-18</sub><br>浏览器中的俯视 2D 汽车仿真，每约 200 毫秒 把传感器状态发给 Jev，并执行它给出的车道、速度、危险和礼让行人答案，可选与聊天模型对比。<br><sub><b>Jev 用法:</b> 一次调用包含两个 Choice、一个危险程度 Score 和一个行人 Noul；置信度门控的规则会覆盖把握不足的变道决定。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/MKhordoo/status/2100950317852455039"><img src="https://pbs.twimg.com/amplify_video_thumb/2100950290618867712/img/FY-SPST7ifK3ls5W.jpg" alt="Jev 驾驶无人机穿越小行星带" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/MKhordoo/status/2100950317852455039">Jev 驾驶无人机穿越小行星带</a></b><br><sub>MKhordoo · X · ♥ 12 · 2026-09-18</sub><br>由 Jev 驾驶无人机穿越小行星带，每 300 毫秒 做一次左/右/减速/加速决策，只有置信度低时才把控制权交给更大的模型；99% 的时间都是 Jev 独立飞行。<br><sub><b>Jev 用法:</b> 每一步在四个动作中做 Choice，置信度低时升级给更大的模型。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/rodenlab/status/2102154848053432443"><img src="https://pbs.twimg.com/amplify_video_thumb/2102154117082734592/img/McNrTg7kpZShzeiX.jpg" alt="搭载 Jev 的仿生机器人" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/rodenlab/status/2102154848053432443">搭载 Jev 的仿生机器人</a></b><br><sub>rodenlab · X · ♥ 11 · 2026-09-21</sub><br>运行在模拟神经系统上的仿生机器人，神经活动被输入 Jev，它的快速决策再被转化为身体动作。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/kavehmz/typesafe-playground"><img src="https://raw.githubusercontent.com/kavehmz/typesafe-playground/main/docs/images/demo03-fable.png" alt="typesafe-playground" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/kavehmz/typesafe-playground">typesafe-playground</a></b><br><sub>kavehmz · GitHub · ⭐ 11 · 2026-09-17</sub><br>一组交互式 Jev 实验：一个 3D 驾驶实验室，Jev 根据摄像头、雷达和限速牌读数选择车道和目标车速；另有一个客服消息路由预览。<br><sub><b>Jev 用法:</b> 驾驶部分基于结构化传感器数据，用 Choice 选车道和目标车速；客服演示把一条消息拆成六个独立判断，再由代码组合。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/TarunTomar122/jev-askable-arm"><img src="https://opengraph.githubassets.com/1/TarunTomar122/jev-askable-arm" alt="能直接下指令的机械臂" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/TarunTomar122/jev-askable-arm">能直接下指令的机械臂</a></b><br><sub>TarunTomar122 · GitHub · ⭐ 10 · 2026-09-17</sub><br>在 ManiSkill 的模拟 Franka 机械臂上零样本执行纯英文目标，Jev 一次抓取一个地串联硬编码的基本动作，每次抓取约 1 秒，无需训练或演示。<br><sub><b>Jev 用法:</b> 每一步根据特权物体和夹爪 state，在约三十个技能和目标中做一个 Choice。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/metrox-eth/moss"><img src="https://raw.githubusercontent.com/metrox-eth/moss/main/media/images/moss_exploded_turntable.gif" alt="MOSS" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/metrox-eth/moss">MOSS</a></b><br><sub>metrox-eth · GitHub · ⭐ 10 · 2026-09-17</sub><br>开放、基本靠 3D 打印的捡垃圾小车，附带浏览器演示，在 MuJoCo 录制的物理过程中由 Jev 选择捡拾的每一步（接近、对准、抓取、抬起、搬运、松开）。<br><sub>相关: <a href="https://www.showrobotics.ai/moss-jev/">demo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/tarat_211/status/2100625153109504483"><img src="https://pbs.twimg.com/amplify_video_thumb/2100624434348294144/img/hJfPYVbpLtVQALI4.jpg" alt="零样本机械臂任务" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/tarat_211/status/2100625153109504483">零样本机械臂任务</a></b><br><sub>tarat_211 · X · ♥ 9 · 2026-09-17</sub><br>机械臂演示：用简单英语给出目标，Jev 把一组硬编码的运动原语串起来完成任务，无需训练。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/arielweinberger/jev-autopilot"><img src="https://raw.githubusercontent.com/arielweinberger/jev-autopilot/main/docs/demo.png" alt="Drone Sim · Jev Autopilot" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/arielweinberger/jev-autopilot">Drone Sim · Jev Autopilot</a></b><br><sub>arielweinberger · GitHub · ⭐ 8 · 2026-09-17</sub><br>Three.js 无人机模拟器，Jev 通过 AI SDK 的 @ai-sdk/typesafe-ai provider 驾驶无人机从停机坪 A 出发，穿过随机生成的城市飞到停机坪 B，同时避开障碍物；一趟花费 $0.01。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/shuvam360/status/2101186415891734728"><img src="https://pbs.twimg.com/amplify_video_thumb/2101183715577847808/img/cZLEIxTpQV1HOWa4.jpg" alt="Jev 机械爪" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/shuvam360/status/2101186415891734728">Jev 机械爪</a></b><br><sub>shuvam360 · X · ♥ 8 · 2026-09-19</sub><br>一个较早的机械爪实验，把 Claude 换成了 Jev：每当板上的物体被移动，模型都会重新推算到达目标的路线。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/Jadfyd/status/2101302137884234221"><img src="https://pbs.twimg.com/amplify_video_thumb/2101301804227325952/img/QjhHxPjGf3gQlVzy.jpg" alt="System 1 + System 2 机器人循环" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/Jadfyd/status/2101302137884234221">System 1 + System 2 机器人循环</a></b><br><sub>Jadfyd · X · ♥ 7 · 2026-09-19</sub><br>基于 PyBullet 的叠方块机器人：Claude 写高层计划，Jev 充当反射层，在不到 100 毫秒 内评估仿真状态并随之调整。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/autonomous-ai/autonomous-os/tree/main/system/buddy/jev"><img src="https://raw.githubusercontent.com/autonomous-ai/autonomous-os/main/robots/intern-v2/images/intern-hero.webp" alt="Autonomous OS 的 Jev 支持" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/autonomous-ai/autonomous-os/tree/main/system/buddy/jev">Autonomous OS 的 Jev 支持</a></b><br><sub>autonomous-ai · GitHub · ⭐ 356 仓库 · 2026-06-04</sub><br>开源机器人操作系统，新增可选的 Jev 决策，用于在候选中解析语音意图、建议 Buddy UI 操作以及路由 Hermes skill。<br><sub><b>Jev 用法:</b> 在候选意图或动作上做 Choice，默认超时 350 毫秒，出错后有冷却期。</sub><br><sub>相关: <a href="https://www.autonomous.ai/lamp">app</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/queso_gato1354/status/2101305412876423459"><img src="https://pbs.twimg.com/amplify_video_thumb/2101305211013001216/img/Dx4RNM5XUJsuyzKq.jpg" alt="行车记录仪驾驶稳定性检测" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/queso_gato1354/status/2101305412876423459">行车记录仪驾驶稳定性检测</a></b><br><sub>queso_gato1354 · X · ♥ 7 · 2026-09-19</sub><br>韩语项目：用 Jev 根据汽车行车记录仪画面判断驾驶稳定性，凭借低延迟近乎实时地分析路况。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/lbotinelly/jev-little-airways"><img src="https://opengraph.githubassets.com/1/lbotinelly/jev-little-airways" alt="Little Airways" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/lbotinelly/jev-little-airways">Little Airways</a></b><br><sub>lbotinelly · GitHub · ⭐ 5 · 2026-09-17</sub><br>玩具级群岛飞行模拟器，每架飞机只能看到自己和附近的交通，Jev 实时决定是否改航、宣布紧急状态、避让、盘旋等待或优先降落，耗时约 150 毫秒。<br><sub>相关: <a href="https://github.com/user-attachments/assets/3edd2a58-b86f-4e79-9756-282cd60ce3c3">video</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/RobotKitAI/piper-astra-jev"><img src="https://opengraph.githubassets.com/1/RobotKitAI/piper-astra-jev" alt="piper-astra-jev" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/RobotKitAI/piper-astra-jev">piper-astra-jev</a></b><br><sub>RobotKitAI · GitHub · ⭐ 5 · 2026-09-19</sub><br>在真实 AgileX PiPER 机械臂上的八次演示运行，对比直接看摄像头画面的 GPT-6 Astra 与基于 Grounding DINO 或 SAM 3 感知做决策的 Jev，任务难度一直到把管件套到立着的盒子上。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/rokbenko/quackd/blob/main/quackd/agent/jev.py"><img src="https://opengraph.githubassets.com/1/rokbenko/quackd" alt="quackd 的 Jev 步进器" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/rokbenko/quackd/blob/main/quackd/agent/jev.py">quackd 的 Jev 步进器</a></b><br><sub>rokbenko · GitHub · ⭐ 225 仓库 · 2026-09-18</sub><br>用 LLM 大脑编排业余机器人和 ROS 机器人的 CLI quackd 中可选的 Jev 步进器：在允许的离散调用中做选择，让这类步骤更便宜，位姿仍由 LLM 编写，安全关卡照常生效。<br><sub>相关: <a href="https://github.com/rokbenko/quackd">repo</a> · <a href="https://www.quackd.org">site</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/hotragn/status/2101251578610974952"><img src="https://pbs.twimg.com/amplify_video_thumb/2101248543117701120/img/n1AWqrdoj_OtGSqW.jpg" alt="Jev 驾驶交接" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/hotragn/status/2101251578610974952">Jev 驾驶交接</a></b><br><sub>hotragn · X · ♥ 3 · 2026-09-19</sub><br>驾驶模拟器片段：Jev 在前进和后退之间犹豫不决，于是由人接管方向盘，展示了“能决定时自己决定，不能时交给人”的设计。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/FazalAAli/jev-robotics-demo"><img src="https://opengraph.githubassets.com/1/FazalAAli/jev-robotics-demo" alt="jev-robotics-demo" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/FazalAAli/jev-robotics-demo">jev-robotics-demo</a></b><br><sub>FazalAAli · GitHub · ⭐ 3 · 2026-09-19</sub><br>MuJoCo 演示：带 Allegro 灵巧手的模拟 Franka 机械臂把蓝色方块叠到红色方块上，一次由使用底层工具的 Claude Opus 5 驱动，一次由 Jev 驱动。<br><sub><b>Jev 用法:</b> 代码提出小幅动作并逐个预先模拟；Jev 负责选动作、决定何时抓取和松开，以及判断任务何时完成。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/shapsider/OmniJev"><img src="https://raw.githubusercontent.com/shapsider/OmniJev/main/docs/media/omnijev-transfer.gif" alt="OmniJev" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/shapsider/OmniJev">OmniJev</a></b><br><sub>shapsider · GitHub · ⭐ 3 · 2026-09-21</sub><br>研究项目，把摄像头图像引入面向机器人的 Jev 风格有限选项决策，提供 HTTP 服务、SDK 和 MuJoCo 机械臂工作台。<br><sub><b>Jev 用法:</b> 在 Nemotron 3 Nano Omni 上使用类 Jev 接口；skill 模式下由模型挑选预设技能，遇到空白或无法观测的输入时会回答证据不足。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/Devonance/rover-claude-jev-demo"><img src="https://raw.githubusercontent.com/Devonance/rover-claude-jev-demo/main/docs/figs/coverage-map.jpg" alt="Jezero Ops" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/Devonance/rover-claude-jev-demo">Jezero Ops</a></b><br><sub>Devonance · GitHub · ⭐ 2 · 2026-09-20</sub><br>模拟毅力号火星车在真实 USGS 耶泽罗陨石坑地形上行驶，Jev 作为 System One 快速做出危险判断和目标选择，Claude 作为 System Two 规划科学任务，每个决策都在屏幕上标注。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/grmkris/robo-harness"><img src="https://raw.githubusercontent.com/grmkris/robo-harness/main/docs/workbench-real.png" alt="Robo Harness" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/grmkris/robo-harness">Robo Harness</a></b><br><sub>grmkris · GitHub · ⭐ 2 · 2026-09-07</sub><br>SO-101 机械臂 agent 工作台，包含 Bun/Effect 协调器、React 与 Rerun 工作区以及掌管电机的 Python LeRobot 进程，Jev 根据摄像头和传感器 state 选择受限的下一步机械臂动作。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/fuzzzypan/status/2102056646281437577"><img src="https://pbs.twimg.com/amplify_video_thumb/2102053874660241408/img/PmXXJNePrSow-TEb.jpg" alt="Jev 城市驾驶游戏" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/fuzzzypan/status/2102056646281437577">Jev 城市驾驶游戏</a></b><br><sub>fuzzzypan · X · ♥ 1 · 2026-09-21</sub><br>带交通流的驾驶游戏，Jev 针对行人、横穿车辆、弯道和坑洼做出停车、让行、减速和通行的决定，转向交给本地代码；一次城市驾驶花费 $0.0208。<br><sub><b>Jev 用法:</b> 每个 tick 在停车/让行/减速/通行中做 Choice；转向和碰撞检测留在代码里。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/robokrunch/jev-physical-ai"><img src="https://raw.githubusercontent.com/robokrunch/jev-physical-ai/main/assets/fleet-triage-demo-poster.png" alt="Jev for Physical AI" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/robokrunch/jev-physical-ai">Jev for Physical AI</a></b><br><sub>robokrunch · GitHub · ⭐ 1 · 2026-09-19</sub><br>可复现的仓储车队事故分诊演示，对模拟事故调用 300 次 Jev，并与在边缘 CPU 上自托管 ModernBERT 做成本对比，附原始结果和注意事项说明。<br><sub>相关: <a href="https://news.ycombinator.com/item?id=49776827">demo</a> · <a href="https://robokrunch.com">site</a> · <a href="https://x.com/SimeonLi82/status/2101694996563026404">demo 2</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/DanielMizr43248/status/2100714507303829829"><img src="https://pbs.twimg.com/amplify_video_thumb/2100714471065034752/img/Ef8YwVTFprkIeArZ.jpg" alt="Jev 控制机器人身体" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/DanielMizr43248/status/2100714507303829829">Jev 控制机器人身体</a></b><br><sub>DanielMizr43248 · X · ♥ 1 · 2026-09-17</sub><br>让 Jev 控制一具机器人身体的实验，效果时好时坏。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/skcache/jevtrafficsim"><img src="https://opengraph.githubassets.com/1/skcache/jevtrafficsim" alt="Jev Traffic Sim" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/skcache/jevtrafficsim">Jev Traffic Sim</a></b><br><sub>skcache · GitHub · ⭐ 1 · 2026-09-18</sub><br>交互式芝加哥交通模拟器，同一段行程分别在固定轮换信号、本地自适应信号和通过 Vercel AI Gateway 运行的全城 Jev 信号策略下运行，方便对比结果。<br><sub>相关: <a href="https://jevtrafficsim.vercel.app">app</a> · <a href="https://jevtrafficsim.vercel.app">app 2</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/andrewsilber/JevsBistro"><img src="https://raw.githubusercontent.com/andrewsilber/JevsBistro/main/docs/screenshots/dining-room.png" alt="JevsBistro" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/andrewsilber/JevsBistro">JevsBistro</a></b><br><sub>andrewsilber · GitHub · ⭐ 1 · 2026-09-20</sub><br>确定性的 3D 餐厅模拟器，重放同一场晚餐服务，对比基于规则、摄像头辅助和由 Jev 规划的服务员，并记录每个决策的选项、置信度和延迟。</td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/using76/TypeEvacSafe"><img src="https://raw.githubusercontent.com/using76/TypeEvacSafe/main/results/hall/bonsai_vs_jev.gif" alt="TypeEvacSafe" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/using76/TypeEvacSafe">TypeEvacSafe</a></b><br><sub>using76 · GitHub · ⭐ 1 · 2026-09-18</sub><br>火灾疏散模拟器：100 名疏散者在模拟火场中分别就角色、救援和路线做类型化决策，对比本地 Bonsai 2 27B 引擎与 Jev。<br><sub><b>Jev 用法:</b> 在本地 LLM 上重建了一个 Jev 风格的类型化决策引擎，与 TypeSafe Jev API 并排运行；行走由社会力模型处理。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://x.com/nishitkhalpada/status/2101755092177473858"><img src="https://pbs.twimg.com/amplify_video_thumb/2101755011676184576/img/Y5z-bgXbBRV0T49b.jpg" alt="自适应交通信号灯仿真" width="240"></a></td>
<td valign="top"><b><a href="https://x.com/nishitkhalpada/status/2101755092177473858">自适应交通信号灯仿真</a></b><br><sub>nishitkhalpada · X · ▶ 64 · 2026-09-20</sub><br>交通仿真，把固定 8 秒的信号周期与由 Jev 根据排队长度、等待时间和来车情况决定保持还是切换绿灯做对比；车流均衡时固定配时更好，车流不均时 Jev 更好。<br><sub><b>Jev 用法:</b> 每个信号步根据排队和等待时间 state 做一次保持或切换的 Choice。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/NellInc/MillOS/blob/main/src/utils/jevClient.ts"><img src="https://raw.githubusercontent.com/NellInc/MillOS/main/src/0.10%20Archive/assets/Screenshot.png" alt="MillOS 的 Jev 事件路由" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/NellInc/MillOS/blob/main/src/utils/jevClient.ts">MillOS 的 Jev 事件路由</a></b><br><sub>NellInc · GitHub · ⭐ 8 仓库 · 2025-12-03</sub><br>基于浏览器的 3D 谷物磨坊数字孪生，带模拟 SCADA，其 AI 搭档可按需询问 Jev 某个事件应归入哪个运维队列，比如设备维护。<br><sub><b>Jev 用法:</b> 通过 OpenRouter Decisions API（typesafe/jev-1.13）在固定的事件队列上做一个 Choice；建议是只读的，缓存 60 s。</sub><br><sub>相关: <a href="http://www.millos.net/">app</a> · <a href="https://github.com/NellInc/MillOS">repo</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"></td>
<td valign="top"><b><a href="https://jev-demo.vercel.app">Companion</a></b><br><sub>jev-demo · 应用</sub><br>3D 场景中的机器人伙伴，能对你说的话做出反应却不生成一个字，每一轮决定是行动、追问还是耸耸肩。<br><sub><b>Jev 用法:</b> 每轮一次调用，包含九个类型化问题；由代码依据置信度决定行动、追问还是只做反应。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/kxzk/typesafe-jev-drone-demo"><img src="https://opengraph.githubassets.com/1/kxzk/typesafe-jev-drone-demo" alt="Jev Flight Lab" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/kxzk/typesafe-jev-drone-demo">Jev Flight Lab</a></b><br><sub>kxzk · GitHub · 2026-09-17</sub><br>Three.js 无人机模拟，后端为 Python/FastAPI，Jev 为穿越四个检查点的每个导航动作做选择，飞行画面旁显示其概率、延迟和原始输入。<br><sub><b>Jev 用法:</b> 对导航动作做一个 Choice，外加一个判断是否有遮挡的 Noul；加入障碍会迫使它重新决策。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/tryaksh/jev-pick-and-place-study"><img src="https://opengraph.githubassets.com/1/tryaksh/jev-pick-and-place-study" alt="Jev 抓取放置研究" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/tryaksh/jev-pick-and-place-study">Jev 抓取放置研究</a></b><br><sub>tryaksh · GitHub · 2026-09-17</sub><br>可复现的 MuJoCo 试点研究，对比 Jev 1.13.0、Claude Haiku 4.5 和反应式规则作为抓取放置控制器的表现；Jev 在两种设置下都 10/10 成功，每次决策中位耗时 146 毫秒，与规则结果完全一致。</td>
</tr>
<tr>
<td width="260" valign="top"></td>
<td valign="top"><b><a href="https://01a0b7a9-5619-7ec6-a0d8-fb357ed42aa3.skydive.app/">JEVCITY</a></b><br><sub>JEVCITY · 应用</sub><br>九个路口的城市网格交通仿真，Jev 大约每 300 毫秒 控制一次所有信号灯；把它关掉，就能看到固定配时让整个路网堵死。<br><sub><b>Jev 用法:</b> 根据程序提供的路口 state，对每个信号灯的相位做决策，并给出置信度和理由。</sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/metrox-eth/moss-jev"><img src="https://opengraph.githubassets.com/1/metrox-eth/moss-jev" alt="MOSS × Jev" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/metrox-eth/moss-jev">MOSS × Jev</a></b><br><sub>metrox-eth · GitHub · 2026-09-18</sub><br>MOSS 捡垃圾小车的浏览器 3D 回放，展示 Jev 在 MuJoCo 运行中选择的每个操作步骤，比如捡起易拉罐或在抓空后重试。<br><sub>相关: <a href="https://metrox-eth.github.io/moss-jev/">app</a> · <a href="https://github.com/metrox-eth/moss">project</a></sub></td>
</tr>
<tr>
<td width="260" valign="top"><a href="https://github.com/juancamiloqhz/roverlab"><img src="https://opengraph.githubassets.com/1/juancamiloqhz/roverlab" alt="RoverLab" width="240"></a></td>
<td valign="top"><b><a href="https://github.com/juancamiloqhz/roverlab">RoverLab</a></b><br><sub>juancamiloqhz · GitHub · 2026-09-17</sub><br>浏览器里的 3D 行星漫游车沙盒：设定任务和环境后，对比本地基线与 TypeSafe 控制器（按 Choice 概率选动作）的表现，同时追踪能耗和发现。</td>
</tr>
</table>

还缺什么？[提交一个资源](https://github.com/Li-Evan/awesome-jev/issues/new/choose)。
