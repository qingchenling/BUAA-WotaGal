"""
WOTA艺 舞蹈原型 — 渲染 + 主循环
"""
import os, math, random
import pygame
from collections import deque
from wota_fsm import (Dir, Act, ArmState, DanceFSM, InputManager,
                       DIR_NAME)


# ═══════════════════════════════════════════════════════════
# 粒子
# ═══════════════════════════════════════════════════════════

class Particles:
    def __init__(self):
        self._p: list[dict] = []  # 粒子列表，每个粒子 dict 含 x/y/vx/vy/life/mx/c/size

    def emit(self, x, y, color, n=6, spread=2, life=12):
        """发射粒子: x,y=位置, color=RGB, n=数量, spread=扩散半径, life=存活帧数"""
        for _ in range(n):
            a = random.uniform(0, math.pi * 2)
            s = random.uniform(0.5, spread)
            self._p.append({'x':x, 'y':y, 'vx':math.cos(a)*s, 'vy':math.sin(a)*s,
                           'life':life, 'mx':life, 'c':color,
                           'size':random.uniform(1.5, 4)})

    def update(self):
        for p in self._p:
            p['x'] += p['vx']; p['y'] += p['vy']; p['life'] -= 1
        self._p = [p for p in self._p if p['life'] > 0]

    def draw(self, surf):
        for p in self._p:
            t = p['life'] / p['mx']
            c = tuple(int(v * t) for v in p['c'])
            pygame.draw.circle(surf, c, (int(p['x']), int(p['y'])), p['size'] * t)


# ═══════════════════════════════════════════════════════════
# 字体
# ═══════════════════════════════════════════════════════════

def _font(size: int):
    for p in ["C:/Windows/Fonts/msyh.ttc", "C:/Windows/Fonts/simhei.ttf",
              "C:/Windows/Fonts/simsun.ttc"]:
        if os.path.exists(p):
            return pygame.font.Font(p, size)
    return pygame.font.Font(None, size)


# ═══════════════════════════════════════════════════════════
# 角色渲染 — 两段手臂
# ═══════════════════════════════════════════════════════════

class Renderer:
    def __init__(self, cx, cy, scale=2.5):
        self.cx, self.cy, self.s = cx, cy, scale  # 人物中心坐标 + 缩放
        self.ul = 35 * scale   # 大臂长度（upper arm length）
        self.fl = 40 * scale   # 小臂长度（forearm length）
        self.th = 55 * scale   # 躯干长度（torso height）
        self.hr = 16 * scale   # 头半径（head radius）
        self.ss = 14 * scale   # 肩半宽（shoulder spread），左右各 ss
        self.trail_l = deque(maxlen=16)  # 左手轨迹（拖尾残影）
        self.trail_r = deque(maxlen=16)  # 右手轨迹（拖尾残影）

    def _shoulder(self, right: bool):
        x = self.cx + (self.ss if right else -self.ss)
        return (x, self.cy - 18 * self.s)

    @staticmethod
    def _joint(origin, angle, length):
        return (origin[0] + math.cos(angle) * length,
                origin[1] + math.sin(angle) * length)

    def draw(self, surf, fsm: DanceFSM, particles: Particles):
        def arm_points(arm: ArmState, is_right: bool):
            s = self._shoulder(is_right)
            e = self._joint(s, arm.upper_angle, self.ul)
            h = self._joint(e, arm.upper_angle + arm.forearm_angle, self.fl)
            return s, e, h

        ls, le, lh = arm_points(fsm.left, False)
        rs, re, rh = arm_points(fsm.right, True)
        self.trail_l.append(lh); self.trail_r.append(rh)

        la = (fsm.left.upper_omega or fsm.left.forearm_omega or fsm.left.strike_target)
        ra = (fsm.right.upper_omega or fsm.right.forearm_omega or fsm.right.strike_target)

        cl = fsm.last_color if la else (255, 100, 80)
        cr = tuple(min(255, v+40) for v in fsm.last_color) if ra else (80, 100, 255)

        self._trail(surf, self.trail_l, cl, 6)
        self._trail(surf, self.trail_r, cr, 6)

        if la: particles.emit(lh[0], lh[1], cl, n=2, spread=1.5, life=10)
        if ra: particles.emit(rh[0], rh[1], cr, n=2, spread=1.5, life=10)

        gl = self._glow(cl); gr = self._glow(cr)
        pygame.draw.line(surf, gl, ls, le, 4); pygame.draw.line(surf, gl, le, lh, 3)
        pygame.draw.line(surf, gr, rs, re, 4); pygame.draw.line(surf, gr, re, rh, 3)
        pygame.draw.circle(surf, (255,255,255), (int(lh[0]), int(lh[1])), 7)
        pygame.draw.circle(surf, (255,255,255), (int(rh[0]), int(rh[1])), 7)
        pygame.draw.circle(surf, (180,180,200), (int(le[0]), int(le[1])), 3)
        pygame.draw.circle(surf, (180,180,200), (int(re[0]), int(re[1])), 3)

        # 身体
        bc = (200,200,210)
        pygame.draw.line(surf, bc, (self.cx, self.cy-14*self.s),
                         (self.cx, self.cy+self.th), int(7*self.s))
        pygame.draw.circle(surf, (240,220,200), (self.cx, int(self.cy-32*self.s)), int(self.hr))
        lt = self.cy + self.th; lb = lt + 40*self.s
        pygame.draw.line(surf, bc, (self.cx, lt), (self.cx-10*self.s, lb), 4)
        pygame.draw.line(surf, bc, (self.cx, lt), (self.cx+10*self.s, lb), 4)

    def _trail(self, surf, trail, color, mw):
        if len(trail) < 2: return
        n = len(trail)
        for i in range(n-1):
            r = i/n; w = max(1, int(mw*r))
            c = tuple(int(v*r) for v in color)
            p1 = (int(trail[i][0]), int(trail[i][1]))
            p2 = (int(trail[i+1][0]), int(trail[i+1][1]))
            pygame.draw.line(surf, c, p1, p2, w)

    @staticmethod
    def _glow(b): return tuple(min(255, int(v*1.3+40)) for v in b)


