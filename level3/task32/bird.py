from level3.task32.animal import Animal


class Bird(Animal):
    def __init__(self, name: str, price: int, animal_type: str = 'Bird'):
        super().__init__(name, price, animal_type)


    def sound(self) -> str:
        return 'Whistle!'