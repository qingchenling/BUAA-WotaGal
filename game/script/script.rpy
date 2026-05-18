# 游戏的脚本可置于此文件中。

# 声明此游戏使用的角色。颜色参数可使角色姓名着色。



#角色常量
define p = Character("旁白")
define l =Character("林若")
define s = Character("宋柯")

image lawn:
    "images/lawn.png"
    zoom 1.5
# 游戏在此开始。


label start:
    scene lawn
    #show sylvie blue giggle
     
    # 此处显示各行对话。
    s "林若，我有话跟你说。"
    l"怎么了？"
    s"我打算退出宅艺研了"
    l"……什么？"
    s"我从没觉得打艺开心过。"
    l"你在说什么？你明明——"
    s" 就这样吧。"

    jump game_start
    p "您已创建一个新的 Ren'Py 游戏。"

    p "当您完善了故事、图片和音乐之后，您就可以向全世界发布了！"

    # 此处为游戏结尾。

   
# label map: