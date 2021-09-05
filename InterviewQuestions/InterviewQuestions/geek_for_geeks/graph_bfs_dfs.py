from collections import defaultdict


# This class represents a directed graph
# using adjacency list representation
class Graph:

    # Constructor
    def __init__(self):
        # default dictionary to store graph
        self.graph = defaultdict(list)

    # function to add an edge to graph
    def add_edge(self, u, v):
        self.graph[u].append(v)

    def do_bfs(self, start_node: int):
        """
        BFS algorithm:

        create queue

        curr_node = first node

        add curr node to visited

        add all of curr nodes neighbors to Queue

        pop off node that node then do the same for next node

        Do this until all nodes have been visited

        Runtime complexity: O(|V| + |E|)
        where E ~ number of edges on entire graph

        At first I thought runtime was |V| * |E|. However we only touch each
        edge of the graph once during the algorithm so its not.

        """
        queue = []
        visited = set()
        curr_node = start_node

        print('top')
        while queue or curr_node == start_node:
            if curr_node in visited:
                continue

            visited.add(curr_node)

            print(curr_node)

            neighbors = self.graph[curr_node]

            for neighbor in neighbors:
                queue.append(neighbor)

            curr_node = queue.pop(0)


if __name__ == "__main__":
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)

    print("Following is Breadth First Traversal"
          " (starting from vertex 2)")
    g.do_bfs(2)
