## 设置界面
##
## 提供游戏设置的调整：显示模式、文本速度、自动推进时间、音量等。
screen preferences():
    tag menu
    use game_menu("设置", scroll="viewport"):

        style_prefix "pref"

        vbox:
            spacing 28

            # ── 显示模式 ──
            vbox:
                spacing 10
                style_prefix "pref_section"

                label "显示"

                hbox:
                    spacing 16
                    style_prefix "pref_radio"

                    textbutton "窗口" action Preference("display", "window")
                    textbutton "全屏" action Preference("display", "fullscreen")

            # ── 文本设置 ──
            vbox:
                spacing 10
                style_prefix "pref_section"

                label "文本速度"

                hbox:
                    style_prefix "pref_slider"
                    bar value Preference("text speed")

            # ── 自动推进时间 ──
            vbox:
                spacing 10
                style_prefix "pref_section"

                label "自动推进时间"

                hbox:
                    style_prefix "pref_slider"
                    bar value Preference("auto-forward time")

            # ── 音乐音量 ──
            if config.has_music:
                vbox:
                    spacing 10
                    style_prefix "pref_section"

                    label "音乐音量"

                    hbox:
                        spacing 16
                        style_prefix "pref_slider"
                        bar value Preference("music volume")

            # ── 音效音量 ──
            if config.has_sound:
                vbox:
                    spacing 10
                    style_prefix "pref_section"

                    label "音效音量"

                    hbox:
                        spacing 16
                        style_prefix "pref_slider"

                        bar value Preference("sound volume")

                        if config.sample_sound:
                            textbutton "试听" action Play("sound", config.sample_sound)

            # ── 语音音量 ──
            if config.has_voice:
                vbox:
                    spacing 10
                    style_prefix "pref_section"

                    label "语音音量"

                    hbox:
                        spacing 16
                        style_prefix "pref_slider"

                        bar value Preference("voice volume")

                        if config.sample_voice:
                            textbutton "试听" action Play("voice", config.sample_voice)

            # ── 静音 ──
            if config.has_music or config.has_sound or config.has_voice:
                null height 10

                textbutton "全部静音":
                    style_prefix "pref_check"
                    action Preference("all mute", "toggle")
