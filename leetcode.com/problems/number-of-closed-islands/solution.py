class Solution:
	def closedIsland(self, grid: List[List[int]]) -> int:
		rows = len(grid)
		cols = len(grid[0])

		visited = [[False for _ in range(cols)] for _ in range(rows)]
		
		def explore(r, c):
			print(r,c)
			if r<0 or r>=rows or c<0 or c>=cols:
				return False
			
			if visited[r][c]:
				return True

			visited[r][c] = True
			
			if grid[r][c]==1:
				return True
			
			return explore(r-1,c) and explore(r+1,c) and explore(r,c-1) and explore(r,c+1)


		total = 0
		for r in range(rows):
			for c in range(cols):
				if not visited[r][c] and grid[r][c]==0:
					if explore(r,c):
						total +=1

		return total
