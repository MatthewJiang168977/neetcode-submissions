class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in strs:
            res += str(len(i)) + "#" + i
        return res
    def decode(self, s: str) -> List[str]:
        # print(s)
        res = [] 
        i = 0 
        while i < len(s): 
            word = ""
            length = ""
            while s[i] != "#": 
                length += s[i]
                i += 1 
            print(length)
            i += 1 
            length = int(length)
            for j in range(length): 
                word += s[i]
                i += 1 
            res.append(word)
        return res 