"""
Sample Input

9 6 2015
6 6 2015
Sample Output

45

"""

import sys


d1,m1,y1 = map(int, raw_input().strip().split())

d2,m2,y2 = map(int, raw_input().strip().split())

if y1 > y2:
    print 10000
elif y1 == y2 and m1 > m2:
    print 500*(m1-m2)
elif y1 == y2 and m1 == m2 and d1 > d2:
    print 15*(d1-d2)
else:
    print 0
