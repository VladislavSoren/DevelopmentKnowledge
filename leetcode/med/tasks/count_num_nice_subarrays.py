# class Solution(object):
#     def numberOfSubarrays(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: int
#         """

#         def is_odd(num):
#             return num % 2 != 0
        
#         def delete_first_element():
#             nonlocal odd_number
#             deleted_num = sub_array.pop(0)
#             if is_odd(deleted_num):
#                 odd_number -= 1

#         def add_new_element(num):
#             nonlocal odd_number
#             sub_array.append(num) 
#             if is_odd(num):
#                 odd_number += 1

#         nice_arrs_count = 0

#         sub_array = nums[:k]
#         odd_number = len(list(i for i in sub_array if is_odd(i)))
#         if odd_number == k:
#             nice_arrs_count += 1
        
#         for i in range(k, len(nums)):
            
#             add_new_element(nums[i])

#             if odd_number == k:
#                 delete_first_element()
#                 nice_arrs_count += 1
        
#         return nice_arrs_count
    

# class Solution(object):
#     def numberOfSubarrays(self, nums, k):
#         def is_odd(num):
#             return num % 2 != 0

#         nice_arrs_count = 0
#         sub_array = nums[:k]
#         odd_number = len([i for i in sub_array if is_odd(i)])
        
#         if odd_number == k:
#             nice_arrs_count += 1
        
#         for i in range(k, len(nums)):
#             sub_array.append(nums[i])
#             if is_odd(nums[i]):
#                 odd_number += 1

#             if odd_number == k:
#                 deleted_num = sub_array.pop(0)
#                 if is_odd(deleted_num):
#                     odd_number -= 1
#                 nice_arrs_count += 1
        
#         return nice_arrs_count


# class Solution(object):
#     def numberOfSubarrays(self, nums, k):
#         def is_odd(num):
#             return num % 2 != 0

#         nice_arrs_count = 0
#         left = 0
#         odd_count = 0
        
#         for right in range(len(nums)):
#             if is_odd(nums[right]):
#                 odd_count += 1
            
#             while odd_count > k:
#                 if is_odd(nums[left]):
#                     odd_count -= 1
#                 left += 1
            
#             if odd_count == k:
#                 temp = left
#                 while not is_odd(nums[temp]) and temp <= right:
#                     nice_arrs_count += 1
#                     temp += 1
#                 nice_arrs_count += 1
        
#         return nice_arrs_count


class Solution(object):
    def numberOfSubarrays(self, nums, k):
        def is_odd(num):
            return num % 2 != 0

        nice_arrs_count = 0
        left = 0
        odd_count = 0
        prev_count = 0  # количество чётных чисел перед текущим окном
        
        for right in range(len(nums)):
            if is_odd(nums[right]):
                odd_count += 1
                prev_count = 0  # сбрасываем при встрече нечётного
            
            while odd_count == k:
                # Считаем чётные числа слева
                if is_odd(nums[left]):
                    odd_count -= 1
                prev_count += 1
                left += 1
            
            nice_arrs_count += prev_count
        
        return nice_arrs_count