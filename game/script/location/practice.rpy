#这一块写不同地点触发的行为


label loc_practice:

    scene black

    "你练习了一整天。"
    #基础数值变化
    
    #这里后面要改为技能池经验点吗?感觉选择很多
    $ add_skill(3)
    #这里感觉要取决于地点，主要zhi
    $ add_fame(2)
    $ skill_name, add_mastery = practice_skill()
    "练习了[skill_name],熟练度提高[add_mastery]"

    $ next_week()
    return