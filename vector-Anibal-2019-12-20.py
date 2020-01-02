from manimlib.imports import *

class vect(Scene): # Antiguo
	
	def construct(self):
		tr= TextMobject("Esto es un vector").shift(3*UP)
		tr2= TextMobject("en el plano cartesiano se puede representar por una matriz (1,2,0)").shift(2.9*UP)
		tr3=TextMobject("Ahora, si tenemos otro vector (-2,2,0) podemos\\\\"
		"ya sea sumarlos o restarlos").shift(2.9*DOWN)
		v1=np.array([1,2,0])
		v2=np.array([-2,2,0])
		v3=v2+v1
		v4=v1-v2
		vr1= TextMobject("$\\vec{A}$").shift(0.5*v1+0.8*RIGHT)
		vr2= TextMobject("$\\vec{B}$").shift(0.5*v2-0.8*RIGHT)
		vr3= TextMobject("$\\vec{A}+\\vec{B}$").shift(0.5*v3+0.8*RIGHT)
		vr4= TextMobject("$\\vec{A}-\\vec{B}$").shift(0.5*v4)
		
		tr2.scale(0.8)
		grid=NumberPlane()
		vec1= Vector(v1, color="green")
		vec2=Vector(v2)
		vec3= Vector(v3)
		vec4= Vector(v4)
		vec1f=Vector(v1).shift(v2)
		vec2f=Vector(-1*v2).shift(v1)
		self.play(ShowCreation(tr))
		self.wait()
		self.play(ShowCreation(vec1))
		self.play(Transform(tr,tr2)) 
		self.add(grid)
		self.play(ShowCreation(grid))
		self.play(FadeOut(vec1))
		self.play(FadeOut(tr))
		self.wait()
		self.play(ShowCreation(tr3))
		self.play(ShowCreation(vec2),FadeIn(vec1))
		self.play(ShowCreation(vr1))
		self.play(ShowCreation(vr2))
		self.play(Transform(vec1,vec1f))
		self.play(ShowCreation(vec3))
		self.play(ShowCreation(vr3))
		
		
		
		
		self.wait(2)
		
class S(Scene):  # Nuevo
	#CONFIG = {"camera_config": {"frame_center": 2*UP+3*RIGHT}}
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
		vec2f = DashedVMobject(Vector(v2,color="green")).shift(v1)
		vec32 = DashedVMobject(Vector(v3))

		self.play(ShowCreation(vec1i))
		self.play(ShowCreation(lv1i))
		self.play(ShowCreation(vec2i))
		self.play(ShowCreation(lv2))
		self.play(Transform(vec1i, vec1f),Transform(lv1i,lv1f))
		self.wait()
		self.play(ShowCreation(vec3))
		self.play(ShowCreation(lv3))
		#self.play(Transform(vec2i, vec2f))

		suma1i =  VGroup(vec1i,lv1i,vec2i,lv2,vec3,lv3)
		#VGroup(vec1i,vec1f,vec1i2,vec2i,vec2f,vec2i2,vec3, lv1i, lv2, lv1f, lv3)
		suma1i.scale(0.5)
	#	self.play(Transform(suma1i,suma1i_2))
		self.play(ApplyMethod(suma1i.to_edge, LEFT - 3.5*UP, {"buff": 1.6}))
		self.wait()
		self.play(ShowCreation(vec1i2),ShowCreation(vec2i2))
		self.play(Transform(vec2i2,vec2f))
		self.play(ShowCreation(vec32))
		self.wait()
		suma1i.scale(2)
		self.play(ApplyMethod(suma1i.to_edge, 0.15*UP + 1.3*RIGHT ,{"buff":1.6}))
		#suma1i.scale(2)
		self.wait()

