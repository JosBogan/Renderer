def calculateDeterminant(a, b):
    return 0


def calculatePlaneIntersection(ray, triangle):
    P = ray['point']
    # d = 0
    n = findNormal(triangle['a'], triangle['b'], triangle['c'])
    D = ray['direction']

    topHalf = -findDotProduct(n, P)
    bottomHalf = findDotProduct(n, D)
    if (bottomHalf == 0 ):
        return False

    t = topHalf / bottomHalf

    print(vectorAddition(vectorMultiplication(ray['direction'], t), P))
    return vectorAddition(vectorMultiplication(ray['direction'], t), P)

# print(findCrossProduct({"x":0, "y":0, "z":0}, {"x": 3, "y": 1, "z": 4}, {"x": 3, "y": 2, "z":6}))
# print(findCrossProduct({"x":-1, "y":1, "z":2}, {"x": -4, "y": 2, "z": 2}, {"x": -2, "y": 1, "z":5}))

calculatePlaneIntersection(
    {'point': {'x':2, 'y':1, 'z':3}, 'direction': {'x':2, 'y': 2, 'z': 1}}, 
    {'a': {'x': 4, 'y': 5, 'z': 5}, 'b': {'x': 2, 'y': 8,'z': 7}, 'c': {'x': 2, 'y': 3,'z': 9}}
    )