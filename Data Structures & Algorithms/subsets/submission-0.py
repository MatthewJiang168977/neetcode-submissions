class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [] 
        def dfs(subset, start): 
            res.append(subset[:])
            for i in range(start, len(nums)):
                subset.append(nums[i])
                dfs(subset, i+1)
                subset.pop()
        dfs([], 0)
        return res 