from manim import *


class BasicTransform(Scene):
    def construct(self):
        title = Text("shape becomes idea", font_size=42).to_edge(UP)
        square = Square(side_length=2.2, color=YELLOW).set_stroke(width=7)
        circle = Circle(radius=1.15, color=BLUE).set_fill(BLUE, opacity=0.32)
        caption = Text("Create -> Transform -> Resolve", font_size=28).to_edge(DOWN)

        self.play(Write(title))
        self.play(Create(square), FadeIn(caption, shift=UP * 0.25))
        self.play(Transform(square, circle), run_time=1.5)
        self.play(square.animate.set_fill(GREEN, opacity=0.45).scale(1.08))
        self.wait()
