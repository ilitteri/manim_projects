from manim import *

class Equivalences(Scene):
    def bullet_to_opening_transition(self, law_title: Title, title: Title, overview: BulletedList, law: MathTex) -> None:
        self.play(
            FadeOutAndShift(law_title, UP),
            FadeOutAndShift(law, DOWN)
        )
        self.play(
            FadeInFrom(title, UP),
            FadeInFrom(overview, DOWN),
        )
        self.wait()
    
    def opening_to_bullet_transition(self, title: Title, overview: BulletedList, bullet_index: int) -> None:
        self.play(FadeToColor(overview[bullet_index], "#E7D40A"))
        self.wait()
        self.play(
            FadeOutAndShift(title, UP),
            FadeOutAndShift(overview, DOWN)
        )
        self.wait()
    
    def regular_bullet_transition(self, bullet_title: Title, law: MathTex, equiv_index: int, items: int) -> None:
        self.play(Write(bullet_title))
        self.wait()
        for i in range(items):
            self.play(Write(law[i][0:equiv_index]))
            self.wait()
            self.play(
                FadeIn(law[i][equiv_index]),
                ReplacementTransform(law[i][0:equiv_index].copy(), law[i][equiv_index+1:])
            )
            self.wait()
    
    def construct(self):
        title = Title("Equivalencias Lógicas", scale_factor=2).to_edge(UP)
        overview = BulletedList(
            "Leyes de Identidad",
            "Leyes de Dominación",
            "Leyes de Idempotentes",
            "Ley de la Doble Negación",
            "Leyes Conmutativas",
            "Leyes Asociativas",
            "Leyes Distributivas",
            "Leyes de De Morgan",
            "Leyes de Absorción",
            "Leyes de Negación",
            "Equivalencias lógicas sobre declaraciones condicionales",
            "Equivalencias lógicas sobre declaraciones bicondicionales"
        ).scale(.75).arrange_in_grid(n_cols=2)
        law_titles = VGroup(
            Title("Leyes de Identidad", scale_factor=2).to_edge(UP),
            Title("Leyes de Dominación", scale_factor=2).to_edge(UP),
            Title("Leyes de Idempotencia", scale_factor=2).to_edge(UP),
            Title("Ley de la Doble Negación", scale_factor=2).to_edge(UP),
            Title("Leyes Conmutativas", scale_factor=2).to_edge(UP),
            Title("Leyes Asociativas", scale_factor=2).to_edge(UP),
            Title("Leyes Distributivas", scale_factor=2).to_edge(UP),
            Title("Leyes de De Morgan", scale_factor=2).to_edge(UP),
            Title("Leyes de Absorción", scale_factor=2).to_edge(UP),
            Title("Ley de Negación", scale_factor=2).to_edge(UP),
            Title("Equivalencias lógicas sobre declaraciones condicionales").to_edge(UP),
            Title("Equivalencias lógicas sobre declaraciones bicondicionales").to_edge(UP)
        )
        identity = VGroup(
            MathTex(r"p", r"\cdot", r"1", r"\equiv", r"p").scale(2),
            MathTex(r"p", r"+", r"0", r"\equiv", r"p").scale(2)
        ).arrange(DOWN, buff=1)
        domination = VGroup(
            MathTex(r"p", r"+", r"1", r"\equiv", r"1").scale(2),
            MathTex(r"p", r"\cdot", r"0", r"\equiv", r"0").scale(2)
        ).arrange(DOWN, buff=1)
        idempotent = VGroup(
            MathTex(r"p", r"\cdot", r"p", r"\equiv", r"p").scale(2),
            MathTex(r"p", r"+", r"p", r"\equiv", r"p").scale(2)
        ).arrange(DOWN, buff=1)
        double_negation = VGroup(
            MathTex(r"(", r"p", r"'", r")", r"'", r"\equiv", r"p").scale(2)
        ).arrange(DOWN, buff=1)
        conmutative = VGroup(
            MathTex(r"p", r"+", r"q", r"\equiv", r"q", r"+", r"p").scale(2),
            MathTex(r"p", r"\cdot", r"q", r"\equiv", r"q", r"\cdot", r"p").scale(2)
        ).arrange(DOWN, buff=1)
        associative = VGroup(
            MathTex(r"(", r"p", r"+", r"q", r")", r"+", r"r", r"\equiv", r"p", r"+", r"(", r"q", r"+", r"r", r")").scale(2),
            MathTex(r"(", r"p", r"\cdot", r"q", r")", r"\cdot", r"r", r"\equiv", r"p", r"\cdot", r"(", r"q", r"\cdot", r"r", r")").scale(2)
        ).arrange(DOWN, buff=1)
        distributive = VGroup(
            MathTex(r"p", r"+", r"(", r"q", r"\cdot", r"r", r")", r"\equiv", r"(", r"p", r"+", r"q", r")", r"\cdot", r"(", r"p", r"+", r"r", r")").scale(2),
            MathTex(r"p", r"\cdot", r"(", r"q", r"+", r"r", r")", r"\equiv", r"(", r"p", r"\cdot", r"q", r")", r"+", r"(", r"p", r"\cdot", r"r", r")").scale(2)
        ).arrange(DOWN, buff=1)
        deMorgan = VGroup(
            MathTex(r"(", r"p", r"+", r"q", r")", r"'", r"\equiv", r"p", r"'", r"\cdot", r"q", r"'").scale(2),
            MathTex(r"(", r"p", r"\cdot", r"q", r")", r"'", r"\equiv", r"p", r"'", r"+", r"q", r"'").scale(2)
        ).arrange(DOWN, buff=1)
        absortion = VGroup(
            MathTex(r"p", r"+", r"(", r"p", r"\cdot", r"q", r")", r"\equiv", r"p").scale(2),
            MathTex(r"p", r"\cdot", r"(", r"p", r"+", r"q", r")", r"\equiv", r"p").scale(2)
        ).arrange(DOWN, buff=1)
        negation = VGroup(
            MathTex(r"p", r"+", r"p", r"'", r"\equiv", r"1").scale(2),
            MathTex(r"p", r"\cdot", r"p", r"'", r"\equiv", r"0").scale(2)
        ).arrange(DOWN, buff=1)
        conditional = VGroup(
            MathTex(r"p", r"\rightarrow", r"q", r"\equiv", r"p", r"'", r"+", r"q"),
			MathTex(r"p", r"\rightarrow", r"q", r"\equiv", r"q", r"'", r"+", r"p"),
			MathTex(r"p", r"+", r"q", r"\equiv", r"p", r"'", r"\rightarrow", r"q"),
			MathTex(r"p", r"\cdot", r"q", r"\equiv", r"(", r"p", r"\rightarrow", r"q", r"'", r")", r"'"),
			MathTex(r"(", r"p", r"+", r"q", r"'", r")", r"\equiv", r"p", r"\rightarrow", r"q", r"'"),
			MathTex(r"(", r"p", r"\rightarrow", r"q", r")", r"\cdot", r"(", r"p", r"\rightarrow", r"r", r")", r"\equiv", r"p", r"\rightarrow", r"(", r"q", r"\cdot", r"r", r")"),
			MathTex(r"(", r"p", r"\rightarrow", r"r", r")", r"\cdot", r"(", r"q", r"\rightarrow", r"r", r")", r"\equiv", r"(", r"p", r"+", r"q", r")", r"\rightarrow", r"r"),
			MathTex(r"(", r"p", r"\rightarrow", r"q", r")", r"+", r"(", r"p" r"\rightarrow", r"r", r")", r"\equiv", r"p", r"\rightarrow", r"(", r"q", r"+" r"r", r")"),
			MathTex(r"(", r"p", r"\rightarrow", r"r", r")", r"+", r"(", r"q", r"\rightarrow", r"r", r")", r"\equiv", r"(", r"p" r"\cdot", r"q", r")" r"\rightarrow",  r"r")
        ).arrange(DOWN, buff=.1)
        biconditional = VGroup(
            MathTex(r"p", r"\leftrightarrow", r"q", r"\equiv", r"(", r"p", r"\rightarrow", r"q", r")", r"\cdot", r"(", r"q", r"\rightarrow", r"p", r")").scale(1.25),
            MathTex(r"p", r"\leftrightarrow", r"q", r"\equiv", r"p", r"'", r"\leftrightarrow", r"q", r"'").scale(1.25),
            MathTex(r"p", r"\leftrightarrow", r"q", r"\equiv", r"(", r"p", r"\cdot", r"q", r")", r"+", r"(", r"p", r"'", r"\cdot", r"q", r"'", r")").scale(1.25),
            MathTex(r"(", r"p", r"\leftrightarrow", r"q", r")", r"'", r"\equiv", r"p", r"\leftrightarrow", r"q", r"'").scale(1.25)
        ).arrange(DOWN, buff=.8)
        ''' OPENING '''
        overview_copy = overview.copy()
        self.play(Write(title))
        self.wait()
        self.play(Write(overview_copy))
        self.wait()
        ''' OPENING -> FIRST BULLET '''
        self.opening_to_bullet_transition(title, overview_copy, 0)

        ''' FIRST BULLET '''
        self.regular_bullet_transition(law_titles[0], identity, 3, 2)
        ''' FIRST BULLET -> OPENING '''
        self.bullet_to_opening_transition(law_titles[0], title, overview_copy, identity)
        ''' OPENING -> SECOND BULLET '''
        self.opening_to_bullet_transition(title, overview_copy, 1)

        ''' SECOND BULLET '''
        self.regular_bullet_transition(law_titles[1], domination, 3, 2)
        ''' SECOND BULLET -> OPENING '''
        self.bullet_to_opening_transition(law_titles[1], title, overview_copy, domination)
        ''' OPENING -> THIRD BULLET '''
        self.opening_to_bullet_transition(title, overview_copy, 2)

        ''' THIRD BULLET '''
        self.regular_bullet_transition(law_titles[2], idempotent, 3, 2)
        ''' THIRD BULLET -> OPENING '''
        self.bullet_to_opening_transition(law_titles[2], title, overview_copy, idempotent)
        ''' OPENING -> FOURTH BULLET '''
        self.opening_to_bullet_transition(title, overview_copy, 3)

        ''' FOURTH BULLET '''
        self.regular_bullet_transition(law_titles[3], double_negation, 5, 1)
        ''' FOURTH BULLET -> OPENING '''
        self.bullet_to_opening_transition(law_titles[3], title, overview_copy, double_negation)
        ''' OPENING -> FIFTH BULLET '''
        self.opening_to_bullet_transition(title, overview_copy, 4)

        ''' FIFTH BULLET '''
        # self.regular_bullet_transition(law_titles[4], conmutative, 3, 2)
        self.play(Write(law_titles[4]))
        self.wait()
        for i in range(2):
            self.play(Write(conmutative[i][0:3]))
            self.wait()
            self.play(
                FadeIn(conmutative[i][3]),
                FadeIn(conmutative[i][5])
            )

            self.play(ReplacementTransform(conmutative[i][0].copy(), conmutative[i][6]))
            self.play(ReplacementTransform(conmutative[i][2].copy(), conmutative[i][4]))
            self.wait()
        ''' FIFTH BULLET -> OPENING '''
        self.bullet_to_opening_transition(law_titles[4], title, overview_copy, conmutative)
        ''' OPENING -> SIXTH BULLET '''
        self.opening_to_bullet_transition(title, overview_copy, 5)

        ''' SIXTH BULLET '''
        self.play(Write(law_titles[5]))
        self.wait()
        for i in range(2):
            self.play(Write(associative[i][0:7]))
            self.wait()
            self.play(
                FadeIn(associative[i][7]),
                FadeIn(associative[i][9]),
                FadeIn(associative[i][12])
            )
            self.play(ReplacementTransform(associative[i][1].copy(), associative[i][8]))
            self.play(ReplacementTransform(associative[i][3].copy(), associative[i][11]))
            self.play(ReplacementTransform(associative[i][6].copy(), associative[i][13]))
            self.play(
                ReplacementTransform(associative[i][0].copy(), associative[i][10]),
                ReplacementTransform(associative[i][4].copy(), associative[i][14])
            )
            self.wait()
        ''' SIXTH BULLET -> OPENING '''
        self.bullet_to_opening_transition(law_titles[5], title, overview_copy, associative)
        ''' OPENING -> SEVENTH BULLET '''
        self.opening_to_bullet_transition(title, overview_copy, 6)

        ''' SEVENTH BULLET '''
        self.play(Write(law_titles[6]))
        self.wait()
        for i in range(2):
            self.play(Write(distributive[i][0:7]))
            self.wait()
            self.play(FadeIn(distributive[i][7]))
            self.play(ReplacementTransform(distributive[i][0].copy(), distributive[i][9]))
            self.play(ReplacementTransform(distributive[i][1].copy(), distributive[i][10]))
            self.play(ReplacementTransform(distributive[i][3].copy(), distributive[i][11]))
            self.play(
                FadeIn(distributive[i][8]),
                FadeIn(distributive[i][12])
            )
            self.play(ReplacementTransform(distributive[i][4].copy(), distributive[i][13]))
            self.play(ReplacementTransform(distributive[i][0].copy(), distributive[i][15]))
            self.play(ReplacementTransform(distributive[i][1].copy(), distributive[i][16]))
            self.play(ReplacementTransform(distributive[i][5].copy(), distributive[i][17]))
            self.play(
                FadeIn(distributive[i][14]),
                FadeIn(distributive[i][18])
            )
            self.wait()
        ''' SEVENTH BULLET -> OPENING '''
        self.bullet_to_opening_transition(law_titles[6], title, overview_copy, distributive)
        ''' OPENING -> EIGHTH BULLET '''
        self.opening_to_bullet_transition(title, overview_copy, 7)

        ''' EIGHTH BULLET '''
        self.play(Write(law_titles[7]))
        self.wait()
        for i in range(2):
            self.play(Write(deMorgan[i][0:6]))
            self.wait()
            self.play(FadeIn(deMorgan[i][6]))
            self.play(
                ReplacementTransform(deMorgan[i][1:4].copy(), deMorgan[i][7]),
                ReplacementTransform(deMorgan[i][1:4].copy(), deMorgan[i][9:11])
            )
            self.play(ReplacementTransform(deMorgan[i][5].copy(), deMorgan[i][8]))
            self.play(ReplacementTransform(deMorgan[i][5].copy(), deMorgan[i][11]))
            self.wait()
        ''' EIGHTH BULLET -> OPENING '''
        self.bullet_to_opening_transition(law_titles[7], title, overview_copy, deMorgan)
        ''' OPENING -> NINETH BULLET '''
        self.opening_to_bullet_transition(title, overview_copy, 8)

        ''' NINETH BULLET '''
        self.regular_bullet_transition(law_titles[8], absortion, 7, 2)
        ''' NINETH BULLET -> OPENING '''
        self.bullet_to_opening_transition(law_titles[8], title, overview_copy, absortion)
        ''' OPENING -> TENTH BULLET '''
        self.opening_to_bullet_transition(title, overview_copy, 9)

        ''' TENTH BULLET '''
        self.regular_bullet_transition(law_titles[9], negation, 4, 2)
        ''' TENTH BULLET -> OPENING '''
        self.bullet_to_opening_transition(law_titles[9], title, overview_copy, negation)
        ''' OPENING -> ELEVENTH BULLET '''
        self.opening_to_bullet_transition(title, overview_copy, 10)

        ''' ELEVENTH BULLET '''
        self.play(Write(law_titles[10]))
        self.wait()
        for i in range(9):
            self.play(Write(conditional[i]))
            self.wait()
        ''' ELEVENTH BULLET -> OPENING '''
        self.bullet_to_opening_transition(law_titles[10], title, overview_copy, conditional)
        ''' OPENING -> TWELVETH BULLET '''
        self.opening_to_bullet_transition(title, overview_copy, 11)

        ''' TWELVETH BULLET '''
        self.play(Write(law_titles[11]))
        self.wait()
        for i in range(4):
            self.play(Write(biconditional[i]))
            self.wait()
        ''' ENDING '''
        self.play(
            FadeOutAndShift(law_titles[11], UP),
            FadeOutAndShift(biconditional, DOWN)
        )
        self.wait()
        github_logo = SVGMobject("../outro/github")
        github_link = Text("github.com/ilitteri")
        outro = VGroup(
            github_logo.scale(2),
            github_link
        ).arrange(DOWN, buff=1)
        self.play(
            Write(outro[0], run_time=2),
            Write(outro[1])
        )
        self.wait()