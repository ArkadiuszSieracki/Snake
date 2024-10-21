from injector import Injector, Module, Binder, singleton
from  shared.GamesSettings import GameSettings
from shared.Map import Map, MapFactory
import busines.Game as Gam
from shared.GameState import GameState  as GS
from console.ConsoleSnake import ConsoleRenderer as Csr
import console
import console.ConsoleSnake
from shared.Interfaces import Renderer, InputController
# DI Container
# class Container(containers.DeclarativeContainer):
#     config = providers.Configuration()
#     settings = providers.Singleton(GameSettings)
#     map_factory = providers.Factory(MapFactory)
#     map = providers.Factory(lambda container: container.map_factory().getMap())
     
#     game_state = providers.Factory(GS)
#     renderer = providers.Factory(Csr)
#     game = providers.Factory(Gam.Game)
#     ConsoleInputCollector = providers.Factory(console.ConsoleSnake.ConsoleInputCollector)

# if __name__ == "__main__":
#     container = Container()
    
#     # Dependency injection happens automatically here
#     data_fetcher = container.data_fetcher()
    
#     print(data_fetcher.get_data())  


# Define your services and objects
# @singleton
# class Game:
#     @inject
#     def __init__(self, map: Map, renderer: Csr, state: GS, input_collector: console.ConsoleSnake.ConsoleInputCollector):
#         self.map = map
#         self.renderer = renderer
#         self.state = state
#         self.input_collector = input_collector

# class Container(Module):
#     def configure(self, binder: Binder) -> None:
#         binder.bind(GameSettings, to=GameSettings, scope=singleton)
#         binder.bind(Map, to=binder.injector.get(MapFactory).getMap(), scope=singleton)
#         binder.bind(Renderer, to=GS, scope=singleton)
#         binder.bind(Csr, to=Csr, scope=singleton)
#         binder.bind(console.ConsoleSnake.ConsoleInputCollector, to=console.ConsoleSnake.ConsoleInputCollector, scope=singleton)
#         binder.bind(Gam.Game, to=Gam.Game, scope=singleton)

class GameModule(Module):
    def configure(self, binder: Binder) -> None:
        binder.bind(GameSettings, to=GameSettings, scope=singleton)
        binder.bind(MapFactory, to=MapFactory, scope=singleton)
        binder.bind(Map, to=lambda: binder.injector.get(MapFactory).getMap(), scope=singleton)
        binder.bind(Renderer, to=Csr, scope=singleton)  # Ensure ConsoleRenderer is used for Renderer
        binder.bind(GS, to=GS, scope=singleton)
        binder.bind(InputController, to=console.ConsoleSnake.ConsoleInputCollector, scope=singleton)
        binder.bind(Gam.Game, to=Gam.Game, scope=singleton)