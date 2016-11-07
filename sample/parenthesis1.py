import sys, os

my_s = "())"

def parenthes(expr):
    my_l = list(expr)
    new_l = []
    left = 0
    right = 0
    for char in my_l:
        if char == '(':
            left += 1
            new_l.append(char)
        elif char == ')':
            right += 1
            new_l.append(char)

    if left != right:
        return "unbalanced"

    count = 0
    result = []
    for index, char in enumerate(new_l):
        if new_l[index] == '(':
            count += 1
            result.append(count)
        elif new_l[index] == ')':
            if new_l[index-1] == '(':
                result.append(count)
            else:
                count -= 1
                result.append(count)
        if count < 0:
            return "unbalanced"

    output = ''.join(str(x) for x in result)
    return output


print parenthes(my_s)
