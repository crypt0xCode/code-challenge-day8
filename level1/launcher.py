from level1.car import Car
from level1.rectangle import Rectangle


def start_level1() -> None:
    my_car = Car('Chevrolet', 'Taho')
    my_car.display_info()

    my_rect = Rectangle(10, 4)
    print(f'Area of {str(my_rect)} is {my_rect.calculate_area()}')