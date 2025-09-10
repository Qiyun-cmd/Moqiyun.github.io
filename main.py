from manim import *
import numpy as np
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from my_manim_setup import *

# =========================================
# 字体与配色
# =========================================

def CText(s, **kwargs):
    # 中文统一使用 STSong
    return Text(s, font="STSong", **kwargs)

MAIN_COLOR = "#2E86AB"
ACCENT = "#F18F01"
DNA_COLOR = "#0055FF"
RNA_COLOR = "#00AA88"
PRO_COLOR = "#D7263D"
VIRUS_PURPLE = "#7F3FBF"
PLANT_GREEN = "#2FAA60"
BACTERIA_CYAN = "#21A0A0"
WALL_ORANGE = "#F6A01A"
NAG_COLOR = "#6FA8DC"   # NAG
NAM_COLOR = "#F5A623"   # NAM
LINK_COLOR = "#BBBBBB"

# =========================================
# 小工具：带底板的中文文本，避免遮挡
# =========================================

def label_with_bg(text_cn, color=WHITE, bg_color="#0E1222", pad=0.15, scale=0.55):
    t = CText(text_cn, color=color).scale(scale)
    bg = RoundedRectangle(width=t.width + 2*pad, height=t.height + 2*pad, corner_radius=0.12)
    bg.set_fill(bg_color, opacity=0.85).set_stroke("#334", width=1)
    g = VGroup(bg, t)
    t.move_to(bg.get_center())
    g.set_z_index(10)
    return g

def section_card(title, subtitle=None):
    base = RoundedRectangle(width=12.0, height=6.0, corner_radius=0.3).set_fill("#0F1226", opacity=0.95).set_stroke("#334", width=2)
    head = Rectangle(width=12.0, height=0.9).set_fill("#1D2545", opacity=1.0).set_stroke(width=0).move_to(base.get_top()+DOWN*0.45)
    t1 = CText(title, color=WHITE).scale(0.7).move_to(head.get_center())
    g = VGroup(base, head, t1)
    if subtitle:
        t2 = CText(subtitle, color=GREY_B).scale(0.45).next_to(t1, DOWN, buff=0.08)
        g.add(t2)
    g.set_z_index(9)
    return g

def make_stage_panel():
    # 舞台面板：所有复杂动画都放在这里，避免与外界元素交错
    panel = RoundedRectangle(width=12.0, height=6.2, corner_radius=0.25).set_fill("#0D1020", opacity=0.95).set_stroke("#223", width=2)
    return panel

# =========================================
# 基础图元
# =========================================

def make_cell():
    cell = Circle(radius=2.8, color=WHITE, stroke_width=6)
    cell.set_fill(MAIN_COLOR, opacity=0.06)
    nucleus = Circle(radius=1.0, color=BLUE_E, stroke_width=4).set_fill(BLUE_E, opacity=0.1)
    nucleus.shift(0.6*LEFT + 0.2*UP)
    return VGroup(cell, nucleus)

def make_ribosome():
    top = Ellipse(width=1.6, height=0.6).set_fill(GREY_E, opacity=0.8).set_stroke(GREY_E, width=2)
    bot = Ellipse(width=2.2, height=0.8).set_fill(GREY_D, opacity=0.8).set_stroke(GREY_D, width=2)
    top.shift(0.2*UP); bot.shift(0.2*DOWN)
    return VGroup(bot, top)

def make_gene_diagram():
    line = Line(LEFT*5, RIGHT*5, stroke_width=6, color=DNA_COLOR)
    promoter = Rectangle(width=1.5, height=0.6).set_fill(YELLOW, opacity=0.5).set_stroke(YELLOW, width=2)
    exon1 = Rectangle(width=1.8, height=0.6).set_fill(GREEN, opacity=0.6).set_stroke(GREEN, width=2)
    intron = Rectangle(width=2.4, height=0.4).set_fill(GREY_BROWN, opacity=0.4).set_stroke(GREY_BROWN, width=2)
    exon2 = Rectangle(width=2.0, height=0.6).set_fill(GREEN, opacity=0.6).set_stroke(GREEN, width=2)
    promoter.move_to(line.get_left() + RIGHT*1.2)
    exon1.next_to(promoter, RIGHT, buff=0.2)
    intron.next_to(exon1, RIGHT, buff=0.2).align_to(exon1, DOWN)
    exon2.next_to(intron, RIGHT, buff=0.2).align_to(exon1, UP)
    t_promoter = CText("启动子", color=BLACK).scale(0.5).move_to(promoter)
    t_exon1 = CText("外显子", color=BLACK).scale(0.5).move_to(exon1)
    t_intron = CText("内含子", color=BLACK).scale(0.5).move_to(intron)
    t_exon2 = CText("外显子", color=BLACK).scale(0.5).move_to(exon2)
    g = VGroup(line, promoter, exon1, intron, exon2, t_promoter, t_exon1, t_intron, t_exon2)
    return g

