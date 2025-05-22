class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        """
        idea: Monotonic stack
        for add stack
            while stack & stack top > cur & k > 0
                => pop stack top
                => k--
            
            1 more edge case to figure out
            => remove tu top
        """
        stack = []
        for digit in num:
            while k and stack and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)

        if k > 0:
            stack = stack[:-k]

        return "".join(stack).lstrip("0") or "0"

        


                