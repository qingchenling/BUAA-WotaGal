
init python:
    gui.init(1920, 1080)


define config.enter_transition = Dissolve(0.4)
define config.enter_yesno_transition = Dissolve(0.2)
define config.exit_transition = Dissolve(0.2)
define config.exit_yesno_transition = Dissolve(0.2)
define config.game_main_transition = Fade(0.2, 1 ,0.3)
define config.intra_transition = Dissolve(0.5)
define config.end_game_transition = Fade(0.1, 1, 0.1)

define config.enter_sound = "audio/menu_in.mp3"
define config.exit_sound = "audio/menu_out.mp3"

define say_text_font = "assets/fonts/XiaoLai-Regular.ttf"
define en_font = "assets/fonts/NotoSerif-Regular.ttf"

define btn_sound = "audio/button.mp3"

style default:
    font "assets/fonts/GlowSansSC-Normal-Book.otf"

