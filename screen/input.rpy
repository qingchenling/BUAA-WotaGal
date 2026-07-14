## 输入界面
##
## 用于 renpy.input() 调用时显示的文本输入界面。
## 居中显示，外边框为圆角矩形。

init python:
    import math

    class RoundedRect(renpy.Displayable):
        """使用多边形手动绘制纯色圆角矩形背景的 Displayable。
        兼容所有 Ren'Py 版本，不依赖 border_radius 参数。"""

        def __init__(self, color, radius=20, **properties):
            super().__init__(**properties)
            self.color = color
            self.radius = radius

        def render(self, width, height, st, at):
            rv = renpy.Render(width, height)
            canvas = rv.canvas()
            r = min(self.radius, width / 2, height / 2)
            steps = 8  # 每个圆角的采样点数

            points = []
            # 左上角 (π → π/2)
            for i in range(steps + 1):
                a = math.pi - (math.pi / 2) * i / steps
                points.append((r + r * math.cos(a), r - r * math.sin(a)))
            # 右上角 (π/2 → 0)
            for i in range(steps + 1):
                a = math.pi / 2 - (math.pi / 2) * i / steps
                points.append((width - r + r * math.cos(a), r - r * math.sin(a)))
            # 右下角 (0 → -π/2)
            for i in range(steps + 1):
                a = - (math.pi / 2) * i / steps
                points.append((width - r + r * math.cos(a), height - r - r * math.sin(a)))
            # 左下角 (-π/2 → -π)
            for i in range(steps + 1):
                a = -math.pi / 2 - (math.pi / 2) * i / steps
                points.append((r + r * math.cos(a), height - r - r * math.sin(a)))

            canvas.polygon(self.color, points)
            return rv


screen input(prompt):

    # 半透明遮罩，阻止点击穿透
    frame:
        xfill True
        yfill True
        background "#00000088"

        # 圆角矩形输入框
        frame:
            xalign 0.5
            yalign 0.5
            xmaximum 800
            xfill True

            background RoundedRect("#1a1a2eee", radius=24)
            padding (48, 36)

            vbox:
                spacing 24

                if prompt:
                    text prompt:
                        style "input_prompt"

                input:
                    style "input_field"
