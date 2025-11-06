from leetcode.easy.tasks.palindrome_number import Solution
import pytest

class TestSolution:
    @pytest.mark.parametrize(" k, expected", [
        (121, True),
        (1221, True),
        (-121, False),
        (10, False),
    ])
    def test_longest_substr_without_repeat_char(self, k, expected):
        """Test various scenarios for canPlaceFlowers method"""
        result = Solution.isPalindrome(object, k)
        assert result == expected
