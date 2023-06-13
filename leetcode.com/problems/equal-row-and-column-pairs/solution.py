class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:

        n = len(grid)
          
        q = []
        for i in range(n):
            for j in range(n):
                if grid[i][0] == grid[0][j]:
                    q.append((i,j))

        x = 1
        while x < n:
            l = len(q)

            for i in range(l):
                i, j = q[i]
                if grid[i][x] == grid[x][j]:
                    q.append((i,j))

            q = q[l:]
            x += 1

        return len(q)
