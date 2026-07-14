## 历史记录界面
##
## 显示游戏中已经发生过的对话，按时间倒序展示。
## 仅在游戏内（右键菜单）可访问，主菜单不显示。
screen history():
    tag menu
    use game_menu("历史", scroll="viewport"):

        style_prefix "history"

        viewport:
            id "history_viewport"
            scrollbars "vertical"
            mousewheel True
            yinitial 1.0

            vbox:
                xfill True
                spacing 16

                for h in _history_list:

                    if h.who:
                        text "[h.who]":
                            style "history_who"

                    text h.what:
                        style "history_what"

                    null height 4
