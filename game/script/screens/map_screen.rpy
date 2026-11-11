# 地图界面

screen map_screen():

    # 顶部周次
    text "第 [week] 周" xpos 30 ypos 30 size 28

    # 共通线末段 / 个人线显示当前路线
    if route is not None:
        text "[route_label]" xpos 30 ypos 66 size 20 color "#DC143C"

    text "名气 [fame]" xpos 30 ypos 110 size 22

    text "技艺值 [person_skill]" xpos 30 ypos 150 size 22

    if route == "yoko":
        text "叶子好感 [affection_yoko]" xpos 30 ypos 190 size 20 color "#AAAAAA"
    elif route == "songke":
        text "圈内知名度 [fame_club]" xpos 30 ypos 190 size 20 color "#AAAAAA"
    elif route == "rin":
        text "林若好感 [affection_rin]" xpos 30 ypos 190 size 20 color "#AAAAAA"

    $ picks = get_pick_count()
    text "本周可选 [picks] 次" xpos 30 ypos 230 size 20 color "#AAAAAA"

    # 本周行动（一周一次）
    if has_acted:
        textbutton "练习场地（本周已用过）":
            xpos 100
            ypos 300
            sensitive False
            text_color "#666666"
    else:
        textbutton "{color=#DC143C}练习场地{/color}":
            xpos 100
            ypos 300
            action Call("loc_practice")

    # 结束本周
    textbutton "结束本周":
        xpos 1600
        ypos 800
        action Return()
