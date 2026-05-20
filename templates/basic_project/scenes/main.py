from manim import *


class MainScene(Scene):
    def construct(self):
        title = Text("A clear visual idea").to_edge(UP)
        plane = NumberPlane(
            x_range=(-5, 5, 1),
            y_range=(-3, 3, 1),
            background_line_style={"stroke_opacity": 0.35},
        )
        dot = Dot(color=YELLOW)
        path = TracedPath(dot.get_center, stroke_color=YELLOW)

        self.play(Write(title), Create(plane))
        self.add(path, dot)
        self.play(dot.animate.move_to(RIGHT * 3 + UP), run_time=1.5)
        self.play(dot.animate.move_to(LEFT * 3 + DOWN), run_time=1.5)
        self.wait()
