class Conference:
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity


    def __str__(self) -> str:
        return f'{self.name} with capacity for {self.capacity} participants'