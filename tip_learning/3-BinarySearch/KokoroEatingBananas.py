from typing import List
import math

def minEatingSpeed(self, piles: List[int], h: int) -> int:
    # binary search but not straightforward
    # gott define my own monotonic function
    def can_eat(k) -> bool:
        hours = h
        for num in piles:
            hours -= math.ceil(num / k)
        return hours >= 0

    # binary search
    l, r = 1, max(piles)
    min_k = r
    while l <= r:
        mid = (l + r) >> 1
        if can_eat(mid):
            r = mid - 1
            min_k = mid
        else:
            l = mid + 1
    return min_k
