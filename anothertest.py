import unittest
from anotherfunc import classify


class MyTestCase(unittest.TestCase):
    def test_classify(self):
        array = [40, 40, 40, 80]
        result = classify(array)
        assert result == 40


if __name__ == '__main__':
    unittest.main()
