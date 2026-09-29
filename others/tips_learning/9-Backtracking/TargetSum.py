from functools import cache
from typing import List


def findTargetSumWays(self, nums: List[int], target: int) -> int:
    n = len(nums)

    # memoization
    @cache
    def backtrack(cur_sum, i):
        if i == n:
            if cur_sum == target:
                return 1
            else:
                return 0
        if i > n:
            return 0
        return backtrack(cur_sum + nums[i], i + 1) + backtrack(cur_sum - nums[i], i + 1)

    return backtrack(0, 0)
