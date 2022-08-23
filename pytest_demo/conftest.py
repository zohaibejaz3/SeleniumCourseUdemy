"""
The purpose of this file "conftest.py" is to make sure setup and teardown methods can be executed for ALL modules in
this path e.g. lesson_1.py and lesson_2.py will both execute their fixture methods from this file.

TLDR; common fixture methods can be used from this file for all tests
"""

import pytest


@pytest.fixture(scope="module")  # decorator # scope argument tells fixture when to execute. Default -> scope="function"
def onetime_setup():
    print("--- Run ONCE before all tests! ---")
    yield  # anything above will run before and anything after will run after EVERY test
    print("--- Run ONCE after all tests! ---")


@pytest.fixture()  # decorator
def setup():
    print("--- Run before every method! ---")
    yield  # anything above will run before and anything after will run after EVERY test
    print("--- Run after every method! ---")

# -- how to add CLI arguments to make the code a little smarter --
# no idea. The tutorial used a method that didnt work at all.
