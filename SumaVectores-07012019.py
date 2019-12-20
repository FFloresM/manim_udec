from manimlib.imports import *

class Suma(Scene):
	def construct(self):
		O  = np.array([0,0,0])
		v1 = np.array([3,0,0])
		v2 = np.array([2,3,0])
		v3 = v1+v2
		lv1 = "$\\vec{A}$"
		lv2 = "$\\vec{B}$"
		lv3 = "$\\vec{C}=\\vec{A}+\\vec{B}$"
		labelinicialv1 = TextMobject(lv1,color="red").shift(0.5*v1-0.5*DOWN)
		labelfinalv1 = TextMobject(lv1,color="red").shift(0.5*v1-0.5*DOWN+v2)
		labelinicialv2 = TextMobject(lv2,color="green").shift(0.5*v2+0.3*LEFT+0.3*UP)
		labelsuma = TextMobject(lv3).shift(0.5*v3+0.5*DOWN+0.8*RIGHT)

		vector1 = Vector(v1,color="red")
		vector2 = Vector(v2,color="green")
		vector3 = Vector(v3)
		vector1f = Vector(v1,color="red").shift(v2)
	#	self.move_camera(0.5*LEFT)
		self.play(ShowCreation(labelinicialv1))
		self.play(ShowCreation(vector1))
		self.play(ShowCreation(labelinicialv2))
		self.play(ShowCreation(vector2))
		self.play(ShowCreation(vector3))
		self.play(Transform(vector1, vector1f),Transform(labelinicialv1,labelfinalv1),ShowCreation(labelsuma))
		self.wait()
