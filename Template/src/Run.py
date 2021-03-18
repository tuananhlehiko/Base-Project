from unittest.case import TestCase
import HtmlTestRunner
import unittest
import os

from TestCase.GameLobby import GameLobby

main = unittest.TestLoader().loadTestsFromTestCase(GameLobby)
unittest.TextTestRunner().run(main)

# # Create test_suite
# test_suite = unittest.TestSuite([main])