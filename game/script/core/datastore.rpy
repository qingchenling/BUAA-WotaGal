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
# 技名取自 中文WOTA艺wiki（wotagei.huijiwiki.com）分类:技。
# 难度分档依据：門系/村正/蛇系等基础技为 d1；派生、复合、双持类为 d2；奥义、多段终结技为 d3。
define SKILL_DEFS = [
    # d1 基础技 (25个)
    {"id": 1,  "name": "OAD",      "difficulty": 1, "charm": 2},
    {"id": 2,  "name": "罗曼斯",    "difficulty": 1, "charm": 3},
    {"id": 3,  "name": "十字架",    "difficulty": 1, "charm": 2},
    {"id": 4,  "name": "雷蛇",      "difficulty": 1, "charm": 3},
    {"id": 5,  "name": "白门",      "difficulty": 1, "charm": 2},
    {"id": 6,  "name": "赤门",      "difficulty": 1, "charm": 2},
    {"id": 7,  "name": "虎之门",    "difficulty": 1, "charm": 3},
    {"id": 8,  "name": "半藏门",    "difficulty": 1, "charm": 2},
    {"id": 9,  "name": "光化门",    "difficulty": 1, "charm": 3},
    {"id": 10, "name": "仁王门",    "difficulty": 1, "charm": 2},
    {"id": 11, "name": "守礼门",    "difficulty": 1, "charm": 2},
    {"id": 12, "name": "长安门",    "difficulty": 1, "charm": 3},
    {"id": 13, "name": "村正",      "difficulty": 1, "charm": 3},
    {"id": 14, "name": "村雨",      "difficulty": 1, "charm": 2},
    {"id": 15, "name": "天照",      "difficulty": 1, "charm": 3},
    {"id": 16, "name": "天翔",      "difficulty": 1, "charm": 2},
    {"id": 17, "name": "天空兜",    "difficulty": 1, "charm": 2},
    {"id": 18, "name": "青雀",      "difficulty": 1, "charm": 3},
    {"id": 19, "name": "红",        "difficulty": 1, "charm": 2},
    {"id": 20, "name": "苍",        "difficulty": 1, "charm": 2},
    {"id": 21, "name": "初春",      "difficulty": 1, "charm": 3},
    {"id": 22, "name": "谷雨",      "difficulty": 1, "charm": 2},
    {"id": 23, "name": "流水加速",  "difficulty": 1, "charm": 2},
    {"id": 24, "name": "矢波",      "difficulty": 1, "charm": 3},
    {"id": 25, "name": "式波",      "difficulty": 1, "charm": 2},

    # d2 进阶技 (25个)
    {"id": 26, "name": "鹤望兰",    "difficulty": 2, "charm": 5},
    {"id": 27, "name": "胡蝶刃",    "difficulty": 2, "charm": 4},
    {"id": 28, "name": "苍月剑",    "difficulty": 2, "charm": 5},
    {"id": 29, "name": "虚闪·握",   "difficulty": 2, "charm": 4},
    {"id": 30, "name": "十拳剑",    "difficulty": 2, "charm": 5},
    {"id": 31, "name": "千鸟",      "difficulty": 2, "charm": 4},
    {"id": 32, "name": "白千鸟",    "difficulty": 2, "charm": 5},
    {"id": 33, "name": "二羽蝶",    "difficulty": 2, "charm": 4},
    {"id": 34, "name": "二羽鹤",    "difficulty": 2, "charm": 4},
    {"id": 35, "name": "月华门",    "difficulty": 2, "charm": 4},
    {"id": 36, "name": "应天门",    "difficulty": 2, "charm": 5},
    {"id": 37, "name": "焰狱门",    "difficulty": 2, "charm": 4},
    {"id": 38, "name": "霞门",      "difficulty": 2, "charm": 4},
    {"id": 39, "name": "樱田门",    "difficulty": 2, "charm": 5},
    {"id": 40, "name": "不知火蛇",  "difficulty": 2, "charm": 4},
    {"id": 41, "name": "吹雪蛇",    "difficulty": 2, "charm": 5},
    {"id": 42, "name": "春风蛇",    "difficulty": 2, "charm": 4},
    {"id": 43, "name": "黑蝶蛇",    "difficulty": 2, "charm": 4},
    {"id": 44, "name": "鬼人蛇",    "difficulty": 2, "charm": 5},
    {"id": 45, "name": "超重力蛇",  "difficulty": 2, "charm": 5},
    {"id": 46, "name": "闪电蛇",    "difficulty": 2, "charm": 4},
    {"id": 47, "name": "流星蛇",    "difficulty": 2, "charm": 5},
    {"id": 48, "name": "双剑蛇",    "difficulty": 2, "charm": 5},
    {"id": 49, "name": "JK蛇",      "difficulty": 2, "charm": 4},
    {"id": 50, "name": "羚黄泉",    "difficulty": 2, "charm": 5},

    # d3 高阶技 (10个)
    {"id": 51, "name": "八雷神",        "difficulty": 3, "charm": 7},
    {"id": 52, "name": "伏魔御厨子",    "difficulty": 3, "charm": 6},
    {"id": 53, "name": "乖离剑",        "difficulty": 3, "charm": 6},
    {"id": 54, "name": "王虚之闪光",    "difficulty": 3, "charm": 7},
    {"id": 55, "name": "王虚·破",       "difficulty": 3, "charm": 7},
    {"id": 56, "name": "重奏虚闪",      "difficulty": 3, "charm": 6},
    {"id": 57, "name": "天地无双刀",    "difficulty": 3, "charm": 6},
    {"id": 58, "name": "唯我独尊",      "difficulty": 3, "charm": 7},
    {"id": 59, "name": "万象圣堂",      "difficulty": 3, "charm": 6},
    {"id": 60, "name": "神威灵装·十番", "difficulty": 3, "charm": 7},
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
