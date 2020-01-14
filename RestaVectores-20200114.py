from manimlib.imports import *

class Resta(Scene):
	CONFIG = {
        "camera_config": {"frame_center": 2*UP+1*RIGHT}
	}
	def construct(self):
		O  = np.array([0,0,0])
		vB = np.array([3,0,0])
		vA = np.array([2,3,0])
		vmB = -vB
		vR = vA-vB
		lvB = TextMobject("$\\vec{B}$",color="red").shift(0.5*vB-0.5*DOWN)
		lvB2 = TextMobject("$\\vec{B}$",color="red").shift(0.5*vB-0.5*DOWN)
		lvmB = TextMobject("$-\\vec{B}$",color="red").shift(-0.5*vB-0.5*DOWN)
		lvA = TextMobject("$\\vec{A}$",color="green").shift(0.5*vA+0.3*LEFT+0.3*UP)
		lvR1 = TextMobject("$\\vec{A}+(-\\vec{B})$").shift(0.5*vR+0.3*DOWN+1.1*LEFT)
		lvR2 = TextMobject("$\\vec{A}-\\vec{B}$").shift(0.5*vR+0.3*DOWN+vB+1*RIGHT)

		vecB = Vector(vB,color="red")
		vecBd = DashedVMobject(vecB)
		vecAi = Vector(vA,color="green")
		vecR = Vector(vR)
		vecmBd = DashedVMobject(Vector(vmB,color="red"))
		vecBd = DashedVMobject(Vector(vB,color="red"))
		vecRd = DashedVMobject(vecR)
		self.play(ShowCreation(vecAi))
		self.play(ShowCreation(lvA))
		self.play(ShowCreation(vecBd),ShowCreation(vecB))
		self.play(ShowCreation(lvB),ShowCreation(lvB2))
		self.wait(2)
		self.play(Transform(vecBd, vecmBd),Transform(lvB, lvmB))
		self.wait(2)
		self.play(ApplyMethod(vecBd.shift, vA),ApplyMethod(lvB.shift, vA))
		self.play(ShowCreation(vecR))
		self.play(ShowCreation(lvR1))
		self.wait(2)
		self.play(ApplyMethod(vecR.shift,vB), Transform(lvR1,lvR2), FadeOut(vecBd), FadeOut(lvB))
		self.wait(2)
