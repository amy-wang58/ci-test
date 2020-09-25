import unittest
import sys
sys.path.append('ci-test/all_funcs')
from all_funcs.func import add, subtract, multiply


class Tests(unittest.TestCase):
    def test_math(self):
        a, b = 1, 2
        add_result = add(a, b)
        subtract_result = subtract(a, b)
        multiply_result = multiply(a, b)
        assert add_result == 3
        assert subtract_result == -1
        assert multiply_result == 2


if __name__ == '__main__':
    unittest.main()
