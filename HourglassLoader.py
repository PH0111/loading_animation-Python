from manim import *

class loading(Scene):
    def construct(self):
        hourglass = SVGMobject("SVGimg/hourglass.svg").scale(0.3)
        hourglass.set_color(WHITE)

        self.play(DrawBorderThenFill(hourglass))
        self.play(
            Rotate(
                hourglass,
                angle= PI,
                about_point=ORIGIN,
            )
        )
        self.play(Uncreate(hourglass))
