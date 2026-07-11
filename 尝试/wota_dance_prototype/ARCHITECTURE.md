# WOTA艺 Dance Prototype — 架构总结

## 文件结构

```
wota_dance_prototype/
  main.py        # 渲染 + 粒子 + HUD + 主循环（Pygame）
  wota_fsm.py    # 舞蹈状态机 + 手臂物理 + 输入管理
```

## 整体数据流

```
键盘输入 → InputManager 解析 → DanceFSM.input_act() 改变状态
                                    ↓
                            ArmState.update(dt) 物理更新
                                    ↓
                            Renderer.draw() 渲染手臂+拖尾+粒子
                            HUD.draw() 渲染状态文字
```

---

## wota_fsm.py — 状态机核心

### 枚举

| 类型 | 值 | 含义 |
|---|---|---|
| `Dir` | N/U/D/L/R/UL/UR/DL/DR | 9 个方向（摇杆） |
| `Act` | LEFT/RIGHT/SMALL/LARGE/TOGGLE_ROT/TOGGLE_SHAPE | 6 种动作 |

### 常量表

**DIR_ANCHOR** — 每个方向对应的大臂「锚点角度」(rad)。画圈/挥击时以此为基准。

```
0°=右, 90°=下, -90°=上, ±180°=左
N:80°  U:-80°  D:120°  L:160°  R:20°
UL:-120°  UR:-50°  DL:150°  DR:60°
```

**DIR_ACT_INFO** — `(方向, 动作) → (招式名, RGB颜色)` 的招式映射表。

**速度常量：**

| 常量 | 值 | 含义 |
|---|---|---|
| `LARGE_SPEED` | `2π × 1.2` rad/s | 大圈：大臂绕肩匀速公转 |
| `SMALL_SPEED` | `2π × 2.5` rad/s | 小圈：小臂绕肘匀速自转 |
| `STRIKE_DURATION` | `0.07` s | 挥击：固定 70ms 快照急停 |

### ArmState — 单臂物理状态

```
upper_angle   : float  # 大臂绝对角度 (rad)
upper_omega   : float  # 大臂角速度（大圈公转，0=静止）
forearm_angle : float  # 小臂相对大臂的角度（0=伸直）
forearm_omega : float  # 小臂角速度（小圈自转，0=静止）

strike_target      : float|None  # 挥击目标锚点，None=不在挥击
strike_t            : float      # 挥击已用时间 (s)
strike_start_angle  : float      # 挥击起始角度

idle_angle  : float  # 初始锚点（reset 时恢复）
```

**update(dt) 逻辑：**

1. 如果 `strike_target is not None`（正在挥击）：
   - `strike_t` 累加 dt
   - 计算进度 `t = min(strike_t / 0.07, 1.0)`
   - 缓出曲线 `eased = 1 - (1-t)³`（开头极快，末尾骤停）
   - `upper_angle = strike_start_angle + diff × eased`
   - t≥1.0 时精确停在目标，置 `strike_target = None`
2. 否则：`upper_angle += upper_omega × dt`（大圈驱动）
3. 始终：`forearm_angle += forearm_omega × dt`（小圈驱动）

### DanceFSM — 舞蹈状态机

**全局状态：**

```
left, right : ArmState   # 双臂（左手 idle=100°, 右手 idle=80°）
direction   : Dir        # 当前摇杆方向
omega_sign  : +1顺/-1逆  # 旋向，翻转所有角速度符号
shape_sign  : +1凹(同向)/-1凸(反向)  # 形态，凸=右臂用反方向锚点
```

**6 种动作的响应：**

