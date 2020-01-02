from manimlib.imports import *

class TestScene(Scene):
	CONFIG = {

	}

	def construct(self):

		g1 =VGroup(*[
			TextMobject("Text " + str((i+1)))
			for i in range(20)
			])

		g1.scale(0.5).arrange(DOWN, aligned_edge=LEFT).to_edge(UP+LEFT)
		self.add(g1[0:10])
		self.wait(2)

		rec = SurroundingRectangle(g1[0:10], buff=SMALL_BUFF)
		self.play(ShowCreation(rec))
		self.scroll(g1,10, 10)
		self.wait(2)

	def scroll(self, g, scrolls, visible_elements):
		sh_val = g[0].get_corner(UP + LEFT)[1] - g[1].get_corner(UP + LEFT)[1]
		for i in range(scrolls):
			g[visible_elements + i].next_to(g[visible_elements-1+i], DOWN, aligned_edge=LEFT)
			self.play(FadeOut(g[i], run_time=0.3), FadeIn(g[visible_elements+i]),
			g[(i + 1):(visible_elements + 1 + i)].shift, sh_val * UP, run_time=0.1)