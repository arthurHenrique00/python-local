import unittest

from TDD.addn_op import add_op

class MathOp(unittest.TestCase):
    def test_add(self):
        math_add_result = add_op(num_1=5, num_2=10)
        self.assertEqual(math_add_result, 15)

if __name__ == '__main__':
    unittest.main()