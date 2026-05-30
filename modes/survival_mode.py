# Survival mode - last car standing wins
from modes import GameMode

class SurvivalMode(GameMode):
    name = "Survival"
    description = "Last car standing wins! Avoid elimination."
    
    def on_start(self):
        # Survival mode specific initialization
        pass
