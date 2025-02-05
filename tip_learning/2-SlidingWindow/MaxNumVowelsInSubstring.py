def maxVowels(self, s: str, k: int) -> int:
    res, count = 0, 0
    for i in range(k):
        count += s[i] in "aeiou"
    res = max(res, count)
    for i in range(k, len(s)):
        count += (s[i] in "aeiou") - (s[i - k] in "aeiou")
        res = max(res, count)
    return res
