
# An abstract base class for basic geometric shapes

from abc import ABC, abstractmethod
from xml.sax.handler import property_declaration_handler

class BasicShape(ABC):
    def __init__(self, area: float, name: str):
        self._area = area
        self._name = name

    @property
    def area(self):
        return self._area

    @area.setter
    def area(self, value: float):
        self._area = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value: float):
        self._name = value

    @abstractmethod
    def calc_area(self):
        pass

