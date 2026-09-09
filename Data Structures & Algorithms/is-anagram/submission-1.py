class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_s = [0]*26
        char_t = [0]*26
        for i in s: 
            char_s[ord(i) - ord("a")] += 1
        
        for j in t: 
            char_t[ord(j) - ord("a")] += 1
        
        if char_s == char_t:
            return True
        return False
