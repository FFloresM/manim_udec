from manimlib.imports import *

class Suma(Scene):
	def construct(self):
		v1 = np.array([3,0,0])
		v1_duplicado = np.array([3,0,0])
		vmult = -1*v1
		label_v1 = "$\\vec{A}$"
		label_vmult = "$\\vec{M}=-\\vec{A}$"
		label_inicialv1 = TextMobject(label_v1,color="red").shift(0.5*v1+0.5*DOWN+2*RIGHT)
		label_multi = TextMobject(label_vmult).shift(0.5*vmult+0.5*DOWN+2*RIGHT)
		texto1 = TextMobject("Sea $\\vec{A}=(3,0)$").shift(5*LEFT+3*UP)
		texto2 = TextMobject("Sea $c=-1$").shift(5*LEFT+2*UP)
		texto3 = TextMobject("Calculemos el vector $\\vec{M}=c\\vec{A}$").shift(2*RIGHT+3.5*UP)
		texto4 = TextMobject("\\begin{eqnarray} \\vec{M} & = & c\\vec{A} \\nonumber \\\\ & = & -1\\times (3,0) \\nonumber \\\\ & = & (-3,0) \\nonumber \\\\ & = & -\\vec{A} \\nonumber \\end{eqnarray} ").shift(4*LEFT+1*DOWN)

		vector1 = Vector(v1,color="red").shift(2*RIGHT)
		vector1_duplicado= Vector(v1,color="red").shift(2*RIGHT)
		vector3 = Vector(vmult).shift(2*RIGHT)

		self.play(ShowCreation(texto1),ShowCreation(label_inicialv1),ShowCreation(vector1),ShowCreation(vector1_duplicado))
		self.play(ShowCreation(texto2))
		self.wait(1)
		self.play(ShowCreation(texto3))
		self.wait(1)
		self.play(ShowCreation(texto4))
		self.wait(1)
		self.play(Transform(vector1, vector3),Transform(label_inicialv1,label_multi))
		self.wait()
