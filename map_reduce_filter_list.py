def double(x):
  return x * 2

def is_even(x):
  return x % 2 is 0

def sum(x, y):
  return x + y

a = xrange(1, 10)

# apply same function on a list, return the modified list
print "map"
print map(double, a)
print [double(x) for x in a]
print map(lambda x: double(x), a)

# Filter items out of a list, return filtered list
print "filter"
print filter(is_even, a)
print [x for x in a if is_even(x)]

print "reduce"
print reduce(sum, a)

my_sum = lambda x,y: x + y

mx = lambda x,y:x if x>y else y
print mx(8, 5)


# Map can be applied to multiple list
a = [1, 2, 3, 4]
b = [12, 14, 3, 19]
c = [-1,-4,5,9]
print map(lambda x,y,z:x+y-z, a,b,c)
