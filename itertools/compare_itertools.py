from itertools import combinations_with_replacement, combinations, product, permutations


A = ['1','2','3']
print list(permutations(A, 2))
'''
[('1', '2'), ('1', '3'),
 ('2', '1'), ('2', '3'),
 ('3', '1'), ('3', '2')]

'''
print list(product(A, repeat = 2))
'''
[('1', '1'), ('1', '2'), ('1', '3'),
 ('2', '1'), ('2', '2'), ('2', '3'),
 ('3', '1'), ('3', '2'), ('3', '3')]
'''

print list(combinations(A, 2))
'''
[('1', '2'), ('1', '3'), ('2', '3')]
'''

print list(combinations_with_replacement(A, 2))
'''
[('1', '1'), ('1', '2'), ('1', '3'),
 ('2', '2'), ('2', '3'), ('3', '3')]
'''

A = [[1,2,3],[3,4,5]]
print list(product(*A))
'''
[(1, 3), (1, 4), (1, 5),
 (2, 3), (2, 4), (2, 5),
 (3, 3), (3, 4), (3, 5)]
'''


from itertools import groupby

print [list(g) for k, g in groupby('AAAABBBCCD')]
'''
[['A', 'A', 'A', 'A'], ['B', 'B', 'B'], ['C', 'C'], ['D']]
'''
