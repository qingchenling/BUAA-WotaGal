
#根据日期周期来的
label weekly_story_check:

    if week == 2:
        #call这里写第二周故事
        #call week2_story
        
        p"第二周了"
        p"确实是到了"
        p"第二周了"

    if week == 4:
        #call week4_story
        p"第四周了"

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
    "今天的幸运数字是 [lucky] ！"



    return