from manim import *
import numpy as np
import random

import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from my_manim_setup import *


# 自定义替代函数，替换SVGMobject的功能
def SafeSVGMobject(filename, height=2, *args, **kwargs):
    # 忽略文件名，总是返回简单图形
    if "human" in filename.lower():
        # 人形轮廓
        return VGroup(
            Circle(radius=0.5).shift(UP * 1.5),  # 头
            Line(UP * 1, DOWN * 1),  # 身体
            Line(UP * 0.5, UP * 0.5 + LEFT),  # 左臂
            Line(UP * 0.5, UP * 0.5 + RIGHT),  # 右臂
            Line(DOWN * 1, DOWN * 2 + LEFT * 0.5),  # 左腿
            Line(DOWN * 1, DOWN * 2 + RIGHT * 0.5)  # 右腿
        ).scale(height / 4)
    else:
        # 其他SVG文件的通用替代形状
        return Circle(radius=height / 2)


# 自定义替代函数，替换ImageMobject的功能
def SafeImageMobject(filename, height=2, *args, **kwargs):
    # 根据文件名返回不同的替代图形
    if "xray" in filename.lower() or "dna_xray" in filename.lower():
        # X射线衍射图案替代
        circle = Circle(radius=1.5).set_fill(WHITE, opacity=0.2)
        # 添加十字形衍射图案
        x_ray_pattern = VGroup(
            Line(UP, DOWN, color=WHITE),
            Line(LEFT, RIGHT, color=WHITE),
            *[Line(ORIGIN, unit_vector, color=WHITE) for unit_vector in
              [UP + RIGHT, UP + LEFT, DOWN + RIGHT, DOWN + LEFT]]
        )
        result = VGroup(circle, x_ray_pattern)
    else:
        # 通用图像替代
        result = Rectangle(height=2, width=3, color=WHITE).set_fill(WHITE, opacity=0.2)
        result.add(Text("图像替代", font="SimHei").scale(0.5).move_to(result.get_center()))

    # 应用高度缩放
    result.scale(height / 3)
    return result


# 替换原始的SVGMobject和ImageMobject类
OriginalSVGMobject = SVGMobject
OriginalImageMobject = ImageMobject
SVGMobject = SafeSVGMobject
ImageMobject = SafeImageMobject

# 设置中文字体支持
config.text_font = "SimHei"

# 主要颜色定义
DNA_COLOR = "#3498db"
RNA_COLOR = "#e74c3c"
PROTEIN_COLOR = "#2ecc71"
CHROMOSOME_COLOR = "#9b59b6"
BACKGROUND_COLOR = "#000000"  # 黑色背景


