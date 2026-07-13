## 对话界面
screen say(who, what):
    style_prefix "say"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "say_namebox"
                text who id "who" style "say_namebox_text"

        text what id "what"
