class circle:
    def __init__(self, radius):
        self.radius = radius
    def area (self):
        return 22/7*(self.radius**2)
    def perimeter (self):
        return 2*22/7*self.radius
Circles=circle(4)
print('area of circle is',Circles.area())
print('area of circle is',Circles.perimeter())