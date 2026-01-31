"""
═══════════════════════════════════════════════════════════════════════════════
    积分与浪漫邂逅 —— 领略数学几何之美
    Integration Meets Romance — Embracing the Beauty of Mathematical Geometry
    
    Manim Community Edition 动画脚本
    预计时长: 约 10 分钟 | Estimated Duration: ~10 minutes
    
    作者提示：请确保安装了 Manim Community 和所需字体
    Note: Ensure Manim Community and required fonts are installed
    
    运行命令: manim -pql integration_romance.py IntegrationAndRomance
═══════════════════════════════════════════════════════════════════════════════
"""

from manim import *
import numpy as np

# ═══════════════════════════════════════════════════════════════════════════════
# 全局配置 | Global Configuration
# ═══════════════════════════════════════════════════════════════════════════════

# Manim Community 配置
config.background_color = "#0a0a0a"

# 字体配置
CHINESE_FONT = "Source Han Sans SC"  # 思源黑体
ENGLISH_FONT = "Playfair Display"     # 优雅英文字体

# ═══════════════════════════════════════════════════════════════════════════════
# 辅助函数 | Helper Functions
# ═══════════════════════════════════════════════════════════════════════════════

def get_chinese_text(text, **kwargs):
    """创建中文文字"""
    return Text(text, font=CHINESE_FONT, **kwargs)

def get_english_text(text, **kwargs):
    """创建英文文字"""
    return Text(text, font=ENGLISH_FONT, **kwargs)

def get_bilingual_text(chinese, english, scale=0.6):
    """创建双语字幕"""
    cn = get_chinese_text(chinese).scale(scale)
    en = get_english_text(english).scale(scale * 0.8)
    en.next_to(cn, DOWN, buff=0.2)
    return VGroup(cn, en)

def random_bright_color():
    """生成随机亮色"""
    colors = [RED, BLUE, GREEN, YELLOW, PURPLE, PINK, ORANGE, TEAL, GOLD, MAROON]
    return np.random.choice(colors)


# ═══════════════════════════════════════════════════════════════════════════════
# 场景一：开场 —— 浩瀚星空中的数学
# Scene 1: Opening — Mathematics in the Starry Universe
# 时长约 60 秒 | Duration: ~60 seconds
# ═══════════════════════════════════════════════════════════════════════════════

class Scene01_Opening(Scene):
    def construct(self):
        # === 创建星空背景 ===
        stars = VGroup()
        np.random.seed(42)  # 确保可重复
        
        for _ in range(200):
            star = Dot(
                point=np.array([
                    np.random.uniform(-7, 7),
                    np.random.uniform(-4, 4),
                    0
                ]),
                radius=np.random.uniform(0.01, 0.04),
                color=np.random.choice([WHITE, BLUE_A, BLUE_B, YELLOW_A])
            )
            stars.add(star)
        
        # 星星闪烁进入
        self.play(
            LaggedStart(
                *[FadeIn(star, scale=0.1) for star in stars],
                lag_ratio=0.01,
                run_time=3
            )
        )
        
        # === 标题展示 ===
        title_cn = get_chinese_text("积分与浪漫邂逅").scale(1.2)
        title_cn.set_color_by_gradient(BLUE, PURPLE, PINK)
        
        title_en = get_english_text("Integration Meets Romance").scale(0.7)
        title_en.set_color(WHITE)
        title_en.next_to(title_cn, DOWN, buff=0.3)
        
        subtitle = get_bilingual_text(
            "领略数学几何之美",
            "Embracing the Beauty of Mathematical Geometry"
        ).scale(0.8)
        subtitle.next_to(title_en, DOWN, buff=0.5)
        
        # 标题动画
        self.play(Write(title_cn), run_time=2)
        self.play(FadeIn(title_en, shift=UP), run_time=1.5)
        self.wait(0.5)
        self.play(FadeIn(subtitle, shift=UP), run_time=1.5)
        
        # === 积分符号闪现 ===
        integral = MathTex(r"\int", color=GOLD).scale(5)
        integral.move_to(ORIGIN)
        integral.set_opacity(0)
        
        self.wait(1)
        
        title_group = VGroup(title_cn, title_en, subtitle)
        self.play(
            title_group.animate.shift(UP * 2).scale(0.7),
            run_time=1.5
        )
        
        # 积分符号出现
        self.play(
            integral.animate.set_opacity(1),
            Flash(integral.get_center(), color=GOLD, line_length=0.5, num_lines=12),
            run_time=1.5
        )
        
        # 让积分符号发光
        glow = integral.copy()
        glow.set_color(YELLOW)
        glow.set_stroke(YELLOW, width=10, opacity=0.5)
        
        self.play(
            FadeIn(glow),
            glow.animate.scale(1.2).set_opacity(0),
            run_time=1
        )
        self.remove(glow)
        
        # 过渡语
        quote = get_bilingual_text(
            "在数学的世界里，积分是连接离散与连续的桥梁",
            "In mathematics, integration bridges the discrete and continuous"
        )
        quote.to_edge(DOWN)
        
        self.play(FadeIn(quote), run_time=1.5)
        self.wait(2)
        
        # 淡出
        self.play(
            *[FadeOut(mob) for mob in self.mobjects],
            run_time=2
        )


# ═══════════════════════════════════════════════════════════════════════════════
# 场景二：积分的几何意义 —— 曲线下的面积
# Scene 2: Geometric Meaning of Integration — Area Under Curves
# 时长约 90 秒 | Duration: ~90 seconds
# ═══════════════════════════════════════════════════════════════════════════════

