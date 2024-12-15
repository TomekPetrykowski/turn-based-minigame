class Character:
    def __init__(self, name: str, life_points: int, attack_power: int):
        self.name = name
        self.life_points = life_points
        self.attack_power = attack_power

    def attack(self, target):
        target.life_points -= self.attack_power

    def describe(self):
        print(f"I'm {self.name}")

    def is_alive(self):
        return self.life_points > 0
