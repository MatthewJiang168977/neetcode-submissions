class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # char_s = [0] * 26 
        # char_t = [0] * 26
        # for i in range(len(s)):
        #     char_s[ord(s[i]) - ord("a")] += 1
        # for j in range(len(t)):
        #     char_t[ord(t[j]) - ord("a")] += 1

        # if char_s == char_t: 
        #     return True
        # return False
        char_s = [0] * 26 
        char_t = [0] * 26
        for letter in s: 
            char_s[ord(letter)-ord("a")] += 1 
        for letter in t: 
            char_t[ord(letter)-ord("a")] += 1 
        if char_s == char_t:
            return True
        return False

        
        