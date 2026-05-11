class Solution:
    def countComponents(self, n, edges):

        # Build adjacency list
        graph = {i: [] for i in range(n)}

        for u, v in edges:

            # Undirected graph
            graph[u].append(v)
            graph[v].append(u)

        # Visited nodes
        visited = set()

        # Connected component count
        components = 0

        # DFS function
        def dfs(node):

            # Already visited
            if node in visited:
                return

            # Mark visited
            visited.add(node)

            # Explore neighbors
            for neighbor in graph[node]:
                dfs(neighbor)

        # Traverse all nodes
        for node in range(n):

            # New component found
            if node not in visited:

                components += 1

                # Visit entire component
                dfs(node)

        return components

if __name__ == "__main__":
    n = 5
    edges = [
        [0, 1],
        [1, 2],
        [3, 4] ]
    sol = Solution()
    result = sol.countComponents(n, edges)
    print("Number of Connected Components:", result)