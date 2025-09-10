from manim import *
import numpy as np
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService
import random
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from my_manim_setup import *

class CognitiveBiasAnimation(Scene):
    def construct(self):
        # 设置背景
        self.camera.background_color = "#1a1a2e"

        # 第一部分：开场动画
        self.opening_animation()

        # 第二部分：认知偏差概述
        self.cognitive_bias_overview()

        # 第三部分：确认偏差
        self.confirmation_bias_section()

        # 第四部分：锚定效应
        self.anchoring_effect_section()

        # 第五部分：可得性启发
        self.availability_heuristic_section()

        # 第六部分：群体思维
        self.groupthink_section()

        # 第七部分：当代应用
        self.modern_applications()

        # 第八部分：如何克服
        self.overcoming_biases()

        # 结尾
        self.ending_animation()

    def opening_animation(self):
        # 标题动画
        title = Text("认知偏差", font="STSong", font_size=72, color=BLUE_B)
        subtitle = Text("决策心理学的隐形陷阱", font="STSong", font_size=36, color=BLUE_D)
        subtitle.next_to(title, DOWN, buff=0.5)

        # 创建大脑轮廓
        brain_points = [
            [-2, 0, 0], [-1.8, 1, 0], [-1, 1.5, 0], [0, 1.8, 0],
            [1, 1.5, 0], [1.8, 1, 0], [2, 0, 0], [1.8, -0.8, 0],
            [1, -1.2, 0], [0, -1.5, 0], [-1, -1.2, 0], [-1.8, -0.8, 0]
        ]
        brain = Polygon(*brain_points, color=BLUE, fill_opacity=0.3).scale(0.8)
        brain.shift(UP * 0.5)

        # 神经网络效果
        neurons = VGroup()
        for _ in range(20):
            start = np.array([random.uniform(-4, 4), random.uniform(-2, 2), 0])
            end = np.array([random.uniform(-4, 4), random.uniform(-2, 2), 0])
            neuron = Line(start, end, stroke_width=1).set_color(BLUE_E)
            neurons.add(neuron)

        self.play(
            Create(neurons, lag_ratio=0.1),
            run_time=2
        )
        self.play(
            FadeOut(neurons),
            FadeIn(brain),
            run_time=1.5
        )
        self.play(
            brain.animate.scale(0.5).shift(UP * 2),
            Write(title),
            run_time=2
        )
        self.play(Write(subtitle))
        self.wait(2)

        # 过渡动画
        self.play(
            FadeOut(title),
            FadeOut(subtitle),
            brain.animate.shift(LEFT * 5).scale(0.5),
            run_time=1.5
        )

    def cognitive_bias_overview(self):
        # 认知偏差定义
        definition_title = Text("什么是认知偏差？", font="STSong", font_size=48, color=YELLOW)
        definition_title.to_edge(UP)

        definition = Text(
            "认知偏差是人类思维中的系统性错误，\n影响我们的判断和决策过程。",
            font="STSong",
            font_size=32,
            color=WHITE
        ).center()

        self.play(Write(definition_title))
        self.play(FadeIn(definition, shift=UP))
        self.wait(2)

        # 展示大脑处理信息的过程
        info_boxes = VGroup()
        info_texts = ["信息输入", "认知处理", "决策输出"]
        colors = [GREEN, YELLOW, RED]

        for i, (text, color) in enumerate(zip(info_texts, colors)):
            box = Rectangle(width=3, height=1.5, color=color, fill_opacity=0.3)
            label = Text(text, font="STSong", font_size=24, color=color)
            label.move_to(box.get_center())
            group = VGroup(box, label)
            group.shift(RIGHT * (i - 1) * 4)
            info_boxes.add(group)

        arrows = VGroup()
        for i in range(2):
            arrow = Arrow(
                info_boxes[i].get_right(),
                info_boxes[i + 1].get_left(),
                color=WHITE,
                buff=0.1
            )
            arrows.add(arrow)

        self.play(
            FadeOut(definition),
            definition_title.animate.scale(0.8).to_corner(UL),
            run_time=1
        )

        self.play(
            *[Create(box) for box in info_boxes],
            run_time=2
        )
        self.play(
            *[Create(arrow) for arrow in arrows],
            run_time=1
        )

        # 添加偏差干扰
        bias_symbol = Text("偏差", font="STSong", font_size=28, color=RED)
        bias_arrow = CurvedArrow(
            start_point=UP * 2,
            end_point=info_boxes[1].get_top(),
            color=RED
        )
        bias_symbol.next_to(bias_arrow.get_start(), UP)

        self.play(
            Create(bias_arrow),
            Write(bias_symbol)
        )
        self.wait(2)

        # 清理场景
        self.play(
            *[FadeOut(mob) for mob in self.mobjects],
            run_time=1.5
        )

    def confirmation_bias_section(self):
        # 确认偏差标题
        title = Text("确认偏差", font="STSong", font_size=56, color=BLUE)
        subtitle = Text("Confirmation Bias", font_size=32, color=BLUE_D)
        title_group = VGroup(title, subtitle).arrange(DOWN, buff=0.3)
        title_group.to_edge(UP)

        self.play(Write(title), Write(subtitle))

        # 社交媒体例子
        phone = Rectangle(width=2, height=4, color=WHITE, fill_opacity=0.1)
        phone.shift(LEFT * 4)

        # 创建社交媒体帖子
        posts = VGroup()
        post_contents = [
            ("观点A：支持", GREEN),
            ("观点A：赞同", GREEN),
            ("观点B：反对", RED),
            ("观点A：证据", GREEN),
            ("观点B：质疑", RED),
        ]

        for i, (content, color) in enumerate(post_contents):
            post = Rectangle(width=1.8, height=0.6, color=color, fill_opacity=0.3)
            text = Text(content, font="STSong", font_size=14, color=color)
            text.move_to(post.get_center())
            post_group = VGroup(post, text)
            post_group.move_to(phone.get_center() + UP * (1.5 - i * 0.7))
            posts.add(post_group)

        self.play(Create(phone))
        self.play(
            *[FadeIn(post, shift=DOWN * 0.2) for post in posts],
            lag_ratio=0.2,
            run_time=2
        )

        # 展示选择性注意
        attention_circle = Circle(radius=1, color=YELLOW, stroke_width=4)
        attention_circle.move_to(posts[0].get_center())

        self.play(Create(attention_circle))

        # 高亮支持观点
        for i in [0, 1, 3]:
            self.play(
                attention_circle.animate.move_to(posts[i].get_center()),
                posts[i].animate.scale(1.1),
                run_time=0.8
            )
            self.wait(0.5)
            self.play(posts[i].animate.scale(1 / 1.1), run_time=0.3)

        # 忽略反对观点
        for i in [2, 4]:
            self.play(
                posts[i].animate.set_opacity(0.2),
                run_time=0.5
            )

        # 解释文本
        explanation = Text(
            "我们倾向于寻找和关注\n支持自己既有观点的信息",
            font="STSong",
            font_size=28,
            color=WHITE
        ).shift(RIGHT * 3)

        self.play(Write(explanation))
        self.wait(3)

        # 数据可视化
        self.play(
            *[FadeOut(mob) for mob in [phone, posts, attention_circle, explanation]],
            run_time=1
        )

        # 创建数据图表
        axes = Axes(
            x_range=[0, 100, 20],
            y_range=[0, 100, 20],
            x_length=6,
            y_length=4,
            axis_config={"color": WHITE},
        ).shift(DOWN * 0.5)

        x_label = Text("接触信息量", font="STSong", font_size=20)
        y_label = Text("认同程度", font="STSong", font_size=20)
        x_label.next_to(axes.x_axis, DOWN)
        y_label.rotate(PI / 2).next_to(axes.y_axis, LEFT)

        # 创建两条曲线
        support_curve = axes.plot(
            lambda x: 80 + 0.15 * x,
            x_range=[0, 100],
            color=GREEN
        )
        oppose_curve = axes.plot(
            lambda x: 20 - 0.1 * x,
            x_range=[0, 100],
            color=RED
        )

        support_label = Text("支持信息", font="STSong", font_size=16, color=GREEN)
        oppose_label = Text("反对信息", font="STSong", font_size=16, color=RED)
        support_label.next_to(support_curve.get_end(), RIGHT)
        oppose_label.next_to(oppose_curve.get_end(), RIGHT)

        self.play(
            Create(axes),
            Write(x_label),
            Write(y_label)
        )
        self.play(
            Create(support_curve),
            Create(oppose_curve),
            Write(support_label),
            Write(oppose_label)
        )

        # 添加数据点
        data_points = VGroup()
        for _ in range(20):
            x = random.uniform(20, 80)
            y_support = 80 + 0.15 * x + random.uniform(-5, 5)
            point = Dot(axes.c2p(x, y_support), color=GREEN, radius=0.05)
            data_points.add(point)

        for _ in range(5):
            x = random.uniform(20, 80)
            y_oppose = 20 - 0.1 * x + random.uniform(-5, 5)
            point = Dot(axes.c2p(x, y_oppose), color=RED, radius=0.05)
            data_points.add(point)

        self.play(
            *[Create(point) for point in data_points],
            lag_ratio=0.05,
            run_time=2
        )

        self.wait(3)

        # 过渡到下一部分
        self.play(
            *[FadeOut(mob) for mob in self.mobjects],
            run_time=1.5
        )

    def anchoring_effect_section(self):
        # 锚定效应标题
        title = Text("锚定效应", font="STSong", font_size=56, color=PURPLE)
        subtitle = Text("Anchoring Effect", font_size=32, color=PURPLE_D)
        title_group = VGroup(title, subtitle).arrange(DOWN, buff=0.3)
        title_group.to_edge(UP)

        self.play(Write(title), Write(subtitle))

        # 价格实验演示
        experiment_title = Text("价格判断实验", font="STSong", font_size=36, color=YELLOW)
        experiment_title.shift(UP * 2)

        self.play(Write(experiment_title))

        # 创建两组实验
        group_a = VGroup()
        group_b = VGroup()

        # A组：高锚定
        anchor_a = Text("这款手表原价", font="STSong", font_size=24)
        price_a = Text("¥9999", font_size=48, color=RED)
        question_a = Text("您愿意支付多少？", font="STSong", font_size=24)

        group_a.add(anchor_a, price_a, question_a)
        group_a.arrange(DOWN, buff=0.5)
        group_a.shift(LEFT * 3.5)

        # B组：低锚定
        anchor_b = Text("这款手表原价", font="STSong", font_size=24)
        price_b = Text("¥999", font_size=48, color=GREEN)
        question_b = Text("您愿意支付多少？", font="STSong", font_size=24)

        group_b.add(anchor_b, price_b, question_b)
        group_b.arrange(DOWN, buff=0.5)
        group_b.shift(RIGHT * 3.5)

        # 分隔线
        divider = Line(UP * 2, DOWN * 2, color=WHITE, stroke_width=2)

        self.play(
            Create(divider),
            FadeIn(group_a, shift=RIGHT * 0.5),
            FadeIn(group_b, shift=LEFT * 0.5)
        )
        self.wait(2)

        # 显示结果
        result_a = Text("平均出价：¥5500", font="STSong", font_size=28, color=ORANGE)
        result_b = Text("平均出价：¥1200", font="STSong", font_size=28, color=ORANGE)

        result_a.next_to(group_a, DOWN, buff=0.8)
        result_b.next_to(group_b, DOWN, buff=0.8)

        self.play(
            Write(result_a),
            Write(result_b)
        )
        self.wait(2)

        # 清理并展示原理
        self.play(
            *[FadeOut(mob) for mob in [experiment_title, group_a, group_b, divider, result_a, result_b]],
            run_time=1
        )

        # 锚定效应原理图
        anchor = Circle(radius=0.3, color=RED, fill_opacity=0.8)
        anchor_label = Text("锚", font="STSong", font_size=24, color=WHITE)
        anchor_label.move_to(anchor.get_center())
        anchor_group = VGroup(anchor, anchor_label)
        anchor_group.shift(LEFT * 5)

        # 创建判断范围
        judgment_line = Line(LEFT * 3, RIGHT * 3, color=WHITE)
        judgment_line.shift(DOWN)

        # 标记点
        points = VGroup()
        labels = VGroup()
        values = [1000, 3000, 5000, 7000, 9000]
        for i, val in enumerate(values):
            point = Dot(judgment_line.point_from_proportion(i / 4), radius=0.1)
            label = Text(f"¥{val}", font_size=16)
            label.next_to(point, DOWN)
            points.add(point)
            labels.add(label)

        self.play(
            Create(anchor_group),
            Create(judgment_line),
            *[Create(p) for p in points],
            *[Write(l) for l in labels]
        )

        # 展示锚定影响
        influence_arrow = CurvedArrow(
            anchor_group.get_right(),
            points[3].get_top() + UP * 0.5,
            color=YELLOW
        )

        self.play(Create(influence_arrow))

        # 创建分布曲线
        curve1 = FunctionGraph(
            lambda x: 2 * np.exp(-((x - 1) ** 2) / 0.5),
            x_range=[-3, 3],
            color=BLUE
        ).shift(DOWN + RIGHT * 1)

        curve2 = FunctionGraph(
            lambda x: 2 * np.exp(-((x + 1) ** 2) / 0.5),
            x_range=[-3, 3],
            color=GREEN
        ).shift(DOWN + LEFT * 1)

        self.play(
            Create(curve1),
            Create(curve2)
        )

        # 添加说明
        explanation = Text(
            "初始锚定值会显著影响\n我们的最终判断",
            font="STSong",
            font_size=28,
            color=WHITE
        ).shift(UP * 2 + RIGHT * 2)

        self.play(Write(explanation))
        self.wait(3)

        # 清理场景
        self.play(
            *[FadeOut(mob) for mob in self.mobjects],
            run_time=1.5
        )

    def availability_heuristic_section(self):
        # 可得性启发标题
        title = Text("可得性启发", font="STSong", font_size=56, color=GREEN)
        subtitle = Text("Availability Heuristic", font_size=32, color=GREEN_D)
        title_group = VGroup(title, subtitle).arrange(DOWN, buff=0.3)
        title_group.to_edge(UP)

        self.play(Write(title), Write(subtitle))

        # 新闻媒体示例
        news_title = Text("为什么我们高估某些风险？", font="STSong", font_size=36, color=YELLOW)
        news_title.shift(UP * 2)

        self.play(Write(news_title))

        # 创建新闻框架
        news_frames = VGroup()
        news_data = [
            ("飞机失事", "1/1,100万", RED, 3),
            ("车祸", "1/5,000", ORANGE, 1),
            ("心脏病", "1/6", YELLOW, 0.5),
        ]

        for i, (event, prob, color, media_size) in enumerate(news_data):
            # 新闻框
            frame = Rectangle(width=4, height=2, color=color, fill_opacity=0.2)
            event_text = Text(event, font="STSong", font_size=24, color=color)
            prob_text = Text(f"实际概率：{prob}", font="STSong", font_size=18)

            news_group = VGroup(frame, event_text, prob_text)
            event_text.move_to(frame.get_center() + UP * 0.3)
            prob_text.move_to(frame.get_center() + DOWN * 0.3)

            news_group.shift(LEFT * 4 + DOWN * (i - 1) * 2.5)
            news_frames.add(news_group)

        self.play(
            *[FadeIn(frame, shift=RIGHT) for frame in news_frames],
            lag_ratio=0.3,
            run_time=2
        )

        # 媒体报道量可视化
        media_bars = VGroup()
        bar_heights = [3, 1, 0.5]

        for i, (height, color) in enumerate(zip(bar_heights, [RED, ORANGE, YELLOW])):
            bar = Rectangle(width=1, height=height, color=color, fill_opacity=0.6)
            bar.shift(RIGHT * 2 + RIGHT * i * 1.5 + DOWN * (1.5 - height / 2))
            media_bars.add(bar)

        media_label = Text("媒体报道量", font="STSong", font_size=20)
        media_label.next_to(media_bars, UP)

        self.play(
            Write(media_label),
            *[GrowFromEdge(bar, DOWN) for bar in media_bars],
            run_time=2
        )

        # 感知风险 vs 实际风险
        self.wait(2)
        self.play(
            *[FadeOut(mob) for mob in [news_frames, media_bars, media_label, news_title]],
            run_time=1
        )

        # 创建对比图表
        perception_title = Text("感知风险 vs 实际风险", font="STSong", font_size=32, color=WHITE)
        perception_title.shift(UP * 2.5)

        self.play(Write(perception_title))

        # 创建散点图
        axes = Axes(
            x_range=[0, 10, 2],
            y_range=[0, 10, 2],
            x_length=6,
            y_length=6,
            axis_config={"color": WHITE},
        )

        x_label = Text("实际风险", font="STSong", font_size=20)
        y_label = Text("感知风险", font="STSong", font_size=20)
        x_label.next_to(axes.x_axis, DOWN)
        y_label.rotate(PI / 2).next_to(axes.y_axis, LEFT)

        # 理想线（y=x）
        ideal_line = axes.plot(lambda x: x, x_range=[0, 10], color=GRAY, stroke_width=2)

        # 实际数据点
        risk_points = [
            (8, 9, "飞机", RED),
            (5, 3, "车祸", ORANGE),
            (2, 1, "心脏病", YELLOW),
            (1, 6, "恐怖袭击", PURPLE),
            (7, 4, "癌症", BLUE),
        ]

        dots = VGroup()
        dot_labels = VGroup()

        for x, y, label, color in risk_points:
            dot = Dot(axes.c2p(x, y), color=color, radius=0.1)
            text = Text(label, font="STSong", font_size=14, color=color)
            text.next_to(dot, UR, buff=0.1)
            dots.add(dot)
            dot_labels.add(text)

        self.play(
            Create(axes),
            Write(x_label),
            Write(y_label),
            Create(ideal_line)
        )

        self.play(
            *[Create(dot) for dot in dots],
            *[Write(label) for label in dot_labels],
            lag_ratio=0.2,
            run_time=3
        )

        # 添加解释
        explanation = Text(
            "容易回忆的事件\n被认为更可能发生",
            font="STSong",
            font_size=24,
            color=WHITE
        ).to_corner(UR)

        self.play(Write(explanation))
        self.wait(3)

        # 清理场景
        self.play(
            *[FadeOut(mob) for mob in self.mobjects],
            run_time=1.5
        )

    def groupthink_section(self):
        # 群体思维标题
        title = Text("群体思维", font="STSong", font_size=56, color=ORANGE)
        subtitle = Text("Groupthink", font_size=32, color=ORANGE)
        title_group = VGroup(title, subtitle).arrange(DOWN, buff=0.3)
        title_group.to_edge(UP)

        self.play(Write(title), Write(subtitle))

        # 创建群体决策场景
        # 中心人物
        center_person = Circle(radius=0.4, color=BLUE, fill_opacity=0.8)
        center_label = Text("领导", font="STSong", font_size=16, color=WHITE)
        center_label.move_to(center_person.get_center())
        leader = VGroup(center_person, center_label)

        # 周围成员
        members = VGroup()
        member_positions = [
            (2, 1), (2, -1), (1.5, 2), (-1.5, 2),
            (-2, 1), (-2, -1), (0, -2)
        ]

        for i, (x, y) in enumerate(member_positions):
            member = Circle(radius=0.3, color=GRAY, fill_opacity=0.5)
            member.shift(RIGHT * x + UP * y)
            members.add(member)

        self.play(
            Create(leader),
            *[Create(member) for member in members],
            run_time=2
        )

        # 展示意见同化过程
        # 领导发表意见
        opinion_bubble = Ellipse(width=2, height=1, color=BLUE, fill_opacity=0.2)
        opinion_text = Text("方案A", font="STSong", font_size=20, color=BLUE)
        opinion_bubble.next_to(leader, UR)
        opinion_text.move_to(opinion_bubble.get_center())

        self.play(
            Create(opinion_bubble),
            Write(opinion_text)
        )

        # 成员逐渐同化
        agreement_bubbles = VGroup()
        for i, member in enumerate(members):
            bubble = Ellipse(width=1.5, height=0.8, color=BLUE, fill_opacity=0.2)
            text = Text("同意", font="STSong", font_size=16, color=BLUE)
            bubble.next_to(member, UP, buff=0.1)
            text.move_to(bubble.get_center())
            agreement_bubbles.add(VGroup(bubble, text))

        # 展示压力效应
        pressure_arrows = VGroup()
        for member in members:
            arrow = Arrow(
                leader.get_center(),
                member.get_center(),
                color=RED,
                stroke_width=2,
                buff=0.5
            )
            pressure_arrows.add(arrow)

        self.play(
            *[Create(arrow) for arrow in pressure_arrows],
            lag_ratio=0.1,
            run_time=2
        )

        # 成员变色表示同化
        self.play(
            *[member.animate.set_color(BLUE).set_fill_opacity(0.8) for member in members],
            *[FadeIn(bubble) for bubble in agreement_bubbles],
            lag_ratio=0.1,
            run_time=3
        )

        # 显示后果
        self.wait(2)
        self.play(
            *[FadeOut(mob) for mob in [opinion_bubble, opinion_text, agreement_bubbles, pressure_arrows]],
            run_time=1
        )

        # 群体思维的危害
        consequences = VGroup()
        consequence_texts = [
            "缺乏批判性思考",
            "忽视替代方案",
            "过度自信",
            "决策质量下降"
        ]

        for i, text in enumerate(consequence_texts):
            consequence = Text(text, font="STSong", font_size=24, color=RED)
            consequence.shift(DOWN * 3 + RIGHT * (i - 1.5) * 3)
            consequences.add(consequence)

        self.play(
            *[Write(consequence) for consequence in consequences],
            lag_ratio=0.3,
            run_time=3
        )

        self.wait(3)

        # 清理场景
        self.play(
            *[FadeOut(mob) for mob in self.mobjects],
            run_time=1.5
        )

    def modern_applications(self):
        # 当代应用标题
        title = Text("认知偏差在数字时代", font="STSong", font_size=48, color=TEAL)
        title.to_edge(UP)

        self.play(Write(title))

        # 算法推荐系统
        algorithm_title = Text("算法推荐与信息茧房", font="STSong", font_size=36, color=YELLOW)
        algorithm_title.shift(UP * 2)

        self.play(Write(algorithm_title))

        # 创建用户和内容网络
        user = Circle(radius=0.5, color=BLUE, fill_opacity=0.8)
        user_label = Text("用户", font="STSong", font_size=20, color=WHITE)
        user_label.move_to(user.get_center())
        user_group = VGroup(user, user_label)

        # 内容节点
        content_nodes = VGroup()
        content_types = [
            ("科技", BLUE, (-3, 2)),
            ("娱乐", RED, (-3, 0)),
            ("体育", GREEN, (-3, -2)),
            ("政治", PURPLE, (3, 2)),
            ("教育", ORANGE, (3, 0)),
            ("艺术", PINK, (3, -2))
        ]

        for content, color, pos in content_types:
            node = Circle(radius=0.4, color=color, fill_opacity=0.5)
            label = Text(content, font="STSong", font_size=16, color=color)
            node.shift(RIGHT * pos[0] + UP * pos[1])
            label.move_to(node.get_center())
            content_nodes.add(VGroup(node, label))

        self.play(
            Create(user_group),
            *[Create(node) for node in content_nodes],
            run_time=2
        )

        # 显示用户偏好
        preference_lines = VGroup()
        preferred_indices = [0, 1]  # 科技和娱乐

        for i in preferred_indices:
            line = Line(
                user.get_center(),
                content_nodes[i][0].get_center(),
                color=content_nodes[i][0].get_color(),
                stroke_width=4
            )
            preference_lines.add(line)

        self.play(
            *[Create(line) for line in preference_lines],
            run_time=1
        )

        # 算法强化效果
        reinforcement_circles = VGroup()
        for i in preferred_indices:
            for j in range(3):
                circle = Circle(
                    radius=0.1 + j * 0.1,
                    color=content_nodes[i][0].get_color(),
                    stroke_opacity=0.5 - j * 0.15
                ).move_to(content_nodes[i][0].get_center())
                reinforcement_circles.add(circle)

        self.play(
            *[Create(circle) for circle in reinforcement_circles],
            lag_ratio=0.1,
            run_time=2
        )

        # 其他内容逐渐消失
        non_preferred_indices = [2, 3, 4, 5]
        self.play(
            *[content_nodes[i].animate.set_opacity(0.2) for i in non_preferred_indices],
            run_time=2
        )

        # 信息茧房效果
        cocoon = Ellipse(
            width=5,
            height=3,
            color=YELLOW,
            stroke_width=3,
            fill_opacity=0.1
        ).move_to(user.get_center())

        cocoon_label = Text("信息茧房", font="STSong", font_size=24, color=YELLOW)
        cocoon_label.next_to(cocoon, DOWN)

        self.play(
            Create(cocoon),
            Write(cocoon_label)
        )

        self.wait(2)

        # 清理并转到社交媒体回音室
        self.play(
            *[FadeOut(mob) for mob in self.mobjects if mob != title],
            run_time=1
        )

        # 社交媒体回音室
        echo_title = Text("社交媒体回音室效应", font="STSong", font_size=36, color=YELLOW)
        echo_title.shift(UP * 2)

        self.play(Write(echo_title))

        # 创建社交网络
        network_nodes = VGroup()
        positions = [
            (0, 0), (2, 1), (2, -1), (-2, 1), (-2, -1),
            (0, 2), (0, -2), (3, 0), (-3, 0)
        ]

        # 创建节点
        for i, pos in enumerate(positions):
            node = Dot(point=RIGHT * pos[0] + UP * pos[1], radius=0.15, color=BLUE)
            network_nodes.add(node)

        # 创建连接
        connections = VGroup()
        connection_pairs = [
            (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6),
            (1, 2), (1, 5), (3, 4), (3, 5), (2, 6), (4, 6),
            (1, 7), (3, 8)
        ]

        for i, j in connection_pairs:
            line = Line(
                network_nodes[i].get_center(),
                network_nodes[j].get_center(),
                stroke_width=1,
                color=GRAY
            )
            connections.add(line)

        self.play(
            *[Create(node) for node in network_nodes],
            *[Create(line) for line in connections],
            run_time=3
        )

        # 观点传播动画
        opinion_wave = VGroup()
        center_opinion = Circle(radius=0.3, color=RED, fill_opacity=0.8)
        center_opinion.move_to(network_nodes[0].get_center())

        self.play(Create(center_opinion))

        # 观点扩散
        for distance in [1, 2]:
            wave_nodes = []
            if distance == 1:
                wave_nodes = [1, 2, 3, 4, 5, 6]
            else:
                wave_nodes = [7, 8]

            self.play(
                *[network_nodes[i].animate.set_color(RED) for i in wave_nodes],
                *[connections[j].animate.set_color(RED) for j in range(len(connections))
                  if any(pair[0] in wave_nodes or pair[1] in wave_nodes
                         for pair in [connection_pairs[j]])],
                run_time=1.5
            )

        # 添加统计数据
        stats_box = Rectangle(width=4, height=2, color=WHITE, fill_opacity=0.1)
        stats_box.to_corner(DR)

        stats_text = Text(
            "相似观点暴露：85%\n不同观点暴露：15%",
            font="STSong",
            font_size=20,
            color=WHITE
        ).move_to(stats_box.get_center())

        self.play(
            Create(stats_box),
            Write(stats_text)
        )

        self.wait(3)

        # 清理场景
        self.play(
            *[FadeOut(mob) for mob in self.mobjects],
            run_time=1.5
        )

    def overcoming_biases(self):
        # 克服偏差标题
        title = Text("如何克服认知偏差", font="STSong", font_size=48, color=GREEN)
        title.to_edge(UP)

        self.play(Write(title))

        # 策略列表
        strategies = VGroup()
        strategy_data = [
            ("1. 意识到偏差的存在", "认识到自己可能存在偏差"),
            ("2. 寻求多元观点", "主动接触不同意见"),
            ("3. 系统性思考", "使用结构化决策方法"),
            ("4. 数据驱动", "依靠客观数据而非直觉"),
            ("5. 反思与复盘", "定期审视自己的决策")
        ]

        for i, (strategy, description) in enumerate(strategy_data):
            # 策略标题
            strategy_text = Text(strategy, font="STSong", font_size=28, color=YELLOW)
            strategy_text.shift(LEFT * 3 + DOWN * (i * 1.2 - 1.5))

            # 描述文本
            desc_text = Text(description, font="STSong", font_size=20, color=WHITE)
            desc_text.next_to(strategy_text, RIGHT, buff=1)

            strategy_group = VGroup(strategy_text, desc_text)
            strategies.add(strategy_group)

        # 逐个展示策略
        for strategy in strategies:
            self.play(
                Write(strategy[0]),
                FadeIn(strategy[1], shift=RIGHT),
                run_time=1.5
            )
            self.wait(0.5)

        self.wait(2)

        # 创建决策框架图
        self.play(
            strategies.animate.scale(0.6).to_corner(UL),
            run_time=1
        )

        # 决策框架
        framework_title = Text("结构化决策框架", font="STSong", font_size=32, color=BLUE)
        framework_title.shift(RIGHT * 2 + UP * 2)

        self.play(Write(framework_title))

        # 创建流程图
        steps = VGroup()
        step_names = ["识别问题", "收集信息", "生成方案", "评估选项", "做出决策", "反馈学习"]

        for i, name in enumerate(step_names):
            if i < 3:
                x = -2 + i * 2
                y = 0
            else:
                x = 2 - (i - 3) * 2
                y = -2

            step = Rectangle(width=1.8, height=0.8, color=BLUE, fill_opacity=0.3)
            step.shift(RIGHT * x + UP * y)

            label = Text(name, font="STSong", font_size=16, color=WHITE)
            label.move_to(step.get_center())

            step_group = VGroup(step, label)
            steps.add(step_group)

        # 连接箭头
        arrows = VGroup()
        arrow_paths = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 0)]

        for i, j in arrow_paths:
            if j == 0:  # 回到起点的箭头
                arrow = CurvedArrow(
                    steps[i].get_center(),
                    steps[j].get_center(),
                    angle=-TAU / 4,
                    color=GREEN
                )
            else:
                arrow = Arrow(
                    steps[i].get_center(),
                    steps[j].get_center(),
                    buff=0.4,
                    color=GREEN
                )
            arrows.add(arrow)

        self.play(
            *[Create(step) for step in steps],
            run_time=2
        )
        self.play(
            *[Create(arrow) for arrow in arrows],
            lag_ratio=0.2,
            run_time=3
        )

        # 强调关键点
        key_points = VGroup()
        key_point_texts = [
            "多角度思考",
            "客观数据",
            "持续改进"
        ]

        for i, text in enumerate(key_point_texts):
            point = Text(text, font="STSong", font_size=20, color=ORANGE)
            point.shift(RIGHT * 4 + DOWN * (i * 0.8))
            key_points.add(point)

        self.play(
            *[Write(point) for point in key_points],
            lag_ratio=0.3,
            run_time=2
        )

        self.wait(3)

        # 清理场景
        self.play(
            *[FadeOut(mob) for mob in self.mobjects],
            run_time=1.5
        )

    def ending_animation(self):
        # 总结标题
        title = Text("认知偏差：了解、识别、克服", font="STSong", font_size=48, color=GOLD)
        title.to_edge(UP)

        self.play(Write(title))

        # 核心信息
        core_messages = VGroup()
        messages = [
            "认知偏差是人类思维的固有特征",
            "在数字时代，偏差可能被算法放大",
            "意识和方法可以帮助我们做出更好的决策"
        ]

        for i, message in enumerate(messages):
            text = Text(message, font="STSong", font_size=32, color=WHITE)
            text.shift(DOWN * (i * 1.5 - 0.5))
            core_messages.add(text)

        for message in core_messages:
            self.play(
                Write(message),
                run_time=2
            )
            self.wait(1)

        # 创建大脑和光芒效果
        brain_outline = self.create_brain_outline()
        brain_outline.scale(1.5).shift(DOWN * 0.5)

        # 光芒效果
        rays = VGroup()
        for i in range(12):
            angle = i * TAU / 12
            start = brain_outline.get_center() + 0.8 * np.array([np.cos(angle), np.sin(angle), 0])
            end = brain_outline.get_center() + 2 * np.array([np.cos(angle), np.sin(angle), 0])
            ray = Line(start, end, color=YELLOW, stroke_width=3)
            rays.add(ray)

        self.play(
            FadeOut(core_messages),
            FadeIn(brain_outline),
            run_time=1
        )

        self.play(
            *[Create(ray) for ray in rays],
            brain_outline.animate.set_color(GOLD),
            lag_ratio=0.1,
            run_time=2
        )

        # 最终信息
        final_message = Text(
            "理性思考，明智决策",
            font="STSong",
            font_size=40,
            color=WHITE
        ).next_to(brain_outline, DOWN, buff=1)

        self.play(Write(final_message))

        # 淡出效果
        self.play(
            *[mob.animate.set_opacity(0.3) for mob in self.mobjects],
            run_time=2
        )

        # 感谢观看
        thanks = Text("感谢观看", font="STSong", font_size=56, color=WHITE)
        thanks.set_opacity(0)

        self.play(
            thanks.animate.set_opacity(1),
            run_time=2
        )

        self.wait(3)

    def create_brain_outline(self):
        """创建大脑轮廓"""
        points = [
            [-2, 0, 0], [-1.8, 1, 0], [-1, 1.5, 0], [0, 1.8, 0],
            [1, 1.5, 0], [1.8, 1, 0], [2, 0, 0], [1.8, -0.8, 0],
            [1, -1.2, 0], [0, -1.5, 0], [-1, -1.2, 0], [-1.8, -0.8, 0]
        ]
        return Polygon(*points, color=BLUE, fill_opacity=0.3, stroke_width=3)

    # 渲染命令
    if __name__ == "__main__":
        scene = CognitiveBiasAnimation()