class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in strs: 
            res += str(len(i)) + "#" + i
        print(res)
        return res 
    def decode(self, s: str) -> List[str]:
        # print(s, "xdxd")
        res = []
        i = 0 
        while i < len(s):
            word = ""
            length = ""
            while s[i] != "#":
                length += s[i]
                i += 1
            count = int(length)
            i += 1 
            for j in range(count):
                word += s[i]
                i += 1 
            res.append(word) 
        return res 


    