| 按键 | 动作 | 效果 |
|---|---|---|
| 1 | LEFT | 左手清零所有圈 → 快照急停到锚点 |
| 2 | RIGHT | 右手清零所有圈 → 快照急停到锚点 |
| 3 | SMALL | 小圈开关：两端臂锚点对齐，toggle `forearm_omega`，取消挥击 |
| 4 | LARGE | 大圈开关：两端臂锚点对齐，toggle `upper_omega`，取消挥击 |
| 5 | TOGGLE_ROT | `omega_sign *= -1`，翻转所有 `upper_omega`/`forearm_omega` |
| 6 | TOGGLE_SHAPE | `shape_sign *= -1`，翻转右臂锚点+角速度（同向↔反向） |

**凹凸形态逻辑 (SMALL/LARGE 共用)：**
- 凹(shape_sign=+1)：双手同锚点、同旋向 → 对称运动
- 凸(shape_sign=-1)：右手用反方向锚点 + 反旋向 → 双手反向运动

**连击系统：**
- 每次 act 触发 `_combo()`：`combo_count++`，重置 `combo_timer = 90帧`
- update 中 `combo_timer` 倒计时，归零时结算 max_combo
- 90帧（约1.5秒）内无操作则连击中断

### InputManager — 输入解析

- `resolve_direction(keys)` — 读取 WASD/方向键 → 返回 Dir
- `ACT_MAP` — 键盘映射：主键盘 1-6 + 小键盘 KP1-KP6
- `get_actions(events)` — 从事件队列提取本帧的 Act 列表

---

## main.py — 渲染与主循环

### 主循环流程

```
60fps 循环:
  1. clock.tick(60) → dt（上限 0.05s 防跳帧）
  2. 处理 pygame 事件（QUIT/ESC 退出，键盘→fsm.input_act）
  3. 持续读取方向键 → fsm.input_dir()
  4. SPACE → fsm.reset()
  5. fsm.update(dt) + particles.update()
  6. 清屏 → 画地面线 → 画粒子 → 画角色 → 画 HUD → flip
```

### Renderer — 角色渲染

**身体结构（均为 scale=2.5 下的像素值）：**

```
        头 (circle, r=hr, y=-32*s)
         |
  肩左 --躯干-- 肩右  (ss=肩半宽, th=躯干长)
         |       |
       大腿    大腿
```

**手臂为两段 IK：**
```
肩(s)──大臂(ul=35*s, angle=upper_angle)──肘(e)──小臂(fl=40*s, angle=upper_angle+forearm_angle)──手(h)
```

**拖尾：** `deque(maxlen=16)` 存储最近 16 帧的手部位置，画渐隐线条。
**粒子：** 手臂活跃时在手部发射 2 个粒子（life=10 帧），颜色与招式对应。

活跃判定（决定是否画拖尾/粒子/发光）：
```python
active = upper_omega or forearm_omega or strike_target is not None
```

### HUD 布局

```
左上角:   锚点方向（大字）  +  旋向/形态（小字）
左中:     左手状态（大圈 rpm / 小圈 rpm / 挥击中!）
          右手状态
右上角:   N HIT（连击数）+ MAX 记录
中央上方: 招式名称（持续 90 帧淡出）
底部栏:   操作提示
```

### Particles

- 粒子结构：`{x, y, vx, vy, life, mx(最大生命), c(RGB), size}`
- 每帧 `life--`，透明度 = `life/mx`，`life≤0` 时移除
- emit 参数：位置、颜色、数量(默认6)、扩散半径(默认2)、生命帧数(默认12)

---

## 关键设计决策

1. **角速度驱动而非位置驱动** — 大小圈用持续角速度，手臂自然旋转，不需要关键帧或动画曲线
2. **挥击用缓出快照而非等速** — 70ms 固定时长 + 三次方缓出，视觉上看像"啪"一下急停，不会像圆弧滑行
3. **状态可叠加** — 大圈 + 小圈可同时开启（卫星轨道效果），挥击中禁止大小圈
4. **最短路径** — 角度插值总是走 `[-π, π]` 最短弧，不会绕远路
5. **凹凸形态通过翻转锚点和符号实现** — 不需要额外的手部动画数据，纯数学变换
