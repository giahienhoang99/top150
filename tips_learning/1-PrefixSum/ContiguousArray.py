from typing import List

def findMaxLength(self, nums: List[int]) -> int:
    # count0, count1: prefix sums/counts of 0s and 1s
    # use a map: diff between count0 and count1 -> index of first diff occurrence
    maxlen, count0, count1, diffToIdx = 0, 0, 0, {0: -1}
    for i in range(len(nums)):
        # dung arr count
        count0 += 1 if nums[i] == 0 else 0
        count1 += 1 if nums[i] == 1 else 0
        diff = count0 - count1
        if diff in diffToIdx:
            maxlen = max(maxlen, i - diffToIdx[diff])
        else:
            diffToIdx[diff] = i
    return maxlen
