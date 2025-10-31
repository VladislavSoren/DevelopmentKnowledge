"""
You have a long flowerbed in which some of the plots are planted, 
and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, 
where 0 means empty and 1 means not empty, and an integer n, 
return true if n new flowers can be planted in the flowerbed 
without violating the no-adjacent-flowers rule and false otherwise.
"""

class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        
        plant_count = 0

        if n == 0:
            return True

        if len(flowerbed) <= 3:

            if flowerbed == [0,0,0] and n in (0,1,2):
                return True

            if flowerbed == [0,0,1] and n in (0,1):
                return True
            
            if flowerbed == [1,0,0] and n in (0,1):
                return True
            
            if flowerbed == [0,0] and n in (0,1):
                return True
            
            if flowerbed == [0] and n in (0,1):
                return True

            return False

        for i, _ in enumerate(flowerbed, 1):

            if plant_count >= n:
                return True

            # start case: [0 0 0 ...]
            common_succes = flowerbed[i-1] == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0
            if i == 1 and common_succes:
                flowerbed[i-1] = 1
                plant_count += 1
                continue

            # start case: [0 0 1 ...]
            can_plant_start = flowerbed[i-1] == 0 and  flowerbed[i] == 0 and  flowerbed[i+1] == 1
            if i == 1 and can_plant_start:
                flowerbed[i-1] = 1
                plant_count += 1
                continue

            # end case [1 0 0 ...]
            can_plant_end = flowerbed[i-1] == 1 and  flowerbed[i] == 0 and  flowerbed[i+1] == 0
            if i == len(flowerbed) - 2 and can_plant_end:
                flowerbed[i+1] = 1
                plant_count += 1
                break

            # common case  
            common_succes = flowerbed[i-1] == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0
            if common_succes:
                flowerbed[i] = 1
                plant_count += 1

            # Условие выхода, когда дошли до конца (до предпоследнего элемента)
            if i == len(flowerbed) - 2:
                break

        if plant_count >= n:
            return True
        else:
            return False


# class Solution(object):
#     def canPlaceFlowers(self, flowerbed, n):
#         if n == 0:
#             return True
#         for i in range(len(flowerbed)):
#             if flowerbed[i] == 0 and (i == 0 or flowerbed[i-1] == 0) and (i == len(flowerbed)-1 or flowerbed[i+1] == 0):
#                 flowerbed[i] = 1
#                 n -= 1
#                 if n == 0:
#                     return True
#         return False

"""
Если (текущая пустая) И
    (в начале ИЛИ пусто слева) И
    (в конце ИЛИ пусто справа)

Сценарии:
- текущая пустая -> в начале -> пусто справа
- текущая пустая -> в конце -> пусто слева
- текущая пустая -> пусто слева -> пусто справа
"""