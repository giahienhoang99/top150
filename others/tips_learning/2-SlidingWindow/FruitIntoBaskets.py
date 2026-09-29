from collections import defaultdict
from typing import List

def totalFruit(self, fruits: List[int]) -> int:
    # Objective: find longest subarr that has exactly 2 distinct values
    l, maxlen = 0, 0
    fruitToCount = defaultdict(int)
    for r in range(len(fruits)):
        fruitToCount[fruits[r]] += 1
        # while > 2 fruit types, shorten and remove fruit until 2 left
        while len(fruitToCount) > 2 and l <= r:
            fruitToCount[fruits[l]] -= 1
            if fruitToCount[fruits[l]] == 0:
                fruitToCount.pop(fruits[l])
            l += 1
        # update maxlen
        maxlen = max(maxlen, r - l + 1)
    return maxlen
