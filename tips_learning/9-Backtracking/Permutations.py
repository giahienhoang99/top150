from typing import List


def permute(self, nums: List[int]) -> List[List[int]]:
    """
    def backtrack(i):
        if <stop condition>:
            <record result of the decisions>
            return

        for <decision x> in <set of decisions at state i>:
            <make decision>
            backtrack(i+1)
            <revert decision>
    """
    N = len(nums)
    result = []
    used = [False] * N

    def backtrack(cur_perm, used):
        if len(cur_perm) == N:
            result.append(list(cur_perm))
            return

        for i, num in enumerate(nums):
            if not used[i]:
                cur_perm.append(num)
                used[i] = True
                backtrack(cur_perm, used)
                cur_perm.pop()
                used[i] = False

    backtrack([], used)
    return result
