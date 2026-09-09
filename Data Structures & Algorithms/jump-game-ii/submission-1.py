class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0
        num_jumps = 0 
        current_end = 0
        farthest = 0
        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])
            print(farthest, "dfdfsdf")
            if i == current_end:
                print("xdxd")
                num_jumps += 1
                current_end = farthest
                print(current_end, "stuff")
                if current_end >= len(nums) - 1:
                    break
        return num_jumps