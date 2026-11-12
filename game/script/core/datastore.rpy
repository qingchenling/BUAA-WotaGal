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

# 熟练度称号门槛（判定基于隐藏值；面板显示仍封顶 100）
define MASTERY_TIER_GREEN = 50    # 熟练
define MASTERY_TIER_CYAN = 100    # 大成（同时触发技艺值奖励）
define MASTERY_TIER_PURPLE = 160  # 登峰
define MASTERY_TIER_GOLD = 220    # 造极

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

# 技能池分级开放：早期只出基础技，逐段放开
define TIER2_WEEK = 4    # 第 4 周起开放 d2
define TIER3_WEEK = 10   # 第 10 周起开放 d3

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
# 技名与人数取自社团技表《焲痕技表.xlsx》，缺额用中文WOTA艺wiki的高阶技补齐。
# 难度规则：会的人越多越基础（top25 → d1，中间25 → d2，最冷门2个 + wiki 8个 → d3）。
# 魅力规则：d1/d2/d3 底值 2/4/6，火把类 +2（对圈外人更亮眼）。
# 技名与人数取自社团技表《焲痕技表.xlsx》，缺额用中文WOTA艺wiki的高阶技补齐。
# 难度规则：会的人越多越基础（top25 → d1，中间25 → d2，最冷门2个 + wiki 8个 → d3）。
# 魅力规则：d1/d2/d3 底值 2/4/6，火把类 +2（对圈外人更亮眼）。
# 技名与人数取自社团技表《焲痕技表.xlsx》，缺额用中文WOTA艺wiki的高阶技补齐。
# 难度规则：会的人越多越基础（top25 → d1，中间25 → d2，最冷门2个 + wiki 8个 → d3）。
# 魅力规则：d1/d2/d3 底值 2/4/6，火把类 +2（对圈外人更亮眼）。
# 技名与人数取自社团技表《焲痕技表.xlsx》，缺额用中文WOTA艺wiki的高阶技补齐。
# 难度规则：会的人越多越基础（top25 → d1，中间25 → d2，最冷门2个 + wiki 8个 → d3）。
# 魅力规则：d1/d2/d3 底值 2/4/6，火把类 +2（对圈外人更亮眼）。
define SKILL_DEFS = [
    # d1 基础技
    {"id":  1, "name": "嘘月",          "difficulty": 1, "charm": 4},  # 会7人
    {"id":  2, "name": "天照",          "difficulty": 1, "charm": 2},  # 会7人
    {"id":  3, "name": "月读",          "difficulty": 1, "charm": 2},  # 会7人
    {"id":  4, "name": "村正",          "difficulty": 1, "charm": 2},  # 会7人
    {"id":  5, "name": "樱华",          "difficulty": 1, "charm": 2},  # 会7人
    {"id":  6, "name": "水仙夫人",      "difficulty": 1, "charm": 2},  # 会7人
    {"id":  7, "name": "消力",          "difficulty": 1, "charm": 2},  # 会7人
    {"id":  8, "name": "烈剑",          "difficulty": 1, "charm": 2},  # 会7人
    {"id":  9, "name": "烈火舞",        "difficulty": 1, "charm": 4},  # 会7人
    {"id": 10, "name": "金刚",          "difficulty": 1, "charm": 2},  # 会7人
    {"id": 11, "name": "镇魂曲",        "difficulty": 1, "charm": 2},  # 会7人
    {"id": 12, "name": "雷蛇",          "difficulty": 1, "charm": 2},  # 会7人
    {"id": 13, "name": "青雀",          "difficulty": 1, "charm": 2},  # 会7人
    {"id": 14, "name": "龙击剑",        "difficulty": 1, "charm": 4},  # 会6人
    {"id": 15, "name": "不知火",        "difficulty": 1, "charm": 4},  # 会5人
    {"id": 16, "name": "娜露梅亚",      "difficulty": 1, "charm": 4},  # 会5人
    {"id": 17, "name": "圣白莲",        "difficulty": 1, "charm": 4},  # 会4人
    {"id": 18, "name": "旋空弧月",      "difficulty": 1, "charm": 2},  # 会4人
    {"id": 19, "name": "九吹雪",        "difficulty": 1, "charm": 2},  # 会3人
    {"id": 20, "name": "仙女座",        "difficulty": 1, "charm": 2},  # 会3人
    {"id": 21, "name": "北航拳",        "difficulty": 1, "charm": 2},  # 会3人
    {"id": 22, "name": "洛水天依",      "difficulty": 1, "charm": 4},  # 会3人
    {"id": 23, "name": "逆抚",          "difficulty": 1, "charm": 4},  # 会3人
    {"id": 24, "name": "宝石天照",      "difficulty": 1, "charm": 2},  # 会2人
    {"id": 25, "name": "天元ノ斩",      "difficulty": 1, "charm": 4},  # 会2人

    # d2 进阶技
    {"id": 26, "name": "十拳剑·鲜血",  "difficulty": 2, "charm": 4},  # 会2人
    {"id": 27, "name": "和歌鸢舞",      "difficulty": 2, "charm": 6},  # 会2人
    {"id": 28, "name": "凤凰之舞",      "difficulty": 2, "charm": 6},  # 会2人
    {"id": 29, "name": "昭和四十七门",  "difficulty": 2, "charm": 4},  # 会2人
    {"id": 30, "name": "煌刀",          "difficulty": 2, "charm": 6},  # 会2人
    {"id": 31, "name": "神代樱",        "difficulty": 2, "charm": 4},  # 会2人
    {"id": 32, "name": "行界阵",        "difficulty": 2, "charm": 6},  # 会2人
    {"id": 33, "name": "ロトの纹章",    "difficulty": 2, "charm": 4},  # 会1人
    {"id": 34, "name": "伊奘诺尊",      "difficulty": 2, "charm": 4},  # 会1人
    {"id": 35, "name": "名刀·银纸竹光","difficulty": 2, "charm": 4},  # 会1人
    {"id": 36, "name": "如来像",        "difficulty": 2, "charm": 6},  # 会1人
    {"id": 37, "name": "摩耶",          "difficulty": 2, "charm": 4},  # 会1人
    {"id": 38, "name": "深雪",          "difficulty": 2, "charm": 6},  # 会1人
    {"id": 39, "name": "清华拳",        "difficulty": 2, "charm": 4},  # 会1人
    {"id": 40, "name": "炎火",          "difficulty": 2, "charm": 4},  # 会1人
    {"id": 41, "name": "烈火爆炎刃",    "difficulty": 2, "charm": 4},  # 会1人
    {"id": 42, "name": "煌珑",          "difficulty": 2, "charm": 4},  # 会1人
    {"id": 43, "name": "狩猎神忯大剑",  "difficulty": 2, "charm": 6},  # 会1人
    {"id": 44, "name": "白虎纹章",      "difficulty": 2, "charm": 4},  # 会1人
    {"id": 45, "name": "胧刀",          "difficulty": 2, "charm": 6},  # 会1人
    {"id": 46, "name": "蓝鸟",          "difficulty": 2, "charm": 4},  # 会1人
    {"id": 47, "name": "诗岚·极",      "difficulty": 2, "charm": 6},  # 会1人
    {"id": 48, "name": "霞斩",          "difficulty": 2, "charm": 4},  # 会1人
    {"id": 49, "name": "风雅",          "difficulty": 2, "charm": 4},  # 会1人
    {"id": 50, "name": "鹤望兰",        "difficulty": 2, "charm": 6},  # 会1人

    # d3 高阶技
    {"id": 51, "name": "两生花",        "difficulty": 3, "charm": 8},  # 会1人
    {"id": 52, "name": "诗岚·双极",    "difficulty": 3, "charm": 8},  # 会1人
    {"id": 53, "name": "八雷神",        "difficulty": 3, "charm": 6},  # wiki
    {"id": 54, "name": "伏魔御厨子",    "difficulty": 3, "charm": 6},  # wiki
    {"id": 55, "name": "乖离剑",        "difficulty": 3, "charm": 6},  # wiki
    {"id": 56, "name": "王虚之闪光",    "difficulty": 3, "charm": 6},  # wiki
    {"id": 57, "name": "王虚·破",      "difficulty": 3, "charm": 6},  # wiki
    {"id": 58, "name": "重奏虚闪",      "difficulty": 3, "charm": 6},  # wiki
    {"id": 59, "name": "天地无双刀",    "difficulty": 3, "charm": 6},  # wiki
    {"id": 60, "name": "唯我独尊",      "difficulty": 3, "charm": 6},  # wiki
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
