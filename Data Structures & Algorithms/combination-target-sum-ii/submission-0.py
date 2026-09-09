class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = [] 
        def dfs(comb, total, start): 
            if total == 0 and comb not in res: 
                res.append(comb.copy())
                return 
            elif total < 0: 
                return 
            else: 
                for i in range(start, len(candidates)): 
                    if i > start and candidates[i] == candidates[i-1]:
                        continue 
                    comb.append(candidates[i])
                    dfs(comb, total - candidates[i], i+1)
                    comb.pop() 
        dfs([],target,0)
        return res 