from manim import *


class AttentionFlow(Scene):
    def construct(self):
        title = Text("attention routes context", font_size=40).to_edge(UP)
        tokens = ["the", "shape", "moves"]
        token_boxes = VGroup(
            *[
                RoundedRectangle(width=1.7, height=0.75, corner_radius=0.08)
                .set_stroke(WHITE, width=2)
                .set_fill(color, opacity=0.24)
                for color in (BLUE, GREEN, YELLOW)
            ]
        ).arrange(RIGHT, buff=0.55)
        token_labels = VGroup(
            *[Text(token, font_size=28).move_to(box) for token, box in zip(tokens, token_boxes)]
        )
        top = VGroup(token_boxes, token_labels).shift(UP * 1.2)

        query = RoundedRectangle(width=1.7, height=0.75, corner_radius=0.08)
        query.set_fill(RED, opacity=0.28).set_stroke(RED, width=3)
        query_label = Text("query", font_size=28).move_to(query)
        query_group = VGroup(query, query_label).shift(DOWN * 1.6)

        weights = [0.18, 0.62, 0.38]
        edges = VGroup()
        weight_labels = VGroup()
        for box, weight in zip(token_boxes, weights):
            edge = Line(query.get_top(), box.get_bottom(), color=BLUE_C)
            edge.set_stroke(width=2 + 8 * weight, opacity=0.35 + 0.55 * weight)
            edges.add(edge)
            weight_labels.add(
                Text(f"{weight:.2f}", font_size=22, color=BLUE_C).move_to(edge.get_center())
            )

        summary = Text("larger weights pull more information", font_size=28).to_edge(DOWN)

        self.play(Write(title))
        self.play(FadeIn(top, shift=DOWN * 0.3), FadeIn(query_group, shift=UP * 0.3))
        self.play(LaggedStart(*(Create(edge) for edge in edges), lag_ratio=0.15))
        self.play(FadeIn(weight_labels))
        self.play(FadeIn(summary, shift=UP * 0.2))
        self.wait()
