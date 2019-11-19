from manimlib.imports import *

class Suma(Scene):
	def construct(self):
		v1 = np.array([3,0,0])
		v2 = np.array([2,3,0])
		v3 = v1+v2

		vector1 = Vector(v1)
		vector2 = Vector(v2)
		vector3 = Vector(v3)
		vector1f = Vector(v1).shift(v2)
		self.play(ShowCreation(vector1))
		self.play(ShowCreation(vector2))
		self.play(ShowCreation(vector3))
		self.play(Transform(vector1, vector1f))
		self.wait()


class Suma_text(Scene):
	def construct(self):
		v1 = np.array([-3,3,0])
		v2 = np.array([5,0,0])
		v3 = v1+v2

		v1_tex = "\\vec{v}"
		v2_tex = "\\vec{u}"
		v3_tex = "\\vec{u}+\\vec{v}"

		v_1 = TexMobject(v1_tex, color="red").align_to((-1.5,1.5,0), (1,1,0))
		v_2 = TexMobject(v2_tex, color="blue").align_to((2.5,0,0), (1,1,0))
		v_3 = TexMobject(v3_tex).align_to((2.3,1.5,0), (1,1,0))
		

		vector1 = Vector(v1, color="red")
		vector2 = Vector(v2, color="blue")
		vector3 = Vector(v3)
		vector1t = Vector(v1).shift(v2)
		vector2t = Vector(v2).shift(v1)

		vg1 = VGroup(vector1, v_1)
		vg2 = Group(vector2, v_2)
		vg3 = Group(vector3, v_3)

		self.play(ShowCreation(vg1))
		self.play(ShowCreation(vg2))
		self.play(ShowCreation(vg3))
		self.play(Transform(Vector(v1), vector1t))
		self.play(Transform(Vector(v2), vector2t))

		self.wait()

