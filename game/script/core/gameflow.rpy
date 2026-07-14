#游戏流程规范
define p=Character("旁白")

label game_start:

    p"主角入校故事序章"

    jump week_loop


image map:
    "images/bg/map.png"
    zoom 1.5
label week_loop:
    
    scene map
    #这个在screens里

    p"我打算做什么呢？"
    call screen map_screen
    #这两个是story里
    call weekly_story_check

    call random_event_check
    call special_event_check
    p"主角入校故事序章"




    jump week_loop
