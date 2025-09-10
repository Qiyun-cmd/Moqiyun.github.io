from manim import *
import numpy as np
import random
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from my_manim_setup import *
class PeriodicTableOrigins(Scene):
    def construct(self):
        # 设置背景为深空黑
        self.camera.background_color = "#000000"
        
        # 第一幕：宇宙大爆炸
        self.big_bang_scene()
        
        # 第二幕：原子的形成
        self.atom_formation_scene()
        
        # 第三幕：元素的诞生
        self.element_birth_scene()
        
        # 第四幕：门捷列夫的发现
        self.mendeleev_discovery_scene()
        
        # 第五幕：现代周期表的形成
        self.modern_periodic_table_scene()
    
    def big_bang_scene(self):
        # 标题
        title = Text("元素周期表的起源", font_size=48, color=WHITE)
        subtitle = Text("从宇宙大爆炸到科学发现", font_size=24, color=GREY)
        subtitle.next_to(title, DOWN)
        title_group = VGroup(title, subtitle)
        
        self.play(Write(title), Write(subtitle), run_time=2)
        self.wait(1)
        self.play(FadeOut(title_group))
        
        # 大爆炸点
        bang_point = Dot(radius=0.05, color=WHITE)
        self.play(FadeIn(bang_point))
        
        # 爆炸效果
        explosion_circles = []
        for i in range(20):
            circle = Circle(
                radius=0.1,
                color=random.choice([YELLOW, ORANGE, RED, WHITE]),
                fill_opacity=0.8,
                stroke_width=0
            )
            explosion_circles.append(circle)
        
        explosion_group = VGroup(*explosion_circles)
        explosion_group.move_to(ORIGIN)
        
        # 爆炸动画
        self.play(
            bang_point.animate.scale(50).set_opacity(0),
            *[circle.animate.scale(random.uniform(20, 40)).move_to(
                np.array([
                    random.uniform(-7, 7),
                    random.uniform(-4, 4),
                    0
                ])
            ).set_opacity(0) for circle in explosion_circles],
            run_time=3,
            rate_func=rush_from
        )
        
        # 宇宙背景
        stars = VGroup()
        for _ in range(100):
            star = Dot(
                radius=random.uniform(0.01, 0.03),
                color=WHITE,
                fill_opacity=random.uniform(0.3, 1)
            ).move_to(np.array([
                random.uniform(-8, 8),
                random.uniform(-4.5, 4.5),
                0
            ]))
            stars.add(star)
        
        self.play(FadeIn(stars), run_time=2)
        
        # 显示时间
        time_text = Text("138亿年前", font_size=36, color=YELLOW)
        time_text.to_edge(UP)
        self.play(Write(time_text))
        self.wait(1)
        self.play(FadeOut(time_text), FadeOut(stars))
    
    def atom_formation_scene(self):
        # 标题
        title = Text("第一批原子的形成", font_size=36, color=WHITE)
        title.to_edge(UP)
        self.play(Write(title))
        
        # 创建质子、中子、电子
        def create_particle(color, label):
            particle = VGroup(
                Circle(radius=0.2, color=color, fill_opacity=0.8),
                Text(label, font_size=16, color=WHITE)
            )
            particle[1].move_to(particle[0])
            return particle
        
        # 基本粒子
        proton = create_particle(RED, "p+")
        neutron = create_particle(BLUE, "n")
        electron = create_particle(GREEN, "e-")
        
        particles = VGroup(proton, neutron, electron)
        particles.arrange(RIGHT, buff=2)
        particles.move_to(ORIGIN)
        
        # 粒子标签
        labels = VGroup(
            Text("质子", font_size=20, color=RED).next_to(proton, DOWN),
            Text("中子", font_size=20, color=BLUE).next_to(neutron, DOWN),
            Text("电子", font_size=20, color=GREEN).next_to(electron, DOWN)
        )
        
        self.play(
            *[FadeIn(p) for p in particles],
            *[Write(l) for l in labels],
            run_time=2
        )
        self.wait(1)
        
        # 粒子运动和碰撞
        self.play(
            particles.animate.move_to(ORIGIN),
            labels.animate.set_opacity(0),
            run_time=1
        )
        
        # 形成氢原子
        hydrogen_nucleus = VGroup(
            Circle(radius=0.3, color=RED, fill_opacity=0.8),
            Text("H", font_size=24, color=WHITE)
        )
        hydrogen_nucleus[1].move_to(hydrogen_nucleus[0])
        
        # 电子轨道
        electron_orbit = Circle(radius=1, color=GREEN, stroke_width=1)
        electron_dot = Dot(radius=0.1, color=GREEN).move_to(electron_orbit.get_start())
        
        hydrogen_atom = VGroup(hydrogen_nucleus, electron_orbit, electron_dot)
        
        # 破碎重组动画
        self.play(
            Transform(particles, hydrogen_nucleus),
            Create(electron_orbit),
            FadeIn(electron_dot),
            run_time=2
        )
        
        # 电子绕核运动
        def electron_updater(mob, dt):
            mob.rotate(2 * dt, about_point=ORIGIN)
        
        electron_dot.add_updater(electron_updater)
        
        hydrogen_label = Text("氢原子 (H)", font_size=24, color=WHITE).next_to(hydrogen_atom, DOWN, buff=1)
        self.play(Write(hydrogen_label))
        self.wait(2)
        
        electron_dot.remove_updater(electron_updater)
        
        # 形成氦原子
        helium_nucleus = VGroup(
            Circle(radius=0.4, color=PURPLE, fill_opacity=0.8),
            Text("He", font_size=24, color=WHITE)
        )
        helium_nucleus[1].move_to(helium_nucleus[0])
        
        helium_orbit = Circle(radius=1.2, color=GREEN, stroke_width=1)
        electron1 = Dot(radius=0.1, color=GREEN).move_to(helium_orbit.get_start())
        electron2 = Dot(radius=0.1, color=GREEN).move_to(helium_orbit.get_start()).rotate(PI, about_point=ORIGIN)
        
        helium_atom = VGroup(helium_nucleus, helium_orbit, electron1, electron2)
        helium_atom.shift(RIGHT * 3)
        
        helium_label = Text("氦原子 (He)", font_size=24, color=WHITE).next_to(helium_atom, DOWN, buff=1)
        
        self.play(
            hydrogen_atom.animate.shift(LEFT * 3),
            hydrogen_label.animate.shift(LEFT * 3),
            FadeIn(helium_atom),
            Write(helium_label),
            run_time=2
        )
        
        self.wait(1)
        self.play(
            FadeOut(VGroup(hydrogen_atom, hydrogen_label, helium_atom, helium_label, title)),
            run_time=1
        )
    
    def element_birth_scene(self):
        # 恒星内部核聚变
        title = Text("恒星熔炉：重元素的诞生", font_size=36, color=WHITE)
        title.to_edge(UP)
        self.play(Write(title))
        
        # 创建恒星
        star_core = Circle(radius=2, color=YELLOW, fill_opacity=0.9)
        star_glow = Circle(radius=2.5, color=ORANGE, fill_opacity=0.3)
        star = VGroup(star_glow, star_core)
        
        self.play(FadeIn(star), run_time=2)
        
        # 核聚变反应
        fusion_particles = []
        for i in range(20):
            particle = Dot(
                radius=0.1,
                color=random.choice([RED, YELLOW, WHITE])
            ).move_to(star_core.get_center() + np.array([
                random.uniform(-1.5, 1.5),
                random.uniform(-1.5, 1.5),
                0
            ]))
            fusion_particles.append(particle)
        
        # 粒子运动
        def particle_updater(particle):
            def update(mob, dt):
                # 向中心运动
                direction = star_core.get_center() - mob.get_center()
                if np.linalg.norm(direction) > 0.1:
                    mob.shift(direction * 0.5 * dt)
                else:
                    # 到达中心后随机位置
                    mob.move_to(star_core.get_center() + np.array([
                        random.uniform(-1.5, 1.5),
                        random.uniform(-1.5, 1.5),
                        0
                    ]))
            return update
        
        for particle in fusion_particles:
            self.add(particle)
            particle.add_updater(particle_updater(particle))
        
        # 元素符号螺旋上升
        elements = ["C", "N", "O", "Ne", "Mg", "Si", "S", "Fe"]
        element_texts = []
        
        for i, element in enumerate(elements):
            text = Text(element, font_size=30, color=WHITE)
            angle = i * TAU / len(elements)
            radius = 3
            text.move_to(np.array([
                radius * np.cos(angle),
                radius * np.sin(angle) - 5,
                0
            ]))
            element_texts.append(text)
        
        # 螺旋上升动画
        for i, text in enumerate(element_texts):
            self.play(
                text.animate.shift(UP * 8).rotate(TAU).set_opacity(0),
                run_time=3,
                rate_func=linear
            )
            if i < len(element_texts) - 1:
                self.add(element_texts[i + 1])
        
        # 超新星爆炸
        self.wait(1)
        
        explosion_text = Text("超新星爆炸！", font_size=48, color=RED)
        explosion_text.move_to(star.get_center())
        
        # 移除更新器
        for particle in fusion_particles:
            particle.clear_updaters()
        
        # 爆炸效果
        self.play(
            star_core.animate.scale(3).set_opacity(0),
            star_glow.animate.scale(5).set_opacity(0),
            *[particle.animate.move_to(
                particle.get_center() + np.array([
                    random.uniform(-8, 8),
                    random.uniform(-4, 4),
                    0
                ])
            ).set_opacity(0) for particle in fusion_particles],
            Write(explosion_text),
            run_time=2,
            rate_func=rush_from
        )
        
        self.play(FadeOut(explosion_text), FadeOut(title))
    
    def mendeleev_discovery_scene(self):
        # 门捷列夫场景
        title = Text("1869年：门捷列夫的发现", font_size=36, color=WHITE)
        title.to_edge(UP)
        self.play(Write(title))
        
        # 创建卡片
        element_cards = []
        card_data = [
            {"symbol": "H", "mass": "1", "color": BLUE},
            {"symbol": "Li", "mass": "7", "color": RED},
            {"symbol": "Be", "mass": "9", "color": GREEN},
            {"symbol": "B", "mass": "11", "color": YELLOW},
            {"symbol": "C", "mass": "12", "color": PURPLE},
            {"symbol": "N", "mass": "14", "color": ORANGE},
            {"symbol": "O", "mass": "16", "color": TEAL},
            {"symbol": "F", "mass": "19", "color": PINK},
        ]
        
        for i, data in enumerate(card_data):
            card = self.create_element_card(data["symbol"], data["mass"], data["color"])
            card.move_to(np.array([
                random.uniform(-5, 5),
                random.uniform(-2, 2),
                0
            ]))
            card.rotate(random.uniform(-PI/6, PI/6))
            element_cards.append(card)
        
        cards_group = VGroup(*element_cards)
        
        # 卡片出现
        self.play(*[FadeIn(card) for card in element_cards], run_time=2)
        
        # 混乱状态
        for _ in range(2):
            animations = []
            for card in element_cards:
                new_pos = np.array([
                    random.uniform(-5, 5),
                    random.uniform(-2, 2),
                    0
                ])
                animations.append(card.animate.move_to(new_pos).rotate(random.uniform(-PI/4, PI/4)))
            self.play(*animations, run_time=1)
        
        # 突然的顿悟 - 闪光效果
        flash = Circle(radius=0.1, color=YELLOW, fill_opacity=1)
        self.play(
            flash.animate.scale(100).set_opacity(0),
            run_time=0.5,
            rate_func=rush_from
        )
        
        # 卡片自动排列
        arranged_positions = []
        for i in range(len(element_cards)):
            row = i // 4
            col = i % 4
            pos = np.array([col * 1.5 - 2.25, -row * 1.5 + 1, 0])
            arranged_positions.append(pos)
        
        # 排列动画
        self.play(
            *[card.animate.move_to(pos).set_rotation(0) 
              for card, pos in zip(element_cards, arranged_positions)],
            run_time=2,
            rate_func=smooth
        )
        
        # 显示规律
        pattern_text = Text("原子量递增的规律！", font_size=28, color=YELLOW)
        pattern_text.next_to(cards_group, DOWN, buff=1)
        self.play(Write(pattern_text))
        
        self.wait(2)
        self.play(
            FadeOut(cards_group),
            FadeOut(pattern_text),
            FadeOut(title)
        )
    
    def modern_periodic_table_scene(self):
        # 现代周期表的形成
        title = Text("现代元素周期表", font_size=42, color=WHITE)
        title.to_edge(UP)
        self.play(Write(title))
        
        # 创建简化的周期表框架
        table_width = 12
        table_height = 6
        
        # 创建网格线
        grid_lines = VGroup()
        
        # 横线
        for i in range(8):
            line = Line(
                start=np.array([-table_width/2, table_height/2 - i * table_height/7, 0]),
                end=np.array([table_width/2, table_height/2 - i * table_height/7, 0]),
                stroke_width=1,
                color=GREY
            )
            grid_lines.add(line)
        
        # 竖线
        for i in range(19):
            line = Line(
                start=np.array([-table_width/2 + i * table_width/18, table_height/2, 0]),
                end=np.array([-table_width/2 + i * table_width/18, -table_height/2, 0]),
                stroke_width=1,
                color=GREY
            )
            grid_lines.add(line)
        
        # 网格破碎效果
        broken_pieces = []
        for line in grid_lines:
            # 将每条线分成几段
            pieces = self.break_line_into_pieces(line, 3)
            broken_pieces.extend(pieces)
        
        # 破碎动画
        self.play(
            *[Create(piece) for piece in broken_pieces],
            run_time=2,
            lag_ratio=0.01
        )
        
        # 重组成完整网格
        self.play(
            *[piece.animate.shift(ORIGIN) for piece in broken_pieces],
            run_time=1.5
        )
        
        # 元素填充动画
        # 创建一些代表性元素
        representative_elements = [
            {"symbol": "H", "pos": [-5.5, 2.5, 0], "color": "#FF9999"},
            {"symbol": "He", "pos": [5.5, 2.5, 0], "color": "#C0FFFF"},
            {"symbol": "Li", "pos": [-5.5, 1.5, 0], "color": "#FF9999"},
            {"symbol": "C", "pos": [-0.5, 1.5, 0], "color": "#A0FFA0"},
            {"symbol": "O", "pos": [1.5, 1.5, 0], "color": "#A0FFA0"},
            {"symbol": "Fe", "pos": [-1.5, -0.5, 0], "color": "#FFC0C0"},
            {"symbol": "Au", "pos": [0.5, -2.5, 0], "color": "#FFC0C0"},
            {"symbol": "U", "pos": [-2.5, -3.5, 0], "color": "#FF99CC"},
        ]
        
        element_blocks = []
        for elem_data in representative_elements:
            block = self.create_modern_element_block(
                elem_data["symbol"],
                elem_data["color"]
            )
            block.move_to(elem_data["pos"])
            block.scale(0)
            element_blocks.append(block)
        
        # 元素块生长动画
        for block in element_blocks:
            self.play(
                block.animate.scale(1),
                run_time=0.3,
                rate_func=there_and_back_with_pause
            )
        
        # 添加族的颜色标识
        legend_items = [
            {"name": "碱金属", "color": "#FF9999"},
            {"name": "卤素", "color": "#FFFF99"},
            {"name": "稀有气体", "color": "#C0FFFF"},
            {"name": "过渡金属", "color": "#FFC0C0"},
        ]
        
        legend = VGroup()
        for i, item in enumerate(legend_items):
            color_box = Square(side_length=0.3, fill_color=item["color"], fill_opacity=0.8)
            label = Text(item["name"], font_size=16, color=WHITE)
            label.next_to(color_box, RIGHT, buff=0.1)
            legend_item = VGroup(color_box, label)
            legend_item.shift(DOWN * i * 0.5)
            legend.add(legend_item)
        
        legend.to_edge(RIGHT).shift(UP * 0.5)
        self.play(FadeIn(legend))
        
        # 量子数显示
        quantum_text = Text("基于量子力学的现代理解", font_size=24, color=BLUE)
        quantum_text.to_edge(DOWN)
        
        # 电子轨道动画
        orbital_center = np.array([-4, -1, 0])
        s_orbital = Circle(radius=0.5, color=RED, stroke_width=2)
        p_orbital = self.create_p_orbital()
        d_orbital = self.create_d_orbital()
        
        orbitals = VGroup(s_orbital, p_orbital, d_orbital)
        orbitals.move_to(orbital_center)
        
        orbital_labels = VGroup(
            Text("s", font_size=20, color=RED).next_to(s_orbital, DOWN),
            Text("p", font_size=20, color=GREEN).next_to(p_orbital, DOWN),
            Text("d", font_size=20, color=BLUE).next_to(d_orbital, DOWN)
        )
        
        self.play(
            Write(quantum_text),
            Create(orbitals),
            Write(orbital_labels),
            run_time=2
        )
        
        # 最终的整合动画
        final_text = Text(
            "118个元素，一个统一的规律",
            font_size=32,
            color=GOLD
        )
        final_text.move_to(ORIGIN)
        
        # 所有元素向中心汇聚
        self.play(
            *[block.animate.move_to(ORIGIN).scale(0.1) for block in element_blocks],
            FadeOut(VGroup(broken_pieces)),
            FadeOut(legend),
            FadeOut(orbitals),
            FadeOut(orbital_labels),
            FadeOut(quantum_text),
            run_time=2
        )
        
        # 爆发成完整周期表
        self.play(
            Write(final_text),
            *[block.animate.move_to(
                np.array([
                    random.uniform(-6, 6),
                    random.uniform(-3, 3),
                    0
                ])
            ).scale(10).set_opacity(0) for block in element_blocks],
            run_time=2,
            rate_func=rush_from
        )
        
        self.wait(2)
        
        # 结束语
        end_text = VGroup(
            Text("从宇宙尘埃到科学瑰宝", font_size=36, color=WHITE),
            Text("元素周期表 - 自然界的密码", font_size=28, color=YELLOW)
        )
        end_text.arrange(DOWN, buff=0.5)
        
        self.play(
            Transform(final_text, end_text),
            run_time=2
        )
        
        self.wait(3)
    
    # 辅助函数
    def create_element_card(self, symbol, mass, color):
        """创建门捷列夫时代的元素卡片"""
        card = VGroup()
        
        # 卡片背景
        bg = Rectangle(
            width=1.2,
            height=1.6,
            fill_color=color,
            fill_opacity=0.8,
            stroke_color=WHITE,
            stroke_width=2
        )
        
        # 元素符号
        symbol_text = Text(symbol, font_size=36, color=WHITE, weight=BOLD)
        symbol_text.move_to(bg.get_center() + UP * 0.2)
        
        # 原子量
        mass_text = Text(mass, font_size=20, color=WHITE)
        mass_text.move_to(bg.get_center() + DOWN * 0.3)
        
        card.add(bg, symbol_text, mass_text)
        return card
    
    def create_modern_element_block(self, symbol, color):
        """创建现代元素块"""
        block = VGroup()
        
        # 方块背景
        bg = RoundedRectangle(
            width=0.6,
            height=0.6,
            corner_radius=0.05,
            fill_color=color,
            fill_opacity=0.8,
            stroke_color=WHITE,
            stroke_width=1
        )
        
        # 元素符号
        symbol_text = Text(symbol, font_size=20, color=BLACK, weight=BOLD)
        symbol_text.move_to(bg.get_center())
        
        block.add(bg, symbol_text)
        return block
    
    def break_line_into_pieces(self, line, num_pieces):
        """将线条破碎成多个片段"""
        pieces = []
        start = line.get_start()
        end = line.get_end()
        
        for i in range(num_pieces):
            piece_start = start + (end - start) * i / num_pieces
            piece_end = start + (end - start) * (i + 1) / num_pieces
            
            # 添加随机偏移
            offset = np.array([
                random.uniform(-0.2, 0.2),
                random.uniform(-0.2, 0.2),
                0
            ])
            
            piece = Line(
                start=piece_start + offset,
                end=piece_end + offset,
                stroke_width=line.stroke_width,
                color=line.color
            )
            pieces.append(piece)
        
        return pieces
    
    def create_p_orbital(self):
        """创建p轨道形状"""
        p_orbital = VGroup()
        
        # 创建哑铃形状
        lobe1 = Ellipse(width=0.3, height=0.6, color=GREEN, fill_opacity=0.5)
        lobe2 = Ellipse(width=0.3, height=0.6, color=GREEN, fill_opacity=0.5)
        
        lobe1.shift(UP * 0.3)
        lobe2.shift(DOWN * 0.3)
        
        p_orbital.add(lobe1, lobe2)
        return p_orbital
    
    def create_d_orbital(self):
        """创建d轨道形状"""
        d_orbital = VGroup()
        
        # 创建四叶草形状
        for angle in [0, PI/2, PI, 3*PI/2]:
            lobe = Ellipse(width=0.2, height=0.4, color=BLUE, fill_opacity=0.5)
            lobe.rotate(angle)
            lobe.shift(0.3 * np.array([np.cos(angle), np.sin(angle), 0]))
            d_orbital.add(lobe)
        
        return d_orbital


