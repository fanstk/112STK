# Survival mode - last car standing wins
from modes import GameMode

class SurvivalMode(GameMode):
    name = "Survival"
    description = "Last car standing wins! Avoid obstacles and powerup attacks. Don't get eliminated!"
    
    def on_start(self):
        # Survival mode specific initialization
        # In survival mode, we keep all players but add hazards
        from Game import Game
        # Keep the selected number of players but make it more challenging
        print(f"Survival Mode: {Game.numPlayers} players will compete until one remains")
