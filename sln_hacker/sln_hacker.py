'''Second largest number'''

class Secondlargest(object):
    '''class for second largest number'''
    def __init__(self):
        '''initiate the number and a list'''
        self.num = int(raw_input())
        self.nlist = map(int, (raw_input().split()))

    def get_secondlargest(self):
        '''return the second largest number'''
        my_list = list(set(self.nlist))
        my_list.sort()
        return my_list[-2]

    def main(self):
        '''print the thing'''
        print self.get_secondlargest()

if __name__ == '__main__':
    SL = Secondlargest()
    SL.main()
