class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        digit_set = set(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])


        INT_MAX = 2147483647 # 2**31 - 1
        INT_MIN = -2147483648 # -2**31

        s = s.strip()
        if not s:
            return 0

        s_new = ''
        zero_start = False
        if s[0] in ('+', '-') or s[0] in digit_set:
            if s[0] in digit_set and s[0] != '0':
                zero_start = True
            s_new += s[0]
            for i in range(1, len(s)):
                if i == 1 and s[i] not in digit_set and s[i] != '.':
                    break
                
                if s[i] == '0':
                    if not zero_start:
                        continue

                if s[i] == '.':
                    break

                if s[i] in digit_set:
                    zero_start = True
                    s_new += s[i]
                else:
                    break

        else:
            return 0
        
        try:
            s_new_int = int(s_new)
        except ValueError:
            return 0

        if s_new_int > INT_MAX:
            return INT_MAX
        if s_new_int < INT_MIN:
            return INT_MIN
        
        return s_new_int
