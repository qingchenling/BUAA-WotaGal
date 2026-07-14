## ============================================================
## 设置界面样式
## ============================================================

## 设置 - 分区标题
style pref_section_label:
    color "#ffcc00"
    size 28

style pref_section_label_text:
    color "#ffcc00"
    size 28

## 设置 - 滑块
## 使用 Solid + Frame 绘制，无需外部图片资源
style pref_slider_bar:
    xsize 400
    ysize 36
    base_bar Frame(Solid("#333333"), 8, 0)
    hover_base_bar Frame(Solid("#555555"), 8, 0)
    thumb Solid("#ffcc00")

## 设置 - 单选按钮（窗口 / 全屏）
style pref_radio_button:
    background None
    padding (12, 8)

style pref_radio_button_text:
    color "#999999"
    size 24
    hover_color "#ffffff"
    selected_color "#ffcc00"

## 设置 - 开关按钮（静音等）
style pref_check_button:
    background None
    padding (12, 8)

style pref_check_button_text:
    color "#999999"
    size 24
    hover_color "#ffffff"
    selected_color "#ffcc00"

## 设置 - 试听按钮（音效 / 语音测试）
style pref_slider_button:
    background None
    padding (8, 6)

style pref_slider_button_text:
    color "#999999"
    size 20
    hover_color "#ffffff"
