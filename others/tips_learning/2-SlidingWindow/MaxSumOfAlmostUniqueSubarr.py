from collections import defaultdict
from typing import List


def maxSum(self, nums: List[int], m: int, k: int) -> int:
    # fixed sliding window
    # use cursum to track max sum
    # use hashmap to track freq
    maxsum, cursum, l, freq = 0, 0, 0, defaultdict(int)
    for r in range(0, len(nums)):
        # extend
        cursum += nums[r]
        freq[nums[r]] += 1
        if r >= k:
            # shorten
            cursum -= nums[l]
            freq[nums[l]] -= 1
            if freq[nums[l]] == 0:
                del freq[nums[l]]
            l += 1
        # update maxsum
        maxsum = max(maxsum, cursum) if len(freq) >= m else maxsum
    return maxsum
