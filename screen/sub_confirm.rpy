## belong to "Global"
##
## System Screen
## 

screen confirm(message, yes_action, no_action):
    modal True
    style_prefix "confirm"

    ## 绑定 ESC 和 右键
    key "game_menu" action no_action

    add "#000000aa"

    frame:
        background "#00cccc"
        xalign 0.5
        yalign 0.5
        padding (90, 60, 90, 60)

        vbox:
            xalign 0.5
            yalign 0.5
            spacing 30

            text message:
                xalign 0.5
                size 32

            hbox:
                xalign 0.5
                spacing 100

                textbutton "Yes" action yes_action
                textbutton "No" action no_action


## --------- Style ---------

style confirm_button_text:
    size 40
    color "#ffffff"
    hover_color "#ffcc00"
