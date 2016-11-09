"""
Two people are playing game of Nim. The basic rules for this game are as follows
The game starts with  piles of stones indexed from  to. Each pile  (where) has  stones
The players move in alternating turns. During each move, the current player must remove one or more stones from a single pile.
The player who removes the last stone loses the game.
Given the value of  and the number of stones in each pile, determine whether the person who wins the game is the first or second person to move. If the first player to move wins, print First on a new line; otherwise, print Second. Assume both players move optimally.

For SECOND to win, one of the following conditions must be true:
1) (if the number of stones in EACH pile is <= 1) AND (XOR of the number of stones in each pile is 1)
2) (if the number of stones in ANY pile is > 1) AND (XOR of the number of stones in each pile is 0)

For ANY other case FIRST wins...

"""
#N = int(raw_input())

"""
def check_list(stones):
    flag = 1
    for st in stones:
	    if st > 1:
	        flag = 2
    if flag == 1:
        return False
    else:
        return True
    return all(st >=1 for st in stones)

def check_xor(stones):

    return reduce(lambda x,y: x^y, stones)

for case in range(N):
    pipes = int(raw_input())
    stones = map(int, raw_input().strip().split())
    if check_list(stones) == False and check_xor(stones) == 1:
        print "Second"
    elif check_list(stones) == True and check_xor(stones) == 0:
        print "Second"
    else:
        print "First"
"""
for _ in xrange(int(raw_input().strip())):
    __, heaps = input(), map(int, raw_input().strip().split())
    print ['First', 'Second'][reduce(lambda x,y: x^y, heaps) == all(x <=1 for x in heaps)]
