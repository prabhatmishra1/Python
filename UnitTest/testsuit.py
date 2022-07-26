"""
Using Testsuit we run multiple test case
"""
from index import DemoTestCase
from login import LoginTestCase
import unittest
testcase1 = unittest.TestLoader().loadTestsFromTestCase(DemoTestCase)
testcase2 = unittest.TestLoader().loadTestsFromTestCase(LoginTestCase)

all_testcase = unittest.TestSuite([testcase1, testcase2])
unittest.TextTestRunner().run(all_testcase)

