from typing import List

def checkSubarraySum(self, nums: List[int], k: int) -> bool:
    # map: remainder -> index
    prefsum, remToIdx = 0, {0: -1}

    for i, num in enumerate(nums):
        prefsum += num
        rem = prefsum % k
        if rem in remToIdx:
            if i - remToIdx[rem] > 1:
                return True
        else:
            remToIdx[rem] = i
    return False
