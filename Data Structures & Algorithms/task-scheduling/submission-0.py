class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = defaultdict(int)
        for i in tasks:
            freq[i] += 1 
        #freq = Counter(tasks)
        max_heap = [] 
        for i,k in freq.items():
            max_heap.append(-k)
        heapq.heapify(max_heap)
        queue = deque()
        time = 0 
        while max_heap or queue: 
            time+=1 
            
            if max_heap: 
                count = 1 + heapq.heappop(max_heap)
                if count:
                    queue.append((count,time+n))
            if queue and queue[0][1] == time:
                heapq.heappush(max_heap, queue.popleft()[0])
        return time
