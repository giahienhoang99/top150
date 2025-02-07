from collections import defaultdict
from typing import List

def numberOfSubarrays(self, nums: List[int], k: int) -> int:
    # Objective: number of subarrays having exactly k odd numbers
    #         => bao nhieu window ma countOdd[right] - countOdd[left] = k
    # Strategy: using prefsum = hashmap
    # map: # of odd numbers seen -> # of indices that has been associated with that # of odd numbers seen

    # nums: [2,2,1,2,2,1,2,2,1,2], k = 2, expected ans: 15
    # odd  0 0 0 1 1 1 2 2 2 3 3
    result, count_odd, num_odds_to_count = 0, 0, defaultdict(int)
    num_odds_to_count[0] = 1  # count subarrs from index 0 to i that has k odd nums

    for num in nums:
        count_odd += num % 2
        num_odds_to_count[count_odd] += 1
        result += num_odds_to_count[count_odd - k]

    return result
