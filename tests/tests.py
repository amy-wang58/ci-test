import unittest
from funcs.func import add


class Tests(unittest.TestCase):
    def test_add(self):
        a, b = 1, 2
        result = add(a, b)
        assert result == 3


if __name__ == '__main__':
    unittest.main()
