# 游戏全局变量存储
# 所有变量用 default 定义（可存档），常量用 define 定义（不可变）
# 变量修改方法集中在 api.rpy

# ============================================================
# 基础常量
# ============================================================
define PS_START = 100
define PS_MAX = 1000
define PS_DIVISOR = 6
define MASTERY_DISPLAY_MAX = 100
define MASTERY_DECAY_RATE = 0.7
define OVERFLOW_DECAY_HALF = 100
define MASTERY_HIDDEN_SOFT_CAP = 500

# 技艺值增长
define PS_GAIN_NEW_SKILL = 25
define PS_GAIN_PER_PRACTICE = 10
define PS_MAX_BONUS_D1 = 20
define PS_MAX_BONUS_D2 = 40
define PS_MAX_BONUS_D3 = 80

# 选技机制
define KNOWN_SLOTS = 2
define OPTIONS_BASE = 3
define OPTIONS_STEP = 200
define PICKS_STEP = 200
define MAX_PICKS = 3

# 表演（W18 之后进入结局卷，不再走日常循环）
define PERFORMANCE_WEEKS = [5, 9, 14]

# 时间轴节点
define COMMON_ROUTE_END = 10    # 共通线最后一整周（W10）
define ROUTE_SPLIT_WEEK = 11    # W11 开场选线
define FINAL_CHOICE_WEEK = 17   # W17 最终选择（HE / BE）
define ENDING_WEEK = 18         # W18 起进入结局卷，覆盖 W18-W20
define TOTAL_WEEKS = 21         # W0-W20 共 21 周

# 天气值（常数）
define weathers = [
    {"id": 1, "factor": 1,   "name": "凉爽的夜晚"},
    {"id": 2, "factor": 0.2, "name": "阴雨的夜晚"},
]

