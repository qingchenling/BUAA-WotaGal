# 游戏流程控制

image map:
    "images/bg/map.png"
    zoom 1.5

label week_loop:

    scene map

    p"我打算做什么呢？"
    call screen map_screen

    # 周常剧情
    call weekly_story_check from _call_weekly_story_check
    call performance_event_check from _call_performance_event_check
    call random_event_check from _call_random_event_check
    call special_event_check from _call_special_event_check

    # 游戏结束判定
    if is_game_over():
        jump game_end

    jump week_loop

label game_end:
    p"这个学期结束了。"
    p"累计名气：[fame]，技艺值：[person_skill]。"
    return
