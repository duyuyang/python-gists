n = 3
numbers = []
for i in range(10**(n-1), 10**n):
    print list(str(i))
    if sum(map(int, list(str(i)))) > 9:
        numbers.append(i)
print sum(numbers)
