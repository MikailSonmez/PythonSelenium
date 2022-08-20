import pytest


@pytest.yield_fixture()
def setup():
    print("Opening URL to Login")
    yield
    print("Closing browser after Login")


def test_signByEmail(setup):
    print("This is sign up by email test")


def test_signByFacebook(setup):
    print("This is sign up by facebook test")
