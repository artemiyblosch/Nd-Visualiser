from world import World
from math import cos,sin

class Polytope:
    def __init__(self, structure, colors):
        self.structure = structure
        self.colors = colors
    
    def draw_on(self,world : World, color : tuple[int,int,int] = (0,0,0)):
        colorL = [(-1,0,0) for i in self.structure[1]]
        for index in range(len(self.structure[-1])):
            if self.colors[index][0] == -1: continue
            cFacets = struct_bfs(self.structure,index)
            for j in cFacets:
                if colorL[j][0] == -1: colorL[j] = self.colors[index]
                else: colorL[j] = ((self.colors[index][0]+colorL[j][0])/2,\
                                   (self.colors[index][1]+colorL[j][1])/2,\
                                   (self.colors[index][2]+colorL[j][2])/2)
        for i in range(len(self.structure[1])):
            c = list(map(int,colorL[i]))
            if c[0] == -1: c = color if color != None else (-1,0,0)

            world.draw_face([self.structure[0][v] for v in self.structure[1][i]],c)
        return self

    def rotate(self, plane : tuple[int,int], angle : float, around_point : list[float] = None):
        def r(p):
            for i in range(len(p)):
                p[i] -= around_point[i] if around_point != None else 0
            tp = (p[plane[0]],p[plane[1]])
            p[plane[0]] = tp[0]*cos(angle)+tp[1]*sin(angle)
            p[plane[1]] = -tp[0]*sin(angle)+tp[1]*cos(angle)
            return p
        for i in range(len(self.structure[0])):
            self.structure[0][i] = r(self.structure[0][i])
        return self
    
    def upcast(self, dimension : int):
        for i in range(len(self.structure[0])):
            a = self.structure[0][i]
            self.structure[0][i] = a + [0]*(dimension-len(a))
        return self
    
def import_OFF(path : str) -> Polytope:
    with open(path) as f:
        file = f.read().split("\n")
    
    for i in range(len(file)):
        for j in range(len(file[i])):
            if file[i][j] != "#": continue
            file[i] = file[i][:j]
            break
    file = list(filter(lambda a: a != "",file))

    del file[0]
    count = list(map(int,file[0].split()))
    del file[0]

    del count[2]
    struct = []
    for i in count:
        tmp = []
        for j in range(i):
            tmp.append(list(map(float,file[0].split())))
            del file[0]
        struct.append(tmp)
    verticies, *struct = struct
    colors = [(-1,0,0)]*len(struct[-1])
    for j,facets in enumerate(struct):
        for i,v in enumerate(facets):
            v = [int(I) for I in v]
            count = v[0]

            tmp_struct, tmp_col = v[1:count+1], v[count+1:]
            struct[j][i] = tmp_struct

            if tmp_col != []: colors[i] = tuple(tmp_col)
    return Polytope([verticies] + struct,colors)

def struct_bfs(structure : list, facet : int):
    facets = [facet]
    struct = structure[:]

    while len(struct) != 2:
        ridges = set()
        for f in facets:
            for i in struct[-1][f]: ridges.add(i)
        facets = list(ridges)
        struct = struct[:-1]

    return facets
    