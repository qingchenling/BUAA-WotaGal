"""
WOTA艺 舞蹈状态机 — 角速度驱动 + 可叠加状态
大圈=大臂公转  小圈=小臂自转  1/2=直线挥击急停  3/4=圈开关(可叠加)  5=顺逆  6=凹凸
"""
import math
import pygame
from enum import Enum, auto


# ═══════════════════════════════════════════════════════════
# 枚举
# ═══════════════════════════════════════════════════════════

class Dir(Enum):
    N = auto(); U = auto(); D = auto(); L = auto(); R = auto()
    UL = auto(); UR = auto(); DL = auto(); DR = auto()


class Act(Enum):
    LEFT = 1; RIGHT = 2; SMALL = 3; LARGE = 4
    TOGGLE_ROT = 5; TOGGLE_SHAPE = 6


# ═══════════════════════════════════════════════════════════
# 常量表
# ═══════════════════════════════════════════════════════════

# 角度：0=右, π/2=下, -π/2=上, ±π=左
# 每个方向对应大臂的"自然停放角度"（锚点），挥击/画圈时以此角为中心展开
DIR_ANCHOR: dict[Dir, float] = {
    Dir.N: math.radians(80),   # 前方 → 右偏 80°
    Dir.U: math.radians(-80),  # 头顶 → 略偏前
    Dir.D: math.radians(120),  # 下方 → 斜下
    Dir.L: math.radians(160),  # 左方 → 接近水平左
    Dir.R: math.radians(20),   # 右方 → 接近水平右
    Dir.UL: math.radians(-120),# 左上
    Dir.UR: math.radians(-50), # 右上
    Dir.DL: math.radians(150), # 左下
    Dir.DR: math.radians(60),  # 右下
}

DIR_NAME: dict[Dir, str] = {
    Dir.N:"中", Dir.U:"↑上", Dir.D:"↓下", Dir.L:"←左", Dir.R:"→右",
    Dir.UL:"↖左上", Dir.UR:"↗右上", Dir.DL:"↙左下", Dir.DR:"↘右下"
}

# 反方向映射：凸形态(反向)时，右臂指向此方向
_OPPOSITE_DIR: dict[Dir, Dir] = {
    Dir.N:Dir.N,       # 前 ← 本身无反向，保持不变
    Dir.U:Dir.D, Dir.D:Dir.U,   # 上下互逆
    Dir.L:Dir.R, Dir.R:Dir.L,   # 左右互逆
    Dir.UL:Dir.DR, Dir.DR:Dir.UL, # 对角线互逆
    Dir.UR:Dir.DL, Dir.DL:Dir.UR,
}

