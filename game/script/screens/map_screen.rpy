# 地图界面

screen map_screen():

    # 顶部周次
    text "第 [week] 周" xpos 30 ypos 30 size 28

    # 个人线显示当前路线
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

    # 沙河校区地点
    $ locs = [
        ("咏曼剧场", "loc_practice", True,                     "抽 5 选 2 学新技"),
        ("天空之境", "loc_sky",      True,                     "所有已解锁技 熟练度 +10"),
        ("北京壹号", "loc_beijing",  len(get_unlocked_skills()) >= 3, "选 3 技换名气（需会 3 个技）"),
    ]

    vbox:
        xpos 100
        ypos 320
        spacing 18

        for nm, lbl, ok, desc in locs:
            button:
                sensitive (ok and not has_acted)
                action Call(lbl)
                text (nm + "    " + desc) size 26

    # 本周行动状态
    if has_acted:
        text "本周已行动" xpos 100 ypos 520 size 20 color "#666666"

    # 结束本周
    textbutton "结束本周":
        xpos 1600
        ypos 800
        action Return()
