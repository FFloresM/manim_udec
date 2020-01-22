from manimlib.imports import *

class Resta(Scene):
	CONFIG = {
        "camera_config": {"frame_center": 0.5*UP+1*RIGHT}
	}
	def construct(self):
		O  = np.array([0,0,0])
		vB = np.array([3,0,0])
		vA = np.array([2,3,0])
		vmB = -vB
		vR = vA-vB
		texto = TextMobject("Resta de vectores").shift(4*UP+1*RIGHT)

		lvA = TextMobject("$\\vec{A}$",color="green").shift(0.5*vA+0.3*LEFT+0.3*UP)
		lvR1 = TextMobject("$\\vec{A}+(-\\vec{B})$").shift(0.5*vR+0.3*DOWN+1.1*LEFT)
		lvR2 = TextMobject("$\\vec{A}-\\vec{B}$").shift(0.5*vR+0.3*DOWN+vB+1*RIGHT)

		lvB = TextMobject("$\\vec{B}$",color="red").shift(0.5*vB+0.5*DOWN)
		lvB2 = TextMobject("$\\vec{B}$",color="red").shift(0.5*vB+0.5*DOWN)
		lvmB = TextMobject("$-\\vec{B}$",color="red").shift(-0.5*vB+0.5*DOWN)
	
		vecAi = Vector(vA,color="green")
		vecAid = DashedVMobject(vecAi)
		vecR = Vector(vR)
		vecB = Vector(vB,color="red")
		vecBd = DashedVMobject(vecB)

		vecmBd = DashedVMobject(Vector(vmB,color="red"))
		vecBd = DashedVMobject(Vector(vB,color="red"))
		vecRd = DashedVMobject(vecR)

		self.play(Write(texto))
		self.wait(2)
		self.play(ShowCreation(vecAi))
		self.play(ShowCreation(lvA))
		self.play(ShowCreation(vecBd),ShowCreation(vecB))
		self.play(ShowCreation(lvB),ShowCreation(lvB2))
		self.wait(2)
		self.play(Transform(vecBd, vecmBd),Transform(lvB, lvmB))
		self.wait(2)
		self.play(ApplyMethod(vecBd.shift, vA),ApplyMethod(lvB.shift, vA+UP))
		self.play(ShowCreation(vecR))
		self.play(ShowCreation(lvR1))
		self.wait(2)
		self.play(ApplyMethod(vecR.shift,vB), Transform(lvR1,lvR2), FadeOut(vecBd), FadeOut(lvB))
		self.wait(4)

		vecmAd = DashedVMobject(Vector(-vA,color="green"))
		lmA = TextMobject("$-\\vec{A}$",color="green").shift(-0.5*vA+0.5*LEFT+0.3*UP)
		lvA2 = TextMobject("$\\vec{A}$",color="green").shift(0.5*vA+0.3*LEFT+0.3*UP)

		self.play(Transform(vecAid,vecmAd), Transform(lvA2,lmA))
		self.wait(2)
		self.play(ApplyMethod(vecAid.shift,vB),ApplyMethod(lvA2.shift,vB))
		self.wait(2)

		vecR2 = Vector(-vR)
		self.play(ShowCreation(vecR2))
		lvR3 = TextMobject("$\\vec{B}-\\vec{A}$").shift(-0.5*vR+0.3*DOWN+vB+4*LEFT)
		self.play(ShowCreation(lvR3))
		self.wait(2)
		self.play(ApplyMethod(vecR2.shift,0.95*vA),ApplyMethod(lvR3.shift,vA), FadeOut(vecAid), FadeOut(lvA2))
		self.wait(2)
		
