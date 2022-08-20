import unittest

def setUpModule():  # will be executed before executing any class or any method presen in the test class
    print("setUpModule")

def tearDownModule():  # will be executed after completing everything present in the python module
    print("tearDownModule")


class AppTesting(unittest.TestCase):

    @classmethod
    def setUp(self):
        print("This is login test")

    @classmethod
    def tearDown(self):
        print("This is logout test")

    @classmethod
    def setUpClass(cls):    # Execute once when the class started
        print("Open Application")

    @classmethod
    def tearDownClass(cls):     # Execute once after the class completed
        print("Close Application")

    def test_search(self):
        print("This is search test")

    def test_advancedsearch(self):
        print("This is Advanced search test")

    def test_prepaidRecharge(self):
        print("This is prepaid Recharge test")

    def test_postpaidRecharge(self):
        print("This is post paidRecharge test")

if __name__ == "__main__":
    unittest.main()
