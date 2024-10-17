import unicurses

from shared.Interfaces import Renderer, InputController
from busines.GameState import GameState  as GS
# Initialize the screen
class ConsoleRenderer(Renderer):
    def __init__(self) -> None:
        self.menuWidth = 10
        self.menuTop = 1 
        self.borderwidth =1
    def renderRectangle(self,width,height, horizontalOffset, verticalOffset, sign = '*'):
        for x in range(width):
          for y in range(height):
              if x == 0 or x == width-1:
                 unicurses.move(y + verticalOffset,x+horizontalOffset)
                 unicurses.addch(sign)
              else:
                  if y == 0 or y == height-1:
                     unicurses.move(y + verticalOffset,x+horizontalOffset)
                     unicurses.addch(sign)    
        unicurses.move(0,0)    
    def renderFrame(self,map,state:GS):
        unicurses.clear()
        self.renderMap(map)
        self.renderMenu(map)
        self.renderSnake(state)
        
        unicurses.refresh()  
    def renderSnake(self, state:GS ):    
        for i,j in state.snakePos:
             self.renderRectangle(1, 1  ,3* (2 * self.borderwidth)+self.menuWidth+i, j + (2 * self.borderwidth), "#") 
    def renderMenu(self,map):
        frame_height = map.height + (2 * self.borderwidth)
        self.renderRectangle(self.menuWidth, frame_height  , 0, self.menuTop)    
    def renderMap(self,map):
        frame_width = map.width + (2 * self.borderwidth)
        frame_height = map.height + (2 * self.borderwidth)
        self.renderRectangle(frame_width,frame_height,self.menuWidth,self.menuTop)     
    
    

from shared import move_direction

class ConsoleInputCollector(InputController):
    def __init__(self) -> None:
        super().__init__()
        self.move_direction = None
        self.char = None
        import threading
        input_thread = threading.Thread(target=self.read_input)
        input_thread.start()

    def read_input(self):
        while True:
            self.char =   unicurses.getch()
            if self.char == 27:
                unicurses.addstr("Game ended") 
                break
            if self.char in [direction.value for direction in move_direction.move_direction]:
                self.move_direction = move_direction.move_direction(self.char)
            unicurses.move(0,0)    
            unicurses.addstr(self.char)     
            
            
    def GetDirection(self):
       return self.move_direction
stdscr = unicurses.initscr()    
unicurses.clear()
unicurses.cbreak()
unicurses.noecho()
unicurses.keypad(stdscr, True)

# Move the cursor to row 10, column 30 and write a character


# Refresh the screen to update the display
unicurses.refresh()

# Wait for user input before ending the session
#unicurses.getch()

# End the window session
#unicurses.endwin()