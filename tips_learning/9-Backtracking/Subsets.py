from typing import List


def subsets(self, nums: List[int]) -> List[List[int]]:
    """
    def backtrack(i):
        if <stop condition>:
            <record result of the decisions>
            return

        for <decision x> for <set of decisions at state i>:
            <make decision>
            backtrack(i+1)
            <revert decision>
    """
    N = len(nums)
    result = []
    cur_subset = []

    def backtrack(i):
        if i == N:
            result.append(list(cur_subset))
            return

        # make decision 1: include element
        cur_subset.append(nums[i])
        backtrack(i + 1)
        cur_subset.pop()

        # make decision 2: dont include element
        backtrack(i + 1)

    backtrack(0)
    return result
