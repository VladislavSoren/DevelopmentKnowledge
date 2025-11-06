from leetcode.easy.tasks.get_nearest_numbers import get_nearest_numbers


import pytest

class TestSolution:
    @pytest.mark.parametrize("a, index, k, expected", [
        ([3,5,7,8], 1, 2, [5,3]),
        ([3,5,7,8,8], 2, 3, [7,8,8]),
        ([3,5,7,8,8], 2, 4, [7,8,8,5]),
        # Дополнительные тесты:
        
        # 1. Все элементы одинаковые
        ([1,1,1,1,1], 2, 3, [1,1,1]),
        
        # 2. Крайний левый элемент как опорный
        ([1,3,5,7,9], 0, 2, [1,3]),
        
        # 3. Крайний правый элемент как опорный  
        ([1,3,5,7,9], 4, 3, [9,7,5]),
        
        # 4. k = 1 (минимальный случай)
        ([2,4,6,8,10], 2, 1, [6]),
        
        # 5. k = N (все элементы)
        ([1,2,3,4,5], 2, 5, [3,2,4,1,5]),
        
        # 6. Отрицательные числа
        ([-5,-3,0,2,4], 2, 3, [0,-3,2]),
    ])
    def test_longest_substr_without_repeat_char(self, a, index, k, expected):
        """Test various scenarios for canPlaceFlowers method"""
        result = get_nearest_numbers(a, index, k)
        assert set(result) == set(expected)
