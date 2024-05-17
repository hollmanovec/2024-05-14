

from typing import List
from abc import ABC, abstractmethod

class Figure(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

class Rectangle(Figure):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

class Square(Figure):
    def __init__(self, side):
        self.side = side

    def calculate_area(self):
        return self.side * self.side

def calculate_total_area(figures:List[Figure]):
    total_area = 0
    for obj in figures:
        total_area += obj.calculate_area()
    return total_area

figures = [Rectangle(5,6),Square(10)]
print (calculate_total_area(figures))