'''Unit test for list comprehensions'''
import unittest
import mock
from listc_hacker import Listchacker

class TestListComprehensionMethods(unittest.TestCase):
    '''Test case for list comprehensions'''
    def setUp(self):
        '''Mock the raw_input and initial the listchacker object'''
        with mock.patch('__builtin__.raw_input', side_effect=[1, 1, 1, 2]):
            self.listchacker = Listchacker()

    def test_get_filtered_coordinates(self):
        '''input X Y Z and test all the possible coordinates'''
        output = self.listchacker.get_filtered_coordinates()
        self.assertEqual([[0, 0, 0],
                          [0, 0, 1],
                          [0, 1, 0],
                          [1, 0, 0],
                          [1, 1, 1]],
                         output,
                         'Incorrect printing all the coordinates: %s' % output)

if __name__ == '__main__':
    unittest.main(verbosity=2)