class GeneExpressionAnimation(Scene):
    def construct(self):
        # 设置背景颜色
        self.camera.background_color = BACKGROUND_COLOR

        # 播放引言
        self.play_introduction()

        # 播放各个章节
        self.play_mendel_laws()
        self.play_gene_chromosome()
        self.play_dna_structure()
        self.play_dna_replication()
        self.play_molecular_techniques()
        self.play_gene_expression()
        self.play_gene_regulation()
        self.play_genotype_phenotype()
        self.play_extended_content()

        # 播放结语
        self.play_conclusion()

    def play_introduction(self):
        """引言部分动画"""
        # 创建星空背景
        stars = VGroup()
        for _ in range(200):
            pos = np.array([random.uniform(-7, 7), random.uniform(-4, 4), 0])
            star = Dot(pos, radius=random.uniform(0.005, 0.02), color=WHITE)
            stars.add(star)

        self.play(FadeIn(stars, run_time=2))

        # 创建地球
        earth = Circle(radius=2, color=BLUE).set_fill(BLUE, opacity=0.8)
        earth_details = VGroup(
            Arc(radius=1.5, angle=PI / 4, color=GREEN).set_fill(GREEN, opacity=0.6),
            Arc(radius=1.7, angle=PI / 3, color=GREEN).set_fill(GREEN, opacity=0.6).shift(RIGHT * 0.5),
            Arc(radius=1.3, angle=PI / 5, color=GREEN).set_fill(GREEN, opacity=0.6).shift(LEFT * 0.7)
        )
        earth_group = VGroup(earth, earth_details)

        self.play(FadeIn(earth_group, run_time=2))

        # 缩放到人体
        human_outline = SVGMobject("human_outline.svg", height=4)  # 假设有此SVG文件
        # 如果没有SVG，可以用简单形状代替
        if not os.path.exists("human_outline.svg"):
            human_outline = VGroup(
                Circle(radius=0.5).shift(UP * 1.5),  # 头
                Line(UP * 1, DOWN * 1),  # 身体
                Line(UP * 0.5, UP * 0.5 + LEFT),  # 左臂
                Line(UP * 0.5, UP * 0.5 + RIGHT),  # 右臂
                Line(DOWN * 1, DOWN * 2 + LEFT * 0.5),  # 左腿
                Line(DOWN * 1, DOWN * 2 + RIGHT * 0.5)  # 右腿
            )

        self.play(
            FadeOut(stars),
            Transform(earth_group, human_outline),
            run_time=3
        )

        # 放大到细胞
        cell = Circle(radius=2, color=WHITE).set_fill(opacity=0.2)
        nucleus = Circle(radius=0.8, color=BLUE_D).set_fill(BLUE_D, opacity=0.4)
        cell_group = VGroup(cell, nucleus)

        self.play(
            Transform(earth_group, cell_group),
            run_time=2
        )

        # 显示DNA双螺旋
        dna = self.create_dna_helix(num_rungs=10)

        self.play(
            FadeOut(earth_group),
            FadeIn(dna),
            run_time=2
        )

        # 旋转DNA同时显示标题
        title = Text("生命的密码：基因表达全过程", font="SimHei").scale(1.2)
        subtitle = Text("从DNA到性状的奇妙旅程", font="SimHei").scale(0.8).next_to(title, DOWN)
        title_group = VGroup(title, subtitle).to_edge(UP)

        self.play(
            Rotate(dna, angle=2 * PI, axis=UP, run_time=5),
            FadeIn(title_group, run_time=2)
        )

        # 引言文字
        intro_text = Text(
            "生命，这个宇宙中最神奇的现象，其奥秘隐藏在每个生物的细胞核中。\n"
            "今天，我们将带您踏上一段穿越时空的旅程，揭示从基因到性状的完整过程，\n"
            "理解生命传递的密码。",
            font="SimHei",
            line_spacing=0.5
        ).scale(0.6).to_edge(DOWN, buff=1)

        self.play(Write(intro_text, run_time=3))
        self.wait(2)

        self.play(
            FadeOut(dna),
            FadeOut(title_group),
            FadeOut(intro_text),
            run_time=1
        )

    def create_dna_helix(self, num_rungs=10, width=0.6, height=0.2, helix_radius=1):
        """创建DNA双螺旋结构"""
        dna = VGroup()

        # 创建两条螺旋骨架
        strand1_points = []
        strand2_points = []

        for i in np.linspace(0, num_rungs * PI / 2, 100):
            x1 = helix_radius * np.cos(i)
            y1 = i / (num_rungs * PI / 2) * 4 - 2
            z1 = helix_radius * np.sin(i)

            x2 = helix_radius * np.cos(i + PI)
            y2 = y1
            z2 = helix_radius * np.sin(i + PI)

            strand1_points.append([x1, y1, 0])
            strand2_points.append([x2, y2, 0])

        strand1 = VMobject(color=BLUE)
        strand1.set_points_as_corners(strand1_points)

        strand2 = VMobject(color=RED)
        strand2.set_points_as_corners(strand2_points)

        dna.add(strand1, strand2)

        # 添加碱基对
        for i in range(num_rungs):
            y = i / (num_rungs - 1) * 4 - 2

            angle = i * PI / 2
            x1 = helix_radius * np.cos(angle)
            z1 = helix_radius * np.sin(angle)

            x2 = helix_radius * np.cos(angle + PI)
            z2 = helix_radius * np.sin(angle + PI)

            rung = Line(
                [x1, y, 0],
                [x2, y, 0],
                color=YELLOW
            )

            # 随机选择碱基对
            if random.random() > 0.5:
                base1 = Text("A", font="Arial").scale(0.3).move_to([x1, y, 0])
                base2 = Text("T", font="Arial").scale(0.3).move_to([x2, y, 0])
            else:
                base1 = Text("G", font="Arial").scale(0.3).move_to([x1, y, 0])
                base2 = Text("C", font="Arial").scale(0.3).move_to([x2, y, 0])

            dna.add(rung, base1, base2)

        return dna

    def play_mendel_laws(self):
        """孟德尔遗传规律部分动画"""
        # 章节标题
        title = Text("第一部分：孟德尔遗传规律", font="SimHei").scale(1.2)
        self.play(Write(title))
        self.wait(1)
        self.play(FadeOut(title))

        # 展示孟德尔修道院场景
        monastery = Rectangle(height=3, width=4, color=WHITE).set_fill(GREY, opacity=0.3)
        garden = Rectangle(height=1, width=3, color=GREEN).set_fill(GREEN_E, opacity=0.5).next_to(monastery, DOWN,
                                                                                                  buff=0.2)

        mendel = Circle(radius=0.3, color=WHITE).set_fill(WHITE, opacity=0.8)
        mendel_body = Rectangle(height=1, width=0.6, color=BLACK).set_fill(BLACK, opacity=0.8).next_to(mendel, DOWN,
                                                                                                       buff=0)
        mendel_group = VGroup(mendel, mendel_body).move_to(garden)

        scene = VGroup(monastery, garden, mendel_group)

        # 历史背景文字
        history_text = Text(
            "1856年，奥地利修道士格雷戈尔·孟德尔在布鲁诺修道院开始了他的豌豆杂交实验。\n"
            "他选择了对比鲜明的七对性状，通过精心控制的杂交实验，发现了遗传的基本规律。",
            font="SimHei",
            line_spacing=0.5
        ).scale(0.5).to_edge(DOWN, buff=1)

        self.play(FadeIn(scene), Write(history_text))
        self.wait(2)
        self.play(FadeOut(scene), FadeOut(history_text))

        # 展示豌豆实验
        # 展示纯种亲本
        parent1 = Circle(radius=0.5, color=GREEN).set_fill(GREEN, opacity=0.7).shift(LEFT * 3)
        parent2 = Circle(radius=0.5, color=YELLOW).set_fill(YELLOW, opacity=0.7).shift(RIGHT * 3)

        p1_label = Text("黄色纯种(YY)", font="SimHei").scale(0.5).next_to(parent1, DOWN)
        p2_label = Text("绿色纯种(yy)", font="SimHei").scale(0.5).next_to(parent2, DOWN)

        self.play(
            FadeIn(parent1),
            FadeIn(parent2),
            Write(p1_label),
            Write(p2_label)
        )

        # 展示F1代
        cross_arrow = Arrow(LEFT * 2, RIGHT * 2, buff=0)
        cross_text = Text("杂交", font="SimHei").scale(0.5).next_to(cross_arrow, UP)

        self.play(GrowArrow(cross_arrow), Write(cross_text))

        f1 = VGroup(*[Circle(radius=0.3, color=GREEN).set_fill(GREEN, opacity=0.7) for _ in range(4)])
        f1.arrange(RIGHT, buff=0.2).shift(DOWN)

        f1_label = Text("F1代：全为黄色(Yy)", font="SimHei").scale(0.5).next_to(f1, DOWN)

        self.play(FadeIn(f1), Write(f1_label))

        # 展示F2代
        self.play(
            f1.animate.shift(UP * 2 + LEFT * 1.5),
            f1_label.animate.shift(UP * 2 + LEFT * 1.5)
        )

        f1_self = Arrow(DOWN, DOWN * 2, buff=0).next_to(f1, DOWN)
        f1_self_text = Text("自交", font="SimHei").scale(0.5).next_to(f1_self, RIGHT)

        self.play(GrowArrow(f1_self), Write(f1_self_text))

        # 创建16个F2代豌豆
        f2 = VGroup()
        for i in range(16):
            if i < 12:  # 12个黄色 (3/4)
                pea = Circle(radius=0.2, color=GREEN).set_fill(GREEN, opacity=0.7)
            else:  # 4个绿色 (1/4)
                pea = Circle(radius=0.2, color=YELLOW).set_fill(YELLOW, opacity=0.7)
            f2.add(pea)

        f2.arrange_in_grid(rows=4, cols=4, buff=0.1).shift(DOWN)

        f2_label = Text("F2代：3/4黄色，1/4绿色 (3:1)", font="SimHei").scale(0.5).next_to(f2, DOWN)

        self.play(FadeIn(f2), Write(f2_label))
        self.wait(2)

        # 清除场景
        self.play(
            FadeOut(VGroup(parent1, parent2, p1_label, p2_label,
                           cross_arrow, cross_text, f1, f1_label,
                           f1_self, f1_self_text, f2, f2_label))
        )

        # 展示遗传分离规律图解
        title_segregation = Text("分离规律图解", font="SimHei").scale(0.8).to_edge(UP)
        self.play(Write(title_segregation))

        # 创建Punnett方格
        square = Square(side_length=4).set_stroke(WHITE)
        h_line = Line(LEFT * 2, RIGHT * 2).shift(UP)
        v_line = Line(UP * 2, DOWN * 2).shift(RIGHT)

        punnett = VGroup(square, h_line, v_line)

        # 添加基因型标签
        p1_gametes = Text("Y", font="Arial").scale(0.8).shift(UP * 1.5 + LEFT * 3)
        p1_gametes_arrow = Arrow(LEFT * 3, LEFT * 2.5, buff=0).shift(UP * 1.5)

        p2_gametes = Text("y", font="Arial").scale(0.8).shift(RIGHT * 3 + UP * 1.5)
        p2_gametes_arrow = Arrow(RIGHT * 3, RIGHT * 2.5, buff=0).shift(UP * 1.5)

        p3_gametes = Text("Y", font="Arial").scale(0.8).shift(UP * 3 + LEFT * 1.5)
        p3_gametes_arrow = Arrow(UP * 3, UP * 2.5, buff=0).shift(LEFT * 1.5)

        p4_gametes = Text("y", font="Arial").scale(0.8).shift(UP * 3 + RIGHT * 1.5)
        p4_gametes_arrow = Arrow(UP * 3, UP * 2.5, buff=0).shift(RIGHT * 1.5)

        self.play(
            FadeIn(punnett),
            Write(VGroup(p1_gametes, p2_gametes, p3_gametes, p4_gametes)),
            GrowArrow(p1_gametes_arrow),
            GrowArrow(p2_gametes_arrow),
            GrowArrow(p3_gametes_arrow),
            GrowArrow(p4_gametes_arrow)
        )

        # 填充方格
        genotype1 = Text("YY", font="Arial").scale(0.7).move_to(LEFT * 1.5 + UP * 1.5)
        genotype2 = Text("Yy", font="Arial").scale(0.7).move_to(RIGHT * 1.5 + UP * 1.5)
        genotype3 = Text("Yy", font="Arial").scale(0.7).move_to(LEFT * 1.5 + DOWN * 1.5)
        genotype4 = Text("yy", font="Arial").scale(0.7).move_to(RIGHT * 1.5 + DOWN * 1.5)

        phenotype1 = Circle(radius=0.3, color=GREEN).set_fill(GREEN, opacity=0.5).next_to(genotype1, DOWN, buff=0.1)
        phenotype2 = Circle(radius=0.3, color=GREEN).set_fill(GREEN, opacity=0.5).next_to(genotype2, DOWN, buff=0.1)
        phenotype3 = Circle(radius=0.3, color=GREEN).set_fill(GREEN, opacity=0.5).next_to(genotype3, DOWN, buff=0.1)
        phenotype4 = Circle(radius=0.3, color=YELLOW).set_fill(YELLOW, opacity=0.5).next_to(genotype4, DOWN, buff=0.1)

        self.play(
            Write(genotype1),
            Write(genotype2),
            Write(genotype3),
            Write(genotype4),
            FadeIn(phenotype1),
            FadeIn(phenotype2),
            FadeIn(phenotype3),
            FadeIn(phenotype4)
        )

        # 展示比例
        ratio_text = Text("表现型比例：3黄色:1绿色", font="SimHei").scale(0.7).to_edge(DOWN)

        self.play(Write(ratio_text))
        self.wait(2)

        # 清除场景
        self.play(
            FadeOut(VGroup(title_segregation, punnett, p1_gametes, p2_gametes, p3_gametes, p4_gametes,
                           p1_gametes_arrow, p2_gametes_arrow, p3_gametes_arrow, p4_gametes_arrow,
                           genotype1, genotype2, genotype3, genotype4,
                           phenotype1, phenotype2, phenotype3, phenotype4, ratio_text))
        )

        # 展示自由组合定律
        title_independent = Text("自由组合定律", font="SimHei").scale(0.8).to_edge(UP)

        self.play(Write(title_independent))

        # 展示双因子杂交
        example_text = Text(
            "双因子杂交：形状(圆R/皱r)和颜色(黄Y/绿y)\n"
            "纯种圆黄(RRYY) × 纯种皱绿(rryy)",
            font="SimHei",
            line_spacing=1
        ).scale(0.7).next_to(title_independent, DOWN)

        self.play(Write(example_text))

        # 简化展示F2代9:3:3:1比例
        f2_genotypes = VGroup(
            Text("9/16 圆黄(R_Y_)", font="SimHei").scale(0.6),
            Text("3/16 圆绿(R_yy)", font="SimHei").scale(0.6),
            Text("3/16 皱黄(rrY_)", font="SimHei").scale(0.6),
            Text("1/16 皱绿(rryy)", font="SimHei").scale(0.6)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).next_to(example_text, DOWN, buff=0.5)

        self.play(Write(f2_genotypes, run_time=3))
        self.wait(2)

        # 展示历史意义
        significance = Text(
            "孟德尔的发现直到1900年才被重新发现，\n"
            "成为现代遗传学的基础。",
            font="SimHei",
            line_spacing=1
        ).scale(0.7).to_edge(DOWN)

        self.play(Write(significance))
        self.wait(2)

        # 清除场景
        self.play(
            FadeOut(VGroup(title_independent, example_text, f2_genotypes, significance))
        )

    def play_gene_chromosome(self):
        """基因与染色体关系部分动画"""
        # 章节标题
        title = Text("第二部分：基因与染色体", font="SimHei").scale(1.2)
        self.play(Write(title))
        self.wait(1)
        self.play(FadeOut(title))

        # 展示细胞核和染色体
        nucleus = Circle(radius=2, color=BLUE_E).set_fill(BLUE_E, opacity=0.2)

        # 创建染色体组
        chromosomes = VGroup()
        for i in range(3):
            for j in range(-1, 2, 2):  # 创建同源染色体对
                chromosome = self.create_chromosome(
                    height=1.5,
                    width=0.3,
                    color=CHROMOSOME_COLOR,
                    position=RIGHT * (i - 1) * 1.2 + UP * j * 0.6
                )
                chromosomes.add(chromosome)

        self.play(FadeIn(nucleus))
        self.play(FadeIn(chromosomes))

        # 文字说明
        chromosome_text = Text(
            "染色体位于细胞核中，是DNA和蛋白质的复合体，\n"
            "人类有23对染色体，每对来自父母各一条。",
            font="SimHei",
            line_spacing=1
        ).scale(0.7).to_edge(DOWN)

        self.play(Write(chromosome_text))
        self.wait(2)

        # 放大一对染色体
        selected_pair = VGroup(chromosomes[0], chromosomes[1])

        self.play(
            FadeOut(chromosome_text),
            FadeOut(nucleus),
            FadeOut(chromosomes[2:]),
            selected_pair.animate.scale(1.5).move_to(ORIGIN)
        )

        # 标记基因座位
        gene_loci = VGroup()
        gene_labels = VGroup()

        loci_positions = [(0.3, "A"), (0, "B"), (-0.3, "C")]

        for pos, label in loci_positions:
            # 为两条染色体添加相同位置的基因座
            for i, chrom in enumerate(selected_pair):
                locus = Circle(radius=0.15, color=YELLOW).set_fill(YELLOW, opacity=0.7)
                locus.move_to(chrom.get_center() + UP * pos)

                # 为同源染色体上的等位基因使用大小写区分
                if i == 0:
                    locus_label = Text(label, font="Arial").scale(0.3).move_to(locus.get_center())
                else:
                    locus_label = Text(label.lower(), font="Arial").scale(0.3).move_to(locus.get_center())

                gene_loci.add(locus)
                gene_labels.add(locus_label)

        self.play(FadeIn(gene_loci), FadeIn(gene_labels))

        # 文字说明
        gene_text = Text(
            "基因位于染色体的特定位置，称为基因座。\n"
            "同源染色体上的相同位置有等位基因。",
            font="SimHei",
            line_spacing=1
        ).scale(0.7).to_edge(DOWN)

        self.play(Write(gene_text))
        self.wait(2)

        # 清除场景
        self.play(
            FadeOut(VGroup(selected_pair, gene_loci, gene_labels, gene_text))
        )

        # 展示摩尔根果蝇实验
        title_morgan = Text("摩尔根果蝇实验：基因在染色体上", font="SimHei").scale(0.8).to_edge(UP)
        self.play(Write(title_morgan))

        # 简化的果蝇图示
        fly1 = VGroup(
            Circle(radius=0.3, color=WHITE).set_fill(WHITE, opacity=0.7),  # 头
            Ellipse(width=0.8, height=0.5, color=WHITE).set_fill(WHITE, opacity=0.7).next_to(UP * 0, RIGHT * 0.4),  # 身体
            Rectangle(height=0.1, width=0.6, color=WHITE).next_to(UP * 0.1, LEFT * 0.2)  # 翅膀
        ).shift(LEFT * 3)

        fly2 = fly1.copy().shift(RIGHT * 6)

        # 果蝇眼睛
        red_eye1 = Circle(radius=0.08, color=RED).set_fill(RED, opacity=1).move_to(
            fly1[0].get_center() + LEFT * 0.1 + UP * 0.05)
        red_eye2 = red_eye1.copy().shift(RIGHT * 0.2)

        white_eye1 = Circle(radius=0.08, color=WHITE).set_fill(WHITE, opacity=1).move_to(
            fly2[0].get_center() + LEFT * 0.1 + UP * 0.05)
        white_eye2 = white_eye1.copy().shift(RIGHT * 0.2)

        fly1.add(red_eye1, red_eye2)
        fly2.add(white_eye1, white_eye2)

        # 标签
        fly1_label = Text("红眼雌蝇\n(X^R X^R)", font="SimHei").scale(0.5).next_to(fly1, DOWN)
        fly2_label = Text("白眼雄蝇\n(X^r Y)", font="SimHei").scale(0.5).next_to(fly2, DOWN)

        self.play(
            FadeIn(fly1),
            FadeIn(fly2),
            Write(fly1_label),
            Write(fly2_label)
        )

        # 交配箭头
        cross_arrow = Arrow(LEFT * 2, RIGHT * 2, buff=0)
        cross_text = Text("交配", font="SimHei").scale(0.5).next_to(cross_arrow, UP)

        self.play(GrowArrow(cross_arrow), Write(cross_text))

        # F1代结果
        f1_flies = VGroup()
        f1_labels = VGroup()

        # 所有F1雌蝇都是红眼
        female_f1 = fly1.copy().scale(0.7).shift(DOWN * 2 + LEFT * 1.5)
        female_f1_label = Text("红眼雌蝇\n(X^R X^r)", font="SimHei").scale(0.4).next_to(female_f1, DOWN)

        # 所有F1雄蝇都是红眼
        male_f1 = fly1.copy().scale(0.7).shift(DOWN * 2 + RIGHT * 1.5)
        male_f1_label = Text("红眼雄蝇\n(X^R Y)", font="SimHei").scale(0.4).next_to(male_f1, DOWN)

        f1_flies.add(female_f1, male_f1)
        f1_labels.add(female_f1_label, male_f1_label)

        self.play(
            FadeIn(f1_flies),
            Write(f1_labels)
        )

        # F1自交结果说明
        f1_result = Text(
            "F2代：雌蝇全部红眼，雄蝇一半红眼一半白眼\n"
            "这表明眼色基因位于X染色体上",
            font="SimHei",
            line_spacing=1
        ).scale(0.6).to_edge(DOWN)

        self.play(Write(f1_result))
        self.wait(2)

        # 清除场景
        self.play(
            FadeOut(VGroup(title_morgan, fly1, fly2, fly1_label, fly2_label,
                           cross_arrow, cross_text, f1_flies, f1_labels, f1_result))
        )

        # 展示减数分裂中的交叉互换
        title_crossing = Text("交叉互换：基因重组的机制", font="SimHei").scale(0.8).to_edge(UP)
        self.play(Write(title_crossing))

        # 创建一对同源染色体
        chromosome1 = self.create_chromosome(height=3, width=0.4, color=RED, position=LEFT * 1.5)
        chromosome2 = self.create_chromosome(height=3, width=0.4, color=BLUE, position=RIGHT * 1.5)

        # 染色体上的基因标记
        gene_markers = VGroup()

        # 在染色体1上添加基因标记
        positions1 = [0.8, 0.3, -0.3, -0.8]
        for pos in positions1:
            marker = Circle(radius=0.15, color=YELLOW).set_fill(YELLOW, opacity=0.7)
            marker.move_to(chromosome1.get_center() + UP * pos)
            gene_markers.add(marker)

        # 在染色体2上添加基因标记
        positions2 = [0.8, 0.3, -0.3, -0.8]
        for pos in positions2:
            marker = Circle(radius=0.15, color=GREEN).set_fill(GREEN, opacity=0.7)
            marker.move_to(chromosome2.get_center() + UP * pos)
            gene_markers.add(marker)

        self.play(FadeIn(chromosome1), FadeIn(chromosome2), FadeIn(gene_markers))

        # 演示交叉互换
        # 染色体配对
        self.play(
            chromosome1.animate.shift(RIGHT * 0.75),
            chromosome2.animate.shift(LEFT * 0.75)
        )

        # 创建交叉点
        cross_point_y = 0
        cross_point = Dot(color=WHITE).move_to([0, cross_point_y, 0])

        self.play(FadeIn(cross_point))

        # 交换片段
        # 创建交换后的染色体部分
        upper_red = self.create_chromosome_segment(height=1.5, width=0.4, color=RED,
                                                   position=UP * 0.75, y_start=cross_point_y)
        lower_blue = self.create_chromosome_segment(height=1.5, width=0.4, color=BLUE,
                                                    position=DOWN * 0.75, y_start=cross_point_y)

        upper_blue = self.create_chromosome_segment(height=1.5, width=0.4, color=BLUE,
                                                    position=UP * 0.75, y_start=cross_point_y)
        lower_red = self.create_chromosome_segment(height=1.5, width=0.4, color=RED,
                                                   position=DOWN * 0.75, y_start=cross_point_y)

        # 重新排列基因标记
        self.play(
            FadeOut(gene_markers),
            FadeOut(chromosome1),
            FadeOut(chromosome2)
        )

        # 显示重组后的染色体
        recombined1 = VGroup(upper_red, lower_blue)
        recombined2 = VGroup(upper_blue, lower_red)

        self.play(
            FadeIn(recombined1.shift(LEFT * 1.5)),
            FadeIn(recombined2.shift(RIGHT * 1.5))
        )

        # 文字说明
        crossing_text = Text(
            "交叉互换使同源染色体之间交换DNA片段，\n"
            "产生基因重组，增加遗传多样性。",
            font="SimHei",
            line_spacing=1
        ).scale(0.7).to_edge(DOWN)

        self.play(Write(crossing_text))
        self.wait(2)

        # 清除场景
        self.play(
            FadeOut(VGroup(title_crossing, recombined1, recombined2, cross_point, crossing_text))
        )

    def create_chromosome(self, height, width, color, position):
        """创建染色体形状"""
        # 创建X形状的染色体
        upper_arm = Rectangle(height=height / 2, width=width, color=color).set_fill(color, opacity=0.7)
        lower_arm = Rectangle(height=height / 2, width=width, color=color).set_fill(color, opacity=0.7)

        upper_arm.move_to(UP * height / 4)
        lower_arm.move_to(DOWN * height / 4)

        # 创建着丝粒（染色体中央收缩部分）
        centromere = Circle(radius=width / 2, color=color).set_fill(color, opacity=0.9)

        chromosome = VGroup(upper_arm, lower_arm, centromere)
        chromosome.move_to(position)

        return chromosome

    def create_chromosome_segment(self, height, width, color, position, y_start=0):
        """创建染色体片段"""
        segment = Rectangle(height=height, width=width, color=color).set_fill(color, opacity=0.7)
        segment.move_to(position)

        # 调整起始位置
        current_y = segment.get_center()[1]
        delta_y = y_start - (current_y - height / 2)
        segment.shift(UP * delta_y)

        return segment

    def play_dna_structure(self):
        """DNA结构与本质部分动画"""
        # 章节标题
        title = Text("第三部分：DNA结构与本质", font="SimHei").scale(1.2)
        self.play(Write(title))
        self.wait(1)
        self.play(FadeOut(title))

        # 展示遗传物质本质的探索历程
        title_experiments = Text("遗传物质本质的探索", font="SimHei").scale(0.8).to_edge(UP)
        self.play(Write(title_experiments))

        # 展示格里菲斯转化实验
        experiment1 = Text(
            "格里菲斯实验(1928)：\n"
            "死的S型肺炎球菌 + 活的R型肺炎球菌 → 活的S型肺炎球菌\n"
            "某种物质从死菌转移到活菌，引起遗传性状改变",
            font="SimHei",
            line_spacing=1
        ).scale(0.6).next_to(title_experiments, DOWN, buff=0.5)

        self.play(Write(experiment1))
        self.wait(2)

        # 展示艾弗里实验
        experiment2 = Text(
            "艾弗里实验(1944)：\n"
            "分离S型菌的成分，只有DNA部分能引起转化\n"
            "首次证明DNA是遗传物质",
            font="SimHei",
            line_spacing=1
        ).scale(0.6).next_to(experiment1, DOWN, buff=0.5)

        self.play(Write(experiment2))
        self.wait(2)

        # 展示Hershey-Chase实验
        experiment3 = Text(
            "Hershey-Chase实验(1952)：\n"
            "用放射性标记区分病毒的DNA和蛋白质\n"
            "只有DNA进入宿主细胞并指导病毒繁殖",
            font="SimHei",
            line_spacing=1
        ).scale(0.6).next_to(experiment2, DOWN, buff=0.5)

        self.play(Write(experiment3))
        self.wait(2)

        # 清除实验描述
        self.play(FadeOut(VGroup(title_experiments, experiment1, experiment2, experiment3)))

        # 展示DNA结构发现历程
        title_structure = Text("DNA结构的发现", font="SimHei").scale(0.8).to_edge(UP)
        self.play(Write(title_structure))

        # 展示X射线衍射照片
        x_ray = ImageMobject("dna_xray.png")  # 假设有此图片
        # 如果没有图片，用圆形代替
        if not os.path.exists("dna_xray.png"):
            x_ray = Circle(radius=1.5).set_fill(WHITE, opacity=0.2)
            # 添加十字形衍射图案
            x_ray_pattern = VGroup(
                Line(UP, DOWN, color=WHITE),
                Line(LEFT, RIGHT, color=WHITE),
                *[Line(ORIGIN, unit_vector, color=WHITE) for unit_vector in
                  [UP + RIGHT, UP + LEFT, DOWN + RIGHT, DOWN + LEFT]]
            )
            x_ray.add(x_ray_pattern)

        x_ray.scale(0.8).next_to(title_structure, DOWN, buff=0.5)
        x_ray_label = Text("罗莎琳德·富兰克林拍摄的DNA X射线衍射照片", font="SimHei").scale(0.5).next_to(x_ray, DOWN)

        self.play(FadeIn(x_ray), Write(x_ray_label))
        self.wait(1)

        # 展示沃森和克里克
        watson_crick_text = Text(
            "1953年，詹姆斯·沃森和弗朗西斯·克里克\n"
            "根据X射线衍射数据提出DNA双螺旋模型",
            font="SimHei",
            line_spacing=1
        ).scale(0.6).next_to(x_ray_label, DOWN, buff=0.5)

        self.play(Write(watson_crick_text))
        self.wait(2)

        # 清除历史内容
        self.play(FadeOut(VGroup(title_structure, x_ray, x_ray_label, watson_crick_text)))

        # 展示DNA分子结构
        title_molecular = Text("DNA分子结构", font="SimHei").scale(0.8).to_edge(UP)
        self.play(Write(title_molecular))

        # 创建更详细的DNA双螺旋结构
        dna = self.create_detailed_dna_helix(num_rungs=10)

        self.play(FadeIn(dna))

        # 放大展示碱基配对
        base_pair = self.create_base_pair()
        base_pair.scale(3).to_edge(RIGHT)

        self.play(FadeIn(base_pair))

        # 添加说明文字
        dna_features = VGroup(
            Text("1. 双螺旋结构", font="SimHei").scale(0.6),
            Text("2. 反向平行的糖-磷酸骨架", font="SimHei").scale(0.6),
            Text("3. 碱基配对规则：A-T, G-C", font="SimHei").scale(0.6),
            Text("4. 每个螺旋周期10个碱基对", font="SimHei").scale(0.6),
            Text("5. 大沟和小沟结构", font="SimHei").scale(0.6)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).to_edge(LEFT)

        self.play(Write(dna_features, run_time=3))

        # 旋转DNA展示三维结构
        self.play(Rotate(dna, angle=2 * PI, axis=UP, run_time=5))

        # 结构意义
        dna_significance = Text(
            "DNA结构揭示了遗传信息储存和复制的分子基础，\n"
            "碱基序列编码生物体全部遗传信息。",
            font="SimHei",
            line_spacing=1
        ).scale(0.6).to_edge(DOWN)

        self.play(Write(dna_significance))
        self.wait(2)

        # 清除场景
        self.play(
            FadeOut(VGroup(title_molecular, dna, base_pair, dna_features, dna_significance))
        )

    def create_detailed_dna_helix(self, num_rungs=10, helix_radius=1.2):
        """创建更详细的DNA双螺旋结构"""
        dna = VGroup()

        # 创建两条螺旋骨架
        strand1 = VMobject(color=BLUE_D)
        strand2 = VMobject(color=RED_D)

        points_per_turn = 30
        points1 = []
        points2 = []

        for i in range(points_per_turn * num_rungs):
            t = i / points_per_turn

            x1 = helix_radius * np.cos(t * TAU)
            y1 = t - num_rungs / 2
            z1 = helix_radius * np.sin(t * TAU)

            x2 = helix_radius * np.cos(t * TAU + PI)
            y2 = t - num_rungs / 2
            z2 = helix_radius * np.sin(t * TAU + PI)

            points1.append([x1, y1, 0])
            points2.append([x2, y2, 0])

        strand1.set_points_smoothly(points1)
        strand2.set_points_smoothly(points2)

        # 使骨架更粗
        strand1.set_stroke(width=10)
        strand2.set_stroke(width=10)

        dna.add(strand1, strand2)

        # 添加碱基对
        for i in range(num_rungs):
            t = i + 0.5

            x1 = helix_radius * np.cos(t * TAU / points_per_turn * 30)
            y1 = t - num_rungs / 2
            z1 = helix_radius * np.sin(t * TAU / points_per_turn * 30)

            x2 = helix_radius * np.cos(t * TAU / points_per_turn * 30 + PI)
            y2 = t - num_rungs / 2
            z2 = helix_radius * np.sin(t * TAU / points_per_turn * 30 + PI)

            # 创建碱基对连接线
            base_pair = Line(
                [x1, y1, 0],
                [x2, y2, 0],
                color=YELLOW
            )

            # 随机选择碱基对类型
            if random.random() > 0.5:
                base1 = Text("A", font="Arial").scale(0.2).move_to([x1, y1, 0])
                base2 = Text("T", font="Arial").scale(0.2).move_to([x2, y2, 0])
            else:
                base1 = Text("G", font="Arial").scale(0.2).move_to([x1, y1, 0])
                base2 = Text("C", font="Arial").scale(0.2).move_to([x2, y2, 0])

            dna.add(base_pair, base1, base2)

        return dna

    def create_base_pair(self):
        """创建碱基对详细结构"""
        base_pair = VGroup()

        # 创建碱基
        adenine = Text("A", font="Arial").scale(0.6).set_color(BLUE)
        thymine = Text("T", font="Arial").scale(0.6).set_color(RED)

        # 创建氢键
        h_bonds = VGroup(
            Line(LEFT * 0.2, RIGHT * 0.2, color=WHITE),
            Line(LEFT * 0.2, RIGHT * 0.2, color=WHITE).shift(UP * 0.2)
        )

        # 组合碱基对
        adenine.next_to(h_bonds, LEFT)
        thymine.next_to(h_bonds, RIGHT)

        base_pair.add(adenine, h_bonds, thymine)

        # 添加说明标签
        a_label = Text("腺嘌呤", font="SimHei").scale(0.3).next_to(adenine, UP)
        t_label = Text("胸腺嘧啶", font="SimHei").scale(0.3).next_to(thymine, UP)
        h_label = Text("氢键", font="SimHei").scale(0.3).next_to(h_bonds, DOWN)

        base_pair.add(a_label, t_label, h_label)

        return base_pair

    def play_dna_replication(self):
        """DNA复制过程部分动画"""
        # 章节标题
        title = Text("第四部分：DNA复制", font="SimHei").scale(1.2)
        self.play(Write(title))
        self.wait(1)
        self.play(FadeOut(title))

        # 展示半保留复制模型
        title_semiconservative = Text("半保留复制模型", font="SimHei").scale(0.8).to_edge(UP)
        self.play(Write(title_semiconservative))

        # 创建原始DNA
        original_dna = self.create_simple_dna(length=5, strand1_color=BLUE, strand2_color=RED)
        original_dna.move_to(UP * 1.5)

        self.play(FadeIn(original_dna))

        # 展示模型示意图
        model_text = Text(
            "Watson和Crick提出：DNA复制时双链解开，\n"
            "每条单链作为模板合成新链。",
            font="SimHei",
            line_spacing=1
        ).scale(0.6).next_to(original_dna, DOWN, buff=0.5)

        self.play(Write(model_text))
        self.wait(1)

        # 展示Meselson-Stahl实验
        experiment_text = Text(
            "Meselson-Stahl实验(1958)通过\n"
            "同位素标记证实了半保留复制模型",
            font="SimHei",
            line_spacing=1
        ).scale(0.6).next_to(model_text, DOWN, buff=0.5)

        self.play(Write(experiment_text))
        self.wait(2)

        # 清除半保留复制模型内容
        self.play(FadeOut(VGroup(title_semiconservative, original_dna, model_text, experiment_text)))

        # 展示DNA复制过程
        title_process = Text("DNA复制过程", font="SimHei").scale(0.8).to_edge(UP)
        self.play(Write(title_process))

        # 创建DNA复制动画
        # 起始DNA
        dna_segment = self.create_detailed_dna_segment(length=6)
        dna_segment.move_to(ORIGIN)

        self.play(FadeIn(dna_segment))

        # 展示解旋酶作用
        helicase = Circle(radius=0.3, color=YELLOW).set_fill(YELLOW, opacity=0.7)
        helicase.move_to(dna_segment.get_center())

        helicase_label = Text("解旋酶", font="SimHei").scale(0.5).next_to(helicase, UP)

        self.play(FadeIn(helicase), Write(helicase_label))

        # 展示DNA解旋
        unwound_dna = self.create_unwound_dna(length=6)
        unwound_dna.move_to(ORIGIN)

        self.play(
            Transform(dna_segment, unwound_dna),
            helicase.animate.shift(RIGHT * 0.5),
            helicase_label.animate.shift(RIGHT * 0.5)
        )

        # 添加DNA聚合酶
        polymerase1 = Triangle(color=GREEN).set_fill(GREEN, opacity=0.7).scale(0.3)
        polymerase1.move_to(unwound_dna[0].get_center() + RIGHT * 1 + UP * 0.3)

        polymerase2 = Triangle(color=GREEN).set_fill(GREEN, opacity=0.7).scale(0.3)
        polymerase2.move_to(unwound_dna[1].get_center() + RIGHT * 1 + DOWN * 0.3)

        poly_label1 = Text("DNA聚合酶", font="SimHei").scale(0.4).next_to(polymerase1, UP)
        poly_label2 = Text("DNA聚合酶", font="SimHei").scale(0.4).next_to(polymerase2, DOWN)

        self.play(
            FadeIn(VGroup(polymerase1, polymerase2)),
            Write(VGroup(poly_label1, poly_label2))
        )

        # 展示新链合成
        new_strand1 = self.create_dna_strand(length=3, color=BLUE_E, position=RIGHT * 2 + UP * 0.3)
        new_strand2 = self.create_dna_strand(length=3, color=RED_E, position=RIGHT * 2 + DOWN * 0.3)

        self.play(
            GrowFromPoint(new_strand1, polymerase1.get_center()),
            GrowFromPoint(new_strand2, polymerase2.get_center())
        )

        # 添加说明
        replication_text = Text(
            "复制过程:\n"
            "1. 解旋酶打开双螺旋\n"
            "2. 单链结合蛋白稳定单链\n"
            "3. 引物酶合成RNA引物\n"
            "4. DNA聚合酶延伸新链\n"
            "5. 前导链连续合成，滞后链分段合成\n"
            "6. DNA连接酶连接片段",
            font="SimHei",
            line_spacing=0.5
        ).scale(0.5).to_edge(LEFT)

        self.play(Write(replication_text))

        # 展示前导链和滞后链
        leading_label = Text("前导链(连续合成)", font="SimHei").scale(0.4).next_to(new_strand1, RIGHT)
        lagging_label = Text("滞后链(分段合成)", font="SimHei").scale(0.4).next_to(new_strand2, RIGHT)

        self.play(
            Write(leading_label),
            Write(lagging_label)
        )
        self.wait(2)

        # 清除场景
        self.play(
            FadeOut(VGroup(
                title_process, dna_segment, helicase, helicase_label,
                polymerase1, polymerase2, poly_label1, poly_label2,
                new_strand1, new_strand2, replication_text, leading_label, lagging_label
            ))
        )

        # 展示复制精确性
        title_fidelity = Text("DNA复制的精确性", font="SimHei").scale(0.8).to_edge(UP)
        self.play(Write(title_fidelity))

        # 展示错误率
        fidelity_text = Text(
            "DNA聚合酶每复制10^9个碱基只出现一个错误\n"
            "这种高精确度依赖于几种机制:",
            font="SimHei",
            line_spacing=1
        ).scale(0.7).next_to(title_fidelity, DOWN, buff=0.5)

        self.play(Write(fidelity_text))

        # 展示校对和修复机制
        mechanisms = VGroup(
            Text("1. 碱基配对几何形状识别", font="SimHei").scale(0.6),
            Text("2. DNA聚合酶的3'→5'外切酶活性", font="SimHei").scale(0.6),
            Text("3. 复制后错配修复系统", font="SimHei").scale(0.6),
            Text("4. 多种修复机制相互协作", font="SimHei").scale(0.6)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).next_to(fidelity_text, DOWN, buff=0.5)

        self.play(Write(mechanisms, run_time=3))

        # 展示意义
        significance = Text(
            "高精确的DNA复制确保遗传信息准确传递，\n"
            "是生命延续的基础。",
            font="SimHei",
            line_spacing=1
        ).scale(0.6).to_edge(DOWN)

        self.play(Write(significance))
        self.wait(2)

        # 清除场景
        self.play(
            FadeOut(VGroup(title_fidelity, fidelity_text, mechanisms, significance))
        )

    def create_simple_dna(self, length=5, strand1_color=BLUE, strand2_color=RED):
        """创建简化DNA结构"""
        dna = VGroup()

        # 创建两条平行链
        strand1 = Line(LEFT * length / 2, RIGHT * length / 2, color=strand1_color)
        strand2 = Line(LEFT * length / 2, RIGHT * length / 2, color=strand2_color).shift(DOWN * 0.5)

        dna.add(strand1, strand2)

        # 添加碱基对
        for i in range(int(length) + 1):
            x = -length / 2 + i
            base_pair = Line(UP * 0.25, DOWN * 0.25, color=YELLOW).move_to([x, -0.25, 0])
            dna.add(base_pair)

        return dna

    def create_detailed_dna_segment(self, length=5):
        """创建更详细的DNA片段"""
        dna = VGroup()

        # 创建两条螺旋骨架
        strand1_points = []
        strand2_points = []

        for i in np.linspace(-length / 2, length / 2, 50):
            x1 = 0.3 * np.cos(i * 5)
            y1 = i

            x2 = 0.3 * np.cos(i * 5 + PI)
            y2 = i

            strand1_points.append([x1, y1, 0])
            strand2_points.append([x2, y2, 0])

        strand1 = VMobject(color=BLUE)
        strand1.set_points_as_corners(strand1_points)

        strand2 = VMobject(color=RED)
        strand2.set_points_as_corners(strand2_points)

        dna.add(strand1, strand2)

        # 添加碱基对
        for i in np.linspace(-length / 2, length / 2, int(length) + 1):
            x1 = 0.3 * np.cos(i * 5)
            y1 = i

            x2 = 0.3 * np.cos(i * 5 + PI)
            y2 = i

            base_pair = Line(
                [x1, y1, 0],
                [x2, y2, 0],
                color=YELLOW
            )

            dna.add(base_pair)

        return dna

    def create_unwound_dna(self, length=5):
        """创建解旋的DNA"""
        dna = VGroup()

        # 创建两条分离的链
        strand1_points = []
        strand2_points = []

        for i in np.linspace(-length / 2, length / 2, 50):
            # 左半部分保持螺旋
            if i < 0:
                x1 = 0.3 * np.cos(i * 5)
                y1 = i

                x2 = 0.3 * np.cos(i * 5 + PI)
                y2 = i
            # 右半部分分离
            else:
                x1 = 0.3 * np.cos(i * 5) + i * 0.2
                y1 = i

                x2 = 0.3 * np.cos(i * 5 + PI) - i * 0.2
                y2 = i

            strand1_points.append([x1, y1, 0])
            strand2_points.append([x2, y2, 0])

        strand1 = VMobject(color=BLUE)
        strand1.set_points_as_corners(strand1_points)

        strand2 = VMobject(color=RED)
        strand2.set_points_as_corners(strand2_points)

        dna.add(strand1, strand2)

        # 添加碱基对（只在左半部分）
        for i in np.linspace(-length / 2, 0, int(length / 2) + 1):
            x1 = 0.3 * np.cos(i * 5)
            y1 = i

            x2 = 0.3 * np.cos(i * 5 + PI)
            y2 = i

            base_pair = Line(
                [x1, y1, 0],
                [x2, y2, 0],
                color=YELLOW
            )

            dna.add(base_pair)

        return dna

    def create_dna_strand(self, length=3, color=BLUE, position=ORIGIN):
        """创建DNA单链"""
        strand = VMobject(color=color)

        points = []
        for i in np.linspace(0, length, 20):
            x = i
            y = 0.1 * np.sin(i * 5)

            points.append([x, y, 0])

        strand.set_points_as_corners(points)
        strand.move_to(position)

        return strand

    def play_molecular_techniques(self):
        """分子生物学技术部分动画"""
        # 章节标题
        title = Text("第五部分：分子生物学技术", font="SimHei").scale(1.2)
        self.play(Write(title))
        self.wait(1)
        self.play(FadeOut(title))

        # 展示荧光原位杂交技术
        title_fish = Text("荧光原位杂交技术(FISH)", font="SimHei").scale(0.8).to_edge(UP)
        self.play(Write(title_fish))

        # 展示染色体和荧光探针
        chromosome = self.create_chromosome(height=3, width=0.4, color=GREY, position=LEFT * 2)

        # 荧光探针
        probe1 = Circle(radius=0.2, color=GREEN).set_fill(GREEN, opacity=0.7).move_to(
            chromosome.get_center() + UP * 0.8)
        probe2 = Circle(radius=0.2, color=RED).set_fill(RED, opacity=0.7).move_to(chromosome.get_center() + DOWN * 0.8)

        self.play(FadeIn(chromosome))

        # 展示探针结合过程
        fish_text = Text(
            "FISH技术原理：\n"
            "1. 制备特异性DNA荧光探针\n"
            "2. 探针与目标DNA序列杂交\n"
            "3. 荧光显微镜下观察信号",
            font="SimHei",
            line_spacing=0.5
        ).scale(0.6).next_to(chromosome, RIGHT, buff=1)

        self.play(Write(fish_text))

        self.play(FadeIn(VGroup(probe1, probe2)))

        # 展示应用
        fish_applications = Text(
            "应用：\n"
            "1. 染色体异常检测\n"
            "2. 基因定位与映射\n"
            "3. 微缺失综合征诊断\n"
            "4. 肿瘤细胞遗传学分析",
            font="SimHei",
            line_spacing=0.5
        ).scale(0.6).to_edge(DOWN, buff=1)

        self.play(Write(fish_applications))
        self.wait(2)

        # 清除FISH内容
        self.play(
            FadeOut(VGroup(title_fish, chromosome, probe1, probe2, fish_text, fish_applications))
        )

        # 展示GFP技术
        title_gfp = Text("绿色荧光蛋白(GFP)技术", font="SimHei").scale(0.8).to_edge(UP)
        self.play(Write(title_gfp))

        # 展示GFP蛋白
        gfp = Circle(radius=1, color=GREEN).set_fill(GREEN, opacity=0.3)
        gfp_label = Text("GFP", font="Arial").scale(0.8).move_to(gfp.get_center())

        self.play(FadeIn(gfp), Write(gfp_label))

        # GFP原理
        gfp_text = Text(
            "GFP技术原理：\n"
            "1. 将GFP基因与目标基因融合\n"
            "2. 目标蛋白表达时同时产生GFP\n"
            "3. 荧光显微镜下实时观察",
            font="SimHei",
            line_spacing=0.5
        ).scale(0.6).next_to(gfp, RIGHT, buff=1)

        self.play(Write(gfp_text))

        # 展示细胞中的GFP标记
        cell = Circle(radius=1.5, color=WHITE).set_fill(opacity=0.1)
        nucleus = Circle(radius=0.6, color=BLUE_E).set_fill(BLUE_E, opacity=0.2)

        # 多个GFP标记的蛋白质
        proteins = VGroup()
        for _ in range(10):
            pos = np.array([
                random.uniform(-1.2, 1.2),
                random.uniform(-1.2, 1.2),
                0
            ])
            protein = Circle(radius=0.1, color=GREEN).set_fill(GREEN, opacity=0.7).move_to(pos)
            proteins.add(protein)

        cell_group = VGroup(cell, nucleus, proteins).to_edge(DOWN, buff=1)

        self.play(FadeIn(cell_group))

        # 展示GFP应用
        gfp_applications = Text(
            "应用：\n"
            "1. 蛋白质定位研究\n"
            "2. 蛋白质相互作用\n"
            "3. 基因表达实时监测\n"
            "4. 细胞命运追踪",
            font="SimHei",
            line_spacing=0.5
        ).scale(0.6).next_to(cell, LEFT, buff=1)

        self.play(Write(gfp_applications))
        self.wait(2)

        # 清除GFP内容
        self.play(
            FadeOut(VGroup(title_gfp, gfp, gfp_label, gfp_text, cell_group, gfp_applications))
        )

        # 展示现代DNA分析技术
        title_modern = Text("现代DNA分析技术", font="SimHei").scale(0.8).to_edge(UP)
        self.play(Write(title_modern))

        # 展示PCR技术
        pcr_title = Text("聚合酶链式反应(PCR)", font="SimHei").scale(0.7).next_to(title_modern, DOWN, buff=0.5)
        self.play(Write(pcr_title))

        # 简化展示PCR循环
        pcr_cycle = VGroup()

        # 变性
        dna1 = self.create_simple_dna(length=3).scale(0.8).shift(LEFT * 3 + UP * 0.5)
        dna1_label = Text("双链DNA", font="SimHei").scale(0.5).next_to(dna1, DOWN)

        # 退火
        strand1 = Line(LEFT * 1.5, RIGHT * 1.5, color=BLUE).shift(UP * 1)
        strand2 = Line(LEFT * 1.5, RIGHT * 1.5, color=RED).shift(DOWN * 0.5)
        primers = VGroup(
            Line(LEFT * 0.5, RIGHT * 0.5, color=GREEN).move_to(strand1.get_start() + RIGHT * 0.5),
            Line(LEFT * 0.5, RIGHT * 0.5, color=GREEN).move_to(strand2.get_start() + RIGHT * 0.5)
        )
        anneal = VGroup(strand1, strand2, primers)
        anneal_label = Text("引物退火", font="SimHei").scale(0.5).next_to(anneal, DOWN)

        # 延伸
        new_dna1 = self.create_simple_dna(length=3).scale(0.8).shift(RIGHT * 3 + UP * 0.5)
        new_dna2 = self.create_simple_dna(length=3).scale(0.8).shift(RIGHT * 3 + DOWN * 1.5)
        extension = VGroup(new_dna1, new_dna2)
        extension_label = Text("扩增", font="SimHei").scale(0.5).next_to(extension, DOWN)

        pcr_cycle.add(
            dna1, dna1_label,
            anneal, anneal_label,
            extension, extension_label
        )

        # 箭头连接各步骤
        arrow1 = Arrow(dna1.get_right(), anneal.get_left(), buff=0.2)
        arrow2 = Arrow(anneal.get_right(), extension.get_left(), buff=0.2)

        pcr_cycle.add(arrow1, arrow2)

        self.play(FadeIn(pcr_cycle))

        # PCR应用
        pcr_applications = Text(
            "应用：\n"
            "1. 基因克隆\n"
            "2. 基因诊断\n"
            "3. 法医DNA分析\n"
            "4. 分子进化研究",
            font="SimHei",
            line_spacing=0.5
        ).scale(0.6).to_edge(LEFT)

        self.play(Write(pcr_applications))
        self.wait(2)

        # 清除PCR内容，保留标题
        self.play(
            FadeOut(VGroup(pcr_title, pcr_cycle, pcr_applications))
        )

        # 展示DNA测序技术
        sequencing_title = Text("DNA测序技术", font="SimHei").scale(0.7).next_to(title_modern, DOWN, buff=0.5)
        self.play(Write(sequencing_title))

        # 展示测序读数
        sequence_data = Text(
            "ATGCCTGAAGTCAGTCGCATTAGCGATT...",
            font="Courier"
        ).scale(0.8).shift(UP * 0.5)

        self.play(Write(sequence_data))

        # 测序技术发展
        sequencing_evolution = VGroup(
            Text("Sanger测序 (1977)", font="SimHei").scale(0.6),
            Text("下一代测序 (2005)", font="SimHei").scale(0.6),
            Text("单分子实时测序 (2010)", font="SimHei").scale(0.6),
            Text("纳米孔测序 (2014)", font="SimHei").scale(0.6)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).shift(DOWN)

        self.play(Write(sequencing_evolution))

        # 测序应用
        sequencing_applications = Text(
            "应用：\n"
            "1. 基因组测序\n"
            "2. 转录组分析\n"
            "3. 临床基因诊断\n"
            "4. 个性化医疗",
            font="SimHei",
            line_spacing=0.5
        ).scale(0.6).to_edge(RIGHT)

        self.play(Write(sequencing_applications))
        self.wait(2)

        # 清除场景
        self.play(
            FadeOut(
                VGroup(title_modern, sequencing_title, sequence_data, sequencing_evolution, sequencing_applications))
        )

    def play_gene_expression(self):
        """基因表达详细过程部分动画"""
        # 章节标题
        title = Text("第六部分：基因表达详细过程", font="SimHei").scale(1.2)
        self.play(Write(title))
        self.wait(1)
        self.play(FadeOut(title))

        # 展示中心法则
        central_dogma = Text("中心法则：DNA → RNA → 蛋白质", font="SimHei").scale(1)
        self.play(Write(central_dogma))
        self.wait(1)
        self.play(FadeOut(central_dogma))

        # 展示转录过程
        title_transcription = Text("转录过程", font="SimHei").scale(0.8).to_edge(UP)
        self.play(Write(title_transcription))

        # 创建DNA模板
        dna_template = self.create_simple_dna(length=6)
        dna_template.move_to(UP * 1)

        self.play(FadeIn(dna_template))

        # RNA聚合酶
        polymerase = Circle(radius=0.3, color=GREEN).set_fill(GREEN, opacity=0.7)
        polymerase.move_to(dna_template.get_center() + LEFT * 2)

        polymerase_label = Text("RNA聚合酶", font="SimHei").scale(0.5).next_to(polymerase, UP)

        self.play(FadeIn(polymerase), Write(polymerase_label))

        # 展示RNA合成
        rna_strand = VMobject(color=RNA_COLOR)
        rna_points = []

        for i in np.linspace(-3, -1, 10):
            rna_points.append([i, 0.5, 0])

        rna_strand.set_points_as_corners(rna_points)

        self.play(FadeIn(rna_strand))

        # 聚合酶移动并合成RNA
        self.play(
            polymerase.animate.shift(RIGHT * 2),
            polymerase_label.animate.shift(RIGHT * 2)
        )

        # 延长RNA链
        new_rna_points = []
        for i in np.linspace(-3, 1, 20):
            new_rna_points.append([i, 0.5, 0])

        new_rna = VMobject(color=RNA_COLOR)
        new_rna.set_points_as_corners(new_rna_points)

        self.play(Transform(rna_strand, new_rna))

        # 转录过程说明
        transcription_steps = Text(
            "转录步骤：\n"
            "1. RNA聚合酶结合启动子\n"
            "2. DNA局部解链，形成转录泡\n"
            "3. 按照A-U, G-C碱基配对原则合成RNA\n"
            "4. 到达终止子，RNA链释放",
            font="SimHei",
            line_spacing=0.5
        ).scale(0.6).to_edge(LEFT)

        self.play(Write(transcription_steps))

        # RNA加工
        processing_title = Text("RNA加工", font="SimHei").scale(0.6).next_to(transcription_steps, DOWN, buff=0.5)

        processing_steps = VGroup(
            Text("1. 5'端加帽", font="SimHei").scale(0.5),
            Text("2. 3'端加尾", font="SimHei").scale(0.5),
            Text("3. 内含子剪切", font="SimHei").scale(0.5),
            Text("4. mRNA出核", font="SimHei").scale(0.5)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2).next_to(processing_title, DOWN, buff=0.3)

        self.play(Write(processing_title), Write(processing_steps))
        self.wait(2)

        # 清除转录内容
        self.play(
            FadeOut(VGroup(title_transcription, dna_template, polymerase, polymerase_label,
                           rna_strand, transcription_steps, processing_title, processing_steps))
        )

        # 展示翻译过程
        title_translation = Text("翻译过程", font="SimHei").scale(0.8).to_edge(UP)
        self.play(Write(title_translation))

        # 创建mRNA
        mrna = Line(LEFT * 4, RIGHT * 4, color=RNA_COLOR)

        # 添加密码子
        codons = VGroup()
        for i in range(-3, 4):
            codon = Text(random.choice(["AUG", "GCA", "UUC", "AAG", "GGU"]), font="Courier").scale(0.4)
            codon.move_to([i, 0, 0])
            codons.add(codon)

        mrna_group = VGroup(mrna, codons)
        mrna_group.move_to(UP * 1.5)

        self.play(FadeIn(mrna_group))

        # 创建核糖体
        ribosome = Rectangle(height=1, width=1.5, color=BLUE_E).set_fill(BLUE_E, opacity=0.3)
        ribosome.move_to(mrna.get_center() + LEFT * 2)

        ribosome_label = Text("核糖体", font="SimHei").scale(0.5).next_to(ribosome, UP)

        self.play(FadeIn(ribosome), Write(ribosome_label))

        # 创建tRNA
        trna = VGroup(
            Polygon(
                DOWN, RIGHT, UP, LEFT,
                color=YELLOW_E
            ).set_fill(YELLOW_E, opacity=0.3).scale(0.4),
            Text("Ala", font="Courier").scale(0.3)
        )
        trna.move_to(ribosome.get_center() + DOWN * 1)

        trna_label = Text("tRNA", font="SimHei").scale(0.5).next_to(trna, DOWN)

        self.play(FadeIn(trna), Write(trna_label))

        # tRNA进入核糖体
        self.play(trna.animate.move_to(ribosome.get_center()))

        # 核糖体移动并合成肽链
        peptide = VGroup()

        # 移动核糖体并添加氨基酸
        for i in range(3):
            self.play(
                ribosome.animate.shift(RIGHT * 1),
                ribosome_label.animate.shift(RIGHT * 1)
            )

            new_aa = Circle(radius=0.1, color=PROTEIN_COLOR).set_fill(PROTEIN_COLOR, opacity=0.7)

            if len(peptide) == 0:
                new_aa.move_to(ribosome.get_center() + DOWN * 0.5)
                peptide.add(new_aa)
            else:
                new_aa.next_to(peptide[-1], RIGHT * 0.2)
                peptide.add(new_aa)

                # 连接肽链
                if len(peptide) > 1:
                    line = Line(peptide[-2].get_center(), peptide[-1].get_center(), color=PROTEIN_COLOR)
                    peptide.add(line)

            self.play(FadeIn(new_aa))

        # 翻译过程说明
        translation_steps = Text(
            "翻译步骤：\n"
            "1. 核糖体结合mRNA\n"
            "2. tRNA携带氨基酸进入A位点\n"
            "3. 形成肽键，肽链延长\n"
            "4. 核糖体向前移动\n"
            "5. 遇到终止密码子，肽链释放",
            font="SimHei",
            line_spacing=0.5
        ).scale(0.6).to_edge(RIGHT)

        self.play(Write(translation_steps))

        # 遗传密码表
        genetic_code_title = Text("遗传密码表", font="SimHei").scale(0.6).to_edge(DOWN, buff=2)

        genetic_code = Text(
            "密码子示例：\n"
            "AUG - 甲硫氨酸(起始)\n"
            "UGG - 色氨酸\n"
            "UAA, UAG, UGA - 终止",
            font="SimHei",
            line_spacing=0.5
        ).scale(0.5).next_to(genetic_code_title, DOWN)

        self.play(Write(genetic_code_title), Write(genetic_code))
        self.wait(2)

        # 清除翻译内容
        self.play(
            FadeOut(VGroup(title_translation, mrna_group, ribosome, ribosome_label,
                           trna, trna_label, peptide, translation_steps,
                           genetic_code_title, genetic_code))
        )

        # 展示蛋白质修饰与运输
        title_modification = Text("蛋白质修饰与运输", font="SimHei").scale(0.8).to_edge(UP)
        self.play(Write(title_modification))

        # 创建新合成的蛋白质
        protein = self.create_protein_chain(length=5)
        protein.move_to(LEFT * 3)

        self.play(FadeIn(protein))

        # 展示蛋白质折叠
        folded_protein = self.create_folded_protein()
        folded_protein.move_to(ORIGIN)

        self.play(Transform(protein, folded_protein))

        # 展示翻译后修饰
        modified_protein = self.create_modified_protein()
        modified_protein.move_to(RIGHT * 3)

        self.play(Transform(protein, modified_protein))

        # 蛋白质修饰与运输说明
        modification_steps = Text(
            "蛋白质成熟过程：\n"
            "1. 肽链合成后进行折叠\n"
            "2. 分子伴侣辅助正确折叠\n"
            "3. 翻译后修饰(糖基化、磷酸化等)\n"
            "4. 蛋白质分选与转运\n"
            "5. 蛋白质在特定位置行使功能",
            font="SimHei",
            line_spacing=0.5
        ).scale(0.6).to_edge(DOWN)

        self.play(Write(modification_steps))
        self.wait(2)

        # 清除场景
        self.play(
            FadeOut(VGroup(title_modification, protein, modification_steps))
        )

    def create_protein_chain(self, length=5):
        """创建蛋白质链"""
        protein = VGroup()

        # 创建氨基酸链
        for i in range(length):
            aa = Circle(radius=0.2, color=PROTEIN_COLOR).set_fill(PROTEIN_COLOR, opacity=0.7)
            aa.move_to([i * 0.5, 0, 0])
            protein.add(aa)

            # 添加肽键连接
            if i > 0:
                bond = Line(
                    protein[i - 1].get_center(),
                    aa.get_center(),
                    color=PROTEIN_COLOR
                )
                protein.add(bond)

        return protein

    def create_folded_protein(self):
        """创建折叠的蛋白质"""
        protein = VGroup()

        # 创建球形蛋白结构
        num_aa = 10
        radius = 0.8

        for i in range(num_aa):
            angle = i * TAU / num_aa
            pos = [radius * np.cos(angle), radius * np.sin(angle), 0]

            aa = Circle(radius=0.15, color=PROTEIN_COLOR).set_fill(PROTEIN_COLOR, opacity=0.7)
            aa.move_to(pos)
            protein.add(aa)

            # 添加肽键连接
            if i > 0:
                bond = Line(
                    protein[2 * (i - 1)].get_center(),
                    aa.get_center(),
                    color=PROTEIN_COLOR
                )
                protein.add(bond)

        return protein

    def create_modified_protein(self):
        """创建修饰后的蛋白质"""
        protein = self.create_folded_protein()

        # 添加修饰基团
        modifications = VGroup()

        # 添加糖基（用小三角表示）
        for i in range(3):
            sugar = Triangle(color=YELLOW).set_fill(YELLOW, opacity=0.7).scale(0.1)
            pos = protein[2 * i].get_center() + UP * 0.2 + RIGHT * 0.2
            sugar.move_to(pos)
            modifications.add(sugar)

        # 添加磷酸基团（用小方块表示）
        for i in range(2):
            phosphate = Square(side_length=0.1, color=RED).set_fill(RED, opacity=0.7)
            pos = protein[2 * i + 1].get_center() + DOWN * 0.2 + LEFT * 0.2
            phosphate.move_to(pos)
            modifications.add(phosphate)

        protein.add(modifications)

        return protein

    def play_gene_regulation(self):
        """基因表达调控部分动画"""
        # 章节标题
        title = Text("第七部分：基因表达调控", font="SimHei").scale(1.2)
        self.play(Write(title))
        self.wait(1)
        self.play(FadeOut(title))

        # 展示原核生物调控
        title_prokaryotic = Text("原核生物基因表达调控", font="SimHei").scale(0.8).to_edge(UP)
        self.play(Write(title_prokaryotic))

        # 展示乳糖操纵子模型
        lac_operon = self.create_lac_operon()
        lac_operon.move_to(ORIGIN)

        self.play(FadeIn(lac_operon))

        # 操纵子说明
        operon_text = Text(
            "乳糖操纵子组成：\n"
            "1. 调节基因(lacI)：编码阻遏蛋白\n"
            "2. 启动子(P)：RNA聚合酶结合位点\n"
            "3. 操作子(O)：阻遏蛋白结合位点\n"
            "4. 结构基因(lacZ, lacY, lacA)：编码酶",
            font="SimHei",
            line_spacing=0.5
        ).scale(0.6).to_edge(LEFT)

        self.play(Write(operon_text))

        # 展示乳糖缺乏时的阻遏
        repression_title = Text("乳糖缺乏：基因表达被阻遏", font="SimHei").scale(0.6).next_to(operon_text, DOWN,
                                                                                             buff=0.5)

        # 阻遏蛋白结合操作子
        repressor = Circle(radius=0.3, color=RED).set_fill(RED, opacity=0.5)
        repressor.move_to(lac_operon[2].get_center() + UP * 0.5)

        repressor_arrow = Arrow(repressor.get_bottom(), lac_operon[2].get_top(), buff=0.1)

        self.play(
            Write(repression_title),
            FadeIn(repressor),
            GrowArrow(repressor_arrow)
        )

        # 展示乳糖存在时的诱导
        induction_title = Text("乳糖存在：基因表达被诱导", font="SimHei").scale(0.6).next_to(repression_title, DOWN,
                                                                                            buff=0.5)

        # 乳糖分子
        lactose = Text("乳糖", font="SimHei").scale(0.4).set_color(BLUE)
        lactose.move_to(repressor.get_center() + RIGHT * 0.8)

        # 阻遏蛋白构象改变
        modified_repressor = Circle(radius=0.3, color=GREY).set_fill(GREY, opacity=0.3)
        modified_repressor.move_to(repressor.get_center() + RIGHT * 1.5)

        self.play(
            Write(induction_title),
            FadeIn(lactose)
        )

        self.play(
            Transform(repressor, modified_repressor),
            FadeOut(repressor_arrow)
        )

        # RNA聚合酶结合并开始转录
        rna_pol = Circle(radius=0.25, color=GREEN).set_fill(GREEN, opacity=0.7)
        rna_pol.move_to(lac_operon[1].get_center() + UP * 0.5)

        pol_arrow = Arrow(rna_pol.get_bottom(), lac_operon[1].get_top(), buff=0.1)

        self.play(
            FadeIn(rna_pol),
            GrowArrow(pol_arrow)
        )

        # mRNA合成
        mrna = Line(lac_operon[1].get_right(), lac_operon[4].get_right() + RIGHT * 0.5, color=RNA_COLOR)
        mrna.shift(UP * 0.3)

        self.play(GrowFromPoint(mrna, lac_operon[1].get_center()))
        self.wait(2)

        # 清除原核调控内容
        self.play(
            FadeOut(VGroup(title_prokaryotic, lac_operon, operon_text, repression_title,
                           repressor, lactose, induction_title, rna_pol, pol_arrow, mrna))
        )

        # 展示真核生物调控
        title_eukaryotic = Text("真核生物基因表达调控", font="SimHei").scale(0.8).to_edge(UP)
        self.play(Write(title_eukaryotic))

        # 展示真核转录调控
        regulation_levels = Text(
            "真核生物调控复杂，发生在多个水平：\n"
            "1. 染色质水平调控\n"
            "2. 转录水平调控\n"
            "3. RNA加工水平调控\n"
            "4. 翻译水平调控\n"
            "5. 翻译后水平调控",
            font="SimHei",
            line_spacing=0.5
        ).scale(0.7).next_to(title_eukaryotic, DOWN, buff=0.5)

        self.play(Write(regulation_levels))

        # 展示染色质结构调控
        chromatin_title = Text("染色质结构调控", font="SimHei").scale(0.7).next_to(regulation_levels, DOWN, buff=0.5)
        self.play(Write(chromatin_title))

        # 创建染色质结构
        nucleosome = VGroup()

        # 组蛋白八聚体
        histone = Circle(radius=0.5, color=BLUE_E).set_fill(BLUE_E, opacity=0.5)

        # DNA缠绕
        dna_wrap = VMobject(color=DNA_COLOR)
        points = []

        for t in np.linspace(0, TAU * 1.75, 50):
            r = 0.5 + 0.1 * np.cos(4 * t)
            x = r * np.cos(t)
            y = r * np.sin(t)
            points.append([x, y, 0])

        dna_wrap.set_points_smoothly(points)

        nucleosome.add(histone, dna_wrap)
        nucleosome.move_to(LEFT * 3)

        self.play(FadeIn(nucleosome))

        # 展示组蛋白修饰
        modification_title = Text("组蛋白修饰", font="SimHei").scale(0.6).next_to(nucleosome, DOWN)

        # 添加组蛋白修饰
        modifications = VGroup()

        # 乙酰化（三角形）
        for i in range(3):
            angle = i * TAU / 3
            pos = histone.get_center() + 0.4 * np.array([np.cos(angle), np.sin(angle), 0])

            acetyl = Triangle(color=YELLOW).set_fill(YELLOW, opacity=0.7).scale(0.1)
            acetyl.move_to(pos)

            modifications.add(acetyl)

        # 甲基化（方块）
        for i in range(2):
            angle = PI / 2 + i * PI
            pos = histone.get_center() + 0.4 * np.array([np.cos(angle), np.sin(angle), 0])

            methyl = Square(side_length=0.1, color=GREEN).set_fill(GREEN, opacity=0.7)
            methyl.move_to(pos)

            modifications.add(methyl)

        self.play(
            Write(modification_title),
            FadeIn(modifications)
        )

        # 染色质解聚
        open_chromatin = VGroup()

        # 组蛋白
        open_histone = histone.copy()

        # 展开的DNA
        open_dna = Line(LEFT * 1, RIGHT * 1, color=DNA_COLOR)

        open_chromatin.add(open_histone, open_dna)
        open_chromatin.move_to(RIGHT * 3)

        # 转录活性变化
        open_label = Text("开放染色质\n(转录活跃)", font="SimHei").scale(0.5).next_to(open_chromatin, DOWN)

        self.play(
            FadeIn(open_chromatin),
            Write(open_label)
        )

        # 染色质调控说明
        chromatin_regulation = Text(
            "染色质调控机制：\n"
            "1. 组蛋白修饰(乙酰化、甲基化等)\n"
            "2. DNA甲基化\n"
            "3. 染色质重塑复合物\n"
            "4. 组蛋白变体",
            font="SimHei",
            line_spacing=0.5
        ).scale(0.6).to_edge(RIGHT)

        self.play(Write(chromatin_regulation))
        self.wait(2)

        # 清除染色质调控内容
        self.play(
            FadeOut(VGroup(chromatin_title, nucleosome, modification_title, modifications,
                           open_chromatin, open_label, chromatin_regulation))
        )

        # 展示转录因子调控
        tf_title = Text("转录因子调控", font="SimHei").scale(0.7).next_to(regulation_levels, DOWN, buff=0.5)
        self.play(Write(tf_title))

        # 创建基因及其调控元件
        gene = Rectangle(height=0.3, width=4, color=DNA_COLOR).set_fill(DNA_COLOR, opacity=0.3)

        # 启动子
        promoter = Rectangle(height=0.3, width=0.5, color=YELLOW).set_fill(YELLOW, opacity=0.5)
        promoter.move_to(gene.get_left() + RIGHT * 0.25)

        # 增强子
        enhancer = Rectangle(height=0.3, width=0.5, color=GREEN).set_fill(GREEN, opacity=0.5)
        enhancer.move_to(gene.get_left() + LEFT * 1)

        # 沉默子
        silencer = Rectangle(height=0.3, width=0.5, color=RED).set_fill(RED, opacity=0.5)
        silencer.move_to(gene.get_right() + RIGHT * 1)

        gene_elements = VGroup(gene, promoter, enhancer, silencer)
        gene_elements.move_to(DOWN * 0.5)

        self.play(FadeIn(gene_elements))

        # 标记各元件
        labels = VGroup(
            Text("基因", font="SimHei").scale(0.4).next_to(gene, DOWN),
            Text("启动子", font="SimHei").scale(0.4).next_to(promoter, UP),
            Text("增强子", font="SimHei").scale(0.4).next_to(enhancer, UP),
            Text("沉默子", font="SimHei").scale(0.4).next_to(silencer, UP)
        )

        self.play(Write(labels))

        # 添加转录因子
        tf1 = Circle(radius=0.2, color=GREEN).set_fill(GREEN, opacity=0.7)
        tf1.move_to(enhancer.get_center() + UP * 0.5)

        tf2 = Circle(radius=0.2, color=BLUE).set_fill(BLUE, opacity=0.7)
        tf2.move_to(promoter.get_center() + UP * 0.5)

        tf3 = Circle(radius=0.2, color=RED).set_fill(RED, opacity=0.7)
        tf3.move_to(silencer.get_center() + UP * 0.5)

        tf_labels = VGroup(
            Text("激活因子", font="SimHei").scale(0.4).next_to(tf1, UP),
            Text("基础转录因子", font="SimHei").scale(0.4).next_to(tf2, UP),
            Text("抑制因子", font="SimHei").scale(0.4).next_to(tf3, UP)
        )

        self.play(
            FadeIn(VGroup(tf1, tf2, tf3)),
            Write(tf_labels)
        )

        # 展示DNA环化
        dna_loop = CubicBezier(
            enhancer.get_center() + UP * 0.2,
            enhancer.get_center() + UP * 1,
            promoter.get_center() + UP * 1,
            promoter.get_center() + UP * 0.2,
            color=DNA_COLOR
        )

        self.play(Create(dna_loop))

        # 转录因子说明
        tf_regulation = Text(
            "转录因子调控机制：\n"
            "1. 激活因子促进转录\n"
            "2. 抑制因子阻碍转录\n"
            "3. 远距离调控元件通过DNA环化作用\n"
            "4. 转录因子网络形成复杂调控",
            font="SimHei",
            line_spacing=0.5
        ).scale(0.6).to_edge(RIGHT)

        self.play(Write(tf_regulation))
        self.wait(2)

        # 清除场景
        self.play(
            FadeOut(VGroup(title_eukaryotic, regulation_levels, tf_title, gene_elements,
                           labels, tf1, tf2, tf3, tf_labels, dna_loop, tf_regulation))
        )

    def create_lac_operon(self):
        """创建乳糖操纵子模型"""
        operon = VGroup()

        # 调节基因
        regulator = Rectangle(height=0.4, width=1, color=BLUE).set_fill(BLUE, opacity=0.3)
        regulator_label = Text("lacI", font="Arial").scale(0.3).move_to(regulator.get_center())

        # 启动子
        promoter = Rectangle(height=0.4, width=0.5, color=GREEN).set_fill(GREEN, opacity=0.3)
        promoter_label = Text("P", font="Arial").scale(0.3).move_to(promoter.get_center())

        # 操作子
        operator = Rectangle(height=0.4, width=0.5, color=RED).set_fill(RED, opacity=0.3)
        operator_label = Text("O", font="Arial").scale(0.3).move_to(operator.get_center())

        # 结构基因
        genes = VGroup()
        gene_labels = VGroup()

        gene_names = ["lacZ", "lacY", "lacA"]
        gene_colors = [YELLOW, PURPLE, ORANGE]

        for i, (name, color) in enumerate(zip(gene_names, gene_colors)):
            gene = Rectangle(height=0.4, width=1, color=color).set_fill(color, opacity=0.3)
            gene_label = Text(name, font="Arial").scale(0.3).move_to(gene.get_center())

            genes.add(gene)
            gene_labels.add(gene_label)

        # 排列操纵子元件
        regulator.move_to(LEFT * 3.5)
        promoter.next_to(regulator, RIGHT, buff=0.2)
        operator.next_to(promoter, RIGHT, buff=0.1)

        for i, gene in enumerate(genes):
            if i == 0:
                gene.next_to(operator, RIGHT, buff=0.1)
            else:
                gene.next_to(genes[i - 1], RIGHT, buff=0.1)

        operon.add(regulator, regulator_label, promoter, promoter_label,
                   operator, operator_label, genes, gene_labels)

        return operon

    def play_genotype_phenotype(self):
        """基因表达与性状关系部分动画"""
        # 章节标题
        title = Text("第八部分：基因表达与性状关系", font="SimHei").scale(1.2)
        self.play(Write(title))
        self.wait(1)
        self.play(FadeOut(title))

        # 展示基因型与表型关系概述
        overview = Text(
            "基因型(Genotype)：生物体的基因组成\n"
            "表型(Phenotype)：生物体可观察到的特征\n\n"
            "基因型通过基因表达影响表型，\n"
            "但这种关系并非简单的一一对应。",
            font="SimHei",
            line_spacing=1
        ).scale(0.7)

        self.play(Write(overview))
        self.wait(2)
        self.play(FadeOut(overview))

        # 展示单基因遗传病
        title_single_gene = Text("单基因遗传病", font="SimHei").scale(0.8).to_edge(UP)
        self.play(Write(title_single_gene))

        # 镰刀型贫血症示例
        sickle_cell_title = Text("镰刀型贫血症", font="SimHei").scale(0.7).next_to(title_single_gene, DOWN, buff=0.5)
        self.play(Write(sickle_cell_title))

        # 创建正常和镰刀型红细胞
        normal_cell = Circle(radius=0.8, color=RED).set_fill(RED, opacity=0.3)
        normal_cell.move_to(LEFT * 3)

        sickle_cell = ArcPolygon(
            [-0.8, 0.3, 0],
            [0.8, 0.3, 0],
            [0.6, -0.3, 0],
            [-0.6, -0.3, 0],
            color=RED
        ).set_fill(RED, opacity=0.3)
        sickle_cell.move_to(RIGHT * 3)

        self.play(FadeIn(normal_cell), FadeIn(sickle_cell))

        # 细胞标签
        normal_label = Text("正常红细胞(HbA/HbA)", font="SimHei").scale(0.5).next_to(normal_cell, DOWN)
        sickle_label = Text("镰刀型红细胞(HbS/HbS)", font="SimHei").scale(0.5).next_to(sickle_cell, DOWN)

        self.play(Write(normal_label), Write(sickle_label))

        # 展示分子机制
        mechanism_title = Text("分子机制", font="SimHei").scale(0.6).to_edge(LEFT, buff=1).shift(UP * 0.5)
        self.play(Write(mechanism_title))

        # DNA序列变异
        dna_normal = Text("...CTGAGG...", font="Courier").scale(0.6).next_to(mechanism_title, DOWN, buff=0.3)
        dna_mutant = Text("...CTGTGG...", font="Courier").scale(0.6).next_to(dna_normal, DOWN, buff=0.3)

        # 高亮突变位点
        dna_mutant[6].set_color(RED)

        self.play(Write(dna_normal), Write(dna_mutant))

        # 蛋白质变化
        protein_normal = Text("...Glu...", font="Courier").scale(0.6).next_to(dna_normal, RIGHT, buff=1)
        protein_mutant = Text("...Val...", font="Courier").scale(0.6).next_to(dna_mutant, RIGHT, buff=1)

        protein_normal.set_color(GREEN)
        protein_mutant.set_color(RED)

        arrow1 = Arrow(dna_normal.get_right(), protein_normal.get_left(), buff=0.2)
        arrow2 = Arrow(dna_mutant.get_right(), protein_mutant.get_left(), buff=0.2)

        self.play(
            GrowArrow(arrow1),
            GrowArrow(arrow2),
            Write(protein_normal),
            Write(protein_mutant)
        )

        # 疾病后果
        consequences = Text(
            "后果：\n"
            "1. 血红蛋白结构异常\n"
            "2. 红细胞变形\n"
            "3. 血液循环障碍\n"
            "4. 组织缺氧、疼痛",
            font="SimHei",
            line_spacing=0.5
        ).scale(0.6).to_edge(RIGHT)

        self.play(Write(consequences))
        self.wait(2)

        # 清除单基因疾病内容
        self.play(
            FadeOut(VGroup(title_single_gene, sickle_cell_title, normal_cell, sickle_cell,
                           normal_label, sickle_label, mechanism_title, dna_normal, dna_mutant,
                           protein_normal, protein_mutant, arrow1, arrow2, consequences))
        )

        # 展示多基因性状
        title_polygenic = Text("多基因性状", font="SimHei").scale(0.8).to_edge(UP)
        self.play(Write(title_polygenic))

        # 身高示例
        height_title = Text("人类身高", font="SimHei").scale(0.7).next_to(title_polygenic, DOWN, buff=0.5)
        self.play(Write(height_title))

        # 创建正态分布图
        axes = Axes(
            x_range=[-4, 4, 1],
            y_range=[0, 0.5, 0.1],
            axis_config={"include_tip": False}
        )

        # 创建正态分布曲线
        def normal_pdf(x):
            return np.exp(-x ** 2 / 2) / np.sqrt(2 * np.pi)

        normal_curve = axes.plot(normal_pdf, color=BLUE)

        # 添加轴标签
        x_label = Text("身高", font="SimHei").scale(0.5).next_to(axes.x_axis, DOWN)
        y_label = Text("频率", font="SimHei").scale(0.5).next_to(axes.y_axis, LEFT)

        graph = VGroup(axes, normal_curve, x_label, y_label)
        graph.scale(0.7).shift(DOWN * 0.5)

        self.play(Create(graph))

        # 多基因性状说明
        polygenic_text = Text(
            "身高是典型的多基因性状：\n"
            "1. 受数百个基因共同影响\n"
            "2. 每个基因效应较小\n"
            "3. 呈连续分布\n"
            "4. 环境因素也有重要影响",
            font="SimHei",
            line_spacing=0.5
        ).scale(0.6).to_edge(LEFT)

        self.play(Write(polygenic_text))

        # 展示影响身高的因素
        factors = VGroup(
            Text("基因因素：", font="SimHei").scale(0.6),
            Text("GH1(生长激素)", font="SimHei").scale(0.5),
            Text("HMGA2", font="SimHei").scale(0.5),
            Text("IGF1(胰岛素样生长因子)", font="SimHei").scale(0.5),
            Text("...(数百个基因)", font="SimHei").scale(0.5),
            Text("环境因素：", font="SimHei").scale(0.6),
            Text("营养状况", font="SimHei").scale(0.5),
            Text("疾病状态", font="SimHei").scale(0.5),
            Text("激素水平", font="SimHei").scale(0.5)
        )

        factors.arrange(DOWN, aligned_edge=LEFT, buff=0.2).to_edge(RIGHT)

        self.play(Write(factors, run_time=3))
        self.wait(2)

        # 清除多基因性状内容
        self.play(
            FadeOut(VGroup(title_polygenic, height_title, graph, polygenic_text, factors))
        )

        # 展示基因-环境互作
        title_interaction = Text("基因-环境互作", font="SimHei").scale(0.8).to_edge(UP)
        self.play(Write(title_interaction))

        # 创建基因-环境互作示意图
        genotype_label = Text("基因型", font="SimHei").scale(0.7).shift(LEFT * 3 + UP * 1)
        environment_label = Text("环境", font="SimHei").scale(0.7).shift(RIGHT * 3 + UP * 1)
        phenotype_label = Text("表型", font="SimHei").scale(0.7).shift(DOWN * 1.5)

        g_arrow = Arrow(genotype_label.get_bottom(), phenotype_label.get_top() + LEFT * 1, buff=0.2)
        e_arrow = Arrow(environment_label.get_bottom(), phenotype_label.get_top() + RIGHT * 1, buff=0.2)

        interaction_arrow = CubicBezier(
            genotype_label.get_right(),
            UP * 1,
            UP * 1,
            environment_label.get_left(),
            color=YELLOW
        )

        self.play(
            Write(genotype_label),
            Write(environment_label),
            Write(phenotype_label),
            GrowArrow(g_arrow),
            GrowArrow(e_arrow),
            Create(interaction_arrow)
        )

        # 表观遗传示例
        epigenetic_title = Text("表观遗传调控", font="SimHei").scale(0.6).to_edge(DOWN, buff=2)

        epigenetic_text = Text(
            "环境因素可通过表观遗传修饰影响基因表达：\n"
            "- 饮食影响DNA甲基化\n"
            "- 压力影响组蛋白修饰\n"
            "- 毒素暴露改变非编码RNA表达",
            font="SimHei",
            line_spacing=0.5
        ).scale(0.5).next_to(epigenetic_title, DOWN)

        self.play(Write(epigenetic_title), Write(epigenetic_text))

        # 实例说明
        example_title = Text("实例：相同基因型，不同环境", font="SimHei").scale(0.6).next_to(interaction_arrow, DOWN,
                                                                                           buff=0.5)

        examples = VGroup(
            Text("1. 同卵双胞胎在不同环境中表型差异", font="SimHei").scale(0.5),
            Text("2. 植物在不同光照条件下形态变化", font="SimHei").scale(0.5),
            Text("3. 蜜蜂幼虫食用蜂王浆发育为蜂王", font="SimHei").scale(0.5)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).next_to(example_title, DOWN)

        self.play(Write(example_title), Write(examples))
        self.wait(2)

        # 清除场景
        self.play(
            FadeOut(VGroup(title_interaction, genotype_label, environment_label, phenotype_label,
                           g_arrow, e_arrow, interaction_arrow, epigenetic_title, epigenetic_text,
                           example_title, examples))
        )

    def play_extended_content(self):
        """扩展内容部分动画"""
        # 章节标题
        title = Text("第九部分：扩展内容", font="SimHei").scale(1.2)
        self.play(Write(title))
        self.wait(1)
        self.play(FadeOut(title))

        # 展示基因组学与后基因组学
        title_genomics = Text("基因组学与后基因组学", font="SimHei").scale(0.8).to_edge(UP)
        self.play(Write(title_genomics))

        # 人类基因组计划时间线
        timeline = Line(LEFT * 5, RIGHT * 5, color=WHITE)

        events = [
            (LEFT * 5, "1990", "人类基因组计划启动"),
            (LEFT * 3, "2001", "人类基因组草图"),
            (LEFT * 1, "2003", "人类基因组完成"),
            (RIGHT * 1, "2010", "1000基因组计划"),
            (RIGHT * 3, "2015", "精准医学计划"),
            (RIGHT * 5, "2022", "完整人类基因组")
        ]

        timeline_points = VGroup()
        timeline_labels = VGroup()

        for pos, year, event in events:
            point = Dot(color=WHITE).move_to(pos)
            year_label = Text(year, font="Arial").scale(0.4).next_to(point, UP, buff=0.1)
            event_label = Text(event, font="SimHei").scale(0.4).next_to(year_label, UP, buff=0.1)

            timeline_points.add(point)
            timeline_labels.add(VGroup(year_label, event_label))

        timeline_group = VGroup(timeline, timeline_points, timeline_labels)
        timeline_group.move_to(ORIGIN)

        self.play(Create(timeline), FadeIn(timeline_points))
        self.play(Write(timeline_labels))

        # 展示基因组学发展
        genomics_text = Text(
            "基因组学进展：\n"
            "1. 从基因组测序到功能解析\n"
            "2. 比较基因组学揭示进化关系\n"
            "3. 多组学整合研究生命系统\n"
            "4. 大数据和AI加速发现",
            font="SimHei",
            line_spacing=0.5
        ).scale(0.6).to_edge(DOWN, buff=1)

        self.play(Write(genomics_text))
        self.wait(2)

        # 清除基因组学内容
        self.play(
            FadeOut(VGroup(title_genomics, timeline_group, genomics_text))
        )

        # 展示精准医疗
        title_medicine = Text("精准医疗", font="SimHei").scale(0.8).to_edge(UP)
        self.play(Write(title_medicine))

        # 创建精准医疗流程图
        flow_start = Circle(radius=0.5, color=BLUE).set_fill(BLUE, opacity=0.3)
        flow_start_text = Text("基因检测", font="SimHei").scale(0.4).move_to(flow_start.get_center())

        flow_step1 = Rectangle(height=1, width=1.5, color=GREEN).set_fill(GREEN, opacity=0.3)
        flow_step1_text = Text("风险评估", font="SimHei").scale(0.4).move_to(flow_step1.get_center())

        flow_step2 = Rectangle(height=1, width=1.5, color=YELLOW).set_fill(YELLOW, opacity=0.3)
        flow_step2_text = Text("个性化治疗", font="SimHei").scale(0.4).move_to(flow_step2.get_center())

        flow_end = Circle(radius=0.5, color=RED).set_fill(RED, opacity=0.3)
        flow_end_text = Text("疗效监测", font="SimHei").scale(0.4).move_to(flow_end.get_center())

        # 排列流程图
        flow_start.move_to(LEFT * 4)
        flow_step1.move_to(LEFT * 1.5)
        flow_step2.move_to(RIGHT * 1.5)
        flow_end.move_to(RIGHT * 4)

        # 连接箭头
        arrow1 = Arrow(flow_start.get_right(), flow_step1.get_left(), buff=0.2)
        arrow2 = Arrow(flow_step1.get_right(), flow_step2.get_left(), buff=0.2)
        arrow3 = Arrow(flow_step2.get_right(), flow_end.get_left(), buff=0.2)

        flow_chart = VGroup(
            flow_start, flow_start_text,
            flow_step1, flow_step1_text,
            flow_step2, flow_step2_text,
            flow_end, flow_end_text,
            arrow1, arrow2, arrow3
        )

        self.play(FadeIn(flow_chart))

        # 精准医疗应用
        applications = VGroup(
            Text("肿瘤治疗：", font="SimHei").scale(0.6),
            Text("根据癌症基因组特征选择靶向药物", font="SimHei").scale(0.5),
            Text("药物基因组学：", font="SimHei").scale(0.6),
            Text("根据个体代谢基因调整用药剂量", font="SimHei").scale(0.5),
            Text("疾病预防：", font="SimHei").scale(0.6),
            Text("评估遗传性疾病风险，早期干预", font="SimHei").scale(0.5)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2).to_edge(DOWN, buff=1)

        self.play(Write(applications))
        self.wait(2)

        # 清除精准医疗内容
        self.play(
            FadeOut(VGroup(title_medicine, flow_chart, applications))
        )

        # 展示前沿技术
        title_frontier = Text("前沿技术展望", font="SimHei").scale(0.8).to_edge(UP)
        self.play(Write(title_frontier))

        # 创建CRISPR基因编辑示意图
        dna = self.create_simple_dna(length=6)
        dna.move_to(UP * 0.5)

        # Cas9蛋白
        cas9 = RegularPolygon(n=6, color=GREEN).set_fill(GREEN, opacity=0.5).scale(0.5)
        cas9.move_to(dna.get_center())

        cas9_label = Text("Cas9", font="Arial").scale(0.4).next_to(cas9, UP)

        # 引导RNA
        guide_rna = ArcBetweenPoints(
            cas9.get_left() + LEFT * 0.2,
            cas9.get_bottom() + DOWN * 0.2,
            angle=PI / 2,
            color=RNA_COLOR
        )

        guide_label = Text("gRNA", font="Arial").scale(0.4).next_to(guide_rna, LEFT)

        # 切割位点
        cut_line = Line(UP * 0.2, DOWN * 0.2, color=RED)
        cut_line.move_to(cas9.get_right())

        crispr_group = VGroup(dna, cas9, cas9_label, guide_rna, guide_label, cut_line)

        self.play(FadeIn(crispr_group))

        # CRISPR说明
        crispr_text = Text(
            "CRISPR-Cas9基因编辑：\n"
            "1. 精确靶向DNA特定序列\n"
            "2. 切割DNA引入修饰\n"
            "3. 应用于基础研究和疾病治疗",
            font="SimHei",
            line_spacing=0.5
        ).scale(0.6).to_edge(LEFT)

        self.play(Write(crispr_text))

        # 其他前沿技术
        other_tech = VGroup(
            Text("单细胞测序", font="SimHei").scale(0.6),
            Text("空间转录组学", font="SimHei").scale(0.6),
            Text("基因治疗", font="SimHei").scale(0.6),
            Text("合成生物学", font="SimHei").scale(0.6),
            Text("生物计算", font="SimHei").scale(0.6)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).to_edge(RIGHT)

        self.play(Write(other_tech))

        # 未来展望
        future = Text(
            "未来展望：\n"
            "1. 治愈遗传疾病\n"
            "2. 个性化健康管理\n"
            "3. 延长健康寿命\n"
            "4. 解答生命本质",
            font="SimHei",
            line_spacing=0.5
        ).scale(0.6).to_edge(DOWN, buff=1)

        self.play(Write(future))
        self.wait(2)

        # 清除场景
        self.play(
            FadeOut(VGroup(title_frontier, crispr_group, crispr_text, other_tech, future))
        )

    def play_conclusion(self):
        """结语部分动画"""
        # 从DNA到生物体的过渡
        dna = self.create_dna_helix(num_rungs=10)
        self.play(FadeIn(dna))

        # 缩放至细胞
        cell = Circle(radius=2, color=WHITE).set_fill(opacity=0.2)
        nucleus = Circle(radius=0.8, color=BLUE_D).set_fill(BLUE_D, opacity=0.4)
        cell_group = VGroup(cell, nucleus)

        self.play(
            Transform(dna, cell_group),
            run_time=2
        )

        # 缩放至组织
        tissue = VGroup()
        for i in range(5):
            for j in range(5):
                c = Circle(radius=0.3, color=WHITE).set_fill(WHITE, opacity=0.1)
                c.move_to([0.7 * i - 1.4, 0.7 * j - 1.4, 0])
                tissue.add(c)

        self.play(
            Transform(dna, tissue),
            run_time=2
        )

        # 缩放至人体轮廓
        human = SVGMobject("human_outline.svg", height=4)  # 假设有此SVG文件
        # 如果没有SVG，可以用简单形状代替
        if not os.path.exists("human_outline.svg"):
            human = VGroup(
                Circle(radius=0.5).shift(UP * 1.5),  # 头
                Line(UP * 1, DOWN * 1),  # 身体
                Line(UP * 0.5, UP * 0.5 + LEFT),  # 左臂
                Line(UP * 0.5, UP * 0.5 + RIGHT),  # 右臂
                Line(DOWN * 1, DOWN * 2 + LEFT * 0.5),  # 左腿
                Line(DOWN * 1, DOWN * 2 + RIGHT * 0.5)  # 右腿
            )

        self.play(
            Transform(dna, human),
            run_time=2
        )

        # 缩放至生物多样性
        diversity = VGroup()
        # 简化的动物轮廓
        for i in range(5):
            shape = random.choice([
                Circle(radius=0.3),  # 简单生物
                Triangle(radius=0.6),  # 鱼类
                Square(side_length=0.5),  # 昆虫
                RegularPolygon(n=5, radius=0.3),  # 星形动物
                RegularPolygon(n=6, radius=0.3)  # 花朵
            ])
            pos = np.array([random.uniform(-4, 4), random.uniform(-3, 3), 0])
            shape.move_to(pos)
            diversity.add(shape)

        self.play(
            Transform(dna, diversity),
            run_time=2
        )

        # 最终转变为DNA和星空
        final_dna = self.create_dna_helix(num_rungs=8)

        # 创建星空背景
        stars = VGroup()
        for _ in range(100):
            pos = np.array([random.uniform(-7, 7), random.uniform(-4, 4), 0])
            star = Dot(pos, radius=random.uniform(0.005, 0.02), color=WHITE)
            stars.add(star)

        final_scene = VGroup(final_dna, stars)

        self.play(
            Transform(dna, final_scene),
            run_time=3
        )

        # 添加结语文字
        conclusion = Text(
            "从简单的分子到复杂的生命，基因表达编织着生命的奇迹。\n"
            "每一个生命都是数十亿年进化的产物，每一个基因都承载着漫长历史的印记。\n"
            "随着科技的进步，我们正逐渐揭开生命的奥秘，\n"
            "但仍有无数未知等待探索。",
            font="SimHei",
            line_spacing=1
        ).scale(0.6).to_edge(DOWN, buff=1)

        self.play(Write(conclusion, run_time=5))

        # 最终标题
        final_title = Text("生命的密码：永无止境的探索", font="SimHei").scale(1.2).to_edge(UP)

        self.play(Write(final_title))
        self.play(
            Rotate(final_dna, angle=2 * PI, axis=UP, run_time=5)
        )
        self.wait(3)

        self.play(
            FadeOut(dna),
            FadeOut(conclusion),
            FadeOut(final_title),
            run_time=2
        )