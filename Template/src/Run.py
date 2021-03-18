from unittest.case import TestCase
import HtmlTestRunner
import unittest
import os

from TestCase.GameLobby import *
from TestCase.CasinoLobby import *

game = unittest.TestLoader().loadTestsFromTestCase(GameLobby)
casino = unittest.TestLoader().loadTestsFromTestCase(CasinoLobby)
# unittest.TextTestRunner().run(main)

# # Create test_suite
test_suite = unittest.TestSuite([casino])
unittest.TextTestRunner().run(test_suite)