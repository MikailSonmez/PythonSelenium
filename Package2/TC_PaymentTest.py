import unittest


class PaymentTest(unittest.TestCase):
    def test_paymentindolar(self):
        print("This is payment in dolar test")
        self.assertTrue(True)

    def test_paymentinturkishlira(self):
        print("This is payment in turkishlira test")
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()
