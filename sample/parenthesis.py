import re

my_s = "((a (+ b) * c)"

def parenthes(expr):
    stack = []
    for c in expr:
        if c == '(':
            stack.append(c)
        elif c == ')':
            if not len(stack):
                return "unbalanced"
            else:
                stackTop = stack.pop()


print parenthes(my_s)
