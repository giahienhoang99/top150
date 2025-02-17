from typing import List

def findPeakElement(self, nums: List[int]) -> int:
    # at nums[mid]:
    #   peak: nums[i-1] < num[i] > nums[i+1]
    #   if ascending:  nums[i-1] < num[i] < nums[i+1] => l = mid + 1
    #   if descending: nums[i-1] > num[i] > nums[i+1] => r = mid - 1
    l, r = 0, len(nums) - 1
    while l < r:
        mid = (l + r) // 2
        if nums[mid] < nums[mid + 1]:
            l = mid + 1
        else:
            r = mid
    return l
