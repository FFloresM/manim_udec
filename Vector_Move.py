from manimlib.imports import *

class VectorMove(Scene):
    def construct(self):
        v1 = np.array([3,0,0])
        v2 = np.array([2,3,0])
        v3 = v1+v2
        vector1 = Vector(v1)
        vector2 = Vector(v2)
        vector3 = Vector(v3)
        v1txt = TextMobject("X").next_to(vector1,DOWN)
        v2txt = TextMobject("Y").next_to(vector2,LEFT)
        v3txt = TextMobject("X+Y").next_to(vector3,RIGHT)

        self.play(ShowCreation(vector1),Write(v1txt))
        self.play(ShowCreation(vector2),Write(v2txt))
        self.play(ShowCreation(vector3),Write(v3txt))
        

        vgroup_ = VGroup(vector1,v1txt,vector2,v2txt,vector3,v3txt)
        self.play(ApplyMethod(vgroup_.to_edge, LEFT, {"buff": 1.6}))
        #self.play(ShowCreation(v1txt))

        #self.play(ShowCreation(vector2))
        #self.play(ShowCreation(v2txt))
        
class Vector3(Scene):
    def construct(self):
        v1 = np.array([3,0,0])
        v2 = np.array([-3,0,0])
        v3 = v1+v2
        vector1 = Vector(v1)
        vector2 = Vector(v2)
        vector3 = Vector(v3)
       # v1txt = TextMobject("A").next_to(vector1,DOWN)
        #v2txt = TextMobject("-A").next_to(vector2,LEFT)
        v3txt = TextMobject("X+Y").next_to(vector3,RIGHT)
        v1txt = TextMobject("A")
        v2txt = TextMobject("-A")
        v1txt.shift(UR)
        v2txt.shift(UL)
        #self.play(ShowCreation(v1txt))
        self.play(ShowCreation(vector1),Write(v1txt))
        self.wait()
        self.play(Transform(vector1,vector2),Transform(v1txt,v2txt))
        #self.play(Transform(v1txt,v2txt))
        #self.play(ShowCreation(vector3),Write(v3txt))
        

        #vgroup_ = VGroup(vector1,v1txt,vector2,v2txt,vector3,v3txt)
        #self.play(ApplyMethod(vgroup_.to_edge, LEFT, {"buff": 1.6}))
        #self.play(ShowCreation(v1txt))

        #self.play(ShowCreation(vector2))
        #self.play(ShowCreation(v2txt))
