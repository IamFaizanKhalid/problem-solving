class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)

        visited = [[False for _ in range(n)] for _ in range(n)]

        def in_grid(i,j):
            return i>=0 and i<n and j>=0 and j<n

        def is_not_land(i,j):
            return not in_grid(i,j) or grid[i][j] == 0
            
        def is_border(i,j):
            return grid[i][j] == 1 and (is_not_land(i-1,j) or is_not_land(i+1,j) or is_not_land(i,j-1) or is_not_land(i,j+1))
            

        def get_borders(i,j):
            if not in_grid(i,j):
                return []

            if grid[i][j] == 0 or visited[i][j]:
                return []

            visited[i][j] = True

            ans = []
            if is_border(i,j):
                ans = [(i,j)]

            return ans + get_borders(i-1,j) + get_borders(i+1,j) + get_borders(i,j-1) + get_borders(i,j+1)



        borders = []
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1 and not visited[i][j]:
                    borders.append(get_borders(i,j))

        # print(borders)

        
        def calc_dist(i1,j1, i2,j2):
            return abs(i2-i1)+abs(j2-j1)

        mn = float('inf')
        for p1 in borders[0]:
            for p2 in borders[1]:
                mn = min(mn, calc_dist(*p1,*p2))

        return mn-1 # if mn != float('inf') else -1
