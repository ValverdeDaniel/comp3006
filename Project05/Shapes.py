#SHAPE Classes WORKING

import math

class Shape:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'I am a {self.name}'

    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Oval(Shape):
    def area(self, majorAxis, minorAxis):
        self.area = math.pi * (majorAxis/2) * (minorAxis/2)
        return f'I am an {self.name} and have a major axis of {majorAxis} and a minor axis of {minorAxis} my area is {self.area}'

#could make polygon scalable to multiple
class Polygon(Shape):
    def area(self, sides, sideLength, apothem):
        self.area = (apothem * (sides*sideLength))/2
        return f'I am a {self.name} I have {sides} sides, of length {sideLength}, an apothem of {apothem} and area of {self.area}'

class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)

class Triangle(Shape):
    def area(self, base, height):
        self.area = (base*height)/2
        return f'I am a {self.name} and have a base of {base} and height of {height} with an area of {self.area}'

class Pentagon(Shape):
    def area(self, apothem, sideLength):
        self.area = ((sideLength*apothem)/2)*5
        return f'I am a {self.name} and have an apothem of {apothem} and a sideLength of {sideLength} with an area of {self.area}'

class Circle(Shape):
    def area(self, radius):
        self.area = math.pi*(radius**2)
        return f'I am a {self.name} and have a radius of {radius} so my area is {self.area}'

class Parallelogram(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)


class Rhombus(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)

def main():
    #Rectangle
    rectangle = Rectangle(2,4)
    # print(rectangle)
    print(f'I am a rectangle and my area is {rectangle.area()}')

    #Oval
    oval = Oval('oval')
    print(oval.area(10,6))

    #Polygon
    polygon7 = Polygon('polygon')
    print(polygon7.area(7,3,5))
    polygon10 = Polygon('polygon')
    print(polygon10.area(10,10,5))

    #Square
    square = Square(4)
    print(f'I am a square and my area is {square.area()}')

    #Triangle
    triangle = Triangle('triangle')
    print(triangle.area(5,5))

    #Pentagon
    pentagon = Pentagon('pentagon')
    print(pentagon.area(3,2))

    #Circle
    circle = Circle('circle')
    print(circle.area(5))

    #Parallelogram
    parallelogram = Parallelogram(3)
    print(f'I am a parallelogram and my area is {parallelogram.area()}')

    #Rhombus
    rhombus = Rhombus(5)
    print(f'I am a rhombus and my area is {rhombus.area()}')

main()
