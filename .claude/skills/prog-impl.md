# Skill: 实现游戏功能 (prog-impl)

## 触发场景
需要新增或修改 Ren'Py 游戏功能（新系统、新UI、新机制）。

## 执行流程

1. **读取上下文**
   - 读取 `CLAUDE.md` 确认架构
   - 读取 `game/script/core/datastore.rpy` 确认现有变量
   - 读取 `game/script/core/api.rpy` 确认现有函数
   - 若涉及UI，读取 `game/script/screens/map_screen.rpy` 和相关 screen 文件

2. **输出方案**
   - 用 2-3 句话描述实现方案
   - 列出涉及的文件和需要新增/修改的变量
   - 等待用户确认

3. **实现代码**
   - 用户确认后，按以下顺序修改：
     1. `datastore.rpy` — 新增变量
     2. `api.rpy` — 新增修改函数
     3. `gameflow.rpy` — 集成到主循环（如需要）
     4. screen 文件 — UI 变更
   - 每处修改标注文件路径和行号

4. **自检**
   - 变量名是否与 datastore.rpy 一致
   - 函数签名是否正确
   - Ren'Py 语法是否正确

## 输出格式
```
## 方案
[2-3句描述]

## 涉及文件
- game/script/core/datastore.rpy: 新增变量 xxx
- game/script/core/api.rpy: 新增函数 yyy()
- ...

## 代码
[逐文件输出，标注位置]
```
