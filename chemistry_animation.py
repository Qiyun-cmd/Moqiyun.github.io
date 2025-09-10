from manim import *
import numpy as np

from manim_chemistry import *

import networkx as nx

import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from my_manim_setup import *

class ComprehensiveChemistryAnimation(Scene):
    def construct(self):
        # 标题动画
        self.show_title()

        # 第一部分：化学平衡基础
        self.chemical_equilibrium_basics()

        # 第二部分：平衡常数深入
        self.equilibrium_constant_details()

        # 第三部分：有机化合物分类
        self.organic_compounds_classification()

        # 第四部分：官能团展示
        self.functional_groups_showcase()

        # 第五部分：同分异构体
        self.isomers_demonstration()

        # 第六部分：手性分子
        self.chirality_exploration()

        # 第七部分：综合反应机理
        self.comprehensive_reaction_mechanism()

        # 结尾
        self.ending_sequence()

    def show_title(self):
        # 创建渐变背景
        gradient = Rectangle(
            width=config.frame_width,
            height=config.frame_height,
            fill_opacity=1,
            fill_color=[BLUE_E, PURPLE_E, PINK]
        ).set_sheen_direction(UP)

        self.add(gradient)

        # 主标题
        title = Text("化学世界的奇妙之旅", font="STSong", font_size=72)
        subtitle = Text("从平衡到有机化学的深度探索", font="STSong", font_size=36)
        subtitle.next_to(title, DOWN, buff=0.5)

        # 装饰元素
        molecules = VGroup()
        for i in range(8):
            angle = i * TAU / 8
            mol = self.create_simple_molecule().scale(0.3)
            mol.move_to(4 * np.array([np.cos(angle), np.sin(angle), 0]))
            molecules.add(mol)

        self.play(
            Write(title),
            Create(molecules, lag_ratio=0.1),
            run_time=3
        )
        self.play(FadeIn(subtitle, shift=UP))
        self.wait(2)

        self.play(
            FadeOut(VGroup(title, subtitle, molecules)),
            gradient.animate.set_fill(opacity=0.3),
            run_time=2
        )

    def chemical_equilibrium_basics(self):
        # 章节标题
        chapter_title = Text("第一章：化学平衡的本质", font="STSong", font_size=48)
        chapter_title.to_edge(UP)
        self.play(Write(chapter_title))
        self.wait()

        # 可逆反应示例
        reaction_text = Text("可逆反应示例", font="STSong", font_size=36)
        reaction_text.next_to(chapter_title, DOWN, buff=0.5)

        # N2 + 3H2 ⇌ 2NH3 反应
        equation = MathTex(
            r"N_2", r"+", r"3H_2", r"\rightleftharpoons", r"2NH_3"
        ).scale(1.5)
        equation.next_to(reaction_text, DOWN, buff=1)

        self.play(Write(reaction_text))
        self.play(Write(equation))
        self.wait()

        # 创建分子动画
        n2_molecules = VGroup(*[self.create_n2_molecule() for _ in range(3)])
        h2_molecules = VGroup(*[self.create_h2_molecule() for _ in range(9)])
        nh3_molecules = VGroup(*[self.create_nh3_molecule() for _ in range(6)])

        # 初始位置
        reactants = VGroup(n2_molecules, h2_molecules)
        reactants.arrange(RIGHT, buff=0.5).shift(3 * LEFT)
        products = nh3_molecules.arrange_in_grid(2, 3, buff=0.3).shift(3 * RIGHT)

        # 动态平衡演示
        self.play(
            FadeIn(reactants),
            FadeIn(products),
            FadeOut(VGroup(reaction_text, equation))
        )

        # 创建平衡箭头
        forward_arrow = Arrow(LEFT, RIGHT, color=GREEN).shift(UP)
        backward_arrow = Arrow(RIGHT, LEFT, color=RED).shift(DOWN)

        self.play(
            Create(forward_arrow),
            Create(backward_arrow)
        )

        # 动态平衡动画
        for _ in range(3):
            self.play(
                reactants.animate.shift(0.5 * RIGHT),
                products.animate.shift(0.5 * LEFT),
                run_time=1
            )
            self.play(
                reactants.animate.shift(0.5 * LEFT),
                products.animate.shift(0.5 * RIGHT),
                run_time=1
            )

        # 平衡概念说明
        equilibrium_text = Text(
            "化学平衡：正逆反应速率相等的动态状态",
            font="STSong",
            font_size=32
        ).to_edge(DOWN)

        self.play(Write(equilibrium_text))
        self.wait(2)

        # 清理场景
        self.play(
            FadeOut(VGroup(
                chapter_title, reactants, products,
                forward_arrow, backward_arrow, equilibrium_text
            ))
        )

    def equilibrium_constant_details(self):
        # 章节标题
        chapter_title = Text("第二章：平衡常数的奥秘", font="STSong", font_size=48)
        chapter_title.to_edge(UP)
        self.play(Write(chapter_title))

        # 平衡常数定义
        kc_definition = MathTex(
            r"K_c = \frac{[C]^c[D]^d}{[A]^a[B]^b}"
        ).scale(1.5)

        general_equation = MathTex(
            r"aA + bB \rightleftharpoons cC + dD"
        )
        general_equation.next_to(kc_definition, UP, buff=0.5)

        VGroup(general_equation, kc_definition).move_to(ORIGIN)

        self.play(Write(general_equation))
        self.play(Write(kc_definition))
        self.wait(2)

        # 具体例子
        example_title = Text("实例分析", font="STSong", font_size=36)
        example_title.next_to(kc_definition, DOWN, buff=1)

        example_eq = MathTex(
            r"2SO_2(g) + O_2(g) \rightleftharpoons 2SO_3(g)"
        )
        example_kc = MathTex(
            r"K_c = \frac{[SO_3]^2}{[SO_2]^2[O_2]}"
        )

        example_eq.next_to(example_title, DOWN, buff=0.5)
        example_kc.next_to(example_eq, DOWN, buff=0.5)

        self.play(
            FadeOut(VGroup(general_equation, kc_definition)),
            Write(example_title)
        )
        self.play(Write(example_eq))
        self.play(Write(example_kc))

        # 温度对平衡的影响
        temp_effect = self.create_temperature_effect_graph()
        temp_effect.scale(0.8).shift(3 * RIGHT)

        temp_label = Text("温度对K的影响", font="STSong", font_size=28)
        temp_label.next_to(temp_effect, UP)

        self.play(
            VGroup(example_title, example_eq, example_kc).animate.shift(3 * LEFT),
            FadeIn(temp_effect),
            Write(temp_label)
        )
        self.wait(3)

        # 清理
        self.play(FadeOut(Group(*self.mobjects)))

    def organic_compounds_classification(self):
        # 章节标题
        chapter_title = Text("第三章：有机化合物的分类体系", font="STSong", font_size=48)
        chapter_title.to_edge(UP)
        self.play(Write(chapter_title))

        # 创建分类树
        classification_tree = self.create_organic_classification_tree()
        classification_tree.scale(0.8).move_to(ORIGIN)

        self.play(Create(classification_tree, lag_ratio=0.05), run_time=4)
        self.wait(2)

        # 烃类详细展示
        hydrocarbons_title = Text("烃类化合物", font="STSong", font_size=36)
        hydrocarbons_title.to_edge(UP).shift(DOWN)

        self.play(
            FadeOut(classification_tree),
            Transform(chapter_title, hydrocarbons_title)
        )

        # 烷烃系列
        alkanes = self.create_alkane_series()
        alkanes.arrange(RIGHT, buff=1).move_to(ORIGIN)

        self.play(Create(alkanes, lag_ratio=0.2))

        # 通式展示
        general_formula = MathTex(r"C_nH_{2n+2}").scale(1.5)
        general_formula.to_edge(DOWN).shift(UP)
        formula_label = Text("烷烃通式", font="STSong", font_size=28)
        formula_label.next_to(general_formula, UP)

        self.play(
            Write(formula_label),
            Write(general_formula)
        )
        self.wait(2)

        # 烯烃和炔烃
        self.play(FadeOut(VGroup(alkanes, general_formula, formula_label)))

        alkenes_alkynes = self.create_alkenes_alkynes_comparison()
        alkenes_alkynes.move_to(ORIGIN)

        self.play(Create(alkenes_alkynes))
        self.wait(3)

        # 清理
        self.play(FadeOut(Group(*self.mobjects)))

    def functional_groups_showcase(self):
        # 章节标题
        chapter_title = Text("第四章：官能团的世界", font="STSong", font_size=48)
        chapter_title.to_edge(UP)
        self.play(Write(chapter_title))

        # 创建官能团展示网格
        functional_groups = self.create_functional_groups_grid()
        functional_groups.scale(0.7).move_to(ORIGIN)

        # 逐个展示官能团
        for i, group in enumerate(functional_groups):
            self.play(
                FadeIn(group, scale=0.8),
                run_time=0.5
            )

        self.wait(2)

        # 官能团转化关系
        transformation_title = Text("官能团相互转化", font="STSong", font_size=36)
        transformation_title.next_to(chapter_title, DOWN, buff=0.5)

        self.play(
            functional_groups.animate.scale(0.5).to_edge(LEFT),
            Write(transformation_title)
        )

        # 创建转化流程图
        transformation_diagram = self.create_transformation_diagram()
        transformation_diagram.scale(0.8).shift(2 * RIGHT)

        self.play(Create(transformation_diagram, lag_ratio=0.1), run_time=3)
        self.wait(3)

        # 清理
        self.play(FadeOut(Group(*self.mobjects)))

    def isomers_demonstration(self):
        # 章节标题
        chapter_title = Text("第五章：同分异构现象", font="STSong", font_size=48)
        chapter_title.to_edge(UP)
        self.play(Write(chapter_title))

        # 结构异构体示例 - C4H10
        struct_title = Text("结构异构体", font="STSong", font_size=36)
        struct_title.next_to(chapter_title, DOWN, buff=0.5)

        formula = MathTex(r"C_4H_{10}").scale(1.5)
        formula.next_to(struct_title, DOWN, buff=0.5)

        self.play(Write(struct_title), Write(formula))

        # 正丁烷和异丁烷
        n_butane = self.create_n_butane()
        iso_butane = self.create_iso_butane()

        n_butane.shift(3 * LEFT)
        iso_butane.shift(3 * RIGHT)

        n_label = Text("正丁烷", font="STSong", font_size=28)
        iso_label = Text("异丁烷", font="STSong", font_size=28)

        n_label.next_to(n_butane, DOWN)
        iso_label.next_to(iso_butane, DOWN)

        self.play(
            Create(n_butane),
            Create(iso_butane),
            Write(n_label),
            Write(iso_label)
        )
        self.wait(2)

        # 立体异构体
        self.play(
            FadeOut(VGroup(
                struct_title, formula, n_butane, iso_butane,
                n_label, iso_label
            ))
        )

        stereo_title = Text("立体异构体", font="STSong", font_size=36)
        stereo_title.next_to(chapter_title, DOWN, buff=0.5)

        self.play(Write(stereo_title))

        # 顺反异构示例
        cis_trans = self.create_cis_trans_isomers()
        cis_trans.move_to(ORIGIN)

        self.play(Create(cis_trans))
        self.wait(3)

        # 清理
        self.play(FadeOut(Group(*self.mobjects)))

    def chirality_exploration(self):
        # 章节标题
        chapter_title = Text("第六章：手性分子的奥秘", font="STSong", font_size=48)
        chapter_title.to_edge(UP)
        self.play(Write(chapter_title))

        # 手性概念
        chirality_def = Text(
            "手性：物体与其镜像不能重合的性质",
            font="STSong",
            font_size=32
        )
        chirality_def.next_to(chapter_title, DOWN, buff=0.5)

        self.play(Write(chirality_def))

        # 创建手性碳示例
        chiral_carbon = self.create_chiral_carbon_3d()
        chiral_carbon.shift(3 * LEFT)

        mirror_image = self.create_chiral_carbon_3d(mirror=True)
        mirror_image.shift(3 * RIGHT)

        # 镜面
        mirror_line = DashedLine(3 * UP, 3 * DOWN, color=BLUE)
        mirror_label = Text("镜面", font="STSong", font_size=24)
        mirror_label.next_to(mirror_line, UP)

        self.play(
            Create(chiral_carbon),
            Create(mirror_image),
            Create(mirror_line),
            Write(mirror_label)
        )

        # 旋转展示不能重合
        self.play(
            Rotate(chiral_carbon, angle=PI, axis=UP),
            Rotate(mirror_image, angle=PI, axis=UP),
            run_time=3
        )

        # R/S命名法
        rs_title = Text("R/S命名体系", font="STSong", font_size=36)
        rs_title.to_edge(DOWN).shift(UP)

        self.play(Write(rs_title))

        # 优先级规则
        priority_rules = self.create_priority_rules()
        priority_rules.scale(0.8).next_to(rs_title, UP)

        self.play(Create(priority_rules))
        self.wait(3)

        # 清理
        self.play(FadeOut(Group(*self.mobjects)))

    def comprehensive_reaction_mechanism(self):
        # 章节标题
        chapter_title = Text("第七章：综合反应机理", font="STSong", font_size=48)
        chapter_title.to_edge(UP)
        self.play(Write(chapter_title))

        # SN2反应机理
        sn2_title = Text("SN2反应机理", font="STSong", font_size=36)
        sn2_title.next_to(chapter_title, DOWN, buff=0.5)

        self.play(Write(sn2_title))

        # 创建反应物
        substrate = self.create_alkyl_halide()
        nucleophile = self.create_nucleophile()

        substrate.move_to(2 * LEFT)
        nucleophile.move_to(4 * LEFT + UP)

        self.play(
            FadeIn(substrate),
            FadeIn(nucleophile)
        )

        # 过渡态
        transition_state = self.create_sn2_transition_state()
        transition_state.move_to(ORIGIN)

        # 产物
        product = self.create_sn2_product()
        leaving_group = self.create_leaving_group()

        product.move_to(2 * RIGHT)
        leaving_group.move_to(4 * RIGHT + DOWN)

        # 反应动画
        self.play(
            nucleophile.animate.move_to(substrate.get_center() + 0.5 * UP),
            run_time=1
        )

        self.play(
            Transform(VGroup(substrate, nucleophile), transition_state),
            run_time=1.5
        )

        self.play(
            ReplacementTransform(
                transition_state,
                VGroup(product, leaving_group)
            ),
            run_time=1.5
        )

        # 能量图
        energy_diagram = self.create_energy_diagram()
        energy_diagram.scale(0.6).to_edge(DOWN)

        self.play(Create(energy_diagram))
        self.wait(2)

        # 立体化学结果
        stereo_text = Text(
            "立体化学：构型翻转",
            font="STSong",
            font_size=28
        )
        stereo_text.next_to(energy_diagram, UP)

        self.play(Write(stereo_text))
        self.wait(2)

        # 清理并准备下一个反应
        self.play(FadeOut(Group(*self.mobjects)))
        self.play(Write(chapter_title))

        # E2消除反应
        e2_title = Text("E2消除反应", font="STSong", font_size=36)
        e2_title.next_to(chapter_title, DOWN, buff=0.5)

        self.play(Write(e2_title))

        # E2反应展示
        e2_mechanism = self.create_e2_mechanism()
        e2_mechanism.move_to(ORIGIN)

        self.play(Create(e2_mechanism, lag_ratio=0.1), run_time=4)

        # Zaitsev规则
        zaitsev_rule = Text(
            "Zaitsev规则：主要生成取代程度更高的烯烃",
            font="STSong",
            font_size=28
        )
        zaitsev_rule.to_edge(DOWN)

        self.play(Write(zaitsev_rule))
        self.wait(3)

        # 清理
        self.play(FadeOut(Group(*self.mobjects)))

    def ending_sequence(self):
        # 创建总结画面
        summary_title = Text("化学世界的统一性", font="STSong", font_size=56)
        summary_title.to_edge(UP)

        self.play(Write(summary_title))

        # 创建概念网络
        concept_network = self.create_concept_network()
        concept_network.scale(0.8).move_to(ORIGIN)

        self.play(Create(concept_network, lag_ratio=0.02), run_time=5)

        # 关键概念总结
        key_concepts = VGroup(
            Text("• 化学平衡是动态的过程", font="STSong", font_size=28),
            Text("• 官能团决定有机物的性质", font="STSong", font_size=28),
            Text("• 立体化学影响分子的活性", font="STSong", font_size=28),
            Text("• 反应机理揭示转化的本质", font="STSong", font_size=28)
        )
        key_concepts.arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        key_concepts.to_edge(DOWN).shift(UP)

        self.play(
            concept_network.animate.scale(0.6).to_edge(RIGHT),
            Write(key_concepts, lag_ratio=0.2),
            run_time=3
        )

        # 结束语
        ending_text = Text(
            "探索永无止境，化学创造未来",
            font="STSong",
            font_size=48,
            color=GOLD
        )
        ending_text.move_to(ORIGIN)

        self.play(
            FadeOut(VGroup(concept_network, key_concepts)),
            Write(ending_text),
            run_time=3
        )

        # 最终动画
        self.play(
            ending_text.animate.scale(1.2),
            run_time=2
        )
        self.wait(3)

    # 辅助方法
    def create_simple_molecule(self):
        """创建简单分子模型"""
        center = Dot(radius=0.2, color=BLUE)
        atoms = VGroup()
        for i in range(4):
            angle = i * TAU / 4
            atom = Dot(radius=0.15, color=RED)
            atom.move_to(0.5 * np.array([np.cos(angle), np.sin(angle), 0]))
            bond = Line(center.get_center(), atom.get_center(), color=WHITE)
            atoms.add(bond, atom)
        return VGroup(center, atoms)

    def create_n2_molecule(self):
        """创建氮气分子"""
        n1 = Circle(radius=0.3, color=BLUE, fill_opacity=0.8)
        n2 = Circle(radius=0.3, color=BLUE, fill_opacity=0.8)
        n1.shift(0.4 * LEFT)
        n2.shift(0.4 * RIGHT)

        # 三键
        bonds = VGroup()
        for i in [-0.1, 0, 0.1]:
            bond = Line(n1.get_center(), n2.get_center(), color=WHITE)
            bond.shift(i * UP)
            bonds.add(bond)

        label = MathTex("N_2").scale(0.5).next_to(VGroup(n1, n2), DOWN, buff=0.1)

        return VGroup(n1, n2, bonds, label)

    def create_h2_molecule(self):
        """创建氢气分子"""
        h1 = Circle(radius=0.2, color=WHITE, fill_opacity=0.8)
        h2 = Circle(radius=0.2, color=WHITE, fill_opacity=0.8)
        h1.shift(0.3 * LEFT)
        h2.shift(0.3 * RIGHT)

        bond = Line(h1.get_center(), h2.get_center(), color=WHITE)
        label = MathTex("H_2").scale(0.5).next_to(VGroup(h1, h2), DOWN, buff=0.1)

        return VGroup(h1, h2, bond, label)

    def create_nh3_molecule(self):
        """创建氨分子"""
        n = Circle(radius=0.3, color=BLUE, fill_opacity=0.8)

        h_atoms = VGroup()
        positions = [
            0.5 * UP + 0.3 * LEFT,
            0.5 * UP + 0.3 * RIGHT,
            0.5 * DOWN
        ]

        for pos in positions:
            h = Circle(radius=0.2, color=WHITE, fill_opacity=0.8)
            h.move_to(pos)
            bond = Line(n.get_center(), h.get_center(), color=WHITE)
            h_atoms.add(bond, h)

        label = MathTex("NH_3").scale(0.5).next_to(n, DOWN, buff=0.3)

        return VGroup(n, h_atoms, label)

    def create_temperature_effect_graph(self):
        """创建温度对平衡常数影响的图表"""
        axes = Axes(
            x_range=[0, 10, 1],
            y_range=[0, 10, 1],
            x_length=5,
            y_length=4,
            axis_config={"include_tip": True}
        )

        x_label = Text("T", font_size=24).next_to(axes.x_axis, RIGHT)
        y_label = Text("K", font_size=24).next_to(axes.y_axis, UP)

        # 放热反应曲线
        exothermic = axes.plot(
            lambda x: 10 * np.exp(-x / 3),
            color=BLUE,
            x_range=[0.1, 10]
        )
        exo_label = Text("放热反应", font="STSong", font_size=20, color=BLUE)
        exo_label.next_to(exothermic.get_end(), RIGHT)

        # 吸热反应曲线
        endothermic = axes.plot(
            lambda x: 0.5 * np.exp(x / 4),
            color=RED,
            x_range=[0, 8]
        )
        endo_label = Text("吸热反应", font="STSong", font_size=20, color=RED)
        endo_label.next_to(endothermic.get_end(), RIGHT)

        return VGroup(axes, x_label, y_label, exothermic, exo_label,
                      endothermic, endo_label)

    def create_organic_classification_tree(self):
        """创建有机化合物分类树"""
        # 根节点
        root = Text("有机化合物", font="STSong", font_size=32)
        root.to_edge(UP).shift(DOWN)

        # 第一层
        hydrocarbons = Text("烃类", font="STSong", font_size=28)
        derivatives = Text("烃的衍生物", font="STSong", font_size=28)

        hydrocarbons.move_to(3 * LEFT + UP)
        derivatives.move_to(3 * RIGHT + UP)

        # 第二层 - 烃类
        alkanes = Text("烷烃", font="STSong", font_size=24)
        alkenes = Text("烯烃", font="STSong", font_size=24)
        alkynes = Text("炔烃", font="STSong", font_size=24)
        aromatics = Text("芳烃", font="STSong", font_size=24)

        hydro_children = VGroup(alkanes, alkenes, alkynes, aromatics)
        hydro_children.arrange(RIGHT, buff=0.5).next_to(hydrocarbons, DOWN, buff=1)

        # 第二层 - 衍生物
        alcohols = Text("醇", font="STSong", font_size=24)
        ethers = Text("醚", font="STSong", font_size=24)
        aldehydes = Text("醛", font="STSong", font_size=24)
        ketones = Text("酮", font="STSong", font_size=24)
        acids = Text("酸", font="STSong", font_size=24)
        esters = Text("酯", font="STSong", font_size=24)

        deriv_children = VGroup(alcohols, ethers, aldehydes, ketones, acids, esters)
        deriv_children.arrange_in_grid(2, 3, buff=0.5).next_to(derivatives, DOWN, buff=1)

        # 连接线
        lines = VGroup()

        # 根到第一层
        lines.add(Line(root.get_bottom(), hydrocarbons.get_top(), color=GRAY))
        lines.add(Line(root.get_bottom(), derivatives.get_top(), color=GRAY))

        # 第一层到第二层
        for child in hydro_children:
            lines.add(Line(hydrocarbons.get_bottom(), child.get_top(), color=GRAY))

        for child in deriv_children:
            lines.add(Line(derivatives.get_bottom(), child.get_top(), color=GRAY))

        return VGroup(root, hydrocarbons, derivatives, hydro_children,
                      deriv_children, lines)

    def create_alkane_series(self):
        """创建烷烃系列"""
        alkanes_data = [
            ("CH_4", "甲烷"),
            ("C_2H_6", "乙烷"),
            ("C_3H_8", "丙烷"),
            ("C_4H_{10}", "丁烷")
        ]

        alkanes = VGroup()

        for formula, name in alkanes_data:
            molecule = VGroup()

            # 分子式
            formula_tex = MathTex(formula).scale(0.8)

            # 中文名
            name_text = Text(name, font="STSong", font_size=24)
            name_text.next_to(formula_tex, DOWN, buff=0.2)

            # 结构简图
            if formula == "CH_4":
                struct = self.create_methane_structure()
            elif formula == "C_2H_6":
                struct = self.create_ethane_structure()
            elif formula == "C_3H_8":
                struct = self.create_propane_structure()
            else:
                struct = self.create_butane_structure()

            struct.scale(0.5).next_to(name_text, DOWN, buff=0.3)

            molecule.add(formula_tex, name_text, struct)
            alkanes.add(molecule)

        return alkanes

    def create_alkenes_alkynes_comparison(self):
        """创建烯烃和炔烃对比"""
        comparison = VGroup()

        # 标题
        alkene_title = Text("烯烃", font="STSong", font_size=32)
        alkyne_title = Text("炔烃", font="STSong", font_size=32)

        alkene_title.move_to(3 * LEFT + 2 * UP)
        alkyne_title.move_to(3 * RIGHT + 2 * UP)

        # 通式
        alkene_formula = MathTex(r"C_nH_{2n}").next_to(alkene_title, DOWN, buff=0.5)
        alkyne_formula = MathTex(r"C_nH_{2n-2}").next_to(alkyne_title, DOWN, buff=0.5)

        # 示例
        ethene = self.create_ethene_structure()
        ethyne = self.create_ethyne_structure()

        ethene.scale(0.8).next_to(alkene_formula, DOWN, buff=0.5)
        ethyne.scale(0.8).next_to(alkyne_formula, DOWN, buff=0.5)

        # 特征
        alkene_features = VGroup(
            Text("• 含有C=C双键", font="STSong", font_size=20),
            Text("• 可发生加成反应", font="STSong", font_size=20),
            Text("• 存在顺反异构", font="STSong", font_size=20)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        alkene_features.next_to(ethene, DOWN, buff=0.5)

        alkyne_features = VGroup(
            Text("• 含有C≡C三键", font="STSong", font_size=20),
            Text("• 更活泼的加成反应", font="STSong", font_size=20),
            Text("• 末端炔烃呈酸性", font="STSong", font_size=20)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        alkyne_features.next_to(ethyne, DOWN, buff=0.5)

        comparison.add(
            alkene_title, alkyne_title,
            alkene_formula, alkyne_formula,
            ethene, ethyne,
            alkene_features, alkyne_features
        )

        return comparison

    def create_functional_groups_grid(self):
        """创建官能团网格展示"""
        groups_data = [
            ("-OH", "羟基", "醇"),
            ("-O-", "醚键", "醚"),
            ("-CHO", "醛基", "醛"),
            ("C=O", "羰基", "酮"),
            ("-COOH", "羧基", "羧酸"),
            ("-COO-", "酯基", "酯"),
            ("-NH_2", "氨基", "胺"),
            ("-NO_2", "硝基", "硝基化合物"),
            ("-X", "卤素", "卤代烃")
        ]

        groups = VGroup()

        for i, (formula, name, compound_type) in enumerate(groups_data):
            group_display = VGroup()

            # 官能团结构
            if formula == "-OH":
                structure = self.create_hydroxyl_group()
            elif formula == "-O-":
                structure = self.create_ether_group()
            elif formula == "-CHO":
                structure = self.create_aldehyde_group()
            elif formula == "C=O":
                structure = self.create_ketone_group()
            elif formula == "-COOH":
                structure = self.create_carboxyl_group()
            elif formula == "-COO-":
                structure = self.create_ester_group()
            elif formula == "-NH_2":
                structure = self.create_amino_group()
            elif formula == "-NO_2":
                structure = self.create_nitro_group()
            else:
                structure = self.create_halogen_group()

            structure.scale(0.6)

            # 标签
            formula_text = MathTex(formula).scale(0.8)
            name_text = Text(name, font="STSong", font_size=20)
            type_text = Text(compound_type, font="STSong", font_size=16, color=BLUE)

            formula_text.next_to(structure, DOWN, buff=0.2)
            name_text.next_to(formula_text, DOWN, buff=0.1)
            type_text.next_to(name_text, DOWN, buff=0.1)

            group_display.add(structure, formula_text, name_text, type_text)

            # 添加边框
            box = SurroundingRectangle(group_display, color=GRAY, buff=0.2)
            group_display.add(box)

            groups.add(group_display)

        groups.arrange_in_grid(3, 3, buff=0.5)
        return groups

    def create_transformation_diagram(self):
        """创建官能团转化关系图"""
        # 节点
        alcohol = self.create_node("醇", "R-OH")
        aldehyde = self.create_node("醛", "R-CHO")
        acid = self.create_node("羧酸", "R-COOH")
        ester = self.create_node("酯", "R-COOR'")
        ketone = self.create_node("酮", "R-CO-R'")

        # 布局
        alcohol.move_to(3 * LEFT)
        aldehyde.move_to(UP)
        acid.move_to(3 * RIGHT)
        ester.move_to(DOWN)
        ketone.move_to(ORIGIN)

        nodes = VGroup(alcohol, aldehyde, acid, ester, ketone)

        # 反应箭头和条件
        arrows = VGroup()

        # 醇 → 醛
        arrow1 = CurvedArrow(
            alcohol.get_right(), aldehyde.get_left(),
            angle=-TAU / 6, color=GREEN
        )
        condition1 = Text("[O]", font_size=20).next_to(arrow1, UP, buff=0.1)

        # 醛 → 酸
        arrow2 = CurvedArrow(
            aldehyde.get_right(), acid.get_left(),
            angle=-TAU / 6, color=GREEN
        )
        condition2 = Text("[O]", font_size=20).next_to(arrow2, UP, buff=0.1)

        # 酸 → 酯
        arrow3 = CurvedArrow(
            acid.get_bottom(), ester.get_right(),
            angle=TAU / 6, color=BLUE
        )
        condition3 = Text("ROH/H+", font_size=20).next_to(arrow3, RIGHT, buff=0.1)

        # 醇 → 酮
        arrow4 = Arrow(alcohol.get_right(), ketone.get_left(), color=ORANGE)
        condition4 = Text("[O]", font_size=20).next_to(arrow4, UP, buff=0.1)

        arrows.add(arrow1, arrow2, arrow3, arrow4)
        conditions = VGroup(condition1, condition2, condition3, condition4)

        return VGroup(nodes, arrows, conditions)

    def create_node(self, name, formula):
        """创建转化图节点"""
        circle = Circle(radius=0.8, color=WHITE, fill_opacity=0.2)
        name_text = Text(name, font="STSong", font_size=24)
        formula_text = MathTex(formula).scale(0.7)

        name_text.move_to(circle.get_center() + 0.2 * UP)
        formula_text.move_to(circle.get_center() + 0.2 * DOWN)

        return VGroup(circle, name_text, formula_text)

    def create_n_butane(self):
        """创建正丁烷结构"""
        carbons = VGroup()
        for i in range(4):
            c = Circle(radius=0.2, color=BLACK, fill_opacity=0.8)
            c.move_to(i * 0.8 * RIGHT)
            carbons.add(c)

        # C-C键
        bonds = VGroup()
        for i in range(3):
            bond = Line(
                carbons[i].get_center(),
                carbons[i + 1].get_center(),
                color=WHITE
            )
            bonds.add(bond)

        # 氢原子
        hydrogens = VGroup()
        h_positions = [
            # 第一个碳
            (-0.5, 0.3), (-0.5, -0.3), (-0.3, 0),
            # 第二个碳
            (0.8, 0.3), (0.8, -0.3),
            # 第三个碳
            (1.6, 0.3), (1.6, -0.3),
            # 第四个碳
            (2.7, 0), (2.9, 0.3), (2.9, -0.3)
        ]

        for x, y in h_positions:
            h = Circle(radius=0.1, color=WHITE, fill_opacity=0.8)
            h.move_to(np.array([x, y, 0]))
            hydrogens.add(h)

        return VGroup(carbons, bonds, hydrogens)

    def create_iso_butane(self):
        """创建异丁烷结构"""
        # 中心碳
        center_c = Circle(radius=0.2, color=BLACK, fill_opacity=0.8)

        # 三个甲基
        methyl_positions = [
            0.8 * UP + 0.5 * LEFT,
            0.8 * UP + 0.5 * RIGHT,
            0.8 * DOWN
        ]

        methyls = VGroup()
        bonds = VGroup()

        for pos in methyl_positions:
            c = Circle(radius=0.2, color=BLACK, fill_opacity=0.8)
            c.move_to(pos)
            methyls.add(c)

            bond = Line(center_c.get_center(), c.get_center(), color=WHITE)
            bonds.add(bond)

        # 氢原子
        hydrogens = VGroup()
        # 中心碳上的氢
        h_center = Circle(radius=0.1, color=WHITE, fill_opacity=0.8)
        h_center.move_to(0.3 * LEFT)
        hydrogens.add(h_center)

        # 甲基上的氢
        for i, methyl in enumerate(methyls):
            for j in range(3):
                angle = j * TAU / 3 + i * TAU / 6
                h = Circle(radius=0.1, color=WHITE, fill_opacity=0.8)
                h.move_to(methyl.get_center() + 0.3 * np.array([
                    np.cos(angle), np.sin(angle), 0
                ]))
                hydrogens.add(h)

        return VGroup(center_c, methyls, bonds, hydrogens)

    def create_cis_trans_isomers(self):
        """创建顺反异构体示例"""
        # 顺式-2-丁烯
        cis_group = VGroup()

        # 双键碳
        c1_cis = Circle(radius=0.2, color=BLACK, fill_opacity=0.8)
        c2_cis = Circle(radius=0.2, color=BLACK, fill_opacity=0.8)
        c1_cis.move_to(0.4 * LEFT)
        c2_cis.move_to(0.4 * RIGHT)

        # 双键
        double_bond_cis = VGroup(
            Line(c1_cis.get_center() + 0.05 * UP, c2_cis.get_center() + 0.05 * UP),
            Line(c1_cis.get_center() + 0.05 * DOWN, c2_cis.get_center() + 0.05 * DOWN)
        )

        # 甲基
        ch3_1_cis = self.create_methyl_group().move_to(c1_cis.get_center() + 0.6 * UP + 0.3 * LEFT)
        ch3_2_cis = self.create_methyl_group().move_to(c2_cis.get_center() + 0.6 * UP + 0.3 * RIGHT)

        # 氢
        h1_cis = Circle(radius=0.1, color=WHITE, fill_opacity=0.8)
        h2_cis = Circle(radius=0.1, color=WHITE, fill_opacity=0.8)
        h1_cis.move_to(c1_cis.get_center() + 0.4 * DOWN)
        h2_cis.move_to(c2_cis.get_center() + 0.4 * DOWN)

        cis_label = Text("顺式", font="STSong", font_size=24)
        cis_label.next_to(VGroup(c1_cis, c2_cis), DOWN, buff=0.8)

        cis_group.add(
            c1_cis, c2_cis, double_bond_cis,
            ch3_1_cis, ch3_2_cis, h1_cis, h2_cis,
            cis_label
        )
        cis_group.shift(3 * LEFT)

        # 反式-2-丁烯
        trans_group = VGroup()

        # 双键碳
        c1_trans = Circle(radius=0.2, color=BLACK, fill_opacity=0.8)
        c2_trans = Circle(radius=0.2, color=BLACK, fill_opacity=0.8)
        c1_trans.move_to(0.4 * LEFT)
        c2_trans.move_to(0.4 * RIGHT)

        # 双键
        double_bond_trans = VGroup(
            Line(c1_trans.get_center() + 0.05 * UP, c2_trans.get_center() + 0.05 * UP),
            Line(c1_trans.get_center() + 0.05 * DOWN, c2_trans.get_center() + 0.05 * DOWN)
        )

        # 甲基
        ch3_1_trans = self.create_methyl_group().move_to(c1_trans.get_center() + 0.6 * UP + 0.3 * LEFT)
        ch3_2_trans = self.create_methyl_group().move_to(c2_trans.get_center() + 0.6 * DOWN + 0.3 * RIGHT)

        # 氢
        h1_trans = Circle(radius=0.1, color=WHITE, fill_opacity=0.8)
        h2_trans = Circle(radius=0.1, color=WHITE, fill_opacity=0.8)
        h1_trans.move_to(c1_trans.get_center() + 0.4 * DOWN)
        h2_trans.move_to(c2_trans.get_center() + 0.4 * UP)

        trans_label = Text("反式", font="STSong", font_size=24)
        trans_label.next_to(VGroup(c1_trans, c2_trans), DOWN, buff=0.8)

        trans_group.add(
            c1_trans, c2_trans, double_bond_trans,
            ch3_1_trans, ch3_2_trans, h1_trans, h2_trans,
            trans_label
        )
        trans_group.shift(3 * RIGHT)

        return VGroup(cis_group, trans_group)

    def create_chiral_carbon_3d(self, mirror=False):
        """创建手性碳的3D表示"""
        # 中心碳原子
        carbon = Sphere(radius=0.3, color=BLACK)

        # 四个不同的取代基
        # 使用不同颜色和大小区分
        h_atom = Sphere(radius=0.15, color=WHITE)
        cl_atom = Sphere(radius=0.25, color=GREEN)
        br_atom = Sphere(radius=0.3, color=RED_B)
        ch3_group = self.create_3d_methyl_group()

        # 四面体排列
        if not mirror:
            h_atom.move_to(np.array([0, 0, 1]))
            cl_atom.move_to(np.array([0.866, 0, -0.5]))
            br_atom.move_to(np.array([-0.433, 0.75, -0.5]))
            ch3_group.move_to(np.array([-0.433, -0.75, -0.5]))
        else:
            h_atom.move_to(np.array([0, 0, 1]))
            cl_atom.move_to(np.array([-0.866, 0, -0.5]))
            br_atom.move_to(np.array([0.433, 0.75, -0.5]))
            ch3_group.move_to(np.array([0.433, -0.75, -0.5]))

        # 键
        bonds = VGroup()
        for atom in [h_atom, cl_atom, br_atom, ch3_group]:
            bond = Line3D(
                start=carbon.get_center(),
                end=atom.get_center(),
                color=WHITE
            )
            bonds.add(bond)

        # 标签
        labels = VGroup(
            Text("H", font_size=20).next_to(h_atom, UP),
            Text("Cl", font_size=20).next_to(cl_atom, RIGHT),
            Text("Br", font_size=20).next_to(br_atom, LEFT),
            MathTex("CH_3").scale(0.7).next_to(ch3_group, DOWN)
        )

        return VGroup(carbon, h_atom, cl_atom, br_atom, ch3_group, bonds, labels)

    def create_3d_methyl_group(self):
        """创建3D甲基"""
        c = Sphere(radius=0.2, color=BLACK)
        h_atoms = VGroup()

        # 三个氢原子的四面体排列
        positions = [
            np.array([0.3, 0, 0.2]),
            np.array([-0.15, 0.26, 0.2]),
            np.array([-0.15, -0.26, 0.2])
        ]

        for pos in positions:
            h = Sphere(radius=0.1, color=WHITE)
            h.move_to(pos)
            h_atoms.add(h)

        return VGroup(c, h_atoms)

    def create_priority_rules(self):
        """创建优先级规则说明"""
        rules = VGroup()

        title = Text("CIP优先级规则", font="STSong", font_size=28)

        rule1 = Text("1. 原子序数大的优先", font="STSong", font_size=20)
        example1 = MathTex(r"Br > Cl > O > N > C > H").scale(0.8)
        example1.next_to(rule1, DOWN, buff=0.2)

        rule2 = Text("2. 相同原子看下一级", font="STSong", font_size=20)
        rule2.next_to(example1, DOWN, buff=0.4)

        rule3 = Text("3. 多重键等效处理", font="STSong", font_size=20)
        example3 = MathTex(r"C=O \rightarrow C(-O)(-O)").scale(0.8)
        example3.next_to(rule3, DOWN, buff=0.2)
        rule3.next_to(rule2, DOWN, buff=0.4)

        rules.add(title, rule1, example1, rule2, rule3, example3)
        rules.arrange(DOWN, aligned_edge=LEFT, buff=0.3)

        return rules

    def create_alkyl_halide(self):
        """创建卤代烷"""
        # 中心碳
        carbon = Circle(radius=0.25, color=BLACK, fill_opacity=0.8)

        # 溴原子（离去基团）
        br = Circle(radius=0.3, color=RED_B, fill_opacity=0.8)
        br.move_to(0.6 * RIGHT)
        br_label = Text("Br", font_size=20, color=WHITE).move_to(br.get_center())

        # 三个氢
        h_positions = [0.5 * UP, 0.5 * DOWN + 0.3 * LEFT, 0.5 * DOWN + 0.3 * RIGHT]
        hydrogens = VGroup()
        for pos in h_positions:
            h = Circle(radius=0.15, color=WHITE, fill_opacity=0.8)
            h.move_to(pos)
            hydrogens.add(h)

        # 键
        bonds = VGroup()
        c_br_bond = Line(carbon.get_center(), br.get_center(), color=WHITE)
        bonds.add(c_br_bond)

        for h in hydrogens:
            bond = Line(carbon.get_center(), h.get_center(), color=WHITE)
            bonds.add(bond)

        return VGroup(carbon, br, br_label, hydrogens, bonds)

    def create_nucleophile(self):
        """创建亲核试剂"""
        # 氢氧根离子
        oxygen = Circle(radius=0.25, color=RED, fill_opacity=0.8)
        o_label = MathTex("O^-").scale(0.8).move_to(oxygen.get_center())

        hydrogen = Circle(radius=0.15, color=WHITE, fill_opacity=0.8)
        hydrogen.move_to(oxygen.get_center() + 0.5 * RIGHT)

        bond = Line(oxygen.get_center(), hydrogen.get_center(), color=WHITE)

        # 孤对电子
        electrons = VGroup()
        for angle in [PI / 3, 2 * PI / 3, 4 * PI / 3, 5 * PI / 3]:
            e_pair = VGroup(
                Dot(radius=0.05, color=YELLOW),
                Dot(radius=0.05, color=YELLOW)
            ).arrange(RIGHT, buff=0.05)
            e_pair.move_to(oxygen.get_center() + 0.3 * np.array([
                np.cos(angle), np.sin(angle), 0
            ]))
            electrons.add(e_pair)

        return VGroup(oxygen, o_label, hydrogen, bond, electrons)

    def create_sn2_transition_state(self):
        """创建SN2过渡态"""
        # 中心碳
        carbon = Circle(radius=0.25, color=BLACK, fill_opacity=0.8)

        # 进攻的OH和离去的Br在一条直线上
        oh_group = VGroup(
            Circle(radius=0.2, color=RED, fill_opacity=0.6),
            Circle(radius=0.1, color=WHITE, fill_opacity=0.6)
        ).arrange(RIGHT, buff=0.1)
        oh_group.move_to(1.2 * LEFT)

        br = Circle(radius=0.3, color=RED_B, fill_opacity=0.6)
        br.move_to(1.2 * RIGHT)
        br_label = Text("Br", font_size=20, color=WHITE).move_to(br.get_center())

        # 虚线表示部分键
        dashed_bond1 = DashedLine(
            oh_group.get_right(), carbon.get_left(),
            color=WHITE, dash_length=0.1
        )
        dashed_bond2 = DashedLine(
            carbon.get_right(), br.get_left(),
            color=WHITE, dash_length=0.1
        )

        # 三个氢在同一平面
        h_positions = [0.5 * UP, 0.5 * DOWN + 0.3 * LEFT, 0.5 * DOWN + 0.3 * RIGHT]
        hydrogens = VGroup()
        bonds = VGroup()

        for pos in h_positions:
            h = Circle(radius=0.15, color=WHITE, fill_opacity=0.8)
            h.move_to(pos)
            hydrogens.add(h)
            bond = Line(carbon.get_center(), h.get_center(), color=WHITE)
            bonds.add(bond)

        # 过渡态符号
        ts_symbol = MathTex(r"\ddagger").scale(1.5).next_to(carbon, UP, buff=0.5)

        return VGroup(
            carbon, oh_group, br, br_label,
            dashed_bond1, dashed_bond2,
            hydrogens, bonds, ts_symbol
        )

    def create_sn2_product(self):
        """创建SN2产物"""
        # 中心碳
        carbon = Circle(radius=0.25, color=BLACK, fill_opacity=0.8)

        # OH基团
        oh_group = VGroup(
            Circle(radius=0.2, color=RED, fill_opacity=0.8),
            Circle(radius=0.1, color=WHITE, fill_opacity=0.8)
        ).arrange(RIGHT, buff=0.1)
        oh_group.move_to(0.6 * LEFT)

        # 三个氢（注意构型翻转）
        h_positions = [0.5 * DOWN, 0.5 * UP + 0.3 * LEFT, 0.5 * UP + 0.3 * RIGHT]
        hydrogens = VGroup()
        bonds = VGroup()

        # C-OH键
        c_oh_bond = Line(carbon.get_center(), oh_group.get_right(), color=WHITE)
        bonds.add(c_oh_bond)

        for pos in h_positions:
            h = Circle(radius=0.15, color=WHITE, fill_opacity=0.8)
            h.move_to(pos)
            hydrogens.add(h)
            bond = Line(carbon.get_center(), h.get_center(), color=WHITE)
            bonds.add(bond)

        return VGroup(carbon, oh_group, hydrogens, bonds)

    def create_leaving_group(self):
        """创建离去基团"""
        # 溴离子
        br = Circle(radius=0.3, color=RED_B, fill_opacity=0.8)
        br_label = MathTex("Br^-").move_to(br.get_center())

        # 孤对电子
        electrons = VGroup()
        for angle in np.linspace(0, 2 * PI, 8, endpoint=False):
            e = Dot(radius=0.05, color=YELLOW)
            e.move_to(br.get_center() + 0.4 * np.array([
                np.cos(angle), np.sin(angle), 0
            ]))
            electrons.add(e)

        return VGroup(br, br_label, electrons)

    def create_energy_diagram(self):
        """创建能量图"""
        axes = Axes(
            x_range=[0, 10, 1],
            y_range=[0, 10, 1],
            x_length=8,
            y_length=4,
            axis_config={"include_tip": False}
        )

        # 坐标轴标签
        x_label = Text("反应进程", font="STSong", font_size=20)
        x_label.next_to(axes.x_axis, DOWN)
        y_label = Text("能量", font="STSong", font_size=20)
        y_label.next_to(axes.y_axis, LEFT).rotate(PI / 2)

        # SN2能量曲线
        curve = axes.plot(
            lambda x: 2 + 6 * np.exp(-((x - 5) ** 2) / 2),
            x_range=[0, 10],
            color=BLUE
        )

        # 标记
        reactants_level = DashedLine(
            axes.c2p(0, 2), axes.c2p(2, 2),
            color=GRAY
        )
        products_level = DashedLine(
            axes.c2p(8, 2), axes.c2p(10, 2),
            color=GRAY
        )
        ts_point = Dot(axes.c2p(5, 8), color=RED)

        # 标签
        reactants_label = Text("反应物", font="STSong", font_size=16)
        reactants_label.next_to(reactants_level, LEFT)

        products_label = Text("产物", font="STSong", font_size=16)
        products_label.next_to(products_level, RIGHT)

        ts_label = Text("过渡态", font="STSong", font_size=16)
        ts_label.next_to(ts_point, UP)

        # 活化能
        ea_arrow = DoubleArrow(
            axes.c2p(1, 2), axes.c2p(1, 8),
            color=GREEN,
            buff=0
        )
        ea_label = MathTex("E_a").next_to(ea_arrow, LEFT)

        return VGroup(
            axes, x_label, y_label, curve,
            reactants_level, products_level, ts_point,
            reactants_label, products_label, ts_label,
            ea_arrow, ea_label
        )

    def create_e2_mechanism(self):
        """创建E2消除机理"""
        # 反应物
        substrate = VGroup()

        # 碳骨架
        c1 = Circle(radius=0.25, color=BLACK, fill_opacity=0.8)
        c2 = Circle(radius=0.25, color=BLACK, fill_opacity=0.8)
        c1.move_to(LEFT)
        c2.move_to(RIGHT)

        # C-C键
        cc_bond = Line(c1.get_center(), c2.get_center(), color=WHITE)

        # 离去基团Br
        br = Circle(radius=0.3, color=RED_B, fill_opacity=0.8)
        br.move_to(c2.get_center() + RIGHT)
        br_label = Text("Br", color=WHITE, font_size=20).move_to(br.get_center())

        # β氢
        h_beta = Circle(radius=0.15, color=WHITE, fill_opacity=0.8)
        h_beta.move_to(c1.get_center() + 0.5 * DOWN)

        # 其他氢
        other_h = VGroup()
        h_positions = [
            c1.get_center() + 0.5 * UP,
            c1.get_center() + 0.5 * LEFT,
            c2.get_center() + 0.5 * UP,
            c2.get_center() + 0.5 * DOWN
        ]

        for pos in h_positions:
            h = Circle(radius=0.15, color=WHITE, fill_opacity=0.8)
            h.move_to(pos)
            other_h.add(h)

        # 碱
        base = VGroup(
            Circle(radius=0.2, color=BLUE, fill_opacity=0.8),
            MathTex("B^-").scale(0.8)
        )
        base[1].move_to(base[0].get_center())
        base.move_to(h_beta.get_center() + 1.5 * DOWN)

        substrate.add(c1, c2, cc_bond, br, br_label, h_beta, other_h, base)

        # 过渡态箭头
        arrow1 = CurvedArrow(
            base.get_top(), h_beta.get_bottom(),
            angle=-TAU / 8, color=GREEN
        )
        arrow2 = CurvedArrow(
            c1.get_center(), c2.get_center(),
            angle=TAU / 8, color=BLUE
        ).shift(0.3 * UP)
        arrow3 = CurvedArrow(
            c2.get_center(), br.get_center(),
            angle=-TAU / 8, color=RED
        ).shift(0.3 * DOWN)

        # 产物
        product = VGroup()

        # 双键碳
        c1_prod = Circle(radius=0.25, color=BLACK, fill_opacity=0.8)
        c2_prod = Circle(radius=0.25, color=BLACK, fill_opacity=0.8)
        c1_prod.move_to(LEFT)
        c2_prod.move_to(RIGHT)

        # C=C双键
        double_bond = VGroup(
            Line(c1_prod.get_center() + 0.1 * UP, c2_prod.get_center() + 0.1 * UP),
            Line(c1_prod.get_center() + 0.1 * DOWN, c2_prod.get_center() + 0.1 * DOWN)
        )

        # 剩余的氢
        remaining_h = VGroup()
        h_positions_prod = [
            c1_prod.get_center() + 0.5 * UP,
            c1_prod.get_center() + 0.5 * LEFT,
            c2_prod.get_center() + 0.5 * UP,
            c2_prod.get_center() + 0.5 * DOWN
        ]

        for pos in h_positions_prod:
            h = Circle(radius=0.15, color=WHITE, fill_opacity=0.8)
            h.move_to(pos)
            remaining_h.add(h)

        product.add(c1_prod, c2_prod, double_bond, remaining_h)
        product.shift(5 * RIGHT)

        # HBr
        hbr = VGroup(
            MathTex("HBr").scale(1.2),
            Text("+", font_size=30).shift(0.5 * LEFT)
        )
        hbr.next_to(product, DOWN, buff=0.5)

        # 反应箭头
        reaction_arrow = Arrow(
            substrate.get_right() + 0.5 * RIGHT,
            product.get_left() - 0.5 * LEFT,
            color=WHITE
        )

        return VGroup(
            substrate, arrow1, arrow2, arrow3,
            reaction_arrow, product, hbr
        )

    def create_concept_network(self):
        """创建概念网络图"""
        # 使用networkx创建图
        G = nx.Graph()

        # 添加节点
        concepts = [
            "化学平衡", "平衡常数", "反应速率",
            "有机化合物", "官能团", "异构体",
            "反应机理", "立体化学", "手性",
            "烃类", "衍生物", "取代反应",
            "消除反应", "加成反应", "氧化还原"
        ]

        G.add_nodes_from(concepts)

        # 添加边（概念之间的联系）
        connections = [
            ("化学平衡", "平衡常数"),
            ("化学平衡", "反应速率"),
            ("有机化合物", "官能团"),
            ("有机化合物", "异构体"),
            ("有机化合物", "烃类"),
            ("有机化合物", "衍生物"),
            ("异构体", "立体化学"),
            ("立体化学", "手性"),
            ("反应机理", "取代反应"),
            ("反应机理", "消除反应"),
            ("反应机理", "加成反应"),
            ("官能团", "氧化还原"),
            ("烃类", "加成反应"),
            ("衍生物", "取代反应")
        ]

        G.add_edges_from(connections)

        # 使用spring布局
        pos = nx.spring_layout(G, k=2, iterations=50)

        # 创建Manim对象
        network = VGroup()

        # 创建节点
        node_objects = {}
        for node, position in pos.items():
            # 缩放位置
            x, y = position[0] * 5, position[1] * 3

            # 节点圆圈
            circle = Circle(
                radius=0.6,
                color=self.get_node_color(node),
                fill_opacity=0.3
            )
            circle.move_to(np.array([x, y, 0]))

            # 节点文本
            text = Text(node, font="STSong", font_size=16)
            text.move_to(circle.get_center())

            node_group = VGroup(circle, text)
            node_objects[node] = node_group
            network.add(node_group)

        # 创建边
        for edge in G.edges():
            node1, node2 = edge
            start = node_objects[node1].get_center()
            end = node_objects[node2].get_center()

            line = Line(start, end, color=GRAY, stroke_width=2)
            network.add(line)

            # 将线移到节点后面
            line.z_index = -1

        return network

    def get_node_color(self, node_name):
        """根据节点类型返回颜色"""
        color_map = {
            "化学平衡": BLUE,
            "平衡常数": BLUE_B,
            "反应速率": BLUE_D,
            "有机化合物": GREEN,
            "官能团": GREEN_B,
            "异构体": GREEN_D,
            "反应机理": RED,
            "立体化学": PURPLE,
            "手性": PURPLE_B,
            "烃类": ORANGE,
            "衍生物": YELLOW,
            "取代反应": RED_B,
            "消除反应": RED_C,
            "加成反应": RED_D,
            "氧化还原": PINK
        }
        return color_map.get(node_name, WHITE)

    # 辅助方法：创建各种分子结构
    def create_methane_structure(self):
        """创建甲烷结构"""
        c = Circle(radius=0.2, color=BLACK, fill_opacity=0.8)
        h_atoms = VGroup()

        # 四面体顶点
        positions = [
            0.4 * UP, 0.4 * DOWN + 0.3 * LEFT,
            0.4 * DOWN + 0.3 * RIGHT, 0.4 * LEFT
        ]

        for pos in positions:
            h = Circle(radius=0.1, color=WHITE, fill_opacity=0.8)
            h.move_to(pos)
            bond = Line(c.get_center(), h.get_center(), color=WHITE)
            h_atoms.add(bond, h)

        return VGroup(c, h_atoms)

    def create_ethane_structure(self):
        """创建乙烷结构"""
        c1 = Circle(radius=0.2, color=BLACK, fill_opacity=0.8)
        c2 = Circle(radius=0.2, color=BLACK, fill_opacity=0.8)
        c1.move_to(0.4 * LEFT)
        c2.move_to(0.4 * RIGHT)

        cc_bond = Line(c1.get_center(), c2.get_center(), color=WHITE)

        h_atoms = VGroup()
        # C1的氢
        for angle in [PI / 3, PI, 5 * PI / 3]:
            h = Circle(radius=0.1, color=WHITE, fill_opacity=0.8)
            h.move_to(c1.get_center() + 0.3 * np.array([
                np.cos(angle), np.sin(angle), 0
            ]))
            bond = Line(c1.get_center(), h.get_center(), color=WHITE)
            h_atoms.add(bond, h)

        # C2的氢
        for angle in [0, 2 * PI / 3, 4 * PI / 3]:
            h = Circle(radius=0.1, color=WHITE, fill_opacity=0.8)
            h.move_to(c2.get_center() + 0.3 * np.array([
                np.cos(angle), np.sin(angle), 0
            ]))
            bond = Line(c2.get_center(), h.get_center(), color=WHITE)
            h_atoms.add(bond, h)

        return VGroup(c1, c2, cc_bond, h_atoms)

    def create_propane_structure(self):
        """创建丙烷结构"""
        carbons = VGroup()
        for i in range(3):
            c = Circle(radius=0.2, color=BLACK, fill_opacity=0.8)
            c.move_to(i * 0.8 * RIGHT - 0.8 * RIGHT)
            carbons.add(c)

        bonds = VGroup()
        for i in range(2):
            bond = Line(
                carbons[i].get_center(),
                carbons[i + 1].get_center(),
                color=WHITE
            )
            bonds.add(bond)

        h_atoms = VGroup()
        # 端碳的氢（各3个）
        for i in [0, 2]:
            if i == 0:
                angles = [2 * PI / 3, PI, 4 * PI / 3]
            else:
                angles = [0, PI / 3, 5 * PI / 3]

            for angle in angles:
                h = Circle(radius=0.1, color=WHITE, fill_opacity=0.8)
                h.move_to(carbons[i].get_center() + 0.3 * np.array([
                    np.cos(angle), np.sin(angle), 0
                ]))
                bond = Line(carbons[i].get_center(), h.get_center(), color=WHITE)
                h_atoms.add(bond, h)

        # 中间碳的氢（2个）
        for angle in [PI / 2, 3 * PI / 2]:
            h = Circle(radius=0.1, color=WHITE, fill_opacity=0.8)
            h.move_to(carbons[1].get_center() + 0.3 * np.array([
                np.cos(angle), np.sin(angle), 0
            ]))
            bond = Line(carbons[1].get_center(), h.get_center(), color=WHITE)
            h_atoms.add(bond, h)

        return VGroup(carbons, bonds, h_atoms)

    def create_butane_structure(self):
        """创建丁烷结构"""
        return self.create_n_butane().scale(0.8)

    def create_ethene_structure(self):
        """创建乙烯结构"""
        c1 = Circle(radius=0.2, color=BLACK, fill_opacity=0.8)
        c2 = Circle(radius=0.2, color=BLACK, fill_opacity=0.8)
        c1.move_to(0.4 * LEFT)
        c2.move_to(0.4 * RIGHT)

        # 双键
        double_bond = VGroup(
            Line(c1.get_center() + 0.05 * UP, c2.get_center() + 0.05 * UP),
            Line(c1.get_center() + 0.05 * DOWN, c2.get_center() + 0.05 * DOWN)
        )

        # 氢原子
        h_atoms = VGroup()
        h_positions = [
            c1.get_center() + 0.4 * UP + 0.2 * LEFT,
            c1.get_center() + 0.4 * DOWN + 0.2 * LEFT,
            c2.get_center() + 0.4 * UP + 0.2 * RIGHT,
            c2.get_center() + 0.4 * DOWN + 0.2 * RIGHT
        ]

        for pos in h_positions:
            h = Circle(radius=0.1, color=WHITE, fill_opacity=0.8)
            h.move_to(pos)
            h_atoms.add(h)

        return VGroup(c1, c2, double_bond, h_atoms)

    def create_ethyne_structure(self):
        """创建乙炔结构"""
        c1 = Circle(radius=0.2, color=BLACK, fill_opacity=0.8)
        c2 = Circle(radius=0.2, color=BLACK, fill_opacity=0.8)
        c1.move_to(0.4 * LEFT)
        c2.move_to(0.4 * RIGHT)

        # 三键
        triple_bond = VGroup(
            Line(c1.get_center(), c2.get_center()),
            Line(c1.get_center() + 0.08 * UP, c2.get_center() + 0.08 * UP),
            Line(c1.get_center() + 0.08 * DOWN, c2.get_center() + 0.08 * DOWN)
        )

        # 氢原子
        h1 = Circle(radius=0.1, color=WHITE, fill_opacity=0.8)
        h2 = Circle(radius=0.1, color=WHITE, fill_opacity=0.8)
        h1.move_to(c1.get_center() + 0.5 * LEFT)
        h2.move_to(c2.get_center() + 0.5 * RIGHT)

        return VGroup(c1, c2, triple_bond, h1, h2)

    def create_methyl_group(self):
        """创建甲基"""
        c = Circle(radius=0.15, color=BLACK, fill_opacity=0.8)
        ch3_label = MathTex("CH_3").scale(0.5).move_to(c.get_center())
        return VGroup(c, ch3_label)

    # 官能团创建方法
    def create_hydroxyl_group(self):
        """创建羟基"""
        o = Circle(radius=0.2, color=RED, fill_opacity=0.8)
        h = Circle(radius=0.1, color=WHITE, fill_opacity=0.8)
        h.move_to(o.get_center() + 0.4 * RIGHT)

        bond = Line(o.get_center(), h.get_center(), color=WHITE)

        # 连接碳的位置
        c_connector = DashedLine(
            o.get_center() + 0.3 * LEFT,
            o.get_center(),
            color=GRAY
        )

        return VGroup(o, h, bond, c_connector)

    def create_ether_group(self):
        """创建醚键"""
        o = Circle(radius=0.2, color=RED, fill_opacity=0.8)

        # 两个连接碳的位置
        c1_connector = DashedLine(
            o.get_center() + 0.4 * LEFT,
            o.get_center(),
            color=GRAY
        )
        c2_connector = DashedLine(
            o.get_center(),
            o.get_center() + 0.4 * RIGHT,
            color=GRAY
        )

        return VGroup(o, c1_connector, c2_connector)

    def create_aldehyde_group(self):
        """创建醛基"""
        c = Circle(radius=0.2, color=BLACK, fill_opacity=0.8)
        o = Circle(radius=0.2, color=RED, fill_opacity=0.8)
        h = Circle(radius=0.1, color=WHITE, fill_opacity=0.8)

        o.move_to(c.get_center() + 0.5 * UP)
        h.move_to(c.get_center() + 0.4 * RIGHT)

        # 双键
        double_bond = VGroup(
            Line(c.get_center() + 0.05 * LEFT, o.get_center() + 0.05 * LEFT),
            Line(c.get_center() + 0.05 * RIGHT, o.get_center() + 0.05 * RIGHT)
        )

        # C-H键
        ch_bond = Line(c.get_center(), h.get_center(), color=WHITE)

        # 连接R的位置
        r_connector = DashedLine(
            c.get_center() + 0.4 * LEFT,
            c.get_center(),
            color=GRAY
        )

        return VGroup(c, o, h, double_bond, ch_bond, r_connector)

    def create_ketone_group(self):
        """创建酮基"""
        c = Circle(radius=0.2, color=BLACK, fill_opacity=0.8)
        o = Circle(radius=0.2, color=RED, fill_opacity=0.8)

        o.move_to(c.get_center() + 0.5 * UP)

        # 双键
        double_bond = VGroup(
            Line(c.get_center() + 0.05 * LEFT, o.get_center() + 0.05 * LEFT),
            Line(c.get_center() + 0.05 * RIGHT, o.get_center() + 0.05 * RIGHT)
        )

        # 连接两个R的位置
        r1_connector = DashedLine(
            c.get_center() + 0.4 * LEFT,
            c.get_center(),
            color=GRAY
        )
        r2_connector = DashedLine(
            c.get_center(),
            c.get_center() + 0.4 * RIGHT,
            color=GRAY
        )

        return VGroup(c, o, double_bond, r1_connector, r2_connector)

    def create_carboxyl_group(self):
        """创建羧基"""
        c = Circle(radius=0.2, color=BLACK, fill_opacity=0.8)
        o1 = Circle(radius=0.2, color=RED, fill_opacity=0.8)  # 羰基氧
        o2 = Circle(radius=0.2, color=RED, fill_opacity=0.8)  # 羟基氧
        h = Circle(radius=0.1, color=WHITE, fill_opacity=0.8)

        o1.move_to(c.get_center() + 0.5 * UP)
        o2.move_to(c.get_center() + 0.5 * RIGHT)
        h.move_to(o2.get_center() + 0.3 * RIGHT)

        # 双键
        double_bond = VGroup(
            Line(c.get_center() + 0.05 * LEFT, o1.get_center() + 0.05 * LEFT),
            Line(c.get_center() + 0.05 * RIGHT, o1.get_center() + 0.05 * RIGHT)
        )

        # 单键
        co_bond = Line(c.get_center(), o2.get_center(), color=WHITE)
        oh_bond = Line(o2.get_center(), h.get_center(), color=WHITE)

        # 连接R的位置
        r_connector = DashedLine(
            c.get_center() + 0.4 * LEFT,
            c.get_center(),
            color=GRAY
        )

        return VGroup(c, o1, o2, h, double_bond, co_bond, oh_bond, r_connector)

    def create_ester_group(self):
        """创建酯基"""
        c = Circle(radius=0.2, color=BLACK, fill_opacity=0.8)
        o1 = Circle(radius=0.2, color=RED, fill_opacity=0.8)  # 羰基氧
        o2 = Circle(radius=0.2, color=RED, fill_opacity=0.8)  # 醚氧

        o1.move_to(c.get_center() + 0.5 * UP)
        o2.move_to(c.get_center() + 0.5 * RIGHT)

        # 双键
        double_bond = VGroup(
            Line(c.get_center() + 0.05 * LEFT, o1.get_center() + 0.05 * LEFT),
            Line(c.get_center() + 0.05 * RIGHT, o1.get_center() + 0.05 * RIGHT)
        )

        # 单键
        co_bond = Line(c.get_center(), o2.get_center(), color=WHITE)

        # 连接R的位置
        r1_connector = DashedLine(
            c.get_center() + 0.4 * LEFT,
            c.get_center(),
            color=GRAY
        )
        r2_connector = DashedLine(
            o2.get_center(),
            o2.get_center() + 0.4 * RIGHT,
            color=GRAY
        )

        return VGroup(c, o1, o2, double_bond, co_bond, r1_connector, r2_connector)

    def create_amino_group(self):
        """创建氨基"""
        n = Circle(radius=0.2, color=BLUE, fill_opacity=0.8)
        h1 = Circle(radius=0.1, color=WHITE, fill_opacity=0.8)
        h2 = Circle(radius=0.1, color=WHITE, fill_opacity=0.8)

        h1.move_to(n.get_center() + 0.3 * UP + 0.2 * LEFT)
        h2.move_to(n.get_center() + 0.3 * UP + 0.2 * RIGHT)

        # N-H键
        nh1_bond = Line(n.get_center(), h1.get_center(), color=WHITE)
        nh2_bond = Line(n.get_center(), h2.get_center(), color=WHITE)

        # 连接R的位置
        r_connector = DashedLine(
            n.get_center() + 0.4 * DOWN,
            n.get_center(),
            color=GRAY
        )

        return VGroup(n, h1, h2, nh1_bond, nh2_bond, r_connector)

    def create_nitro_group(self):
        """创建硝基"""
        n = Circle(radius=0.2, color=BLUE, fill_opacity=0.8)
        o1 = Circle(radius=0.2, color=RED, fill_opacity=0.8)
        o2 = Circle(radius=0.2, color=RED, fill_opacity=0.8)

        o1.move_to(n.get_center() + 0.4 * UP + 0.3 * LEFT)
        o2.move_to(n.get_center() + 0.4 * UP + 0.3 * RIGHT)

        # N=O双键
        double_bond1 = VGroup(
            Line(n.get_center() + 0.02 * LEFT, o1.get_center() + 0.02 * RIGHT),
            Line(n.get_center() + 0.02 * UP, o1.get_center() + 0.02 * DOWN)
        )
        double_bond2 = VGroup(
            Line(n.get_center() + 0.02 * RIGHT, o2.get_center() + 0.02 * LEFT),
            Line(n.get_center() + 0.02 * UP, o2.get_center() + 0.02 * DOWN)
        )

        # 连接R的位置
        r_connector = DashedLine(
            n.get_center() + 0.4 * DOWN,
            n.get_center(),
            color=GRAY
        )

        # 电荷标记
        plus_sign = MathTex("+").scale(0.5).next_to(n, UR, buff=0.05)
        minus_sign1 = MathTex("-").scale(0.5).next_to(o1, UL, buff=0.05)
        minus_sign2 = MathTex("-").scale(0.5).next_to(o2, UR, buff=0.05)

        return VGroup(
            n, o1, o2, double_bond1, double_bond2,
            r_connector, plus_sign, minus_sign1, minus_sign2
        )

    def create_halogen_group(self):
        """创建卤素基团"""
        x = Circle(radius=0.25, color=GREEN, fill_opacity=0.8)
        x_label = Text("X", font_size=20, color=WHITE).move_to(x.get_center())

        # 连接R的位置
        r_connector = DashedLine(
            x.get_center() + 0.4 * LEFT,
            x.get_center(),
            color=GRAY
        )

        # 说明文字
        note = Text("X = F, Cl, Br, I", font_size=16).next_to(x, DOWN, buff=0.3)

        return VGroup(x, x_label, r_connector, note)


# 3D场景类
class ChemistryAnimation3D(ThreeDScene):
    def construct(self):
        # 设置相机
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)

        # 标题
        title = Text("立体化学的三维世界", font="STSong", font_size=48)
        title.to_edge(UP)
        self.add_fixed_in_frame_mobjects(title)
        self.play(Write(title))

        # 创建手性分子
        chiral_molecule = self.create_3d_chiral_molecule()

        self.play(Create(chiral_molecule))

        # 旋转展示
        self.begin_ambient_camera_rotation(rate=0.2)
        self.wait(5)
        self.stop_ambient_camera_rotation()

        # 展示镜像
        mirror_molecule = self.create_3d_chiral_molecule(mirror=True)
        mirror_molecule.shift(4 * RIGHT)

        self.play(Create(mirror_molecule))

        # 同时旋转
        self.play(
            Rotate(chiral_molecule, angle=2 * PI, axis=UP),
            Rotate(mirror_molecule, angle=2 * PI, axis=UP),
            run_time=4
        )

        # 说明文字
        explanation = Text(
            "手性分子与其镜像不能重合",
            font="STSong",
            font_size=32
        )
        explanation.to_edge(DOWN)
        self.add_fixed_in_frame_mobjects(explanation)
        self.play(Write(explanation))

        self.wait(3)

    def create_3d_chiral_molecule(self, mirror=False):
        """创建3D手性分子"""
        # 中心碳原子
        carbon = Sphere(radius=0.4, color=BLACK)

        # 四个不同的取代基
        h_atom = Sphere(radius=0.2, color=WHITE)
        cl_atom = Sphere(radius=0.3, color=GREEN)
        br_atom = Sphere(radius=0.35, color=RED_B)
        ch3_group = self.create_3d_methyl()

        # 四面体排列
        if not mirror:
            h_atom.move_to(np.array([0, 0, 1.2]))
            cl_atom.move_to(np.array([1.04, 0, -0.6]))
            br_atom.move_to(np.array([-0.52, 0.9, -0.6]))
            ch3_group.move_to(np.array([-0.52, -0.9, -0.6]))
        else:
            h_atom.move_to(np.array([0, 0, 1.2]))
            cl_atom.move_to(np.array([-1.04, 0, -0.6]))
            br_atom.move_to(np.array([0.52, 0.9, -0.6]))
            ch3_group.move_to(np.array([0.52, -0.9, -0.6]))

        # 创建键
        bonds = VGroup()
        for atom in [h_atom, cl_atom, br_atom, ch3_group]:
            bond = Line3D(
                start=carbon.get_center(),
                end=atom.get_center(),
                color=WHITE,
                thickness=0.02
            )
            bonds.add(bond)

        return VGroup(carbon, h_atom, cl_atom, br_atom, ch3_group, bonds)

    def create_3d_methyl(self):
        """创建3D甲基"""
        c = Sphere(radius=0.25, color=BLACK)
        h_atoms = VGroup()

        # 三个氢原子的四面体排列
        positions = [
            np.array([0.4, 0, 0.3]),
            np.array([-0.2, 0.35, 0.3]),
            np.array([-0.2, -0.35, 0.3])
        ]

        for pos in positions:
            h = Sphere(radius=0.15, color=WHITE)
            h.move_to(pos)
            h_atoms.add(h)

        return VGroup(c, h_atoms)


# 额外的动画场景类
class OrganicReactionMechanisms(Scene):
    def construct(self):
        # 标题
        title = Text("有机反应机理详解", font="STSong", font_size=56)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait()

        # 第一部分：亲核取代反应对比
        self.nucleophilic_substitution_comparison()

        # 第二部分：消除反应对比
        self.elimination_comparison()

        # 第三部分：加成反应
        self.addition_reactions()

        # 第四部分：重排反应
        self.rearrangement_reactions()

    def nucleophilic_substitution_comparison(self):
        """SN1 vs SN2对比"""
        section_title = Text("亲核取代反应：SN1 vs SN2", font="STSong", font_size=42)
        section_title.to_edge(UP).shift(DOWN)
        self.play(Transform(self.mobjects[0], section_title))

        # SN1机理
        sn1_title = Text("SN1机理", font="STSong", font_size=32)
        sn1_title.move_to(3 * LEFT + 2 * UP)

        # SN2机理
        sn2_title = Text("SN2机理", font="STSong", font_size=32)
        sn2_title.move_to(3 * RIGHT + 2 * UP)

        self.play(Write(sn1_title), Write(sn2_title))

        # SN1步骤
        sn1_steps = self.create_sn1_mechanism()
        sn1_steps.scale(0.7).next_to(sn1_title, DOWN, buff=0.5)

        # SN2步骤
        sn2_steps = self.create_sn2_mechanism()
        sn2_steps.scale(0.7).next_to(sn2_title, DOWN, buff=0.5)

        self.play(
            Create(sn1_steps, lag_ratio=0.1),
            Create(sn2_steps, lag_ratio=0.1),
            run_time=4
        )

        # 特征对比
        comparison_table = self.create_comparison_table()
        comparison_table.to_edge(DOWN)

        self.play(Create(comparison_table))
        self.wait(3)

        # 清理
        self.play(FadeOut(Group(*self.mobjects[1:])))

    def create_sn1_mechanism(self):
        """创建SN1机理"""
        steps = VGroup()

        # 第一步：离去基团离去
        step1 = VGroup()

        # 反应物
        substrate = self.create_tertiary_substrate()
        substrate.move_to(2 * LEFT)

        # 碳正离子
        carbocation = self.create_carbocation()
        carbocation.move_to(2 * RIGHT)

        # 离去的溴离子
        br_ion = self.create_bromide_ion()
        br_ion.move_to(2 * RIGHT + DOWN)

        # 箭头
        arrow1 = Arrow(substrate.get_right(), carbocation.get_left())
        step1_label = Text("慢", font="STSong", font_size=20).next_to(arrow1, UP)

        step1.add(substrate, arrow1, step1_label, carbocation, br_ion)

        # 第二步：亲核试剂进攻
        step2 = VGroup()

        # 亲核试剂
        nucleophile = self.create_hydroxide()
        nucleophile.move_to(carbocation.get_center() + 2 * UP)

        # 产物
        product = self.create_alcohol_product()
        product.move_to(carbocation.get_center() + 2 * DOWN)

        # 箭头
        arrow2 = Arrow(nucleophile.get_bottom(), product.get_top())
        step2_label = Text("快", font="STSong", font_size=20).next_to(arrow2, RIGHT)

        step2.add(nucleophile, arrow2, step2_label, product)
        step2.shift(2 * DOWN)

        steps.add(step1, step2)
        return steps

    def create_sn2_mechanism(self):
        """创建SN2机理"""
        mechanism = VGroup()

        # 反应物
        substrate = self.create_primary_substrate()
        substrate.move_to(2 * LEFT)

        # 亲核试剂
        nucleophile = self.create_hydroxide()
        nucleophile.move_to(substrate.get_center() + 2 * UP + LEFT)

        # 过渡态
        ts = self.create_sn2_transition_state()
        ts.move_to(ORIGIN)

        # 产物
        product = self.create_inverted_product()
        product.move_to(2 * RIGHT)

        # 离去基团
        leaving_group = self.create_bromide_ion()
        leaving_group.move_to(product.get_center() + 2 * DOWN + RIGHT)

        # 箭头
        arrow1 = CurvedArrow(
            nucleophile.get_bottom(),
            ts.get_left(),
            angle=-TAU / 6
        )
        arrow2 = CurvedArrow(
            ts.get_right(),
            product.get_left(),
            angle=-TAU / 6
        )

        # 协同标记
        concerted_label = Text("协同机理", font="STSong", font_size=24)
        concerted_label.next_to(ts, UP)

        mechanism.add(
            substrate, nucleophile, arrow1,
            ts, arrow2, product, leaving_group,
            concerted_label
        )

        return mechanism

    def create_comparison_table(self):
        """创建SN1/SN2对比表"""
        # 表格数据
        headers = ["特征", "SN1", "SN2"]
        rows = [
            ["机理", "两步", "一步协同"],
            ["速率方程", "v = k[RX]", "v = k[RX][Nu]"],
            ["立体化学", "外消旋化", "构型翻转"],
            ["底物", "3° > 2° > 1°", "1° > 2° > 3°"],
            ["溶剂", "质子性", "非质子性"]
        ]

        # 创建表格
        table = VGroup()

        # 表头
        header_row = VGroup()
        for i, header in enumerate(headers):
            cell = VGroup(
                Rectangle(width=2.5, height=0.6, color=BLUE),
                Text(header, font="STSong", font_size=20)
            )
            cell[1].move_to(cell[0].get_center())
            if i > 0:
                cell.next_to(header_row[-1], RIGHT, buff=0)
            header_row.add(cell)

        table.add(header_row)

        # 数据行
        for row_data in rows:
            row = VGroup()
            for i, data in enumerate(row_data):
                cell = VGroup(
                    Rectangle(width=2.5, height=0.5, color=WHITE),
                    Text(data, font="STSong", font_size=16)
                )
                cell[1].move_to(cell[0].get_center())
                if i > 0:
                    cell.next_to(row[-1], RIGHT, buff=0)
                else:
                    cell.align_to(header_row[0], LEFT)
                row.add(cell)
            row.next_to(table[-1], DOWN, buff=0)
            table.add(row)

        return table

    def elimination_comparison(self):
        """E1 vs E2对比"""
        section_title = Text("消除反应：E1 vs E2", font="STSong", font_size=42)
        section_title.to_edge(UP).shift(DOWN)
        self.play(Transform(self.mobjects[0], section_title))

        # E1和E2机理展示
        e1_mechanism = self.create_e1_mechanism()
        e2_mechanism = self.create_e2_mechanism_detailed()

        e1_mechanism.scale(0.6).move_to(3 * LEFT)
        e2_mechanism.scale(0.6).move_to(3 * RIGHT)

        e1_label = Text("E1机理", font="STSong", font_size=28).next_to(e1_mechanism, UP)
        e2_label = Text("E2机理", font="STSong", font_size=28).next_to(e2_mechanism, UP)

        self.play(
            Write(e1_label), Write(e2_label),
            Create(e1_mechanism), Create(e2_mechanism),
            run_time=3
        )

        # Zaitsev vs Hofmann产物
        product_comparison = self.create_elimination_products()
        product_comparison.to_edge(DOWN)

        self.play(Create(product_comparison))
        self.wait(3)

        # 清理
        self.play(FadeOut(Group(*self.mobjects[1:])))

    def addition_reactions(self):
        """加成反应展示"""
        section_title = Text("加成反应机理", font="STSong", font_size=42)
        section_title.to_edge(UP).shift(DOWN)
        self.play(Transform(self.mobjects[0], section_title))

        # 亲电加成
        electrophilic_addition = self.create_electrophilic_addition()
        electrophilic_addition.scale(0.7).shift(2 * UP)

        # 自由基加成
        radical_addition = self.create_radical_addition()
        radical_addition.scale(0.7).shift(2 * DOWN)

        self.play(
            Create(electrophilic_addition, lag_ratio=0.1),
            Create(radical_addition, lag_ratio=0.1),
            run_time=4
        )

        self.wait(3)

        # 清理
        self.play(FadeOut(Group(*self.mobjects[1:])))

    def rearrangement_reactions(self):
        """重排反应展示"""
        section_title = Text("重排反应", font="STSong", font_size=42)
        section_title.to_edge(UP).shift(DOWN)
        self.play(Transform(self.mobjects[0], section_title))

        # 碳正离子重排
        carbocation_rearrangement = self.create_carbocation_rearrangement()
        carbocation_rearrangement.move_to(ORIGIN)

        self.play(Create(carbocation_rearrangement, lag_ratio=0.1), run_time=3)

        # 重排驱动力说明
        driving_force = Text(
            "驱动力：形成更稳定的碳正离子",
            font="STSong",
            font_size=28
        ).to_edge(DOWN)

        self.play(Write(driving_force))
        self.wait(3)

    # 辅助方法
    def create_tertiary_substrate(self):
        """创建三级底物"""
        c = Circle(radius=0.25, color=BLACK, fill_opacity=0.8)
        br = Circle(radius=0.3, color=RED_B, fill_opacity=0.8)
        br.next_to(c, RIGHT, buff=0.1)

        # 三个甲基
        methyls = VGroup()
        for angle in [2 * PI / 3, 4 * PI / 3, 0]:
            ch3 = self.create_methyl_simple()
            ch3.move_to(c.get_center() + 0.5 * np.array([
                np.cos(angle), np.sin(angle), 0
            ]))
            methyls.add(ch3)

        return VGroup(c, br, methyls)

    def create_carbocation(self):
        """创建碳正离子"""
        c = Circle(radius=0.25, color=BLACK, fill_opacity=0.8)
        plus = MathTex("+").move_to(c.get_center())

        # 三个甲基
        methyls = VGroup()
        for angle in [0, 2 * PI / 3, 4 * PI / 3]:
            ch3 = self.create_methyl_simple()
            ch3.move_to(c.get_center() + 0.5 * np.array([
                np.cos(angle), np.sin(angle), 0
            ]))
            methyls.add(ch3)

        return VGroup(c, plus, methyls)

    def create_methyl_simple(self):
        """创建简化甲基"""
        return VGroup(
            Circle(radius=0.15, color=BLACK, fill_opacity=0.6),
            MathTex("CH_3").scale(0.5)
        )

    def create_bromide_ion(self):
        """创建溴离子"""
        br = Circle(radius=0.3, color=RED_B, fill_opacity=0.8)
        label = MathTex("Br^-").scale(0.8).move_to(br.get_center())
        return VGroup(br, label)

    def create_hydroxide(self):
        """创建氢氧根离子"""
        o = Circle(radius=0.25, color=RED, fill_opacity=0.8)
        h = Circle(radius=0.15, color=WHITE, fill_opacity=0.8)
        h.next_to(o, RIGHT, buff=0.1)

        bond = Line(o.get_center(), h.get_center(), color=WHITE)
        minus = MathTex("-").scale(0.6).next_to(o, UL, buff=0.05)

        return VGroup(o, h, bond, minus)

    def create_alcohol_product(self):
        """创建醇产物"""
        c = Circle(radius=0.25, color=BLACK, fill_opacity=0.8)
        oh = self.create_oh_group()
        oh.next_to(c, RIGHT, buff=0.1)

        # 三个甲基
        methyls = VGroup()
        for angle in [2 * PI / 3, 4 * PI / 3, 0]:
            ch3 = self.create_methyl_simple()
            ch3.move_to(c.get_center() + 0.5 * np.array([
                np.cos(angle), np.sin(angle), 0
            ]))
            methyls.add(ch3)

        return VGroup(c, oh, methyls)

    def create_oh_group(self):
        """创建OH基团"""
        o = Circle(radius=0.2, color=RED, fill_opacity=0.8)
        h = Circle(radius=0.1, color=WHITE, fill_opacity=0.8)
        h.next_to(o, RIGHT, buff=0.05)
        bond = Line(o.get_center(), h.get_center(), color=WHITE)
        return VGroup(o, h, bond)

    def create_primary_substrate(self):
        """创建一级底物"""
        c = Circle(radius=0.25, color=BLACK, fill_opacity=0.8)
        br = Circle(radius=0.3, color=RED_B, fill_opacity=0.8)
        br.next_to(c, RIGHT, buff=0.1)

        # 两个氢和一个乙基
        h1 = Circle(radius=0.1, color=WHITE, fill_opacity=0.8)
        h2 = Circle(radius=0.1, color=WHITE, fill_opacity=0.8)
        ethyl = self.create_ethyl_group()

        h1.move_to(c.get_center() + 0.4 * UP)
        h2.move_to(c.get_center() + 0.4 * DOWN)
        ethyl.move_to(c.get_center() + 0.6 * LEFT)

        return VGroup(c, br, h1, h2, ethyl)

    def create_ethyl_group(self):
        """创建乙基"""
        c1 = Circle(radius=0.15, color=BLACK, fill_opacity=0.6)
        c2 = Circle(radius=0.15, color=BLACK, fill_opacity=0.6)
        c2.next_to(c1, LEFT, buff=0.1)

        bond = Line(c1.get_center(), c2.get_center(), color=WHITE)
        label = MathTex("CH_3").scale(0.4).move_to(c2.get_center())

        return VGroup(c1, c2, bond, label)

    def create_inverted_product(self):
        """创建构型翻转的产物"""
        c = Circle(radius=0.25, color=BLACK, fill_opacity=0.8)
        oh = self.create_oh_group()
        oh.next_to(c, LEFT, buff=0.1)  # 注意位置相反

        # 两个氢和一个乙基
        h1 = Circle(radius=0.1, color=WHITE, fill_opacity=0.8)
        h2 = Circle(radius=0.1, color=WHITE, fill_opacity=0.8)
        ethyl = self.create_ethyl_group()

        h1.move_to(c.get_center() + 0.4 * UP)
        h2.move_to(c.get_center() + 0.4 * DOWN)
        ethyl.move_to(c.get_center() + 0.6 * RIGHT)

        # 标记构型翻转
        inversion_label = Text("构型翻转", font="STSong", font_size=16)
        inversion_label.next_to(VGroup(c, oh, h1, h2, ethyl), DOWN)

        return VGroup(c, oh, h1, h2, ethyl, inversion_label)

    def create_e1_mechanism(self):
        """创建E1机理"""
        mechanism = VGroup()

        # 第一步：形成碳正离子
        step1 = VGroup()
        substrate = self.create_tertiary_substrate()
        carbocation = self.create_carbocation()
        br_ion = self.create_bromide_ion()

        substrate.move_to(2 * LEFT)
        carbocation.move_to(2 * RIGHT + UP)
        br_ion.move_to(2 * RIGHT + DOWN)

        arrow1 = Arrow(substrate.get_right(), carbocation.get_left())
        step1_label = Text("慢", font="STSong", font_size=16).next_to(arrow1, UP)

        step1.add(substrate, arrow1, step1_label, carbocation, br_ion)

        # 第二步：β-H消除
        step2 = VGroup()
        base = self.create_weak_base()
        alkene = self.create_alkene_product()

        base.move_to(carbocation.get_center() + 2 * LEFT)
        alkene.move_to(carbocation.get_center() + 2 * RIGHT)

        arrow2 = Arrow(base.get_right(), alkene.get_left())
        step2_label = Text("快", font="STSong", font_size=16).next_to(arrow2, UP)

        step2.add(base, arrow2, step2_label, alkene)
        step2.shift(2 * DOWN)

        mechanism.add(step1, step2)
        return mechanism

    def create_e2_mechanism_detailed(self):
        """创建详细的E2机理"""
        mechanism = VGroup()

        # 反应物复合体
        substrate = self.create_anti_periplanar_substrate()
        base = self.create_strong_base()

        substrate.move_to(ORIGIN)
        base.move_to(substrate.get_center() + 2 * DOWN + LEFT)

        # 过渡态
        ts_arrows = VGroup()
        # β-H到碱的箭头
        arrow1 = CurvedArrow(
            substrate.get_center() + 0.5 * DOWN,
            base.get_top(),
            angle=TAU / 6,
            color=GREEN
        )
        # C-C形成π键的箭头
        arrow2 = CurvedArrow(
            substrate.get_center() + 0.2 * LEFT,
            substrate.get_center() + 0.2 * RIGHT,
            angle=-TAU / 8,
            color=BLUE
        )
        # C-Br断裂的箭头
        arrow3 = CurvedArrow(
            substrate.get_center() + 0.5 * RIGHT,
            substrate.get_center() + 1.5 * RIGHT,
            angle=TAU / 8,
            color=RED
        )

        ts_arrows.add(arrow1, arrow2, arrow3)

        # 产物
        alkene = self.create_alkene_product()
        hbase = self.create_protonated_base()
        br_ion = self.create_bromide_ion()

        alkene.move_to(2 * RIGHT + UP)
        hbase.move_to(2 * RIGHT)
        br_ion.move_to(2 * RIGHT + DOWN)

        # 协同标记
        concerted = Text("协同消除", font="STSong", font_size=20)
        concerted.next_to(ts_arrows, UP)

        mechanism.add(
            substrate, base, ts_arrows, concerted,
            alkene, hbase, br_ion
        )

        return mechanism

    def create_weak_base(self):
        """创建弱碱"""
        h2o = VGroup(
            Circle(radius=0.2, color=RED, fill_opacity=0.8),
            Circle(radius=0.1, color=WHITE, fill_opacity=0.8),
            Circle(radius=0.1, color=WHITE, fill_opacity=0.8)
        )
        h2o[1].move_to(h2o[0].get_center() + 0.3 * UP + 0.2 * LEFT)
        h2o[2].move_to(h2o[0].get_center() + 0.3 * UP + 0.2 * RIGHT)

        label = MathTex("H_2O").scale(0.6).next_to(h2o, DOWN)

        return VGroup(h2o, label)

    def create_strong_base(self):
        """创建强碱"""
        base = VGroup(
            Circle(radius=0.25, color=BLUE, fill_opacity=0.8),
            MathTex("B^-").scale(0.8)
        )
        base[1].move_to(base[0].get_center())

        label = Text("强碱", font="STSong", font_size=16).next_to(base, DOWN)

        return VGroup(base, label)

    def create_alkene_product(self):
        """创建烯烃产物"""
        c1 = Circle(radius=0.2, color=BLACK, fill_opacity=0.8)
        c2 = Circle(radius=0.2, color=BLACK, fill_opacity=0.8)
        c1.move_to(0.4 * LEFT)
        c2.move_to(0.4 * RIGHT)

        # 双键
        double_bond = VGroup(
            Line(c1.get_center() + 0.05 * UP, c2.get_center() + 0.05 * UP),
            Line(c1.get_center() + 0.05 * DOWN, c2.get_center() + 0.05 * DOWN)
        )

        # 取代基
        r_groups = VGroup()
        for i, pos in enumerate([c1.get_center() + 0.5 * LEFT,
                                 c1.get_center() + 0.5 * UP,
                                 c2.get_center() + 0.5 * RIGHT,
                                 c2.get_center() + 0.5 * DOWN]):
            r = self.create_r_group(i)
            r.move_to(pos)
            r_groups.add(r)

        return VGroup(c1, c2, double_bond, r_groups)

    def create_r_group(self, index):
        """创建R基团"""
        if index < 2:
            return VGroup(
                Circle(radius=0.1, color=GRAY, fill_opacity=0.6),
                MathTex(f"R_{index + 1}").scale(0.4)
            )
        else:
            return Circle(radius=0.08, color=WHITE, fill_opacity=0.8)

    def create_anti_periplanar_substrate(self):
        """创建反式共平面构象"""
        # Newman投影式
        front_c = Circle(radius=0.3, color=BLACK, fill_opacity=0.8)
        back_c = Circle(radius=0.5, color=BLACK, fill_opacity=0.2)

        # 前碳上的取代基
        h_front = Circle(radius=0.1, color=WHITE, fill_opacity=0.8)
        h_front.move_to(front_c.get_center() + 0.4 * DOWN)

        # 后碳上的取代基
        br_back = Circle(radius=0.25, color=RED_B, fill_opacity=0.8)
        br_back.move_to(back_c.get_center() + 0.6 * UP)
        br_label = Text("Br", font_size=16, color=WHITE).move_to(br_back.get_center())

        # 其他取代基
        other_groups = VGroup()
        positions = [
            front_c.get_center() + 0.4 * UP + 0.3 * LEFT,
            front_c.get_center() + 0.4 * UP + 0.3 * RIGHT,
            back_c.get_center() + 0.6 * DOWN + 0.4 * LEFT,
            back_c.get_center() + 0.6 * DOWN + 0.4 * RIGHT
        ]

        for pos in positions:
            group = Circle(radius=0.08, color=GRAY, fill_opacity=0.6)
            group.move_to(pos)
            other_groups.add(group)

        # 标记反式共平面
        label = Text("反式共平面", font="STSong", font_size=16)
        label.next_to(VGroup(front_c, back_c), DOWN, buff=0.5)

        return VGroup(back_c, front_c, h_front, br_back, br_label,
                      other_groups, label)

    def create_protonated_base(self):
        """创建质子化的碱"""
        base = VGroup(
            Circle(radius=0.25, color=BLUE, fill_opacity=0.8),
            Circle(radius=0.1, color=WHITE, fill_opacity=0.8)
        )
        base[1].next_to(base[0], UP, buff=0.05)

        bond = Line(base[0].get_center(), base[1].get_center(), color=WHITE)
        label = MathTex("BH").scale(0.8).move_to(base[0].get_center())

        return VGroup(base, bond, label)

    def create_elimination_products(self):
        """创建消除反应产物对比"""
        products = VGroup()

        # Zaitsev产物
        zaitsev_title = Text("Zaitsev产物", font="STSong", font_size=24)
        zaitsev_product = self.create_more_substituted_alkene()
        zaitsev_label = Text("(主要产物)", font="STSong", font_size=18)

        zaitsev_group = VGroup(zaitsev_title, zaitsev_product, zaitsev_label)
        zaitsev_group.arrange(DOWN, buff=0.3)
        zaitsev_group.move_to(3 * LEFT)

        # Hofmann产物
        hofmann_title = Text("Hofmann产物", font="STSong", font_size=24)
        hofmann_product = self.create_less_substituted_alkene()
        hofmann_label = Text("(次要产物)", font="STSong", font_size=18)

        hofmann_group = VGroup(hofmann_title, hofmann_product, hofmann_label)
        hofmann_group.arrange(DOWN, buff=0.3)
        hofmann_group.move_to(3 * RIGHT)

        # 条件解释
        conditions = VGroup(
            Text("强碱/高温", font="STSong", font_size=20),
            Text("↓", font_size=24),
            Text("Hofmann产物增加", font="STSong", font_size=18)
        )
        conditions.arrange(DOWN, buff=0.2)
        conditions.move_to(ORIGIN)

        products.add(zaitsev_group, hofmann_group, conditions)
        return products

    def create_more_substituted_alkene(self):
        """创建取代度更高的烯烃"""
        c1 = Circle(radius=0.2, color=BLACK, fill_opacity=0.8)
        c2 = Circle(radius=0.2, color=BLACK, fill_opacity=0.8)
        c1.move_to(0.4 * LEFT)
        c2.move_to(0.4 * RIGHT)

        # 双键
        double_bond = VGroup(
            Line(c1.get_center() + 0.05 * UP, c2.get_center() + 0.05 * UP),
            Line(c1.get_center() + 0.05 * DOWN, c2.get_center() + 0.05 * DOWN)
        )

        # C1有两个甲基
        ch3_1 = Circle(radius=0.12, color=BLACK, fill_opacity=0.6)
        ch3_1.move_to(c1.get_center() + 0.4 * UP)
        ch3_label1 = MathTex("CH_3").scale(0.4).move_to(ch3_1.get_center())

        ch3_2 = Circle(radius=0.12, color=BLACK, fill_opacity=0.6)
        ch3_2.move_to(c1.get_center() + 0.4 * DOWN)
        ch3_label2 = MathTex("CH_3").scale(0.4).move_to(ch3_2.get_center())

        # C2有一个甲基和一个氢
        ch3_3 = Circle(radius=0.12, color=BLACK, fill_opacity=0.6)
        ch3_3.move_to(c2.get_center() + 0.4 * UP)
        ch3_label3 = MathTex("CH_3").scale(0.4).move_to(ch3_3.get_center())

        h = Circle(radius=0.1, color=WHITE, fill_opacity=0.8)
        h.move_to(c2.get_center() + 0.4 * DOWN)

        return VGroup(
            c1, c2, double_bond,
            ch3_1, ch3_label1, ch3_2, ch3_label2,
            ch3_3, ch3_label3, h
        )

    def create_less_substituted_alkene(self):
        """创建取代度更低的烯烃"""
        c1 = Circle(radius=0.2, color=BLACK, fill_opacity=0.8)
        c2 = Circle(radius=0.2, color=BLACK, fill_opacity=0.8)
        c1.move_to(0.4 * LEFT)
        c2.move_to(0.4 * RIGHT)

        # 双键
        double_bond = VGroup(
            Line(c1.get_center() + 0.05 * UP, c2.get_center() + 0.05 * UP),
            Line(c1.get_center() + 0.05 * DOWN, c2.get_center() + 0.05 * DOWN)
        )

        # C1有一个甲基和一个氢
        ch3_1 = Circle(radius=0.12, color=BLACK, fill_opacity=0.6)
        ch3_1.move_to(c1.get_center() + 0.4 * UP)
        ch3_label1 = MathTex("CH_3").scale(0.4).move_to(ch3_1.get_center())

        h1 = Circle(radius=0.1, color=WHITE, fill_opacity=0.8)
        h1.move_to(c1.get_center() + 0.4 * DOWN)

        # C2有两个氢
        ch3_2 = Circle(radius=0.12, color=BLACK, fill_opacity=0.6)
        ch3_2.move_to(c2.get_center() + 0.4 * UP)
        ch3_label2 = MathTex("CH_3").scale(0.4).move_to(ch3_2.get_center())

        h2 = Circle(radius=0.1, color=WHITE, fill_opacity=0.8)
        h2.move_to(c2.get_center() + 0.4 * DOWN)

        return VGroup(
            c1, c2, double_bond,
            ch3_1, ch3_label1, h1,
            ch3_2, ch3_label2, h2
        )

    def create_electrophilic_addition(self):
        """创建亲电加成机理"""
        mechanism = VGroup()

        # 标题
        title = Text("亲电加成：烯烃与HBr", font="STSong", font_size=28)

        # 起始烯烃
        alkene = self.create_simple_alkene()
        alkene.move_to(3 * LEFT)

        # HBr
        hbr = MathTex("HBr").move_to(2 * LEFT + UP)

        # 中间体
        intermediate = self.create_carbocation_intermediate()
        intermediate.move_to(ORIGIN)

        # 产物
        product = self.create_addition_product()
        product.move_to(3 * RIGHT)

        # 箭头和标记
        arrow1 = Arrow(alkene.get_right(), intermediate.get_left())
        arrow2 = Arrow(intermediate.get_right(), product.get_left())

        # Markovnikov规则说明
        markovnikov = Text(
            "Markovnikov规则：H加到碳原子少的碳上",
            font="STSong",
            font_size=20
        )
        markovnikov.next_to(VGroup(alkene, intermediate, product), DOWN, buff=0.5)

        mechanism.add(
            title, alkene, hbr, arrow1, intermediate,
            arrow2, product, markovnikov
        )

        return mechanism

    def create_simple_alkene(self):
        """创建简单烯烃"""
        c1 = Circle(radius=0.2, color=BLACK, fill_opacity=0.8)
        c2 = Circle(radius=0.2, color=BLACK, fill_opacity=0.8)
        c1.move_to(0.4 * LEFT)
        c2.move_to(0.4 * RIGHT)

        # 双键
        double_bond = VGroup(
            Line(c1.get_center() + 0.05 * UP, c2.get_center() + 0.05 * UP),
            Line(c1.get_center() + 0.05 * DOWN, c2.get_center() + 0.05 * DOWN)
        )

        # C1上的氢和甲基
        h1 = Circle(radius=0.1, color=WHITE, fill_opacity=0.8)
        h1.move_to(c1.get_center() + 0.4 * UP)

        h2 = Circle(radius=0.1, color=WHITE, fill_opacity=0.8)
        h2.move_to(c1.get_center() + 0.4 * LEFT)

        # C2上的两个氢
        h3 = Circle(radius=0.1, color=WHITE, fill_opacity=0.8)
        h3.move_to(c2.get_center() + 0.4 * UP)

        h4 = Circle(radius=0.1, color=WHITE, fill_opacity=0.8)
        h4.move_to(c2.get_center() + 0.4 * RIGHT)

        # 标签
        label = Text("烯烃", font="STSong", font_size=20).next_to(
            VGroup(c1, c2), DOWN, buff=0.3
        )

        return VGroup(c1, c2, double_bond, h1, h2, h3, h4, label)

    def create_carbocation_intermediate(self):
        """创建碳正离子中间体"""
        c1 = Circle(radius=0.2, color=BLACK, fill_opacity=0.8)
        c2 = Circle(radius=0.2, color=BLACK, fill_opacity=0.8)
        c1.move_to(0.4 * LEFT)
        c2.move_to(0.4 * RIGHT)

        # 单键
        bond = Line(c1.get_center(), c2.get_center(), color=WHITE)

        # C1上的氢、甲基和H
        h1 = Circle(radius=0.1, color=WHITE, fill_opacity=0.8)
        h1.move_to(c1.get_center() + 0.4 * UP)

        h2 = Circle(radius=0.1, color=WHITE, fill_opacity=0.8)
        h2.move_to(c1.get_center() + 0.4 * LEFT)

        h_new = Circle(radius=0.1, color=WHITE, fill_opacity=0.8)
        h_new.move_to(c1.get_center() + 0.4 * DOWN)

        # C2带正电荷
        plus = MathTex("+").scale(0.6).move_to(c2.get_right() + 0.2 * RIGHT)

        # C2上的两个氢
        h3 = Circle(radius=0.1, color=WHITE, fill_opacity=0.8)
        h3.move_to(c2.get_center() + 0.4 * UP)

        h4 = Circle(radius=0.1, color=WHITE, fill_opacity=0.8)
        h4.move_to(c2.get_center() + 0.4 * RIGHT)

        # 标签
        label = Text("碳正离子", font="STSong", font_size=20).next_to(
            VGroup(c1, c2), DOWN, buff=0.3
        )

        return VGroup(c1, c2, bond, h1, h2, h_new, h3, h4, plus, label)

    def create_addition_product(self):
        """创建加成产物"""
        c1 = Circle(radius=0.2, color=BLACK, fill_opacity=0.8)
        c2 = Circle(radius=0.2, color=BLACK, fill_opacity=0.8)
        c1.move_to(0.4 * LEFT)
        c2.move_to(0.4 * RIGHT)

        # 单键
        bond = Line(c1.get_center(), c2.get_center(), color=WHITE)

        # C1上的氢、甲基和H
        h1 = Circle(radius=0.1, color=WHITE, fill_opacity=0.8)
        h1.move_to(c1.get_center() + 0.4 * UP)

        h2 = Circle(radius=0.1, color=WHITE, fill_opacity=0.8)
        h2.move_to(c1.get_center() + 0.4 * LEFT)

        h_new = Circle(radius=0.1, color=WHITE, fill_opacity=0.8)
        h_new.move_to(c1.get_center() + 0.4 * DOWN)

        # C2上的溴和氢
        br = Circle(radius=0.2, color=RED_B, fill_opacity=0.8)
        br_label = Text("Br", font_size=16, color=WHITE).move_to(br.get_center())
        br.move_to(c2.get_center() + 0.4 * RIGHT)

        h3 = Circle(radius=0.1, color=WHITE, fill_opacity=0.8)
        h3.move_to(c2.get_center() + 0.4 * UP)

        h4 = Circle(radius=0.1, color=WHITE, fill_opacity=0.8)
        h4.move_to(c2.get_center() + 0.4 * DOWN)

        # 标签
        label = Text("产物", font="STSong", font_size=20).next_to(
            VGroup(c1, c2), DOWN, buff=0.3
        )

        return VGroup(c1, c2, bond, h1, h2, h_new, h3, h4, br, br_label, label)

    def create_radical_addition(self):
        """创建自由基加成机理"""
        mechanism = VGroup()

        # 标题
        title = Text("自由基加成：Anti-Markovnikov加成", font="STSong", font_size=28)

        # 起始反应物
        alkene = self.create_simple_alkene()
        hbr = MathTex("HBr")
        peroxide = MathTex("ROOR")

        alkene.move_to(3 * LEFT)
        hbr.next_to(alkene, UP, buff=0.5)
        peroxide.next_to(hbr, RIGHT, buff=0.5)

        # 自由基中间体
        radical = self.create_radical_intermediate()
        radical.move_to(ORIGIN)

        # 产物
        product = self.create_anti_markovnikov_product()
        product.move_to(3 * RIGHT)

        # 箭头和标记
        arrow1 = Arrow(alkene.get_right(), radical.get_left())
        arrow2 = Arrow(radical.get_right(), product.get_left())

        # 反Markovnikov规则说明
        anti_markovnikov = Text(
            "反Markovnikov加成：Br加到碳原子少的碳上",
            font="STSong",
            font_size=20
        )
        anti_markovnikov.next_to(VGroup(alkene, radical, product), DOWN, buff=0.5)

        mechanism.add(
            title, alkene, hbr, peroxide, arrow1, radical,
            arrow2, product, anti_markovnikov
        )

        return mechanism

    def create_radical_intermediate(self):
        """创建自由基中间体"""
        c1 = Circle(radius=0.2, color=BLACK, fill_opacity=0.8)
        c2 = Circle(radius=0.2, color=BLACK, fill_opacity=0.8)
        c1.move_to(0.4 * LEFT)
        c2.move_to(0.4 * RIGHT)

        # 单键
        bond = Line(c1.get_center(), c2.get_center(), color=WHITE)

        # C1上带自由基点
        dot = Dot(color=RED).move_to(c1.get_right() + 0.2 * LEFT)

        # C1上的氢和甲基
        h1 = Circle(radius=0.1, color=WHITE, fill_opacity=0.8)
        h1.move_to(c1.get_center() + 0.4 * UP)

        h2 = Circle(radius=0.1, color=WHITE, fill_opacity=0.8)
        h2.move_to(c1.get_center() + 0.4 * LEFT)

        # C2上有溴和两个氢
        br = Circle(radius=0.2, color=RED_B, fill_opacity=0.8)
        br_label = Text("Br", font_size=16, color=WHITE).move_to(br.get_center())
        br.move_to(c2.get_center() + 0.4 * RIGHT)

        h3 = Circle(radius=0.1, color=WHITE, fill_opacity=0.8)
        h3.move_to(c2.get_center() + 0.4 * UP)

        h4 = Circle(radius=0.1, color=WHITE, fill_opacity=0.8)
        h4.move_to(c2.get_center() + 0.4 * DOWN)

        # 标签
        label = Text("自由基中间体", font="STSong", font_size=20).next_to(
            VGroup(c1, c2), DOWN, buff=0.3
        )

        return VGroup(c1, c2, bond, dot, h1, h2, h3, h4, br, br_label, label)

    def create_anti_markovnikov_product(self):
        """创建反Markovnikov产物"""
        c1 = Circle(radius=0.2, color=BLACK, fill_opacity=0.8)
        c2 = Circle(radius=0.2, color=BLACK, fill_opacity=0.8)
        c1.move_to(0.4 * LEFT)
        c2.move_to(0.4 * RIGHT)

        # 单键
        bond = Line(c1.get_center(), c2.get_center(), color=WHITE)

        # C1上的氢、甲基和溴
        h1 = Circle(radius=0.1, color=WHITE, fill_opacity=0.8)
        h1.move_to(c1.get_center() + 0.4 * UP)

        h2 = Circle(radius=0.1, color=WHITE, fill_opacity=0.8)
        h2.move_to(c1.get_center() + 0.4 * LEFT)

        br = Circle(radius=0.2, color=RED_B, fill_opacity=0.8)
        br_label = Text("Br", font_size=16, color=WHITE).move_to(br.get_center())
        br.move_to(c1.get_center() + 0.4 * DOWN)

        # C2上的三个氢
        h3 = Circle(radius=0.1, color=WHITE, fill_opacity=0.8)
        h3.move_to(c2.get_center() + 0.4 * UP)

        h4 = Circle(radius=0.1, color=WHITE, fill_opacity=0.8)
        h4.move_to(c2.get_center() + 0.4 * RIGHT)

        h5 = Circle(radius=0.1, color=WHITE, fill_opacity=0.8)
        h5.move_to(c2.get_center() + 0.4 * DOWN)

        # 标签
        label = Text("反Markovnikov产物", font="STSong", font_size=20).next_to(
            VGroup(c1, c2), DOWN, buff=0.3
        )

        return VGroup(c1, c2, bond, h1, h2, br, br_label, h3, h4, h5, label)

    def create_sn2_transition_state(self):
        """创建SN2过渡态"""
        c = Circle(radius=0.25, color=BLACK, fill_opacity=0.8)

        # 进攻的OH和离去的Br
        oh = Circle(radius=0.2, color=RED, fill_opacity=0.6)
        oh_label = MathTex("OH^-").scale(0.6).move_to(oh.get_center())
        oh.move_to(c.get_center() + 0.8 * LEFT)

        br = Circle(radius=0.3, color=RED_B, fill_opacity=0.6)
        br_label = Text("Br", font_size=20, color=WHITE).move_to(br.get_center())
        br.move_to(c.get_center() + 0.8 * RIGHT)

        # 虚线表示部分键
        dashed_bond1 = DashedLine(
            oh.get_right(), c.get_left(),
            color=WHITE, dash_length=0.1
        )
        dashed_bond2 = DashedLine(
            c.get_right(), br.get_left(),
            color=WHITE, dash_length=0.1
        )

        # 三个氢
        h_positions = [0.4 * UP, 0.4 * DOWN + 0.2 * LEFT, 0.4 * DOWN + 0.2 * RIGHT]
        hydrogens = VGroup()
        bonds = VGroup()

        for pos in h_positions:
            h = Circle(radius=0.1, color=WHITE, fill_opacity=0.8)
            h.move_to(c.get_center() + pos)
            hydrogens.add(h)
            bond = Line(c.get_center(), h.get_center(), color=WHITE)
            bonds.add(bond)

        # 过渡态符号
        ts_symbol = MathTex(r"\ddagger").scale(1.2).next_to(c, UP, buff=0.3)

        return VGroup(
            c, oh, oh_label, br, br_label,
            dashed_bond1, dashed_bond2,
            hydrogens, bonds, ts_symbol
        )

    def create_carbocation_rearrangement(self):
        """创建碳正离子重排"""
        # 初始碳正离子
        initial = VGroup()

        c1 = Circle(radius=0.2, color=BLACK, fill_opacity=0.8)
        c2 = Circle(radius=0.2, color=BLACK, fill_opacity=0.8)
        c2.move_to(c1.get_center() + 0.6 * RIGHT)

        bond = Line(c1.get_center(), c2.get_center(), color=WHITE)

        # C1带正电荷
        plus = MathTex("+").scale(0.6).move_to(c1.get_top() + 0.2 * UP)

        # 甲基
        methyl = self.create_methyl_simple()
        methyl.move_to(c2.get_center() + 0.5 * RIGHT)

        # 氢原子
        h1 = Circle(radius=0.1, color=WHITE, fill_opacity=0.8)
        h1.move_to(c1.get_center() + 0.4 * LEFT)

        h2 = Circle(radius=0.1, color=WHITE, fill_opacity=0.8)
        h2.move_to(c1.get_center() + 0.4 * DOWN)

        h3 = Circle(radius=0.1, color=WHITE, fill_opacity=0.8)
        h3.move_to(c2.get_center() + 0.4 * UP)

        h4 = Circle(radius=0.1, color=WHITE, fill_opacity=0.8)
        h4.move_to(c2.get_center() + 0.4 * DOWN)

        initial.add(c1, c2, bond, plus, methyl, h1, h2, h3, h4)
        initial.move_to(3 * LEFT)

        # 重排过渡态
        ts = VGroup()

        c1_ts = Circle(radius=0.2, color=BLACK, fill_opacity=0.8)
        c2_ts = Circle(radius=0.2, color=BLACK, fill_opacity=0.8)
        c2_ts.move_to(c1_ts.get_center() + 0.6 * RIGHT)

        bond_ts = Line(c1_ts.get_center(), c2_ts.get_center(), color=WHITE)

        # 氢迁移
        h_migrate = Circle(radius=0.1, color=WHITE, fill_opacity=0.8)
        h_migrate.move_to(midpoint(c1_ts.get_center(), c2_ts.get_center()) + 0.3 * UP)

        # 电荷分散
        plus_ts = MathTex("\delta^+").scale(0.5).move_to(c1_ts.get_top() + 0.2 * UP)
        plus_ts2 = MathTex("\delta^+").scale(0.5).move_to(c2_ts.get_top() + 0.2 * UP)

        # 甲基
        methyl_ts = self.create_methyl_simple()
        methyl_ts.move_to(c2_ts.get_center() + 0.5 * RIGHT)

        # 其他氢原子
        h1_ts = Circle(radius=0.1, color=WHITE, fill_opacity=0.8)
        h1_ts.move_to(c1_ts.get_center() + 0.4 * LEFT)

        h2_ts = Circle(radius=0.1, color=WHITE, fill_opacity=0.8)
        h2_ts.move_to(c1_ts.get_center() + 0.4 * DOWN)

        h4_ts = Circle(radius=0.1, color=WHITE, fill_opacity=0.8)
        h4_ts.move_to(c2_ts.get_center() + 0.4 * DOWN)

        # 迁移箭头
        migrate_arrow = CurvedArrow(
            c2_ts.get_center() + 0.3 * UP,
            c1_ts.get_center() + 0.3 * UP,
            angle=-TAU / 6,
            color=RED
        )

        ts.add(c1_ts, c2_ts, bond_ts, h_migrate, plus_ts, plus_ts2,
               methyl_ts, h1_ts, h2_ts, h4_ts, migrate_arrow)
        ts.move_to(ORIGIN)

        # 重排后的碳正离子
        final = VGroup()

        c1_f = Circle(radius=0.2, color=BLACK, fill_opacity=0.8)
        c2_f = Circle(radius=0.2, color=BLACK, fill_opacity=0.8)
        c2_f.move_to(c1_f.get_center() + 0.6 * RIGHT)

        bond_f = Line(c1_f.get_center(), c2_f.get_center(), color=WHITE)

        # C2带正电荷
        plus_f = MathTex("+").scale(0.6).move_to(c2_f.get_top() + 0.2 * UP)

        # 甲基
        methyl_f = self.create_methyl_simple()
        methyl_f.move_to(c2_f.get_center() + 0.5 * RIGHT)

        # 氢原子
        h1_f = Circle(radius=0.1, color=WHITE, fill_opacity=0.8)
        h1_f.move_to(c1_f.get_center() + 0.4 * LEFT)

        h2_f = Circle(radius=0.1, color=WHITE, fill_opacity=0.8)
        h2_f.move_to(c1_f.get_center() + 0.4 * UP)

        h3_f = Circle(radius=0.1, color=WHITE, fill_opacity=0.8)
        h3_f.move_to(c1_f.get_center() + 0.4 * DOWN)

        h4_f = Circle(radius=0.1, color=WHITE, fill_opacity=0.8)
        h4_f.move_to(c2_f.get_center() + 0.4 * DOWN)

        final.add(c1_f, c2_f, bond_f, plus_f, methyl_f, h1_f, h2_f, h3_f, h4_f)
        final.move_to(3 * RIGHT)

        # 箭头
        arrow1 = Arrow(initial.get_right(), ts.get_left())
        arrow2 = Arrow(ts.get_right(), final.get_left())

        # 标签
        initial_label = Text("1° 碳正离子", font="STSong", font_size=20)
        initial_label.next_to(initial, DOWN, buff=0.5)

        ts_label = Text("氢迁移", font="STSong", font_size=20)
        ts_label.next_to(ts, DOWN, buff=0.5)

        final_label = Text("更稳定的2° 碳正离子", font="STSong", font_size=20)
        final_label.next_to(final, DOWN, buff=0.5)

        return VGroup(
            initial, arrow1, ts, arrow2, final,
            initial_label, ts_label, final_label
        )
