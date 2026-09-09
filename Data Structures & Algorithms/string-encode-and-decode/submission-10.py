class Solution:

    def encode(self, strs: List[str]) -> str:
        new = ""
        for i in strs: 
            new += str(len(i)) + "#" + i 
        print(new)
        return new 
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0 
        while i < len(s): 
            word = ""
            length = ""
            while s[i] != "#": 
                length += s[i]
                i += 1 
            i += 1 
            length = int(length)
            for j in range(length): 
                word += s[i]
                i += 1 
            res.append(word) 
        return res  
