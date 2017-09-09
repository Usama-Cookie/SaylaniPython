''' Define a class named Shape and its subclass Square. The Square class
has an init function which takes a length as argument. Both classes
have a area function which can print the area of the shape where
Shape's area is 0 by default.
Hints:
To override a method in super class, we can define a method with the
same name in the super class. '''


class Shape():
    def __init__(self):
        pass
    def area(self):
        print('Area = ',0)
class Square(Shape):
    def __init__(self,length):
        self.length = length
    def area(self):
        area = self.length * self.length
        print('Area = ', area)

x = int(input('Length of side of Square: '))
a = Shape()
a.area()
b = Square(x)
b.area()