class Solution:
    def pacificAtlantic(self, heights):

        rows = len(heights)
        cols = len(heights[0])

        # Reachable cells
        pacific = set()
        atlantic = set()

        # 4 directions
        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1) ]

        # DFS function
        def dfs(r, c, visited):
            visited.add((r, c))

            # Explore neighbors
            for dr, dc in directions:

                nr = r + dr
                nc = c + dc

                # Valid upward flow
                if (
                    0 <= nr < rows and
                    0 <= nc < cols and
                    (nr, nc) not in visited and
                    heights[nr][nc] >= heights[r][c] ):

                    dfs(nr, nc, visited)

        # Pacific Ocean DFS
        # Left border
        for r in range(rows):
            dfs(r, 0, pacific)

        # Top border
        for c in range(cols):
            dfs(0, c, pacific)

        # Atlantic Ocean DFS
        # Right border
        for r in range(rows):
            dfs(r, cols - 1, atlantic)

        # Bottom border
        for c in range(cols):
            dfs(rows - 1, c, atlantic)

        result = []

        # Cells reachable from both oceans
        for r in range(rows):
            for c in range(cols):

                if (
                    (r, c) in pacific and
                    (r, c) in atlantic ):

                    result.append([r, c])

        return result

if __name__ == "__main__":
    heights = [
        [1,2,2,3,5],
        [3,2,3,4,4],
        [2,4,5,3,1],
        [6,7,1,4,5],
        [5,1,1,2,4] ]
    sol = Solution()
    result = sol.pacificAtlantic(heights)
    print("Cells reaching both oceans:")
    for cell in result:
        print(cell)