# 招式映射：(方向, 动作) → (招式名称, RGB颜色)
DIR_ACT_INFO: dict[tuple, tuple] = {
    (Dir.U, Act.LEFT): ("上·左手", (255,100,100)),
    (Dir.D, Act.LEFT): ("下·左手", (255,80,80)),
    (Dir.L, Act.LEFT): ("左·左手", (255,120,120)),
    (Dir.R, Act.LEFT): ("右·左手", (255,90,90)),
    (Dir.N, Act.LEFT): ("前·左手", (255,110,110)),
    (Dir.UL, Act.LEFT):("左上·左手",(255,130,100)),
    (Dir.UR, Act.LEFT):("右上·左手",(255,100,130)),
    (Dir.DL, Act.LEFT):("左下·左手",(200,80,80)),
    (Dir.DR, Act.LEFT):("右下·左手",(200,90,80)),
    (Dir.U, Act.RIGHT): ("上·右手", (100,100,255)),
    (Dir.D, Act.RIGHT): ("下·右手", (80,80,255)),
    (Dir.L, Act.RIGHT): ("左·右手", (120,120,255)),
    (Dir.R, Act.RIGHT): ("右·右手", (90,90,255)),
    (Dir.N, Act.RIGHT): ("前·右手", (110,110,255)),
    (Dir.UL, Act.RIGHT):("左上·右手",(100,130,255)),
    (Dir.UR, Act.RIGHT):("右上·右手",(130,100,255)),
    (Dir.DL, Act.RIGHT):("左下·右手",(80,80,200)),
    (Dir.DR, Act.RIGHT):("右下·右手",(90,80,200)),
    (Dir.U, Act.SMALL): ("弥7·上小圈",(255,255,100)),
    (Dir.D, Act.SMALL): ("下小圈",    (200,200,50)),
    (Dir.L, Act.SMALL): ("左小圈",    (220,220,80)),
    (Dir.R, Act.SMALL): ("右小圈",    (220,220,80)),
    (Dir.N, Act.SMALL): ("前小圈",    (255,240,100)),
    (Dir.UL, Act.SMALL):("弥7·左斜上",(200,255,120)),
    (Dir.UR, Act.SMALL):("弥7·右斜上",(200,255,120)),
    (Dir.U, Act.LARGE): ("大圈·天",  (100,255,100)),
    (Dir.D, Act.LARGE): ("大圈·地",  (50,200,50)),
    (Dir.N, Act.LARGE): ("大圈·前",  (80,255,80)),
    (Dir.L, Act.LARGE): ("大圈·左旋",(100,200,100)),
    (Dir.R, Act.LARGE): ("大圈·右旋",(100,200,100)),
}

# 角速度常量 (rad/s)
# 大圈 = 大臂绕肩关节匀速公转，数值越大转越快
LARGE_SPEED = math.pi * 2 * 1.2    # 大圈角速度：每秒约 1.2 转
# 小圈 = 小臂绕肘关节匀速自转，通常比大圈快（视觉更灵动）
SMALL_SPEED = math.pi * 2 * 2.5    # 小圈角速度：每秒约 2.5 转
# 挥击 = 固定时长内快照急停（缓出曲线，开头极快 → 末尾猛停，不像画弧）
STRIKE_DURATION = 0.07             # 挥击固定时长 (s)，越小越像"啪"一下


# ═══════════════════════════════════════════════════════════
# 手臂状态
# ═══════════════════════════════════════════════════════════

class ArmState:
    """单臂物理状态：大臂角度 + 持续角速度 + 挥击快照急停"""

    def __init__(self, idle_angle: float):
        # ── 物理状态（每帧由角速度驱动） ──
        self.upper_angle = idle_angle     # 大臂角度 (rad)，0=右，π/2=下
        self.upper_omega = 0.0            # 大臂角速度 rad/s（大圈公转）
        self.forearm_angle = 0.0          # 小臂相对大臂的角度 (rad)，0=伸直
        self.forearm_omega = 0.0          # 小臂角速度 rad/s（小圈自转）
        # ── 挥击快照（固定时长 + 缓出曲线，不像画弧） ──
        self.strike_target = None         # None=不在挥击, float=目标锚点角度
        self.strike_t = 0.0               # 挥击已用时间 (s)
        self.strike_start_angle = 0.0     # 挥击起始角度
        # ── 基准 ──
        self.idle_angle = idle_angle      # 初始锚点，reset() 时恢复到此角度

    def reset(self):
        self.upper_angle = self.idle_angle
        self.upper_omega = 0.0
        self.forearm_angle = 0.0
        self.forearm_omega = 0.0
        self.strike_target = None
        self.strike_t = 0.0

    def update(self, dt: float):
        # 挥击快照：固定时长内从起始角缓出冲到目标，到达即停
        if self.strike_target is not None:
            self.strike_t += dt
            t = min(self.strike_t / STRIKE_DURATION, 1.0)  # 0→1 进度
            # 三次方缓出：开头极快（像爆发），末尾减速骤停（不像圆弧滑行）
            eased = 1.0 - (1.0 - t) ** 3
            diff = self.strike_target - self.strike_start_angle
            diff = (diff + math.pi) % (2 * math.pi) - math.pi  # 最短路径
            self.upper_angle = self.strike_start_angle + diff * eased
            if t >= 1.0:
                self.upper_angle = self.strike_target  # 精确停住
                self.strike_target = None
        else:
            self.upper_angle += self.upper_omega * dt

        self.forearm_angle += self.forearm_omega * dt


