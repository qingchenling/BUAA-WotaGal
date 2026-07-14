## 存档界面
screen save():
    tag menu
    use game_menu("保存"):
        use file_slots

## 读档界面
screen load():
    tag menu
    use game_menu("读取"):
        use file_slots

## 共用存档 / 读档槽位布局
screen file_slots():
    style_prefix "slot"

    fixed:
        xfill True
        yfill True

        ## 当前存档页名称（可点击编辑）
        button:
            style "slot_page_label"
            key_events True
            xalign 0.5
            ypos 0
            action FilePageNameInputValue(pattern="第 {} 页", auto="自动存档", quick="快速存档").Toggle()

            input:
                style "slot_page_label_text"
                value FilePageNameInputValue(pattern="第 {} 页", auto="自动存档", quick="快速存档")

        ## 存档槽位网格 (3 列 × 3 行)
        grid 3 3:
            xalign 0.5
            yalign 0.5
            spacing 24

            for i in range(3 * 3):
                $ slot = i + 1

                button:
                    id "slot_button"
                    action FileAction(slot)

                    has vbox:
                        spacing 8

                    add FileScreenshot(slot) xalign 0.5

                    text FileTime(slot, format="%Y/%m/%d %H:%M", empty="空槽位"):
                        style "slot_time_text"

                    text FileSaveName(slot):
                        style "slot_name_text"

                    key "save_delete" action FileDelete(slot)

        ## 翻页按钮
        hbox:
            style_prefix "slot_page"
            xalign 0.5
            yalign 1.0
            spacing 12

            textbutton "<" action FilePagePrevious()
            key "save_page_prev" action FilePagePrevious()

            if config.has_autosave:
                textbutton "A" action FilePage("auto")

            if config.has_quicksave:
                textbutton "Q" action FilePage("quick")

            for page in range(1, 10):
                textbutton "[page]" action FilePage(page)

            textbutton ">" action FilePageNext()
            key "save_page_next" action FilePageNext()
