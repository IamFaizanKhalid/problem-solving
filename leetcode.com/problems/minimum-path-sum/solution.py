class Solution:
	def minPathSum(self, grid: List[List[int]]) -> int:

		m = len(grid)
		n = len(grid[0])

		for i in range(1,m):
			grid[i][0] += grid[i-1][0]

		for j in range(1,n):
			grid[0][j] += grid[0][j-1]

		for x in range(1, min(m,n)):
			grid[x][x] += min(grid[x][x-1], grid[x-1][x])

			for i in range(x+1,m):
				grid[i][x] += min(grid[i-1][x],grid[i][x-1])

			for j in range(x+1,n):
				grid[x][j] += min(grid[x-1][j], grid[x][j-1])


		return grid[m-1][n-1]
