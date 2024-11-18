from injector import Injector, Module, Binder, singleton
from  shared.GamesSettings import GameSettings
from shared.Map import Map, MapFactory
import busines.Game as Gam
from shared.GameState import GameState  as GS
from console.ConsoleSnake import ConsoleRenderer as Csr
import console
import console.ConsoleSnake
from shared.Interfaces import Renderer, InputController
from shared.MenuState import MenuState
class GameModule(Module):
    def configure(self, binder: Binder) -> None:
        binder.bind(GameSettings, to=GameSettings, scope=singleton)
        binder.bind(MapFactory, to=MapFactory, scope=singleton)
        binder.bind(Map, to=lambda: binder.injector.get(MapFactory).getMap(), scope=singleton)
        binder.bind(Renderer, to=Csr, scope=singleton)  # Ensure ConsoleRenderer is used for Renderer
        binder.bind(MenuState, to=MenuState, scope=singleton)  # Ensure ConsoleRenderer is used for Renderer
        binder.bind(GS, to=GS, scope=singleton)
        binder.bind(InputController, to=console.ConsoleSnake.ConsoleInputCollector, scope=singleton)
        binder.bind(Gam.Game, to=Gam.Game, scope=singleton)