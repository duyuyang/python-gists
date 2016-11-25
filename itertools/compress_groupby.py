from itertools import groupby

print [list(g) for k, g in groupby('AAAABBBCCD')]
'''
[['A', 'A', 'A', 'A'], ['B', 'B', 'B'], ['C', 'C'], ['D']]
'''

print ' '.join(map(str, [(len(list(g)), int(k)) for k, g in groupby('1222311')]))
