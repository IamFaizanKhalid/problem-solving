class Solution:
	def closedIsland(self, grid: List[List[int]]) -> int:
		rows = len(grid)
		cols = len(grid[0])

		visited = [[False for _ in range(cols)] for _ in range(rows)]
		
		def explore(r, c):
			if r<0 or r>=rows or c<0 or c>=cols:
				return False
			
			if visited[r][c]:
				return True
			visited[r][c] = True

			if grid[r][c]==1:
				return True

			closed = True

			closed &= explore(r,c-1)
			closed &= explore(r+1,c)
			closed &= explore(r,c+1)
			closed &= explore(r-1,c)

			return closed
			

		total = 0
		for r in range(rows):
			for c in range(cols):
				if not visited[r][c] and grid[r][c]==0:
					if explore(r,c):
						total +=1

		return total
