from manim import *

class loading(Scene):
    def construct(self):
        coin = SVGMobject("SVGimg/coins.svg").scale(0.3)

        self.play(DrawBorderThenFill(coin))
        self.play(coin.animate.shift(UP*0.3).set_opacity(0), rate_func = rush_from)
