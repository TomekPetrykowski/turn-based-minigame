class Character:
    def __init__(self, name: str, life_points: int) -> None:
        self.name = name
        self.life_points = life_points
        self.max_life_points = life_points

    def describe(self) -> None:
        print(f"I'm {self.name} and i have now {self.life_points}")
