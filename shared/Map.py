class Map:
    def __init__(self, width: int, height: int) -> None:
        print(f"width {width}, height {height}")
        self.width = width
        self.height = height
from shared.GamesSettings  import GameSettings  
from injector import inject
class MapFactory():
    @inject
    def __init__(self, settings:GameSettings) -> None:
        self.settings = settings
    def getMap(self):
        return Map(self.settings.map_width, self.settings.map_height)

