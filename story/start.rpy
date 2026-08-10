
## Background

# 咏曼剧场
image BG yongman = Placeholder("bg")
image BG practice_room = Placeholder("bg")
image BG sky = Placeholder("bg")
image BG school_gate = Placeholder("bg")
image BG BJOne = Placeholder("bg")



## Characters

define C_lin = Character("林若")
image Lin normal = Placeholder("girl")
image Lin surprise = Placeholder("girl")
image Lin serious = Placeholder("girl")
image Lin relax = Placeholder("girl")

define C_song = Character("宋柯")
image Song normal = Placeholder("boy")
image Song angry = Placeholder("boy")

define C_ye = Character("叶子")

define NPC_driver = Character("司机")
define NPC_senior = Character("学长")



## BGM

define BGM1 = ""
define BGM2 = ""
define BGM5 = ""
define BGM6 = "audio/bgm/bgm6.mp3"



## Sound

define Action = ""
define Run = ""



default Player_name = "player name"
define P = Character("[player_name]")



# 游戏在此开始。
label start:

    if persistent.secondPlay == 0:
        "光不会熄灭。"
        "只要还有人记得它划过的痕迹，"
        "只要还有人曾在那道光里并肩过——"
        "焲痕就在，羁绊就在。"
    else:
        "凡曾见过那道光的人，"
        "不会真正离散。"
        "他们只是散落在不同的时间里，"
        "等待——"
        "在下一个春天，重新亮起。"
    
    jump W0

    return
