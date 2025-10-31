from leetcode.easy.tasks.maximum_average_subarray import Solution
import pytest

class TestSolution:
    @pytest.mark.parametrize("nums,k,expected", [
        # Основные случаи
        ([1,12,-5,-6,50,3], 4, 12.75),
        ([3,1,12,-5,-6,50], 4, 12.75),
        ([12,-5,-6,50], 4, 12.75),
        ([5], 1, 5)
    ])
    def test_maximum_average_subarray(self, nums, k, expected):
        """Test various scenarios for canPlaceFlowers method"""
        result = Solution.findMaxAverage(object, nums, k)
        assert result == expected