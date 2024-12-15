from .character import Character


class Hero(Character):
    def __init__(self, name: str, life_points: int, attack_power: int, class_name: str):
        super().__init__(name, life_points, attack_power)
        self.class_name = class_name

    # Nadpisaliśmy metodę z klasy nadrzędnej
    def describe(self):
        print(f"I'm {self.name} of class {self.class_name}")

    # nadpisaliśmy metodę attack tylko częściowo
    def attack(self, target):
        super().attack(target)
        print(f"Monster {target.name} has been hit")
