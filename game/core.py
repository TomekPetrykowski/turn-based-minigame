from game.entities import *
from .settings import *


# Klasa, która zawiera w sobie logikę gry
class Game:
    def __init__(self) -> None:
        self.hero = Hero(
            name="Jerzy na Wieży", life_points=100, attack_power=50, class_name="elf"
        )
        self.monster = Monster(name="Orek", life_points=100, attack_power=25)

    def run(self):
        while self.hero.is_alive():
            self.hero.attack(self.monster)

            if not self.monster.is_alive():
                print("Wygrał człek!")
                break

            self.monster.attack(self.hero)
        else:
            print("Ciemne czasy nastały")
