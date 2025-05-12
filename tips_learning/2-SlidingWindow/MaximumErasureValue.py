from typing import List

def maximumUniqueSubarray(self, nums: List[int]) -> int:
    # Objective: find max sum of unique subarr
    # dynamic length sliding window
    # extend if valid
    # if invalid shorten til valid
    # update max sum
    maxsum, cursum, l = 0, 0, 0
    seen = set()  # set to track seen vals in cur window
    for r, num in enumerate(nums):
        cursum += num
        while num in seen:
            cursum -= nums[l]
            seen.discard(nums[l])
            l += 1
        seen.add(num)
        maxsum = max(maxsum, cursum)
    return maxsum
