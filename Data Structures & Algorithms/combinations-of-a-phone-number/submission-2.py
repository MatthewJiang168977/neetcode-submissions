class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        res = [] 
        number_to_letters = {2:"abc", 3:"def", 4:"ghi", 5:"jkl", 6:"mno", 7:"pqrs", 8:"tuv", 9:"wxyz"}
    
        def dfs(comb, start):
            if len(comb) == len(digits):
                res.append(comb)
                return
            for char in number_to_letters[int(digits[start])]:
                #comb += char
                dfs(comb + char ,start+1)
                #comb = comb[:-1]
        dfs("",0)
        return res