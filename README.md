# 《光轨》WOTA

## 简介

《光轨》是一款以「北航 Wota 艺社团重建」为主题的周次制文字养成游戏，基于 Ren'Py 引擎开发。玩家扮演一名大一新生，在 20 周内通过选择地点行动、学习技能、积累知名度、触发剧情，最终影响社团走向及个人故事结局。

**背景：** 2025 年秋，飞梦 ACG 联盟元气大伤，其下属宅艺研仅剩最后一名成员林若。你在高考后的暑假通过 B 站第一次接触 Wota 艺——荧光棒在黑暗中划出光弧的姿态，让你看到了梦想中大学的自己。来北航之前你就查好了宅艺研的信息。你不知道的是，等你到的时候，那个社团已经面临废社。

## 项目结构

```
根目录/
├── game/                      # Ren'Py 游戏主体
│   ├── script/                # 游戏脚本（Python/Ren'Py）
│   │   ├── core/              # 核心逻辑
│   │   │   ├── datastore.rpy  # 全局变量定义
│   │   │   ├── api.rpy        # 状态修改函数
│   │   │   └── gameflow.rpy   # 主游戏循环
│   │   ├── story/             # 周次剧情 & 事件触发
│   │   ├── location/          # 地点行动（练习等）
│   │   ├── screens/           # 自定义 UI（地图界面）
│   │   ├── script.rpy         # 入口：角色定义 → 开场
│   │   ├── gui.rpy            # GUI 配置
│   │   ├── screens.rpy        # 系统界面
│   │   └── options.rpy        # 语言/转场/构建选项
│   ├── images/                # 美术资源
│   │   ├── bg/                # 背景图
│   │   ├── sprites/           # 角色立绘
│   │   └── images.rpy         # 图片声明
│   ├── gui/                   # UI 组件图片
│   ├── audio/                 # 音频资源
│   └── tl/                    # 翻译文件
├── assets/                    # 构建素材（图标、构建配置）
│   ├── icons/                 # 平台图标（ico/icns/svg/android/ios）
│   ├── android.json
│   ├── project.json
│   └── progressive_download.txt
├── 剧本讨论/                  # 设计文档（剧本、人设）
│   ├── 人设.md
│   ├── 叶子线剧情.md
│   ├── 剧本（完整设定）.docx
│   └── 开发指导.docx
├── temp/                      # 废弃/临时文件（已 gitignore）
├── CLAUDE.md                  # Claude Code 项目指南
├── README.md                  # 本文件
└── LICENSE
```

## 技术栈

- **引擎：** Ren'Py（Python）
- **脚本：** 所有 `.rpy` 文件在构建时统一编译，无需显式 `import`
- **变量：** 使用 Ren'Py 的 `default` 关键字在 `core/datastore.rpy` 统一定义，`define` 用于常量

## 开发指南

详细架构约定和开发命令请参阅 [CLAUDE.md](CLAUDE.md)。

### 快速开始

```bash
# Windows
renpy.exe F:\game\galgame\WOTA

# macOS / Linux
./renpy.sh F:/game/galgame/WOTA

# 代码检查
renpy.exe F:\game\galgame\WOTA lint
```

构建前需将 `assets/icons/` 中的图标复制到项目根目录。

## 许可

[LICENSE](LICENSE)
