from manimlib.imports import *

class Suma(Scene):
	CONFIG = {
		"camera_config": {"frame_center": 4*RIGHT}
	}
	def construct(self):
		color = "white"
		v1 = np.array([1,0,0])
		v1_tex = TexMobject("\\vec{A}", color=color).shift(0.5*v1-0.5*DOWN)


		A = Vector(v1).shift(2*UP)
		vect1 = Vector(v1, color=color)

		v2 = v1*3
		A3 = Vector(v2).shift(2*DOWN)
		A3_tex = TexMobject("3\\vec{A}", color=color).shift(0.5*v2+1.5*DOWN)

		ec = TexMobject("\\vec{A}+\\vec{A}+\\vec{A} = 3\\vec{A}").shift(7*RIGHT)


		self.play(ShowCreation(A), ShowCreation(TexMobject("\\vec{A}").shift(0.5*v1+2.5*UP)))
	#	cvect1 = DashedVMobject(vect1)	#linea punteada
		self.play(Transform(Vector(v1).shift(2*UP),vect1))
		self.play(ShowCreation(v1_tex))
		self.play(ShowCreation(Vector(v1, color=color).shift(v1)), ShowCreation(TexMobject("\\vec{A}", color=color).shift(1.5*v1-0.5*DOWN)))
		self.play(ShowCreation(Vector(v1, color=color).shift([2,0,0])), ShowCreation(TexMobject("\\vec{A}", color=color).shift(2.5*v1-0.5*DOWN)))
		
		self.play(ShowCreation(A3), ShowCreation(A3_tex))
		self.play(ShowCreation(ec))
		self.wait(4)


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

