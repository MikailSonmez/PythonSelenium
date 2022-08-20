import pytest


@pytest.yield_fixture()
def setup():
    print("Once Before every method")
    yield
    print("Once After every method")


def testMethod1(setup):
    print("This is test method 1")


def testMethod2(setup):
    print("This is test method 2")
