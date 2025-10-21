from manim import *
import numpy as np
import random

class DualityScene(Scene):
    def construct(self):
        # ----------------
        # TITLE
        title = Text("Wave–Particle Duality of Light", font_size=48)
        self.play(FadeIn(title, shift=UP))
        self.wait(1.5)
        self.play(FadeOut(title))

        # ----------------
        # WAVE BEHAVIOR
        wave_label = Text("Wave Behavior", font_size=36).to_edge(UP)
        self.play(Write(wave_label))

        wave = FunctionGraph(lambda x: 0.5*np.sin(3*x), x_range=[-5, 5], color=BLUE)
        self.play(Create(wave))
        self.wait(1.5)
        self.play(FadeOut(wave), FadeOut(wave_label))

        # ----------------
        # PARTICLE BEHAVIOR
        particle_label = Text("Particle Behavior", font_size=36).to_edge(UP)
        self.play(Write(particle_label))

        emitter = Dot(LEFT*5, color=YELLOW)
        screen = Line(RIGHT*4+UP*2, RIGHT*4+DOWN*2)
        self.play(FadeIn(emitter), Create(screen))

        # Simulate photons hitting screen
        hits = VGroup()
        for _ in range(40):  # number of photons
            y = random.uniform(-2,2)
            photon = Dot(emitter.get_center(), color=YELLOW, radius=0.06)
            self.add(photon)
            self.play(photon.animate.move_to([4, y, 0]), run_time=0.25)
            hit = Dot([4, y, 0], radius=0.05, color=WHITE)
            hits.add(hit)
            self.remove(photon)
            self.add(hit)

        self.wait(1)
        final_text = Text("Light is both Wave and Particle", font_size=40)
        self.play(Write(final_text))
        self.wait(2)
