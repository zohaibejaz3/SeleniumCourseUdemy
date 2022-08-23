import pytest

"""
How to run:
1.0. go into terminal
2.0. cd to module
3.0. run command "pytest [name of script].py [-v for verbose] [-s for print] for entire file
3.1. run command "pytest [name of script].py::[name of the method] [-v for verbose] [-s for print] for one method
"""


# using conftest.py for both fixtures

def test_method_c(onetime_setup, setup):  # same name as the fixture method needs to be passed
    print("Running test method C")


def test_method_d(onetime_setup, setup):  # if fixture method name is not passed, it will not be used.
    print("Running test method D")
