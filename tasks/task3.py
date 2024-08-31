# subtask1
# Bunny Prisoner Locating
# =======================

# Keeping track of Commander Lambda's many bunny prisoners is starting to get tricky. You've been tasked with writing a program to match bunny prisoner IDs to cell locations.

# The LAMBCHOP doomsday device takes up much of the interior of Commander Lambda's space station, and as a result the prison blocks have an unusual layout. They are stacked in a triangular shape, and the bunny prisoners are given numerical IDs starting from the corner, as follows:

# | 7
# | 4 8
# | 2 5 9
# | 1 3 6 10

# Each cell can be represented as points (x, y), with x being the distance from the vertical wall, and y being the height from the ground. 

# For example, the bunny prisoner at (1, 1) has ID 1, the bunny prisoner at (3, 2) has ID 9, and the bunny prisoner at (2,3) has ID 8. This pattern of numbering continues indefinitely (Commander Lambda has been taking a LOT of prisoners). 

# Write a function solution(x, y) which returns the prisoner ID of the bunny at location (x, y). Each value of x and y will be at least 1 and no greater than 100,000. Since the prisoner ID can be very large, return your solution as a string representation of the number.

# Test cases
# ==========
# Your code should pass the following test cases.
# Note that it may also be run against hidden test cases not shown here.


# -- Python cases --
# Input:
# solution.solution(5, 10)
# Output:
#     96

# Input:
# solution.solution(3, 2)
# Output:
#     9

def solution1(x, y):
    return None


# subtask2
# The Grandest Staircase Of Them All
# ==================================

# With her LAMBCHOP doomsday device finished, Commander Lambda is preparing for her debut on the galactic stage - but in order to make a grand entrance, she needs a grand staircase! As her personal assistant, you've been tasked with figuring out how to build the best staircase EVER. 

# Lambda has given you an overview of the types of bricks available, plus a budget. You can buy different amounts of the different types of bricks (for example, 3 little pink bricks, or 5 blue lace bricks). Commander Lambda wants to know how many different types of staircases can be built with each amount of bricks, so she can pick the one with the most options. 

# Each type of staircase should consist of 2 or more steps.  No two steps are allowed to be at the same height - each step must be lower than the previous one. All steps must contain at least one brick. A step's height is classified as the total amount of bricks that make up that step.
# For example, when N = 3, you have only 1 choice of how to build the staircase, with the first step having a height of 2 and the second step having a height of 1: (# indicates a brick)

# #
# ##
# 21

# When N = 4, you still only have 1 staircase choice:

# #
# #
# ##
# 31

# But when N = 5, there are two ways you can build a staircase from the given bricks. The two staircases can have heights (4, 1) or (3, 2), as shown below:

# #
# #
# #
# ##
# 41

# #
# ##
# ##
# 32

# Write a function called solution(n) that takes a positive integer n and returns the number of different staircases that can be built from exactly n bricks. n will always be at least 3 (so you can have a staircase at all), but no more than 200, because Commander Lambda's not made of money!

# Test cases
# ==========
# Your code should pass the following test cases.
# Note that it may also be run against hidden test cases not shown here.

# -- Python cases --
# Input:
# solution.solution(200)
# Output:
#     487067745

# Input:
# solution.solution(3)
# Output:
#     1

def solution2(n):
    return 0


if __name__ == "__main__":
    print(solution1(5, 10))
