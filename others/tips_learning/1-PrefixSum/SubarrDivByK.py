from collections import List


def subarraysDivByK(self, nums: List[int], k: int) -> int:
    mod = [0] * k
    mod[0] = 1

    prefix_sum = 0
    ret = 0
    for x in nums:
        prefix_sum += x
        ret += mod[prefix_sum % k]
        mod[prefix_sum % k] += 1

    return ret
