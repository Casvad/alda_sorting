import unittest

from heap.algorithm import heap_sort
from utils.constants_test import arrays, expected


class AlgorithmTest(unittest.TestCase):
    def test_heap_sort(self):
        for i in range(len(arrays)):
            array = arrays[i]
            result = heap_sort(array)
            self.assertTrue(result, expected[i])


if __name__ == "__main__":
    unittest.main()
