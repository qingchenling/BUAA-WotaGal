# 背景
# 素材都是 1280x720，游戏是 1920x1080，统一 zoom 1.5 铺满。

image bg map         = "images/bg/map.png"
image bg stage       = Transform("images/bg/stage.png", zoom=1.5)
image bg auditorium  = Transform("images/bg/auditorium.png", zoom=1.5)
image bg danceroom   = Transform("images/bg/danceroom.png", zoom=1.5)
image bg cafe        = Transform("images/bg/cafeinterior.png", zoom=1.5)
image bg quietcorner = Transform("images/bg/quietcorner.png", zoom=1.5)
image bg skymirror   = Transform("images/bg/skymirror.png", zoom=1.5)
image bg skymirror1  = Transform("images/bg/Skymirror1.png", zoom=1.5)
image bg lawn        = Transform("images/bg/lawn.png", zoom=1.5)
image bg meadow      = Transform("images/bg/bg meadow.jpg", zoom=1.5)
image bg uni         = Transform("images/bg/bg uni.jpg", zoom=1.5)
image bg club        = Transform("images/bg/bg club.jpg", zoom=1.5)
image bg lecturehall = Transform("images/bg/bg lecturehall.jpg", zoom=1.5)

# 立绘
#   叶子 → 制服短发（原「立绘A」）
#   林若 → 黑T（原「立绘B」）
image yoko = "images/sprites/yoko_normal.png"
image rin = "images/sprites/rin_normal.png"

# 立绘站位：底部对齐，左右各留一点边
transform sprite_left:
    xalign 0.22
    yalign 1.0

transform sprite_right:
    xalign 0.78
    yalign 1.0

transform sprite_center:
    xalign 0.5
    yalign 1.0
