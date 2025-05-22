from collections import deque


class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        """
        use 2 stacks:
        - one for char
        - one for char's freq

        "deeedbbcccbdaa"
        """
        chars = deque([""])
        freq = deque([1])
        
        for c in s:
            if c == chars[-1]:
                freq[-1] += 1
                if freq[-1] == k:
                    freq.pop()
                    chars.pop()
            else:
                chars.append(c)
                freq.append(1)
        
        res = [c * f for c, f in zip(chars, freq)]
        return "".join(res)



