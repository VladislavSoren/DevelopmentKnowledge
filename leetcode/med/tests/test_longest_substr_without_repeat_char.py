from leetcode.med.tasks.longest_substr_without_repeat_char import Solution
import pytest

class TestSolution:
    @pytest.mark.parametrize("s, expected", [
        # Основные случаи
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
    ])
    def test_longest_substr_without_repeat_char(self, s, expected):
        """Test various scenarios for canPlaceFlowers method"""
        result = Solution.lengthOfLongestSubstring(object, s)
        assert result == expected