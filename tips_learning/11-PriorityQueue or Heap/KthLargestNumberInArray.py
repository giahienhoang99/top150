import heapq

def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        Note:   after pq is filled with k elements, compare with top element of 
                min heap first before pushing to avoid pushing and then popping
                => then return the top element of min heap
                => should be the kth largest element
        """
        pq = []
        for num in nums:
            if len(pq) >= k:
                if num <= pq[0]:
                    continue
                else:
                    heapq.heappop(pq)
                    heapq.heappush(pq, num)
            else:
                heapq.heappush(pq, num)

        return pq[0]

def findKthLargest(self, nums: List[int], k: int) -> int:
    """
    - push num in min heap until len(min heap) = k
    - then when len(min heap) > k, we push and pop at the same time
        => idea: keep removing smallest num
        => in the end the heap will contain k largest elements => res = heap[0] 
        => o(n log k)
    """
    pq = []
    for num in nums:
        heapq.heappush(pq, num)
        if len(pq) > k:
            heapq.heappop(pq)
    
    return heapq.heappop(pq)

