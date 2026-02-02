from manim import *

class loading(Scene):
    def construct(self):
        crs = Circle(stroke_color=WHITE, fill_color=WHITE, fill_opacity=1).scale(0.1)
        crb = Circle(stroke_color=WHITE, fill_color=WHITE, fill_opacity=1).scale(0.1)

        self.add(crs)
        self.add(crb)

        self.play(
            crs.animate.scale(1/0.1 * 0.2),
            crb.animate.scale(1/0.1 * 0.4).set_opacity(0)
        )
