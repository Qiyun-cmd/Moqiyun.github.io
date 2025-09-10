from manim import *
import numpy as np
import math
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from my_manim_setup import *

# 全局字体：中文请用系统已安装字体
config.font = "Microsoft YaHei"

# ---------- 工具函数（模块级） ----------
def safe_normalize(v):
    n = np.linalg.norm(v)
    return v / (n if n > 1e-8 else 1)

def Rz(a):
    c, s = np.cos(a), np.sin(a)
    return np.array([[c, -s, 0], [s, c, 0], [0, 0, 1]])

def Rx(a):
    c, s = np.cos(a), np.sin(a)
    return np.array([[1, 0, 0], [0, c, -s], [0, s, c]])

def kepler_pos_3d(f, a, e, Omega=0, inc=0, omega=0):
    # 真近点角 f → 焦点极坐标 → 3D 姿态
    p = a * (1 - e * e)
    r = p / (1 + e * np.cos(f))
    x, y, z = r * np.cos(f), r * np.sin(f), 0.0
    R = Rz(Omega) @ Rx(inc) @ Rz(omega)
    return (R @ np.array([x, y, z])).astype(float)

def make_sphere(center, radius, color):
    # 球体的通用构造，若 Sphere 不可用，退化为 Dot3D 或 Dot
    try:
        s = Sphere(center=center, radius=radius, color=color)
        s.set_fill(color, opacity=1.0).set_stroke(width=0)
        if hasattr(s, "set_shade_in_3d"):
            s.set_shade_in_3d(True)
        return s
    except Exception:
        try:
            return Dot3D(center, radius=radius, color=color)
        except Exception:
            return Dot(center[:2], color=color).scale(1.2)

def segmented_polar_conic(e_val, l_val, color=YELLOW, stroke_width=4):
    """
    极坐标统一方程：r = l / (1 + e cosθ)
    分段避开奇点（抛物线与双曲线），返回 VGroup 片段。
    """
    segs = VGroup()
    eps = 0.06
    if e_val < 1 - 1e-6:  # 圆/椭圆
        spans = [(-PI, PI)]
    elif abs(e_val - 1) <= 1e-6:  # 抛物线
        spans = [(-PI + eps, PI - eps)]
    else:  # 双曲线
        th0 = math.acos(-1 / e_val)  # singular angles
        spans = [(-PI + eps, -th0 - eps), (-th0 + eps, th0 - eps), (th0 + eps, PI - eps)]

    def fn(theta):
        denom = 1 + e_val * math.cos(theta)
        if abs(denom) < 1e-4:
            denom = np.sign(denom) * 1e-4
        r = l_val / denom
        return np.array([r * math.cos(theta), r * math.sin(theta), 0])
    for t0, t1 in spans:
        segs.add(ParametricFunction(fn, t_range=(t0, t1), color=color, stroke_width=stroke_width))
    return segs


