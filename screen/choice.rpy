screen choice(items):
    vbox:
        xalign 0.5
        yalign 0.5
        spacing 30

        for i in items:
            button:
                action i.action
                activate_sound btn_sound
                text i.caption:
                    size 32
                    color "#ffffff"
                    hover_color "#ffcc00"
