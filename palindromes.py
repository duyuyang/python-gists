"""
Changes all the words in the letter into palindromes.
To do this, he follows two rules:
He can reduce the value of a letter, e.g. he can change d to c, but he cannot change c to d.
In order to form a palindrome, if he has to repeatedly reduce the value of a letter, he can do it until the letter becomes a. Once a letter has been changed to a, it can no longer be changed.
Each reduction in the value of any letter is counted as a single operation. Find the minimum number of operations required to convert a given string into a palindrome.

N = int(raw_input())
for a_str in range(N):
    my_list = map(ord, list(raw_input()))
    count = 0
    num = len(my_list)//2
    for x in range(num):
        count += abs(my_list[-(x+1)] - my_list[x])
    print count

map(lambda x: x+1, [0, 1])
-> [1, 2]
x = 0 than x = 1
sum([1, 2, 3])
-> 6

"""

s = raw_input()
print sum(map(lambda x: abs(ord(s[x]) - ord(s[len(s) - x - 1])),
              range(len(s)/2)))
