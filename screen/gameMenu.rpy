## 通用子菜单布局：左侧导航栏 + 分割线 + 右侧内容区
##
## 使用方式：
##   screen save():
##       tag menu
##       use game_menu("保存"):
##           # 右侧内容
##
## 参数：
##   title  - 当前子页面标题，显示在导航栏顶部
##   scroll - 设为 "viewport" 时右侧内容区使用可滚动 viewport，
##            设为 "vpgrid" 时使用纵向网格滚动，不传则直接放置内容
screen game_menu(title, scroll=None):

    # frame 包裹以支持 background，padding 归零使内容填满
    frame:
        xfill True
        yfill True
        background "#000000dd"
        padding (0, 0)

        hbox:
            style_prefix "gameMenu"
            xfill True
            yfill True

            # ── 左侧导航栏 ──
            vbox:
                style_prefix "gameMenu_nav"

                # 当前页面标题
                label title

                null height 40

                # 仅在游戏内（右键菜单）显示
                if not main_menu:
                    textbutton "历史" action ShowMenu("history")
                    textbutton "保存" action ShowMenu("save")

                textbutton "读取" action ShowMenu("load")
                textbutton "设置" action ShowMenu("preferences")
                textbutton "帮助" action ShowMenu("help")
                if main_menu:
                    textbutton "主菜单" action ShowMenu("main_menu")
                else:
                    textbutton "主菜单" action MainMenu()

                textbutton "退出" action Quit(confirm=not main_menu)

            # ── 分割线 ──
            fixed:
                xsize 2
                yfill True
                add Solid("#ffffff44")

            # ── 右侧内容区 ──
            frame:
                style_prefix ""
                background None
                yfill True
                xfill True
                if scroll == "viewport":

                    viewport:
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True
                        
                        xfill True
                        yfill True
                        
                        transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial 1.0

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        xfill True
                        yfill True

                        transclude

                else:

                    transclude
