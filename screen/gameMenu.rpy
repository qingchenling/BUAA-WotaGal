## 子菜单布局
## 由其他 screen 调用

default menu_hover = ""

screen game_menu(title):

    add "#123456"

    ## 系统变量 main_menu
    if main_menu:
        key "game_menu" action Return()

    frame:
        xfill True
        ysize 100
        background "#00aadd"
        
        text title:
            size 100

        frame:
            background "#ffffff"
            xfill True
            ysize 3
            yalign 1.0

    frame:
        xfill True
        yfill True
        padding (30,150,30,200)
        
        transclude

    frame:
        xfill True
        yalign 1.0
        ysize 150
        left_padding 100
        right_padding 50
        background "assets/gameMenu.png"

        hbox:
            xfill True
            box_align 0.5
            yalign 0.5
            spacing 190

            style_prefix "gameMenu_list"
            
            button:
                action ShowMenu("save")

                hovered SetVariable("menu_hover", "save")
                unhovered SetVariable("menu_hover", "")

                vbox:
                    text "Save" style "gameMenu_e":
                        color ("#b3c0f5" if menu_hover == "save" else "#899de3")
                        outlines (
                            [(1, "#b3c0f5aa", 0, 0)]
                            if menu_hover == "save"
                            else [(1, "#00000000", 0, 0)]
                        )

                    text "存档" style "gameMenu_c":
                        color ("#b3c0f5" if menu_hover == "save" else "#899de3")
                        outlines (
                            [(1, "#b3c0f5aa", 0, 0)]
                            if menu_hover == "save"
                            else [(1, "#00000000", 0, 0)]
                        )


            button:
                action ShowMenu("load")

                hovered SetVariable("menu_hover", "load")
                unhovered SetVariable("menu_hover", "")

                vbox:
                    text "Load" style "gameMenu_e":
                        color ("#a0efbc" if menu_hover == "load" else "#73de9a")
                        outlines (
                            [(1, "#a0efbcaa", 0, 0)]
                            if menu_hover == "load"
                            else [(1, "#00000000", 0, 0)]
                        )

                    text "读档" style "gameMenu_c":
                        color ("#a0efbc" if menu_hover == "load" else "#73de9a")
                        outlines (
                            [(1, "#a0efbcaa", 0, 0)]
                            if menu_hover == "load"
                            else [(1, "#00000000", 0, 0)]
                        )


            button:
                action ShowMenu("config")

                hovered SetVariable("menu_hover", "config")
                unhovered SetVariable("menu_hover", "")

                vbox:
                    text "Config" style "gameMenu_e":
                        color ("#f08fb6" if menu_hover == "config" else "#d95c8f")
                        outlines (
                            [(1, "#f08fb6aa", 0, 0)]
                            if menu_hover == "config"
                            else [(1, "#00000000", 0, 0)]
                        )

                    text "设置" style "gameMenu_c":
                        color ("#f08fb6" if menu_hover == "config" else "#d95c8f")
                        outlines (
                            [(1, "#f08fb6aa", 0, 0)]
                            if menu_hover == "config"
                            else [(1, "#00000000", 0, 0)]
                        )


            button:
                action MainMenu()

                hovered SetVariable("menu_hover", "title")
                unhovered SetVariable("menu_hover", "")

                vbox:
                    text "Title" style "gameMenu_e":
                        color ("#f3dfab" if menu_hover == "title" else "#e2c982")
                        outlines (
                            [(1, "#f3dfabaa", 0, 0)]
                            if menu_hover == "title"
                            else [(1, "#00000000", 0, 0)]
                        )

                    text "主菜单" style "gameMenu_c":
                        color ("#f3dfab" if menu_hover == "title" else "#e2c982")
                        outlines (
                            [(1, "#f3dfabaa", 0, 0)]
                            if menu_hover == "title"
                            else [(1, "#00000000", 0, 0)]
                        )


            button:
                action Quit()

                hovered SetVariable("menu_hover", "quit")
                unhovered SetVariable("menu_hover", "")

                vbox:
                    text "Quit" style "gameMenu_e":
                        color ("#d4a8f0" if menu_hover == "quit" else "#b576df")
                        outlines (
                            [(1, "#d4a8f0aa", 0, 0)]
                            if menu_hover == "quit"
                            else [(1, "#00000000", 0, 0)]
                        )

                    text "退出游戏" style "gameMenu_c":
                        color ("#d4a8f0" if menu_hover == "quit" else "#b576df")
                        outlines (
                            [(1, "#d4a8f0aa", 0, 0)]
                            if menu_hover == "quit"
                            else [(1, "#00000000", 0, 0)]
                        )


            button:
                action Return()

                hovered SetVariable("menu_hover", "back")
                unhovered SetVariable("menu_hover", "")

                vbox:
                    text "Back" style "gameMenu_e":
                        color ("#9ee7ef" if menu_hover == "back" else "#73d2de")
                        outlines (
                            [(1, "#9ee7efaa", 0, 0)]
                            if menu_hover == "back"
                            else [(1, "#00000000", 0, 0)]
                        )

                    text "返回游戏" style "gameMenu_c":
                        color ("#9ee7ef" if menu_hover == "back" else "#73d2de")
                        outlines (
                            [(1, "#9ee7efaa", 0, 0)]
                            if menu_hover == "back"
                            else [(1, "#00000000", 0, 0)]
                        )


## --------- Style ---------

style gameMenu_list_button:
    xsize 120

style gameMenu_e:
    xalign 0.5
    size 42
    kerning 3

style gameMenu_c:
    xalign 0.5
    size 24
    kerning 5
