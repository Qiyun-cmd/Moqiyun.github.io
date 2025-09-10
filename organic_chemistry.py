# -*- coding: utf-8 -*-
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from my_manim_setup import *


from manim import *
import numpy as np
from manim.utils.space_ops import rotate_vector  # 添加这个导入用于旋转向量

class OrganicChemistryBeauty(Scene):
    def construct(self):
        # 标题动画
        title = Text("有机化合物结构式之美", font="STSong", font_size=56)
        subtitle = Text("探索分子世界的奇妙结构", font="STSong", font_size=32)
        subtitle.next_to(title, DOWN)
        
        self.play(Write(title))
        self.play(FadeIn(subtitle))
        self.wait(2)
        self.play(FadeOut(title), FadeOut(subtitle))
        
        # 1. 重要的烃
        self.show_hydrocarbons()
        
        # 2. 同系物
        self.show_homologous_series()
        
        # 3. 同分异构体
        self.show_isomers()
        
        # 4. 石油裂解和裂化
        self.show_petroleum_cracking()
        
        # 5. 合成材料生产
        self.show_synthetic_materials()
        
        # 6. 乙醇和乙酸
        self.show_ethanol_acetic_acid()
        
        # 7. 乙酸乙酯
        self.show_ethyl_acetate()
        
        # 8. 官能团
        self.show_functional_groups()
        
        # 9. 乙炔制备
        self.show_acetylene_preparation()
        
        # 10. 芳香烃
        self.show_aromatic_hydrocarbons()
        
        # 11. 醛酮羧酸酯
        self.show_carbonyl_compounds()
        
        # 12. 综合流程图
        self.show_synthesis_flowchart()
    
    def show_hydrocarbons(self):
        title = Text("重要的烃", font="STSong", font_size=48)
        title.to_edge(UP)
        self.play(Write(title))
        
        # 甲烷
        methane_struct = self.create_methane_structure()
        methane_label = Text("甲烷", font="STSong", font_size=24)
        methane_formula = MathTex("CH_4")
        methane_electron = self.create_electron_formula("CH4")
        
        methane_group = VGroup(methane_struct, methane_label, methane_formula, methane_electron)
        methane_group.arrange(DOWN, buff=0.3)
        methane_group.shift(LEFT * 4)
        
        # 乙烯
        ethene_struct = self.create_ethene_structure()
        ethene_label = Text("乙烯", font="STSong", font_size=24)
        ethene_formula = MathTex("C_2H_4")
        ethene_electron = self.create_electron_formula("C2H4")
        
        ethene_group = VGroup(ethene_struct, ethene_label, ethene_formula, ethene_electron)
        ethene_group.arrange(DOWN, buff=0.3)
        
        # 乙炔
        ethyne_struct = self.create_ethyne_structure()
        ethyne_label = Text("乙炔", font="STSong", font_size=24)
        ethyne_formula = MathTex("C_2H_2")
        ethyne_electron = self.create_electron_formula("C2H2")
        
        ethyne_group = VGroup(ethyne_struct, ethyne_label, ethyne_formula, ethyne_electron)
        ethyne_group.arrange(DOWN, buff=0.3)
        ethyne_group.shift(RIGHT * 4)
        
        self.play(
            FadeIn(methane_group),
            FadeIn(ethene_group),
            FadeIn(ethyne_group)
        )
        self.wait(3)
        
        # 化学性质展示
        reaction1 = MathTex("CH_4 + 2O_2 \\rightarrow CO_2 + 2H_2O")
        reaction1.next_to(methane_group, DOWN, buff=0.5)
        
        self.play(Write(reaction1))
        self.wait(2)
        
        self.play(FadeOut(VGroup(title, methane_group, ethene_group, ethyne_group, reaction1)))
    
    def create_methane_structure(self):
        # 创建甲烷的结构式
        c = Circle(radius=0.3, color=BLACK, fill_opacity=1)
        c_text = Text("C", font_size=20, color=WHITE)
        carbon = VGroup(c, c_text)
        
        h_positions = [UP, DOWN, LEFT, RIGHT]
        hydrogens = VGroup()
        bonds = VGroup()
        
        for pos in h_positions:
            h = Circle(radius=0.2, color=GRAY, fill_opacity=1)
            h_text = Text("H", font_size=16, color=WHITE)
            h_atom = VGroup(h, h_text)
            h_atom.move_to(carbon.get_center() + pos * 0.8)
            hydrogens.add(h_atom)
            
            bond = Line(carbon.get_center(), h_atom.get_center(), color=BLACK)
            bonds.add(bond)
        
        return VGroup(bonds, carbon, hydrogens)
    
    def create_ethene_structure(self):
        # 创建乙烯的结构式
        c1 = Circle(radius=0.3, color=BLACK, fill_opacity=1)
        c1_text = Text("C", font_size=20, color=WHITE)
        carbon1 = VGroup(c1, c1_text)
        carbon1.shift(LEFT * 0.5)
        
        c2 = Circle(radius=0.3, color=BLACK, fill_opacity=1)
        c2_text = Text("C", font_size=20, color=WHITE)
        carbon2 = VGroup(c2, c2_text)
        carbon2.shift(RIGHT * 0.5)
        
        # 双键
        bond1 = Line(carbon1.get_center() + UP * 0.1, carbon2.get_center() + UP * 0.1, color=BLACK)
        bond2 = Line(carbon1.get_center() + DOWN * 0.1, carbon2.get_center() + DOWN * 0.1, color=BLACK)
        
        # 氢原子
        h_positions = [
            (carbon1, LEFT + UP * 0.5),
            (carbon1, LEFT + DOWN * 0.5),
            (carbon2, RIGHT + UP * 0.5),
            (carbon2, RIGHT + DOWN * 0.5)
        ]
        
        hydrogens = VGroup()
        h_bonds = VGroup()
        
        for carbon, direction in h_positions:
            h = Circle(radius=0.2, color=GRAY, fill_opacity=1)
            h_text = Text("H", font_size=16, color=WHITE)
            h_atom = VGroup(h, h_text)
            h_atom.move_to(carbon.get_center() + direction * 0.6)
            hydrogens.add(h_atom)
            
            bond = Line(carbon.get_center(), h_atom.get_center(), color=BLACK)
            h_bonds.add(bond)
        
        return VGroup(bond1, bond2, h_bonds, carbon1, carbon2, hydrogens)
    
    def create_ethyne_structure(self):
        # 创建乙炔的结构式
        c1 = Circle(radius=0.3, color=BLACK, fill_opacity=1)
        c1_text = Text("C", font_size=20, color=WHITE)
        carbon1 = VGroup(c1, c1_text)
        carbon1.shift(LEFT * 0.5)
        
        c2 = Circle(radius=0.3, color=BLACK, fill_opacity=1)
        c2_text = Text("C", font_size=20, color=WHITE)
        carbon2 = VGroup(c2, c2_text)
        carbon2.shift(RIGHT * 0.5)
        
        # 三键
        bond1 = Line(carbon1.get_center(), carbon2.get_center(), color=BLACK)
        bond2 = Line(carbon1.get_center() + UP * 0.15, carbon2.get_center() + UP * 0.15, color=BLACK)
        bond3 = Line(carbon1.get_center() + DOWN * 0.15, carbon2.get_center() + DOWN * 0.15, color=BLACK)
        
        # 氢原子
        h1 = Circle(radius=0.2, color=GRAY, fill_opacity=1)
        h1_text = Text("H", font_size=16, color=WHITE)
        h_atom1 = VGroup(h1, h1_text)
        h_atom1.move_to(carbon1.get_center() + LEFT * 0.8)
        
        h2 = Circle(radius=0.2, color=GRAY, fill_opacity=1)
        h2_text = Text("H", font_size=16, color=WHITE)
        h_atom2 = VGroup(h2, h2_text)
        h_atom2.move_to(carbon2.get_center() + RIGHT * 0.8)
        
        h_bond1 = Line(carbon1.get_center(), h_atom1.get_center(), color=BLACK)
        h_bond2 = Line(carbon2.get_center(), h_atom2.get_center(), color=BLACK)
        
        return VGroup(bond1, bond2, bond3, h_bond1, h_bond2, carbon1, carbon2, h_atom1, h_atom2)
    
    def create_electron_formula(self, compound):
        # 创建电子式
        if compound == "CH4":
            formula = MathTex("H:C:H", "\\quad", "H:C:H")
            formula.scale(0.8)
        elif compound == "C2H4":
            formula = MathTex("H:C::C:H", "\\quad", "H\\quad H")
            formula.scale(0.8)
        elif compound == "C2H2":
            formula = MathTex("H:C:::C:H")
            formula.scale(0.8)
        else:
            formula = MathTex("")
        
        return formula
    
    def show_homologous_series(self):
        title = Text("烷烃同系物", font="STSong", font_size=48)
        title.to_edge(UP)
        self.play(Write(title))
        
        # 创建同系物表格
        alkanes = [
            ("甲烷", "CH_4", "C_nH_{2n+2}, n=1"),
            ("乙烷", "C_2H_6", "C_nH_{2n+2}, n=2"),
            ("丙烷", "C_3H_8", "C_nH_{2n+2}, n=3"),
            ("丁烷", "C_4H_{10}", "C_nH_{2n+2}, n=4")
        ]
        
        table = VGroup()
        for i, (name, formula, general) in enumerate(alkanes):
            name_text = Text(name, font="STSong", font_size=24)
            formula_tex = MathTex(formula)
            general_tex = MathTex(general)
            
            row = VGroup(name_text, formula_tex, general_tex)
            row.arrange(RIGHT, buff=1)
            row.shift(DOWN * i * 0.8)
            table.add(row)
        
        table.center()
        
        self.play(Create(table))
        self.wait(2)
        
        # 展示通式
        general_formula = MathTex("C_nH_{2n+2}", font_size=48)
        general_formula.next_to(table, DOWN, buff=0.5)
        general_formula.set_color(YELLOW)
        
        self.play(Write(general_formula))
        self.wait(2)
        
        self.play(FadeOut(VGroup(title, table, general_formula)))
    
    def show_isomers(self):
        title = Text("同分异构体", font="STSong", font_size=48)
        title.to_edge(UP)
        self.play(Write(title))
        
        # C4H10的两种异构体
        subtitle = MathTex("C_4H_{10}", font_size=36)
        subtitle.next_to(title, DOWN)
        self.play(Write(subtitle))
        
        # 正丁烷
        n_butane = self.create_n_butane()
        n_butane_label = Text("正丁烷", font="STSong", font_size=24)
        n_butane_label.next_to(n_butane, DOWN)
        n_butane_group = VGroup(n_butane, n_butane_label)
        n_butane_group.shift(LEFT * 3)
        
        # 异丁烷
        iso_butane = self.create_iso_butane()
        iso_butane_label = Text("异丁烷", font="STSong", font_size=24)
        iso_butane_label.next_to(iso_butane, DOWN)
        iso_butane_group = VGroup(iso_butane, iso_butane_label)
        iso_butane_group.shift(RIGHT * 3)
        
        self.play(
            Create(n_butane_group),
            Create(iso_butane_group)
        )
        self.wait(3)
        
        # 性质对比
        properties = Text("沸点：正丁烷 -0.5°C，异丁烷 -11.7°C", font="STSong", font_size=20)
        properties.next_to(subtitle, DOWN, buff=3)
        self.play(Write(properties))
        self.wait(2)
        
        self.play(FadeOut(VGroup(title, subtitle, n_butane_group, iso_butane_group, properties)))
    
    def create_n_butane(self):
        # 创建正丁烷结构
        carbons = VGroup()
        bonds = VGroup()
        hydrogens = VGroup()
        
        # 碳链
        for i in range(4):
            c = Circle(radius=0.25, color=BLACK, fill_opacity=1)
            c_text = Text("C", font_size=18, color=WHITE)
            carbon = VGroup(c, c_text)
            carbon.shift(RIGHT * i * 0.8)
            carbons.add(carbon)
            
            if i < 3:
                bond = Line(carbon.get_center() + RIGHT * 0.25, 
                           carbon.get_center() + RIGHT * 0.55, color=BLACK)
                bonds.add(bond)
        
        # 添加氢原子
        h_positions = [
            (0, [LEFT, UP, DOWN]),
            (1, [UP, DOWN]),
            (2, [UP, DOWN]),
            (3, [RIGHT, UP, DOWN])
        ]
        
        for c_idx, positions in h_positions:
            for pos in positions:
                h = Circle(radius=0.15, color=GRAY, fill_opacity=1)
                h_text = Text("H", font_size=14, color=WHITE)
                h_atom = VGroup(h, h_text)
                h_atom.move_to(carbons[c_idx].get_center() + pos * 0.5)
                hydrogens.add(h_atom)
                
                bond = Line(carbons[c_idx].get_center(), h_atom.get_center(), color=BLACK)
                bonds.add(bond)
        
        return VGroup(bonds, carbons, hydrogens)
    
    def create_iso_butane(self):
        # 创建异丁烷结构
        # 中心碳
        c_center = Circle(radius=0.25, color=BLACK, fill_opacity=1)
        c_center_text = Text("C", font_size=18, color=WHITE)
        carbon_center = VGroup(c_center, c_center_text)
        
        # 三个甲基
        carbons = VGroup(carbon_center)
        bonds = VGroup()
        hydrogens = VGroup()
        
        methyl_positions = [UP, LEFT + DOWN * 0.5, RIGHT + DOWN * 0.5]
        
        for pos in methyl_positions:
            c = Circle(radius=0.25, color=BLACK, fill_opacity=1)
            c_text = Text("C", font_size=18, color=WHITE)
            carbon = VGroup(c, c_text)
            carbon.move_to(carbon_center.get_center() + pos * 0.8)
            carbons.add(carbon)
            
            bond = Line(carbon_center.get_center(), carbon.get_center(), color=BLACK)
            bonds.add(bond)
            
            # 每个甲基的氢
            # 使用rotate_vector而不是pos.rotate
            for h_pos in [rotate_vector(pos, PI/3), rotate_vector(pos, -PI/3), pos]:
                if np.all(h_pos != -pos):  # 避免与中心碳重叠
                    h = Circle(radius=0.15, color=GRAY, fill_opacity=1)
                    h_text = Text("H", font_size=14, color=WHITE)
                    h_atom = VGroup(h, h_text)
                    h_atom.move_to(carbon.get_center() + h_pos * 0.4)
                    hydrogens.add(h_atom)
                    
                    h_bond = Line(carbon.get_center(), h_atom.get_center(), color=BLACK)
                    bonds.add(h_bond)
        
        # 中心碳的氢
        h = Circle(radius=0.15, color=GRAY, fill_opacity=1)
        h_text = Text("H", font_size=14, color=WHITE)
        h_atom = VGroup(h, h_text)
        h_atom.move_to(carbon_center.get_center() + DOWN * 0.5)
        hydrogens.add(h_atom)
        
        h_bond = Line(carbon_center.get_center(), h_atom.get_center(), color=BLACK)
        bonds.add(h_bond)
        
        return VGroup(bonds, carbons, hydrogens)
    
    def show_petroleum_cracking(self):
        title = Text("石油裂解与裂化", font="STSong", font_size=48)
        title.to_edge(UP)
        self.play(Write(title))
        
        # 裂解过程
        cracking_title = Text("裂解：高温分解", font="STSong", font_size=32)
        cracking_title.next_to(title, DOWN)
        self.play(Write(cracking_title))
        
        # 裂解反应
        reaction1 = MathTex("C_{16}H_{34} \\xrightarrow{800^{\\circ}C} C_8H_{18} + C_8H_{16}")
        reaction1.shift(UP)
        
        # 修复：分离中文部分
        reaction2_left = MathTex("C_8H_{18}")
        arrow2 = MathTex("\\xrightarrow{}")
        condition2 = Text("高温", font="STSong", font_size=16)
        reaction2_right = MathTex("C_4H_{10} + C_4H_8")
        reaction2 = VGroup(reaction2_left, arrow2, condition2, reaction2_right).arrange(RIGHT, buff=0.1)
        
        # 修复：分离中文部分
        reaction3_left = MathTex("C_4H_{10}")
        arrow3 = MathTex("\\xrightarrow{}")
        condition3 = Text("高温", font="STSong", font_size=16)
        reaction3_right = MathTex("C_2H_6 + C_2H_4")
        reaction3 = VGroup(reaction3_left, arrow3, condition3, reaction3_right).arrange(RIGHT, buff=0.1)
        reaction3.shift(DOWN)
        
        self.play(Write(reaction1))
        self.wait(1)
        self.play(Write(reaction2))
        self.wait(1)
        self.play(Write(reaction3))
        self.wait(2)
        
        self.play(FadeOut(VGroup(reaction1, reaction2, reaction3)))
        
        # 裂化过程
        catalytic_title = Text("催化裂化：催化剂作用", font="STSong", font_size=32)
        catalytic_title.next_to(title, DOWN)
        self.play(Transform(cracking_title, catalytic_title))
        
        # 催化裂化反应 - 修复：分离中文部分
        cat_reaction_left = MathTex("C_{16}H_{34}")
        arrow_cat = MathTex("\\xrightarrow{500^{\\circ}C}_{}")
        catalyst_text = Text("Al₂O₃", font="STSong", font_size=16)
        cat_reaction_right = MathTex("C_8H_{18} + C_4H_{10} + C_4H_8")
        cat_reaction = VGroup(cat_reaction_left, arrow_cat, catalyst_text, cat_reaction_right).arrange(RIGHT, buff=0.1)
        cat_reaction.shift(UP * 0.5)
        
        # 催化剂示意图
        catalyst = self.create_catalyst_diagram()
        catalyst.next_to(cat_reaction, DOWN, buff=0.5)
        
        self.play(Write(cat_reaction))
        self.play(Create(catalyst))
        self.wait(3)
        
        self.play(FadeOut(VGroup(title, cracking_title, cat_reaction, catalyst)))
    
    def create_catalyst_diagram(self):
        # 创建催化剂示意图
        catalyst_surface = Rectangle(width=4, height=0.3, color=GRAY, fill_opacity=0.8)
        catalyst_label = Text("催化剂表面", font="STSong", font_size=16)
        catalyst_label.next_to(catalyst_surface, DOWN)
        
        # 反应物分子
        reactant = Circle(radius=0.3, color=BLUE, fill_opacity=0.7)
        reactant_label = Text("大分子", font="STSong", font_size=14)
        reactant_label.move_to(reactant.get_center())
        reactant_group = VGroup(reactant, reactant_label)
        reactant_group.next_to(catalyst_surface, UP, buff=0.5)
        
        # 产物分子
        products = VGroup()
        for i in range(3):
            product = Circle(radius=0.15, color=GREEN, fill_opacity=0.7)
            product_label = Text("小", font="STSong", font_size=10)
            product_label.move_to(product.get_center())
            product_group = VGroup(product, product_label)
            product_group.shift(RIGHT * (i - 1) * 0.8)
            products.add(product_group)
        
        products.next_to(catalyst_surface, DOWN, buff=1)
        
        # 箭头
        arrow = Arrow(reactant_group.get_bottom(), products.get_top(), color=YELLOW)
        
        return VGroup(catalyst_surface, catalyst_label, reactant_group, arrow, products)
    
    def show_synthetic_materials(self):
        title = Text("合成材料生产", font="STSong", font_size=48)
        title.to_edge(UP)
        self.play(Write(title))
        
        # 三大原料
        sources = VGroup()
        source_names = ["煤", "石油", "天然气"]
        source_colors = [BLACK, GREEN, BLUE]
        
        for i, (name, color) in enumerate(zip(source_names, source_colors)):
            source = Circle(radius=0.5, color=color, fill_opacity=0.8)
            label = Text(name, font="STSong", font_size=24, color=WHITE)
            label.move_to(source.get_center())
            source_group = VGroup(source, label)
            source_group.shift(LEFT * 4 + RIGHT * i * 2)
            sources.add(source_group)
        
        self.play(Create(sources))
        
        # 中间产物
        intermediates = VGroup()
        inter_names = ["乙烯", "丙烯", "苯"]
        inter_formulas = ["C_2H_4", "C_3H_6", "C_6H_6"]
        
        for i, (name, formula) in enumerate(zip(inter_names, inter_formulas)):
            inter_box = Rectangle(width=1.5, height=0.8, color=YELLOW)
            name_text = Text(name, font="STSong", font_size=18)
            formula_text = MathTex(formula, font_size=16)
            text_group = VGroup(name_text, formula_text).arrange(DOWN, buff=0.1)
            text_group.move_to(inter_box.get_center())
            inter_group = VGroup(inter_box, text_group)
            inter_group.shift(LEFT * 2 + RIGHT * i * 2)
            intermediates.add(inter_group)
        
        self.play(Create(intermediates))
        
        # 箭头连接
        arrows1 = VGroup()
        for source in sources:
            for inter in intermediates:
                arrow = Arrow(source.get_bottom(), inter.get_top(), 
                            color=GRAY, stroke_width=2)
                arrows1.add(arrow)
        
        self.play(Create(arrows1))
        
        # 最终产品
        products = VGroup()
        product_names = ["聚乙烯", "聚丙烯", "聚苯乙烯"]
        
        for i, name in enumerate(product_names):
            product_box = Rectangle(width=2, height=1, color=GREEN, fill_opacity=0.7)
            product_text = Text(name, font="STSong", font_size=20)
            product_text.move_to(product_box.get_center())
            product_group = VGroup(product_box, product_text)
            product_group.shift(DOWN * 2.5 + LEFT * 2 + RIGHT * i * 2)
            products.add(product_group)
        
        # 修复：分离中文部分
        polymerization_left = MathTex("n(C_2H_4)")
        arrow_poly = MathTex("\\xrightarrow{}")
        catalyst_poly = Text("催化剂", font="STSong", font_size=16)
        polymerization_right = MathTex("[-CH_2-CH_2-]_n")
        polymerization = VGroup(polymerization_left, arrow_poly, catalyst_poly, polymerization_right).arrange(RIGHT, buff=0.1)
        polymerization.shift(DOWN * 1.5)
        
        self.play(Create(products), Write(polymerization))
        self.wait(3)
        
        self.play(FadeOut(VGroup(title, sources, intermediates, arrows1, products, polymerization)))
    
    def show_ethanol_acetic_acid(self):
        title = Text("乙醇与乙酸", font="STSong", font_size=48)
        title.to_edge(UP)
        self.play(Write(title))
        
        # 乙醇结构
        ethanol_struct = self.create_ethanol_structure()
        ethanol_label = Text("乙醇", font="STSong", font_size=24)
        ethanol_formula = MathTex("C_2H_5OH")
        ethanol_group = VGroup(ethanol_struct, ethanol_label, ethanol_formula)
        ethanol_group.arrange(DOWN, buff=0.3)
        ethanol_group.shift(LEFT * 3)
        
        # 乙酸结构
        acetic_acid_struct = self.create_acetic_acid_structure()
        acetic_label = Text("乙酸", font="STSong", font_size=24)
        acetic_formula = MathTex("CH_3COOH")
        acetic_group = VGroup(acetic_acid_struct, acetic_label, acetic_formula)
        acetic_group.arrange(DOWN, buff=0.3)
        acetic_group.shift(RIGHT * 3)
        
        self.play(Create(ethanol_group), Create(acetic_group))
        
        # 氧化反应
        oxidation = MathTex("C_2H_5OH + O_2 \\xrightarrow{Cu} CH_3CHO + H_2O")
        oxidation.shift(DOWN * 1.5)
        
        oxidation2 = MathTex("2CH_3CHO + O_2 \\xrightarrow{} 2CH_3COOH")
        oxidation2.next_to(oxidation, DOWN)
        
        self.play(Write(oxidation))
        self.wait(1)
        self.play(Write(oxidation2))
        self.wait(2)
        
        # 性质对比
        properties = VGroup(
            Text("乙醇：无色液体，易燃", font="STSong", font_size=18),
            Text("乙酸：无色液体，有刺激性气味", font="STSong", font_size=18)
        ).arrange(DOWN, buff=0.3)
        properties.next_to(oxidation2, DOWN, buff=0.5)
        
        self.play(Write(properties))
        self.wait(2)
        
        self.play(FadeOut(VGroup(title, ethanol_group, acetic_group, oxidation, oxidation2, properties)))
    
    def create_ethanol_structure(self):
        # 创建乙醇结构式
        c1 = Circle(radius=0.25, color=BLACK, fill_opacity=1)
        c1_text = Text("C", font_size=18, color=WHITE)
        carbon1 = VGroup(c1, c1_text)
        carbon1.shift(LEFT * 0.5)
        
        c2 = Circle(radius=0.25, color=BLACK, fill_opacity=1)
        c2_text = Text("C", font_size=18, color=WHITE)
        carbon2 = VGroup(c2, c2_text)
        carbon2.shift(RIGHT * 0.5)
        
        o = Circle(radius=0.25, color=RED, fill_opacity=1)
        o_text = Text("O", font_size=18, color=WHITE)
        oxygen = VGroup(o, o_text)
        oxygen.shift(RIGHT * 1.5)
        
        h_oh = Circle(radius=0.15, color=GRAY, fill_opacity=1)
        h_oh_text = Text("H", font_size=14, color=WHITE)
        h_hydroxyl = VGroup(h_oh, h_oh_text)
        h_hydroxyl.shift(RIGHT * 2.3)
        
        # 键
        c_c_bond = Line(carbon1.get_center(), carbon2.get_center(), color=BLACK)
        c_o_bond = Line(carbon2.get_center(), oxygen.get_center(), color=BLACK)
        o_h_bond = Line(oxygen.get_center(), h_hydroxyl.get_center(), color=BLACK)
        
        # 其他氢原子
        hydrogens = VGroup()
        h_bonds = VGroup()
        
        h_positions = [
            (carbon1, LEFT + UP * 0.3),
            (carbon1, LEFT),
            (carbon1, LEFT + DOWN * 0.3),
            (carbon2, UP),
            (carbon2, DOWN)
        ]
        
        for carbon, pos in h_positions:
            h = Circle(radius=0.15, color=GRAY, fill_opacity=1)
            h_text = Text("H", font_size=14, color=WHITE)
            h_atom = VGroup(h, h_text)
            h_atom.move_to(carbon.get_center() + pos * 0.5)
            hydrogens.add(h_atom)
            
            bond = Line(carbon.get_center(), h_atom.get_center(), color=BLACK)
            h_bonds.add(bond)
        
        return VGroup(c_c_bond, c_o_bond, o_h_bond, h_bonds, 
                     carbon1, carbon2, oxygen, h_hydroxyl, hydrogens)
    
    def create_acetic_acid_structure(self):
        # 创建乙酸结构式
        c1 = Circle(radius=0.25, color=BLACK, fill_opacity=1)
        c1_text = Text("C", font_size=18, color=WHITE)
        carbon1 = VGroup(c1, c1_text)
        carbon1.shift(LEFT * 0.8)
        
        c2 = Circle(radius=0.25, color=BLACK, fill_opacity=1)
        c2_text = Text("C", font_size=18, color=WHITE)
        carbon2 = VGroup(c2, c2_text)
        
        o1 = Circle(radius=0.25, color=RED, fill_opacity=1)
        o1_text = Text("O", font_size=18, color=WHITE)
        oxygen1 = VGroup(o1, o1_text)
        oxygen1.shift(RIGHT * 0.8 + UP * 0.5)
        
        o2 = Circle(radius=0.25, color=RED, fill_opacity=1)
        o2_text = Text("O", font_size=18, color=WHITE)
        oxygen2 = VGroup(o2, o2_text)
        oxygen2.shift(RIGHT * 0.8 + DOWN * 0.5)
        
        h_acid = Circle(radius=0.15, color=GRAY, fill_opacity=1)
        h_acid_text = Text("H", font_size=14, color=WHITE)
        h_hydroxyl = VGroup(h_acid, h_acid_text)
        h_hydroxyl.shift(RIGHT * 1.6 + DOWN * 0.5)
        
        # 键
        c_c_bond = Line(carbon1.get_center(), carbon2.get_center(), color=BLACK)
        c_o_double1 = Line(carbon2.get_center() + UP * 0.05, oxygen1.get_center() + DOWN * 0.05, color=BLACK)
        c_o_double2 = Line(carbon2.get_center() + UP * 0.15, oxygen1.get_center() + DOWN * 0.15, color=BLACK)
        c_o_single = Line(carbon2.get_center(), oxygen2.get_center(), color=BLACK)
        o_h_bond = Line(oxygen2.get_center(), h_hydroxyl.get_center(), color=BLACK)
        
        # 甲基氢原子
        hydrogens = VGroup()
        h_bonds = VGroup()
        
        h_positions = [
            LEFT + UP * 0.3,
            LEFT,
            LEFT + DOWN * 0.3
        ]
        
        for pos in h_positions:
            h = Circle(radius=0.15, color=GRAY, fill_opacity=1)
            h_text = Text("H", font_size=14, color=WHITE)
            h_atom = VGroup(h, h_text)
            h_atom.move_to(carbon1.get_center() + pos * 0.5)
            hydrogens.add(h_atom)
            
            bond = Line(carbon1.get_center(), h_atom.get_center(), color=BLACK)
            h_bonds.add(bond)
        
        return VGroup(c_c_bond, c_o_double1, c_o_double2, c_o_single, o_h_bond, h_bonds,
                     carbon1, carbon2, oxygen1, oxygen2, h_hydroxyl, hydrogens)
    
    def show_ethyl_acetate(self):
        title = Text("乙酸乙酯的制备与水解", font="STSong", font_size=48)
        title.to_edge(UP)
        self.play(Write(title))
        
        # 酯化反应
        esterification_title = Text("酯化反应", font="STSong", font_size=32)
        esterification_title.next_to(title, DOWN)
        self.play(Write(esterification_title))
        
        # 修复：分离中文部分的反应方程式，使用标准箭头
        ester_reaction_left = MathTex("CH_3COOH + C_2H_5OH")
        ester_arrow = MathTex("\\overset{}{\\underset{\\Delta}{\\rightleftarrows}}")
        ester_catalyst = Text("H₂SO₄", font="STSong", font_size=16)
        ester_reaction_right = MathTex("CH_3COOC_2H_5 + H_2O")
        ester_reaction = VGroup(ester_reaction_left, ester_arrow, ester_catalyst, 
                               ester_reaction_right).arrange(RIGHT, buff=0.1)
        ester_reaction.shift(UP * 0.5)
        
        self.play(Write(ester_reaction))
        
        # 反应装置
        apparatus = self.create_esterification_apparatus()
        apparatus.shift(DOWN * 1.5)
        apparatus.scale(0.8)
        
        self.play(Create(apparatus))
        self.wait(2)
        
        # 水解反应
        self.play(FadeOut(apparatus))
        
        hydrolysis_title = Text("水解反应", font="STSong", font_size=32)
        self.play(Transform(esterification_title, hydrolysis_title))
        
        # 酸性水解
        acid_hydrolysis = MathTex(
            "CH_3COOC_2H_5 + H_2O \\xrightarrow{H^+} CH_3COOH + C_2H_5OH"
        )
        acid_hydrolysis.shift(DOWN * 0.5)
        
        # 碱性水解（皂化）
        base_hydrolysis = MathTex(
            "CH_3COOC_2H_5 + NaOH \\rightarrow CH_3COONa + C_2H_5OH"
        )
        base_hydrolysis.shift(DOWN * 1.5)
        
        self.play(Write(acid_hydrolysis))
        self.wait(1)
        self.play(Write(base_hydrolysis))
        self.wait(2)
        
        # 乙酸乙酯结构
        ethyl_acetate_struct = self.create_ethyl_acetate_structure()
        ethyl_acetate_struct.shift(DOWN * 3)
        ethyl_acetate_struct.scale(0.8)
        
        self.play(Create(ethyl_acetate_struct))
        self.wait(2)
        
        self.play(FadeOut(VGroup(title, esterification_title, ester_reaction, 
                                acid_hydrolysis, base_hydrolysis, ethyl_acetate_struct)))
    
    def create_esterification_apparatus(self):
        # 创建酯化反应装置
        # 圆底烧瓶
        flask = Circle(radius=1, color=BLUE_E, stroke_width=3)
        flask_neck = Rectangle(width=0.3, height=0.8, color=BLUE_E, stroke_width=3)
        flask_neck.next_to(flask, UP, buff=0)
        
        # 冷凝管
        condenser_outer = Rectangle(width=0.6, height=2, color=BLUE_E, stroke_width=3)
        condenser_inner = Rectangle(width=0.3, height=1.8, color=BLUE_E, stroke_width=2)
        condenser_outer.next_to(flask_neck, UP, buff=0.2)
        condenser_inner.move_to(condenser_outer.get_center())
        
        # 水流标记
        water_in = Arrow(condenser_outer.get_left() + DOWN * 0.5, 
                        condenser_outer.get_left() + DOWN * 0.3, color=BLUE)
        water_out = Arrow(condenser_outer.get_right() + UP * 0.3,
                         condenser_outer.get_right() + UP * 0.5, color=BLUE)
        
        # 接收瓶
        receiver = Circle(radius=0.6, color=BLUE_E, stroke_width=3)
        receiver.next_to(condenser_outer, UR, buff=0.5)
        
        # 标签
        flask_label = Text("反应混合物", font="STSong", font_size=16)
        flask_label.next_to(flask, DOWN)
        
        condenser_label = Text("冷凝管", font="STSong", font_size=16)
        condenser_label.next_to(condenser_outer, RIGHT)
        
        receiver_label = Text("乙酸乙酯", font="STSong", font_size=16)
        receiver_label.next_to(receiver, DOWN)
        
        return VGroup(flask, flask_neck, condenser_outer, condenser_inner,
                     water_in, water_out, receiver,
                     flask_label, condenser_label, receiver_label)
    
    def create_ethyl_acetate_structure(self):
        # 创建乙酸乙酯结构式
        # 乙酸部分
        c1 = Circle(radius=0.2, color=BLACK, fill_opacity=1)
        c1_text = Text("C", font_size=16, color=WHITE)
        carbon1 = VGroup(c1, c1_text)
        carbon1.shift(LEFT * 1.5)
        
        c2 = Circle(radius=0.2, color=BLACK, fill_opacity=1)
        c2_text = Text("C", font_size=16, color=WHITE)
        carbon2 = VGroup(c2, c2_text)
        carbon2.shift(LEFT * 0.5)
        
        o1 = Circle(radius=0.2, color=RED, fill_opacity=1)
        o1_text = Text("O", font_size=16, color=WHITE)
        oxygen1 = VGroup(o1, o1_text)
        oxygen1.shift(LEFT * 0.5 + UP * 0.7)
        
        # 酯基氧
        o2 = Circle(radius=0.2, color=RED, fill_opacity=1)
        o2_text = Text("O", font_size=16, color=WHITE)
        oxygen2 = VGroup(o2, o2_text)
        oxygen2.shift(RIGHT * 0.5)
        
        # 乙基部分
        c3 = Circle(radius=0.2, color=BLACK, fill_opacity=1)
        c3_text = Text("C", font_size=16, color=WHITE)
        carbon3 = VGroup(c3, c3_text)
        carbon3.shift(RIGHT * 1.5)
        
        c4 = Circle(radius=0.2, color=BLACK, fill_opacity=1)
        c4_text = Text("C", font_size=16, color=WHITE)
        carbon4 = VGroup(c4, c4_text)
        carbon4.shift(RIGHT * 2.5)
        
        # 键
        bonds = VGroup(
            Line(carbon1.get_center(), carbon2.get_center(), color=BLACK),
            Line(carbon2.get_center() + UP * 0.05, oxygen1.get_center() + DOWN * 0.05, color=BLACK),
            Line(carbon2.get_center() + UP * 0.15, oxygen1.get_center() + DOWN * 0.15, color=BLACK),
            Line(carbon2.get_center(), oxygen2.get_center(), color=BLACK),
            Line(oxygen2.get_center(), carbon3.get_center(), color=BLACK),
            Line(carbon3.get_center(), carbon4.get_center(), color=BLACK)
        )
        
        # 氢原子
        hydrogens = VGroup()
        h_bonds = VGroup()
        
        # 添加所有氢原子
        h_positions = [
            (carbon1, [LEFT + UP * 0.3, LEFT, LEFT + DOWN * 0.3]),
            (carbon3, [UP, DOWN]),
            (carbon4, [RIGHT + UP * 0.3, RIGHT, RIGHT + DOWN * 0.3])
        ]
        
        for carbon, positions in h_positions:
            for pos in positions:
                h = Circle(radius=0.12, color=GRAY, fill_opacity=1)
                h_text = Text("H", font_size=12, color=WHITE)
                h_atom = VGroup(h, h_text)
                h_atom.move_to(carbon.get_center() + pos * 0.4)
                hydrogens.add(h_atom)
                
                bond = Line(carbon.get_center(), h_atom.get_center(), color=BLACK)
                h_bonds.add(bond)
        
        return VGroup(bonds, h_bonds, carbon1, carbon2, carbon3, carbon4,
                     oxygen1, oxygen2, hydrogens)
    
    def show_functional_groups(self):
        title = Text("官能团与化学性质", font="STSong", font_size=48)
        title.to_edge(UP)
        self.play(Write(title))
        
        # 创建官能团表格
        functional_groups = [
            ("羟基", "-OH", "醇类", "氧化反应"),
            ("醛基", "-CHO", "醛类", "氧化还原"),
            ("羧基", "-COOH", "羧酸", "酸性"),
            ("酯基", "-COO-", "酯类", "水解反应"),
            ("碳碳双键", "C=C", "烯烃", "加成反应"),
            ("苯环", "C6H5-", "芳香烃", "取代反应")
        ]
        
        # 创建表格
        table = VGroup()
        headers = VGroup(
            Text("官能团", font="STSong", font_size=20),
            Text("结构", font="STSong", font_size=20),
            Text("类别", font="STSong", font_size=20),
            Text("特征反应", font="STSong", font_size=20)
        ).arrange(RIGHT, buff=1.5)
        headers.shift(UP * 2)
        table.add(headers)
        
        for i, (name, structure, category, reaction) in enumerate(functional_groups):
            row = VGroup(
                Text(name, font="STSong", font_size=18),
                MathTex(structure, font_size=18),
                Text(category, font="STSong", font_size=18),
                Text(reaction, font="STSong", font_size=18)
            ).arrange(RIGHT, buff=1.5)
            row.shift(UP * (1 - i * 0.5))
            table.add(row)
        
        table.center()
        self.play(Create(table))
        self.wait(3)
        
        # 鉴别试剂
        self.play(FadeOut(table))
        
        reagent_title = Text("有机物鉴别试剂", font="STSong", font_size=36)
        reagent_title.next_to(title, DOWN)
        self.play(Write(reagent_title))
        
        # 鉴别反应
        reactions = VGroup()
        
        # 溴水鉴别烯烃
        bromine_test = VGroup(
            Text("溴水褪色：", font="STSong", font_size=20),
            MathTex("C_2H_4 + Br_2 \\rightarrow C_2H_4Br_2"),
            Text("（红棕色→无色）", font="STSong", font_size=16)
        ).arrange(RIGHT, buff=0.3)
        bromine_test.shift(UP)
        
        # 高锰酸钾鉴别
        kmno4_test = VGroup(
            Text("酸性高锰酸钾：", font="STSong", font_size=20),
            MathTex("5C_2H_4 + 2KMnO_4 + 3H_2SO_4 \\rightarrow"),
            Text("（紫色→无色）", font="STSong", font_size=16)
        ).arrange(RIGHT, buff=0.3)
        
        # 银镜反应鉴别醛
        silver_test = VGroup(
            Text("银镜反应：", font="STSong", font_size=20),
            MathTex("RCHO + 2Ag(NH_3)_2OH \\rightarrow RCOONH_4 + 2Ag\\downarrow"),
            Text("（银镜）", font="STSong", font_size=16)
        ).arrange(RIGHT, buff=0.3)
        silver_test.shift(DOWN)
        
        reactions.add(bromine_test, kmno4_test, silver_test)
        self.play(Create(reactions))
        self.wait(3)
        
        self.play(FadeOut(VGroup(title, reagent_title, reactions)))
    
    def show_acetylene_preparation(self):
        title = Text("乙炔的实验室制法", font="STSong", font_size=48)
        title.to_edge(UP)
        self.play(Write(title))
        
        # 反应方程式
        reaction = MathTex("CaC_2 + 2H_2O \\rightarrow C_2H_2\\uparrow + Ca(OH)_2")
        reaction.next_to(title, DOWN, buff=0.5)
        self.play(Write(reaction))
        
        # 实验装置
        apparatus = self.create_acetylene_apparatus()
        apparatus.shift(DOWN * 0.5)
        apparatus.scale(0.8)
        
        self.play(Create(apparatus))
        
        # 注意事项
        notes = VGroup(
            Text("注意事项：", font="STSong", font_size=24),
            Text("1. 控制水的滴加速度", font="STSong", font_size=18),
            Text("2. 使用饱和食盐水代替纯水", font="STSong", font_size=18),
            Text("3. 收集前先检验纯度", font="STSong", font_size=18)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        notes.shift(DOWN * 2.5)
        
        self.play(Write(notes))
        self.wait(3)
        
        # 乙炔性质
        self.play(FadeOut(VGroup(apparatus, notes)))
        
        properties_title = Text("乙炔的化学性质", font="STSong", font_size=36)
        properties_title.next_to(reaction, DOWN, buff=0.5)
        self.play(Write(properties_title))
        
        # 加成反应 - 修复：使用LaTeX命令而不是Unicode字符
        addition1 = MathTex("HC\\equiv CH + Br_2 \\rightarrow CHBr=CHBr")
        addition2 = MathTex("CHBr=CHBr + Br_2 \\rightarrow CHBr_2-CHBr_2")
        addition1.shift(DOWN * 0.5)
        addition2.next_to(addition1, DOWN)
        
        # 氧化反应
        oxidation = MathTex("2C_2H_2 + 5O_2 \\rightarrow 4CO_2 + 2H_2O")
        oxidation.next_to(addition2, DOWN, buff=0.5)
        
        self.play(Write(addition1))
        self.wait(1)
        self.play(Write(addition2))
        self.wait(1)
        self.play(Write(oxidation))
        self.wait(2)
        
        self.play(FadeOut(VGroup(title, reaction, properties_title, 
                                addition1, addition2, oxidation)))
    
    def create_acetylene_apparatus(self):
        # 创建乙炔发生装置
        # 分液漏斗
        funnel = VGroup()
        funnel_top = Circle(radius=0.3, color=BLUE_E, stroke_width=3)
        funnel_neck = Polygon(
            funnel_top.get_bottom() + LEFT * 0.1,
            funnel_top.get_bottom() + RIGHT * 0.1,
            funnel_top.get_bottom() + DOWN * 0.8 + RIGHT * 0.05,
            funnel_top.get_bottom() + DOWN * 0.8 + LEFT * 0.05,
            color=BLUE_E, stroke_width=3
        )
        funnel.add(funnel_top, funnel_neck)
        funnel.shift(UP * 1.5)
        
        # 圆底烧瓶
        flask = Circle(radius=0.8, color=BLUE_E, stroke_width=3)
        flask_neck = Rectangle(width=0.3, height=0.5, color=BLUE_E, stroke_width=3)
        flask_neck.next_to(flask, UP, buff=0)
        
        # 导管
        tube1 = Line(flask.get_right(), flask.get_right() + RIGHT * 1.5, 
                    color=BLUE_E, stroke_width=3)
        tube2 = Line(tube1.get_end(), tube1.get_end() + DOWN * 0.5,
                    color=BLUE_E, stroke_width=3)
        
        # 集气瓶
        collector = Rectangle(width=0.8, height=1.2, color=BLUE_E, stroke_width=3)
        collector.next_to(tube2, DOWN, buff=0.2)
        
        # 水槽
        water_trough = Rectangle(width=2, height=0.8, color=BLUE, fill_opacity=0.3)
        water_trough.move_to(collector.get_bottom() + DOWN * 0.2)
        
        # 标签
        cac2_label = Text("电石", font="STSong", font_size=16)
        cac2_label.move_to(flask.get_center())
        
        water_label = Text("水", font="STSong", font_size=16)
        water_label.move_to(funnel_top.get_center())
        
        gas_label = Text("乙炔", font="STSong", font_size=16)
        gas_label.next_to(collector, RIGHT)
        
        return VGroup(funnel, flask, flask_neck, tube1, tube2, 
                     collector, water_trough,
                     cac2_label, water_label, gas_label)
    
    def show_aromatic_hydrocarbons(self):
        title = Text("芳香烃的结构与性质", font="STSong", font_size=48)
        title.to_edge(UP)
        self.play(Write(title))
        
        # 苯的结构
        benzene_struct = self.create_benzene_structure()
        benzene_label = Text("苯", font="STSong", font_size=24)
        benzene_formula = MathTex("C_6H_6")
        benzene_group = VGroup(benzene_struct, benzene_label, benzene_formula)
        benzene_group.arrange(DOWN, buff=0.3)
        benzene_group.shift(LEFT * 3)
        
        # 甲苯的结构
        toluene_struct = self.create_toluene_structure()
        toluene_label = Text("甲苯", font="STSong", font_size=24)
        toluene_formula = MathTex("C_6H_5CH_3")
        toluene_group = VGroup(toluene_struct, toluene_label, toluene_formula)
        toluene_group.arrange(DOWN, buff=0.3)
        
        # 萘的结构
        naphthalene_struct = self.create_naphthalene_structure()
        naphthalene_label = Text("萘", font="STSong", font_size=24)
        naphthalene_formula = MathTex("C_{10}H_8")
        naphthalene_group = VGroup(naphthalene_struct, naphthalene_label, naphthalene_formula)
        naphthalene_group.arrange(DOWN, buff=0.3)
        naphthalene_group.shift(RIGHT * 3)
        
        self.play(
            Create(benzene_group),
            Create(toluene_group),
            Create(naphthalene_group)
        )
        self.wait(2)
        
        # 苯的化学性质
        self.play(FadeOut(toluene_group), FadeOut(naphthalene_group))
        benzene_group.animate.move_to(ORIGIN + UP)
        
        reactions_title = Text("苯的化学反应", font="STSong", font_size=32)
        reactions_title.next_to(benzene_group, DOWN, buff=0.5)
        self.play(Write(reactions_title))
        
        # 取代反应
        substitution = VGroup(
            Text("硝化：", font="STSong", font_size=20),
            MathTex("C_6H_6 + HNO_3 \\xrightarrow{H_2SO_4} C_6H_5NO_2 + H_2O")
        ).arrange(RIGHT, buff=0.3)
        substitution.shift(DOWN * 1.5)
        
        # 加成反应
        addition = VGroup(
            Text("加氢：", font="STSong", font_size=20),
            MathTex("C_6H_6 + 3H_2 \\xrightarrow{Ni} C_6H_{12}")
        ).arrange(RIGHT, buff=0.3)
        addition.next_to(substitution, DOWN, buff=0.3)
        
        self.play(Write(substitution))
        self.wait(1)
        self.play(Write(addition))
        self.wait(2)
        
        self.play(FadeOut(VGroup(title, benzene_group, reactions_title, 
                                substitution, addition)))
    
    def create_benzene_structure(self):
        # 创建苯环结构
        hexagon = RegularPolygon(6, radius=0.8, color=BLACK)
        
        # 内圈表示离域π电子
        inner_circle = Circle(radius=0.5, color=BLACK)
        
        # 碳原子和氢原子
        carbons = VGroup()
        hydrogens = VGroup()
        bonds = VGroup()
        
        vertices = hexagon.get_vertices()
        for i, vertex in enumerate(vertices):
            # 碳原子
            c = Circle(radius=0.15, color=BLACK, fill_opacity=1)
            c_text = Text("C", font_size=12, color=WHITE)
            carbon = VGroup(c, c_text)
            carbon.move_to(vertex)
            carbons.add(carbon)
            
            # 氢原子
            h = Circle(radius=0.1, color=GRAY, fill_opacity=1)
            h_text = Text("H", font_size=10, color=WHITE)
            h_atom = VGroup(h, h_text)
            direction = vertex - hexagon.get_center()
            h_atom.move_to(vertex + direction * 0.4)
            hydrogens.add(h_atom)
            
            # C-H键
            bond = Line(carbon.get_center(), h_atom.get_center(), color=BLACK)
            bonds.add(bond)
        
        return VGroup(hexagon, inner_circle, bonds, carbons, hydrogens)
    
    def create_toluene_structure(self):
        # 创建甲苯结构（苯环+甲基）
        benzene = self.create_benzene_structure()
        benzene.scale(0.8)
        
        # 移除顶部的氢原子
        benzene[-1][0].set_opacity(0)  # 隐藏顶部氢原子
        benzene[-2][0].set_opacity(0)  # 隐藏对应的键
        
        # 添加甲基
        methyl_c = Circle(radius=0.15, color=BLACK, fill_opacity=1)
        methyl_c_text = Text("C", font_size=12, color=WHITE)
        methyl_carbon = VGroup(methyl_c, methyl_c_text)
        methyl_carbon.move_to(benzene.get_top() + UP * 0.6)
        
        # 甲基的氢原子
        methyl_hydrogens = VGroup()
        h_positions = [UP * 0.3, LEFT * 0.3 + UP * 0.15, RIGHT * 0.3 + UP * 0.15]
        
        for pos in h_positions:
            h = Circle(radius=0.1, color=GRAY, fill_opacity=1)
            h_text = Text("H", font_size=10, color=WHITE)
            h_atom = VGroup(h, h_text)
            h_atom.move_to(methyl_carbon.get_center() + pos)
            methyl_hydrogens.add(h_atom)
        
        # 连接键
        c_c_bond = Line(benzene[-3][0].get_center(), methyl_carbon.get_center(), color=BLACK)
        
        methyl_bonds = VGroup()
        for h in methyl_hydrogens:
            bond = Line(methyl_carbon.get_center(), h.get_center(), color=BLACK)
            methyl_bonds.add(bond)
        
        return VGroup(benzene, c_c_bond, methyl_bonds, methyl_carbon, methyl_hydrogens)
    
    def create_naphthalene_structure(self):
        # 创建萘的结构（两个苯环稠合）
        # 左边苯环
        hex1 = RegularPolygon(6, radius=0.6, color=BLACK)
        hex1.shift(LEFT * 0.52)
        
        # 右边苯环
        hex2 = RegularPolygon(6, radius=0.6, color=BLACK)
        hex2.shift(RIGHT * 0.52)
        
        # 内圈
        circle1 = Circle(radius=0.35, color=BLACK)
        circle1.move_to(hex1.get_center())
        
        circle2 = Circle(radius=0.35, color=BLACK)
        circle2.move_to(hex2.get_center())
        
        return VGroup(hex1, hex2, circle1, circle2)
    
    def show_carbonyl_compounds(self):
        title = Text("醛、酮、羧酸、酯的结构与性质", font="STSong", font_size=48)
        title.to_edge(UP)
        self.play(Write(title))
        
        # 醛的结构
        aldehyde_struct = self.create_aldehyde_structure()
        aldehyde_label = Text("乙醛", font="STSong", font_size=20)
        aldehyde_formula = MathTex("CH_3CHO")
        aldehyde_group = VGroup(aldehyde_struct, aldehyde_label, aldehyde_formula)
        aldehyde_group.arrange(DOWN, buff=0.2)
        aldehyde_group.shift(LEFT * 4.5 + UP * 1.5)
        
        # 酮的结构
        ketone_struct = self.create_ketone_structure()
        ketone_label = Text("丙酮", font="STSong", font_size=20)
        ketone_formula = MathTex("CH_3COCH_3")
        ketone_group = VGroup(ketone_struct, ketone_label, ketone_formula)
        ketone_group.arrange(DOWN, buff=0.2)
        ketone_group.shift(LEFT * 1.5 + UP * 1.5)
        
        # 羧酸的结构
        acid_struct = self.create_carboxylic_acid_structure()
        acid_label = Text("丙酸", font="STSong", font_size=20)
        acid_formula = MathTex("C_2H_5COOH")
        acid_group = VGroup(acid_struct, acid_label, acid_formula)
        acid_group.arrange(DOWN, buff=0.2)
        acid_group.shift(RIGHT * 1.5 + UP * 1.5)
        
        # 酯的结构
        ester_struct = self.create_ester_structure()
        ester_label = Text("乙酸甲酯", font="STSong", font_size=20)
        ester_formula = MathTex("CH_3COOCH_3")
        ester_group = VGroup(ester_struct, ester_label, ester_formula)
        ester_group.arrange(DOWN, buff=0.2)
        ester_group.shift(RIGHT * 4.5 + UP * 1.5)
        
        self.play(
            Create(aldehyde_group),
            Create(ketone_group),
            Create(acid_group),
            Create(ester_group)
        )
        self.wait(2)
        
        # 化学性质对比
        properties_table = self.create_carbonyl_properties_table()
        properties_table.shift(DOWN * 1.5)
        properties_table.scale(0.8)
        
        self.play(Create(properties_table))
        self.wait(3)
        
        # 特征反应
        self.play(FadeOut(properties_table))
        
        reactions_title = Text("特征反应", font="STSong", font_size=36)
        reactions_title.shift(DOWN * 1)
        self.play(Write(reactions_title))
        
        # 醛的氧化
        aldehyde_oxidation = MathTex("RCHO + [O] \\rightarrow RCOOH")
        aldehyde_oxidation.shift(DOWN * 2)
        
        # 酮不易氧化
        ketone_property = Text("酮：不易被氧化", font="STSong", font_size=20)
        ketone_property.next_to(aldehyde_oxidation, DOWN, buff=0.3)
        
        # 羧酸的酸性
        acid_reaction = MathTex("RCOOH + NaOH \\rightarrow RCOONa + H_2O")
        acid_reaction.next_to(ketone_property, DOWN, buff=0.3)
        
        # 酯的水解 - 修复：使用标准的箭头表示可逆反应
        ester_hydrolysis = MathTex("RCOOR' + H_2O \\overset{H^+}{\\rightleftarrows} RCOOH + R'OH")
        ester_hydrolysis.next_to(acid_reaction, DOWN, buff=0.3)
        
        self.play(
            Write(aldehyde_oxidation),
            Write(ketone_property),
            Write(acid_reaction),
            Write(ester_hydrolysis)
        )
        self.wait(3)
        
        self.play(FadeOut(VGroup(title, aldehyde_group, ketone_group, acid_group, ester_group,
                                reactions_title, aldehyde_oxidation, ketone_property,
                                acid_reaction, ester_hydrolysis)))
    
    def create_aldehyde_structure(self):
        # 创建乙醛结构
        c1 = Circle(radius=0.2, color=BLACK, fill_opacity=1)
        c1_text = Text("C", font_size=16, color=WHITE)
        carbon1 = VGroup(c1, c1_text)
        carbon1.shift(LEFT * 0.5)
        
        c2 = Circle(radius=0.2, color=BLACK, fill_opacity=1)
        c2_text = Text("C", font_size=16, color=WHITE)
        carbon2 = VGroup(c2, c2_text)
        carbon2.shift(RIGHT * 0.5)
        
        o = Circle(radius=0.2, color=RED, fill_opacity=1)
        o_text = Text("O", font_size=16, color=WHITE)
        oxygen = VGroup(o, o_text)
        oxygen.shift(RIGHT * 0.5 + UP * 0.7)
        
        h_aldehyde = Circle(radius=0.12, color=GRAY, fill_opacity=1)
        h_aldehyde_text = Text("H", font_size=12, color=WHITE)
        h_atom = VGroup(h_aldehyde, h_aldehyde_text)
        h_atom.shift(RIGHT * 1.2)
        
        # 键
        c_c_bond = Line(carbon1.get_center(), carbon2.get_center(), color=BLACK)
        c_o_double1 = Line(carbon2.get_center() + UP * 0.05, oxygen.get_center() + DOWN * 0.05, color=BLACK)
        c_o_double2 = Line(carbon2.get_center() + UP * 0.15, oxygen.get_center() + DOWN * 0.15, color=BLACK)
        c_h_bond = Line(carbon2.get_center(), h_atom.get_center(), color=BLACK)
        
        # 甲基氢
        methyl_h = self.create_methyl_hydrogens(carbon1)
        
        return VGroup(c_c_bond, c_o_double1, c_o_double2, c_h_bond,
                     carbon1, carbon2, oxygen, h_atom, methyl_h)
    
    def create_ketone_structure(self):
        # 创建丙酮结构
        c1 = Circle(radius=0.2, color=BLACK, fill_opacity=1)
        c1_text = Text("C", font_size=16, color=WHITE)
        carbon1 = VGroup(c1, c1_text)
        carbon1.shift(LEFT * 0.8)
        
        c2 = Circle(radius=0.2, color=BLACK, fill_opacity=1)
        c2_text = Text("C", font_size=16, color=WHITE)
        carbon2 = VGroup(c2, c2_text)
        
        c3 = Circle(radius=0.2, color=BLACK, fill_opacity=1)
        c3_text = Text("C", font_size=16, color=WHITE)
        carbon3 = VGroup(c3, c3_text)
        carbon3.shift(RIGHT * 0.8)
        
        o = Circle(radius=0.2, color=RED, fill_opacity=1)
        o_text = Text("O", font_size=16, color=WHITE)
        oxygen = VGroup(o, o_text)
        oxygen.shift(UP * 0.7)
        
        # 键
        c1_c2_bond = Line(carbon1.get_center(), carbon2.get_center(), color=BLACK)
        c2_c3_bond = Line(carbon2.get_center(), carbon3.get_center(), color=BLACK)
        c_o_double1 = Line(carbon2.get_center() + UP * 0.05, oxygen.get_center() + DOWN * 0.05, color=BLACK)
        c_o_double2 = Line(carbon2.get_center() + UP * 0.15, oxygen.get_center() + DOWN * 0.15, color=BLACK)
        
        # 甲基氢
        methyl_h1 = self.create_methyl_hydrogens(carbon1)
        methyl_h3 = self.create_methyl_hydrogens(carbon3)
        
        return VGroup(c1_c2_bond, c2_c3_bond, c_o_double1, c_o_double2,
                     carbon1, carbon2, carbon3, oxygen, methyl_h1, methyl_h3)
    
    def create_carboxylic_acid_structure(self):
        # 创建丙酸结构
        c1 = Circle(radius=0.2, color=BLACK, fill_opacity=1)
        c1_text = Text("C", font_size=16, color=WHITE)
        carbon1 = VGroup(c1, c1_text)
        carbon1.shift(LEFT * 1.2)
        
        c2 = Circle(radius=0.2, color=BLACK, fill_opacity=1)
        c2_text = Text("C", font_size=16, color=WHITE)
        carbon2 = VGroup(c2, c2_text)
        carbon2.shift(LEFT * 0.4)
        
        c3 = Circle(radius=0.2, color=BLACK, fill_opacity=1)
        c3_text = Text("C", font_size=16, color=WHITE)
        carbon3 = VGroup(c3, c3_text)
        carbon3.shift(RIGHT * 0.4)
        
        o1 = Circle(radius=0.2, color=RED, fill_opacity=1)
        o1_text = Text("O", font_size=16, color=WHITE)
        oxygen1 = VGroup(o1, o1_text)
        oxygen1.shift(RIGHT * 0.4 + UP * 0.7)
        
        o2 = Circle(radius=0.2, color=RED, fill_opacity=1)
        o2_text = Text("O", font_size=16, color=WHITE)
        oxygen2 = VGroup(o2, o2_text)
        oxygen2.shift(RIGHT * 1.2)
        
        h_acid = Circle(radius=0.12, color=GRAY, fill_opacity=1)
        h_acid_text = Text("H", font_size=12, color=WHITE)
        h_hydroxyl = VGroup(h_acid, h_acid_text)
        h_hydroxyl.shift(RIGHT * 1.8)
        
        # 键
        bonds = VGroup(
            Line(carbon1.get_center(), carbon2.get_center(), color=BLACK),
            Line(carbon2.get_center(), carbon3.get_center(), color=BLACK),
            Line(carbon3.get_center() + UP * 0.05, oxygen1.get_center() + DOWN * 0.05, color=BLACK),
            Line(carbon3.get_center() + UP * 0.15, oxygen1.get_center() + DOWN * 0.15, color=BLACK),
            Line(carbon3.get_center(), oxygen2.get_center(), color=BLACK),
            Line(oxygen2.get_center(), h_hydroxyl.get_center(), color=BLACK)
        )
        
        # 烷基氢
        alkyl_h = self.create_alkyl_hydrogens(carbon1, carbon2)
        
        return VGroup(bonds, carbon1, carbon2, carbon3, oxygen1, oxygen2, h_hydroxyl, alkyl_h)
    
    def create_ester_structure(self):
        # 创建乙酸甲酯结构
        c1 = Circle(radius=0.2, color=BLACK, fill_opacity=1)
        c1_text = Text("C", font_size=16, color=WHITE)
        carbon1 = VGroup(c1, c1_text)
        carbon1.shift(LEFT * 0.8)
        
        c2 = Circle(radius=0.2, color=BLACK, fill_opacity=1)
        c2_text = Text("C", font_size=16, color=WHITE)
        carbon2 = VGroup(c2, c2_text)
        
        o1 = Circle(radius=0.2, color=RED, fill_opacity=1)
        o1_text = Text("O", font_size=16, color=WHITE)
        oxygen1 = VGroup(o1, o1_text)
        oxygen1.shift(UP * 0.7)
        
        o2 = Circle(radius=0.2, color=RED, fill_opacity=1)
        o2_text = Text("O", font_size=16, color=WHITE)
        oxygen2 = VGroup(o2, o2_text)
        oxygen2.shift(RIGHT * 0.8)
        
        c3 = Circle(radius=0.2, color=BLACK, fill_opacity=1)
        c3_text = Text("C", font_size=16, color=WHITE)
        carbon3 = VGroup(c3, c3_text)
        carbon3.shift(RIGHT * 1.6)
        
        # 键
        bonds = VGroup(
            Line(carbon1.get_center(), carbon2.get_center(), color=BLACK),
            Line(carbon2.get_center() + UP * 0.05, oxygen1.get_center() + DOWN * 0.05, color=BLACK),
            Line(carbon2.get_center() + UP * 0.15, oxygen1.get_center() + DOWN * 0.15, color=BLACK),
            Line(carbon2.get_center(), oxygen2.get_center(), color=BLACK),
            Line(oxygen2.get_center(), carbon3.get_center(), color=BLACK)
        )
        
        # 甲基氢
        methyl_h1 = self.create_methyl_hydrogens(carbon1)
        methyl_h3 = self.create_methyl_hydrogens(carbon3)
        
        return VGroup(bonds, carbon1, carbon2, carbon3, oxygen1, oxygen2, methyl_h1, methyl_h3)
    
    def create_methyl_hydrogens(self, carbon):
        # 为甲基碳添加三个氢原子
        hydrogens = VGroup()
        h_positions = [
            carbon.get_center() + LEFT * 0.4 + UP * 0.2,
            carbon.get_center() + LEFT * 0.4,
            carbon.get_center() + LEFT * 0.4 + DOWN * 0.2
        ]
        
        for pos in h_positions:
            h = Circle(radius=0.1, color=GRAY, fill_opacity=1)
            h_text = Text("H", font_size=10, color=WHITE)
            h_atom = VGroup(h, h_text)
            h_atom.move_to(pos)
            hydrogens.add(h_atom)
            
            bond = Line(carbon.get_center(), h_atom.get_center(), color=BLACK)
            hydrogens.add(bond)
        
        return hydrogens
    
    def create_alkyl_hydrogens(self, carbon1, carbon2):
        # 为丙酸的烷基部分添加氢原子
        hydrogens = VGroup()
        
        # 第一个碳的氢
        h_positions1 = [
            carbon1.get_center() + LEFT * 0.4 + UP * 0.2,
            carbon1.get_center() + LEFT * 0.4,
            carbon1.get_center() + LEFT * 0.4 + DOWN * 0.2
        ]
        
        for pos in h_positions1:
            h = Circle(radius=0.1, color=GRAY, fill_opacity=1)
            h_text = Text("H", font_size=10, color=WHITE)
            h_atom = VGroup(h, h_text)
            h_atom.move_to(pos)
            hydrogens.add(h_atom)
            
            bond = Line(carbon1.get_center(), h_atom.get_center(), color=BLACK)
            hydrogens.add(bond)
        
        # 第二个碳的氢
        h_positions2 = [
            carbon2.get_center() + UP * 0.4,
            carbon2.get_center() + DOWN * 0.4
        ]
        
        for pos in h_positions2:
            h = Circle(radius=0.1, color=GRAY, fill_opacity=1)
            h_text = Text("H", font_size=10, color=WHITE)
            h_atom = VGroup(h, h_text)
            h_atom.move_to(pos)
            hydrogens.add(h_atom)
            
            bond = Line(carbon2.get_center(), h_atom.get_center(), color=BLACK)
            hydrogens.add(bond)
        
        return hydrogens
    
    def create_carbonyl_properties_table(self):
        # 创建羰基化合物性质对比表格
        table = VGroup()
        
        headers = VGroup(
            Text("类别", font="STSong", font_size=20),
            Text("沸点", font="STSong", font_size=20),
            Text("溶解性", font="STSong", font_size=20),
            Text("还原性", font="STSong", font_size=20)
        ).arrange(RIGHT, buff=1)
        
        rows = [
            [
                Text("醛", font="STSong", font_size=18),
                Text("较低", font="STSong", font_size=18),
                Text("较小", font="STSong", font_size=18),
                Text("强", font="STSong", font_size=18)
            ],
            [
                Text("酮", font="STSong", font_size=18),
                Text("较低", font="STSong", font_size=18),
                Text("较小", font="STSong", font_size=18),
                Text("弱", font="STSong", font_size=18)
            ],
            [
                Text("羧酸", font="STSong", font_size=18),
                Text("较高", font="STSong", font_size=18),
                Text("较大", font="STSong", font_size=18),
                Text("无", font="STSong", font_size=18)
            ],
            [
                Text("酯", font="STSong", font_size=18),
                Text("中等", font="STSong", font_size=18),
                Text("小", font="STSong", font_size=18),
                Text("无", font="STSong", font_size=18)
            ]
        ]
        
        table.add(headers)
        
        for i, row_content in enumerate(rows):
            row = VGroup(*row_content).arrange(RIGHT, buff=1)
            row.shift(DOWN * (i + 1) * 0.6)
            table.add(row)
        
        # 添加表格边框
        table_rect = Rectangle(
            width=headers.width + 0.5,
            height=(len(rows) + 1) * 0.6 + 0.3,
            color=BLUE_E
        )
        table_rect.move_to(table.get_center())
        
        return VGroup(table_rect, table)
    
    def show_synthesis_flowchart(self):
        title = Text("有机化合物合成路线图", font="STSong", font_size=48)
        title.to_edge(UP)
        self.play(Write(title))
        
        # 创建主要原料
        starting_materials = VGroup()
        
        coal = Circle(radius=0.5, color=BLACK, fill_opacity=0.8)
        coal_label = Text("煤", font="STSong", font_size=18, color=WHITE)
        coal_label.move_to(coal.get_center())
        coal_group = VGroup(coal, coal_label)
        
        petroleum = Circle(radius=0.5, color=BLUE, fill_opacity=0.8)
        petroleum_label = Text("石油", font="STSong", font_size=18, color=WHITE)
        petroleum_label.move_to(petroleum.get_center())
        petroleum_group = VGroup(petroleum, petroleum_label)
        
        natural_gas = Circle(radius=0.5, color=BLUE, fill_opacity=0.8)
        natural_gas_label = Text("天然气", font="STSong", font_size=18, color=WHITE)
        natural_gas_label.move_to(natural_gas.get_center())
        natural_gas_group = VGroup(natural_gas, natural_gas_label)
        
        starting_materials.add(coal_group, petroleum_group, natural_gas_group)
        starting_materials.arrange(RIGHT, buff=1.5)
        starting_materials.shift(UP * 2)
        
        self.play(Create(starting_materials))
        
        # 基础原料层
        basic_materials = VGroup()
        
        ethylene = self.create_basic_box("乙烯", "C_2H_4")
        propylene = self.create_basic_box("丙烯", "C_3H_6")
        benzene = self.create_basic_box("苯", "C_6H_6")
        acetylene = self.create_basic_box("乙炔", "C_2H_2")
        
        basic_materials.add(ethylene, propylene, benzene, acetylene)
        basic_materials.arrange(RIGHT, buff=0.8)
        basic_materials.shift(UP * 0.5)
        
        self.play(Create(basic_materials))
        
        # 连接箭头 - 从原料到基础原料
        arrows1 = VGroup()
        for source in starting_materials:
            for target in basic_materials:
                arrow = Arrow(source.get_bottom(), target.get_top(),
                            color=GRAY, stroke_width=2)
                arrows1.add(arrow)
        
        self.play(Create(arrows1))
        
        # 中间产物层
        intermediates = VGroup()
        
        ethanol = self.create_basic_box("乙醇", "C_2H_5OH")
        acetaldehyde = self.create_basic_box("乙醛", "CH_3CHO")
        acetic_acid = self.create_basic_box("乙酸", "CH_3COOH")
        ethyl_acetate = self.create_basic_box("乙酸乙酯", "CH_3COOC_2H_5")
        
        intermediates.add(ethanol, acetaldehyde, acetic_acid, ethyl_acetate)
        intermediates.arrange(RIGHT, buff=0.8)
        intermediates.shift(DOWN * 1)
        
        self.play(Create(intermediates))
        
        # 连接箭头 - 从基础原料到中间产物
        arrows2 = VGroup()
        key_connections = [
            (ethylene, ethanol),
            (ethylene, acetaldehyde),
            (acetylene, acetaldehyde),
            (acetaldehyde, acetic_acid),
            (acetic_acid, ethyl_acetate),
            (ethanol, ethyl_acetate)
        ]
        
        for source, target in key_connections:
            arrow = Arrow(source.get_bottom(), target.get_top(),
                        color=YELLOW, stroke_width=3)
            arrows2.add(arrow)
        
        self.play(Create(arrows2))
        
        # 最终产品层
        final_products = VGroup()
        
        polyethylene = self.create_product_box("聚乙烯", "高分子材料")
        pvc = self.create_product_box("聚氯乙烯", "建筑材料")
        medicines = self.create_product_box("药物", "医药化工")
        plastics = self.create_product_box("塑料制品", "日用品")
        
        final_products.add(polyethylene, pvc, medicines, plastics)
        final_products.arrange(RIGHT, buff=0.8)
        final_products.shift(DOWN * 2.5)
        
        self.play(Create(final_products))
        
        # 连接箭头 - 从中间产物到最终产品
        arrows3 = VGroup()
        for intermediate in intermediates:
            for product in final_products:
                arrow = Arrow(intermediate.get_bottom(), product.get_top(),
                            color=GRAY, stroke_width=2)
                arrows3.add(arrow)
        
        self.play(Create(arrows3))
        
        # 添加反应类型标注
        reactions = VGroup(
            Text("加成", font="STSong", font_size=16, color=RED),
            Text("氧化", font="STSong", font_size=16, color=RED),
            Text("酯化", font="STSong", font_size=16, color=RED),
            Text("聚合", font="STSong", font_size=16, color=RED)
        )
        
        reactions[0].next_to(arrows2[0], RIGHT)
        reactions[1].next_to(arrows2[3], RIGHT)
        reactions[2].next_to(arrows2[4], RIGHT)
        reactions[3].next_to(Arrow(ethylene.get_bottom(), polyethylene.get_top(),
                                 color=YELLOW, stroke_width=3), RIGHT)
        
        self.play(Write(reactions))
        self.wait(3)
        
        # 结束动画
        ending_text = Text("有机化学 - 分子世界的艺术", font="STSong", font_size=36)
        ending_text.to_edge(DOWN)
        
        self.play(
            FadeOut(VGroup(title, starting_materials, arrows1, basic_materials,
                          arrows2, intermediates, arrows3, final_products, reactions)),
            Write(ending_text)
        )
        self.wait(2)
        self.play(FadeOut(ending_text))
    
    def create_basic_box(self, name, formula):
        box = Rectangle(width=1.8, height=1, color=BLUE_E, fill_opacity=0.2)
        name_text = Text(name, font="STSong", font_size=16)
        formula_text = MathTex(formula, font_size=14)
        
        text_group = VGroup(name_text, formula_text).arrange(DOWN, buff=0.1)
        text_group.move_to(box.get_center())
        
        return VGroup(box, text_group)
    
    def create_product_box(self, name, category):
        box = Rectangle(width=2, height=1.2, color=GREEN_E, fill_opacity=0.3)
        name_text = Text(name, font="STSong", font_size=16)
        category_text = Text(category, font="STSong", font_size=12)
        
        text_group = VGroup(name_text, category_text).arrange(DOWN, buff=0.1)
        text_group.move_to(box.get_center())
        
        return VGroup(box, text_group)


class OrganicChemistry3D(ThreeDScene):
    def construct(self):
        # 3D分子结构展示
        title = Text("有机分子的三维结构", font="STSong", font_size=48)
        title.to_edge(UP)
        self.add_fixed_in_frame_mobjects(title)
        self.play(Write(title))
        
        # 甲烷的四面体结构
        methane = self.create_methane_3d()
        methane.scale(0.8)
        
        self.play(Create(methane))
        self.wait(1)
        
        # 旋转展示3D结构
        self.move_camera(phi=75 * DEGREES, theta=30 * DEGREES)
        self.begin_ambient_camera_rotation(rate=0.2)
        self.wait(5)
        self.stop_ambient_camera_rotation()
        
        # 移动到另一个视角
        self.move_camera(phi=45 * DEGREES, theta=135 * DEGREES)
        self.wait(2)
        
        # 切换到乙烯的平面结构
        self.play(FadeOut(methane))
        
        ethene = self.create_ethene_3d()
        ethene.scale(0.8)
        
        self.play(Create(ethene))
        self.wait(1)
        
        # 旋转展示乙烯结构
        self.begin_ambient_camera_rotation(rate=0.2)
        self.wait(5)
        self.stop_ambient_camera_rotation()
        
        # 切换到苯环结构
        self.play(FadeOut(ethene))
        
        benzene = self.create_benzene_3d()
        benzene.scale(0.7)
        
        self.play(Create(benzene))
        self.wait(1)
        
        # 旋转展示苯环结构
        self.begin_ambient_camera_rotation(rate=0.2)
        self.wait(5)
        self.stop_ambient_camera_rotation()
        
        # 结束
        conclusion = Text("分子结构决定性质", font="STSong", font_size=32)
        conclusion.next_to(title, DOWN)
        self.add_fixed_in_frame_mobjects(conclusion)
        
        self.play(Write(conclusion))
        self.wait(2)
        
        self.play(FadeOut(VGroup(title, conclusion, benzene)))
    
    def create_methane_3d(self):
        # 创建甲烷四面体结构
        # 中心碳原子
        carbon = Sphere(radius=0.3, color=BLACK)
        
        # 计算四面体顶点坐标
        h_coords = [
            np.array([1, 1, 1]),
            np.array([1, -1, -1]),
            np.array([-1, 1, -1]),
            np.array([-1, -1, 1])
        ]
        h_coords = [coord / np.linalg.norm(coord) for coord in h_coords]
        
        # 氢原子
        hydrogens = VGroup()
        bonds = VGroup()
        
        for coord in h_coords:
            h = Sphere(radius=0.15, color=GRAY)
            h.move_to(coord)
            hydrogens.add(h)
            
            # C-H键
            bond = Line3D(
                start=ORIGIN,
                end=coord,
                color=WHITE,
                thickness=0.05
            )
            bonds.add(bond)
        
        return VGroup(carbon, hydrogens, bonds)
    
    def create_ethene_3d(self):
        # 创建乙烯的平面结构
        # 两个碳原子
        c1 = Sphere(radius=0.3, color=BLACK)
        c1.shift(LEFT * 0.6)
        
        c2 = Sphere(radius=0.3, color=BLACK)
        c2.shift(RIGHT * 0.6)
        
        # C=C双键
        double_bond1 = Cylinder(
            height=1.2,
            radius=0.05,
            direction=RIGHT,
            color=WHITE
        )
        double_bond1.shift(UP * 0.1)
        
        double_bond2 = Cylinder(
            height=1.2,
            radius=0.05,
            direction=RIGHT,
            color=WHITE
        )
        double_bond2.shift(DOWN * 0.1)
        
        # 氢原子位置
        h_positions = [
            c1.get_center() + LEFT * 0.6 + UP * 0.6,
            c1.get_center() + LEFT * 0.6 + DOWN * 0.6,
            c2.get_center() + RIGHT * 0.6 + UP * 0.6,
            c2.get_center() + RIGHT * 0.6 + DOWN * 0.6
        ]
        
        # 氢原子
        hydrogens = VGroup()
        h_bonds = VGroup()
        
        for pos in h_positions:
            h = Sphere(radius=0.15, color=GRAY)
            h.move_to(pos)
            hydrogens.add(h)
            
            start = c1.get_center() if np.linalg.norm(pos - c1.get_center()) < np.linalg.norm(pos - c2.get_center()) else c2.get_center()
            
            # C-H键
            bond = Line3D(
                start=start,
                end=pos,
                color=WHITE,
                thickness=0.05
            )
            h_bonds.add(bond)
        
        return VGroup(c1, c2, double_bond1, double_bond2, hydrogens, h_bonds)
    
    def create_benzene_3d(self):
        # 创建苯环的平面结构
        # 六个碳原子
        carbons = VGroup()
        hydrogens = VGroup()
        c_c_bonds = VGroup()
        c_h_bonds = VGroup()
        
        # 创建正六边形的顶点坐标
        radius = 1.2
        angles = np.linspace(0, 2*np.pi, 7)[:-1]
        
        for angle in angles:
            x = radius * np.cos(angle)
            y = radius * np.sin(angle)
            
            # 碳原子
            c = Sphere(radius=0.25, color=BLACK)
            c.move_to([x, y, 0])
            carbons.add(c)
            
            # 氢原子
            h = Sphere(radius=0.15, color=GRAY)
            h.move_to([x * 1.5, y * 1.5, 0])
            hydrogens.add(h)
            
            # C-H键
            c_h_bond = Line3D(
                start=[x, y, 0],
                end=[x * 1.5, y * 1.5, 0],
                color=WHITE,
                thickness=0.05
            )
            c_h_bonds.add(c_h_bond)
        
        # 创建C-C键
        for i in range(6):
            start = carbons[i].get_center()
            end = carbons[(i+1) % 6].get_center()
            
            bond = Line3D(
                start=start,
                end=end,
                color=WHITE,
                thickness=0.05
            )
            c_c_bonds.add(bond)
        
        # π电子云示意
        pi_cloud_top = Surface(
            lambda u, v: np.array([
                radius * 0.8 * np.cos(u),
                radius * 0.8 * np.sin(u),
                0.2 * np.sin(3*u) * np.cos(v)
            ]),
            u_range=[0, 2*np.pi],
            v_range=[0, 2*np.pi],
            resolution=(12, 12),
            fill_opacity=0.2,
            fill_color=BLUE,
            stroke_width=0
        )
        
        pi_cloud_bottom = Surface(
            lambda u, v: np.array([
                radius * 0.8 * np.cos(u),
                radius * 0.8 * np.sin(u),
                -0.2 * np.sin(3*u) * np.cos(v)
            ]),
            u_range=[0, 2*np.pi],
            v_range=[0, 2*np.pi],
            resolution=(12, 12),
            fill_opacity=0.2,
            fill_color=BLUE,
            stroke_width=0
        )
        
        return VGroup(carbons, hydrogens, c_c_bonds, c_h_bonds, pi_cloud_top, pi_cloud_bottom)