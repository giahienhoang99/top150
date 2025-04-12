from itertools import permutations


def largestTimeFromDigits(self, arr: List[int]) -> str:
    """
    arr = [1,2,3,4]

    h 12
    h 123
    m 1234
    m 1234
    """
    ans = ""

    for perm in permutations(arr):
        # print(perm)
        hour = perm[0] * 10 + perm[1]
        mins = perm[2] * 10 + perm[3]

        if not 0 <= hour <= 23:
            continue
        if not 0 <= mins <= 59:
            continue

        s = ":".join([str(hour).zfill(2), str(mins).zfill(2)])
        ans = max(ans, s)

    return ans
