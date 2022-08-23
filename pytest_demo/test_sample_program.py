import pytest
from sample_program_class import Arithmetic


# MAKE SURE TO DELETE __init__.py from directory containing tests!!!

# @pytest.mark.usefixtures("onetime_setup", "setup")  # to use fixtures from conftest.py
class TestSampleProgram:

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.obj = Arithmetic(10, 15)

    def test_addition_1(self):
        assert self.obj.add() == 25

    def test_addition_2(self):
        assert self.obj.add() == 20

    def test_subtraction(self):
        assert self.obj.subtract() == 10

    def test_multiplication(self):
        assert self.obj.multiply() == 150

# use pytest-html module to generate reports.
# COMMAND: pytest [test.py] -v --html=[path and/or name].html
# NOTE: using the -s argument gives a "No logs captured" message in the report which is bad, so don't use it!
