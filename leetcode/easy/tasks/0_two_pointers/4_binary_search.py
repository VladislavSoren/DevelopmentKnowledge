def has_sub_01(s):
    left = 0
    right = len(s) - 1

    while left <= right:
        mid = (left + right) // 2
        print(1)
        if s[mid] == '1' and s[mid-1] != '0':
            right = mid - 1
        elif s[mid] == '0' and s[mid+1] != '1':
            left = mid + 1
        else:
            return True
    return False




s = '0000000000000000001'
assert has_sub_01(s) == True