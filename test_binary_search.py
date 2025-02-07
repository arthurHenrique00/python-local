import unittest

from binary_search import bin_search

class TeestBubbleSort(unittest.TestCase):
    def test_binary_search(self):
        array = [3, 4, 5, 6, 7, 8, 9]
        find = 4

        result = bin_search(array, find, 0, len(array)-1)
        self.assertEqual(result, 1)

if __name__ == '__main__':
    unittest.main()