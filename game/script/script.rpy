# 角色常量
define p = Character(None)
define l = Character("林若")
define s = Character("宋柯")
define w = Character("我")
define y = Character("叶子")
define n = Character("夜凪")
define h = Character("灰白")

image lawn:
    "images/bg/lawn.png"
    zoom 1.5

image danceroom:
    "images/bg/danceroom.png"
    zoom 1.5

image skymirror1:
    "images/bg/skymirror.png"
    zoom 1.5

label start:
    scene danceroom

    l"你在看什么？歇了这么久？帮我磨一下这个莉莉丝吧。"
    s "……。"
    l"……嗯？"
    s"……………………我打算……退出宅艺研了。"
    l"你让我冷静一下。"
    l"……这个…是什么……恶作剧吗？"
    l"上次的爬台吗？不就是因为咱们技艺不行，所以才得赶紧来多加练啊！"
    s"够了！你技练的再好有什么用？"
    s"这种幼稚活动到底哪里好玩了？"
    s"我从没觉得打艺开心过！"
    l"你在说什么？你明明——"
    s"就这样吧。"

    jump game_start

label game_start:
    # 初始化 / 继承数值
    if not inherit_unlocked or len(skill_pool) == 0:
        $ reset_game_state()
    else:
        $ reset_weekly_tracking()

    scene danceroom
    w"……"
    w"……嗯？"
    y"快到了，起来吧。"
    p"我猛地坐起来。"

    jump week_loop
