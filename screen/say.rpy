## System Screen
## id="who"     接收 who_* 参数
## id="what"    接收 what_* 参数
## id="window"  接收 window_* 参数

screen say(who, what):
    window id "window":
        xfill True
        yalign 1.0
        ysize 300
        background "#000000cc"
        padding (360, 60, 120, 60)

        vbox:
            if who is not None:
                text who id "who":
                    size 32

            text what id "what":
                size 32
