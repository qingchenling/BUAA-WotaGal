screen main_menu():
    tag menu
    style_prefix "mainMenu"

    add "assets/menuBg.png"

    vbox:
        textbutton "开始游戏" action Start()
        textbutton "继续游戏" action ShowMenu("load")
        textbutton "退出" action Quit()
