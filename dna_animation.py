from manim import *
import numpy as np
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from my_manim_setup import *

class DNACentralDogmaAntibiotics(Scene):
    def construct(self):
        # 标题动画
        self.show_title()

        # 第一部分：中心法则概述
        self.central_dogma_overview()

        # 第二部分：DNA结构与复制
        self.dna_structure_and_replication()

        # 第三部分：转录过程
        self.transcription_process()

        # 第四部分：翻译过程
        self.translation_process()

        # 第五部分：逆转录
        self.reverse_transcription()

        # 第六部分：抗生素原理
        self.antibiotic_principles()

        # 第七部分：抗生素作用机制
        self.antibiotic_mechanisms()

        # 第八部分：拓展内容
        self.extended_content()

    def show_title(self):
        # 主标题
        title = Text("分子生物学中心法则与抗生素原理", font="STSong", font_size=48)
        subtitle = Text("DNA逆转录、基因表达与药物作用机制", font="STSong", font_size=32)
        subtitle.next_to(title, DOWN, buff=0.5)

        self.play(Write(title), run_time=2)
        self.play(FadeIn(subtitle), run_time=1.5)
        self.wait(2)
        self.play(FadeOut(title), FadeOut(subtitle))

    def central_dogma_overview(self):
        # 中心法则示意图
        title = Text("中心法则概述", font="STSong", font_size=40)
        title.to_edge(UP)
        self.play(Write(title))

        # 创建流程图
        dna_box = RoundedRectangle(width=2, height=1, corner_radius=0.2, color=BLUE)
        dna_text = Text("DNA", font="STSong", font_size=24)
        dna_group = VGroup(dna_box, dna_text)

        rna_box = RoundedRectangle(width=2, height=1, corner_radius=0.2, color=GREEN)
        rna_text = Text("RNA", font="STSong", font_size=24)
        rna_group = VGroup(rna_box, rna_text)

        protein_box = RoundedRectangle(width=2, height=1, corner_radius=0.2, color=RED)
        protein_text = Text("蛋白质", font="STSong", font_size=24)
        protein_group = VGroup(protein_box, protein_text)

        # 排列位置
        dna_group.shift(LEFT * 4)
        rna_group.shift(ORIGIN)
        protein_group.shift(RIGHT * 4)

        # 箭头
        arrow1 = Arrow(dna_group.get_right(), rna_group.get_left(), buff=0.1)
        arrow1_text = Text("转录", font="STSong", font_size=20).next_to(arrow1, UP)

        arrow2 = Arrow(rna_group.get_right(), protein_group.get_left(), buff=0.1)
        arrow2_text = Text("翻译", font="STSong", font_size=20).next_to(arrow2, UP)

        # 逆转录箭头
        reverse_arrow = CurvedArrow(rna_group.get_left(), dna_group.get_right(),
                                    angle=-TAU / 4, color=YELLOW)
        reverse_text = Text("逆转录", font="STSong", font_size=20, color=YELLOW)
        reverse_text.next_to(reverse_arrow, DOWN)

        # 动画展示
        self.play(Create(dna_group), Create(rna_group), Create(protein_group))
        self.wait(1)
        self.play(Create(arrow1), Write(arrow1_text))
        self.play(Create(arrow2), Write(arrow2_text))
        self.wait(1)
        self.play(Create(reverse_arrow), Write(reverse_text))
        self.wait(2)

        # 添加说明文字
        explanation = Text(
            "中心法则描述了遗传信息的流动方向",
            font="STSong", font_size=24
        ).to_edge(DOWN)
        self.play(Write(explanation))
        self.wait(3)

        self.play(FadeOut(Group(*self.mobjects)))

    def dna_structure_and_replication(self):
        title = Text("DNA结构与复制", font="STSong", font_size=40)
        title.to_edge(UP)
        self.play(Write(title))

        # DNA双螺旋结构
        helix = self.create_dna_helix()
        self.play(Create(helix), run_time=3)
        self.wait(1)

        # 碱基配对说明
        base_pairs = VGroup()
        bases = [("A", "T", BLUE, RED), ("G", "C", GREEN, YELLOW)]
        for i, (b1, b2, c1, c2) in enumerate(bases):
            pair = VGroup(
                Text(b1, color=c1, font_size=30),
                Text("-", font_size=30),
                Text(b2, color=c2, font_size=30)
            ).arrange(RIGHT, buff=0.2)
            pair.shift(DOWN * 2 + RIGHT * (i * 3 - 1.5))
            base_pairs.add(pair)

        pair_text = Text("碱基互补配对", font="STSong", font_size=24)
        pair_text.next_to(base_pairs, DOWN)

        self.play(Create(base_pairs), Write(pair_text))
        self.wait(2)

        # DNA复制过程
        self.play(FadeOut(base_pairs), FadeOut(pair_text))

        # 解旋
        unwound_text = Text("DNA解旋", font="STSong", font_size=28)
        unwound_text.next_to(helix, DOWN, buff=1)
        self.play(Write(unwound_text))

        # 模拟解旋动画
        self.play(
            helix.animate.rotate(PI / 6, axis=UP),
            rate_func=there_and_back,
            run_time=2
        )

        # 复制叉
        fork_text = Text("形成复制叉", font="STSong", font_size=24)
        fork_text.next_to(unwound_text, DOWN)
        self.play(Write(fork_text))
        self.wait(2)

        self.play(FadeOut(Group(*self.mobjects)))

    def create_dna_helix(self):
        """创建DNA双螺旋结构"""
        helix = VGroup()
        n_turns = 3
        n_points = 100

        for i in range(2):
            strand = ParametricFunction(
                lambda t: np.array([
                    np.cos(2 * PI * n_turns * t) * (1 + 0.3 * i),
                    t * 4 - 2,
                    np.sin(2 * PI * n_turns * t) * (1 + 0.3 * i)
                ]),
                t_range=[0, 1],
                color=[BLUE, RED][i]
            )
            helix.add(strand)

        # 添加碱基对连接
        for t in np.linspace(0, 1, 20):
            y = t * 4 - 2
            x1 = np.cos(2 * PI * n_turns * t)
            z1 = np.sin(2 * PI * n_turns * t)
            x2 = np.cos(2 * PI * n_turns * t) * 1.3
            z2 = np.sin(2 * PI * n_turns * t) * 1.3

            line = Line(
                start=np.array([x1, y, z1]),
                end=np.array([x2, y, z2]),
                color=GRAY,
                stroke_width=2
            )
            helix.add(line)

        helix.scale(0.8)
        return helix

    def transcription_process(self):
        title = Text("转录过程", font="STSong", font_size=40)
        title.to_edge(UP)
        self.play(Write(title))

        # DNA模板链
        dna_template = self.create_dna_strand("DNA模板链", "3'-TACGGATCC-5'", BLUE)
        dna_template.shift(UP * 2)

        # RNA聚合酶
        rna_pol = Circle(radius=0.5, color=YELLOW, fill_opacity=0.7)
        rna_pol_text = Text("RNA\n聚合酶", font="STSong", font_size=16)
        rna_pol_group = VGroup(rna_pol, rna_pol_text)
        rna_pol_group.next_to(dna_template, LEFT, buff=1)

        self.play(Create(dna_template), Create(rna_pol_group))

        # RNA聚合酶移动
        self.play(
            rna_pol_group.animate.move_to(dna_template.get_left() + RIGHT * 0.5),
            run_time=2
        )

        # 生成mRNA
        mrna = self.create_dna_strand("mRNA", "5'-AUGCCUAGG-3'", GREEN)
        mrna.next_to(dna_template, DOWN, buff=0.5)

        # 逐步显示mRNA合成
        for i in range(len(mrna[1])):
            self.play(
                FadeIn(mrna[1][i]),
                rna_pol_group.animate.shift(RIGHT * 0.5),
                run_time=0.5
            )

        # 添加说明
        explanation = VGroup(
            Text("转录过程：", font="STSong", font_size=24),
            Text("• RNA聚合酶识别启动子", font="STSong", font_size=20),
            Text("• 解开DNA双链", font="STSong", font_size=20),
            Text("• 合成互补RNA链", font="STSong", font_size=20),
            Text("• 终止并释放mRNA", font="STSong", font_size=20)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        explanation.to_edge(DOWN).shift(UP * 0.5)

        self.play(Write(explanation), run_time=3)
        self.wait(3)

        self.play(FadeOut(Group(*self.mobjects)))

    def create_dna_strand(self, label, sequence, color):
        """创建DNA/RNA链"""
        strand = VGroup()
        label_text = Text(label, font="STSong", font_size=20, color=color)

        bases = VGroup()
        for i, base in enumerate(sequence):
            if base in "ATGCU":
                b = Text(base, font_size=24, color=color)
                b.shift(RIGHT * i * 0.5)
                bases.add(b)

        label_text.next_to(bases, LEFT, buff=0.5)
        strand.add(label_text, bases)
        return strand

    def translation_process(self):
        title = Text("翻译过程", font="STSong", font_size=40)
        title.to_edge(UP)
        self.play(Write(title))

        # 核糖体
        ribosome = self.create_ribosome()
        ribosome.shift(UP)

        # mRNA
        mrna = Line(LEFT * 4, RIGHT * 4, color=GREEN, stroke_width=4)
        mrna_label = Text("mRNA", font="STSong", font_size=20, color=GREEN)
        mrna_label.next_to(mrna, UP)

        # 密码子
        codons = ["AUG", "CCU", "AGG", "UAA"]
        codon_texts = VGroup()
        for i, codon in enumerate(codons):
            c_text = Text(codon, font_size=18, color=GREEN)
            c_text.move_to(mrna.get_left() + RIGHT * (i * 2 + 1))
            codon_texts.add(c_text)

        self.play(Create(ribosome), Create(mrna), Write(mrna_label))
        self.play(Write(codon_texts))

        # tRNA和氨基酸
        amino_acids = ["Met", "Pro", "Arg", "Stop"]

        for i, (codon, aa) in enumerate(zip(codons, amino_acids)):
            if aa != "Stop":
                # 创建tRNA
                trna = self.create_trna(aa)
                trna.move_to(ribosome.get_center() + UP * 2)

                # 移动核糖体
                self.play(
                    ribosome.animate.move_to(codon_texts[i].get_center()),
                    FadeIn(trna),
                    run_time=1
                )

                # 添加氨基酸到肽链
                aa_circle = Circle(radius=0.3, color=PURPLE, fill_opacity=0.7)
                aa_text = Text(aa, font_size=14)
                aa_group = VGroup(aa_circle, aa_text)
                aa_group.move_to(ribosome.get_center() + DOWN * 2 + RIGHT * i * 0.8)

                self.play(
                    Transform(trna, aa_group),
                    run_time=1
                )

                if i > 0:
                    # 连接肽键
                    peptide_bond = Line(
                        aa_group.get_left(),
                        aa_group.get_left() + LEFT * 0.8,
                        color=PURPLE
                    )
                    self.play(Create(peptide_bond), run_time=0.5)

        # 终止密码子说明
        stop_text = Text("终止密码子 - 翻译结束", font="STSong", font_size=24, color=RED)
        stop_text.to_edge(DOWN)
        self.play(Write(stop_text))
        self.wait(3)

        self.play(FadeOut(Group(*self.mobjects)))

    def create_ribosome(self):
        """创建核糖体模型"""
        large_subunit = Ellipse(width=2, height=1.5, color=GOLD, fill_opacity=0.5)
        small_subunit = Ellipse(width=1.8, height=1.2, color=GOLD_A, fill_opacity=0.5)
        small_subunit.shift(DOWN * 0.2)

        ribosome = VGroup(large_subunit, small_subunit)
        ribosome_text = Text("核糖体", font="STSong", font_size=20)
        ribosome_text.next_to(ribosome, RIGHT)

        return VGroup(ribosome, ribosome_text)

    def create_trna(self, amino_acid):
        """创建tRNA模型"""
        # tRNA形状
        points = [
            LEFT * 0.5,
            LEFT * 0.5 + UP * 0.8,
            RIGHT * 0.5 + UP * 0.8,
            RIGHT * 0.5
        ]
        trna_shape = VMobject(color=YELLOW, fill_opacity=0.3)
        trna_shape.set_points_as_corners(points)

        # 添加底部的反密码子
        anticodon = Text("反密码子", font="STSong", font_size=14)
        anticodon.next_to(trna_shape, DOWN, buff=0.1)

        # 添加氨基酸
        aa = Text(amino_acid, font_size=16, color=RED)
        aa.next_to(trna_shape, UP, buff=0.1)

        return VGroup(trna_shape, anticodon, aa)

    def reverse_transcription(self):
        title = Text("逆转录过程", font="STSong", font_size=40)
        title.to_edge(UP)
        self.play(Write(title))

        # 创建RNA模板
        rna_template = self.create_dna_strand("RNA模板", "5'-AUGGCCUAG-3'", GREEN)
        rna_template.shift(UP * 2)

        # 逆转录酶
        rt_enzyme = RoundedRectangle(width=1.5, height=1, corner_radius=0.2, color=YELLOW, fill_opacity=0.7)
        rt_text = Text("逆转录酶", font="STSong", font_size=20)
        rt_group = VGroup(rt_enzyme, rt_text)
        rt_group.next_to(rna_template, LEFT, buff=1)

        self.play(Create(rna_template), Create(rt_group))

        # 逆转录酶移动
        self.play(
            rt_group.animate.move_to(rna_template.get_left() + RIGHT * 0.5),
            run_time=2
        )

        # 生成cDNA
        cdna = self.create_dna_strand("cDNA", "3'-TACCGGATC-5'", BLUE)
        cdna.next_to(rna_template, DOWN, buff=0.5)

        # 逐步显示cDNA合成
        for i in range(len(cdna[1])):
            self.play(
                FadeIn(cdna[1][i]),
                rt_group.animate.shift(RIGHT * 0.5),
                run_time=0.5
            )

        # 添加逆转录病毒的例子
        virus_text = VGroup(
            Text("逆转录病毒示例：", font="STSong", font_size=24),
            Text("• HIV（艾滋病病毒）", font="STSong", font_size=20),
            Text("• HTLV（人类T细胞白血病病毒）", font="STSong", font_size=20)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        virus_text.to_edge(RIGHT).shift(DOWN)

        # 解释逆转录的意义
        explanation = VGroup(
            Text("逆转录的意义：", font="STSong", font_size=24),
            Text("• 病毒基因组整合入宿主DNA", font="STSong", font_size=20),
            Text("• 反转了中心法则的信息流", font="STSong", font_size=20),
            Text("• 在基因工程中用于构建cDNA文库", font="STSong", font_size=20)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        explanation.to_edge(LEFT).shift(DOWN * 2)

        self.play(Write(explanation), Write(virus_text), run_time=3)
        self.wait(3)

        self.play(FadeOut(Group(*self.mobjects)))

    def antibiotic_principles(self):
        title = Text("抗生素作用原理", font="STSong", font_size=40)
        title.to_edge(UP)
        self.play(Write(title))

        # 抗生素定义
        definition = Text(
            "抗生素是干扰细菌生命活动的化合物，通常用于治疗细菌感染",
            font="STSong", font_size=24
        )
        definition.next_to(title, DOWN, buff=0.5)

        self.play(Write(definition))
        self.wait(1)

        # 抗生素分类图
        classification = self.create_antibiotic_classification()
        classification.next_to(definition, DOWN, buff=1)

        self.play(Create(classification), run_time=3)

        # 抗生素作用靶点解释
        targets = VGroup(
            Text("抗生素主要靶点：", font="STSong", font_size=28),
            Text("1. 细胞壁合成", font="STSong", font_size=24),
            Text("2. 蛋白质合成", font="STSong", font_size=24),
            Text("3. 核酸合成", font="STSong", font_size=24),
            Text("4. 叶酸代谢", font="STSong", font_size=24),
            Text("5. 细胞膜结构", font="STSong", font_size=24)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        targets.to_edge(DOWN, buff=0.5)

        self.play(Write(targets), run_time=3)
        self.wait(3)

        self.play(FadeOut(Group(*self.mobjects)))

    def create_antibiotic_classification(self):
        """创建抗生素分类示意图"""
        # 主分类
        main_circle = Circle(radius=2, color=WHITE)
        main_text = Text("抗生素", font="STSong", font_size=30)

        # 子分类
        sub_circles = VGroup()
        categories = [
            ("β-内酰胺类", RED),
            ("氨基糖苷类", BLUE),
            ("大环内酯类", GREEN),
            ("四环素类", YELLOW),
            ("喹诺酮类", PURPLE)
        ]

        for i, (name, color) in enumerate(categories):
            angle = i * TAU / len(categories)
            sub_circle = Circle(radius=0.8, color=color, fill_opacity=0.3)
            sub_circle.move_to(main_circle.get_center() + 2.5 * RIGHT * np.cos(angle) + 2.5 * UP * np.sin(angle))

            sub_text = Text(name, font="STSong", font_size=20)
            sub_text.move_to(sub_circle.get_center())

            line = Line(main_circle.get_center(), sub_circle.get_center(), color=color)

            sub_circles.add(VGroup(sub_circle, sub_text, line))

        return VGroup(main_circle, main_text, sub_circles)

    def antibiotic_mechanisms(self):
        title = Text("抗生素作用机制", font="STSong", font_size=40)
        title.to_edge(UP)
        self.play(Write(title))

        # 创建细菌细胞模型
        cell = self.create_bacterial_cell()
        cell.scale(0.8).shift(UP * 0.5)

        self.play(Create(cell), run_time=2)

        # 蛋白质合成抑制
        self.explain_protein_synthesis_inhibition(cell)

        # 细胞壁合成抑制
        self.explain_cell_wall_inhibition(cell)

        # 核酸合成抑制
        self.explain_nucleic_acid_inhibition(cell)

        # 抗生素耐药性问题
        resistance_title = Text("抗生素耐药性问题", font="STSong", font_size=32, color=RED)
        resistance_title.to_edge(DOWN, buff=2)

        resistance_mechanisms = VGroup(
            Text("• 酶促降解", font="STSong", font_size=24),
            Text("• 外排泵增加", font="STSong", font_size=24),
            Text("• 靶点变异", font="STSong", font_size=24),
            Text("• 细胞通透性降低", font="STSong", font_size=24)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        resistance_mechanisms.next_to(resistance_title, DOWN)

        self.play(Write(resistance_title), run_time=1)
        self.play(Write(resistance_mechanisms), run_time=3)
        self.wait(3)

        self.play(FadeOut(Group(*self.mobjects)))

    def create_bacterial_cell(self):
        """创建细菌细胞模型"""
        # 细胞轮廓
        cell_membrane = Circle(radius=3, color=BLUE, fill_opacity=0.1)

        # 细胞壁
        cell_wall = DashedVMobject(
            Circle(radius=3.2, color=GREEN, fill_opacity=0)
        )

        # 细胞核区（细菌无真正细胞核）
        nucleoid = Circle(radius=1, color=YELLOW, fill_opacity=0.3)

        # 核糖体
        ribosomes = VGroup()
        for _ in range(15):
            r = Dot(color=RED)
            r.move_to(
                cell_membrane.get_center() +
                np.random.uniform(-2.5, 2.5) * RIGHT +
                np.random.uniform(-2.5, 2.5) * UP
            )
            ribosomes.add(r)

        # 标签
        labels = VGroup(
            Text("细胞壁", font="STSong", font_size=16).next_to(cell_wall, UP, buff=0.2),
            Text("细胞膜", font="STSong", font_size=16).next_to(cell_membrane, LEFT, buff=0.2),
            Text("核区", font="STSong", font_size=16).move_to(nucleoid),
            Text("核糖体", font="STSong", font_size=16).next_to(cell_membrane, RIGHT, buff=0.5)
        )

        return VGroup(cell_wall, cell_membrane, nucleoid, ribosomes, labels)

    def explain_protein_synthesis_inhibition(self, cell):
        """解释蛋白质合成抑制机制"""
        title = Text("蛋白质合成抑制", font="STSong", font_size=28, color=YELLOW)
        title.to_edge(LEFT).shift(DOWN * 0.5)

        # 标记核糖体
        ribosome_highlight = Circle(radius=0.5, color=YELLOW).move_to(cell[3][0].get_center())

        # 抗生素示例
        examples = VGroup(
            Text("四环素类 - 阻止tRNA与核糖体结合", font="STSong", font_size=20),
            Text("氨基糖苷类 - 干扰mRNA解码", font="STSong", font_size=20),
            Text("大环内酯类 - 阻断肽链延长", font="STSong", font_size=20)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        examples.next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(ribosome_highlight))
        self.play(Write(examples), run_time=2)
        self.wait(1)

        self.play(FadeOut(title), FadeOut(examples), FadeOut(ribosome_highlight))

    def explain_cell_wall_inhibition(self, cell):
        """解释细胞壁合成抑制机制"""
        title = Text("细胞壁合成抑制", font="STSong", font_size=28, color=GREEN)
        title.to_edge(LEFT).shift(DOWN * 0.5)

        # 标记细胞壁
        wall_highlight = Circle(radius=3.3, color=GREEN, stroke_width=5).move_to(cell[0].get_center())

        # 抗生素示例
        examples = VGroup(
            Text("青霉素类 - 抑制肽聚糖交联", font="STSong", font_size=20),
            Text("头孢菌素类 - 干扰细胞壁合成", font="STSong", font_size=20),
            Text("万古霉素 - 阻断肽聚糖前体合成", font="STSong", font_size=20)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        examples.next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(wall_highlight))
        self.play(Write(examples), run_time=2)
        self.wait(1)

        self.play(FadeOut(title), FadeOut(examples), FadeOut(wall_highlight))

    def explain_nucleic_acid_inhibition(self, cell):
        """解释核酸合成抑制机制"""
        title = Text("核酸合成抑制", font="STSong", font_size=28, color=BLUE)
        title.to_edge(LEFT).shift(DOWN * 0.5)

        # 标记核区
        nucleoid_highlight = Circle(radius=1.2, color=BLUE, stroke_width=5).move_to(cell[2].get_center())

        # 抗生素示例
        examples = VGroup(
            Text("喹诺酮类 - 抑制DNA螺旋酶", font="STSong", font_size=20),
            Text("利福平 - 抑制RNA聚合酶", font="STSong", font_size=20),
            Text("磺胺类 - 抑制叶酸合成", font="STSong", font_size=20)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        examples.next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(nucleoid_highlight))
        self.play(Write(examples), run_time=2)
        self.wait(1)

        self.play(FadeOut(title), FadeOut(examples), FadeOut(nucleoid_highlight))

    def extended_content(self):
        title = Text("拓展内容：分子生物学技术与药物开发", font="STSong", font_size=40)
        title.to_edge(UP)
        self.play(Write(title))

        # PCR技术
        self.explain_pcr_technique()

        # CRISPR基因编辑
        self.explain_crispr()

        # 新型抗生素开发
        self.explain_new_antibiotics()

        # 总结
        self.create_summary()

    def explain_pcr_technique(self):
        """解释PCR技术"""
        title = Text("PCR技术", font="STSong", font_size=32)
        title.shift(UP * 2)

        self.play(Write(title))

        # PCR原理图
        pcr_steps = VGroup()

        # 变性
        denaturation = RoundedRectangle(width=2, height=1, corner_radius=0.2, color=RED)
        denat_text = Text("变性\n95°C", font="STSong", font_size=20)
        denat_group = VGroup(denaturation, denat_text)

        # 退火
        annealing = RoundedRectangle(width=2, height=1, corner_radius=0.2, color=BLUE)
        anneal_text = Text("退火\n55°C", font="STSong", font_size=20)
        anneal_group = VGroup(annealing, anneal_text)

        # 延伸
        extension = RoundedRectangle(width=2, height=1, corner_radius=0.2, color=GREEN)
        ext_text = Text("延伸\n72°C", font="STSong", font_size=20)
        ext_group = VGroup(extension, ext_text)

        # 排列步骤
        pcr_steps.add(denat_group, anneal_group, ext_group)
        pcr_steps.arrange(RIGHT, buff=1)
        pcr_steps.next_to(title, DOWN, buff=0.5)

        # 添加箭头
        arrows = VGroup()
        for i in range(len(pcr_steps) - 1):
            arrow = Arrow(
                pcr_steps[i].get_right(),
                pcr_steps[i + 1].get_left(),
                buff=0.1
            )
            arrows.add(arrow)

        # 循环箭头
        cycle_arrow = CurvedArrow(
            pcr_steps[-1].get_right(),
            pcr_steps[0].get_left(),
            angle=-TAU / 4
        )
        cycle_text = Text("30-40个循环", font="STSong", font_size=18)
        cycle_text.next_to(cycle_arrow, DOWN)

        self.play(Create(pcr_steps), Create(arrows))
        self.play(Create(cycle_arrow), Write(cycle_text))

        # PCR应用
        applications = VGroup(
            Text("PCR应用：", font="STSong", font_size=24),
            Text("• DNA扩增", font="STSong", font_size=20),
            Text("• 分子诊断", font="STSong", font_size=20),
            Text("• 基因克隆", font="STSong", font_size=20),
            Text("• 法医DNA分析", font="STSong", font_size=20)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        applications.to_edge(DOWN, buff=0.5)

        self.play(Write(applications), run_time=2)
        self.wait(2)

        self.play(FadeOut(Group(*self.mobjects, title)))

    def explain_crispr(self):
        """解释CRISPR基因编辑技术"""
        title = Text("CRISPR基因编辑", font="STSong", font_size=32)
        title.to_edge(UP)

        self.play(Write(title))

        # 创建CRISPR-Cas9系统模型
        dna = Line(LEFT * 4, RIGHT * 4, color=BLUE, stroke_width=4)
        dna_label = Text("靶向DNA", font="STSong", font_size=20, color=BLUE)
        dna_label.next_to(dna, UP)

        # 使用Arc代替CurvedLine
        guide_rna = Arc(
            start_angle=PI,
            angle=-PI,
            radius=1.5,
            color=GREEN
        )
        guide_rna.shift(UP * 0.5)  # 将弧线向上移动一点

        grna_label = Text("引导RNA", font="STSong", font_size=20, color=GREEN)
        grna_label.next_to(guide_rna, UP)

        cas9 = Circle(radius=1, color=RED, fill_opacity=0.5)
        cas9.move_to(guide_rna.get_center() + UP * 0.5)
        cas9_label = Text("Cas9蛋白", font="STSong", font_size=20, color=RED)
        cas9_label.next_to(cas9, RIGHT)

        crispr_system = VGroup(dna, dna_label, guide_rna, grna_label, cas9, cas9_label)
        crispr_system.scale(0.8).shift(UP * 0.5)

        self.play(Create(crispr_system), run_time=2)

        # CRISPR工作原理
        explanation = VGroup(
            Text("CRISPR-Cas9工作原理：", font="STSong", font_size=24),
            Text("1. 引导RNA识别特定DNA序列", font="STSong", font_size=20),
            Text("2. Cas9蛋白切割DNA", font="STSong", font_size=20),
            Text("3. 细胞修复机制可引入修改", font="STSong", font_size=20)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        explanation.to_edge(LEFT).shift(DOWN * 1.5)

        self.play(Write(explanation), run_time=2)

        # CRISPR应用
        applications = VGroup(
            Text("应用前景：", font="STSong", font_size=24),
            Text("• 基因治疗", font="STSong", font_size=20),
            Text("• 农作物改良", font="STSong", font_size=20),
            Text("• 模式生物研究", font="STSong", font_size=20),
            Text("• 感染性疾病治疗", font="STSong", font_size=20)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        applications.to_edge(RIGHT).shift(DOWN * 1.5)

        self.play(Write(applications), run_time=2)
        self.wait(2)

        self.play(FadeOut(Group(*self.mobjects)))

    def explain_new_antibiotics(self):
        """解释新型抗生素开发"""
        title = Text("新型抗生素开发", font="STSong", font_size=32)
        title.to_edge(UP)

        self.play(Write(title))

        # 创建新型抗生素开发流程
        flow_chart = self.create_drug_development_flowchart()
        flow_chart.next_to(title, DOWN, buff=0.5)

        self.play(Create(flow_chart), run_time=3)

        # 新型靶点
        targets = VGroup(
            Text("新型抗菌靶点：", font="STSong", font_size=24),
            Text("• 细菌毒力因子", font="STSong", font_size=20),
            Text("• 生物膜形成", font="STSong", font_size=20),
            Text("• 细菌通讯系统", font="STSong", font_size=20),
            Text("• CRISPR-Cas系统", font="STSong", font_size=20)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        targets.to_edge(LEFT).shift(DOWN * 1.5)

        self.play(Write(targets), run_time=2)

        # 新型策略
        strategies = VGroup(
            Text("创新策略：", font="STSong", font_size=24),
            Text("• 噬菌体疗法", font="STSong", font_size=20),
            Text("• 抗菌肽", font="STSong", font_size=20),
            Text("• 抗生素联合用药", font="STSong", font_size=20),
            Text("• 药物递送系统", font="STSong", font_size=20)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        strategies.to_edge(RIGHT).shift(DOWN * 1.5)

        self.play(Write(strategies), run_time=2)
        self.wait(2)

        self.play(FadeOut(Group(*self.mobjects)))

    def create_drug_development_flowchart(self):
        """创建药物开发流程图"""
        # 创建各阶段框
        stages = ["靶点发现", "先导化合物筛选", "药物优化", "临床前研究", "临床试验", "批准上市"]
        boxes = VGroup()

        for i, stage in enumerate(stages):
            box = RoundedRectangle(width=2, height=0.8, corner_radius=0.2)
            text = Text(stage, font="STSong", font_size=18)
            text.move_to(box.get_center())

            group = VGroup(box, text)

            if i < 3:  # 前三个水平排列
                group.shift(RIGHT * (i - 1) * 3)
            else:  # 后三个水平排列，在下一行
                group.shift(RIGHT * (i - 4) * 3 + DOWN * 2)

            boxes.add(group)

        # 添加连接箭头
        arrows = VGroup()
        # 连接前三个框
        for i in range(2):
            arrow = Arrow(
                boxes[i].get_right(),
                boxes[i + 1].get_left(),
                buff=0.1
            )
            arrows.add(arrow)

        # 从第三个框到第四个框（跨行）
        down_arrow = Arrow(
            boxes[2].get_bottom(),
            boxes[3].get_top(),
            buff=0.1
        )
        arrows.add(down_arrow)

        # 连接后三个框
        for i in range(3, 5):
            arrow = Arrow(
                boxes[i].get_right(),
                boxes[i + 1].get_left(),
                buff=0.1
            )
            arrows.add(arrow)

        return VGroup(boxes, arrows)

    def create_summary(self):
        """创建总结页面"""
        title = Text("总结", font="STSong", font_size=40)
        title.to_edge(UP)

        self.play(Write(title))

        # 创建总结内容
        summary = VGroup(
            Text("1. 中心法则描述了遗传信息从DNA到RNA再到蛋白质的流动", font="STSong", font_size=24),
            Text("2. 逆转录是RNA向DNA信息流动的特殊机制", font="STSong", font_size=24),
            Text("3. 抗生素通过干扰细菌生命过程发挥作用", font="STSong", font_size=24),
            Text("4. 分子生物学技术促进了基础研究和药物开发", font="STSong", font_size=24),
            Text("5. 抗生素耐药性是全球面临的重大挑战", font="STSong", font_size=24)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        summary.next_to(title, DOWN, buff=1)

        self.play(Write(summary), run_time=3)

        # 结束语
        conclusion = Text(
            "分子生物学与药物研发的交叉，将持续推动人类健康事业的发展",
            font="STSong", font_size=28, color=YELLOW
        )
        conclusion.to_edge(DOWN, buff=1)

        self.play(Write(conclusion), run_time=2)
        self.wait(3)

        # 渐变消失
        self.play(FadeOut(Group(*self.mobjects)))


class DNAStructure3D(ThreeDScene):
    def construct(self):
        # 标题
        title = Text("DNA三维结构", font="STSong", font_size=40)
        title.to_edge(UP)
        self.add_fixed_in_frame_mobjects(title)
        self.play(Write(title))

        # 设置3D视角
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        self.begin_ambient_camera_rotation(rate=0.1)

        # 创建DNA双螺旋
        dna = self.create_3d_dna_helix()
        self.play(Create(dna), run_time=3)

        # 添加说明
        explanation = VGroup(
            Text("DNA双螺旋特点：", font="STSong", font_size=24),
            Text("• 右手螺旋", font="STSong", font_size=20),
            Text("• 直径约2nm", font="STSong", font_size=20),
            Text("• 每转约10个碱基对", font="STSong", font_size=20),
            Text("• 大沟和小沟结构", font="STSong", font_size=20)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        explanation.to_edge(DOWN).shift(UP * 0.5)

        self.add_fixed_in_frame_mobjects(explanation)
        self.play(Write(explanation), run_time=2)

        # 旋转展示DNA结构
        self.wait(5)

        # 展示不同视角 - 使用move_camera而不是camera.animate
        self.move_camera(phi=45 * DEGREES, theta=90 * DEGREES, run_time=2)
        self.wait(2)

        self.move_camera(phi=90 * DEGREES, theta=0 * DEGREES, run_time=2)
        self.wait(2)

        self.stop_ambient_camera_rotation()
        self.wait(1)

        # 退出
        self.play(FadeOut(dna))
        self.play(FadeOut(explanation), FadeOut(title))

    def create_3d_dna_helix(self):
        """创建3D DNA双螺旋结构"""
        dna = VGroup()

        # 参数
        height = 6
        radius = 1
        turns = 3
        n_bases = 30

        # 创建两条DNA链
        for strand_idx in range(2):
            strand = VGroup()

            # 使用小圆球表示主链上的磷酸
            for i in range(40):
                t = i / 39
                angle = turns * TAU * t
                if strand_idx == 1:
                    angle += PI  # 第二条链偏移180度

                x = radius * np.cos(angle)
                y = height * (t - 0.5)  # 中心在原点
                z = radius * np.sin(angle)

                phosphate = Sphere(radius=0.15)
                phosphate.set_color([BLUE, RED][strand_idx])
                phosphate.move_to([x, y, z])

                strand.add(phosphate)

            # 添加碱基表示
            for i in range(n_bases):
                t = i / (n_bases - 1)
                angle = turns * TAU * t
                if strand_idx == 1:
                    angle += PI

                x = radius * np.cos(angle)
                y = height * (t - 0.5)
                z = radius * np.sin(angle)

                # 向内部延伸的柱体表示碱基
                inner_x = 0.5 * radius * np.cos(angle)
                inner_z = 0.5 * radius * np.sin(angle)

                # 计算方向向量
                direction = np.array([inner_x - x, 0, inner_z - z])
                length = np.linalg.norm(direction)
                if length > 0:
                    direction = direction / length

                # 创建柱体
                base = Cylinder(height=length * radius * 0.5, radius=0.05)
                base.set_color(GRAY)

                # 定位和旋转柱体
                base.move_to([x + (inner_x - x) / 2, y, z + (inner_z - z) / 2])

                # 计算旋转轴和角度
                axis = np.cross([0, 1, 0], direction)
                angle = np.arccos(np.dot([0, 1, 0], direction))
                if np.linalg.norm(axis) > 0:
                    base.rotate(angle, axis)

                strand.add(base)

            dna.add(strand)

        # 添加碱基对连接
        for i in range(n_bases):
            t = i / (n_bases - 1)
            angle1 = turns * TAU * t
            angle2 = angle1 + PI

            y = height * (t - 0.5)

            inner_x1 = 0.5 * radius * np.cos(angle1)
            inner_z1 = 0.5 * radius * np.sin(angle1)

            inner_x2 = 0.5 * radius * np.cos(angle2)
            inner_z2 = 0.5 * radius * np.sin(angle2)

            # 创建小球表示碱基对连接
            base_pair_sphere = Sphere(radius=0.08)
            base_pair_sphere.set_color(GREEN)
            base_pair_sphere.move_to([(inner_x1 + inner_x2) / 2, y, (inner_z1 + inner_z2) / 2])

            dna.add(base_pair_sphere)

        return dna


class AntibioticResistance3D(ThreeDScene):
    def construct(self):
        # 标题
        title = Text("抗生素耐药性的分子机制", font="STSong", font_size=36)
        title.to_edge(UP)
        self.add_fixed_in_frame_mobjects(title)
        self.play(Write(title))

        # 设置3D视角
        self.set_camera_orientation(phi=60 * DEGREES, theta=45 * DEGREES)

        # 创建细菌细胞的3D模型
        cell = self.create_3d_bacterial_cell()
        cell.scale(0.8)

        self.play(Create(cell), run_time=2)

        # 展示几种耐药机制
        self.show_enzymatic_degradation(cell)
        self.show_efflux_pump(cell)
        self.show_target_modification(cell)

        # 最后的总结
        summary = Text("抗生素耐药性威胁公共健康，需要开发新型药物和合理用药",
                       font="STSong", font_size=24)
        summary.to_edge(DOWN)

        self.add_fixed_in_frame_mobjects(summary)
        self.play(Write(summary), run_time=2)
        self.wait(2)

        # 退出
        self.play(FadeOut(cell))
        self.play(FadeOut(summary), FadeOut(title))

    def create_3d_bacterial_cell(self):
        """创建3D细菌细胞模型"""
        cell = VGroup()

        # 细胞膜 - 使用球体
        membrane = Sphere(radius=2, resolution=(20, 20))
        membrane.set_fill(BLUE, opacity=0.1)
        membrane.set_stroke(BLUE, opacity=0.5, width=1)

        # 细胞质内的DNA区域
        dna_region = Sphere(radius=0.8, resolution=(20, 20))
        dna_region.set_fill(YELLOW, opacity=0.3)
        dna_region.set_stroke(YELLOW, opacity=0.5, width=1)

        # 核糖体 - 随机放置的小球
        ribosomes = VGroup()
        for _ in range(20):
            r = 0.2 + 0.6 * np.random.random()  # 距离细胞中心的半径
            theta = np.random.uniform(0, 2 * PI)
            phi = np.random.uniform(0, PI)

            x = r * np.sin(phi) * np.cos(theta)
            y = r * np.sin(phi) * np.sin(theta)
            z = r * np.cos(phi)

            ribosome = Dot3D(point=[x, y, z], color=RED)
            ribosomes.add(ribosome)

        cell.add(membrane, dna_region, ribosomes)
        return cell

    def show_enzymatic_degradation(self, cell):
        """展示酶促降解机制"""
        title = Text("β-内酰胺酶降解抗生素", font="STSong", font_size=28)
        title.to_edge(LEFT).shift(UP * 0.5)

        self.add_fixed_in_frame_mobjects(title)
        self.play(Write(title))

        # 创建β-内酰胺酶
        enzyme = Prism(dimensions=[0.5, 0.5, 0.5])
        enzyme.set_fill(GREEN, opacity=0.8)
        enzyme.move_to([1.5, 0, 0])

        # 抗生素分子
        antibiotic = Sphere(radius=0.2)
        antibiotic.set_fill(PURPLE, opacity=0.8)
        antibiotic.move_to([3, 0, 0])

        self.play(Create(enzyme), Create(antibiotic))

        # 抗生素接近酶
        self.play(
            antibiotic.animate.move_to([1.8, 0, 0]),
            run_time=2
        )

        # 抗生素被降解
        degraded = VGroup()
        for i in range(5):
            frag = Dot3D(point=[
                1.8 + 0.3 * np.random.random(),
                0.3 * np.random.random() - 0.15,
                0.3 * np.random.random() - 0.15
            ], color=PURPLE, radius=0.05)
            degraded.add(frag)

        self.play(
            Transform(antibiotic, degraded),
            run_time=1.5
        )

        # 解释
        explanation = Text(
            "细菌产生β-内酰胺酶可以水解β-内酰胺抗生素的β-内酰胺环",
            font="STSong", font_size=20
        )
        explanation.to_edge(DOWN).shift(UP * 0.5)

        self.add_fixed_in_frame_mobjects(explanation)
        self.play(Write(explanation))
        self.wait(2)

        self.play(FadeOut(enzyme), FadeOut(antibiotic))
        self.play(FadeOut(explanation), FadeOut(title))

    def show_efflux_pump(self, cell):
        """展示外排泵机制"""
        title = Text("外排泵机制", font="STSong", font_size=28)
        title.to_edge(LEFT).shift(UP * 0.5)

        self.add_fixed_in_frame_mobjects(title)
        self.play(Write(title))

        # 创建细胞膜上的外排泵
        pump_base = Cylinder(radius=0.3, height=0.6)
        pump_base.set_fill(ORANGE, opacity=0.8)
        pump_base.move_to([0, 2, 0])

        # 让泵的方向垂直于细胞表面
        pump_base.rotate(PI / 2, RIGHT)

        self.play(Create(pump_base))

        # 抗生素分子
        antibiotics = VGroup()
        for i in range(3):
            ab = Sphere(radius=0.15)
            ab.set_fill(PURPLE, opacity=0.8)
            ab.move_to([
                -0.5 + i * 0.5,
                1,
                0
            ])
            antibiotics.add(ab)

        self.play(Create(antibiotics))

        # 抗生素被泵出细胞
        for i, ab in enumerate(antibiotics):
            self.play(
                ab.animate.move_to([0, 1.5, 0]),
                run_time=1
            )

            self.play(
                ab.animate.move_to([0, 3 + i * 0.5, 0]),
                run_time=1
            )

        # 解释
        explanation = Text(
            "外排泵可以主动将抗生素从细菌细胞内泵出，降低细胞内抗生素浓度",
            font="STSong", font_size=20
        )
        explanation.to_edge(DOWN).shift(UP * 0.5)

        self.add_fixed_in_frame_mobjects(explanation)
        self.play(Write(explanation))
        self.wait(2)

        self.play(FadeOut(pump_base), FadeOut(antibiotics))
        self.play(FadeOut(explanation), FadeOut(title))

    def show_target_modification(self, cell):
        """展示靶点修饰机制"""
        title = Text("靶点修饰机制", font="STSong", font_size=28)
        title.to_edge(LEFT).shift(UP * 0.5)

        self.add_fixed_in_frame_mobjects(title)
        self.play(Write(title))

        # 创建正常靶点
        target = Cube(side_length=0.5)
        target.set_fill(BLUE, opacity=0.8)
        target.move_to([0, 0, 1])

        # 抗生素分子
        antibiotic = Sphere(radius=0.2)
        antibiotic.set_fill(PURPLE, opacity=0.8)
        antibiotic.move_to([1, 0, 1])

        self.play(Create(target), Create(antibiotic))

        # 抗生素与靶点结合
        self.play(
            antibiotic.animate.move_to([0.25, 0, 1]),
            run_time=1.5
        )

        # 靶点变异
        mutated_target = Cube(side_length=0.5)
        mutated_target.set_fill(RED, opacity=0.8)
        mutated_target.move_to([0, 0, 1])

        self.play(
            Transform(target, mutated_target),
            antibiotic.animate.move_to([1, 0, 1]),
            run_time=2
        )

        # 抗生素无法与变异靶点结合
        self.play(
            antibiotic.animate.move_to([0.5, 0, 1]),
            run_time=1.5
        )
        self.play(
            antibiotic.animate.move_to([1, 0, 1]),
            run_time=1.5
        )

        # 解释
        explanation = Text(
            "靶点突变可改变抗生素的结合位点，使抗生素无法有效结合并发挥作用",
            font="STSong", font_size=20
        )
        explanation.to_edge(DOWN).shift(UP * 0.5)

        self.add_fixed_in_frame_mobjects(explanation)
        self.play(Write(explanation))
        self.wait(2)

        self.play(FadeOut(target), FadeOut(antibiotic))
        self.play(FadeOut(explanation), FadeOut(title))