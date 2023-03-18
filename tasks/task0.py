def solution(l, x):
    '''
    Check if x in given list of integers.
    Args:
        l - List[Int] - list of incoming integers.
        x - element that should be found
    Returns:
        Boolean - True if found.
    '''
    return False

def test_func1():
    assert solution([1,2,3], 3) == True, "Check your implementation!"
    assert solution([-1,5,3], 1) == False, "Check your implementation!"
    print("Local tests for func passed!")


if __name__ == "__main__":
    test_func1()