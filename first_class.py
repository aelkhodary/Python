class MyFirstClass:
    pass

class Point:
    def reset(self):
        self.x=0
        self.y=0
p1=Point()
p1.reset()
print(p1.x,p1.y)

p2=Point()
Point.reset(p2)
print(p1.x,p1.y)