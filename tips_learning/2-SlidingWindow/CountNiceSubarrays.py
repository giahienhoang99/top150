from typing import List

def numberOfSubarrays(self, nums: List[int], k: int) -> int:
    # not sliding window but an index-based approach
    # Objective: number of subarr having exactly k odd nums

    odd_indices = [-1]  # virtual "left boundary"
    result = 0

    # Step 1: Record indices of all odd numbers
    for i in range(len(nums)):
        if nums[i] % 2 == 1:
            odd_indices.append(i)
    odd_indices.append(len(nums))  # virtual "right boundary"

    # Step 2: For each window of exactly k odd numbers
    for i in range(1, len(odd_indices) - k):
        left_even = odd_indices[i] - odd_indices[i - 1] - 1
        right_even = odd_indices[i + k] - odd_indices[i + k - 1] - 1
        result += (left_even + 1) * (right_even + 1)

    return result
    # nums: 2 2 1 2 2 1 2 2 1 2
    # k = 2
    # odd indices: -1 2 5 8 10
    # expected ans: 15
