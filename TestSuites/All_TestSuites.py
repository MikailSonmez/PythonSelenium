import unittest
from Package1.TC_LoginTest import LoginTest
from Package1.TC_SignupTest import SignupTest

from Package2.TC_PaymentTest import PaymentTest
from Package2.TC_PaymentReturnsTest import PaymentReturnsTest

# Get all tests from LoginTest,SignUpTest,PaymentTest and PaymentReturnsTest
tc1 = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
tc2 = unittest.TestLoader().loadTestsFromTestCase(SignupTest)
tc3 = unittest.TestLoader().loadTestsFromTestCase(PaymentTest)
tc4 = unittest.TestLoader().loadTestsFromTestCase(PaymentReturnsTest)

# Creating test suites
sanityTestSuite = unittest.TestSuite([tc1, tc2])  # Sanity test suite
functionalTestSuite = unittest.TestSuite([tc3, tc4])  # Functional test suite
masterTestSuite = unittest.TestSuite([tc1, tc2, tc3, tc4])  # Master test suite

unittest.TextTestRunner(verbosity=2).run(masterTestSuite)


if __name__ == "__main__":
    unittest.main()