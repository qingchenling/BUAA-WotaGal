screen main_menu():
    tag menu
    style_prefix "mainMenu"

    vbox:
        style "mainMenu_vbox"

        text "光轨" style "mainMenu_title"

        null height 100

        textbutton "开始游戏" action Start()
        textbutton "继续游戏" action ShowMenu("load")
        textbutton "退出" action Quit()
