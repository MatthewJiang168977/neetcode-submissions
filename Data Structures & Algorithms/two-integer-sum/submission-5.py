class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # compliments = defaultdict(int)
        # for i in range(len(nums)): 
        #     compliment = target - nums[i]
        #     if compliment in compliments: 
        #         return [compliments[compliment], i]
        #     compliments[nums[i]] = i

        two_sum = defaultdict(int)
        for i in range(len(nums)):
            compliment = target - nums[i]
            if compliment in two_sum: 
                return [two_sum[compliment], i]
            else: 
                two_sum[nums[i]] = i
