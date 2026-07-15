
image bg practice_room = Placeholder("bg")
image bg sky = Placeholder("bg")

define C_lin = Character("林若")
image lin normal = Placeholder("boy")
image lin surprise = Placeholder("boy")

define C_song = Character("宋柯")
image song normal = Placeholder("boy")
image song angry = Placeholder("boy")

default player_name = "player name"

define P = Character("[player_name]")

label W0:

    scene bg practice_room

    show song normal at left

    show lin normal at right

    C_lin "你在看什么？歇了这么久？帮我磨一下这个莉莉丝吧。"

    C_song "……"

    C_lin "……嗯？"

    C_song "……………………我打算……退出宅艺研了。"
    C_song "你让我冷静一下。"

    show lin surprise

    C_lin "……这个…是什么……恶作剧吗？"
    C_lin "次的爬台吗？不就是因为咱们技艺不行，所以才得赶紧来多加练啊！"

    show song angry

    C_song "够了！你技练的再好有什么用？"
    C_song "这种唐氏活动到底哪里好玩了？"
    C_song "我从没觉得打艺开心过！"

    hide song with dissolve

    C_lin "啊…"

    show lin normal

    C_lin "…………………"

    scene bg sky with fade

    $ player_name = renpy.input("请输入你的名字：")
    $ player_name = player_name.strip()

    P "……嗯？"

    P "竟然没有做完"


    return
