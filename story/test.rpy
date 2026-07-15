image bg bg1 = Placeholder("bg")
image bg bg2 = Placeholder("bg")
image bg bg3 = Placeholder("bg")
image bg bg4 = Placeholder("bg")

define C_a = Character("人物 A")
image a normal = Placeholder("girl")
image a happy = Placeholder("girl")
image a sad = Placeholder("girl")
image a angry = Placeholder("girl")

define C_b = Character("人物 B")
image b normal = Placeholder("boy")
image b happy = Placeholder("boy")
image b sad = Placeholder("boy")
image b angry = Placeholder("boy")

define N_a = Character("NPC A")

define player_name = "player"
define P = Character("[player_name]")

label test:

    "Test 1: 背景切换"

    scene black

    scene white

    scene red

    "夹杂对话"

    scene yellow

    C_a "人物说话"

    scene black with fade

    "切换动画"

    scene bg bg1 with fade

    "Test 2"

    "这是旁白"

    show a normal at left

    C_a "A say"

    show b normal at right

    C_b "B say"

    C_b "B continue"

    "Test 3：立绘切换"

    show a happy

    C_a "开心。"

    show a sad

    C_a "伤心。"

    show a angry

    C_a "生气。"

    show b happy

    C_b "我也有表情。"

    "Test 4：立绘隐藏"

    hide a with dissolve

    C_b "A 消失了。"

    hide b with dissolve

    "现在屏幕上没人。"

    "Test 5：玩家输入"

    $ player_name = renpy.input(
        "请输入名字：",
        default="玩家",
        length=12
    )

    $ player_name = player_name.strip()

    if player_name == "":
        $ player_name = "玩家"

    P "原来我叫 [player_name]。"

    "Test 6：菜单"

    menu:

        "选项一":

            P "你选择了选项一。"

        "选项二":

            P "你选择了选项二。"

        "选项三":

            P "你选择了选项三。"

    "Test 7：变量"

    $ favor = 0

    menu:

        "增加好感":

            $ favor += 1

        "减少好感":

            $ favor -= 1

    if favor > 0:

        C_a "好感增加。"

    else:

        C_a "好感减少。"

    "Test 8：音效"

    play sound "audio/click.ogg"

    "播放了一次音效。"

    "Test 9：BGM"

    play music "audio/bgm.ogg" fadein 1.0

    P "背景音乐开始。"

    stop music fadeout 1.0

    "音乐停止。"

    "Test 10：时间跳转"

    scene black with Fade(0.5, 1.0, 0.5)

    centered "三天后"

    scene bg bg2 with dissolve

    "Test 11：跳转"

    menu:

        "Good End":

            jump test_good

        "Bad End":

            jump test_bad
