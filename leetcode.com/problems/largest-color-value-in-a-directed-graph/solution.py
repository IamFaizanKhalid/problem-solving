class Solution:
	def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
		INF = float('inf')
		cN = lambda c:ord(c)-97

		n = len(colors)

		paths = defaultdict(list)
		incoming = [0 for _ in range(n)]

		for a,b in edges:
			paths[a].append(b)
			incoming[b]+=1


		visited = [False for _ in range(n)]
		curPath = [False for _ in range(n)]
		dp = [[0 for _ in range(26)] for _ in range(n)]
		
		def recurse(x):
			if curPath[x]:
				return INF

			col = cN(colors[x])

			if not visited[x]:
				visited[x] = True

				curPath[x] = True
				for adj in paths[x]:
					if recurse(adj) == INF:
						return INF

					for c in range(26):
						dp[x][c] = max(dp[x][c], dp[adj][c])

				dp[x][col] += 1
				curPath[x] = False

			return dp[x][col]



		answer = 0
		for i in range(n):
			answer = max(answer, recurse(i))


		if answer==INF:
			return -1

		return answer
