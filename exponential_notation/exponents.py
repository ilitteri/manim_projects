from colour import Color
from manim import *

class Exponents(Scene):

    def construct(self):
        '''
        Opening
        '''
        # Title
        title = Title(r"Potenciación", scale_factor=2)
        title.to_edge(UP)
        # self.add(title)
        self.play(Write(title))
        self.wait()

        # Overview
        overview = BulletedList(
            "Notación exponencial", 
            "Orden de las operaciones",
            "Propiedades de la potenciación", 
        )
        overview_copy = overview.copy()
        self.play(Write(overview_copy))
        self.wait()
        # Prepare for first bullet
        self.play(FadeToColor(overview_copy[0], "#E7D40A"))
        self.wait()
        exponential_notation_title = Tex(r"Notación Exponencial")
        exponential_notation_title.to_corner(LEFT+UP)
        self.play(
            FadeOutAndShift(title, UP),
            Transform(overview_copy, exponential_notation_title)
        )
        self.wait()
        self.play(FadeOut(overview_copy))

        '''
        Notación exponencial
        '''
        exp_not_explanation = VGroup(
            Tex(r"En la multiplicación, los números que son multiplicados se\\ llaman factores.").to_edge(UP),
            Tex(r"En multiplicaciones repetidas los factores son los mismos y en\\ multiplicaciones no repetidas, los factores no son los mismos.").to_edge(UP),
            Tex(r"La notación exponencial se usa para mostrar multiplicaciones\\ que repiten el mismo factor.").to_edge(UP),
            Tex(r"La notación consiste en usar un superíndice en el factor que se\\ repite, y ese superíndice indica cuántas veces se repite.").to_edge(UP),
        )
        # Escribe la primera explicación
        self.play(Write(exp_not_explanation[0]))
        self.wait()
        # Escribe la segunda explicación (transforma a la primera en la segunda)
        self.play(Transform(exp_not_explanation[0], exp_not_explanation[1]))
        self.wait()
        multiplications = VGroup(
            MathTex(r"18 \cdot 18 \cdot 18 \cdot 18", r"=", r"18^{4}"),
            MathTex(r"x \cdot x \cdot x \cdot x", r"=", r"x^{4}"),
            MathTex(r"3 \cdot 7 \cdot a", r"=", r"3 \cdot 7 \cdot a")
        )
        multiplications_bis = VGroup(
            MathTex(r"18^{2} \cdot 18^{2}", r"=", r"18^{4}"),
            MathTex(r"x^{2} \cdot x^{2}", r"=", r"x^{4}"),
            MathTex(r"3 \cdot 7 \cdot a", r"=", r"3 \cdot 7 \cdot a")
        )
        multiplications_bisbis = VGroup(
            MathTex(r"18^{4}", r"=", r"18^{4}"),
            MathTex(r"x^{4}", r"=", r"x^{4}"),
            MathTex(r"3 \cdot 7 \cdot a", r"=", r"3 \cdot 7 \cdot a")
        )
        multiplications.arrange(DOWN, buff=1)
        multiplications_bis.arrange(DOWN, buff=1)
        multiplications_bisbis.arrange(DOWN, buff=1)
        # Escribo los ejemplos
        for i in range(3):
            self.play(FadeIn(multiplications[i][0]))
        self.wait()
        # Escribe la segunda explicación (transforma a la segunda en la tercera)
        self.play(Transform(exp_not_explanation[0], exp_not_explanation[2]))
        self.wait(2)
        # Escribe la segunda explicación (transforma a la tercera en la cuarta)
        self.play(Transform(exp_not_explanation[0], exp_not_explanation[3]))
        self.wait()
        # Escribe las igualdades de los ejemplos
        for i in range(3):
            self.play(
                FadeIn(multiplications[i][1]),
                ReplacementTransform(multiplications[i][0].copy(), multiplications[i][2])
            )
            self.wait()
        # Simplifica los ejemplos
        for i in range(2):
            self.play(Transform(multiplications[i], multiplications_bis[i]))
            self.wait()
            self.play(Transform(multiplications[i], multiplications_bisbis[i]))
            self.wait()
        self.wait()
        exponential_notation = VGroup(
            Tex(r"Si x es un número real y n es un número natural, entonces"),
            MathTex(r"x^{n}", r"=", r"x \cdot x \cdot ... \cdot x").scale(2)
        )
        exponential_notation.arrange(DOWN, buff=1)
        # Desaparece lo anterios
        self.play(
            FadeOut(multiplications),
            FadeOut(exp_not_explanation[0])
        )
        self.wait()
        # Muestra la definición
        for i in range(2):
            self.play(Write(exponential_notation[i]))
            self.wait()
        brace1 = Brace(exponential_notation[1][2], DOWN, buff=SMALL_BUFF)
        t1 = brace1.get_tex(r"n \text{ factores de } x")
        # Abre una llave
        self.play(
            GrowFromCenter(brace1),
            FadeIn(t1),
        )
        self.wait()
        self.play(
            FadeOut(exponential_notation),
            FadeOut(brace1),
            FadeOut(t1)
        )
        self.wait()

        '''
        Orden de las operaciones
        '''
        op_order_explanation = BulletedList(
            r"Las operaciones dentro de paréntesis se hacen\\ desde adentro hacia afuera.",
            r"Las operaciones exponenciales se hacen de\\ izquierda a derecha.",
            r"Las multiplicaciones y divisiones se hacen\\ de izquierda a derecha.",
            r"Las sumas y restas se hacen de izquierda\\ a derecha."
        )
        op_order_examples = VGroup(
            MathTex(
                r"7 \cdot 6",
                r"-",
                r"4^{2}",
                r"+",
                r"1^{5}",
                r"&=",
                r"7 \cdot 6",
                r"-",
                r"16",
                r"+",
                r"1",
                r"\\",
                r"&=",
                r"42",
                r"-",
                r"16",
                r"+",
                r"1",
                r"\\",
                r"&=",
                r"27"
            ).scale(2),
            MathTex(
                r"(2+3)^{3}",
                r"+",
                r"7^{2}",
                r"-",
                r"3(4+1)^{2}",
                r"&=",
                r"(5)^{3}",
                r"+",
                r"7^{2}",
                r"-",
                r"3(5)^{2}",
                r"\\",
                r"&=",
                r"125",
                r"+",
                r"49",
                r"-",
                r"3(25)",
                r"\\",
                r"&=",
                r"125",
                r"+",
                r"49",
                r"-",
                r"75",
                r"\\",
                r"&=",
                r"99"
            ).scale(1.25),
            MathTex(
                r"[4(6+2)^{3}]^{2}",
                r"&=",
                r"[4(8)^{3}]^{2}",
                r"\\",
                r"&=",
                r"[4(512)]^{2}",
                r"\\",
                r"&=",
                r"[2.048]^{2}",
                r"\\",
                r"&=",
                r"4.194.304"
            ).scale(2)
        )
        self.play(Write(title))
        overview_copy = overview.copy()
        self.play(Write(overview_copy))
        self.wait()
        # Prepare for second bullet
        self.play(FadeToColor(overview_copy[1], "#E7D40A"))
        self.wait()
        exponential_notation_title = Tex(r"Orden de las operaciones")
        exponential_notation_title.to_corner(LEFT+UP)
        self.play(
            FadeOutAndShift(title, UP),
            Transform(overview_copy, exponential_notation_title)
        )
        self.wait()
        self.play(FadeOut(overview_copy))
        self.wait()
        for i in range(4):
            self.play(Write(op_order_explanation[i]))
            self.wait()
        self.wait()

        # Example 1
        self.play(
            FadeOutAndShift(op_order_explanation, UP),
            GrowFromCenter(op_order_examples[0][:6])
        )
        self.wait()
        self.play(
            ReplacementTransform(op_order_examples[0][0].copy(), op_order_examples[0][6]),
            FadeIn(op_order_examples[0][7]),
            ReplacementTransform(op_order_examples[0][2].copy(), op_order_examples[0][8]),
            FadeIn(op_order_examples[0][9]),
            ReplacementTransform(op_order_examples[0][4].copy(), op_order_examples[0][10]),
        )
        self.wait()
        self.play(
            FadeIn(op_order_examples[0][12]),
            ReplacementTransform(op_order_examples[0][6].copy(), op_order_examples[0][13]),
            FadeIn(op_order_examples[0][14]),
            ReplacementTransform(op_order_examples[0][8].copy(), op_order_examples[0][15]),
            FadeIn(op_order_examples[0][16]),
            ReplacementTransform(op_order_examples[0][10].copy(), op_order_examples[0][17]),
        )
        self.wait()
        self.play(
            FadeIn(op_order_examples[0][-2]),
            ReplacementTransform(op_order_examples[0][14:18].copy(), op_order_examples[0][-1])
        )
        self.wait()

        # Example 2
        self.play(
            FadeOutAndShift(op_order_examples[0], UP),
            Write(op_order_examples[1][:6])
        )
        self.wait()
        self.play(
            ReplacementTransform(op_order_examples[1][0].copy(), op_order_examples[1][6]),
            FadeIn(op_order_examples[1][7]),
            ReplacementTransform(op_order_examples[1][2].copy(), op_order_examples[1][8]),
            FadeIn(op_order_examples[1][9]),
            ReplacementTransform(op_order_examples[1][4].copy(), op_order_examples[1][10]),
        )
        self.wait()
        self.play(
            FadeIn(op_order_examples[1][12]),
            ReplacementTransform(op_order_examples[1][6].copy(), op_order_examples[1][13]),
            FadeIn(op_order_examples[1][14]),
            ReplacementTransform(op_order_examples[1][8].copy(), op_order_examples[1][15]),
            FadeIn(op_order_examples[1][16]),
            ReplacementTransform(op_order_examples[1][10].copy(), op_order_examples[1][17]),
        )
        self.wait()
        self.play(
            FadeIn(op_order_examples[1][19]),
            ReplacementTransform(op_order_examples[1][13].copy(), op_order_examples[1][20]),
            FadeIn(op_order_examples[1][21]),
            ReplacementTransform(op_order_examples[1][15].copy(), op_order_examples[1][22]),
            FadeIn(op_order_examples[1][23]),
            ReplacementTransform(op_order_examples[1][17].copy(), op_order_examples[1][24]),
        )
        self.wait()
        self.play(
            FadeIn(op_order_examples[1][-2]),
            ReplacementTransform(op_order_examples[1][20:25].copy(), op_order_examples[1][-1])
        )
        self.wait()
        self.play(FadeOutAndShift(op_order_examples[1]))
        self.wait()

        # Example 3
        self.play(Write(op_order_examples[2][:2]))
        self.wait()
        self.play(ReplacementTransform(op_order_examples[2][0].copy(), op_order_examples[2][2]))
        self.wait()
        for i in range(4, 11, 3):
            self.play(
                FadeIn(op_order_examples[2][i]),
                ReplacementTransform(op_order_examples[2][i-2].copy(), op_order_examples[2][i+1])
            )
            self.wait()

        