import unittest

class Apptesting(unittest.TestCase):

    @unittest.SkipTest  #  decorator
    def test_search(self):
        print("This is search test")

    @unittest.skip("I am skipping this test method because it is not yet ready")
    def test_advancedsearch(self):
        print("This is adv search method")

    @unittest.skipIf(1==1, " ONE IS EQUALS TO ONE")
    def test_prepaidrecharge(self):
        print("This is pre-paid recharge")

    def test_postpaidreacharge(self):
        print("This is post-paid recharge")

    def test_loginbygmail(self):
        print("This is login by email")

    def test_loginbytwitter(self):
        print("This is login by twitter")

if __name__ == "__main__":
    unittest.main()