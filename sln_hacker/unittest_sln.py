'''Unit test for getting the second largest number'''

import unittest
import mock
from sln_hacker import Secondlargest

class TestSecondLargestNumber(unittest.TestCase):
    '''Test case for output of second largest number'''
    def setUp(self):
        '''initiate the object'''
        with mock.patch('__builtin__.raw_input', side_effect=['5', '2 3 6 6 5']):
            self.secondlargestnum = Secondlargest()

    def test_get_secondlargest(self):
        '''test the result for secondlargest'''
        output = self.secondlargestnum.get_secondlargest()
        self.assertEqual(5, output, 'Incorrect second largest number %s' % output)

if __name__ == '__main__':
    unittest.main(verbosity=2)
