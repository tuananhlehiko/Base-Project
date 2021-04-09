from unittest.case import TestCase
import HtmlTestRunner
import unittest
import os

# HEADING TITLE CONTENT Testcase
from TopAsia.src.TestCase.Heading_Title_Content.GameLobby import *
from TopAsia.src.TestCase.Heading_Title_Content.CasinoLobby import *
# URL FORMAT Testcase
from TopAsia.src.TestCase.Url_Format.GameLobby import *
from TopAsia.src.TestCase.Url_Format.CasinoLobby import *
# LOGIN SIGNUP Testcase
from TopAsia.src.TestCase.Login.Login import *
from TopAsia.src.TestCase.Login.Signup import *
# UPDATE USER INFO Testcase
from TopAsia.src.TestCase.UserInformation.UpdateInformation import *
from TopAsia.src.TestCase.UserInformation.ChangePassword import *
# RECHARGE FLOW
from TopAsia.src.TestCase.Recharge.Bank import *
from TopAsia.src.TestCase.Recharge.Momo import *
from TopAsia.src.TestCase.Recharge.Card import *
from TopAsia.src.TestCase.Recharge.Paywin import *



game_url_test = unittest.TestLoader().loadTestsFromTestCase(GameLobby)
casino_url_test = unittest.TestLoader().loadTestsFromTestCase(CasinoLobby)
game_heading_test = unittest.TestLoader().loadTestsFromTestCase(GameLobbyHeadingTitle)
casino_heading_test = unittest.TestLoader().loadTestsFromTestCase(CasinoLobbyHeadingTitle)
loginflow = unittest.TestLoader().loadTestsFromTestCase(LoginFlow)
signupflow = unittest.TestLoader().loadTestsFromTestCase(SignupFlow)
updateinfo = unittest.TestLoader().loadTestsFromTestCase(UpdateUserInformation)
changepass = unittest.TestLoader().loadTestsFromTestCase(ChangePasswordFlow)
rechargebank = unittest.TestLoader().loadTestsFromTestCase(RechargeBanksFlow)
rechargemomo = unittest.TestLoader().loadTestsFromTestCase(RechargeMomoFlow)
rechargecard = unittest.TestLoader().loadTestsFromTestCase(RechargeCardsFlow)
rechargepaywin = unittest.TestLoader().loadTestsFromTestCase(RechargePaywinFlow)
# unittest.TextTestRunner().run(main)

# # Create test_suite
# test_suite = unittest.TestSuite([casino_heading_test, game_heading_test, casino_url_test, game_url_test])
# test_suite = unittest.TestSuite([casino_heading_test, game_heading_test])
test_suite = unittest.TestSuite([game_heading_test])
unittest.TextTestRunner().run(test_suite)