from typing import List


def constructDistancedSequence(self, n: int) -> List[int]:
    """
    len_ans = 1 + 2(n - 1) = 2n - 1

    idea: backtracking to try all possible permutations

    notes:
        - lexicographically largest sequence
            => try numbers in range 1->n but in decreasing order (from n to 1)
        - check if 2 slots in candidate is filled already
        - have to check the boundary when inserting number
        - have to check which number is used each backtracking turn
        - case num = 1: 1 appears once only
    """
    len_ans = 2 * n - 1
    candidate = [0] * len_ans
    visited = set()
    largest = []

    def backtrack(i) -> bool:
        nonlocal largest
        # end condition: match len ans
        if i == len_ans:
            if largest == [] or candidate > largest:
                largest = list(candidate)  # update new largest sequence
            return True

        # if slot filled, continue til find new open slot or end
        if candidate[i] > 0:
            return backtrack(i + 1)

        for x in range(n, 0, -1):
            if x in visited:
                continue

            # if x = 1 then 1 only appears once
            if x == 1:
                candidate[i] = 1
                visited.add(1)

                if backtrack(i + 1):
                    return True

                visited.remove(1)
                candidate[i] = 0

            else:
                j = i + x
                if j >= len_ans:
                    continue
                if candidate[j] > 0:
                    continue

                candidate[i] = candidate[j] = x
                visited.add(x)

                if backtrack(i + 1):
                    return True

                visited.remove(x)
                candidate[i] = candidate[j] = 0
        return False

    backtrack(0)
    return largest
