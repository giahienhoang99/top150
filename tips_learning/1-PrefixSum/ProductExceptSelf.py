from collections import List

def productExceptSelf(self, nums: List[int]) -> List[int]:
    res, l, r = [1] * len(nums), 1, 1
    for i, num in enumerate(nums):
        res[i] *= l
        l *= num
    for i in range(len(nums) - 1, -1, -1):
        res[i] *= r
        r *= nums[i]
    return res
