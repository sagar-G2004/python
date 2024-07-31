4.	Write a Python program to create a class that represents a shape. Include methods to calculate its area and perimeter. Implement subclasses for different shapes like circle, triangle, and square.
import math

class shapes:
    def area(self):
        None
    def perimeter(self):
        None
class circle(shapes):
    def __init__(self,r):
        self.rad=r
    def area(self):
        a=3.14*self.rad*self.rad
        print("C:area:",a)
    def perimeter(self):
        p=2*3.14*self.rad
        print("C:perimeter:",p)
class square(shapes):
    def __init__(self, s):
        self.side = s

    def area(self):
        a = self.side * self.side
        print("Square area:", a)

    def perimeter(self):
        p = 4 * self.side
        print("Square perimeter:", p)
shape=circle(2)
shape.area()
shape.perimeter()
shape2=square(4)
shape2.area()
shape2.perimeter()
    
