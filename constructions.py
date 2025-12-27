from polytope import Polytope
from math import sin, cos, pi
from fractions import Fraction

def pyramidify(polytope : Polytope, point : list[float]) -> Polytope:
    polytope.upcast(len(point))
    polytope.structure[0].append(point)
    if len(polytope.structure[-1]) != 1: 
        polytope.structure += [[list(range(len(polytope.structure[-1])))]]
    
    count = [len(i) for i in polytope.structure]
    d = {}
    for index in range(count[1]):
        i = polytope.structure[1][index]
        for j in range(-1,len(i)-1):
            if frozenset((i[j],i[j+1])) in d: continue

            polytope.structure[1].append([i[j],len(polytope.structure[0])-1,i[j+1]])
            d[frozenset((i[j],i[j+1]))] = len(polytope.structure[1]) - 1

    polytope.colors = [(-1,0,0)]*len(polytope.structure[-1])
    if len(polytope.structure) == 2: return polytope

    td = {}
    for index in range(count[1]):
        i = polytope.structure[1][index]
        tc = [index]

        for j in range(-1,len(i)-1):
            tc.append(d[frozenset((i[j],i[j+1]))])
        polytope.structure[2].append(tc)
        td[index] = len(polytope.structure[2]) - 1
    d = td.copy()

    for dim in range(2,len(polytope.structure)-1):
        td = {}
        for index in range(count[dim]):
            i = polytope.structure[dim][index]
            tc = [index]

            for j in i:
                tc.append(d[j])
            polytope.structure[dim + 1].append(tc)
            td[index] = len(polytope.structure[dim + 1]) - 1
        d = td.copy()

    polytope.colors = [(-1,0,0)]*len(polytope.structure[-1])
    return polytope

def prismify(polytope : Polytope) -> Polytope:
    count = [len(i) for i in polytope.structure]

    for i in range(count[0]):
        vertex = polytope.structure[0][i]
        polytope.structure[0].append(vertex + [-1])
        polytope.structure[0][i] += [1]
    
    for dim in range(1,len(count)):
        for facet in range(count[dim]):
            tf = polytope.structure[dim][facet]
            polytope.structure[dim].append([i + count[dim-1] for i in tf])

    if count[-1] != 1:
        polytope.structure.append([list(range(count[-1])),list(range(count[-1],2*count[-1]))])
        count.append(2)
    else:
        polytope.structure.append([])
        count.append(0)
    
    d = {}
    for index in range(count[1]):
        i = polytope.structure[1][index]
        for j in range(-1,len(i)-1):
            if frozenset((i[j],i[j+1])) in d: continue

            polytope.structure[1].append([i[j],i[j]+count[0],i[j+1]+count[0],i[j+1]])
            d[frozenset((i[j],i[j+1]))] = len(polytope.structure[1]) - 1

    td = {}
    for index in range(count[1]):
        i = polytope.structure[1][index]
        tc = [index,index+count[1]]

        for j in range(-1,len(i)-1):
            tc.append(d[frozenset((i[j],i[j+1]))])
        polytope.structure[2].append(tc)
        td[index] = len(polytope.structure[2]) - 1
    d = td.copy()

    for dim in range(2,len(polytope.structure)-1):
        td = {}
        for index in range(count[dim]):
            i = polytope.structure[dim][index]
            tc = [index,index+count[dim]]

            for j in i:
                tc.append(d[j])
            polytope.structure[dim + 1].append(tc)
            td[index] = len(polytope.structure[dim + 1]) - 1
        d = td.copy()
    
    if count[-1] == 0: polytope.structure.pop()
    polytope.colors = [(-1,0,0)]*len(polytope.structure[-1])
    return polytope

def polygon(sides : float | Fraction) -> Polytope:
    if not isinstance(sides,Fraction): sides = Fraction(sides)
    
    angle = pi/sides.numerator
    angle *= 2 * sides.denominator
    return Polytope([
        [[sin(i*angle), cos(i*angle)] for i in range(sides.numerator)],
        [list(range(sides.numerator))]
    ])

def product(p1 : Polytope, p2 : Polytope) -> Polytope:
    structure = [[] for _ in range(len(p1.structure)+len(p2.structure)-1)]

    if len(p1.structure[-1]) == 1: dim1 = len(p1.structure)
    else: dim1 = len(p1.structure) + 1

    if len(p2.structure[-1]) == 1: dim2 = len(p2.structure)
    else: dim2 = len(p2.structure) + 1

    d = {}
    for i in p2.structure[0]: pass


def canonize(p : Polytope) -> Polytope:
    new_faces = []
    d = {}
    p.structure.insert(1,[])
    for face in p.structure[2]:
        new_faces.append([])
        for i in range(-1,len(face)-1):
            if edge:=frozenset(face[i],face[i+1]) not in d:
                p.structure[1].append((face[i],face[i+1]))
                d[edge] = len(p.structure[1]) - 1
            new_faces[-1].append(d[edge])
    return p
