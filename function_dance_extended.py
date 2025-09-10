from manim import *
import numpy as np
import random
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from my_manim_setup import *

class FunctionDanceExtended(ThreeDScene):
    def construct(self):
        # 设置默认配置
        self.camera.background_color = "#0a0e27"

        # ========== 序幕：宇宙中的数学之声 ==========
        self.prologue_universe_of_math()

        # ========== 第一幕：一维函数的觉醒（3分钟）==========
        self.act1_awakening_of_functions()

        # ========== 第二幕：二维平面的芭蕾（3分钟）==========
        self.act2_planar_ballet()

        # ========== 第三幕：极坐标的圆舞曲（3分钟）==========
        self.act3_polar_waltz()

        # ========== 第四幕：参数方程的探戈（3分钟）==========
        self.act4_parametric_tango()

        # ========== 第五幕：心形函数的浪漫诗（2分钟）==========
        self.act5_heart_romance()

        # ========== 第六幕：三维空间的交响曲（3分钟）==========
        self.act6_3d_symphony()

        # ========== 第七幕：分形与混沌的狂想（3分钟）==========
        self.act7_fractal_chaos()

        # ========== 第八幕：傅里叶的魔法（2分钟）==========
        self.act8_fourier_magic()

        # ========== 终幕：函数宇宙的狂欢（2分钟）==========
        self.finale_universal_celebration()

    def prologue_universe_of_math(self):
        """序幕：宇宙中的数学之声"""
        # 星空背景
        stars = VGroup()
        for _ in range(100):
            star = Dot(
                point=np.array([
                    np.random.uniform(-7, 7),
                    np.random.uniform(-4, 4),
                    0
                ]),
                radius=np.random.uniform(0.01, 0.03),
                color=WHITE
            ).set_opacity(np.random.uniform(0.3, 1))
            stars.add(star)

        self.add(stars)

        # 标题渐现
        title = VGroup(
            Text("函数之舞", font="STSong", font_size=84, gradient=(BLUE, PURPLE, PINK)),
            Text("The Dance of Functions", font_size=42, color=GREY_A)
        ).arrange(DOWN, buff=0.3)

        subtitle = Text(
            "一场数学与艺术的视觉盛宴",
            font="STSong", font_size=32, color=WHITE
        ).next_to(title, DOWN, buff=1)

        self.play(
            Write(title[0]),
            stars.animate.set_opacity(0.2),
            run_time=3
        )
        self.play(FadeIn(title[1], shift=UP), run_time=1)
        self.play(Write(subtitle), run_time=2)
        self.wait(2)

        # 引言
        quote = VGroup(
            Text("\"Mathematics is the music of reason\"", font_size=28, slant=ITALIC),
            Text("- James Joseph Sylvester", font_size=24, color=GREY_B)
        ).arrange(DOWN).next_to(subtitle, DOWN, buff=1)

        self.play(Write(quote), run_time=2)
        self.wait(2)

        # 清理并过渡
        self.play(
            FadeOut(title),
            FadeOut(subtitle),
            FadeOut(quote),
            FadeOut(stars),
            run_time=2
        )
        self.wait(0.5)

    def act1_awakening_of_functions(self):
        """第一幕：一维函数的觉醒"""
        # 章节标题动画
        chapter_title = Text("第一幕：一维函数的觉醒", font="STSong", font_size=48)
        chapter_subtitle = Text("The Awakening of One-Dimensional Functions", font_size=24, color=GREY_A)
        chapter_group = VGroup(chapter_title, chapter_subtitle).arrange(DOWN)

        self.play(Write(chapter_title), run_time=1.5)
        self.play(FadeIn(chapter_subtitle, shift=UP), run_time=0.5)
        self.wait(1)
        self.play(FadeOut(chapter_group))

        # 创建坐标轴
        axes = Axes(
            x_range=[-3 * PI, 3 * PI, PI],
            y_range=[-3, 3, 1],
            x_length=12,
            y_length=6,
            axis_config={
                "color": BLUE_D,
                "include_numbers": False,
                "include_ticks": True
            },
            tips=False
        )
        axes_labels = axes.get_axis_labels(
            x_label=MathTex("x"),
            y_label=MathTex("y")
        )

        grid = NumberPlane(
            x_range=[-3 * PI, 3 * PI],
            y_range=[-3, 3],
            x_length=12,
            y_length=6,
            background_line_style={
                "stroke_color": BLUE_E,
                "stroke_width": 1,
                "stroke_opacity": 0.3
            }
        )

        self.play(Create(grid), run_time=1)
        self.play(Create(axes), Write(axes_labels), run_time=1.5)

        # 1. 基础三角函数的苏醒
        sin_func = axes.plot(lambda x: np.sin(x), color=BLUE, stroke_width=3)
        sin_label = MathTex(r"f(x) = \sin(x)", color=BLUE).to_corner(UR)

        # 从直线逐渐变成正弦
        straight_line = axes.plot(lambda x: 0, color=BLUE, stroke_width=3)
        self.play(Create(straight_line), run_time=1)
        self.play(
            Transform(straight_line, sin_func),
            Write(sin_label),
            run_time=2
        )
        self.wait(1)

        # 2. 振幅的呼吸
        amplitude_tracker = ValueTracker(1)

        animated_sin = always_redraw(lambda: axes.plot(
            lambda x: amplitude_tracker.get_value() * np.sin(x),
            color=BLUE,
            stroke_width=3
        ))

        self.play(FadeOut(straight_line))
        self.add(animated_sin)

        # 振幅变化动画
        self.play(amplitude_tracker.animate.set_value(2), run_time=1)
        self.play(amplitude_tracker.animate.set_value(0.5), run_time=1)
        self.play(amplitude_tracker.animate.set_value(1.5), run_time=1)

        # 更新标签
        animated_label = MathTex(r"f(x) = 1.5\sin(x)", color=BLUE).to_corner(UR)
        self.play(Transform(sin_label, animated_label), run_time=0.5)

        # 3. 频率的舞动
        freq_tracker = ValueTracker(1)

        freq_sin = always_redraw(lambda: axes.plot(
            lambda x: 1.5 * np.sin(freq_tracker.get_value() * x),
            color=interpolate_color(BLUE, PURPLE, (freq_tracker.get_value() - 1) / 3),
            stroke_width=3
        ))

        self.remove(animated_sin)
        self.add(freq_sin)

        # 频率变化
        for freq in [2, 3, 4]:
            new_label = MathTex(f"f(x) = 1.5\\sin({freq}x)",
                                color=interpolate_color(BLUE, PURPLE, (freq - 1) / 3)).to_corner(UR)
            self.play(
                freq_tracker.animate.set_value(freq),
                Transform(sin_label, new_label),
                run_time=1.5
            )
            self.wait(0.5)

        # 4. 相位的漂移
        phase_tracker = ValueTracker(0)

        phase_sin = always_redraw(lambda: axes.plot(
            lambda x: 1.5 * np.sin(4 * x + phase_tracker.get_value()),
            color=PURPLE,
            stroke_width=3
        ))

        self.remove(freq_sin)
        self.add(phase_sin)

        # 相位动画
        self.play(phase_tracker.animate.set_value(PI), run_time=2)
        self.play(phase_tracker.animate.set_value(2 * PI), run_time=2)

        # 5. 多函数的和谐共舞
        self.play(FadeOut(phase_sin), FadeOut(sin_label))

        # 创建函数族
        func_family = VGroup()
        colors = [BLUE, GREEN, YELLOW, ORANGE, RED]
        labels_group = VGroup()

        for i, color in enumerate(colors):
            func = axes.plot(
                lambda x, n=i + 1: np.sin(n * x) / n,
                color=color,
                stroke_width=2
            )
            func_family.add(func)

            label = MathTex(f"\\frac{{\\sin({i + 1}x)}}{{{i + 1}}}",
                            color=color, font_size=24)
            labels_group.add(label)

        labels_group.arrange(DOWN, buff=0.2).to_corner(UR)

        # 逐个添加
        for func, label in zip(func_family, labels_group):
            self.play(Create(func), Write(label), run_time=0.8)

        # 6. 傅里叶级数的形成
        self.wait(1)

        fourier_sum = axes.plot(
            lambda x: sum(np.sin((2 * k + 1) * x) / (2 * k + 1) for k in range(5)),
            color=WHITE,
            stroke_width=4
        )

        fourier_label = MathTex(
            r"f(x) = \sum_{k=0}^{4} \frac{\sin((2k+1)x)}{2k+1}",
            color=WHITE,
            font_size=28
        ).to_corner(UL)

        self.play(
            FadeOut(func_family),
            FadeOut(labels_group),
            Create(fourier_sum),
            Write(fourier_label),
            run_time=2
        )

        # 展示方波逼近
        square_wave_text = Text("方波的诞生", font="STSong", font_size=32, color=YELLOW).next_to(fourier_label, DOWN)
        self.play(Write(square_wave_text), run_time=1)
        self.wait(2)

        # 7. 指数函数的生长
        self.play(
            FadeOut(fourier_sum),
            FadeOut(fourier_label),
            FadeOut(square_wave_text)
        )

        exp_func = axes.plot(
            lambda x: np.exp(x / 3) - 1,
            x_range=[-3 * PI, 2],
            color=GREEN,
            stroke_width=3
        )
        exp_label = MathTex(r"f(x) = e^{x/3} - 1", color=GREEN).to_corner(UR)

        self.play(Create(exp_func), Write(exp_label), run_time=2)

        # 8. 对数函数的平衡
        log_func = axes.plot(
            lambda x: np.log(x + 3 * PI + 0.1),
            x_range=[-3 * PI, 3 * PI],
            color=ORANGE,
            stroke_width=3
        )
        log_label = MathTex(r"g(x) = \ln(x + 3\pi)", color=ORANGE).next_to(exp_label, DOWN)

        self.play(Create(log_func), Write(log_label), run_time=2)

        # 展示指数与对数的对称性
        symmetry_text = Text("指数与对数的对称之美", font="STSong", font_size=28, color=WHITE).to_corner(DL)
        self.play(Write(symmetry_text), run_time=1)
        self.wait(2)

        # 清理场景
        self.play(
            FadeOut(grid),
            FadeOut(axes),
            FadeOut(axes_labels),
            FadeOut(exp_func),
            FadeOut(log_func),
            FadeOut(exp_label),
            FadeOut(log_label),
            FadeOut(symmetry_text),
            run_time=2
        )
        self.wait(0.5)

    def act2_planar_ballet(self):
        """第二幕：二维平面的芭蕾"""
        # 章节标题
        chapter_title = Text("第二幕：二维平面的芭蕾", font="STSong", font_size=48)
        chapter_subtitle = Text("Ballet in the Two-Dimensional Plane", font_size=24, color=GREY_A)
        chapter_group = VGroup(chapter_title, chapter_subtitle).arrange(DOWN)

        self.play(Write(chapter_title), run_time=1.5)
        self.play(FadeIn(chapter_subtitle, shift=UP), run_time=0.5)
        self.wait(1)
        self.play(FadeOut(chapter_group))

        # 创建坐标平面
        plane = NumberPlane(
            x_range=[-6, 6, 1],
            y_range=[-4, 4, 1],
            x_length=12,
            y_length=8,
            background_line_style={
                "stroke_color": BLUE_E,
                "stroke_width": 1,
                "stroke_opacity": 0.2
            }
        )
        self.play(Create(plane), run_time=1.5)

        # 1. 圆形家族的圆舞
        circles_group = VGroup()
        circle_colors = [BLUE, TEAL, GREEN, YELLOW, ORANGE]

        for i, color in enumerate(circle_colors):
            radius = 0.5 + i * 0.5
            circle = Circle(radius=radius, color=color, stroke_width=2)
            circles_group.add(circle)

        self.play(
            *[Create(circle) for circle in circles_group],
            run_time=2
        )

        # 同心圆的呼吸
        self.play(
            *[circle.animate.scale(1.2) for circle in circles_group],
            run_time=1
        )
        self.play(
            *[circle.animate.scale(1 / 1.2) for circle in circles_group],
            run_time=1
        )

        # 2. 椭圆的变形舞蹈
        self.play(FadeOut(circles_group))

        ellipse_tracker = ValueTracker(1)

        ellipse = always_redraw(lambda: ParametricFunction(
            lambda t: np.array([
                3 * np.cos(t),
                ellipse_tracker.get_value() * np.sin(t),
                0
            ]),
            t_range=[0, 2 * PI],
            color=PURPLE,
            stroke_width=3
        ))

        ellipse_label = always_redraw(lambda: MathTex(
            f"\\frac{{x^2}}{{9}} + \\frac{{y^2}}{{{ellipse_tracker.get_value() ** 2:.1f}}} = 1",
            color=PURPLE
        ).to_corner(UR))

        self.add(ellipse, ellipse_label)
        self.play(Create(ellipse), Write(ellipse_label), run_time=2)

        # 椭圆变形动画
        for val in [2, 0.5, 3, 1]:
            self.play(ellipse_tracker.animate.set_value(val), run_time=1.5)

        # 3. 李萨茹图形的编织
        self.play(FadeOut(ellipse), FadeOut(ellipse_label))

        lissajous_params = [
            (3, 2, 0, BLUE),
            (5, 4, PI / 4, GREEN),
            (7, 6, PI / 3, ORANGE)
        ]

        lissajous_group = VGroup()

        for a, b, delta, color in lissajous_params:
            liss = ParametricFunction(
                lambda t: np.array([
                    3 * np.sin(a * t + delta),
                    3 * np.sin(b * t),
                    0
                ]),
                t_range=[0, 2 * PI],
                color=color,
                stroke_width=2
            )
            lissajous_group.add(liss)

        # 逐个绘制李萨茹图形
        for liss in lissajous_group:
            self.play(Create(liss), run_time=1.5)

        # 旋转整体
        self.play(Rotate(lissajous_group, angle=PI / 2), run_time=2)
        self.wait(1)

        # 4. 玫瑰线的绽放
        self.play(FadeOut(lissajous_group))

        rose_petals = ValueTracker(3)

        rose = always_redraw(lambda: ParametricFunction(
            lambda t: np.array([
                3 * np.sin(rose_petals.get_value() * t) * np.cos(t),
                3 * np.sin(rose_petals.get_value() * t) * np.sin(t),
                0
            ]),
            t_range=[0, 2 * PI],
            color=interpolate_color(RED, PINK, (rose_petals.get_value() - 3) / 5),
            stroke_width=3
        ))

        rose_label = always_redraw(lambda: MathTex(
            f"r = 3\\sin({int(rose_petals.get_value())}\\theta)",
            color=interpolate_color(RED, PINK, (rose_petals.get_value() - 3) / 5)
        ).to_corner(UR))

        self.add(rose, rose_label)
        self.play(Create(rose), Write(rose_label), run_time=2)

        # 改变花瓣数
        for petals in [4, 5, 6, 7, 8]:
            self.play(rose_petals.animate.set_value(petals), run_time=1)
            self.wait(0.5)

        # 5. 螺旋线的展开
        self.play(FadeOut(rose), FadeOut(rose_label))

        # 阿基米德螺旋
        archimedean = ParametricFunction(
            lambda t: np.array([
                t * np.cos(t) / 2,
                t * np.sin(t) / 2,
                0
            ]),
            t_range=[0, 6 * PI],
            color=YELLOW,
            stroke_width=3
        )

        arch_label = MathTex(r"r = \frac{\theta}{2}", color=YELLOW).to_corner(UR)

        self.play(Create(archimedean), Write(arch_label), run_time=3)

        # 对数螺旋
        logarithmic = ParametricFunction(
            lambda t: np.array([
                np.exp(0.1 * t) * np.cos(t) / 2,
                np.exp(0.1 * t) * np.sin(t) / 2,
                0
            ]),
            t_range=[0, 4 * PI],
            color=TEAL,
            stroke_width=3
        )

        log_label = MathTex(r"r = \frac{1}{2}e^{0.1\theta}", color=TEAL).next_to(arch_label, DOWN)

        self.play(Create(logarithmic), Write(log_label), run_time=3)

        # 6. 双曲线的对称
        self.play(
            FadeOut(archimedean),
            FadeOut(logarithmic),
            FadeOut(arch_label),
            FadeOut(log_label)
        )

        hyperbola1 = ParametricFunction(
            lambda t: np.array([
                2 * np.cosh(t),
                2 * np.sinh(t),
                0
            ]),
            t_range=[-2, 2],
            color=BLUE,
            stroke_width=3
        )

        hyperbola2 = ParametricFunction(
            lambda t: np.array([
                -2 * np.cosh(t),
                2 * np.sinh(t),
                0
            ]),
            t_range=[-2, 2],
            color=BLUE,
            stroke_width=3
        )

        hyp_label = MathTex(r"\frac{x^2}{4} - \frac{y^2}{4} = 1", color=BLUE).to_corner(UR)

        self.play(
            Create(hyperbola1),
            Create(hyperbola2),
            Write(hyp_label),
            run_time=2
        )

        # 渐近线
        asymptote1 = Line(
            start=np.array([-6, -6, 0]),
            end=np.array([6, 6, 0]),
            color=GREY,
            stroke_width=1
        )
        asymptote2 = Line(
            start=np.array([-6, 6, 0]),
            end=np.array([6, -6, 0]),
            color=GREY,
            stroke_width=1
        )

        self.play(
            Create(asymptote1),
            Create(asymptote2),
            run_time=1
        )
        self.wait(2)

        # 清理场景
        self.play(
            FadeOut(plane),
            FadeOut(hyperbola1),
            FadeOut(hyperbola2),
            FadeOut(asymptote1),
            FadeOut(asymptote2),
            FadeOut(hyp_label),
            run_time=2
        )
        self.wait(0.5)

    def act3_polar_waltz(self):
        """第三幕：极坐标的圆舞曲"""
        # 章节标题
        chapter_title = Text("第三幕：极坐标的圆舞曲", font="STSong", font_size=48)
        chapter_subtitle = Text("Waltz in Polar Coordinates", font_size=24, color=GREY_A)
        chapter_group = VGroup(chapter_title, chapter_subtitle).arrange(DOWN)

        self.play(Write(chapter_title), run_time=1.5)
        self.play(FadeIn(chapter_subtitle, shift=UP), run_time=0.5)
        self.wait(1)
        self.play(FadeOut(chapter_group))

        # 创建极坐标系
        polar_plane = PolarPlane(
            radius_max=4,
            size=8,
            azimuth_step=12,
            radius_step=0.5
        ).set_stroke(BLUE_D, 1, opacity=0.4)

        self.play(Create(polar_plane), run_time=2)

        # 1. 心形线家族
        cardioid_family = VGroup()
        cardioid_params = [
            (1, 1, RED, r"r = 1 + \cos\theta"),
            (1, 0.5, PINK, r"r = 1 + 0.5\cos\theta"),
            (1, 2, MAROON, r"r = 1 + 2\cos\theta")
        ]

        labels_group = VGroup()

        for a, b, color, tex in cardioid_params:
            cardioid = ParametricFunction(
                lambda t: polar_plane.polar_to_point(a + b * np.cos(t), t),
                t_range=[0, 2 * PI],
                color=color,
                stroke_width=2
            )
            cardioid_family.add(cardioid)

            label = MathTex(tex, color=color, font_size=28)
            labels_group.add(label)

        labels_group.arrange(DOWN, buff=0.2).to_corner(UR)

        for card, label in zip(cardioid_family, labels_group):
            self.play(Create(card), Write(label), run_time=1.5)

        self.wait(1)
        self.play(FadeOut(cardioid_family), FadeOut(labels_group))

        # 2. 蝴蝶曲线
        butterfly = ParametricFunction(
            lambda t: polar_plane.polar_to_point(
                np.exp(np.sin(t)) - 2 * np.cos(4 * t) + np.sin((2 * t - PI) / 24) ** 5,
                t
            ),
            t_range=[0, 12 * PI],
            color=PURPLE,
            stroke_width=2
        )

        butterfly_label = Text("蝴蝶曲线", font="STSong", font_size=32, color=PURPLE).to_corner(UR)
        butterfly_eq = MathTex(
            r"r = e^{\sin\theta} - 2\cos(4\theta) + \sin^5\left(\frac{2\theta - \pi}{24}\right)",
            color=PURPLE,
            font_size=20
        ).next_to(butterfly_label, DOWN)

        self.play(Create(butterfly), Write(butterfly_label), run_time=4)
        self.play(Write(butterfly_eq), run_time=1)
        self.wait(2)

        # 3. 花瓣曲线动态变化
        self.play(FadeOut(butterfly), FadeOut(butterfly_label), FadeOut(butterfly_eq))

        petal_tracker = ValueTracker(2)
        amplitude_tracker = ValueTracker(2)

        dynamic_rose = always_redraw(lambda: ParametricFunction(
            lambda t: polar_plane.polar_to_point(
                amplitude_tracker.get_value() * np.sin(petal_tracker.get_value() * t),
                t
            ),
            t_range=[0, 2 * PI],
            color=interpolate_color(BLUE, PURPLE, (petal_tracker.get_value() - 2) / 6),
            stroke_width=3
        ))

        dynamic_label = always_redraw(lambda: MathTex(
            f"r = {amplitude_tracker.get_value():.1f}\\sin({petal_tracker.get_value():.1f}\\theta)",
            color=interpolate_color(BLUE, PURPLE, (petal_tracker.get_value() - 2) / 6)
        ).to_corner(UR))

        self.add(dynamic_rose, dynamic_label)
        self.play(Create(dynamic_rose), Write(dynamic_label), run_time=2)

        # 花瓣数变化
        for petals in [3, 4, 5, 6, 7, 8]:
            self.play(petal_tracker.animate.set_value(petals), run_time=1)

        # 振幅变化
        self.play(amplitude_tracker.animate.set_value(3), run_time=1)
        self.play(amplitude_tracker.animate.set_value(1), run_time=1)
        self.play(amplitude_tracker.animate.set_value(2), run_time=1)

        # 4. 螺旋线系列
        self.play(FadeOut(dynamic_rose), FadeOut(dynamic_label))

        # 费马螺旋
        fermat_spiral = ParametricFunction(
            lambda t: polar_plane.polar_to_point(np.sqrt(t), t),
            t_range=[0, 8 * PI],
            color=GREEN,
            stroke_width=2
        )

        fermat_label = MathTex(r"r = \sqrt{\theta}", color=GREEN).to_corner(UR)

        self.play(Create(fermat_spiral), Write(fermat_label), run_time=3)

        # 双曲螺旋
        hyperbolic_spiral = ParametricFunction(
            lambda t: polar_plane.polar_to_point(4 / t if t > 0.5 else 8, t),
            t_range=[0.5, 4 * PI],
            color=ORANGE,
            stroke_width=2
        )

        hyp_spiral_label = MathTex(r"r = \frac{4}{\theta}", color=ORANGE).next_to(fermat_label, DOWN)

        self.play(Create(hyperbolic_spiral), Write(hyp_spiral_label), run_time=3)

        # 5. 复合曲线
        self.play(
            FadeOut(fermat_spiral),
            FadeOut(hyperbolic_spiral),
            FadeOut(fermat_label),
            FadeOut(hyp_spiral_label)
        )

        # 创建复合图案
        compound_curve = ParametricFunction(
            lambda t: polar_plane.polar_to_point(
                2 + np.sin(6 * t) * np.cos(4 * t),
                t
            ),
            t_range=[0, 2 * PI],
            color=TEAL,
            stroke_width=3
        )

        compound_label = MathTex(r"r = 2 + \sin(6\theta)\cos(4\theta)", color=TEAL).to_corner(UR)

        self.play(Create(compound_curve), Write(compound_label), run_time=3)

        # 旋转效果
        self.play(Rotate(compound_curve, angle=2 * PI, about_point=ORIGIN), run_time=4)

        # 清理场景
        self.play(
            FadeOut(polar_plane),
            FadeOut(compound_curve),
            FadeOut(compound_label),
            run_time=2
        )
        self.wait(0.5)

    def act4_parametric_tango(self):
        """第四幕：参数方程的探戈"""
        # 章节标题
        chapter_title = Text("第四幕：参数方程的探戈", font="STSong", font_size=48)
        chapter_subtitle = Text("Tango of Parametric Equations", font_size=24, color=GREY_A)
        chapter_group = VGroup(chapter_title, chapter_subtitle).arrange(DOWN)

        self.play(Write(chapter_title), run_time=1.5)
        self.play(FadeIn(chapter_subtitle, shift=UP), run_time=0.5)
        self.wait(1)
        self.play(FadeOut(chapter_group))

        # 创建坐标系
        axes = Axes(
            x_range=[-5, 5, 1],
            y_range=[-5, 5, 1],
            x_length=10,
            y_length=10,
            axis_config={"color": BLUE_D, "include_ticks": False},
            tips=False
        )

        self.play(Create(axes), run_time=1.5)

        # 1. 摆线（Cycloid）
        cycloid = ParametricFunction(
            lambda t: np.array([
                t - np.sin(t),
                1 - np.cos(t),
                0
            ]) + np.array([-3, -3, 0]),
            t_range=[0, 4 * PI],
            color=BLUE,
            stroke_width=3
        )

        cycloid_label = VGroup(
            Text("摆线", font="STSong", font_size=28, color=BLUE),
            MathTex(r"\begin{cases} x = t - \sin t \\ y = 1 - \cos t \end{cases}",
                    color=BLUE, font_size=24)
        ).arrange(DOWN, buff=0.1).to_corner(UR)

        # 创建滚动圆动画
        rolling_circle = Circle(radius=1, color=BLUE_B, stroke_width=2)
        rolling_circle.move_to(np.array([-3, -2, 0]))

        dot = Dot(color=YELLOW, radius=0.08)
        dot.move_to(rolling_circle.get_bottom())

        self.play(Create(cycloid), Write(cycloid_label), run_time=3)
        self.add(rolling_circle, dot)

        # 滚动动画
        path = TracedPath(dot.get_center, stroke_color=YELLOW, stroke_width=2)
        self.add(path)

        for t in np.linspace(0, 2 * PI, 30):
            rolling_circle.move_to(np.array([t - 3, -2, 0]))
            dot.move_to(rolling_circle.get_center() +
                        np.array([np.sin(t), -np.cos(t), 0]))
            self.wait(0.05)

        self.play(FadeOut(rolling_circle), FadeOut(dot), FadeOut(path))

        # 2. 星形线（Astroid）
        self.play(FadeOut(cycloid), FadeOut(cycloid_label))

        astroid = ParametricFunction(
            lambda t: np.array([
                3 * np.cos(t) ** 3,
                3 * np.sin(t) ** 3,
                0
            ]),
            t_range=[0, 2 * PI],
            color=PURPLE,
            stroke_width=3
        )

        astroid_label = VGroup(
            Text("星形线", font="STSong", font_size=28, color=PURPLE),
            MathTex(r"\begin{cases} x = 3\cos^3 t \\ y = 3\sin^3 t \end{cases}",
                    color=PURPLE, font_size=24)
        ).arrange(DOWN, buff=0.1).to_corner(UR)

        self.play(Create(astroid), Write(astroid_label), run_time=3)

        # 内接圆动画
        inner_circle = Circle(radius=3 / 4, color=PURPLE_B, stroke_width=1)
        self.play(Create(inner_circle), run_time=1)
        self.play(Rotate(inner_circle, angle=2 * PI), run_time=3)
        self.play(FadeOut(inner_circle))

        # 3. 魔术曲线
        self.play(FadeOut(astroid), FadeOut(astroid_label))

        t_tracker = ValueTracker(0)

        magic_curve = always_redraw(lambda: ParametricFunction(
            lambda u: np.array([
                3 * np.cos(u) + np.cos(3 * u) * np.cos(t_tracker.get_value()),
                3 * np.sin(u) + np.sin(3 * u) * np.sin(t_tracker.get_value()),
                0
            ]),
            t_range=[0, 2 * PI],
            color=interpolate_color(GREEN, YELLOW, t_tracker.get_value() / (2 * PI)),
            stroke_width=3
        ))

        magic_label = Text("魔术曲线", font="STSong", font_size=28, color=GREEN).to_corner(UR)

        self.add(magic_curve)
        self.play(Create(magic_curve), Write(magic_label), run_time=2)

        # 动态变化
        self.play(t_tracker.animate.set_value(2 * PI), run_time=4, rate_func=linear)

        # 4. 双纽线
        self.play(FadeOut(magic_curve), FadeOut(magic_label))

        lemniscate = ParametricFunction(
            lambda t: np.array([
                4 * np.cos(t) / (1 + np.sin(t) ** 2),
                4 * np.sin(t) * np.cos(t) / (1 + np.sin(t) ** 2),
                0
            ]),
            t_range=[0, 2 * PI],
            color=ORANGE,
            stroke_width=3
        )

        lemn_label = VGroup(
            Text("双纽线", font="STSong", font_size=28, color=ORANGE),
            MathTex(r"(x^2 + y^2)^2 = 16(x^2 - y^2)",
                    color=ORANGE, font_size=24)
        ).arrange(DOWN, buff=0.1).to_corner(UR)

        self.play(Create(lemniscate), Write(lemn_label), run_time=3)

        # 添加对称轴
        sym_line1 = DashedLine(
            start=np.array([-5, -5, 0]),
            end=np.array([5, 5, 0]),
            color=GREY,
            stroke_width=1
        )
        sym_line2 = DashedLine(
            start=np.array([-5, 5, 0]),
            end=np.array([5, -5, 0]),
            color=GREY,
            stroke_width=1
        )

        self.play(Create(sym_line1), Create(sym_line2), run_time=1)
        self.wait(1)
        self.play(FadeOut(sym_line1), FadeOut(sym_line2))

        # 5. 组合参数曲线艺术
        self.play(FadeOut(lemniscate), FadeOut(lemn_label))

        # 创建多条曲线的组合
        art_curves = VGroup()

        for i in range(5):
            phase = i * PI / 5
            curve = ParametricFunction(
                lambda t, p=phase: np.array([
                    (3 - i * 0.5) * np.cos(t + p),
                    (3 - i * 0.5) * np.sin(2 * t + p),
                    0
                ]),
                t_range=[0, 2 * PI],
                color=interpolate_color(RED, BLUE, i / 4),
                stroke_width=2
            )
            art_curves.add(curve)

        self.play(*[Create(curve) for curve in art_curves], run_time=3)

        # 旋转组合
        self.play(Rotate(art_curves, angle=PI), run_time=3)

        # 清理场景
        self.play(
            FadeOut(axes),
            FadeOut(art_curves),
            run_time=2
        )
        self.wait(0.5)

    def act5_heart_romance(self):
        """第五幕：心形函数的浪漫诗"""
        # 章节标题
        chapter_title = Text("第五幕：心形函数的浪漫诗", font="STSong", font_size=48, color=PINK)
        chapter_subtitle = Text("Romance of Heart Functions", font_size=24, color=GREY_A)
        chapter_group = VGroup(chapter_title, chapter_subtitle).arrange(DOWN)

        self.play(Write(chapter_title), run_time=1.5)
        self.play(FadeIn(chapter_subtitle, shift=UP), run_time=0.5)
        self.wait(1)
        self.play(FadeOut(chapter_group))

        # 创建坐标系
        axes = Axes(
            x_range=[-4, 4, 1],
            y_range=[-4, 5, 1],
            x_length=8,
            y_length=9,
            axis_config={"color": PINK, "include_ticks": False},
            tips=False
        )

        self.play(Create(axes), run_time=1)

        # 1. 经典参数心形
        classic_heart = ParametricFunction(
            lambda t: np.array([
                16 * np.sin(t) ** 3 / 5,
                (13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t)) / 5,
                0
            ]),
            t_range=[0, 2 * PI],
            color=RED,
            stroke_width=4
        )

        self.play(Create(classic_heart), run_time=3)

        # 添加填充
        filled_heart = classic_heart.copy().set_fill(RED, opacity=0.3)
        self.play(FadeIn(filled_heart), run_time=1)

        # 心跳效果
        for _ in range(5):
            self.play(
                filled_heart.animate.scale(1.1).set_fill(RED, opacity=0.5),
                run_time=0.4
            )
            self.play(
                filled_heart.animate.scale(1 / 1.1).set_fill(RED, opacity=0.3),
                run_time=0.4
            )

        # 2. 爱的方程式
        love_equation = MathTex(
            r"(x^2 + y^2 - 1)^3 = x^2 y^3",
            color=PINK,
            font_size=36
        ).to_corner(UR)

        self.play(Write(love_equation), run_time=2)

        # 3. 心形变奏曲
        self.play(FadeOut(classic_heart), FadeOut(filled_heart))

        # 创建多个不同大小和颜色的心形
        hearts_symphony = VGroup()
        heart_colors = [RED, PINK, MAROON, PURPLE, "#FF69B4"]

        for i, color in enumerate(heart_colors):
            scale = 0.2 + i * 0.15
            offset = np.array([
                2 * np.cos(i * 2 * PI / 5),
                2 * np.sin(i * 2 * PI / 5),
                0
            ])

            heart = ParametricFunction(
                lambda t, s=scale: np.array([
                    s * 16 * np.sin(t) ** 3 / 5,
                    s * (13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t)) / 5,
                    0
                ]),
                t_range=[0, 2 * PI],
                color=color,
                stroke_width=3
            ).shift(offset)

            hearts_symphony.add(heart)

        self.play(*[Create(heart) for heart in hearts_symphony], run_time=2)

        # 让心形们旋转
        self.play(
            Rotate(hearts_symphony, angle=2 * PI, about_point=ORIGIN),
            run_time=4,
            rate_func=smooth
        )

        # 4. 心形万花筒
        self.play(FadeOut(hearts_symphony))

        kaleidoscope = VGroup()
        for angle in np.linspace(0, 2 * PI, 8, endpoint=False):
            heart = classic_heart.copy().rotate(angle).set_color(
                interpolate_color(RED, PURPLE, angle / (2 * PI))
            ).scale(0.5)
            kaleidoscope.add(heart)

        self.play(*[Create(h) for h in kaleidoscope], run_time=2)
        self.play(Rotate(kaleidoscope, angle=PI / 4), run_time=2)

        # 5. 爱的诗句
        self.play(FadeOut(kaleidoscope), FadeOut(love_equation))

        poem = VGroup(
            Text("在数学的语言里", font="STSong", font_size=32, color=WHITE),
            Text("爱是最美的曲线", font="STSong", font_size=32, color=PINK),
            Text("每一个参数", font="STSong", font_size=32, color=WHITE),
            Text("都诉说着永恒", font="STSong", font_size=32, color=RED)
        ).arrange(DOWN, buff=0.3)

        for line in poem:
            self.play(Write(line), run_time=1)

        self.wait(2)

        # 清理场景
        self.play(
            FadeOut(axes),
            FadeOut(poem),
            run_time=2
        )
        self.wait(0.5)

    def act6_3d_symphony(self):
        """第六幕：三维空间的交响曲"""
        # 章节标题
        chapter_title = Text("第六幕：三维空间的交响曲", font="STSong", font_size=48)
        chapter_subtitle = Text("Symphony in Three-Dimensional Space", font_size=24, color=GREY_A)
        chapter_group = VGroup(chapter_title, chapter_subtitle).arrange(DOWN)

        self.play(Write(chapter_title), run_time=1.5)
        self.play(FadeIn(chapter_subtitle, shift=UP), run_time=0.5)
        self.wait(1)
        self.play(FadeOut(chapter_group))

        # 创建3D坐标系
        axes = ThreeDAxes(
            x_range=[-5, 5, 1],
            y_range=[-5, 5, 1],
            z_range=[-5, 5, 1],
            x_length=7,
            y_length=7,
            z_length=7
        )

        self.set_camera_orientation(phi=60 * DEGREES, theta=-45 * DEGREES)
        self.play(Create(axes), run_time=2)

        # 1. DNA双螺旋
        helix1 = ParametricFunction(
            lambda t: np.array([
                2 * np.cos(t),
                2 * np.sin(t),
                t / 2
            ]),
            t_range=[-3 * PI, 3 * PI],
            color=BLUE,
            stroke_width=4
        )

        helix2 = ParametricFunction(
            lambda t: np.array([
                2 * np.cos(t + PI),
                2 * np.sin(t + PI),
                t / 2
            ]),
            t_range=[-3 * PI, 3 * PI],
            color=RED,
            stroke_width=4
        )

        # 连接线
        connections = VGroup()
        for t in np.linspace(-3 * PI, 3 * PI, 20):
            line = Line(
                start=np.array([2 * np.cos(t), 2 * np.sin(t), t / 2]),
                end=np.array([2 * np.cos(t + PI), 2 * np.sin(t + PI), t / 2]),
                color=GREY,
                stroke_width=1
            )
            connections.add(line)

        self.play(Create(helix1), Create(helix2), run_time=3)
        self.play(Create(connections), run_time=2)

        self.begin_ambient_camera_rotation(rate=0.2)
        self.wait(3)
        self.stop_ambient_camera_rotation()

        # 2. 环面
        self.play(FadeOut(helix1), FadeOut(helix2), FadeOut(connections))

        torus = Surface(
            lambda u, v: np.array([
                (3 + np.cos(v)) * np.cos(u),
                (3 + np.cos(v)) * np.sin(u),
                np.sin(v)
            ]),
            u_range=[0, 2 * PI],
            v_range=[0, 2 * PI],
            resolution=(30, 30),
            fill_opacity=0.7,
            checkerboard_colors=[PURPLE_D, PURPLE_E]
        )

        self.play(Create(torus), run_time=3)
        self.begin_ambient_camera_rotation(rate=0.3)
        self.wait(4)
        self.stop_ambient_camera_rotation()

        # 3. 莫比乌斯带
        self.play(FadeOut(torus))

        mobius = Surface(
            lambda u, v: np.array([
                (2 + v * np.cos(u / 2)) * np.cos(u),
                (2 + v * np.cos(u / 2)) * np.sin(u),
                v * np.sin(u / 2)
            ]),
            u_range=[0, 2 * PI],
            v_range=[-1, 1],
            resolution=(30, 10),
            fill_opacity=0.7,
            checkerboard_colors=[GREEN_D, GREEN_E]
        )

        self.play(Create(mobius), run_time=3)
        self.move_camera(phi=75 * DEGREES, theta=-30 * DEGREES, run_time=2)
        self.begin_ambient_camera_rotation(rate=0.2)
        self.wait(4)
        self.stop_ambient_camera_rotation()

        # 4. 球面谐波
        self.play(FadeOut(mobius))

        spherical_harmonic = Surface(
            lambda u, v: np.array([
                2 * np.abs(np.cos(2 * v)) * np.sin(u) * np.cos(v),
                2 * np.abs(np.cos(2 * v)) * np.sin(u) * np.sin(v),
                2 * np.abs(np.cos(2 * v)) * np.cos(u)
            ]),
            u_range=[0, PI],
            v_range=[0, 2 * PI],
            resolution=(30, 30),
            fill_opacity=0.8,
            checkerboard_colors=[BLUE_D, TEAL]
        )

        self.play(Create(spherical_harmonic), run_time=3)
        self.begin_ambient_camera_rotation(rate=0.25)
        self.wait(4)
        self.stop_ambient_camera_rotation()

        # 5. 克莱因瓶的投影
        self.play(FadeOut(spherical_harmonic))

        klein_bottle = ParametricFunction(
            lambda t: np.array([
                (2 + np.cos(t)) * np.cos(2 * t),
                (2 + np.cos(t)) * np.sin(2 * t),
                np.sin(t) * 2
            ]),
            t_range=[0, 2 * PI],
            color=ORANGE,
            stroke_width=4
        )

        self.play(Create(klein_bottle), run_time=3)
        self.move_camera(phi=45 * DEGREES, theta=45 * DEGREES, run_time=3)

        # 清理场景
        self.play(
            FadeOut(axes),
            FadeOut(klein_bottle),
            run_time=2
        )

        # 重置相机
        self.set_camera_orientation(phi=0, theta=-90 * DEGREES)
        self.wait(0.5)

    def act7_fractal_chaos(self):
        """第七幕：分形与混沌的狂想"""
        # 章节标题
        chapter_title = Text("第七幕：分形与混沌的狂想", font="STSong", font_size=48)
        chapter_subtitle = Text("Rhapsody of Fractals and Chaos", font_size=24, color=GREY_A)
        chapter_group = VGroup(chapter_title, chapter_subtitle).arrange(DOWN)

        self.play(Write(chapter_title), run_time=1.5)
        self.play(FadeIn(chapter_subtitle, shift=UP), run_time=0.5)
        self.wait(1)
        self.play(FadeOut(chapter_group))

        # 1. 科赫雪花
        def koch_curve(start, end, depth):
            if depth == 0:
                return Line(start=start, end=end, color=BLUE, stroke_width=1)

            points = []
            points.append(start)

            # 计算三等分点
            p1 = start + (end - start) / 3
            p2 = start + 2 * (end - start) / 3

            # 计算突出点
            angle = np.arctan2(end[1] - start[1], end[0] - start[0])
            length = np.linalg.norm(end - start) / 3
            p_mid = p1 + length * np.array([
                np.cos(angle + PI / 3),
                np.sin(angle + PI / 3),
                0
            ])

            # 递归创建
            curves = VGroup()
            curves.add(koch_curve(start, p1, depth - 1))
            curves.add(koch_curve(p1, p_mid, depth - 1))
            curves.add(koch_curve(p_mid, p2, depth - 1))
            curves.add(koch_curve(p2, end, depth - 1))

            return curves

        # 创建雪花的三边
        triangle_points = [
            np.array([-3, -2, 0]),
            np.array([3, -2, 0]),
            np.array([0, 3, 0])
        ]

        snowflake = VGroup()
        for depth in range(5):
            iteration = VGroup()
            for i in range(3):
                start = triangle_points[i]
                end = triangle_points[(i + 1) % 3]
                iteration.add(koch_curve(start, end, depth))

            if depth == 0:
                self.play(Create(iteration), run_time=2)
                current = iteration
            else:
                self.play(Transform(current, iteration), run_time=1.5)
            self.wait(0.5)

        # 2. 龙形曲线
        self.play(FadeOut(current))

        def dragon_curve(order, length=4, start_angle=0):
            if order == 0:
                return Line(
                    start=ORIGIN,
                    end=length * RIGHT,
                    color=GREEN,
                    stroke_width=2
                )

            sequence = [1]
            for _ in range(order):
                sequence = sequence + [1] + [-x for x in sequence[::-1]]

            points = [np.array([0, 0, 0])]
            angle = start_angle

            for turn in sequence:
                angle += turn * PI / 2
                new_point = points[-1] + length / (2 ** (order / 2)) * np.array([
                    np.cos(angle),
                    np.sin(angle),
                    0
                ])
                points.append(new_point)

            curve = VMobject()
            curve.set_points_as_corners(points)
            curve.set_color(color=GREEN)
            curve.set_stroke(width=2)

            return curve

        dragon_iterations = VGroup()
        for order in range(1, 11):
            dragon = dragon_curve(order)
            dragon.move_to(ORIGIN)

            if order == 1:
                self.play(Create(dragon), run_time=1)
                current_dragon = dragon
            else:
                self.play(Transform(current_dragon, dragon), run_time=0.8)
            self.wait(0.3)

        # 3. Sierpinski三角形
        self.play(FadeOut(current_dragon))

        def sierpinski_triangle(order, size=4, position=ORIGIN):
            if order == 0:
                triangle = Polygon(
                    position + np.array([0, size, 0]),
                    position + np.array([-size * np.sqrt(3) / 2, -size / 2, 0]),
                    position + np.array([size * np.sqrt(3) / 2, -size / 2, 0]),
                    color=PURPLE,
                    fill_opacity=0.7,
                    stroke_width=1
                )
                return triangle

            triangles = VGroup()
            # 上方三角形
            triangles.add(sierpinski_triangle(
                order - 1, size / 2,
                position + np.array([0, size / 2, 0])
            ))
            # 左下三角形
            triangles.add(sierpinski_triangle(
                order - 1, size / 2,
                position + np.array([-size * np.sqrt(3) / 4, -size / 4, 0])
            ))
            # 右下三角形
            triangles.add(sierpinski_triangle(
                order - 1, size / 2,
                position + np.array([size * np.sqrt(3) / 4, -size / 4, 0])
            ))

            return triangles

        for order in range(6):
            sierpinski = sierpinski_triangle(order)

            if order == 0:
                self.play(Create(sierpinski), run_time=1)
                current_sierpinski = sierpinski
            else:
                self.play(Transform(current_sierpinski, sierpinski), run_time=1)
            self.wait(0.5)

        # 4. 洛伦兹吸引子
        self.play(FadeOut(current_sierpinski))

        # 创建坐标系
        axes = ThreeDAxes(
            x_range=[-20, 20, 5],
            y_range=[-30, 30, 5],
            z_range=[0, 50, 10],
            x_length=6,
            y_length=6,
            z_length=6
        )

        self.set_camera_orientation(phi=60 * DEGREES, theta=-45 * DEGREES)
        self.play(Create(axes), run_time=1)

        # Lorenz系统参数
        sigma = 10
        rho = 28
        beta = 8 / 3

        def lorenz_step(point, dt=0.01):
            x, y, z = point
            dx = sigma * (y - x)
            dy = x * (rho - z) - y
            dz = x * y - beta * z
            return point + dt * np.array([dx, dy, dz])

        # 创建轨迹
        point = np.array([1, 1, 1])
        points = [point]

        for _ in range(5000):
            point = lorenz_step(point)
            points.append(point / 10)  # 缩放以适应屏幕

        lorenz_curve = VMobject()
        lorenz_curve.set_points_smoothly([p for p in points[::10]])
        lorenz_curve.set_color_by_gradient(BLUE, PURPLE, RED)
        lorenz_curve.set_stroke(width=2)

        self.play(Create(lorenz_curve), run_time=4)
        self.begin_ambient_camera_rotation(rate=0.2)
        self.wait(3)
        self.stop_ambient_camera_rotation()

        # 清理场景
        self.play(
            FadeOut(axes),
            FadeOut(lorenz_curve),
            run_time=2
        )

        self.set_camera_orientation(phi=0, theta=-90 * DEGREES)
        self.wait(0.5)

    def act8_fourier_magic(self):
        """第八幕：傅里叶的魔法"""
        # 章节标题
        chapter_title = Text("第八幕：傅里叶的魔法", font="STSong", font_size=48)
        chapter_subtitle = Text("The Magic of Fourier", font_size=24, color=GREY_A)
        chapter_group = VGroup(chapter_title, chapter_subtitle).arrange(DOWN)

        self.play(Write(chapter_title), run_time=1.5)
        self.play(FadeIn(chapter_subtitle, shift=UP), run_time=0.5)
        self.wait(1)
        self.play(FadeOut(chapter_group))

        # 创建坐标轴
        axes = Axes(
            x_range=[-PI, PI, PI / 2],
            y_range=[-2, 2, 0.5],
            x_length=10,
            y_length=6,
            axis_config={"color": BLUE_D},
            tips=False
        )

        self.play(Create(axes), run_time=1)

        # 1. 方波的傅里叶级数
        def square_wave_term(n, x):
            return (4 / (n * PI)) * np.sin(n * x) if n % 2 == 1 else 0

        # 显示各个谐波分量
        harmonics = VGroup()
        colors = [BLUE, GREEN, YELLOW, ORANGE, RED]

        for i, n in enumerate([1, 3, 5, 7, 9]):
            harmonic = axes.plot(
                lambda x: square_wave_term(n, x),
                color=colors[i % len(colors)],
                stroke_width=2
            )
            harmonics.add(harmonic)

            label = MathTex(f"\\frac{{4}}{{\\pi}}\\sin({n}x)",
                            color=colors[i % len(colors)], font_size=24)
            label.move_to(3 * UP + 4 * RIGHT + i * 0.5 * DOWN)

            self.play(Create(harmonic), Write(label), run_time=0.8)

        # 合成方波
        self.wait(1)

        square_wave = axes.plot(
            lambda x: sum(square_wave_term(2 * k + 1, x) for k in range(20)),
            color=WHITE,
            stroke_width=3
        )

        self.play(
            FadeOut(harmonics),
            Create(square_wave),
            run_time=2
        )

        # 2. 傅里叶圆圈动画
        self.play(FadeOut(square_wave), FadeOut(axes))

        # 创建新的平面
        plane = NumberPlane(
            x_range=[-4, 4],
            y_range=[-4, 4],
            background_line_style={
                "stroke_color": BLUE_E,
                "stroke_width": 1,
                "stroke_opacity": 0.2
            }
        )
        self.play(Create(plane), run_time=1)

        # 傅里叶圆圈
        t = ValueTracker(0)
        circles = VGroup()
        vectors = VGroup()

        # 创建多个旋转圆
        frequencies = [1, 2, 3, 4]
        amplitudes = [1.5, 0.7, 0.4, 0.2]
        colors = [BLUE, GREEN, YELLOW, RED]

        for freq, amp, color in zip(frequencies, amplitudes, colors):
            circle = Circle(radius=amp, color=color, stroke_width=1)
            circles.add(circle)

            vector = Arrow(
                start=ORIGIN,
                end=amp * RIGHT,
                color=color,
                buff=0
            )
            vectors.add(vector)

        # 定位圆圈
        circles[0].move_to(ORIGIN)
        for i in range(1, len(circles)):
            circles[i].move_to(circles[i - 1].get_center() + amplitudes[i - 1] * RIGHT)

        self.play(*[Create(c) for c in circles], run_time=2)

        # 追踪路径
        path = VMobject()
        path.set_color(WHITE)

        def update_circles(mob):
            time = t.get_value()
            # 更新第一个圆的向量
            angle1 = frequencies[0] * time
            end1 = circles[0].get_center() + amplitudes[0] * np.array([
                np.cos(angle1), np.sin(angle1), 0
            ])

            # 更新后续圆圈位置
            for i in range(1, len(circles)):
                angle = frequencies[i] * time
                prev_end = circles[i - 1].get_center() + amplitudes[i - 1] * np.array([
                    np.cos(frequencies[i - 1] * time),
                    np.sin(frequencies[i - 1] * time),
                    0
                ])
                circles[i].move_to(prev_end)

            # 获取最后一个点
            last_angle = frequencies[-1] * time
            last_point = circles[-1].get_center() + amplitudes[-1] * np.array([
                np.cos(last_angle), np.sin(last_angle), 0
            ])

            # 添加到路径
            if len(path.points) == 0:
                path.set_points_as_corners([last_point, last_point])
            else:
                path.add_points_as_corners([last_point])

        circles.add_updater(update_circles)
        self.add(path)

        self.play(t.animate.set_value(4 * PI), run_time=8, rate_func=linear)

        circles.remove_updater(update_circles)

        # 清理场景
        self.play(
            FadeOut(plane),
            FadeOut(circles),
            FadeOut(path),
            run_time=2
        )
        self.wait(0.5)

    def finale_universal_celebration(self):
        """终幕：函数宇宙的狂欢"""
        # 章节标题
        finale_title = Text(
            "终幕：函数宇宙的狂欢",
            font="STSong",
            font_size=56,
            gradient=(BLUE, PURPLE, PINK, ORANGE, YELLOW)
        )
        self.play(Write(finale_title), run_time=2)
        self.wait(1)
        self.play(FadeOut(finale_title))

        # 创建星空背景
        stars = VGroup()
        for _ in range(150):
            star = Dot(
                point=np.array([
                    np.random.uniform(-7, 7),
                    np.random.uniform(-4, 4),
                    0
                ]),
                radius=np.random.uniform(0.01, 0.04),
                color=random.choice([WHITE, YELLOW, BLUE_A])
            ).set_opacity(np.random.uniform(0.4, 1))
            stars.add(star)

        self.add(stars)

        # 创建函数烟花
        def create_firework(center, color):
            explosion = VGroup()
            for angle in np.linspace(0, 2 * PI, 20):
                trace = ParametricFunction(
                    lambda t: center + t * np.array([
                        np.cos(angle) * (1 + 0.3 * np.sin(5 * t)),
                        np.sin(angle) * (1 + 0.3 * np.sin(5 * t)),
                        0
                    ]),
                    t_range=[0, 2],
                    color=color,
                    stroke_width=2
                )
                explosion.add(trace)
            return explosion

        # 发射多个烟花
        fireworks = []
        firework_centers = [
            np.array([-3, 2, 0]),
            np.array([3, 1, 0]),
            np.array([0, -2, 0]),
            np.array([-2, -1, 0]),
            np.array([2, 2, 0])
        ]
        firework_colors = [RED, BLUE, GREEN, YELLOW, PURPLE]

        for center, color in zip(firework_centers, firework_colors):
            firework = create_firework(center, color)
            fireworks.append(firework)
            self.play(Create(firework), run_time=0.8)

        # 函数大合唱
        function_parade = VGroup()

        # 各种函数同时出现
        functions_data = [
            (lambda t: np.array([t, np.sin(2 * t), 0]), [-3, 3], BLUE),
            (lambda t: np.array([2 * np.cos(t), 2 * np.sin(t), 0]), [0, 2 * PI], RED),
            (lambda t: np.array([t, t ** 2 / 4 - 2, 0]), [-3, 3], GREEN),
            (lambda t: np.array([3 * np.cos(t), 1.5 * np.sin(t), 0]), [0, 2 * PI], YELLOW),
            (lambda t: np.array([np.cos(3 * t), np.sin(2 * t), 0]), [0, 2 * PI], PURPLE)
        ]

        for func, t_range, color in functions_data:
            curve = ParametricFunction(
                func,
                t_range=t_range,
                color=color,
                stroke_width=3
            ).scale(0.7)
            function_parade.add(curve)

        self.play(
            *[FadeOut(f) for f in fireworks],
            *[Create(f) for f in function_parade],
            run_time=2
        )

        # 函数的舞蹈
        self.play(
            function_parade.animate.rotate(PI / 4),
            run_time=2
        )

        self.play(
            *[f.animate.scale(1.2).set_stroke(width=4) for f in function_parade],
            run_time=1
        )

        self.play(
            *[f.animate.scale(1 / 1.2).set_stroke(width=3) for f in function_parade],
            run_time=1
        )

        # 汇聚成最终图案
        final_heart = ParametricFunction(
            lambda t: np.array([
                16 * np.sin(t) ** 3 / 4,
                (13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t)) / 4,
                0
            ]),
            t_range=[0, 2 * PI],
            color=(PINK, RED),
            stroke_width=5
        )

        self.play(
            Transform(function_parade, final_heart),
            run_time=3
        )

        # 结束语
        ending_messages = VGroup(
            Text("数学之美", font="STSong", font_size=64, color=GOLD),
            Text("在于无限的可能", font="STSong", font_size=48, color=WHITE),
            Text("The Beauty of Mathematics", font_size=36, color=GREY_A),
            Text("Lies in Infinite Possibilities", font_size=28, color=GREY_B),
            Text("", font_size=24),
            Text("感谢观看", font="STSong", font_size=32, color=PINK),
            Text("Thank You for Watching", font_size=24, color=PINK)
        ).arrange(DOWN, buff=0.2)

        self.play(
            FadeOut(function_parade),
            stars.animate.set_opacity(0.2),
            run_time=2
        )

        for message in ending_messages:
            self.play(Write(message), run_time=0.8)

        self.wait(3)

        # 最终淡出
        self.play(
            *[FadeOut(mob) for mob in self.mobjects],
            run_time=3
        )


if __name__ == "__main__":
    # 运行命令：
    # manim -pql function_dance_extended.py FunctionDanceExtended
    # 高质量版本：
    # manim -pqh function_dance_extended.py FunctionDanceExtended
    pass