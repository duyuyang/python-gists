#N = int(raw_input().strip())
N = 3
#length = (N-1)*2*2+1 = N*4-3
import string

alph = string.ascii_lowercase

L = []

for i in xrange(N):
    s = alph[i: N]
    st = s[::-1] + s[1:]
    L.append('-'.join(st).center((N*4-3), '-'))

#for x in (L[::-1][:-1] + L):
#    print x

print '\n'.join(L[:0:-1] + L)
