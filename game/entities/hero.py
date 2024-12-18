from .character import Character
import pygame as pg
from pygame.surface import SurfaceType  # Customowy typ powierzchni w pygame
from pygame.typing import RectLike
from game.settings import *


class Hero(Character):
    def __init__(self, name: str, hp: int, attack_power: int):
        super().__init__(name, hp, attack_power)

        self.image: SurfaceType = pg.image.load(
            "./assets/images/knight.png"
        ).convert_alpha()
        self.image: SurfaceType = pg.transform.scale_by(self.image, SCALE_FACTOR)
        self.image: SurfaceType = pg.transform.flip(self.image, True, False)
        self.rect: RectLike = self.image.get_rect()
        self.rect.center = (200, HEIGHT - 300)
