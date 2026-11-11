# 周常剧情 & 事件判定
#
# 周剧本查找顺序：
#   1. w{week}_{route}   例：w12_rin —— 个人线专用
#   2. w{week}           例：w12      —— 共通 / 兜底
#   3. week_filler       都没有时用一段过场，保证不崩
#
# 写个人线时只需要新建 w11_rin.rpy 这样的文件，不用改流程。

label weekly_story_check:

    python:
        _target = None
        if route is not None:
            _cand = "w%d_%s" % (week, route)
            if renpy.has_label(_cand):
                _target = _cand
        if _target is None:
            _cand = "w%d" % week
            if renpy.has_label(_cand):
                _target = _cand

    if _target:
        call expression _target from _call_weekly_story
    else:
        call week_filler from _call_week_filler

    return


label week_filler:
    p "这一周过得很快。练习、上课、社团，日子在重复里往前挪。"
    return


# ============================================================
# 表演事件
# ============================================================
label performance_event_check:

    if not is_performance_week():
        return

    if week == 5:
        call performance_week5 from _call_performance_week5
    elif week == 9:
        call performance_week9 from _call_performance_week9
    elif week == 14:
        call performance_week14 from _call_performance_week14

    return


label performance_week5:
    $ gained = apply_performance_fame()
    p "第 5 周 —— 初期小演。"
    p "你在学院晚会上首次登台，虽然紧张，但光弧划破黑暗的一刻，一切都值了。"
    p "本次表演获得名气 [gained]！累计名气：[fame]。"
    return


label performance_week9:
    $ gained = apply_performance_fame()
    p "第 9 周 —— 中期汇演。"
    p "经过半个学期的磨炼，你的技艺有了长足进步。这次表演吸引了更多目光。"
    p "本次表演获得名气 [gained]！累计名气：[fame]。"
    return


label performance_week14:
    $ gained = apply_performance_fame()
    p "第 14 周 —— 后期主舞台。"
    p "期末的联合演出，是这学期最重要的舞台。你全力以赴。"
    p "本次表演获得名气 [gained]！累计名气：[fame]。"
    return


# 终演放在结局卷里，见 route.rpy / story/endings.rpy
label performance_week18:
    $ gained = apply_performance_fame()
    p "第 18 周 —— 终演。"
    p "这是本学期最后一次登台。"
    p "本次表演获得名气 [gained]！累计名气：[fame]。"
    return


# ============================================================
# 条件剧情
# ============================================================
label special_event_check:

    if fame >= 10 and not has_first_stage:
        $ has_first_stage = True
        p "首次演出完成，名气开始积累……"

    # 通往个人线的入口：走到 W10 还没有进线，说明剧本没接上
    if week == COMMON_ROUTE_END and route is None:
        p "（共通线到这里为止，下一周进入个人线。）"

    return


# ============================================================
# 日常随机事件：低概率的小插曲，不影响主线
# ============================================================
label random_event_check:

    $ _roll = renpy.random.randint(1, 100)
    if _roll <= 15:
        call random_event_pool from _call_random_event_pool

    return


label random_event_pool:
    $ _pick = renpy.random.randint(1, 3)
    if _pick == 1:
        p "练习结束，有人把喝剩的半瓶水忘在窗台上，瓶子被暖气烘得发烫。"
    elif _pick == 2:
        p "楼下有人练到很晚，光弧隔着玻璃一晃一晃，像有人在窗外打信号。"
    else:
        p "你在储物间翻到一根用旧的电棒，握把上缠的胶带已经发黄。"
    return
