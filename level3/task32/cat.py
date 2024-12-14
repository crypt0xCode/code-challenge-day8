from level3.task32.animal import Animal


class Cat(Animal):
    def __init__(self, name: str, price: int, animal_type: str = 'Cat'):
        super().__init__(name, price, animal_type)


    def sound(self) -> str:
        return 'Meow!'