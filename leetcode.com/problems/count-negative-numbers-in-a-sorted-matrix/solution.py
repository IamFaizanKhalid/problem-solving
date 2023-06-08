class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        count = 0

        for r in range(m):
            c = 0
            while c < n:
                if grid[r][c] < 0:
                    count += (n-c)*(m-r)
                    n = c # reducing columns as next columns are negative
                    break
                c += 1

        return count
     
