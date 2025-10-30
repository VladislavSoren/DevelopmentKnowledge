"""
485. Max Consecutive Ones

Given a binary array nums, return the maximum number of consecutive 1's in the array.
"""

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_str = str(nums)[1:-1].replace(' ', '').replace(',', '')
        groups_ones = nums_str.split('0')
        return len(max(groups_ones))
