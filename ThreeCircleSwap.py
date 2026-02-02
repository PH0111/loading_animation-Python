from manim import *

class loading(Scene):
    def construct(self):
        crl = Circle(stroke_color=WHITE, fill_color=WHITE, fill_opacity=1).scale(0.2).shift(0.5 * LEFT)
        crm = Circle(stroke_color=WHITE, fill_color=WHITE, fill_opacity=1).scale(0.2)
        crr = Circle(stroke_color=WHITE, fill_color=WHITE, fill_opacity=1).scale(0.2).shift(0.5 * RIGHT)

        self.add(crl)
        self.add(crm)
        self.add(crr)

        self.play(
            Rotate(
                crl,
                angle=PI,
                about_point=ORIGIN
            ),
            crr.animate.move_to(ORIGIN),
            crm.animate.shift(0.5 * LEFT),
            run_time=1.3
        )
