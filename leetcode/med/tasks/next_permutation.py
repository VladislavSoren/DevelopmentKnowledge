"""
A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

For example, for arr = [1,2,3], the following are all the permutations of arr: [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].
The next permutation of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the next permutation of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

For example, the next permutation of arr = [1,2,3] is [1,3,2].
Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.
Given an array of integers nums, find the next permutation of nums.

The replacement must be in place and use only constant extra memory.
"""

class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        def change(stop_index):
            min_greater = float('inf')
            min_index = -1
            
            for j in range(len(nums)-1, stop_index, -1):
                if nums[j] > nums[stop_index]:
                    if nums[j] < min_greater:
                        min_greater = nums[j]
                        min_index = j
            
            if min_index != -1:
                nums[min_index], nums[stop_index] = nums[stop_index], nums[min_index]

        def turn(start_index):
            left, right = start_index, len(nums)-1
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        found = False
        for i in range(len(nums)-2, -1, -1):
            if nums[i] < nums[i+1]:
                change(i)
                turn(i+1)
                found = True
                break
        
        if not found:
            nums.reverse()
