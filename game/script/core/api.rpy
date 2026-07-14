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

    def choose_skill(count=None):
        """
        从技能池中无重复随机选取指定数量的技能，供玩家选择练习哪个。

        参数:
            count: 选取数量，默认使用 practice_skill_number

        返回:
            list[dict]: 每个技能包含 id, name, difficulty
        """
        global skill_pool
        global practice_skill_number
        if count is None:
            count = practice_skill_number
        count = min(count, len(skill_pool))
        chosen = random.sample(skill_pool, count)
        return [
            {"id": s["id"], "name": s["name"], "difficulty": s["difficulty"], "mastery": s["mastery"]}
            for s in chosen
        ]


    def practice_skill(skill_id=None):
        """
        练习指定技能（或随机技能），根据天气系数和人物技艺增加熟练度。

        参数:
            skill_id: 要练习的技能 id，为 None 时随机选取

        返回:
            tuple: (技能名称, 实际增加的熟练度)
        """
        global skill_pool
        global weathers
        global person_skill

        if skill_id is not None:
            skill = next((s for s in skill_pool if s["id"] == skill_id), None)
            if skill is None:
                return "", 0
        else:
            skill = random.choice(skill_pool)

        skill_name = skill["name"]
        difficulty = skill["difficulty"]

        weather = random.choice(weathers)
        weather_factor = weather["factor"]

        gain = int(person_skill * weather_factor / difficulty)
        if gain < 1:
            gain = 1

        old_mastery = skill["mastery"]
        new_mastery = min(100, old_mastery + gain)
        actual_gain = new_mastery - old_mastery
        skill["mastery"] = new_mastery

        return skill_name, actual_gain



