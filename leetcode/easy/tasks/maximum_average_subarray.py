"""
643. Maximum Average Subarray I

You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k 
that has the maximum average value and return this value. 
Any answer with a calculation error less than 10-5 will be accepted.
"""

class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """

        current_sum = max_sum = sum(nums[:k])
        for i in range(1, len(nums) - k + 1):
            current_sum = current_sum - nums[i-1] + nums[i+k-1]
            if current_sum > max_sum:
                max_sum = current_sum
        return float(max_sum) / k
