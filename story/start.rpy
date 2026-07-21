
## Background

image BG practice_room = Placeholder("bg")
image BG sky = Placeholder("bg")
image BG school_gate = Placeholder("bg")
image BG BJOne = Placeholder("bg")



## Characters

define C_lin = Character("林若")
image Lin normal = Placeholder("boy")
image Lin surprise = Placeholder("boy")

define C_song = Character("宋柯")
image Song normal = Placeholder("boy")
image Song angry = Placeholder("boy")

define C_ye = Character("叶子")

define NPC_driver = Character("司机")
define NPC_senior = Character("学长")

## BGM

define BGM1 = ""
define BGM2 = ""
define BGM6 = "audio/bgm/bgm6.mp3"



## Sound

define Action = ""
define Run = ""



default Player_name = "player name"
define P = Character("[player_name]")



# 游戏在此开始。
label start:

    menu:
        "测试选择标题"

        "主线流程":
            jump W0

        "测试剧情":
            jump test

    return
