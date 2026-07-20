# 周常剧情 & 事件判定

# 周常剧情：根据 week 数字跳转到对应标签 w1~wN
label weekly_story_check:

    $ target_label = "w" + str(week)
    call expression target_label from _call_expression

    return

# 表演事件判定
label performance_event_check:

    if not is_performance_week():
        return

    if week == 5:
        call performance_week5 from _call_performance_week5
    elif week == 9:
        call performance_week9 from _call_performance_week9
    elif week == 14:
        call performance_week14 from _call_performance_week14
    elif week == 18:
        call performance_week18 from _call_performance_week18

    return

# 条件剧情
label special_event_check:

    if fame >= 10 and not has_first_stage:
        $ has_first_stage = True
        p"首次演出完成，名气开始积累……"

    return

# 日常随机事件
label random_event_check:
    $ lucky = renpy.random.randint(1, 100)
    p"今天的幸运数字是 [lucky] ！"

    return

# ============================================================
# 表演事件
# ============================================================
label performance_week5:
    $ gained = apply_performance_fame()
    p"第 5 周 —— 初期小演。"
    p"你在学院晚会上首次登台，虽然紧张，但光弧划破黑暗的一刻，一切都值了。"
    p"本次表演获得名气 [gained]！累计名气：[fame]。"
    return

label performance_week9:
    $ gained = apply_performance_fame()
    p"第 9 周 —— 中期汇演。"
    p"经过半个学期的磨炼，你的技艺有了长足进步。这次表演吸引了更多目光。"
    p"本次表演获得名气 [gained]！累计名气：[fame]。"
    return

label performance_week14:
    $ gained = apply_performance_fame()
    p"第 14 周 —— 后期主舞台。"
    p"期末的联合演出，是这学期最重要的舞台。你全力以赴。"
    p"本次表演获得名气 [gained]！累计名气：[fame]。"
    return

label performance_week18:
    $ gained = apply_performance_fame()
    p"第 18 周 —— 终演。"
    p"这是本学期最后一次登台。你回顾这一路走来，每一道光弧都在心中留下了不可磨灭的痕迹。"
    p"本次表演获得名气 [gained]！累计名气：[fame]。"
    return
