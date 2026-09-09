class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # new_nums = defaultdict(int)
        # for i in range(len(nums)): 
        #     compliment = target - nums[i]
        #     if compliment in new_nums: 
        #         return [new_nums[compliment], i]
        #     new_nums[nums[i]] = i

        compliments = defaultdict(int)
        for i in range(len(nums)): 
            compliment = target - nums[i]
            if compliment in compliments: 
                return [compliments[compliment], i]
            compliments[nums[i]] = i 

        # compliments = defaultdict(int)
        # for i in range(len(nums)): 
        #     compliment = target - nums[i]
        #     if compliment in compliments:
        #         return [compliments[nums[compliment]], i]
        #     compliments[nums[i]] = i    