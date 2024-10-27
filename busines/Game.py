from shared.GameState import GameState  as GS
import time
import shared.Interfaces as interfacces
from shared import move_direction
from shared.Map import Map
from shared.event_type import event_type, game_event
from shared.GamesSettings import GameSettings
# printing the start time

#import console.ConsoleSnake
# using sleep() to hault the code execution
from injector import inject
class Game:
    @inject
    def __init__(self, map: Map, renderer: interfacces.Renderer,state: GS , input_collector:interfacces.InputController, game_settings: GameSettings) -> None:
        self.map = map
        self.renderer = renderer
        self.state = state
        self.input_collector = input_collector
        self.game_settings = game_settings
    def play(self):
        import threading
        input_thread = threading.Thread(target=self.renderLoop)
        input_thread.start()
        while True:
            if (event_type.SELF_HIT in  self.state.events) == False:
                self.makeMove()
                self.detect_colisions()

            time.sleep(1)    
    def renderLoop(self):
        while True:
          self.renderer.renderFrame(self.map, self.state)        
          time.sleep(1/self.game_settings.frames_per_second)    
           
    def detect_colisions(self):
        from datetime import datetime
        snake_tip =  self.state.snakePos[0]
        if  len(self.state.snakePos) != len(set(self.state.snakePos))  :
            print("self hit event ") #self hit
            self.state.events.clear()
            self.state.events[event_type.SELF_HIT] = game_event(event_type.SELF_HIT, datetime.now())
        if snake_tip[0] < 0 or snake_tip[1] < 0 or snake_tip[0] >= self.map.width  or snake_tip[1] >= self.map.height:
            print("wall hit event")    
            self.state.events.clear()
            self.state.events[event_type.WALL_HIT] = game_event(event_type.WALL_HIT, datetime.now())           
    def makeMove(self):
        direction = self.input_collector.GetDirection()
        snake_tip = self.state.snakePos[0]
        if direction == move_direction.move_direction.UP:
            # print("Moving up!")
            self.state.snakePos.insert(0, (snake_tip[0] , snake_tip[1]-1) )
        elif direction == move_direction.move_direction.DOWN:
            # print("Moving down!")
            self.state.snakePos.insert(0, ( snake_tip[0],  snake_tip[1]+1) )
        elif direction == move_direction.move_direction.LEFT:
            # print("Moving left!")
            self.state.snakePos.insert(0, ( snake_tip[0]+1,  snake_tip[1]) )
        elif direction == move_direction.move_direction.RIGHT:
            self.state.snakePos.insert(0, ( snake_tip[0]-1,  snake_tip[1]) )
        if len( self.state.snakePos) > 1:
             self.state.snakePos.pop()    
 
      
        
        