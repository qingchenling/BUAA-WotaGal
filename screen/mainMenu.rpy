## System Screen

screen main_menu():
    tag menu

    style_prefix "mainMenu"

    add "assets/menuBg.png"

    vbox:
        xalign 0.9
        yalign 0.1
        spacing 40

        textbutton "开始游戏" action Start()
        textbutton "继续游戏" action Continue()
        textbutton "读档" action ShowMenu("load")
        textbutton "设置" action ShowMenu("config")
        textbutton "退出" action Quit()



## --------- Style ---------

style mainMenu_button:
    activate_sound btn_sound
    xalign 0.5

style mainMenu_button_text:
    size 32
    color "#ffffff"
    hover_color "#ffcc00"

