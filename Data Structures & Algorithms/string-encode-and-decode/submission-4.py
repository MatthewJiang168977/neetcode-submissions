class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        for i in strs: 
            string += str(len(i)) + "#" + i 
        print (string)
        return string

    def decode(self, s: str) -> List[str]:
        lst = []
        # word = ""
        # for i in range(len(s)): 
        #     if s[i] != " ": 
        #         word += s[i]
        #     else: 
        #         lst.append(word)
        #         word = ""
        i = 0 
        while i < len(s): 
            j = i 
            while s[j] != "#": 
                j += 1
            length = int(s[i:j])
            lst.append(s[j+1:j+1+length])
            i = j + 1 + length
        return lst


