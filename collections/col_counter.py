from collections import Counter

a = [1,1,2,3,4,5,3,2,3,4,2,1,2,3]
print Counter(a)
'''
Counter({2: 4, 3: 4, 1: 3, 4: 2, 5: 1})
'''
print Counter(a).items()
'''
[(1, 3), (2, 4), (3, 4), (4, 2), (5, 1)]
'''

print Counter(a).keys()
'''
[1, 2, 3, 4, 5]
'''

print Counter(a).values()
'''
[3, 4, 4, 2, 1]
'''

n, s, m = raw_input(), raw_input().split(), int(raw_input())
c = Counter(map(int,s))
for i in xrange(m):
