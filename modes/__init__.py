# Mode base class
class GameMode:
    """Base class for all game modes"""
    
    name = "Default Mode"
    description = "Default game mode description"
    
    def get_name(self):
        return self.name
    
    def get_description(self):
        return self.description
    
    def on_start(self):
        """Called when this mode is selected and started"""
        pass
