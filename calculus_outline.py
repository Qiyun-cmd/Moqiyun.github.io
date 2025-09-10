import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from my_manim_setup import *
import random
import itertools
from manim import *
import numpy as np

config.background_color = "#111111"

class MathematicalDepthJourney(Scene):
    def construct(self):
        # 设置高质量渲染参数
        config.frame_height = 8
        config.frame_width = 14
        config.pixel_height = 1440
        config.pixel_width = 2560
        
        # 精致开场序列
        self.cinematic_intro()
        
        # 第一章：黄金分割与自然界的数学
        self.golden_ratio_and_nature()
        
        # 第二章：拓扑变换与莫比乌斯变换
        self.topology_and_mobius()
        
        # 第三章：复分析与黎曼曲面
        self.complex_analysis()
        
        # 第四章：微分几何与曲率
        self.differential_geometry()
        
        # 第五章：分形维度与混沌
        self.fractals_and_chaos()
        
        # 第六章：傅里叶变换与信号处理
        self.fourier_transform()
        
        # 结束：高维空间投影与数学之美
        self.hyperdimensions_finale()
    
    def cinematic_intro(self):
        # 创建开场粒子系统
        particles = VGroup(*[
            Dot(radius=0.03, color=interpolate_color(BLUE_A, PURPLE_A, random.random()))
            for _ in range(300)
        ])
        
        for particle in particles:
            particle.move_to([
                random.uniform(-7, 7),
                random.uniform(-4, 4),
                0
            ])
        
        # 粒子系统动画
        self.play(FadeIn(particles, lag_ratio=0.01, run_time=2))
        
        # 粒子形成数学符号
        target_points = self.get_mathematical_symbol_points()
        anims = []
        for i, particle in enumerate(particles[:len(target_points)]):
            anims.append(particle.animate.move_to(target_points[i]))
        
        self.play(LaggedStart(*anims, lag_ratio=0.005, run_time=3))
        self.wait(0.5)
        
        # 标题渐入
        title = Text("数学之美的深度探索", font="Source Han Sans CN").scale(1.5)
        subtitle = Text("从几何到混沌的视觉之旅", font="Source Han Sans CN").scale(0.7)
        subtitle.next_to(title, DOWN, buff=0.7)
        
        self.play(
            Write(title, run_time=1.5),
            particles.animate.set_opacity(0.3),
        )
        self.play(FadeIn(subtitle, run_time=1))
        self.wait(1)
        
        # 优雅淡出
        self.play(
            FadeOut(title),
            FadeOut(subtitle),
            FadeOut(particles, lag_ratio=0.01)
        )
    
    def get_mathematical_symbol_points(self):
        # 创建数学符号的点集合（如希腊字母π、无穷、积分符号等组合的艺术排列）
        math_symbol = MathTex(r"\pi", r"\infty", r"\int", r"\sum", r"\partial", r"\nabla")
        math_symbol.scale(4).arrange(RIGHT, buff=1.2)
        return [math_symbol.get_center() + np.array([random.uniform(-0.1, 0.1), random.uniform(-0.1, 0.1), 0]) 
                for _ in range(200)]
    
    def golden_ratio_and_nature(self):
        section_title = Text("黄金分割与自然界的数学", font="Source Han Sans CN").scale(1.2).to_edge(UP)
        section_title.set_color_by_gradient(GOLD_A, GOLD_E)
        
        self.play(Write(section_title))
        self.wait(0.5)
        
        # 创建黄金矩形
        golden_ratio = (1 + np.sqrt(5)) / 2
        
        # 1. 黄金矩形级联
        rectangle = Rectangle(
            width=4 * golden_ratio,
            height=4,
            fill_color=GOLD_E,
            fill_opacity=0.3,
            stroke_color=GOLD_A,
            stroke_width=2
        )
        
        formula = MathTex(r"\varphi = \frac{1 + \sqrt{5}}{2} \approx 1.618").scale(0.8)
        formula.next_to(rectangle, DOWN, buff=0.5)
        
        self.play(Create(rectangle), Write(formula))
        self.wait(0.5)
        
        # 递归生成黄金矩形
        rectangles = VGroup(rectangle)
        squares = VGroup()
        
        # 创建5个递归黄金矩形
        for i in range(5):
            prev_rect = rectangles[-1]
            width, height = prev_rect.width, prev_rect.height
            
            # 新矩形的尺寸
            if width > height:
                new_width = height
                new_height = height
                new_x = prev_rect.get_center()[0] - (width - new_width) / 2
                new_y = prev_rect.get_center()[1]
            else:
                new_width = width
                new_height = width
                new_x = prev_rect.get_center()[0]
                new_y = prev_rect.get_center()[1] - (height - new_height) / 2
            
            # 创建新正方形
            square = Rectangle(
                width=new_width,
                height=new_height,
                fill_color=GOLD_E,
                fill_opacity=0.5 - i * 0.08,
                stroke_color=GOLD_A,
                stroke_width=2
            )
            square.move_to([new_x, new_y, 0])
            squares.add(square)
            
            # 创建剩余矩形
            if width > height:
                remaining_width = width - new_width
                remaining_height = height
                remaining_x = prev_rect.get_center()[0] + (width - remaining_width) / 2
                remaining_y = prev_rect.get_center()[1]
            else:
                remaining_width = width
                remaining_height = height - new_height
                remaining_x = prev_rect.get_center()[0]
                remaining_y = prev_rect.get_center()[1] + (height - remaining_height) / 2
            
            new_rect = Rectangle(
                width=remaining_width,
                height=remaining_height,
                fill_color=GOLD_E,
                fill_opacity=0.3 - i * 0.05,
                stroke_color=GOLD_A,
                stroke_width=2
            )
            new_rect.move_to([remaining_x, remaining_y, 0])
            rectangles.add(new_rect)
        
        # 依次显示正方形
        for square in squares:
            self.play(FadeIn(square), run_time=0.5)
        
        # 2. 黄金螺旋
        spiral = VMobject(stroke_color=WHITE, stroke_width=3)
        spiral_points = []
        
        # 黄金螺旋参数方程
        t_values = np.linspace(0, 2 * np.pi * 2, 200)
        a = 0.1  # 螺旋增长系数
        
        for t in t_values:
            r = a * np.exp(t / golden_ratio)
            x = r * np.cos(t)
            y = r * np.sin(t)
            spiral_points.append([x, y, 0])
        
        spiral.set_points_as_corners(spiral_points)
        
        # 螺旋和矩形一起缩放适应
        spiral_group = VGroup(spiral)
        spiral_group.scale(1.8).move_to(rectangle)
        
        self.play(Create(spiral), run_time=2)
        self.wait(0.5)
        
        # 3. 自然界中的斐波那契序列动画
        fib_formula = MathTex(r"F_n = F_{n-1} + F_{n-2}").scale(0.8)
        fib_formula.next_to(formula, DOWN, buff=0.5)
        
        self.play(Write(fib_formula))
        
        # 创建树叶排列模拟
        leaves = VGroup()
        angle = 0
        for i in range(50):
            leaf = Dot(radius=0.02, color=GREEN_A)
            # 使用黄金角度 (约137.5°) 旋转
            r = 0.1 * np.sqrt(i)
            angle += 137.5 * DEGREES
            x = r * np.cos(angle)
            y = r * np.sin(angle)
            leaf.move_to([x, y, 0])
            leaves.add(leaf)
        
        leaves.scale(5).to_edge(RIGHT, buff=1)
        
        self.play(FadeIn(leaves, lag_ratio=0.01))
        self.wait(1)
        
        # 向下一部分过渡
        self.play(
            FadeOut(rectangle),
            FadeOut(squares),
            FadeOut(spiral),
            FadeOut(formula),
            FadeOut(fib_formula),
            FadeOut(leaves),
            FadeOut(section_title)
        )
    
    def topology_and_mobius(self):
        section_title = Text("拓扑变换与莫比乌斯变换", font="Source Han Sans CN").scale(1.2).to_edge(UP)
        section_title.set_color_by_gradient(BLUE_A, TEAL_A)
        
        self.play(Write(section_title))
        
        # 1. 创建莫比乌斯带模型
        # 使用参数化曲面
        def mobius_strip_param(u, v):
            # u: 圆周参数 [0, 2pi]
            # v: 宽度参数 [-1, 1]
            r = 2  # 主半径
            w = 0.8  # 带宽
            
            # 莫比乌斯带参数方程
            x = (r + v/2 * np.cos(u/2)) * np.cos(u)
            y = (r + v/2 * np.cos(u/2)) * np.sin(u)
            z = v/2 * np.sin(u/2)
            return np.array([x, y, z])
        
        # 创建网格点
        u_range = np.linspace(0, 2 * np.pi, 50)
        v_range = np.linspace(-1, 1, 10)
        
        # 创建表面
        mobius_surface = VGroup()
        
        # 添加u方向的线
        for v_val in v_range:
            points = []
            for u_val in u_range:
                points.append(mobius_strip_param(u_val, v_val))
            
            line = VMobject()
            line.set_points_as_corners(points)
            line.set_stroke(BLUE_B, width=1.5, opacity=0.7)
            mobius_surface.add(line)
        
        # 添加v方向的线
        for i, u_val in enumerate(u_range):
            if i % 5 == 0:  # 减少线的数量以避免过度拥挤
                points = []
                for v_val in v_range:
                    points.append(mobius_strip_param(u_val, v_val))
                
                line = VMobject()
                line.set_points_as_corners(points)
                line.set_stroke(BLUE_D, width=1.5, opacity=0.7)
                mobius_surface.add(line)
        
        # 让莫比乌斯带居中且旋转为最佳视角
        mobius_surface.scale(0.8).shift(LEFT * 3)
        
        # 添加照明效果
        ambient_light = AmbientLight(color=BLUE_A, opacity=0.3)
        ambient_light.move_to(mobius_surface)
        
        # 显示莫比乌斯带
        self.play(FadeIn(ambient_light, run_time=1))
        self.play(Create(mobius_surface, run_time=3))
        
        # 2. 莫比乌斯带上的旅行者
        traveler = Dot(color=YELLOW, radius=0.1)
        
        # 定义运动轨迹
        def get_traveler_position(t):
            u = t * 2 * np.pi  # 围绕一圈
            v = np.sin(t * 4 * np.pi) * 0.8  # 在宽度方向上摆动
            return mobius_strip_param(u, v)
        
        # 动画显示运动
        traveler_path = []
        traveler_trace = VMobject(stroke_color=YELLOW_A, stroke_width=3)
        
        # 初始位置
        initial_pos = get_traveler_position(0)
        traveler.move_to(initial_pos)
        self.play(FadeIn(traveler))
        
        # 运动动画
        n_steps = 120
        for i in range(n_steps + 1):
            t = i / n_steps
            new_pos = get_traveler_position(t)
            traveler_path.append(new_pos)
            
            if i % 5 == 0:  # 每5步更新一次轨迹以提高性能
                traveler_trace.set_points_as_corners(traveler_path)
                self.play(
                    traveler.animate.move_to(new_pos),
                    UpdateFromFunc(traveler_trace, lambda m: m.set_points_as_corners(traveler_path)),
                    run_time=0.1,
                    rate_func=linear
                )
        
        self.wait(0.5)
        
        # 3. 复平面上的莫比乌斯变换
        complex_title = Text("复平面上的莫比乌斯变换", font="Source Han Sans CN").scale(0.8)
        complex_title.next_to(section_title, DOWN, buff=0.7).to_edge(RIGHT, buff=2)
        
        mobius_formula = MathTex(r"f(z) = \frac{az + b}{cz + d}").scale(0.8)
        mobius_formula.next_to(complex_title, DOWN, buff=0.5)
        
        self.play(Write(complex_title), Write(mobius_formula))
        
        # 创建复平面
        complex_plane = ComplexPlane(
            x_range=[-2, 2, 0.5],
            y_range=[-2, 2, 0.5],
            background_line_style={
                "stroke_opacity": 0.6,
                "stroke_width": 1,
            }
        ).scale(0.8)
        
        complex_plane.next_to(mobius_formula, DOWN, buff=0.7)
        
        # 添加坐标轴标签
        x_label = MathTex("Re(z)").next_to(complex_plane.x_axis, RIGHT)
        y_label = MathTex("Im(z)").next_to(complex_plane.y_axis, UP)
        labels = VGroup(x_label, y_label)
        
        self.play(Create(complex_plane), Write(labels))
        
        # 网格变换动画
        # 定义莫比乌斯变换 f(z) = (z-i)/(z+i)
        def mobius_transform(z, t):
            a = complex(np.cos(t * np.pi), np.sin(t * np.pi))
            b = complex(0, 0)
            c = complex(0, np.sin(t * np.pi))
            d = complex(1, 0)
            
            return (a * z + b) / (c * z + d)
        
        # 创建原始网格点
        grid_dots = VGroup()
        grid_lines_h = VGroup()
        grid_lines_v = VGroup()
        
        # 创建水平和垂直网格线
        for x in np.linspace(-1.5, 1.5, 7):
            h_points = []
            for y in np.linspace(-1.5, 1.5, 30):
                z = complex(x, y)
                point = complex_plane.n2p(z)
                h_points.append(point)
            
            h_line = VMobject(stroke_width=1, stroke_opacity=0.7, stroke_color=BLUE_B)
            h_line.set_points_as_corners(h_points)
            grid_lines_h.add(h_line)
        
        for y in np.linspace(-1.5, 1.5, 7):
            v_points = []
            for x in np.linspace(-1.5, 1.5, 30):
                z = complex(x, y)
                point = complex_plane.n2p(z)
                v_points.append(point)
            
            v_line = VMobject(stroke_width=1, stroke_opacity=0.7, stroke_color=BLUE_B)
            v_line.set_points_as_corners(v_points)
            grid_lines_v.add(v_line)
        
        # 显示原始网格
        self.play(
            Create(grid_lines_h),
            Create(grid_lines_v),
            run_time=1.5
        )
        
        # 莫比乌斯变换动画
        def update_grid(t):
            new_h_lines = VGroup()
            new_v_lines = VGroup()
            
            for h_line in grid_lines_h:
                new_points = []
                for point in h_line.get_points():
                    z = complex_plane.p2n(point)
                    new_z = mobius_transform(z, t)
                    new_point = complex_plane.n2p(new_z)
                    new_points.append(new_point)
                
                new_h_line = VMobject(stroke_width=1, stroke_opacity=0.7, stroke_color=BLUE_B)
                new_h_line.set_points_as_corners(new_points)
                new_h_lines.add(new_h_line)
            
            for v_line in grid_lines_v:
                new_points = []
                for point in v_line.get_points():
                    z = complex_plane.p2n(point)
                    new_z = mobius_transform(z, t)
                    new_point = complex_plane.n2p(new_z)
                    new_points.append(new_point)
                
                new_v_line = VMobject(stroke_width=1, stroke_opacity=0.7, stroke_color=BLUE_B)
                new_v_line.set_points_as_corners(new_points)
                new_v_lines.add(new_v_line)
            
            return new_h_lines, new_v_lines
        
        # 执行变换
        t_values = np.linspace(0, 1, 20)
        for i, t in enumerate(t_values):
            new_h_lines, new_v_lines = update_grid(t)
            
            if i == 0:
                continue  # 跳过第一帧，因为它与原始网格相同
            
            self.play(
                Transform(grid_lines_h, new_h_lines),
                Transform(grid_lines_v, new_v_lines),
                run_time=0.2,
                rate_func=linear
            )
        
        self.wait(1)
        
        # 过渡到下一部分
        self.play(
            FadeOut(mobius_surface),
            FadeOut(traveler),
            FadeOut(traveler_trace),
            FadeOut(ambient_light),
            FadeOut(complex_title),
            FadeOut(mobius_formula),
            FadeOut(complex_plane),
            FadeOut(labels),
            FadeOut(grid_lines_h),
            FadeOut(grid_lines_v),
            FadeOut(section_title)
        )
    
    def complex_analysis(self):
        section_title = Text("复分析与黎曼曲面", font="Source Han Sans CN").scale(1.2).to_edge(UP)
        section_title.set_color_by_gradient(PURPLE_A, PURPLE_E)
        
        self.play(Write(section_title))
        
        # 1. 复变函数可视化
        complex_function_title = Text("复变函数 f(z) = z²", font="Source Han Sans CN").scale(0.7)
        complex_function_title.next_to(section_title, DOWN, buff=0.5)
        
        self.play(Write(complex_function_title))
        
        # 创建域和值域复平面
        domain_plane = ComplexPlane(
            x_range=[-2, 2, 1],
            y_range=[-2, 2, 1],
            background_line_style={
                "stroke_opacity": 0.5,
                "stroke_width": 1,
            }
        ).scale(0.5).to_edge(LEFT, buff=1)
        
        range_plane = ComplexPlane(
            x_range=[-4, 4, 1],
            y_range=[-4, 4, 1],
            background_line_style={
                "stroke_opacity": 0.5,
                "stroke_width": 1,
            }
        ).scale(0.5).to_edge(RIGHT, buff=1)
        
        # 标签
        domain_label = Text("z-平面", font="Source Han Sans CN").scale(0.6).next_to(domain_plane, DOWN)
        range_label = Text("f(z)-平面", font="Source Han Sans CN").scale(0.6).next_to(range_plane, DOWN)
        
        self.play(
            Create(domain_plane),
            Create(range_plane),
            Write(domain_label),
            Write(range_label)
        )
        
        # 创建域中的网格点和映射点
        def complex_function(z):
            return z**2
        
        grid_dots = VGroup()
        mapped_dots = VGroup()
        
        # 创建动态映射线
        mapping_lines = VGroup()
        
        # 创建颜色编码的点和线
        for x in np.linspace(-1.5, 1.5, 10):
            for y in np.linspace(-1.5, 1.5, 10):
                z = complex(x, y)
                w = complex_function(z)
                
                # 计算色调
                hue = (np.angle(z) % (2 * np.pi)) / (2 * np.pi)
                color = color_gradient([RED, YELLOW, GREEN, BLUE, PURPLE], hue)
                
                # 在域和值域中创建点
                dot_z = Dot(domain_plane.n2p(z), color=color, radius=0.05)
                dot_w = Dot(range_plane.n2p(w), color=color, radius=0.05)
                
                grid_dots.add(dot_z)
                mapped_dots.add(dot_w)
                
                # 创建映射线
                line = Line(
                    dot_z.get_center(), 
                    dot_w.get_center(),
                    stroke_width=1,
                    stroke_opacity=0.3,
                    stroke_color=color
                )
                mapping_lines.add(line)
        
        # 显示域中的点
        self.play(FadeIn(grid_dots, lag_ratio=0.05))
        
        # 显示映射过程
        self.play(
            LaggedStart(*[
                FadeIn(line) for line in mapping_lines
            ], lag_ratio=0.01),
            run_time=2
        )
        
        self.play(FadeIn(mapped_dots, lag_ratio=0.05))
        self.wait(0.5)
        
        # 2. 黎曼曲面可视化
        riemann_title = Text("黎曼曲面（多值函数 f(z) = √z）", font="Source Han Sans CN").scale(0.7)
        riemann_title.next_to(complex_function_title, DOWN, buff=1.5)
        
        self.play(Write(riemann_title))
        
        # 为简化，我们创建一个简化的双叶黎曼曲面模型
        def riemann_surface(u, v, sheet=0):
            # 参数化为极坐标 u=r, v=theta
            r = u
            theta = v + sheet * np.pi  # 不同的片
            
            z = r * np.exp(1j * theta)
            w = np.sqrt(abs(z)) * np.exp(1j * theta / 2)
            
            # 将复数w转换为3D点
            x = r * np.cos(theta)
            y = r * np.sin(theta)
            z_height = abs(w) * np.cos(np.angle(w) / 2)
            
            return np.array([x, y, z_height])
        
        # 创建两个黎曼曲面片
        sheet1_points = []
        sheet2_points = []
        
        r_values = np.linspace(0.1, 1.5, 20)
        theta_values = np.linspace(0, 2*np.pi, 40)
        
        # 生成第一片的网格
        for r in r_values:
            theta_line = []
            for theta in theta_values:
                point = riemann_surface(r, theta, sheet=0)
                theta_line.append(point)
            sheet1_points.append(theta_line)
        
        # 生成第二片的网格
        for r in r_values:
            theta_line = []
            for theta in theta_values:
                point = riemann_surface(r, theta, sheet=1)
                theta_line.append(point)
            sheet2_points.append(theta_line)
        
        # 创建曲面
        riemann_sheets = VGroup()
        
        # 第一片
        for i in range(len(r_values)):
            for j in range(len(theta_values)):
                if i < len(r_values) - 1 and j < len(theta_values) - 1:
                    quad = Polygon(
                        sheet1_points[i][j],
                        sheet1_points[i][j+1],
                        sheet1_points[i+1][j+1],
                        sheet1_points[i+1][j],
                        fill_color=BLUE_E,
                        fill_opacity=0.7,
                        stroke_width=0.5,
                        stroke_color=BLUE_B
                    )
                    riemann_sheets.add(quad)
        
        # 第二片
        for i in range(len(r_values)):
            for j in range(len(theta_values)):
                if i < len(r_values) - 1 and j < len(theta_values) - 1:
                    quad = Polygon(
                        sheet2_points[i][j],
                        sheet2_points[i][j+1],
                        sheet2_points[i+1][j+1],
                        sheet2_points[i+1][j],
                        fill_color=RED_E,
                        fill_opacity=0.7,
                        stroke_width=0.5,
                        stroke_color=RED_B
                    )
                    riemann_sheets.add(quad)
        
        # 缩放和定位
        riemann_sheets.scale(1.2).move_to(ORIGIN)
        
        self.play(FadeIn(riemann_sheets))
        
        # 添加旋转动画
        self.play(
            Rotate(riemann_sheets, angle=2*PI, axis=UP, run_time=5),
        )
        
        self.wait(1)
        
        # 过渡到下一部分
        self.play(
            FadeOut(domain_plane),
            FadeOut(range_plane),
            FadeOut(domain_label),
            FadeOut(range_label),
            FadeOut(grid_dots),
            FadeOut(mapped_dots),
            FadeOut(mapping_lines),
            FadeOut(complex_function_title),
            FadeOut(riemann_title),
            FadeOut(riemann_sheets),
            FadeOut(section_title)
        )
    
    def differential_geometry(self):
        section_title = Text("微分几何与曲率", font="Source Han Sans CN").scale(1.2).to_edge(UP)
        section_title.set_color_by_gradient(GREEN_A, BLUE_C)
        
        self.play(Write(section_title))
        
        # 1. 曲面与曲率可视化
        # 创建一个曲面参数方程 - 选择鞍面作为示例
        def saddle_surface(u, v):
            x = u
            y = v
            z = u**2 - v**2
            return np.array([x, y, z])
        
        # 创建曲面
        u_range = np.linspace(-1, 1, 20)
        v_range = np.linspace(-1, 1, 20)
        
        saddle = VGroup()
        
        # 创建曲面网格
        for u in u_range:
            v_line = []
            for v in v_range:
                v_line.append(saddle_surface(u, v))
            
            line = VMobject()
            line.set_points_as_corners(v_line)
            line.set_stroke(GREEN_B, width=1.5, opacity=0.8)
            saddle.add(line)
        
        for v in v_range:
            u_line = []
            for u in u_range:
                u_line.append(saddle_surface(u, v))
            
            line = VMobject()
            line.set_points_as_corners(u_line)
            line.set_stroke(GREEN_D, width=1.5, opacity=0.8)
            saddle.add(line)
        
        # 缩放和定位
        saddle.scale(1.5).to_edge(LEFT, buff=1)
        
        # 创建曲面标题
        saddle_title = Text("鞍面: z = x² - y²", font="Source Han Sans CN").scale(0.7)
        saddle_title.next_to(section_title, DOWN, buff=0.5)
        
        self.play(Write(saddle_title))
        self.play(Create(saddle, run_time=2))
        
        # 2. 显示曲率方程
        curvature_title = Text("高斯曲率", font="Source Han Sans CN").scale(0.7)
        curvature_title.next_to(saddle_title, DOWN, buff=0.8)
        
        gauss_curvature = MathTex(r"K = \frac{LN - M^2}{EG - F^2}").scale(0.8)
        gauss_curvature.next_to(curvature_title, DOWN, buff=0.5)
        
        self.play(Write(curvature_title), Write(gauss_curvature))
        
        # 3. 创建曲率可视化
        # 为鞍面计算高斯曲率
        def gauss_curvature_saddle(u, v):
            # 对于z = x^2 - y^2，高斯曲率为常数 K = -4/(1+(2x)^2+(2y)^2)^2
            x, y = u, v
            return -4 / ((1 + 4*x**2 + 4*y**2)**2)
        
        # 创建曲率可视化
        curvature_surface = VGroup()
        
        for u in u_range:
            v_line = []
            for v in v_range:
                point = saddle_surface(u, v)
                # 计算该点的曲率
                k = gauss_curvature_saddle(u, v)
                
                # 根据曲率映射颜色
                # 负曲率 -> 蓝色，零曲率 -> 白色，正曲率 -> 红色
                if k < 0:
                    color = interpolate_color(BLUE_E, WHITE, min(1, abs(k) / 4))
                else:
                    color = interpolate_color(WHITE, RED_E, min(1, k / 4))
                
                # 创建点
                dot = Dot(point, color=color, radius=0.05)
                curvature_surface.add(dot)
        
        # 定位
        curvature_surface.scale(1.5).to_edge(RIGHT, buff=1)
        
        # 曲率图例
        curvature_scale = VGroup()
        
        # 创建颜色条
        n_colors = 10
        for i in range(n_colors):
            t = i / (n_colors - 1)
            if t < 0.5:
                color = interpolate_color(BLUE_E, WHITE, t * 2)
            else:
                color = interpolate_color(WHITE, RED_E, (t - 0.5) * 2)
            
            rect = Rectangle(
                width=0.2,
                height=0.1,
                fill_color=color,
                fill_opacity=1,
                stroke_width=0
            )
            rect.next_to(ORIGIN, RIGHT, buff=0.05 * i)
            curvature_scale.add(rect)
        
        # 添加标签
        neg_label = MathTex("K < 0").scale(0.6)
        zero_label = MathTex("K = 0").scale(0.6)
        pos_label = MathTex("K > 0").scale(0.6)
        
        neg_label.next_to(curvature_scale[0], DOWN, buff=0.2)
        zero_label.next_to(curvature_scale[n_colors // 2], DOWN, buff=0.2)
        pos_label.next_to(curvature_scale[-1], DOWN, buff=0.2)
        
        curvature_scale.add(neg_label, zero_label, pos_label)
        
        # 定位图例
        curvature_scale.scale(0.8).to_corner(DR, buff=0.5)
        
        # 显示曲率可视化
        self.play(FadeIn(curvature_surface, lag_ratio=0.01, run_time=2))
        self.play(FadeIn(curvature_scale))
        
        self.wait(1)
        
        # 4. 测地线动画
        geodesic_title = Text("测地线", font="Source Han Sans CN").scale(0.7)
        geodesic_title.next_to(gauss_curvature, DOWN, buff=0.8)
        
        self.play(Write(geodesic_title))
        
        # 在曲面上创建一条测地线
        # 注：真实的测地线需要求解微分方程，这里用参数曲线近似
        def geodesic_curve(t):
            # 参数化的曲线
            u = np.cos(t)
            v = np.sin(t)
            return saddle_surface(u, v)
        
        # 创建测地线
        t_values = np.linspace(0, 2 * np.pi, 100)
        geodesic_points = [geodesic_curve(t) for t in t_values]
        
        geodesic = VMobject(stroke_color=YELLOW, stroke_width=4)
        geodesic.set_points_as_corners(geodesic_points)
        geodesic.scale(1.5).to_edge(LEFT, buff=1)
        
        # 显示测地线
        self.play(Create(geodesic, run_time=2))
        
        # 添加动画粒子沿测地线运动
        particle = Sphere(radius=0.08, color=RED_A)
        particle.move_to(geodesic.get_start())
        
        self.play(FadeIn(particle))
        
        # 沿测地线运动
        self.play(
            MoveAlongPath(particle, geodesic),
            run_time=4,
            rate_func=linear
        )
        
        self.wait(1)
        
        # 过渡到下一部分
        self.play(
            FadeOut(saddle),
            FadeOut(saddle_title),
            FadeOut(curvature_title),
            FadeOut(gauss_curvature),
            FadeOut(curvature_surface),
            FadeOut(curvature_scale),
            FadeOut(geodesic_title),
            FadeOut(geodesic),
            FadeOut(particle),
            FadeOut(section_title)
        )
    
    def fractals_and_chaos(self):
        section_title = Text("分形维度与混沌", font="Source Han Sans CN").scale(1.2).to_edge(UP)
        section_title.set_color_by_gradient(MAROON_A, RED_C)
        
        self.play(Write(section_title))
        
        # 1. 曼德布罗特集合
        mandelbrot_title = Text("曼德布罗特集合", font="Source Han Sans CN").scale(0.8)
        mandelbrot_title.next_to(section_title, DOWN, buff=0.5)
        
        self.play(Write(mandelbrot_title))
        
        # 创建曼德布罗特集合
        mandelbrot_plane = ComplexPlane(
            x_range=[-2, 1, 0.5],
            y_range=[-1.5, 1.5, 0.5],
            background_line_style={
                "stroke_opacity": 0.3,
                "stroke_width": 1,
            }
        ).scale(1.2)
        
        # 简化的曼德布罗特集合（真实渲染需要更多计算）
        def in_mandelbrot(c, max_iter=20):
            z = 0
            for i in range(max_iter):
                z = z**2 + c
                if abs(z) > 2:
                    return i
            return max_iter
        
        # 创建曼德布罗特集合点云
        mandelbrot_set = VGroup()
        
        # 降低分辨率以提高性能
        resolution = 40
        x_range = np.linspace(-2, 1, resolution)
        y_range = np.linspace(-1.5, 1.5, resolution)
        
        for x in x_range:
            for y in y_range:
                c = complex(x, y)
                iter_count = in_mandelbrot(c)
                
                if iter_count == 20:  # 在集合内
                    color = BLACK
                else:
                    # 根据迭代次数着色
                    t = iter_count / 20
                    color = interpolate_color(
                        interpolate_color(BLACK, PURPLE, t),
                        interpolate_color(BLUE, WHITE, t),
                        t
                    )
                
                point = mandelbrot_plane.n2p(c)
                dot = Dot(point, radius=0.05, color=color)
                mandelbrot_set.add(dot)
        
        # 显示曼德布罗特集合
        self.play(
            Create(mandelbrot_plane),
            run_time=1
        )
        
        self.play(
            FadeIn(mandelbrot_set, lag_ratio=0.01),
            run_time=3
        )
        
        # 2. 茱莉亚集合
        julia_title = Text("茱莉亚集合", font="Source Han Sans CN").scale(0.8)
        julia_title.next_to(mandelbrot_title, DOWN, buff=3)
        
        self.play(Write(julia_title))
        
        # 创建茱莉亚集合
        julia_plane = ComplexPlane(
            x_range=[-1.5, 1.5, 0.5],
            y_range=[-1.5, 1.5, 0.5],
            background_line_style={
                "stroke_opacity": 0.3,
                "stroke_width": 1,
            }
        ).scale(1.2)
        
        julia_plane.to_edge(DOWN, buff=1)
        
        # 简化的茱莉亚集合函数
        def in_julia(z, c=complex(-0.7, 0.27), max_iter=20):
            for i in range(max_iter):
                z = z**2 + c
                if abs(z) > 2:
                    return i
            return max_iter
        
        # 创建茱莉亚集合点云
        julia_set = VGroup()
        
        # 降低分辨率
        resolution = 40
        x_range = np.linspace(-1.5, 1.5, resolution)
        y_range = np.linspace(-1.5, 1.5, resolution)
        
        for x in x_range:
            for y in y_range:
                z = complex(x, y)
                iter_count = in_julia(z)
                
                if iter_count == 20:  # 在集合内
                    color = BLACK
                else:
                    # 根据迭代次数着色
                    t = iter_count / 20
                    color = interpolate_color(
                        interpolate_color(BLACK, RED, t),
                        interpolate_color(YELLOW, WHITE, t),
                        t
                    )
                
                point = julia_plane.n2p(z)
                dot = Dot(point, radius=0.05, color=color)
                julia_set.add(dot)
        
        # 显示茱莉亚集合
        self.play(
            Create(julia_plane),
            run_time=1
        )
        
        self.play(
            FadeIn(julia_set, lag_ratio=0.01),
            run_time=3
        )
        
        # 3. 分形维度概念
        fractal_dim_title = Text("分形维度", font="Source Han Sans CN").scale(0.7)
        fractal_dim_formula = MathTex(r"D = \frac{\log N}{\log(1/r)}").scale(0.8)
        
        fractal_dim_title.to_edge(RIGHT, buff=2)
        fractal_dim_formula.next_to(fractal_dim_title, DOWN, buff=0.5)
        
        # 添加解释
        explanation = Text("曼德布罗特集合维度 ≈ 2", font="Source Han Sans CN").scale(0.6)
        explanation.next_to(fractal_dim_formula, DOWN, buff=0.5)
        
        self.play(
            Write(fractal_dim_title),
            Write(fractal_dim_formula),
            Write(explanation)
        )
        
        self.wait(1)
        
        # 放大曼德布罗特集合的一部分展示自相似性
        zoom_box = Square(side_length=0.5, color=WHITE)
        zoom_box.move_to(mandelbrot_plane.n2p(complex(-0.75, 0.1)))
        
        self.play(Create(zoom_box))
        
        # 创建放大的区域
        zoomed_mandelbrot = mandelbrot_set.copy()
        zoomed_mandelbrot.generate_target()
        zoomed_mandelbrot.target.scale(4)
        zoomed_mandelbrot.target.move_to(mandelbrot_set)
        
        # 放大动画
        self.play(
            MoveToTarget(zoomed_mandelbrot),
            FadeOut(zoom_box),
            run_time=2
        )
        
        self.wait(1)
        
        # 过渡到下一部分
        self.play(
            FadeOut(mandelbrot_plane),
            FadeOut(mandelbrot_set),
            FadeOut(zoomed_mandelbrot),
            FadeOut(julia_plane),
            FadeOut(julia_set),
            FadeOut(mandelbrot_title),
            FadeOut(julia_title),
            FadeOut(fractal_dim_title),
            FadeOut(fractal_dim_formula),
            FadeOut(explanation),
            FadeOut(section_title)
        )
    
    def fourier_transform(self):
        section_title = Text("傅里叶变换与信号处理", font="Source Han Sans CN").scale(1.2).to_edge(UP)
        section_title.set_color_by_gradient(TEAL_A, TEAL_E)
        
        self.play(Write(section_title))
        
        # 1. 傅里叶变换公式
        fourier_formula = MathTex(
            r"\hat{f}(\xi) = \int_{-\infty}^{\infty} f(x) e^{-2\pi i x \xi} \, dx"
        ).scale(1)
        
        fourier_formula.next_to(section_title, DOWN, buff=0.7)
        
        self.play(Write(fourier_formula))
        
        # 2. 创建波形和其频谱
        axes_time = Axes(
            x_range=[0, 10, 1],
            y_range=[-1.5, 1.5, 0.5],
            axis_config={"include_tip": False},
        ).scale(0.5)
        
        axes_freq = Axes(
            x_range=[0, 10, 1],
            y_range=[0, 1.2, 0.2],
            axis_config={"include_tip": False},
        ).scale(0.5)
        
        # 设置位置
        axes_time.to_edge(LEFT, buff=1)
        axes_time.to_edge(DOWN, buff=2)
        
        axes_freq.to_edge(RIGHT, buff=1)
        axes_freq.to_edge(DOWN, buff=2)
        
        # 标签
        time_label = Text("时域", font="Source Han Sans CN").scale(0.6)
        time_label.next_to(axes_time, UP, buff=0.2)
        
        freq_label = Text("频域", font="Source Han Sans CN").scale(0.6)
        freq_label.next_to(axes_freq, UP, buff=0.2)
        
        self.play(
            Create(axes_time),
            Create(axes_freq),
            Write(time_label),
            Write(freq_label)
        )
        
        # 3. 创建复合波形和其傅里叶变换
        # 定义波形（包含多个频率成分）
        def wave_function(t):
            return 0.5 * np.sin(2 * np.pi * 1 * t) + \
                   0.3 * np.sin(2 * np.pi * 2 * t) + \
                   0.15 * np.sin(2 * np.pi * 3 * t) + \
                   0.05 * np.sin(2 * np.pi * 5 * t)
        
        # 创建波形
        wave = axes_time.plot(
            wave_function,
            x_range=[0, 10, 0.01],
            color=TEAL
        )
        
        # 频谱（简化版，真实FFT需要更多计算）
        bar1 = Rectangle(height=0.5, width=0.1, fill_color=TEAL, fill_opacity=1)
        bar1.move_to(axes_freq.c2p(1, 0.25))
        
        bar2 = Rectangle(height=0.3, width=0.1, fill_color=TEAL, fill_opacity=1)
        bar2.move_to(axes_freq.c2p(2, 0.15))
        
        bar3 = Rectangle(height=0.15, width=0.1, fill_color=TEAL, fill_opacity=1)
        bar3.move_to(axes_freq.c2p(3, 0.075))
        
        bar5 = Rectangle(height=0.05, width=0.1, fill_color=TEAL, fill_opacity=1)
        bar5.move_to(axes_freq.c2p(5, 0.025))
        
        spectrum = VGroup(bar1, bar2, bar3, bar5)
        
        # 显示波形
        self.play(Create(wave))
        
        # 显示频谱
        self.play(FadeIn(spectrum))
        
        # 4. 动态演示波形合成
        # 显示各个频率分量
        def single_wave(t, freq, amp):
            return amp * np.sin(2 * np.pi * freq * t)
        
        wave1 = axes_time.plot(
            lambda t: single_wave(t, 1, 0.5),
            x_range=[0, 10, 0.01],
            color=RED
        )
        
        wave2 = axes_time.plot(
            lambda t: single_wave(t, 2, 0.3),
            x_range=[0, 10, 0.01],
            color=GREEN
        )
        
        wave3 = axes_time.plot(
            lambda t: single_wave(t, 3, 0.15),
            x_range=[0, 10, 0.01],
            color=BLUE
        )
        
        wave5 = axes_time.plot(
            lambda t: single_wave(t, 5, 0.05),
            x_range=[0, 10, 0.01],
            color=YELLOW
        )
        
        # 一一显示各个分量
        self.play(FadeOut(wave))
        
        component_waves = [wave1, wave2, wave3, wave5]
        component_colors = [RED, GREEN, BLUE, YELLOW]
        
        # 显示各个分量
        for i, (w, color) in enumerate(zip(component_waves, component_colors)):
            self.play(Create(w))
            
            # 高亮对应的频谱条
            self.play(
                spectrum[i].animate.set_color(color),
                run_time=0.5
            )
        
        # 组合所有分量
        self.play(
            Transform(
                VGroup(*component_waves),
                wave,
            ),
            spectrum.animate.set_color(TEAL),
            run_time=2
        )
        
        self.wait(1)
        
        # 5. 动态时频域变换演示
        # 创建波形变换器
        def morph_wave(t, alpha):
            # 从简单的正弦波变成复杂的方波
            # alpha从0到1，控制变换程度
            return (1 - alpha) * np.sin(2 * np.pi * t) + alpha * sum([
                (4 / ((2*k + 1) * np.pi)) * np.sin(2 * np.pi * (2*k + 1) * t)
                for k in range(5)
            ])
        
        # 创建变换条
        alpha_tracker = ValueTracker(0)
        
        morph_wave_graph = always_redraw(
            lambda: axes_time.plot(
                lambda t: morph_wave(t, alpha_tracker.get_value()),
                x_range=[0, 10, 0.01],
                color=interpolate_color(TEAL, RED, alpha_tracker.get_value())
            )
        )
        
        # 从正弦波变成方波时的频谱变化
        bars = VGroup()
        for k in range(10):
            freq = 2*k + 1
            # 初始高度几乎为0，只有k=0时为1
            height = 1 if k == 0 else 0.02
            
            bar = always_redraw(
                lambda k=k, freq=freq: Rectangle(
                    height=interpolate(
                        height, 
                        4 / (freq * np.pi) if freq <= 9 else 0.02,
                        alpha_tracker.get_value()
                    ),
                    width=0.1,
                    fill_color=interpolate_color(TEAL, RED, alpha_tracker.get_value()),
                    fill_opacity=1
                ).move_to(axes_freq.c2p(freq, interpolate(
                    height / 2, 
                    (4 / (freq * np.pi)) / 2 if freq <= 9 else 0.01,
                    alpha_tracker.get_value()
                )))
            )
            bars.add(bar)
        
        # 清除原有的图形
        self.play(
            FadeOut(VGroup(*component_waves)),
            FadeOut(spectrum)
        )
        
        # 显示新的图形
        self.play(
            FadeIn(morph_wave_graph),
            FadeIn(bars)
        )
        
        # 变换动画
        self.play(
            alpha_tracker.animate.set_value(1),
            run_time=5,
            rate_func=smooth
        )
        
        self.wait(1)
        
        # 过渡到下一部分
        self.play(
            FadeOut(axes_time),
            FadeOut(axes_freq),
            FadeOut(time_label),
            FadeOut(freq_label),
            FadeOut(morph_wave_graph),
            FadeOut(bars),
            FadeOut(fourier_formula),
            FadeOut(section_title)
        )
    
    def hyperdimensions_finale(self):
        section_title = Text("高维空间与数学之美", font="Source Han Sans CN").scale(1.2).to_edge(UP)
        section_title.set_color_by_gradient(*[random_bright_color() for _ in range(5)])
        
        self.play(Write(section_title))
        
        # 1. 创建四维超立方体投影
        def hypercube_vertices(dim=4):
            # 生成超立方体的顶点
            return np.array(list(itertools.product([-1, 1], repeat=dim)))
        
        def project_4d_to_3d(vertices_4d, w_factor=0.5):
            # 从4D投影到3D
            vertices_3d = []
            for vertex in vertices_4d:
                x, y, z, w = vertex
                factor = 1 / (w_factor - w)
                x_proj = x * factor
                y_proj = y * factor
                z_proj = z * factor
                vertices_3d.append([x_proj, y_proj, z_proj])
            return np.array(vertices_3d)
        
        def project_3d_to_2d(vertices_3d, view_distance=4):
            # 从3D投影到2D（简化视角）
            vertices_2d = []
            for vertex in vertices_3d:
                x, y, z = vertex
                factor = 1 / (view_distance - z)
                x_proj = x * factor
                y_proj = y * factor
                vertices_2d.append([x_proj, y_proj, 0])
            return np.array(vertices_2d)
        
        # 生成4D超立方体顶点
        hypercube_4d = hypercube_vertices(4)
        
        # 投影到3D，再到2D
        hypercube_3d = project_4d_to_3d(hypercube_4d)
        hypercube_2d = project_3d_to_2d(hypercube_3d)
        
        # 创建顶点
        vertices = VGroup(*[Dot(point, radius=0.05, color=WHITE) for point in hypercube_2d])
        
        # 连接边（只连接汉明距离为1的顶点，即只相差一个坐标）
        edges = VGroup()
        for i, v1 in enumerate(hypercube_4d):
            for j, v2 in enumerate(hypercube_4d):
                if i < j and np.sum(np.abs(v1 - v2)) == 2:  # 汉明距离为1
                    edge = Line(
                        hypercube_2d[i],
                        hypercube_2d[j],
                        stroke_width=1,
                        stroke_opacity=0.7
                    )
                    edges.add(edge)
        
        # 创建超立方体
        hypercube = VGroup(edges, vertices)
        hypercube.scale(1.5).move_to(ORIGIN)
        
        # 显示超立方体
        self.play(
            Create(edges, lag_ratio=0.02),
            FadeIn(vertices, lag_ratio=0.02),
            run_time=2
        )
        
        # 2. 旋转动画
        def update_hypercube(mob, alpha):
            # 在4D空间中旋转
            angle = alpha * 2 * np.pi
            
            # 旋转矩阵 (在xy和zw平面上)
            rot_xy = np.array([
                [np.cos(angle), -np.sin(angle), 0, 0],
                [np.sin(angle), np.cos(angle), 0, 0],
                [0, 0, 1, 0],
                [0, 0, 0, 1]
            ])
            
            rot_zw = np.array([
                [1, 0, 0, 0],
                [0, 1, 0, 0],
                [0, 0, np.cos(angle), -np.sin(angle)],
                [0, 0, np.sin(angle), np.cos(angle)]
            ])
            
            # 应用旋转
            rotated_4d = np.dot(hypercube_4d, rot_xy.T)
            rotated_4d = np.dot(rotated_4d, rot_zw.T)
            
            # 重新投影
            rotated_3d = project_4d_to_3d(rotated_4d)
            rotated_2d = project_3d_to_2d(rotated_3d)
            
            # 更新顶点和边
            for i, vertex in enumerate(vertices):
                vertex.move_to(rotated_2d[i])
            
            for i, edge in enumerate(edges):
                # 找到对应的顶点索引
                for j, v1 in enumerate(rotated_4d):
                    for k, v2 in enumerate(rotated_4d):
                        if j < k and np.sum(np.abs(v1 - v2)) == 2:
                            if i == 0:  # 只更新一次
                                edge.put_start_and_end_on(
                                    rotated_2d[j],
                                    rotated_2d[k]
                                )
                                break
                    else:
                        continue
                    break
        
        # 执行旋转动画
        self.play(
            UpdateFromAlphaFunc(hypercube, update_hypercube),
            run_time=8,
            rate_func=linear
        )
        
        # 3. 数学之美的总结
        beauty_title = Text("数学是宇宙的语言", font="Source Han Sans CN").scale(1)
        beauty_title.set_color_by_gradient(GOLD_A, GOLD_E)
        
        # 淡出超立方体，显示标题
        self.play(
            FadeOut(hypercube),
            Write(beauty_title),
            run_time=2
        )
        
        # 创建最终的数学公式画廊
        equations = VGroup(
            MathTex(r"e^{i\pi} + 1 = 0"),
            MathTex(r"\oint_{\partial \Omega} \omega = \int_{\Omega} d\omega"),
            MathTex(r"G_{\mu\nu} = \frac{8\pi G}{c^4} T_{\mu\nu}"),
            MathTex(r"\sum_{n=1}^{\infty} \frac{1}{n^2} = \frac{\pi^2}{6}"),
            MathTex(r"\nabla \times \vec{E} = -\frac{\partial \vec{B}}{\partial t}")
        )
        
        equations.arrange(DOWN, buff=0.5)
        equations.scale(0.7)
        
        # 依次显示公式
        for eq in equations:
            self.play(
                FadeIn(eq, shift=UP * 0.5),
                run_time=0.7
            )
        
        self.wait(1)
        
        # 最终淡出
        self.play(
            FadeOut(beauty_title),
            FadeOut(equations),
            FadeOut(section_title),
            run_time=2
        )