# Pliki __init__.py pozwalają utworzyć z folderu, który zawiera pliku .py moduł,
# czyli zbiór logicznie powiązanego ze sobą kodu
# Możemy umieścić tu początkowe ustawienia (np importy) albo zostawić pustego.

from .character import Character
from .hero import Hero
from .monster import Monster


# Poniższa zmienna mówi o tym, co zostanie zaimportowane, kiedy użyjemy
# from game.entities import *
# jest to zamiennik tej gwiazdki
__all__ = ["Character", "Hero", "Monster"]
