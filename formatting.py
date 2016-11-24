'''
a = int(raw_input())

width = bin(a)
for i in xrange(1, a+1):
    print "%s  %s  %s  %s" % (i, oct(i)[1:], hex(i)[2:], bin(i)[2:])
'''

n = int(raw_input())
width = len("{0:b}".format(n))
for i in xrange(1,n+1):
  print "{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(i, width=width)
