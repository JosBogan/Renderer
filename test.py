from definitions.triangle import Triangle
from definitions.ray import Ray
from definitions.point import Point
from definitions.vectors import Vector


# ! Test 1 - Simple perpendicular

# a = Point(6, 0, 7)
# b = Point(6, 4, 7)
# c = Point(6, 4, 0)

# tri = Triangle(a, b, c)

# triangles = [tri]

# ray = Ray(Vector(0, 1, 1), Vector(1, 1, 1), 10)

# ray.calculateIntersection(triangles)

# print(ray.getHit())

#! Test 2 - simple perpendicular with angled ray


a = Point(6, 0, 7)
b = Point(6, 4, 7)
c = Point(6, 4, 0)

tri = Triangle(a, b, c)

triangles = [tri]

ray2 = Ray(Vector(-2, 4, 1), Vector(-1, 3, 1), 10)

ray2.calculateIntersection(triangles)

print(ray2.getHit())

#! Test 3 - complex

# a = Point(6, 9, 2)
# b = Point(4, 2, 7)
# c = Point(-3, 1, 1)

# tri = Triangle(a, b, c)

# triangles = [tri]

# ray3 = Ray(Vector(-4, 3, 2), Vector(-3, 3, 2), 10)

# ray3.calculateIntersection(triangles)

# print(ray3.getHit())

# ! Test 4 - didHit triangle?

# a = Point(6, 0, 7)
# b = Point(6, 4, 7)
# c = Point(6, 4, 0)

# tri = Triangle(a, b, c)

# triangles = [tri]

# ray = Ray(Vector(0, 3, 6), Vector(1, 3, 6), 10)

# ray.calculateIntersection(triangles)

# print(ray.getHit())

