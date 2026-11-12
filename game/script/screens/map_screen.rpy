# 地图界面
#
# 布局：1122x995 的校园图按 1080 高度铺满（缩放 1.0854，宽 1217，左侧偏移 351），
# 三个地点用图标直接标在地图对应位置。

define MAP_ZOOM = 1.0854

screen map_screen():

    # 地图上不显示底部快捷菜单，避免压住地图
    on "show" action SetVariable("quick_menu", False)
    on "hide" action SetVariable("quick_menu", True)

    # 底色与地图边缘同色，左右留白不会突兀
    add Solid("#002E3B")

    # 地图底图（自己画，避免从地点返回后残留别的背景）
    add "images/bg/map.png" zoom MAP_ZOOM xalign 0.5 yalign 0.5

    $ picks = get_pick_count()

    # ---------------- 顶部信息 ----------------
    frame:
        background "#0B1A1F99"
        padding (20, 14)
        xpos 28
        ypos 24

        vbox:
            spacing 4
            text "第 [week] 周" size 32 color "#FFFFFF"
            if route is not None:
                text "[route_label]" size 20 color "#DC143C"
            text "名气 [fame]　技艺值 [person_skill]" size 21 color "#DCE6E8"
            if route == "yoko":
                text "叶子好感 [affection_yoko]" size 18 color "#9FB3B8"
            elif route == "songke":
                text "圈内知名度 [fame_club]" size 18 color "#9FB3B8"
            elif route == "rin":
                text "林若好感 [affection_rin]" size 18 color "#9FB3B8"
            text "本周可选 [picks] 次" size 18 color "#9FB3B8"

    # ---------------- 地点图标 ----------------

    # 咏曼剧场：抽 5 选 2 学技
    imagebutton:
        idle "images/ui/icon_yongman.png"
        hover "images/ui/icon_yongman_hover.png"
        insensitive "images/ui/icon_yongman_off.png"
        sensitive (not has_acted)
        xpos LOC_YONGMAN_X
        ypos LOC_YONGMAN_Y
        xanchor 0.5
        yanchor 0.5
        action Call("loc_practice")

    text "咏曼剧场" size 24:
        xpos LOC_YONGMAN_X
        xanchor 0.5
        ypos LOC_YONGMAN_LY
        color ("#FFFFFF" if not has_acted else "#8FA6AC")
        outlines [(3, "#002E3B", 0, 0)]

    text "抽 5 选 2 学新技" size 17 color "#CFE0E4" outlines [(2, "#002E3B", 0, 0)]:
        xpos LOC_YONGMAN_X
        xanchor 0.5
        ypos LOC_YONGMAN_DY

    # 天空之境：所有已解锁技 熟练度 +10
    imagebutton:
        idle "images/ui/icon_sky.png"
        hover "images/ui/icon_sky_hover.png"
        insensitive "images/ui/icon_sky_off.png"
        sensitive (not has_acted)
        xpos LOC_SKY_X
        ypos LOC_SKY_Y
        xanchor 0.5
        yanchor 0.5
        action Call("loc_sky")

    text "天空之境" size 24:
        xpos LOC_SKY_X
        xanchor 0.5
        ypos LOC_SKY_LY
        color ("#FFFFFF" if not has_acted else "#8FA6AC")
        outlines [(3, "#002E3B", 0, 0)]

    text "已解锁技 熟练度 +10" size 17 color "#CFE0E4" outlines [(2, "#002E3B", 0, 0)]:
        xpos LOC_SKY_X
        xanchor 0.5
        ypos LOC_SKY_DY

    # 北京壹号：选 3 技换名气（需已解锁技 >= 3）
    $ bei_ok = (not has_acted) and len(get_unlocked_skills()) >= 3

    imagebutton:
        idle "images/ui/icon_beijing.png"
        hover "images/ui/icon_beijing_hover.png"
        insensitive "images/ui/icon_beijing_off.png"
        sensitive bei_ok
        xpos LOC_BEIJING_X
        ypos LOC_BEIJING_Y
        xanchor 0.5
        yanchor 0.5
        action Call("loc_beijing")

    text "北京壹号" size 24:
        xpos LOC_BEIJING_X
        xanchor 0.5
        ypos LOC_BEIJING_LY
        color ("#FFFFFF" if bei_ok else "#8FA6AC")
        outlines [(3, "#002E3B", 0, 0)]

    text "选 3 技换名气（需会 3 个技）" size 17 color "#CFE0E4" outlines [(2, "#002E3B", 0, 0)]:
        xpos LOC_BEIJING_X
        xanchor 0.5
        ypos LOC_BEIJING_DY

    # ---------------- 状态与结束 ----------------
    if has_acted:
        text "本周已行动" xpos 28 ypos 210 size 20 color "#8AA0A6"

    textbutton "结束本周 →":
        xpos 1860
        ypos 1020
        xanchor 1.0
        yanchor 1.0
        action Return()