class Scene02_AreaUnderCurve(Scene):
    def construct(self):
        # === 标题 ===
        title = get_bilingual_text(
            "第一章：积分的几何意义",
            "Chapter 1: Geometric Meaning of Integration"
        )
        title.to_edge(UP)
        self.play(Write(title), run_time=2)
        self.wait(1)
        
        # === 坐标系 ===
        axes = Axes(
            x_range=[-0.5, 5, 1],
            y_range=[-0.5, 4, 1],
            x_length=8,
            y_length=5,
            axis_config={
                "include_tip": True,
                "include_numbers": True,
            },
            tips=True
        )
        axes.shift(DOWN * 0.5)
        
        x_label = axes.get_x_axis_label("x")
        y_label = axes.get_y_axis_label("y")
        
        self.play(
            Create(axes),
            Write(x_label),
            Write(y_label),
            run_time=2
        )
        
        # === 函数曲线 f(x) = sin(x) + 1.5 ===
        def func(x):
            return np.sin(x) + 1.5
        
        curve = axes.plot(func, x_range=[0.5, 4], color=YELLOW)
        curve.set_stroke(width=3)
        
        func_label = MathTex(r"f(x) = \sin(x) + 1.5", color=YELLOW).scale(0.8)
        func_label.next_to(curve, UP + RIGHT)
        
        self.play(
            Create(curve),
            Write(func_label),
            run_time=2
        )
        
        # === 解释文字 ===
        explanation = get_bilingual_text(
            "积分的本质，是计算曲线下的面积",
            "The essence of integration is calculating the area under a curve"
        )
        explanation.to_edge(DOWN)
        self.play(FadeIn(explanation), run_time=1.5)
        self.wait(1)
        
        # === 黎曼和动画 —— 矩形逼近 ===
        self.play(FadeOut(explanation))
        
        riemann_text = get_bilingual_text(
            "让我们用矩形来逼近这个面积",
            "Let's approximate this area with rectangles"
        )
        riemann_text.to_edge(DOWN)
        self.play(FadeIn(riemann_text), run_time=1)
        
        prev_rects = None
        prev_count = None
        
        # 不同数量的矩形
        for n_rects in [4, 8, 16, 32, 64]:
            dx = (4 - 0.5) / n_rects
            rects = axes.get_riemann_rectangles(
                curve,
                x_range=[0.5, 4],
                dx=dx,
                fill_opacity=0.6,
                stroke_width=1,
                stroke_color=WHITE
            )
            
            # 设置渐变色
            for i, rect in enumerate(rects):
                t = i / len(rects)
                rect.set_fill(color=interpolate_color(BLUE, GREEN, t))
            
            if n_rects == 4:
                self.play(Create(rects), run_time=2)
            else:
                self.play(
                    ReplacementTransform(prev_rects, rects),
                    run_time=1.5
                )
            
            # 显示矩形数量
            count_text = MathTex(f"n = {n_rects}").scale(0.8)
            count_text.to_corner(UR)
            
            if n_rects == 4:
                self.play(Write(count_text))
            else:
                self.play(
                    ReplacementTransform(prev_count, count_text),
                    run_time=0.5
                )
            
            prev_rects = rects
            prev_count = count_text
            self.wait(0.5)
        
        # === 极限过程 ===
        limit_text = get_bilingual_text(
            "当矩形数量趋向无穷，我们得到精确的面积",
            "As rectangles approach infinity, we get the exact area"
        )
        limit_text.to_edge(DOWN)
        self.play(
            ReplacementTransform(riemann_text, limit_text),
            run_time=1
        )
        
        # 填充精确面积
        area = axes.get_area(curve, x_range=[0.5, 4], color=[BLUE, GREEN])
        area.set_opacity(0.7)
        
        self.play(
            FadeOut(prev_rects),
            FadeOut(prev_count),
            FadeIn(area),
            run_time=2
        )
        
        # === 积分公式 ===
        integral_formula = MathTex(
            r"\int_{0.5}^{4} (\sin(x) + 1.5) \, dx = \text{Area}"
        ).scale(0.8)
        integral_formula.set_color_by_gradient(GOLD, YELLOW)
        integral_formula.next_to(limit_text, UP, buff=0.5)
        
        self.play(Write(integral_formula), run_time=2)
        self.wait(2)
        
        # 淡出
        self.play(
            *[FadeOut(mob) for mob in self.mobjects],
            run_time=2
        )


# ═══════════════════════════════════════════════════════════════════════════════
# 场景三：浪漫的心形曲线
# Scene 3: The Romantic Heart Curve
# 时长约 80 秒 | Duration: ~80 seconds
# ═══════════════════════════════════════════════════════════════════════════════

class Scene03_HeartCurve(Scene):
    def construct(self):
        # === 标题 ===
        title = get_bilingual_text(
            "第二章：浪漫的心形曲线",
            "Chapter 2: The Romantic Heart Curve"
        )
        title.to_edge(UP)
        self.play(Write(title), run_time=2)
        
        # === 心形曲线参数方程 ===
        equation_title = get_bilingual_text(
            "心形线的参数方程",
            "Parametric Equation of the Heart Curve"
        )
        equation_title.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(equation_title), run_time=1)
        
        # 参数方程
        parametric_eq = MathTex(
            r"x &= 16\sin^3(t) \\",
            r"y &= 13\cos(t) - 5\cos(2t) - 2\cos(3t) - \cos(4t)"
        ).scale(0.7)
        parametric_eq.set_color(PINK)
        
        self.play(Write(parametric_eq), run_time=2)
        self.wait(1)
        
        # 移动方程到角落
        self.play(
            FadeOut(equation_title),
            parametric_eq.animate.scale(0.8).to_corner(UL).shift(DOWN * 0.8),
            run_time=1
        )
        
        # === 绘制心形曲线 ===
        def heart_curve(t):
            x = 16 * np.sin(t) ** 3
            y = 13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)
            return np.array([x * 0.15, y * 0.15, 0])
        
        heart = ParametricFunction(
            heart_curve,
            t_range=[0, TAU],
            color=RED
        )
        heart.set_stroke(width=4)
        heart.shift(DOWN * 0.5)
        
        # 动态绘制
        trace_text = get_bilingual_text(
            "让爱随曲线绽放",
            "Let love bloom along the curve"
        )
        trace_text.to_edge(DOWN)
        self.play(FadeIn(trace_text), run_time=1)
        
        self.play(
            Create(heart),
            run_time=4,
            rate_func=smooth
        )
        
        # === 心形填充动画 ===
        self.play(FadeOut(trace_text), run_time=0.5)
        
        area_text = get_bilingual_text(
            "心形曲线围成的面积也可以用积分计算",
            "The area enclosed by the heart can be calculated by integration"
        )
        area_text.to_edge(DOWN)
        self.play(FadeIn(area_text), run_time=1)
        
        # 填充心形
        heart_filled = heart.copy()
        heart_filled.set_fill(RED, opacity=0.6)
        heart_filled.set_stroke(RED, width=2)
        
        self.play(
            Transform(heart, heart_filled),
            run_time=2
        )
        
        # === 面积积分公式 ===
        area_formula = MathTex(
            r"A = \frac{1}{2} \oint (x \, dy - y \, dx)"
        ).scale(0.8)
        area_formula.set_color(GOLD)
        area_formula.next_to(heart, RIGHT, buff=0.8)
        
        self.play(Write(area_formula), run_time=2)
        self.wait(1)
        
        # === 心跳动画 ===
        self.play(FadeOut(area_text))
        
        heartbeat_text = get_bilingual_text(
            "数学也有心跳的节奏",
            "Mathematics has its own heartbeat"
        )
        heartbeat_text.to_edge(DOWN)
        self.play(FadeIn(heartbeat_text), run_time=1)
        
        # 心跳效果
        for _ in range(3):
            self.play(
                heart.animate.scale(1.15),
                rate_func=there_and_back,
                run_time=0.6
            )
            self.wait(0.2)
        
        self.wait(1)
        
        # === 散落的小心 ===
        small_hearts = VGroup()
        np.random.seed(123)
        
        for _ in range(12):
            small_heart = ParametricFunction(
                heart_curve,
                t_range=[0, TAU],
                color=random_bright_color()
            )
            small_heart.scale(0.08)
            small_heart.set_fill(small_heart.get_color(), opacity=0.7)
            small_heart.move_to([
                np.random.uniform(-5, 5),
                np.random.uniform(-2.5, 2.5),
                0
            ])
            small_hearts.add(small_heart)
        
        self.play(
            LaggedStart(
                *[GrowFromCenter(h) for h in small_hearts],
                lag_ratio=0.1,
                run_time=2
            )
        )
        
        self.wait(2)
        
        # 淡出
        self.play(
            *[FadeOut(mob) for mob in self.mobjects],
            run_time=2
        )


