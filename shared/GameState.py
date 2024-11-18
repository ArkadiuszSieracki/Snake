from shared.event_type import event_type, game_event
from datetime import datetime
class GameState:
    def __init__(self) -> None:
        self.snakePos = [(0,0)]
        self.events ={ event_type.MAIN_MENU: game_event(event_type.MAIN_MENU, datetime.now())}
        self.sneakLength = 1
        self.lives = 4 ##TODO: assign from settings
        self.points = 0
        self.food_eaten = 0
    def getSnakeHead(self):
        return self.snakePos[0]    
        
        