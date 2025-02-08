from typing import List
from collections import defaultdict

def maximumSubarraySum(self, nums: List[int], k: int) -> int:
    # Obj: maxsum of a good subarr
    #     |num - target| = k
    #      num - target  = k or -k
    # map: num -> min prefsum of that num
    #      => so curpref - that prefsum = max
    max_sum, cur_sum, num_to_min_prefsum = (
        -float("inf"),
        0,
        defaultdict(lambda: float("inf")),
    )
    for num in nums:
        cur_sum += num
        num_to_min_prefsum[num] = min(num_to_min_prefsum[num], cur_sum)
        if (num + k) in num_to_min_prefsum:
            max_sum = max(max_sum, cur_sum - num_to_min_prefsum[num + k] + num + k)
        if (num - k) in num_to_min_prefsum:
            max_sum = max(max_sum, cur_sum - num_to_min_prefsum[num - k] + num - k)
    return max_sum if max_sum != -float("inf") else 0