# ═══════════════════════════════════════════════════════════════════════════════
# 场景四：玫瑰曲线之美
# Scene 4: Beauty of Rose Curves
# 时长约 70 秒 | Duration: ~70 seconds
# ═══════════════════════════════════════════════════════════════════════════════

class Scene04_RoseCurve(Scene):
    def construct(self):
        # === 标题 ===
        title = get_bilingual_text(
            "第三章：玫瑰曲线之美",
            "Chapter 3: Beauty of Rose Curves"
        )
        title.to_edge(UP)
        self.play(Write(title), run_time=2)
        
        # === 极坐标方程 ===
        equation = MathTex(r"r = a \cos(k\theta)", color=PINK).scale(1.2)
        equation.next_to(title, DOWN, buff=0.5)
        self.play(Write(equation), run_time=1.5)
        
        explanation = get_bilingual_text(
            "改变 k 值，获得不同花瓣的玫瑰",
            "Changing k produces roses with different petals"
        )
        explanation.to_edge(DOWN)
        self.play(FadeIn(explanation), run_time=1)
        
        # === 绘制不同 k 值的玫瑰曲线 ===
        def rose_curve(k, a=2):
            def curve(theta):
                r = a * np.cos(k * theta)
                x = r * np.cos(theta)
                y = r * np.sin(theta)
                return np.array([x, y, 0])
            return curve
        
        colors = [RED, PINK, MAROON, PURPLE, ORANGE]
        k_values = [2, 3, 4, 5, 6]
        
        roses = VGroup()
        k_labels = VGroup()
        
        positions = [
            LEFT * 3 + UP * 0.3,
            RIGHT * 3 + UP * 0.3,
            LEFT * 3 + DOWN * 2.2,
            ORIGIN + DOWN * 1.3,
            RIGHT * 3 + DOWN * 2.2
        ]
        
        for i, (k, color) in enumerate(zip(k_values, colors)):
            # 确定 theta 范围
            theta_max = TAU if k % 2 == 0 else PI
            
            rose = ParametricFunction(
                rose_curve(k),
                t_range=[0, theta_max],
                color=color
            )
            rose.set_stroke(width=3)
            rose.scale(0.5)
            rose.move_to(positions[i])
            
            k_label = MathTex(f"k = {k}", color=color).scale(0.6)
            k_label.next_to(rose, DOWN, buff=0.15)
            
            roses.add(rose)
            k_labels.add(k_label)
        
        # 逐个展示
        for rose, label in zip(roses, k_labels):
            self.play(
                Create(rose),
                Write(label),
                run_time=1.2
            )
            self.wait(0.2)
        
        self.wait(1)
        
        # === 玫瑰曲线的面积 ===
        self.play(FadeOut(explanation))
        
        area_text = get_bilingual_text(
            "玫瑰曲线的面积用极坐标积分计算",
            "Rose curve area is calculated using polar integration"
        )
        area_text.to_edge(DOWN)
        
        area_formula = MathTex(
            r"A = \frac{1}{2} \int_0^{2\pi} r^2 \, d\theta = \frac{\pi a^2}{2}"
        ).scale(0.7)
        area_formula.set_color(GOLD)
        area_formula.next_to(area_text, UP, buff=0.3)
        
        self.play(
            FadeIn(area_text),
            Write(area_formula),
            run_time=2
        )
        
        # === 花瓣填充动画 ===
        self.play(
            *[rose.animate.set_fill(rose.get_color(), opacity=0.5) 
              for rose in roses],
            run_time=2
        )
        
        self.wait(2)
        
        # === 动态变换 ===
        self.play(
            FadeOut(area_formula),
            FadeOut(area_text),
            FadeOut(k_labels),
            run_time=1
        )
        
        # 所有玫瑰移到中心并重叠
        transform_text = get_bilingual_text(
            "当玫瑰相遇，绽放无限美丽",
            "When roses meet, infinite beauty blooms"
        )
        transform_text.to_edge(DOWN)
        self.play(FadeIn(transform_text), run_time=1)
        
        self.play(
            *[rose.animate.move_to(ORIGIN + DOWN * 0.5).scale(1.8).set_opacity(0.4) 
              for rose in roses],
            run_time=3
        )
        
        self.wait(2)
        
        # 淡出
        self.play(
            *[FadeOut(mob) for mob in self.mobjects],
            run_time=2
        )


# ═══════════════════════════════════════════════════════════════════════════════
# 场景五：旋转体体积 —— 从二维到三维
# Scene 5: Volume of Revolution — From 2D to 3D
# 时长约 90 秒 | Duration: ~90 seconds
# ═══════════════════════════════════════════════════════════════════════════════

