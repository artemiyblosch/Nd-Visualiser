from world import World
from polytope import import_OFF,export_OFF
from projections import center,iso
from constructions import prismify,polygon,pyramidify
from math import *
from fractions import Fraction
def frame():
    w.clear()
    p1.rotate((0,2),0.1)
    p1.rotate((1,3),-0.1)
    p1.draw_on(w,None)


w = World([center([4]),center([4])],(500,500),"white",((-4,4),(-4,4)))
p1 = prismify(prismify(polygon(Fraction(4,1))))
p1.colors = [(0,0,0)]*len(p1.structure[-1])
#export_OFF(p1,"prism.off")
p1.draw_on(w)
w.mainloop(frame,1/60)