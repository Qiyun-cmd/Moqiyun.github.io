from manim import *
import numpy as np
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from my_manim_setup import *

class MathematicalFormulasEvolution(Scene):
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#0f0f23"

        # ========== 开场：数学公式的史诗 ==========
        self.opening_title()

        # ========== 第一章：欧拉恒等式 - 最美公式 ==========
        self.euler_identity()

        # ========== 第二章：勾股定理 - 几何基石 ==========
        self.pythagorean_theorem()

        # ========== 第三章：微积分基本定理 ==========
        self.fundamental_theorem_calculus()

        # ========== 第四章：二项式定理 ==========
        self.binomial_theorem()

        # ========== 第五章：泰勒级数 - 函数的展开 ==========
        self.taylor_series()

        # ========== 第六章：傅里叶级数 - 信号分解 ==========
        self.fourier_series()

        # ========== 第七章：高斯积分 ==========
        self.gaussian_integral()

        # ========== 第八章：贝叶斯定理 ==========
        self.bayes_theorem()

        # ========== 第九章：黄金分割 ==========
        self.golden_ratio()

        # ========== 第十章：质数定理 ==========
        self.prime_number_theorem()

        # ========== 终章：公式的交响曲 ==========
        self.finale_symphony()

    def opening_title(self):
        """开场：数学公式的史诗"""
        # 标题
        title = Text(
            "数学公式的演化",
            font="STSong",
            font_size=72,
            gradient=(BLUE, PURPLE)
        )
        subtitle = Text(
            "The Evolution of Mathematical Formulas",
            font_size=36,
            color=GREY_A
        )
        subtitle.next_to(title, DOWN)

        # 名言
        quote = VGroup(
            Text(
                "\"God created the integers, all else is the work of man\"",
                font_size=24,
                slant=ITALIC,
                color=GREY_B
            ),
            Text(
                "- Leopold Kronecker",
                font_size=20,
                color=GREY_C
            )
        ).arrange(DOWN, buff=0.2)
        quote.next_to(subtitle, DOWN, buff=1)

        self.play(Write(title), run_time=2)
        self.play(FadeIn(subtitle, shift=UP), run_time=1)
        self.play(Write(quote), run_time=2)
        self.wait(2)

        self.play(
            FadeOut(title),
            FadeOut(subtitle),
            FadeOut(quote),
            run_time=1.5
        )

    def euler_identity(self):
        """第一章：欧拉恒等式"""
        # 章节标题
        chapter = Text("第一章：欧拉恒等式", font="STSong", font_size=48)
        chapter_en = Text("Euler's Identity", font_size=24, color=GREY_A)
        chapter_group = VGroup(chapter, chapter_en).arrange(DOWN)

        self.play(Write(chapter), FadeIn(chapter_en), run_time=1.5)
        self.wait(1)
        self.play(FadeOut(chapter_group))

        # 展示欧拉公式的组成部分
        title = Text("数学中最美的公式", font="STSong", font_size=32, color=BLUE)
        title.to_edge(UP)
        self.play(Write(title))

        # 从基础开始
        exp_def = MathTex(r"e^{ix} = \cos(x) + i\sin(x)")
        exp_def.scale(1.2)
        self.play(Write(exp_def), run_time=2)
        self.wait(2)

        # 代入 x = π
        step1 = MathTex(r"x = \pi")
        step1.next_to(exp_def, DOWN, buff=0.5)
        self.play(Write(step1))
        self.wait(1)

        # 展示推导
        step2 = MathTex(r"e^{i\pi} = \cos(\pi) + i\sin(\pi)")
        step2.next_to(step1, DOWN, buff=0.5)
        self.play(Write(step2), run_time=1.5)

        step3 = MathTex(r"e^{i\pi} = -1 + i \cdot 0")
        step3.next_to(step2, DOWN, buff=0.5)
        self.play(Write(step3), run_time=1.5)

        step4 = MathTex(r"e^{i\pi} = -1")
        step4.next_to(step3, DOWN, buff=0.5)
        self.play(Write(step4), run_time=1.5)

        # 最终形式
        self.wait(1)
        euler_identity = MathTex(
            r"e^{i\pi} + 1 = 0",
            font_size=72,
            color=YELLOW
        )

        self.play(
            FadeOut(exp_def),
            FadeOut(step1),
            FadeOut(step2),
            FadeOut(step3),
            FadeOut(step4),
            run_time=1
        )

        self.play(Write(euler_identity), run_time=2)

        # 添加说明
        explanation = Text(
            "包含了数学中5个最重要的常数：e, i, π, 1, 0",
            font="STSong",
            font_size=24,
            color=GREY_A
        )
        explanation.next_to(euler_identity, DOWN, buff=1)
        self.play(Write(explanation), run_time=2)

        # 可视化复平面上的旋转
        self.wait(2)
        self.play(
            FadeOut(title),
            FadeOut(euler_identity),
            FadeOut(explanation),
            run_time=1
        )

        # 创建复平面
        plane = ComplexPlane(
            x_range=[-2, 2, 1],
            y_range=[-2, 2, 1],
            x_length=6,
            y_length=6
        ).add_coordinates()

        self.play(Create(plane), run_time=1.5)

        # 单位圆
        unit_circle = Circle(radius=2, color=BLUE, stroke_width=2)
        self.play(Create(unit_circle))

        # 动画展示 e^(iθ) 的轨迹
        theta = ValueTracker(0)

        # 创建移动点
        dot = Dot(color=YELLOW, radius=0.08)
        dot.add_updater(
            lambda m: m.move_to(
                plane.n2p(np.exp(1j * theta.get_value()))
            )
        )

        # 创建向量
        vector = always_redraw(
            lambda: Arrow(
                start=plane.n2p(0),
                end=plane.n2p(np.exp(1j * theta.get_value())),
                color=RED,
                buff=0
            )
        )

        # 角度标签
        angle_label = always_redraw(
            lambda: MathTex(
                f"\\theta = {theta.get_value():.2f}",
                color=GREEN
            ).to_corner(UR)
        )

        self.add(dot, vector, angle_label)

        # 旋转到π
        self.play(theta.animate.set_value(PI), run_time=3, rate_func=linear)

        # 标记点 e^(iπ) = -1
        label = MathTex(r"e^{i\pi} = -1", color=YELLOW)
        label.next_to(dot, LEFT)
        self.play(Write(label))

        self.wait(2)

        # 清理
        self.play(
            FadeOut(plane),
            FadeOut(unit_circle),
            FadeOut(dot),
            FadeOut(vector),
            FadeOut(angle_label),
            FadeOut(label),
            run_time=1.5
        )

    def pythagorean_theorem(self):
        """第二章：勾股定理"""
        # 章节标题
        chapter = Text("第二章：勾股定理", font="STSong", font_size=48)
        chapter_en = Text("Pythagorean Theorem", font_size=24, color=GREY_A)
        chapter_group = VGroup(chapter, chapter_en).arrange(DOWN)

        self.play(Write(chapter), FadeIn(chapter_en), run_time=1.5)
        self.wait(1)
        self.play(FadeOut(chapter_group))

        # 创建直角三角形
        triangle = Polygon(
            np.array([-2, -2, 0]),
            np.array([2, -2, 0]),
            np.array([2, 1, 0]),
            color=WHITE,
            stroke_width=3
        )

        # 标记直角
        right_angle = Square(side_length=0.3, color=WHITE, stroke_width=2)
        right_angle.move_to(np.array([1.85, -1.85, 0]))

        self.play(Create(triangle), Create(right_angle))

        # 标记边长
        a_label = MathTex("a", color=BLUE).next_to(triangle, DOWN)
        b_label = MathTex("b", color=GREEN).next_to(triangle, RIGHT)
        c_label = MathTex("c", color=RED).move_to(np.array([-0.2, -0.2, 0]))

        self.play(Write(a_label), Write(b_label), Write(c_label))

        # 创建正方形
        square_a = Square(side_length=4, color=BLUE, fill_opacity=0.3)
        square_a.next_to(triangle, DOWN, buff=0)

        square_b = Square(side_length=3, color=GREEN, fill_opacity=0.3)
        square_b.next_to(triangle, RIGHT, buff=0)

        square_c = Square(side_length=5, color=RED, fill_opacity=0.3)
        square_c.rotate(np.arctan(3 / 4))
        square_c.move_to(triangle.get_center() + np.array([-2.5, 0.5, 0]))

        # 显示面积
        self.play(
            Create(square_a),
            Create(square_b),
            Create(square_c),
            run_time=2
        )

        # 显示公式
        formula = MathTex(r"a^2 + b^2 = c^2", font_size=60, color=YELLOW)
        formula.to_edge(UP)

        self.play(Write(formula), run_time=2)

        # 数值验证
        values = MathTex(r"3^2 + 4^2 = 5^2", font_size=48)
        values.next_to(formula, DOWN)
        calculation = MathTex(r"9 + 16 = 25", font_size=48)
        calculation.next_to(values, DOWN)

        self.play(Write(values), run_time=1)
        self.play(Write(calculation), run_time=1)

        self.wait(2)

        # 几何证明动画
        self.play(
            FadeOut(square_a),
            FadeOut(square_b),
            FadeOut(square_c),
            FadeOut(values),
            FadeOut(calculation),
            run_time=1
        )

        # 展示经典的几何证明
        proof_text = Text("几何证明", font="STSong", font_size=32, color=BLUE)
        proof_text.next_to(formula, DOWN)
        self.play(Write(proof_text))

        # 创建四个相同的直角三角形组成正方形
        triangles = VGroup()
        for i, angle in enumerate([0, 90, 180, 270]):
            tri = triangle.copy()
            tri.rotate(angle * DEGREES, about_point=ORIGIN)
            tri.set_color(interpolate_color(BLUE, GREEN, i / 3))
            triangles.add(tri)

        self.play(
            FadeOut(triangle),
            FadeOut(right_angle),
            FadeOut(a_label),
            FadeOut(b_label),
            FadeOut(c_label),
            *[Create(tri) for tri in triangles],
            run_time=2
        )

        self.wait(2)

        # 清理
        self.play(
            FadeOut(triangles),
            FadeOut(formula),
            FadeOut(proof_text),
            run_time=1.5
        )

    def fundamental_theorem_calculus(self):
        """第三章：微积分基本定理"""
        # 章节标题
        chapter = Text("第三章：微积分基本定理", font="STSong", font_size=48)
        chapter_en = Text("Fundamental Theorem of Calculus", font_size=24, color=GREY_A)
        chapter_group = VGroup(chapter, chapter_en).arrange(DOWN)

        self.play(Write(chapter), FadeIn(chapter_en), run_time=1.5)
        self.wait(1)
        self.play(FadeOut(chapter_group))

        # 创建坐标系
        axes = Axes(
            x_range=[0, 5, 1],
            y_range=[0, 10, 2],
            x_length=8,
            y_length=6,
            axis_config={"color": BLUE_D},
            tips=False
        )
        axes_labels = axes.get_axis_labels(x_label="x", y_label="y")

        self.play(Create(axes), Write(axes_labels))

        # 定义函数
        func = lambda x: 0.5 * x ** 2
        graph = axes.plot(func, color=BLUE, x_range=[0, 4])
        func_label = MathTex(r"f(x) = \frac{1}{2}x^2", color=BLUE)
        func_label.to_corner(UR)

        self.play(Create(graph), Write(func_label))

        # 显示积分区域
        area = axes.get_area(graph, x_range=[1, 3], color=BLUE, opacity=0.3)
        self.play(FadeIn(area))

        # 积分公式
        integral = MathTex(
            r"\int_a^b f(x)\,dx = F(b) - F(a)",
            font_size=48
        )
        integral.to_edge(UP)

        self.play(Write(integral), run_time=2)

        # 具体计算
        calculation = VGroup(
            MathTex(r"F(x) = \frac{1}{6}x^3"),
            MathTex(r"\int_1^3 \frac{1}{2}x^2\,dx"),
            MathTex(r"= F(3) - F(1)"),
            MathTex(r"= \frac{27}{6} - \frac{1}{6}"),
            MathTex(r"= \frac{26}{6} = \frac{13}{3}")
        ).arrange(DOWN, buff=0.3)
        calculation.next_to(integral, DOWN, buff=0.5)

        for calc in calculation:
            self.play(Write(calc), run_time=1)
            self.wait(0.5)

        # 黎曼和的可视化
        self.play(
            FadeOut(calculation),
            run_time=1
        )

        # 创建矩形近似
        riemann_text = Text("黎曼和近似", font="STSong", font_size=28, color=GREEN)
        riemann_text.next_to(integral, DOWN)
        self.play(Write(riemann_text))

        for n in [4, 8, 16, 32]:
            rectangles = axes.get_riemann_rectangles(
                graph,
                x_range=[1, 3],
                dx=(3 - 1) / n,
                color=GREEN,
                fill_opacity=0.5
            )

            if n == 4:
                self.play(Create(rectangles), run_time=1)
                current_rects = rectangles
            else:
                self.play(Transform(current_rects, rectangles), run_time=1)

            n_label = MathTex(f"n = {n}", color=GREEN)
            n_label.next_to(riemann_text, DOWN)

            if n == 4:
                self.play(Write(n_label))
                current_label = n_label
            else:
                self.play(Transform(current_label, n_label))

            self.wait(0.5)

        self.wait(2)

        # 清理
        self.play(
            FadeOut(axes),
            FadeOut(axes_labels),
            FadeOut(graph),
            FadeOut(func_label),
            FadeOut(area),
            FadeOut(integral),
            FadeOut(riemann_text),
            FadeOut(current_rects),
            FadeOut(current_label),
            run_time=1.5
        )

    def binomial_theorem(self):
        """第四章：二项式定理"""
        # 章节标题
        chapter = Text("第四章：二项式定理", font="STSong", font_size=48)
        chapter_en = Text("Binomial Theorem", font_size=24, color=GREY_A)
        chapter_group = VGroup(chapter, chapter_en).arrange(DOWN)

        self.play(Write(chapter), FadeIn(chapter_en), run_time=1.5)
        self.wait(1)
        self.play(FadeOut(chapter_group))

        # 基本形式
        binomial = MathTex(
            r"(a + b)^n = \sum_{k=0}^{n} \binom{n}{k} a^{n-k} b^k",
            font_size=48
        )
        self.play(Write(binomial), run_time=2)
        self.wait(2)

        # 展示几个具体例子
        examples_title = Text("具体展开", font="STSong", font_size=32, color=BLUE)
        examples_title.to_edge(UP)

        self.play(
            binomial.animate.next_to(examples_title, DOWN),
            Write(examples_title)
        )

        # n=2
        exp2 = MathTex(
            r"(a + b)^2 = a^2 + 2ab + b^2",
            color=GREEN
        )
        exp2.next_to(binomial, DOWN, buff=0.5)

        # n=3
        exp3 = MathTex(
            r"(a + b)^3 = a^3 + 3a^2b + 3ab^2 + b^3",
            color=YELLOW
        )
        exp3.next_to(exp2, DOWN, buff=0.3)

        # n=4
        exp4 = MathTex(
            r"(a + b)^4 = a^4 + 4a^3b + 6a^2b^2 + 4ab^3 + b^4",
            color=ORANGE,
            font_size=36
        )
        exp4.next_to(exp3, DOWN, buff=0.3)

        self.play(Write(exp2), run_time=1.5)
        self.play(Write(exp3), run_time=1.5)
        self.play(Write(exp4), run_time=1.5)

        self.wait(2)

        # 帕斯卡三角形
        self.play(
            FadeOut(examples_title),
            FadeOut(binomial),
            FadeOut(exp2),
            FadeOut(exp3),
            FadeOut(exp4),
            run_time=1
        )

        pascal_title = Text("帕斯卡三角形", font="STSong", font_size=40, color=PURPLE)
        pascal_title.to_edge(UP)
        self.play(Write(pascal_title))

        # 创建帕斯卡三角形
        pascal_rows = [
            [1],
            [1, 1],
            [1, 2, 1],
            [1, 3, 3, 1],
            [1, 4, 6, 4, 1],
            [1, 5, 10, 10, 5, 1],
            [1, 6, 15, 20, 15, 6, 1]
        ]

        pascal_triangle = VGroup()

        for i, row in enumerate(pascal_rows):
            row_group = VGroup()
            for j, num in enumerate(row):
                num_tex = MathTex(str(num))
                num_tex.move_to(
                    UP * (3 - i * 0.6) +
                    RIGHT * (j - len(row) / 2 + 0.5) * 0.8
                )
                # 根据数值大小设置颜色
                if num == 1:
                    num_tex.set_color(BLUE)
                elif num <= 5:
                    num_tex.set_color(GREEN)
                elif num <= 10:
                    num_tex.set_color(YELLOW)
                else:
                    num_tex.set_color(ORANGE)

                row_group.add(num_tex)

            pascal_triangle.add(row_group)
            self.play(Write(row_group), run_time=0.5)

        # 显示规律
        pattern_text = Text(
            "每个数等于上方两数之和",
            font="STSong",
            font_size=28,
            color=GREY_A
        )
        pattern_text.to_edge(DOWN)
        self.play(Write(pattern_text))

        self.wait(3)

        # 清理
        self.play(
            FadeOut(pascal_title),
            FadeOut(pascal_triangle),
            FadeOut(pattern_text),
            run_time=1.5
        )

    def taylor_series(self):
        """第五章：泰勒级数"""
        # 章节标题
        chapter = Text("第五章：泰勒级数", font="STSong", font_size=48)
        chapter_en = Text("Taylor Series", font_size=24, color=GREY_A)
        chapter_group = VGroup(chapter, chapter_en).arrange(DOWN)

        self.play(Write(chapter), FadeIn(chapter_en), run_time=1.5)
        self.wait(1)
        self.play(FadeOut(chapter_group))

        # 泰勒级数公式
        taylor_formula = MathTex(
            r"f(x) = \sum_{n=0}^{\infty} \frac{f^{(n)}(a)}{n!}(x-a)^n",
            font_size=48
        )
        taylor_formula.to_edge(UP)
        self.play(Write(taylor_formula), run_time=2)

        # 创建坐标系
        axes = Axes(
            x_range=[-PI, PI, PI / 2],
            y_range=[-2, 2, 0.5],
            x_length=10,
            y_length=6,
            axis_config={"color": BLUE_D},
            tips=False
        )
        axes_labels = axes.get_axis_labels()

        self.play(Create(axes), Write(axes_labels))

        # 以 sin(x) 为例
        sin_func = axes.plot(lambda x: np.sin(x), color=BLUE, stroke_width=3)
        sin_label = MathTex(r"f(x) = \sin(x)", color=BLUE)
        sin_label.next_to(taylor_formula, DOWN)

        self.play(Create(sin_func), Write(sin_label))

        # 展示泰勒级数逼近
        taylor_terms = [
            (lambda x: x, r"T_1(x) = x", GREEN),
            (lambda x: x - x ** 3 / 6, r"T_3(x) = x - \frac{x^3}{6}", YELLOW),
            (lambda x: x - x ** 3 / 6 + x ** 5 / 120, r"T_5(x) = x - \frac{x^3}{6} + \frac{x^5}{120}", ORANGE),
            (lambda x: x - x ** 3 / 6 + x ** 5 / 120 - x ** 7 / 5040,
             r"T_7(x) = x - \frac{x^3}{6} + \frac{x^5}{120} - \frac{x^7}{5040}", RED)
        ]

        current_approx = None
        current_label = sin_label

        for func, tex, color in taylor_terms:
            approx = axes.plot(func, color=color, stroke_width=2, x_range=[-PI, PI])
            label = MathTex(tex, color=color, font_size=32)
            label.next_to(taylor_formula, DOWN)

            if current_approx is None:
                self.play(Create(approx), Transform(current_label, label), run_time=1.5)
                current_approx = approx
            else:
                self.play(
                    Transform(current_approx, approx),
                    Transform(current_label, label),
                    run_time=1.5
                )

            self.wait(1)

        # 展示误差减小
        error_text = Text(
            "随着项数增加，逼近越来越精确",
            font="STSong",
            font_size=28,
            color=GREY_A
        )
        error_text.to_edge(DOWN)
        self.play(Write(error_text))

        self.wait(2)

        # 清理
        self.play(
            FadeOut(axes),
            FadeOut(axes_labels),
            FadeOut(sin_func),
            FadeOut(current_approx),
            FadeOut(current_label),
            FadeOut(taylor_formula),
            FadeOut(error_text),
            run_time=1.5
        )

    def fourier_series(self):
        """第六章：傅里叶级数"""
        # 章节标题
        chapter = Text("第六章：傅里叶级数", font="STSong", font_size=48)
        chapter_en = Text("Fourier Series", font_size=24, color=GREY_A)
        chapter_group = VGroup(chapter, chapter_en).arrange(DOWN)

        self.play(Write(chapter), FadeIn(chapter_en), run_time=1.5)
        self.wait(1)
        self.play(FadeOut(chapter_group))

        # 傅里叶级数公式
        fourier_formula = MathTex(
            r"f(x) = \frac{a_0}{2} + \sum_{n=1}^{\infty} \left[a_n\cos(nx) + b_n\sin(nx)\right]",
            font_size=42
        )
        fourier_formula.to_edge(UP)
        self.play(Write(fourier_formula), run_time=2)

        # 创建坐标系
        axes = Axes(
            x_range=[-PI, PI, PI / 2],
            y_range=[-2, 2, 0.5],
            x_length=10,
            y_length=6,
            axis_config={"color": BLUE_D},
            tips=False
        )

        self.play(Create(axes))

        # 方波函数
        def square_wave(x):
            return 1 if (x % (2 * PI)) < PI else -1

        # 绘制方波
        square = axes.plot(
            lambda x: 1 if (x % (2 * PI)) < PI else -1,
            x_range=[-PI, PI],
            color=BLUE,
            stroke_width=3,
            discontinuities = [-PI, 0, PI]
        )

        square_label = Text("方波", font="STSong", font_size=28, color=BLUE)
        square_label.next_to(fourier_formula, DOWN)

        self.play(Create(square), Write(square_label))

        # 傅里叶级数逼近
        def fourier_approx(x, n_terms):
            result = 0
            for n in range(1, n_terms + 1, 2):
                result += (4 / (n * PI)) * np.sin(n * x)
            return result

        # 展示不同阶数的逼近
        approx_colors = [GREEN, YELLOW, ORANGE, RED, PURPLE]
        current_approx = None

        for i, n_terms in enumerate([1, 3, 5, 9, 19]):
            approx = axes.plot(
                lambda x: fourier_approx(x, n_terms),
                color=approx_colors[i % len(approx_colors)],
                stroke_width=2
            )

            terms_label = MathTex(f"n = {n_terms}", color=approx_colors[i % len(approx_colors)])
            terms_label.next_to(square_label, DOWN)

            if current_approx is None:
                self.play(Create(approx), Write(terms_label), run_time=1.5)
                current_approx = approx
                current_label = terms_label
            else:
                self.play(
                    Transform(current_approx, approx),
                    Transform(current_label, terms_label),
                    run_time=1.5
                )

            self.wait(0.5)

        # 吉布斯现象说明
        gibbs_text = Text(
            "吉布斯现象：不连续点处的过冲",
            font="STSong",
            font_size=24,
            color=GREY_A
        )
        gibbs_text.to_edge(DOWN)
        self.play(Write(gibbs_text))

        self.wait(2)

        # 清理
        self.play(
            FadeOut(axes),
            FadeOut(square),
            FadeOut(current_approx),
            FadeOut(fourier_formula),
            FadeOut(square_label),
            FadeOut(current_label),
            FadeOut(gibbs_text),
            run_time=1.5
        )

    def gaussian_integral(self):
        """第七章：高斯积分"""
        # 章节标题
        chapter = Text("第七章：高斯积分", font="STSong", font_size=48)
        chapter_en = Text("Gaussian Integral", font_size=24, color=GREY_A)
        chapter_group = VGroup(chapter, chapter_en).arrange(DOWN)

        self.play(Write(chapter), FadeIn(chapter_en), run_time=1.5)
        self.wait(1)
        self.play(FadeOut(chapter_group))

        # 高斯积分公式
        gaussian = MathTex(
            r"\int_{-\infty}^{\infty} e^{-x^2} dx = \sqrt{\pi}",
            font_size=60,
            color=YELLOW
        )
        self.play(Write(gaussian), run_time=2)
        self.wait(2)

        # 创建坐标系
        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[0, 1.2, 0.2],
            x_length=10,
            y_length=6,
            axis_config={"color": BLUE_D},
            tips=False
        )
        axes_labels = axes.get_axis_labels()

        self.play(
            gaussian.animate.to_edge(UP),
            Create(axes),
            Write(axes_labels)
        )

        # 绘制高斯曲线
        gauss_curve = axes.plot(
            lambda x: np.exp(-x ** 2),
            color=BLUE,
            stroke_width=3
        )

        self.play(Create(gauss_curve))

        # 显示面积
        area = axes.get_area(
            gauss_curve,
            x_range=[-3, 3],
            color=BLUE,
            opacity=0.3
        )

        self.play(FadeIn(area))

        # 证明思路
        proof_title = Text("证明思路", font="STSong", font_size=32, color=GREEN)
        proof_title.next_to(gaussian, DOWN)
        self.play(Write(proof_title))

        # 关键步骤
        steps = VGroup(
            MathTex(r"I = \int_{-\infty}^{\infty} e^{-x^2} dx"),
            MathTex(r"I^2 = \int_{-\infty}^{\infty} e^{-x^2} dx \cdot \int_{-\infty}^{\infty} e^{-y^2} dy"),
            MathTex(r"I^2 = \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} e^{-(x^2+y^2)} dx dy"),
            MathTex(r"I^2 = \int_0^{2\pi} \int_0^{\infty} e^{-r^2} r\,dr\,d\theta"),
            MathTex(r"I^2 = 2\pi \cdot \frac{1}{2} = \pi"),
            MathTex(r"I = \sqrt{\pi}", color=YELLOW),
            VGroup(
            Text("极坐标变换：", font="STSong", font_size=24),
            MathTex(r"I^2 = \int_0^{2\pi} \int_0^{\infty} e^{-r^2} r\,dr\,d\theta")
            ).arrange(RIGHT),
            MathTex(r"I^2 = 2\pi \cdot \frac{1}{2} = \pi"),
            MathTex(r"I = \sqrt{\pi}", color=YELLOW)
        )
        steps.arrange(DOWN, buff=0.2)
        steps.scale(0.7)
        steps.next_to(proof_title, DOWN, buff=0.3)

        for step in steps:
            self.play(Write(step), run_time=1)
            self.wait(0.5)

        self.wait(2)

        # 清理
        self.play(
            FadeOut(axes),
            FadeOut(axes_labels),
            FadeOut(gauss_curve),
            FadeOut(area),
            FadeOut(gaussian),
            FadeOut(proof_title),
            FadeOut(steps),
            run_time=1.5
        )

    def bayes_theorem(self):
        """第八章：贝叶斯定理"""
        # 章节标题
        chapter = Text("第八章：贝叶斯定理", font="STSong", font_size=48)
        chapter_en = Text("Bayes' Theorem", font_size=24, color=GREY_A)
        chapter_group = VGroup(chapter, chapter_en).arrange(DOWN)

        self.play(Write(chapter), FadeIn(chapter_en), run_time=1.5)
        self.wait(1)
        self.play(FadeOut(chapter_group))

        # 贝叶斯定理公式
        bayes = MathTex(
            r"P(A|B) = \frac{P(B|A) \cdot P(A)}{P(B)}",
            font_size=60
        )
        self.play(Write(bayes), run_time=2)

        # 解释各项
        explanations = VGroup(
            MathTex(r"P(A|B)", color=BLUE, font_size=36),
            Text("：在B发生的条件下A发生的概率", font="STSong", font_size=24),
            MathTex(r"P(B|A)", color=GREEN, font_size=36),
            Text("：在A发生的条件下B发生的概率", font="STSong", font_size=24),
            MathTex(r"P(A)", color=YELLOW, font_size=36),
            Text("：A的先验概率", font="STSong", font_size=24),
            MathTex(r"P(B)", color=ORANGE, font_size=36),
            Text("：B的边际概率", font="STSong", font_size=24)
        )

        # 排列解释
        for i in range(0, len(explanations), 2):
            explanations[i:i + 2].arrange(RIGHT, buff=0.2)

        explanations.arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        explanations.scale(0.8)
        explanations.next_to(bayes, DOWN, buff=0.5)

        self.play(
            bayes.animate.to_edge(UP),
            Write(explanations),
            run_time=3
        )

        self.wait(2)

        # 可视化例子：医学检测
        self.play(FadeOut(explanations))

        example_title = Text(
            "应用：医学检测",
            font="STSong",
            font_size=32,
            color=PURPLE
        )
        example_title.next_to(bayes, DOWN)
        self.play(Write(example_title))

        # 创建概率树
        tree = VGroup()

        # 根节点
        root = Circle(radius=0.3, color=WHITE)
        root.move_to(ORIGIN)

        # 疾病/健康分支
        disease = Circle(radius=0.3, color=RED)
        disease.move_to(UP * 2 + LEFT * 3)
        healthy = Circle(radius=0.3, color=GREEN)
        healthy.move_to(UP * 2 + RIGHT * 3)

        # 检测结果分支
        positive_d = Circle(radius=0.3, color=ORANGE)
        positive_d.move_to(LEFT * 4)
        negative_d = Circle(radius=0.3, color=BLUE)
        negative_d.move_to(LEFT * 2)

        positive_h = Circle(radius=0.3, color=ORANGE)
        positive_h.move_to(RIGHT * 2)
        negative_h = Circle(radius=0.3, color=BLUE)
        negative_h.move_to(RIGHT * 4)

        tree.add(root, disease, healthy, positive_d, negative_d, positive_h, negative_h)

        # 添加连线
        lines = VGroup(
            Line(root.get_center(), disease.get_center()),
            Line(root.get_center(), healthy.get_center()),
            Line(disease.get_center(), positive_d.get_center()),
            Line(disease.get_center(), negative_d.get_center()),
            Line(healthy.get_center(), positive_h.get_center()),
            Line(healthy.get_center(), negative_h.get_center())
        )

        # 添加概率标签
        prob_labels = VGroup(
            MathTex(r"0.01", color=RED, font_size=24).next_to(disease, UP),
            MathTex(r"0.99", color=GREEN, font_size=24).next_to(healthy, UP),
            MathTex(r"0.95", font_size=20).move_to((disease.get_center() + positive_d.get_center()) / 2 + UP * 0.3),
            MathTex(r"0.05", font_size=20).move_to((disease.get_center() + negative_d.get_center()) / 2 + UP * 0.3),
            MathTex(r"0.02", font_size=20).move_to((healthy.get_center() + positive_h.get_center()) / 2 + UP * 0.3),
            MathTex(r"0.98", font_size=20).move_to((healthy.get_center() + negative_h.get_center()) / 2 + UP * 0.3)
        )

        self.play(
            Create(tree),
            Create(lines),
            Write(prob_labels),
            run_time=3
        )

        # 计算后验概率
        calculation = MathTex(
            r"P(D|+) = \frac{0.95 \times 0.01}{0.95 \times 0.01 + 0.02 \times 0.99} \approx 0.324",
            font_size=28,
            color=YELLOW
        )
        calculation.to_edge(DOWN)
        self.play(Write(calculation), run_time=2)

        self.wait(3)

        # 清理
        self.play(
            FadeOut(bayes),
            FadeOut(example_title),
            FadeOut(tree),
            FadeOut(lines),
            FadeOut(prob_labels),
            FadeOut(calculation),
            run_time=1.5
        )

    def golden_ratio(self):
        """第九章：黄金分割"""
        # 章节标题
        chapter = Text("第九章：黄金分割", font="STSong", font_size=48)
        chapter_en = Text("Golden Ratio", font_size=24, color=GREY_A)
        chapter_group = VGroup(chapter, chapter_en).arrange(DOWN)

        self.play(Write(chapter), FadeIn(chapter_en), run_time=1.5)
        self.wait(1)
        self.play(FadeOut(chapter_group))

        # 黄金比例公式
        golden = MathTex(
            r"\varphi = \frac{1 + \sqrt{5}}{2} \approx 1.618",
            font_size=60,
            color=GOLD
        )
        self.play(Write(golden), run_time=2)

        # 定义方程
        equation = MathTex(
            r"x^2 = x + 1",
            font_size=48
        )
        equation.next_to(golden, DOWN, buff=0.5)
        self.play(Write(equation))

        # 几何展示
        self.play(
            golden.animate.to_edge(UP),
            equation.animate.next_to(golden, DOWN)
        )

        # 创建黄金矩形
        golden_rect = Rectangle(
            width=5,
            height=5 / 1.618,
            color=GOLD,
            stroke_width=3
        )
        golden_rect.shift(LEFT * 2)

        # 创建正方形
        square = Square(
            side_length=5 / 1.618,
            color=BLUE,
            stroke_width=2
        )
        square.move_to(golden_rect.get_left() + RIGHT * (5 / 1.618) / 2)

        # 小矩形
        small_rect = Rectangle(
            width=5 - 5 / 1.618,
            height=5 / 1.618,
            color=GREEN,
            stroke_width=2
        )
        small_rect.move_to(golden_rect.get_right() - RIGHT * (5 - 5 / 1.618) / 2)

        self.play(
            Create(golden_rect),
            Create(square),
            Create(small_rect),
            run_time=2
        )

        # 标注比例
        ratio_label = MathTex(r"\frac{a+b}{a} = \frac{a}{b} = \varphi", color=GOLD)
        ratio_label.next_to(golden_rect, DOWN)
        self.play(Write(ratio_label))

        # 斐波那契数列
        self.wait(2)
        self.play(
            FadeOut(golden_rect),
            FadeOut(square),
            FadeOut(small_rect),
            FadeOut(ratio_label)
        )

        fib_title = Text("斐波那契数列", font="STSong", font_size=36, color=BLUE)
        fib_title.next_to(equation, DOWN, buff=0.5)
        self.play(Write(fib_title))

        # 斐波那契数
        fib_numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
        fib_tex = VGroup()

        for i, num in enumerate(fib_numbers):
            num_tex = MathTex(str(num))
            num_tex.move_to(LEFT * 5 + RIGHT * i * 0.8)
            fib_tex.add(num_tex)

        self.play(Write(fib_tex), run_time=2)

        # 显示比值趋向黄金比例
        ratios = VGroup()
        for i in range(len(fib_numbers) - 1):
            ratio = fib_numbers[i + 1] / fib_numbers[i]
            ratio_tex = MathTex(f"\\frac{{{fib_numbers[i + 1]}}}{{{fib_numbers[i]}}} = {ratio:.3f}")
            ratio_tex.scale(0.6)
            ratios.add(ratio_tex)

        ratios.arrange(DOWN, buff=0.1)
        ratios.scale(0.8)
        ratios.next_to(fib_tex, DOWN, buff=0.5)

        # 只显示后几个比值
        for ratio in ratios[-4:]:
            self.play(Write(ratio), run_time=0.5)

        convergence = MathTex(r"\rightarrow \varphi", color=GOLD, font_size=48)
        convergence.next_to(ratios, RIGHT)
        self.play(Write(convergence))

        self.wait(2)

        # 清理
        self.play(
            FadeOut(golden),
            FadeOut(equation),
            FadeOut(fib_title),
            FadeOut(fib_tex),
            FadeOut(ratios[-4:]),
            FadeOut(convergence),
            run_time=1.5
        )

    def prime_number_theorem(self):
        """第十章：质数定理"""
        # 章节标题
        chapter = Text("第十章：质数定理", font="STSong", font_size=48)
        chapter_en = Text("Prime Number Theorem", font_size=24, color=GREY_A)
        chapter_group = VGroup(chapter, chapter_en).arrange(DOWN)

        self.play(Write(chapter), FadeIn(chapter_en), run_time=1.5)
        self.wait(1)
        self.play(FadeOut(chapter_group))

        # 质数定理公式
        pnt = MathTex(
            r"\pi(n) \sim \frac{n}{\ln(n)}",
            font_size=60
        )
        self.play(Write(pnt), run_time=2)

        # 解释
        explanation = Text(
            "π(n) 表示不超过 n 的质数个数",
            font="STSong",
            font_size=28,
            color=GREY_A
        )
        explanation.next_to(pnt, DOWN)
        self.play(Write(explanation))

        self.wait(2)

        # 可视化质数分布
        self.play(
            pnt.animate.to_edge(UP),
            FadeOut(explanation)
        )

        # 创建数轴显示质数
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

        number_line = NumberLine(
            x_range=[0, 50, 5],
            length=12,
            include_numbers=True
        )
        self.play(Create(number_line))

        # 标记质数
        prime_dots = VGroup()
        for p in primes:
            dot = Dot(
                point=number_line.n2p(p),
                color=RED,
                radius=0.08
            )
            prime_dots.add(dot)

        self.play(Create(prime_dots), run_time=2)

        # 显示密度递减
        density_text = Text(
            "质数密度随着数值增大而递减",
            font="STSong",
            font_size=28,
            color=BLUE
        )
        density_text.next_to(number_line, DOWN, buff=1)
        self.play(Write(density_text))

        # 显示具体数值
        values = VGroup(
            MathTex(r"\pi(10) = 4", color=GREEN),
            MathTex(r"\pi(100) = 25", color=GREEN),
            MathTex(r"\pi(1000) = 168", color=GREEN),
            MathTex(r"\pi(10000) = 1229", color=GREEN)
        ).arrange(DOWN, buff=0.2)
        values.scale(0.8)
        values.to_edge(LEFT)

        approximations = VGroup(
            MathTex(r"\frac{10}{\ln(10)} \approx 4.3", color=YELLOW),
            MathTex(r"\frac{100}{\ln(100)} \approx 21.7", color=YELLOW),
            MathTex(r"\frac{1000}{\ln(1000)} \approx 144.8", color=YELLOW),
            MathTex(r"\frac{10000}{\ln(10000)} \approx 1085.7", color=YELLOW)
        ).arrange(DOWN, buff=0.2)
        approximations.scale(0.8)
        approximations.to_edge(RIGHT)

        self.play(
            Write(values),
            Write(approximations),
            run_time=3
        )

        self.wait(2)

        # 清理
        self.play(
            FadeOut(pnt),
            FadeOut(number_line),
            FadeOut(prime_dots),
            FadeOut(density_text),
            FadeOut(values),
            FadeOut(approximations),
            run_time=1.5
        )

    def finale_symphony(self):
        """终章：公式的交响曲"""
        # 章节标题
        finale_title = Text(
            "终章：公式的交响曲",
            font="STSong",
            font_size=56,
            gradient=(BLUE, PURPLE, GOLD)
        )
        self.play(Write(finale_title), run_time=2)
        self.wait(1)
        self.play(FadeOut(finale_title))

        # 展示所有重要公式
        formulas = VGroup(
            MathTex(r"e^{i\pi} + 1 = 0", color=BLUE),
            MathTex(r"a^2 + b^2 = c^2", color=GREEN),
            MathTex(r"\int_a^b f(x)dx = F(b) - F(a)", color=YELLOW),
            MathTex(r"(a+b)^n = \sum_{k=0}^n \binom{n}{k}a^{n-k}b^k", color=ORANGE),
            MathTex(r"f(x) = \sum_{n=0}^\infty \frac{f^{(n)}(a)}{n!}(x-a)^n", color=RED),
            MathTex(r"\int_{-\infty}^\infty e^{-x^2}dx = \sqrt{\pi}", color=PURPLE),
            MathTex(r"P(A|B) = \frac{P(B|A)P(A)}{P(B)}", color=TEAL),
            MathTex(r"\varphi = \frac{1+\sqrt{5}}{2}", color=GOLD),
            MathTex(r"\pi(n) \sim \frac{n}{\ln(n)}", color=PINK)
        )

        # 排列成圆形
        formulas.arrange_in_grid(rows=3, cols=3, buff=0.5)
        formulas.scale(0.7)

        # 逐个显示
        for formula in formulas:
            self.play(FadeIn(formula, scale=0.5), run_time=0.5)

        self.wait(2)

        # 旋转排列
        self.play(
            formulas.animate.arrange_in_grid(rows=3, cols=3, buff=0.8),
            run_time=2
        )

        # 添加连线展示关系
        connections = VGroup()
        # 欧拉公式连接到泰勒级数
        connections.add(Line(
            formulas[0].get_center(),
            formulas[4].get_center(),
            color=GREY,
            stroke_width=1
        ))
        # 微积分连接到泰勒级数
        connections.add(Line(
            formulas[2].get_center(),
            formulas[4].get_center(),
            color=GREY,
            stroke_width=1
        ))

        self.play(Create(connections), run_time=1)

        # 结束语
        ending = VGroup(
            Text("数学公式", font="STSong", font_size=48, color=GOLD),
            Text("人类智慧的结晶", font="STSong", font_size=36, color=WHITE),
            Text("Mathematical Formulas", font_size=32, color=GREY_A),
            Text("The Crystallization of Human Wisdom", font_size=24, color=GREY_B)
        ).arrange(DOWN, buff=0.3)

        self.play(
            FadeOut(formulas),
            FadeOut(connections),
            run_time=1.5
        )

        for line in ending:
            self.play(Write(line), run_time=0.8)

        self.wait(3)

        # 最终淡出
        self.play(
            FadeOut(ending),
            run_time=2
        )


if __name__ == "__main__":
    # 渲染命令：
    # manim -pql mathematical_formulas.py MathematicalFormulasEvolution  # 低质量预览
    # manim -pqh mathematical_formulas.py MathematicalFormulasEvolution  # 高质量渲染
    pass