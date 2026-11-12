# 沙河校区 · 行动地点
# 咏曼剧场见 location/practice.rpy
# 天空之境、北京壹号在这里

# ============================================================
# 天空之境：所有已解锁技 熟练度 +10
# ============================================================
label loc_sky:

    if has_acted:
        p "这周已经行动过了，剩下的时间由你自己安排。"
        return

    $ boosted = boost_all_mastery(10)

    if boosted == 0:
        scene bg skymirror
        p "天空之境。你站了一会儿，发现自己还什么都不会。"
        return

    scene bg skymirror
    p "反复练习，你找到了正确的发力感觉。"
    p "（[boosted] 个技的熟练度 +10）"

    $ has_acted = True
    return


# ============================================================
# 北京壹号：选 3 技录视频换名气（需已解锁技 ≥ 3）
# ============================================================
label loc_beijing:

    if has_acted:
        p "这周已经行动过了，剩下的时间由你自己安排。"
        return

    $ pool = list(get_unlocked_skills())
    $ n_unlocked = len(pool)

    if n_unlocked < 3:
        p "至少要会 3 个技，才敢录视频。现在你会 [n_unlocked] 个。"
        return

    scene bg danceroom
    p "北京壹号。你把手机架在窗台上，调了三遍角度。"

    $ chosen = []

    while len(chosen) < 3:
        $ menu_items = [(s["name"] + "　熟练度 " + str(s["mastery"]) + "　魅力 " + str(s["charm"]), s["id"]) for s in pool]
        $ sid = renpy.display_menu(menu_items)
        $ chosen.append(sid)
        $ pool = [s for s in pool if s["id"] != sid]

    $ gained = apply_show_fame(chosen)

    p "视频上传。你关上屏幕，胳膊还有点酸。"
    p "本次获得名气 [gained]，累计名气 [fame]。"

    $ has_acted = True
    return
