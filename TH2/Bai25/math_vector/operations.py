import math

def add(v1, v2):
    return (
        v1[0]+v2[0],
        v1[1]+v2[1],
        v1[2]+v2[2]
    )

def subtract(v1, v2):
    return (
        v1[0]-v2[0],
        v1[1]-v2[1],
        v1[2]-v2[2]
    )

def distance(v):
    return math.sqrt(v[0]**2 + v[1]**2 + v[2]**2)

def opposite(v):
    return (-v[0], -v[1], -v[2])