# ═══════════════════════════════════════════════════════════
# HUD
# ═══════════════════════════════════════════════════════════

class HUD:
    def __init__(self, w, h):
        self.w, self.h = w, h
        self.fs = _font(20)   # 小字（坐标信息）
        self.fm = _font(28)   # 中字（方向/状态）
        self.fl = _font(44)   # 大字（招式名 / HIT 连击）

    def draw(self, surf, fsm: DanceFSM):
        # 底部栏
        bar = pygame.Surface((self.w, 80), pygame.SRCALPHA)
        bar.fill((0,0,0,170)); surf.blit(bar, (0, self.h-80))
        hint = self.fs.render(
            "WASD/↑↓←→=方向 | 1=左手挥击 2=右手挥击 3=小圈开关 4=大圈开关(+3叠加) 5=顺逆 6=凹凸 | SPACE=归零",
            True, (160,160,160))
        surf.blit(hint, (12, self.h-68))

        # 方向+状态
        dt = self.fm.render(f"锚点: {DIR_NAME.get(fsm.direction,'?')}", True, (255,255,255))
        surf.blit(dt, (12, 8))
        rot = "顺" if fsm.omega_sign == 1 else "逆"
        shp = "凹(同向)" if fsm.shape_sign == 1 else "凸(反向)"
        st = self.fs.render(f"旋向: {rot}  形态: {shp}", True, (200,200,200))
        surf.blit(st, (190, 12))

        # 各臂状态
        def arm_line(label, arm: ArmState, y):
            u = arm.upper_omega*60/(math.pi*2)
            f = arm.forearm_omega*60/(math.pi*2)
            parts = [f"大圈:{u:+.0f}rpm", f"小圈:{f:+.0f}rpm"]
            if arm.strike_target is not None:
                parts.append("挥击中!")
            t = self.fs.render(f"{label}  {'  '.join(parts)}", True, (140,200,140))
            surf.blit(t, (12, y))
        arm_line("左手", fsm.left, 40)
        arm_line("右手", fsm.right, 60)

        # 招式名
        if fsm.label_timer > 0:
            t = self.fl.render(fsm.last_label, True, fsm.last_color)
            surf.blit(t, (self.w//2 - t.get_width()//2, self.h-120))

        # 连击
        if fsm.combo_count >= 2:
            t = self.fl.render(f"{fsm.combo_count} HIT", True, (255,220,50))
            surf.blit(t, (self.w - t.get_width() - 16, 8))
        if fsm.max_combo > 0:
            t = self.fs.render(f"MAX: {fsm.max_combo} HIT", True, (130,130,130))
            surf.blit(t, (self.w - t.get_width() - 16, 52))


# ═══════════════════════════════════════════════════════════
# 主循环
# ═══════════════════════════════════════════════════════════

def main():
    pygame.init()
    W, H = 1024, 700
    screen = pygame.display.set_mode((W, H))
    pygame.display.set_caption("WOTA艺 Dance Prototype")
    clock = pygame.time.Clock()

    fsm = DanceFSM()
    renderer = Renderer(W//2, H//2-20, scale=2.5)
    particles = Particles()
    hud = HUD(W, H)

    while True:
        dt = min(clock.tick(60) / 1000.0, 0.05)
        events = pygame.event.get()
        keys = pygame.key.get_pressed()

        for ev in events:
            if ev.type == pygame.QUIT: return
            if ev.type == pygame.KEYDOWN and ev.key == pygame.K_ESCAPE: return

        fsm.input_dir(InputManager.resolve_direction(keys))
        for a in InputManager.get_actions(events):
            fsm.input_act(a)
        if keys[pygame.K_SPACE]:
            fsm.reset()

        fsm.update(dt)
        particles.update()

        screen.fill((12, 12, 22))
        fy = H//2 + 105
        pygame.draw.line(screen, (35,35,55), (40,fy), (W-40,fy), 1)
        particles.draw(screen)
        renderer.draw(screen, fsm, particles)
        hud.draw(screen, fsm)
        pygame.display.flip()


if __name__ == "__main__":
    main()
    pygame.quit()
