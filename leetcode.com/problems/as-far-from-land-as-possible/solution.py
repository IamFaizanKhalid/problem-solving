class Solution:
	def maxDistance(self, grid: List[List[int]]) -> int:
		n = len(grid)

		dist = [[float('inf') for _ in range(n)] for _ in range(n)]

		for i in range(n):
			for j in range(n):
				if grid[i][j] == 1:
					dist[i][j] = 0
				else:
					di = float('inf')
					if i > 0:
						di = dist[i - 1][j] + 1
					dj = float('inf')
					if j > 0:
						dj = dist[i][j - 1] + 1

					dist[i][j] = min(dist[i][j], min(di, dj))


		ans = float('-inf')

		for i in range(n-1, -1, -1):
			for j in range(n-1, -1, -1):
				di = float('inf')
				if i < n - 1:
					di = dist[i + 1][j] + 1
				dj = float('inf')
				if j < n - 1:
					dj = dist[i][j + 1] + 1

				dist[i][j] = min(dist[i][j], min(di, dj))
				
				ans = max(ans, dist[i][j])

				
		return -1 if ans == 0 or ans == float('inf') else ans

