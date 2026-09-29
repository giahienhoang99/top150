from collections import deque


def removeDuplicates(self, s: str, k: int) -> str:
    """
    use 2 stacks:
    - one for char
    - one for char's freq

    "deeedbbcccbdaa"
    """
    chars = deque()
    freq = deque()

    for c in s:
        if not chars:
            chars.append(c)
            freq.append(1)
        else:
            if c == chars[-1]:
                new_freq = (freq.pop() + 1) % k
                if new_freq != 0:
                    freq.append(new_freq)
                else:
                    chars.pop()
            else:
                chars.append(c)
                freq.append(1)

    res = [chars[i] * freq[i] for i in range(len(chars))]
    return "".join(res)
