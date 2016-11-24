a = set([1, 2, 3])
b = [4, 5]

s = a.union(b)
print s == set([1, 2, 3, 4, 5])
a.update(b)
print a == set([1, 2, 3, 4, 5])


a = set([1, 2, 3])
b = [3, 4]
s = a.intersection(b)
print s == set([3])
a.intersection_update(b)
print a == set([3])


a = set([1, 2, 3])
b = [3, 4]
s = a.difference(b)
print s == set([1, 2])
a.difference_update(b)
print a == set([1, 2])

a = set([1, 2, 3])
b = [3, 4]
s = a.symmetric_difference(b)
print s == set([1, 2, 4])
a.symmetric_difference_update(b)
print a == set([1, 2, 4])
