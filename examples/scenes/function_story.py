from manim import *
import numpy as np


def curve(x: float) -> float:
    return 0.35 * (x - 1) * (x + 2) + 1.2 * np.sin(1.2 * x)


class FunctionStory(Scene):
    def construct(self):
        title = Text("watch one input move through a function", font_size=36).to_edge(UP)
        axes = Axes(
            x_range=(-4, 4, 1),
            y_range=(-3, 4, 1),
            x_length=8.5,
            y_length=5.5,
            tips=False,
        ).to_edge(DOWN)
        graph = axes.plot(curve, x_range=(-3.5, 3.5), color=YELLOW)
        x_tracker = ValueTracker(-3)

        moving_dot = always_redraw(
            lambda: Dot(
                axes.c2p(x_tracker.get_value(), curve(x_tracker.get_value())),
                color=BLUE,
            )
        )
        vertical = always_redraw(
            lambda: DashedLine(
                axes.c2p(x_tracker.get_value(), 0),
                axes.c2p(x_tracker.get_value(), curve(x_tracker.get_value())),
                color=BLUE,
                stroke_opacity=0.65,
            )
        )
        label = always_redraw(
            lambda: Text(
                f"x = {x_tracker.get_value():.2f}",
                font_size=26,
                color=BLUE,
            ).next_to(moving_dot, UP)
        )

        self.play(Write(title), Create(axes))
        self.play(Create(graph), run_time=1.5)
        self.add(vertical, moving_dot, label)
        self.play(x_tracker.animate.set_value(3), run_time=4, rate_func=smooth)
        self.wait()
