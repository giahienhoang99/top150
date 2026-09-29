def generateParenthesis(self, n: int) -> List[str]:
    """
    test1:
    n = 3
    [
        "((()))",
        "(()())",
        "(())()",
        "()(())",
        "()()()"
    ]
    n = 3 => len of str = 6
    has to start with an open paren (
                                   (
                    ()                            ((
            ()(                         (((                (()
        ()()    ()((                    ((()        (()(        (())
        ()()(   ()(()                   ((())       (()()       (())(
        ()()()  ()(())                  ((()))      (()())      (())()

    constraints:
    - number of open parens
    - cannot append close paren if cur state is completed

    idea:
    - can use an int to track the # open paren
    - cur = 0
        if append an open paren => +1
        if append a close paren => -1
    - cur can never be < 0 or > n
    - end condition: len(cur_comb) = n * 2 (and cur = 0)

    """
    results = []

    def backtrack(cur_comb, score):
        if score == 0 and len(cur_comb) == n * 2:
            results.append("".join(cur_comb))
            return

        if score >= 0 and score < n and len(cur_comb) < n * 2:
            cur_comb.append("(")
            backtrack(cur_comb, score + 1)
            cur_comb.pop()

        if score <= n and score > 0 and len(cur_comb) < n * 2:
            cur_comb.append(")")
            backtrack(cur_comb, score - 1)
            cur_comb.pop()

    backtrack([], 0)
    return results
