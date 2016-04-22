'''Hackerrank swap case'''

class Swapcasehacker(object):
    '''class for swap case'''
    def __init__(self):
        '''initiate a input'''
        self.custom_input = raw_input()
	
    def get_swapcased(self):
        '''swap case for the custom input'''
        return self.custom_input.swapcase()

    def main(self):
        '''print the thing'''
        print self.get_swapcased()

if __name__ == '__main__':
    SC = Swapcasehacker()
    SC.main()

