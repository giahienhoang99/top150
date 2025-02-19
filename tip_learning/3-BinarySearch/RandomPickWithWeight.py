import random
from itertools import accumulate
from typing import List

class Solution:
    def __init__(self, w: List[int]):
        self.prefix_sums = list(accumulate(w))

    def pickIndex(self) -> int:
        # w  1 2 3 4  5
        # ps 1 3 6 10 15
        # sum = 15
        # 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
        # ^   ^     ^       ^              ^ 
        # l = 0, r = 4, mid = 2
        # 
        # random.randint(1, 15) -> x -> find x in which range of prefix_sums
        random_num = random.randint(1, self.prefix_sums[-1])
        l, r = 0, len(self.prefix_sums) - 1
        result = -1
        while l <= r:
            mid = (l + r) // 2
            if random_num <= self.prefix_sums[mid]:
                result = mid
                r = mid - 1
            elif random_num > self.prefix_sums[mid]:
                l = mid + 1
        return result
        

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()