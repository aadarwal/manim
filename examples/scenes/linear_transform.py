from manim import *


class LinearTransformDemo(Scene):
    def construct(self):
        title = Text("a matrix moves the whole plane", font_size=40).to_edge(UP)
        plane = NumberPlane(
            x_range=(-6, 6, 1),
            y_range=(-4, 4, 1),
            background_line_style={"stroke_opacity": 0.45},
        )

        basis_i = Arrow(ORIGIN, RIGHT * 2, buff=0, color=GREEN, stroke_width=8)
        basis_j = Arrow(ORIGIN, UP * 2, buff=0, color=BLUE, stroke_width=8)
        i_label = Text("i", font_size=30, color=GREEN).next_to(basis_i, RIGHT)
        j_label = Text("j", font_size=30, color=BLUE).next_to(basis_j, UP)
        matrix_text = Text("[[1, 0.7], [0.35, 1]]", font_size=28).to_edge(DOWN)
        transform_group = VGroup(plane, basis_i, basis_j)
        matrix = [[1, 0.7], [0.35, 1]]

        self.play(Write(title), Create(plane))
        self.play(GrowArrow(basis_i), GrowArrow(basis_j), FadeIn(i_label), FadeIn(j_label))
        self.play(FadeIn(matrix_text, shift=UP * 0.3))
        self.play(ApplyMatrix(matrix, transform_group), run_time=2.2)

        i_label.next_to(basis_i.get_end(), RIGHT)
        j_label.next_to(basis_j.get_end(), UP)
        self.play(FadeIn(Text("same grid, new coordinates", font_size=30).next_to(title, DOWN)))
        self.wait()
