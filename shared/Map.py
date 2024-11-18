class Map:
    def __init__(self, width: int, height: int) -> None:
        print(f"width {width}, height {height}")
        self.width = width
        self.height = height
        self.obstacles:list = []
        self.monkeys: list = []
from shared.GamesSettings  import GameSettings  
from injector import inject
import random
class MapFactory():
    @inject
    def __init__(self, settings:GameSettings) -> None:
        self.settings = settings
    def getMap(self):
        map = Map(self.settings.map_width, self.settings.map_height)
        x = random.randint(0, map.width)
        y = random.randint(0, map.height)
        map.monkeys.append((3,3))
        map.monkeys.append((x,y))
        return map
        
    

