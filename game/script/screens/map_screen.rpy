#地图界面
#其他页面也在这里写



screen map_screen():

    text "第 [week]周" xpos 30 ypos 30

    text "名声[fame]" xpos 30 ypos 70

    text "个人技艺值 [person_skill]" xpos 30 ypos 110
    #这里的位置还需要调整一下

    textbutton "{color=#DC143C}练习场地1{/color}":

        xpos 100
        ypos 300

        action Call("loc_practice")
    
    textbutton "{color=#DC143C}练习场地2{/color}":

        xpos 100
        ypos 500

        action Call("loc_practice")