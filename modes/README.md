# Game Modes for Animal Racers

This folder contains game mode scripts that can be dynamically loaded by the game.

## How to Add a New Game Mode

1. Create a new Python file in this folder with the naming convention: `<mode_name>_mode.py`
   - Example: `capture_the_flag_mode.py`

2. Your mode class must:
   - Import the `GameMode` base class from `modes`
   - Inherit from `GameMode`
   - Define a `name` class attribute (display name)
   - Define a `description` class attribute (shown in the menu)
   - Optionally implement the `on_start()` method for mode-specific initialization

3. The class name should be the mode name in PascalCase followed by "Mode"
   - Example: `capture_the_flag_mode.py` → `CaptureTheFlagMode`

## Example Template

```python
# my_new_mode_mode.py
from modes import GameMode

class MyNewModeMode(GameMode):
    name = "My New Mode"
    description = "Description of what this mode does."
    
    def on_start(self):
        # Mode-specific initialization code
        pass
```

## Available Base Class Methods

- `get_name()`: Returns the mode name
- `get_description()`: Returns the mode description
- `on_start()`: Called when the mode is selected and the game starts

## Current Modes

- `classic_mode.py` - Classic Race: Standard racing mode
- `time_trial_mode.py` - Time Trial: Race against the clock
- `survival_mode.py` - Survival: Last car standing wins
