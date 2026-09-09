class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []
        total = 1
        for i in range(len(nums)): 
            if nums[i] != 0:
                total *= nums[i] 
        zeros = 0
        for t in nums: 
            if t == 0: 
                zeros += 1
        if zeros == 0:
            for j in range(len(nums)): 
                if nums[j] != 0:
                    new = total//nums[j]
                    answer.append(new)
        elif zeros == 1: 
            for i in range(len(nums)): 
                if nums[i] != 0: 
                    answer.append(0)
                else: 
                    answer.append(total)
        else: 
            for i in range(len(nums)):
                answer.append(0)
        return answer