from collections import Counter
import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        - need to track freq of each num
        => use hashmap: num -> freq (time: o(n), space: o(n))

        - need to track k most freq
        => make a max heap to insert tuples (-freq, num) (time: o(nlogn), o(n))
        
        - pop out k elements to a list (o(k))
        """
        freq = Counter(nums)
        pq = []
        for num, f in freq.items():
            heapq.heappush(pq, (-f, num))
        res = [heapq.heappop(pq)[1] for _ in range(k)]
        return res