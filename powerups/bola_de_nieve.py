# Bola de nieve (Red Shell inspired) powerup
# A white sphere that targets and hits the leading opponent

from panda3d.core import *
from direct.interval.IntervalGlobal import *
import math

class BolaDeNieve:
    """
    A homing projectile powerup similar to Mario Kart's red shell.
    When activated, it automatically targets and hits the car in first place.
    """
    
    name = "bola_de_nieve"
    display_name = "Bola de Nieve"
    description = "A homing snowball that automatically targets and hits the leading opponent!"
    duration = 0  # Instant effect when it hits
    color = (1, 1, 1, 1)  # White sphere
    
    def __init__(self, game, owner_car):
        self.game = game
        self.owner_car = owner_car
        self.active = False
        self.model = None
        self.target_car = None
        self.speed = 25  # Speed of the projectile
        self.hit_timeout = 5.0  # Max time before it disappears
        
    def activate(self):
        """Activate the powerup - find target and launch"""
        if not self.game or not self.owner_car:
            return
            
        # Find the car in first place (excluding the owner)
        cars = self.game.cars
        if len(cars) < 2:
            return
            
        # Sort cars by lap and checkpoint to find leader
        sorted_cars = sorted(
            [c for c in cars if c.id != self.owner_car.id],
            key=lambda c: (c.currLap, sum(c.passedCheckpoints)),
            reverse=True
        )
        
        if not sorted_cars:
            return
            
        self.target_car = sorted_cars[0]
        self.active = True
        
        # Create the white sphere model
        self.model = loader.loadModel("models/sphere")
        self.model.reparentTo(self.game.render)
        self.model.setScale(0.5)
        self.model.setColor(1, 1, 1, 1)  # White color
        
        # Start position: from owner car
        owner_pos = self.owner_car.getPos()
        self.model.setPos(owner_pos)
        
        # Add collision sphere
        col_sphere = CollisionSphere(0, 0, 0, 0.5)
        col_node = self.model.attachNewNode(CollisionNode("bola_de_nieve"))
        col_node.node().addSolid(col_sphere)
        col_node.node().setFromCollideMask(BitMask32.allOff())
        col_node.node().setIntoCollideMask(self.game.colBitMask["wall"])
        
        # Store reference for cleanup
        self.col_node = col_node
        
        # Start tracking task
        self.start_time = globalClock.getFrameTime()
        self.game.taskMgr.add(self.update, "BolaDeNieveUpdate")
        
    def update(self, task):
        """Update the projectile's position to track target"""
        if not self.active or not self.target_car or not self.model:
            self.cleanup()
            return Task.done
            
        # Check timeout
        current_time = globalClock.getFrameTime()
        if current_time - self.start_time > self.hit_timeout:
            self.cleanup()
            return Task.done
            
        # Get target position
        target_pos = self.target_car.getPos()
        current_pos = self.model.getPos()
        
        # Calculate direction to target
        direction = target_pos - current_pos
        direction.normalize()
        
        # Move towards target
        new_pos = current_pos + direction * self.speed * globalClock.getDt()
        self.model.setPos(new_pos)
        
        # Rotate to face direction
        self.model.lookAt(target_pos)
        
        # Check if close enough to hit
        distance = (target_pos - new_pos).length()
        if distance < 1.0:
            self.onHit()
            return Task.done
            
        return Task.cont
        
    def onHit(self):
        """Handle hitting the target"""
        if self.target_car:
            # Stop the target car temporarily
            self.target_car.setSpeed(0, 0)
            self.target_car.setAcceleration(0, 0)
            
            # Visual feedback - flash red
            flash_interval = LerpColorScaleInterval(
                self.target_car.model,
                duration=0.3,
                colorScale=(1, 0.5, 0.5, 1),
                blendType="easeInOut"
            )
            restore_interval = LerpColorScaleInterval(
                self.target_car.model,
                duration=0.3,
                colorScale=(1, 1, 1, 1),
                blendType="easeInOut"
            )
            Sequence(flash_interval, restore_interval).start()
            
            if hasattr(self.game, 'printStatements') and self.game.printStatements:
                print(f"Bola de nieve hit car {self.target_car.id}!")
                
        self.cleanup()
        
    def cleanup(self):
        """Clean up the powerup"""
        self.active = False
        
        if self.model:
            if self.col_node:
                self.col_node.removeNode()
            self.model.removeNode()
            self.model = None
            
        # Remove task if still running
        if self.game and hasattr(self.game, 'taskMgr'):
            self.game.taskMgr.remove("BolaDeNieveUpdate")


def create_powerup(game, owner_car):
    """Factory function to create a BolaDeNieve instance"""
    return BolaDeNieve(game, owner_car)
