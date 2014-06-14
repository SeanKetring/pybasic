"""Unittest for the arm"""

import unittest

import arm
import lib

class TestExtend(unittest.TestCase):
    
    """Test extedning the robot's arm"""
    
    def setUp(self):
        """buid an arm object"""

        self.arm = arm.Arm()


    def test_basic(self):

        """test bassic extension"""
        self.arm.arm_state = "retracted"
        self.arm.extend()
        assert self.arm.arm_state == "extended"

class TestExtend(unittest.TestCase):
    
    """Test extedning the robot's arm"""
    
    def setUp(self):
        """buid an arm object"""

        self.arm = arm.Arm()


    def test_basic(self):

        """test bassic extension"""
        self.arm.arm_state = "extended"
        self.arm.retract()
        assert self.arm.arm_state == "Retracted"


