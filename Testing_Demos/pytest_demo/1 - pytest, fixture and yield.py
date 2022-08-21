import pytest

"""
How to run:
1.0. go into terminal
2.0. cd to module
3.0. run command "pytest [name of script].py [-v for verbose] [-s for print] for entire file
3.1. run command "pytest [name of script].py::[name of the method] [-v for verbose] [-s for print] for one method
"""


# Using conftest.py instead
# @pytest.fixture()  # decorator
# def setup():
#     print("--- Run before every method! ---")
#     yield  # anything above will run before and anything after will run after EVERY test
#     print("--- Run after every method! ---")


def test_method_a(setup):  # same name as the fixture method needs to be passed
    print("Running test method A")


def test_method_b():  # if fixture method name is not passed, it will not be used.
    print("Running test method B")
