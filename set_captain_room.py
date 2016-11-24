'''
n = raw_input()
my_list = raw_input().strip().split()
'''
my_list = [1, 2, 3, 6, 5, 4, 4, 2, 5, 3, 6, 1, 6, 5, 3, 2, 4, 1, 2, 5, 1, 4, 3, 6, 8, 4, 3, 1, 5, 6, 2]
new_list = list(set(my_list))
new_list = map(int, new_list)
my_list1 = map(int, my_list)
my_count = [my_list1.count(i) for i in new_list]
for index, x in enumerate(my_count):
    if x == 1:
        print new_list[index]


k,arr = int(input()),list(map(int, input().split()))
myset = set(arr)
print(((sum(myset)*k)-(sum(arr)))//(k-1))
