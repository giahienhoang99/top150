from typing import List

def longestOnes(self, nums: List[int], k: int) -> int:
    # dynamic sliding window
    # use a var zeros to track numbers of 0s in window
    #   (init val = k, zeros -= 1 if add 0 to window else 0)
    # use a var maxlen to track result
    # shorten window while zeros < 0
    maxlen, zeros, l = 0, k, 0
    for r in range(len(nums)):
        zeros -= 1 if nums[r] == 0 else 0
        # shorten window until valid
        while zeros < 0:
            zeros += 1 if nums[l] == 0 else 0
            l += 1
        maxlen = max(maxlen, r - l + 1)
    return maxlen
