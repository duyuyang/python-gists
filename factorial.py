# Enter your code here. Read input from STDIN. Print output to STDOUT

#N = int(raw_input())

factorial = lambda x : 1 if x<=1 else x*factorial(x-1)

N = 3

def factorial(x):
    if x <=1:
        return 1
    else:
        return x*factorial(x-1)
print(factorial(N))
