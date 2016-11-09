"""Nested list hackerrank"""

class Nestedlists(object):
    """class for nested lists"""
    def __init__(self):
        """initiate the object"""
        self.stu_sum = int(raw_input())

    def get_students_list(self):
        """return a list of students with grades"""
        stu_list = []
        for i in range(self.stu_sum):
            stu_list.append([raw_input(), raw_input()])
        return stu_list

    def get_second_lowest(self, stu_list):
        """return the second lowest grade from the given list"""
        grade_list = []
        for i in stu_list:
            grade_list.append(i[1])
        grade_no_duplicated = list(set(grade_list))
        grade_float = map(float, grade_no_duplicated)
        grade_float.sort()
        return grade_float[1]

    def get_the_students(self, stu_list, second_lowest):
        """return the names of students"""
        slstu = []
        for stu in stu_list:
            if float(stu[1]) == second_lowest:
                slstu.append(stu[0])
        slstu.sort()
        return slstu

    def main(self):
        """main function"""
        stu_list = self.get_students_list()
        second_lowest = self.get_second_lowest(stu_list)
        names = self.get_the_students(stu_list, second_lowest)
        for i in names:
            print i


if __name__ == "__main__":
    NL = Nestedlists()
    NL.main()
