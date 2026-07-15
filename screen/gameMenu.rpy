## 子菜单布局
## 由其他 screen 调用

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
        padding (30,150,30,150)
        
        transclude

    frame:
        xfill True
        yalign 1.0
        ysize 100
        background "#dddddd"

        hbox:
            xfill True
            box_align 0.5
            spacing 100

            style_prefix "gameMenu_list"

            textbutton "Save" action ShowMenu("save")
            textbutton "Load" action ShowMenu("load")
            textbutton "Config" action ShowMenu("config")
            textbutton "Title" action MainMenu()
            textbutton "Quit" action Quit()
            textbutton "Back" action Return()
            

## --------- Style ---------

style gameMenu_list_button_text:
    size 64
