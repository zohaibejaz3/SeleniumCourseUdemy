import unittest


class TestCaseDemo(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("#" * 30)
        print("I will run before ALL test.")
        print("#" * 30)

    def setUp(self):
        print("Run once before every test.")

    def test_method_a(self):
        print("running method A.")

    def test_method_b(self):
        print("running method A.")

    def tearDown(self):
        print("I will run after every test.")

    @classmethod
    def tearDownClass(cls):
        print("#" * 30)
        print("I will run after ALL test.")
        print("#" * 30)


if __name__ == '__main__':
    unittest.main(verbosity=2)
