# Skill: 调试Bug (prog-debug)

## 触发场景
用户报告 Ren'Py 游戏运行异常（报错、逻辑不符合预期、UI显示异常）。

## 执行流程

1. **获取报错信息**
   - 让用户提供完整的 error traceback
   - 确认报错时的游戏状态（当前周数、触发什么剧情、哪个操作）

2. **定位问题**
   - 根据 traceback 找到出错文件和行号
   - 读取相关源文件
   - 向上追溯变量赋值路径（在 api.rpy 和 datastore.rpy 中 grep 相关变量名）

3. **诊断**
   - 用一句话描述根因
   - 区分：语法错误 / 变量未定义 / 逻辑错误 / Ren'Py 引擎问题
   - 若需要更多信息，追问用户

4. **修复**
   - 输出修复方案
   - 标注修改位置和变更内容
   - 若涉及多个文件，按依赖顺序输出

## 常见问题速查

| 症状 | 常见原因 |
|------|----------|
| `NameError: name 'xxx' is not defined` | 变量未在 datastore.rpy 中用 `default` 声明 |
| `AttributeError` | Ren'Py 对象方法调用错误 |
| Screen 不显示 | screen 名称拼写错误 / `show screen` 未生效 |
| 变量值不对 | 多个地方修改同一变量 / save 加载后未正确恢复 |
| `IndentationError` | `.rpy` 文件混用 tab 和空格 |
