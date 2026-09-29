def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
    """
    candidates: 2 3 5
    target = 8
    2 2 2 2
    2 2 2 3
    2 2 2 5
    2 2 3 3
    2 2 3 5
    2 3 3
    2 3 5
    2 5 5
    3 3 3
    3 3 5
    3 5
    5 5

    - use backtracking to explore all combinations
    - sort candidates to explore all combinations of multiple smaller nums first
    - can add numbers as long as sum of cur list < target

    => have to pass the following values to backtrack():
        - cur_list: list containing cur combination
        - cur_sum: sum of cur combination
        - start_index: index to start adding value in sorted candidate list
    """
    candidates.sort()
    result = []

    def backtrack(cur_list, cur_sum, start_index):
        if cur_sum == target:
            result.append(list(cur_list))
            return

        if cur_sum > target:
            return

        for i in range(start_index, len(candidates)):
            num = candidates[i]

            cur_list.append(num)
            backtrack(cur_list, cur_sum + num, i)
            cur_list.pop()

    backtrack([], 0, 0)
    return result
