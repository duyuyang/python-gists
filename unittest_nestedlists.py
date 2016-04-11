"""Unit test for Nested lists"""
import unittest
import mock
from nestedlists_hacker import Nestedlists

class TestNestedLists(unittest.TestCase):
    """Test case class"""
    def setUp(self):
        """initiate the object"""
        with mock.patch('__builtin__.raw_input',
                        return_value='5'):
            self.nestedlists = Nestedlists()

    def test_get_students_list(self):
        """Test the length of students list"""
        with mock.patch('__builtin__.raw_input',
                        side_effect=['Harry', '37.21',
                                     'Berry', '37.21',
                                     'Tina', '37.2',
                                     'Akriti', '41',
                                     'Harsh', '39']):
            stu_list = self.nestedlists.get_students_list()
        self.assertEqual(5, len(stu_list),
                         'incorrect length of stu list')
        self.assertEqual(2, len(stu_list[0]),
                         'incorrect length of per student')

    def test_get_second_lowest(self):
        """test the second lowest score"""
        mock_stu_list = [['Harry', '37.21'],
                         ['Berry', '37.21'],
                         ['Tina', '37.2'],
                         ['Akriti', '41'],
                         ['Harsh', '39']]
        second_lowest = self.nestedlists.get_second_lowest(mock_stu_list)
        self.assertEqual(37.21, second_lowest,
                         'incorrect score: %s' % second_lowest)

    def test_get_the_students(self):
        """test a list of student names who get the second lowest score"""
        mock_stu_list = [['Harry', '37.21'],
                         ['Berry', '37.21'],
                         ['Tina', '37.2'],
                         ['Akriti', '41'],
                         ['Harsh', '39']]
        mock_grade = 37.21
        slstu = self.nestedlists.get_the_students(mock_stu_list, mock_grade)
        self.assertEqual(2, len(slstu),
                         'incorrect length of students')
        self.assertEqual(['Berry', 'Harry'], slstu,
                         'incorrect student names: %s' % slstu)

if __name__ == '__main__':
    unittest.main(verbosity=2)
