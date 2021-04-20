from manim import *

PRODUCT_PROPERTY_FORMULA = VGroup(
    MathTex(r"\sqrt{x \cdot y}}"),
    MathTex(r"="),
    MathTex(r"\sqrt x \cdot \sqrt y")
).arrange(RIGHT).scale(2)

QUOTIENT_PROPERTY_FORMULA = VGroup(
    MathTex(r"\sqrt{\frac{x}{y}}"),
    MathTex(r"="),
    MathTex(r"\frac{\sqrt x}{\sqrt y}")
).arrange(RIGHT).scale(2)