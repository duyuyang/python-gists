"""
3
11 2 4
4 5 6
10 8 -12

"""
n = int(raw_input().strip())
a = []
b = []
#for a_i in xrange(n):
#    a_temp = map(int,raw_input().strip().split(' '))
#    a.append(a_temp)
for i in xrange(n):
    x = map(int, raw_input().split())
    a.append(x[i])
    b.append(x[-(i+1)])

print abs(sum(a) - sum(b))
