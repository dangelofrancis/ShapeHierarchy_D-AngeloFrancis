# This is a Square class that inherits from Rectangle

from Rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, s: float, n: str = "Square"):
        super().__init__(s, s, n)
        self._side = s
        self.set_name(n)

    @property
    def side(self) -> float:
        return self._side

    @side.setter
    def side(self, value: float):
        self._side = value
        self.calc_area()