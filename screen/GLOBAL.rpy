
init python:
    gui.init(1920, 1080)


define config.enter_transition = Dissolve(0.5)
define config.enter_yesno_transition = Dissolve(0.5)
define config.exit_transition = Dissolve(0.5)
define config.exit_yesno_transition = Dissolve(0.5)
define config.game_main_transition = Fade(0.3, 1 ,0.3)
define config.intra_transition = Dissolve(0.5)

define say_text_font = "assets/fonts/XiaoLai-Regular.ttf"

style default:
    font "assets/fonts/GlowSansSC-Normal-Book.otf"

