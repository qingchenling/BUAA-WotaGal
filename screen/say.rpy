## System Screen
## id="who"     接收 who_* 参数
## id="what"    接收 what_* 参数
## id="window"  接收 window_* 参数

screen say(who, what):
    window id "window":
        xfill True
        yalign 1.0
        ysize 350
        add "assets/say_bck.png":
            xalign 0.5
            yalign 0.5
            xoffset 10
            yoffset 10
        add "assets/say_fnt.png":
            xalign 0.5
            yalign 0.5

        if who is not None:
            add "assets/namebox.png":
                xalign 0.25
                yoffset 5
            text who id "who":
                xpos 0.28
                ypos 0.04
                size 36
                font say_text_font

        text what id "what":
            xpos 0.2
            ypos 0.25
            xsize 0.6
            size 32
            font say_text_font

    hbox:
        xalign 0.5
        yalign 1.0
        spacing 10

        button:
            action QuickSave()

            text "Q.Save"

        button:
            action QuickLoad()

            text "Q.Load"

        button:
            action ShowMenu("save")

            text "Save"

        button:
            action ShowMenu("load")

            text "Load"

        button:
            action Preference("auto-forward", "toggle")

            text "Auto"

        button:
            action Skip()

            text "Skip"

        button:
            action MainMenu()

            text "Title"

        button:
            action Quit()

            text "Quit"

        button:
            action ShowMenu("config")

            text "Config"
