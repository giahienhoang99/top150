from itertools import accumulate
from collections import List

class NumArray:
    def __init__(self, nums: List[int]):
        self.sums = list(accumulate(nums))

    def sumRange(self, left: int, right: int) -> int:
        return self.sums[right] - (self.sums[left - 1] if left else 0)

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)