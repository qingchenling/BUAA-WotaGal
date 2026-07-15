screen save():
    tag menu
    use game_menu("SAVE"):
        use file_slots

screen load():
    tag menu
    use game_menu("LOAD"):
        use file_slots

screen file_slots:
    frame:
        xfill True
        yfill True
        bottom_padding 50

        grid 5 2:
            xfill True
            yfill True
            spacing 10

            for i in range(1, 11):
                button:
                    action FileAction(i)
                    xfill True
                    yfill True
                    background "#00000080"

                    hbox:
                        xfill True
                        ysize 32
                        spacing 20

                        text FileSlotName(i, 10, 'A', 'Q'):
                            size 32
                        text FileTime(i, format="%Y/%m/%d %H:%M"):
                            size 28

                    add FileScreenshot(i):
                        xalign 0.5
                        ypos 32
                        fit "contain"

                    text FileSaveName(i):
                        xfill True
                        yalign 0.95

    hbox:
        yalign 1.0
        ysize 30
        xalign 1.0
        xfill True
        box_align True
        spacing 20

        style_prefix "save_buttons"

        textbutton "<" action FilePagePrevious()
        textbutton "A" action FilePage("auto")
        textbutton "Q" action FilePage("quick")
        for i in range(1, 6):
            textbutton "[i]" action FilePage(i)
        textbutton ">" action FilePageNext(5)

        key "save_page_prev" action FilePagePrevious()
        key "save_page_next" action FilePageNext(5)


## --------- Style ---------

style save_buttons_button:
    yfill True

style save_buttons_button_text:
    size 36
    color "#ffffff"
    hover_color "#ffcc00"
