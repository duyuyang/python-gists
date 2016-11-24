'''
Sample Input

9
1 2 3 4 5 6 7 8 9
10
pop
remove 9
discard 9
discard 8
remove 7
pop
discard 6
remove 5
pop
discard 5

'''
'''
n = input()
s = set(map(int, raw_input().split()))

for _ in range(int(input())):
    x = raw_input().split()
    eval('s.{0}({1})'.format(*x+['']))
print sum(s)
'''
s = set([1, 2, 3, 4, 5])
x = ['remove', '3']
eval('s.{0}({1})'.format(*x+['']))
print s
