from manimlib.imports import *

class Suma(Scene):
	def construct(self):
		v1 = np.array([3,0,0])
		v1_duplicado = np.array([3,0,0])
		v1_negativo = -1*v1
		v1_multiplicado = -0.5*v1

		label_v1 = TextMobject("$\\vec{A}$",color="red").shift(0.5*v1+0.5*DOWN+2*RIGHT+2*UP)
		label_v1_duplicado = TextMobject("$\\vec{A}$",color="red").shift(0.5*v1+0.5*DOWN+2*RIGHT+2*UP)
		label_v1_negativo = TextMobject("$-\\vec{A}$").shift(0.5*v1_negativo+0.5*DOWN+2*RIGHT+2*UP)
		label_v1_multiplicado = TextMobject("$\\vec{M}=-\\frac{1}{2}\\vec{A}$").shift(0.5*v1_multiplicado+0.5*DOWN+2*RIGHT)

		texto1 = TextMobject("Sea $\\vec{A}=(3,0)$").shift(5*LEFT+3.5*UP)
		texto2 = TextMobject("Sea $c=-\\frac{1}{2}$").shift(5*LEFT+2.5*UP)
		texto3 = TextMobject("Calculemos el vector $\\vec{M}=c\\vec{A}$").shift(2*RIGHT+3.5*UP)
		texto4 = TextMobject("\\begin{eqnarray} \\vec{M} & = & c\\vec{A} \\nonumber \\\\ & = & -\\frac{1}{2}\\times \\vec{A} \\nonumber \\\\ & = & \\frac{1}{2}(-\\vec{A}) \\nonumber \\end{eqnarray} ").shift(4*LEFT+0.5*UP)
		texto5 = TextMobject("\\begin{eqnarray} \\vec{M} & = & -\\frac{1}{2} (3,0) \\nonumber \\\\ & = &  (-\\frac{3}{2},0)\\nonumber \\end{eqnarray}").shift(4*LEFT+2*DOWN)
		
		vector1 = Vector(v1,color="red").shift(2*RIGHT+2*UP)
		vector1_duplicado= Vector(v1,color="red").shift(2*RIGHT+2*UP)
		vector2 = Vector(v1_negativo).shift(2*RIGHT+2*UP)
		vector2d = DashedVMobject(vector2)
		vector3 = Vector(v1_multiplicado).shift(2*RIGHT)

		self.play(ShowCreation(texto1),ShowCreation(label_v1),ShowCreation(vector1),ShowCreation(vector1_duplicado),ShowCreation(label_v1_duplicado))
		self.wait(1)
		self.play(ShowCreation(texto2))
		self.wait(1)
		self.play(ShowCreation(texto3))
		self.wait(1)
		self.play(ShowCreation(texto4))
		self.wait(2)
		self.play(ShowCreation(texto5))
		self.wait(1)
		self.play(Transform(vector1, vector2d),Transform(label_v1,label_v1_negativo))
		self.wait(1)
		self.play(Transform(vector2d,vector3),Transform(label_v1_negativo,label_v1_multiplicado))
		self.wait()
