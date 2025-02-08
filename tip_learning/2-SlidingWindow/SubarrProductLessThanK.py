def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
    l, prod, count = 0, 1, 0
    if k <= 1:
        return count
    for r, num in enumerate(nums):
        prod *= num
        while prod >= k and l <= r:
            prod /= nums[l]
            l += 1
        count += r - l + 1  # all subarr starting from l to r
    return count
