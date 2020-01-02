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
        PATH = os.getcwd()
        ruler = PATH+'/logo/ruler.svg'
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

        img = SVGMobject(ruler)
        img.scale(1)
        img.set_width(6)
        img.rotate(45 * DEGREES)
        img.shift(DOWN)
        self.play(ShowCreation(img))
        #self.play(ShowCreation(v1txt))
        self.play(ShowCreation(vector1),Write(v1txt))
        self.wait()
        self.play(Transform(vector1,vector2),Transform(v1txt,v2txt))
        self.wait()
 
class View3D(ThreeDScene):
   
    def construct(self):
        axes = ThreeDAxes()
        v1 = np.array([3,-3,0])
        v2 = np.array([3,-3,3])
        v3 = np.array([0,-3,0])

        #ln1 = DashedLine(np.array([3,0,0]),np.array([3,-3,0]),buff=0.1)
        ln0 = self.drawline([0,0,0],[0,-3,0])
        ln1 = self.drawline([0,-3,0],[3,-3,0])
        ln2 = self.drawline([3,-3,0],[3,0,0])
        ln3 = self.drawline([3,0,0],[0,0,0])
        
        #top
        ln0t = self.drawline([0,0,3],[0,-3,3])
        ln1t = self.drawline([0,-3,3],[3,-3,3])
        ln2t = self.drawline([3,-3,3],[3,0,3])
        ln3t = self.drawline([3,0,3],[0,0,3])

        vector1 = Vector(v1,color="red")
        vector2 = Vector(v2,color="red")
        #line
        ln0r = self.drawline([0,0,0],[0,0,3])
        ln1r = self.drawline([0,-3,0],[0,-3,3])
        ln2r = self.drawline([3,0,0],[3,0,3])
        ln3r = self.drawline([3,-3,0],[3,-3,3])

        self.play(ShowCreation(axes))
        self.play(ShowCreation(vector1))
        self.play(ShowCreation(ln0))
        self.play(ShowCreation(ln1))
        self.play(ShowCreation(ln2))
        self.play(ShowCreation(ln3))
        self.wait()
        self.move_camera(phi=65*DEGREES,theta=-75*DEGREES)
        self.wait()
        self.play(ShowCreation(ln0t))
        self.play(ShowCreation(ln1t))
        self.play(ShowCreation(ln2t))
        self.play(ShowCreation(ln3t))
        self.play(ShowCreation(ln0r),ShowCreation(ln1r),ShowCreation(ln2r),ShowCreation(ln3r))
        self.play(Transform(vector1,vector2))



    def drawline(self,initial,endline):
        #print(initial,endline)
        ln = DashedLine(np.array(initial),np.array(endline),buff=0.1)
        ln.set_color(YELLOW)
        return ln
