from collections import defaultdict, deque
from typing import List


def numBusesToDestination(
    self, routes: List[List[int]], source: int, target: int
) -> int:
    """
    IDEA: bfs with each level being the bus instead of stops

    test 1:
    routes = [[1,2,7],[3,6,7]], source = 1, target = 6

    => use a defaultdict(set)
    stop_to_buses = {
        1: 0
        2: 0
        7: 0, 1
        3: 1
        6: 1
    }
    """
    if source == target:
        return 0

    stop_to_buses = defaultdict(list)  # stop -> list of buses
    for i, route in enumerate(routes):
        for stop in route:
            stop_to_buses[stop].append(i)

    q = deque()
    visited_buses = set()

    # append all possible buses from starting stop
    for bus in stop_to_buses[source]:
        q.append(bus)
        visited_buses.add(bus)

    num_bus = 1
    while q:
        for _ in range(len(q)):
            bus = q.popleft()

            for stop in routes[bus]:
                if stop == target:
                    return num_bus
                for bus in stop_to_buses[stop]:
                    if bus not in visited_buses:
                        q.append(bus)
                        visited_buses.add(bus)
        num_bus += 1

    return -1
