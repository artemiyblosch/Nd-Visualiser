from polytope import Polytope
def pyramidify(polytope : Polytope, point : list[float]):
    polytope.colors = None

    polytope.structure[0].append(point)
    if len(polytope.structure[-1]) != 1: 
        polytope.structure += [[list(range(len(polytope.structure[-1])))]]
    
    count = [len(i) for i in polytope.structure]
    d = {}
    for index in range(count[1]):
        i = polytope.structure[1][index]
        for j in range(len(i)-1):
            if frozenset((i[j],i[j+1])) in d: continue

            polytope.structure[1].append([i[j],len(polytope.structure[0])-1,i[j+1]])
            d[frozenset((i[j],i[j+1]))] = len(polytope.structure[1]) - 1

    if len(polytope.structure) == 2: return polytope

    td = {}
    for index in range(count[1]):
        i = polytope.structure[1][index]
        tc = [index]

        for j in range(len(i)-1):
            tc.append(d[frozenset((i[j],i[j+1]))])
        polytope.structure[2].append(tc)
        td[index] = len(polytope.structure[2]) - 1
    d = td.copy()

    if len(polytope.structure) == 3: return polytope
    print(d)
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

    return polytope