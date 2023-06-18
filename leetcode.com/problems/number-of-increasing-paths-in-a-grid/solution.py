class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        modulo = lambda x: x%1000000007
        m = len(grid)
        n = len(grid[0])

        in_range = lambda i,j: (0 <= i < m) and (0 <= j < n)
        
        directions = [(-1,0),(1,0),(0,-1),(0,1)]

        @cache
        def paths(i,j):
            count = 1

            for x,y in directions:
                ix,jy = i+x,j+y
                if in_range(ix,jy) and grid[ix][jy]>grid[i][j]:
                    count = modulo(count + paths(ix,jy))

            return count


        total = 0

        for i in range(m):
            for j in range(n):
                total = modulo(total + paths(i,j))

        return total
