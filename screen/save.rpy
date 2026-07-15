screen save():
    tag menu
    use game_menu("SAVE"):
        use file_slots

screen load():
    tag menu
    use game_menu("LOAD"):
        use file_slots

screen file_slots:
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

                has vbox:
                    xfill True

                hbox:
                    text "%2d" % i:
                        size 32
                    text FileTime(i, format="%Y/%m/%d %H:%M"):
                        size 28
                add FileScreenshot(i)
                text FileSaveName(i)
