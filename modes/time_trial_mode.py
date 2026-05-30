# Time trial mode - race against the clock
from modes import GameMode

class TimeTrialMode(GameMode):
    name = "Time Trial"
    description = "Race against the clock! Beat your best time. No opponents, just you and the track."
    
    def on_start(self):
        # Time trial mode specific initialization
        # Set numPlayers to 1 (only the human player)
        from Game import Game
        Game.numPlayers = 1
        print("Time Trial Mode: Only player car will be spawned")
