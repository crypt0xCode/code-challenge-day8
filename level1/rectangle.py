"""
2) Создайте класс Rectangle, который имеет атрибуты width (ширина) и height (высота).
Реализуйте метод calculate_area(), который возвращает площадь прямоугольника.
"""
class Rectangle:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height


    def __str__(self):
        return f'Rectangle: width = {self.width}, height = {self.height}'


    def calculate_area(self) -> int:
        """
        Calculate area of current rectangle.

        :return: calculated area for current rectangle.
        """
        return self.width * self.height