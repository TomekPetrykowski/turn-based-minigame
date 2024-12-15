from .character import Character


class Monster(Character):
    def __init__(self, name: str, life_points: int, attack_power: int):
        super().__init__(name, life_points, attack_power)

    # nadpisaliśmy metodę attack tylko częściowo
    def attack(self, target):
        super().attack(target)
        print(f"Hero {target.name} has been hit")
