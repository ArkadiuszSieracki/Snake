from shared.GameState import GameState  as GS
import time
import shared.Interfaces as interfacces
from shared import move_direction
from shared.Map import Map
from shared.event_type import event_type
# printing the start time

#import console.ConsoleSnake
# using sleep() to hault the code execution
from injector import inject
class Game:
    @inject
    def __init__(self, map: Map, renderer: interfacces.Renderer,state: GS , input_collector:interfacces.InputController) -> None:
        self.map = map
        self.renderer = renderer
        self.state = state
        self.input_collector = input_collector
    def play(self):
        while True:
            self.makeMove()
            self.detect_colisions()
            self.renderer.renderFrame(self.map,self.state)
            time.sleep(1)    
    def detect_colisions(self):
        snake_tip =  self.state.snakePos[0]
        if  len(self.state.snakePos) != len(set(self.state.snakePos))  :
            print("self hit event ") #self hit
            self.state.events.clear()
            self.state.events.append(event_type.SELF_HIT) 
        if snake_tip[0] < 0 or snake_tip[1] < 0 or snake_tip[0] >= self.map.width  or snake_tip[1] >= self.map.height:
            print("wall hit event")    
            self.state.events.clear()
            self.state.events.append(event_type.WALL_HIT)            
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
 
      
        
        