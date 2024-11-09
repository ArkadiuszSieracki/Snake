import unittest
from unittest.mock import Mock, patch
from injector import Injector, Module, Binder, singleton
import os, sys
print(os.path.curdir)
print(os.path.abspath(os.path.curdir))
print("+++++++++++++++++++++++++++")
sys.path.append(os.path.abspath(os.path.curdir))
#print(sys.path)
from shared import GameState
from shared import GamesSettings
from busines import Game
from shared.GameState import GameState as GS
from console.ConsoleSnake import ConsoleRenderer, ConsoleInputCollector
from shared.Map import MapFactory, Map
from shared.GamesSettings import GameSettings
import console.ConsoleSnake
from bootstrap import GameModule
from shared.Interfaces import Renderer, InputController
# # Extend GameModule to override specific bindings
class TestGameModule(GameModule):
    def configure(self, binder: Binder) -> None:
        super().configure(binder)  # Call the original configure method
        binder.bind(GameSettings, to=Mock(GameSettings), scope=singleton)
        binder.bind(MapFactory, to=Mock(MapFactory), scope=singleton)
        binder.bind(Map, to=Mock(Map), scope=singleton)
        binder.bind(Renderer, to=Mock(ConsoleRenderer), scope=singleton)
        binder.bind(GS, to=Mock(GS), scope=singleton)
        binder.bind(InputController, to=Mock(InputController), scope=singleton)

class TestGame(unittest.TestCase):
    def setUp(self):
        self.injector = Injector([TestGameModule()])
    
    def test_game_initialization(self):
        game_instance = self.injector.get(Game.Game)
        state = self.injector.get(GameState.GameState)
        map = self.injector.get(Map)
        map.height = 10
        map.width = 10
        
        #raise Exception("AAAAAAAA")
        self.assertIsInstance(game_instance.map, Mock)
        self.assertIsInstance(game_instance.renderer, Mock)
        self.assertIsInstance(game_instance.state, Mock)
        self.assertIsInstance(game_instance.input_collector, Mock)
     
    def test_colision_happens(self):
       print("Rosie")
       game_instance = self.injector.get(Game.Game)
       state = self.injector.get(GameState.GameState)
       map = self.injector.get(Map)
       map.height = 10
       map.width = 10  
       state.snakePos = []
       state.snakePos.append((10,10))
       state.events = {}
       game_instance.detect_colisions()
       from shared.event_type import event_type
       isAny =  any(event.event_type == event_type.WALL_HIT for event in state.events.values())
       self.assertTrue(isAny, "We should have found event wall hit")
    def test_self_colision_happens(self):
       print("Rosie")
       game_instance = self.injector.get(Game.Game)
       state = self.injector.get(GameState.GameState)
       map = self.injector.get(Map)
       map.height = 10
       map.width = 10  
       state.snakePos = []
       state.snakePos.append((1,1))
       state.snakePos.append((1,1))
       state.events = {}
       game_instance.detect_colisions()
       from shared.event_type import event_type
       isAny = any(o.event_type == event_type.SELF_HIT for o in state.events.values())
       
       self.assertTrue(isAny, "self hit should be detected")

if __name__ == '__main__':
    unittest.main()
