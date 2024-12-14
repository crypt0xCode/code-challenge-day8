from level3.task32.animal import Animal


class Shop:
    def __init__(self, animals: list, budget: int):
        self.animals = animals
        self.budget = budget


    def __str__(self) -> str:
        return f'Shop with budget = {self.budget} and animals: {self.animals_to_str()}'


    def animals_to_str(self) -> str:
        """
        Convert Animal object notation in human-like string.

        :return: string with animals names and prices.
        """
        new_s: str = ''
        for animal in self.animals:
            new_s += str(animal) + ' | '

        return new_s


    def buy_animal(self, animal: Animal):
        """
        Add new animal in animals list.

        :param animal: Animal object.
        """
        if self.check_budget(animal.price):
            self.budget -= animal.price
            self.animals.append(animal)


    def sell_animal(self, animal: Animal):
        """
        Remove animal from animals list.

        :param animal: Animal object.
        """
        if self.check_animal(animal):
            self.budget += animal.price
            self.animals.remove(animal)


    def check_budget(self, price: int) -> bool:
        """
        Check available budget of current shop.

        :param price: price of specify animal.
        :return: bool flag.
        """
        flag: bool = True
        if self.budget < price:
            flag = False
            print(f'Not enough budget to buy animal for {price}')

        return flag


    def check_animal(self, animal: Animal) -> bool:
        """
        Check availability of specify animal in the current animals list.

        :param animal: Animal object.
        :return: bool flag.
        """
        flag: bool = True
        if animal not in self.animals:
            flag = False
            print(f'Animal: {str(animal)} not existed in animals list!')

        return flag
