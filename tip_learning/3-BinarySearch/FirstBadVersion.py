def firstBadVersion(self, n: int) -> int:
    l, r = 0, n
    ans = 0
    while l <= r:
        mid = (r + l) >> 1  # bitwise op
        if isBadVersion(mid):
            r = mid - 1
            ans = mid
        else:
            l = mid + 1
    return ans
