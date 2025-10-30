from leetcode.easy.tasks.max_consecutive_ones import Solution


def test_simple_1():
    """
    Input: nums = [1,1,0,1,1,1]
    Output: 3
    Explanation: The first two digits or the last three digits are consecutive 1s. 
    The maximum number of consecutive 1s is 3.
    """
    nums = [1,1,0,1,1,1]

    max_number = Solution.findMaxConsecutiveOnes(object, nums)

    assert max_number == 3

def test_simple_2():
    """
    Input: nums = [1,0,1,1,0,1]
    Output: 2
    """
    nums = [1,0,1,1,0,1]

    max_number = Solution.findMaxConsecutiveOnes(object, nums)

    assert max_number == 2
