# Time trial mode - race against the clock
from modes import GameMode

class TimeTrialMode(GameMode):
    name = "Time Trial"
    description = "Race against the clock! Beat your best time."
    
    def on_start(self):
        # Time trial mode specific initialization
        pass
