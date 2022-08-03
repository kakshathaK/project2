'''hi'''
import unittest
import calc

class Calc(unittest.TestCase):
    '''creating calculator class'''

    def test_sample1(self):
        '''comment1'''
        self.assertEqual(calc.add(4, 8), 12)

    def test_sample2(self):
        '''comment2'''
        self.assertEqual(calc.subtract(8, 2), 6)


if __name__ == '__main__':
    unittest.main()
