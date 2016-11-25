from itertools import product

n, v = raw_input().split()

A = [map(int, raw_input().split()[1:]) for i in xrange(int(n))]

print max([sum(map(lambda x: x**2, i))%int(v) for i in list(product(*A))])
