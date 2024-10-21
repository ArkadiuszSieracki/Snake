from abc import ABC, abstractmethod
from shared.GameState import GameState  as GS
class Renderer:
    @abstractmethod
    def renderFrame(self,map, state:GS):
        pass

class InputController:
    def __init__(self) -> None:
        pass
    @abstractmethod
    def GetDirection(self):
        pass