# ═══════════════════════════════════════════════════════════
# 舞蹈状态机
# ═══════════════════════════════════════════════════════════

class DanceFSM:
    """角速度驱动的舞蹈状态机。

    1/2 = 直线挥击急停（最短路径冲到锚点 → 停住）
    3   = 小圈开关（小臂自转）
    4   = 大圈开关（大臂公转）
    3+4 = 叠加：公转+自转（卫星轨道）
    5   = 顺逆切换（翻转所有角速度符号）
    6   = 凹凸切换（双手同向/反向）
    """

    def __init__(self):
        # ── 双臂物理状态 ──
        self.left = ArmState(math.radians(100))   # 左手初始锚点: 100°
        self.right = ArmState(math.radians(80))   # 右手初始锚点: 80°
        # ── 全局方向与变换 ──
        self.direction = Dir.N          # 当前摇杆方向（锚点方向）
        self.omega_sign = 1             # 旋向: +1=顺时针, -1=逆时针
        self.shape_sign = 1             # 形态: +1=凹(同向), -1=凸(反向)
        # ── HUD 展示状态 ──
        self.last_label = ""            # 最近一次招式名
        self.last_color = (255, 255, 255)  # 最近一次招式颜色
        self.label_timer = 0            # 招式名显示剩余帧数
        # ── 连击 ──
        self.combo_count = 0            # 当前连击数
        self.combo_timer = 0            # 连击超时倒计时（帧）
        self.max_combo = 0              # 本局最高连击

    # ── 输入 ──

    def input_dir(self, d: Dir):
        self.direction = d

    def input_act(self, a: Act):
        anchor = DIR_ANCHOR.get(self.direction, DIR_ANCHOR[Dir.N])

        if a == Act.TOGGLE_ROT:
            self.omega_sign *= -1
            # 翻转所有活跃角速度的方向（挥击目标不受影响，因为它是绝对角度）
            for arm in (self.left, self.right):
                arm.upper_omega *= -1
                arm.forearm_omega *= -1
            name = "顺" if self.omega_sign == 1 else "逆"
            self._flash(f"切换: {name}时针", (255, 200, 100))
            return

        if a == Act.TOGGLE_SHAPE:
            self.shape_sign *= -1
            # 立即翻转右臂锚点：同向→同锚点，反向→反方向锚点
            r_anchor = anchor if self.shape_sign == 1 else DIR_ANCHOR.get(
                _OPPOSITE_DIR.get(self.direction, Dir.N), anchor)
            self.right.upper_angle = r_anchor
            # 右臂角速度也翻转（凸=反向运动）
            self.right.upper_omega *= -1
            self.right.forearm_omega *= -1
            name = "凹(同向)" if self.shape_sign == 1 else "凸(反向)"
            self._flash(f"切换: {name}", (200, 150, 255))
            return

        name, color = DIR_ACT_INFO.get((self.direction, a), ("???", (200, 200, 200)))
        self._flash(name, color)
        self._combo()

        if a == Act.LEFT:
            # 停止左手画圈 → 快照急停到锚点
            self.left.upper_omega = 0.0
            self.left.forearm_omega = 0.0
            self.left.forearm_angle = 0.0
            self.left.strike_start_angle = self.left.upper_angle
            self.left.strike_t = 0.0
            self.left.strike_target = anchor

        elif a == Act.RIGHT:
            # 停止右手画圈 → 快照急停到锚点
            self.right.upper_omega = 0.0
            self.right.forearm_omega = 0.0
            self.right.forearm_angle = 0.0
            self.right.strike_start_angle = self.right.upper_angle
            self.right.strike_t = 0.0
            self.right.strike_target = anchor

        elif a == Act.SMALL:
            r_anchor = anchor if self.shape_sign == 1 else DIR_ANCHOR.get(
                _OPPOSITE_DIR.get(self.direction, Dir.N), anchor)
            r_sign = self.omega_sign if self.shape_sign == 1 else -self.omega_sign
            for arm, ang, sign in ((self.left, anchor, self.omega_sign),
                                    (self.right, r_anchor, r_sign)):
                arm.upper_angle = ang
                arm.strike_target = None  # 取消挥击
                arm.forearm_omega = 0.0 if arm.forearm_omega != 0.0 else SMALL_SPEED * sign

        elif a == Act.LARGE:
            r_anchor = anchor if self.shape_sign == 1 else DIR_ANCHOR.get(
                _OPPOSITE_DIR.get(self.direction, Dir.N), anchor)
            r_sign = self.omega_sign if self.shape_sign == 1 else -self.omega_sign
            for arm, ang, sign in ((self.left, anchor, self.omega_sign),
                                    (self.right, r_anchor, r_sign)):
                arm.upper_angle = ang
                arm.strike_target = None  # 取消挥击
                arm.upper_omega = 0.0 if arm.upper_omega != 0.0 else LARGE_SPEED * sign

    def reset(self):
        self.left.reset()
        self.right.reset()
        self._flash("归零", (150, 150, 150))

    def update(self, dt: float):
        self.left.update(dt)
        self.right.update(dt)
        if self.label_timer > 0:
            self.label_timer -= 1
        if self.combo_timer > 0:
            self.combo_timer -= 1
            if self.combo_timer == 0:
                if self.combo_count > self.max_combo:
                    self.max_combo = self.combo_count
                self.combo_count = 0

    def _flash(self, text, color):
        self.last_label = text
        self.last_color = color
        self.label_timer = 90

    def _combo(self):
        self.combo_count += 1
        self.combo_timer = 90


