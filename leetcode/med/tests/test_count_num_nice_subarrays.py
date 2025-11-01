from leetcode.med.tasks.count_num_nice_subarrays import Solution
import pytest

class TestSolution:
    @pytest.mark.parametrize("nums, k, expected", [
        ([1,1,2,1,1], 3, 2),
        ([2,4,6], 1, 0),
        ([2,2,2,1,2,2,1,2,2,2], 2, 16)
    ])
    def test_longest_substr_without_repeat_char(self, nums, k, expected):
        """Test various scenarios for canPlaceFlowers method"""
        result = Solution.numberOfSubarrays(object, nums, k)
        assert result == expected