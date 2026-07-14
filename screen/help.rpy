## 帮助 / 关于界面
##
## 显示游戏介绍、世界背景和基本操作说明。
screen help():
    tag menu
    use game_menu("帮助", scroll="viewport"):

        style_prefix "help"

        vbox:
            xmaximum 860
            xalign 0.5
            spacing 20
            xfill True

            text "光轨":
                style "help_title"

            text "Dahuo Light  ·  ver. [config.version!t]":
                style "help_subtitle"

            null height 20

            text "故事背景":
                style "help_section"

            text "2025 年秋，飞梦 ACG 联盟元气大伤，其下属宅艺研仅剩最后一名成员林若。\n你在高考后的暑假通过 B 站第一次接触 Wota 艺。\n荧光棒在黑暗中划出光弧的姿态让你看到了梦想中大学的自己。\n来北航之前你就查好了宅艺研的信息，你不知道的是，等你到的时候，那个社团已经面临废社。":
                style "help_body"

            null height 20

            text "操作方法":
                style "help_section"

            text "• 鼠标左键 / 空格 / Enter —— 推进对话\n• 鼠标右键 / Esc —— 调出系统菜单\n• 滚轮 —— 回顾历史对话\n• 鼠标点击 —— 选择行动地点和选项":
                style "help_body"

            null height 24

            text "Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only]":
                style "help_footer"
