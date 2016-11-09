"""Unit Test cases for Swap Case"""
import unittest
import mock
from swapcase_hacker import Swapcasehacker

class TestSwapCaseTestCase1(unittest.TestCase):
    """Test case 1, a simple string"""
    def setUp(self):
        """mock the input as Www.HackerRank.com"""
        with mock.patch('__builtin__.raw_input',
                        return_value='Www.HackerRank.com'):
            self.swapcasehacker = Swapcasehacker()

    def test_get_swapcased(self):
        """test the result the swap cased string"""
        result = self.swapcasehacker.get_swapcased()
        self.assertEqual('wWW.hACKERrANK.COM', result,
                         'incorrect output: %s' % result)

class TestSwapCaseTestCase2(unittest.TestCase):
    """Test case 2, a longer string with numbers"""
    def setUp(self):
        '''mock the input as hACKERrANK.COM PRESENTS "pYTHONIST 2".'''
        with mock.patch('__builtin__.raw_input',
			            return_value='HackerRank.com presents "Pythonist 2".'):
            self.swapcasehacker = Swapcasehacker()

    def test_get_swapcased(self):
        """test the result the swap cased string"""
        result = self.swapcasehacker.get_swapcased()
        self.assertEqual('hACKERrANK.COM PRESENTS "pYTHONIST 2".', result,
                         'incorrect output: %s' % result)

if __name__ == '__main__':
    unittest.main(verbosity=2)
