"""
1) Создайте систему регистрации на конференцию. Реализуйте классы Conference (конференция), Participant (участник)
и RegistrationSystem (система регистрации). Класс Conference должен иметь атрибуты name (название) и capacity (вместимость),
класс Participant - атрибуты name (имя) и email (электронная почта), а класс RegistrationSystem - атрибуты conference (конференция)
и participants (список участников), а также методы register(participant) для регистрации участника и is_registration_available()
для проверки доступности регистрации на конференцию. Реализуйте проверку наличия свободных мест на конференции перед регистрацией.
"""
from level3.task31.conference import Conference
from level3.task31.participant import Participant
from level3.task31.regsystem import RegistrationSystem


def start_level31() -> None:
    my_conf = Conference('IT Conference', 4)
    p1 = Participant('Bob', 'bobthebig@gmail.com')
    p2 = Participant('John', 'friend123@gmail.com')
    p3 = Participant('Kate', 'unicornagain@gmail.com')
    participants: list = [str(p1), str(p2), str(p3)]
    print(f'{str(my_conf)}')
    print(f'Participants: {participants}\n\n')

    my_system = RegistrationSystem(my_conf, participants)
    print(f'Initialize new registration system.')
    print(f'{str(my_system)}\n')

    my_system.register(Participant('Sarah', 'stronger123@gmail.com'))
    print(f'Registration new participant.')
    print(f'{str(my_system)}\n')

    my_system.register(Participant('Kyle', 'kylemann@gmail.com'))
    print(f'Secondary registration new participant.')
    print(f'{str(my_system)}')