"""
******** TIME & SPACE COMPLEXITY ********

addEdge:
- Time: O(1)
- Space: O(1) per edge added

removeEdge:
- Time: O(1)
- Space: O(1)

hasPath (DFS/BFS):
- Time: O(V + E) where V = vertices, E = edges
- Space: O(V) for visited set or queue

*****************************************
"""

# Graph Implementation using Adjacency List
class Graph:
    def __init__(self):
        self.adj_list = {}

    def addEdge(self, src: int, dst: int) -> None:
        # If src or dst don't exist, add them
        if src not in self.adj_list:
            self.adj_list[src] = set()
        if dst not in self.adj_list:
            self.adj_list[dst] = set()
        # Add edge if not already exists
        self.adj_list[src].add(dst)

    def removeEdge(self, src: int, dst: int) -> bool:
        # Check if src and dst exist in the graph
        if src not in self.adj_list or dst not in self.adj_list[src]:
            return False
        # Remove the edge
        self.adj_list[src].remove(dst)
        return True

    def hasPath(self, src: int, dst: int) -> bool:
        visited = set()
        return self._dfs(src, dst, visited)

    def _dfs(self, src: int, dst: int, visited: set) -> bool:
        if src == dst:
            return True
        visited.add(src)
        for neighbor in self.adj_list.get(src, []):
            if neighbor not in visited:
                if self._dfs(neighbor, dst, visited):
                    return True
        return False

    # Alternatively, use BFS for hasPath
    #
