from collections import Counter, defaultdict, List


def findAnagrams(self, s: str, p: str) -> List[int]:
    k = len(p)
    freq_p = defaultdict(int, Counter(p))
    freq_s = defaultdict(int, Counter(s[:k]))
    ans = []
    if freq_s == freq_p:
        ans.append(0)
    for i in range(k, len(s)):
        freq_s[s[i - k]] -= 1
        freq_s[s[i]] += 1
        if freq_s[s[i - k]] == 0:
            del freq_s[s[i - k]]
        if freq_s == freq_p:
            ans.append(i - k + 1)

    return ans
