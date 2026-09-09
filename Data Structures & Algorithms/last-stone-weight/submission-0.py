class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            curr_max = heapq.heappop(stones)
            print(curr_max)
            print(stones[0])
            if stones[0] == curr_max: 
                heapq.heappop(stones)
            elif stones[0] != curr_max:    
                next_max = heapq.heappop(stones)
                heapq.heappush(stones, curr_max - next_max)
                
        if stones: 
            return -stones[0]
        return 0 