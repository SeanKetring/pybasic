"""Code for controlling the robots arm"""
import lib

class Arm():

    """Code for abstracting the robot's arm."""
    def __init__(self):
        
        """ Get Logger Object """
        self.logger = lib.get_logger()
        self.arm_state = "retracted"
        self.logger.debug("Arm built")

    def extend(self):
        """Extend the robot's arm.""" 
        self.arm_state = "extended"
        self.logger.debug("Extended arm")

    def retract(self):
        """Retract the robot's arm."""
        self.arm_state = "Retracted"
        self.logger.debug("Retracted arm")

            
