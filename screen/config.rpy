screen config:
    tag menu
    
    use game_menu("Config"):
        grid 2 1:
            xfill True

            style_prefix "config"

            vbox:
                spacing 50

                hbox:
                    text "画面模式"
                    textbutton "窗口模式" action Preference("display", "window")
                    textbutton "全屏模式" action Preference("display", "fullscreen")

                hbox:
                    text "文本快进"
                    textbutton "仅已读文本" action Preference("skip", "seen")
                    textbutton "全部文本" action Preference("skip", "all")

                hbox:
                    text "文本显示速度"
                    bar value Preference("text speed")

                hbox:
                    text "自动模式速度"
                    bar value Preference("auto-forward time")

            vbox:
                spacing 50

                hbox:
                    text "BGM"
                    bar value Preference("music volume")

                hbox:
                    text "效果音"
                    bar value Preference("sound volume")

                hbox:
                    text "语音"
                    bar value Preference("voice volume")


## --------- Style ---------

style config_text:
    size 32

style config_button_text:
    size 32

style config_slider:
    xsize 200
    ysize 20
    left_bar "#4caf50"
    right_bar "#666666"
