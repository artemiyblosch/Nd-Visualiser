from world import World
from polytope import import_OFF
from projections import center,iso
from constructions import prismify

def frame():
    w.clear()
    p1.rotate((1,2),-0.05)
    p1.rotate((0,3),0.05)
    p1.draw_on(w,None)

w = World([center([4]),center([4]),center([4])],(500,500),"white",((-4,4),(-4,4)))
p1 = import_OFF("Triangle.off")
p1 = prismify(prismify(prismify(p1)))
p1.colors[4] = (255,0,0)
p1.draw_on(w)
w.mainloop(frame,1/60)