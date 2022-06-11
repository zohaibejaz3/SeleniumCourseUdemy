import unittest


class TestCaseDemo():  # will run if unittest.TestCase is inherited

    @classmethod  # decorator or annotation
    def setUpClass(cls) -> None:
        print("--- I will run ONCE before ALL tests ---")

    def setUp(self):
        print("I will run before every test")

    def test_methodA(self):
        print("Running method A")

    def test_methodB(self):
        print("Running method B")

    def tearDown(self):
        print("--- I will run after every test ---")

    @classmethod  # decorator or annotation
    def tearDownClass(cls) -> None:
        print("I will run ONCE after ALL tests")


class AssertDemo(unittest.TestCase):

    def test_AssertTrueFalse(self):
        a = True
        self.assertTrue(a, "'a' is not True")  # message will only show if the assert fails
        b = False
        self.assertFalse(b, "'b' is not False")

    def test_AssertEquals(self):
        a = 'Test'
        b = 'Test'
        self.assertEqual(a, b, f"{a} is not equals to {b}")


if __name__ == '__main__':
    unittest.main(verbosity=2)
