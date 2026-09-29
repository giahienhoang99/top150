from typing import List

def maxProfitAssignment(
    self, difficulty: List[int], profit: List[int], worker: List[int]
) -> int:
    # list of jobs: each job = a list where list[0] = diff, list[1] = profit
    job_list = [[difficulty[i], profit[i]] for i in range(len(difficulty))]
    # sort job_list by difficulty
    job_list = sorted(job_list)
    # update profit of each difficulty to max profit seen from first up to that difficulty
    for i in range(1, len(job_list)):
        job_list[i][1] = max(job_list[i][1], job_list[i - 1][1])
    # find index of the most difficult job the current worker can finish using binary search
    max_profit = 0
    for w in worker:
        max_profit_for_worker = 0  # max profit current worker can get
        l, r = 0, len(job_list) - 1
        while l <= r:
            mid = (l + r) // 2
            if w >= job_list[mid][0]:
                max_profit_for_worker = job_list[mid][1]
                l = mid + 1
            elif w < job_list[mid][0]:
                r = mid - 1
        max_profit += max_profit_for_worker

    return max_profit
