class Participant:
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email


    def __str__(self) -> str:
        return f'{self.name}, e-mail: {self.email}'