class Scene05_VolumeOfRevolution(Scene):
    def construct(self):
        # === 标题 ===
        title = get_bilingual_text(
            "第四章：旋转体的体积",
            "Chapter 4: Volume of Revolution"
        )
        title.to_edge(UP)
        self.play(Write(title), run_time=2)
        
        # === 初始曲线 ===
        axes = Axes(
            x_range=[-0.5, 4, 1],
            y_range=[-0.5, 3, 1],
            x_length=7,
            y_length=4,
            axis_config={"include_numbers": True}
        )
        axes.shift(DOWN * 0.5)
        
        self.play(Create(axes), run_time=1.5)
        
        # 函数 f(x) = sqrt(x)
        def func(x):
            return np.sqrt(x)
        
        curve = axes.plot(func, x_range=[0.01, 3.5], color=YELLOW)
        curve.set_stroke(width=3)
        
        func_label = MathTex(r"f(x) = \sqrt{x}", color=YELLOW).scale(0.8)
        func_label.next_to(curve, UP + RIGHT)
        
        self.play(
            Create(curve),
            Write(func_label),
            run_time=2
        )
        
        # === 解释 ===
        explanation = get_bilingual_text(
            "将曲线绕 x 轴旋转，形成三维立体",
            "Rotating the curve around x-axis forms a 3D solid"
        )
        explanation.to_edge(DOWN)
        self.play(FadeIn(explanation), run_time=1)
        self.wait(1)
        
        # === 显示旋转过程（用圆盘法） ===
        self.play(FadeOut(explanation))
        
        disk_text = get_bilingual_text(
            "圆盘法：将立体切成无数薄圆盘",
            "Disk Method: Slice the solid into thin disks"
        )
        disk_text.to_edge(DOWN)
        self.play(FadeIn(disk_text), run_time=1)
        
        # 创建圆盘（用椭圆表示侧面视角）
        disks = VGroup()
        x_vals = np.linspace(0.3, 3.2, 15)
        
        for x_val in x_vals:
            y_val = func(x_val)
            # 用椭圆表示侧面看的圆盘
            disk = Ellipse(
                width=0.18,
                height=2 * y_val * 0.65,
                color=BLUE,
                fill_opacity=0.5,
                stroke_width=2
            )
            disk_center = axes.c2p(x_val, 0)
            disk.move_to(disk_center)
            disks.add(disk)
        
        # 设置渐变色
        for i, disk in enumerate(disks):
            t = i / len(disks)
            disk.set_fill(interpolate_color(BLUE, TEAL, t), opacity=0.6)
        
        self.play(
            LaggedStart(
                *[GrowFromCenter(disk) for disk in disks],
                lag_ratio=0.1,
                run_time=3
            )
        )
        
        self.wait(1)
        
        # === 积分公式 ===
        self.play(FadeOut(disk_text))
        
        formula_text = get_bilingual_text(
            "体积等于所有圆盘体积之和",
            "Volume equals the sum of all disk volumes"
        )
        formula_text.to_edge(DOWN)
        self.play(FadeIn(formula_text), run_time=1)
        
        volume_formula = MathTex(
            r"V = \int_a^b \pi [f(x)]^2 \, dx = \int_0^b \pi x \, dx = \frac{\pi b^2}{2}"
        ).scale(0.7)
        volume_formula.set_color_by_gradient(BLUE, GREEN)
        volume_formula.to_corner(UR).shift(DOWN * 0.5 + LEFT * 0.3)
        
        self.play(Write(volume_formula), run_time=2)
        self.wait(1)
        
        # === 动态旋转效果 ===
        self.play(FadeOut(formula_text))
        
        rotate_text = get_bilingual_text(
            "想象曲线绕轴旋转的美妙过程",
            "Imagine the beautiful rotation around the axis"
        )
        rotate_text.to_edge(DOWN)
        self.play(FadeIn(rotate_text), run_time=1)
        
        # 模拟3D效果 - 让圆盘产生波动
        for _ in range(2):
            self.play(
                *[disk.animate.stretch(1.4, 0) for disk in disks],
                rate_func=there_and_back,
                run_time=1.2
            )
            self.wait(0.2)
        
        # === 填充效果 ===
        filled_area = axes.get_area(
            curve,
            x_range=[0.01, 3.5],
            color=[BLUE_E, TEAL],
            opacity=0.6
        )
        
        self.play(
            FadeOut(disks),
            FadeIn(filled_area),
            run_time=2
        )
        
        # 最终公式
        final_formula = MathTex(
            r"V = \frac{\pi b^2}{2}",
            color=GOLD
        ).scale(1)
        final_formula.next_to(volume_formula, DOWN, buff=0.5)
        
        # 添加方框
        box = SurroundingRectangle(final_formula, color=GOLD, buff=0.2)
        
        self.play(
            Write(final_formula),
            Create(box),
            run_time=1.5
        )
        
        self.wait(2)
        
        # 淡出
        self.play(
            *[FadeOut(mob) for mob in self.mobjects],
            run_time=2
        )


# ═══════════════════════════════════════════════════════════════════════════════
# 场景六：螺旋之美 —— 阿基米德与费马
# Scene 6: Beauty of Spirals — Archimedes and Fermat
# 时长约 70 秒 | Duration: ~70 seconds
# ═══════════════════════════════════════════════════════════════════════════════

