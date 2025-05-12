def mySqrt(self, x: int) -> int:
    l, r = 0, x
    while l <= r:
        mid = (l + r) // 2
        prod = mid * mid
        if prod == x:
            return mid
        elif prod > x:
            r = mid - 1
        else:
            l = mid + 1
    return r
