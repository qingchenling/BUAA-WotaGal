#这一块写不同地点触发的行为


label loc_practice:

    scene black

    p"你来到练习场地，开始今天的训练。"

    $ add_skill(3)
    $ add_fame(2)

    # 选取候选技能，提取到简单变量给菜单用
    $ skill_options = choose_skill()
    $ s0_name = skill_options[0]['name']
    $ s0_diff = skill_options[0]['difficulty']
    $ s0_mastery = skill_options[0]['mastery']
    $ s0_id   = skill_options[0]['id']
    $ s1_name = skill_options[1]['name']
    $ s1_diff = skill_options[1]['difficulty']
    $ s1_mastery = skill_options[1]['mastery']
    $ s1_id   = skill_options[1]['id']
    $ s2_name = skill_options[2]['name']
    $ s2_diff = skill_options[2]['difficulty']
    $ s2_mastery = skill_options[2]['mastery']
    $ s2_id   = skill_options[2]['id']

    menu:
        "要重点练习哪个技？"
        "[s0_name] (难度 [s0_diff], 熟练度 [s0_mastery])":
            $ chosen_id = s0_id
        "[s1_name] (难度 [s1_diff], 熟练度 [s1_mastery])":
            $ chosen_id = s1_id
        "[s2_name] (难度 [s2_diff], 熟练度 [s2_mastery])":
            $ chosen_id = s2_id

    $ skill_name, add_mastery = practice_skill(chosen_id)
    p"练习了[skill_name]，熟练度提高[add_mastery]"

    $ next_week()
    return