# 游戏代码结构分析 — 快进功能问题

## 用户症状

所有 wN.rpy 周文件在播放时无法快进（skip），不只是旁白行。

## 完整代码流追踪

```
script.rpy (无，只有 .rpyc)
  └─ story/story.rpy label start     ← 开场 (宋柯退社)
       └─ label game_start            ← 到北航，见学长
            └─ jump week_loop
                 │
                 ▼ core/gameflow.rpy
            label week_loop:
              scene map
              p"我打算做什么呢？"       ← p = Character(" ") 旁白
              call screen map_screen   ← 阻塞等待地图选择
              call weekly_story_check  ← 动态 call w1/w2/.../w10
              call random_event_check
              call special_event_check
              p"主角入校故事序章"
              jump week_loop
```

### 地图屏幕调用链
```
call screen map_screen
  → screen map_screen() 显示
    → 玩家点击按钮 → Call("loc_practice")
      → location/practice.rpy:
          scene black
          "你练习了一整天。"        ← 注意：这里用裸字符串，不是 p""
          $ add_skill(3)
          $ add_fame(2)
          $ skill_name, add_mastery = practice_skill()
          "练习了[skill_name],熟练度提高[add_mastery]"
          $ next_week()            ← week += 1
          return
        → 返回 map_screen (重新显示)
    → ⚠ map_screen 没有 Return() 按钮，永远不退！
```

### 周故事调度
```
weekly_story_check (story/story.rpy:58):
    $ target_label = "w" + str(week)
    call expression target_label    ← 动态调用 w0/w1/.../w10
    return
```

## 快进 (Skip) 机制全链路分析

### 1. Ren'Py 快进工作原理

快进是通过 Tab 键或 Ctrl 触发的游戏模式。实现机制：

- **`_preferences.skip`**: 控制跳过模式
  - `"seen"` (默认): 只跳过已读文本
  - `"all"`: 跳过所有文本（含未读）
- **`config.allow_skipping`**: 全局开关，默认 True
- **`config.skip_delay`**: 跳过速度控制
- **`_dismiss_pause`**: 点击继续前的延迟，默认 False
- **`config.say_allow_dismiss`**: 是否允许点击继续，默认 True

### 2. 当前项目快进配置检查

| 配置项 | 状态 | 文件位置 |
|--------|------|----------|
| `config.allow_skipping` | 未显式设置 → 默认 True | — |
| `config.say_allow_dismiss` | 未显式设置 → 默认 True | — |
| `preferences.text_cps` | **0 (瞬间显示)** | `options.rpy:115` |
| `preferences.afm_time` | 15 | `options.rpy:120` |
| 快进按钮 | ✓ 存在 | `screens.rpy:739` |
| skip_indicator 屏幕 | ✓ 存在 | `screens.rpy:1192` |
| 跳过转场按钮 | ✓ 存在 | `screens.rpy:741` |
| `modal True` 阻塞 | ✗ 不在对话流程中 | `screens.rpy:1133` (仅 confirm 弹窗) |
| `renpy.pause()` | ✗ 全项目无 | — |
| `block_rollback()` | ✗ 全项目无 | — |

### 3. Say 屏幕 dismiss/click 链路

```renpy
# screens.rpy:95
screen say(who, what):
    window:
        id "window"              ← 点击此区域触发 dismiss
        if who is not None:      ← p 的 who=" " → True
            window:
                id "namebox"
                style "namebox"
                text who id "who" ← 渲染空格
        text what id "what"      ← 对话正文
```

### 4. 关键发现：代码中存在两种旁白模式混用

| 模式 | 位置 | 示例 |
|------|------|------|
| `p"..."` (自定义 Character) | story.rpy, gameflow.rpy, w0~w10.rpy | `p"我猛地坐起来。"` |
| `"..."` (裸字符串 = 内置 narrator) | practice.rpy, story.rpy(L83) | `"你练习了一整天。"` |

这种混乱是**同一项目中使用两种旁白派发方式**。

## 快进失效的可能根因

### 可能性排序（高→低）

**1. `text_cps = 0` 与 Skip 的交互问题**

