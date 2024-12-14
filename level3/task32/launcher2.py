"""
2) Создайте игру "Магазин животных". Реализуйте базовый класс Animal (животное) с атрибутами name (имя) и price (цена),
а также методом sound(), который возвращает звук, издаваемый животным. От него унаследуйте классы Dog, Cat и Bird,
каждый из которых переопределяет метод sound() для возврата соответствующего звука для каждого типа животного.
Класс Shop должен иметь атрибуты animals (список доступных животных) и budget (бюджет магазина), а также методы buy_animal(animal)
для покупки животного и sell_animal(animal) для продажи животного. Реализуйте проверки наличия достаточного бюджета у магазина для покупки и
наличия животного в магазине для продажи.
"""
from level3.task32.animal import Animal
from level3.task32.dog import Dog
from level3.task32.cat import Cat
from level3.task32.bird import Bird
from level3.task32.shop import Shop


def start_level32():
    dog = Dog('Fluffy', 10)
    cat = Cat('Orange', 5)
    bird = Bird('Jackie', 4)
    animals: list = [dog, cat, bird]
    pet_shop = Shop(animals, 10)
    print(f'{str(pet_shop)}\n')

    print('Buy new animal.')
    pet_shop.buy_animal(
        Animal('Rattie', 10)
    )
    print('After buying:')
    print(f'{str(pet_shop)}\n')

    print('Secondary buying new animal.')
    pet_shop.buy_animal(
        Dog('Brasco', 10)
    )
    print('After buying:')
    print(f'{str(pet_shop)}\n')

    print('Sell animal.')
    pet_shop.sell_animal(cat)
    print('After selling:')
    print(f'{str(pet_shop)}\n')

    print('Secondary selling animal.')
    pet_shop.sell_animal(cat)
    print('After selling:')
    print(f'{str(pet_shop)}')