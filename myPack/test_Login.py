import pytest


@pytest.yield_fixture()
def setup():
    print("Opening URL to Login")
    yield
    print("Closing browser after Login")


def test_loginByEmail(setup):
    print("This is login by email test")


def test_loginByFacebook(setup):
    print("This is login by facebook test")
