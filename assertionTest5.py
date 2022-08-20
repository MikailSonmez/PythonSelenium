# Relational comparison

import unittest

from selenium import webdriver


class Test(unittest.TestCase):
    def testName(self):
        self.assertLessEqual(100, 100)
        # self.assertLess(10, 100)

        # self.assertGreater(100, 10)
        # self.assertGreaterEqual(100, 100)


if __name__ == "__main__":
    unittest.main()
