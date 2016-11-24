#https://www.hackerrank.com/challenges/merge-the-tools/forum
#S = raw_input().strip()
#N = int(raw_input().strip())
'''
import collections
S = 'AABCAAAD'
N = 3
if len(S) % N == 0:
    ln = len(S)/N
else:
    ln = len(S)/N + 1

for i in range(0, len(S), N):
    z = collections.OrderedDict.fromkeys(list(S[i:i+N]))
    print ''.join(z.keys())



S, N = raw_input(), int(raw_input())
for part in zip(*[iter(S)] * N):
    d = dict()
    print(''.join([ d.setdefault(c, c) for c in part if c not in d ]))
'''





s = 'AABCAAADA'
k = 3
n = len(s)
for x in xrange(0, n, k):
    slicedStr = s[x : x+k]
    print slicedStr
    uni =[]
    for y in slicedStr:
        if y not in uni:
            uni.append(y)
    #print ''.join(uni)
