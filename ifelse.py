#!/bin/python

import sys


N = int(raw_input().strip())

if N % 2 is 1:
    print "Weird"
elif N % 2 is 0 and N in range(2, 6):
    print "Not Weird"
elif N % 2 is 0 and N in range(6, 21):
    print "Weird"
elif N % 2 is 0 and N > 20:
    print "Not Weird"
else:
    sys.exit(0)
