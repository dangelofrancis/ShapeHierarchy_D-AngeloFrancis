
# This is a Circle class that inherits from BasicShape

from BasicShape import BasicShape
from math import pi

class Circle(BasicShape):
    def __init__(self, x: float, y: float, r: float, n: str = "Circle"):
        super().__init__(area = 0, name = n)
        self._x_center = x
        self._y_center = y
        self._radius = r
        self.calc_area()

    @property
    def x_center(self) -> float:
        return self._x_center

    @property
    def y_center(self) -> float:
        return self._y_center

    @property 
    def radius(self) -> float:
        return self._radius

    @radius.setter
    def radius(self, value: float):
        self._radius = value
        self.calc_area()

    def calc_area(self):
        self._area = pi * (self._radius ** 2)