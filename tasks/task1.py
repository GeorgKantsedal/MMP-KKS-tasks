# subtask 1
# Given a binary tree, write a function that returns the sum of the values of that tree.
import random


class Node:
    def __init__(self, l=None, r=None, v=0) -> None:
        self.left = l
        self.right = r
        self.value = v


def get_tree(max=50):
    nodes = [Node(v=random.randint(-100, 100)) for i in range(max + 1)]

    tree = Node()
    for i in range(max):
        sight = random.choice(['l', 'r'])
        val = random.randint(-100, 100)
        vall = random.randint(0, max)
        if sight == 'l':
            tree = Node(l=tree, r=nodes[vall], v=val)
        else:
            tree = Node(l=nodes[vall], r=tree, v=val)
    return tree


tree1 = get_tree(5)
tree2 = get_tree(10)
tree3 = get_tree(50)


def solution1(tree: Node):
    """
    Return sum of values.
    Args:
        l - tree
    Returns:
        float.
    """
    rez = tree.value
    return rez


# subtask 2
# Find an area of the intersection of two rectangles.
class Rect:
    def __init__(self, x=0, y=0, w=0, h=0) -> None:
        self.x = x
        self.y = y
        self.wight = w
        self.height = h


def solution2(r1: Rect, r2: Rect):
    """
    Args:
        r1 - Rect
        r2 - Rect
    Returns:
        float.
        """
    return 0


rects = [Rect(x=random.randint(-100, 100),
              y=random.randint(-100, 100),
              w=random.randint(0, 100),
              h=random.randint(0, 100)) for i in range(20)]

r1 = rects[random.randint(0, 19)]
r2 = rects[random.randint(0, 19)]


# subtask 3
# Write an efficient function that checks whether any permutation of an input string is a palindrome.
# Note that the function is not a palindrome check 

def solution3(s: str):
    return True


def solution(tree: Node, r1: Rect, r2: Rect, s: str):
    return solution1(tree), solution2(r1, r2), solution3(s)


def test_func1():
    print(solution1(tree1))
    print(solution1(tree2))
    print(solution1(tree3))

    print(solution2(r1, r2))

    assert solution3('civic') == True, "Check your implementation!"
    assert solution3('ivicc') == True, "Check your implementation!"
    assert solution3('civil') == False, "Check your implementation!"
    assert solution3('livci') == False, "Check your implementation!"

    print("Local tests for func passed!")


if __name__ == "__main__":
    test_func1()
