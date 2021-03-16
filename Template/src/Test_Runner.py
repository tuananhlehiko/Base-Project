from unittest.case import TestCase
import HtmlTestRunner
import unittest
import os

from pages.components.main import Homepage_Test

# Get directory to export report file
dir = os.getcwd()

# Get all test case from class Homepage_Test
main = unittest.TestLoader().loadTestsFromTestCase(Homepage_Test)


# Create test_suite
test_suite = unittest.TestSuite([main])

folder = 'Homepage_Test'

# Open report file
output_file = open(dir + "\Homepage Test.html", "w")

# Configure HtmlTestRunner options
runner = HtmlTestRunner.HTMLTestRunner(
    stream=output_file, report_title='Test report', descriptions='Acceptance Test')

# Run test_suite using html test runner
runner.run(test_suite)
