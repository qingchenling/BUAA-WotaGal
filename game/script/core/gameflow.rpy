# 游戏流程控制
#
# 时间轴：
#   W0-W10   共通线
#   W11      选线（林若 / 叶子 / 宋柯）
#   W11-W16  个人线
#   W17      最终选择（HE / BE）
#   W18-W20  结局卷
#
# 每周固定顺序：
#   周次提示 → 路线门 → 周剧情 → 最终选择门 → 行动 → 演出 → 特殊事件 → 结算 → 推进
#
# 原则：一周只推进一次，且只能由本文件的 next_week() 推进。
# 任何地点行为（练习等）都不许自己改 week。

image map:
    "images/bg/map.png"
    zoom 1.5

label week_loop:

    # 结局卷不再回日常循环
    if week >= ENDING_WEEK:
        jump play_ending

    call week_intro
    call route_gate
    call weekly_story_check
    call route_event_check
    call final_gate
    call action_phase
    call performance_event_check
    call random_event_check
    call special_event_check
    call week_settle

    if is_game_over():
        jump play_ending

    $ next_week()
    jump week_loop


# ------------------------------------------------------------
# 周次提示
# ------------------------------------------------------------
label week_intro:
    scene map
    if route is None:
        p "第 [week] 周。"
    else:
        p "第 [week] 周。现在是 [route_label]。"
    return


# ------------------------------------------------------------
# 本周行动
# ------------------------------------------------------------
label action_phase:
    $ has_acted = False
    call screen map_screen
    return


# ------------------------------------------------------------
# 周结算
# ------------------------------------------------------------
label week_settle:
    # 进入个人线后，每周行动会积累路线好感与圈内知名度。
    # W11-W16 六周全勤 = 好感 60 / 知名度 120，刚好够到 HE 线。
    if route is not None and has_acted:
        $ add_affection(route, 10)
        $ add_fame_club(20)
    return


# ------------------------------------------------------------
# 结局
# ------------------------------------------------------------
label play_ending:
    $ resolve_ending()

    if ending == "rin_he":
        jump ending_rin_he
    elif ending == "rin_be":
        jump ending_rin_be
    elif ending == "yoko_he":
        jump ending_yoko_he
    elif ending == "yoko_be":
        jump ending_yoko_be
    elif ending == "songke_he":
        jump ending_songke_he
    elif ending == "songke_be":
        jump ending_songke_be

    jump ending_none


label game_end:
    python:
        rank_text = "默默无闻"
        if fame >= 3000:
            rank_text = "圈内传说"
        elif fame >= 1500:
            rank_text = "小有名气"
        elif fame >= 500:
            rank_text = "初露头角"

    p "这个学期结束了。"
    p "累计名气 [fame]，技艺值 [person_skill]，社团 [member_count] 人。"
    p "（评价：[rank_text]）"

    return
