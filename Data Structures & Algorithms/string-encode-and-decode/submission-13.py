class Solution:

    def encode(self, strs: List[str]) -> str:
        new_str = ""
        for i in strs: 
            new_str += str(len(i))+"#"+i 
        print(new_str)
        return new_str
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0 
        while i < len(s): 
            string = ""
            length = "" 
            while s[i] != '#': 
                length += s[i]
                i += 1 
            i += 1
            length = int(length) 
            for j in range(length): 
                string += s[i]
                i += 1 
            res.append(string)
        return res 

