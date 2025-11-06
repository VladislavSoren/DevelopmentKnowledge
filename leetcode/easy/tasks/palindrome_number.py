class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        x_len = len(x)
        left = 0
        right = x_len - 1

        while right > left: 
            if x[right] == x[left]:
                    left += 1
                    right -= 1
            else:
                return False
        return True


# class Solution(object):
#     def isPalindrome(self, x):
#         """
#         :type x: int
#         :rtype: bool
#         """
#         x = str(x)
#         x_len = len(x)
#         left = 0
#         right = x_len - 1

#         if x_len % 2 == 0:
#             while (right - left) > 0:
#                 if x[right] == x[left]:
#                      left += 1
#                      right -= 1
#                 else:
#                     return False
#         else:
#             while (right - left) > 1:
#                 if x[right] == x[left]:
#                      left += 1
#                      right -= 1
#                 else:
#                     return False
#         return True

# # 10ms Beats 57.12%, 12.44MB Beats 52.12%


# class Solution(object):
#     def isPalindrome(self, x):
#         """
#         :type x: int
#         :rtype: bool
#         """
#         x = str(x)
#         x_len = len(x)
#         if x_len % 2 == 0:
#             right_i = int(x_len / 2)
#             if x[:right_i] == x[right_i:][::-1]:
#                 return True
#         else:
#             central_i = int((x_len + 1) / 2) - 1
#             if x[:central_i] == x[central_i + 1:][::-1]:
#                 return True
#         return False    
    
# # 7ms Beats 75.89%, 12.45MB Beats 52.12%
