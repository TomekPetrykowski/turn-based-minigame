import pygame as pg
from .button import Button
from game.settings import BLACK, ORANGE
from collections.abc import Callable
from pygame.typing import RectLike, ColorLike
from pygame import Font


# Otypowany przycisk gracza, pora na button ogólny!
class PlayerButton(Button):
    def __init__(self, x: int, y: int, text: str, action: Callable):

        self.rect: RectLike = pg.Rect(x, y, 150, 50)
        self.text: str = text
        self.action: Callable = action
        self.font: Font = pg.font.SysFont("Comic Sans", 24)
        self.bg_color: ColorLike = ORANGE
        self.text_color: ColorLike = BLACK