def make_bacterium():
    cell = RoundedRectangle(width=5.5, height=3.0, corner_radius=1.4).set_stroke(BACTERIA_CYAN, width=6)
    cell.set_fill(BACTERIA_CYAN, opacity=0.08)
    wall = RoundedRectangle(width=6.1, height=3.6, corner_radius=1.6).set_stroke(WALL_ORANGE, width=6)
    wall.set_fill(WALL_ORANGE, opacity=0.05).move_to(cell.get_center())
    dots = VGroup(*[Dot(color=GREY_B, radius=0.06).move_to(cell.get_center() + np.array([
        np.random.uniform(-2.0, 2.0), np.random.uniform(-1.1, 1.1), 0])) for _ in range(60)])
    return VGroup(wall, cell, dots)

# =========================================
# HIV（带锥形核心）
# =========================================

def make_capsid_cone(scale=1.0, color=VIRUS_PURPLE):
    h = 1.0 * scale
    w_top = 0.20 * scale
    w_bot = 0.60 * scale
    pts = [
        np.array([0,  0.50*h, 0.0]),
        np.array([0.5*w_top,  0.30*h, 0.0]),
        np.array([0.5*w_bot, -0.45*h, 0.0]),
        np.array([0,        -0.50*h, 0.0]),
        np.array([-0.5*w_bot, -0.45*h, 0.0]),
        np.array([-0.5*w_top,  0.30*h, 0.0]),
    ]
    cone = Polygon(*pts).set_stroke(color, width=3).set_fill(color, opacity=0.18)
    cross1 = Line(0.35*w_bot*LEFT + 0.1*h*UP, 0.35*w_bot*RIGHT + 0.1*h*UP, color=color, stroke_width=2, stroke_opacity=0.6)
    cross2 = Line(0.45*w_bot*LEFT + 0.0*UP, 0.45*w_bot*RIGHT + 0.0*UP, color=color, stroke_width=2, stroke_opacity=0.45)
    cross3 = Line(0.25*w_bot*LEFT + 0.25*h*DOWN, 0.25*w_bot*RIGHT + 0.25*h*DOWN, color=color, stroke_width=2, stroke_opacity=0.35)
    g = VGroup(cone, cross1, cross2, cross3)
    g.set_z_index(3)
    return g

def make_hiv_virion(scale=1.0, cone_core=False):
    outer = Circle(radius=0.9*scale, color=VIRUS_PURPLE, stroke_width=6)
    outer.set_fill(VIRUS_PURPLE, opacity=0.08)
    spikes = VGroup()
    for k in range(12):
        ang = k * TAU / 12
        tri = Triangle().scale(0.12*scale)
        tri.set_fill(VIRUS_PURPLE, opacity=0.9).set_stroke(VIRUS_PURPLE, width=1.5)
        tri.rotate(ang + PI/2)
        tri.move_to(outer.point_at_angle(ang) + 0.12*scale*np.array([np.cos(ang), np.sin(ang), 0]))
        spikes.add(tri)
    core = make_capsid_cone(scale=0.6*scale) if cone_core else Polygon(
        0.33*scale*LEFT + 0.30*scale*UP,
        0.40*scale*RIGHT + 0.15*scale*UP,
        0.45*scale*RIGHT + 0.05*scale*DOWN,
        0.20*scale*RIGHT + 0.30*scale*DOWN,
        0.25*scale*LEFT + 0.25*scale*DOWN,
        0.38*scale*LEFT + 0.05*scale*UP
    ).set_stroke(VIRUS_PURPLE, width=3).set_fill(VIRUS_PURPLE, opacity=0.15)

    r1 = ParametricFunction(
        lambda t: np.array([0.24*scale*np.cos(2*t), 0.12*scale*np.sin(t)-0.05*scale, 0]),
        t_range=[-PI, PI], color=RNA_COLOR, stroke_width=3
    )
    r2 = ParametricFunction(
        lambda t: np.array([0.22*scale*np.cos(2*t+0.9), 0.12*scale*np.sin(t+0.3)-0.08*scale, 0]),
        t_range=[-PI, PI], color=RNA_COLOR, stroke_width=3
    )
    g = VGroup(outer, spikes, core, r1, r2)
    g.set_z_index(2)
    return g

# =========================================
# TMV 螺旋装配（二维近似）
# =========================================

def make_tmv(scale=1.0):
    body = RoundedRectangle(corner_radius=0.15*scale, width=2.0*scale, height=0.35*scale)
    body.set_fill(PLANT_GREEN, opacity=0.3).set_stroke(PLANT_GREEN, width=4)
    inner_rna = ParametricFunction(
        lambda t: np.array([0.8*scale*t, 0.12*scale*np.sin(6*PI*t), 0]),
        t_range=[-0.9, 0.9], color=RNA_COLOR, stroke_width=3
    ).move_to(body.get_center())
    g = VGroup(body, inner_rna)
    g.set_z_index(2)
    return g

