"""
3. Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without duplicate characters.
"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = 0
        unique_group = set()
        max_len = 0
        for right in range(len(s)):
            while s[right] in unique_group:
                unique_group.remove(s[left])
                left += 1
            unique_group.add(s[right])
            max_len = max(max_len, right - left + 1)
        return max_len