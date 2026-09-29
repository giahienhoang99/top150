from collections import namedtuple
import heapq


class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        """
        int t: time
        min heap: to track tasks with min processing time (use a tuple)

        idea:
        - seems like enqueue time is increasing (should be increasing, logically)
            => not mentioned in description if sorted
            => need to sort

        - init time = first job's enqueue time
            => update t by adding processing time of each chosen task

        - at a time t, there can be many jobs
            => for each time, have to add all available tasks to heap
            => (processing time, index)
            => pop all nodes in heap to add index to the result list

        - after all tasks in tasks have been added to min heap
            => just pop out the heap and add the rest indexes in result list
        """
        pq = []
        n = len(tasks)
        result = []

        Task = namedtuple("Task", ["enqueue_time", "process_time", "index"])

        sorted_tasks = []
        for i, (e, p) in enumerate(tasks):
            sorted_tasks.append(Task(e, p, i))
        sorted_tasks.sort()

        i = 0
        t = sorted_tasks[0][0]
        while len(tasks) != len(result):
            # add all available tasks at t to queue
            while i < n and sorted_tasks[i].enqueue_time <= t:
                task = sorted_tasks[i]
                heapq.heappush(pq, (task.process_time, task.index))
                i += 1

            if pq:
                # process the one with shortest processing time
                time, index = heapq.heappop(pq)

                t += time
                result.append(index)
            else:
                t = sorted_tasks[i].enqueue_time

        return result
