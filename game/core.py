from game.entities import *
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

    # Główna pętla gry
    def run(self) -> None:
        while self.running:

            # Sprawdzanie zdarzeń w grze
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False

                # Jeśli naciskamy spacje, to chcemy wykonać turę
                # (w tym momencie nie jest to istotne czy to hero czy monster
                # robimy to dla obu)
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_SPACE:
                        self.handle_turn()

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

    # Metoda, która zajmuje się tym, kto (monster czy hero) ma teraz swoją turę
    def handle_turn(self):
        if self.current_turn == "Hero":
            self.hero.attack(self.monster)
            if not self.monster.is_alive():
                print(f"{self.monster.name} has been defeated!")
                self.running = False
            else:
                self.current_turn = "Monster"
        elif self.current_turn == "Monster":
            self.monster.attack(self.hero)
            if not self.hero.is_alive():
                print(f"{self.hero.name} has been defeated!")
                self.running = False
            else:
                self.current_turn = "Hero"
