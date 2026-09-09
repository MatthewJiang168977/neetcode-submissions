class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_string = ""
        for j in s:
            if j.isalpha() or j.isdigit():
                new_string += j
        new_string = new_string.lower()
        print(new_string)
        left = 0
        right = len(new_string)-1
        for i in range(len(new_string)): 
            if new_string[left] != new_string[right]: 
                return False
            left += 1
            right -= 1
        return True