class Scene06_Spirals(Scene):
    def construct(self):
        # === 标题 ===
        title = get_bilingual_text(
            "第五章：螺旋之美",
            "Chapter 5: Beauty of Spirals"
        )
        title.to_edge(UP)
        self.play(Write(title), run_time=2)
        
        # === 阿基米德螺旋 ===
        def archimedean_spiral(t):
            a = 0.1
            r = a * t
            return np.array([r * np.cos(t), r * np.sin(t), 0])
        
        archimedes = ParametricFunction(
            archimedean_spiral,
            t_range=[0, 6 * PI],
            color=BLUE
        )
        archimedes.set_stroke(width=3)
        archimedes.scale(0.9)
        archimedes.shift(LEFT * 3.5 + DOWN * 0.3)
        
        archimedes_label = MathTex(r"r = a\theta", color=BLUE).scale(0.7)
        archimedes_label.next_to(archimedes, DOWN, buff=0.3)
        
        archimedes_name = get_chinese_text("阿基米德螺线").scale(0.45)
        archimedes_name.next_to(archimedes_label, DOWN, buff=0.1)
        
        # === 费马螺旋 ===
        def fermat_spiral_pos(t):
            a = 0.35
            r = a * np.sqrt(t)
            return np.array([r * np.cos(t), r * np.sin(t), 0])
        
        def fermat_spiral_neg(t):
            a = 0.35
            r = -a * np.sqrt(t)
            return np.array([r * np.cos(t), r * np.sin(t), 0])
        
        fermat_pos = ParametricFunction(
            fermat_spiral_pos,
            t_range=[0, 6 * PI],
            color=GREEN
        )
        fermat_neg = ParametricFunction(
            fermat_spiral_neg,
            t_range=[0, 6 * PI],
            color=GREEN
        )
        fermat = VGroup(fermat_pos, fermat_neg)
        fermat.set_stroke(width=3)
        fermat.scale(0.85)
        fermat.shift(RIGHT * 3.5 + DOWN * 0.3)
        
        fermat_label = MathTex(r"r^2 = a^2\theta", color=GREEN).scale(0.7)
        fermat_label.next_to(fermat, DOWN, buff=0.3)
        
        fermat_name = get_chinese_text("费马螺线").scale(0.45)
        fermat_name.next_to(fermat_label, DOWN, buff=0.1)
        
        # 动画展示
        self.play(
            Create(archimedes),
            Create(fermat_pos),
            Create(fermat_neg),
            run_time=4
        )
        
        self.play(
            Write(archimedes_label),
            Write(fermat_label),
            FadeIn(archimedes_name),
            FadeIn(fermat_name),
            run_time=1.5
        )
        
        # === 对数螺旋 ===
        self.wait(1)
        
        log_text = get_bilingual_text(
            "对数螺旋 —— 自然界最美的曲线",
            "Logarithmic Spiral — Nature's most beautiful curve"
        )
        log_text.to_edge(DOWN)
        self.play(FadeIn(log_text), run_time=1)
        
        def logarithmic_spiral(t):
            a = 0.1
            b = 0.12
            r = a * np.exp(b * t)
            return np.array([r * np.cos(t), r * np.sin(t), 0])
        
        log_spiral = ParametricFunction(
            logarithmic_spiral,
            t_range=[0, 4.5 * PI],
            color=GOLD
        )
        log_spiral.set_stroke(width=4)
        
        # 淡出之前的螺旋
        self.play(
            FadeOut(archimedes),
            FadeOut(fermat),
            FadeOut(archimedes_label),
            FadeOut(fermat_label),
            FadeOut(archimedes_name),
            FadeOut(fermat_name),
            run_time=1
        )
        
        self.play(
            Create(log_spiral),
            run_time=3
        )
        
        log_equation = MathTex(r"r = ae^{b\theta}", color=GOLD).scale(1)
        log_equation.to_corner(UR).shift(DOWN * 0.5)
        self.play(Write(log_equation), run_time=1)
        
        # === 黄金螺旋联系 ===
        golden_text = get_bilingual_text(
            "它与黄金分割有着神秘的联系",
            "It has a mysterious connection to the Golden Ratio"
        )
        golden_text.to_edge(DOWN)
        self.play(
            ReplacementTransform(log_text, golden_text),
            run_time=1
        )
        
        # 黄金分割比
        golden_ratio = MathTex(
            r"\phi = \frac{1 + \sqrt{5}}{2} \approx 1.618",
            color=YELLOW
        ).scale(0.8)
        golden_ratio.next_to(log_equation, DOWN, buff=0.5)
        
        self.play(Write(golden_ratio), run_time=1.5)
        
        # 添加发光效果
        glow = log_spiral.copy()
        glow.set_stroke(YELLOW, width=8, opacity=0.4)
        
        self.play(
            FadeIn(glow),
            glow.animate.scale(1.05).set_opacity(0),
            run_time=1.5
        )
        
        self.wait(2)
        
        # 淡出
        self.play(
            *[FadeOut(mob) for mob in self.mobjects],
            run_time=2
        )


# ═══════════════════════════════════════════════════════════════════════════════
# 场景七：傅里叶级数 —— 用圆画出一切
# Scene 7: Fourier Series — Drawing Everything with Circles
# 时长约 90 秒 | Duration: ~90 seconds
# ═══════════════════════════════════════════════════════════════════════════════

