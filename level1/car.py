"""
1) Создайте класс Car, который имеет атрибуты make (марка) и model (модель).
Реализуйте метод display_info(), который выводит информацию о марке и модели автомобиля.
"""
class Car:
    def __init__(self, make: str, model: str):
        self.make = make
        self.model = model

    def display_info(self) -> None:
        """
        Display info of current car.
        """
        print(f'Car info: {self.make}, model {self.model}')