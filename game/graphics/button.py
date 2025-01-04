import pygame as pg


class Button:
    def __init__(self, x, y, width, height, bg_color, text, text_color, font, action):
        self.rect = pg.Rect(x, y, width, height)
        self.text = text
        self.font = font
        self.bg_color = bg_color
        self.text_color = text_color
        self.action = action

    def handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            # event.pos to koordynaty eventu, czyli kliknięcia myszką
            if self.rect.collidepoint(event.pos):
                if self.action:
                    self.action()

    def draw(self, screen):
        pg.draw.rect(screen, self.bg_color, self.rect)
        pg.draw.rect(screen, (0, 0, 0), self.rect, 2)

        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)
