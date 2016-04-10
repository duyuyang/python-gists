'''Hackerrank list comprehensions'''

class Listchacker(object):
    '''list comprehensions class'''
    def __init__(self):
        self.xint = int(raw_input())
        self.yint = int(raw_input())
        self.zint = int(raw_input())
        self.nint = int(raw_input())

    def get_filtered_coordinates(self):
        '''return all the possible coordinates, sorted'''
        coordinates = [[i, j, k] for i in range(self.xint + 1)
                       for j in range(self.yint + 1)
                       for k in range(self.zint + 1)
                       if i + j + k != self.nint]
        return coordinates

    def main(self):
        '''print out the final result'''
        print self.get_filtered_coordinates()


if __name__ == '__main__':
    LISTCHACKER = Listchacker()
    LISTCHACKER.main()
