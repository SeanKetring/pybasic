"""Test cases for lib module"""

import unittest
import logging

import lib

class TestGetLogger(unittest.TestCase):

    """Test cases for get logger function."""

    def test_type(self):
        """Test the type of the logger object"""

        assert type(lib.get_logger()) is logging.Logger
    

