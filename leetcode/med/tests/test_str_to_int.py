from leetcode.med.tasks.str_to_int import Solution
import pytest

class TestSolution:
    @pytest.mark.parametrize("s, expected", [
        # Основные случаи
        ("-042", -42),
        (" -042", -42),
        ("1337c0d3", 1337),
        ("0-1", 0),
        ("words and 987", 0),
        ("+-12", 0), 
        ("3.14159", 3),
        ("+", 0),
        ("20000000000000000000", 2147483647),
        ("1a", 1),
    ])
    def test_longest_substr_without_repeat_char(self, s, expected):
        """Test various scenarios for canPlaceFlowers method"""
        result = Solution.myAtoi(object, s)
        assert result == expected