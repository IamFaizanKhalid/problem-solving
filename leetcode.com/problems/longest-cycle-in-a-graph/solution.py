class Solution:
	def longestCycle(self, edges: List[int]) -> int:
		n = len(edges)

		visited = [False for _ in range(n)]

		def cycleLength(i, steps):
			visited[i] = True

			nxt = edges[i]
			if nxt == -1:
				return -1

			if nxt in steps:
				return steps[i] - steps[nxt] + 1

			if visited[nxt]: # visited but not in this turn
				return -1

			steps[nxt] = steps[i] + 1
			return cycleLength(nxt, steps)


		cl = -1

		for i in range(n):
			if not visited[i]:
				steps = {}
				steps[i] = 1

				cl = max(cl, cycleLength(i, steps))

		return cl
