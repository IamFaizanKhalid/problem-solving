class Solution:
	def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
		paths = {}

		for edge in edges:
			if edge[0] in paths:
				paths[edge[0]].append(edge[1])
			else:
				paths[edge[0]]=[edge[1]]
			if edge[1] in paths:
				paths[edge[1]].append(edge[0])
			else:
				paths[edge[1]]=[edge[0]]

		def dfs(cur, parent, hasApple):
			total = 0

			for nxt in paths[cur]:
				if nxt == parent:
					continue

				count = dfs(nxt, cur, hasApple)
				total += count

				if count > 0 or hasApple[nxt]: # if child or subtree has an apple
					total += 2 # to the nxt and back

			return total

		return dfs(0, -1, hasApple);
