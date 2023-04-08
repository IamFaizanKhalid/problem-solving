class Solution:
	def numEnclaves(self, grid: List[List[int]]) -> int:
		rows = len(grid)
		cols = len(grid[0])

		visited = [[False for _ in range(cols)] for _ in range(rows)]
		
		def explore(r, c):
			if r<0 or r>=rows or c<0 or c>=cols:
				return
			
			if visited[r][c] or grid[r][c]==0:
				return

			visited[r][c] = True

			explore(r,c-1)
			explore(r+1,c)
			explore(r,c+1)
			explore(r-1,c)
			
		for r in range(rows):
			explore(r, 0)
			explore(r, cols-1)
			
		for c in range(cols):
			explore(0, c)
			explore(rows-1, c)
			

		total = 0
		for r in range(1,rows-1):
			for c in range(1,cols-1):
				if grid[r][c]==1 and not visited[r][c]:
					total +=1

		return total
