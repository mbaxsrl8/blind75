# Tags: union-find, graph, needs-review
# You are given a connected undirected graph with n nodes labeled from 1 to n. Initially, it contained no cycles and consisted of n-1 edges.

# We have now added one additional edge to the graph. The edge has two different vertices chosen from 1 to n, and was not an edge that previously existed in the graph.

# The graph is represented as an array edges of length n where edges[i] = [ai, bi] represents an edge between nodes ai and bi in the graph.

# Return an edge that can be removed so that the graph is still a connected non-cyclical graph. If there are multiple answers, return the edge that appears last in the input edges.


class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        parent = list(range(len(edges) + 1))
        size = [1] * (len(edges) + 1)

        def findRoot(node: int) -> int:
            while parent[node] != node:
                node = parent[node]
            return node

        for u, v in edges:
            root_u = findRoot(u)
            root_v = findRoot(v)

            if root_u == root_v:
                return [u, v]

            if size[root_u] < size[root_v]:
                root_u, root_v = root_v, root_u

            parent[root_v] = root_u
            size[root_u] += size[root_v]


if __name__ == "__main__":
    sol = Solution()
    print(sol.findRedundantConnection(edges=[[1, 2], [1, 3], [3, 4], [2, 4]]))
