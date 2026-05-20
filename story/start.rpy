define C_lin = Character("林若")
define C_song = Character("宋柯")

image bg lawn = "assets/background/lawn.png"

# 游戏在此开始。
label start:

    scene bg lawn

    C_song  "林若，我有话跟你说。"

    C_lin   "怎么了？"

    C_song  "我打算退出宅艺研了"

    C_lin   "……什么？"

    C_song  "我从没觉得打艺开心过。"

    C_lin   "你在说什么？你明明——"

    C_song  "就这样吧。"

    "主角入校故事序章"

    call screen map

    return
