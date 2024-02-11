import unittest

from quick.algorithm import quick_sort
from utils.constants_test import arrays, expected


class AlgorithmTest(unittest.TestCase):
    def test_quick_sort(self):
        for i in range(len(arrays)):
            array = arrays[i]
            result = quick_sort(array)
            self.assertTrue(result, expected[i])


if __name__ == "__main__":
    unittest.main()
