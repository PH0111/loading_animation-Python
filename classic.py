from manim import *

class loading(Scene):
        def construct(self):
            cr = Circle(stroke_color=ManimColor("#6A6A6A")).scale(0.4)
            dot1 = Dot(stroke_color=WHITE, fill_color=WHITE, fill_opacity=1, stroke_width=0.5).scale(0.7).shift(0.4*UP)
            dot2 = Dot(stroke_color=WHITE, fill_color=WHITE, fill_opacity=1, stroke_width=0.5).scale(0.7).shift(0.2 * DOWN + 0.35 * LEFT)
            dot3 = Dot(stroke_color=WHITE, fill_color=WHITE, fill_opacity=1, stroke_width=0.5).scale(0.7).shift(0.2 * DOWN + 0.35 * RIGHT)

            self.add(cr)
            self.add(dot1)
            self.add(dot2)
            self.add(dot3)

            self.play(
                Rotate(
                    dot1,
                    angle=PI*2,
                    about_point=cr.get_center()
                ),
                Rotate(
                    dot2,
                    angle=PI*2,
                    about_point=cr.get_center()
                ),
                Rotate(
                    dot3,
                    angle=PI*2,
                    about_point=cr.get_center()
                )
            )
