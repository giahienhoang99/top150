from typing import List

def search(self, nums: List[int], target: int) -> int:
    rotate_index, l, r = 0, 0, len(nums) - 1
    # find rotate index
    while l < r:
        mid = (l + r) >> 1
        if nums[mid] < nums[len(nums) - 1]:
            r = mid
        else:
            l = mid + 1
    rotate_index = l

    # find target in 2 sorted subarr
    l = 0 if target >= nums[0] else rotate_index
    r = rotate_index - 1 if target >= nums[0] else len(nums) - 1

    if rotate_index == 0:
        l, r = 0, len(nums) - 1

    while l <= r:
        mid = (l + r) >> 1
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            r = mid - 1
        else:
            l = mid + 1
    return -1
