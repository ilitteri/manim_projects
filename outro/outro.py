from manim import *

class Outro(Scene):
    def construct(self):
        github_logo = SVGMobject("github")
        github_link = Text("github.com/ilitteri")
        self.add_sound()
        outro = VGroup(
            github_logo.scale(2),
            github_link
        ).arrange(DOWN, buff=1)
        self.play(
            Write(outro[0], run_time=2),
            Write(outro[1])
        )
        self.wait()