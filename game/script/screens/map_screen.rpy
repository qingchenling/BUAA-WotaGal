# 地图界面

screen map_screen():

    text "第 [week] 周" xpos 30 ypos 30 size 28

    text "名气 [fame]" xpos 30 ypos 70 size 22

    text "技艺值 [person_skill]" xpos 30 ypos 110 size 22

    $ picks = get_pick_count()
    text "本周可选 [picks] 次" xpos 30 ypos 150 size 20 color "#AAAAAA"

    textbutton "{color=#DC143C}练习场地{/color}":

        xpos 100
        ypos 300

        action Call("loc_practice")

    textbutton "继续":
        xpos 1600
        ypos 800
        action Return()
