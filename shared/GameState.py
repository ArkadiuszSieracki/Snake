from shared.event_type import event_type
class GameState:
    def __init__(self) -> None:
        self.snakePos = [(0,0)]
        self.events =[event_type.GAME_READY]
        