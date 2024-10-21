import enum

class event_type(enum.Enum):
    SELF_HIT = 1
    WALL_HIT = 2
    GAME_READY = 3