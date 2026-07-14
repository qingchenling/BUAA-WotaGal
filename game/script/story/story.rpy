# 游戏的脚本可置于此文件中。

# 声明此游戏使用的角色。颜色参数可使角色姓名着色。



#角色常量
define p = Character(None)
define l =Character("林若")
define s = Character("宋柯")
define w =Character("我")
define y = Character("叶子")
define n = Character("夜凪")
define h = Character("灰白")

image lawn:
    "images/bg/lawn.png"
    zoom 1.5
# 游戏在此开始。
image danceroom:
    "images/bg/danceroom.png"
    zoom 1.5
# 游戏在此开始。
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
    scene danceroom
    w"……"
    w"……嗯？"
    y"快到了，起来吧。"
    p"我猛地坐起来。"


    jump week_loop
   
# label map:
#根据日期周期来的
label weekly_story_check:

    $ target_label = "w" + str(week)
    call expression target_label


    return


#条件剧情
label special_event_check:

    if fame >= 10 and not has_first_stage:

        $ has_first_stage = True

        #call event_first_show
        p"开始演出"
    return

    

#占个位，主要写一下日常的插科打诨
label random_event_check:
    $ lucky = random.randint(1, 100)
    p"今天的幸运数字是 [lucky] ！"



    return