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
                    padding (10,10,10,10)

                    text FileSlotName(i, 10, 'A', 'Q'):
                        size 32
                        font en_font
                    text FileTime(i, format="%Y/%m/%d %H:%M"):
                        xalign 1.0
                        size 28
                        font en_font

                    add FileScreenshot(i):
                        xalign 0.5
                        ypos 48
                        fit "contain"

                    if not FileLoadable(i):
                        text "NO DATA":
                            xalign 0.5
                            ypos 108
                            size 42
                            color "#555555"

                    text FileSaveName(i):
                        xfill True
                        yalign 0.95
                        size 32

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
