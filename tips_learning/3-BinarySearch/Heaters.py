from typing import List

def findRadius(self, houses: List[int], heaters: List[int]) -> int:
    houses.sort()
    heaters.sort()

    # check if all houses covered when k is range of heaters
    def can_heat(k):
        i = j = 0
        while i < len(houses) and j < len(heaters):
            # if covered then check next house, else use next heater
            if abs(houses[i] - heaters[j]) <= k:
                i += 1
            else:
                j += 1
        return i == len(houses)

    # max of heat range k = max dist. tween a house and a heater
    l, r = 0, max(max(houses) - min(heaters), max(heaters) - min(houses))
    min_k = r
    while l <= r:
        mid = (l + r) // 2
        if can_heat(mid):
            r = mid - 1
            min_k = mid
        else:
            l = mid + 1
    return min_k