from shared.event_type import event_type, game_event
from datetime import datetime
class GameState:
    def __init__(self) -> None:
        self.snakePos = [(0,0)]
        self.events ={ event_type.GAME_READY: game_event(event_type.GAME_READY, datetime.now())}
    def getSnakeHead(self):
        return self.snakePos[0]    
        
        