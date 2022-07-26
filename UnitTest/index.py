import unittest
class DemoTestCase(unittest.TestCase):
    """
    Demo class to understand the Unit Test
    """
    @classmethod
    def setUpClass(cls):
        #this will setup only one time
        #this is class method
        print("setUpClass method executed")
        cls.a = 10

    def setUp(self):
        print("data initalized......")

    def test_method1(self):
        DemoTestCase.a 
        print("test1 method working......")

    def test_method2(self):
        print("a = ", DemoTestCase.a)
        print("test2 method working......")

    @classmethod
    def update(cls, value):
        cls.a = value
    def test_method3(self):
        print("test3 method working......")

    def test_method3(self):
        print("test2 method working......")
        10/0

    def tearDown(self):
        print("close Testing.......")
    @classmethod
    def tearDownClass(self):
        print("tearDownClass is started.......")

unittest.main()
