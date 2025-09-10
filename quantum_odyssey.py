# quantum_odyssey.py
from manim import *
import numpy as np
import random
from math import sin, cos, pi
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from my_manim_setup import *

# 自定义颜色
PHOTON_YELLOW = "#FFD700"
ELECTRON_GREEN = "#00FF00"
WAVE_BLUE = "#00BFFF"
QUANTUM_PURPLE = "#9370DB"
ENERGY_RED = "#FF4500"


class QuantumOdyssey(Scene):
    """
    一个完整的10-15分钟动画，深入探索光的本质
    """

    def construct(self):
        # 设置高质量渲染
        self.camera.background_color = "#000814"

        # 序章
        self.play_intro()

        # 第一章：光的几何世界
        self.chapter_1_geometric_optics()

        # 第二章：波动革命
        self.chapter_2_wave_revolution()

        # 第三章：量子觉醒
        self.chapter_3_quantum_awakening()

        # 第四章：双缝实验的启示
        self.chapter_4_double_slit_revelation()

        # 第五章：宇宙尺度的光
        self.chapter_5_cosmic_light()

        # 终章
        self.play_outro()

    def play_intro(self):
        """序章：史诗开场"""
        # 标题动画
        title = Text("光 · 量子奥德赛", font_size=72, font="STSong")
        title.set_color_by_gradient(PHOTON_YELLOW, QUANTUM_PURPLE)

        subtitle = Text("从经典到量子的认知革命", font_size=36, font="STSong")
        subtitle.next_to(title, DOWN, buff=0.5)

        # 背景粒子效果
        particles = VGroup()
        for _ in range(50):
            particle = Dot(
                point=np.array([
                    random.uniform(-7, 7),
                    random.uniform(-4, 4),
                    0
                ]),
                radius=random.uniform(0.01, 0.03),
                color=random.choice([PHOTON_YELLOW, WAVE_BLUE, QUANTUM_PURPLE])
            )
            particles.add(particle)

        self.add(particles)
        self.play(
            *[particle.animate.shift(random.uniform(-0.5, 0.5) * RIGHT + random.uniform(-0.5, 0.5) * UP)
              for particle in particles],
            Write(title, run_time=3),
            rate_func=smooth
        )
        self.play(FadeIn(subtitle, shift=UP))
        self.wait(3)

        # 过渡效果
        self.play(
            FadeOut(particles),
            title.animate.scale(0.5).to_corner(UL),
            FadeOut(subtitle)
        )
        self.wait(0.5)

    def chapter_1_geometric_optics(self):
        """第一章：光的几何世界 - 增强版"""
        chapter_title = Text("第一章：光的几何世界", font_size=48, font="STSong").to_edge(UP)
        self.play(Write(chapter_title))
        self.wait(1)

        # 1.1 光的直线传播 - 激光秀效果
        self.play(chapter_title.animate.scale(0.7).to_corner(UL))

        subtitle = Text("光的直线传播", font_size=36, font="STSong").next_to(chapter_title, DOWN)
        self.play(FadeIn(subtitle))

        # 创建激光源
        laser_source = VGroup(
            Rectangle(width=0.5, height=1, fill_opacity=1, color=GREY),
            Dot(radius=0.1, color=ENERGY_RED)
        ).shift(LEFT * 6)

        # 创建多个障碍物
        obstacles = VGroup()
        for i in range(3):
            obstacle = Circle(
                radius=0.5,
                fill_opacity=1,
                color=BLUE_E
            ).shift(LEFT * 2 + i * 2 * RIGHT + (i - 1) * 0.5 * UP)
            obstacles.add(obstacle)

        self.play(FadeIn(laser_source), FadeIn(obstacles))

        # 激光束动画
        laser_beams = VGroup()
        for angle in np.linspace(-PI / 6, PI / 6, 7):
            end_point = laser_source.get_center() + 10 * np.array([cos(angle), sin(angle), 0])
            beam = Line(
                laser_source.get_center(),
                end_point,
                stroke_width=3,
                color=ENERGY_RED
            )
            laser_beams.add(beam)

        # 计算阴影
        shadows = VGroup()
        for obstacle in obstacles:
            shadow = obstacle.copy()
            shadow.set_fill(BLACK, opacity=0.8)
            shadow.shift(RIGHT * 2)
            shadows.add(shadow)

        self.play(
            LaggedStart(*[Create(beam) for beam in laser_beams], lag_ratio=0.1),
            run_time=2
        )
        self.play(FadeIn(shadows))
        self.wait(2)

        # 清理场景
        self.play(FadeOut(VGroup(subtitle, laser_source, obstacles, laser_beams, shadows)))

        # 1.2 折射现象 - 水下世界
        subtitle = Text("折射：光的弯曲", font_size=36, font="STSong").next_to(chapter_title, DOWN)
        self.play(FadeIn(subtitle))

        # 创建水面
        water_surface = Line(LEFT * 7, RIGHT * 7, color=WAVE_BLUE)
        water = Rectangle(
            width=14, height=4,
            fill_color=WAVE_BLUE,
            fill_opacity=0.3,
            stroke_width=0
        ).next_to(water_surface, DOWN, buff=0)

        # 添加波纹效果
        wave_func = lambda x: 0.1 * sin(2 * x)
        water_wave = ParametricFunction(
            lambda t: np.array([t, wave_func(t), 0]),
            t_range=[-7, 7],
            color=WAVE_BLUE
        )

        self.play(Create(water_surface), FadeIn(water))
        self.play(Create(water_wave))

        # 光线折射动画
        incident_ray = Line(
            start=np.array([-4, 3, 0]),
            end=np.array([-1, 0, 0]),
            color=PHOTON_YELLOW,
            stroke_width=5
        )

        refracted_ray = Line(
            start=np.array([-1, 0, 0]),
            end=np.array([1, -2, 0]),
            color=PHOTON_YELLOW,
            stroke_width=5
        )

        # 法线
        normal = DashedLine(
            start=np.array([-1, 2, 0]),
            end=np.array([-1, -2, 0]),
            color=GREY
        )

        # 角度标记
        theta_i = Arc(
            radius=0.5,
            start_angle=PI,
            angle=-PI / 4,
            color=WHITE
        ).shift(np.array([-1, 0, 0]))

        theta_r = Arc(
            radius=0.5,
            start_angle=-PI / 2,
            angle=PI / 6,
            color=WHITE
        ).shift(np.array([-1, 0, 0]))

        # Snell定律
        snell_law = MathTex(
            r"n_1\sin\theta_1 = n_2\sin\theta_2",
            font_size=36
        ).to_corner(UR)

        self.play(
            Create(incident_ray),
            Create(normal)
        )
        self.play(
            Create(refracted_ray),
            Create(theta_i),
            Create(theta_r),
            Write(snell_law)
        )
        self.wait(2)

        # 全反射演示
        critical_text = Text("临界角与全反射", font_size=30, font="STSong").to_corner(DR)
        self.play(Write(critical_text))

        # 动态改变入射角
        angle_tracker = ValueTracker(PI / 6)

        incident_ray_2 = Line(
            start=np.array([2, -2, 0]),
            end=np.array([0, 0, 0]),
            color=PHOTON_YELLOW,
            stroke_width=5
        )

        reflected_ray = Line(
            start=np.array([0, 0, 0]),
            end=np.array([2, 2, 0]),
            color=PHOTON_YELLOW,
            stroke_width=5,
            stroke_opacity=0
        )

        incident_ray_2.add_updater(
            lambda m: m.put_start_and_end_on(
                start=np.array([2, -2, 0]),
                end=np.array([0, 0, 0])
            ).rotate(
                angle_tracker.get_value(),
                about_point=np.array([0, 0, 0])
            )
        )

        self.add(incident_ray_2)
        self.play(angle_tracker.animate.set_value(PI / 3), run_time=3)
        self.play(reflected_ray.animate.set_stroke(opacity=1))

        # 光纤原理
        fiber_text = Text("光纤通信原理", font_size=30, font="STSong").to_corner(DL)
        self.play(
            Write(fiber_text),
            FadeOut(VGroup(
                incident_ray, refracted_ray, theta_i, theta_r,
                incident_ray_2, reflected_ray, critical_text
            ))
        )

        # 光纤动画
        fiber_core = Rectangle(
            width=8, height=0.3,
            fill_color=WAVE_BLUE,
            fill_opacity=0.5,
            stroke_width=0
        )
        fiber_cladding = Rectangle(
            width=8, height=0.5,
            stroke_color=GREY,
            stroke_width=2,
            fill_opacity=0
        )

        self.play(
            FadeIn(fiber_core),
            Create(fiber_cladding)
        )

        # 光脉冲在光纤中传播
        light_pulse = Dot(radius=0.1, color=PHOTON_YELLOW)
        light_path = VMobject()
        light_path.set_points_as_corners([
            [-4, 0, 0], [-3, 0.15, 0], [-2, -0.15, 0],
            [-1, 0.15, 0], [0, -0.15, 0], [1, 0.15, 0],
            [2, -0.15, 0], [3, 0.15, 0], [4, 0, 0]
        ])

        self.play(
            MoveAlongPath(light_pulse, light_path),
            ShowPassingFlash(
                light_path.copy().set_stroke(PHOTON_YELLOW, width=4),
                run_time=3
            ),
            run_time=3
        )

        self.wait(1)
        self.play(FadeOut(VGroup(
            subtitle, water_surface, water, water_wave, normal, snell_law,
            fiber_text, fiber_core, fiber_cladding, light_pulse
        )))

        # 1.3 色散 - 彩虹形成
        subtitle = Text("色散：白光的分解", font_size=36, font="STSong").next_to(chapter_title, DOWN)
        self.play(FadeIn(subtitle))

        # 创建三棱镜
        prism = Polygon(
            [-2, -1.5, 0], [2, -1.5, 0], [0, 1.5, 0],
            fill_color=GREY,
            fill_opacity=0.3,
            stroke_color=WHITE
        )

        # 白光入射
        white_light = Line(
            LEFT * 6, [-1, -0.5, 0],
            stroke_width=8,
            color=WHITE
        )

        self.play(
            DrawBorderThenFill(prism),
            Create(white_light)
        )

        # 创建彩虹光谱
        spectrum_colors = [
            "#FF0000", "#FF7F00", "#FFFF00",
            "#00FF00", "#0000FF", "#4B0082", "#9400D3"
        ]

        spectrum = VGroup()
        for i, color in enumerate(spectrum_colors):
            angle = (i - 3) * 0.1
            ray = Line(
                [0.5, 0.3, 0],
                [6, angle * 5, 0],
                stroke_width=4,
                color=color
            )
            spectrum.add(ray)

        # 添加波长标注
        wavelength_labels = VGroup()
        wavelengths = ["700nm", "620nm", "580nm", "530nm", "470nm", "450nm", "400nm"]
        for i, (ray, wl) in enumerate(zip(spectrum, wavelengths)):
            label = Text(wl, font_size=20).next_to(ray.get_end(), RIGHT)
            wavelength_labels.add(label)

        self.play(
            LaggedStart(*[Create(ray) for ray in spectrum], lag_ratio=0.2),
            run_time=3
        )
        self.play(
            LaggedStart(*[Write(label) for label in wavelength_labels], lag_ratio=0.1),
            run_time=2
        )

        # 彩虹形成原理
        rainbow_text = Text("彩虹的形成", font_size=30, font="STSong").to_corner(DR)
        self.play(Write(rainbow_text))

        # 水滴模型
        water_drop = Circle(
            radius=1,
            fill_color=WAVE_BLUE,
            fill_opacity=0.4,
            stroke_color=WHITE
        ).shift(RIGHT * 3)

        # 光线在水滴中的路径
        ray_path = VMobject()
        ray_path.set_points_as_corners([
            [0, 0, 0], [2.5, 1, 0], [3.5, 0, 0], [3, -1, 0], [1, -1.5, 0]
        ])
        ray_path.set_stroke(WHITE, width=2)

        rainbow_effect = Arc(
            radius=2,
            start_angle=-PI / 3,
            angle=2 * PI / 3,
            stroke_width=20,
            stroke_color=WHITE
        ).next_to(water_drop, RIGHT, buff=0.5)
        # 直接使用颜色列表，无需Color转换
        rainbow_effect.set_color_by_gradient(*spectrum_colors)

        self.play(
            FadeOut(VGroup(spectrum, wavelength_labels, rainbow_text)),
            FadeIn(water_drop),
            Transform(prism, water_drop),
            FadeOut(white_light)
        )

        # 光在水滴中的反射和折射
        sun_rays = VGroup()
        for i in range(5):
            y = 0.3 * (i - 2)
            ray = Line(LEFT * 4, water_drop.get_left() + UP * y, color=WHITE)
            sun_rays.add(ray)

        self.play(LaggedStart(*[Create(ray) for ray in sun_rays], lag_ratio=0.2))
        # 使用Create替代ShowCreation
        self.play(Create(ray_path))
        self.play(Create(rainbow_effect))

        self.wait(2)
        self.play(FadeOut(VGroup(
            subtitle, prism, water_drop, sun_rays, ray_path, rainbow_effect,
            chapter_title
        )))

    def chapter_2_wave_revolution(self):
        """第二章：波动革命 - 增强版"""
        chapter_title = Text("第二章：波动革命", font_size=48, font="STSong").to_edge(UP)
        self.play(Write(chapter_title))
        self.wait(1)

        # 2.1 波的基本性质
        subtitle = Text("波的本质：振动与传播", font_size=36, font="STSong").next_to(chapter_title, DOWN)
        self.play(FadeIn(subtitle))

        # 创建坐标系
        axes = Axes(
            x_range=[-1, 5, 1],
            y_range=[-1.5, 1.5, 0.5],
            axis_config={"include_tip": False}
        )
        x_label = MathTex("x").next_to(axes.x_axis.get_end(), RIGHT)
        y_label = MathTex("y").next_to(axes.y_axis.get_end(), UP)
        self.play(Create(axes), Write(x_label), Write(y_label))

        # 波函数
        def wave_func(x, t):
            return np.sin(2 * PI * (x - t))

        # 创建波的图形
        t_tracker = ValueTracker(0)
        wave = always_redraw(
            lambda: axes.plot(
                lambda x: wave_func(x, t_tracker.get_value()),
                x_range=[0, 4],
                color=WAVE_BLUE
            )
        )

        # 振动粒子
        particles = VGroup()
        for x in np.linspace(0, 4, 20):
            particle = Dot(
                axes.c2p(x, 0),
                radius=0.05,
                color=BLUE
            )
            particle.add_updater(
                lambda d, x=x: d.move_to(
                    axes.c2p(x, wave_func(x, t_tracker.get_value()))
                )
            )
            particles.add(particle)

        # 波动方程
        wave_equation = MathTex(
            r"\frac{\partial^2 y}{\partial x^2} = \frac{1}{v^2}\frac{\partial^2 y}{\partial t^2}"
        ).to_corner(UR)

        self.play(Create(wave), FadeIn(particles))
        self.play(Write(wave_equation))
        self.play(t_tracker.animate.set_value(2), run_time=5, rate_func=linear)

        self.wait(1)
        self.play(FadeOut(VGroup(
            wave, particles, axes, x_label, y_label, wave_equation
        )))

        # 2.2 杨氏双缝干涉实验
        subtitle_new = Text("杨氏双缝干涉实验", font_size=36, font="STSong").next_to(chapter_title, DOWN)
        self.play(Transform(subtitle, subtitle_new))

        # 创建实验装置
        source = Dot(LEFT * 6, color=PHOTON_YELLOW, radius=0.1)
        source_label = Text("光源", font_size=24, font="STSong").next_to(source, DOWN)

        barrier = Rectangle(height=4, width=0.2, color=GREY, fill_opacity=1)
        slits = VGroup(
            Rectangle(height=0.3, width=0.2, color=BLACK, fill_opacity=1).move_to(barrier).shift(UP * 0.5),
            Rectangle(height=0.3, width=0.2, color=BLACK, fill_opacity=1).move_to(barrier).shift(DOWN * 0.5)
        )
        barrier_with_slits = VGroup(barrier, slits).shift(LEFT * 2)

        screen = Rectangle(height=4, width=0.2, color=WHITE, fill_opacity=0.5).shift(RIGHT * 4)

        self.play(
            FadeIn(source),
            Write(source_label),
            FadeIn(barrier_with_slits),
            FadeIn(screen)
        )

        # 惠更斯原理
        huygens_text = Text("惠更斯原理", font_size=24, font="STSong").to_edge(DOWN)
        self.play(Write(huygens_text))

        # 从缝隙发出的圆形波
        waves = VGroup()
        for slit in slits:
            for i in range(4):
                wave = Circle(
                    radius=i * 0.5,
                    stroke_width=2,
                    stroke_opacity=1 - i * 0.2,
                    color=WAVE_BLUE
                ).move_to(slit)
                waves.add(wave)

        self.play(FadeIn(waves))

        # 创建干涉条纹
        interference_pattern = VGroup()
        for y in np.linspace(-1.5, 1.5, 100):
            # 模拟干涉图样
            x = 4
            d = 1  # 缝间距
            wavelength = 0.3
            path_diff = np.sqrt((x + 2) ** 2 + (y - 0.5) ** 2) - np.sqrt((x + 2) ** 2 + (y + 0.5) ** 2)
            intensity = np.cos(PI * path_diff / wavelength) ** 2

            point = Dot(
                RIGHT * x + UP * y,
                radius=0.03,
                color=WAVE_BLUE,
                fill_opacity=intensity
            )
            interference_pattern.add(point)

        self.play(FadeIn(interference_pattern))

        # 干涉方程
        interference_eq = MathTex(
            r"d\sin\theta = n\lambda",
            font_size=36
        ).to_corner(UR)

        self.play(Write(interference_eq))
        self.wait(2)

        # 清理场景
        self.play(FadeOut(VGroup(
            subtitle, source, source_label, barrier_with_slits,
            screen, waves, interference_pattern, interference_eq, huygens_text
        )))

        # 2.3 衍射现象
        subtitle = Text("衍射：波绕过障碍物", font_size=36, font="STSong").next_to(chapter_title, DOWN)
        self.play(FadeIn(subtitle))

        # 单缝衍射
        slit = Rectangle(height=0.5, width=0.2, color=GREY, fill_opacity=1).shift(LEFT * 2)

        # 入射平面波
        plane_waves = VGroup()
        for i in range(5):
            line = Line(
                LEFT * 6 + UP * (i - 2) * 0.5,
                LEFT * 2 + UP * (i - 2) * 0.5,
                stroke_width=2,
                color=WAVE_BLUE
            )
            plane_waves.add(line)

        self.play(FadeIn(slit), Create(plane_waves))

        # 衍射波
        diffraction_arcs = VGroup()
        for i in range(1, 6):
            arc = Arc(
                radius=i * 0.5,
                start_angle=-PI / 2 - PI / 4,
                angle=PI / 2 + PI / 2,
                stroke_width=3 / (i * 0.7),
                color=WAVE_BLUE
            ).shift(LEFT * 2)
            diffraction_arcs.add(arc)

        # 衍射图样
        diffraction_pattern = VGroup()
        screen_pos = RIGHT * 4
        for y in np.linspace(-2, 2, 100):
            # 单缝衍射公式: I = I0 * (sin(β)/β)^2 where β = (πa/λ)sinθ
            x = 4
            slit_width = 0.5
            wavelength = 0.2
            angle = np.arctan(y / x)
            beta = PI * slit_width * np.sin(angle) / wavelength
            if abs(beta) < 0.001:  # 避免除以零
                intensity = 1
            else:
                intensity = (np.sin(beta) / beta) ** 2

            point = Dot(
                screen_pos + UP * y,
                radius=0.03,
                color=WAVE_BLUE,
                fill_opacity=intensity
            )
            diffraction_pattern.add(point)

        self.play(Create(diffraction_arcs))
        self.play(FadeIn(diffraction_pattern))

        # 衍射公式
        diffraction_eq = MathTex(
            r"a\sin\theta = n\lambda",
            font_size=36
        ).to_corner(UR)

        self.play(Write(diffraction_eq))
        self.wait(2)

        self.play(FadeOut(VGroup(
            subtitle, slit, plane_waves, diffraction_arcs,
            diffraction_pattern, diffraction_eq, chapter_title
        )))

    def chapter_3_quantum_awakening(self):
        """第三章：量子觉醒 - 增强版"""
        chapter_title = Text("第三章：量子觉醒", font_size=48, font="STSong").to_edge(UP)
        self.play(Write(chapter_title))
        self.wait(1)

        # 3.1 黑体辐射 - 量子理论的起源
        subtitle = Text("黑体辐射：量子理论的起源", font_size=36, font="STSong").next_to(chapter_title, DOWN)
        self.play(FadeIn(subtitle))

        # 坐标系
        axes = Axes(
            x_range=[0, 5, 1],
            y_range=[0, 4, 1],
            axis_config={"include_tip": True}
        )

        x_label = MathTex(r"\lambda \ (µm)").next_to(axes.x_axis.get_end(), RIGHT)
        y_label = MathTex(r"I(\lambda)").next_to(axes.y_axis.get_end(), UP)

        self.play(Create(axes), Write(x_label), Write(y_label))

        # 经典理论曲线 (Rayleigh-Jeans)
        classical_curve = axes.plot(
            lambda x: 4 / (x ** 2) if x > 0.2 else 0,
            x_range=[0.2, 5],
            color=RED
        )
        classical_label = Text(
            "经典理论 (瑞利-金斯)",
            font_size=24,
            font="STSong"
        ).next_to(classical_curve.point_from_proportion(0.8), UP)

        # 普朗克量子曲线
        def planck_law(x, T=5000):
            h = 6.63e-34
            c = 3e8
            k = 1.38e-23
            # 简化的公式，不使用实际物理单位
            return 8 * PI * (1 / x ** 5) / (np.exp(1 / (x * T * 0.0001)) - 1)

        planck_curve = axes.plot(
            lambda x: planck_law(x) if x > 0.1 else 0,
            x_range=[0.1, 5],
            color=QUANTUM_PURPLE
        )
        planck_label = Text(
            "普朗克量子理论",
            font_size=24,
            font="STSong"
        ).next_to(planck_curve.point_from_proportion(0.5), RIGHT)

        self.play(Create(classical_curve), Write(classical_label))
        self.wait(1)

        # 紫外灾变
        uv_disaster = Text(
            "紫外灾变",
            font_size=24,
            color=RED,
            font="STSong"
        ).next_to(classical_curve.point_from_proportion(0.1), RIGHT)
        self.play(Write(uv_disaster))

        self.play(Create(planck_curve), Write(planck_label))

        # 普朗克量子假设
        planck_hypothesis = MathTex(
            r"E = nh\nu, \quad n = 1,2,3,\ldots",
            font_size=36
        ).to_edge(DOWN)

        self.play(Write(planck_hypothesis))
        self.wait(2)

        self.play(FadeOut(VGroup(
            subtitle, axes, x_label, y_label, classical_curve, classical_label,
            planck_curve, planck_label, uv_disaster, planck_hypothesis
        )))

        # 3.2 光电效应 - 爱因斯坦的贡献
        subtitle = Text("光电效应：光子的粒子性", font_size=36, font="STSong").next_to(chapter_title, DOWN)
        self.play(FadeIn(subtitle))

        # 金属板
        metal_plate = Rectangle(
            width=3, height=0.5,
            fill_color=GREY_D,
            fill_opacity=1
        ).shift(DOWN)

        self.play(FadeIn(metal_plate))

        # 红光实验（低频高强）
        red_light_source = Dot(LEFT * 4 + UP, color=RED, radius=0.15)
        red_label = Text("低频红光\n(高强度)", font_size=24, font="STSong").next_to(red_light_source, UP)

        red_photons = VGroup(*[
            Dot(
                red_light_source.get_center() + 0.2 * RIGHT * i,
                color=RED,
                radius=0.08
            ) for i in range(10)
        ])

        self.play(FadeIn(red_light_source), Write(red_label))
        self.play(LaggedStart(*[
            photon.animate.move_to(metal_plate.get_center() + UP * 0.25 + 0.2 * i * LEFT)
            for i, photon in enumerate(red_photons)
        ], lag_ratio=0.1))

        no_effect_text = Text(
            "没有电子逸出!",
            font_size=24,
            color=RED,
            font="STSong"
        ).next_to(metal_plate, DOWN)

        self.play(Write(no_effect_text))
        self.play(FadeOut(red_photons))

        # 蓝光实验（高频低强）
        blue_light_source = Dot(RIGHT * 4 + UP, color=BLUE, radius=0.15)
        blue_label = Text("高频蓝光\n(低强度)", font_size=24, font="STSong").next_to(blue_light_source, UP)

        blue_photon = Dot(blue_light_source.get_center(), color=BLUE, radius=0.1)

        self.play(FadeIn(blue_light_source), Write(blue_label))
        self.play(blue_photon.animate.move_to(metal_plate.get_center() + UP * 0.25))

        # 电子逸出
        electron = Dot(metal_plate.get_center() + UP * 0.25, color=ELECTRON_GREEN, radius=0.08)

        self.play(FadeOut(blue_photon), FadeIn(electron))
        self.play(electron.animate.move_to(RIGHT * 3 + DOWN * 2))

        # 光电效应方程
        photoelectric_eq = MathTex(
            r"E_k = h\nu - \phi",
            font_size=36
        ).to_corner(UR)

        self.play(Write(photoelectric_eq))

        # 爱因斯坦的解释
        einstein_text = Text(
            "光是由粒子(光子)组成的!",
            font_size=30,
            color=YELLOW,
            font="STSong"
        ).to_edge(DOWN)

        self.play(
            FadeOut(no_effect_text),
            Write(einstein_text)
        )

        self.wait(2)
        self.play(FadeOut(VGroup(
            subtitle, metal_plate, red_light_source, red_label,
            blue_light_source, blue_label, electron,
            photoelectric_eq, einstein_text
        )))

        # 3.3 康普顿散射
        subtitle = Text("康普顿散射：光子动量", font_size=36, font="STSong").next_to(chapter_title, DOWN)
        self.play(FadeIn(subtitle))

        # 自由电子
        electron = Dot(ORIGIN, color=ELECTRON_GREEN, radius=0.15)
        electron_label = MathTex("e^-").next_to(electron, DOWN)

        self.play(FadeIn(electron), Write(electron_label))

        # 入射光子
        incident_photon = Dot(LEFT * 4 + UP, color=PHOTON_YELLOW, radius=0.1)
        photon_path = Line(LEFT * 4 + UP, ORIGIN)

        self.play(MoveAlongPath(incident_photon, photon_path))

        # 散射光子与电子
        scattered_photon = Dot(ORIGIN, color=RED, radius=0.1)
        recoil_electron = Dot(ORIGIN, color=ELECTRON_GREEN, radius=0.15)

        scattered_path = Line(ORIGIN, RIGHT * 3 + UP * 2)
        recoil_path = Line(ORIGIN, RIGHT * 2 + DOWN * 2)

        self.play(
            MoveAlongPath(scattered_photon, scattered_path),
            MoveAlongPath(recoil_electron, recoil_path)
        )

        # 波长增加
        wavelength_increase = MathTex(
            r"\Delta\lambda = \frac{h}{m_e c}(1 - \cos\theta)",
            font_size=36
        ).to_edge(DOWN)

        self.play(Write(wavelength_increase))

        # 动量守恒
        momentum_conservation = MathTex(
            r"\vec{p}_{\gamma,i} = \vec{p}_{\gamma,f} + \vec{p}_{e}",
            font_size=36
        ).to_edge(UP, buff=1.5)

        self.play(Write(momentum_conservation))

        self.wait(2)
        self.play(FadeOut(VGroup(
            subtitle, electron, electron_label, incident_photon,
            scattered_photon, recoil_electron, wavelength_increase,
            momentum_conservation, chapter_title
        )))

    def chapter_4_double_slit_revelation(self):
        """第四章：双缝实验的启示 - 增强版"""
        chapter_title = Text("第四章：双缝实验的启示", font_size=48, font="STSong").to_edge(UP)
        self.play(Write(chapter_title))
        self.wait(1)

        # 4.1 经典双缝实验与量子迷题
        subtitle = Text("经典双缝实验的量子迷题", font_size=36, font="STSong").next_to(chapter_title, DOWN)
        self.play(FadeIn(subtitle))

        # 创建实验装置
        source = Dot(LEFT * 6, color=ELECTRON_GREEN, radius=0.15)
        source_label = Text("电子源", font_size=24, font="STSong").next_to(source, DOWN)

        barrier = Rectangle(height=4, width=0.2, color=GREY, fill_opacity=1)
        slits = VGroup(
            Rectangle(height=0.3, width=0.2, color=BLACK, fill_opacity=1).move_to(barrier).shift(UP * 0.5),
            Rectangle(height=0.3, width=0.2, color=BLACK, fill_opacity=1).move_to(barrier).shift(DOWN * 0.5)
        )
        barrier_with_slits = VGroup(barrier, slits).shift(LEFT * 2)

        screen = Rectangle(height=4, width=0.2, color=WHITE, fill_opacity=0.5).shift(RIGHT * 4)

        self.play(
            FadeIn(source),
            Write(source_label),
            FadeIn(barrier_with_slits),
            FadeIn(screen)
        )

        # 第一部分：单个电子累积过程
        single_electron_text = Text(
            "单个电子逐个发射",
            font_size=30,
            font="STSong"
        ).to_edge(DOWN)
        self.play(Write(single_electron_text))

        # 干涉条纹（最终结果）
        interference_pattern = VGroup()
        for y in np.linspace(-1.5, 1.5, 100):
            # 模拟干涉图样
            x = 4
            d = 1  # 缝间距
            wavelength = 0.3
            path_diff = np.sqrt((x + 2) ** 2 + (y - 0.5) ** 2) - np.sqrt((x + 2) ** 2 + (y + 0.5) ** 2)
            intensity = np.cos(PI * path_diff / wavelength) ** 2

            point = Dot(
                RIGHT * x + UP * y,
                radius=0.03,
                color=ELECTRON_GREEN,
                fill_opacity=intensity
            )
            interference_pattern.add(point)

        # 模拟电子逐个累积
        dots_on_screen = VGroup()

        # 定义干涉条纹的概率分布
        def get_interference_y_pos():
            y_values = np.linspace(-1.5, 1.5, 500)
            k = 2.5
            probabilities = (np.cos(y_values * k) ** 2)
            probabilities /= np.sum(probabilities)
            return np.random.choice(y_values, p=probabilities)

        # 逐个电子动画
        for i in range(30):
            electron = Dot(source.get_center(), color=ELECTRON_GREEN, radius=0.1)
            self.add(electron)

            # 电子到达双缝
            self.play(
                electron.animate.move_to(LEFT * 2 + UP * random.choice([-0.5, 0.5])),
                run_time=0.3,
                rate_func=linear
            )

            # 电子形成波包
            wave_packet = VGroup(*[
                Circle(
                    radius=r,
                    stroke_width=2,
                    stroke_opacity=0.8 - r * 0.2,
                    color=WAVE_BLUE
                ).move_to(electron.get_center())
                for r in np.linspace(0.1, 0.5, 3)
            ])

            self.play(
                FadeOut(electron),
                FadeIn(wave_packet),
                run_time=0.2
            )

            # 波消失，电子在屏幕上显现
            target_y = get_interference_y_pos()
            hit_dot = Dot(
                RIGHT * 4 + UP * target_y,
                radius=0.05,
                color=ELECTRON_GREEN
            )

            self.play(
                FadeOut(wave_packet),
                FadeIn(hit_dot),
                run_time=0.2
            )

            dots_on_screen.add(hit_dot)

            if i % 10 == 9:
                self.wait(0.5)

        # 展示最终的干涉图样
        self.play(
            FadeOut(single_electron_text),
            FadeOut(dots_on_screen),
            FadeIn(interference_pattern)
        )

        # 粒子还是波？
        question_text = Text(
            "电子是粒子，为何表现出波动性？",
            font_size=30,
            color=YELLOW,
            font="STSong"
        ).to_edge(DOWN)

        self.play(Write(question_text))
        self.wait(2)

        self.play(FadeOut(VGroup(
            subtitle, source, source_label, barrier_with_slits,
            screen, interference_pattern, question_text
        )))

        # 4.2 观察者效应
        subtitle = Text("观察者效应：测量导致波函数坍缩", font_size=36, font="STSong").next_to(chapter_title, DOWN)
        self.play(FadeIn(subtitle))

        # 重新创建实验装置
        source = Dot(LEFT * 6, color=ELECTRON_GREEN, radius=0.15)
        barrier_with_slits = VGroup(barrier, slits).shift(LEFT * 2)
        screen = Rectangle(height=4, width=0.2, color=WHITE, fill_opacity=0.5).shift(RIGHT * 4)

        # 添加探测器
        detectors = VGroup(
            Square(side_length=0.5, color=RED, fill_opacity=0.3).move_to(slits[0].get_center() + RIGHT * 0.5),
            Square(side_length=0.5, color=RED, fill_opacity=0.3).move_to(slits[1].get_center() + RIGHT * 0.5)
        )
        detector_label = Text("探测器", font_size=24, font="STSong").next_to(detectors, RIGHT)

        self.play(
            FadeIn(source),
            FadeIn(barrier_with_slits),
            FadeIn(screen),
            FadeIn(detectors),
            Write(detector_label)
        )

        # 有探测器时的结果
        detector_text = Text(
            "探测电子经过哪个缝",
            font_size=30,
            font="STSong"
        ).to_edge(DOWN)
        self.play(Write(detector_text))

        # 单个电子通过，被探测
        for i in range(20):
            electron = Dot(source.get_center(), color=ELECTRON_GREEN, radius=0.1)
            self.add(electron)

            # 随机选择一个缝
            chosen_slit = random.choice([0, 1])
            chosen_detector = detectors[chosen_slit]

            # 电子到达缝
            self.play(
                electron.animate.move_to(slits[chosen_slit].get_center()),
                run_time=0.3,
                rate_func=linear
            )

            # 探测器闪烁
            self.play(
                chosen_detector.animate.set_color(YELLOW),
                run_time=0.2
            )
            self.play(
                chosen_detector.animate.set_color(RED),
                run_time=0.2
            )

            # 电子到达屏幕
            # 现在是两个亮带，不再是干涉条纹
            target_y = 0.5 if chosen_slit == 0 else -0.5
            target_y += random.gauss(0, 0.2)  # 添加随机偏移

            hit_dot = Dot(
                RIGHT * 4 + UP * target_y,
                radius=0.05,
                color=ELECTRON_GREEN
            )

            self.play(
                FadeOut(electron),
                FadeIn(hit_dot),
                run_time=0.2
            )

            if i % 10 == 9:
                self.wait(0.5)

        # 双峰分布
        double_peak = VGroup()
        for y in np.linspace(-1.5, 1.5, 100):
            # 模拟双峰分布
            intensity = np.exp(-(y - 0.5) ** 2 / 0.1) + np.exp(-(y + 0.5) ** 2 / 0.1)
            intensity /= 2  # 归一化

            point = Dot(
                RIGHT * 4 + UP * y,
                radius=0.03,
                color=ELECTRON_GREEN,
                fill_opacity=intensity
            )
            double_peak.add(point)

        self.play(FadeIn(double_peak))

        # 解释波函数坍缩
        collapse_text = Text(
            "测量导致波函数坍缩!",
            font_size=30,
            color=RED,
            font="STSong"
        ).to_edge(DOWN)

        self.play(
            FadeOut(detector_text),
            Write(collapse_text)
        )

        # 波函数数学表达
        wavefunction = MathTex(
            r"|\psi\rangle = \frac{1}{\sqrt{2}}(|slit_1\rangle + |slit_2\rangle)",
            font_size=36
        ).to_corner(UR)

        measured_state = MathTex(
            r"|\psi_{measured}\rangle = |slit_1\rangle \text{ or } |slit_2\rangle",
            font_size=36
        ).next_to(wavefunction, DOWN, aligned_edge=LEFT)

        self.play(Write(wavefunction))
        self.play(Write(measured_state))

        self.wait(2)
        self.play(FadeOut(VGroup(
            subtitle, source, barrier_with_slits, screen, detectors,
            detector_label, double_peak, collapse_text,
            wavefunction, measured_state, chapter_title
        )))

    def chapter_5_cosmic_light(self):
        """第五章：宇宙尺度的光 - 增强版"""
        chapter_title = Text("第五章：宇宙尺度的光", font_size=48, font="STSong").to_edge(UP)
        self.play(Write(chapter_title))
        self.wait(1)

        # 5.1 光的相对论性质
        subtitle = Text("光的相对论性质", font_size=36, font="STSong").next_to(chapter_title, DOWN)
        self.play(FadeIn(subtitle))

        # 光速不变性
        light_speed_text = Text(
            "光速恒定: c ≈ 299,792,458 m/s",
            font_size=30,
            font="STSong"
        )

        einstein_postulate = Text(
            "光速对所有观察者都相同",
            font_size=36,
            color=YELLOW,
            font="STSong"
        ).next_to(light_speed_text, DOWN)

        self.play(Write(light_speed_text))
        self.play(Write(einstein_postulate))

        # 相对论效应动画
        self.play(
            FadeOut(light_speed_text),
            FadeOut(einstein_postulate)
        )

        # 时间膨胀
        time_dilation_text = Text(
            "时间膨胀",
            font_size=36,
            font="STSong"
        )

        time_dilation_eq = MathTex(
            r"\Delta t' = \frac{\Delta t}{\sqrt{1-\frac{v^2}{c^2}}}",
            font_size=36
        ).next_to(time_dilation_text, DOWN)

        self.play(Write(time_dilation_text))
        self.play(Write(time_dilation_eq))

        # 光钟演示
        light_clock = VGroup(
            Line(LEFT * 0.5, RIGHT * 0.5, color=GREY),
            Line(LEFT * 0.5, LEFT * 0.5 + UP * 2, color=GREY),
            Line(RIGHT * 0.5, RIGHT * 0.5 + UP * 2, color=GREY),
            Line(LEFT * 0.5 + UP * 2, RIGHT * 0.5 + UP * 2, color=GREY)
        )

        photon = Dot(LEFT * 0.5, color=PHOTON_YELLOW, radius=0.1)

        self.play(
            FadeOut(time_dilation_text),
            FadeOut(time_dilation_eq),
            Create(light_clock),
            FadeIn(photon)
        )

        # 静止参考系中的光钟
        paths = [
            Line(LEFT * 0.5, LEFT * 0.5 + UP * 2),
            Line(LEFT * 0.5 + UP * 2, RIGHT * 0.5 + UP * 2),
            Line(RIGHT * 0.5 + UP * 2, RIGHT * 0.5),
            Line(RIGHT * 0.5, LEFT * 0.5)
        ]

        for path in paths:
            self.play(
                MoveAlongPath(photon, path),
                run_time=0.5
            )

        # 匀速运动参考系中的光钟
        moving_text = Text(
            "在运动参考系中",
            font_size=30,
            font="STSong"
        ).to_edge(DOWN)

        self.play(
            Write(moving_text),
            light_clock.animate.shift(RIGHT * 2)
        )

        # 光在运动钟中走"之"字形
        zigzag_path = VMobject()
        zigzag_path.set_points_as_corners([
            LEFT * 0.5 + RIGHT * 2,
            LEFT * 0.5 + UP * 2 + RIGHT * 3,
            RIGHT * 0.5 + UP * 2 + RIGHT * 4,
            RIGHT * 0.5 + RIGHT * 5
        ])

        self.play(
            MoveAlongPath(photon, zigzag_path),
            run_time=1
        )

        time_dilation_conclusion = Text(
            "运动钟变慢!",
            font_size=36,
            color=RED,
            font="STSong"
        ).next_to(moving_text, UP)

        self.play(Write(time_dilation_conclusion))

        self.wait(2)
        self.play(FadeOut(VGroup(
            subtitle, light_clock, photon, moving_text,
            time_dilation_conclusion
        )))

        # 5.2 质能方程与核能
        subtitle = Text("质能方程与核能", font_size=36, font="STSong").next_to(chapter_title, DOWN)
        self.play(FadeIn(subtitle))

        # 爱因斯坦质能方程
        emc2 = MathTex(
            r"E = mc^2",
            font_size=72
        )

        self.play(Write(emc2))

        # 核裂变动画
        uranium_nucleus = Circle(
            radius=0.8,
            color=ENERGY_RED,
            fill_opacity=0.5
        ).shift(LEFT * 3)

        uranium_label = Text(
            "铀-235",
            font_size=24,
            font="STSong"
        ).next_to(uranium_nucleus, DOWN)

        neutron = Dot(
            LEFT * 6,
            color=BLUE,
            radius=0.2
        )

        neutron_label = Text(
            "中子",
            font_size=24,
            font="STSong"
        ).next_to(neutron, DOWN)

        self.play(
            FadeOut(emc2),
            FadeIn(uranium_nucleus),
            Write(uranium_label),
            FadeIn(neutron),
            Write(neutron_label)
        )

        self.play(
            neutron.animate.move_to(uranium_nucleus.get_center()),
            run_time=1
        )

        # 裂变产物
        fission_products = VGroup(
            Circle(radius=0.5, color=ORANGE, fill_opacity=0.5),
            Circle(radius=0.4, color=GREEN, fill_opacity=0.5)
        )

        energy_rays = VGroup(*[
            Line(
                ORIGIN,
                0.5 * np.array([cos(i * PI / 4), sin(i * PI / 4), 0]),
                stroke_width=3,
                color=PHOTON_YELLOW
            ) for i in range(8)
        ])

        self.play(
            FadeOut(neutron),
            Transform(
                uranium_nucleus,
                VGroup(
                    fission_products[0].copy().shift(LEFT * 2 + UP),
                    fission_products[1].copy().shift(LEFT * 2 + DOWN)
                )
            ),
            Flash(LEFT * 3, color=PHOTON_YELLOW, line_length=1, flash_radius=1)
        )

        # 放出能量
        energy_value = Text(
            "1个原子 ≈ 200 MeV",
            font_size=30,
            font="STSong"
        ).shift(RIGHT * 3)

        mass_defect = MathTex(
            r"\Delta m \cdot c^2 = \Delta E",
            font_size=36
        ).next_to(energy_value, DOWN)

        self.play(
            Write(energy_value),
            Write(mass_defect)
        )

        self.wait(2)
        self.play(FadeOut(VGroup(
            subtitle, uranium_nucleus, uranium_label, neutron_label,
            energy_value, mass_defect, chapter_title
        )))

    def play_outro(self):
        """终章：宇宙之谜"""
        outro_title = Text("结语：宇宙之谜", font_size=60, font="STSong")
        self.play(Write(outro_title))
        self.wait(1)
        self.play(outro_title.animate.to_edge(UP))

        wave_particle = Text(
            "光既是波，又是粒子",
            font_size=36,
            color=PHOTON_YELLOW,
            font="STSong"
        )

        measurement_effect = Text(
            "观察改变现实",
            font_size=36,
            color=QUANTUM_PURPLE,
            font="STSong"
        ).next_to(wave_particle, DOWN, buff=0.5)

        uncertainty = Text(
            "测不准原理限制我们的认知",
            font_size=36,
            color=WAVE_BLUE,
            font="STSong"
        ).next_to(measurement_effect, DOWN, buff=0.5)

        self.play(Write(wave_particle))
        self.wait(1)
        self.play(Write(measurement_effect))
        self.wait(1)
        self.play(Write(uncertainty))
        self.wait(2)

        final_message = Text(
            "世界远比我们想象的更奇妙",
            font_size=48,
            color=ENERGY_RED,
            font="STSong"
        ).shift(DOWN * 2)

        self.play(Write(final_message))

        # 粒子效果结尾
        particles = VGroup()
        for _ in range(100):
            particle = Dot(
                point=np.array([
                    random.uniform(-7, 7),
                    random.uniform(-4, 4),
                    0
                ]),
                radius=random.uniform(0.02, 0.05),
                color=random.choice([
                    PHOTON_YELLOW, WAVE_BLUE, QUANTUM_PURPLE, ENERGY_RED
                ])
            )
            particles.add(particle)

        self.play(FadeIn(particles))
        self.play(
            *[particle.animate.shift(
                random.uniform(-2, 2) * RIGHT +
                random.uniform(-1, 1) * UP
            ) for particle in particles],
            run_time=3
        )

        self.wait(3)
        self.play(FadeOut(VGroup(
            outro_title, wave_particle, measurement_effect,
            uncertainty, final_message, particles
        )))

        # 最终的致谢画面
        thanks = Text(
            "感谢观看",
            font_size=72,
            color=WHITE,
            font="STSong"
        )
        self.play(Write(thanks))
        self.wait(3)