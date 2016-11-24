import sys


n = int(raw_input().strip())
a = map(int,raw_input().strip().split(' '))

a.sort()
a1 = a[1:]

print a1
maxa1 = a1[-1]-a1[0]

a2 = a[:-1]

print a2
maxa2 = a2[-1]-a2[0]

print maxa1, maxa2

print min(maxa1, maxa2)
