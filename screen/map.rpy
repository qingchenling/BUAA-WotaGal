screen map():
    modal True

    frame:
        xalign 0.2
        yalign 0.2
        background "#ffffff"
        text "第%d周" % week:
            color "#000000"

    textbutton "永慢剧场":
        xalign 0.3
        yalign 0.6
        action Return("yongman")
