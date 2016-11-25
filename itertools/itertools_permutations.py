from itertools import permutations

print list(permutations([1, 2, 3]))
'''
[(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]
'''

print list(permutations(['1','2','3'],2))
'''
[('1', '2'), ('1', '3'), ('2', '1'), ('2', '3'), ('3', '1'), ('3', '2')]
'''
print list(permutations('abc',3))
'''
[('a', 'b', 'c'), ('a', 'c', 'b'), ('b', 'a', 'c'), ('b', 'c', 'a'), ('c', 'a', 'b'), ('c', 'b', 'a')]
'''

A = [''.join(x) for x in map(list, list(permutations('HACK', 2)))]
A.sort()
for i in A:
    print i
