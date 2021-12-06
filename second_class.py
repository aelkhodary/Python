import math


class Point:
    "Represents a point in two-dimensional geometric coordinates"
    def __init__(self,x=0,y=0):
        """Initialize the position of a new point. The x and y
                   coordinates can be specified. If they are not, the
                   point defaults to the origin."""
        self.move(x,y)

    def move(self,x,y):
        "Move the point to new location in 2D space."
        self.x=x
        self.y=y

    def reset(self):
        self.move(0,0)

    def calculate_distance(self,other_point):
        """“Calculate the distance from this point to a second
        point passed as a parameter.

        This function uses the Pythagorean Theorem to calculate
        the distance between the two points. The distance is
        returned as a float. """
        return math.sqrt((self.x-other_point.x)**2 + (self.y-other_point.y)**2)
#How to use it

p1=Point()
p2=Point()

p1.reset()
p2.move(5,0)
print(p2.calculate_distance(p1))
assert p2.calculate_distance(p1)==p1.calculate_distance(p2)
p1.move(3,4)
print(p1.calculate_distance(p2))
print(p1.calculate_distance(p1))

#Initializing Object
p3=Point(3,5)
print(p3.x,p3.y)

