## ============================================================
## game_menu 整体布局样式
## ============================================================

## 主 hbox - 全屏布局，背景直接在 screen 中设置
style gameMenu_hbox:
    background None

## ── 左侧导航栏 ──

## 导航栏容器
style gameMenu_nav_vbox:
    xsize 320
    yfill True
    spacing 12
    padding (80, 60, 30, 60)

## 导航栏 - 当前页面标题
style gameMenu_nav_label:
    color "#ffffff"
    size 36
    textalign 0.5
    xalign 0.5

style gameMenu_nav_label_text:
    color "#ffffff"
    size 36
    textalign 0.5

## 导航栏 - 按钮
style gameMenu_nav_button:
    xfill True
    ysize 44
    background None
    padding (16, 8)

style gameMenu_nav_button_text:
    color "#999999"
    size 26
    hover_color "#ffffff"
    selected_color "#ffcc00"
    xalign 0.5

## ── 右侧内容区 ──
style gameMenu_content:
    background None
    padding (60, 60)
    xfill True
    yfill True
