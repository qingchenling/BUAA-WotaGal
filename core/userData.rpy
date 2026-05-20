
#游戏初始化是全局变量存储
#把所有变量尽量都写在这里，然后调整变量的方法写作api中，这样后续变量改变时可以看谁调用的api中函数
#基础属性（数值）
default week = 1
default fame = 0
default skill = 18



#剧情变量


#地图锁
default shahe_unlocked =True
default yongman_unlocked = False

#团体线
default member_count = 2


#个人线
default has_recruited = False
default has_first_stage =False


#技能池
default skill_pool = [
    {
        "id": "dance_basic",
        "name": "烈剑",
        "difficulty": 2,
        "mastery": 0,
        "charm":3
    },

    {
        "id": "vocal_basic",
        "name": "金刚",
        "difficulty": 2,
        "charm":3,
        "mastery": 0,
    },

    {
        "id": "stage_smile",
        "name": "雷蛇",
        "difficulty": 1,
        "charm":3,
        "mastery": 0,
    },
]
