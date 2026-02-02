from manim import *

class loading(Scene):
    def construct(self):
        wifi = SVGMobject("SVGimg/wifi.svg").scale(0.3)
        wifi.set_color(WHITE)
        wifi.set_fill(WHITE)
        wifi.set_opacity(1)


        self.play(DrawBorderThenFill(wifi))
        self.play(wifi.animate.shift(UP*0.2).set_opacity(0))
