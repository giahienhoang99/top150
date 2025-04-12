def letterCasePermutation(self, s: str) -> List[str]:
    """
    Input: s = "a1b2"
    Output: ["a1b2","a1B2","A1b2","A1B2"]
              0000   0010   1000   1010
              00     01     10     11

    note: there are non binary chars (the numeric chars)
    => cant be uppercase or lowercase but just the number
    => skip when met
    """
    res, c = [], []

    def backtrack(i):
        if i == len(s):
            res.append("".join(c))
            return

        if s[i].isalpha():
            c.append(s[i].lower())
            backtrack(i + 1)
            c.pop()

            c.append(s[i].upper())
            backtrack(i + 1)
            c.pop()
        else:
            c.append(s[i])
            backtrack(i + 1)
            c.pop()

    backtrack(0)
    return res
