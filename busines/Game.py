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
from datetime import datetime, timedelta
from shared.MenuState import MenuState
class Game:
    @inject
    def __init__(self, map: Map, renderer: interfacces.Renderer,state: GS , input_collector:interfacces.InputController, game_settings: GameSettings, menu_state: MenuState) -> None:
        self.map = map
        self.renderer : interfacces.Renderer = renderer
        self.state : GS= state
        self.input_collector = input_collector
        self.game_settings = game_settings
        self.input_thread = None
        self.menu_state: MenuState = menu_state
        self.Run = True
    def play(self):
        import threading
        self.input_thread = threading.Thread(target=self.renderLoop)
        self.input_thread.start()
        while self.Run :
            if self.has_happend(event_type.MAIN_MENU):
               self.display_menu()  
            else:
               self.dispalay_game()    
            time.sleep(0.5)   
    def display_menu(self):  
        self.menu_state.MenuPosition = self.input_collector.GetLastKey()
        if  self.menu_state.MenuPosition == 49:
            self.reset_state()
            self.state.lives = self.game_settings.lives 
            self.map.monkeys.clear()
            self.locate_new_food()     
            self.state.events[event_type.GAME_READY] = game_event(event_type.GAME_READY, datetime.now())
        elif self.menu_state.MenuPosition == 50:
            #exit game1
            self.Run  = False
            self.input_collector.Stop()
            import sys
            sys.exit(0)    
    def dispalay_game(self):
            if (self.has_happend(event_type.GAME_READY)) :
                self.handle_game_ready()
            elif (self.has_happend(event_type.SNAKE_MOVE)):    
               self.handle_snake_move()
            elif (self.has_happend(event_type.SELF_HIT) or self.has_happend(event_type.WALL_HIT) ):
                self.handle_colision()   
            self.detect_food_eaten()     
            self.clear_finished_events() 
    def locate_new_food(self):
        import random
        #we need -1 as it is mmax index in the map
        x = random.randint(0,self. map.width-1)
        y = random.randint(0,self. map.height-1) 
        self.map.monkeys.append((x,y))
    def handle_snake_move(self): 
        self.makeMove()
        self.detect_colisions()
        self.detect_food_eaten()
        self.clear_finished_events() 
    def detect_food_eaten(self):
        if not  any(self.state.getSnakeHead() == a for a in self.map.monkeys ):
            if len( self.state.snakePos) > self.state.sneakLength:
                self.state.snakePos.pop()   
        else:
            self.state.sneakLength = self.state.sneakLength +1
            self.map.monkeys.remove(self.state.getSnakeHead())
            self.locate_new_food()
            self.state.points = self.state.points + 10
            self.state.food_eaten = self.state.food_eaten + 1
            
            print("Jummy")         
    def handle_colision(self):
        if self.state.events.__contains__(event_type.GAME_OVER):
            if self.state.events[event_type.SELF_HIT].isFinished():
                self.go_to_main_menu()
            return
        if(self.state.events.__contains__(event_type.SELF_HIT) and self.state.events[event_type.SELF_HIT].isFinished()):
           self.reset_state()
           
        if(self.state.events.__contains__(event_type.WALL_HIT) and self.state.events[event_type.WALL_HIT].isFinished()):
           self.reset_state()
        if(self.state.events.__contains__(event_type.SNAKE_MOVE)):
           self.state.events[event_type.SNAKE_MOVE].MarkAsDone()   
    def go_to_main_menu(self):
         self.state.events[event_type.MAIN_MENU] = game_event(event_type.MAIN_MENU, datetime.now())      

    def handle_game_ready(self):
        if  (self.canMove()):
            self.state.events[event_type.GAME_READY].MarkAsDone()
            self.state.events[event_type.SNAKE_MOVE] = game_event(event_type.SNAKE_MOVE, datetime.now())
        else:
            time.sleep(1)   
    def reset_state(self):
        self.state.events.clear()
        self.state.snakePos.clear()
        self.state.snakePos.append((0,0))   

        self.state.events[event_type.GAME_READY] = game_event(event_type.GAME_READY, datetime.now())      
        self.state.lives = self.state.lives -1   
        self.state.sneakLength = 1
        self.input_collector.Reset()
    def has_happend(self, event:event_type):
        return event in self.state.events          
    def renderLoop(self):
        while self.Run:
          self.renderer.renderFrame(self.map, self.state)        
          time.sleep(1/self.game_settings.frames_per_second)    
           
    def detect_colisions(self):
        from datetime import datetime, timedelta
        snake_tip =  self.state.snakePos[0]
        colisionHappend : bool = False
        if  len(self.state.snakePos) != len(set(self.state.snakePos))  :
            #print("self hit event ") #self hit
            colisionHappend = True  
            self.state.events.clear()
            self.state.events[event_type.SELF_HIT] = game_event(event_type.SELF_HIT, datetime.now(), timedelta(seconds=6))
        if snake_tip[0] < 0 or snake_tip[1] < 0 or snake_tip[0] >= self.map.width  or snake_tip[1] >= self.map.height:
            #print("wall hit event")    
            self.state.events.clear()
            newEvent = game_event(event_type.WALL_HIT, datetime.now(), timedelta(seconds=6))
            self.state.events[event_type.WALL_HIT] =    newEvent  
            colisionHappend = True
        if colisionHappend and self.state.lives == 1:
            self.state.events[event_type.GAME_OVER] = game_event(event_type.GAME_OVER, datetime.now(),timedelta(seconds=6))   

                 
    def canMove(self) -> bool:
        direction = self.input_collector.GetDirection()
        return direction != None
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
        self.state.points = self.state.points + 1  
    def clear_finished_events(self):
        for e in list(self.state.events.values()):
            if(e.isFinished()):
                self.state.events.pop(e.event_type)
            
      
        
        