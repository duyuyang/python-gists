from itertools import combinations, permutations, product

print list(combinations('12345', 2))
'''
[('1', '2'), ('1', '3'), ('1', '4'), ('1', '5'),
 ('2', '3'), ('2', '4'), ('2', '5'),
 ('3', '4'), ('3', '5'),
 ('4', '5')]'''

print list(permutations('12345', 2))
'''
[('1', '2'), ('1', '3'), ('1', '4'), ('1', '5'),
 ('2', '1'), ('2', '3'), ('2', '4'), ('2', '5'),
 ('3', '1'), ('3', '2'), ('3', '4'), ('3', '5'),
 ('4', '1'), ('4', '2'), ('4', '3'), ('4', '5'),
 ('5', '1'), ('5', '2'), ('5', '3'), ('5', '4')]
'''

print list(product('12345', repeat = 2))
'''
[('1', '1'), ('1', '2'), ('1', '3'), ('1', '4'), ('1', '5'),
 ('2', '1'), ('2', '2'), ('2', '3'), ('2', '4'), ('2', '5'),
 ('3', '1'), ('3', '2'), ('3', '3'), ('3', '4'), ('3', '5'),
 ('4', '1'), ('4', '2'), ('4', '3'), ('4', '4'), ('4', '5'),
 ('5', '1'), ('5', '2'), ('5', '3'), ('5', '4'), ('5', '5')]
'''

A = [1, 1, 3, 3, 3]
print list(combinations(A, 4))
'''
[(1, 1, 3, 3),
 (1, 1, 3, 3),
 (1, 1, 3, 3),
 (1, 3, 3, 3),
 (1, 3, 3, 3)]
'''

a = map(list, list(combinations('HACK', 2)))

from itertools import combinations
v = raw_input().split()
hack = v[0]
n = int(v[1])

def solution(hack, n):
    a = map(list, list(combinations(hack, n)))
    for i in a:
        i.sort()
    a = [''.join(x) for x in a]
    a.sort()
    for i in a:
        print i

for i in range(1, n+1):
    solution(hack, i)


from itertools import combinations


"""Others"""
s , n  = raw_input().split()

for i in range(1, int(n)+1):
    for j in combinations(sorted(s), i):
        print ''.join(j)