def build_tmv_helical_units(length=3.6, pitch=0.28, amp=0.16, density=28, center=ORIGIN, color=PLANT_GREEN):
    units = VGroup()
    turns = length / pitch / TAU
    N = int(turns * density * TAU)
    for i in range(N):
        t = i / density
        x = t * pitch
        y = amp * np.sin(2*PI * t)
        rect = RoundedRectangle(width=0.16, height=0.10, corner_radius=0.03).set_fill(color, opacity=0.85).set_stroke(color, width=1.5)
        rect.move_to(center + RIGHT*x + UP*y)
        rect.rotate(0.4*np.sin(2*PI * t))
        rect.set_z_index(3)
        units.add(rect)
    rna = Line(center + LEFT*0.1, center + RIGHT*length + LEFT*0.1, color=RNA_COLOR, stroke_width=5)
    rna.set_z_index(2)
    return VGroup(rna, units)

# =========================================
# 肽聚糖网格（更精细交联）
# =========================================

def make_pg_mesh(rows=5, cols=10, spacing_x=0.46, spacing_y=0.40, origin=ORIGIN):
    sugars = VGroup()
    bonds = VGroup()
    sugar_grid = []
    for r in range(rows):
        row_objs = []
        for c in range(cols):
            color = NAG_COLOR if (c % 2 == 0) else NAM_COLOR
            bead = RoundedRectangle(width=0.14, height=0.12, corner_radius=0.03)\
                .set_fill(color, opacity=0.95).set_stroke(color, width=1)
            bead.move_to(origin + RIGHT*spacing_x*c + DOWN*spacing_y*r)
            bead.set_z_index(2)
            sugars.add(bead)
            row_objs.append(bead)
            if c > 0:
                prev = row_objs[c-1].get_center()
                cur = bead.get_center()
                line = Line(prev, cur, color=LINK_COLOR, stroke_width=3)
                line.set_z_index(1)
                bonds.add(line)
        sugar_grid.append(row_objs)
    crosslinks = VGroup()
    for r in range(rows-1):
        for c in range(1, cols-1, 2):
            p = sugar_grid[r][c].get_center()
            q = sugar_grid[r+1][c].get_center()
            mid = 0.5*(p+q) + 0.08*RIGHT
            seg1 = Line(p+0.05*DOWN, mid, color=YELLOW, stroke_width=3)
            seg2 = Line(mid, q+0.05*UP, color=YELLOW, stroke_width=3)
            crosslinks.add(VGroup(seg1, seg2))
    return VGroup(bonds, sugars), crosslinks

# =========================================
# 卡片组件
# =========================================

def make_card(title_cn, bullets_cn, color=ACCENT, width=7.2, height=4.2):
    card = RoundedRectangle(width=width, height=height, corner_radius=0.25)\
        .set_stroke(color, width=4).set_fill(BLACK, opacity=0.06)
    shadow = card.copy().set_fill(BLACK, opacity=0.12).set_stroke(width=0).shift(0.12*DOWN+0.12*RIGHT)
    header = Rectangle(width=width, height=0.7).set_fill(color, opacity=0.9).set_stroke(color, width=0)\
        .move_to(card.get_top()+DOWN*0.35)
    title = CText(title_cn, color=BLACK).scale(0.6).move_to(header.get_center())
    items = VGroup(*[CText(txt).scale(0.52).set_color(WHITE) for txt in bullets_cn])\
        .arrange(DOWN, aligned_edge=LEFT, buff=0.25)
    items.next_to(header, DOWN, buff=0.4).align_to(card, LEFT).shift(RIGHT*0.4)
    g = VGroup(shadow, card, header, title, items)
    g.set_z_index(8)
    return g

# =========================================
# 主场景（一次性渲染 2D+3D，避免遮挡）
# =========================================

