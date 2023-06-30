class UnionFind:
	def __init__(self, n: int):
		self.group = [i for i in range(n)]
   
	def find(self, x: int) -> int:
		if self.group[x] != x:
			self.group[x] = self.find(self.group[x]) 

		return self.group[x]

	def union(self, x: int, y: int) -> None:
		x = self.find(x)
		y = self.find(y)

		if x < y:
			self.group[y] = x
		elif x > y:
			self.group[x] = y

	def are_connected(self, x: int, y: int) -> bool:
		return self.find(x) == self.find(y)
	 
	def one_group(self) -> bool:
		v = self.find(0)
		for g in self.group:
			if self.find(g) != v:
				return False
		return True
	 

class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:

        WATER = 1
        LAND = 0


        grid = [[1 for _ in range(col)] for _ in range(row)]

        in_bound = lambda i,j: (0<=j<col) and (0<=i<row)
        linear_index = lambda i,j: i*col + j + 1

        total_cells = row*col

        uf = UnionFind(total_cells + 2) # 1 start, 1 end

        for day in range(len(cells)-1, -1, -1):
            r, c = cells[day]
            r -= 1
            c -= 1

            grid[r][c] = LAND

            cur = linear_index(r,c)

            for x, y in [(r+1, c), (r-1, c), (r, c-1), (r, c+1)]:

                adj = linear_index(x,y)

                if in_bound(x,y) and grid[x][y] == LAND:
                    uf.union(cur, adj)
                   
                    
            if r == 0:
                uf.union(0, cur)

            if r == row-1:
                uf.union(cur, total_cells+1)

            # water between first and last cell, no way to bottom line
            if uf.are_connected(0, total_cells+1):
                return day # 0 indexed, -1 no needed

        return len(cells)
