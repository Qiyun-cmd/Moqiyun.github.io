import os
os.environ["PYTHONIOENCODING"] = "utf-8"
from manim import *
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from my_manim_setup import *
# 设置使用 XeLaTeX 并全局支持中文
config.tex_compiler = "xelatex"  # 重要：必须安装 XeLaTeX
config.tex_template = TexTemplateLibrary.ctex  # 使用中文模板 (需确认是否已加载)

from manim import *
import numpy as np
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
class PhysicsFormulasAnimation(Scene):
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1e1e1e"
        
        # 标题动画
        self.show_title()
        
        # 1. 经典力学部分 (约2分钟)
        self.classical_mechanics()
        
        # 2. 电磁学部分 (约2分钟)
        self.electromagnetism()
        
        # 3. 热力学部分 (约1.5分钟)
        self.thermodynamics()
        
        # 4. 量子力学部分 (约2分钟)
        self.quantum_mechanics()
        
        # 5. 相对论部分 (约2分钟)
        self.relativity()
        
        # 结尾 (约0.5分钟)
        self.ending()
    
    def show_title(self):
        title = Text("物理学核心公式", font_size=72, color=BLUE)
        subtitle = Text("数形结合的动态演示", font_size=36, color=WHITE)
        subtitle.next_to(title, DOWN)
        
        self.play(Write(title), run_time=2)
        self.play(FadeIn(subtitle), run_time=1)
        self.wait(2)
        self.play(FadeOut(title), FadeOut(subtitle))
        
    def classical_mechanics(self):
        # 章节标题
        section_title = Text("经典力学", font_size=48, color=YELLOW)
        self.play(Write(section_title))
        self.wait(1)
        self.play(section_title.animate.to_edge(UP).scale(0.7))
        
        # 牛顿第二定律 F = ma
        self.newton_second_law()
        
        # 动能定理
        self.kinetic_energy()
        
        # 简谐振动
        self.simple_harmonic_motion()
        
        self.clear()
        
    def newton_second_law(self):
        # 公式
        formula = MathTex(r"\vec{F} = m\vec{a}", font_size=60)
        formula.to_edge(UP, buff=1.5)
        self.play(Write(formula))
        
        # 创建物体
        mass = Square(side_length=1, color=BLUE, fill_opacity=0.8)
        mass_label = MathTex("m", color=WHITE).scale(0.8)
        mass_label.move_to(mass.get_center())
        object_group = VGroup(mass, mass_label)
        object_group.shift(LEFT * 4)
        
        # 力的箭头
        force_arrow = Arrow(
            start=object_group.get_right(),
            end=object_group.get_right() + RIGHT * 2,
            color=RED,
            buff=0
        )
        force_label = MathTex(r"\vec{F}", color=RED).next_to(force_arrow, UP)
        
        self.play(FadeIn(object_group))
        self.play(GrowArrow(force_arrow), Write(force_label))
        
        # 演示加速运动
        path = Line(object_group.get_center(), object_group.get_center() + RIGHT * 6)
        
        def update_arrow(arrow):
            arrow.put_start_and_end_on(
                object_group.get_right(),
                object_group.get_right() + RIGHT * 2
            )
        
        force_arrow.add_updater(update_arrow)
        force_label.add_updater(lambda m: m.next_to(force_arrow, UP))
        
        self.play(
            MoveAlongPath(object_group, path, rate_func=rate_functions.ease_in_quad),
            run_time=3
        )
        
        force_arrow.clear_updaters()
        force_label.clear_updaters()
        
        self.wait(1)
        self.play(FadeOut(VGroup(formula, object_group, force_arrow, force_label)))
        
    def kinetic_energy(self):
        # 动能公式
        formula = MathTex(r"E_k = \frac{1}{2}mv^2", font_size=60)
        formula.to_edge(UP, buff=1.5)
        self.play(Write(formula))
        
        # 创建坐标系
        axes = Axes(
            x_range=[0, 10, 1],
            y_range=[0, 50, 10],
            x_length=8,
            y_length=5,
            axis_config={"color": GREY}
        ).shift(DOWN * 0.5)
        
        x_label = MathTex("v").next_to(axes.x_axis, RIGHT)
        y_label = MathTex("E_k").next_to(axes.y_axis, UP)
        
        # 绘制抛物线
        parabola = axes.plot(
            lambda x: 0.5 * x**2,
            x_range=[0, 10],
            color=GREEN
        )
        
        self.play(Create(axes), Write(x_label), Write(y_label))
        self.play(Create(parabola), run_time=2)
        
        # 动态点
        dot = Dot(color=YELLOW)
        value_tracker = ValueTracker(0)
        
        dot.add_updater(
            lambda m: m.move_to(axes.c2p(value_tracker.get_value(), 0.5 * value_tracker.get_value()**2))
        )
        
        # 速度和能量标签
        v_label = always_redraw(
            lambda: MathTex(f"v = {value_tracker.get_value():.1f}", color=BLUE).next_to(dot, UR)
        )
        ek_label = always_redraw(
            lambda: MathTex(f"E_k = {0.5 * value_tracker.get_value()**2:.1f}", color=GREEN).next_to(dot, RIGHT)
        )
        
        self.play(FadeIn(dot), Write(v_label), Write(ek_label))
        self.play(value_tracker.animate.set_value(8), run_time=4)
        
        self.wait(1)
        self.play(FadeOut(VGroup(formula, axes, x_label, y_label, parabola, dot, v_label, ek_label)))
        
    def simple_harmonic_motion(self):
        # 简谐振动公式
        formula = MathTex(r"x(t) = A\cos(\omega t + \phi)", font_size=60)
        formula.to_edge(UP, buff=1.5)
        self.play(Write(formula))
        
        # 创建弹簧振子
        spring_start = LEFT * 4
        spring_end = LEFT * 2
        
        spring = self.create_spring(spring_start, spring_end)
        mass = Circle(radius=0.5, color=BLUE, fill_opacity=0.8)
        mass.next_to(spring_end, RIGHT, buff=0)
        
        self.play(Create(spring), FadeIn(mass))
        
        # 振动动画
        amplitude = 1.5
        omega = 2
        
        def oscillate(t):
            return amplitude * np.cos(omega * t)
        
        def update_mass(mob, dt):
            mob.shift(RIGHT * oscillate(self.time_val) * dt * omega * np.sin(omega * self.time_val))
        
        def update_spring(mob):
            new_spring = self.create_spring(spring_start, mass.get_left())
            mob.become(new_spring)
        
        # 添加时间轴
        time_axis = NumberLine(
            x_range=[0, 4 * PI, PI],
            length=8,
            include_numbers=False
        ).shift(DOWN * 2)
        
        time_label = MathTex("t").next_to(time_axis, RIGHT)
        
        # 位移-时间图
        graph_axes = Axes(
            x_range=[0, 4 * PI, PI],
            y_range=[-2, 2, 1],
            x_length=8,
            y_length=3,
            axis_config={"color": GREY}
        ).shift(DOWN * 2)
        
        sine_curve = graph_axes.plot(
            lambda t: amplitude * np.cos(omega * t),
            x_range=[0, 4 * PI],
            color=YELLOW
        )
        
        self.play(Create(graph_axes), Write(time_label))
        self.play(Create(sine_curve))
        
        # 同步振动和图像
        self.time_val = 0
        mass.add_updater(update_mass)
        spring.add_updater(update_spring)
        
        # 追踪点
        trace_dot = Dot(color=RED)
        trace_dot.add_updater(
            lambda m: m.move_to(graph_axes.c2p(self.time_val, amplitude * np.cos(omega * self.time_val)))
        )
        
        self.add(trace_dot)
        
        # 运行振动
        for _ in range(120):
            self.wait(0.05)
            self.time_val += 0.05
        
        mass.clear_updaters()
        spring.clear_updaters()
        trace_dot.clear_updaters()
        
        self.wait(1)
        self.clear()
        
    def create_spring(self, start, end):
        """创建弹簧"""
        spring_points = []
        n_coils = 10
        width = 0.3
        
        for i in range(n_coils * 4 + 1):
            t = i / (n_coils * 4)
            x = start[0] + t * (end[0] - start[0])
            if i % 4 == 1:
                y = width
            elif i % 4 == 3:
                y = -width
            else:
                y = 0
            spring_points.append([x, y, 0])
        
        return VMobject().set_points_as_corners(spring_points).set_color(GREY)
    
    def electromagnetism(self):
        # 章节标题
        section_title = Text("电磁学", font_size=48, color=YELLOW)
        self.play(Write(section_title))
        self.wait(1)
        self.play(section_title.animate.to_edge(UP).scale(0.7))
        
        # 库仑定律
        self.coulombs_law()
        
        # 麦克斯韦方程组
        self.maxwell_equations()
        
        # 电磁波
        self.electromagnetic_wave()
        
        self.clear()
        
    def coulombs_law(self):
        # 库仑定律公式
        formula = MathTex(r"F = k\frac{q_1 q_2}{r^2}", font_size=60)
        formula.to_edge(UP, buff=1.5)
        self.play(Write(formula))
        
        # 创建两个电荷
        charge1 = Circle(radius=0.5, color=RED, fill_opacity=0.8)
        charge1_label = MathTex("+q_1", color=WHITE).scale(0.7)
        charge1_label.move_to(charge1.get_center())
        q1_group = VGroup(charge1, charge1_label)
        q1_group.shift(LEFT * 3)
        
        charge2 = Circle(radius=0.5, color=BLUE, fill_opacity=0.8)
        charge2_label = MathTex("-q_2", color=WHITE).scale(0.7)
        charge2_label.move_to(charge2.get_center())
        q2_group = VGroup(charge2, charge2_label)
        q2_group.shift(RIGHT * 3)
        
        self.play(FadeIn(q1_group), FadeIn(q2_group))
        
        # 电场线
        field_lines = VGroup()
        n_lines = 8
        for i in range(n_lines):
            angle = i * TAU / n_lines
            start = charge1.get_center() + 0.5 * np.array([np.cos(angle), np.sin(angle), 0])
            
            # 创建曲线路径
            points = []
            for t in np.linspace(0, 1, 20):
                r1 = start - charge1.get_center() + t * 6 * (start - charge1.get_center()) / np.linalg.norm(start - charge1.get_center())
                r2 = charge2.get_center() - (charge1.get_center() + r1)
                if np.linalg.norm(r2) > 0.5:
                    direction = r2 / np.linalg.norm(r2)
                    point = charge1.get_center() + r1
                    points.append(point)
            
            if len(points) > 1:
                line = VMobject().set_points_as_corners(points).set_color(YELLOW)
                field_lines.add(line)
        
        self.play(Create(field_lines), run_time=2)
        
        # 力的箭头
        force_arrow1 = Arrow(
            start=q1_group.get_center(),
            end=q1_group.get_center() + LEFT * 1.5,
            color=GREEN,
            buff=0.5
        )
        force_arrow2 = Arrow(
            start=q2_group.get_center(),
            end=q2_group.get_center() + RIGHT * 1.5,
            color=GREEN,
            buff=0.5
        )
        
        force_label1 = MathTex(r"\vec{F}", color=GREEN).next_to(force_arrow1, UP)
        force_label2 = MathTex(r"\vec{F}", color=GREEN).next_to(force_arrow2, UP)
        
        self.play(
            GrowArrow(force_arrow1), GrowArrow(force_arrow2),
            Write(force_label1), Write(force_label2)
        )
        
        # 演示距离变化对力的影响
        distance_tracker = ValueTracker(6)
        
        def update_q2_position(mob):
            mob.move_to(RIGHT * distance_tracker.get_value() / 2)
        
        def update_force_arrow2(mob):
            new_length = 3 / (distance_tracker.get_value() / 6)**2
            mob.put_start_and_end_on(
                q2_group.get_center() + RIGHT * 0.5,
                q2_group.get_center() + RIGHT * (0.5 + new_length)
            )
        
        q2_group.add_updater(update_q2_position)
        force_arrow2.add_updater(update_force_arrow2)
        force_label2.add_updater(lambda m: m.next_to(force_arrow2, UP))
        
        # 距离标签
        distance_label = always_redraw(
            lambda: MathTex(f"r = {distance_tracker.get_value():.1f}", color=WHITE).shift(DOWN * 2)
        )
        
        self.play(Write(distance_label))
        self.play(distance_tracker.animate.set_value(3), run_time=2)
        self.play(distance_tracker.animate.set_value(8), run_time=2)
        
        q2_group.clear_updaters()
        force_arrow2.clear_updaters()
        force_label2.clear_updaters()
        
        self.wait(1)
        self.play(FadeOut(VGroup(formula, q1_group, q2_group, field_lines, 
                                force_arrow1, force_arrow2, force_label1, force_label2, distance_label)))
    
    def maxwell_equations(self):
        # 麦克斯韦方程组
        title = Text("麦克斯韦方程组", font_size=48, color=YELLOW)
        title.to_edge(UP)
        self.play(Write(title))
        
        # 四个方程
        gauss_law = MathTex(r"\nabla \cdot \vec{E} = \frac{\rho}{\epsilon_0}", font_size=40)
        gauss_mag = MathTex(r"\nabla \cdot \vec{B} = 0", font_size=40)
        faraday = MathTex(r"\nabla \times \vec{E} = -\frac{\partial \vec{B}}{\partial t}", font_size=40)
        ampere = MathTex(r"\nabla \times \vec{B} = \mu_0 \vec{J} + \mu_0 \epsilon_0 \frac{\partial \vec{E}}{\partial t}", font_size=40)
        
        equations = VGroup(gauss_law, gauss_mag, faraday, ampere)
        equations.arrange(DOWN, buff=0.5)
        equations.shift(LEFT * 3)
        
        # 方程名称
        names = VGroup(
            Text("高斯定律", font_size=24, color=BLUE),
            Text("高斯磁定律", font_size=24, color=BLUE),
            Text("法拉第定律", font_size=24, color=BLUE),
            Text("安培-麦克斯韦定律", font_size=24, color=BLUE)
        )
        
        for i, name in enumerate(names):
            name.next_to(equations[i], RIGHT, buff=1)
        
        # 逐个显示
        for eq, name in zip(equations, names):
            self.play(Write(eq), FadeIn(name), run_time=1.5)
            self.wait(0.5)
        
        # 可视化演示
        # 创建3D场景区域
        viz_area = Rectangle(width=5, height=5, color=GREY).shift(RIGHT * 3)
        self.play(Create(viz_area))
        
        # 演示电场的散度（高斯定律）
        self.visualize_divergence(viz_area)
        
        self.wait(1)
        self.play(FadeOut(VGroup(title, equations, names, viz_area)))
    
    def visualize_divergence(self, area):
        # 在区域中心创建一个正电荷
        charge = Dot(color=RED, radius=0.2).move_to(area.get_center())
        charge_label = MathTex("+", color=WHITE).move_to(charge.get_center())
        
        self.play(FadeIn(charge), Write(charge_label))
        
        # 创建向外发散的电场线
        field_lines = VGroup()
        n_lines = 12
        for i in range(n_lines):
            angle = i * TAU / n_lines
            start = charge.get_center() + 0.2 * np.array([np.cos(angle), np.sin(angle), 0])
            end = charge.get_center() + 2 * np.array([np.cos(angle), np.sin(angle), 0])
            
            arrow = Arrow(start, end, color=YELLOW, buff=0)
            field_lines.add(arrow)
        
        self.play(Create(field_lines), run_time=2)
        self.wait(1)
        self.play(FadeOut(VGroup(charge, charge_label, field_lines)))
    
    def electromagnetic_wave(self):
        # 电磁波公式
        formula = MathTex(r"c = \frac{1}{\sqrt{\mu_0 \epsilon_0}}", font_size=60)
        formula.to_edge(UP, buff=1.5)
        self.play(Write(formula))
        
        # 创建坐标轴
        axes = ThreeDAxes(
            x_range=[-1, 10, 1],
            y_range=[-2, 2, 1],
            z_range=[-2, 2, 1],
            x_length=10,
            y_length=4,
            z_length=4
        ).shift(DOWN * 0.5)
        
        # 标签
        x_label = MathTex("x").next_to(axes.x_axis, RIGHT)
        e_label = MathTex(r"\vec{E}", color=BLUE).next_to(axes.y_axis, UP)
        b_label = MathTex(r"\vec{B}", color=RED).next_to(axes.z_axis, OUT)
        
        self.play(Create(axes), Write(x_label), Write(e_label), Write(b_label))
        
        # 创建电场和磁场波形
        t_tracker = ValueTracker(0)
        
        # 电场波（蓝色，在y方向）
        e_wave = always_redraw(lambda: ParametricFunction(
            lambda x: axes.c2p(x, 1.5 * np.sin(2 * PI * (x - t_tracker.get_value())), 0),
            t_range=[0, 10],
            color=BLUE
        ))
        
        # 磁场波（红色，在z方向）
        b_wave = always_redraw(lambda: ParametricFunction(
            lambda x: axes.c2p(x, 0, 1.5 * np.sin(2 * PI * (x - t_tracker.get_value()))),
            t_range=[0, 10],
            color=RED
        ))
        
        # 添加箭头表示场的方向
        e_arrows = always_redraw(lambda: VGroup(*[
            Arrow(
                axes.c2p(x, 0, 0),
                axes.c2p(x, 1.5 * np.sin(2 * PI * (x - t_tracker.get_value())), 0),
                color=BLUE,
                buff=0
            ).set_stroke(width=2)
            for x in np.linspace(0, 10, 20)
        ]))
        
        b_arrows = always_redraw(lambda: VGroup(*[
            Arrow(
                axes.c2p(x, 0, 0),
                axes.c2p(x, 0, 1.5 * np.sin(2 * PI * (x - t_tracker.get_value()))),
                color=RED,
                buff=0
            ).set_stroke(width=2)
            for x in np.linspace(0, 10, 20)
        ]))
        
        self.play(Create(e_wave), Create(b_wave))
        self.play(Create(e_arrows), Create(b_arrows))
        
        # 波的传播动画
        self.play(t_tracker.animate.set_value(3), run_time=6, rate_func=linear)
        
        # 添加说明文字
        explanation = Text("电场和磁场相互垂直，以光速传播", font_size=24, color=WHITE)
        explanation.shift(DOWN * 3)
        self.play(Write(explanation))
        
        self.wait(2)
        self.clear()
    
    def thermodynamics(self):
        # 章节标题
        section_title = Text("热力学", font_size=48, color=YELLOW)
        self.play(Write(section_title))
        self.wait(1)
        self.play(section_title.animate.to_edge(UP).scale(0.7))
        
        # 理想气体定律
        self.ideal_gas_law()
        
        # 热力学第一定律
        self.first_law_thermodynamics()
        
        # 卡诺循环
        self.carnot_cycle()
        
        self.clear()
    
    def ideal_gas_law(self):
        # 理想气体定律公式
        formula = MathTex(r"PV = nRT", font_size=60)
        formula.to_edge(UP, buff=1.5)
        self.play(Write(formula))
        
        # 创建容器
        container = Rectangle(width=4, height=3, color=WHITE)
        container.shift(LEFT * 3)
        
        # 活塞
        piston = Rectangle(width=0.2, height=3, color=GREY, fill_opacity=0.8)
        piston.move_to(container.get_right() + LEFT * 0.1)
        
        # 气体分子
        molecules = VGroup()
        n_molecules = 20
        for _ in range(n_molecules):
            molecule = Dot(
                point=container.get_center() + np.array([
                    np.random.uniform(-1.8, 1.8),
                    np.random.uniform(-1.3, 1.3),
                    0
                ]),
                radius=0.05,
                color=BLUE
            )
            molecules.add(molecule)
        
        self.play(Create(container), FadeIn(piston), FadeIn(molecules))
        
        # 标签
        p_label = MathTex("P", color=RED).next_to(container, UP)
        v_label = MathTex("V", color=GREEN).next_to(container, DOWN)
        t_label = MathTex("T", color=ORANGE).next_to(container, LEFT)
        
        self.play(Write(p_label), Write(v_label), Write(t_label))
        
        # P-V图
        pv_axes = Axes(
            x_range=[0, 5, 1],
            y_range=[0, 5, 1],
            x_length=4,
            y_length=4,
            axis_config={"color": GREY}
        ).shift(RIGHT * 3)
        
        pv_x_label = MathTex("V").next_to(pv_axes.x_axis, RIGHT)
        pv_y_label = MathTex("P").next_to(pv_axes.y_axis, UP)
        
        self.play(Create(pv_axes), Write(pv_x_label), Write(pv_y_label))
        
        # 等温线
        isotherms = VGroup()
        for T in [1, 2, 3]:
            isotherm = pv_axes.plot(
                lambda V: T / V,
                x_range=[0.5, 4.5],
                color=interpolate_color(BLUE, RED, T/3)
            )
            isotherm_label = MathTex(f"T={T}", font_size=20).next_to(
                pv_axes.c2p(4, T/4), RIGHT
            )
            isotherms.add(isotherm, isotherm_label)
        
        self.play(Create(isotherms), run_time=2)
        
        # 动画：压缩气体
        def update_molecules(mols):
            for mol in mols:
                # 随机运动
                mol.shift(np.array([
                    np.random.uniform(-0.05, 0.05),
                    np.random.uniform(-0.05, 0.05),
                    0
                ]))
                # 边界反弹
                if mol.get_x() > piston.get_left()[0] - 0.1:
                    mol.set_x(piston.get_left()[0] - 0.1)
                if mol.get_x() < container.get_left()[0] + 0.1:
                    mol.set_x(container.get_left()[0] + 0.1)
                if abs(mol.get_y()) > 1.3:
                    mol.set_y(np.sign(mol.get_y()) * 1.3)
        
        molecules.add_updater(update_molecules)
        
        # 移动活塞
        self.play(piston.animate.shift(LEFT * 1.5), run_time=3)
        
        molecules.clear_updaters()
        
        self.wait(1)
        self.play(FadeOut(VGroup(formula, container, piston, molecules, 
                                p_label, v_label, t_label, pv_axes, pv_x_label, pv_y_label, isotherms)))
    
    def first_law_thermodynamics(self):
        # 热力学第一定律
        formula = MathTex(r"dU = \delta Q - \delta W", font_size=60)
        formula.to_edge(UP, buff=1.5)
        self.play(Write(formula))
        
        # 系统示意图
        system = Circle(radius=2, color=WHITE)
        system_label = Text("系统", font_size=24).move_to(system.get_center())
        
        self.play(Create(system), Write(system_label))
        
        # 热量流入
        heat_arrow = Arrow(
            start=system.get_top() + UP * 1.5,
            end=system.get_top(),
            color=RED,
            buff=0
        )
        heat_label = MathTex(r"\delta Q", color=RED).next_to(heat_arrow, LEFT)
        
        # 功输出
        work_arrow = Arrow(
            start=system.get_right(),
            end=system.get_right() + RIGHT * 1.5,
            color=BLUE,
            buff=0
        )
        work_label = MathTex(r"\delta W", color=BLUE).next_to(work_arrow, UP)
        
        # 内能变化
        du_label = MathTex(r"dU", color=GREEN, font_size=36).shift(DOWN * 3)
        
        self.play(GrowArrow(heat_arrow), Write(heat_label))
        self.play(GrowArrow(work_arrow), Write(work_label))
        self.play(Write(du_label))
        
        # 能量条形图 - 修复LaTeX错误
        bar_chart = BarChart(
            values=[3, 1, 2],
            bar_names=["热量", "功", "内能"],  # 使用普通文本而非LaTeX
            y_range=[0, 4, 1],
            x_length=6,
            y_length=3,
            bar_colors=[RED, BLUE, GREEN]
        ).shift(DOWN * 0.5 + RIGHT * 3)
        
        # 手动添加数学标签
        bar_labels = VGroup(
            MathTex(r"\delta Q", color=RED).next_to(bar_chart.bars[0], UP),
            MathTex(r"\delta W", color=BLUE).next_to(bar_chart.bars[1], UP),
            MathTex(r"dU", color=GREEN).next_to(bar_chart.bars[2], UP)
        )
        
        self.play(Create(bar_chart))
        self.play(Write(bar_labels))
        
        # 动态演示热量和功的关系
        dq_tracker = ValueTracker(3)
        dw_tracker = ValueTracker(1)
        
        def update_bars(chart):
            new_values = [dq_tracker.get_value(), dw_tracker.get_value(), 
                          dq_tracker.get_value() - dw_tracker.get_value()]
            chart.change_bar_values(new_values)
        
        bar_chart.add_updater(update_bars)
        
        # 更新标签位置
        def update_labels(lbls):
            lbls[0].next_to(bar_chart.bars[0], UP)
            lbls[1].next_to(bar_chart.bars[1], UP)
            lbls[2].next_to(bar_chart.bars[2], UP)
        
        bar_labels.add_updater(update_labels)
        
        self.play(dq_tracker.animate.set_value(4), run_time=1.5)
        self.play(dw_tracker.animate.set_value(2), run_time=1.5)
        self.play(dq_tracker.animate.set_value(2), run_time=1.5)
        
        bar_chart.clear_updaters()
        bar_labels.clear_updaters()
        
        self.wait(1)
        self.play(FadeOut(VGroup(formula, system, system_label, heat_arrow, heat_label, 
                                work_arrow, work_label, du_label, bar_chart, bar_labels)))
    
    def carnot_cycle(self):
        # 卡诺循环公式
        formula = MathTex(r"\eta = 1 - \frac{T_C}{T_H}", font_size=60)
        formula.to_edge(UP, buff=1.5)
        self.play(Write(formula))
        
        # 创建P-V图
        axes = Axes(
            x_range=[0, 6, 1],
            y_range=[0, 6, 1],
            x_length=6,
            y_length=5,
            axis_config={"color": GREY}
        )
        
        x_label = MathTex("V").next_to(axes.x_axis, RIGHT)
        y_label = MathTex("P").next_to(axes.y_axis, UP)
        
        self.play(Create(axes), Write(x_label), Write(y_label))
        
        # 创建卡诺循环的四个过程
        # 1. 等温膨胀 (高温)
        v1, p1 = 1, 5  # 起点
        v2, p2 = 3, 5/3  # 终点
        isothermal_expansion = axes.plot(
            lambda x: p1 * v1 / x,
            x_range=[v1, v2],
            color=RED
        )
        
        # 2. 绝热膨胀
        v3, p3 = 5, 0.6  # 终点
        gamma = 1.4  # 绝热指数
        adiabatic_expansion = axes.plot(
            lambda x: p2 * (v2 ** gamma) / (x ** gamma),
            x_range=[v2, v3],
            color=GREEN
        )
        
        # 3. 等温压缩 (低温)
        v4, p4 = 3, 1  # 终点
        isothermal_compression = axes.plot(
            lambda x: p3 * v3 / x,
            x_range=[v3, v4],
            color=BLUE
        )
        
        # 4. 绝热压缩
        adiabatic_compression = axes.plot(
            lambda x: p4 * (v4 ** gamma) / (x ** gamma),
            x_range=[v4, v1],
            color=YELLOW
        )
        
        # 创建循环路径
        cycle = VGroup(isothermal_expansion, adiabatic_expansion, 
                      isothermal_compression, adiabatic_compression)
        
        # 过程标签
        labels = VGroup(
            MathTex(r"1 \to 2: T_H", color=RED).scale(0.7).next_to(isothermal_expansion, UP),
            MathTex(r"2 \to 3", color=GREEN).scale(0.7).next_to(adiabatic_expansion, RIGHT),
            MathTex(r"3 \to 4: T_C", color=BLUE).scale(0.7).next_to(isothermal_compression, DOWN),
            MathTex(r"4 \to 1", color=YELLOW).scale(0.7).next_to(adiabatic_compression, LEFT)
        )
        
        # 逐步显示过程
        for i, (process, label) in enumerate(zip(cycle, labels)):
            self.play(Create(process), Write(label), run_time=1.5)
        
        # 添加效率计算
        efficiency = MathTex(r"\eta = \frac{W_{net}}{Q_H} = \frac{\text{Area}}{Q_H}", font_size=30)
        efficiency.shift(DOWN * 2.5)
        
        self.play(Write(efficiency))
        
        # 突出显示循环包围的面积(功)
        cycle_area = Polygon(
            *[axes.c2p(v, p) for v, p in [(v1, p1), (v2, p2), (v3, p3), (v4, p4)]],
            color=WHITE, fill_opacity=0.2
        )
        
        self.play(FadeIn(cycle_area))
        
        self.wait(1)
        self.play(FadeOut(VGroup(formula, axes, x_label, y_label, cycle, labels, efficiency, cycle_area)))
    
    def quantum_mechanics(self):
        # 章节标题
        section_title = Text("量子力学", font_size=48, color=YELLOW)
        self.play(Write(section_title))
        self.wait(1)
        self.play(section_title.animate.to_edge(UP).scale(0.7))
        
        # 薛定谔方程
        self.schrodinger_equation()
        
        # 不确定性原理
        self.uncertainty_principle()
        
        # 量子隧道效应
        self.quantum_tunneling()
        
        self.clear()
    
    def schrodinger_equation(self):
        # 薛定谔方程公式
        formula = MathTex(r"i\hbar\frac{\partial}{\partial t}\Psi(\mathbf{r},t) = \hat{H}\Psi(\mathbf{r},t)", font_size=48)
        formula.to_edge(UP, buff=1.5)
        
        # 哈密顿算符
        hamiltonian = MathTex(r"\hat{H} = -\frac{\hbar^2}{2m}\nabla^2 + V(\mathbf{r})", font_size=36)
        hamiltonian.next_to(formula, DOWN)
        
        self.play(Write(formula))
        self.play(Write(hamiltonian))
        
        # 创建坐标轴
        axes = Axes(
            x_range=[-5, 5, 1],
            y_range=[0, 1.5, 0.5],
            x_length=8,
            y_length=3,
            axis_config={"color": GREY}
        ).shift(DOWN * 1.5)
        
        x_label = MathTex("x").next_to(axes.x_axis, RIGHT)
        y_label = MathTex(r"|\Psi|^2").next_to(axes.y_axis, UP)
        
        self.play(Create(axes), Write(x_label), Write(y_label))
        
        # 创建几个量子态波函数
        def psi_ground(x):
            return np.exp(-0.5 * x**2) * (1/np.pi)**0.25
        
        def psi_first(x):
            return np.sqrt(2) * x * psi_ground(x)
        
        def psi_second(x):
            return (1/np.sqrt(2)) * (2*x**2 - 1) * psi_ground(x)
        
        # 波函数的概率密度
        ground_state = axes.plot(
            lambda x: 0.8 * psi_ground(x)**2,
            x_range=[-5, 5],
            color=BLUE
        )
        
        first_excited = axes.plot(
            lambda x: 0.8 * psi_first(x)**2,
            x_range=[-5, 5],
            color=GREEN
        )
        
        second_excited = axes.plot(
            lambda x: 0.8 * psi_second(x)**2,
            x_range=[-5, 5],
            color=RED
        )
        
        # 量子态标签
        state_labels = VGroup(
            MathTex(r"n=0", color=BLUE).scale(0.7).next_to(ground_state, UP).shift(RIGHT * 2),
            MathTex(r"n=1", color=GREEN).scale(0.7).next_to(first_excited, UP).shift(RIGHT * 3),
            MathTex(r"n=2", color=RED).scale(0.7).next_to(second_excited, UP).shift(RIGHT * 4)
        )
        
        # 势能函数
        potential = axes.plot(
            lambda x: 0.1 * x**2,
            x_range=[-5, 5],
            color=YELLOW
        )
        
        potential_label = MathTex(r"V(x)", color=YELLOW).next_to(potential, RIGHT)
        
        self.play(Create(potential), Write(potential_label))
        
        # 展示各能级波函数
        self.play(Create(ground_state), Write(state_labels[0]))
        self.play(Create(first_excited), Write(state_labels[1]))
        self.play(Create(second_excited), Write(state_labels[2]))
        
        # 波函数演化动画
        t_tracker = ValueTracker(0)
        
        evolving_state = always_redraw(lambda: axes.plot(
            lambda x: 0.6 * (psi_ground(x) * np.cos(t_tracker.get_value()) + 
                           0.5j * psi_first(x) * np.sin(t_tracker.get_value()))**2,
            x_range=[-5, 5],
            color=PURPLE
        ))
        
        evolving_label = MathTex(r"\Psi(x,t)", color=PURPLE).next_to(evolving_state, DOWN).shift(RIGHT * 2)
        
        self.play(
            FadeOut(ground_state), FadeOut(first_excited), FadeOut(second_excited),
            FadeOut(state_labels)
        )
        
        self.play(Create(evolving_state), Write(evolving_label))
        
        self.play(t_tracker.animate.set_value(2 * PI), run_time=5, rate_func=linear)
        
        self.wait(1)
        self.play(FadeOut(VGroup(formula, hamiltonian, axes, x_label, y_label, 
                                potential, potential_label, evolving_state, evolving_label)))
    
    def uncertainty_principle(self):
        # 不确定性原理公式
        formula = MathTex(r"\Delta x \cdot \Delta p \geq \frac{\hbar}{2}", font_size=60)
        formula.to_edge(UP, buff=1.5)
        self.play(Write(formula))
        
        # 创建坐标轴
        axes = Axes(
            x_range=[-5, 5, 1],
            y_range=[0, 1, 0.2],
            x_length=8,
            y_length=3,
            axis_config={"color": GREY}
        ).shift(DOWN * 0.5)
        
        x_label = MathTex("x").next_to(axes.x_axis, RIGHT)
        
        self.play(Create(axes), Write(x_label))
        
        # 创建不同宽度的高斯波包
        def gaussian(x, sigma):
            return np.exp(-x**2 / (2 * sigma**2)) / (sigma * np.sqrt(2 * np.pi))
        
        sigma_values = [0.5, 1, 2]
        wave_packets = VGroup()
        labels = VGroup()
        
        for i, sigma in enumerate(sigma_values):
            wave_packet = axes.plot(
                lambda x: gaussian(x, sigma),
                x_range=[-5, 5],
                color=BLUE_E if i==0 else (GREEN_E if i==1 else RED_E)
            )
            
            label = MathTex(f"\sigma_x = {sigma}", color=wave_packet.get_color())
            label.scale(0.7).next_to(wave_packet, UP, buff=0.5).shift(RIGHT * 2)
            
            wave_packets.add(wave_packet)
            labels.add(label)
        
        # 展示不同宽度的波包
        for wave_packet, label in zip(wave_packets, labels):
            self.play(Create(wave_packet), Write(label))
        
        # 创建动量空间轴
        p_axes = Axes(
            x_range=[-5, 5, 1],
            y_range=[0, 1, 0.2],
            x_length=8,
            y_length=3,
            axis_config={"color": GREY}
        ).shift(DOWN * 3)
        
        p_label = MathTex("p").next_to(p_axes.x_axis, RIGHT)
        
        self.play(Create(p_axes), Write(p_label))
        
        # 创建对应的动量空间波包
        p_wave_packets = VGroup()
        p_labels = VGroup()
        
        for i, sigma in enumerate(sigma_values):
            # 动量空间的宽度与位置空间宽度成反比
            p_sigma = 1 / (2 * sigma)
            
            p_wave_packet = p_axes.plot(
                lambda p: gaussian(p, p_sigma),
                x_range=[-5, 5],
                color=BLUE_E if i==0 else (GREEN_E if i==1 else RED_E)
            )
            
            p_label = MathTex(f"\sigma_p = {p_sigma:.2f}", color=p_wave_packet.get_color())
            p_label.scale(0.7).next_to(p_wave_packet, UP, buff=0.5).shift(RIGHT * 2)
            
            p_wave_packets.add(p_wave_packet)
            p_labels.add(p_label)
        
        # 展示对应的动量空间波包
        for p_wave_packet, p_label in zip(p_wave_packets, p_labels):
            self.play(Create(p_wave_packet), Write(p_label))
        
        # 添加说明文字
        explanation = Text("位置越确定，动量越不确定", font_size=24, color=WHITE)
        explanation.shift(DOWN * 4.5)
        self.play(Write(explanation))
        
        self.wait(1)
        self.play(FadeOut(VGroup(formula, axes, x_label, wave_packets, labels,
                                p_axes, p_label, p_wave_packets, p_labels, explanation)))
    
    def quantum_tunneling(self):
        # 隧穿效应公式
        formula = MathTex(r"T \approx e^{-2\kappa a}", font_size=60)
        kappa_def = MathTex(r"\kappa = \frac{\sqrt{2m(V_0-E)}}{\hbar}", font_size=36)
        
        formula.to_edge(UP, buff=1.5)
        kappa_def.next_to(formula, DOWN)
        
        self.play(Write(formula), Write(kappa_def))
        
        # 创建势垒图
        axes = Axes(
            x_range=[-5, 5, 1],
            y_range=[0, 2, 0.5],
            x_length=10,
            y_length=4,
            axis_config={"color": GREY}
        ).shift(DOWN * 1)
        
        x_label = MathTex("x").next_to(axes.x_axis, RIGHT)
        y_label = MathTex("V(x)").next_to(axes.y_axis, UP)
        
        self.play(Create(axes), Write(x_label), Write(y_label))
        
        # 创建势垒
        barrier_height = 1.5
        barrier_width = 2
        barrier_left = -barrier_width/2
        barrier_right = barrier_width/2
        
        barrier = Rectangle(
            width=barrier_width,
            height=barrier_height,
            fill_color=GREY,
            fill_opacity=0.5,
            stroke_color=WHITE
        )
        
        barrier.move_to(axes.c2p((barrier_left + barrier_right)/2, barrier_height/2))
        
        # 创建波函数
        energy_level = 0.8
        energy_line = DashedLine(
            start=axes.c2p(-5, energy_level),
            end=axes.c2p(5, energy_level),
            color=RED
        )
        
        energy_label = MathTex("E", color=RED).next_to(energy_line, LEFT)
        
        # 入射波、穿过势垒的波和透射波
        incident_wave = axes.plot(
            lambda x: 0.3 * np.cos(3 * x) * np.exp(-0.1 * (x + 3)**2) + energy_level,
            x_range=[-5, barrier_left],
            color=BLUE
        )
        
        barrier_wave = axes.plot(
            lambda x: 0.1 * np.exp(-x**2) + energy_level,
            x_range=[barrier_left, barrier_right],
            color=GREEN
        )
        
        transmitted_wave = axes.plot(
            lambda x: 0.1 * np.cos(3 * x) * np.exp(-0.1 * (x - 3)**2) + energy_level,
            x_range=[barrier_right, 5],
            color=BLUE
        )
        
        self.play(FadeIn(barrier), Create(energy_line), Write(energy_label))
        
        # 添加波函数标签
        psi_label = MathTex(r"\Psi(x)", color=BLUE).next_to(incident_wave, UP)
        
        self.play(Create(incident_wave), Write(psi_label))
        self.play(Create(barrier_wave))
        self.play(Create(transmitted_wave))
        
        # 创建波函数动画
        time_tracker = ValueTracker(0)
        
        moving_incident = always_redraw(lambda: axes.plot(
            lambda x: 0.3 * np.cos(3 * x - time_tracker.get_value()) * 
                      np.exp(-0.1 * (x + 3 - 0.5 * time_tracker.get_value())**2) + energy_level,
            x_range=[-5, barrier_left],
            color=BLUE
        ))
        
        moving_transmitted = always_redraw(lambda: axes.plot(
            lambda x: 0.1 * np.cos(3 * x - time_tracker.get_value()) * 
                      np.exp(-0.1 * (x - 3 - 0.5 * time_tracker.get_value())**2) + energy_level,
            x_range=[barrier_right, 5],
            color=BLUE
        ))
        
        self.remove(incident_wave, transmitted_wave)
        self.add(moving_incident, moving_transmitted)
        
        self.play(time_tracker.animate.set_value(5), run_time=5, rate_func=linear)
        
        # 添加说明文字
        explanation = Text("即使能量低于势垒高度，粒子仍有概率穿透势垒", font_size=24, color=WHITE)
        explanation.shift(DOWN * 3)
        self.play(Write(explanation))
        
        self.wait(1)
        self.play(FadeOut(VGroup(formula, kappa_def, axes, x_label, y_label, barrier, 
                                energy_line, energy_label, barrier_wave, psi_label, 
                                moving_incident, moving_transmitted, explanation)))
    
    def relativity(self):
        # 章节标题
        section_title = Text("相对论", font_size=48, color=YELLOW)
        self.play(Write(section_title))
        self.wait(1)
        self.play(section_title.animate.to_edge(UP).scale(0.7))
        
        # 质能方程
        self.mass_energy_equivalence()
        
        # 洛伦兹变换
        self.lorentz_transformation()
        
        # 时空弯曲
        self.spacetime_curvature()
        
        self.clear()
    
    def mass_energy_equivalence(self):
        # 质能方程公式
        formula = MathTex(r"E = mc^2", font_size=72)
        formula.to_edge(UP, buff=1.5)
        self.play(Write(formula))
        
        # 质量与能量转换示意图
        mass = Square(side_length=2, color=BLUE, fill_opacity=0.8)
        mass_label = MathTex("m", font_size=48, color=WHITE)
        mass_label.move_to(mass.get_center())
        mass_group = VGroup(mass, mass_label)
        mass_group.shift(LEFT * 3)
        
        energy = Star(outer_radius=2, inner_radius=1, color=YELLOW, fill_opacity=0.8)
        energy_label = MathTex("E", font_size=48, color=WHITE)
        energy_label.move_to(energy.get_center())
        energy_group = VGroup(energy, energy_label)
        energy_group.shift(RIGHT * 3)
        
        # 转换箭头
        arrow1 = Arrow(mass_group.get_right(), energy_group.get_left(), color=WHITE)
        arrow2 = Arrow(energy_group.get_left(), mass_group.get_right(), color=WHITE)
        
        arrow1_label = MathTex("c^2", font_size=36, color=WHITE).next_to(arrow1, UP)
        arrow2_label = MathTex("c^{-2}", font_size=36, color=WHITE).next_to(arrow2, DOWN)
        
        self.play(FadeIn(mass_group), FadeIn(energy_group))
        self.play(GrowArrow(arrow1), Write(arrow1_label))
        self.play(GrowArrow(arrow2), Write(arrow2_label))
        
        # 核反应能量示例
        nuclear_reaction = MathTex(
            r"m_{before} - m_{after} = \frac{E_{released}}{c^2}",
            font_size=36
        )
        nuclear_reaction.shift(DOWN * 2.5)
        
        self.play(Write(nuclear_reaction))
        
        self.wait(1)
        self.play(FadeOut(VGroup(formula, mass_group, energy_group, arrow1, arrow2, 
                                arrow1_label, arrow2_label, nuclear_reaction)))
    
    def lorentz_transformation(self):
        # 洛伦兹变换公式
        formula = MathTex(r"x' = \gamma(x - vt)", font_size=48)
        formula2 = MathTex(r"t' = \gamma(t - \frac{vx}{c^2})", font_size=48)
        gamma_def = MathTex(r"\gamma = \frac{1}{\sqrt{1 - \frac{v^2}{c^2}}}", font_size=36)
        
        formula_group = VGroup(formula, formula2, gamma_def).arrange(DOWN)
        formula_group.to_edge(UP, buff=1)
        
        self.play(Write(formula_group))
        
        # 创建参考系
        frame_S = Rectangle(width=6, height=4, color=BLUE)
        frame_S_label = MathTex("S", color=BLUE).next_to(frame_S, UP)
        frame_S_group = VGroup(frame_S, frame_S_label)
        frame_S_group.shift(LEFT * 3)
        
        frame_S_prime = Rectangle(width=6, height=4, color=RED)
        frame_S_prime_label = MathTex("S'", color=RED).next_to(frame_S_prime, UP)
        frame_S_prime_group = VGroup(frame_S_prime, frame_S_prime_label)
        frame_S_prime_group.shift(RIGHT * 0.5)
        
        # 创建坐标轴
        S_axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[-2, 2, 1],
            x_length=6,
            y_length=4,
            axis_config={"color": BLUE}
        )
        S_axes.move_to(frame_S.get_center())
        
        S_prime_axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[-2, 2, 1],
            x_length=6,
            y_length=4,
            axis_config={"color": RED}
        )
        S_prime_axes.move_to(frame_S_prime.get_center())
        
        self.play(Create(frame_S_group), Create(S_axes))
        self.play(Create(frame_S_prime_group), Create(S_prime_axes))
        
        # 相对运动动画
        self.play(frame_S_prime_group.animate.shift(RIGHT * 3), run_time=2)
        
        # 时间膨胀示例
        clock_S = Circle(radius=0.5, color=BLUE)
        clock_S_center = Dot(color=BLUE)
        clock_S_hand = Line(start=ORIGIN, end=UP * 0.4, color=BLUE)
        clock_S_group = VGroup(clock_S, clock_S_center, clock_S_hand)
        clock_S_group.move_to(frame_S.get_center())
        
        clock_S_prime = Circle(radius=0.5, color=RED)
        clock_S_prime_center = Dot(color=RED)
        clock_S_prime_hand = Line(start=ORIGIN, end=UP * 0.4, color=RED)
        clock_S_prime_group = VGroup(clock_S_prime, clock_S_prime_center, clock_S_prime_hand)
        clock_S_prime_group.move_to(frame_S_prime.get_center())
        
        self.play(Create(clock_S_group), Create(clock_S_prime_group))
        
        # 钟表转动
        self.play(
            Rotate(clock_S_hand, angle=2*PI, about_point=clock_S_center.get_center()),
            Rotate(clock_S_prime_hand, angle=PI, about_point=clock_S_prime_center.get_center()),
            run_time=2
        )
        
        # 添加说明文字
        explanation = Text("运动参考系中的时间流逝较慢", font_size=24, color=WHITE)
        explanation.shift(DOWN * 3)
        self.play(Write(explanation))
        
        self.wait(1)
        self.play(FadeOut(VGroup(formula_group, frame_S_group, frame_S_prime_group, 
                                S_axes, S_prime_axes, clock_S_group, 
                                clock_S_prime_group, explanation)))
    
    def spacetime_curvature(self):
        # 爱因斯坦场方程
        formula = MathTex(r"G_{\mu\nu} = \frac{8\pi G}{c^4}T_{\mu\nu}", font_size=60)
        formula.to_edge(UP, buff=1.5)
        self.play(Write(formula))
        
        # 创建网格表示空间
        grid = NumberPlane(
            x_range=[-5, 5, 1],
            y_range=[-5, 5, 1],
            x_length=10,
            y_length=8,
            background_line_style={
                "stroke_color": BLUE_E,
                "stroke_width": 1,
                "stroke_opacity": 0.5
            }
        )
        
        self.play(Create(grid))
        
        # 创建质量
        mass = Circle(radius=1, color=YELLOW, fill_opacity=0.8)
        mass.move_to(grid.c2p(0, 0))
        
        self.play(FadeIn(mass))
        
        # 扭曲空间网格
        def deform_func(point):
            x, y, z = point
            # 距离质量中心的距离
            dist = np.sqrt(x**2 + y**2)
            # 扭曲系数 (避免除以零)
            factor = 1 + 1 / (dist + 0.5)
            # 向中心扭曲
            direction = np.array([x, y, 0]) / (dist + 1e-8)
            return point - 0.3 * direction * (1/factor)
        
        deformed_grid = grid.copy()
        deformed_grid.apply_function(deform_func)
        
        self.play(Transform(grid, deformed_grid), run_time=3)
        
        # 添加说明文字
        explanation = Text("质量使空间时间弯曲，引力即为时空弯曲的表现", font_size=24, color=WHITE)
        explanation.shift(DOWN * 3.5)
        self.play(Write(explanation))
        
        # 光线弯曲演示
        light_ray = Line(
            start=grid.c2p(-5, 1.5),
            end=grid.c2p(5, 1.5),
            color=WHITE
        )
        
        def bend_light(point):
            x, y, z = point
            dist = np.sqrt(x**2 + (y - 0)**2)
            if dist < 3:
                deflection = 0.5 * (3 - dist) / 3
                return np.array([x, y - deflection, z])
            return point
        
        bent_light = light_ray.copy()
        bent_light.set_color(YELLOW)
        bent_light.apply_function(bend_light)
        
        self.play(Create(light_ray))
        self.play(Transform(light_ray, bent_light), run_time=2)
        
        self.wait(1)
        self.play(FadeOut(VGroup(formula, grid, mass, explanation, light_ray)))
    
    def ending(self):
        # 结尾
        final_title = Text("物理学核心公式", font_size=72, color=BLUE)
        subtitle = Text("数形结合的动态演示", font_size=36, color=WHITE)
        subtitle.next_to(final_title, DOWN)
        
        self.play(Write(final_title), run_time=2)
        self.play(FadeIn(subtitle), run_time=1)
        
        # 列出所有覆盖的物理学分支
        branches = VGroup(
            Text("经典力学", font_size=30, color=YELLOW),
            Text("电磁学", font_size=30, color=YELLOW),
            Text("热力学", font_size=30, color=YELLOW),
            Text("量子力学", font_size=30, color=YELLOW),
            Text("相对论", font_size=30, color=YELLOW)
        ).arrange(DOWN, buff=0.4)
        
        branches.next_to(subtitle, DOWN, buff=1)
        
        self.play(Write(branches), run_time=3)
        
        # 结束文字
        conclusion = Text("探索物理学之美", font_size=48, color=GOLD)
        conclusion.next_to(branches, DOWN, buff=1)
        
        self.play(Write(conclusion), run_time=2)
        self.wait(2)
        self.play(FadeOut(VGroup(final_title, subtitle, branches, conclusion)))