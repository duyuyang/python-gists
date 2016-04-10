"""Unit test for Hackerrank"""
import unittest
import mock
from set_hacker import Sethacker

class TestSetMethods(unittest.TestCase):
    """Test case for set methods"""
    def setUp(self):
        """Mock the raw_input and create Sethacker object"""
        with mock.patch('__builtin__.raw_input', side_effect=['4', '2 4 5 9', '4', '2 4 11 12']):
            self.sethacker = Sethacker()

    def tearDown(self):
        """Remove sethacker object"""
        self.sethacker = None

    def test_outputdiff(self):
        """test the output of different set"""
        output = self.sethacker.output_diff()
        self.assertTrue(isinstance(output, set), 'The type of output is not set %s' % type(output))
        self.assertEqual({5, 9, 11, 12},
                         output,
                         "incorret output set %s" % output)

    def test_convert_set_to_list(self):
        """test the sorted list"""
        converted_list = self.sethacker.convert_set_to_list()
        self.assertEqual([5, 9, 11, 12],
                         converted_list,
                         "incorret output sorted list %s" % converted_list)

if __name__ == '__main__':
    unittest.main(verbosity=2)
