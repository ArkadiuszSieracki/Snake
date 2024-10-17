import busines.Map as MMap
import busines.Game as Gam
from busines.GameState import GameState  as GS
from console.ConsoleSnake import ConsoleRenderer as Csr
import console
import console.ConsoleSnake
print("Main")
def start_legacy():
    map = MMap.Map(40,10)
    rend = Csr()
    state = GS()
    collector =console.ConsoleSnake.ConsoleInputCollector()
    game = Gam.Game(map,rend,state, collector)
    game.play()
def main():
    from bootstrap import GameModule
    from injector import Injector, Module, Binder
    injector = Injector([GameModule()])
    game_instance = injector.get(Gam.Game)
    game_instance.play()
    return 1
if __name__ == "__main__":
    main()    