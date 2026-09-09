class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count = defaultdict(int)
        # for i in nums:
        #     count[i] += 1

        # heap = [] 
        # for key, val in count.items():
        #     heapq.heappush(heap, (-1 * val, key))

        # result = []
        # for i in range(k): 
        #     most_freq = heapq.heappop(heap)
        #     result.append(most_freq[1])
        # return result


        count = defaultdict(int)
        for i in nums: 
            count[i] += 1 
        
        heap = [] 
        for key,val in count.items(): 
            heapq.heappush(heap, (-1*val, key))

        result = [] 
        for i in range(k):
            most_freq = heapq.heappop(heap)
            result.append(most_freq[1])
        return result