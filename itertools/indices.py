from __future__ import division
from itertools import combinations


print list(combinations('aacd', 2))

n, s, m = raw_input(), raw_input().split(), raw_input()

l = list(combinations(s, int(m)))
'''
[('a', 'a'), ('a', 'c'), ('a', 'd'), ('a', 'c'), ('a', 'd'), ('c', 'd')]
'''


print round(len(filter(lambda x: 'a' in x, l))/len(l), 4)
