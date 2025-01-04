from game.entities import *
from game.graphics.player_button import PlayerButton
from .settings import *
import pygame as pg


# Klasa, która zawiera w sobie logikę gry
class Game:
    def __init__(self) -> None:
        # Inicjacja i początkowe ustawienia
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("Turn-based game")
        self.clock = pg.time.Clock()
        self.running = True
        self.current_turn = "Hero"
        self.font = pg.font.SysFont("Comic Sans", 30)

        # Gracze jako atrybuty gry - ułatwienie w zarządzaniu nimi
        self.hero = Hero(name="Jerzy na Wieży", hp=100, attack_power=50)
        self.monster = Monster(name="Orek", hp=100, attack_power=25)

        self.buttons = {
            "attack": PlayerButton(200, HEIGHT - 150, "attack", self.hero_attack)
        }

    # Główna pętla gry
    def run(self) -> None:
        while self.running:

            # Sprawdzanie zdarzeń w grze
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False

                # obsługa tur
                if self.current_turn == "Hero":
                    for button in self.buttons.values():
                        button.handle_event(event)
                else:
                    self.handle_monster_turn()

            # Dalsze części pętli gry - rysowanie zaktualizowanych postaci,
            # aktualizowanie ekranu i ustawienie FPSów
            self.draw_characters()
            pg.display.flip()
            self.clock.tick(FPS)

    # Metoda, która rysuje wszystkie obiekty na ekranie
    def draw_characters(self) -> None:
        self.screen.fill(BLACK)

        self.screen.blit(self.hero.image, self.hero.rect)
        self.screen.blit(self.monster.image, self.monster.rect)

        hero_hp_text: pg.Surface = self.font.render(
            f"{self.hero.name}: {self.hero.hp} HP", True, WHITE
        )
        monster_hp_text: pg.Surface = self.font.render(
            f"{self.monster.name}: {self.monster.hp} HP", True, WHITE
        )

        self.screen.blit(hero_hp_text, (20, 20))
        self.screen.blit(
            monster_hp_text, (WIDTH - monster_hp_text.get_width() - 20, 20)
        )

        for button in self.buttons.values():
            button.draw(self.screen)

    def handle_monster_turn(self):
        self.monster.attack(self.hero)
        if not self.hero.is_alive():
            print(f"{self.hero.name} has been defeated!")
            self.running = False
        else:
            self.current_turn = "Hero"

    def end_hero_turn(self):
        if not self.monster.is_alive():
            print(f"{self.monster.name} has been defeated!")
            self.running = False
        else:
            self.current_turn = "Monster"

    def hero_attack(self):
        self.hero.attack(self.monster)
        self.end_hero_turn()