当 `text_cps = 0`（文字瞬间显示），Ren'Py 的 skip 计时器可能无法正确计算跳过间隔。skip 本质是"短暂显示→自动 dismiss"的循环。CPS=0 时，"短暂显示"几乎为零，如果 Ren'Py 在极短时间内尝试跳过大量文本，某些版本的引擎可能出现时序问题。

**2. `call expression` 动态标签 + skip 状态**

Ren'Py 的 skip 功能依赖文本"已读/未读"追踪。动态 `call expression` 调用的标签，其内部 say 语句的标识符基于 `<label>.<line_number>`。如果 Ren'Py 的 seen-text 持久化在动态调用场景下有边界情况，可能导致 skip 认为所有文本都是"未读"而拒绝快进。

验证方法：将 skip 模式切换为"all"（跳过所有文本），看是否恢复正常。

**3. `Character(" ")` 与 `narrator` 的 dismiss 行为差异**

虽然理论上两者都应支持 dismiss，但 Ren'Py narrator 有特殊的 ctc（点击继续指示器）和 ctc_position 默认值，`Character(" ")` 不会继承这些。当 `text_cps=0` 且缺少 CTC 指示器时，玩家可能无法判断当前是否停顿等待点击。

**4. map_screen 循环 bug（间接因素）**

`map_screen` 没有 `Return()` 按钮，只有 `Call("loc_practice")` 按钮。如果玩家先经历了 W0/W1（在 label start/game_start 中硬编码），然后进入 week_loop 的地图屏幕，实际周故事 (`weekly_story_check`) **可能从未真正执行过**，因为 map_screen 永远不会返回。

## 修复记录 (2026-07-15)

### 修复 1: `text_cps = 0` → `50`
**文件**: `options.rpy:115`
**原因**: CPS=0 文字瞬间显示，skip 计时器无法正确计算 dismiss 间隔。改为 50 后文字仍极快（每秒 50 字符）但给了 skip 机制正常运转的余地。

### 修复 2: `p = Character(" ")` → `Character(None)`
**文件**: `story/story.rpy:8`
**原因**: `Character(" ")` 的 who 是空格（truthy），say screen 的条件 `if who is not None` 判定为真，渲染一个空 namebox。这个空 namebox 占据点击区域，干扰 dismiss/skip 的点击目标判断。改为 `Character(None)` 后 `p"..."` 等价于内置 narrator。

### 修复 3: map_screen 添加 Return() 按钮
**文件**: `screens/map_screen.rpy:29-32`
**原因**: `gameflow.rpy` 用 `call screen map_screen` 阻塞等待屏幕返回，但 map_screen 只有 `Call("loc_practice")` 按钮（执行完 return 回 screen），没有 `Return()` 按钮。导致 `call screen` 永远不返回，`weekly_story_check` 永远执行不到。添加"继续"按钮触发 `Return()`，使主循环能推进到周故事检查。

### 修复 4: 统一旁白模式
**文件**: `location/practice.rpy`, `story/story.rpy`
**原因**: 项目中混用裸字符串 `"..."` 和 `p"..."`。裸字符串走内置 narrator，`p"..."` 走自定义 Character。修复 2 之后二者等价，统一改为 `p"..."` 消除隐式 narrator 引用。

## 代码文件职责速查

| 文件 | 职责 |
|------|------|
| `story/story.rpy` | 角色定义(label start/game_start/weekly/special/random) |
| `story/w0~w10.rpy` | 各周固定剧情对话 |
| `core/gameflow.rpy` | 主循环 week_loop |
| `core/datastore.rpy` | 全局变量 default 声明 |
| `core/api.rpy` | 变量修改函数 (init python) |
| `location/practice.rpy` | 地点行为 (练习) |
| `screens/map_screen.rpy` | 地图选择界面 |
| `screens.rpy` | 系统 UI (say/菜单/设置/快进指示器) |
| `options.rpy` | 游戏设置 (text_cps/转场/构建) |
| `gui.rpy` | GUI 样式 (字体/颜色/布局) |
| `testcases.rpy` | 自动化测试用例 (bad_end/good_end/...) |
