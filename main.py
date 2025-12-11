from world import World
from polytope import import_OFF
from math import *
from projections import iso,ortho,center

def angled(rad : float):
    return [sin(rad),cos(rad)]

def frame():
    w.clear()
    p1.rotate((0,3),-0.05)
    p1.rotate((1,2),0.05)
    p1.draw_on(w,None)

even = [angled(pi/4),angled(pi*3/4)]
w = World([center([4]),center([4])],(500,500),"white",((-2,2),(-2,2)))
p1 = import_OFF("tesseract.off")
p1.draw_on(w)
w.mainloop(frame,1/60)