class Solution:
    def isPalindrome(self, s: str) -> bool:
        # new_string = ""
        # for j in s:
        #     if j.isalpha() or j.isdigit():
        #         new_string += j
        # new_string = new_string.lower()
        # print(new_string)
        # left = 0
        # right = len(new_string)-1
        # for i in range(len(new_string)): 
        #     if new_string[left] != new_string[right]: 
        #         return False
        #     left += 1
        #     right -= 1
        # return True

        left = 0
        right = len(s) - 1

        while left < right: 
            if s[left].isalnum() and s[right].isalnum(): 
                if s[left].lower() != s[right].lower(): 
                    return False 
                left += 1
                right -= 1
            elif (s[left].isalnum() and not s[right].isalnum()):
                right -= 1
            elif (not s[left].isalnum()) and s[right].isalnum():
                left += 1 
            else:
                left += 1
                right -= 1
        return True 
