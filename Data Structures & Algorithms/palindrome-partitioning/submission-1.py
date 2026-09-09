class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = [] 

        def isPalindrome(str,left,right):
            while left < right: 
                if str[left] != str[right]: 
                    return False
                left+=1 
                right-=1 
            return True      

        def dfs(substring, start):
            if start == len(s):
                res.append(substring.copy())
            for i in range(start, len(s)): 
                if isPalindrome(s, start, i):
                    substring.append(s[start:i+1])
                    dfs(substring, i+1)
                    substring.pop()

        dfs([], 0)
        return res 
