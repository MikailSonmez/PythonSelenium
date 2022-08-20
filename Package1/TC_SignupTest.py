import unittest


class SignupTest(unittest.TestCase):

    def test_signByEmail(self):
        print("This is sign up by email test")
        self.assertTrue(True)

    def test_signByFacebook(self):
        print("This is sign up by facebook test")
        self.assertTrue(True)

    def test_signByTwitter(self):
        print("This is sign up by twitter test")
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()