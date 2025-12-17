from world import World
from polytope import import_OFF,export_OFF
from projections import center,iso
from constructions import prismify

def frame():
    w.clear()
    p1.rotate((0,2),0.05)
    p1.draw_on(w,None)

w = World([center([4])]*2,(500,500),"white",((-4,4),(-4,4)))
p1 = prismify(prismify(import_OFF("Triangle.off")))
p1.colors[0] = (255,0,0)
#export_OFF(p1,"prism.off")
p1.draw_on(w)
w.mainloop(frame,1/60)