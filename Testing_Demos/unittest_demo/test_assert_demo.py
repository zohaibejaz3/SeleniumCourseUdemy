import unittest


class AssertDemo(unittest.TestCase):

    def test_assert_true_false(self):
        a = True
        self.assertTrue(a, "A is not true")
        b = False
        self.assertFalse(b, "B is not false")

    def test_assert_equal(self):
        a = "Test"
        b = "hello"
        self.assertEqual(a, b, "A and B are not equal")


if __name__ == '__main__':
    unittest.main(verbosity=2)
