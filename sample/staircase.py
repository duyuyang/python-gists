import sys

class Staircase(object):
    def __init__(self):
        '''initiate a input'''
        self.custom_input = int(raw_input())

    def generate_staircase(self):
        for line in range(self.custom_input):
            space = self.custom_input - line - 1
            mark = line + 1
            my_l = space*" " + mark*"#"
            sys.stdout.write(my_l+'\n')

    def main(self):
        '''print the thing'''
        self.generate_staircase()

if __name__ == '__main__':
    SC = Staircase()
    SC.main()
