class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minheap = nums 
        self.k = k 
        heapq.heapify(self.minheap)
        print(self.minheap)
        while len(self.minheap) > self.k: 
            heapq.heappop(self.minheap)
        print(self.minheap, "hajsd")

    def add(self, val: int) -> int:
        heapq.heappush(self.minheap, val)
        if len(self.minheap) > self.k: 
            print(self.minheap)
            print(heapq.heappop(self.minheap))
            
        return self.minheap[0]

        
