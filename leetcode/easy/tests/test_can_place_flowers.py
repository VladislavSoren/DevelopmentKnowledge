from leetcode.easy.tasks.can_place_flowers import Solution
import pytest


class TestSolution:
    @pytest.mark.parametrize("flowerbed,n,expected", [
        # Основные случаи
        ([1,0,0,0,1], 1, True),
        ([1,0,0,0,1], 2, False),
        
        # Тесты начала массива
        ([0,0,1,0,1], 1, True),
        ([1,0,1,0,1], 1, False),
        
        # Тесты конца массива
        ([1,0,1,0,1,0,0], 1, True),
        ([1,0,1,0,1,0,1], 1, False),
        
        # Специальные случаи
        ([1,0,0,0,0,0,1], 2, True),
        ([1,0,0,0,0,1], 2, False),
        ([0,0,0,0,1], 2, True),
        
        # Маленький цветник
        ([1], 1, False),
    ])
    def test_can_place_flowers(self, flowerbed, n, expected):
        """Test various scenarios for canPlaceFlowers method"""
        solution = Solution()
        result = solution.canPlaceFlowers(flowerbed, n)
        assert result == expected
