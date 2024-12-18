from __future__ import (
    annotations,
)  # Jeśli chcemy otypować coś, co jeszcze nie jest ukończone (np klasę w samej definicji klasy)
import pygame as pg
from random import randint


class Character:
    def __init__(self, name: str, hp: int, attack_power: int):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power

    def attack(self, target: Character) -> None:
        damage: int = randint(self.attack_power - 5, self.attack_power + 5)
        target.hp -= damage
        print(f"{self.name} attacks {target.name} for {damage} damage!")

    def describe(self) -> None:
        print(f"I'm {self.name}")

    def is_alive(self) -> bool:
        return self.hp > 0