# ═══════════════════════════════════════════════════════════
# 输入管理
# ═══════════════════════════════════════════════════════════

class InputManager:
    # 键盘绑定：主键盘 + 小键盘均可用
    ACT_MAP = {
        pygame.K_1: Act.LEFT,          # 左手直线挥击急停
        pygame.K_KP1: Act.LEFT,
        pygame.K_2: Act.RIGHT,         # 右手直线挥击急停
        pygame.K_KP2: Act.RIGHT,
        pygame.K_3: Act.SMALL,         # 小圈开关（小臂自转）
        pygame.K_KP3: Act.SMALL,
        pygame.K_4: Act.LARGE,         # 大圈开关（大臂公转）
        pygame.K_KP4: Act.LARGE,
        pygame.K_5: Act.TOGGLE_ROT,    # 顺逆切换（翻转所有角速度符号）
        pygame.K_KP5: Act.TOGGLE_ROT,
        pygame.K_6: Act.TOGGLE_SHAPE,  # 凹凸切换（双手同向/反向）
        pygame.K_KP6: Act.TOGGLE_SHAPE,
    }

    @staticmethod
    def resolve_direction(keys) -> Dir:
        up = keys[pygame.K_UP] or keys[pygame.K_w]
        down = keys[pygame.K_DOWN] or keys[pygame.K_s]
        left = keys[pygame.K_LEFT] or keys[pygame.K_a]
        right = keys[pygame.K_RIGHT] or keys[pygame.K_d]
        if up and left:    return Dir.UL
        if up and right:   return Dir.UR
        if down and left:  return Dir.DL
        if down and right: return Dir.DR
        if up:             return Dir.U
        if down:           return Dir.D
        if left:           return Dir.L
        if right:          return Dir.R
        return Dir.N

    @staticmethod
    def get_actions(events) -> list[Act]:
        result = []
        for ev in events:
            if ev.type == pygame.KEYDOWN:
                a = InputManager.ACT_MAP.get(ev.key)
                if a is not None:
                    result.append(a)
        return result
