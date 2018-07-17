import new4
import unittest


class TestOlder(unittest.TestCase):

    def setUp(self):
        """Init"""

    def test_is_older_man(self):
        """Test for is _prime"""
        self.assertEqual(new4.is_older_man([0, 0, 1, 1],
                                           [77, 100, 77, 25], 4), (1, 2))
        self.assertEqual(new4.is_older_man([0, 0, 0, 0],
                                           [77, 100, 77, 25], 4), (0, 4))

    def tearDown(self):
        """Finish"""


if __name__ == "__main__":
    unittest.main()
