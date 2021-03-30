from unittest.case import TestCase
import HtmlTestRunner
import unittest
import os

# HEADING TITLE CONTENT Testcase
from TestCase.Heading_Title_Content.GameLobby import *
from TestCase.Heading_Title_Content.CasinoLobby import *
# URL FORMAT Testcase
from TestCase.Url_Format.GameLobby import *
from TestCase.Url_Format.CasinoLobby import *
# URL FORMAT Testcase
from TestCase.Login.Login import *



game_url_test = unittest.TestLoader().loadTestsFromTestCase(GameLobby)
casino_url_test = unittest.TestLoader().loadTestsFromTestCase(CasinoLobby)
game_heading_test = unittest.TestLoader().loadTestsFromTestCase(GameLobbyHeadingTitle)
casino_heading_test = unittest.TestLoader().loadTestsFromTestCase(CasinoLobbyHeadingTitle)
loginflow = unittest.TestLoader().loadTestsFromTestCase(LoginFlow)
# unittest.TextTestRunner().run(main)

# # Create test_suite
# test_suite = unittest.TestSuite([casino_heading_test, game_heading_test, casino_url_test, game_url_test])
# test_suite = unittest.TestSuite([casino_heading_test, game_heading_test])
test_suite = unittest.TestSuite([loginflow])
unittest.TextTestRunner().run(test_suite)