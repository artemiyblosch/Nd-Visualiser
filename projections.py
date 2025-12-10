from math import copysign

def ortho(point : list[float]):
    return point[:-1]

def iso(direction : list[float],failsafe = True):
    return lambda point: point if failsafe and len(point) <= 2 else \
        [v + (direction[i] if i < len(direction) else 0)*point[-1] for i,v in enumerate(point[:-1])]


def cProjection(cy,ay,ax):
    if cy == ay: return copysign(float("inf"),ax)
    return cy*ax/(cy-ay)

def center(cen : list[float]):
    def __(point : list[float]):
        c = [0] * (len(point)-len(cen)) + cen
        return [cProjection(c[-1],point[-1],v - c[i]) + c[i] for i,v in enumerate(point[:-1])]
    return __