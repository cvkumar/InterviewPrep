import sys

def nightRoute(city):
    """
    Algorithms:

    1) Dijkstra

    Mark distance from 0th island to all others as -1
    Mark distance from 0th to 0th island as 0

    Put 0th island it on Priority Q

    Until Q empty
        Grab island from Q

        For each edge:
            if bridge available and dist[source] + dist[dest with new edfe] < dist[current to dest]
            then update
            Add island to Priority Q

    Grab next element from Heap Queue

    """
    li = set([])
    visited = {}
    dist = [-1] * len(city)

    for i in range(len(city)):
        if i == 0:
            dist[i] = 0
        else:
            dist[i] = -1
        visited[i] = False

    li.add(0)

    # li = (0), visited = (0: False ...), dist = [0, -1, ...]

    while len(li) > 0:

        # Grab unvisited island that has shortest distance to it
        m = [-1, sys.maxint]
        for island in li:
            if dist[island] != -1 and dist[island] < m[1] and not visited[island]:
                m = [island, dist[island]]

        island = m[0]
        dist_to_island = m[1]
        li.remove(island)
        visited[island] = True

        # Update our distances
        for j in range(len(city)):
            if city[island][j] != -1:
                alt = city[island][j] + dist_to_island
                if alt < dist[j] or dist[j] == -1:
                    dist[j] = alt

                if not visited[j]:
                    li.add(j)

    return dist[len(city) - 1]



city = [[-1, 5, 20],
        [21, -1, 10],
        [-1, 1, -1]]

print(nightRoute(city))
