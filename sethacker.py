"""Hackerrank question on data set"""

class Sethacker(object):
    """For set functions"""
    def __init__(self):
        self.num1 = raw_input()
        self.lisa = map(int, raw_input().split())
        self.num2 = raw_input()
        self.lisb = map(int, raw_input().split())

    def output_diff(self):
        """output difference"""
        seta, setb = set(self.lisa), set(self.lisb)
        setab, setba = seta.difference(setb), setb.difference(seta)
        setab.update(setba)
        return setab

    def convert_set_to_list(self):
        """convert the set data to list, sort it"""
        my_list = list(self.output_diff())
        my_list.sort()
        return my_list

    def main(self):
        """print out the number in lines"""
        for num in self.convert_set_to_list():
            print num

if __name__ == '__main__':
    SETHACKER = Sethacker()
    SETHACKER.main()
