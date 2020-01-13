from manimlib.imports import *

class Suma(Scene):
	CONFIG = {
        "camera_config": {"frame_center": 2*UP+2.5*RIGHT}
	}
	def construct(self):
		O  = np.array([0,0,0])
		v1 = np.array([3,0,0])
		v2 = np.array([2,3,0])
		v3 = v1+v2
		lv1i = TextMobject("$\\vec{B}$",color="red").shift(0.5*v1-0.5*DOWN)
		lv1f = TextMobject("$\\vec{B}$",color="red").shift(0.5*v1-0.5*DOWN+v2)
		lv2 = TextMobject("$\\vec{A}$",color="green").shift(0.5*v2+0.3*LEFT+0.3*UP)
		lv3 = TextMobject("$\\vec{A}+\\vec{B}$").shift(0.5*v3+0.3*DOWN+0.6*RIGHT)

		vec1i = Vector(v1,color="red")
		vec1id = DashedVMobject(vec1i)
		vec2i = Vector(v2,color="green")
		vec2id = DashedVMobject(vec2i)
		vec3 = Vector(v3)
		vec1fd = DashedVMobject(Vector(v1,color="red")).shift(v2)
		vec2fd = DashedVMobject(Vector(v2,color="green")).shift(v1)
		vec3d = DashedVMobject(vec3)
		self.play(ShowCreation(vec2id),ShowCreation(vec2i))
		self.play(ShowCreation(lv2))
		self.play(ShowCreation(vec1id),ShowCreation(vec1i))
		self.play(ShowCreation(lv1i))
		self.wait()
		self.play(Transform(vec1id, vec1fd))
		self.wait()
		self.play(ShowCreation(vec3),ShowCreation(lv3))
		S1 = VGroup(vec2id,vec1id,vec3d,lv3)
		S1b =VGroup(vec1i,vec2i,lv1i,lv2) 
		self.wait(2)
		self.play(ApplyMethod(S1.shift, 3*LEFT), ApplyMethod(S1b.shift, 3*RIGHT), FadeOut(vec3))
		self.wait()

	# segunda suma
		vec1i = Vector(v1,color="red").shift(3*RIGHT)
#		vec1id = DashedVMobject(vec1i)
		vec2i = Vector(v2,color="green").shift(3*RIGHT)
		vec2id = DashedVMobject(vec2i)
		lv32 = TextMobject("$\\vec{B}+\\vec{A}$").shift(0.5*v3+0.3*DOWN+0.6*RIGHT)
		#self.play(ShowCreation(vec1id))
		#self.play(ShowCreation(vec2id))
		self.play(Transform(vec2id, vec2fd.shift(3*RIGHT)))
		self.wait()
		self.play(ShowCreation(vec3.shift(3*RIGHT)),ShowCreation(lv32.shift(3*RIGHT)))
		self.wait(2)
		S2 = VGroup(S1b,vec2id,vec3)
		self.play(ApplyMethod(S1.shift, 3*RIGHT), ApplyMethod(S2.shift, 3*LEFT), ApplyMethod(lv32.shift,1*LEFT))		
		igual = TextMobject("$=$").shift(0.5*v3+0.35*DOWN+1.6*RIGHT)
		self.play(ShowCreation(igual))
		self.wait(3)