class Scene07_FourierSeries(Scene):
    def construct(self):
        # === 标题 ===
        title = get_bilingual_text(
            "第六章：傅里叶的魔法",
            "Chapter 6: Fourier's Magic"
        )
        title.to_edge(UP)
        self.play(Write(title), run_time=2)
        
        # === 介绍 ===
        intro = get_bilingual_text(
            "用旋转的圆可以画出任何图形",
            "Rotating circles can draw any shape"
        )
        intro.to_edge(DOWN)
        self.play(FadeIn(intro), run_time=1)
        
        # === 傅里叶级数公式 ===
        fourier_eq = MathTex(
            r"f(x) = \sum_{n=-\infty}^{\infty} c_n e^{inx}"
        ).scale(1)
        fourier_eq.set_color_by_gradient(BLUE, PURPLE)
        
        self.play(Write(fourier_eq), run_time=2)
        self.wait(1)
        
        self.play(
            fourier_eq.animate.scale(0.6).to_corner(UL).shift(DOWN * 0.8),
            run_time=1
        )
        
        # === 方波的傅里叶分解 ===
        self.play(FadeOut(intro))
        
        square_text = get_bilingual_text(
            "让我们用正弦波合成方波",
            "Let's synthesize a square wave with sine waves"
        )
        square_text.to_edge(DOWN)
        self.play(FadeIn(square_text), run_time=1)
        
        # 坐标系
        axes = Axes(
            x_range=[-4, 4, 1],
            y_range=[-2, 2, 1],
            x_length=10,
            y_length=4,
            axis_config={"include_numbers": False}
        )
        axes.shift(DOWN * 0.3)
        
        self.play(Create(axes), run_time=1)
        
        # 傅里叶级数逐项相加
        def square_wave_approx(n_terms):
            def func(x):
                result = 0
                for n in range(1, n_terms + 1, 2):
                    result += (4 / (n * PI)) * np.sin(n * x)
                return result
            return func
        
        colors = [RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE]
        n_values = [1, 3, 5, 9, 15, 25]
        
        prev_curve = None
        prev_label = None
        
        for i, n in enumerate(n_values):
            func = square_wave_approx(n)
            curve = axes.plot(func, x_range=[-3.8, 3.8], color=colors[i % len(colors)])
            curve.set_stroke(width=3)
            
            n_label = MathTex(f"n = {n}").scale(0.8)
            n_label.to_corner(UR)
            
            if prev_curve is None:
                self.play(
                    Create(curve),
                    Write(n_label),
                    run_time=1.5
                )
            else:
                self.play(
                    ReplacementTransform(prev_curve, curve),
                    ReplacementTransform(prev_label, n_label),
                    run_time=1
                )
            
            prev_curve = curve
            prev_label = n_label
            self.wait(0.3)
        
        # === 理想方波 ===
        self.play(FadeOut(square_text))
        
        perfect_text = get_bilingual_text(
            "当项数趋向无穷，完美的方波出现",
            "As terms approach infinity, a perfect square wave emerges"
        )
        perfect_text.to_edge(DOWN)
        self.play(FadeIn(perfect_text), run_time=1)
        
        # 画出接近理想的方波
        high_approx = square_wave_approx(99)
        square_wave = axes.plot(high_approx, x_range=[-3.8, 3.8], color=WHITE)
        square_wave.set_stroke(width=3)
        
        self.play(
            ReplacementTransform(prev_curve, square_wave),
            FadeOut(prev_label),
            run_time=2
        )
        
        infinity_label = MathTex(r"n \to \infty").scale(0.8)
        infinity_label.to_corner(UR)
        self.play(Write(infinity_label), run_time=1)
        
        self.wait(2)
        
        # === 圆的叠加可视化 ===
        self.play(
            FadeOut(square_wave),
            FadeOut(axes),
            FadeOut(perfect_text),
            FadeOut(infinity_label),
            run_time=1
        )
        
        circle_text = get_bilingual_text(
            "每一项都是一个旋转的圆",
            "Each term is a rotating circle"
        )
        circle_text.to_edge(DOWN)
        self.play(FadeIn(circle_text), run_time=1)
        
        # 创建叠加的圆
        circles = VGroup()
        radii = [1.5, 0.5, 0.3, 0.2, 0.15]
        colors_c = [BLUE, GREEN, YELLOW, ORANGE, RED]
        
        current_center = ORIGIN
        for r, c in zip(radii, colors_c):
            circle = Circle(radius=r, color=c, stroke_width=3)
            circle.move_to(current_center)
            circles.add(circle)
            current_center = circle.point_at_angle(0)
        
        self.play(
            LaggedStart(
                *[Create(c) for c in circles],
                lag_ratio=0.3,
                run_time=2
            )
        )
        
        # 添加圆心连线和轨迹点
        dots = VGroup()
        for i, circle in enumerate(circles):
            dot = Dot(circle.get_center(), color=colors_c[i], radius=0.05)
            dots.add(dot)
        
        self.play(FadeIn(dots), run_time=0.5)
        
        # 旋转动画
        angle = PI
        self.play(
            Rotate(circles, angle=angle, about_point=ORIGIN),
            Rotate(dots, angle=angle, about_point=ORIGIN),
            run_time=3,
            rate_func=smooth
        )
        
        self.wait(1)
        
        # 结语
        ending = get_bilingual_text(
            "傅里叶揭示：复杂源于简单的叠加",
            "Fourier revealed: complexity arises from simple superposition"
        )
        ending.to_edge(DOWN)
        self.play(
            ReplacementTransform(circle_text, ending),
            run_time=1
        )
        
        self.wait(2)
        
        # 淡出
        self.play(
            *[FadeOut(mob) for mob in self.mobjects],
            run_time=2
        )


# ═══════════════════════════════════════════════════════════════════════════════
# 场景八：终章 —— 积分之诗
# Scene 8: Finale — The Poetry of Integration
# 时长约 80 秒 | Duration: ~80 seconds
# ═══════════════════════════════════════════════════════════════════════════════

