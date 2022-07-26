import unittest


class LoginTestCase(unittest.TestCase):
    """
    Demo class to understand the Unit Test
    """
    @classmethod
    def setUpClass(cls):
        #this will setup only one time
        #this is class method
        print("Login Test setUpClass method executed")

    def setUp(self):
        print(" Login Test data initalized......")

    def test_method1(self):
        print("Login Test method working......")
    def tearDown(self):
        print(" Login Test close Testing.......")

    @classmethod
    def tearDownClass(self):
        print(" Login Test tearDownClass is started.......")


unittest.main()
