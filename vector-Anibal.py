from manimlib.imports import *

class vect(Scene):
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
