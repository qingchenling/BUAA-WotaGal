# 练习场地行为

label loc_practice:

    # 一周只能行动一次，防止反复刷数值
    if has_acted:
        p "这周已经练过了，剩下的时间由你自己安排。"
        return

    scene black

    p"咏曼剧场旁边的舞蹈房。今晚是周常训练。"
    p"林若演示了一遍完整的动作。你终于学会了。"

    $ options, picks = choose_skills()
    $ pick_index = 0

label practice_pick:
    if pick_index >= picks:
        jump practice_done

    # 构建动态菜单
    # 注意：标签级 python 块是全局作用域，循环变量不能叫 s / y / w 等，
    # 否则会把同名 Character 覆盖掉（曾导致 w6 报 "Sayer 's' is not a function"）。
    $ menu_items = []
    python:
        for sk in options:
            sid = sk['id']
            color = get_mastery_color(sk['hidden_mastery'])
            tag = "【新】" if sk['is_new'] else ""
            caption = "{color=" + color + "}" + sk['name'] + "{/color}"
            caption += " 难度" + str(sk['difficulty'])
            caption += " 熟练度" + str(sk['mastery'])
            title_str = get_mastery_title(sk['hidden_mastery'])
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

    # 只标记本周已行动，周数由 gameflow 统一推进
    $ has_acted = True
    return
