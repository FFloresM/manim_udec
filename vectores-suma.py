from manimlib.imports import *

class Suma(Scene):
	def construct(self):
		O  = np.array([0,0,0])
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

