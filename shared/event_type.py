from enum import Enum
from datetime import datetime

class event_type(Enum):
    SELF_HIT = 1
    WALL_HIT = 1  
    GAME_READY = 3

class game_event:
    def __init__(self, type: event_type, t: datetime):
        self.event_type : event_type = type  # Use the parameter 'type'
        self.timestamp : datetime= t