class Scene08_Finale(Scene):
    def construct(self):
        # === 诗意开场 ===
        poem_lines_cn = [
            "积分如诗，",
            "将无穷微小化为宏大；",
            "几何如画，",
            "让抽象数字变得可见。"
        ]
        
        poem_cn = VGroup(*[get_chinese_text(line).scale(0.7) for line in poem_lines_cn])
        poem_cn.arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        poem_cn.move_to(ORIGIN)
        
        for line in poem_cn:
            self.play(Write(line), run_time=1.5)
            self.wait(0.3)
        
        self.wait(1)
        
        self.play(
            poem_cn.animate.shift(UP * 2).scale(0.8),
            run_time=1.5
        )
        
        # === 英文诗 ===
        poem_lines_en = [
            "Integration, like poetry,",
            "transforms the infinitesimal into the grand;",
            "Geometry, like art,",
            "makes abstract numbers visible."
        ]
        
        poem_en = VGroup(*[get_english_text(line).scale(0.5) for line in poem_lines_en])
        poem_en.arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        poem_en.set_color(BLUE_B)
        poem_en.next_to(poem_cn, DOWN, buff=0.5)
        
        self.play(
            LaggedStart(
                *[FadeIn(line, shift=UP) for line in poem_en],
                lag_ratio=0.3,
                run_time=2
            )
        )
        
        self.wait(2)
        
        # === 经典积分符号 ===
        self.play(
            FadeOut(poem_cn),
            FadeOut(poem_en),
            run_time=1
        )
        
        integral_symbol = MathTex(r"\int_a^b f(x) \, dx").scale(2.5)
        integral_symbol.set_color_by_gradient(GOLD, YELLOW, ORANGE)
        
        self.play(Write(integral_symbol), run_time=3)
        
        # 发光效果
        for _ in range(2):
            glow = integral_symbol.copy()
            glow.set_stroke(color=YELLOW, width=15, opacity=0.5)
            
            self.play(
                FadeIn(glow),
                glow.animate.scale(1.15).set_opacity(0),
                run_time=1.2
            )
            self.remove(glow)
        
        # === 最终信息 ===
        final_cn = get_chinese_text("数学之美，无处不在").scale(0.8)
        final_en = get_english_text("Mathematical beauty is everywhere").scale(0.6)
        final_en.set_color(BLUE_B)
        
        final_text = VGroup(final_cn, final_en)
        final_en.next_to(final_cn, DOWN, buff=0.2)
        final_text.to_edge(DOWN)
        
        self.play(
            integral_symbol.animate.shift(UP),
            FadeIn(final_text, shift=UP),
            run_time=1.5
        )
        
        self.wait(1)
        
        # === 绘制装饰性曲线 ===
        np.random.seed(456)
        background_curves = VGroup()
        
        for _ in range(8):
            # 随机花瓣形状
            k = np.random.choice([2, 3, 4, 5])
            def make_curve(k_val):
                def curve(t):
                    r = 1 + 0.5 * np.sin(k_val * t)
                    return np.array([r * np.cos(t), r * np.sin(t), 0])
                return curve
            
            decoration = ParametricFunction(
                make_curve(k),
                t_range=[0, TAU],
                color=random_bright_color()
            )
            decoration.scale(np.random.uniform(0.3, 0.7))
            decoration.move_to([
                np.random.uniform(-5, 5),
                np.random.uniform(-1.5, 1.5),
                0
            ])
            decoration.set_opacity(0.3)
            background_curves.add(decoration)
        
        self.play(
            LaggedStart(
                *[Create(c) for c in background_curves],
                lag_ratio=0.1,
                run_time=3
            )
        )
        
        self.wait(2)
        
        # === 致谢 ===
        thank_cn = get_chinese_text("感谢观看").scale(1.2)
        thank_en = get_english_text("Thank You for Watching").scale(0.8)
        thank_en.next_to(thank_cn, DOWN, buff=0.3)
        thanks = VGroup(thank_cn, thank_en)
        thanks.set_color_by_gradient(PINK, PURPLE)
        
        self.play(
            FadeOut(background_curves),
            FadeOut(final_text),
            integral_symbol.animate.scale(0.4).to_edge(UP),
            run_time=1.5
        )
        
        self.play(Write(thanks), run_time=2)
        
        # 心形点缀
        def heart_curve(t):
            x = 16 * np.sin(t) ** 3
            y = 13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)
            return np.array([x * 0.04, y * 0.04, 0])
        
        small_hearts = VGroup()
        np.random.seed(789)
        
        for _ in range(8):
            heart = ParametricFunction(
                heart_curve,
                t_range=[0, TAU],
                color=RED,
                fill_opacity=0.6
            )
            heart.set_fill(RED, opacity=0.6)
            heart.move_to([
                np.random.uniform(-5, 5),
                np.random.uniform(-2, 2),
                0
            ])
            small_hearts.add(heart)
        
        self.play(
            LaggedStart(
                *[GrowFromCenter(h) for h in small_hearts],
                lag_ratio=0.15,
                run_time=2
            )
        )
        
        # 心跳效果
        for _ in range(2):
            self.play(
                *[h.animate.scale(1.2) for h in small_hearts],
                rate_func=there_and_back,
                run_time=0.6
            )
            self.wait(0.3)
        
        self.wait(2)
        
        # 最终淡出
        self.play(
            *[FadeOut(mob, scale=0.5) for mob in self.mobjects],
            run_time=3
        )
        
        # 黑屏等待
        self.wait(1)


# ═══════════════════════════════════════════════════════════════════════════════
# 主场景：完整动画
# Main Scene: Complete Animation
# 将所有场景串联在一起
# ═══════════════════════════════════════════════════════════════════════════════

class IntegrationAndRomance(Scene):
    """
    完整动画入口 - Manim Community Edition
    
    运行命令:
        manim -pql integration_romance.py IntegrationAndRomance   # 低质量预览
        manim -pqh integration_romance.py IntegrationAndRomance   # 高质量
        manim -pqk integration_romance.py IntegrationAndRomance   # 4K质量
    """
    def construct(self):
        # 场景1: 开场
        Scene01_Opening.construct(self)
        
        # 场景2: 积分的几何意义
        Scene02_AreaUnderCurve.construct(self)
        
        # 场景3: 心形曲线
        Scene03_HeartCurve.construct(self)
        
        # 场景4: 玫瑰曲线
        Scene04_RoseCurve.construct(self)
        
        # 场景5: 旋转体体积
        Scene05_VolumeOfRevolution.construct(self)
        
        # 场景6: 螺旋之美
        Scene06_Spirals.construct(self)
        
        # 场景7: 傅里叶级数
        Scene07_FourierSeries.construct(self)
        
        # 场景8: 终章
        Scene08_Finale.construct(self)


# ═══════════════════════════════════════════════════════════════════════════════
# 3D 加强版场景：心形曲面
# 3D Enhanced Scene: Heart Surface
# ═══════════════════════════════════════════════════════════════════════════════

class Scene3D_HeartSurface(ThreeDScene):
    """
    3D心形曲面展示 - 需要 ThreeDScene
    运行: manim -pql integration_romance.py Scene3D_HeartSurface
    """
    def construct(self):
        # 设置相机
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)
        
        # 3D 坐标轴
        axes = ThreeDAxes(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            z_range=[-3, 3, 1],
            x_length=6,
            y_length=6,
            z_length=6
        )
        
        self.play(Create(axes), run_time=2)
        
        # 3D 心形曲面参数化
        def heart_surface(u, v):
            # 基于心形曲线的旋转曲面
            x = 16 * np.sin(u) ** 3
            y = 13 * np.cos(u) - 5 * np.cos(2*u) - 2 * np.cos(3*u) - np.cos(4*u)
            # 绕 y 轴旋转
            scale = 0.1
            return np.array([
                x * np.cos(v) * scale,
                y * scale,
                x * np.sin(v) * scale
            ])
        
        heart_3d = Surface(
            heart_surface,
            u_range=[0, TAU],
            v_range=[0, TAU],
            resolution=(50, 50),
            fill_opacity=0.8,
            checkerboard_colors=[RED_D, RED_E],
            stroke_width=0.5
        )
        
        self.play(Create(heart_3d), run_time=4)
        
        # 旋转展示
        self.begin_ambient_camera_rotation(rate=0.3)
        self.wait(5)
        self.stop_ambient_camera_rotation()
        
        # 标题
        title = Text("3D Heart Surface", font_size=36, color=PINK)
        title.to_corner(UL)
        title.fix_in_frame()
        
        self.play(Write(title), run_time=1)
        self.wait(2)
        
        self.play(
            *[FadeOut(mob) for mob in self.mobjects],
            run_time=2
        )


