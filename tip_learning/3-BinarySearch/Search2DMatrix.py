from typing import List

def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    # find row the target could be in
    m, n = len(matrix), len(matrix[0])
    l, r = 0, m - 1
    row_to_explore = 0
    while l <= r:
        mid = (l + r) // 2
        if target >= matrix[mid][0] and target <= matrix[mid][n - 1]:
            row_to_explore = mid
            break
        elif target < matrix[mid][0]:
            r = mid - 1
        elif target > matrix[mid][n - 1]:
            l = mid + 1

    # binary search on found row
    l, r = 0, n - 1
    while l <= r:
        mid = (l + r) // 2
        num = matrix[row_to_explore][mid]
        if num == target:
            return True
        elif num > target:
            r = mid - 1
        else:
            l = mid + 1
    return False
