"""
input:
6 3
5 1
2 1
1 1
8 1
10 0
5 0

Output:
29


"""

[n, m] = map(int, raw_input().split())
lis = [map(int, raw_input().split()) for i in xrange(n)]
a = [x[0] for x in lis if x[1] == 0]
b = [x[0] for x in lis if x[1] > 0]
b.sort()
y = n-m-len(a)
luck1 = [ x*(-1) for x in b[:y]]
luck2 = [x for x in b[-(m):]]
luck = sum(luck1) + sum(luck2) + sum(a)
print luck


n,k = map(int, raw_input().strip().split(' '))
luck = 0
contests = []
for i in xrange(n):
    contest = map(int, raw_input().strip().split(' '))
    if contest[1]:
        contests.append(contest)
    else:
        luck += contest[0]

contests.sort(key=lambda x: x[0])

for i in xrange(len(contests)):
    if i < len(contests)-k:
        luck -= contests[i][0]
    else:
        luck += contests[i][0]

print luck
