import unittest
from unittest.mock import Mock, patch
from injector import Injector, Module, Binder, singleton
import os, sys
print(os.path.curdir)
print(os.path.abspath(os.path.curdir))
print("+++++++++++++++++++++++++++")
sys.path.append(os.path.abspath(os.path.curdir))
#print(sys.path)
from busines import GameState
from busines import GamesSettings
from busines import Game
# from busines.GameState import GameState as GS
# from console.ConsoleSnake import ConsoleRenderer, ConsoleInputCollector
# from busines.Map import MapFactory, Map
# from busines.GamesSettings import GameSettings
# import console.ConsoleSnake
#from bootstrap import GameModule
# from shared.Interfaces import Renderer
# Extend GameModule to override specific bindings
# class TestGameModule(GameModule):
#     def configure(self, binder: Binder) -> None:
#         super().configure(binder)  # Call the original configure method
#         binder.bind(GameSettings, to=Mock(GameSettings), scope=singleton)
#         binder.bind(MapFactory, to=Mock(MapFactory), scope=singleton)
#         binder.bind(Map, to=Mock(Map), scope=singleton)
#         binder.bind(Renderer, to=Mock(ConsoleRenderer), scope=singleton)
#         binder.bind(GS, to=Mock(GS), scope=singleton)
#         binder.bind(ConsoleInputCollector, to=Mock(console.ConsoleSnake.ConsoleInputCollector), scope=singleton)

class TestGame(unittest.TestCase):
    def setUp(self):
        print("ABC")
        # self.injector = Injector([TestGameModule()])
    
    def test_game_initialization(self):
        print("BCD..")
        # game_instance = self.injector.get(Game)
        # #raise Exception("AAAAAAAA")
        # self.assertIsInstance(game_instance.map, Mock)
        # self.assertIsInstance(game_instance.renderer, Mock)
        # self.assertIsInstance(game_instance.state, Mock)
        # self.assertIsInstance(game_instance.input_collector, Mock)


if __name__ == '__main__':
    unittest.main()
