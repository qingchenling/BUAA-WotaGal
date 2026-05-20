screen main_menu():
    tag menu
    style_prefix "mainMenu"

    vbox:
        style "mainMenu_buttonBox"
        textbutton "开始游戏" action Start()
        textbutton "退出" action Quit()
