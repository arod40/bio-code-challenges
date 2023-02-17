from collections import defaultdict

# linked list
class PathNode:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

    def insert_after(self, value):
        node = PathNode(value, self, self.next)
        if self.next is not None:
            self.next.prev = None
        self.next = node
        return node

    def collect_all(self):
        path = []
        current = self
        while current is not None:
            path.append(current.val)
            current = current.next
        return path


def eulerian_cycle(g):
    # Keep the cycle as a linked list so that we can
    # efficiently extend it in its middle with new sub-cycles.
    start = PathNode(list(g.keys())[0])

    # Store all the nodes that have been visited.
    # If the graph is eulerian, one of them must have outdegree != 0
    # and we can use it to continue the algorithm.
    visited_nodes = [start]

    # Whenever visited_nodes is empty, that means that every node
    # visited before has outdegree == 0, therefore, all edges have been covered.
    while visited_nodes:
        current = visited_nodes.pop()
        while g[current.val]:
            # neighbor is popped out the list.
            # this way a visited edge is removed from the graph altogether.
            neighbor = g[current.val].pop()
            current = current.insert_after(neighbor)
            visited_nodes.append(current)

    return start.collect_all()


if __name__ == "__main__":
    from pathlib import Path

    # I'm assuming there is a line per node in the range [0,V-1]
    lines = Path("dataset_873150_2.txt").read_text().split("\n")[:-1]
    g = defaultdict(list)

    for line in lines:
        v, neighbors_str = line.split(":")
        for w in neighbors_str.strip().split():
            g[v].append(w)
            if w not in g:
                g[w] = []
    print(" ".join(eulerian_cycle(g)))
