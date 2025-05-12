from typing import List

#https://leetcode.com/problems/subarray-sum-equals-k/
def subarraySum(self, nums: List[int], k: int) -> int:
       prefsum, count, sumToCount = 0, 0, {0: 1}
       for num in nums:
           prefsum += num
           count += sumToCount.get(prefsum - k, 0)
           sumToCount[prefsum] = sumToCount.get(prefsum, 0) + 1
       return count
