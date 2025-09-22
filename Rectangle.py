# This is a Rectangle class that inherits from BasicShape

from BasicShape import BasicShape

class Rectangle(BasicShape):
    def __init__(self, l: float, w: float, n: str = "Rectangle"):
        super().__init__(area = 0.0, name = n)
        self._length = l
        self._width = w
        self.calc_area()

    @property
    def length(self) -> float:
        return self._length

    @property
    def width(self) -> float:
        return self._width

    @length.setter
    def length(self, value: float):
        self._length = value
        self.calc_area()

    @width.setter
    def width(self, value: float):
        self._width = value
        self.calc_area()

    def calc_area(self):
        self._area = self._length * self._width