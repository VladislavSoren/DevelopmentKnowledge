from leetcode.med.tasks.longest_palindrom_substr import Solution
import pytest

class TestSolution:
    @pytest.mark.parametrize("s, expected", [
        ("a", "a"),
        ("aa", "aa"),
        ("aaa", "aaa"),
        ("aaaa", "aaaa"),
        ("aaba", "aba"),
        ("aababa", "ababa"),
        ("babad", "bab"),
        ("badad", "ada"),
        ("cbbd", "bb" ),
    ])
    def test_longest_substr_without_repeat_char(self, s, expected):
        """Test various scenarios for canPlaceFlowers method"""
        result = Solution.longestPalindrome(object, s)
        assert result == expected