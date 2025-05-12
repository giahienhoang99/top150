from typing import List

def maxDistance(self, position: List[int], m: int) -> int:
    # 1 2 3 4 7
    # distance: 1 ... 7-1
    # l = 1, r = 6
    # check if each distance (aka force) is good to fit m in buckets
    # if good, raise the distance by l = mid + 1
    # else, decrease the distance by r = mid - 1

    def can_fit(dist: int) -> bool:
        start = -inf
        count = 0
        for pos in position:
            if pos - start >= dist:
                count += 1
                start = pos
        return count >= m

    position.sort()
    max_dist, l, r = 1, 1, position[-1] - position[0]
    while l <= r:
        mid = (l + r) // 2
        if can_fit(mid):
            max_dist = max(mid, max_dist)
            l = mid + 1
        else:
            r = mid - 1
    return max_dist
