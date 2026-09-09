class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # instance = defaultdict(int)
        # for num in nums: 
        #     if num in instance: 
        #         return True  
        #     else: 
        #         instance[num] = 1
        # return False 
        
        instances = defaultdict(int)
        for num in nums: 
            if num in instances: 
                return True 
            else: 
                instances[num] = 1
        return False

