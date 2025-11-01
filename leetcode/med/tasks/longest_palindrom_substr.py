class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        def expand_from_center(s, left, right):
            """Расширяется от центра пока символы совпадают"""
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return left + 1, right - 1


        max_polindrom = ""

        for i in range(len(s)):
            left1, right1 = expand_from_center(s, i, i)
            left2, right2 = expand_from_center(s, i, i + 1)
            
            len1 = right1 - left1 + 1
            len2 = right2 - left2 + 1
            
            if len1 > len2:
                if len1 > len(max_polindrom):
                    max_polindrom = s[left1:right1+1]
            else:
                if len2 > len(max_polindrom):
                    max_polindrom = s[left2:right2+1]

        return max_polindrom