# ============================================================
# 技能定义（60个，恒定不变）
# ============================================================
define SKILL_DEFS = [
    # d1 基础技 (25个)
    {"id": 1,  "name": "OAD",       "difficulty": 1, "charm": 2},
    {"id": 2,  "name": "羅刹",      "difficulty": 1, "charm": 2},
    {"id": 3,  "name": "月光",      "difficulty": 1, "charm": 2},
    {"id": 4,  "name": "流星",      "difficulty": 1, "charm": 2},
    {"id": 5,  "name": "飛燕",      "difficulty": 1, "charm": 2},
    {"id": 6,  "name": "桜花",      "difficulty": 1, "charm": 3},
    {"id": 7,  "name": "疾風",      "difficulty": 1, "charm": 2},
    {"id": 8,  "name": "閃光",      "difficulty": 1, "charm": 3},
    {"id": 9,  "name": "流水",      "difficulty": 1, "charm": 2},
    {"id": 10, "name": "明星",      "difficulty": 1, "charm": 2},
    {"id": 11, "name": "旋風",      "difficulty": 1, "charm": 2},
    {"id": 12, "name": "光刃",      "difficulty": 1, "charm": 2},
    {"id": 13, "name": "飛翔",      "difficulty": 1, "charm": 3},
    {"id": 14, "name": "白夜",      "difficulty": 1, "charm": 2},
    {"id": 15, "name": "蒼界",      "difficulty": 1, "charm": 2},
    {"id": 16, "name": "翠嵐",      "difficulty": 1, "charm": 2},
    {"id": 17, "name": "紅蓮",      "difficulty": 1, "charm": 3},
    {"id": 18, "name": "雷光",      "difficulty": 1, "charm": 2},
    {"id": 19, "name": "氷刃",      "difficulty": 1, "charm": 2},
    {"id": 20, "name": "烈火",      "difficulty": 1, "charm": 3},
    {"id": 21, "name": "雷蛇",      "difficulty": 1, "charm": 3},
    {"id": 22, "name": "暁",        "difficulty": 1, "charm": 2},
    {"id": 23, "name": "宵闇",      "difficulty": 1, "charm": 2},
    {"id": 24, "name": "蛍火",      "difficulty": 1, "charm": 3},
    {"id": 25, "name": "陽炎",      "difficulty": 1, "charm": 2},

    # d2 进阶技 (25个)
    {"id": 26, "name": "烈剣",      "difficulty": 2, "charm": 3},
    {"id": 27, "name": "金剛",      "difficulty": 2, "charm": 3},
    {"id": 28, "name": "残像",      "difficulty": 2, "charm": 3},
    {"id": 29, "name": "刹那",      "difficulty": 2, "charm": 3},
    {"id": 30, "name": "無明",      "difficulty": 2, "charm": 3},
    {"id": 31, "name": "斬月",      "difficulty": 2, "charm": 4},
    {"id": 32, "name": "紫電",      "difficulty": 2, "charm": 3},
    {"id": 33, "name": "焔",        "difficulty": 2, "charm": 4},
    {"id": 34, "name": "不知火",    "difficulty": 2, "charm": 3},
    {"id": 35, "name": "神楽",      "difficulty": 2, "charm": 4},
    {"id": 36, "name": "千鳥",      "difficulty": 2, "charm": 3},
    {"id": 37, "name": "不知火改",  "difficulty": 2, "charm": 4},
    {"id": 38, "name": "朧",        "difficulty": 2, "charm": 3},
    {"id": 39, "name": "刹那改",    "difficulty": 2, "charm": 4},
    {"id": 40, "name": "飛天",      "difficulty": 2, "charm": 3},
    {"id": 41, "name": "桜花乱舞",  "difficulty": 2, "charm": 4},
    {"id": 42, "name": "羅刹改",    "difficulty": 2, "charm": 3},
    {"id": 43, "name": "雷神",      "difficulty": 2, "charm": 4},
    {"id": 44, "name": "氷嵐",      "difficulty": 2, "charm": 3},
    {"id": 45, "name": "残月",      "difficulty": 2, "charm": 4},
    {"id": 46, "name": "幻日",      "difficulty": 2, "charm": 3},
    {"id": 47, "name": "螺旋",      "difficulty": 2, "charm": 4},
    {"id": 48, "name": "天輪",      "difficulty": 2, "charm": 3},
    {"id": 49, "name": "月影",      "difficulty": 2, "charm": 4},
    {"id": 50, "name": "破軍",      "difficulty": 2, "charm": 3},

    # d3 高阶技 (10个)
    {"id": 51, "name": "天照",      "difficulty": 3, "charm": 5},
    {"id": 52, "name": "月読",      "difficulty": 3, "charm": 5},
    {"id": 53, "name": "須佐之男",  "difficulty": 3, "charm": 6},
    {"id": 54, "name": "伊邪那美",  "difficulty": 3, "charm": 5},
    {"id": 55, "name": "迦具土",    "difficulty": 3, "charm": 6},
    {"id": 56, "name": "八咫烏",    "difficulty": 3, "charm": 5},
    {"id": 57, "name": "神威",      "difficulty": 3, "charm": 6},
    {"id": 58, "name": "荒覇吐",    "difficulty": 3, "charm": 5},
    {"id": 59, "name": "経津主",    "difficulty": 3, "charm": 6},
    {"id": 60, "name": "布都御魂",  "difficulty": 3, "charm": 7},
]

# ============================================================
# 运行时变量（可存档）
# ============================================================
default week = 0
default fame = 0
default person_skill = PS_START
default skill_pool = []
default inherit_unlocked = False

# 地图锁
default shahe_unlocked = True
default yongman_unlocked = False

# 团体线
default member_count = 2

# 个人线
default has_recruited = False
default has_first_stage = False

# ============================================================
# 路线系统
# ============================================================
# route：None = 共通线，"rin" 林若 / "yoko" 叶子 / "songke" 宋柯
default route = None
default route_label = "共通线"   # 给界面显示用，随 route 同步
default final_choice = None      # None / "he" / "be"
default ending = None            # 结算后的结局标识

# 好感与知名度
default affection_rin = 0
default affection_yoko = 0
default fame_club = 0            # 圈内知名度（宋柯线 HE 条件）

# 路线关键事件旗标
default flag_co_choreo = False    # 林若线：共同编舞
default flag_record_reply = False # 叶子线：记录与回应
default flag_light_sync = False   # 宋柯线：灯光同步试验

# 本周行动状态
default has_acted = False

# 结局面板用的临时显示变量
default rank_text = ""

# 本周练习追踪（每次练习重置）
default weekly_new_skills = 0
default weekly_picks = 0
default weekly_maxed_difficulty = []
