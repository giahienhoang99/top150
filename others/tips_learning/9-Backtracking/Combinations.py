def combine(self, n: int, k: int) -> List[List[int]]:
    """
    test1:
    if 1 is used first time as locked val, it wont be used no more
    12 13 14
    23 24
    34

    my test:
    k = 3, n = 4
    1
      2
        3
        4 -> 2
      3
        4 -> 1
      4
        x -> 0

    2
      3
        4 -> 1
      4
        x -> 0
    => total combs = 2 + 1 + 1 = 4
    """
    combinations = []
    used = [False] * (n + 1)

    def backtrack(cur_comb, start):
        # condition met: len of cur_comb = k
        if len(cur_comb) == k:
            combinations.append(list(cur_comb))
            return

        for num in range(start, n + 1):
            if used[num]:
                continue
            cur_comb.append(num)
            used[num] = True

            backtrack(cur_comb, num)

            cur_comb.pop()
            used[num] = False

    backtrack([], 1)
    return combinations
