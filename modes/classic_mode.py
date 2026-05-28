# Classic racing mode - first to finish wins
from modes import GameMode

class ClassicMode(GameMode):
    name = "Classic Race"
    description = "Standard racing mode. First to cross the finish line wins!"
    
    def on_start(self):
        # Classic mode specific initialization
        pass
