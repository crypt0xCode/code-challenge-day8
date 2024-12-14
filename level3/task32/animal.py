class Animal:
    def __init__(self, name: str, price: int, animal_type: str = 'Animal'):
        self.name = name
        self.price = price
        self.animal_type = animal_type


    def __str__(self) -> str:
        return f'{self.animal_type} with name: {self.name} and price: {self.price}'


    def sound(self) -> str:
        pass