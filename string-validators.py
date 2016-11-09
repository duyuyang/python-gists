class StringValidators(object):
    def __init__(self):
        self.inp = raw_input()

    def check_is_any_num(self, inp):
        for i in inp:
            if i.isalnum():
                return True
        return False


    def check_is_any_pha(self, inp):
        for i in inp:
            if i.isalpha():
                return True
        return False

    def check_is_any_digit(self, inp):
        for i in inp:
            if i.isdigit():
                return True
        return False

    def check_is_any_lower(self, inp):
        for i in inp:
            if i.islower():
                return True
        return False

    def check_is_any_upper(self, inp):
        for i in inp:
            if i.isupper():
                return True
        return False

    def print_thing(self, arg):
        if arg:
            print "True"
        else:
            print "False"


    def main(self):
        self.print_thing(self.check_is_any_num(self.inp))
        self.print_thing(self.check_is_any_pha(self.inp))
        self.print_thing(self.check_is_any_digit(self.inp))
        self.print_thing(self.check_is_any_lower(self.inp))
        self.print_thing(self.check_is_any_upper(self.inp))

if __name__ == '__main__':
    SV = StringValidators()
    SV.main()
