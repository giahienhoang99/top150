from typing import List


MAPPINGS = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz",
}

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
        234
        2: abc
        3: def
        4: ghi

        a d g
        a d h
        a d i
        a e g
        a e h
        a e i
        ...

        backtracking
        stop condition: len(cur_list) == len(digits)
        """
        result = []
        candidate = []

        if digits == "":
            return result

        def backtrack(i):
            if i == len(digits):
                result.append("".join(candidate))
                return

            for char in MAPPINGS[digits[i]]:
                candidate.append(char)
                backtrack(i + 1)
                candidate.pop()

        backtrack(0)
        return result