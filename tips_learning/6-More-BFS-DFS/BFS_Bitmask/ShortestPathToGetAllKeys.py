import collections


def shortestPathAllKeys(self, grid: List[str]) -> int:
    """
    - use bfs since we looking for shortest route
    - when meet a lock check if has corresponding key

    bfs w complicated states
    usually: (x,y) coords

    this prob:
    gotta remember keys state for each exploration/path
    => (x, y, keys)

    if use set to store  keys, we would have to copy set each time we branch out
    => not efficient for both time and space complexity
    => use bitmask to store keys state
    """
    DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    M, N = len(grid), len(grid[0])
    K = 0
    start_x, start_y = 0, 0
    # get start point and #keys
    for i in range(M):
        for j in range(N):
            if grid[i][j] == "@":
                start_x, start_y = i, j
            if "a" <= grid[i][j] <= "f":
                K += 1

    MAPPINGS = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5}
    DES = (1 << K) - 1
    q = collections.deque([(start_x, start_y, 0)])
    visited = set([(start_x, start_y, 0)])
    steps = 0
    while q:
        for _ in range(len(q)):
            x, y, keys = q.popleft()
            # print("current state: ", x, y, keys)
            
            # check if has all keys
            if keys == DES:
                return steps

            for dx, dy in DIRECTIONS:
                nx, ny, nkeys = x + dx, y + dy, keys
                # check in grid
                if not (0 <= nx < M and 0 <= ny < N):
                    continue
                # check if visited
                if (nx, ny, nkeys) in visited:
                    continue
                # check block
                if grid[nx][ny] == "#":
                    continue
                # if key => update bitmask
                if "a" <= grid[nx][ny] <= "f":
                    i = MAPPINGS[grid[nx][ny]]
                    nkeys |= 1 << i
                # check if has key for lock
                if "A" <= grid[nx][ny] <= "F":
                    # satisfy condition: x & (1 << i) > 0
                    i = MAPPINGS[grid[nx][ny].lower()]
                    if keys & (1 << i) == 0:
                        continue
                q.append((nx, ny, nkeys))
                visited.add((nx, ny, nkeys))
        steps += 1
    return -1
