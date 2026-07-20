# 练习场地行为

label loc_practice:

    scene black

    p"你来到练习场地，开始今天的训练。"

    $ options, picks = choose_skills()
    $ pick_index = 0

label practice_pick:
    if pick_index >= picks:
        jump practice_done

    # 构建动态菜单
    $ menu_items = []
    python:
        for s in options:
            sid = s['id']
            color = get_mastery_color(s['hidden_mastery'])
            tag = "【新】" if s['is_new'] else ""
            caption = "{color=" + color + "}" + s['name'] + "{/color}"
            caption += " 难度" + str(s['difficulty'])
            caption += " 熟练度" + str(s['mastery'])
            title_str = get_mastery_title(s['hidden_mastery'])
            if title_str:
                caption += " " + title_str
            if tag:
                caption += " " + tag
            menu_items.append((caption, sid))

        menu_items.append(("跳过剩余练习", -1))

    $ chosen_id = renpy.display_menu(menu_items)

    if chosen_id == -1:
        jump practice_done

    $ name, gain, maxed, diff = practice_skill(chosen_id)

    if maxed:
        p"[name] 已达到「大成」！技艺值将在本周结算时额外提升。"
    else:
        p"练习了 [name]，熟练度 +[gain]"

    $ pick_index += 1

    if pick_index < picks:
        $ options = choose_skills()[0]
        jump practice_pick
    jump practice_done

label practice_done:
    $ ps_gain = apply_weekly_ps()
    if ps_gain > 0:
        p"本周技艺值提升了 [ps_gain] 点。"
    p"当前技艺值：[person_skill]，名气：[fame]"

    $ next_week()
    return
