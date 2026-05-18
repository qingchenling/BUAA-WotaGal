init python:
    import random
    #基础数值
    def add_fame(value):
        global fame
        fame += value


    def add_skill(value):
        global person_skill
        person_skill += value


    def add_member(value=1):
        global member_count
        member_count += value
        
    def next_week():
        global week
        week += 1    

    #剧情变量
    def unlock_yongman():
        global yongman_unlocked
        yongman_unlocked = True
    
    def practice_skill():
        """
        随机抽取一个技能，根据天气系数和难度增加熟练度。
        

        返回:
            tuple: (技能名称, 实际增加的熟练度)
        """
        global skill_pool
        global weathers
        global person_skill

        # 随机抽取一个技能
        skill = random.choice(skill_pool)
        skill_id = skill["id"]
        skill_name = skill["name"]
        difficulty = skill["difficulty"]
        
        weather = random.choice(weathers)
        weather_factor =weather["factor"]
        
        # 计算增量：基础值 * 天气系数 / 难度
        gain = int(person_skill * weather_factor / difficulty)
        if gain < 1:
            gain = 1  # 至少增加 1 点，避免没有增长
        
        # 更新熟练度，上限 100
        old_mastery = skill["mastery"]
        new_mastery = min(100, old_mastery + gain)
        actual_gain = new_mastery - old_mastery
        skill["mastery"] = new_mastery
        
        return skill_name, actual_gain



