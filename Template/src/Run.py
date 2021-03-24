from unittest.case import TestCase
import HtmlTestRunner
import unittest
import os

from TestCase.GameLobby_url_format import *
from TestCase.CasinoLobby_url_format import *
from TestCase.GameLobby_heading_title import *

game_url_test = unittest.TestLoader().loadTestsFromTestCase(GameLobby)
casino = unittest.TestLoader().loadTestsFromTestCase(CasinoLobby)
game_heading_test = unittest.TestLoader().loadTestsFromTestCase(GameLobbyHeadingTitle)
# unittest.TextTestRunner().run(main)

# # Create test_suite
test_suite = unittest.TestSuite([game_heading_test])
unittest.TextTestRunner().run(test_suite)