from enum import Enum
from datetime import datetime, timedelta 

class event_type(Enum):
    SELF_HIT = 1
    WALL_HIT = 2  
    GAME_READY = 3
    SNAKE_MOVE = 4
    GAME_OVER = 666
    MAIN_MENU = 667
    DASHBOARD = 668
class game_event:
    def __init__(self, type: event_type, t: datetime, duration: timedelta=timedelta(days=666)):
        self.event_type : event_type = type  # Use the parameter 'type'
        self.timestamp : datetime= t
        self.duration :timedelta = duration
        self.force_finished :bool= False
   
    def isFinished(self):
         if self.force_finished:
             return True
         else:
             return datetime.now() - self.timestamp > self.duration   
    def MarkAsDone(self):
        self.force_finished = True