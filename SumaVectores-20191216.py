from manimlib.imports import *

class Suma(Scene):
	CONFIG = {
        "camera_config": {"frame_center": 2*UP+3*RIGHT}
	}
	def construct(self):
		O  = np.array([0,0,0])
		v1 = np.array([3,0,0])
		v2 = np.array([2,3,0])
		v3 = v1+v2
		lv1 = "$\\vec{A}$"
		lv2 = "$\\vec{B}$"
		lv3 = "$\\vec{C}=\\vec{A}+\\vec{B}$"
		lv1i = TextMobject(lv1,color="red").shift(0.5*v1-0.5*DOWN)
		lv1f = TextMobject(lv1,color="red").shift(0.5*v1-0.5*DOWN+v2)
		lv2 = TextMobject(lv2,color="green").shift(0.5*v2+0.3*LEFT+0.3*UP)
		lv3 = TextMobject(lv3).shift(0.5*v3+0.5*DOWN+0.8*RIGHT)

		vec1i = Vector(v1,color="red")
		vec1i2 = DashedVMobject(Vector(v1,color="red"))
		vec2i = Vector(v2,color="green")
		vec2i2 = DashedVMobject(Vector(v2,color="green"))
		vec3 = Vector(v3)
		vec1f = Vector(v1,color="red").shift(v2)
		vec2f = Vector(v2,color="green").shift(v1)

		self.play(ShowCreation(vec1i2),ShowCreation(vec1i))
		self.play(ShowCreation(lv1i))
		self.play(ShowCreation(vec2i2),ShowCreation(vec2i))
		self.play(ShowCreation(lv2))
		self.play(Transform(vec1i, vec1f),Transform(lv1i,lv1f))
		self.wait()
		self.play(ShowCreation(vec3))
		self.play(ShowCreation(lv3))
		self.play(Transform(vec2i, vec2f))

		suma1i = VGroup(vec1i,vec1f,vec1i2,vec2i,vec2f,vec2i2,vec3, lv1i, lv2, lv1f, lv3)
		suma1i.move_to(UP)
		self.wait()
