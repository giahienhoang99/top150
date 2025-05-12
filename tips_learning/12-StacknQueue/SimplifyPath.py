from collections import deque


def simplifyPath(self, path: str) -> str:
    stack = deque()
    splitted = path.split("/")

    for cur in splitted:
        if cur == "" or cur == ".":
            continue
        if cur == "..":
            if len(stack) > 0:
                stack.pop()
        else:
            stack.append(cur)

    return "/" + "/".join(list(stack))
