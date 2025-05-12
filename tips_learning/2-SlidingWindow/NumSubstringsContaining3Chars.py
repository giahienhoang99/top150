from collections import defaultdict

def numberOfSubstrings(self, s: str) -> int:
    # dynamic sliding window
    # using hashmap to store frequency of abc
    # find first valid window
    # when found valid window:
    #       result += len(s) - i
    #       shift up left 1 and every time shorten window and cur window still valid
    #       => result += len(s) - 1
    result, freq, l = 0, defaultdict(int), 0
    for r in range(len(s)):
        freq[s[r]] += 1
        while len(freq) == 3 and l <= r:
            result += len(s) - r
            freq[s[l]] -= 1
            if freq[s[l]] == 0:
                del freq[s[l]]
            l += 1
    return result
