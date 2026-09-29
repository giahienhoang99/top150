from typing import List

def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        maxLen, prefsum, mapSumToFirstIdx = 0, 0, {0: -1}
        for i in range(0, len(nums)):
            prefsum += nums[i]
            # check if the target prefix sum exists
            if prefsum - k in mapSumToFirstIdx:
                maxLen = max(maxLen, i - mapSumToFirstIdx[prefsum - k])
            # set the first occurrence of prefsum
            if prefsum not in mapSumToFirstIdx:
                mapSumToFirstIdx[prefsum] = i
        return maxLen
