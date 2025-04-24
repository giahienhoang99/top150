from collections import defaultdict
import heapq


class NumberContainers:
    """
    change(i, num) -> change index with num
    find(num) -> smallest index

    - each num -> min heap
    - dict: index -> latest num

    change(i, num):
    - dict[i] = num
    - lazy removal in heap: pop only when first node unused
    """
    def __init__(self):
        self.smallest_index = defaultdict(list)
        self.container = defaultdict(int)

    def change(self, index: int, number: int) -> None:
        self.container[index] = number
        heapq.heappush(self.smallest_index[number], index)

    def find(self, number: int) -> int:
        pq = self.smallest_index[number]
        while pq and number != self.container[pq[0]]:
            heapq.heappop(pq)
        return pq[0] if pq else -1

# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)