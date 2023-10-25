# Ref: https://realpython.com/inheritance-composition-python/

"""
    
"""

# Inheritance
from abc import ABC, abstractmethod


class SimpleClass:
    pass


class Polygon:
    """
     - name: class attribute
     - size: instance attribute
    """
    name = 'Polygon'

    def __init__(self, size: int) -> None:
        self.size = size


class Square(Polygon):
    name = 'Square'

    def __init__(self, size: int, base: int) -> None:
        super().__init__(size)  # <- call init method of the superclass (Polygon) => self.size = size
        self.base = base

    @property
    def area(self) -> float:
        return self.base ** 2

    @property
    def dimension(self):
        return self.size


# Abstract Base Class (ABC): class to be inherited but never instanciated

class ABCPolygon(ABC):
    """
        - object of type ACBPolygon can't be created
        - get_volume method must be implemented (overrided) by subclasses
    """

    def __init__(self, size) -> None:
        self.size = size

    @abstractmethod
    def get_volume(self):
        pass


class ABCSquare(ABCPolygon):
    """
    Example of interface inheritance
    """

    def __init__(self, size) -> None:
        super().__init__(size)

    # Must implement get volume
    def get_volume(self):
        return self.size ** 3


if __name__ == '__main__':
    a = SimpleClass()
    # print(a) # <__main__.<ClassName or Objet Type> object at <Memory address>

    # Method Resolution Order
    sq = Square(4, 5)
    print("MRO: ", Square.__mro__)
    print('Surface: ', sq.area)
    print('Size or dimension: ', sq.dimension)
    print("Name: ", sq.name)

    print("-" * 10)
