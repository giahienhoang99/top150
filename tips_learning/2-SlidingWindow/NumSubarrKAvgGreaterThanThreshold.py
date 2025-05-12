from typing import List
#https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/
def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        s = sum(arr[:k])
        count = int(s/k >= threshold)
        for i in range(k, len(arr)):
            s += arr[i] - arr[i-k]
            count += s/k >= threshold
        return count