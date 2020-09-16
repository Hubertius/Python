"""
    Stwórz trzy klasy:
    1) Rectangle - prostokąt
    2) Square - kwadrat
    3) Cube - sześcian

    a) Stwórz konstruktory (__init__)
    b) Metody obliczające powierzchnię prostokąta, kwadratu i sześcianu
    c) Metodę obliczającą objętość sześcianu

    Zastanów się jak możesz wykorzystać do tego dziedziczenie, aby nie powtarzać kodu.
    
"""


class Rectangle():
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Square(Rectangle):
    def __init__(self, sideLength):
        super().__init__(sideLength, sideLength)


class Cube(Square):
    def cube_area(self):
        return super().area() * 6
    def volume(self):
        return super().area() * self.height


cube = Cube(3)
print(cube.cube_area())
print(cube.volume())
