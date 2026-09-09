class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        instance = defaultdict(int)
        for num in nums: 
            instance[num] += 1
            if instance[num] == 2: 
                return True
        return False