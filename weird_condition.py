N = 3

if N % 2 is not 0:
    print "Weird"
elif N % 2 is 0 and N in xrange(2, 6):
    print "Not Weird"
elif N % 2 is 0 and N in xrange(6, 21):
    print "Weird"
elif N % 2 is 0 and N > 20:
    print "Not Weird"
else:
    print "Unknown"
