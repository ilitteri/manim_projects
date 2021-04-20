from manim import *
from formulas import *
from titles import *

class Radicals(Scene):

    def play_title(self, title: Title):
        self.play(Write(title))
        self.wait()

    def vanish_title(self, title: Title):
        self.play(FadeOutAndShift(title, UP))

    def play_overview(self, overview: BulletedList):
        self.play(Write(overview))
        self.wait()

    def play_opening(self, title: Title, overview: BulletedList):
        self.play_title(title)
        self.play_overview(overview)

    def vanish_opening(self, title: Title, overview: BulletedList):
        self.play(
            FadeOutAndShift(title, UP),
            FadeOutAndShift(overview, DOWN)
        )
        self.wait()

    def factorization(self):
        x = MathTex(r"x^{4}").scale(3)
        self.play(Write(x))
        self.wait()
        self.play(Transform(x, MathTex(r"x^{2} \cdot x^{2}").scale(3)))
        self.wait()

    def play_property(self, title: Title, formula: VGroup):
        # Opening
        self.play_title(title)
        self.play(Write(formula[0]))
        self.wait()
        self.play(
            FadeIn(formula[1]),
            ReplacementTransform(formula[0].copy(), formula[2])
        )
        self.wait()
        # Vanishing
        self.play(
            FadeOut(title),
            FadeOut(formula)
        )
        self.wait()

    def construct(self):
        title = Title("Propiedades de la radicación").to_edge(UP).scale(2)
        overview = BulletedList(
            "Propiedad del producto",
            "Propiedad del cociente"
        ).scale(1.5)

        self.play_opening(title, overview)
        self.vanish_opening(title, overview)

        self.play_property(PRODUCT_PROPERTY_TITLE, PRODUCT_PROPERTY_FORMULA)
        self.play_property(QUOTIENT_PROPERTY_TITLE, QUOTIENT_PROPERTY_FORMULA)