# ═══════════════════════════════════════════════════════════════════════════════
# 3D 加强版场景：旋转体
# 3D Enhanced Scene: Surface of Revolution
# ═══════════════════════════════════════════════════════════════════════════════

class Scene3D_Revolution(ThreeDScene):
    """
    真正的3D旋转体展示
    运行: manim -pql integration_romance.py Scene3D_Revolution
    """
    def construct(self):
        self.set_camera_orientation(phi=70 * DEGREES, theta=-60 * DEGREES)
        
        axes = ThreeDAxes(
            x_range=[0, 4, 1],
            y_range=[-2, 2, 1],
            z_range=[-2, 2, 1],
            x_length=6,
            y_length=4,
            z_length=4
        )
        
        self.play(Create(axes), run_time=1.5)
        
        # f(x) = sqrt(x) 绕 x 轴旋转
        def revolution_surface(u, v):
            x = u
            r = np.sqrt(u) if u > 0 else 0
            return np.array([
                x,
                r * np.cos(v),
                r * np.sin(v)
            ])
        
        surface = Surface(
            revolution_surface,
            u_range=[0.01, 3],
            v_range=[0, TAU],
            resolution=(30, 30),
            fill_opacity=0.7,
            checkerboard_colors=[BLUE_D, BLUE_E],
            stroke_width=0.3
        )
        
        # 标题
        title = MathTex(r"V = \int_0^b \pi x \, dx", font_size=36, color=GOLD)
        title.to_corner(UL)
        title.fix_in_frame()
        
        self.play(Write(title), run_time=1)
        self.play(Create(surface), run_time=4)
        
        # 旋转展示
        self.begin_ambient_camera_rotation(rate=0.2)
        self.wait(6)
        self.stop_ambient_camera_rotation()
        
        self.play(
            *[FadeOut(mob) for mob in self.mobjects],
            run_time=2
        )


# ═══════════════════════════════════════════════════════════════════════════════
# 运行说明 | Instructions
# ═══════════════════════════════════════════════════════════════════════════════
"""
【Manim Community Edition 运行方式】

═══════════════════════════════════════════════════════════════════════════════
基本命令 | Basic Commands
═══════════════════════════════════════════════════════════════════════════════

1. 运行完整动画 (低质量预览 - 快速):
   manim -pql integration_romance.py IntegrationAndRomance
   
2. 运行完整动画 (高质量):
   manim -pqh integration_romance.py IntegrationAndRomance
   
3. 运行完整动画 (4K超高质量):
   manim -pqk integration_romance.py IntegrationAndRomance

4. 运行单个场景:
   manim -pql integration_romance.py Scene01_Opening
   manim -pql integration_romance.py Scene02_AreaUnderCurve
   manim -pql integration_romance.py Scene03_HeartCurve
   manim -pql integration_romance.py Scene04_RoseCurve
   manim -pql integration_romance.py Scene05_VolumeOfRevolution
   manim -pql integration_romance.py Scene06_Spirals
   manim -pql integration_romance.py Scene07_FourierSeries
   manim -pql integration_romance.py Scene08_Finale

5. 运行3D场景:
   manim -pql integration_romance.py Scene3D_HeartSurface
   manim -pql integration_romance.py Scene3D_Revolution

═══════════════════════════════════════════════════════════════════════════════
命令参数说明 | Command Arguments
═══════════════════════════════════════════════════════════════════════════════

-p : 预览 (播放生成的视频)
-q : 质量设置
     l = 低质量 (480p, 15fps) - 快速预览
     m = 中等质量 (720p, 30fps)
     h = 高质量 (1080p, 60fps)
     k = 4K质量 (2160p, 60fps)
-a : 渲染所有场景
-s : 只保存最后一帧 (截图)
--format gif : 输出GIF格式

═══════════════════════════════════════════════════════════════════════════════
安装依赖 | Installation
═══════════════════════════════════════════════════════════════════════════════

# 安装 Manim Community
pip install manim

# 或使用 conda
conda install -c conda-forge manim

# 验证安装
manim --version

═══════════════════════════════════════════════════════════════════════════════
字体安装 | Font Installation
═══════════════════════════════════════════════════════════════════════════════

1. 思源黑体 (Source Han Sans SC):
   - 下载: https://github.com/adobe-fonts/source-han-sans/releases
   - 或: https://fonts.google.com/specimen/Noto+Sans+SC
   
2. Playfair Display:
   - 下载: https://fonts.google.com/specimen/Playfair+Display

3. 安装字体后重启 Manim

═══════════════════════════════════════════════════════════════════════════════
预计时长 | Estimated Duration
═══════════════════════════════════════════════════════════════════════════════

场景1 (开场): ~60秒
场景2 (积分几何意义): ~90秒
场景3 (心形曲线): ~80秒
场景4 (玫瑰曲线): ~70秒
场景5 (旋转体体积): ~90秒
场景6 (螺旋之美): ~70秒
场景7 (傅里叶级数): ~90秒
场景8 (终章): ~80秒
──────────────────────────────────────
总计: ~630秒 (约10.5分钟)

═══════════════════════════════════════════════════════════════════════════════
常见问题 | Troubleshooting
═══════════════════════════════════════════════════════════════════════════════

1. 字体未找到:
   - 确保字体已正确安装在系统中
   - 可以修改 CHINESE_FONT 和 ENGLISH_FONT 变量使用其他可用字体
   
2. LaTeX 错误:
   - 确保安装了 LaTeX 发行版 (如 TeX Live, MiKTeX)
   - 或使用 MathTex 替代 Tex
   
3. 内存不足:
   - 使用低质量模式 (-ql) 进行预览
   - 分场景渲染

4. 颜色显示问题:
   - 确保使用 Manim 内置颜色常量
   - 或使用十六进制颜色 "#RRGGBB"
"""

if __name__ == "__main__":
    print("Manim Community Edition - 积分与浪漫邂逅")
    print("=" * 60)
    print("运行完整动画: manim -pql integration_romance.py IntegrationAndRomance")
    print("=" * 60)