class LectureAll(ThreeDScene):
    def construct(self):
        # ---------- 开场 ----------
        splash = section_card("遗传信息传递与中心法则：从病毒到抗菌机制",
                              "HIV / TMV 生命历程 · 基因表达 · 青霉素/红霉素/利福平机制")
        self.play(FadeIn(splash, shift=UP*0.2), run_time=1.2)
        self.wait(2.5)
        self.play(FadeOut(splash), run_time=0.8)

        # ---------- 中心法则 ----------
        title = CText("中心法则与信息流扩展", color=MAIN_COLOR).scale(0.8).to_edge(UP)
        self.play(FadeIn(title, shift=UP*0.2), run_time=0.8)

        dogma = MathTex(r"\text{DNA} \rightarrow \text{RNA} \rightarrow \text{Protein}", font_size=60).shift(UP*0.5)
        note = label_with_bg("经典中心法则：DNA → RNA → 蛋白质", scale=0.55).next_to(dogma, DOWN, buff=0.4)
        self.play(Write(dogma), run_time=2.0)
        self.play(FadeIn(note), run_time=0.8)
        self.wait(1.5)

        flows = VGroup(
            MathTex(r"\text{RNA} \xrightarrow{\text{reverse transcription}} \text{DNA}", font_size=42),
            MathTex(r"\text{RNA} \xrightarrow{\text{RdRP}} \text{RNA}", font_size=42),
            MathTex(r"\text{DNA} \xrightarrow{\text{DNA Pol}} \text{DNA}", font_size=42),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.35).next_to(dogma, DOWN, buff=1.0)
        caps = VGroup(
            label_with_bg("逆转录：如 HIV（逆转录病毒）", color=YELLOW_A),
            label_with_bg("RNA 复制：如 TMV 等 RNA 病毒", color=YELLOW_A),
            label_with_bg("DNA 复制：细胞与 DNA 病毒通用", color=YELLOW_A),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.22).next_to(flows, RIGHT, buff=0.6)
        self.play(LaggedStart(*[Write(f) for f in flows], lag_ratio=0.2), run_time=2.8)
        self.play(LaggedStart(*[FadeIn(c, shift=RIGHT*0.2) for c in caps], lag_ratio=0.15), run_time=1.6)
        self.wait(3)

        # ---------- 基因表达 ----------
        self.play(FadeOut(caps), FadeOut(flows), FadeOut(note), dogma.animate.to_edge(UP), run_time=0.8)
        stage = make_stage_panel().move_to(ORIGIN)
        self.play(FadeIn(stage), run_time=0.6)
        gene = make_gene_diagram().scale(0.85).move_to(stage.get_top()+DOWN*1.3)
        cap_gene = label_with_bg("基因结构：启动子/外显子/内含子", scale=0.55).next_to(gene, UP, buff=0.2)
        self.play(Create(gene), FadeIn(cap_gene), run_time=1.6)

        pol_arrow = Arrow(start=gene.get_left()+RIGHT*0.8, end=gene.get_left()+RIGHT*2.0,
                          buff=0.0, color=RNA_COLOR).shift(0.9*UP)
        pol_label = MathTex(r"\text{RNA Pol II}", color=RNA_COLOR).scale(0.6).next_to(pol_arrow, UP, buff=0.2)
        self.play(GrowArrow(pol_arrow), FadeIn(pol_label), run_time=1.0)
        pre_mrna = Line(LEFT*4.0, RIGHT*4.0, color=RNA_COLOR, stroke_width=6).move_to(stage.get_center()+UP*0.6)
        cap_pre = label_with_bg("前体 mRNA（含内含子）", color=RNA_COLOR, scale=0.5).next_to(pre_mrna, DOWN, buff=0.2)
        self.play(Create(pre_mrna), FadeIn(cap_pre), run_time=1.2)

        splice_brace = BraceBetweenPoints(pre_mrna.get_left()+RIGHT*1.8, pre_mrna.get_left()+RIGHT*3.6, color=YELLOW)
        splice_txt = label_with_bg("剪接：去除内含子", color=YELLOW, scale=0.5).next_to(splice_brace, DOWN)
        self.play(Create(splice_brace), FadeIn(splice_txt), run_time=0.8)
        mature_mrna = Line(LEFT*3.0, RIGHT*3.0, color=RNA_COLOR, stroke_width=6).move_to(stage.get_center()+UP*0.05)
        cap_mrna = label_with_bg("成熟 mRNA（外显子拼接）", color=RNA_COLOR, scale=0.5).next_to(mature_mrna, DOWN, buff=0.2)
        self.play(Transform(pre_mrna, mature_mrna), ReplacementTransform(cap_pre, cap_mrna), run_time=1.2)

        ribo = make_ribosome().scale(0.8).move_to(mature_mrna.get_left()+RIGHT*0.5+UP*0.2)
        cap_tr = label_with_bg("翻译：核糖体沿 mRNA → 多肽链", scale=0.5).next_to(ribo, UP, buff=0.15)
        self.play(FadeIn(ribo), FadeIn(cap_tr), run_time=0.8)
        peptide = VGroup()
        for i in range(12):
            self.play(ribo.animate.shift(RIGHT*0.45), run_time=0.35, rate_func=linear)
            aa = Dot(color=PRO_COLOR, radius=0.06).move_to(ribo.get_bottom()+DOWN*0.18+RIGHT*0.12*i)
            peptide.add(aa)
            self.add(aa)
        cap_pep = label_with_bg("多肽链形成与折叠", color=PRO_COLOR, scale=0.5).next_to(peptide, DOWN, buff=0.2)
        self.play(FadeIn(cap_pep), run_time=0.6)
        self.wait(1.6)

        self.play(FadeOut(gene), FadeOut(pol_arrow), FadeOut(pol_label), FadeOut(splice_brace),
                  FadeOut(splice_txt), FadeOut(cap_gene), FadeOut(cap_tr), FadeOut(cap_pep),
                  FadeOut(pre_mrna), FadeOut(cap_mrna), FadeOut(ribo), FadeOut(peptide), run_time=0.8)

        # ---------- HIV 生命历程（独立舞台） ----------
        cap_hiv = label_with_bg("HIV 生命历程（逆转录病毒）", color=VIRUS_PURPLE, scale=0.6).move_to(stage.get_top()+DOWN*0.4)
        self.play(FadeIn(cap_hiv), run_time=0.6)

        cell = make_cell().scale(0.72).move_to(stage.get_center()+LEFT*2.6+DOWN*0.5)
        hiv = make_hiv_virion(scale=0.95, cone_core=False).move_to(stage.get_center()+RIGHT*3.4+UP*1.8)
        self.play(FadeIn(cell), FadeIn(hiv), run_time=0.8)

        bullet_box = RoundedRectangle(width=4.4, height=4.8, corner_radius=0.2)\
            .set_fill("#131933", opacity=0.9).set_stroke("#334", width=2).move_to(stage.get_center()+RIGHT*3.4+DOWN*0.2)
        steps = VGroup(
            CText("1. 粘附/进入：识别 CD4 与 CCR5/CXCR4").scale(0.48),
            CText("2. 逆转录：RNA → DNA（逆转录酶）").scale(0.48),
            CText("3. 整合：前病毒 DNA 融入宿主基因组").scale(0.48),
            CText("4. 转录/翻译/加工：多聚蛋白 → 蛋白酶切割").scale(0.48),
            CText("5. 装配/出芽/成熟：锥形核心形成").scale(0.48),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.28).move_to(bullet_box.get_center())
        steps.set_z_index(10)
        self.play(FadeIn(bullet_box), LaggedStart(*[FadeIn(s, shift=RIGHT*0.1) for s in steps], lag_ratio=0.12), run_time=1.2)

        # 1. 进入
        tag1 = label_with_bg("粘附与融合", scale=0.5).move_to(cell.get_top()+UP*0.1)
        self.play(FadeIn(tag1), hiv.animate.move_to(cell[0].point_at_angle(PI/4)), run_time=1.2)
        self.wait(0.6)
        # 2. 核心释放 + 逆转录
        tag2 = label_with_bg("衣壳解包 → 核心释放", scale=0.5).next_to(tag1, DOWN, buff=0.15)
        capsid = make_capsid_cone(scale=0.55).move_to(cell.get_center()+RIGHT*0.4)
        self.play(ReplacementTransform(tag1, tag2), FadeIn(capsid, shift=DOWN*0.2), run_time=0.8)
        rt_eq = MathTex(r"\text{RNA} \rightarrow \text{DNA}", color=YELLOW_B).scale(0.9).move_to(cell.get_center()+RIGHT*0.4)
        self.play(FadeIn(rt_eq), run_time=0.6)
        self.wait(0.6)
        # 3. 整合
        tag3 = label_with_bg("核内转运与整合", scale=0.5).move_to(tag2.get_center())
        self.play(ReplacementTransform(tag2, tag3), rt_eq.animate.move_to(cell[1].get_center()), run_time=0.8)
        self.wait(0.4)
        # 4. 转录/翻译
        mline = Line(cell[1].get_left()+RIGHT*0.2, cell[1].get_right()+LEFT*0.2, color=RNA_COLOR, stroke_width=5)
        poly = Rectangle(width=1.8, height=0.5).set_fill(PRO_COLOR, opacity=0.7).set_stroke(PRO_COLOR, width=2)\
            .move_to(cell.get_center()+RIGHT*2.1)
        tag4 = label_with_bg("转录/翻译/蛋白酶加工", scale=0.5).move_to(tag3.get_center())
        self.play(ReplacementTransform(tag3, tag4), Create(mline), FadeIn(poly), run_time=0.9)
        self.wait(0.4)
        # 5. 装配/出芽
        new_virion = make_hiv_virion(scale=0.75, cone_core=True).move_to(cell[0].point_at_angle(-PI/6))
        tag5 = label_with_bg("装配/出芽/成熟（锥形核心）", scale=0.5).move_to(tag4.get_center())
        self.play(ReplacementTransform(tag4, tag5), FadeIn(new_virion, shift=OUT*0.1), run_time=0.9)
        self.play(new_virion.animate.move_to(stage.get_center()+RIGHT*5.2+UP*0.3), run_time=1.0)
        self.wait(1.2)

        self.play(FadeOut(tag5), FadeOut(capsid), FadeOut(rt_eq), FadeOut(mline), FadeOut(poly),
                  FadeOut(new_virion), FadeOut(hiv), FadeOut(cell), FadeOut(bullet_box), FadeOut(steps), run_time=0.9)

        # ---------- TMV 生命历程（独立舞台） ----------
        cap_tmv = label_with_bg("烟草花叶病毒（TMV）生命历程", color=PLANT_GREEN, scale=0.6).move_to(stage.get_top()+DOWN*0.4)
        self.play(FadeIn(cap_tmv), run_time=0.6)

        plant_cell = RoundedRectangle(width=8.8, height=5.0, corner_radius=0.25).set_stroke(PLANT_GREEN, width=6)\
            .set_fill(PLANT_GREEN, opacity=0.05).move_to(stage.get_center()+LEFT*2.0)
        nuc = Circle(radius=0.9).set_stroke(BLUE_E, width=4).set_fill(BLUE_E, opacity=0.1)\
            .move_to(plant_cell.get_center()+LEFT*1.2+UP*0.4)
        self.play(FadeIn(plant_cell), FadeIn(nuc), run_time=0.8)

        tmv_in = make_tmv(scale=1.0).move_to(stage.get_center()+RIGHT*4.0+UP*1.5)
        self.play(FadeIn(tmv_in), tmv_in.animate.move_to(plant_cell.get_right()+LEFT*0.6+UP*0.8), run_time=1.0)

        tag_i = label_with_bg("伤口进入/解离，释放 RNA", scale=0.5).move_to(plant_cell.get_top()+DOWN*0.2)
        self.play(FadeIn(tag_i), run_time=0.6)

        rd_tag = label_with_bg("翻译复制酶（RdRP）→ 复制基因组 RNA", scale=0.5).next_to(tag_i, DOWN, buff=0.15)
        rd_icon = RegularPolygon(n=6).set_stroke(RNA_COLOR, width=3).set_fill(RNA_COLOR, opacity=0.2)\
            .scale(0.55).move_to(plant_cell.get_center()+RIGHT*1.2)
        tmpl = Line(LEFT*1.4, RIGHT*1.4, color=RNA_COLOR, stroke_width=5).move_to(plant_cell.get_center()+RIGHT*1.2+DOWN*0.6)
        self.play(ReplacementTransform(tag_i, rd_tag), FadeIn(rd_icon), Create(tmpl), run_time=1.0)

        sg_tag = label_with_bg("次基因组 RNA → 运动蛋白/外壳蛋白", scale=0.5).move_to(rd_tag.get_center())
        sg1 = Line(LEFT*1.0, RIGHT*1.0, color=RNA_COLOR, stroke_width=4).move_to(plant_cell.get_center()+LEFT*0.4+DOWN*0.9)
        sg2 = Line(LEFT*0.8, RIGHT*0.8, color=RNA_COLOR, stroke_width=4).move_to(plant_cell.get_center()+RIGHT*0.4+DOWN*1.2)
        self.play(ReplacementTransform(rd_tag, sg_tag), Create(sg1), Create(sg2), run_time=1.0)

        asm_tag = label_with_bg("螺旋对称装配：衣壳亚基沿 RNA 组装", scale=0.5).move_to(sg_tag.get_center())
        helix = build_tmv_helical_units(length=3.6, pitch=0.28, amp=0.16, density=28,
                                        center=plant_cell.get_center()+LEFT*0.2)
        rna_axis, units = helix[0], helix[1]
        self.play(ReplacementTransform(sg_tag, asm_tag), Create(rna_axis), run_time=0.9)
        self.play(LaggedStart(*[FadeIn(u, scale=0.7) for u in units], lag_ratio=0.02), run_time=2.8)
        envelope = RoundedRectangle(corner_radius=0.15, width=4.0, height=0.5).set_stroke(PLANT_GREEN, width=4)\
            .set_fill(PLANT_GREEN, opacity=0.12).move_to(helix.get_center())
        self.play(FadeIn(envelope), run_time=0.6)
        self.wait(1.2)

        self.play(FadeOut(asm_tag), FadeOut(envelope), FadeOut(rna_axis), FadeOut(units),
                  FadeOut(sg1), FadeOut(sg2), FadeOut(rd_icon), FadeOut(tmpl), FadeOut(plant_cell), FadeOut(nuc), FadeOut(tmv_in),
                  FadeOut(cap_tmv), run_time=0.9)

        # ---------- 总结信息流差异 ----------
        sum_card = make_card(
            "小结：不同生物的信息传递路径",
            ["细胞：DNA → RNA → 蛋白质（中心法则）",
             "逆转录病毒：RNA → DNA（逆转录）→ RNA → 蛋白质",
             "多数 RNA 病毒：RNA → RNA（RdRP）→ 蛋白质"],
            color=MAIN_COLOR
        )
        sum_card.move_to(stage.get_center())
        self.play(FadeIn(sum_card, shift=UP*0.1), run_time=0.8)
        self.wait(2.5)
        self.play(FadeOut(sum_card), run_time=0.6)

        # ---------- 抗菌机制（章节卡片风格） ----------
        ab_section = section_card("章节：抗菌机制", "青霉素 / 红霉素 / 利福平（细菌特有靶点）")
        self.play(ReplacementTransform(cap_hiv, ab_section), run_time=0.8)
        self.wait(1.2)
        self.play(FadeOut(ab_section), run_time=0.6)

        # 舞台左：演示；右：卡片
        demo_box = RoundedRectangle(width=7.2, height=5.0, corner_radius=0.2)\
            .set_stroke("#445", width=2).set_fill("#141935", opacity=0.95).move_to(stage.get_left()+RIGHT*4.1)
        self.play(FadeIn(demo_box), run_time=0.5)

        # 卡片 1：青霉素
        card1 = make_card(
            "青霉素：β-内酰胺抑制转肽酶（PBP）",
            ["抑制肽聚糖交联 → 细胞壁缺陷",
             "渗透压失衡 → 易裂解",
             "对革兰阳性更敏感（总体趋势）"],
            color="#FFB000"
        ).move_to(stage.get_right()+LEFT*3.2)
        self.play(FadeIn(card1, shift=UP*0.1), run_time=0.7)

        # 网格演示
        pg_origin = demo_box.get_center()+LEFT*1.5+UP*0.6
        mesh, crosslinks = make_pg_mesh(rows=5, cols=12, origin=pg_origin)
        bonds, sugars = mesh[0], mesh[1]
        self.play(Create(bonds), FadeIn(sugars, lag_ratio=0.03), run_time=1.4)
        self.play(LaggedStart(*[Create(cl[0]) for cl in crosslinks], lag_ratio=0.06), run_time=1.0)
        self.play(LaggedStart(*[Create(cl[1]) for cl in crosslinks], lag_ratio=0.06), run_time=1.0)

        pbps = VGroup()
        pens = VGroup()
        for i, cl in enumerate(crosslinks[:8]):
            anchor = cl.get_center()
            pbp = RegularPolygon(n=8).scale(0.15).set_fill(WHITE, opacity=1.0).set_stroke(YELLOW, width=3).move_to(anchor + 0.18*UP)
            ring = Square(side_length=0.20).set_stroke(RED, width=3).set_fill(RED, opacity=0.2).rotate(PI/4).move_to(anchor + 0.45*UP + 0.15*RIGHT)
            pbps.add(pbp); pens.add(ring)
        self.play(LaggedStart(*[FadeIn(p) for p in pbps], lag_ratio=0.08), run_time=0.8)
        self.play(LaggedStart(*[FadeIn(x) for x in pens], lag_ratio=0.08), run_time=0.8)

        dashed = VGroup(*[VGroup(
            DashedLine(cl[0].get_start(), cl[0].get_end(), dash_length=0.06, color=YELLOW),
            DashedLine(cl[1].get_start(), cl[1].get_end(), dash_length=0.06, color=YELLOW)
        ) for cl in crosslinks])
        self.play(ReplacementTransform(crosslinks, dashed), run_time=0.8)

        cracks = VGroup(*[
            DashedLine(pg_origin+RIGHT*(1.0+i*0.8)+UP*(0.3-j*0.45),
                       pg_origin+RIGHT*(1.0+i*0.8)+DOWN*(0.4-j*0.45),
                       color=RED, dash_length=0.08)
            for i in range(6) for j in range(5)
        ])
        self.play(LaggedStart(*[Create(c) for c in cracks], lag_ratio=0.03), run_time=1.0)
        self.wait(1.6)

        # 卡片 2：红霉素
        card2 = make_card(
            "红霉素：结合 50S 亚基，阻断转位",
            ["阻断肽链转位 → 翻译停滞",
             "主要作用于革兰阳性与非典型细菌",
             "药代：组织穿透强，常用于上呼吸道感染"],
            color="#E64A19"
        ).move_to(card1.get_center())
        self.play(ReplacementTransform(card1, card2), FadeOut(mesh), FadeOut(dashed), FadeOut(cracks), FadeOut(pbps), FadeOut(pens), run_time=0.9)

        ribo = make_ribosome().scale(0.9).move_to(demo_box.get_center()+LEFT*0.6+UP*0.2)
        mrna = Line(LEFT*2.0, RIGHT*2.0, color=RNA_COLOR, stroke_width=5).move_to(ribo.get_center()+DOWN*0.35)
        self.play(FadeIn(ribo), Create(mrna), run_time=0.8)
        aa_chain = VGroup()
        for i in range(6):
            aa = Dot(color=PRO_COLOR, radius=0.07).move_to(ribo.get_center()+DOWN*0.9+RIGHT*0.18*i)
            aa_chain.add(aa)
            self.add(aa)
            self.play(ribo.animate.shift(RIGHT*0.15), run_time=0.22, rate_func=linear)
        block = Cross(ribo, stroke_color=RED, stroke_width=8).scale(1.1)
        self.play(Create(block), run_time=0.6)
        self.wait(1.2)

        # 卡片 3：利福平
        card3 = make_card(
            "利福平：结合 RNAP β 亚基，抑制转录起始",
            ["拮抗细菌 RNA 聚合酶 → 无法启动转录",
             "抗结核治疗基石药之一",
             "易诱导肝酶，注意药物相互作用"],
            color="#5D6D7E"
        ).move_to(card2.get_center())
        self.play(ReplacementTransform(card2, card3), FadeOut(ribo), FadeOut(mrna), FadeOut(block), FadeOut(aa_chain), run_time=0.8)

        rnapii = MathTex(r"\text{RNAP}_{\beta}", color=YELLOW_A).scale(1.0).move_to(demo_box.get_center()+UP*0.8)
        dna = Line(LEFT*2.2, RIGHT*2.2, color=DNA_COLOR, stroke_width=5).move_to(demo_box.get_center()+DOWN*0.1)
        self.play(FadeIn(rnapii), Create(dna), run_time=0.8)
        stop_mark = Cross(rnapii, stroke_color=RED, stroke_width=8).scale(1.2)
        self.play(Create(stop_mark), run_time=0.6)
        self.wait(1.6)

        ab_sum = make_card(
            "小结：三类抗菌机制",
            ["青霉素：细胞壁（PBP/交联）",
             "红霉素：蛋白质合成（50S 转位）",
             "利福平：转录（RNAP β 起始）",
             "以上为细菌靶点，区别于抗病毒策略"],
            color=ACCENT
        ).move_to(card3.get_center())
        self.play(ReplacementTransform(card3, ab_sum), FadeOut(rnapii), FadeOut(dna), FadeOut(stop_mark), run_time=0.8)
        self.wait(2.2)

        # ---------- 3D 补充 ----------
        self.play(FadeOut(ab_sum), FadeOut(demo_box), FadeOut(stage), FadeOut(title), FadeOut(dogma), run_time=0.9)

        title3d = CText("三维中心法则演示：DNA → RNA → 蛋白质", color=WHITE).scale(0.7).to_edge(UP)
        self.add_fixed_in_frame_mobjects(title3d)
        self.play(FadeIn(title3d), run_time=0.6)

        def helix(a=1.0, b=0.18, turns=3, phase=0):
            return ParametricFunction(
                lambda t: np.array([a*np.cos(t+phase), a*np.sin(t+phase), b*t]),
                t_range=[0, turns*TAU],
                color=DNA_COLOR
            )
        left = helix(a=1.0, b=0.18, turns=3, phase=0)
        right = helix(a=1.0, b=0.18, turns=3, phase=PI)
        ladders = VGroup()
        for t in np.linspace(0, 3*TAU, 28):
            p1 = np.array([np.cos(t), np.sin(t), 0.18*t])
            p2 = np.array([np.cos(t+PI), np.sin(t+PI), 0.18*t])
            ladders.add(Line(p1, p2, color=GREY_B, stroke_width=2))
        dna3d = VGroup(left, right, ladders).scale(1.1)

        self.set_camera_orientation(phi=75*DEGREES, theta=-45*DEGREES, zoom=1.0)
        self.play(Create(dna3d), run_time=2.0)

        pol = Sphere(radius=0.12, color=YELLOW).move_to(left.points[0])
        self.play(FadeIn(pol), run_time=0.6)

        mRNA_path = VMobject(color=RNA_COLOR)
        mRNA_path.set_points_as_corners([left.points[0], left.points[0]])

        def update_path(mob, alpha):
            idx = int(alpha * (len(left.points)-1))
            idx = np.clip(idx, 0, len(left.points)-1)
            p = left.points[idx]
            new_end = np.array([0.0, 0.0, p[2]]) + RIGHT*2.6
            mob.set_points_as_corners([left.points[0], new_end])
            pol.move_to(p)

        self.play(UpdateFromAlphaFunc(mRNA_path, update_path), run_time=5.5, rate_func=linear)
        self.add(mRNA_path)
        self.wait(0.4)

        ribo2d = make_ribosome().scale(0.5)
        ribo_3d = always_redraw(lambda: VGroup(*[m.copy() for m in ribo2d]).move_to(mRNA_path.get_end()))
        self.play(FadeIn(ribo_3d), run_time=0.6)

        peptide3d = VGroup()
        for i in range(14):
            self.play(ribo_3d.animate.shift(RIGHT*0.24), run_time=0.35, rate_func=linear)
            bead = Sphere(radius=0.06, color=PRO_COLOR).move_to(mRNA_path.get_end()+DOWN*0.15+RIGHT*0.1*i)
            peptide3d.add(bead)
            self.add(bead)
        self.wait(1.2)

        self.play(Rotate(dna3d, angle=TAU/3, axis=OUT), run_time=2.5)
        self.move_camera(phi=70*DEGREES, theta=20*DEGREES, run_time=2.0)
        self.wait(1.6)

        outro = CText("不同生物可偏离“经典流程”（逆转录、RNA 复制）", color=YELLOW_A).scale(0.55).to_edge(DOWN)
        self.add_fixed_in_frame_mobjects(outro)
        self.play(FadeIn(outro), run_time=0.6)
        self.wait(2.0)

        thanks = CText("感谢观看｜如遇 API 差异，请参考 ManimCE 0.19 文档适配", color=GREY_B).scale(0.55)
        self.add_fixed_in_frame_mobjects(thanks)
        self.play(FadeIn(thanks, shift=UP*0.1), run_time=0.6)
        self.wait(2.0)