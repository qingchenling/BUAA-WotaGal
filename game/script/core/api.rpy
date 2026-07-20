init python:
    import random

    # ============================================================
    # 每周追踪重置
    # ============================================================
    def reset_weekly_tracking():
        global weekly_new_skills, weekly_picks, weekly_maxed_difficulty
        weekly_new_skills = 0
        weekly_picks = 0
        weekly_maxed_difficulty = []

    # ============================================================
    # 技能池初始化 / 重置
    # ============================================================
    def init_skill_pool():
        """深拷贝 SKILL_DEFS，附加 mastery 和 hidden_mastery 字段"""
        global skill_pool
        skill_pool = []
        for s in SKILL_DEFS:
            skill_pool.append(dict(
                id=s["id"],
                name=s["name"],
                difficulty=s["difficulty"],
                charm=s["charm"],
                mastery=0,
                hidden_mastery=0,
            ))

    def reset_game_state():
        """新周目重置所有数值（inherit_unlocked 时跳过）"""
        global person_skill, fame, skill_pool
        person_skill = PS_START
        fame = 0
        init_skill_pool()
        reset_weekly_tracking()

    # ============================================================
    # 选技数量
    # ============================================================
    def get_option_count(ps=None):
        """候选技总数"""
        if ps is None:
            ps = person_skill
        return OPTIONS_BASE + ps // OPTIONS_STEP

    def get_pick_count(ps=None):
        """每周可选次数"""
        if ps is None:
            ps = person_skill
        return min(MAX_PICKS, 1 + ps // PICKS_STEP)

    # ============================================================
    # 熟练度颜色
    # ============================================================
    def get_mastery_color(hidden):
        if hidden >= 300:
            return "#FFD700"  # 金色 造极
        elif hidden >= 200:
            return "#AA55FF"  # 紫色 登峰
        elif hidden >= 150:
            return "#00DDFF"  # 青色 入化
        elif hidden >= 100:
            return "#00FF88"  # 绿色 大成
        return "#FFFFFF"       # 白色

    def get_mastery_title(hidden):
        if hidden >= 300:
            return "造极"
        elif hidden >= 200:
            return "登峰"
        elif hidden >= 150:
            return "入化"
        elif hidden >= 100:
            return "大成"
        return ""

    # ============================================================
    # 熟练度增长公式
    # ============================================================
    def calc_mastery_gain(ps, difficulty, hidden_mastery):
        """
        双阶段衰减公式，返回本次练习的熟练度增量。
        阶段 1 (h ≤ 100): decay = 1.0 - MASTERY_DECAY_RATE * (h / 100)
        阶段 2 (h > 100): decay = 0.3 / (1 + overflow / OVERFLOW_DECAY_HALF)
        """
        effective = ps / PS_DIVISOR
        h = hidden_mastery

        if h <= 100:
            decay = 1.0 - MASTERY_DECAY_RATE * (h / 100.0)
        else:
            overflow = h - 100
            decay = 0.3 / (1.0 + overflow / float(OVERFLOW_DECAY_HALF))

        gain = int(effective * decay / difficulty)
        return max(1, gain)

    # ============================================================
    # 选技逻辑
    # ============================================================
    def choose_skills(ps=None):
        """
        返回 (options_list, picks)：
          options_list: 候选技列表，每个包含 id/name/difficulty/mastery/is_new
          picks: 本周可选次数
        已知技抽取权重 = max(1, 100 - mastery)
        """
        global skill_pool

        if ps is None:
            ps = person_skill

        option_count = get_option_count(ps)
        pick_count = get_pick_count(ps)

        known = [s for s in skill_pool if s["mastery"] > 0]
        unlearned = [s for s in skill_pool if s["mastery"] == 0]

        # 已知技：按权重取 KNOWN_SLOTS 个
        known_slots = min(KNOWN_SLOTS, len(known))
        known_chosen = []
        if known_slots > 0 and known:
            weights = [max(1, 100 - s["mastery"]) for s in known]
            total_w = sum(weights)
            # 无重复加权抽样
            temp_known = list(known)
            temp_weights = list(weights)
            for _ in range(known_slots):
                if not temp_known:
                    break
                r = random.uniform(0, sum(temp_weights))
                acc = 0
                for i, w in enumerate(temp_weights):
                    acc += w
                    if acc >= r:
                        known_chosen.append(temp_known.pop(i))
                        temp_weights.pop(i)
                        break

        # 新技：填满剩余槽位
        new_slots = option_count - len(known_chosen)
        new_slots = min(new_slots, len(unlearned))
        new_chosen = random.sample(unlearned, new_slots) if new_slots > 0 else []

        # 合并并打乱
        options = known_chosen + new_chosen
        random.shuffle(options)

        result = []
        for s in options:
            result.append({
                "id": s["id"],
                "name": s["name"],
                "difficulty": s["difficulty"],
                "mastery": s["mastery"],
                "hidden_mastery": s["hidden_mastery"],
                "is_new": s["mastery"] == 0,
            })

        return result, pick_count

    # ============================================================
    # 练习技能
    # ============================================================
    def practice_skill(skill_id):
        """
        练习指定技能，返回 (name, gain, just_maxed, difficulty)。
        just_maxed: hidden_mastery 首次达到 100 时为 True
        """
        global skill_pool, person_skill, weekly_new_skills, weekly_picks, weekly_maxed_difficulty

        skill = next((s for s in skill_pool if s["id"] == skill_id), None)
        if skill is None:
            return ("", 0, False, 0)

        was_new = skill["mastery"] == 0
        old_hidden = skill["hidden_mastery"]

        gain = calc_mastery_gain(person_skill, skill["difficulty"], old_hidden)
        new_hidden = old_hidden + gain

        skill["hidden_mastery"] = new_hidden
        skill["mastery"] = min(MASTERY_DISPLAY_MAX, new_hidden)

        # 追踪
        weekly_picks += 1
        if was_new:
            weekly_new_skills += 1

        just_maxed = old_hidden < 100 and new_hidden >= 100
        if just_maxed:
            weekly_maxed_difficulty.append(skill["difficulty"])

        return (skill["name"], gain, just_maxed, skill["difficulty"])

    # ============================================================
    # 技艺值周结算
    # ============================================================
    def get_maxed_bonus(difficulty):
        if difficulty == 3:
            return PS_MAX_BONUS_D3
        elif difficulty == 2:
            return PS_MAX_BONUS_D2
        return PS_MAX_BONUS_D1

    def apply_weekly_ps():
        """结算本周技艺值增长"""
        global person_skill, weekly_new_skills, weekly_picks, weekly_maxed_difficulty

        ps_gain = 0
        ps_gain += weekly_new_skills * PS_GAIN_NEW_SKILL
        ps_gain += weekly_picks * PS_GAIN_PER_PRACTICE
        for diff in weekly_maxed_difficulty:
            ps_gain += get_maxed_bonus(diff)

        person_skill = min(PS_MAX, person_skill + ps_gain)

        # 重置周追踪
        reset_weekly_tracking()
        return ps_gain

    # ============================================================
    # 名气系统
    # ============================================================
    def calc_performance_fame():
        """
        计算当前所有技能产生的单次表演名气。
        fame = Σ charm × (hidden_mastery / 10)^2
        """
        global skill_pool
        total = 0
        for s in skill_pool:
            if s["hidden_mastery"] > 0:
                total += s["charm"] * (s["hidden_mastery"] / 10.0) ** 2
        return int(total)

    def apply_performance_fame():
        """执行表演：计算名气并累加到 fame"""
        global fame
        gained = calc_performance_fame()
        fame += gained
        return gained

    # ============================================================
    # 作弊码
    # ============================================================
    def toggle_inherit():
        global inherit_unlocked
        inherit_unlocked = not inherit_unlocked
        return inherit_unlocked

    # ============================================================
    # 周推进
    # ============================================================
    def next_week():
        global week
        week += 1

    def is_performance_week(w=None):
        if w is None:
            w = week
        return w in PERFORMANCE_WEEKS

    def is_game_over():
        return week >= TOTAL_WEEKS

    # ============================================================
    # 剧情变量
    # ============================================================
    def add_member(value=1):
        global member_count
        member_count += value

    def unlock_yongman():
        global yongman_unlocked
        yongman_unlocked = True
