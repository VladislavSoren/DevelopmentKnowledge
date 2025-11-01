from leetcode.med.tasks.next_permutation import Solution
import pytest

class TestSolution:
    @pytest.mark.parametrize("nums, expected", [
        ([1,2,3], [1,3,2]),
        ([3,2,1], [1,2,3]),
        ([1,1,5], [1,5,1]),
    ])
    def test_longest_substr_without_repeat_char(self, nums, expected):
        """Test various scenarios for canPlaceFlowers method"""
        Solution.nextPermutation(object, nums)
        assert nums == expected