# ============ 主场景：整合全部内容（ThreeDScene） ============
class ConicSectionsComplete(ThreeDScene):
    def construct(self):
        self.camera.background_color = "#1a1a1a"

        # 1. 片头
        self.opening_animation()
        # 2. 历史背景
        self.historical_background()
        # 3. 3D 圆锥截切
        self.cone_sections_3d()
        # 4. 焦点-准线与离心率
        self.focus_directrix_definition()
        # 5. 离心率形变
        self.eccentricity_magic()
        # 6. 标准方程与参数
        self.standard_equations()
        # 7. 椭圆双焦点性质
        self.ellipse_foci_property()
        # 8. 抛物线反射
        self.parabola_reflection()

        # 9. 加料：3D 天体与拓展
        self.kepler_orbits_3d()
        self.binary_stars_3d()
        self.gravitation_derivation()
        self.cardioid_playground()
        self.heart_surface_3d()
        self.conic_surfaces_3d()

        # 10. 结尾
        self.closing_animation()

    # ---------- 片头 ----------
    def opening_animation(self):
        self.set_camera_orientation(phi=0*DEGREES, theta=-90*DEGREES, zoom=1.0)
        title = Text("圆锥曲线", font_size=72).set_color_by_gradient(BLUE, GREEN)
        subtitle = Text("从几何到天体与3D曲面", font_size=36, color=GRAY_A).next_to(title, DOWN, buff=0.4)
        self.play(Write(title), run_time=1.6)
        self.play(FadeIn(subtitle, shift=UP*0.2), run_time=1.2)
        self.wait(0.6)

        # 四类曲线概览
        circle = Circle(radius=1.0, color=BLUE).set_stroke(width=5)
        ellipse = Ellipse(width=2.2, height=1.4, color=GREEN).set_stroke(width=5)
        p = 0.5
        parabola = ParametricFunction(lambda t: np.array([p * t * t, 2 * p * t, 0]),
                                      t_range=(-2.0, 2.0), color=YELLOW, stroke_width=5)
        a, b = 1.0, 0.7
        u_max = 1.3
        right_h = ParametricFunction(lambda u: np.array([a * math.cosh(u), b * math.sinh(u), 0]),
                                     t_range=(-u_max, u_max), color=RED, stroke_width=5)
        left_h = right_h.copy().apply_matrix([[-1, 0, 0], [0, 1, 0], [0, 0, 1]])
        hyper = VGroup(left_h, right_h)
        g = VGroup(circle, ellipse, parabola, hyper).arrange(RIGHT, buff=1.0).shift(DOWN*0.5)
        labels = VGroup(
            Text("圆", font_size=26).next_to(circle, DOWN, buff=0.15),
            Text("椭圆", font_size=26).next_to(ellipse, DOWN, buff=0.15),
            Text("抛物线", font_size=26).next_to(parabola, DOWN, buff=0.15),
            Text("双曲线", font_size=26).next_to(hyper, DOWN, buff=0.15),
        )
        self.play(LaggedStartMap(Create, g, lag_ratio=0.15, run_time=2.6))
        self.play(LaggedStartMap(FadeIn, labels, lag_ratio=0.1, run_time=1.0))
        self.wait(1.2)
        self.play(FadeOut(title, subtitle, g, labels))

    # ---------- 历史背景 ----------
    def historical_background(self):
        timeline = Line(LEFT*6, RIGHT*6, color=GRAY).shift(DOWN*2)
        self.play(Create(timeline))
        events = [
            ("公元前200年", "阿波罗尼乌斯", "系统研究圆锥曲线"),
            ("1609年", "开普勒", "行星运动定律"),
            ("1687年", "牛顿", "万有引力定律"),
            ("现代", "应用", "卫星轨道、抛物面天线"),
        ]
        dots, labs = [], []
        for i, (year, person, ach) in enumerate(events):
            x = -6 + i * 4
            dot = Dot([x, -2, 0], color=YELLOW)
            l1 = Text(year, font_size=22).next_to(dot, DOWN)
            l2 = Text(person, font_size=26, color=BLUE).next_to(dot, UP)
            l3 = Text(ach, font_size=20, color=GRAY_A).next_to(l2, UP)
            dots.append(dot); labs.extend([l1, l2, l3])
            self.play(FadeIn(dot, scale=1.3), Write(l1), Write(l2), Write(l3), run_time=1.0)
        self.wait(1.2)
        self.play(FadeOut(timeline, *dots, *labs), run_time=0.8)

    # ---------- 3D 圆锥截切 ----------
    def cone_sections_3d(self):
        self.set_camera_orientation(phi=65*DEGREES, theta=30*DEGREES, zoom=1.0)
        axes = ThreeDAxes(x_range=(-4, 4, 1), y_range=(-4, 4, 1), z_range=(-3, 3, 1))
        k, r_max = 0.9, 2.5
        def cone(u, v, sign=1.0):
            r = v
            z = sign * k * v
            return np.array([r * np.cos(u), r * np.sin(u), z])
        top_cone = Surface(lambda u, v: cone(u, v, +1.0), u_range=(0, TAU), v_range=(0, r_max),
                           resolution=(32, 16), fill_opacity=0.6, checkerboard_colors=[BLUE_D, BLUE_E])
        bottom_cone = Surface(lambda u, v: cone(u, v, -1.0), u_range=(0, TAU), v_range=(0, r_max),
                              resolution=(32, 16), fill_opacity=0.6, checkerboard_colors=[BLUE_D, BLUE_E])
        plane = Rectangle(width=6, height=6, color=GREEN_E).set_fill(GREEN_E, opacity=0.45).set_stroke(width=0)
        if hasattr(plane, "set_shade_in_3d"):
            plane.set_shade_in_3d(True)

        label = Text("截交曲线：圆", font_size=30)
        self.add_fixed_in_frame_mobjects(label); label.to_corner(UR).shift(LEFT*0.2+DOWN*0.2)

        self.play(FadeIn(axes), FadeIn(top_cone), FadeIn(bottom_cone), FadeIn(plane), run_time=1.4)
        self.begin_ambient_camera_rotation(rate=0.05)
        self.wait(1.2)

        # 椭圆
        self.play(Rotate(plane, angle=20*DEGREES, axis=RIGHT),
                  Transform(label, Text("截交曲线：椭圆", font_size=30).to_corner(UR).shift(LEFT*0.2+DOWN*0.2)),
                  run_time=1.8)
        self.wait(0.8)

        # 抛物线（近似：平面 ∥ 母线）
        alpha = math.atan(1/k)
        self.play(Rotate(plane, angle=(alpha - 20*DEGREES)),
                  Transform(label, Text("截交曲线：抛物线", font_size=30).to_corner(UR).shift(LEFT*0.2+DOWN*0.2)),
                  run_time=2.0)
        self.wait(0.8)

        # 双曲线
        self.play(Rotate(plane, angle=25*DEGREES, axis=RIGHT),
                  Transform(label, Text("截交曲线：双曲线", font_size=30).to_corner(UR).shift(LEFT*0.2+DOWN*0.2)),
                  run_time=1.8)
        self.wait(1.2)
        self.stop_ambient_camera_rotation()
        self.play(FadeOut(axes, top_cone, bottom_cone, plane, label), run_time=0.8)

    # ---------- 焦点-准线与离心率 ----------
    def focus_directrix_definition(self):
        self.set_camera_orientation(phi=0*DEGREES, theta=-90*DEGREES, zoom=1.0)
        plane = NumberPlane(x_range=(-8, 8, 1), y_range=(-4.5, 4.5, 1)).set_opacity(0.6)
        title = Text("焦点-准线定义与极坐标方程", font_size=36).to_edge(UP)
        self.play(FadeIn(plane), Write(title), run_time=0.8)

        e = ValueTracker(0.0)  # 离心率
        l = 3.0               # 半通径
        focus = Dot(ORIGIN, color=YELLOW)
        focus_label = Text("F", font_size=24, color=YELLOW).next_to(focus, UR, buff=0.15)

        directrix = always_redraw(lambda: Line(
            start=np.array([-l / max(e.get_value(), 1e-3), -4.5, 0]),
            end=np.array([-l / max(e.get_value(), 1e-3),  4.5, 0]),
            color=GRAY_B, stroke_width=3
        ))
        dlabel = Text("准线", font_size=24, color=GRAY_B)
        dlabel.add_updater(lambda m: m.next_to(directrix, UP, buff=0.2))

        formula = MathTex(r"r=\frac{l}{1+e\cos\theta}").to_corner(UR)
        etext = VGroup(Text("e =", font_size=28),
                       always_redraw(lambda: DecimalNumber(e.get_value(), num_decimal_places=2, color=YELLOW, font_size=32))
                      ).arrange(RIGHT, buff=0.15).to_corner(UL)

        conic_curve = always_redraw(lambda: segmented_polar_conic(e.get_value(), l, color=TEAL, stroke_width=5))
        self.play(FadeIn(focus), FadeIn(focus_label), FadeIn(directrix), FadeIn(dlabel), Write(formula), FadeIn(etext))
        self.add(conic_curve)
        self.wait(0.6)

        # e 变化
        self.play(e.animate.set_value(0.70), run_time=2.4)
        self.play(e.animate.set_value(1.00), run_time=2.0)
        self.play(e.animate.set_value(1.60), run_time=2.0)

        # |PF| = e · |PD|
        theta = ValueTracker(-1.0)
        def point_on_conic():
            th = theta.get_value()
            denom = 1 + e.get_value() * math.cos(th)
            if abs(denom) < 1e-4:
                th += 0.2  # 避开奇点
                denom = 1 + e.get_value() * math.cos(th)
            r = l / denom
            return np.array([r * math.cos(th), r * math.sin(th), 0])

        P = always_redraw(lambda: Dot(point_on_conic(), color=WHITE))
        pf_line = always_redraw(lambda: Line(focus.get_center(), P.get_center(), color=YELLOW, stroke_width=3))
        pd_line = always_redraw(lambda: Line(
            P.get_center(),
            np.array([-l / max(e.get_value(), 1e-3), P.get_center()[1], 0]),
            color=GRAY_B, stroke_width=3
        ))
        prop = MathTex(r"|PF| = e\cdot|PD|").to_corner(DR)

        self.add(P, pf_line, pd_line)
        self.play(Write(prop), run_time=0.6)
        self.play(theta.animate.set_value(1.2), run_time=3.0)
        self.play(FadeOut(plane, title, focus, focus_label, directrix, dlabel, formula, etext, conic_curve, P, pf_line, pd_line, prop))

    # ---------- 离心率形变（类型切换） ----------
    def eccentricity_magic(self):
        self.set_camera_orientation(phi=0*DEGREES, theta=-90*DEGREES, zoom=1.0)
        axes = Axes(x_range=[-6, 6, 1], y_range=[-4, 4, 1], axis_config={"color": GRAY_B}).scale(0.9)
        e_tracker = ValueTracker(0.0)
        title = Text("离心率的魔力", font_size=36).to_edge(UP)
        e_text = always_redraw(lambda: Text(f"e = {e_tracker.get_value():.2f}", font_size=28, color=YELLOW).to_corner(UR))
        type_text = always_redraw(lambda: Text(
            "圆" if e_tracker.get_value() < 0.01 else ("椭圆" if e_tracker.get_value() < 0.99 else ("抛物线" if e_tracker.get_value() <= 1.01 else "双曲线")),
            font_size=32, color=TEAL
        ).to_corner(UL))

        def get_curve():
            e = e_tracker.get_value()
            if e < 0.01:
                return Circle(radius=2.2, color=BLUE)
            elif e < 0.99:
                a = 2.5; b = 2.5 * np.sqrt(1 - e*e)
                return Ellipse(width=2*a, height=2*b, color=GREEN)
            elif e <= 1.01:
                return FunctionGraph(lambda x: x*x/4, x_range=[-3, 3], color=YELLOW)
            else:
                return VGroup(
                    FunctionGraph(lambda x: np.sqrt(1 + x*x), x_range=[0.3, 3.0], color=RED),
                    FunctionGraph(lambda x: -np.sqrt(1 + x*x), x_range=[0.3, 3.0], color=RED)
                )
        curve = always_redraw(get_curve)

        self.play(Write(title), Create(axes), FadeIn(e_text), FadeIn(type_text))
        self.add(curve)
        self.play(e_tracker.animate.set_value(0.70), run_time=2.0)
        self.play(e_tracker.animate.set_value(1.00), run_time=2.0)
        self.play(e_tracker.animate.set_value(1.50), run_time=2.0)
        self.wait(0.6)
        self.play(FadeOut(title, axes, e_text, type_text, curve))

    # ---------- 标准方程与参数 ----------
    def standard_equations(self):
        self.set_camera_orientation(phi=0*DEGREES, theta=-90*DEGREES, zoom=1.0)
        title = Text("标准方程与参数关系", font_size=38).to_edge(UP)
        self.play(Write(title), run_time=0.7)

        eq_specs = [
            ("圆：",     r"x^2 + y^2 = R^2",                       BLUE),
            ("椭圆：",   r"\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1", GREEN),
            ("抛物线：", r"y^2 = 4px",                             YELLOW),
            ("双曲线：", r"\frac{x^2}{a^2} - \frac{y^2}{b^2} = 1", RED),
        ]
        rows = []
        for label_text, tex, col in eq_specs:
            t = Text(label_text, font_size=34, color=col)
            m = MathTex(rf"{tex}", font_size=34).set_color(col)
            rows.append(VGroup(t, m).arrange(RIGHT, buff=0.35))
        equations = VGroup(*rows).arrange(DOWN, buff=0.6, aligned_edge=LEFT).next_to(title, DOWN, buff=0.6).to_edge(LEFT, buff=0.7)
        self.play(LaggedStart(*[Write(row) for row in equations], lag_ratio=0.15), run_time=3.0)

        rel_specs = [
            (r"c^2 = a^2 - b^2", "（椭圆）",         GREEN),
            (r"c^2 = a^2 + b^2", "（双曲线）",       RED),
            (r"e = \frac{c}{a}", "（椭圆、双曲线）", WHITE),
            (r"e = 1",           "（抛物线）",       YELLOW),
        ]
        rel_rows = []
        for tex, zh, col in rel_specs:
            m = MathTex(rf"{tex}", font_size=28).set_color(col)
            t = Text(zh, font_size=26, color=col)
            rel_rows.append(VGroup(m, t).arrange(RIGHT, buff=0.25))
        relations = VGroup(*rel_rows).arrange(DOWN, buff=0.35, aligned_edge=LEFT)
        rel_title = Text("参数关系：", font_size=30)
        right_block = VGroup(rel_title, relations).arrange(DOWN, buff=0.4).next_to(equations, RIGHT, buff=1.0)

        self.play(Write(rel_title), LaggedStart(*[Write(r) for r in relations], lag_ratio=0.2), run_time=2.4)
        self.wait(0.6)
        self.play(FadeOut(title, equations, right_block), run_time=0.8)

    # ---------- 椭圆双焦点性质 ----------
    def ellipse_foci_property(self):
        self.set_camera_orientation(phi=0*DEGREES, theta=-90*DEGREES, zoom=1.0)
        title = Text("椭圆性质：|PF₁| + |PF₂| = 2a", font_size=34).to_edge(UP)
        self.play(Write(title), run_time=0.7)

        a, e = 3.0, 0.6
        c = a * e
        b = a * math.sqrt(1 - e * e)
        ellipse = Ellipse(width=2 * a, height=2 * b, color=GREEN).set_stroke(width=5)
        F1 = Dot(np.array([-c, 0, 0]), color=YELLOW)
        F2 = Dot(np.array([ c, 0, 0]), color=YELLOW)
        P_t = ValueTracker(0.0)
        P = always_redraw(lambda: Dot(np.array([a * math.cos(P_t.get_value()), b * math.sin(P_t.get_value()), 0]), color=WHITE))
        L1 = always_redraw(lambda: Line(P.get_center(), F1.get_center(), color=BLUE, stroke_width=3))
        L2 = always_redraw(lambda: Line(P.get_center(), F2.get_center(), color=RED,  stroke_width=3))
        sum_lab = Text("距离和", font_size=24).to_corner(UR)
        sum_val = always_redraw(lambda: DecimalNumber(
            np.linalg.norm(P.get_center()-F1.get_center()) + np.linalg.norm(P.get_center()-F2.get_center()),
            num_decimal_places=2
        ).scale(0.8).next_to(sum_lab, DOWN, buff=0.2))
        const_lab = MathTex(rf"2a = {2*a:.2f}", font_size=34).next_to(sum_lab, DOWN, buff=1.0)

        self.play(Create(ellipse), FadeIn(F1, F2), FadeIn(sum_lab), FadeIn(sum_val), FadeIn(const_lab))
        self.add(P, L1, L2)
        self.play(P_t.animate.set_value(2*PI), run_time=6.0, rate_func=linear)
        self.play(FadeOut(title, ellipse, F1, F2, P, L1, L2, sum_lab, sum_val, const_lab))

    # ---------- 抛物线反射 ----------
    def parabola_reflection(self):
        self.set_camera_orientation(phi=0*DEGREES, theta=-90*DEGREES, zoom=1.0)
        title = Text("抛物线的反射性质：平行光线汇聚于焦点", font_size=34).to_edge(UP)
        self.play(Write(title), run_time=0.7)

        p = 1.5
        parabola = ParametricFunction(lambda t: np.array([p*t*t, 2*p*t, 0]), t_range=(-2.2, 2.2),
                                      color=YELLOW, stroke_width=5)
        focus = Dot(np.array([p, 0, 0]), color=RED)
        self.play(Create(parabola), FadeIn(focus))

        t = ValueTracker(-1.4)
        def pt(tt): return np.array([p*tt*tt, 2*p*tt, 0])
        P = always_redraw(lambda: Dot(pt(t.get_value()), color=WHITE))
        def tangent_dir(tt): return np.array([2*p*tt, 2*p, 0])
        tan_line = always_redraw(lambda: Line(P.get_center()-safe_normalize(tangent_dir(t.get_value()))*3.0,
                                              P.get_center()+safe_normalize(tangent_dir(t.get_value()))*3.0,
                                              color=BLUE, stroke_width=3))
        ray_in = always_redraw(lambda: Arrow(P.get_center()+LEFT*4.5, P.get_center(), buff=0, color=GRAY_B, stroke_width=3))
        def reflected_dir(tt):
            vin = safe_normalize(np.array([1.0, 0.0, 0.0]))
            th = safe_normalize(tangent_dir(tt))
            vout = 2 * np.dot(vin, th) * th - vin
            return safe_normalize(vout)
        ray_out = always_redraw(lambda: Arrow(P.get_center(), P.get_center()+reflected_dir(t.get_value())*4.0,
                                              buff=0, color=GREEN, stroke_width=3))
        tip = Text("反射线穿过焦点", font_size=26, color=GREEN).to_corner(UR)

        self.add(P, tan_line, ray_in, ray_out)
        self.play(FadeIn(tip))
        self.play(t.animate.set_value(1.2), run_time=5.0, rate_func=linear)
        self.play(FadeOut(title, parabola, focus, P, tan_line, ray_in, ray_out, tip))

    # ---------- 3D 行星轨道 ----------
    def kepler_orbits_3d(self):
        self.set_camera_orientation(phi=70*DEGREES, theta=40*DEGREES, zoom=0.9)
        axes = ThreeDAxes(x_range=(-8,8,2), y_range=(-8,8,2), z_range=(-6,6,2))
        self.play(FadeIn(axes), run_time=0.6)

        a, e = 5.0, 0.6
        Omega, inc, omega = 25*DEGREES, 28*DEGREES, 15*DEGREES
        p = a*(1-e*e)

        sun = make_sphere(ORIGIN, 0.25, YELLOW)
        orbit = ParametricFunction(lambda f: kepler_pos_3d(f, a, e, Omega, inc, omega),
                                   t_range=(-PI, PI), color=TEAL, stroke_width=4)

        f_tracker = ValueTracker(-PI)
        def P():
            return kepler_pos_3d(f_tracker.get_value(), a, e, Omega, inc, omega)

        planet = always_redraw(lambda: make_sphere(P(), 0.15, BLUE))
        radius_line = always_redraw(lambda: Line(ORIGIN, P(), color=GRAY_B, stroke_width=3))

        def tdir(df=1e-3):
            p1 = kepler_pos_3d(f_tracker.get_value(), a, e, Omega, inc, omega)
            p2 = kepler_pos_3d(f_tracker.get_value()+df, a, e, Omega, inc, omega)
            return safe_normalize(p2-p1)
        vel_vec = always_redraw(lambda: Line(P(), P()+tdir()*1.2, color=GREEN, stroke_width=4))
        acc_vec = always_redraw(lambda: Line(P(), P()+safe_normalize(ORIGIN-P())*1.2, color=RED, stroke_width=4))

        title = Text("3D 行星轨道与开普勒定律", font_size=34)
        law2 = Text("第二定律：等时扫过面积相等", font_size=26, color=GRAY_A)
        law3 = VGroup(Text("第三定律：", font_size=26, color=GRAY_A),
                      MathTex(r"T^2 = \frac{4\pi^2}{GM}a^3", font_size=30)).arrange(RIGHT, buff=0.25)
        self.add_fixed_in_frame_mobjects(title, law2, law3)
        title.to_corner(UL); law2.next_to(title, DOWN, aligned_edge=LEFT); law3.to_corner(UR)

        self.play(FadeIn(sun), Create(orbit), FadeIn(title), FadeIn(law2), FadeIn(law3), run_time=1.2)
        self.add(planet, radius_line, vel_vec, acc_vec)
        self.begin_ambient_camera_rotation(rate=0.05)
        self.play(f_tracker.animate.set_value(PI), run_time=8, rate_func=linear)

        # 第二定律：近拱/远拱等面积
        f_peri, f_ap = 0.0, PI
        r_peri = p/(1+e*np.cos(f_peri)); r_ap = p/(1+e*np.cos(f_ap))
        dth1 = 35*DEGREES
        dth2 = dth1*(r_peri**2)/(r_ap**2)
        def wedge(f0, dth, col):
            A = kepler_pos_3d(f0, a, e, Omega, inc, omega)
            B = kepler_pos_3d(f0+dth, a, e, Omega, inc, omega)
            return Polygon(A, B, ORIGIN, color=col, stroke_width=0).set_fill(col, opacity=0.4)
        w1 = wedge(f_peri, dth1, BLUE); w2 = wedge(f_ap, dth2, ORANGE)
        cap = Text("等面积 ⇒ 等时间", font_size=26, color=WHITE)
        self.add_fixed_in_frame_mobjects(cap); cap.to_edge(DOWN)

        self.play(FadeIn(w1), FadeIn(w2), FadeIn(cap), run_time=1.0)
        self.wait(1.4)
        self.stop_ambient_camera_rotation()
        self.play(FadeOut(axes, orbit, sun, planet, radius_line, vel_vec, acc_vec, w1, w2, title, law2, law3, cap), run_time=0.8)

    # ---------- 3D 双星系统 ----------
    def binary_stars_3d(self):
        self.set_camera_orientation(phi=65*DEGREES, theta=35*DEGREES, zoom=0.95)
        axes = ThreeDAxes(x_range=(-8,8,2), y_range=(-8,8,2), z_range=(-6,6,2))
        self.play(FadeIn(axes), run_time=0.5)

        m1, m2 = 2.0, 1.0
        a_total, e = 6.0, 0.5
        mu1, mu2 = m1/(m1+m2), m2/(m1+m2)
        Omega, inc, omega = 10*DEGREES, 25*DEGREES, 20*DEGREES

        def r_rel(f): return kepler_pos_3d(f, a_total, e, Omega, inc, omega)
        def pos1(f): return -mu2 * r_rel(f)
        def pos2(f): return  mu1 * r_rel(f)

        orbit1 = ParametricFunction(lambda f: pos1(f), t_range=(-PI, PI), color=BLUE, stroke_width=3)
        orbit2 = ParametricFunction(lambda f: pos2(f), t_range=(-PI, PI), color=RED,  stroke_width=3)

        f_tracker = ValueTracker(-PI)
        star1 = always_redraw(lambda: make_sphere(pos1(f_tracker.get_value()), 0.22, BLUE))
        star2 = always_redraw(lambda: make_sphere(pos2(f_tracker.get_value()), 0.18, RED))
        bary = make_sphere(ORIGIN, 0.06, YELLOW)
        link = always_redraw(lambda: Line(pos1(f_tracker.get_value()), pos2(f_tracker.get_value()), color=GRAY_B, stroke_width=3))

        formula = MathTex(r"F = \frac{G m_1 m_2}{r^2}", font_size=36)
        cap = Text("双星绕质心椭圆轨道（同周期）", font_size=26, color=GRAY_A)
        self.add_fixed_in_frame_mobjects(formula, cap)
        formula.to_corner(UR); cap.to_corner(UL)

        self.play(Create(orbit1), Create(orbit2), FadeIn(bary), FadeIn(formula), FadeIn(cap), run_time=1.2)
        self.add(star1, star2, link)
        self.begin_ambient_camera_rotation(rate=0.05)
        self.play(f_tracker.animate.set_value(PI), run_time=8, rate_func=linear)
        self.stop_ambient_camera_rotation()

        note = Text("距离比 r₁:r₂ = m₂:m₁", font_size=26, color=GRAY_A)
        self.add_fixed_in_frame_mobjects(note); note.to_edge(DOWN)
        self.play(FadeIn(note), run_time=0.6)
        self.wait(0.8)
        self.play(FadeOut(axes, orbit1, orbit2, star1, star2, link, bary, formula, cap, note), run_time=0.8)

    # ---------- 万有引力推导（板书） ----------
    def gravitation_derivation(self):
        self.set_camera_orientation(phi=0*DEGREES, theta=-90*DEGREES, zoom=1.0)
        title = Text("万有引力与开普勒第三定律", font_size=38)
        self.play(Write(title)); self.play(title.animate.to_edge(UP).scale(0.8))

        steps = VGroup(
            Text("圆轨道向心力：", font_size=28, color=GRAY_A),
            MathTex(r"m\frac{v^2}{r} = \frac{G M m}{r^2}", font_size=40),
            MathTex(r"v^2 = \frac{G M}{r}", font_size=40),
            Text("轨道周期：", font_size=28, color=GRAY_A),
            MathTex(r"T = \frac{2\pi r}{v}", font_size=40),
            MathTex(r"T^2 = \frac{4\pi^2}{G M} r^3", font_size=40),
            Text("椭圆推广：r → a：", font_size=28, color=GRAY_A),
            MathTex(r"T^2 = \frac{4\pi^2}{G M} a^3", font_size=44).set_color(YELLOW),
        ).arrange(DOWN, buff=0.35).next_to(title, DOWN, buff=0.6).to_edge(LEFT, buff=0.8)

        for s in steps:
            self.play(Write(s), run_time=0.7)
        self.wait(1.0)
        self.play(FadeOut(title, steps), run_time=0.6)

    # ---------- 心形函数（极坐标与等径外摆线） ----------
    def cardioid_playground(self):
        self.set_camera_orientation(phi=0*DEGREES, theta=-90*DEGREES, zoom=1.0)
        title = Text("心形函数：极坐标与等径外摆线", font_size=36)
        self.play(Write(title)); self.play(title.animate.to_edge(UP).scale(0.8))

        plane = NumberPlane(x_range=(-6,6,1), y_range=(-4,4,1), faded_line_ratio=2).set_opacity(0.6)
        self.play(Create(plane))

        a = 2.5
        cardioid = ParametricFunction(lambda t: np.array([a*(1-np.cos(t))*np.cos(t), a*(1-np.cos(t))*np.sin(t), 0]),
                                      t_range=(0, TAU), color=RED, stroke_width=6)
        cap1 = VGroup(Text("极坐标：", font_size=26), MathTex(r"r = a(1-\cos\theta)", font_size=30)).arrange(RIGHT).to_corner(UR)
        self.play(Create(cardioid), FadeIn(cap1), run_time=2.0)
        self.wait(0.6)

        # 等径外摆线：x=R(2cos t - cos2t), y=R(2sin t - sin2t)
        R = 1.4
        theta = ValueTracker(0.0)
        big_circle = Circle(radius=2*R, color=GRAY_B)
        trace_point = always_redraw(lambda: Dot(np.array([
            R*(2*np.cos(theta.get_value()) - np.cos(2*theta.get_value())),
            R*(2*np.sin(theta.get_value()) - np.sin(2*theta.get_value())), 0]), color=YELLOW, radius=0.06))
        traced = TracedPath(trace_point.get_center, stroke_color=YELLOW, stroke_width=4)
        cap2 = Text("等径外摆线生成心形", font_size=26).to_corner(UL)
        self.play(Create(big_circle), FadeIn(cap2))
        self.add(trace_point, traced)
        self.play(theta.animate.set_value(TAU), run_time=5, rate_func=linear)
        self.wait(0.6)
        self.play(FadeOut(plane, cardioid, cap1, big_circle, trace_point, traced, cap2, title), run_time=0.6)

    # ---------- 心形曲面（3D） ----------
    def heart_surface_3d(self):
        self.set_camera_orientation(phi=65*DEGREES, theta=35*DEGREES, zoom=1.0)
        axes = ThreeDAxes(x_range=(-5,5,1), y_range=(-5,5,1), z_range=(-5,5,1))
        self.play(FadeIn(axes), run_time=0.5)

        a = 1.6
        def x_of(t): return a*(1-np.cos(t))*np.cos(t)
        def y_of(t): return a*(1-np.cos(t))*np.sin(t)

        heart_surface = Surface(
            lambda u, v: np.array([x_of(u), y_of(u)*np.cos(v), y_of(u)*np.sin(v)]),
            u_range=(0, TAU), v_range=(0, TAU),
            resolution=(40, 20),
            checkerboard_colors=[PINK, PURPLE], fill_opacity=0.7
        )
        if hasattr(heart_surface, "set_shade_in_3d"):
            heart_surface.set_shade_in_3d(True)

        cap = Text("心形面：心形曲线绕 x 轴旋转", font_size=28)
        self.add_fixed_in_frame_mobjects(cap); cap.to_corner(UL)

        self.begin_ambient_camera_rotation(rate=0.05)
        self.play(FadeIn(heart_surface, scale=0.9), run_time=1.2)
        self.wait(1.4)
        self.stop_ambient_camera_rotation()
        self.play(FadeOut(axes, heart_surface, cap), run_time=0.6)

    # ---------- 维度拓展：经典二次曲面（3D） ----------
    def conic_surfaces_3d(self):
        self.set_camera_orientation(phi=70*DEGREES, theta=40*DEGREES, zoom=0.95)
        axes = ThreeDAxes(x_range=(-4,4,1), y_range=(-4,4,1), z_range=(-4,4,1))
        self.play(FadeIn(axes), run_time=0.5)

        title = Text("由圆锥曲线生成的经典曲面", font_size=30)
        self.add_fixed_in_frame_mobjects(title); title.to_corner(UL)

        a,b,c = 2.0, 1.2, 1.0
        ellipsoid = Surface(
            lambda u,v: np.array([a*np.sin(v)*np.cos(u), b*np.sin(v)*np.sin(u), c*np.cos(v)]),
            u_range=(0, TAU), v_range=(0, PI), resolution=(32,16),
            checkerboard_colors=[GREEN_D, GREEN_E], fill_opacity=0.6
        ).shift(LEFT*3)

        p = 1.0
        paraboloid = Surface(
            lambda u,v: np.array([u*np.cos(v), u*np.sin(v), (u*u)/(2*p)]),
            u_range=(0, 2.2), v_range=(0, TAU), resolution=(32,16),
            checkerboard_colors=[YELLOW_D, YELLOW_E], fill_opacity=0.65
        )

        a2,b2,c2 = 1.2, 0.9, 1.0
        hyper_one = Surface(
            lambda u,v: np.array([a2*np.cosh(u)*np.cos(v), b2*np.cosh(u)*np.sin(v), c2*np.sinh(u)]),
            u_range=(-1.0, 1.0), v_range=(0, TAU), resolution=(40,20),
            checkerboard_colors=[RED_D, RED_E], fill_opacity=0.55
        ).shift(RIGHT*3)

        self.begin_ambient_camera_rotation(rate=0.05)
        self.play(FadeIn(ellipsoid), run_time=1.0)
        self.play(FadeIn(paraboloid), run_time=1.0)
        self.play(FadeIn(hyper_one), run_time=1.0)
        self.wait(2.0)
        self.stop_ambient_camera_rotation()
        self.play(FadeOut(axes, ellipsoid, paraboloid, hyper_one, title), run_time=0.6)

    # ---------- 结尾 ----------
    def closing_animation(self):
        self.set_camera_orientation(phi=0*DEGREES, theta=-90*DEGREES, zoom=1.0)
        title = Text("总结", font_size=48).to_edge(UP)
        bullets = VGroup(
            Text("• 几何起源：平面截双圆锥", font_size=28),
            Text("• 统一视角：焦点-准线与离心率", font_size=28),
            Text("• 标准方程与参数关系", font_size=28),
            Text("• 高光性质：椭圆距离和、抛物线反射", font_size=28),
            Text("• 拓展：天体轨道、心形函数、3D曲面", font_size=28),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).next_to(title, DOWN, buff=0.6)
        self.play(Write(title), LaggedStartMap(FadeIn, bullets, lag_ratio=0.15), run_time=2.0)
        self.wait(1.0)
        thanks = Text("感谢观看！", font_size=52, color=TEAL)
        self.play(FadeOut(title, bullets), FadeIn(thanks, scale=1.1), run_time=1.2)
        self.wait(1.0)